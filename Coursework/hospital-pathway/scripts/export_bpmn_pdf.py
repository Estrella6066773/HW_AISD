"""Render the checked-in BPMN DI coordinates to a vector PDF with readable tiles."""

from __future__ import annotations

import hashlib
import math
import textwrap
from pathlib import Path

from lxml import etree
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


MODULE = Path(__file__).resolve().parents[1]
REPO = MODULE.parents[1]
SOURCE = MODULE / "bpmn" / "W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn"
OUTPUT = REPO / "submissions" / "AISD" / "Hospital_All_Processes_Camunda8_Export_2026-09-29.pdf"
NS = {
    "bpmn": "http://www.omg.org/spec/BPMN/20100524/MODEL",
    "bpmndi": "http://www.omg.org/spec/BPMN/20100524/DI",
    "dc": "http://www.omg.org/spec/DD/20100524/DC",
    "di": "http://www.omg.org/spec/DD/20100524/DI",
    "bioc": "http://bpmn.io/schema/bpmn/biocolor/1.0",
}
pdfmetrics.registerFont(TTFont("YaHei", r"C:\Windows\Fonts\msyh.ttc", subfontIndex=0))
pdfmetrics.registerFont(TTFont("YaHeiBold", r"C:\Windows\Fonts\msyhbd.ttc", subfontIndex=0))
TREE = etree.parse(str(SOURCE))
BY_ID = {e.get("id"): e for e in TREE.xpath("//*[@id]")}
SHAPES = TREE.xpath("//bpmndi:BPMNShape", namespaces=NS)
EDGES = TREE.xpath("//bpmndi:BPMNEdge", namespaces=NS)
DEFAULT_FLOW_IDS = {e.get("default") for e in TREE.xpath("//*[@default]")}
HASH = hashlib.sha256(SOURCE.read_bytes()).hexdigest()[:12]


def tag(node):
    return etree.QName(node).localname


def color(value, fallback="#454F58"):
    try:
        return colors.HexColor(value or fallback)
    except ValueError:
        return colors.HexColor(fallback)


def bounds(node):
    b = node.find("dc:Bounds", namespaces=NS)
    return tuple(float(b.get(key)) for key in ("x", "y", "width", "height"))


def label_bounds(node):
    b = node.find("bpmndi:BPMNLabel/dc:Bounds", namespaces=NS)
    return None if b is None else tuple(float(b.get(key)) for key in ("x", "y", "width", "height"))


class View:
    def __init__(self, canvas_, x, y, width, height, scale, ox, oy):
        self.c = canvas_
        self.x, self.y, self.width, self.height = x, y, width, height
        self.scale, self.ox, self.oy = scale, ox, oy

    def px(self, x):
        return self.ox + (x - self.x) * self.scale

    def py(self, y):
        return self.oy + (self.height - (y - self.y)) * self.scale

    def point(self, x, y):
        return self.px(x), self.py(y)

    def line(self, x1, y1, x2, y2):
        self.c.line(self.px(x1), self.py(y1), self.px(x2), self.py(y2))

    def rect(self, x, y, w, h, *, rounded=0, fill=0):
        left, bottom = self.px(x), self.py(y + h)
        w, h = w * self.scale, h * self.scale
        if rounded:
            self.c.roundRect(left, bottom, w, h, rounded * self.scale, stroke=1, fill=fill)
        else:
            self.c.rect(left, bottom, w, h, stroke=1, fill=fill)

    def circle(self, x, y, radius, fill=0):
        self.c.circle(self.px(x), self.py(y), radius * self.scale, stroke=1, fill=fill)


def wrapped_lines(raw, max_width, font, size, max_lines=8):
    words = raw.split()
    if not words:
        return [""]
    lines, current = [], words[0]
    for word in words[1:]:
        attempt = current + " " + word
        if pdfmetrics.stringWidth(attempt, font, size) <= max_width:
            current = attempt
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return lines[:max_lines]


def draw_text(view, name, x, y, w, h, *, size=12, align="center", bold=False, color_value="#253547", max_lines=9):
    if not name:
        return
    c = view.c
    font = "YaHeiBold" if bold else "YaHei"
    fsize = size * view.scale
    available = max(10, w * view.scale - 12 * view.scale)
    lines = []
    for part in name.replace("\r", "").split("\n"):
        lines.extend(wrapped_lines(part, available, font, fsize, max_lines))
    lines = lines[:max_lines]
    line_h = fsize * 1.27
    needed = len(lines) * line_h
    if needed > h * view.scale and h > 0:
        ratio = max(0.66, h * view.scale / needed)
        fsize *= ratio
        line_h *= ratio
    c.setFillColor(color(color_value))
    c.setFont(font, fsize)
    top = view.py(y) - (h * view.scale - len(lines) * line_h) / 2 - fsize
    for i, line in enumerate(lines):
        py = top - i * line_h
        if align == "left":
            c.drawString(view.px(x) + 5 * view.scale, py, line)
        else:
            c.drawCentredString(view.px(x + w / 2), py, line)


def arrow(view, a, b, *, fill=True, stroke="#454F58"):
    dx, dy = b[0] - a[0], b[1] - a[1]
    length = math.hypot(dx, dy)
    if length == 0:
        return
    ux, uy = dx / length, dy / length
    tipx, tipy = view.point(*b)
    scale = view.scale
    back = (tipx - ux * 9 * scale, tipy + uy * 9 * scale)
    side = (-uy * 4.1 * scale, -ux * 4.1 * scale)
    p = view.c.beginPath()
    p.moveTo(tipx, tipy)
    p.lineTo(back[0] + side[0], back[1] + side[1])
    p.lineTo(back[0] - side[0], back[1] - side[1])
    p.close()
    view.c.setStrokeColor(color(stroke))
    view.c.setFillColor(color(stroke) if fill else colors.white)
    view.c.drawPath(p, stroke=1, fill=int(fill))


def draw_edge(view, node):
    element = BY_ID.get(node.get("bpmnElement"))
    if element is None:
        return
    points = [(float(w.get("x")), float(w.get("y"))) for w in node.findall("di:waypoint", namespaces=NS)]
    if len(points) < 2:
        return
    c = view.c
    etype = tag(element)
    stroke = node.get("{%s}stroke" % NS["bioc"], "#667585")
    c.setStrokeColor(color(stroke))
    c.setLineWidth((2.2 if etype == "sequenceFlow" else 1.6) * view.scale)
    c.setDash(()) if etype == "sequenceFlow" else c.setDash(6 * view.scale, 5 * view.scale)
    path = c.beginPath()
    path.moveTo(*view.point(*points[0]))
    for xy in points[1:]:
        path.lineTo(*view.point(*xy))
    c.drawPath(path)
    c.setDash(())
    arrow(view, points[-2], points[-1], fill=etype == "sequenceFlow", stroke=stroke)
    if etype == "messageFlow":
        view.circle(*points[0], 4, fill=0)
    if node.get("bpmnElement") in DEFAULT_FLOW_IDS:
        a, b = points[:2]
        dx, dy = b[0] - a[0], b[1] - a[1]
        length = math.hypot(dx, dy)
        if length > 0:
            nx, ny = -dy / length, dx / length
            cx, cy = a[0] + dx / length * 8, a[1] + dy / length * 8
            view.line(cx - 4 * nx, cy - 4 * ny, cx + 4 * nx, cy + 4 * ny)
    name = element.get("name", "")
    lb = label_bounds(node)
    if name and lb:
        draw_text(view, name, *lb, size=9.5, color_value=stroke, max_lines=3)


def draw_icon(view, kind, x, y):
    c = view.c
    c.setStrokeColor(color("#455767"))
    c.setLineWidth(1.4 * view.scale)
    if kind == "userTask":
        view.circle(x + 12, y + 12, 4)
        view.rect(x + 5, y + 17, 14, 10, rounded=2)
    elif kind == "serviceTask":
        view.circle(x + 12, y + 16, 6)
        for angle in range(0, 360, 60):
            r = math.radians(angle)
            view.line(x + 12 + 6 * math.cos(r), y + 16 + 6 * math.sin(r),
                      x + 12 + 10 * math.cos(r), y + 16 + 10 * math.sin(r))
    elif kind == "sendTask":
        view.rect(x + 4, y + 9, 18, 13)
        view.line(x + 4, y + 9, x + 13, y + 16)
        view.line(x + 22, y + 9, x + 13, y + 16)


def draw_shape(view, node):
    element = BY_ID.get(node.get("bpmnElement"))
    if element is None:
        return
    x, y, w, h = bounds(node)
    typ = tag(element)
    c = view.c
    stroke = node.get("{%s}stroke" % NS["bioc"], "#434C55")
    fill = node.get("{%s}fill" % NS["bioc"], "#FFFFFF")
    c.setStrokeColor(color(stroke))
    c.setFillColor(color(fill, "#FFFFFF"))
    c.setLineWidth((2.6 if typ in {"userTask", "serviceTask", "sendTask"} else 1.9) * view.scale)
    name = element.get("name", "")
    lb = label_bounds(node)
    if typ in {"participant", "lane"}:
        view.rect(x, y, w, h)
        if name:
            if w > 500 and h < 70:
                draw_text(view, name, x, y, w, h, size=11, bold=True)
            else:
                c.saveState()
                cx, cy = view.point(x + min(22, w / 2), y + h / 2)
                c.translate(cx, cy)
                c.rotate(90)
                c.setFont("YaHeiBold", 11 * view.scale)
                c.setFillColor(color("#2E465B"))
                c.drawCentredString(0, 0, name)
                c.restoreState()
    elif typ in {"userTask", "serviceTask", "sendTask"}:
        view.rect(x, y, w, h, rounded=12, fill=1)
        draw_icon(view, typ, x + 4, y + 5)
        draw_text(view, name, x + 19, y + 7, w - 25, h - 13, size=12.4, max_lines=5)
    elif typ in {"startEvent", "endEvent", "intermediateCatchEvent"}:
        cx, cy = x + w / 2, y + h / 2
        view.circle(cx, cy, min(w, h) / 2)
        if typ == "endEvent":
            c.setLineWidth(3.3 * view.scale)
            view.circle(cx, cy, min(w, h) / 2 - 1.7)
        elif typ == "intermediateCatchEvent":
            view.circle(cx, cy, min(w, h) / 2 - 5)
            view.line(cx - 8, cy - 5, cx, cy + 1)
            view.line(cx, cy + 1, cx + 8, cy - 5)
        if name:
            b = lb or (x - 32, y + h + 4, w + 64, 37)
            draw_text(view, name, *b, size=10.5, max_lines=3)
    elif typ == "exclusiveGateway":
        p = c.beginPath()
        p.moveTo(*view.point(x + w / 2, y))
        p.lineTo(*view.point(x + w, y + h / 2))
        p.lineTo(*view.point(x + w / 2, y + h))
        p.lineTo(*view.point(x, y + h / 2))
        p.close()
        c.drawPath(p, stroke=1, fill=1)
        c.setLineWidth(3 * view.scale)
        view.line(x + w * .35, y + h * .35, x + w * .65, y + h * .65)
        view.line(x + w * .65, y + h * .35, x + w * .35, y + h * .65)
        if name:
            b = lb or (x - 45, y + h + 2, w + 90, 35)
            draw_text(view, name, *b, size=10, max_lines=3)
    elif typ == "textAnnotation":
        view.line(x + 7, y, x, y)
        view.line(x, y, x, y + h)
        view.line(x, y + h, x + 7, y + h)
        annotation = element.find("bpmn:text", namespaces=NS)
        raw = annotation.text if annotation is not None and annotation.text else ""
        draw_text(view, raw, x + 6, y, w - 8, h, size=8.5, align="left", max_lines=18)


def render_view(c, page_size, title, x, y, w, h, scale, ox, oy, page_index, page_count):
    c.setPageSize(page_size)
    c.setFillColor(colors.white)
    c.rect(0, 0, page_size[0], page_size[1], fill=1, stroke=0)
    c.setFont("YaHeiBold", 24)
    c.setFillColor(color("#17324D"))
    c.drawString(55, page_size[1] - 49, title)
    c.setFont("YaHei", 12)
    c.setFillColor(color("#4B637A"))
    c.drawString(55, page_size[1] - 72, f"Camunda 8 operational model | source SHA-256 {HASH} | page {page_index}/{page_count}")
    c.setStrokeColor(color("#C2D0DB"))
    c.line(55, page_size[1] - 86, page_size[0] - 55, page_size[1] - 86)
    view = View(c, x, y, w, h, scale, ox, oy)
    c.saveState()
    clip = c.beginPath()
    clip.rect(ox, oy, w * scale, h * scale)
    c.clipPath(clip, stroke=0, fill=0)
    # Participants and lanes are below the flow; edges remain below nodes.
    for shape in SHAPES:
        if tag(BY_ID[shape.get("bpmnElement")]) in {"participant", "lane"}:
            draw_shape(view, shape)
    for edge in EDGES:
        draw_edge(view, edge)
    for shape in SHAPES:
        if tag(BY_ID[shape.get("bpmnElement")]) not in {"participant", "lane"}:
            draw_shape(view, shape)
    c.restoreState()
    c.setFont("YaHei", 10)
    c.setFillColor(color("#4B637A"))
    c.drawRightString(page_size[0] - 55, 30, "Editable model: Coursework/hospital-pathway/bpmn/W02_Hospital_All_Processes_Clean_Lines_Camunda8.bpmn")
    c.showPage()


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUTPUT), pageCompression=1)
    c.setTitle("Hospital All Processes - Camunda 8 BPMN diagram")
    c.setAuthor("Hospital Pathway Group")
    # Entire diagram on one zoomable vector page, followed by eight readable tiles.
    render_view(c, (4120, 2430), "Hospital - all business processes | full BPMN overview",
                100, 45, 4030, 2260, .97, 95, 105, 1, 9)
    idx = 2
    for row, y in enumerate((50, 1140), start=1):
        for col, x in enumerate((100, 1080, 2060, 3040), start=1):
            render_view(c, (1210, 1360), f"Detail {row}.{col} | {['upper', 'lower'][row-1]} section",
                        x, y, 1110, 1180, .99, 55, 38, idx, 9)
            idx += 1
    c.save()
    print(f"{OUTPUT} ({OUTPUT.stat().st_size:,} bytes, 9 vector pages)")


if __name__ == "__main__":
    main()

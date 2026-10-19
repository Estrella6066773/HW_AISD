#!/usr/bin/env python3
"""Render the two BPMN models behind deliverable B-5 to readable A3 PDFs.

What it renders
  Operational (executable, Camunda 8)
      source : Week6 Coursework/bpmn/Hospital_All_Processes_V3.bpmn
      output : submissions/BPMEA/BPMEA_Operational_Process_Readable_2026-10-19.pdf
  Strategic (non-executable)
      source : docs/strategic-bpmn/PB-12_strategic-process_2026-09-29.bpmn
      output : submissions/BPMEA/BPMEA_Strategic_Process_Readable_2026-10-19.pdf

How
  1. bpmn-to-image (npx, bpmn-js in headless Chrome) renders the model to a PNG.
     The BPMN sources are opened read-only; nothing is written next to them.
  2. The PNG is sliced into tiles. Tile boundaries are placed in empty
     corridors of the model (between node boxes), so no task or gateway box
     is ever cut by a page edge. Every tile is validated against the DI bounds
     before the PDF is written.
  3. ReportLab lays out, per model: cover/index, fit-to-page overview (with
     the tile grid drawn on it), symbol legend, verbatim model notes, and the
     detail tiles. Page size A3 landscape.

Requirements
  Python 3.11, reportlab, pillow, npm/npx, Chrome or Edge.

Re-run (verified on this machine; uv stalled on the reportlab wheel, pip did not)
  python -m pip install --target "$env:TEMP\\b5deps" reportlab pillow
  $env:PYTHONPATH="$env:TEMP\\b5deps"
  python "Week6 Coursework/scripts/render_bpmn_readable_pdf.py"

  Only one model:  ... render_bpmn_readable_pdf.py --only operational
  Keep the PNGs:   ... render_bpmn_readable_pdf.py --work-dir D:\\temp\\b5

Scratch PNGs and crops go to a system temp directory (or --work-dir) and are
deleted afterwards, so the repository only gains the PDFs and this script.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image
from reportlab.lib.colors import Color, HexColor
from reportlab.lib.pagesizes import A3, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

ROOT = Path(__file__).resolve().parents[2]
PAGE_W, PAGE_H = landscape(A3)          # 1190.55 x 841.89 pt
MARGIN = 30.0
CONTENT_TOP = PAGE_H - 108.0
CONTENT_BOTTOM = 48.0
CONTENT_W = PAGE_W - 2 * MARGIN
CONTENT_H = CONTENT_TOP - CONTENT_BOTTOM

NAVY = HexColor("#17324d")
INK = HexColor("#253547")
MUTED = HexColor("#4b637a")
FAINT = HexColor("#667481")
ACCENT = HexColor("#1768a6")
RULE = HexColor("#9fb0c0")
PANEL = HexColor("#eef3f8")
RED = Color(0.78, 0.12, 0.12, alpha=0.95)

CHROME = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
EDGE = Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

FONT, FONT_B = "YaHei", "YaHei-Bold"


def register_fonts() -> None:
    """Microsoft YaHei matches the 29 September export; fall back silently."""
    global FONT, FONT_B
    try:
        pdfmetrics.registerFont(TTFont(FONT, r"C:\Windows\Fonts\msyh.ttc", subfontIndex=0))
        pdfmetrics.registerFont(TTFont(FONT_B, r"C:\Windows\Fonts\msyhbd.ttc", subfontIndex=0))
    except Exception:                       # noqa: BLE001 - non-Windows fallback
        FONT, FONT_B = "Helvetica", "Helvetica-Bold"


def tag(elem) -> str:
    return elem.tag.rsplit("}", 1)[-1]


# --------------------------------------------------------------------------- #
# Model facts
# --------------------------------------------------------------------------- #
def read_model(path: Path) -> dict:
    root = ET.parse(path).getroot()

    process = next(e for e in root.iter() if tag(e) == "process")
    collaboration = next((e for e in root if tag(e) == "collaboration"), None)

    direct = list(process)
    counts: dict[str, int] = {}
    for e in direct:
        counts[tag(e)] = counts.get(tag(e), 0) + 1

    job_types = []
    for e in direct:
        if tag(e) == "serviceTask":
            jt = ""
            for d in e.iter():
                if tag(d) == "taskDefinition":
                    jt = d.get("type", "")
            job_types.append((e.get("name", e.get("id", "")), jt))

    participants = []
    message_flows = []
    annotations = []
    if collaboration is not None:
        for e in collaboration:
            if tag(e) == "participant":
                participants.append({"id": e.get("id", ""), "name": e.get("name", ""),
                                     "processRef": e.get("processRef")})
            elif tag(e) == "messageFlow":
                message_flows.append(e.get("name", "") or e.get("id", ""))
            elif tag(e) == "textAnnotation":
                annotations.append({"id": e.get("id", ""),
                                    "text": (findtext(e, "text") or "")})
    for e in root.iter():
        if tag(e) == "textAnnotation" and not any(a["id"] == e.get("id") for a in annotations):
            annotations.append({"id": e.get("id", ""), "text": findtext(e, "text") or ""})

    lanes = []
    for e in process.iter():
        if tag(e) == "lane":
            lanes.append({"id": e.get("id", ""), "name": e.get("name", ""),
                          "nodes": sum(1 for c in e if tag(c) == "flowNodeRef")})

    # --- diagram interchange -------------------------------------------------
    diagram = next(e for e in root.iter() if tag(e) == "BPMNDiagram")
    plane = next(e for e in diagram.iter() if tag(e) == "BPMNPlane")
    boxes: dict[str, tuple[float, float, float, float]] = {}
    edge_label_boxes = []
    for shape in plane:
        if tag(shape) != "BPMNShape":
            continue
        bounds = next((c for c in shape if tag(c) == "Bounds"), None)
        if bounds is None:
            continue
        boxes[shape.get("bpmnElement", "")] = tuple(
            float(bounds.get(k, 0)) for k in ("x", "y", "width", "height")
        )
        for label in shape:
            if tag(label) == "BPMNLabel":
                lb = next((c for c in label if tag(c) == "Bounds"), None)
                if lb is not None:
                    edge_label_boxes.append(tuple(float(lb.get(k, 0))
                                                  for k in ("x", "y", "width", "height")))

    all_x, all_y = [], []
    for shape in plane:
        for b in shape.iter():
            if tag(b) == "Bounds":
                x, y, w, h = (float(b.get(k, 0)) for k in ("x", "y", "width", "height"))
                all_x += [x, x + w]
                all_y += [y, y + h]
            elif tag(b) == "waypoint":
                all_x.append(float(b.get("x", 0)))
                all_y.append(float(b.get("y", 0)))

    bbox = (min(all_x), min(all_y), max(all_x), max(all_y))

    skip = {p["id"] for p in participants} | {l["id"] for l in lanes}
    nodes = []
    for elem_id, (x, y, w, h) in boxes.items():
        if elem_id in skip:
            continue
        nodes.append({"id": elem_id, "box": (x, y, w, h)})

    ann_text = {a["id"]: a["text"] for a in annotations}
    for n in nodes:
        n["label"] = ann_text.get(n["id"], "")

    counts["messageFlow"] = len(message_flows)
    counts["textAnnotation"] = len(annotations)

    return {
        "root": root,
        "process_id": process.get("id", ""),
        "process_name": process.get("name", ""),
        "executable": process.get("isExecutable") == "true",
        "counts": counts,
        "job_types": job_types,
        "participants": participants,
        "message_flows": message_flows,
        "annotations": annotations,
        "lanes": lanes,
        "boxes": boxes,
        "nodes": nodes,
        "edge_label_boxes": edge_label_boxes,
        "bbox": bbox,
    }


def findtext(elem, name: str) -> str:
    for child in elem:
        if tag(child) == name:
            return child.text or ""
    return ""


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def last_commit(path: Path) -> tuple[str, str]:
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%H|%h|%ad", "--date=short", "--", str(path)],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout.strip()
        full, short, date = out.split("|", 2)
        return full, f"{short} ({date})"
    except Exception:                       # noqa: BLE001
        return "", "uncommitted / not tracked"


# --------------------------------------------------------------------------- #
# Rendering with bpmn-to-image
# --------------------------------------------------------------------------- #
def render_png(bpmn: Path, out: Path, scale: float) -> tuple[int, int]:
    env = os.environ.copy()
    browser = CHROME if CHROME.exists() else EDGE
    if browser.exists():
        env["PUPPETEER_EXECUTABLE_PATH"] = str(browser)
    cmd = (
        f'npx -y bpmn-to-image "{bpmn};{out}" '
        f"--scale {scale} --no-title --no-footer"
    )
    print(f"  bpmn-to-image -> {out.name} (scale {scale})")
    proc = subprocess.run(cmd, cwd=ROOT, env=env, shell=True,
                          capture_output=True, text=True, timeout=600)
    if proc.returncode != 0 or not out.exists():
        sys.stderr.write(proc.stdout + "\n" + proc.stderr + "\n")
        raise RuntimeError(f"bpmn-to-image failed for {bpmn}")
    with Image.open(out) as im:
        return im.size


# --------------------------------------------------------------------------- #
# PDF primitives
# --------------------------------------------------------------------------- #
def wrap(text: str, font: str, size: float, width: float) -> list[str]:
    words = re.split(r"(?<= )", text)
    lines, current = [], ""
    for word in words:
        trial = current + word
        if pdfmetrics.stringWidth(trial.rstrip(), font, size) <= width or not current:
            current = trial
        else:
            lines.append(current.rstrip())
            current = word.lstrip()
            while pdfmetrics.stringWidth(current, font, size) > width and len(current) > 1:
                cut = len(current)
                while cut > 1 and pdfmetrics.stringWidth(current[:cut], font, size) > width:
                    cut -= 1
                lines.append(current[:cut])
                current = current[cut:]
    if current.strip():
        lines.append(current.rstrip())
    return lines


def para(c, text, x, y, width, font=FONT, size=9.5, leading=13.2,
         color=INK, align="left") -> float:
    """Draw wrapped text top-down; returns the y after the last line."""
    c.setFont(font, size)
    c.setFillColor(color)
    for line in wrap(text, font, size, width):
        if align == "right":
            c.drawRightString(x + width, y, line)
        elif align == "center":
            c.drawCentredString(x + width / 2, y, line)
        else:
            c.drawString(x, y, line)
        y -= leading
    return y


def footer(c, page_no: int, total: int) -> None:
    c.setStrokeColor(RULE)
    c.setLineWidth(0.5)
    c.line(MARGIN, 38, PAGE_W - MARGIN, 38)
    c.setFont(FONT, 7.6)
    c.setFillColor(MUTED)
    c.drawString(MARGIN, 24, "Group 10  |  UFCEP4-0-3  |  BPM&E submission")
    c.drawRightString(PAGE_W - MARGIN, 24, f"Deliverable B-5  |  Page {page_no} of {total}")


def page_header(c, title: str, subtitle: str, note: str = "") -> None:
    c.setFillColor(NAVY)
    c.rect(0, PAGE_H - 8, PAGE_W, 8, stroke=0, fill=1)
    c.setFont(FONT_B, 15)
    c.setFillColor(NAVY)
    c.drawString(MARGIN, PAGE_H - 50, title)
    c.setFont(FONT, 8.2)
    c.setFillColor(MUTED)
    c.drawString(MARGIN, PAGE_H - 65, subtitle)
    if note:
        c.setFont(FONT, 8.2)
        c.setFillColor(FAINT)
        c.drawRightString(PAGE_W - MARGIN, PAGE_H - 65, note)
    c.setStrokeColor(RULE)
    c.setLineWidth(0.5)
    c.line(MARGIN, PAGE_H - 74, PAGE_W - MARGIN, PAGE_H - 74)


def section_label(c, text, x, y, width=None) -> None:
    c.setFont(FONT_B, 8.2)
    c.setFillColor(ACCENT)
    c.drawString(x, y, text.upper())
    c.setStrokeColor(ACCENT)
    c.setLineWidth(0.9)
    c.line(x, y - 4, x + (width or 120), y - 4)


# --------------------------------------------------------------------------- #
# Legend symbols
# --------------------------------------------------------------------------- #
def sym_user_task(c, x, y, w=96, h=54):
    c.setStrokeColor(INK)
    c.setFillColor(HexColor("#ffffff"))
    c.setLineWidth(1.1)
    c.roundRect(x, y, w, h, 8, stroke=1, fill=1)
    person(c, x + 7, y + h - 16, 9)
    c.setFont(FONT, 6.4)
    c.setFillColor(INK)
    c.drawCentredString(x + w / 2, y + 9, "Task name")


def person(c, x, y, s):
    c.setLineWidth(0.9)
    c.setStrokeColor(INK)
    c.setFillColor(INK)
    c.circle(x + s / 2, y + s * 0.68, s * 0.22, stroke=1, fill=1)
    p = c.beginPath()
    p.moveTo(x + s * 0.12, y)
    p.curveTo(x + s * 0.12, y + s * 0.42, x + s * 0.88, y + s * 0.42, x + s * 0.88, y)
    c.drawPath(p, stroke=1, fill=0)


def gear(c, x, y, r=4.2):
    import math
    c.setStrokeColor(INK)
    c.setFillColor(INK)
    for i in range(8):
        a = math.pi * i / 4
        c.saveState()
        c.translate(x, y)
        c.rotate(a * 180 / math.pi)
        c.rect(r * 0.55, -0.7, r * 0.65, 1.4, stroke=0, fill=1)
        c.restoreState()
    c.circle(x, y, r * 0.55, stroke=1, fill=1)
    c.setFillColor(HexColor("#ffffff"))
    c.circle(x, y, r * 0.22, stroke=0, fill=1)


def sym_service_task(c, x, y, w=96, h=54):
    c.setStrokeColor(INK)
    c.setFillColor(HexColor("#ffffff"))
    c.setLineWidth(1.1)
    c.roundRect(x, y, w, h, 8, stroke=1, fill=1)
    gear(c, x + 12, y + h - 13, 4.0)
    c.setFont(FONT, 6.4)
    c.setFillColor(INK)
    c.drawCentredString(x + w / 2, y + 9, "Job worker task")
    c.setFont(FONT, 5.4)
    c.setFillColor(FAINT)
    c.drawCentredString(x + w / 2, y + 19, "job type: check-slot")


def sym_send_task(c, x, y, w=96, h=54):
    c.setStrokeColor(INK)
    c.setFillColor(HexColor("#ffffff"))
    c.setLineWidth(1.1)
    c.roundRect(x, y, w, h, 8, stroke=1, fill=1)
    envelope(c, x + 8, y + h - 21, 13, 10, filled=True)
    c.setFont(FONT, 6.4)
    c.setFillColor(INK)
    c.drawCentredString(x + w / 2, y + 9, "Send task")


def envelope(c, x, y, w, h, filled=False):
    c.setLineWidth(0.9)
    c.setStrokeColor(INK)
    c.setFillColor(INK)
    c.rect(x, y, w, h, stroke=1, fill=1 if filled else 0)
    if filled:
        c.setStrokeColor(HexColor("#ffffff"))
    p = c.beginPath()
    p.moveTo(x, y + h)
    p.lineTo(x + w / 2, y + h * 0.45)
    p.lineTo(x + w, y + h)
    c.drawPath(p, stroke=1, fill=0)


def diamond(c, cx, cy, r=22):
    c.setStrokeColor(INK)
    c.setFillColor(HexColor("#ffffff"))
    c.setLineWidth(1.1)
    p = c.beginPath()
    p.moveTo(cx, cy + r)
    p.lineTo(cx + r, cy)
    p.lineTo(cx, cy - r)
    p.lineTo(cx - r, cy)
    p.close()
    c.drawPath(p, stroke=1, fill=1)


def sym_exclusive(c, x, y, w=96, h=54, parallel=False):
    cx, cy = x + 26, y + h / 2
    diamond(c, cx, cy, 20)
    c.setLineWidth(1.4)
    c.setStrokeColor(INK)
    if parallel:
        c.line(cx - 8, cy, cx + 8, cy)
        c.line(cx, cy - 8, cx, cy + 8)
    else:
        c.line(cx - 7, cy - 7, cx + 7, cy + 7)
        c.line(cx - 7, cy + 7, cx + 7, cy - 7)



def sym_event(c, x, y, w=96, h=54, kind="end"):
    cx, cy = x + 26, y + h / 2
    c.setStrokeColor(INK)
    c.setFillColor(HexColor("#ffffff"))
    if kind == "end":
        c.setLineWidth(3.2)
        c.circle(cx, cy, 15, stroke=1, fill=1)
    elif kind == "start":
        c.setLineWidth(1.3)
        c.circle(cx, cy, 15, stroke=1, fill=1)
    else:                                   # message catch
        c.setLineWidth(1.3)
        c.circle(cx, cy, 17, stroke=1, fill=1)
        c.circle(cx, cy, 13, stroke=1, fill=1)
        envelope(c, cx - 6, cy - 4, 12, 8)
        c.setStrokeColor(INK)
        c.setFillColor(HexColor("#ffffff"))


def sym_lane(c, x, y, w=96, h=54):
    c.setStrokeColor(INK)
    c.setFillColor(HexColor("#ffffff"))
    c.setLineWidth(1.0)
    c.rect(x, y, w, h, stroke=1, fill=1)
    c.setFillColor(PANEL)
    c.rect(x, y, 16, h, stroke=0, fill=1)
    c.setStrokeColor(INK)
    c.line(x + 16, y, x + 16, y + h)
    c.saveState()
    c.translate(x + 6, y + h / 2)
    c.rotate(90)
    c.setFont(FONT_B, 6.0)
    c.setFillColor(INK)
    c.drawCentredString(0, 0, "Lane")
    c.restoreState()


def arrow_head(c, x, y, angle=0):
    import math
    c.saveState()
    c.translate(x, y)
    c.rotate(angle)
    c.setFillColor(INK)
    c.setStrokeColor(INK)
    p = c.beginPath()
    p.moveTo(0, 0)
    p.lineTo(-7, 3.2)
    p.lineTo(-7, -3.2)
    p.close()
    c.drawPath(p, stroke=0, fill=1)
    c.restoreState()


def sym_sequence(c, x, y, w=96, h=54):
    y0 = y + h / 2
    c.setStrokeColor(INK)
    c.setLineWidth(1.2)
    c.setDash()
    c.line(x + 4, y0, x + w - 10, y0)
    arrow_head(c, x + w - 8, y0)


def sym_message(c, x, y, w=96, h=54):
    y0 = y + h / 2
    c.setStrokeColor(INK)
    c.setLineWidth(1.1)
    c.setDash(4, 3)
    c.line(x + 10, y0, x + w - 10, y0)
    c.setDash()
    c.circle(x + 9, y0, 2.4, stroke=1, fill=0)
    arrow_head(c, x + w - 8, y0)


def sym_annotation(c, x, y, w=96, h=54):
    c.setStrokeColor(FAINT)
    c.setLineWidth(1.0)
    c.line(x + 8, y + 8, x + 8, y + h - 8)
    c.line(x + 8, y + h - 8, x + 14, y + h - 8)
    c.line(x + 8, y + 8, x + 14, y + 8)


def sym_absence(c, x, y, w=96, h=54):
    c.setStrokeColor(FAINT)
    c.setFillColor(HexColor("#ffffff"))
    c.setLineWidth(1.0)
    c.setDash(3, 2)
    c.roundRect(x + 4, y + 8, w - 8, h - 16, 6, stroke=1, fill=1)
    c.setDash()
    c.setLineWidth(1.4)
    c.setStrokeColor(RED)
    c.line(x + 10, y + 12, x + w - 10, y + h - 12)


def sym_pool(c, x, y, w=96, h=54):
    c.setStrokeColor(INK)
    c.setFillColor(HexColor("#ffffff"))
    c.setLineWidth(1.0)
    c.rect(x, y, w, h, stroke=1, fill=1)
    c.setFillColor(PANEL)
    c.rect(x, y, 20, h, stroke=0, fill=1)
    c.rect(x + 20, y + h - 12, w - 20, 12, stroke=0, fill=1)
    c.setStrokeColor(INK)
    c.line(x + 20, y, x + 20, y + h)
    c.line(x + 20, y + h - 12, x + w, y + h - 12)
    c.saveState()
    c.translate(x + 7, y + h / 2 - 6)
    c.rotate(90)
    c.setFont(FONT_B, 6.0)
    c.setFillColor(INK)
    c.drawCentredString(0, 0, "Pool")
    c.restoreState()


# --------------------------------------------------------------------------- #
# Page builders
# --------------------------------------------------------------------------- #
def draw_cover(c, cfg, facts, page_no, total, contents):
    c.setFillColor(NAVY)
    c.rect(0, PAGE_H - 10, PAGE_W, 10, stroke=0, fill=1)

    x = MARGIN
    c.setFont(FONT_B, 8.6)
    c.setFillColor(ACCENT)
    c.drawString(x, PAGE_H - 48,
                 "UFCEP4-0-3  ·  BUSINESS PROCESS MANAGEMENT & ENTERPRISE ARCHITECTURE  ·  GROUP 10")
    c.setFont(FONT_B, 33)
    c.setFillColor(NAVY)
    c.drawString(x, PAGE_H - 96, cfg["cover_title"])
    c.setFont(FONT, 14)
    c.setFillColor(MUTED)
    c.drawString(x, PAGE_H - 120, cfg["cover_subtitle"])
    c.setStrokeColor(NAVY)
    c.setLineWidth(1.2)
    c.line(x, PAGE_H - 136, PAGE_W - MARGIN, PAGE_H - 136)

    left_x, left_w = MARGIN, 640
    right_x, right_w = 700, PAGE_W - MARGIN - 700
    y = PAGE_H - 168

    section_label(c, "Model of record", left_x, y, 130)
    y -= 20
    src_hash = facts["sha256"]
    rows = [
        ("Source file", cfg["source_display"]),
        ("Process id", facts["process_id"]),
        ("Process name", facts["process_name"]),
        ("Executable", "yes" if facts["executable"] else "no (strategic / non-executable)"),
        ("Commit", f"{cfg['commit_short']}  ·  {cfg['commit_full']}" if cfg["commit_full"]
                   else cfg["commit_short"]),
        ("File SHA-256", src_hash),
        ("Canvas", f"{facts['bbox'][2] - facts['bbox'][0]:,.0f} × "
                   f"{facts['bbox'][3] - facts['bbox'][1]:,.0f} model units"),
        ("Element summary", cfg["element_summary"]),
    ]
    for label, value in rows:
        c.setFont(FONT_B, 8.4)
        c.setFillColor(FAINT)
        c.drawString(left_x, y, label)
        yy = para(c, value, left_x + 104, y, left_w - 104, size=9.2, leading=12.4)
        y = min(y - 20.5, yy - 6)

    # members + submission data
    y2 = PAGE_H - 168
    section_label(c, "Submission", right_x, y2, 110)
    y2 -= 20
    for label, value in [("Deliverable", "B-5 — readable PDF exports"),
                         ("Module", "UFCEP4-0-3"),
                         ("Group", "10"),
                         ("Date", "2026-10-19")]:
        c.setFont(FONT_B, 8.4)
        c.setFillColor(FAINT)
        c.drawString(right_x, y2, label)
        c.setFont(FONT, 9.4)
        c.setFillColor(INK)
        c.drawString(right_x + 86, y2, value)
        y2 -= 19

    y2 -= 8
    section_label(c, "Members", right_x, y2, 90)
    y2 -= 20
    for name in ["Hao Zheng / Ruby / 23084382",
                 "Geping Chen / Estrella / 23084393",
                 "Minghao Qin / Ender / 23084402",
                 "Guanyan He / Ryan / 23084395"]:
        c.setFont(FONT, 9.6)
        c.setFillColor(INK)
        c.drawString(right_x, y2, name)
        y2 -= 17

    # contents
    cy = 258
    section_label(c, "Contents", MARGIN, cy, 90)
    cy -= 24
    col_w = (PAGE_W - 2 * MARGIN) / 2
    for i, (label, pno) in enumerate(contents):
        col = i % 2
        row = i // 2
        cx = MARGIN + col * col_w
        yy = cy - row * 18
        c.setFont(FONT, 9.4)
        c.setFillColor(INK)
        c.drawString(cx, yy, label)
        c.setFont(FONT, 9.0)
        c.setFillColor(MUTED)
        c.drawRightString(cx + col_w - 24, yy, f"p{pno}")
        c.setStrokeColor(HexColor("#c8d4df"))
        c.setLineWidth(0.4)
        c.setDash(1, 3)
        c.line(cx + pdfmetrics.stringWidth(label, FONT, 9.4) + 6, yy + 2,
               cx + col_w - 30, yy + 2)
        c.setDash()

    c.setFont(FONT, 8.0)
    c.setFillColor(FAINT)
    para(c, "Diagram pages in this export are raster images produced by bpmn-to-image "
            "(bpmn-js). Task names, gateway conditions and flow labels are therefore "
            "pixel content, not selectable text; this cover, the legend and the notes "
            "pages are vector text and can be searched and copied. The 29 September "
            "initial-release export (submissions/AISD/Hospital_All_Processes_Camunda8_"
            "Export_2026-09-29.pdf) is unchanged by this file.",
         MARGIN, 96, PAGE_W - 2 * MARGIN, size=7.8, leading=10.4, color=FAINT)

    footer(c, page_no, total)


def draw_overview(c, cfg, facts, image_path, tiles, page_no, total):
    page_header(c, cfg["title"] + " — full process overview",
                f"{cfg['source_name']}  ·  process {facts['process_id']}  ·  "
                f"fit to page, not to scale",
                f"SHA-256 {facts['sha256'][:16]}…")
    bx0, by0, bx1, by1 = facts["bbox"]
    iw, ih = bx1 - bx0, by1 - by0
    scale = min(CONTENT_W / iw, (CONTENT_H - 34) / ih)
    w, h = iw * scale, ih * scale
    x = (PAGE_W - w) / 2
    y = CONTENT_BOTTOM + 26 + (CONTENT_H - 34 - h) / 2

    c.setFillColor(HexColor("#ffffff"))
    c.setStrokeColor(RULE)
    c.setLineWidth(0.6)
    c.rect(x, y, w, h, stroke=1, fill=1)
    c.drawImage(ImageReader(str(image_path)), x, y, width=w, height=h)

    # tile grid
    c.setStrokeColor(RED)
    c.setLineWidth(0.8)
    c.setDash(4, 2)
    for col in cfg["columns"][:-1]:
        px = x + (col[1] - bx0) * scale
        c.line(px, y, px, y + h)
    for row in cfg["rows"][:-1]:
        py = y + h - (row[1] - by0) * scale
        c.line(x, py, x + w, py)
    c.setDash()

    c.setFont(FONT_B, 6.2)
    for ri, (ry0, ry1) in enumerate(cfg["rows"], start=1):
        for ci, (cx0, cx1) in enumerate(cfg["columns"], start=1):
            lx = x + (cx0 - bx0) * scale + 4
            ly = y + h - (ry0 - by0) * scale - 11
            label = f"r{ri}c{ci}"
            tw = pdfmetrics.stringWidth(label, FONT_B, 6.2)
            c.setFillColor(Color(1, 1, 1, alpha=0.85))
            c.rect(lx - 2, ly - 2, tw + 4, 9, stroke=0, fill=1)
            c.setFillColor(RED)
            c.drawString(lx, ly, label)

    c.setFont(FONT, 8.4)
    c.setFillColor(MUTED)
    c.drawCentredString(PAGE_W / 2, CONTENT_BOTTOM + 12,
                        f"Whole model on one page — detail follows at "
                        f"{cfg['scale']:.2f}× in {len(cfg['columns'])} columns × "
                        f"{len(cfg['rows'])} rows. Dashed grid = tile boundaries.")
    footer(c, page_no, total)


def draw_legend(c, cfg, facts, page_no, total):
    page_header(c, "Legend — BPMN symbols used in this model",
                cfg["title"] + "  ·  counts are taken from the source file",
                "Symbols drawn from the model's own element set")

    items = cfg["legend"]
    cols, rows = 3, 4
    gap_x, gap_y = 14, 10
    card_w = (CONTENT_W - gap_x * (cols - 1)) / cols
    card_h = (CONTENT_H - 96 - gap_y * (rows - 1)) / rows
    top = CONTENT_TOP - 8
    for idx, item in enumerate(items):
        ci, ri = idx % cols, idx // cols
        x = MARGIN + ci * (card_w + gap_x)
        y = top - (ri + 1) * card_h - ri * gap_y
        c.setFillColor(HexColor("#f7f9fb"))
        c.setStrokeColor(HexColor("#d7e1ea"))
        c.setLineWidth(0.6)
        c.roundRect(x, y, card_w, card_h, 5, stroke=1, fill=1)
        item["draw"](c, x + 12, y + card_h / 2 - 27)
        tx = x + 122
        tw = card_w - 134
        c.setFont(FONT_B, 9.0)
        c.setFillColor(NAVY)
        c.drawString(tx, y + card_h - 20, item["title"])
        c.setFont(FONT, 7.6)
        c.setFillColor(ACCENT)
        c.drawString(tx, y + card_h - 31, item["count"])
        para(c, item["detail"], tx, y + card_h - 44, tw, size=7.4, leading=9.6, color=INK)

    # job-type strip (operational) / note (strategic)
    y = CONTENT_BOTTOM + 6
    if cfg.get("job_table"):
        c.setFont(FONT_B, 7.6)
        c.setFillColor(ACCENT)
        c.drawString(MARGIN, y + 46, "SERVICE TASK → ZEEBE JOB TYPE (zeebe:taskDefinition)")
        entries = cfg["job_table"]
        half = (len(entries) + 1) // 2
        for i, (name, jt) in enumerate(entries):
            col = 0 if i < half else 1
            row = i if i < half else i - half
            xx = MARGIN + col * (CONTENT_W / 2)
            yy = y + 34 - row * 10.5
            c.setFont(FONT, 7.2)
            c.setFillColor(INK)
            c.drawString(xx, yy, f"•  {' '.join(name.split())}")
            c.setFont(FONT, 7.2)
            c.setFillColor(ACCENT)
            c.drawRightString(xx + CONTENT_W / 2 - 26, yy, jt)
    else:
        c.setFont(FONT, 7.8)
        c.setFillColor(FAINT)
        c.drawString(MARGIN, y + 24,
                     "This strategic model uses abstract tasks, not Camunda user/service tasks: "
                     "no forms, job types or assignments are defined in it.")
    footer(c, page_no, total)


def draw_notes(c, cfg, facts, page_no, total):
    page_header(c, cfg["notes_title"],
                "Reproduced verbatim from the collaboration-level text annotations in the source file",
                cfg["source_name"])
    style = ParagraphStyle("notes", fontName=FONT, fontSize=9.6, leading=14.2,
                           textColor=INK, spaceAfter=8)
    story_y = CONTENT_TOP - 6
    blocks = cfg["notes"]
    frame_w = CONTENT_W
    for heading, text in blocks:
        c.setFont(FONT_B, 9.4)
        c.setFillColor(ACCENT)
        c.drawString(MARGIN, story_y, heading)
        story_y -= 16
        paragraphs = [p for p in text.split("\n") if p.strip()]
        for p in paragraphs:
            html = escape(p).replace("  ", "&nbsp;&nbsp;")
            para_obj = Paragraph(html, style)
            w, h = para_obj.wrap(frame_w, 200)
            para_obj.drawOn(c, MARGIN, story_y - h)
            story_y -= h + 8
        story_y -= 6
    footer(c, page_no, total)


def draw_tile(c, cfg, facts, image, thumb_reader, tile, page_no, total):
    ri, ci, (x0, y0, x1, y1) = tile["r"], tile["c"], tile["region"]
    band = cfg["row_labels"][ri - 1]
    page_header(c,
                f"{cfg['short']} — detail tile r{ri}c{ci} of "
                f"{len(cfg['rows'])}×{len(cfg['columns'])}",
                f"{band}  ·  {cfg['source_name']}  ·  process "
                f"{facts['process_id']}  ·  scale {cfg['scale']:.2f}",
                f"Region x {x0:,.0f}–{x1:,.0f}, y {y0:,.0f}–{y1:,.0f} "
                f"(model units)  ·  column {ci} of {len(cfg['columns'])}")

    # locator
    tw, th = 86, 86 * (facts["bbox"][3] - facts["bbox"][1]) / (
        facts["bbox"][2] - facts["bbox"][0])
    tx, ty = PAGE_W - MARGIN - tw, PAGE_H - 104 - th
    c.drawImage(thumb_reader, tx, ty, width=tw, height=th)
    c.setStrokeColor(HexColor("#c8d4df"))
    c.setLineWidth(0.4)
    c.rect(tx, ty, tw, th, stroke=1, fill=0)
    bx0, by0, bx1, by1 = facts["bbox"]
    rx = tx + (x0 - bx0) / (bx1 - bx0) * tw
    ry = ty + th - (y1 - by0) / (by1 - by0) * th
    rw = (x1 - x0) / (bx1 - bx0) * tw
    rh = (y1 - y0) / (by1 - by0) * th
    c.setStrokeColor(RED)
    c.setLineWidth(1.1)
    c.rect(rx, ry, rw, rh, stroke=1, fill=0)

    w = (x1 - x0) * cfg["scale"]
    h = (y1 - y0) * cfg["scale"]
    x = MARGIN
    avail = CONTENT_TOP - (CONTENT_BOTTOM + 18)
    y = CONTENT_BOTTOM + 18 + (avail - h) / 2
    c.setFillColor(HexColor("#ffffff"))
    c.setStrokeColor(HexColor("#d7e1ea"))
    c.setLineWidth(0.5)
    c.rect(x - 2, y - 2, w + 4, h + 4, stroke=1, fill=1)

    # crop in pixel space
    S = image["scale"]
    bx0, by0, bx1, by1 = facts["bbox"]
    px0 = max(0, round((x0 - bx0) * S))
    py0 = max(0, round((y0 - by0) * S))
    px1 = min(image["img"].width, round((x1 - bx0) * S))
    py1 = min(image["img"].height, round((y1 - by0) * S))
    crop = image["img"].crop((px0, py0, px1, py1))
    c.drawImage(ImageReader(crop), x, y, width=w, height=h)

    c.setFont(FONT, 7.2)
    c.setFillColor(FAINT)
    neighbours = []
    if ci < len(cfg["columns"]):
        neighbours.append(f"next column → r{ri}c{ci + 1}")
    if ri < len(cfg["rows"]):
        neighbours.append(f"next row ↓ r{ri + 1}c{ci}")
    c.drawString(MARGIN, CONTENT_BOTTOM + 6,
                 f"Tile boundaries sit in empty corridors between node boxes; "
                 f"flow lines may continue on the adjacent page.   "
                 + "   ·   ".join(neighbours))
    footer(c, page_no, total)


# --------------------------------------------------------------------------- #
# Assembly
# --------------------------------------------------------------------------- #
def build(cfg, workdir: Path, only: str | None) -> Path:
    facts = read_model(cfg["bpmn"])
    facts["sha256"] = sha256(cfg["bpmn"])
    cfg["commit_full"], cfg["commit_short"] = last_commit(cfg["bpmn"])
    cfg["source_name"] = cfg["bpmn"].name
    cfg["element_summary"] = summary_line(facts)

    tiles = [{"r": ri, "c": ci, "region": (cx0, ry0, cx1, ry1)}
             for ri, (ry0, ry1) in enumerate(cfg["rows"], start=1)
             for ci, (cx0, cx1) in enumerate(cfg["columns"], start=1)]
    cfg["tiles"] = tiles
    validate_tiles(facts, cfg)

    # page plan
    pages = ["cover", "overview", "legend", "notes"] + ["tile"] * len(tiles)
    total = len(pages)
    contents = [
        ("Overview — whole process", 2),
        ("Legend — BPMN symbols", 3),
        (cfg["notes_title"].split("—")[0].strip(), 4),
        (f"Detail tiles — {len(cfg['columns'])} columns × {len(cfg['rows'])} rows", 5),
    ]

    png = workdir / f"{cfg['key']}.png"
    size = render_png(cfg["bpmn"], png, cfg["render_scale"])
    expected = (round((facts["bbox"][2] - facts["bbox"][0]) * cfg["render_scale"]),
                round((facts["bbox"][3] - facts["bbox"][1]) * cfg["render_scale"]))
    if abs(size[0] - expected[0]) > 2 or abs(size[1] - expected[1]) > 2:
        print(f"  ! PNG {size} differs from DI bounds {expected}; "
              f"tile offsets may be off")

    full = Image.open(png).convert("RGB")

    # overview image, downsampled for embedding
    ow = 2400
    oh = round(ow * full.height / full.width)
    overview_path = workdir / f"{cfg['key']}_overview.png"
    full.resize((ow, oh), Image.LANCZOS).save(overview_path)

    tw = 360
    th = max(1, round(tw * full.height / full.width))
    thumb_path = workdir / f"{cfg['key']}_thumb.png"
    full.resize((tw, th), Image.LANCZOS).save(thumb_path)
    thumb_reader = ImageReader(str(thumb_path))

    out = cfg["out"]
    out.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(out), pagesize=(PAGE_W, PAGE_H), pageCompression=1)
    c.setTitle(cfg["pdf_title"])
    c.setAuthor("Group 10 — UFCEP4-0-3")
    c.setSubject("B-5 readable BPMN export, 2026-10-19")
    c.setCreator("render_bpmn_readable_pdf.py (bpmn-to-image + ReportLab)")
    c.setProducer("ReportLab PDF Library - (opensource)")

    image = {"img": full, "scale": cfg["render_scale"]}
    for idx, kind in enumerate(pages, start=1):
        if kind == "cover":
            draw_cover(c, cfg, facts, idx, total, contents)
        elif kind == "overview":
            draw_overview(c, cfg, facts, overview_path, tiles, idx, total)
        elif kind == "legend":
            draw_legend(c, cfg, facts, idx, total)
        elif kind == "notes":
            draw_notes(c, cfg, facts, idx, total)
        else:
            draw_tile(c, cfg, facts, image, thumb_reader, tiles[idx - 5], idx, total)
        c.showPage()
    c.save()
    full.close()
    print(f"  wrote {out.relative_to(ROOT)}  ({out.stat().st_size / 1e6:.1f} MB, "
          f"{total} pages)")
    return out


def summary_line(facts: dict) -> str:
    c = facts["counts"]
    parts = []
    pairs = [("userTask", "user task", "user tasks"),
             ("serviceTask", "service task", "service tasks"),
             ("sendTask", "send task", "send tasks"),
             ("task", "abstract task", "abstract tasks"),
             ("exclusiveGateway", "exclusive gateway", "exclusive gateways"),
             ("parallelGateway", "parallel gateway", "parallel gateways"),
             ("startEvent", "start event", "start events"),
             ("endEvent", "end event", "end events"),
             ("intermediateCatchEvent", "message catch event", "message catch events"),
             ("sequenceFlow", "sequence flow", "sequence flows"),
             ("messageFlow", "message flow", "message flows"),
             ("textAnnotation", "text annotation", "text annotations")]
    for key, one, many in pairs:
        n = c.get(key, 0)
        if not n:
            continue
        label = one if n == 1 else many
        extra = ""
        if key == "exclusiveGateway":
            joins = sum(1 for e in facts["root"].iter()
                        if tag(e) == "exclusiveGateway" and (e.get("id") or "").startswith("Join_"))
            if joins:
                extra = f" ({joins} Join_* merges)"
        parts.append(f"{n} {label}{extra}")
    return " · ".join(parts)


def validate_tiles(facts: dict, cfg: dict) -> None:
    """Every node box in the tiled area must sit wholly inside one tile."""
    bx0, by0, bx1, by1 = facts["bbox"]
    regions = [(t["region"], t) for t in cfg["tiles"]]
    failures = []
    for node in facts["nodes"]:
        x, y, w, h = node["box"]
        touches = any(
            x + w > rx0 and x < rx1 and y + h > ry0 and y < ry1
            for (rx0, ry0, rx1, ry1), _ in regions
        )
        if not touches:
            continue                        # outside the tiled area, e.g. the guide band
        inside = any(
            rx0 <= x and x + w <= rx1 and ry0 <= y and y + h <= ry1
            for (rx0, ry0, rx1, ry1), _ in regions
        )
        if not inside:
            failures.append((node["id"], node["box"]))
    for (rx0, ry0, rx1, ry1), t in regions:
        w = (rx1 - rx0) * cfg["scale"]
        h = (ry1 - ry0) * cfg["scale"]
        if w > CONTENT_W + 0.5 or h > CONTENT_H - 18:
            raise SystemExit(f"tile r{t['r']}c{t['c']} does not fit the page "
                             f"({w:.1f} x {h:.1f} pt)")
    if failures:
        raise SystemExit("tile boundaries cut these elements: "
                         + ", ".join(f"{i} {b}" for i, b in failures[:8]))
    print(f"  tile check: {len(facts['nodes'])} node boxes, none cut by a page edge")


# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #
def config_operational() -> dict:
    legend = [
        {"title": "Start event", "count": "1 occurrence",
         "detail": "Thin circle. The process starts when a request is registered.",
         "draw": lambda c, x, y: sym_event(c, x, y, kind="start")},
        {"title": "User task", "count": "22 occurrences",
         "detail": "Human work with a Camunda form. Every user task in this model has "
                   "assignee=\"demo\"; decisions feed the gateway conditions through "
                   "task output mappings.",
         "draw": sym_user_task},
        {"title": "Service task", "count": "8 occurrences",
         "detail": "Zeebe job worker. The job type is shown under the task name and "
                   "listed on this page.",
         "draw": sym_service_task},
        {"title": "Send task", "count": "2 occurrences",
         "detail": "request-payment and send-booking-confirmation. A send task publishes "
                   "a message instead of waiting for one.",
         "draw": sym_send_task},
        {"title": "Exclusive gateway (XOR)", "count": "27 occurrences",
         "detail": "Conditional split or merge. 12 are Join_* pass-through merges with no "
                   "condition; they merge branches before the next task.",
         "draw": sym_exclusive},
        {"title": "Message catch event", "count": "1 occurrence",
         "detail": "PaymentReceived waits for message payment-result "
                   "(correlation key case_reference).",
         "draw": lambda c, x, y: sym_event(c, x, y, kind="message")},
        {"title": "End event", "count": "7 occurrences",
         "detail": "One terminal outcome per branch: referral, report, enquiry (×3), "
                   "care episode, rejection.",
         "draw": lambda c, x, y: sym_event(c, x, y, kind="end")},
        {"title": "Lane", "count": "3 lanes",
         "detail": "Administration, Clinical team and Finance inside the HOSPITAL pool; "
                   "each lane owns its user tasks and workers.",
         "draw": sym_lane},
        {"title": "Sequence flow", "count": "97 occurrences",
         "detail": "Solid arrow inside one pool. Conditions are written on the outgoing "
                   "flows of the XOR gateways.",
         "draw": sym_sequence},
        {"title": "Message flow", "count": "5 occurrences",
         "detail": "Dashed arrow across pool boundaries: referral documents, appointment "
                   "contact, treatment arrangements, payment request and result.",
         "draw": sym_message},
        {"title": "Text annotation", "count": "7 occurrences",
         "detail": "Stage markers 1–4, CHANGES / CANCELLATIONS, and the two reading-guide "
                   "blocks at the bottom of the canvas.",
         "draw": sym_annotation},
        {"title": "Pool / participant", "count": "4 participants",
         "detail": "HOSPITAL is the only pool with process content; the referrer, patient "
                   "and payment provider are black-box participants.",
         "draw": sym_pool},
    ]
    cfg = {
        "key": "operational",
        "bpmn": ROOT / "Week6 Coursework/bpmn/Hospital_All_Processes_V3.bpmn",
        "out": ROOT / "submissions/BPMEA/BPMEA_Operational_Process_Readable_2026-10-19.pdf",
        "source_display": "Week6 Coursework/bpmn/Hospital_All_Processes_V3.bpmn",
        "cover_title": "Hospital patient pathway — operational BPMN",
        "cover_subtitle": "Readable PDF export  ·  executable Camunda 8 model, version 3",
        "title": "Operational BPMN (V3, Camunda 8)",
        "short": "Operational BPMN",
        "pdf_title": "Hospital pathway — operational BPMN (V3) — readable export (B-5)",
        "notes_title": "Reading guide and business controls",
        "render_scale": 3,
        "scale": 0.85,
        "columns": [(140, 650), (650, 1870), (1870, 2835), (2835, 4090)],
        "rows": [(160, 710), (710, 1260), (1260, 2040)],
        "row_labels": ["Administration lane (external pools are on the overview)",
                       "Clinical team lane",
                       "Finance lane and external payment provider"],
        "legend": legend,
        "job_table": None,
    }
    return cfg


def config_strategic() -> dict:
    legend = [
        {"title": "Start event", "count": "1 occurrence",
         "detail": "The incoming request enters the strategic pathway.",
         "draw": lambda c, x, y: sym_event(c, x, y, kind="start")},
        {"title": "Task (abstract)", "count": "14 occurrences",
         "detail": "One business stage per task. The model is non-executable: no forms, "
                   "assignees, job workers or output mappings.",
         "draw": sym_user_task},
        {"title": "Exclusive gateway (XOR)", "count": "5 occurrences",
         "detail": "Business choices: incoming kind, clinical decision, after the "
                   "consultation, enquiry class, money affected.",
         "draw": sym_exclusive},
        {"title": "Parallel gateway (AND)", "count": "1 occurrence",
         "detail": "Attendance recorded — splits into treatment and letter paths.",
         "draw": lambda c, x, y: sym_exclusive(c, x, y, parallel=True)},
        {"title": "End event", "count": "9 occurrences",
         "detail": "Terminal business outcomes, from referral closed to financial review "
                   "recorded.",
         "draw": lambda c, x, y: sym_event(c, x, y, kind="end")},
        {"title": "Message flow", "count": "17 occurrences",
         "detail": "Dashed arrows to and from the black-box participants. These show the "
                   "external interactions the operational model has to realise.",
         "draw": sym_message},
        {"title": "Sequence flow", "count": "30 occurrences",
         "detail": "Solid arrows inside the HOSPITAL pool, carrying the business order of "
                   "stages.",
         "draw": sym_sequence},
        {"title": "Lane", "count": "3 lanes",
         "detail": "Clinical team, Administration and Finance — the same three "
                   "responsibility areas as the operational model.",
         "draw": sym_lane},
        {"title": "Pool / participant", "count": "7 participants",
         "detail": "HOSPITAL plus six black-box participants: referrer, patient, "
                   "scheduler, care services, funder and payment provider.",
         "draw": sym_pool},
        {"title": "Text annotation", "count": "1 occurrence",
         "detail": "The strategic-model note reproduced on the next page.",
         "draw": sym_annotation},
        {"title": "Black-box pool", "count": "6 external participants",
         "detail": "Referrer, patient, scheduler, care services, funder and payment "
                   "provider have no internal process: only message flows cross into them.",
         "draw": sym_pool},
        {"title": "What this model leaves out", "count": "by design",
         "detail": "No forms, assignees, job types, timers or conditions — those live in "
                   "the executable operational model, not here.",
         "draw": sym_absence},
    ]
    return {
        "key": "strategic",
        "bpmn": ROOT / "docs/strategic-bpmn/PB-12_strategic-process_2026-09-29.bpmn",
        "out": ROOT / "submissions/BPMEA/BPMEA_Strategic_Process_Readable_2026-10-19.pdf",
        "source_display": "docs/strategic-bpmn/PB-12_strategic-process_2026-09-29.bpmn",
        "cover_title": "Hospital patient pathway — strategic BPMN",
        "cover_subtitle": "Readable PDF export  ·  non-executable strategic model (PB-12)",
        "title": "Strategic BPMN (PB-12)",
        "short": "Strategic BPMN",
        "pdf_title": "Hospital pathway — strategic BPMN (PB-12) — readable export (B-5)",
        "notes_title": "Strategic model note",
        "render_scale": 3,
        "scale": 0.815,
        "columns": [(70, 1330), (1330, 2710)],
        "rows": [(30, 760), (760, 1300)],
        "row_labels": ["Pools, Clinical team and Administration lanes",
                       "Finance lane, patient pool and model note"],
        "legend": legend,
        "job_table": None,
    }


def prepare_text_blocks(cfg, facts):
    if cfg["key"] == "operational":
        blocks = []
        for ann in facts["annotations"]:
            text = ann["text"].strip()
            if ann["id"] in ("Guide_Main", "Guide_Rules") and text:
                heading = text.split("|")[0].strip().title()
                blocks.append((heading, text))
        cfg["notes"] = blocks
        cfg["job_table"] = facts["job_types"]
    else:
        blocks = []
        for ann in facts["annotations"]:
            text = ann["text"].strip()
            if text:
                blocks.append(("Note on the strategic model", text))
        cfg["notes"] = blocks


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", choices=["operational", "strategic"],
                        help="render only one model")
    parser.add_argument("--work-dir", type=Path,
                        help="keep intermediate PNGs in this directory")
    args = parser.parse_args()

    register_fonts()
    workdir = args.work_dir or Path(tempfile.mkdtemp(prefix="b5_bpmn_"))
    workdir.mkdir(parents=True, exist_ok=True)
    keep = args.work_dir is not None
    print(f"work dir: {workdir}")

    configs = [config_operational(), config_strategic()]
    if args.only:
        configs = [c for c in configs if c["key"] == args.only]

    try:
        for cfg in configs:
            print(f"[{cfg['key']}] {cfg['bpmn']}")
            facts = read_model(cfg["bpmn"])
            prepare_text_blocks(cfg, facts)
            build(cfg, workdir, args.only)
    finally:
        if not keep:
            shutil.rmtree(workdir, ignore_errors=True)


if __name__ == "__main__":
    main()

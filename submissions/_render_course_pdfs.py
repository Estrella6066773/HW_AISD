"""Render the three submitted Markdown reports to readable, searchable PDFs."""

from __future__ import annotations

import html
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parent
pdfmetrics.registerFont(TTFont("YaHei", r"C:\Windows\Fonts\msyh.ttc", subfontIndex=0))
pdfmetrics.registerFont(TTFont("YaHeiBold", r"C:\Windows\Fonts\msyhbd.ttc", subfontIndex=0))
NAVY = colors.HexColor("#17324D")
BLUE = colors.HexColor("#285A81")
GREY = colors.HexColor("#52606D")
LIGHT = colors.HexColor("#EEF4F8")


def style(name: str, size: float, leading: float, *, before=0, after=0, color=NAVY, font="YaHei"):
    return ParagraphStyle(
        name,
        fontName=font,
        fontSize=size,
        leading=leading,
        textColor=color,
        alignment=TA_LEFT,
        spaceBefore=before,
        spaceAfter=after,
        wordWrap="CJK",
        allowWidows=0,
        allowOrphans=0,
    )


ST = {
    "title": style("title", 18, 26, after=13, font="YaHeiBold"),
    "h2": style("h2", 12.5, 19, before=16, after=7, font="YaHeiBold"),
    "h3": style("h3", 10.5, 16, before=12, after=5, font="YaHeiBold"),
    "body": style("body", 9.1, 15.2, after=6),
    "meta": style("meta", 8.8, 14, after=2.5, color=GREY),
    "small": style("small", 8.35, 13.7, after=3),
    "card": style("card", 8.35, 13.8, after=3),
    "cardhead": style("cardhead", 8.7, 14.2, after=5, color=BLUE, font="YaHeiBold"),
}


def markup(raw: str) -> str:
    value = html.escape(raw.strip())
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"\*\*([^*]+)\*\*", r'<font name="YaHeiBold">\1</font>', value)
    value = re.sub(r"`([^`]+)`", r'<font color="#285A81">\1</font>', value)
    return value


def paragraph(raw: str, kind: str = "body") -> Paragraph:
    return Paragraph(markup(raw), ST[kind])


def table_card(headers: list[str], row: list[str]):
    title = row[0] if row else ""
    contents = [paragraph(title, "cardhead")]
    for header, cell in zip(headers[1:], row[1:]):
        contents.append(paragraph(f"**{header}:** {cell}", "card"))
    card = Table([[contents]], colWidths=[A4[0] - 38 * mm], hAlign="LEFT")
    card.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), LIGHT),
                ("BOX", (0, 0), (-1, -1), 0.35, colors.HexColor("#CFDCE6")),
                ("LEFTPADDING", (0, 0), (-1, -1), 9),
                ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    return card


def page_frame(canvas, doc, course: str):
    canvas.saveState()
    width, height = A4
    canvas.setStrokeColor(colors.HexColor("#CCD9E3"))
    canvas.line(19 * mm, height - 18 * mm, width - 19 * mm, height - 18 * mm)
    canvas.setFont("YaHei", 7.5)
    canvas.setFillColor(GREY)
    canvas.drawString(19 * mm, height - 15 * mm, f"{course}  |  Hospital Pathway")
    canvas.drawString(19 * mm, 14 * mm, "Group submission documentation · 29 September 2026")
    canvas.drawRightString(width - 19 * mm, 14 * mm, str(doc.page))
    canvas.restoreState()


def render(md_path: Path, course: str):
    pdf_path = md_path.with_suffix(".pdf")
    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        leftMargin=19 * mm,
        rightMargin=19 * mm,
        topMargin=25 * mm,
        bottomMargin=22 * mm,
        title=md_path.stem.replace("_", " "),
        author="Hospital Pathway Group",
    )
    lines = md_path.read_text(encoding="utf-8").splitlines()
    story = []
    i = 0
    in_metadata = True
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line.startswith("| "):
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append([x.strip() for x in lines[i].strip().strip("|").split("|")])
                i += 1
            headers = block[0]
            for row in block[2:]:
                story.append(table_card(headers, row))
                story.append(Spacer(1, 4))
            story.append(Spacer(1, 3))
            continue
        if line.startswith("# "):
            story.append(paragraph(line[2:], "title"))
            story.append(HRFlowable(width="100%", thickness=1.2, color=BLUE, spaceAfter=8))
        elif line.startswith("## "):
            in_metadata = False
            story.append(paragraph(line[3:], "h2"))
        elif line.startswith("### "):
            story.append(paragraph(line[4:], "h3"))
        elif re.match(r"^\d+\.\s", line):
            story.append(paragraph(line, "body"))
        elif line.startswith("- "):
            story.append(paragraph("• " + line[2:], "body"))
        elif in_metadata:
            story.append(paragraph(line.rstrip("  "), "meta"))
        else:
            parts = [line.rstrip("  ")]
            while i + 1 < len(lines) and lines[i + 1].strip() and not re.match(r"^(#|\||- |\d+\. )", lines[i + 1].strip()):
                i += 1
                parts.append(lines[i].strip().rstrip("  "))
            story.append(paragraph(" ".join(parts), "meta" if in_metadata else "body"))
        i += 1
    frame = lambda canvas, doc: page_frame(canvas, doc, course)
    doc.build(story, onFirstPage=frame, onLaterPages=frame)
    print(f"{pdf_path} | {pdf_path.stat().st_size} bytes")


if __name__ == "__main__":
    render(ROOT / "AISD" / "Group_Design_Decisions_2026-09-29.md", "AISD")
    render(ROOT / "AISD" / "Group_Acceptance_Test_Plan_and_Results_2026-09-29.md", "AISD")
    render(ROOT / "BPMEA" / "Group_Project_and_Test_Plan_2026-09-29.md", "BPM&EA")

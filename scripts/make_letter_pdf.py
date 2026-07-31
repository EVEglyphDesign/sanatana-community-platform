#!/usr/bin/env python3
"""
Bilingual letter PDF — Prasad to the Austin Hindu Temple office.

Content lives in scripts/letter_content.py; this file is layout only.
EVEglyphDesign canon: cream ground, one accent orange, Fraunces display, Inter
body, Noto Sans Telugu with HarfBuzz shaping for the Telugu page.

Three passes: discover the page count, stamp it, stamp the content hash.
"""

from __future__ import annotations
import hashlib
import sys
from datetime import datetime, timezone
from pathlib import Path

from fpdf import FPDF
from fpdf.enums import XPos, YPos

sys.path.insert(0, str(Path(__file__).resolve().parent))
from letter_content import EN, TE, PAGE_URL, GAME_URL  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / ".fonts"
OUT = ROOT / "EVEglyphDesign_Temple_Office_Letter.pdf"

CREAM = (253, 250, 244)
CREAM2 = (247, 242, 231)
INK = (26, 26, 26)
LINE = (231, 225, 211)
MUTE = (107, 102, 92)
ACCENT = (232, 119, 34)
LINKC = (184, 86, 15)

TS = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DOC_ID = "EgD-SCP-002"
KEY_ID = "EgD-KEY-2026-07"


class Letter(FPDF):
    def __init__(self, total_pages, content_hash):
        super().__init__(format="letter", unit="mm")
        self.total_pages = total_pages
        self.content_hash = content_hash
        self.set_auto_page_break(True, margin=22)
        self.set_margins(24, 24, 24)
        self.add_font("Fraunces", "", str(FONTS / "Fraunces.ttf"))
        self.add_font("Inter", "", str(FONTS / "Inter.ttf"))
        self.add_font("Telugu", "", str(FONTS / "NotoSansTelugu.ttf"))
        self.set_text_shaping(True)
        self.set_title("EVEglyphDesign — Temple Office Letter")
        self.set_author("EVEglyphDesign")

    def header(self):
        w, h = self.w, self.h
        self.set_fill_color(*CREAM)
        self.rect(0, 0, w, h, style="F")
        with self.local_context(fill_opacity=0.05, text_color=ACCENT):
            self.set_font("Fraunces", size=46)
            with self.rotation(38, w / 2, h / 2):
                self.set_xy(0, h / 2 - 8)
                self.cell(w, 16, "EVEglyphDesign", align="C")
        self.set_draw_color(*ACCENT)
        self.set_line_width(0.7)
        self.line(24, 15.5, w - 24, 15.5)
        self.set_font("Fraunces", size=8)
        self.set_text_color(*MUTE)
        self.set_xy(24, 9.5)
        self.cell(60, 5, "EVEglyphDesign \u00b7 Controlled copy")
        self.set_xy(w - 84, 9.5)
        self.cell(60, 5, DOC_ID, align="R")
        self.set_xy(24, 23)
        self.set_text_color(*INK)

    def footer(self):
        self.set_draw_color(*LINE)
        self.set_line_width(0.25)
        self.line(24, self.h - 20, self.w - 24, self.h - 20)
        self.set_font("Inter", size=6.8)
        self.set_text_color(*MUTE)
        self.set_xy(24, self.h - 18)
        self.multi_cell(112, 3.6,
                        "\u00a9 2026 EVEglyphDesign. All rights reserved. Community content "
                        f"belongs to the community. Key ID {KEY_ID} \u00b7 {TS}\n"
                        f"SHA-256 {self.content_hash}", align="L")
        self.set_xy(self.w - 84, self.h - 18)
        self.cell(60, 3.6, f"Page {self.page_no()} of {self.total_pages}", align="R")

    # ---- blocks ----
    def titleblock(self, text, kicker, font="Fraunces", size=19):
        self.set_font(font, size=size)
        self.set_text_color(*INK)
        self.multi_cell(0, size * 0.44, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1.2)
        self.set_font("Inter", size=8.6)
        self.set_text_color(*MUTE)
        self.multi_cell(0, 4, kicker, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(3)

    def subject_bar(self, text, font="Inter", size=8.9, lead=5.0):
        self.set_fill_color(*CREAM2)
        self.set_draw_color(*ACCENT)
        self.set_line_width(0.5)
        y = self.get_y()
        self.set_font(font, size=size)
        self.set_text_color(*INK)
        self.multi_cell(0, lead, text, fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.line(24, y, self.w - 24, y)
        self.ln(2.6)

    def h2(self, text, font="Fraunces", size=10.2):
        self.ln(1.8)
        self.set_font(font, size=size)
        self.set_text_color(*LINKC)
        self.multi_cell(0, size * 0.46, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(0.6)

    def body(self, text, font="Inter", size=8.7, color=INK, lead=4.0, gap=1.0):
        if not text:
            return
        self.set_font(font, size=size)
        self.set_text_color(*color)
        self.multi_cell(0, lead, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(gap)

    def bullet(self, text, font="Inter", size=8.6, lead=4.0):
        x0 = self.l_margin
        self.set_x(x0)
        self.set_font(font, size=size)
        self.set_text_color(*ACCENT)
        self.cell(4.5, lead, "\u2022")
        self.set_text_color(*INK)
        self.multi_cell(self.w - self.r_margin - (x0 + 4.5), lead, text,
                        new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(0.9)

    def link_line(self, label, url):
        self.set_font("Inter", size=8.8)
        self.set_text_color(*LINKC)
        self.multi_cell(0, 4.2, f"{label}: {url}", new_x=XPos.LMARGIN, new_y=YPos.NEXT,
                        link=url, align="L")
        self.ln(0.8)


def render(total_pages, content_hash):
    pdf = Letter(total_pages, content_hash)

    # ---------------- English ----------------
    pdf.add_page()
    pdf.titleblock(EN["title"], EN["kicker"], size=17)
    pdf.subject_bar(EN["subject"])
    pdf.body(EN["open"])
    pdf.body(EN["intro"])
    for head, intro, items, tail in EN["sections"]:
        pdf.h2(head)
        pdf.body(intro)
        for it in items:
            pdf.bullet(it)
        if items:
            pdf.ln(0.8)
        pdf.body(tail)
    pdf.h2(EN["closing_head"])
    pdf.body(EN["closing"])
    pdf.body(EN["ask"])
    pdf.h2(EN["links_head"])
    for label, url in EN["links"]:
        pdf.link_line(label, url)
    pdf.ln(1.5)
    pdf.body(EN["thanks"])
    pdf.set_font("Fraunces", size=10.5)
    pdf.set_text_color(*INK)
    pdf.multi_cell(0, 5, EN["sign"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Inter", size=8.6)
    pdf.set_text_color(*MUTE)
    pdf.multi_cell(0, 4.2, EN["contact"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # ---------------- Telugu ----------------
    pdf.add_page()
    pdf.set_font("Telugu", size=15.5)
    pdf.set_text_color(*INK)
    pdf.multi_cell(0, 8, TE["head"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1)
    pdf.body(TE["kicker"], size=8.4, color=MUTE, lead=4, gap=3)
    pdf.subject_bar(TE["subject"], font="Telugu", size=9.1, lead=5.8)
    pdf.body(TE["open"], font="Telugu", size=9.1, lead=5.0)
    pdf.body(TE["intro"], font="Telugu", size=9.1, lead=5.0)
    for head, intro, items, tail in TE["sections"]:
        pdf.h2(head, font="Telugu", size=10.0)
        pdf.body(intro, font="Telugu", size=9.1, lead=5.0)
        for it in items:
            pdf.bullet(it, font="Telugu", size=9.0, lead=4.95)
        if items:
            pdf.ln(0.8)
        pdf.body(tail, font="Telugu", size=9.1, lead=5.0)
    pdf.h2(TE["closing_head"], font="Telugu", size=10.0)
    pdf.body(TE["closing"], font="Telugu", size=9.1, lead=5.0)
    pdf.body(TE["ask"], font="Telugu", size=9.1, lead=5.0)
    pdf.link_line("Game", GAME_URL)
    pdf.link_line("Draft page", PAGE_URL)
    pdf.ln(1)
    pdf.body(TE["thanks"], font="Telugu", size=9.1, lead=5.0)
    pdf.set_font("Telugu", size=10.0)
    pdf.set_text_color(*INK)
    pdf.multi_cell(0, 6, TE["sign"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_auto_page_break(False)
    pdf.set_y(pdf.h - 27)
    pdf.set_x(24)
    pdf.set_font("Fraunces", size=10)
    pdf.set_text_color(*ACCENT)
    pdf.cell(0, 5, "Pour le bien-\u00eatre du peuple.")

    pdf.output(str(OUT))
    return pdf.page_no()


def main():
    pages = render("\u2014", "pending")
    render(pages, "pending")
    h = hashlib.sha256(OUT.read_bytes()).hexdigest()[:32]
    render(pages, h)
    final = hashlib.sha256(OUT.read_bytes()).hexdigest()
    (ROOT / "registry" / "LETTER-HASH.txt").write_text(
        f"{OUT.name}\nstamped-hash-prefix: {h}\nfile-sha256: {final}\ngenerated: {TS}\n",
        encoding="utf-8")
    print(f"pages={pages} stamped={h} sha256={final}")


if __name__ == "__main__":
    main()

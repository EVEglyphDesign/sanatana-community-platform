#!/usr/bin/env python3
"""
Bilingual letter PDF — Prasad to the Austin Hindu Temple office.

English and Telugu, outline form. EVEglyphDesign canon: cream ground, one accent
orange, Fraunces display, Inter body, Noto Sans Telugu for the Telugu section
with HarfBuzz shaping so conjuncts and vowel signs render correctly.

Two passes: pass one discovers the page count, pass two stamps it and the hash.
"""

from __future__ import annotations
import hashlib
from datetime import datetime, timezone
from pathlib import Path

from fpdf import FPDF
from fpdf.enums import XPos, YPos

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
PAGE_URL = "https://eveglyphdesign.github.io/sanatana-community-platform/austin-hindu-temple/"

EN = {
    "subject": "Subject:  Volunteering to run the temple's web presence",
    "open": "Namaste,",
    "intro": ("My name is Prasad. I am a member of this temple community and I work in "
              "enterprise systems. I would like to volunteer for the part of temple work "
              "that is hardest to staff."),
    "offer_head": "What I would take off the office's hands",
    "offer": [
        ("The website, maintained automatically.",
         "Not a volunteer remembering to update a page. Hours, festivals and class times stay "
         "current on their own."),
        ("A GitHub repository the temple owns.",
         "I build it and hand it over. No subscription, no vendor, no login. The temple can "
         "carry it to any host, with or without me."),
        ("A record that can be checked.",
         "Every fact traced to its source. Corrections dated and added, never silently "
         "overwritten."),
        ("Whatever is useful after that.",
         "Festival dates that drop into a phone calendar, class sign-ups, a newsletter archive, "
         "a youth education section."),
    ],
    "draft_head": "A working draft is already up",
    "draft": ("Everything on it comes from the temple's own website and documents, and every "
              "page links back to austinhindutemple.org. It is not an official temple site and "
              "I am not asking it to become one."),
    "open_head": "Five fields I left blank rather than guess",
    "open_fields": [
        "The deities, in the order the temple would list them.",
        "Whether the class schedule is current, and who teaches each class today. Teacher names "
        "are withheld until each teacher agrees.",
        "The board and trustees for this term.",
        "This year's festival calendar.",
        "Opening hours — two pages on the temple site disagree.",
    ],
    "close": ("Correct anything, or tell me to take it down, and it is done the same day."),
    "thanks": "Thank you for your time and your seva.",
    "sign": "Prasad",
    "contact": "[phone]  \u00b7  [email]",
}

TE = {
    "head": "\u0c24\u0c46\u0c32\u0c41\u0c17\u0c41 \u0c2a\u0c4d\u0c30\u0c24\u0c3f",
    "subject": "\u0c35\u0c3f\u0c37\u0c2f\u0c02:  \u0c06\u0c32\u0c2f \u0c35\u0c46\u0c2c\u0c4d\u200c\u0c38\u0c48\u0c1f\u0c4d \u0c28\u0c3f\u0c30\u0c4d\u0c35\u0c39\u0c23 \u0c15\u0c4b\u0c38\u0c02 \u0c38\u0c4d\u0c35\u0c1a\u0c4d\u0c1b\u0c02\u0c26 \u0c38\u0c47\u0c35",
    "open": "\u0c28\u0c2e\u0c38\u0c4d\u0c24\u0c47,",
    "intro": ("\u0c28\u0c3e \u0c2a\u0c47\u0c30\u0c41 \u0c2a\u0c4d\u0c30\u0c38\u0c3e\u0c26\u0c4d. \u0c28\u0c47\u0c28\u0c41 \u0c08 \u0c06\u0c32\u0c2f \u0c38\u0c2e\u0c41\u0c26\u0c3e\u0c2f\u0c02\u0c32\u0c4b \u0c38\u0c2d\u0c4d\u0c2f\u0c41\u0c21\u0c3f\u0c28\u0c3f, "
              "\u0c0e\u0c02\u0c1f\u0c30\u0c4d\u200c\u0c2a\u0c4d\u0c30\u0c48\u0c1c\u0c4d \u0c38\u0c3f\u0c38\u0c4d\u0c1f\u0c2e\u0c4d\u0c38\u0c4d \u0c30\u0c02\u0c17\u0c02\u0c32\u0c4b \u0c2a\u0c28\u0c3f\u0c1a\u0c47\u0c38\u0c4d\u0c24\u0c3e\u0c28\u0c41. "
              "\u0c06\u0c32\u0c2f \u0c2a\u0c28\u0c41\u0c32\u0c4d\u0c32\u0c4b \u0c0e\u0c35\u0c30\u0c3f\u0c15\u0c40 \u0c15\u0c41\u0c26\u0c30\u0c28\u0c3f \u0c2d\u0c3e\u0c17\u0c3e\u0c28\u0c4d\u0c28\u0c3f "
              "\u0c38\u0c4d\u0c35\u0c1a\u0c4d\u0c1b\u0c02\u0c26\u0c02\u0c17\u0c3e \u0c1a\u0c47\u0c2f\u0c17\u0c32\u0c28\u0c41."),
    "offer_head": "\u0c28\u0c47\u0c28\u0c41 \u0c1a\u0c47\u0c2f\u0c17\u0c32\u0c3f\u0c28\u0c35\u0c3f",
    "offer": [
        ("\u0c35\u0c46\u0c2c\u0c4d\u0c38\u0c48\u0c1f\u0c4d \u0c28\u0c3f\u0c30\u0c4d\u0c35\u0c39\u0c23, \u0c06\u0c1f\u0c4b\u0c2e\u0c47\u0c1f\u0c3f\u0c15\u0c4d\u200c\u0c17\u0c3e.",
         "\u0c0e\u0c35\u0c30\u0c4b \u0c12\u0c15\u0c30\u0c41 \u0c17\u0c41\u0c30\u0c4d\u0c24\u0c41\u0c1a\u0c47\u0c38\u0c41\u0c15\u0c41\u0c28\u0c3f \u0c2a\u0c47\u0c1c\u0c40\u0c28\u0c3f \u0c2e\u0c3e\u0c30\u0c4d\u0c1a\u0c35\u0c32\u0c38\u0c3f\u0c28 \u0c05\u0c35\u0c38\u0c30\u0c02 \u0c32\u0c47\u0c26\u0c41. "
         "\u0c38\u0c2e\u0c2f\u0c3e\u0c32\u0c41, \u0c2a\u0c02\u0c21\u0c41\u0c17\u0c32\u0c41, \u0c24\u0c30\u0c17\u0c24\u0c41\u0c32 \u0c35\u0c3f\u0c35\u0c30\u0c3e\u0c32\u0c41 \u0c24\u0c3e\u0c2e\u0c47 \u0c28\u0c35\u0c40\u0c15\u0c30\u0c23 \u0c05\u0c35\u0c41\u0c24\u0c3e\u0c2f\u0c3f."),
        ("\u0c06\u0c32\u0c2f\u0c3e\u0c28\u0c3f\u0c15\u0c47 \u0c38\u0c4d\u0c35\u0c02\u0c24\u0c2e\u0c48\u0c28 GitHub \u0c30\u0c3f\u0c2a\u0c4b\u0c1c\u0c3f\u0c1f\u0c30\u0c40.",
         "\u0c28\u0c47\u0c28\u0c41 \u0c26\u0c3e\u0c28\u0c4d\u0c28\u0c3f \u0c28\u0c3f\u0c30\u0c4d\u0c2e\u0c3f\u0c02\u0c1a\u0c3f \u0c06\u0c32\u0c2f\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c05\u0c2a\u0c4d\u0c2a\u0c17\u0c3f\u0c38\u0c4d\u0c24\u0c3e\u0c28\u0c41. \u0c1a\u0c02\u0c26\u0c3e \u0c32\u0c47\u0c26\u0c41, "
         "\u0c35\u0c46\u0c02\u0c21\u0c30\u0c4d \u0c32\u0c47\u0c26\u0c41, \u0c32\u0c3e\u0c17\u0c3f\u0c28\u0c4d \u0c32\u0c47\u0c26\u0c41. \u0c28\u0c47\u0c28\u0c41 \u0c32\u0c47\u0c15\u0c2a\u0c4b\u0c2f\u0c3f\u0c28\u0c3e \u0c06\u0c32\u0c2f\u0c02 \u0c26\u0c3e\u0c28\u0c4d\u0c28\u0c3f "
         "\u0c0e\u0c15\u0c4d\u0c15\u0c21\u0c3f\u0c15\u0c48\u0c28\u0c3e \u0c24\u0c40\u0c38\u0c41\u0c15\u0c46\u0c33\u0c4d\u0c32\u0c17\u0c32\u0c26\u0c41."),
        ("\u0c38\u0c30\u0c3f\u0c1a\u0c42\u0c21\u0c17\u0c32 \u0c30\u0c3f\u0c15\u0c3e\u0c30\u0c4d\u0c21\u0c41.",
         "\u0c2a\u0c4d\u0c30\u0c24\u0c3f \u0c35\u0c3f\u0c37\u0c2f\u0c02 \u0c26\u0c3e\u0c28\u0c3f \u0c2e\u0c42\u0c32\u0c02\u0c24\u0c4b \u0c15\u0c32\u0c3f\u0c2a\u0c3f \u0c09\u0c02\u0c1f\u0c41\u0c02\u0c26\u0c3f. \u0c38\u0c30\u0c3f\u0c26\u0c3f\u0c26\u0c4d\u0c26\u0c41\u0c32\u0c41 \u0c24\u0c47\u0c26\u0c40\u0c24\u0c4b "
         "\u0c1a\u0c47\u0c30\u0c4d\u0c1a\u0c2c\u0c21\u0c24\u0c3e\u0c2f\u0c3f, \u0c0e\u0c2a\u0c4d\u0c2a\u0c41\u0c21\u0c42 \u0c28\u0c3f\u0c36\u0c4d\u0c36\u0c2c\u0c4d\u0c26\u0c02\u0c17\u0c3e \u0c2e\u0c3e\u0c30\u0c4d\u0c1a\u0c2c\u0c21\u0c35\u0c41."),
        ("\u0c06 \u0c24\u0c30\u0c41\u0c35\u0c3e\u0c24 \u0c09\u0c2a\u0c2f\u0c4b\u0c17\u0c2a\u0c21\u0c47\u0c35\u0c40.",
         "\u0c2b\u0c4b\u0c28\u0c4d \u0c15\u0c4d\u0c2f\u0c3e\u0c32\u0c46\u0c02\u0c21\u0c30\u0c4d\u200c\u0c32\u0c4b \u0c2a\u0c02\u0c21\u0c41\u0c17 \u0c24\u0c47\u0c26\u0c40\u0c32\u0c41, \u0c24\u0c30\u0c17\u0c24\u0c41\u0c32 \u0c28\u0c2e\u0c4b\u0c26\u0c41, "
         "\u0c35\u0c3e\u0c30\u0c4d\u0c24\u0c3e\u0c32\u0c47\u0c16\u0c28\u0c3e\u0c32 \u0c38\u0c02\u0c17\u0c4d\u0c30\u0c39\u0c02, \u0c2a\u0c3f\u0c32\u0c4d\u0c32\u0c32 \u0c35\u0c3f\u0c26\u0c4d\u0c2f\u0c3e \u0c35\u0c3f\u0c2d\u0c3e\u0c17\u0c02."),
    ],
    "draft_head": "\u0c12\u0c15 \u0c21\u0c4d\u0c30\u0c3e\u0c2b\u0c4d\u0c1f\u0c4d \u0c07\u0c2a\u0c4d\u0c2a\u0c1f\u0c3f\u0c15\u0c47 \u0c38\u0c3f\u0c26\u0c4d\u0c27\u0c02\u0c17\u0c3e \u0c09\u0c02\u0c26\u0c3f",
    "draft": ("\u0c05\u0c02\u0c26\u0c41\u0c32\u0c4b\u0c28\u0c3f \u0c2a\u0c4d\u0c30\u0c24\u0c3f \u0c35\u0c3f\u0c37\u0c2f\u0c02 \u0c06\u0c32\u0c2f\u0c02 \u0c38\u0c4d\u0c35\u0c02\u0c24 \u0c35\u0c46\u0c2c\u0c4d\u200c\u0c38\u0c48\u0c1f\u0c4d, \u0c2a\u0c24\u0c4d\u0c30\u0c3e\u0c32 "
              "\u0c28\u0c41\u0c02\u0c21\u0c47 \u0c24\u0c40\u0c38\u0c41\u0c15\u0c41\u0c28\u0c4d\u0c28\u0c26\u0c47. \u0c07\u0c26\u0c3f \u0c05\u0c27\u0c3f\u0c15\u0c3e\u0c30\u0c3f\u0c15 \u0c06\u0c32\u0c2f \u0c38\u0c48\u0c1f\u0c4d \u0c15\u0c3e\u0c26\u0c41, "
              "\u0c05\u0c32\u0c3e \u0c15\u0c3e\u0c35\u0c3e\u0c32\u0c28\u0c3f \u0c28\u0c47\u0c28\u0c41 \u0c15\u0c4b\u0c30\u0c21\u0c02 \u0c32\u0c47\u0c26\u0c41."),
    "open_head": "\u0c0a\u0c39\u0c3f\u0c02\u0c1a\u0c15\u0c41\u0c02\u0c21\u0c3e \u0c16\u0c3e\u0c33\u0c40\u0c17\u0c3e \u0c35\u0c26\u0c3f\u0c32\u0c3f\u0c28 \u0c10\u0c26\u0c41 \u0c35\u0c3f\u0c37\u0c2f\u0c3e\u0c32\u0c41",
    "open_fields": [
        "\u0c06\u0c32\u0c2f\u0c02\u0c32\u0c4b\u0c28\u0c3f \u0c26\u0c47\u0c35\u0c24\u0c32\u0c41, \u0c06\u0c32\u0c2f\u0c02 \u0c1a\u0c46\u0c2a\u0c4d\u0c2a\u0c47 \u0c15\u0c4d\u0c30\u0c2e\u0c02\u0c32\u0c4b.",
        "\u0c24\u0c30\u0c17\u0c24\u0c41\u0c32 \u0c37\u0c46\u0c21\u0c4d\u0c2f\u0c42\u0c32\u0c4d \u0c2a\u0c4d\u0c30\u0c38\u0c4d\u0c24\u0c41\u0c24\u0c02 \u0c38\u0c30\u0c48\u0c28\u0c26\u0c47\u0c28\u0c3e, \u0c07\u0c2a\u0c4d\u0c2a\u0c41\u0c21\u0c41 \u0c0f "
        "\u0c24\u0c30\u0c17\u0c24\u0c3f\u0c28\u0c3f \u0c0e\u0c35\u0c30\u0c41 \u0c2c\u0c4b\u0c27\u0c3f\u0c38\u0c4d\u0c24\u0c41\u0c28\u0c4d\u0c28\u0c3e\u0c30\u0c41. \u0c09\u0c2a\u0c3e\u0c27\u0c4d\u0c2f\u0c3e\u0c2f\u0c41\u0c32 \u0c2a\u0c47\u0c30\u0c4d\u0c32\u0c41 "
        "\u0c35\u0c3e\u0c30\u0c3f \u0c05\u0c02\u0c17\u0c40\u0c15\u0c3e\u0c30\u0c02 \u0c35\u0c1a\u0c4d\u0c1a\u0c47\u0c35\u0c30\u0c15\u0c41 \u0c1a\u0c47\u0c30\u0c4d\u0c1a\u0c32\u0c47\u0c26\u0c41.",
        "\u0c08 \u0c15\u0c3e\u0c32\u0c3e\u0c28\u0c3f\u0c15\u0c3f \u0c2c\u0c4b\u0c30\u0c4d\u0c21\u0c41 \u0c38\u0c2d\u0c4d\u0c2f\u0c41\u0c32\u0c41, \u0c27\u0c30\u0c4d\u0c2e\u0c15\u0c30\u0c4d\u0c24\u0c32\u0c41.",
        "\u0c08 \u0c38\u0c02\u0c35\u0c24\u0c4d\u0c38\u0c30\u0c2a\u0c41 \u0c2a\u0c02\u0c21\u0c41\u0c17\u0c32 \u0c15\u0c4d\u0c2f\u0c3e\u0c32\u0c46\u0c02\u0c21\u0c30\u0c4d.",
        "\u0c26\u0c30\u0c4d\u0c36\u0c28 \u0c38\u0c2e\u0c2f\u0c3e\u0c32\u0c41 \u2014 \u0c06\u0c32\u0c2f \u0c38\u0c48\u0c1f\u0c4d\u200c\u0c32\u0c4b\u0c28\u0c3f \u0c30\u0c46\u0c02\u0c21\u0c41 \u0c2a\u0c47\u0c1c\u0c40\u0c32\u0c4d\u0c32\u0c4b "
        "\u0c35\u0c47\u0c30\u0c4d\u0c35\u0c47\u0c30\u0c41 \u0c38\u0c2e\u0c2f\u0c3e\u0c32\u0c41 \u0c09\u0c28\u0c4d\u0c28\u0c3e\u0c2f\u0c3f.",
    ],
    "close": ("\u0c0f\u0c26\u0c48\u0c28\u0c3e \u0c24\u0c2a\u0c4d\u0c2a\u0c41 \u0c09\u0c02\u0c1f\u0c47 \u0c1a\u0c46\u0c2a\u0c4d\u0c2a\u0c02\u0c21\u0c3f, \u0c32\u0c47\u0c26\u0c3e \u0c24\u0c4a\u0c32\u0c17\u0c3f\u0c02\u0c1a\u0c2e\u0c28\u0c02\u0c21\u0c3f \u2014 "
              "\u0c05\u0c26\u0c47 \u0c30\u0c4b\u0c1c\u0c41 \u0c1a\u0c47\u0c38\u0c4d\u0c24\u0c3e\u0c28\u0c41."),
    "thanks": "\u0c2e\u0c40 \u0c38\u0c2e\u0c2f\u0c3e\u0c28\u0c3f\u0c15\u0c3f, \u0c2e\u0c40 \u0c38\u0c47\u0c35\u0c15\u0c41 \u0c27\u0c28\u0c4d\u0c2f\u0c35\u0c3e\u0c26\u0c3e\u0c32\u0c41.",
    "sign": "\u0c2a\u0c4d\u0c30\u0c38\u0c3e\u0c26\u0c4d",
}


class Letter(FPDF):
    def __init__(self, total_pages, content_hash):
        super().__init__(format="letter", unit="mm")
        self.total_pages = total_pages
        self.content_hash = content_hash
        self.set_auto_page_break(True, margin=26)
        self.set_margins(24, 26, 24)
        self.add_font("Fraunces", "", str(FONTS / "Fraunces.ttf"))
        self.add_font("Inter", "", str(FONTS / "Inter.ttf"))
        self.add_font("Telugu", "", str(FONTS / "NotoSansTelugu.ttf"))
        self.set_text_shaping(True)
        self.set_title("EVEglyphDesign — Temple Office Letter")
        self.set_author("EVEglyphDesign")

    # --- furniture -------------------------------------------------------
    def header(self):
        w, h = self.w, self.h
        self.set_fill_color(*CREAM)
        self.rect(0, 0, w, h, style="F")
        # watermark
        with self.local_context(fill_opacity=0.05, text_color=ACCENT):
            self.set_font("Fraunces", size=46)
            with self.rotation(38, w / 2, h / 2):
                self.set_xy(0, h / 2 - 8)
                self.cell(w, 16, "EVEglyphDesign", align="C")
        self.set_draw_color(*ACCENT)
        self.set_line_width(0.7)
        self.line(24, 17, w - 24, 17)
        self.set_font("Fraunces", size=8)
        self.set_text_color(*MUTE)
        self.set_xy(24, 11)
        self.cell(60, 5, "EVEglyphDesign \u00b7 Controlled copy")
        self.set_xy(w - 84, 11)
        self.cell(60, 5, DOC_ID, align="R")
        self.set_xy(24, 26)
        self.set_text_color(*INK)

    def footer(self):
        self.set_y(-20)
        self.set_draw_color(*LINE)
        self.set_line_width(0.25)
        self.line(24, self.h - 20, self.w - 24, self.h - 20)
        self.set_font("Inter", size=6.8)
        self.set_text_color(*MUTE)
        self.set_xy(24, self.h - 18)
        self.multi_cell(110, 3.6,
                        "\u00a9 2026 EVEglyphDesign. All rights reserved. Community content "
                        f"belongs to the community. Key ID {KEY_ID} \u00b7 {TS}\n"
                        f"SHA-256 {self.content_hash}", align="L")
        self.set_xy(self.w - 84, self.h - 18)
        self.cell(60, 3.6, f"Page {self.page_no()} of {self.total_pages}", align="R")

    # --- blocks ----------------------------------------------------------
    def h1(self, text, font="Fraunces", size=19):
        self.set_font(font, size=size)
        self.set_text_color(*INK)
        self.multi_cell(0, size * 0.42, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)

    def h2(self, text, font="Fraunces", size=11.5):
        self.ln(3)
        self.set_font(font, size=size)
        self.set_text_color(*LINKC)
        self.multi_cell(0, size * 0.45, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1.2)

    def body(self, text, font="Inter", size=9.6, color=INK, lead=4.6):
        self.set_font(font, size=size)
        self.set_text_color(*color)
        self.multi_cell(0, lead, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1.6)

    def bullet(self, lead_text, rest, font="Inter", size=9.6):
        x0 = self.get_x()
        self.set_font(font, size=size)
        self.set_text_color(*ACCENT)
        self.cell(4.5, 4.6, "\u2022")
        self.set_text_color(*INK)
        avail = self.w - 24 - (x0 + 4.5)
        if rest:
            self.multi_cell(avail, 4.6, lead_text, new_x=XPos.LMARGIN, new_y=YPos.NEXT,
                            markdown=False)
            self.set_x(x0 + 4.5)
            self.set_text_color(*MUTE)
            self.multi_cell(avail, 4.6, rest, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        else:
            self.multi_cell(avail, 4.6, lead_text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1.4)

    def subject_bar(self, text, font="Inter"):
        self.set_fill_color(*CREAM2)
        self.set_draw_color(*ACCENT)
        self.set_line_width(0.5)
        y = self.get_y()
        self.set_font(font, size=9.4)
        self.set_text_color(*INK)
        self.multi_cell(0, 6.4, text, fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.line(24, y, self.w - 24, y)
        self.ln(4)


def render(total_pages, content_hash):
    pdf = Letter(total_pages, content_hash)

    # ---------------- English -------------------------------------------
    pdf.add_page()
    pdf.h1("A letter to the temple office")
    pdf.body("Draft for Prasad to send. Austin Hindu Temple & Community Center, Austin, Texas.",
             size=9, color=MUTE)
    pdf.ln(1)
    pdf.subject_bar(EN["subject"])
    pdf.body(EN["open"])
    pdf.body(EN["intro"])
    pdf.h2(EN["offer_head"])
    for lead_text, rest in EN["offer"]:
        pdf.bullet(lead_text, rest)
    pdf.h2(EN["draft_head"])
    pdf.body(EN["draft"])
    pdf.set_font("Inter", size=9.2)
    pdf.set_text_color(*LINKC)
    pdf.multi_cell(0, 4.6, PAGE_URL, new_x=XPos.LMARGIN, new_y=YPos.NEXT,
                   link=PAGE_URL)
    pdf.ln(2)
    pdf.h2(EN["open_head"])
    for f in EN["open_fields"]:
        pdf.bullet(f, "")
    pdf.body(EN["close"])
    pdf.body(EN["thanks"])
    pdf.ln(1)
    pdf.set_font("Fraunces", size=10.5)
    pdf.set_text_color(*INK)
    pdf.multi_cell(0, 5, EN["sign"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Inter", size=8.6)
    pdf.set_text_color(*MUTE)
    pdf.multi_cell(0, 4.2, EN["contact"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # ---------------- Telugu ---------------------------------------------
    pdf.add_page()
    pdf.h1(TE["head"], font="Telugu", size=17)
    pdf.body("Telugu version of the same letter. Send it below the English text in the same "
             "email. A native speaker should read it once before it goes out.",
             size=8.6, color=MUTE)
    pdf.ln(1)
    pdf.subject_bar(TE["subject"], font="Telugu")
    pdf.body(TE["open"], font="Telugu", size=10, lead=5.6)
    pdf.body(TE["intro"], font="Telugu", size=10, lead=5.6)
    pdf.h2(TE["offer_head"], font="Telugu", size=11.5)
    for lead_text, rest in TE["offer"]:
        x0 = pdf.get_x()
        pdf.set_font("Telugu", size=10)
        pdf.set_text_color(*ACCENT)
        pdf.cell(4.5, 5.6, "\u2022")
        pdf.set_text_color(*INK)
        avail = pdf.w - 24 - (x0 + 4.5)
        pdf.multi_cell(avail, 5.6, lead_text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_x(x0 + 4.5)
        pdf.set_text_color(*MUTE)
        pdf.multi_cell(avail, 5.6, rest, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(1.4)
    pdf.h2(TE["draft_head"], font="Telugu", size=11.5)
    pdf.body(TE["draft"], font="Telugu", size=10, lead=5.6)
    pdf.set_font("Inter", size=9.2)
    pdf.set_text_color(*LINKC)
    pdf.multi_cell(0, 4.6, PAGE_URL, new_x=XPos.LMARGIN, new_y=YPos.NEXT, link=PAGE_URL)
    pdf.ln(2)
    pdf.h2(TE["open_head"], font="Telugu", size=11.5)
    for f in TE["open_fields"]:
        x0 = pdf.get_x()
        pdf.set_font("Telugu", size=10)
        pdf.set_text_color(*ACCENT)
        pdf.cell(4.5, 5.6, "\u2022")
        pdf.set_text_color(*INK)
        pdf.multi_cell(pdf.w - 24 - (x0 + 4.5), 5.6, f,
                       new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(1.2)
    pdf.body(TE["close"], font="Telugu", size=10, lead=5.6)
    pdf.body(TE["thanks"], font="Telugu", size=10, lead=5.6)
    pdf.set_font("Telugu", size=11)
    pdf.set_text_color(*INK)
    pdf.multi_cell(0, 6, TE["sign"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_auto_page_break(False)
    pdf.set_y(pdf.h - 31)
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

#!/usr/bin/env python3
"""
Charter PDF generator — Sanatana Community Platform.

Produces EVEglyphDesign_Sanatana_Community_Platform_Charter.pdf in the repository
root, in the EVEglyphDesign canon: cream ground, single accent orange, Fraunces
display, Inter body, watermark, copyright line, SHA-256 content hash, Key ID,
ISO-8601 UTC timestamp, and the closing mark.

Built twice: pass one discovers the page count, pass two stamps it.
"""

from __future__ import annotations
import hashlib
from datetime import datetime, timezone
from pathlib import Path

from reportlab.lib.colors import Color, HexColor
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                               Spacer, Table, TableStyle, KeepTogether)

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / ".fonts"
OUT = ROOT / "EVEglyphDesign_Sanatana_Community_Platform_Charter.pdf"

CREAM = HexColor("#fdfaf4")
CREAM2 = HexColor("#f7f2e7")
INK = HexColor("#1a1a1a")
LINE = HexColor("#e7e1d3")
MUTE = HexColor("#6b665c")
ACCENT = HexColor("#e87722")
LINKC = HexColor("#b8560f")

pdfmetrics.registerFont(TTFont("Fraunces", str(FONTS / "Fraunces.ttf")))
pdfmetrics.registerFont(TTFont("Inter", str(FONTS / "Inter.ttf")))

TS = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
KEY_ID = "EgD-KEY-2026-07"
DOC_ID = "EgD-SCP-001"

H1 = ParagraphStyle("H1", fontName="Fraunces", fontSize=25, leading=29, textColor=INK,
                    spaceAfter=10)
LEAD = ParagraphStyle("LEAD", fontName="Inter", fontSize=11.5, leading=17, textColor=MUTE,
                      spaceAfter=16)
H2 = ParagraphStyle("H2", fontName="Fraunces", fontSize=15, leading=19, textColor=INK,
                    spaceBefore=16, spaceAfter=6)
H3 = ParagraphStyle("H3", fontName="Fraunces", fontSize=12, leading=16, textColor=LINKC,
                    spaceBefore=10, spaceAfter=3)
BODY = ParagraphStyle("BODY", fontName="Inter", fontSize=10, leading=15.4, textColor=INK,
                      alignment=TA_JUSTIFY, spaceAfter=8)
BULLET = ParagraphStyle("BULLET", parent=BODY, leftIndent=14, bulletIndent=3,
                        spaceAfter=4, alignment=0)
SMALL = ParagraphStyle("SMALL", fontName="Inter", fontSize=8.4, leading=12, textColor=MUTE,
                       spaceAfter=6)
CELL = ParagraphStyle("CELL", fontName="Inter", fontSize=9, leading=13, textColor=INK)
CELLH = ParagraphStyle("CELLH", fontName="Fraunces", fontSize=9, leading=13, textColor=INK)
MARK = ParagraphStyle("MARK", fontName="Fraunces", fontSize=10.5, leading=14, textColor=ACCENT,
                      spaceBefore=10)


def link(text: str, url: str) -> str:
    return f'<a href="{url}" color="#b8560f"><u>{text}</u></a>'


def p(t):
    return Paragraph(t, BODY)


def bullets(items):
    return [Paragraph(i, BULLET, bulletText="\u2022") for i in items]


def table(rows, widths):
    data = [[Paragraph(c, CELLH if i == 0 else CELL) for c in row] for i, row in enumerate(rows)]
    t = Table(data, colWidths=widths, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), CREAM2),
        ("LINEBELOW", (0, 0), (-1, -1), 0.5, LINE),
        ("LINEABOVE", (0, 0), (-1, 0), 1.1, ACCENT),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    return t


BASE = "https://eveglyphdesign.github.io/sanatana-community-platform/"
REPO = "https://github.com/EVEglyphDesign/sanatana-community-platform"


def story(total_pages: str, content_hash: str):
    s = []
    s.append(Paragraph("Sanatana Community Platform", H1))
    s.append(Paragraph(
        "Charter and build record for a community-stewarded temple surface &mdash; "
        "reference community: Austin Hindu Temple &amp; Community Center, Austin, Texas. "
        f"Document {DOC_ID}.", LEAD))

    s.append(Paragraph("1 &nbsp;Purpose", H2))
    s.append(p(
        "This repository gives a temple community a public record it owns outright. It mirrors "
        "the community's own published facts into a fast, login-free page set held as plain text "
        "under version control, so the record can be cloned, forked, corrected and carried to "
        "any host without asking a platform for permission. It is the "
        f"{link('PAIX Parish Platform', 'https://github.com/EVEglyphDesign/paix-parish-platform')} "
        "machine &mdash; one repository, one dictionary entry per congregation, one build &mdash; "
        "pointed at a Hindu temple community and written in that community's own vocabulary "
        "rather than in borrowed structure."))

    s.append(Paragraph("2 &nbsp;Steward and standing", H2))
    s.append(p(
        "Steward: Prasad, FICO practitioner, formerly on the Epiq Systems programme. This is the "
        "seed of his own GitHub-backed record: a working surface for engaging local non-profit "
        "entities and the base layer of a community and personal digital twin. His son is the "
        "first reader of the education ladder, which is why that ladder is written to be read by "
        "a child without an adult narrating it."))
    s.append(p(
        "Platform pattern, stylesheet and operating canon: Donat Omer Th&eacute;riault, "
        "EVEglyphDesign. The community owns its content; EVEglyphDesign owns only the pattern."))

    s.append(Paragraph("3 &nbsp;Surfaces delivered", H2))
    s.append(table([
        ["Surface", "What it carries", "Address"],
        ["Portal", "Community cards, the argument for a repository over a website builder, and the two-minute instruction for adding a second community.", link("portal", BASE)],
        ["Austin Hindu Temple", "Address, hours, mission, governance, recurring observances and the last published class roster &mdash; each traced to a temple-published source.", link("temple page", BASE + "austin-hindu-temple/")],
        ["Education ladder", "Five age bands, four to eighteen, each with a stated aim and four units.", link("ladder", BASE + "education/")],
        ["Digital twin", "What the twin records, what it refuses to record, and how consent works in practice.", link("twin", BASE + "twin/")],
        ["Provenance", "Every fact with its source, its handling and its confirmation status.", link("provenance", BASE + "provenance/")],
    ], [1.25 * inch, 3.5 * inch, 1.25 * inch]))

    s.append(Paragraph("4 &nbsp;The education ladder", H2))
    s.append(p(
        "Five bands. Each states its aim in one sentence and carries four units, so a parent "
        "reads a whole year in under a minute and a child sees where they are going."))
    s.append(table([
        ["Band", "Aim"],
        ["Ages 4&ndash;6 &middot; Shishu", "Recognition and rhythm &mdash; the child learns that this is their place."],
        ["Ages 7&ndash;9 &middot; Bala", "Narrative &mdash; the child can retell a story and say what it asks of them."],
        ["Ages 10&ndash;12 &middot; Kishora", "Structure &mdash; the child can explain what Hindus do, and why, to a friend who is not Hindu."],
        ["Ages 13&ndash;15 &middot; Yuva", "Argument &mdash; the teenager holds their ground without contempt for anyone else's."],
        ["Ages 16&ndash;18 &middot; Taruna", "Stewardship &mdash; the young adult can run something and account for it."],
    ], [1.5 * inch, 4.5 * inch]))
    s.append(Paragraph("Design rules", H3))
    s.extend(bullets([
        "Sanskrit terms are glossed in plain English on first use, never left untranslated.",
        "Stories keep their mischief. Krishna is not sanitised into a lesson plan.",
        "Nothing is taught by contempt for another tradition; comparative respect is its own unit.",
        "Every band ends in something the child <i>does</i>, not something the child has been told.",
        "Standing comes from a weekly seva entry &mdash; evidenced help &mdash; not from attendance or scores.",
    ]))
    s.append(Paragraph(
        "The ladder does not replace the temple's own Balagokulam, Bhajans, Tamil and Samskritam "
        "classes. It is the written spine a parent holds against those classes to see what a "
        "child has covered and to fill the gaps in the weeks the family cannot make the drive to "
        "Decker Lake Road.", BODY))

    s.append(Paragraph("5 &nbsp;Consent and refusal", H2))
    s.append(p(
        "The twin records the institution, the calendar, the education ladder per cohort, service "
        "in aggregate, and its own provenance. It refuses the following, by design and not by "
        "oversight:"))
    s.extend(bullets([
        "Children's names, photographs, ages or schools without written parental consent held in the repository.",
        "Attendance used as a compliance instrument &mdash; a family that misses a term owes no explanation to a file.",
        "Donation amounts against named individuals.",
        "Trackers, advertisements, analytics beacons and third-party scripts of any kind.",
        "Anything a member cannot have removed, visibly, in the commit history.",
    ]))
    s.append(p(
        "Consent names the layer and the reader; &lsquo;yes to the class roster, no to "
        "photographs&rsquo; is a valid and recorded answer. Withdrawal is one request and takes "
        "effect in the next commit &mdash; no form, no committee. Where a feature would improve "
        "the record but reduce community safety, the feature loses."))

    s.append(Paragraph("6 &nbsp;Sourcing discipline", H2))
    s.append(p(
        "Address, telephone, general enquiry address, mission, governance and recurring "
        "observances are drawn from the temple's own pages and its own hosted documents, "
        "including the AHTCC bylaws revision 4.0.1 of 29 October 2017 and a temple-issued "
        "panchang. The class roster comes from an undated temple education page and is published "
        "here as a starting point for confirmation, with teacher names withheld pending consent. "
        "Opening hours differ between two temple pages and are flagged as a source conflict for "
        "the temple to settle. Deities and shrines, board and trustee names, and the current "
        "festival calendar are left blank and marked open, because no reachable source settles "
        "them and a plausible guess in a religious record is a worse outcome than a gap."))
    s.append(Paragraph(
        "The temple's site disallows automated reading at its root; facts were taken from its "
        "individually published pages reached through search, each fetched once. Nothing in this "
        "document was generated from a model's recollection of the temple.", SMALL))

    s.append(Paragraph("7 &nbsp;Next actions for the steward", H2))
    s.extend(bullets([
        "Walk the temple page with the temple office and settle the four open fields.",
        "Collect written consent for any named person or photograph before the first named entry.",
        f"Read the ladder with your son and mark the band he is actually in; log corrections in {link('the repository', REPO)}.",
        "Introduce the surface to one local non-profit entity as a worked example, not as a pitch.",
        "Copy the COMMUNITIES entry to add a second community; the portal card generates itself.",
    ]))

    s.append(Paragraph(
        f"Repository: {link(REPO.replace('https://', ''), REPO)} &nbsp;&middot;&nbsp; "
        f"Operating canon: {link('EVEglyphDesign Executive Boot Contract', 'https://eveglyphdesign.github.io/eve-glyph-boot-contract/')}",
        SMALL))
    s.append(Paragraph("Pour le bien-&ecirc;tre du peuple.", MARK))
    s.append(Spacer(1, 4))
    s.append(Paragraph(
        f"Document {DOC_ID} &middot; {total_pages} pages &middot; Key ID {KEY_ID} &middot; "
        f"Generated {TS} &middot; SHA-256 {content_hash}", SMALL))
    return s


class Doc(BaseDocTemplate):
    def __init__(self, path, total_pages):
        super().__init__(str(path), pagesize=LETTER,
                         leftMargin=0.95 * inch, rightMargin=0.95 * inch,
                         topMargin=0.9 * inch, bottomMargin=0.85 * inch,
                         title="EVEglyphDesign — Sanatana Community Platform Charter",
                         author="EVEglyphDesign", subject="Charter " + DOC_ID)
        self.total_pages = total_pages
        frame = Frame(self.leftMargin, self.bottomMargin,
                      self.width, self.height, id="body")
        self.addPageTemplates([PageTemplate(id="main", frames=[frame],
                                            onPage=self.decorate)])

    def decorate(self, canv, doc):
        w, h = LETTER
        canv.saveState()
        canv.setFillColor(CREAM)
        canv.rect(0, 0, w, h, stroke=0, fill=1)
        # watermark
        canv.saveState()
        canv.setFillColor(Color(0.91, 0.47, 0.13, alpha=0.055))
        canv.setFont("Fraunces", 62)
        canv.translate(w / 2, h / 2)
        canv.rotate(38)
        canv.drawCentredString(0, 0, "EVEglyphDesign")
        canv.restoreState()
        # header rule
        canv.setStrokeColor(ACCENT)
        canv.setLineWidth(2)
        canv.line(0.95 * inch, h - 0.68 * inch, w - 0.95 * inch, h - 0.68 * inch)
        canv.setFont("Fraunces", 8.5)
        canv.setFillColor(MUTE)
        canv.drawString(0.95 * inch, h - 0.58 * inch, "EVEglyphDesign \u00b7 Controlled copy")
        canv.drawRightString(w - 0.95 * inch, h - 0.58 * inch, DOC_ID)
        # footer
        canv.setStrokeColor(LINE)
        canv.setLineWidth(0.6)
        canv.line(0.95 * inch, 0.7 * inch, w - 0.95 * inch, 0.7 * inch)
        canv.setFont("Inter", 7.6)
        canv.setFillColor(MUTE)
        canv.drawString(0.95 * inch, 0.54 * inch,
                        "\u00a9 2026 EVEglyphDesign. All rights reserved. "
                        "Community content belongs to the community.")
        canv.drawRightString(w - 0.95 * inch, 0.54 * inch,
                             f"Page {doc.page} of {self.total_pages}")
        canv.restoreState()


def build(total_pages, content_hash):
    doc = Doc(OUT, total_pages)
    doc.build(story(str(total_pages) if isinstance(total_pages, int) else total_pages,
                    content_hash))
    return doc.page


def main():
    # pass one — discover page count
    pages = build("\u2014", "pending")
    # pass two — stamp count, then hash and stamp the hash in a third pass
    build(pages, "pending")
    h = hashlib.sha256(OUT.read_bytes()).hexdigest()[:32]
    build(pages, h)
    final = hashlib.sha256(OUT.read_bytes()).hexdigest()
    (ROOT / "registry" / "CHARTER-HASH.txt").write_text(
        f"{OUT.name}\nstamped-hash-prefix: {h}\nfile-sha256: {final}\ngenerated: {TS}\n",
        encoding="utf-8")
    print(f"pages={pages} stamped={h} file_sha256={final}")


if __name__ == "__main__":
    main()

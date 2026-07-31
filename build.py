#!/usr/bin/env python3
"""
Sanatana Community Platform — build script

Generates a portal page plus one mirrored community surface per COMMUNITIES
entry, an education ladder, and a digital-twin consent page. Styled with the
EVEglyphDesign canon (EgD-BOOT-001 §4): cream and orange, Fraunces display,
Inter body.

Pattern source: EVEglyphDesign/paix-parish-platform (Catholic parish portal).
This repository is the same machine pointed at a Hindu temple community —
one dictionary entry per community, one build, one public surface.

Steward: Prasad (FICO / Epiq Systems programme).
Design founder: Donat Omer Thériault, EVEglyphDesign.
"""

from __future__ import annotations
import html
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent
BUILT = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# ---------------------------------------------------------------------------
# Community data — add one dictionary per temple or community organisation.
# Every field marked CONFIRM is an assumption drawn from public sources and
# must be confirmed by the community before it is presented as their record.
# ---------------------------------------------------------------------------

COMMUNITIES = [
    {
        "slug": "austin-hindu-temple",
        "name": "Austin Hindu Temple &amp; Community Center",
        "short": "Austin Hindu Temple",
        "acronym": "AHTCC",
        "city": "Austin, Texas",
        "address": "9801 Decker Lake Road, Austin, TX 78724 — use the Imperial Drive entrance",
        "phone": "(512) 927-0000",
        "phone_tel": "+15129270000",
        "email": "info@austinhindutemple.org",
        "education_email": "education@austinhindutemple.org",
        "official_url": "https://austinhindutemple.org/",
        "tagline": "A volunteer-driven, community-supported non-profit — worship, education and "
                   "community life for the Hindu families of Central Texas",
        "mission": "The temple strives for spiritual richness and human excellence through the "
                   "values emphasised in Hindu scriptures, applied in daily life, while "
                   "recognising and respecting other religions and belief systems in their "
                   "due context.",
        "governance": "Texas non-profit corporation governed by bylaws (Rev. 4.0.1, 29 October "
                      "2017); principal office at 9801 Decker Lake Road, Austin, Texas 78724.",
        "hours": [
            ("Monday – Friday", "9:00 AM – 1:00 PM · 6:00 PM – 9:00 PM"),
            ("Weekends &amp; public holidays", "10:00 AM – 2:00 PM · 2:00 PM – 5:00 PM (darshan only) · 5:00 PM – 9:00 PM"),
        ],
        "recurring": [
            ("Satyanarayana Puja", "every Poornima — evening on weekdays, morning on weekends"),
            ("Ganapati Abhishekam", "every Sankata-hara Chaturthi"),
            ("Rudrabhishekam", "every Krishna Pradosham"),
        ],
        "classes": [
            ("Saturday", "11:00 AM – 12:00 PM", "Bhajans"),
            ("Saturday", "12:00 – 1:00 PM", "Tamil"),
            ("Sunday", "9:30 – 11:00 AM", "Balagokulam"),
            ("Sunday", "9:30 – 10:00 AM", "Yoga &amp; Surya Namaskar"),
            ("Sunday", "10:00 – 11:00 AM", "Fast Math"),
            ("Sunday", "11:00 AM – 12:00 PM", "Geography Bee"),
            ("Sunday", "12:30 – 1:00 PM", "Meditation &amp; Memory"),
            ("Sunday", "1:00 – 2:00 PM", "Chess"),
            ("Sunday", "2:00 – 3:00 PM", "Tamil"),
            ("Sunday (adults)", "10:00 – 11:00 AM", "Conversational Samskritam"),
            ("Sunday (adults)", "11:00 AM – 12:00 PM", "Patanjali Yoga Sutra"),
        ],
        "portal_blurb": "The reference community for this platform. Public record mirrored from "
                        "the temple's own published pages, nothing invented.",
        "confirm": [
            "Shrine and deity list — deliberately left blank rather than guessed.",
            "Current class roster and teachers — the published schedule page is undated.",
            "Board and trustee names for the current term.",
            "Festival calendar for the current year.",
        ],
    },
]

# ---------------------------------------------------------------------------
# Education ladder — culturally grounded, plainly laid out, age-laddered.
# Designed for a parent to read in one sitting and for a child to follow
# without an adult reading it aloud. Sanskrit terms are given with a plain
# English gloss on first use, never left untranslated.
# ---------------------------------------------------------------------------

LADDER = [
    {
        "band": "Ages 4 – 6 · Shishu",
        "aim": "Recognition and rhythm. The child learns that this is their place.",
        "units": [
            "Festivals of the year — Diwali, Holi, Ugadi, Ganesh Chaturthi: what is lit, cooked, worn and said",
            "Two short slokas (verses) learned by sound, not by translation",
            "Stories: Panchatantra animal tales; Ganesha and the broken tusk",
            "Namaste, pranam and the courtesy of a temple visit — shoes, silence, queue, prasadam",
        ],
    },
    {
        "band": "Ages 7 – 9 · Bala",
        "aim": "Narrative. The child can retell a story and say what it asks of them.",
        "units": [
            "Ramayana in twelve episodes — one per class, told and then retold by the child",
            "Krishna in Vrindavan — the Bhagavatam stories, with the mischief left in",
            "Language: reading the family's own script — Telugu, Tamil, Hindi or Devanagari",
            "Seva (service) log — one act of help a week, written in the child's own hand",
        ],
    },
    {
        "band": "Ages 10 – 12 · Kishora",
        "aim": "Structure. The child can name what Hindus do and why, to a friend who is not Hindu.",
        "units": [
            "Mahabharata — the family quarrel, the choices, the cost",
            "Symbolism: what the lamp, the coconut, the thread and the murti (image) actually stand for",
            "The four purusharthas (aims of life) — dharma, artha, kama, moksha in plain words",
            "Conversational Samskritam — greeting, asking, counting, describing",
        ],
    },
    {
        "band": "Ages 13 – 15 · Yuva",
        "aim": "Argument. The teenager can hold their own ground without contempt for anyone else's.",
        "units": [
            "Bhagavad Gita, chapters 2 and 3 — duty and action, read as a problem not a sermon",
            "Being Hindu in an American school — questions they will actually be asked, and honest answers",
            "Comparative respect — what Christians, Muslims, Jews and Buddhists hold, stated fairly",
            "Digital conduct — what a phone records, what a platform keeps, what consent means",
        ],
    },
    {
        "band": "Ages 16 – 18 · Taruna",
        "aim": "Stewardship. The young adult can run something and account for it.",
        "units": [
            "Teach one Shishu class under supervision, then write up what went wrong",
            "Temple as an institution — bylaws, board, budget, volunteer roster, audit",
            "A digital twin of their own — what they choose to record about themselves, and who may read it",
            "Capstone: one project that leaves the community measurably better, documented in this repository",
        ],
    },
]

FAQ = [
    ("Is this the temple's official website?",
     "No. The temple's own site remains at its own address and is linked from every page here. "
     "This is a community-stewarded mirror and working surface, built so that a family can "
     "keep its own record without asking a platform for permission."),
    ("Who owns what is written here?",
     "The community owns its content. The repository is public and forkable, so any family or "
     "committee can take a copy and continue it without the original author."),
    ("What is a digital twin, in one sentence?",
     "A record of a thing — a person, a family, an institution — kept by the thing itself, "
     "structured well enough that software can read it, and never held anywhere the subject "
     "cannot reach."),
    ("What does this cost?",
     "Nothing. GitHub Pages serves the surface free; the content is plain text under version "
     "control. There is no login, no tracker, no advertisement and no analytics on these pages."),
]

# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@400;600;700'
         '&amp;family=Inter:wght@400;500;600&amp;display=swap" rel="stylesheet">')

NAV = [
    ("index.html", "Portal"),
    ("austin-hindu-temple/index.html", "Austin Hindu Temple"),
    ("education/index.html", "Education ladder"),
    ("twin/index.html", "Digital twin"),
    ("provenance/index.html", "Provenance"),
]


def page(title: str, depth: int, current: str, body: str, sub: str = "") -> str:
    up = "../" * depth
    nav = "\n".join(
        '      <a href="{}{}"{}>{}</a>'.format(
            up, href, ' aria-current="page"' if href == current else "", label)
        for href, label in NAV)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Sanatana Community Platform</title>
<meta name="description" content="{sub or title}">
{FONTS}
<link rel="stylesheet" href="{up}assets/style.css">
</head>
<body>
<header class="masthead">
  <div class="wrap">
    <div class="mark">&#2384;</div>
    <div>
      <h1>Sanatana Community Platform</h1>
      <p class="sub">A community-stewarded surface &middot; EVEglyphDesign pattern</p>
    </div>
  </div>
</header>
<nav class="bar">
  <div class="wrap">
{nav}
  </div>
</nav>
<main>
  <div class="wrap">
{body}
  </div>
</main>
<footer class="foot">
  <div class="wrap">
    <p>Built {BUILT} from <a href="https://github.com/EVEglyphDesign/sanatana-community-platform">the sanatana-community-platform repository</a>. Regenerate with <code>python3 build.py</code>.</p>
    <p>Pattern inherited from <a href="https://github.com/EVEglyphDesign/paix-parish-platform">the PAIX Parish Platform</a>. Operating canon: <a href="https://eveglyphdesign.github.io/eve-glyph-boot-contract/">the EVEglyphDesign Executive Boot Contract</a>.</p>
    <p>Community content belongs to the community. Platform pattern &copy; 2026 EVEglyphDesign. Key ID <code>EgD-KEY-2026-07</code>.</p>
    <p class="mark-line">Pour le bien-&ecirc;tre du peuple.</p>
  </div>
</footer>
</body>
</html>
"""


def write(rel: str, content: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print("wrote", rel)


def portal() -> None:
    cards = []
    for c in COMMUNITIES:
        cards.append(f"""    <a class="card" href="{c['slug']}/index.html">
      <span class="kicker">{c['city']}</span>
      <h3>{c['short']}</h3>
      <p>{c['portal_blurb']}</p>
    </a>""")
    cards.append("""    <a class="card" href="education/index.html">
      <span class="kicker">Children &amp; parents</span>
      <h3>Education ladder</h3>
      <p>Five age bands from four years old to eighteen, each with a stated aim and four units.</p>
    </a>""")
    cards.append("""    <a class="card" href="twin/index.html">
      <span class="kicker">Consent first</span>
      <h3>Digital twin</h3>
      <p>What a community twin records, what it refuses to record, and who may read it.</p>
    </a>""")
    cards.append("""    <a class="card" href="provenance/index.html">
      <span class="kicker">Record</span>
      <h3>Provenance</h3>
      <p>Every fact on this surface, with the source it came from and whether it is confirmed.</p>
    </a>""")
    body = f"""    <h1>One community, one repository, one public surface</h1>
    <p class="lead">This platform mirrors a temple community into a plain, fast, login-free
    public surface that the community itself owns. It is the same machine that built a
    Catholic parish portal, pointed at a Hindu temple and its families.</p>

    <div class="note">
      <strong>Status: seed build.</strong> The Austin Hindu Temple surface below is assembled
      from the temple's own published pages and public filings. It is a working draft prepared
      for review by the community, not an official temple publication. Fields the sources do
      not settle are listed openly on each page rather than filled in by guesswork.
    </div>

    <div class="grid">
{chr(10).join(cards)}
    </div>

    <hr class="rule">

    <h2>Why a repository and not a website builder</h2>
    <p>A website builder rents you a page and keeps the keys. A repository is a file you can
    clone, read, diff, fork and carry to any host on earth. Every change is signed and dated.
    If the steward moves away, the community keeps the record. That is the whole argument, and
    it is why this exists as text under version control rather than as a subscription.</p>

    <h2>How to add a second community</h2>
    <ol>
      <li>Open <code>build.py</code> and copy one <code>COMMUNITIES</code> entry.</li>
      <li>Change the fields. Leave anything you cannot source in the <code>confirm</code> list.</li>
      <li>Run <code>python3 build.py</code> and commit. The portal card appears by itself.</li>
    </ol>

    <h2>Common questions</h2>
    <table>
      <tr><th style="width:34%">Question</th><th>Answer</th></tr>
{chr(10).join(f'      <tr><td>{q}</td><td>{a}</td></tr>' for q, a in FAQ)}
    </table>
"""
    write("index.html", page("Portal", 0, "index.html", body,
                             "A community-stewarded public surface for temple communities."))


def community_page(c: dict) -> None:
    hours = "\n".join(f"      <tr><td>{d}</td><td>{t}</td></tr>" for d, t in c["hours"])
    recurring = "\n".join(f"      <tr><td>{n}</td><td>{w}</td></tr>" for n, w in c["recurring"])
    classes = "\n".join(f"      <tr><td>{d}</td><td>{t}</td><td>{s}</td></tr>"
                        for d, t, s in c["classes"])
    confirm = "\n".join(f"      <li>{x}</li>" for x in c["confirm"])
    body = f"""    <h1>{c['name']}</h1>
    <p class="lead">{c['tagline']}</p>

    <div class="note">
      This page is a community mirror. The temple's own site is
      <a href="{c['official_url']}">the official Austin Hindu Temple website</a> and it governs.
      Where this page and the temple disagree, the temple is right.
    </div>

    <h2>Where and how to reach it</h2>
    <table>
      <tr><th style="width:26%">Address</th><td>{c['address']}</td></tr>
      <tr><th>Telephone</th><td><a href="tel:{c['phone_tel']}">{c['phone']}</a></td></tr>
      <tr><th>General enquiries</th><td><a href="mailto:{c['email']}">{c['email']}</a></td></tr>
      <tr><th>Classes and youth</th><td><a href="mailto:{c['education_email']}">{c['education_email']}</a></td></tr>
      <tr><th>Official website</th><td><a href="{c['official_url']}">austinhindutemple.org</a></td></tr>
    </table>

    <h2>Opening hours</h2>
    <table>
      <tr><th style="width:26%">Days</th><th>Hours</th></tr>
{hours}
    </table>
    <p style="font-size:0.9rem;color:var(--mute)">Published holidays observed: New Year's Day,
    Memorial Day, Independence Day, Labor Day, Thanksgiving Day and the day after, Christmas Day.
    Confirm before travelling — hours on the temple site have changed between versions.</p>

    <h2>Mission, as the temple states it</h2>
    <p>{c['mission']}</p>

    <h2>Governance</h2>
    <p>{c['governance']}</p>

    <h2>Recurring observances</h2>
    <table>
      <tr><th style="width:34%">Observance</th><th>When</th></tr>
{recurring}
    </table>

    <h2>Classes as last published</h2>
    <table>
      <tr><th style="width:22%">Day</th><th style="width:26%">Time</th><th>Class</th></tr>
{classes}
    </table>
    <p style="font-size:0.9rem;color:var(--mute)">Registration and volunteering run through
    <a href="mailto:{c['education_email']}">the temple education address</a>. This roster comes
    from an undated page and is reproduced here as a starting point for confirmation, not as a
    current timetable.</p>

    <h2>Not yet confirmed</h2>
    <ul>
{confirm}
    </ul>
"""
    write(f"{c['slug']}/index.html",
          page(c["short"], 1, f"{c['slug']}/index.html", body, c["tagline"]))


def education_page() -> None:
    blocks = []
    for band in LADDER:
        units = "\n".join(f"      <li>{u}</li>" for u in band["units"])
        blocks.append(f"""    <h3>{band['band']}</h3>
    <p><em>Aim:</em> {band['aim']}</p>
    <ul>
{units}
    </ul>""")
    body = f"""    <h1>Education ladder</h1>
    <p class="lead">Five bands, four years old to eighteen. Each band states its aim in one
    sentence and carries four units. A parent can read the whole thing in five minutes and know
    exactly what a year contains.</p>

    <div class="note">
      <strong>Design rules.</strong> Sanskrit terms are glossed in plain English on first use.
      Stories keep their mischief. Nothing is taught by contempt for another tradition. Every
      band ends in something the child does, not something the child has been told.
    </div>

{chr(10).join(blocks)}

    <hr class="rule">

    <h2>How this sits beside the temple's own classes</h2>
    <p>It does not replace them. Balagokulam, Bhajans, Tamil and Samskritam already run at the
    temple on Saturdays and Sundays. This ladder is the written spine a parent can hold against
    those classes to see what a child has covered and what is still missing — and to fill the
    gaps at home in the weeks the family cannot make the drive to Decker Lake Road.</p>

    <h2>The seva log</h2>
    <p>From age seven the child keeps one line a week: what they did for someone else, and who
    it helped. Written by hand, then typed into this repository once a term by the child.
    Standing in this community comes from evidenced help, not from attendance and not from
    scores. That mechanic is carried over deliberately from
    <a href="https://eveglyphdesign.github.io/eve-glyph-education-public/">the EVE Glyph
    education stream</a>, where service — not follower counts — is what earns a child standing.</p>

    <h2>For the parent teaching at home</h2>
    <ol>
      <li>One unit a week. Twelve weeks a term. Do not accelerate a child through a band.</li>
      <li>Read the story yourself first. If you cannot say why it matters, skip it this year.</li>
      <li>Let the child retell it wrong once before correcting. The retelling is the lesson.</li>
      <li>Write the week down in the repository. An undocumented term did not happen.</li>
    </ol>
"""
    write("education/index.html",
          page("Education ladder", 1, "education/index.html", body,
               "Five age bands from four to eighteen, culturally grounded and plainly laid out."))


def twin_page() -> None:
    body = """    <h1>The community digital twin</h1>
    <p class="lead">A digital twin is a record of a thing, kept by the thing itself, structured
    well enough that software can read it, and held nowhere the subject cannot reach.</p>

    <h2>What this twin records</h2>
    <table>
      <tr><th style="width:34%">Layer</th><th>Contents</th></tr>
      <tr><td>Institution</td><td>Address, hours, governance documents, published observances, contact routes, class roster.</td></tr>
      <tr><td>Calendar</td><td>Festivals and recurring pujas as dates, so they can be read by a phone rather than a poster.</td></tr>
      <tr><td>Education</td><td>The ladder, the units covered, the terms completed. Per cohort, not per named child.</td></tr>
      <tr><td>Service</td><td>Seva entries in aggregate — acts of help recorded, with names only where the family chose to give them.</td></tr>
      <tr><td>Provenance</td><td>Where every fact came from, when it was checked, and whether the community has confirmed it.</td></tr>
    </table>

    <h2>What this twin refuses to record</h2>
    <ul>
      <li>Children's names, photographs, ages or schools without a parent's written consent, held in the repository.</li>
      <li>Attendance as a compliance instrument. A family that misses a term owes no explanation to a file.</li>
      <li>Donation amounts against named individuals.</li>
      <li>Any tracker, advertisement, analytics beacon or third-party script on these pages.</li>
      <li>Anything a member cannot ask to have removed and see removed in the commit history.</li>
    </ul>

    <div class="note">
      <strong>Safety first, betterment second.</strong> Where a feature would make the record
      better but the community less safe, the feature loses. That ordering is not negotiable and
      it is inherited from the operating canon, not invented here.
    </div>

    <h2>Consent, in practice</h2>
    <ol>
      <li>Nothing about a named person enters this repository until they, or a parent, say so in writing.</li>
      <li>Consent names the layer and the reader. "Yes to the class roster, no to photographs" is a valid answer.</li>
      <li>Withdrawal is a single request and takes effect in the next commit. No form, no committee.</li>
      <li>The consent record lives in the repository beside the data, so the two cannot drift apart.</li>
    </ol>

    <h2>Why a family would want one</h2>
    <p>Because the alternative is that the record of a community's life sits inside somebody
    else's product, priced by seat, exportable only in the shapes that product allows. A twin
    kept as plain text under version control outlives the platform, the steward and the
    subscription. In thirty years a grandchild can still read it.</p>
"""
    write("twin/index.html",
          page("Digital twin", 1, "twin/index.html", body,
               "What a community digital twin records, refuses to record, and who may read it."))


def provenance_page() -> None:
    rows = [
        ("Name, mission statement, non-profit and volunteer character",
         "austinhindutemple.org home page", "Quoted, lightly condensed", "Confirmed by source"),
        ("Address, 9801 Decker Lake Road, Imperial Drive entrance",
         "Temple map-and-directions page; AHTCC bylaws principal-office clause",
         "Two independent temple-published sources agree", "Confirmed by source"),
        ("Telephone (512) 927-0000 and info@ address",
         "Temple calendar page footer; temple-issued panchang PDF", "Verbatim", "Confirmed by source"),
        ("Opening hours",
         "Temple map-and-directions page", "Verbatim; an older temple page shows different hours",
         "Source conflict — temple to settle"),
        ("Recurring observances (Satyanarayana Puja, Ganapati Abhishekam, Rudrabhishekam)",
         "Temple-issued panchang PDF", "Verbatim", "Confirmed by source"),
        ("Class roster and times",
         "Temple education page (undated, filename suggests a superseded version)",
         "Verbatim, teacher names withheld pending consent", "Needs confirmation"),
        ("Governance and bylaws revision",
         "AHTCC Bylaws Rev. 4.0.1, 29 October 2017, temple-hosted PDF", "Citation only",
         "Confirmed by source"),
        ("Deities and shrines",
         "None located", "Deliberately left blank rather than inferred", "Open"),
        ("Board and trustee names",
         "None located", "Not published on reachable pages", "Open"),
        ("Education ladder content",
         "Authored for this repository", "Modelled on the age-laddered pattern common to "
         "Balagokulam, Bala Vihar and Bala Vikas programmes in the Austin area", "Draft for review"),
    ]
    table = "\n".join(
        f"      <tr><td>{f}</td><td>{s}</td><td>{h}</td><td>{st}</td></tr>"
        for f, s, h, st in rows)
    body = f"""    <h1>Provenance</h1>
    <p class="lead">Every fact on this surface, where it came from, how it was handled, and
    whether the community has confirmed it. A record without provenance is a rumour with a
    stylesheet.</p>

    <div class="note">
      <strong>Rule.</strong> A field with no source is left blank and listed as open. It is
      never filled with a plausible guess. Deities, board names and the current festival
      calendar are open for exactly that reason.
    </div>

    <table>
      <tr><th style="width:24%">Fact</th><th style="width:26%">Source</th><th style="width:26%">Handling</th><th>Status</th></tr>
{table}
    </table>

    <h2>Retrieval note</h2>
    <p>The temple's own site disallows automated reading at its root. Facts above were taken
    from the temple's individually published pages and its own hosted PDF documents, reached
    through search rather than by reading the site wholesale. No page was fetched more than
    once, and nothing here was generated from a model's recollection of the temple.</p>

    <h2>How to correct this page</h2>
    <ol>
      <li>Open an issue on <a href="https://github.com/EVEglyphDesign/sanatana-community-platform/issues">the repository issue tracker</a>, or send the correction to the steward.</li>
      <li>Corrections are appended and dated. Nothing is silently overwritten.</li>
      <li>A confirmed fact moves from <em>Needs confirmation</em> to <em>Confirmed by community</em> with the date and the person who confirmed it.</li>
    </ol>
"""
    write("provenance/index.html",
          page("Provenance", 1, "provenance/index.html", body,
               "Sources, handling and confirmation status for every fact on this surface."))


def main() -> None:
    portal()
    for c in COMMUNITIES:
        community_page(c)
    education_page()
    twin_page()
    provenance_page()
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    print("done —", BUILT)


if __name__ == "__main__":
    main()

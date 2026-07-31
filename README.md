# Sanatana Community Platform

A community-stewarded public surface for temple communities — one repository, one build, one
login-free page set that the community itself owns.

- Live surface: [the Sanatana Community Platform portal](https://eveglyphdesign.github.io/sanatana-community-platform/)
- Reference community: [Austin Hindu Temple &amp; Community Center](https://eveglyphdesign.github.io/sanatana-community-platform/austin-hindu-temple/)
- Education ladder: [five age bands, four to eighteen](https://eveglyphdesign.github.io/sanatana-community-platform/education/)
- Digital twin: [what is recorded, refused, and who may read it](https://eveglyphdesign.github.io/sanatana-community-platform/twin/)
- Provenance: [every fact with its source and status](https://eveglyphdesign.github.io/sanatana-community-platform/provenance/)
- Charter PDF: [EVEglyphDesign Sanatana Community Platform Charter](https://eveglyphdesign.github.io/sanatana-community-platform/EVEglyphDesign_Sanatana_Community_Platform_Charter.pdf)

## What this is

The [PAIX Parish Platform](https://github.com/EVEglyphDesign/paix-parish-platform) proved that a
single repository plus one dictionary entry per congregation can mirror many Catholic parishes
into one consistent public surface. This repository is the same machine pointed at a Hindu temple
community and its families, following the cultural vocabulary of that community rather than
translating it into borrowed Catholic structure.

The reference community is the Austin Hindu Temple &amp; Community Center, chosen because it is
the community the steward already belongs to. Everything on the temple page is drawn from the
temple's own published pages and its own hosted documents; anything the sources do not settle is
listed openly as unconfirmed rather than filled in with a plausible guess.

## Steward

Prasad — FICO practitioner, formerly on the Epiq Systems programme. This repository is the seed of
his own GitHub-backed record: a working surface for engaging local non-profit entities, and the
base layer of a personal and community digital twin. His son is the first reader of the education
ladder, which is why the ladder is written to be read by a child without an adult narrating it.

Platform pattern and canon: Donat Omer Thériault, EVEglyphDesign.

## Build

```bash
python3 build.py          # regenerates every HTML page
python3 scripts/make_charter_pdf.py   # regenerates the charter PDF and its hash
```

No dependencies beyond the Python standard library for `build.py`; the PDF script uses ReportLab.

## Adding a community

1. Copy one entry in the `COMMUNITIES` list in `build.py`.
2. Replace the fields. Leave anything unsourced in that entry's `confirm` list.
3. Run `python3 build.py`, commit, push. The portal card and the community page appear together.

## Structure

| Path | Contents |
|---|---|
| `build.py` | All community data and every page generator |
| `assets/style.css` | EVEglyphDesign canon — cream and orange, Fraunces display, Inter body |
| `austin-hindu-temple/` | Generated reference community surface |
| `education/` | Generated education ladder |
| `twin/` | Generated digital-twin consent page |
| `provenance/` | Generated source and confirmation register |
| `registry/` | Append-only correction and consent records |
| `scripts/` | Charter PDF generator |

## Rules this repository keeps

- **No unsourced facts.** A blank field with an open status beats a confident invention.
- **Consent before content.** No named child, photograph or donation figure enters this
  repository without written consent held in `registry/`.
- **Append, never overwrite.** Corrections are dated and added. History is not rewritten.
- **No trackers.** No analytics, no advertisement, no third-party script on any page.
- **Safety first, betterment second.** A feature that improves the record but reduces community
  safety loses.

Operating canon: [the EVEglyphDesign Executive Boot Contract](https://eveglyphdesign.github.io/eve-glyph-boot-contract/).

## Licence and ownership

Community content belongs to the community and is theirs to fork, carry and continue. The
platform pattern, stylesheet and canon are © 2026 EVEglyphDesign, controlled copy, Key ID
`EgD-KEY-2026-07`.

*Pour le bien-être du peuple.*

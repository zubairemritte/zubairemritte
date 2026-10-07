"""Generate the profile's SVG covers using Python's standard library.

Run from any directory: python3 scripts/build-profile-assets.py
Edit this source before regenerating the seven files in assets/.
"""

from html import escape
from pathlib import Path


OUT = Path(__file__).resolve().parents[1] / "assets"
PAPER = "#F4F0E7"
INK = "#242D2A"
MUTED = "#5E655E"
RULE = "#C3BDB0"
BRICK = "#AA402E"
GREEN = "#355D4A"
OCHRE = "#855B1D"
WINE = "#824653"
BLUE = "#365D78"
SERIF = "Georgia, 'Times New Roman', serif"
SANS = "Arial, Helvetica, sans-serif"
MONO = "'Courier New', Courier, monospace"


def text(x, y, value, size=24, colour=INK, family=SANS, spacing=0, weight=400):
    return (
        f'<text x="{x}" y="{y}" fill="{colour}" font-family="{family}" '
        f'font-size="{size}" font-weight="{weight}" letter-spacing="{spacing}">'
        f"{escape(value)}</text>"
    )


def line(x1, y1, x2, y2, colour=RULE, width=1):
    return f'<path d="M{x1} {y1}H{x2}" stroke="{colour}" stroke-width="{width}"/>' if y1 == y2 else (
        f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{colour}" stroke-width="{width}"/>'
    )


def rect(x, y, w, h, fill=PAPER, stroke="none", width=1):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>'
    )


def label(x, y, value, colour=MUTED, size=15):
    return text(x, y, value, size, colour, MONO, spacing=0.65)


def monogram(x, y, scale=1):
    # The Z and E share a baseline. The cut between the letters is intentional.
    return (
        f'<g transform="translate({x} {y}) scale({scale})" fill="{BRICK}">'
        '<path d="M0 0H82V15L24 99H83V115H0V100L59 16H0Z"/>'
        '<path d="M99 0H165V16H117V46H156V62H117V99H165V115H99Z"/>'
        '</g>'
    )


def save(name, w, h, title, description, elements):
    OUT.mkdir(parents=True, exist_ok=True)
    body = "\n".join(elements)
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">\n'
        f'<title id="title">{escape(title)}</title>\n'
        f'<desc id="desc">{escape(description)}</desc>\n'
        f'{body}\n</svg>\n'
    )
    (OUT / name).write_text(svg, encoding="utf-8")


def build_hero():
    wide = [
        rect(0, 0, 1440, 412),
        rect(0, 0, 8, 412, BRICK),
        label(56, 48, "DATA SCIENTIST & ANALYST", INK, 17),
        label(1210, 48, "PORTFOLIO / ZE", INK, 16),
        line(56, 70, 1384, 70),
        text(50, 196, "Zubair Emritte", 106, INK, SERIF, -3),
        text(57, 257, "Data science, with business in mind.", 31),
        line(1037, 108, 1037, 283),
        monogram(1132, 117, 1.28),
        line(56, 323, 1384, 323),
        label(56, 367, "APPLIED ECONOMICS / STATISTICS", INK, 16),
        label(931, 367, "BI / CAUSAL ANALYTICS / DATA", BRICK, 16),
    ]
    save(
        "hero.svg", 1440, 412,
        "Zubair Emritte — Data science, with business in mind",
        "A typographic profile cover with a custom ZE monogram. Applied economics, "
        "statistics, BI and causal analytics.",
        wide,
    )

    compact = [
        rect(0, 0, 680, 464),
        rect(0, 0, 6, 464, BRICK),
        label(30, 42, "DATA SCIENTIST & ANALYST", INK, 15),
        line(30, 62, 650, 62),
        text(25, 164, "Zubair", 91, INK, SERIF, -2),
        text(25, 254, "Emritte", 91, INK, SERIF, -2),
        monogram(503, 122, 0.75),
        text(31, 317, "Data science,", 28),
        text(31, 355, "with business in mind.", 28),
        line(30, 386, 650, 386),
        label(31, 428, "ECONOMICS / STATISTICS / DATA", BRICK, 17),
    ]
    save(
        "hero-compact.svg", 680, 464,
        "Zubair Emritte — Data science, with business in mind",
        "Compact typographic profile cover with the ZE monogram. Economics, statistics and data.",
        compact,
    )


def skills_index():
    return [
        rect(1015, 96, 320, 49, PAPER, BRICK, 1.5),
        rect(1031, 145, 320, 49, PAPER, BRICK, 1.5),
        rect(1047, 194, 320, 49, PAPER, BRICK, 1.5),
        label(1034, 127, "01", BRICK, 14),
        text(1100, 129, "Roles", 25, INK, SERIF),
        label(1050, 176, "02", BRICK, 14),
        text(1116, 178, "Skills", 25, INK, SERIF),
        label(1066, 225, "03", BRICK, 14),
        text(1132, 227, "Opportunities", 25, INK, SERIF),
    ]


def build_careergraph():
    cover = [
        rect(0, 0, 1440, 338),
        rect(0, 0, 8, 338, BRICK),
        label(56, 43, "01 / LABOUR MARKET INTELLIGENCE", BRICK, 17),
        label(1160, 43, "FIRST PLANNED BUILD", BRICK, 15),
        line(56, 62, 1384, 62),
        text(50, 157, "CareerGraph Europe", 75, INK, SERIF, -1.8),
        text(56, 211, "Understand demand. Identify the skill gap.", 27),
        line(962, 91, 962, 248),
        *skills_index(),
        line(56, 277, 1384, 277),
        label(56, 314, "DATA ENGINEERING / NLP / ANALYTICS", INK, 16),
        label(1162, 314, "BRIEF AVAILABLE", BRICK, 16),
    ]
    save(
        "careergraph.svg", 1440, 338,
        "01 — CareerGraph Europe",
        "First planned build: labour-market and skills intelligence. "
        "An index of roles, skills and opportunities illustrates the product scope. Product brief available.",
        cover,
    )


def indicator_register():
    elements = [rect(468, 177, 174, 84, PAPER, GREEN, 1.5)]
    for y in (205, 233):
        elements.append(line(468, y, 642, y, GREEN))
    elements.append(line(573, 177, 573, 261, GREEN))
    for y, word in ((197, "SOURCE"), (225, "SERIES"), (253, "UNIT")):
        elements.append(label(478, y, word, GREEN, 13))
        elements.append(line(590, y - 5, 627, y - 5, GREEN, 3))
    return elements


def price_label():
    return [
        f'<path d="M485 173H622V253L613 261L604 253L595 261L586 253L577 261'
        f'L568 253L559 261L550 253L541 261L532 253L523 261L514 253L505 261'
        f'L496 253L485 261Z" fill="{PAPER}" stroke="{OCHRE}" stroke-width="1.5"/>',
        label(500, 196, "PRICE", OCHRE, 13),
        line(500, 204, 607, 204),
        label(500, 224, "DEMAND", OCHRE, 13),
        label(500, 247, "EFFECT", OCHRE, 13),
    ]


def transaction_note():
    return [
        rect(468, 177, 174, 84, PAPER, WINE, 1.5),
        label(481, 198, "TRACE / REVIEW", WINE, 11),
        line(480, 207, 630, 207),
        rect(486, 224, 17, 17, WINE),
        rect(546, 224, 17, 17, PAPER, WINE, 1.5),
        rect(606, 224, 17, 17, PAPER, WINE, 1.5),
        line(503, 232, 546, 232, WINE, 1.5),
        line(563, 232, 606, 232, WINE, 1.5),
        line(614, 241, 614, 251, WINE, 1.5),
        line(494, 251, 614, 251, WINE, 1.5),
        line(494, 241, 494, 251, WINE, 1.5),
    ]


def processing_stages():
    elements = []
    for y, word, x in ((176, "LOAD", 463), (206, "TEST", 481), (236, "SERVE", 499)):
        elements.extend([
            rect(x, y, 130, 25, PAPER, BLUE, 1.5),
            rect(x, y, 6, 25, BLUE),
            label(x + 19, y + 18, word, BLUE, 13),
        ])
    return elements


def build_project_cards():
    # Each cover keeps the same reading order, with a diagram tied to its subject.
    cards = [
        ("luxrisk.svg", "02", "ECONOMIC INDICATORS", "LuxRisk Intelligence",
         "Macroeconomic & financial indicators", GREEN,
         ("Compare countries.", "Trace every indicator."),
         "PYTHON / SQL / POWER BI", indicator_register()),
        ("pricepulse.svg", "03", "PRICING & CAUSALITY", "PricePulse AI",
         "Retail pricing & causal machine learning", OCHRE,
         ("Observe the price.", "Evaluate the effect."),
         "CAUSAL ANALYSIS / ML / MLOPS", price_label()),
        ("amlgraph.svg", "04", "TRANSACTION ANALYSIS", "AMLGraph",
         "Explainable transaction investigations", WINE,
         ("Follow the transaction.", "Explain the signal."),
         "GRAPHS / ANOMALIES / SYNTHETIC DATA", transaction_note()),
        ("platform.svg", "05", "DATA OPERATIONS", "Data Platform Lab",
         "Reproducible cloud data infrastructure", BLUE,
         ("Load. Check. Serve.", "Recover with confidence."),
         "AWS / DBT / AIRFLOW / TERRAFORM", processing_stages()),
    ]
    for filename, number, category, name, subtitle, accent, notes, stack, diagram in cards:
        cover = [
            rect(0, 0, 680, 330),
            rect(0, 0, 5, 330, accent),
            label(31, 35, f"{number} / {category}", accent, 13),
            label(583, 35, "PLANNED", accent, 12),
            line(31, 54, 647, 54),
            text(28, 111, name, 45, INK, SERIF, -1),
            text(31, 146, subtitle, 20),
            text(31, 213, notes[0], 21, accent, SERIF),
            text(31, 244, notes[1], 21, accent, SERIF),
            *diagram,
            line(31, 282, 647, 282),
            label(31, 310, stack, INK, 12.5),
        ]
        save(
            filename, 680, 330, f"{number} — {name}",
            f"{subtitle}. Planned project; product brief available. "
            "The diagram illustrates the concept, not measured results.", cover,
        )


if __name__ == "__main__":
    build_hero()
    build_careergraph()
    build_project_cards()
    print(f"Generated seven SVG covers in {OUT}")

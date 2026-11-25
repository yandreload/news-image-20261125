#!/usr/bin/env python3
"""Render the 25 November 2026 newspaper front page to entry.png.

A single 1024x1024 broadsheet: masthead, one lead story, and ten
short stories in a two-column grid. Every word is fixed in this file,
so two runs produce the same bytes.
"""

import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
PAPER = (248, 244, 233)
LEAD_BG = (239, 231, 207)
INK = (20, 20, 20)
RED = (163, 18, 18)
GREY = (90, 83, 72)

SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns a list of lines that fit `width`."""
    lines, cur = [], ""
    for word in text.split():
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def fit_text(draw, text, path, size, width, min_size=14):
    """Largest font size (down to min_size) whose single line fits."""
    while size > min_size and draw.textlength(text, font=font(path, size)) > width:
        size -= 1
    return font(path, size)


def fit_body(draw, text, path, size, width, max_lines, min_size=13):
    """Largest font size whose wrapped body fits in max_lines lines."""
    while size > min_size:
        fnt = font(path, size)
        if len(wrap(draw, text, fnt, width)) <= max_lines:
            return fnt, wrap(draw, text, fnt, width)
        size -= 1
    fnt = font(path, size)
    return fnt, wrap(draw, text, fnt, width)[:max_lines]


def headline_block(draw, x, y, width, text, path, size, max_lines, lh):
    """Draw a wrapped headline; returns the y just below it."""
    fnt = font(path, size)
    lines = wrap(draw, text, fnt, width)[:max_lines]
    for i, line in enumerate(lines):
        draw.text((x, y + i * lh), line, font=fnt, fill=INK)
    return y + len(lines) * lh


LEAD = {
    "kicker": "SPACE  ·  LEAD STORY",
    "headline": "First Pakistani in orbit as Shenzhou-24 reaches Tiangong",
    "body": (
        "China's Shenzhou-24 lifted off from Jiuquan carrying Muhammad "
        "Zeeshan Ali, the first Pakistani in orbit and the first foreign "
        "astronaut aboard the Tiangong station. A crew of three, on a "
        "five-to-ten-day mission."
    ),
}

STORIES = [
    {
        "kicker": "THE GULF",
        "headline": "Drone hits Riyadh tower; 11 hurt",
        "body": (
            "Houthi fighters hit Riyadh's tallest tower Tuesday, wounding "
            "11. The coalition struck Hodeidah port overnight."
        ),
    },
    {
        "kicker": "UKRAINE",
        "headline": "Kyiv confirms sinking of corvette",
        "body": (
            "Ukraine says naval drones sank the corvette Merkury off Libya "
            "and hit ships in the Baltic. Moscow calls the strikes terrorism."
        ),
    },
    {
        "kicker": "COLOMBIA",
        "headline": "Hostage standoff in Cartagena",
        "body": (
            "Gunmen seized an Éxito supermarket after a failed "
            "armoured-truck robbery, holding about 30 people. Talks ran "
            "into the night."
        ),
    },
    {
        "kicker": "MARKETS",
        "headline": "Nasdaq slides on tariff fears",
        "body": (
            "Nasdaq fell 1.5% and Nvidia about 6% on a report the US is "
            "preparing tariff rises on China, the EU and 14 others."
        ),
    },
    {
        "kicker": "SECURITY",
        "headline": "CIA and ODNI hit by breach",
        "body": (
            "US intelligence agencies suffered a cyber breach involving "
            "some unclassified information, officials confirmed Tuesday."
        ),
    },
    {
        "kicker": "TECH",
        "headline": "Huawei guilty of trade-secret theft",
        "body": (
            "A US court found China's Huawei guilty of stealing trade "
            "secrets in a criminal trial; it was acquitted of racketeering."
        ),
    },
    {
        "kicker": "FRANCE",
        "headline": "Sarkozy and Bruni face trial",
        "body": (
            "French officials ordered a corruption case involving "
            "ex-president Nicolas Sarkozy and his wife Carla Bruni to trial."
        ),
    },
    {
        "kicker": "IRAN",
        "headline": "Singer lashed 74 times in Iran",
        "body": (
            "Parastoo Ahmadi was lashed 74 times in Qom over a 2024 "
            "YouTube concert performed without a hijab. Her team was lashed too."
        ),
    },
    {
        "kicker": "GAZA",
        "headline": "Gaza death toll reaches 74,746",
        "body": (
            "The toll from Israeli attacks reached 74,746, the WAFA news "
            "agency reported on Wednesday."
        ),
    },
    {
        "kicker": "MALI",
        "headline": "Leaked data on Russian deaths in Mali",
        "body": (
            "Leaked data shed new light on Russian deaths in Mali, "
            "reports said on Wednesday."
        ),
    },
]


def draw_masthead(draw):
    date_fnt = font(SANS, 18)
    date = "WEDNESDAY, 25 NOVEMBER 2026"
    draw.text(((W - draw.textlength(date, font=date_fnt)) / 2, 36),
              date, font=date_fnt, fill=GREY)
    title_fnt = fit_text(draw, "THE WORLD IN ONE DAY", SERIF_BOLD, 56, 940)
    title = "THE WORLD IN ONE DAY"
    draw.text(((W - draw.textlength(title, font=title_fnt)) / 2, 60),
              title, font=title_fnt, fill=INK)
    sub_fnt = font(SANS, 19)
    sub = "ELEVEN STORIES  ·  ONE DAY IN THE WORLD"
    draw.text(((W - draw.textlength(sub, font=sub_fnt)) / 2, 128),
              sub, font=sub_fnt, fill=GREY)
    draw.line([(40, 154), (984, 154)], fill=INK, width=3)
    draw.line([(40, 160), (984, 160)], fill=INK, width=1)


def draw_lead(draw):
    draw.rectangle([40, 174, 984, 344], fill=LEAD_BG, outline=INK, width=1)
    kicker_fnt = font(SANS_BOLD, 19)
    draw.text((56, 190), LEAD["kicker"], font=kicker_fnt, fill=RED)
    after = headline_block(draw, 56, 216, 912, LEAD["headline"],
                           SERIF_BOLD, 29, 2, 34)
    body_fnt, lines = fit_body(draw, LEAD["body"], SANS, 19, 912, 2)
    for i, line in enumerate(lines):
        draw.text((56, after + 6 + i * 25), line, font=body_fnt, fill=INK)


def draw_story(draw, box, story):
    x, y, w, h = box
    draw.line([(x, y), (x + w, y)], fill=INK, width=2)
    kicker_fnt = font(SANS_BOLD, 15)
    draw.text((x, y + 8), story["kicker"], font=kicker_fnt, fill=RED)
    head_fnt = fit_text(draw, story["headline"], SERIF_BOLD, 21, w, 16)
    draw.text((x, y + 28), story["headline"], font=head_fnt, fill=INK)
    body_fnt, lines = fit_body(draw, story["body"], SANS, 17, w, 2)
    lh = body_fnt.size + 4
    for i, line in enumerate(lines):
        draw.text((x, y + 56 + i * lh), line, font=body_fnt, fill=INK)


def draw_footer(draw):
    fnt = font(SANS, 14)
    note = "Sources: Reuters · AP · The Wall Street Journal · Xinhua · ISW · CNN — full list in SOURCES.md"
    draw.text(((W - draw.textlength(note, font=fnt)) / 2, 985),
              note, font=fnt, fill=GREY)


def build():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    draw.rectangle([14, 14, 1010, 1010], outline=INK, width=2)
    draw.rectangle([22, 22, 1002, 1002], outline=INK, width=1)
    draw_masthead(draw)
    draw_lead(draw)
    col_w = 464
    xs = [40, 520]
    y0, row_h, gap = 360, 118, 8
    for i, story in enumerate(STORIES):
        row, col = divmod(i, 2)
        draw_story(draw, (xs[col], y0 + row * (row_h + gap), col_w, row_h),
                   story)
    draw_footer(draw)
    img.save(OUT, format="PNG")
    print(f"wrote {OUT} {W}x{H}")


if __name__ == "__main__":
    build()

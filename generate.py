#!/usr/bin/env python3
"""Render entry.png for the make.fun bounty
"Sum up 25 November's world news in one image" (news-image-20261125).

Local build tool only -- NOT the entrypoint. The entrypoint is main.py,
which only copies the committed entry.png to /output/entry.png, so the
submitted program needs no network, no Pillow and no fonts at run time.

Run:  python3 generate.py   (writes entry.png next to this file)
Requires Pillow + Liberation fonts locally (present on this VM).
Deterministic: fixed text, fixed layout, fixed PNG encoder settings.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.png"

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

NAVY = (15, 42, 68)
NAVY2 = (23, 64, 100)
RED = (178, 34, 34)
GOLD = (201, 162, 39)
INK = (24, 24, 24)
GREY = (88, 88, 88)
PAPER = (250, 248, 243)
LINE = (200, 196, 188)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Wrap text to fit pixel width, returning lines."""
    lines = []
    for para in text.split("\n"):
        words, cur = para.split(), ""
        for w in words:
            trial = (cur + " " + w).strip()
            if draw.textlength(trial, font=fnt) <= width:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
    return lines


def para(draw, xy, text, fnt, width, fill=INK, leading=None):
    x, y = xy
    leading = leading or int(fnt.size * 1.28)
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def kicker(draw, xy, text, color=RED):
    f = font(SANS_B, 21)
    draw.text(xy, text.upper(), font=f, fill=color)
    return xy[1] + 28


def headline(draw, xy, text, size, width, fill=INK):
    f = font(SERIF, size)
    return para(draw, xy, text, f, width, fill=fill, leading=int(size * 1.08))


def rule(draw, x0, y, x1, w=2, color=LINE):
    draw.line([(x0, y), (x1, y)], fill=color, width=w)


def bullet(draw, x, y, text, fnt, width, fill=INK, dot=RED):
    draw.ellipse([x, y + 8, x + 9, y + 17], fill=dot)
    return para(draw, (x + 18, y), text, fnt, width - 18, fill=fill,
                leading=int(fnt.size * 1.3))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---------- masthead ----------
    d.rectangle([0, 0, W, 148], fill=NAVY)
    d.rectangle([0, 148, W, 154], fill=GOLD)
    d.text((36, 22), "THE WORLD IN ONE DAY", font=font(SERIF, 50),
           fill=(255, 255, 255))
    d.text((36, 90), "WEDNESDAY  25  NOVEMBER  2026", font=font(SANS_B, 28),
           fill=GOLD)
    d.text((772, 30), "ONE IMAGE.", font=font(SANS_B, 22), fill=(255, 255, 255))
    d.text((772, 58), "THE WHOLE DAY.", font=font(SANS_B, 22),
           fill=(255, 255, 255))
    d.text((772, 96), "11 stories · 5 regions",
           font=font(SANS, 20), fill=(200, 210, 220))

    # ---------- lead: Shenzhou-24 ----------
    y = 178
    y = kicker(d, (36, y), "Lead story  —  Space  ·  Wed 25 Nov")
    y = headline(d, (36, y + 2),
                 "Pakistan's first astronaut\nreaches orbit",
                 48, 640)
    y = para(d, (36, y + 8),
             "China's Shenzhou-24 blasted off from Jiuquan at 00:18 UTC on "
             "Wednesday, carrying Muhammad Zeeshan Ali — the first "
             "Pakistani in orbit and the first foreign astronaut aboard "
             "China's Tiangong space station. He will spend about a week "
             "in orbit running biotech experiments.",
             font(SANS, 22), 640)
    # right-hand fact box: Tiangong
    d.rectangle([712, 178, 988, 452], outline=NAVY2, width=3)
    d.rectangle([712, 178, 988, 222], fill=NAVY2)
    d.text((730, 186), "TIANGONG'S FIRST GUEST", font=font(SANS_B, 17),
           fill=(255, 255, 255))
    d.text((730, 240), "Tiangong station", font=font(SERIF, 30), fill=INK)
    para(d, (730, 282),
         "China's first joint\ncrewed flight with a\nforeign astronaut.\nAli returns on\nShenzhou-23.",
         font(SANS, 20), 240)
    d.text((730, 420), "First Pakistani in orbit.",
           font=font(SANS_B, 20), fill=RED)

    rule(d, 36, 478, 988)

    # ---------- row 2: Gulf | Ukraine ----------
    y = 496
    # Gulf (left)
    y1 = kicker(d, (36, y), "Gulf  ·  overnight into Wed 25 Nov")
    y1 = headline(d, (36, y1 + 2), "Houthis hit Riyadh tower;\ncoalition hits Hodeidah", 34, 440)
    y1 = para(d, (36, y1 + 6),
              "A Houthi drone hit Riyadh's tallest tower on Tuesday, "
              "wounding 11 — the second strike in under a week. The "
              "Saudi-led coalition hit Hodeidah port overnight into "
              "Wednesday.",
              font(SANS, 21), 440)
    # Ukraine (right)
    x2 = 528
    y2 = kicker(d, (x2, y), "Ukraine  ·  Tue–Wed 25 Nov")
    y2 = headline(d, (x2, y2 + 2), "Moscow calls ship\nstrikes 'terrorism'", 34, 440)
    y2 = para(d, (x2, y2 + 6),
              "Zelenskiy confirms Ukraine sank a Russian corvette off "
              "Libya and hit a cargo ship in the Gulf of Finland. NATO "
              "vows space defence amid reports of a Russian nuclear "
              "satellite.",
              font(SANS, 21), 440)

    rule(d, 36, 736, 988)
    d.line([(504, 496), (504, 724)], fill=LINE, width=2)

    # ---------- row 3: Cartagena | Also on Tuesday ----------
    y = 752
    y1 = kicker(d, (36, y), "Colombia  ·  Tue 24 Nov")
    y1 = headline(d, (36, y1 + 2), "30 hostages seized in\nCartagena supermarket", 34, 440)
    y1 = para(d, (36, y1 + 6),
              "Gunmen took about 30 hostages in an Éxito supermarket "
              "after a failed armoured-truck robbery. Ten were freed; "
              "about 20 still held.",
              font(SANS, 20), 440)
    x2 = 528
    y2 = kicker(d, (x2, y), "Also on Tuesday", color=NAVY2)
    yy = y2 + 4
    yy = bullet(d, x2, yy, "Nasdaq -1.5% and Nvidia -6% on tariff-hike "
                "report.", font(SANS, 19), 440)
    yy = bullet(d, x2, yy + 6, "CIA and ODNI hit by cyber breach.",
                font(SANS, 19), 440)
    yy = bullet(d, x2, yy + 6, "Huawei guilty of stealing trade secrets.",
                font(SANS, 19), 440)
    yy = bullet(d, x2, yy + 6, "Sarkozy and Carla Bruni ordered to trial.",
                font(SANS, 19), 440)

    # ---------- footer ----------
    d.rectangle([0, 948, W, H], fill=NAVY)
    d.text((36, 958), "ALSO IN WEDNESDAY'S NEWS  —",
           font=font(SANS_B, 20), fill=GOLD)
    d.text((36, 980), "Iran flogs singer Parastoo Ahmadi 74 lashes  ·  "
           "Gaza death toll 74,746  ·  Russian deaths in Mali",
           font=font(SANS, 19), fill=(255, 255, 255))
    d.text((36, 1004), "Sources: Reuters · AP · Xinhua · CNN · BBC · WSJ · "
           "AFP — as reported 25 Nov 2026",
           font=font(SANS, 16), fill=(170, 185, 200))

    img.save(OUT, format="PNG", optimize=True)
    print(f"wrote {OUT} {W}x{H}")


if __name__ == "__main__":
    main()

# The World in One Day — Wednesday 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/yandreload/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/yandreload/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Entry for the make.fun bounty
[Sum up 25 November's world news in one image](https://make.fun/bounty/news-image-20261125)
($100 USDC, 50 paid places, closes Fri 27 Nov 2026 07:00 WIB).

## The image

A 1024×1024 newspaper front page, "THE WORLD IN ONE DAY", summing up
Wednesday 25 November 2026 in 11 dated stories across 5 regions:

- **Lead — Space (Wed 25 Nov):** China's Shenzhou-24 launches, carrying
  Muhammad Zeeshan Ali — the first Pakistani in orbit and the first
  foreign astronaut aboard the Tiangong space station.
- **Gulf (overnight into Wed 25 Nov):** Houthi drone hits Riyadh's
  tallest tower, wounding 11; Saudi-led coalition strikes Hodeidah port
  overnight.
- **Ukraine (Tue–Wed):** Moscow calls Ukrainian ship strikes
  "terrorism" after Kyiv confirms sinking a Russian corvette off Libya
  and hitting a cargo ship in the Gulf of Finland; NATO vows space
  defence amid reports of a Russian nuclear satellite.
- **Colombia (Tue 24 Nov):** gunmen take about 30 hostages in a
  Cartagena supermarket after a failed armoured-truck robbery.
- **Also on Tuesday:** Nasdaq -1.5% and Nvidia -6% on a tariff-hike
  report; CIA and ODNI hit by a cyber breach; Huawei guilty of stealing
  trade secrets; Sarkozy and Carla Bruni ordered to trial.
- **Also in Wednesday's news:** Iran flogs singer Parastoo Ahmadi
  74 lashes; Gaza death toll 74,746; leaked data on Russian deaths
  in Mali.

Sources for every story: see [SOURCES.md](SOURCES.md).

## How it is built

- `generate.py` — local build tool (Pillow + Liberation fonts). Renders
  `entry.png` from the fixed story text. Not the entrypoint.
- `entry.png` — the committed entry image, 1024×1024, under 1 MiB.
- `main.py` — the entrypoint (Python 3.13, stdlib only). It copies
  `entry.png` to `/output/entry.png`, exactly as the brief suggests
  ("the simplest program copies an image the repository holds"). No
  network, no randomness: two runs write identical bytes.

## Run it

```sh
python3 main.py        # writes /output/entry.png
```

## Verify

```sh
python3 main.py && sha256sum /output/entry.png
python3 main.py && sha256sum /output/entry.png   # same hash
python3 -c "from PIL import Image; im = Image.open('/output/entry.png'); print(im.size, im.format)"
```

## License

MIT — see [LICENSE](LICENSE).

# The World in One Day — Wednesday 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/yandreload/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/yandreload/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Entry for the make.fun bounty
[Sum up 25 November's world news in one image](https://make.fun/bounty/news-image-20261125)
($100 USDC, 50 paid places, closes Fri 27 Nov 2026 07:00 WIB).

## The image

A 1024×1024 newspaper front page, "THE WORLD IN ONE DAY", summing up
Wednesday 25 November 2026 in eleven stories from five regions:

- **Lead — Space:** China's Shenzhou-24 launches, carrying Muhammad
  Zeeshan Ali — the first Pakistani in orbit and the first foreign
  astronaut aboard the Tiangong station.
- **The Gulf:** a Houthi drone hits Riyadh's tallest tower, wounding
  11; the Saudi-led coalition strikes Hodeidah port overnight.
- **Ukraine:** Kyiv confirms sinking the Russian corvette Merkury;
  Moscow calls the ship strikes "terrorism".
- **Colombia:** gunmen hold about 30 hostages in a Cartagena
  supermarket after a failed armoured-truck robbery.
- **Markets:** Nasdaq down 1.5% and Nvidia about 6% on a tariff-hike
  report; **Security:** the CIA and ODNI hit by a cyber breach;
  **Tech:** Huawei found guilty of stealing trade secrets.
- **France:** Sarkozy and Carla Bruni ordered to trial.
  **Iran:** singer Parastoo Ahmadi lashed 74 times.
  **Gaza:** death toll reaches 74,746. **Mali:** leaked data on
  Russian deaths.

Every story is dated on the image or in [SOURCES.md](SOURCES.md).

## How it is built

- `generate.py` — the build tool (Python 3.13 + Pillow). It draws the
  whole front page from the fixed story text in the file and writes
  `entry.png`. Run it to rebuild the image.
- `entry.png` — the committed entry image, 1024×1024, under 1 MiB.
- `main.py` — the entrypoint (Python 3.13, standard library only). It
  copies `entry.png` to `/output/entry.png`. No network, no
  randomness: two runs write identical bytes.

## Run it

```sh
python3 generate.py   # rebuild entry.png from the story text
python3 main.py       # writes /output/entry.png
```

## Verify

```sh
python3 main.py && sha256sum /output/entry.png
python3 main.py && sha256sum /output/entry.png   # same hash
python3 -c "from PIL import Image; im = Image.open('/output/entry.png'); print(im.size, im.format)"
```

## License

MIT — see [LICENSE](LICENSE).

#!/usr/bin/env python3
"""Entry for make.fun bounty "Sum up 25 November's world news in one image"
(slug: news-image-20261125).

The entry image is committed in this repository as entry.png (rendered
locally by generate.py from the news of Wednesday 25 November 2026; see
SOURCES.md for the stories and their sources). This program only copies
that image to /output/entry.png, exactly as the bounty brief suggests:
"the simplest program copies an image the repository holds".

Stdlib only, no network, no randomness, no timestamps: running it twice
writes the same bytes both times.
"""

import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
DEST = Path("/output/entry.png")


def main() -> None:
    DEST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    print(f"wrote {DEST} ({DEST.stat().st_size} bytes)")


if __name__ == "__main__":
    main()

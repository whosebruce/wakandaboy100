#!/usr/bin/env python3
"""Add an Instagram/YouTube media card without self-hosting the video.

Example:
  python scripts/add_media.py --category comedy --title "Clip title" \
    --platform "Instagram Reel" --url "https://www.instagram.com/reel/.../"
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter, ImageOps

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "content/media.json"
IMAGES = ROOT / "assets/images"


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug[:64] or "media"


def create_card(source: Path, destination: Path) -> None:
    image = Image.open(source).convert("RGB")
    background = ImageOps.fit(image, (1200, 675), method=Image.Resampling.LANCZOS)
    background = background.filter(ImageFilter.GaussianBlur(28))
    background = ImageEnhance.Brightness(background).enhance(0.58)
    foreground = ImageOps.contain(image, (430, 640), method=Image.Resampling.LANCZOS)
    x = (1200 - foreground.width) // 2
    y = (675 - foreground.height) // 2
    background.paste(foreground, (x, y))
    background.save(destination, "WEBP", quality=88, method=6)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--category", default="comedy")
    parser.add_argument("--title", required=True)
    parser.add_argument("--platform", required=True)
    parser.add_argument("--url", required=True)
    parser.add_argument("--description", default="A public clip from Collins Wewa.")
    args = parser.parse_args()

    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    entries = catalog.setdefault(args.category, [])
    if any(item.get("url") == args.url for item in entries):
        raise SystemExit(f"URL already exists in {args.category}: {args.url}")

    slug = slugify(args.title)
    destination = IMAGES / f"{slug}-card.webp"
    if destination.exists():
        raise SystemExit(f"Refusing to overwrite existing thumbnail: {destination}")

    yt_dlp = shutil.which("yt-dlp")
    if not yt_dlp:
        raise SystemExit("yt-dlp is required to fetch the public platform thumbnail")

    with tempfile.TemporaryDirectory(prefix="wakanda-media-") as temp:
        output = str(Path(temp) / "source.%(ext)s")
        subprocess.run(
            [yt_dlp, "--skip-download", "--write-thumbnail", "-o", output, args.url],
            check=True,
        )
        candidates = [p for p in Path(temp).iterdir() if p.is_file()]
        if not candidates:
            raise SystemExit("No thumbnail was downloaded")
        create_card(candidates[0], destination)

    entries.append(
        {
            "title": args.title,
            "platform": args.platform,
            "url": args.url,
            "thumbnail": f"/assets/images/{destination.name}",
            "description": args.description,
        }
    )
    CATALOG.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    subprocess.run(["python", "scripts/build_site.py"], cwd=ROOT, check=True)
    subprocess.run(["python", "scripts/verify_site.py"], cwd=ROOT, check=True)
    print(f"Added {args.title} to {args.category}: {destination.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Fail-closed checks for the production GitHub Pages tree."""
from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "index.html": "https://wakandaboy100.com/",
    "about/index.html": "https://wakandaboy100.com/about/",
    "videos/index.html": "https://wakandaboy100.com/videos/",
    "music/index.html": "https://wakandaboy100.com/music/",
    "booking/index.html": "https://wakandaboy100.com/booking/",
    "merch/the-ultimate-cardio/index.html": "https://wakandaboy100.com/merch/the-ultimate-cardio/",
}
FORBIDDEN = (
    "{{", "<sc-", "<x-dc", "support.js", "data-dc-", "shopify.com", "shop.wakandaboy100.com",
    "Fourthwall", "Bella+Canvas", "DTG", "vendor proof", "owner invite", "approved direction",
    "garment direction", "Front quiet", "Store status:",
)


class AuditParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self.in_title = False
        self.h1_count = 0
        self.links: list[str] = []
        self.assets: list[str] = []
        self.meta: dict[str, str] = {}
        self.canonicals: list[str] = []
        self.jsonld: list[str] = []
        self._json_buffer: list[str] | None = None

    def handle_starttag(self, tag: str, attrs) -> None:
        data = dict(attrs)
        href = data.get("href")
        src = data.get("src")
        if tag == "title":
            self.in_title = True
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "a" and isinstance(href, str):
            self.links.append(href)
        elif tag in {"img", "script"} and isinstance(src, str):
            self.assets.append(src)
        elif tag == "link" and isinstance(href, str):
            rel = data.get("rel") or ""
            if "canonical" in rel:
                self.canonicals.append(href)
            elif href.startswith("/"):
                self.assets.append(href)
        elif tag == "meta":
            key = data.get("name") or data.get("property")
            content = data.get("content")
            if isinstance(key, str) and isinstance(content, str):
                self.meta[key] = content
        if tag == "script" and data.get("type") == "application/ld+json":
            self._json_buffer = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False
        if tag == "script" and self._json_buffer is not None:
            self.jsonld.append("".join(self._json_buffer))
            self._json_buffer = None

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data
        if self._json_buffer is not None:
            self._json_buffer.append(data)


def local_target(url: str, current_page: Path) -> Path | None:
    parsed = urlparse(url)
    if parsed.scheme or parsed.netloc or not parsed.path or parsed.path.startswith("#"):
        return None
    path = parsed.path
    if path.startswith("/"):
        candidate = ROOT / path.lstrip("/")
    else:
        candidate = current_page.parent / path
    if path.endswith("/"):
        candidate = candidate / "index.html"
    candidate = candidate.resolve()
    try:
        candidate.relative_to(ROOT.resolve())
    except ValueError:
        return ROOT / "__outside_project__"
    return candidate


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []
    found_canonicals: set[str] = set()
    all_internal_routes: set[str] = set()

    for rel, expected_canonical in EXPECTED.items():
        page = ROOT / rel
        if not page.is_file():
            fail(errors, f"missing page: {rel}")
            continue
        text = page.read_text(encoding="utf-8")
        lower = text.lower()
        for marker in FORBIDDEN:
            if marker.lower() in lower:
                fail(errors, f"{rel}: forbidden marker {marker!r}")
        parser = AuditParser()
        parser.feed(text)
        title = re.sub(r"\s+", " ", parser.title).strip()
        description = parser.meta.get("description", "")
        if not title or len(title) > 65:
            fail(errors, f"{rel}: title length {len(title)}")
        if not 80 <= len(description) <= 180:
            fail(errors, f"{rel}: description length {len(description)}")
        if parser.h1_count != 1:
            fail(errors, f"{rel}: expected one H1, got {parser.h1_count}")
        if parser.canonicals != [expected_canonical]:
            fail(errors, f"{rel}: canonical mismatch {parser.canonicals}")
        found_canonicals.update(parser.canonicals)
        if not parser.jsonld:
            fail(errors, f"{rel}: missing JSON-LD")
        for raw in parser.jsonld:
            try:
                json.loads(raw)
            except json.JSONDecodeError as exc:
                fail(errors, f"{rel}: invalid JSON-LD: {exc}")
        for href in parser.links:
            if href.startswith("#") and href != "#main":
                fail(errors, f"{rel}: public fragment navigation {href}")
            target = local_target(href, page)
            if target is not None:
                all_internal_routes.add(href)
                if not target.exists():
                    fail(errors, f"{rel}: broken internal link {href} -> {target.relative_to(ROOT)}")
        for src in parser.assets:
            target = local_target(src, page)
            if target is not None and not target.exists():
                fail(errors, f"{rel}: missing local asset {src}")

    required_terms = {
        "index.html": ["Collins Wewa", "WAKANDABOY100", "The Ultimate Cardio"],
        "about/index.html": ["Collins Wewa", "WAKANDABOY100"],
        "videos/index.html": ["Comedy skits", "I’m Habibi, Without the Oil Money", "Instagram Reel"],
        "merch/the-ultimate-cardio/index.html": ["The Ultimate Cardio", "WAKANDABOY100"],
    }
    for rel, terms in required_terms.items():
        text = (ROOT / rel).read_text(encoding="utf-8")
        for term in terms:
            if term.lower() not in text.lower():
                fail(errors, f"{rel}: missing entity term {term}")

    sitemap = ROOT / "sitemap.xml"
    try:
        root = ET.fromstring(sitemap.read_text(encoding="utf-8"))
        ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        urls = {node.text for node in root.findall("s:url/s:loc", ns) if node.text}
        expected_urls = set(EXPECTED.values())
        if urls != expected_urls:
            fail(errors, f"sitemap mismatch missing={sorted(expected_urls-urls)} extra={sorted(urls-expected_urls)}")
    except Exception as exc:
        fail(errors, f"sitemap parse failure: {exc}")

    tracked_forbidden = [
        "WAKANDABOY100.dc.html",
        "support.js",
        "deck-stage.js",
        "Brand Guidelines.dc.html",
        "Brand Guidelines Deck.dc.html",
    ]
    for name in tracked_forbidden:
        if (ROOT / name).exists():
            fail(errors, f"prototype/runtime artifact must not ship: {name}")

    style = (ROOT / "style.css").read_text(encoding="utf-8")
    required_style_guards = {
        "transparent navigation mark": ".brand-mark{display:grid;place-items:center;width:42px;height:42px;background:transparent;overflow:visible}",
        "root footer-color fallback": "html{scroll-behavior:smooth;background:#0e0e12;overscroll-behavior-y:none}",
        "body overscroll containment": "overflow-x:hidden;overscroll-behavior-y:none}",
    }
    for label, marker in required_style_guards.items():
        if marker not in style:
            fail(errors, f"style.css: missing {label}")

    if errors:
        print("SITE VERIFICATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("SITE VERIFICATION PASSED")
    print(f"pages={len(EXPECTED)} canonicals={len(found_canonicals)} internal_routes={len(all_internal_routes)}")
    print("prototype_markers=0 forbidden_shopify_links=0 public_fragment_routes=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

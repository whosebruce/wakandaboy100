# WAKANDABOY100 Artist Portfolio

Production static portfolio for **Collins Wewa / WAKANDABOY100** at <https://wakandaboy100.com>.

## Route map

- `/` — official brand home
- `/about/` — Collins Wewa biography/entity page
- `/videos/` — music video and performance catalog
- `/music/` — verified streaming profiles
- `/booking/` — private-event inquiry guidance
- `/merch/the-ultimate-cardio/` — public Drop 001 preview and coming-soon page

Public navigation uses real directory-index routes. There is no HashRouter; the only fragment is the accessibility skip link to `#main`.

## Build and verification

```bash
python scripts/build_site.py
python scripts/verify_site.py
```

The GitHub Pages workflow rebuilds and verifies the same source before uploading the deployment artifact. Verification fails on missing routes/assets, unresolved Design Component runtime markers, invalid JSON-LD, broken internal links, stale Shopify links, public fragment navigation, sitemap drift, or missing entity terms.

## Adding public media

Keep videos on Instagram or YouTube and add them to the website catalog with:

```bash
python scripts/add_media.py \
  --category comedy \
  --title "Public clip title" \
  --platform "Instagram Reel" \
  --url "https://www.instagram.com/reel/.../" \
  --description "Short public description."
```

The helper downloads the platform’s public cover, creates a stable landscape website card, updates `content/media.json`, rebuilds the site, and runs deterministic verification. It does not download or republish the video.

## Brand and commerce state

- Approved dancer mark: `assets/images/wakandaboy100-dancer.svg`
- Approved shirt reference derivative: `assets/images/the-ultimate-cardio-shirt.webp`
- Visual system: athletic heather grey, ink black, paper white; Anton + Barlow Condensed
- Public merchandise copy is limited to launch-ready statements; checkout remains offline until an official release is announced
- Do not publish placeholder products, invented prices, unsupported biography claims, or a dead store link

See `DESIGN.md`, `DESIGN-DIRECTION.md`, and `OPEN_DESIGN.md` for the editable design contract.

# WAKANDABOY100 Artist Portfolio

Production static portfolio for **Collins Wewa / WAKANDABOY100** at <https://wakandaboy100.com>.

## Route map

- `/` — official brand home
- `/about/` — Collins Wewa biography/entity page
- `/videos/` — music video and performance catalog
- `/music/` — verified streaming profiles
- `/booking/` — private-event inquiry guidance
- `/merch/the-ultimate-cardio/` — approved Drop 001 direction and Fourthwall status

Public navigation uses real directory-index routes. There is no HashRouter; the only fragment is the accessibility skip link to `#main`.

## Build and verification

```bash
python scripts/build_site.py
python scripts/verify_site.py
```

The GitHub Pages workflow rebuilds and verifies the same source before uploading the deployment artifact. Verification fails on missing routes/assets, unresolved Design Component runtime markers, invalid JSON-LD, broken internal links, stale Shopify links, public fragment navigation, sitemap drift, or missing entity terms.

## Brand and commerce state

- Approved dancer mark: `assets/images/wakandaboy100-dancer.svg`
- Approved shirt reference derivative: `assets/images/the-ultimate-cardio-shirt.webp`
- Visual system: athletic heather grey, ink black, paper white; Anton + Barlow Condensed
- Commerce platform: Fourthwall Free selected; public checkout remains offline until Wewa creates the owner account and invites Bruce Works as Manager
- Do not publish placeholder products, invented prices, unsupported biography claims, or a dead store link

See `DESIGN.md`, `DESIGN-DIRECTION.md`, and `OPEN_DESIGN.md` for the editable design contract.

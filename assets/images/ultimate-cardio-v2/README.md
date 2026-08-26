# The Ultimate Cardio Campaign v2 Assets

Created for the full nine-style website refresh on 2026-08-25 PDT.

## Campaign images

These GPT Image 2 editorial images are used for campaign atmosphere, not as the source of truth for product specifications:

- `collection-flatlay.webp` — homepage and final collection hero
- `stadium-lifestyle.webp` — merchandise page hero
- `hoodie-locker.webp` — hoodie spotlight
- `training-tops.webp` — men’s tank / women’s crop spotlight
- `headwear-locker.webp` — cap and beanie spotlight
- `shorts-track.webp` — right-leg shorts spotlight

Each was generated from current official Fourthwall product renders and visually checked for composition, garment family, color direction, placement, anatomy, and obvious artifacts. Small wordmarks in generated campaign photography can be imperfect; the product grid therefore uses the official storefront renders below.

## Official product renders

- `product-tshirt.webp`
- `product-hoodie.webp`
- `product-cap.webp`
- `product-beanie.webp`
- `product-mens-tank.webp`
- `product-mens-across.webp`
- `product-womens-crop.webp`
- `product-womens-across.webp`
- `product-shorts.webp`

The official render cards and `content/merch.json` are the source of truth for product names, starting prices, colors, links, and customer expectations.

## Rules

1. Do not use a campaign image to prove an exact print region, stitch color, size, or available variant.
2. Keep product names, prices, and links synchronized with `https://shop.wakandaboy100.com/collections/all`.
3. Never reintroduce the retired `Drop 001` or `collins-wewa-shop.fourthwall.com` links.
4. Build and verify with:

```bash
python scripts/build_site.py
python scripts/verify_site.py
```

# Open Design handoff — WAKANDABOY100 Brand Website

## Canonical workspace

This Git repository is the production source of truth. It is imported into Open Design as an external-folder project so visual changes can be reviewed against the same HTML/CSS/assets that GitHub Pages serves.

- Entry page: `index.html`
- Shared design system: `style.css` and `DESIGN.md`
- Shared behavior: `script.js`
- Page source generator: `scripts/build_site.py`
- Deterministic verifier: `scripts/verify_site.py`

## Editable routes

- `index.html`
- `about/index.html`
- `videos/index.html`
- `music/index.html`
- `booking/index.html`
- `merch/the-ultimate-cardio/index.html`

## Rules for Open Design revisions

1. Preserve the athletic heather/black/white direction and approved dancer mark.
2. Keep WAKANDABOY100 and Collins Wewa visibly connected.
3. Keep public navigation on clean directory-index routes; do not introduce HashRouter or section-fragment navigation.
4. Do not ship `.dc.html`, `support.js`, `deck-stage.js`, Mustache markers, or Open Design prototype runtime helpers.
5. Do not invent prices, products, biography facts, availability, reviews, fulfillment promises, or social proof.
6. Until an official release is announced, merch remains clearly `coming soon` with no dead checkout URL.
7. After editing generated HTML, mirror the approved change into `scripts/build_site.py` or the next build will overwrite it.
8. Run `python scripts/build_site.py && python scripts/verify_site.py`, then verify desktop and 390px mobile screenshots before publication.

## Approved source fingerprints

- Dancer SVG SHA-256: `a827ead2359cb256a2e5b2362e3cebf5f3f932b3e789bccdc7a894bee43e1738`
- Original shirt mockup SHA-256: `3b966b168947cc93ac8ddf82abd8bbd698e1aa505972a7f61a927b9c21a5f579`

Open Design may refine layout and responsive presentation, but these protected sources require an explicit owner-approved creative change before replacement.

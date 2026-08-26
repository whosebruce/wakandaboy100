# Design direction — WAKANDABOY100

## Creative thesis

A clean athletic/collegiate performer identity: **heather grey, ink black, paper white, oversized condensed typography, deliberate restraint, and movement supplied by the WAKANDABOY100 dancer mark.** This supersedes the former dark neon night-stage direction.

## Visual system

- **Primary background:** Heather Grey `#D5D5D9`
- **Primary ink:** Ink Black `#15151A`
- **Cards/reversed type:** Paper White `#F7F7F4`
- **Dark panels:** Panel Charcoal `#1D1D23`
- **Secondary text:** Stone `#56565E`
- **Display type:** Anton, uppercase
- **UI/labels:** Barlow Condensed 500/600/700
- **Body:** Helvetica Neue / Helvetica / Arial
- **Corners:** restrained 8px radii; no pill-heavy UI
- **Texture:** subtle monochrome grain only

## Content hierarchy

1. WAKANDABOY100 and Collins Wewa are visibly connected above the fold.
2. “My Baby” is the flagship public proof point.
3. Music/video/booking/merch each receive a real crawlable route.
4. The Ultimate Cardio is positioned as `The Ultimate Cardio by WAKANDABOY100`, not generic fitness content.
5. Merchandise status must be truthful: the site presents the nine live products and sends checkout to the exact `shop.wakandaboy100.com` collection/product URLs.

## Motion and responsive rules

- Marquee is decorative and disabled under reduced-motion preferences.
- Navigation collapses to an accessible mobile menu.
- No horizontal overflow at 390px.
- Type scales with `clamp()` rather than fixed desktop dimensions.
- External video thumbnails load below the fold with explicit dimensions.

## Protected assets

- Do not redraw or substitute the dancer mark.
- Do not alter merchandise wording, print composition, garment direction, or color mapping without owner approval.
- Production print art, a technical placement proof, and a storefront mockup are separate deliverables.
- Generated lifestyle photography is a campaign layer; official storefront renders remain the product-reference layer.

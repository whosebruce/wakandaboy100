# WAKANDABOY100 Design System

## Brand statement

**WAKANDABOY100 is Collins Wewa: performer first, independent by design, playful without looking amateur.** The interface behaves like athletic editorial packaging—large type, black/grey contrast, compact labels, movement, and clear proof.

## Tokens

| Token | Value | Use |
|---|---|---|
| Heather Grey | `#D5D5D9` | Primary canvas |
| Ink Black | `#15151A` | Type, CTAs, dark sections |
| Panel Charcoal | `#1D1D23` | Secondary dark surfaces |
| Paper White | `#F7F7F4` | Cards and reversed type |
| Stone | `#56565E` | Secondary text |
| Hairline | `rgba(21,21,26,.16)` | Borders and section rules |

## Typography

- Anton 400: display headlines and large numerical proof
- Barlow Condensed 500/600/700: navigation, labels, buttons, stats, chips
- Helvetica Neue / Helvetica / Arial: readable body copy
- Impact words use uppercase; body copy stays sentence case

## Components

- Sticky translucent header with square dancer mark
- Display hero with visible `Collins Wewa / Comedy · Music · Dance` identity line
- Full-width black marquee for brand rhythm
- White proof cards on heather background
- Dark merch band with approved shirt reference
- Route-specific page hero with dancer-mark panel
- Restrained 8px corners; no ornamental pills
- Buttons use square two-pixel borders and high-contrast fills

## Responsive contract

- Desktop max width: 1200px
- Primary breakpoint: 900px
- Narrow mobile proof: 390px × 844px
- Header becomes an explicit Menu button
- Grids collapse without horizontal scrolling
- Typography and hero art scale through `clamp()` and bounded heights
- Reduced motion disables marquee animation and transitions

## Content and commerce guardrails

- WAKANDABOY100, Collins Wewa, and The Ultimate Cardio remain explicit entities.
- The Ultimate Cardio product direction can be shown before launch, but checkout availability and price cannot be implied.
- Checkout remains offline until an official release is announced.
- Never invent testimonials, clients, prices, inventory, shipping promises, or product photography.

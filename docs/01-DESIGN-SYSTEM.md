# The design system

Everything visual in this deck comes from one inline `<style>` block inside the HTML file. There is
no external stylesheet, no framework, no build step. If you keep that block intact and reuse the
class names below, anything you add will look like it belongs.

---

## Colour tokens

Every colour in the deck is a CSS variable declared once at the top of the style block. Change a
value there and it updates everywhere.

```css
:root {
  /* Surfaces */
  --bg: #0a0a12;                          /* page background */
  --bg-2: #0f0f1e;                        /* card gradient bottom */
  --card: #13132a;                        /* card background top */
  --card-2: #1a1a35;                      /* card hover background */
  --card-border: rgba(255,255,255,0.08);
  --card-border-hover: rgba(255,255,255,0.16);

  /* Brand accent. THIS IS THE ONE YOU CHANGE. */
  --accent: #8b5cf6;
  --accent-bright: #a78bfa;
  --accent-deep: #7c3aed;
  --accent-soft: rgba(139,92,246,0.1);

  /* Semantic colours */
  --green: #22c55e;        --green-bright: #4ade80;   --green-soft: rgba(34,197,94,0.1);
  --red: #ef4444;                                     --red-soft: rgba(239,68,68,0.1);
  --amber: #f59e0b;                                   --amber-soft: rgba(245,158,11,0.1);
  --cyan: #06b6d4;
  --pink: #ec4899;

  /* Text */
  --text: #f0f0f5;             /* headlines */
  --text-2: #cbcbe0;           /* body copy */
  --text-secondary: #9898b4;   /* labels, captions */
  --text-muted: #5a5a78;       /* footer, fine print */

  /* Radii */
  --radius: 18px;              --radius-sm: 12px;

  /* Gradients */
  --gradient:       linear-gradient(135deg, #7c3aed, #8b5cf6, #a78bfa);
  --gradient-green: linear-gradient(135deg, #16a34a, #22c55e, #4ade80);
  --gradient-fire:  linear-gradient(135deg, #f59e0b, #ef4444, #ec4899);
}
```

### Rebranding it to your colour

Change these five values and the whole deck follows:

1. `--accent` to your brand colour
2. `--accent-bright` to a lighter tint of it
3. `--accent-deep` to a darker shade of it
4. `--accent-soft` to the same colour at 10 percent opacity
5. `--gradient` to run deep, base, bright

Leave green, red and amber alone. They carry meaning rather than brand, and a deck where the
"problem" colour is also the brand colour is confusing to read.

**A warning about light backgrounds.** This deck is built dark. Flipping `--bg` to white does not
work: the ambient orbs, the card gradients, the glow shadows and the text tokens all assume a dark
ground. If you need a light deck, that is a rebuild, not a token change.

### What each colour means

| Colour | Used for |
|---|---|
| Accent (violet by default) | brand chrome, primary actions, neutral highlights |
| Green | solutions, benefits, results, money returned |
| Red | problems, pain, cost, the old way |
| Amber | warnings, standing still, edge cases |
| Cyan and pink | rotation only, when you need to tell five or more items apart |

Use colour to carry meaning consistently. If green means "good outcome" on slide 3, it cannot mean
"our tier two package" on slide 10.

---

## Typography

Two families, loaded from Google Fonts:

- **Inter** at weights 400 to 900. Everything by default.
- **Playfair Display** italic. Pull quotes only, used sparingly. It earns its impact by being rare.

| Element | Size | Weight | Tracking | Leading |
|---|---|---|---|---|
| h1 (cover only) | clamp(42px, 4.8vw, 68px) | 800 | -0.02em | 1.12 |
| h2 (slide title) | clamp(36px, 4.4vw, 52px) | 800 | -0.02em | 1.12 |
| h3 (section label) | 26px | 800 | -0.02em | 1.12 |
| h4 (card title) | 18 to 22px | 700 | -0.01em | 1.12 |
| Body paragraph | 14.5 to 16px | 400 | 0 | 1.6 to 1.7 |
| `.subtitle` | 20px | 400 | 0 | 1.55 |
| `.eyebrow` | 12px | 700 | 0.16em, uppercase | 1 |
| Uppercase labels | 11px | 800 | 0.14em, uppercase | 1 |
| Hero numbers | 42 to 140px | 900 | -0.04em, tabular | 1.05 |

**Type rules that are not optional:**

- Headings and subtitles use `text-wrap: balance`, card copy uses `text-wrap: pretty`. Both are
  already set. They stop single words being stranded on their own line.
- Hero numbers use `font-variant-numeric: tabular-nums` so digits line up in columns, and
  `display: block` so they do not break when combined with the gradient text classes.
- Nothing below 12px in body copy.
- The type scale is deliberately narrow. Resist adding sizes between the ones listed.

---

## Components

Every one of these is already in the style block. Use them rather than writing new CSS.

| Class | What it is |
|---|---|
| `.card` | The default container. Variants: `.card-red`, `.card-green`, `.card-violet`, `.card-amber`, `.card-glow` change border and background tint. |
| `.glow-card` | The centred call-out that closes most slides. Gradient background and soft glow. Use for the one line you want them to remember. |
| `.criteria-card` | Big number on the left, heading and description on the right. Variants `.cc-1` to `.cc-5` cycle the left border through accent, green, amber, cyan, pink. |
| `.fact-card` | Compact stat: small uppercase label, big gradient number, tiny description. |
| `.scenario-card` | A projection column. Rate label, big percentage, internal stat rows, then a green net-result box at the bottom. |
| `.bonus-card` | Green-bordered card with a top stripe, icon, headline, body, and a struck-through value at the bottom. |
| `.line-item` | A row in an itemised list. `.li-icon` square, `.li-left` name and description, `.li-right` price. `.line-item.total` for the total row. |
| `.pricing-card` | A pricing column with badge ribbon, label, headline, big price, description. `.featured` adds the floating recommended badge. |
| `.video-wrap` | 16:9 container for a case study thumbnail, with a `.play-btn` overlay. |
| `.timeline` | Vertical timeline with a connector line and markers. Add `.milestone` to a row for the highlighted treatment. |
| `.engine-step` | A card in a sequential process row. Icon, label, body, tag at the bottom. |
| `.badge` | Inline pill. `.badge-accent`, `.badge-green`, `.badge-amber`, `.badge-red`, `.badge-glow-green`. |
| `details` | Native HTML disclosure, styled as a card. Closed shows a plus, open tints and rotates it to a cross. Used for the FAQ. |
| `.math-cascade` and `.math-stage` | Horizontal flow of stages with multiply and equals signs between them. Good for showing arithmetic. |

### Template additions

Three things were added to the stylesheet for this template that were not in the original deck:

| Class | What it does |
|---|---|
| `.ph` | A dashed placeholder box standing in for an image you have not added. Variants: `.ph-16x9`, `.ph-square`, `.ph-avatar`, `.ph-logo`, `.ph-wide`. |
| Orphan guard | A lone card in the last row of a three or four column grid stretches to full width automatically. |
| `align-items: stretch` | Set on every grid so cards in a row are always equal height. |

To swap a placeholder for a real image, replace the whole `<div class="ph ...">` with an `<img>`
carrying the same dimensions:

```html
<img src="assets/your-image.png" alt="" style="width:100%; height:auto; display:block; border-radius:12px;">
```

Round headshots use `border-radius:50%` and a fixed width and height.

---

## Layout

```css
.slide-inner { width: 100%; max-width: 1440px; }
```

**Every slide runs full width.** Content concentrated in a narrow column with empty gutters is the
single fastest way to make a deck look like a document.

- Grids: `.grid-2`, `.grid-3`, `.grid-4`, gap 18 to 22px.
- Vertical rhythm: space sections with `mb-24`. Do not stack `mb-24` on one element and `mt-24` on
  the next, that produces a 48px gap that reads as a mistake.
- Slide padding: `56px` top, `44px` sides, `88px` bottom. The deep bottom padding is deliberate, it
  keeps content clear of the navigation bar.

---

## Animation

Direct children of an active slide's inner container rise 20px and fade in over 600ms, staggered
80ms apart. Only the first six children stagger, after that they arrive together, which stops long
slides feeling slow.

The background is three blurred orbs drifting on a 22 second loop. They are decorative and cheap.
If you want a calmer deck, delete the `.ambient` div near the top of the body.

---

## Navigation

A short script at the bottom of the file builds the dot navigation from the number of slides.

- Arrow keys, spacebar and Page Down move forward
- Left arrow and Page Up move back
- Home and End jump to the first and last slide
- Swipe works on touch devices
- Clicking a dot jumps to that slide

The script finds slides by their `data-slide` attribute, not by document order. Every slide must be
numbered 1 to N with no gaps or you will get a dot that navigates nowhere. The `data-tag` attribute
is what shows in the top right corner.

---

## Hard rules

- No em dashes anywhere
- No widow lines in headings, subtitles or card copy
- All slides full width
- `data-slide` sequential from 1, no gaps
- Hero numbers always `display: block`
- No inline icon smaller than 16px or larger than 32px
- 16:9 on every video thumbnail
- Every clickable element has a hover state: a lift, a border change, or a shadow
- One currency throughout

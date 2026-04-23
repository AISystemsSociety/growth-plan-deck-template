# Growth Plan Deck Template

A 21-slide HTML growth plan presentation template for service businesses, plus the methodology skill for turning raw discovery-call data into a deck that survives CFO-level scrutiny.

## What's in this repo

| File | What it is | When to load |
|---|---|---|
| `growth-plan-template.html` | The deck itself — single file, no dependencies | Open in a code editor, fill in `[PLACEHOLDER]` fields, open in a browser to preview |
| `growth-plan-deck-skill.md` | Template usage skill — 21-slide walkthrough, design system reference, deploy options | Load when you're filling in the template |
| `growth-plan-build-methodology.md` | Build methodology skill — data gathering, number defensibility, TAM validation, three-scenario close rates, copy rules, FAQ construction, iteration patterns, pre-ship checklist | Load when you're about to start a build and want to do it well |

## Install via the Starter Kit

```bash
bash <(curl -s https://raw.githubusercontent.com/AISystemsSociety/starter-kit/main/install.sh)
```

Or pull files directly:
```bash
curl -sL https://raw.githubusercontent.com/AISystemsSociety/growth-plan-deck-template/main/growth-plan-template.html -o growth-plan.html
curl -sL https://raw.githubusercontent.com/AISystemsSociety/growth-plan-deck-template/main/growth-plan-deck-skill.md -o ~/.claude/skills/growth-plan-deck.md
curl -sL https://raw.githubusercontent.com/AISystemsSociety/growth-plan-deck-template/main/growth-plan-build-methodology.md -o ~/.claude/skills/growth-plan-build-methodology.md
```

## Quick start

1. Open `growth-plan-template.html` in a code editor
2. Load `growth-plan-build-methodology.md` into Claude Code to walk through data gathering
3. Search `[PLACEHOLDER]` and replace with your real numbers
4. Preview in browser — arrow keys or swipe to navigate
5. Deploy via GitHub Pages, Netlify, or StatiCrypt (password protected)

## The persuasion arc

```
BLOCK 1 — PAIN       (slides 1-5)   Hook, listen back, gaps, cost, old vs new
BLOCK 2 — SOLUTION   (slide 6)      Your mechanism in one slide
BLOCK 3 — PILLARS    (slides 7-10)  Deep dives + bonuses
BLOCK 4 — PROOF      (slides 11-12) TAM math + case studies
BLOCK 5 — ANCHOR     (slides 13-14) Cost to DIY vs value stack
BLOCK 6 — OFFER      (slides 15-16) Guarantee then price
BLOCK 7 — CLOSE      (slides 17-21) ROI, worst case, Brunson close, timeline, summary
```

See `growth-plan-deck-skill.md` for the slide-by-slide reference.

## Hard rules (from the methodology file)

- No em dashes
- No widow words (last line of any block must have 3+ words, or bind with `&nbsp;`)
- Every number on every slide traces to: prospect statement, public benchmark, live tool screenshot, or your own offer math
- TAM slide must include a live screenshot, not a bare number
- Three close-rate columns (Conservative / Expected / Best). Conservative = industry cold-outbound floor, NOT the prospect's warm rate.
- Price never appears before slide 16
- 5 qualification criteria written down and signed off before week 1 if you're pricing per-outcome

## License

MIT. Use it, fork it, brand it however you like. Credit appreciated but not required.

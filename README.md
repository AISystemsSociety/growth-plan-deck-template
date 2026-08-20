# Growth Plan Deck Template (free)

A **20-slide sales presentation** you can make your own in about an hour and present on your next
call. Dark theme, full-screen slides, arrow-key and swipe navigation, works on a phone. One HTML
file, no dependencies, no build tools, no frameworks.

This is the deck structure behind real closed deals, stripped back to a blank. Every company name,
number, price, logo and screenshot in it is a placeholder waiting for yours. It is
**offer-agnostic**: it works whether you sell design, recruitment, bookkeeping, video, consulting
or lead generation.

It also ships with the reasoning. Not just the file, but why each slide is where it is, the design
rules that took about fifty rounds of live presenting to settle, and the mistakes that produced
them.

---

## Start here

**Using Claude Code or Claude?** Open `SKILL.md`. It interviews you about your offer, your prospect
and your numbers, then fills the deck in for you and checks it against the rules.

**Doing it by hand?** Open `CUSTOMIZE.md`. Step by step, written for non-coders, one command at the
end.

---

## What you get

| File | What it is |
|---|---|
| `template/growth-plan.template.html` | The whole deck. 20 slides, one file. |
| `template/values.example.json` | The quick fields: your name, links, prices, key numbers. |
| `build.py` | Fills your values in, copies your images, optionally sets a password. |
| `SKILL.md` | The guided build. Point Claude at it and answer the questions. |
| `CUSTOMIZE.md` | The manual build, for non-coders. |
| `assets/` | Drop your logo, headshots and screenshots here. |

And the part most templates leave out:

| Doc | What is in it |
|---|---|
| `docs/01-DESIGN-SYSTEM.md` | Colour tokens, type scale, every component class, how to rebrand it to your colour in five values. |
| `docs/02-SLIDE-ARCHITECTURE.md` | All 20 slides. What each one does, why it sits there, what happens if you move it. |
| `docs/03-DESIGN-RULES.md` | Every rule the deck is checked against, and the mistake behind each one. |
| `docs/04-ITERATIONS.md` | What changed across roughly fifty rounds of real sales calls, and why. |
| `docs/05-DEPLOY.md` | Getting it online free, with an optional password gate. |

---

## Quick start

```bash
# 1. copy the example values and edit them
cp template/values.example.json my-values.json     # then edit my-values.json

# 2. open template/growth-plan.template.html and replace the [bracketed] text
#    with your own words (see CUSTOMIZE.md)

# 3. build it
python3 build.py my-values.json out/

# 4. open out/index.html in a browser. Arrow keys move between slides.
```

To put a password on it and publish it free on GitHub Pages, see `docs/05-DEPLOY.md`.

---

## What you need before you fill this in

The deck does not work on generic filler. Before you start, you want:

- **Their numbers.** Average deal value, close rate, how many leads they get now.
- **Their words.** What they actually said is going wrong. Quote the call.
- **Their market.** How many potential buyers exist, and where that number came from.
- **Your offer.** What you deliver, what one delivered unit is, your price, your guarantee.
- **Your proof.** Two or three results you can evidence. Two real ones beat three invented ones.

If you have not had a discovery call yet, have the call first. A deck full of assumptions is worse
than no deck, because the first wrong number makes them doubt every other slide.

---

## The three rules that matter most

1. **Do not move the pricing slide earlier.** Everything before it exists to make the price look
   reasonable. Quote too early and you are quoting into a vacuum.
2. **Only guarantee what you control.** Guarantee your own outputs, never their business results.
3. **Delete rather than pad.** An empty slide is worse than a missing one.

The rest is in `docs/03-DESIGN-RULES.md`.

---

## Requirements

Python 3 for the build script. Node.js only if you want the optional password protection. A free
GitHub account if you want to host it. That is all.

---

Made to be used. Change it, rebrand it, sell with it.

*Sanitized for reuse. No client data, no real pricing, no production credentials.*

# Make it yours (no coding needed)

There are four kinds of things to change. Work through them in order. Budget about an hour the
first time, twenty minutes every time after that.

If you would rather be walked through it, open `SKILL.md` in Claude instead and answer its
questions.

---

## Before you start

Get these in front of you. The deck is only as good as these inputs:

- Notes or a transcript from your discovery call with this prospect
- Your prices, and what exactly is included
- Your average client's deal value and close rate, or theirs
- Two or three real results you can evidence
- Your logo, and headshots if you have a team

---

## 1. The quick fields, in `values.json`

Copy `template/values.example.json` to `my-values.json` and edit it. These get filled in
automatically when you build.

| Field | What it is |
|---|---|
| `DECK_TITLE` | Browser tab title, and the title on the password page if you use one |
| `YOUR_COMPANY` | Shown top-left on every slide |
| `YOUR_NAME`, `YOUR_EMAIL` | The signature on the cover and the closing slide |
| `WEBSITE_LINK`, `CTA_LINK` | Your site, and the link the final button points at |
| `PROSPECT_COMPANY` | Who this deck is for |
| `OUTCOME_PLURAL`, `OUTCOME_SINGULAR` | The unit you deliver. "Qualified sales meetings" / "qualified sales meeting". Could be booked demos, finished videos, placed candidates. |
| `OUTCOME_COUNT` | How many of them per month |
| `CURRENCY` | Your currency symbol. Pick one and use it everywhere. |
| `PRICE_MAIN`, `PRICE_MAIN_UNIT` | Your headline recurring price, and the billing period |
| `PRICE_PERF` | Your price per delivered unit, if you charge one |
| `SETUP_LINE` | One short line about setup cost |
| `GUARANTEE_COUNT`, `GUARANTEE_DAYS` | What you promise and by when |
| `TAM_COUNT`, `REGION`, `ICP_ONE_LINER` | How big their market is, where, and who the buyer is |
| `AOV`, `CLOSE_RATE` | Their average deal value and their close rate. These drive the money slides. |
| `TIMELINE_DAYS` | How long the engagement runs |

**Numbers are plain digits.** No currency symbols, no "per month". Write `2,000` not `£2,000/mo`.

---

## 2. The copy, in the HTML

Open `template/growth-plan.template.html` in any text editor. Use Find to jump between `[` square
brackets. Every one tells you what belongs there:

- `[The symptom they described on the call, in their words, one sentence]`
- `[Deliverable name, 3 to 5 words]`
- `[Client name]` · `[What you did, one line]` · `[The measurable result]`

Replace each with your own words. Keep roughly the same length so the layout still balances.

**If a slot does not apply to you, delete the whole card.** Three case studies with one real and
two invented is worse than one real case study on its own.

---

## 3. The images, in `assets/`

Every dashed box in the deck is a placeholder. To use a real image, put the file in `assets/` and
find the matching box in the HTML:

```html
<div class="ph ph-16x9">CASE STUDY THUMBNAIL</div>
```

Replace that whole line with:

```html
<img src="assets/your-file.png" alt="" style="width:100%; height:auto; display:block; border-radius:12px;">
```

Round headshots use a fixed size instead:

```html
<img src="assets/sam.jpg" alt="" style="width:96px; height:96px; border-radius:50%; object-fit:cover; display:block; margin:0 auto;">
```

You can leave any placeholder you do not have an image for. They are styled to look deliberate.
See `assets/README.md` for the full list and suggested sizes.

---

## 4. Your brand colour

Near the top of the HTML, inside the `<style>` block, find `:root`. Change these five lines to your
colour:

```css
--accent: #8b5cf6;                        /* your brand colour */
--accent-bright: #a78bfa;                 /* a lighter tint of it */
--accent-deep: #7c3aed;                   /* a darker shade of it */
--accent-soft: rgba(139,92,246,0.1);      /* the same colour at 10% opacity */
--gradient: linear-gradient(135deg, #7c3aed, #8b5cf6, #a78bfa);   /* deep, base, bright */
```

Leave green, red and amber alone. Green means "good outcome" and red means "problem" throughout the
deck, and overriding them makes it harder to read.

This deck is built dark. Changing the background to white does not work, the whole system assumes a
dark ground.

---

## 5. Build it

```bash
python3 build.py my-values.json out/
```

Open `out/index.html`. Arrow keys or swipe to move between slides.

The script will tell you if a field is missing from your values file, and how many bracketed
placeholders are still unedited.

To password-protect it:

```bash
DECK_PASSWORD=theircompanyname python3 build.py my-values.json out/
```

Hosting it free is covered in `docs/05-DEPLOY.md`.

---

## The maths, and why you have to do it yourself

Slide 5 shows what the problem costs them each month. Slide 13 shows what they make back. Both
contain worked arithmetic that is typed into the HTML, not calculated by a script.

That is deliberate. A number you have checked yourself is safer than one a script produced that
nobody looked at.

**If you change your price, their deal value or their close rate, redo both slides by hand and check
they agree with each other.** A prospect who spots that your two money slides disagree stops
believing the rest of the deck.

---

---

## Why the blank deck looks long

Straight out of the box, several slides are taller than the screen and you have to scroll inside
them. That is expected and it is not a bug.

Two reasons. First, the placeholder text is deliberately wordy, because
`[The symptom they described on the call, in their words, one sentence]` has to explain itself. Your
real copy will be much shorter and most slides will tighten up on their own once you fill them in.

Second, slides in this deck scroll by design. A couple of them, the itemised list and the case
studies in particular, are meant to be scrolled through while you talk. That was true of the deck
this template came from too.

If a slide still feels too tall after you have written your real copy, the fix is always to cut
content, never to shrink the type.

## Before you present

- [ ] Clicked through every slide with the arrow keys
- [ ] No square brackets left that you meant to fill
- [ ] Every row of cards looks even, no card taller or wordier than the one next to it
- [ ] No single word stranded alone on the last line of a heading or paragraph
- [ ] Your money slides agree with each other
- [ ] Every link opens
- [ ] Opened it on your phone
- [ ] Read the last slide once more. It is the one they screenshot.

The full list, with the reasoning behind each item, is in `docs/03-DESIGN-RULES.md`.

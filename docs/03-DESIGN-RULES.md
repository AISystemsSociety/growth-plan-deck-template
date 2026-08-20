# Design rules

Every rule here exists because breaking it cost something: a slide that looked broken on a live
call, an hour lost to a bug, or a prospect who noticed the wrong thing.

Run through this list before you present. Most of it takes two minutes to check and saves the
embarrassment of spotting it mid-call.

---

## Copy rules

### No em dashes. Ever.
Use a period, a comma, a colon, or rewrite the sentence. They creep in most often on long writing
sessions when you are focused on content rather than form.

Check: search the file for the character. The count must be zero.

### No widow words
Never leave one or two words stranded alone on the last line of a heading, subtitle or paragraph.
It is the single most common thing that makes a good-looking deck look amateur.

Three layers of defence, use all three:

1. **Shorten the copy.** Three full lines beat two lines and an orphan.
2. **Bind the last words** with a non-breaking space: `qualified&nbsp;meetings`, `in&nbsp;rotation`.
   This is the most reliable fix.
3. **Let CSS help.** `text-wrap: pretty` and `text-wrap: balance` are already in the stylesheet.
   Modern browsers auto-balance the final lines. Older ones ignore it, which is why you still need
   layers 1 and 2.

Before you call the deck finished, scan every multi-line block for a lone trailing word.

### Spell things out
No acronyms for job titles or industry terms your prospect might not use the same way. Write
"Operations Director", not "Ops Dir". If a term needs explaining, explain it once in brackets in
five words or less.

### One call to action
Multiple calls to action split intent and nothing gets clicked. "Let me know" gives them nothing to
decide on. Pick one specific next action and use it once.

### Never put an unverified link on a button
Open every link before you present. A dead link on a client-facing button is a credibility hit you
cannot recover mid-call.

---

## Layout rules

### Side-by-side cards must match
When two or three cards sit in a row, the description text under each headline must be the **same
number of lines**. Cap at two lines.

Three lines on one card and two on the next distorts the whole row and drags the eye to the wrong
option. This applies to pricing cards, comparison cards, stat boxes, and value-stack rows.

After writing a row of cards, count the lines on each. Trim the long one or expand the short one.

### No orphan cards
Never leave a single card alone in the last row of a grid with empty space beside it. It reads as
unfinished.

The stylesheet already stretches a lone last card to full width in three and four column grids. If
that looks wrong for your content, change the column count so the items balance instead. Five items
in a four-column grid is the classic offender: use a three-column grid and let it run 3 + 2.

### Equal heights
Cards in a row must be the same height. `align-items: stretch` is set on every grid in the
stylesheet. If you add a grid of your own, set it.

### Everything uses the same width
Every content box uses the full `slide-inner` width. A card capped narrower than the rest of the
deck looks like a mistake, not a design choice. One early build capped a card at a smaller width
and it read as broken until it was matched to everything else.

### Centre headings on centred slides
On a centred slide, the eyebrow, the heading AND the subtitle all centre. A centred heading over a
left-aligned subtitle is the kind of small inconsistency people feel without being able to name.

### No decorative divider lines
Gradient rules between sections read as random artifacts rather than structure. Spacing does the
job better.

### Vertical centring
Use the `center-v` class on the slide. Do not reach for `margin: auto` on the inner element, it
fails inside scrollable flex containers. Do not put `align-items: center` on the slide itself, it
clips overflow at the top on shorter screens.

---

## Image rules

### 16:9 for every video thumbnail
Locked with `aspect-ratio: 16/9`. Mixed aspect ratios in a row of case studies is immediately
visible.

### Full width for proof
Screenshots that prove something get the full width, with the bullet points **below** them, not
beside them. Split a proof screenshot into a two-column layout and it stops being readable, which
defeats the purpose.

### Flat asset paths
Keep every image in one flat `assets/` folder. Nested folders are the most common cause of images
that work locally and break once deployed.

### Placeholders are fine
An honest dashed placeholder box looks intentional. A stretched, low-resolution or irrelevant stock
image looks careless. If you do not have the image yet, leave the placeholder.

---

## Numbers rules

### The maths must reconcile across slides
Your cost-of-inaction slide, your ROI slide and your pricing slide all use the same inputs. If they
disagree, a sharp prospect will find it, and everything else you said becomes suspect.

Change your price and you must recompute the ROI slide by hand. This deck has no calculator in it,
by design: a static number you have personally checked is safer than a script producing a figure
you have not.

### Be conservative
The pessimistic scenario should be genuinely pessimistic. A deck where even the worst case looks
great is a deck nobody believes.

### One currency
Pick one and use it everywhere, including the bonus values and the comparison columns. Mixed
currency symbols in one deck is a trust problem, not a formatting problem.

### Never invent a proof number
If you cannot source it, cut it. Attribution errors are worse than a missing stat: one deck went
out with a result credited to the wrong company and had to be corrected after the fact.

---

## Structure rules

### `data-slide` numbers are load-bearing
The navigation builds its dots from the number of slides and then looks each one up by its
`data-slide` value. Every slide must be numbered 1 to N with **no gaps**. A gap means a dot that
navigates nowhere.

The static slide counter at the bottom right also needs to match your total.

### Renumber carefully when inserting a slide
Inserting a slide in the middle means every slide after it shifts up by one. Renumber in
**descending** order so replacements do not collide with each other. Going upwards, slide 4 becomes
5, then that new 5 becomes 6, and you have corrupted the deck.

### Read the file again after a scripted edit
If you renumber with a script, re-open the file before you make further edits. Editors and tools
working from a stale copy will silently write over your changes.

### Never clone a deployed, password-protected deck
An encrypted page contains the encrypted shell, not your markup. Always keep and work from the
readable source file. Encrypt only on the way out.

---

## Before you present, check

- [ ] Zero em dashes in the file
- [ ] No widow words in any heading, subtitle or card
- [ ] Every row of cards has matching line counts and equal heights
- [ ] No lone card sitting in a half-empty row
- [ ] `data-slide` runs 1 to N with no gaps, and the counter total matches
- [ ] The maths on the cost, ROI and pricing slides reconcile
- [ ] Every link opens
- [ ] Every placeholder is either filled or deliberately left
- [ ] One call to action, appearing once
- [ ] Opened it full-screen and clicked through every slide with the arrow keys
- [ ] Opened it on a phone

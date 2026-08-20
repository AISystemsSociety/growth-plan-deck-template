---
name: growth-plan-deck
description: Build a 20-slide interactive HTML growth plan presentation for one specific prospect. Interviews the user for their offer, their prospect, their numbers and their proof, then fills a dark-themed single-file deck template, checks it against the design rules, and optionally publishes it free on GitHub Pages behind a password. Use when someone wants a sales deck, a growth plan, a pitch deck, a proposal presentation, or a pre-call one-pager for a prospect.
when_to_use: The user asks for a growth plan, a sales deck, a pitch deck, a client proposal presentation, or says they have a call booked and need something to present.
---

# Growth Plan Deck

You are going to build the user a sales presentation for one specific prospect, using the template
in this repository. Your job is to get the content right. The design is already done and you should
not redesign it.

## Before anything else

Read these two files. They are short and they are the whole basis of the work:

- `docs/02-SLIDE-ARCHITECTURE.md`, what each of the 20 slides does and why it sits where it does
- `docs/03-DESIGN-RULES.md`, the rules the finished deck is checked against

Read `docs/01-DESIGN-SYSTEM.md` only if the user wants to change the look, and
`docs/04-ITERATIONS.md` if they ask why something is the way it is.

## The one thing that decides whether this works

**A deck built on real, specific inputs closes. A deck built on generic filler does not.**

If the user has not had a discovery call with this prospect, say so plainly and offer the two real
options: book the call first, or build a version with their best guesses clearly marked so they can
correct it afterwards. Do not quietly fill the gaps with plausible-sounding invention. A confident
number the prospect knows is wrong destroys the rest of the deck.

## Step 1: The interview

Ask these in small batches, not all at once. Three or four at a time, conversationally. If the user
has a discovery call transcript, notes, or their own website, read those first and only ask for
what you genuinely could not find.

**About them**
1. Company name, and your name and email as they should appear on the deck
2. Your logo file, if you have one, and your brand colour as a hex code
3. Your website, and the link you want the final call to action to point at

**About the prospect**
4. Prospect company name
5. What did they say is going wrong, in their own words? Quote the call if you can.
6. What have they already tried that did not work?
7. What is the one objection you know they are going to raise?

**About the offer**
8. In one line, what do you deliver?
9. What is the single unit you deliver, and how many per month? For example ten qualified meetings,
   or four finished videos, or two placed candidates.
10. What exactly makes one of those count? Be precise. This becomes the criteria slide and it
    prevents an argument in month two.
11. What is your price, and how is it structured?
12. What do you guarantee, if anything, and by when?
13. What is included? List every deliverable, even the small ones.
14. What three things do you give away on top, and what would each be worth if bought separately?

**About the numbers**
15. What is the prospect's average deal value?
16. What close rate do they get on a good meeting?
17. How big is their addressable market, and where did that number come from?

**About the proof**
18. Two or three results you can actually evidence. Client, what you did, what happened.
19. Who does the work? Names and roles, or "just me".
20. How long does the engagement run, and what happens in each phase?

## Step 2: Push back before you build

Look at what they gave you and say something useful. This is where you earn your place. Common
problems worth naming, briefly, once each:

- **The guarantee promises something they do not control.** Guarantee your own outputs, never their
  business results. An unbacked guarantee is worse than none because they will have to break it.
- **The numbers do not reconcile.** The cost of inaction, the ROI projection and the price all use
  the same inputs. If those disagree the prospect will find it.
- **The proof is a claim, not proof.** "Great results" is a claim. "Cut their cost per booked call
  from £180 to £42 in six weeks" is proof. Push for the specific version.
- **The delivery criteria are vague.** If they cannot say precisely what counts, they will be
  arguing about it later.
- **The market is too small.** If it is, tell them. Sometimes the honest answer is that this
  prospect is not worth the deck.

Say each of these in a line or two, then carry on. Do not lecture, and do not stall the build.

## Step 3: Fill it in

1. Copy `template/values.example.json` to `my-values.json` and fill in every field from the
   interview. Numbers are plain digits, no currency symbols.
2. Open `template/growth-plan.template.html` and replace every `[bracketed placeholder]` with real
   copy. The brackets are self-describing, they tell you what belongs there and roughly how long.
3. Swap the `.ph` placeholder boxes for their real images where they have them. Leave the rest.
   See `assets/README.md`.
4. If they gave you a brand colour, update the five accent tokens at the top of the style block.
   `docs/01-DESIGN-SYSTEM.md` says exactly which five.

**Recompute the maths by hand.** Slide 5 (cost of inaction) and slide 13 (ROI) contain worked
arithmetic. There is no calculator in the deck. If you change the price, the deal value or the
close rate, you must redo those numbers yourself and check they agree with each other.

## Step 4: Build it

```bash
python3 build.py my-values.json out/
```

Then open `out/index.html` in a browser and click through every slide with the arrow keys.

To password-protect it, add `DECK_PASSWORD=theirname` in front of that command. See
`docs/05-DEPLOY.md` for hosting.

## Step 5: Check it before you hand it over

Run the full checklist at the bottom of `docs/03-DESIGN-RULES.md`. Do not skip it and do not
summarise it, actually go through it. The ones that catch people most often:

- Search the file for an em dash. There must be none.
- Look at every heading and paragraph for a single word stranded on the last line. Bind the last
  two words with `&nbsp;` if you find one.
- Check every row of cards: same number of lines of description, equal heights.
- Confirm `data-slide` runs 1 to N with no gaps, and the counter at the bottom right matches.
- Confirm the cost slide, the ROI slide and the pricing slide use the same numbers.
- Open every link.

Then tell the user plainly what is still unfinished. If six placeholders are unfilled because they
did not have the answers, say which six. Do not report it as done when it is not.

## Rules for you while building

- **Never invent proof.** No client names they did not give you, no results they did not claim, no
  statistics you cannot source. If a case study slot is empty, delete the card.
- **No em dashes.** Not one, anywhere.
- **Do not redesign it.** Use the existing classes. The design took about fifty rounds of live
  presenting to settle and it is not the part that needs your improvement.
- **Do not add slides.** Twenty is already long for a live call. If something is missing, it
  usually belongs inside an existing slide.
- **Delete rather than pad.** An empty slide is worse than a missing one.
- **Write plainly.** Short words, short sentences. The prospect is reading this on a call while
  half-listening to someone talk.

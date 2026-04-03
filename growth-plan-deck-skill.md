# Growth Plan Slide Deck - Community Template

## What This Is

A 21-slide HTML presentation deck you can customize for any service business. Dark/light theme, full animations, keyboard + swipe navigation, mobile responsive. One single HTML file - no dependencies, no build tools, no frameworks. Open it in a browser and present.

Deploy it to GitHub Pages, Netlify, Vercel, or anywhere that hosts static files. Password-protect it with StatiCrypt if you want privacy.

## How to Use This

1. Open `growth-plan-template.html` in a code editor
2. Search for every `[PLACEHOLDER]` - each one tells you what to fill in
3. Replace placeholder content with your real numbers, quotes, and offer details
4. Add your logo to an `assets/` folder and update the image paths
5. Add screenshots of your tools/dashboards to `assets/` (or leave the placeholder boxes)
6. Open in browser to preview. Arrow keys or swipe to navigate.

## What You Need Before Building

Before you fill this in, do a proper discovery call with your prospect. You need:

- **Their numbers**: revenue, close rate, average client value, retention, leads per month
- **Their gaps**: what is not working, what is working, direct quotes from the call
- **Their market size**: how many potential buyers exist (LinkedIn Sales Nav is great for this)
- **Your offer details**: what you deliver, your price, your guarantee, your timeline
- **Proof**: case studies, testimonials, screenshots of results

The deck does not work without real data. Do not fill it with generic filler.

## The 21-Slide Structure

The deck follows a proven persuasion arc. Do not rearrange the order unless you understand why each slide exists.

### BLOCK 1: PAIN (Slides 1-5)

**Slide 1 - Title / Hook**
- Your logo + company name
- Outcome-focused headline: "How We [Outcome] for [Prospect Name] [Without Fears]"
- The headline number MUST be backed by real math shown later on slide 11
- 3 metric pills: key stats (conversations guaranteed, timeline, ownership)
- "Prepared for [Names]" + date
- NO PRICE on this slide

**Slide 2 - What We Learned**
- Feed back what they told you on the discovery call
- 4 stat cards: their key business numbers
- Two columns: "What is Not Working" (red) + "What is Working" (green)
- Source: "From our conversation on [date]"

**Slide 3 - Three Gaps**
- 3 tall cards with colored top borders (red, amber, purple)
- Each has: emoji, gap name, description, their direct quote
- Gaps should be specific to their business, not generic

**Slide 4 - Cost of Inaction**
- Big number: their monthly opportunity cost in red
- 4 stat cards: quarterly cost, annual cost, missed clients, LTV per client
- Why this matters - why you are having this conversation

**Slide 5 - Old Way vs New Way**
- Red box (old approach) vs green box (new approach)
- Arrow between them
- Purple punchline card at the bottom

### BLOCK 2: SOLUTION (Slide 6)

**Slide 6 - Solution Summary**
- Your solution name in accent color
- Subtitle explaining the outcome (not the process)
- Flow diagram: your process steps
- 3 pillar cards: what your service includes at a high level

### BLOCK 3: PILLAR DEEP-DIVES (Slides 7-10)

**Slide 7 - Pillar 1 Expanded**
- Accordion dropdowns with volume percentages
- Customize to your service tiers/approaches

**Slide 8 - Pillar 2 Expanded**
- Technical details of your system/process
- Screenshots of your tools ("Under the Hood")

**Slide 9 - Pillar 3 Expanded**
- Management/delivery details
- More tool screenshots

**Slide 10 - Free Bonuses**
- 2 bonus cards with dollar values
- Make these genuinely valuable things you include at no extra charge

### BLOCK 4: PROOF (Slides 11-12)

**Slide 11 - TAM and Math**
- Market size screenshots (Sales Navigator or similar)
- Funnel math: total leads > contacted > replies > conversations > closes > revenue
- The headline number from slide 1 traces back to this math

**Slide 12 - Case Studies**
- Your real results from real clients
- Each: company name, testimonial quote, video thumbnail (optional), bullet results, proof screenshots
- 2-4 case studies is ideal

### BLOCK 5: ANCHOR + VALUE (Slides 13-14)

**Slide 13 - Cost to Build Yourself (Anchor High)**
- Break down what it costs to build your solution in-house
- Each line with a dollar amount in red
- Total at the bottom in a glow card

**Slide 14 - Value Stack**
- Every deliverable with a dollar value in green
- Grouped by pillar/category
- Total at the bottom

### BLOCK 6: OFFER (Slides 15-16)

**Slide 15 - Guarantee**
- Green guarantee card with glow animation
- Two big numbers side by side: your guarantee metric + timeline
- "The risk is entirely on us."

**Slide 16 - The Price**
- Left (dimmed): monthly in-house cost, crossed out
- Right (featured): your price with badge
- Check-list of what is included
- Risk reversal reminder
- Optional retainer footnote

### BLOCK 7: CLOSE (Slides 17-21)

**Slide 17 - ROI Calculator**
- 3 tiers: worst case, conservative, at their actual rate
- Use their real numbers from the discovery call

**Slide 18 - Worst Case Scenario**
- Even if everything goes wrong, what do they keep?
- 4 cards of permanent assets they walk away with

**Slide 19 - "If All This Did Was..." (Brunson Close)**
- 4 cards, each with: "If all this did was [specific outcome]. Would it be worth it?"
- Make these specific to their situation

**Slide 20 - Timeline**
- 5 roadmap steps with colored left borders
- What happens after they say yes, day by day

**Slide 21 - Summary + FAQ**
- Glow card: cost of inaction vs investment vs ROI
- What you get + at-a-glance numbers
- Guarantee reminder
- 5 FAQ dropdowns
- Your company name at the bottom

## Design System Reference

### Color Variables
```css
--bg: #0c0c14          /* Dark background */
--card: #16162a         /* Card background */
--accent: #7c3aed       /* Purple - your primary brand color (change this) */
--green: #22c55e        /* Success, positive, working */
--red: #ef4444          /* Danger, cost, not working */
--amber: #f59e0b        /* Warning, medium priority */
--blue: #3b82f6         /* Info, neutral */
--cyan: #06b6d4         /* Accent for variety */
```

To rebrand: change `--accent` to your brand color. Update all `rgba(124,58,237,...)` values to match your new accent RGB.

### Card Variants
- `.card` - Standard card (dark bg, border, hover effect)
- `.card-sm` - Smaller padding
- `.card-violet` - Purple tint with shimmer animation
- `.card-green` - Green tint (for guarantees, positive)
- `.card-red` - Red tint (for problems, costs)
- `.card-amber` - Amber tint (for warnings)
- `.card-blue` - Blue tint (for info)

### Grid Layouts
- `.grid-2` - 2 columns
- `.grid-3` - 3 columns
- `.grid-4` - 4 columns
All collapse to 2-col at 1024px and 1-col at 640px.

### Key Components
- `.stat` with `.num` + `.label` - Big number stat cards
- `.bullet-list` / `.bullet-list.green` - Colored bullet lists
- `.x-list` - Red X list (for problems)
- `.check-list` - Green checkmark list
- `.quote-card` - Italic quote with left border
- `.glow-card` - Glowing card with pulse animation
- `.gap-visual` - Old way vs new way comparison
- `.flow-row` with `.flow-box` - Process flow diagram
- `.pricing-card.featured` - Featured price card with badge
- `.roadmap-step` - Timeline step card
- `.metric-pill` - Inline metric badges
- `.tier-card` + `.tier-badge` - Tiered content cards
- `.stack-details` - Accordion dropdown
- `.value-line` / `.value-row` - Key-value rows
- `.screenshot-hero` - Full-width screenshot
- `.screenshot-grid` - 2-col screenshot grid
- `.placeholder-img` - Dashed placeholder for missing images
- `.faq-item` - Collapsible FAQ

### Animations
- `.fade-up` - Staggered fade-in on slide entry (auto-delays for child elements 1-8)
- `accentPulse` - Subtle glow pulse on glow cards
- `headlineNeon` - Neon glow on accent-colored headings
- `shimmer` - Moving light sweep on violet cards
- `shineRotate` - Rotating border shine (use `.shine-border`)
- `guaranteeGlow` - Green glow pulse on guarantee cards
- `emojiBob` - Gentle bounce on emoji icons
- `statGlow` - Text glow on stat numbers

### Hard Rules
- No em dashes anywhere - use regular dash or rewrite
- No price before slide 16
- `.fade-up` on all slide children for entrance animation
- Bullet lists inside centered slides need `text-align:left`
- `white-space:nowrap` on any price with /mo suffix
- Strikethrough on number only, not on /mo or /year suffix

## Deployment Options

### GitHub Pages (Free)
```bash
git init
git add .
git commit -m "Growth plan deck"
gh repo create your-username/prospect-growth-plan --public --source=. --push
gh api repos/your-username/prospect-growth-plan/pages -X POST -f "source[branch]=main" -f "source[path]=/"
```

### Password Protection (StatiCrypt)
```bash
cp index.html /tmp/to-encrypt.html
cd /tmp && npx staticrypt@3.5.4 to-encrypt.html -p "yourpassword" -d enc-out --short --remember 30
cp /tmp/enc-out/to-encrypt.html ./index.html
```

### Simple Local Preview
Just open the HTML file in any browser. No server needed.

## What to Customize Per Prospect

- Slide 1: headline number, outcome, fears, names, date
- Slide 2: their specific numbers and gaps from discovery call
- Slide 3: their three gaps with their direct quotes
- Slide 4: their opportunity cost number
- Slide 7: your offers customized to their business
- Slide 8: signal/targeting examples relevant to their industry
- Slide 11: market size + funnel math using their numbers
- Slide 12: your case studies (keep these the same across decks)
- Slide 14: value stack dollar amounts (adjust if scope differs)
- Slide 17: ROI tiers using their client value and close rate
- Slide 19: "if all this did was" statements specific to their situation

## What Stays the Same Every Time

- Design system, CSS, animations
- Case studies (slide 12)
- Anchor high breakdown (slide 13) - adjust numbers slightly
- Guarantee structure (slide 15) - unless your guarantee changes
- Price (slide 16) - unless pricing varies
- Timeline (slide 20) - adjust if your delivery timeline differs
- FAQ content (slide 21) - adjust company-specific references

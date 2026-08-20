# assets/

Put your images in this folder. Keep it flat, no sub-folders. Nested paths are the most common
reason images work on your machine and break once the deck is online.

`build.py` copies this whole folder into your output directory.

## What the deck expects

| Placeholder label in the deck | What to put there | Suggested size |
|---|---|---|
| `LOGO` | Your logo, top-left of every slide | 200 x 200 px, square, transparent PNG |
| `SCREENSHOT OF YOUR MARKET RESEARCH` | Proof of your market size | Full width, at least 1600px wide |
| `CASE STUDY THUMBNAIL` | One per case study | 16:9, at least 1280 x 720 |
| `PHOTO` | Team headshots | Square, at least 400 x 400. Displayed as a circle. |

## Swapping a placeholder for a real image

Find the dashed box in the HTML. It looks like this:

```html
<div class="ph ph-16x9">CASE STUDY THUMBNAIL</div>
```

Replace the whole line with:

```html
<img src="assets/your-file.png" alt="" style="width:100%; height:auto; display:block; border-radius:12px;">
```

For a round headshot, use a fixed size instead:

```html
<img src="assets/sam.jpg" alt="" style="width:96px; height:96px; border-radius:50%; object-fit:cover; display:block; margin:0 auto;">
```

## You can leave placeholders in

They are styled to look deliberate. An honest dashed box reads better than a stretched, blurry or
irrelevant stock photo. Fill the ones you have real images for and leave the rest.

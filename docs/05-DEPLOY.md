# Putting it online

The deck is a single HTML file. Anything that serves a static file will host it. These are the
routes in order of how little work they are.

---

## Option 1: do not host it at all

Open `out/index.html` on your own machine, share your screen, present. Nothing to set up, nothing
to break, no link to leak.

This is the right choice for most first calls. Host it only when you need them to reopen it later,
or when you are sending it ahead.

---

## Option 2: GitHub Pages, free

1. Build the deck: `python3 build.py my-values.json out/`
2. Create a new **public** repository on GitHub.
3. Upload everything inside `out/`: `index.html`, the `assets/` folder, and `.nojekyll`.
4. In the repo, go to **Settings → Pages**. Set Branch to `main` and Folder to `/ (root)`. Save.
5. Wait about a minute. Your deck is live at `https://<your-username>.github.io/<repo-name>/`.

To update it later: edit, rebuild, re-upload `index.html`.

### The `.nojekyll` file matters
GitHub Pages runs your files through Jekyll by default, which quietly ignores anything in folders
starting with an underscore and can drop assets without telling you. The empty `.nojekyll` file
turns that off. `build.py` writes it for you. Do not delete it.

### A public repo is a public deck
Anything you upload is readable by anyone who finds the URL, including your prospect's name and
your pricing. If that bothers you, use the password gate below, or host it privately instead.

---

## Option 3: password-protect it

```bash
DECK_PASSWORD=acme python3 build.py my-values.json out/
```

This encrypts the deck with [StatiCrypt](https://github.com/robinmoisson/staticrypt). Visitors get
a password prompt, and the real content is AES-encrypted until they enter it. It needs Node.js
installed, for the one-off `npx` call.

A good default password is the prospect's company name in lowercase. It is memorable, it is not
guessable by a stranger, and it makes the deck feel prepared for them.

### Two things that will bite you

**Never run StatiCrypt against a file you care about.** Some versions overwrite the input file in
place, which destroys your source. `build.py` handles this by copying to a temporary directory,
encrypting there, and copying the result back. If you ever run StatiCrypt by hand, do the same.

**Keep the unencrypted source.** Once a deck is encrypted, the file contains the encrypted payload
and nothing readable. You cannot recover your markup from a deployed deck. Your source of truth is
always `template/growth-plan.template.html` plus your values file, never the built output.

Password protection is a courtesy gate, not real security. It stops casual sharing. It is not the
place to put anything genuinely confidential.

---

## Option 4: anywhere else

Netlify, Vercel, Cloudflare Pages and every other static host work the same way: point them at the
`out/` folder. Most offer drag-and-drop upload with no command line at all.

---

## Before you send the link

- [ ] Open the live URL yourself, in a private browsing window
- [ ] Click through every slide with the arrow keys
- [ ] Check every image loaded, no broken icons
- [ ] Open it on your phone
- [ ] Click every link on the final slide
- [ ] If it is password-protected, test the password from a different device
- [ ] Read the last slide one more time. It is the one they screenshot.

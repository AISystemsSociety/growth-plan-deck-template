#!/usr/bin/env python3
"""
Build your growth plan deck.

    python3 build.py my-values.json out/

Reads template/growth-plan.template.html, fills in every {{TOKEN}} from your values
file, copies your assets/ folder alongside, and writes out/index.html.

Optionally password-protects the result:

    DECK_PASSWORD=hunter2 python3 build.py my-values.json out/

That step shells out to StatiCrypt via npx, so it needs Node.js installed. Without
the environment variable the deck is built unencrypted, which is fine for local use.
"""

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TEMPLATE = ROOT / "template" / "growth-plan.template.html"
ASSETS = ROOT / "assets"
TOKEN_RE = re.compile(r"\{\{([A-Z_][A-Z0-9_]*)\}\}")


def die(msg):
    print(f"\n  Stopped: {msg}\n", file=sys.stderr)
    sys.exit(1)


def main():
    if len(sys.argv) != 3:
        die("usage: python3 build.py <values.json> <output-dir>")

    values_path = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])

    if not values_path.is_file():
        die(f"cannot find your values file at {values_path}")
    if not TEMPLATE.is_file():
        die(f"cannot find the template at {TEMPLATE}")

    try:
        values = json.loads(values_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        die(f"{values_path} is not valid JSON.\n  {exc}\n"
            "  The usual cause is a missing comma, or a trailing comma after the last entry.")

    values = {k: str(v) for k, v in values.items() if not k.startswith("_")}
    html = TEMPLATE.read_text(encoding="utf-8")

    # Report anything the template needs that the values file does not supply.
    needed = set(TOKEN_RE.findall(html))
    missing = sorted(needed - set(values))
    if missing:
        die("your values file is missing these fields:\n    "
            + "\n    ".join(missing)
            + "\n\n  Copy template/values.example.json and fill it in.")

    unused = sorted(set(values) - needed)
    if unused:
        print("  Note: these values were not used by the template: " + ", ".join(unused))

    html = TOKEN_RE.sub(lambda m: values[m.group(1)], html)

    # Warn, do not block, on unfinished hand-edited copy.
    brackets = re.findall(r"\[[A-Z][^\]\n]{4,80}\]", html)
    if brackets:
        print(f"  Note: {len(brackets)} [bracketed] placeholders are still unedited.")
        print("        That is fine for a first look. Fill them in before you present.")

    if "\u2014" in html:   # em dash, written as an escape so this file stays clean
        print("  Warning: found an em dash. Replace it with a comma, a period, or a rewrite.")

    out_dir.mkdir(parents=True, exist_ok=True)
    index = out_dir / "index.html"
    index.write_text(html, encoding="utf-8")

    if ASSETS.is_dir():
        dest = out_dir / "assets"
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(ASSETS, dest)

    # GitHub Pages skips folders and files it thinks are Jekyll internals without this.
    (out_dir / ".nojekyll").write_text("", encoding="utf-8")

    password = os.environ.get("DECK_PASSWORD")
    if password:
        encrypt(index, password)
        print(f"\n  Built and encrypted: {index}")
        print(f"  Password: {password}\n")
    else:
        print(f"\n  Built: {index}")
        print("  Open it in a browser. Arrow keys to move between slides.")
        print("  To password-protect it, re-run with DECK_PASSWORD=yourpassword\n")


def encrypt(index: Path, password: str) -> None:
    """
    Encrypt in a temp directory, never in place.

    StatiCrypt overwrites its input file in some versions. Running it against a file
    you care about can destroy your source. Always copy out, encrypt, copy back.
    """
    if shutil.which("npx") is None:
        die("password protection needs Node.js installed, for the npx command.\n"
            "  Install Node, or re-run without DECK_PASSWORD to build unencrypted.")

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        staged = tmp_path / "deck.html"
        shutil.copy2(index, staged)
        result = subprocess.run(
            ["npx", "--yes", "staticrypt@3.5.4", str(staged),
             "-p", password, "-d", str(tmp_path / "enc"), "--short", "--remember", "30"],
            capture_output=True, text=True, cwd=tmp,
        )
        encrypted = tmp_path / "enc" / "deck.html"
        if result.returncode != 0 or not encrypted.is_file():
            die("StatiCrypt failed.\n  " + (result.stderr.strip() or "no error output"))
        shutil.copy2(encrypted, index)


if __name__ == "__main__":
    main()

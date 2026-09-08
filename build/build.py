#!/usr/bin/env python3
"""Assemble les versions autonomes : injecte le sprite SVG partagé dans chaque source."""
import pathlib, sys
root = pathlib.Path(__file__).resolve().parent.parent
sprite = (root / "build" / "sprite.html").read_text(encoding="utf-8")

# Les règles CSS ne franchissent pas la frontière d'ombre d'un <use> : on cuit
# les attributs de présentation directement dans les symboles duotone.
sprite = sprite.replace(
    'class="duo-fill"',
    'class="duo-fill" fill="currentColor" fill-opacity=".17" stroke="none"')
sprite = sprite.replace(
    'class="duo-line"',
    'class="duo-line" fill="none" stroke="currentColor" stroke-width="1.7"'
    ' stroke-linecap="round" stroke-linejoin="round"')


for name, out in (("v1", "v1/index.html"), ("v2", "v2/index.html"),
                  ("v3", "v3/index.html")):
    src = root / "build" / f"{name}.src.html"
    if not src.exists():
        print(f"— {name}: source absente, ignorée"); continue
    html = src.read_text(encoding="utf-8")
    if "<!--SPRITE-->" not in html:
        sys.exit(f"{src}: marqueur <!--SPRITE--> introuvable")
    dest = root / out
    dest.parent.mkdir(parents=True, exist_ok=True)
    html = html.replace("<!--SPRITE-->", sprite)
    dest.write_text(html, encoding="utf-8")
    print(f"✓ {out}  ({len(html):,} octets)")

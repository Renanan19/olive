# -*- coding: utf-8 -*-
"""
seo_boost.py  -- site-wide technical SEO + GEO hardening for huiledefes.com

Idempotent. For every HTML page (root + blog/ + recipes/ + guides/) it adds,
only when missing (each block is guarded independently, so partial pages get
completed and re-runs are no-ops):

  * self-referencing <link rel="canonical">
  * hreflang alternate cluster (fr/en/it/el) + x-default
        - suffix pattern  "<base>-<lang>.html"  (recipes, guides)
        - known root-level language clusters (index*, observatoire*, pillars)
  * Open Graph tags   (og:title/description/url/type/site_name/locale/image)
  * Twitter Card tags (summary_large_image)

Recipes only:
  * strips the fake "aggregateRating" object from Recipe JSON-LD
    (self-serving review markup with no real reviews = Google policy risk and
    a trust signal LLMs discount). JSON-LD is re-validated before the file is
    written; on parse failure the file is left untouched.

Usage:  python seo_boost.py [--dry-run]
"""

import os
import re
import sys
import json
import html

SITE = "https://huiledefes.com"
OG_IMAGE = f"{SITE}/assets/og-default.png"
SITE_NAME = "L'Or Vert"
LOCALES = {"fr": "fr_FR", "en": "en_US", "it": "it_IT", "el": "el_GR"}

ROOT = os.path.dirname(os.path.abspath(__file__))
DRY = "--dry-run" in sys.argv

# Root-level language clusters that do NOT use the -<lang>.html suffix.
ROOT_CLUSTERS = [
    {"fr": "index.html", "en": "index-en.html",
     "it": "index-it.html", "el": "index-el.html"},
    {"fr": "observatoire-huile-olive-2026.html", "en": "olive-oil-observatory-2026.html",
     "it": "osservatorio-olio-oliva-2026.html", "el": "paratiritirio-elaio-lado-2026.html"},
    {"fr": "huile-olive.html", "en": "olive-oil.html",
     "it": "olio-oliva.html", "el": "elaio-lado.html"},
]
WEBSITE_TYPE_FILES = {"index.html", "index-en.html", "index-it.html", "index-el.html"}

SUFFIX_RE = re.compile(r'^(?P<base>.+)-(?P<lang>fr|en|it|el)\.html$')
TITLE_RE = re.compile(r'<title>(.*?)</title>', re.S | re.I)
DESC_RE = re.compile(r'<meta\s+name=["\']description["\']\s+content="([^"]*)"', re.I)
LANG_RE = re.compile(r'<html[^>]*\blang=["\']([a-zA-Z-]+)["\']', re.I)
LDJSON_RE = re.compile(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', re.S | re.I)
FAKE_RATING_RE = re.compile(r',\s*"aggregateRating"\s*:\s*\{[^{}]*\}', re.S)


def rel_url(path):
    rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
    return f"{SITE}/{rel}"


def esc(s):
    return html.escape(s, quote=True)


def hreflang_block(cluster):
    """cluster: {lang: url} -> indented <link> lines incl. x-default."""
    lines = [f'<link rel="alternate" hreflang="{lg}" href="{cluster[lg]}" />'
             for lg in ("fr", "en", "it", "el") if lg in cluster]
    xdef = cluster.get("en") or cluster.get("fr")
    if xdef:
        lines.append(f'<link rel="alternate" hreflang="x-default" href="{xdef}" />')
    return "\n    ".join(lines)


def suffix_cluster(path):
    d, fn = os.path.dirname(path), os.path.basename(path)
    m = SUFFIX_RE.match(fn)
    if not m:
        return None
    base = m.group("base")
    cl = {}
    for lg in ("fr", "en", "it", "el"):
        cand = os.path.join(d, f"{base}-{lg}.html")
        if os.path.exists(cand):
            cl[lg] = rel_url(cand)
    return cl if len(cl) >= 2 else None


def root_cluster(path):
    fn = os.path.basename(path)
    for cm in ROOT_CLUSTERS:
        if fn in cm.values():
            return {lg: rel_url(os.path.join(ROOT, f))
                    for lg, f in cm.items() if os.path.exists(os.path.join(ROOT, f))}
    return None


def valid_ldjson(src):
    for m in LDJSON_RE.finditer(src):
        try:
            json.loads(m.group(1))
        except Exception:
            return False
    return True


def process(path, is_recipe):
    with open(path, encoding="utf-8") as f:
        src = f.read()
    if "</head>" not in src.lower():
        return "skip-nohead"
    orig = src

    # --- recipes: strip fake aggregateRating, keep JSON-LD valid ---
    if is_recipe and "aggregateRating" in src:
        cand = FAKE_RATING_RE.sub("", src)
        if valid_ldjson(cand):
            src = cand

    lang_m = LANG_RE.search(src)
    lang = (lang_m.group(1).split("-")[0].lower() if lang_m else "fr")
    if lang not in LOCALES:
        lang = "fr"
    tm = TITLE_RE.search(src)
    title = html.unescape(tm.group(1).strip()) if tm else SITE_NAME
    dm = DESC_RE.search(src)
    desc = html.unescape(dm.group(1).strip()) if dm else ""
    canonical = rel_url(path)

    inserts = []

    if 'rel="canonical"' not in src and "rel='canonical'" not in src:
        inserts.append(f'<link rel="canonical" href="{canonical}" />')

    if "hreflang" not in src:
        cl = root_cluster(path) if os.path.dirname(path) == ROOT else suffix_cluster(path)
        if cl:
            inserts.append(hreflang_block(cl))

    if "og:title" not in src:
        og_type = "website" if os.path.basename(path) in WEBSITE_TYPE_FILES else "article"
        og = [
            f'<meta property="og:title" content="{esc(title)}" />',
            f'<meta property="og:description" content="{esc(desc)}" />',
            f'<meta property="og:url" content="{canonical}" />',
            f'<meta property="og:type" content="{og_type}" />',
            f'<meta property="og:site_name" content="{esc(SITE_NAME)}" />',
            f'<meta property="og:locale" content="{LOCALES[lang]}" />',
            f'<meta property="og:image" content="{OG_IMAGE}" />',
            '<meta property="og:image:width" content="1200" />',
            '<meta property="og:image:height" content="630" />',
            '<meta name="twitter:card" content="summary_large_image" />',
            f'<meta name="twitter:title" content="{esc(title)}" />',
            f'<meta name="twitter:description" content="{esc(desc)}" />',
            f'<meta name="twitter:image" content="{OG_IMAGE}" />',
        ]
        inserts.append("\n    ".join(og))

    if inserts:
        block = "\n    " + "\n    ".join(inserts) + "\n"
        idx = src.lower().index("</head>")
        src = src[:idx] + block + src[idx:]

    if src == orig:
        return "nochange"
    if not DRY:
        with open(path, "w", encoding="utf-8") as f:
            f.write(src)
    return "updated"


def main():
    targets = []
    for fn in sorted(os.listdir(ROOT)):
        if fn.endswith(".html"):
            targets.append((os.path.join(ROOT, fn), False))
    for d in ("blog", "recipes", "guides"):
        dp = os.path.join(ROOT, d)
        if not os.path.isdir(dp):
            continue
        for fn in sorted(os.listdir(dp)):
            if fn.endswith(".html"):
                targets.append((os.path.join(dp, fn), d == "recipes"))

    stats = {}
    for path, is_recipe in targets:
        r = process(path, is_recipe)
        stats[r] = stats.get(r, 0) + 1

    print(f"{'DRY RUN — ' if DRY else ''}processed {len(targets)} files")
    for k in sorted(stats):
        print(f"  {k:14s} {stats[k]}")


if __name__ == "__main__":
    main()

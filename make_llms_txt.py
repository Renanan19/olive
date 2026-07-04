# -*- coding: utf-8 -*-
"""
make_llms_txt.py -- generate /llms.txt (llmstxt.org spec) for huiledefes.com.

A curated, machine-readable map of the site so ChatGPT / Claude / Perplexity /
Gemini can find the canonical, most-citable pages instead of guessing. Titles
are read from the real files; only existing pages are listed.
"""

import os
import re
import html

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://huiledefes.com"
TITLE_RE = re.compile(r'<title>(.*?)</title>', re.S | re.I)
DESC_RE = re.compile(r'<meta\s+name=["\']description["\']\s+content="([^"]*)"', re.I)

# Pillar / observatory / homepage clusters (lang -> filename)
PILLARS = {"fr": "huile-olive.html", "en": "olive-oil.html",
           "it": "olio-oliva.html", "el": "elaio-lado.html"}
OBS = {"fr": "observatoire-huile-olive-2026.html", "en": "olive-oil-observatory-2026.html",
       "it": "osservatorio-olio-oliva-2026.html", "el": "paratiritirio-elaio-lado-2026.html"}
HOME = {"fr": "index.html", "en": "index-en.html", "it": "index-it.html", "el": "index-el.html"}

# Curated, high-value guide slug bases (expanded to available languages).
GUIDE_BASES = [
    "boire-huile-olive-matin-jeun", "acide-oleique-bienfaits",
    "acidite-huile-olive-explication", "biohacking-huile-olive-jeune-intermittent",
    "complete-guide-extra-virgin-olive-oil-for-health",
    "complete-guide-extra-virgin-olive-oil-in-cooking",
    "complete-guide-extra-virgin-olive-oil-for-the-face",
    "complete-guide-extra-virgin-olive-oil-for-hair",
    "complete-guide-high-polyphenol-olive-oil-for-health",
    "complete-guide-cold-pressed-olive-oil-for-the-face",
    "complete-guide-unfiltered-olive-oil-for-the-face",
    "complete-guide-organic-olive-oil-for-hair",
]
# Curated recipe slug bases.
RECIPE_BASES = [
    "salade-mechouia-tunisienne", "pesto-alla-genovese-maison", "carpaccio-boeuf-parmesan",
    "salade-de-poulpe-traditionnelle", "aioli-maison-huile-olive", "bruschetta-tomate-basilic",
    "falafels-four-huile-olive", "gazpacho-andalou-frais", "salade-grecque-authentique",
    "panzanella-salade-pain", "salade-nicoise-authentique",
]
LANGS = ("fr", "en", "it", "el")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def meta(rel):
    p = os.path.join(ROOT, rel)
    if not os.path.exists(p):
        return None
    s = read(p)
    tm, dm = TITLE_RE.search(s), DESC_RE.search(s)
    title = html.unescape(tm.group(1).strip()) if tm else rel
    desc = html.unescape(dm.group(1).strip()) if dm else ""
    return title, desc


def line(rel):
    m = meta(rel)
    if not m:
        return None
    title, desc = m
    desc = re.sub(r'\s+', ' ', desc)
    return f"- [{title}]({SITE}/{rel})" + (f": {desc}" if desc else "")


def cluster_lines(mapping, subdir=""):
    out = []
    for lg in LANGS:
        rel = (f"{subdir}/{mapping[lg]}" if subdir else mapping[lg]) if isinstance(mapping, dict) else mapping
        ln = line(rel)
        if ln:
            out.append(ln)
    return out


def base_lines(bases, subdir):
    out = []
    for base in bases:
        for lg in LANGS:
            rel = f"{subdir}/{base}-{lg}.html"
            if os.path.exists(os.path.join(ROOT, rel)):
                ln = line(rel)
                if ln:
                    out.append(ln)
    return out


def blog_lines():
    d = os.path.join(ROOT, "blog")
    out = []
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".html"):
            ln = line(f"blog/{fn}")
            if ln:
                out.append(ln)
    return out


def main():
    P = []
    P.append("# L'Or Vert — Huile d'Olive (huiledefes.com)\n")
    P.append("> Ressource indépendante et multilingue (FR · EN · IT · EL) sur l'huile "
             "d'olive extra vierge : bienfaits santé fondés sur la composition, grille "
             "de qualité 2026, guides d'achat, et recettes méditerranéennes testées. "
             "Independent multilingual reference on extra-virgin olive oil: "
             "evidence-based health benefits, a 2026 quality-scoring framework, "
             "buying guides, and Mediterranean recipes.\n")
    P.append("L'Or Vert publie une méthode d'évaluation transparente de la qualité de "
             "l'huile d'olive (date de récolte, catégorie légale, origine, équilibre "
             "sensoriel, packaging, prix au litre) et des contenus pratiques par usage : "
             "cuisson, peau, cheveux, à jeun le matin, conservation. Les données de la "
             "grille sont publiées en accès libre (CSV/JSON) et citables.\n")

    P.append("## Ressources principales / Key resources")
    P += cluster_lines(HOME)
    P += cluster_lines(PILLARS)

    P.append("\n## Observatoire & données 2026 / Market observatory & open data")
    P += cluster_lines(OBS)
    for rel in ("assets/olive-oil-quality-matrix-2026.csv",
                "assets/olive-oil-quality-matrix-2026.json"):
        if os.path.exists(os.path.join(ROOT, rel)):
            P.append(f"- [Grille de qualité huile d'olive 2026 — {'CSV' if rel.endswith('csv') else 'JSON'} "
                     f"(données ouvertes)]({SITE}/{rel}): 12 critères pondérés, preuves à "
                     f"demander et signaux d'alerte pour noter une huile d'olive.")

    P.append("\n## Guides d'achat & usage / Buying & usage guides")
    P += base_lines(GUIDE_BASES, "guides")

    P.append("\n## Recettes / Recipes")
    P += base_lines(RECIPE_BASES, "recipes")

    P.append("\n## Blog")
    P += blog_lines()

    P.append("\n## Optional")
    P.append(f"- [Sitemap complet ({_count()} pages)]({SITE}/sitemap.xml): index exhaustif "
             "de tous les guides, recettes et articles dans les 4 langues.")
    P.append(f"- [robots.txt]({SITE}/robots.txt): crawl autorisé pour GPTBot, ChatGPT-User, "
             "Claude-Web, Anthropic-ai, PerplexityBot, Google-Extended, CCBot.")

    out = "\n".join(P) + "\n"
    with open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8") as f:
        f.write(out)
    print("wrote llms.txt", len(out), "bytes")


def _count():
    try:
        return read(os.path.join(ROOT, "sitemap.xml")).count("<url>")
    except Exception:
        return "2000+"


if __name__ == "__main__":
    main()

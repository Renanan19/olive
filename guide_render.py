# -*- coding: utf-8 -*-
"""
guide_render.py -- shared renderer for authentic GUIDE rewrites (guides/ dir).

write_guide_cluster(slug, content_by_lang) rewrites guides/<slug>-<lang>.html with
clean SEO head (canonical + hreflang + OG/Twitter), evidence-based body, and
Article + FAQPage + BreadcrumbList JSON-LD (validated). Health guides carry a
non-medical-advice disclaimer.

Content dict keys: title, desc, h1, lede, intro, sections=[(h, body_html)...],
key_facts=[...]|None, faqs=[(q,a)...], disclaimer=str|None, section (articleSection),
keywords, datePublished optional.
"""

import os
import re
import json
import html

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://huiledefes.com"
OG = f"{SITE}/assets/og-default.png"
LOCALES = {"fr": "fr_FR", "en": "en_US", "it": "it_IT", "el": "el_GR"}
LANGS = ("fr", "en", "it", "el")

UI = {
    "fr": dict(home="Accueil", crumb1="Guides", nav="L'OR VERT / GUIDES",
               also="À lire aussi", pillar="Huile d'olive : le guide pilier complet",
               obs="Voir l'observatoire 2026", pillarhref="../huile-olive.html",
               obshref="../observatoire-huile-olive-2026.html", idx="../index.html",
               kf="En bref", faqh="Questions fréquentes",
               foot="Le carnet de référence de L'Or Vert sur l'huile d'olive, la cuisine méditerranéenne et les usages du quotidien."),
    "en": dict(home="Home", crumb1="Guides", nav="L'OR VERT / GUIDES",
               also="Related", pillar="Olive oil: the complete pillar guide",
               obs="See the 2026 observatory", pillarhref="../olive-oil.html",
               obshref="../olive-oil-observatory-2026.html", idx="../index-en.html",
               kf="Key facts", faqh="Frequently asked questions",
               foot="L'Or Vert's reference notebook on olive oil, Mediterranean cooking and everyday uses."),
    "it": dict(home="Home", crumb1="Guide", nav="L'OR VERT / GUIDE",
               also="Da leggere", pillar="Olio d'oliva: la guida pilastro completa",
               obs="Vedi l'osservatorio 2026", pillarhref="../olio-oliva.html",
               obshref="../osservatorio-olio-oliva-2026.html", idx="../index-it.html",
               kf="In breve", faqh="Domande frequenti",
               foot="Il taccuino di riferimento di L'Or Vert su olio d'oliva, cucina mediterranea e usi quotidiani."),
    "el": dict(home="Αρχική", crumb1="Οδηγοί", nav="L'OR VERT / ΟΔΗΓΟΙ",
               also="Δείτε επίσης", pillar="Ελαιόλαδο: ο πλήρης κεντρικός οδηγός",
               obs="Δείτε το παρατηρητήριο 2026", pillarhref="../elaio-lado.html",
               obshref="../paratiritirio-elaio-lado-2026.html", idx="../index-el.html",
               kf="Με λίγα λόγια", faqh="Συχνές ερωτήσεις",
               foot="Το σημειωματάριο αναφοράς του L'Or Vert για το ελαιόλαδο, τη μεσογειακή κουζίνα και την καθημερινή χρήση."),
}


def esc(s):
    return html.escape(s, quote=True)


def render(slug, lang, d, subdir="guides"):
    ui = dict(UI[lang])
    if d.get("crumb1"):
        ui["crumb1"] = d["crumb1"]
    url = f"{SITE}/{subdir}/{slug}-{lang}.html"
    alts = "\n    ".join(
        f'<link rel="alternate" hreflang="{lg}" href="{SITE}/{subdir}/{slug}-{lg}.html" />'
        for lg in LANGS)

    article = {
        "@context": "https://schema.org", "@type": "Article",
        "headline": d["h1"],
        "description": d["desc"],
        "author": {"@type": "Organization", "name": "L'Or Vert", "@id": f"{SITE}/#organization"},
        "publisher": {"@type": "Organization", "name": "L'Or Vert", "url": SITE,
                      "logo": {"@type": "ImageObject", "url": OG}},
        "datePublished": d.get("datePublished", "2026-05-04"), "dateModified": "2026-07-04",
        "inLanguage": lang, "articleSection": d["section"],
        "image": OG, "keywords": d["keywords"],
        "isAccessibleForFree": True, "mainEntityOfPage": url,
    }
    faqpage = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faqs"]],
    }
    crumbs = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": ui["home"], "item": f"{SITE}/{ui['idx'][3:]}"},
            {"@type": "ListItem", "position": 2, "name": ui["crumb1"], "item": url},
            {"@type": "ListItem", "position": 3, "name": d["h1"], "item": url},
        ],
    }

    parts = [f'<p class="intro">{d["intro"]}</p>']
    if d.get("key_facts"):
        lis = "\n".join(f"            <li>{x}</li>" for x in d["key_facts"])
        parts.append(f'<div class="callout"><strong>{esc(ui["kf"])}</strong>\n        <ul>\n{lis}\n        </ul></div>')
    for h, body in d["sections"]:
        parts.append(f'<h2>{esc(h)}</h2>\n        {body}')
    faq_html = "\n".join(f'        <h3>{esc(q)}</h3>\n        <p>{esc(a)}</p>' for q, a in d["faqs"])
    parts.append(f'<h2>{esc(ui["faqh"])}</h2>\n{faq_html}')
    if d.get("disclaimer"):
        parts.append(f'<p class="disclaimer"><em>{esc(d["disclaimer"])}</em></p>')
    body_html = "\n\n        ".join(parts)

    out = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{esc(d['title'])}</title>
    <meta name="description" content="{esc(d['desc'])}">
    <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%232E4A40'/%3E%3Cpath fill='%23F2D8C4' d='M16 5.5S9.5 14 9.5 19a6.5 6.5 0 0013 0c0-5-6.5-13.5-6.5-13.5z'/%3E%3C/svg%3E" type="image/svg+xml">
    <link rel="stylesheet" href="../assets/seo.css">
    <link rel="canonical" href="{url}" />
    {alts}
    <link rel="alternate" hreflang="x-default" href="{SITE}/{subdir}/{slug}-en.html" />
    <meta property="og:title" content="{esc(d['title'])}" />
    <meta property="og:description" content="{esc(d['desc'])}" />
    <meta property="og:url" content="{url}" />
    <meta property="og:type" content="article" />
    <meta property="og:site_name" content="L'Or Vert" />
    <meta property="og:locale" content="{LOCALES[lang]}" />
    <meta property="og:image" content="{OG}" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{esc(d['title'])}" />
    <meta name="twitter:description" content="{esc(d['desc'])}" />
    <meta name="twitter:image" content="{OG}" />
    <script type="application/ld+json">{json.dumps(article, ensure_ascii=False, indent=2)}</script>
    <script type="application/ld+json">{json.dumps(faqpage, ensure_ascii=False, indent=2)}</script>
    <script type="application/ld+json">{json.dumps(crumbs, ensure_ascii=False, indent=2)}</script>
</head>
<body>
<nav class="site-nav"><div class="container"><a href="{ui['idx']}" class="logo">{esc(ui['nav'])}</a></div></nav>
<header class="page-hero" style="background: linear-gradient(135deg, var(--pine) 0%, var(--avocado-dark) 100%);">
    <div class="container">
        <div class="breadcrumb"><a href="{ui['idx']}">{esc(ui['home'])}</a> &raquo; {esc(ui['crumb1'])}</div>
        <h1>{esc(d['h1'])}</h1>
        <p class="lede">{esc(d['lede'])}</p>
    </div>
</header>
<main class="container">
    <article class="guide">
        {body_html}

        <div class="pillar-linkbox">
            <strong>{esc(ui['also'])}</strong>
            <a href="{ui['pillarhref']}">{esc(ui['pillar'])}</a>
            <a href="{ui['obshref']}">{esc(ui['obs'])}</a>
        </div>
    </article>
</main>
<footer class="site-footer"><div class="container"><h3>L'Or Vert</h3><p>{esc(ui['foot'])}</p><div class="copyright">&copy; 2026 — L'Or Vert</div></div></footer>
</body>
</html>
"""
    for m in re.findall(r'<script[^>]*ld\+json[^>]*>(.*?)</script>', out, re.S):
        json.loads(m)
    return out


def write_guide_cluster(slug, content_by_lang, subdir="guides"):
    n = 0
    for lang, d in content_by_lang.items():
        path = os.path.join(ROOT, subdir, f"{slug}-{lang}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(render(slug, lang, d, subdir))
        n += 1
    print(f"  {subdir}/{slug}: wrote {n} langs")
    return n

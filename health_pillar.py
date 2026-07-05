# -*- coding: utf-8 -*-
"""
health_pillar.py -- root-level "olive oil health benefits" pillar (x4 langs).
Biggest olive-oil topic, already AI-cited ("bienfaits huile d'olive"). Completes
the pillar trio (health / sustainability / tasting). Evidence-informed, cautious
YMYL + disclaimer. Article + HowTo ("how to get the benefits") + FAQPage +
BreadcrumbList JSON-LD. Venice-styled via seo.css.
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

SLUGS = {"fr": "bienfaits-huile-olive", "en": "olive-oil-health-benefits",
         "it": "benefici-olio-oliva", "el": "ofeli-elaioladou"}

UI = {
    "fr": dict(idx="index.html", nav="L'OR VERT", home="Accueil", crumb="Santé",
               pillar="huile-olive.html", pillarlbl="Guide pilier : l'huile d'olive",
               obs="observatoire-huile-olive-2026.html", obslbl="Observatoire qualité 2026",
               g1="guides/complete-guide-extra-virgin-olive-oil-for-health-fr.html", g1l="Approfondir : huile d'olive & santé",
               g2="guides/acide-oleique-bienfaits-fr.html", g2l="L'acide oléique",
               also="Ressources liées", toc="Sommaire", updated="Mis à jour", read="lecture",
               foot="Le carnet de référence de L'Or Vert sur l'huile d'olive, la cuisine méditerranéenne et les usages du quotidien."),
    "en": dict(idx="index-en.html", nav="L'OR VERT", home="Home", crumb="Health",
               pillar="olive-oil.html", pillarlbl="Pillar guide: olive oil",
               obs="olive-oil-observatory-2026.html", obslbl="2026 Quality Observatory",
               g1="guides/complete-guide-extra-virgin-olive-oil-for-health-en.html", g1l="In depth: olive oil & health",
               g2="guides/acide-oleique-bienfaits-en.html", g2l="Oleic acid",
               also="Related resources", toc="Contents", updated="Updated", read="read",
               foot="L'Or Vert's reference notebook on olive oil, Mediterranean cooking and everyday uses."),
    "it": dict(idx="index-it.html", nav="L'OR VERT", home="Home", crumb="Salute",
               pillar="olio-oliva.html", pillarlbl="Guida pilastro: olio d'oliva",
               obs="osservatorio-olio-oliva-2026.html", obslbl="Osservatorio qualità 2026",
               g1="guides/complete-guide-extra-virgin-olive-oil-for-health-it.html", g1l="Approfondisci: olio & salute",
               g2="guides/acide-oleique-bienfaits-it.html", g2l="Acido oleico",
               also="Risorse collegate", toc="Indice", updated="Aggiornato", read="lettura",
               foot="Il taccuino di riferimento di L'Or Vert su olio d'oliva, cucina mediterranea e usi quotidiani."),
    "el": dict(idx="index-el.html", nav="L'OR VERT", home="Αρχική", crumb="Υγεία",
               pillar="elaio-lado.html", pillarlbl="Κεντρικός οδηγός: ελαιόλαδο",
               obs="paratiritirio-elaio-lado-2026.html", obslbl="Παρατηρητήριο ποιότητας 2026",
               g1="guides/complete-guide-extra-virgin-olive-oil-for-health-el.html", g1l="Σε βάθος: ελαιόλαδο & υγεία",
               g2="guides/acide-oleique-bienfaits-el.html", g2l="Ελαϊκό οξύ",
               also="Σχετικές πηγές", toc="Περιεχόμενα", updated="Ενημερώθηκε", read="ανάγνωση",
               foot="Το σημειωματάριο αναφοράς του L'Or Vert για το ελαιόλαδο, τη μεσογειακή κουζίνα και την καθημερινή χρήση."),
}


def esc(s):
    return html.escape(s, quote=True)


def render(lang, d):
    ui = UI[lang]
    slug = SLUGS[lang]
    url = f"{SITE}/{slug}.html"
    alts = "\n    ".join(
        f'<link rel="alternate" hreflang="{lg}" href="{SITE}/{SLUGS[lg]}.html" />' for lg in LANGS)

    article = {
        "@context": "https://schema.org", "@type": "Article",
        "headline": d["h1"], "description": d["desc"],
        "author": {"@type": "Organization", "name": "L'Or Vert", "@id": f"{SITE}/#organization"},
        "publisher": {"@type": "Organization", "name": "L'Or Vert", "url": SITE,
                      "logo": {"@type": "ImageObject", "url": OG}},
        "datePublished": "2026-05-04", "dateModified": "2026-07-05",
        "inLanguage": lang, "articleSection": "Health", "image": OG,
        "keywords": d["keywords"], "isAccessibleForFree": True, "mainEntityOfPage": url,
    }
    howto = {
        "@context": "https://schema.org", "@type": "HowTo",
        "name": d["howto_name"], "description": d["howto_desc"], "inLanguage": lang,
        "step": [{"@type": "HowToStep", "position": i + 1, "name": n, "text": t}
                 for i, (n, t) in enumerate(d["howto_steps"])],
    }
    faqpage = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faqs"]],
    }
    crumbs = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": ui["home"], "item": f"{SITE}/{ui['idx']}"},
            {"@type": "ListItem", "position": 2, "name": ui["crumb"], "item": url},
        ],
    }

    kf = "\n".join(f"            <li>{x}</li>" for x in d["key_facts"])
    toc = "\n".join(f'            <a href="#{i}">{esc(l)}</a>' for i, l in d["toc"])
    secs = [f'<h2 id="{sid}">{esc(h)}</h2>\n        {body}' for sid, h, body in d["sections"]]
    faq_html = "\n".join(f'        <h3>{esc(q)}</h3>\n        <p>{esc(a)}</p>' for q, a in d["faqs"])
    body_html = (
        f'<p class="intro">{esc(d["intro"])}</p>\n\n        '
        f'<div class="callout"><strong>{esc(d["kf_label"])}</strong>\n        <ul>\n{kf}\n        </ul></div>\n\n        '
        f'<div class="pillar-toc"><strong>{esc(ui["toc"])}</strong>\n{toc}\n        </div>\n\n        '
        + "\n\n        ".join(secs)
        + f'\n\n        <h2 id="faq">{esc(d["faq_h"])}</h2>\n{faq_html}'
        + f'\n        <p class="disclaimer"><em>{esc(d["disclaimer"])}</em></p>'
    )

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{esc(d['title'])}</title>
    <meta name="description" content="{esc(d['desc'])}">
    <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%232E4A40'/%3E%3Cpath fill='%23F2D8C4' d='M16 5.5S9.5 14 9.5 19a6.5 6.5 0 0013 0c0-5-6.5-13.5-6.5-13.5z'/%3E%3C/svg%3E" type="image/svg+xml">
    <link rel="stylesheet" href="assets/seo.css">
    <link rel="canonical" href="{url}" />
    {alts}
    <link rel="alternate" hreflang="x-default" href="{SITE}/{SLUGS['en']}.html" />
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
    <script type="application/ld+json">{json.dumps(howto, ensure_ascii=False, indent=2)}</script>
    <script type="application/ld+json">{json.dumps(faqpage, ensure_ascii=False, indent=2)}</script>
    <script type="application/ld+json">{json.dumps(crumbs, ensure_ascii=False, indent=2)}</script>
</head>
<body>
<nav class="site-nav"><div class="container"><a href="{ui['idx']}" class="logo">{esc(ui['nav'])}</a></div></nav>
<header class="page-hero">
    <div class="container">
        <div class="breadcrumb"><a href="{ui['idx']}">{esc(ui['home'])}</a> &raquo; {esc(ui['crumb'])}</div>
        <h1>{esc(d['h1'])}</h1>
        <p class="lede">{esc(d['lede'])}</p>
        <div class="meta">{esc(ui['updated'])} 2026-07-05 · {esc(d['readtime'])} {esc(ui['read'])}</div>
    </div>
</header>
<main class="container">
    <article class="guide pillar-guide">
        {body_html}

        <div class="pillar-linkbox">
            <strong>{esc(ui['also'])}</strong>
            <a href="{ui['g1']}">{esc(ui['g1l'])}</a>
            <a href="{ui['g2']}">{esc(ui['g2l'])}</a>
            <a href="{ui['obs']}">{esc(ui['obslbl'])}</a>
            <a href="{ui['pillar']}">{esc(ui['pillarlbl'])}</a>
        </div>
    </article>
</main>
<footer class="site-footer"><div class="container"><h3>L'Or Vert</h3><p>{esc(ui['foot'])}</p><div class="copyright">&copy; 2026 — L'Or Vert</div></div></footer>
</body>
</html>
"""


def build(content):
    for lang, d in content.items():
        out = render(lang, d)
        for m in re.findall(r'<script[^>]*ld\+json[^>]*>(.*?)</script>', out, re.S):
            json.loads(m)
        path = os.path.join(ROOT, f"{SLUGS[lang]}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(out)
        print("wrote", os.path.basename(path), len(out), "bytes")

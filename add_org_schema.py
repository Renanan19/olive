# -*- coding: utf-8 -*-
"""
add_org_schema.py -- inject a factual Organization entity (JSON-LD) into the
highest-value pages (homepages, pillar guides, observatory) so search engines
and LLMs have a single, citable publisher entity to attribute facts to.

Idempotent: guarded by the @id "#organization".
"""

import os
import json

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://huiledefes.com"

PAGES = [
    "index.html", "index-en.html", "index-it.html", "index-el.html",
    "huile-olive.html", "olive-oil.html", "olio-oliva.html", "elaio-lado.html",
    "observatoire-huile-olive-2026.html", "olive-oil-observatory-2026.html",
    "osservatorio-olio-oliva-2026.html", "paratiritirio-elaio-lado-2026.html",
]

ORG = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "@id": f"{SITE}/#organization",
    "name": "L'Or Vert",
    "alternateName": "Huile de Fès",
    "url": f"{SITE}/",
    "logo": {
        "@type": "ImageObject",
        "url": f"{SITE}/assets/og-default.png",
        "width": 1200,
        "height": 630,
    },
    "image": f"{SITE}/assets/og-default.png",
    "description": ("Projet éditorial indépendant et multilingue (FR, EN, IT, EL) "
                    "consacré à l'huile d'olive extra vierge : méthode transparente "
                    "d'évaluation de la qualité, guides d'achat, contexte santé fondé "
                    "sur la composition, et recettes méditerranéennes."),
    "foundingDate": "2026",
    "knowsAbout": [
        "huile d'olive extra vierge", "extra virgin olive oil", "olive oil quality",
        "polyphénols", "acide oléique", "régime méditerranéen", "Mediterranean diet",
        "dégustation d'huile d'olive", "olive oil tasting", "conservation de l'huile d'olive",
        "cuisine méditerranéenne", "AOP / PDO olive oil",
    ],
    "publishingPrinciples": f"{SITE}/observatoire-huile-olive-2026.html",
    "areaServed": "Worldwide",
    "availableLanguage": ["fr", "en", "it", "el"],
}

BLOCK = ('    <script type="application/ld+json">\n'
         + json.dumps(ORG, ensure_ascii=False, indent=2)
         + "\n    </script>\n")


def main():
    done = 0
    for fn in PAGES:
        p = os.path.join(ROOT, fn)
        if not os.path.exists(p):
            continue
        with open(p, encoding="utf-8") as f:
            s = f.read()
        if "#organization" in s or "</head>" not in s.lower():
            continue
        idx = s.lower().index("</head>")
        s = s[:idx] + BLOCK + s[idx:]
        with open(p, "w", encoding="utf-8") as f:
            f.write(s)
        done += 1
    print(f"Organization schema added to {done} pages")


if __name__ == "__main__":
    main()

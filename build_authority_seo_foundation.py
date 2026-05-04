# -*- coding: utf-8 -*-
"""Build the multilingual authority layer for huiledefes.com.

This script creates long pillar pages, a citeable data observatory, authority
assets for outreach, internal links from every article, and a refreshed sitemap.
It is intentionally deterministic so the site can be regenerated without
duplicating blocks.
"""

from __future__ import annotations

import csv
import json
import re
from datetime import date
from html import escape
from pathlib import Path


ROOT = Path(".")
SITE = "https://huiledefes.com"
TODAY = date(2026, 5, 4).isoformat()


QUALITY_MATRIX = [
    {
        "criterion": "Harvest date",
        "weight": 20,
        "what_it_measures": "Freshness and probability of intact aromas",
        "evidence_to_request": "Harvest year, bottling date, lot number",
        "red_flags": "Only a distant best-before date, no harvest reference",
    },
    {
        "criterion": "Olive category",
        "weight": 18,
        "what_it_measures": "Whether the oil is extra virgin, virgin, refined or blended",
        "evidence_to_request": "Legal category on front or back label",
        "red_flags": "Vague wording such as pure, light or premium without legal category",
    },
    {
        "criterion": "Origin precision",
        "weight": 14,
        "what_it_measures": "Traceability beyond a broad marketing story",
        "evidence_to_request": "Producer, region, estate, mill, PDO or country blend statement",
        "red_flags": "Mediterranean blend with no practical traceability",
    },
    {
        "criterion": "Sensory balance",
        "weight": 14,
        "what_it_measures": "Fruitiness, clean bitterness, clean pungency and absence of defects",
        "evidence_to_request": "Tasting note, intensity scale, defect-free panel statement when available",
        "red_flags": "Greasy, flat, rancid, winey, metallic or muddy aroma",
    },
    {
        "criterion": "Packaging protection",
        "weight": 10,
        "what_it_measures": "Protection against light, oxygen and heat",
        "evidence_to_request": "Dark glass, tin, bag-in-box, tight closure, small format if slow use",
        "red_flags": "Clear bottle exposed to light or oversized bottle for slow household use",
    },
    {
        "criterion": "Use fit",
        "weight": 9,
        "what_it_measures": "Whether intensity matches raw use, cooking, baking or finishing",
        "evidence_to_request": "Suggested uses and intensity description",
        "red_flags": "One bottle presented as perfect for every use",
    },
    {
        "criterion": "Price coherence",
        "weight": 8,
        "what_it_measures": "Whether the price is credible for harvest, origin and packaging",
        "evidence_to_request": "Price per liter, format, producer model, certification",
        "red_flags": "Luxury claims with commodity-level proof, or suspiciously cheap extra virgin claims",
    },
    {
        "criterion": "Responsible sourcing",
        "weight": 7,
        "what_it_measures": "Agronomic, environmental and social credibility",
        "evidence_to_request": "Organic, regenerative, water, biodiversity or cooperative information",
        "red_flags": "Sustainability vocabulary without any concrete practice",
    },
]


PILLAR_PAGES = {
    "fr": {
        "slug": "huile-olive.html",
        "observatory": "observatoire-huile-olive-2026.html",
        "index": "index.html",
        "lang_label": "FR",
        "title": "Huile d'olive : le guide pilier complet pour choisir, goûter, cuisiner et conserver",
        "meta": "Guide pilier sur l'huile d'olive : extra vierge, bienfaits, goût, cuisson, conservation, labels, prix, recettes et méthode d'achat experte.",
        "h1": "Huile d'olive : le guide pilier complet",
        "lede": "La page centrale pour comprendre l'huile d'olive sans folklore inutile : comment la choisir, la goûter, l'utiliser, la conserver et reconnaître les signaux qui séparent une huile sérieuse d'une simple promesse marketing.",
        "short": "La meilleure huile d'olive pour un usage exigeant est généralement une huile d'olive vierge extra récente, traçable, protégée de la lumière, cohérente en goût et adaptée à votre usage réel : cru, cuisson douce, pâtisserie ou assaisonnement final.",
        "breadcrumb_home": "Accueil",
        "breadcrumb_current": "Guide pilier",
        "nav_logo": "L'OR VERT / GUIDE PILIER",
        "updated": "Mis à jour : 4 mai 2026 · dossier pilier",
        "toc_title": "Plan rapide",
        "stats": [
            ("8 critères", "grille d'achat"),
            ("4 usages", "cru, cuisson, pâtisserie, finition"),
            ("0 miracle", "des preuves et du contexte"),
            ("2026", "méthode mise à jour"),
        ],
        "sections": [
            {
                "id": "definition",
                "title": "Ce qu'est vraiment une bonne huile d'olive",
                "body": [
                    "Une bonne huile d'olive n'est pas seulement une huile qui sent l'olive. C'est un produit frais, fragile et lisible : on doit pouvoir comprendre son origine, sa catégorie, son usage conseillé, sa date de récolte et la manière dont il a été protégé avant d'arriver dans votre cuisine.",
                    "Le mot important est cohérence. Une huile peut être douce et excellente, ou très verte et excellente. Ce qui compte, c'est que le goût, le prix, l'étiquette, la bouteille et l'usage racontent la même histoire. Quand un de ces éléments manque, il faut ralentir et comparer.",
                ],
            },
            {
                "id": "categories",
                "title": "Extra vierge, vierge, raffinée : ne mélangez pas tout",
                "body": [
                    "L'huile d'olive vierge extra est obtenue par des procédés mécaniques et doit respecter des critères chimiques et sensoriels précis. Elle ne doit pas présenter de défaut organoleptique. C'est la catégorie à privilégier lorsque l'on cherche le goût, la fraîcheur et le meilleur potentiel nutritionnel.",
                    "Une huile vierge peut rester intéressante pour certains usages, mais elle tolère des défauts ou des niveaux analytiques moins exigeants. Les huiles raffinées ou les mélanges avec huile raffinée répondent à une autre logique : plus neutre, moins expressive, souvent moins chère, mais moins intéressante si l'objectif est de comprendre le caractère de l'olive.",
                    "L'erreur classique consiste à croire que toutes les mentions valorisantes se valent. Les mots « pure », « légère », « sélection », « tradition » ou « premium » peuvent être flatteurs, mais ils ne remplacent jamais la catégorie légale, l'origine et la date de récolte.",
                ],
            },
            {
                "id": "choisir",
                "title": "La méthode d'achat qui évite 80 % des mauvais choix",
                "body": [
                    "Commencez par retourner la bouteille. La face avant séduit ; la face arrière informe. Cherchez la catégorie exacte, la date de récolte si elle existe, l'origine, le conditionneur, le format, les conseils de conservation et les éventuels labels. Une bonne huile n'a pas besoin de tout cacher derrière une photo d'olivier.",
                    "Ensuite, reliez le prix au niveau de preuve. Une huile chère doit apporter davantage qu'une jolie étiquette : origine précise, producteur identifié, variété, récolte récente, packaging protecteur, analyse ou note de dégustation crédible. Une huile très bon marché peut être correcte pour cuire, mais elle ne doit pas prétendre jouer le même rôle qu'un grand fruité vert.",
                    "Enfin, achetez selon votre rythme. Une grande bouteille ouverte trop longtemps perd vite son intérêt. Si vous cuisinez peu, un format plus petit et plus frais vaut mieux qu'un litre prestigieux qui s'oxyde au placard.",
                ],
            },
            {
                "id": "gout",
                "title": "Goût : fruité, amertume et piquant sont des informations",
                "body": [
                    "Le goût d'une huile d'olive parle. Le fruité évoque l'olive fraîche, l'herbe, l'amande, la tomate, l'artichaut ou parfois des notes plus mûres. L'amertume et le piquant ne sont pas des défauts lorsqu'ils sont propres, nets et équilibrés. Ils signalent souvent une huile jeune, expressive et riche en composés phénoliques.",
                    "Le défaut arrive quand les sensations deviennent sales, rances, vineuses, métalliques, poussiéreuses ou lourdes. Une huile qui laisse une impression de vieille noix, de carton humide ou de graisse fatiguée ne devient pas meilleure parce qu'elle est chère ou bien racontée.",
                    "Pour progresser, goûtez l'huile seule puis sur un aliment simple : pain, tomate, pomme de terre vapeur, yaourt nature ou légume grillé. C'est là que l'équilibre apparaît : une bonne huile améliore le plat sans l'écraser.",
                ],
            },
            {
                "id": "sante",
                "title": "Santé : être précis sans vendre du miracle",
                "body": [
                    "L'huile d'olive est au cœur du régime méditerranéen, principalement grâce à sa richesse en acide oléique, à ses composés phénoliques et à sa capacité à remplacer des graisses moins intéressantes. Mais ce n'est pas un médicament, et aucune bouteille ne compense à elle seule une alimentation incohérente.",
                    "La phrase la plus honnête est simple : une bonne huile d'olive vierge extra peut être un excellent choix lipidique dans une alimentation équilibrée, surtout lorsqu'elle remplace beurre, sauces industrielles ou graisses de mauvaise qualité. Son intérêt dépend de la dose, de la fraîcheur, du reste de l'assiette et de la régularité.",
                    "Pour un contenu sérieux, il faut éviter deux excès : banaliser l'huile comme une simple graisse interchangeable, ou la présenter comme une solution magique. La crédibilité se gagne par la nuance.",
                ],
            },
            {
                "id": "cuisson",
                "title": "Cuisson : oui, mais pas n'importe comment",
                "body": [
                    "On peut cuisiner avec l'huile d'olive. Pour une cuisson domestique maîtrisée, une huile vierge extra de bonne qualité reste stable dans de nombreux usages : légumes sautés, poisson, volaille, œufs, pommes de terre, sauces courtes, four modéré. Le problème vient surtout de la surchauffe, de la fumée et de la réutilisation excessive.",
                    "Pour la friture longue ou très intensive, il faut raisonner coût, température, renouvellement et goût. Une huile très aromatique peut être magnifique à cru mais inutilement chère ou dominante pour un bain de friture. Gardez les bouteilles les plus expressives pour les finitions, les salades et les plats où le parfum compte vraiment.",
                    "En pâtisserie, l'huile d'olive donne du moelleux et une longueur aromatique remarquable, à condition de choisir une intensité adaptée. Une huile douce accompagne citron, amande, yaourt et chocolat ; une huile très verte convient mieux aux desserts assumés.",
                ],
            },
            {
                "id": "conservation",
                "title": "Conservation : la qualité se perd après l'achat",
                "body": [
                    "La lumière, l'air, la chaleur et le temps sont les vrais adversaires. Une huile excellente peut devenir ordinaire si elle reste près des plaques, dans une bouteille transparente ou ouverte pendant des mois. Le bon réflexe : placard frais, bouchon fermé, bouteille sombre ou bidon, consommation raisonnablement rapide après ouverture.",
                    "Ne confondez pas date de durabilité minimale et fraîcheur optimale. Une huile peut rester consommable tout en ayant perdu la partie la plus intéressante de son profil aromatique. Pour le goût, la récolte récente et le stockage comptent davantage qu'une promesse générale.",
                ],
            },
            {
                "id": "terroirs",
                "title": "Origines, variétés et terroirs : utiles si c'est vérifiable",
                "body": [
                    "Espagne, Italie, Grèce, France, Tunisie, Maroc, Portugal, Turquie, Croatie : chaque bassin produit des huiles très différentes. Mais l'origine ne suffit pas. Une huile industrielle floue peut venir d'un grand pays producteur ; une petite huile remarquable peut venir d'une région moins célèbre.",
                    "Les variétés aident à anticiper le style : Arbequina souvent plus douce, Picual plus verte et stable, Koroneiki intense et herbacée, Frantoio élégante, Picholine vive, Chemlali plus délicate selon les contextes. Ces repères ne sont pas des règles absolues, mais ils donnent un langage pour comparer.",
                    "Le vrai signal d'autorité est la traçabilité : producteur, moulin, terroir, variété, récolte, méthode. Plus l'information est précise, plus le lecteur peut vérifier, citer et revenir.",
                ],
            },
            {
                "id": "prix",
                "title": "Prix : ce qui est normal, ce qui doit vous alerter",
                "body": [
                    "Le prix d'une huile d'olive reflète la récolte, le rendement, la main-d'œuvre, l'emballage, le transport, les labels, la distribution et parfois la rareté. Une huile très bon marché peut exister, mais elle laisse peu de marge pour une récolte précoce, une sélection stricte, un stockage parfait et une petite production.",
                    "À l'inverse, un prix élevé ne prouve rien seul. Il doit être accompagné de preuves. Un bon achat n'est pas toujours le plus cher : c'est celui dont le niveau de preuve, le goût et l'usage correspondent à ce que vous allez réellement faire.",
                ],
            },
            {
                "id": "usages",
                "title": "Accords et usages : choisissez l'huile comme un ingrédient",
                "body": [
                    "Pour une salade de tomates, cherchez une huile fruitée, nette, capable d'apporter du relief. Pour un poisson délicat, une huile trop amère peut dominer. Pour des légumes grillés, une huile plus intense fonctionne très bien. Pour une purée, un houmous ou une soupe, ajoutez l'huile à la fin pour préserver l'arôme.",
                    "La règle pratique : plus le plat est simple, plus l'huile se voit. Sur pain, tomate, mozzarella, pois chiches, pommes de terre, agrumes ou chocolat, une huile médiocre devient évidente. Sur un plat très épicé ou longuement mijoté, une huile correcte et stable peut suffire.",
                ],
            },
            {
                "id": "autorite",
                "title": "Pourquoi cette page est pensée pour être citée",
                "body": [
                    "Un bon contenu sur l'huile d'olive ne doit pas répéter que l'huile est saine, méditerranéenne et authentique. Il doit aider à décider : quoi acheter, comment goûter, quand payer plus cher, quand économiser, comment stocker, comment cuisiner et quelles preuves demander.",
                    "C'est aussi ce qui aide les moteurs de recherche et les assistants IA. Une page claire, structurée, reliée à des guides spécialisés, dotée d'une grille de critères et capable de répondre sans exagération devient plus facile à comprendre, résumer et recommander.",
                    "Le dossier s'appuie donc sur une logique simple : réponse directe, explication, méthode, critères vérifiables, erreurs, liens internes et données réutilisables. La longueur sert la profondeur ; elle ne remplace jamais la preuve.",
                ],
            },
        ],
        "table_title": "Grille de décision rapide",
        "table_headers": ("Critère", "Ce qu'il faut chercher", "Signal d'alerte"),
        "quick_rows": [
            ("Récolte", "Année ou campagne récente clairement indiquée", "Seulement une date limite lointaine"),
            ("Origine", "Pays, région, producteur ou moulin identifiables", "Origine vague ou mélange sans précision"),
            ("Protection", "Verre sombre, bidon ou bag-in-box", "Bouteille claire exposée à la lumière"),
            ("Goût", "Fruité propre, amertume et piquant équilibrés", "Rance, plat, vineux, métallique"),
            ("Usage", "Intensité adaptée au plat", "Même discours pour tous les usages"),
        ],
        "method_title": "Méthode d'achat en 10 minutes",
        "method_steps": [
            "Définissez l'usage principal : cru, cuisson, pâtisserie ou finition.",
            "Vérifiez la catégorie : cherchez clairement « vierge extra » si vous voulez le meilleur profil.",
            "Cherchez la récolte ou au minimum un lot récent et cohérent.",
            "Regardez l'origine et le producteur plutôt que les photos d'oliviers.",
            "Choisissez un format adapté à votre vitesse de consommation.",
            "Goûtez seul, puis sur un aliment simple avant de juger.",
            "Notez si le prix correspond aux preuves visibles.",
        ],
        "mistakes_title": "Les erreurs qui font perdre de l'argent",
        "mistakes": [
            "Acheter un litre premium puis le garder ouvert six mois.",
            "Confondre douceur et qualité : une huile douce peut être grande, mais une huile plate ne l'est pas.",
            "Utiliser la meilleure bouteille pour une cuisson agressive où le parfum disparaît.",
            "Croire qu'un label remplace la dégustation, la fraîcheur et la conservation.",
            "Choisir seulement par pays sans regarder producteur, récolte et usage.",
        ],
        "faq_title": "Questions fréquentes",
        "faq": [
            ("Quelle est la meilleure huile d'olive ?", "La meilleure est celle qui combine catégorie vierge extra, fraîcheur, traçabilité, protection et adéquation à l'usage. Il n'existe pas une bouteille parfaite pour tout."),
            ("L'huile d'olive peut-elle chauffer ?", "Oui pour de nombreux usages domestiques maîtrisés. Évitez surtout la fumée, la surchauffe et les réutilisations répétées."),
            ("Le piquant est-il un défaut ?", "Non lorsqu'il est net et équilibré. Il peut indiquer la fraîcheur et la présence de composés phénoliques."),
            ("Faut-il acheter bio ?", "Le bio peut être un bon signal, mais il ne remplace pas la fraîcheur, la catégorie, le goût et la conservation."),
            ("Combien de temps garder une bouteille ouverte ?", "Le plus court possible après ouverture. Pour un foyer lent, mieux vaut un format plus petit et bien protégé."),
            ("Pourquoi certaines huiles sont très chères ?", "Rendement faible, récolte précoce, tri, petit volume, labels, packaging et distribution peuvent augmenter le prix. Le prix doit rester cohérent avec les preuves."),
        ],
        "related_title": "Continuer le dossier",
        "related": [
            ("Comment choisir une huile d'olive", "guides/comment-choisir-huile-olive.html"),
            ("Bienfaits santé de l'huile d'olive", "guides/bienfaits-sante-huile-olive.html"),
            ("Cuisiner avec l'huile d'olive", "guides/cuisiner-avec-huile-olive.html"),
            ("Conservation de l'huile d'olive", "guides/conservation-huile-olive-conseils.html"),
            ("Polyphénols de l'huile d'olive", "blog/pouvoir-polyphenols-huile-olive-fr.html"),
            ("Lire une étiquette", "blog/lire-etiquette-huile-olive-fr.html"),
            ("Accords mets et huiles", "blog/accords-mets-huiles-olive-fr.html"),
            ("Aïoli maison", "recipes/aioli-maison-huile-olive-fr.html"),
            ("Gâteau citron huile d'olive", "recipes/gateau-citron-huile-olive-fr.html"),
        ],
        "observatory_title": "Observatoire huile d'olive 2026 : critères de qualité et signaux d'achat",
        "observatory_meta": "Données et grille d'évaluation 2026 pour comparer les huiles d'olive : récolte, origine, goût, packaging, prix et usages.",
        "observatory_h1": "Observatoire huile d'olive 2026",
        "observatory_lede": "Une ressource courte, citables et réutilisable pour comparer les huiles d'olive avec des critères concrets plutôt qu'avec des slogans.",
        "observatory_intro": [
            "Cet observatoire rassemble une grille de décision pondérée. Elle ne remplace pas une analyse de laboratoire ni un jury de dégustation, mais elle permet de comparer des bouteilles de manière plus propre : chaque critère correspond à une preuve que l'on peut chercher sur l'étiquette, chez le producteur ou lors de la dégustation.",
            "L'objectif est simple : fournir une base que les journalistes, blogueurs, chefs, marques et assistants IA peuvent citer sans transformer l'huile d'olive en promesse magique.",
        ],
        "download_label": "Télécharger la matrice CSV",
        "pillar_label": "Guide pilier huile d'olive",
        "linkbox_title": "À lire aussi",
        "linkbox_text": "Pour replacer cet article dans le dossier principal, consultez le guide pilier complet sur l'huile d'olive.",
        "linkbox_data": "Voir l'observatoire 2026",
    },
    "en": {
        "slug": "olive-oil.html",
        "observatory": "olive-oil-observatory-2026.html",
        "index": "index-en.html",
        "lang_label": "EN",
        "title": "Olive oil: the complete pillar guide to buying, tasting, cooking and storing",
        "meta": "Complete olive oil pillar guide: extra virgin quality, health context, taste, cooking, storage, labels, price, recipes and buying method.",
        "h1": "Olive oil: the complete pillar guide",
        "lede": "A central, practical guide to olive oil: how to choose it, taste it, cook with it, store it and recognize the signals that separate a serious bottle from a marketing promise.",
        "short": "The best olive oil for demanding everyday use is usually a recent, traceable, well-protected extra virgin olive oil whose taste and intensity match the way you will actually use it: raw, cooked, baked or as a finishing ingredient.",
        "breadcrumb_home": "Home",
        "breadcrumb_current": "Pillar guide",
        "nav_logo": "L'OR VERT / PILLAR GUIDE",
        "updated": "Updated: May 4, 2026 · pillar dossier",
        "toc_title": "Quick map",
        "stats": [
            ("8 criteria", "buying framework"),
            ("4 uses", "raw, cooking, baking, finishing"),
            ("0 miracle", "evidence and context"),
            ("2026", "updated method"),
        ],
        "sections": [
            {
                "id": "definition",
                "title": "What a good olive oil really is",
                "body": [
                    "A good olive oil is not just a fat that smells vaguely Mediterranean. It is a fresh, fragile and readable product: you should be able to understand its category, origin, harvest context, packaging and intended use before you even taste it.",
                    "The key word is coherence. A mild oil can be excellent, and a bold green oil can also be excellent. What matters is whether the taste, price, label, packaging and use case support the same story. When one of those signals disappears, compare before you trust.",
                ],
            },
            {
                "id": "categories",
                "title": "Extra virgin, virgin, refined: the categories matter",
                "body": [
                    "Extra virgin olive oil is obtained by mechanical means and must meet chemical and sensory standards. It should have no sensory defect. This is the category to prioritize when you want aroma, freshness and the best nutritional potential.",
                    "Virgin olive oil may still be useful, but it allows a lower quality threshold. Refined olive oils and blends have another role: more neutral, usually cheaper, less expressive, and less relevant when the goal is to understand the character of the olive.",
                    "Do not let attractive language replace legal clarity. Words such as pure, light, premium, traditional or selected can sound reassuring, but the legal category, origin and harvest information carry more weight.",
                ],
            },
            {
                "id": "choisir",
                "title": "A buying method that avoids most bad choices",
                "body": [
                    "Start with the back label. The front sells; the back explains. Look for the exact category, harvest year if available, origin, producer or bottler, format, storage advice and certifications. Serious olive oil does not need to hide behind a romantic olive-tree picture.",
                    "Then connect price to proof. An expensive oil should provide more than a beautiful label: precise origin, identified producer, variety, recent harvest, protective packaging, credible analysis or a useful tasting note. A very cheap oil may be fine for some cooking, but it should not pretend to play the same role as a great early-harvest extra virgin.",
                    "Finally, buy for your rhythm. A large bottle opened for too long loses its advantage. If you use olive oil slowly, a smaller and fresher bottle is smarter than an impressive liter that oxidizes in the cupboard.",
                ],
            },
            {
                "id": "gout",
                "title": "Taste: fruitiness, bitterness and pungency are information",
                "body": [
                    "Olive oil speaks through taste. Fruitiness may suggest fresh olive, grass, almond, tomato leaf, artichoke or riper notes. Bitterness and pungency are not defects when they are clean, precise and balanced. They often point to freshness and phenolic compounds.",
                    "Defects appear when sensations become dirty, rancid, winey, metallic, muddy or tired. A bottle that smells like old nuts, damp cardboard or stale fat does not become good because the packaging is attractive.",
                    "To improve your judgement, taste the oil alone and then on simple food: bread, tomato, steamed potato, plain yogurt or grilled vegetables. That is where balance becomes obvious.",
                ],
            },
            {
                "id": "sante",
                "title": "Health: be precise, not miraculous",
                "body": [
                    "Olive oil sits at the heart of the Mediterranean diet because of oleic acid, phenolic compounds and its ability to replace less desirable fats. But it is not medicine, and no bottle can compensate for an inconsistent diet.",
                    "The honest position is simple: a good extra virgin olive oil can be an excellent fat choice within a balanced diet, especially when it replaces butter, industrial sauces or poor-quality fats. Its value depends on dose, freshness, the rest of the plate and regular habits.",
                    "Serious content avoids both extremes: treating olive oil as an interchangeable fat, or presenting it as a cure-all. Trust comes from nuance.",
                ],
            },
            {
                "id": "cuisson",
                "title": "Cooking: yes, with temperature awareness",
                "body": [
                    "You can cook with olive oil. For controlled home cooking, good extra virgin olive oil remains stable in many uses: sautéed vegetables, fish, poultry, eggs, potatoes, short sauces and moderate oven cooking. The main problem is overheating, smoking and repeated reuse.",
                    "For long or intensive frying, think about cost, temperature, renewal and taste. A very aromatic bottle may be beautiful raw but wasteful or dominant in a deep-frying context. Keep the most expressive oils for finishing, salads and dishes where fragrance truly matters.",
                    "In baking, olive oil creates softness and aromatic length. A mild oil works with lemon, almond, yogurt and chocolate; a very green oil suits more deliberate desserts.",
                ],
            },
            {
                "id": "conservation",
                "title": "Storage: quality can disappear after purchase",
                "body": [
                    "Light, air, heat and time are the real enemies. An excellent oil can become ordinary if it sits near the stove, in clear glass or open for months. Store it in a cool cupboard, keep the cap closed, prefer dark glass or tins, and finish it within a sensible period after opening.",
                    "Do not confuse minimum durability with peak freshness. An oil may remain edible while losing its most interesting aromatic profile. For taste, harvest recency and storage matter more than a generic promise.",
                ],
            },
            {
                "id": "terroirs",
                "title": "Origins, varieties and terroirs help when they are verifiable",
                "body": [
                    "Spain, Italy, Greece, France, Tunisia, Morocco, Portugal, Turkey and Croatia all produce very different oils. But origin alone is not enough. A vague industrial blend may come from a famous country, while a remarkable small oil may come from a less famous region.",
                    "Varieties help anticipate style: Arbequina is often milder, Picual greener and stable, Koroneiki intense and herbaceous, Frantoio elegant, Picholine vivid, Chemlali delicate depending on context. These are useful cues, not absolute rules.",
                    "The strongest authority signal is traceability: producer, mill, place, variety, harvest and method. The more precise the information, the easier it is to verify, cite and trust.",
                ],
            },
            {
                "id": "prix",
                "title": "Price: what is normal and what should raise suspicion",
                "body": [
                    "Olive oil price reflects harvest conditions, yield, labor, packaging, transport, certifications, distribution and sometimes scarcity. Very cheap olive oil can exist, but it leaves little room for early harvest, strict selection, perfect storage and small-scale production.",
                    "On the other hand, a high price proves nothing by itself. It must be supported by evidence. A good purchase is not always the most expensive bottle; it is the bottle whose proof, taste and use case match what you will actually do.",
                ],
            },
            {
                "id": "usages",
                "title": "Pairing and use: choose olive oil as an ingredient",
                "body": [
                    "For a tomato salad, choose a clean, fruity oil with enough lift. For delicate fish, too much bitterness can dominate. For grilled vegetables, a stronger oil can be excellent. For hummus, soup or mashed potatoes, add the oil at the end to preserve aroma.",
                    "The practical rule is this: the simpler the dish, the more visible the oil becomes. On bread, tomato, mozzarella, chickpeas, potatoes, citrus or chocolate, a mediocre oil has nowhere to hide.",
                ],
            },
            {
                "id": "autorite",
                "title": "Why this page is built to be cited",
                "body": [
                    "Strong olive oil content should not merely repeat that olive oil is healthy, Mediterranean and authentic. It should help people decide what to buy, how to taste, when to pay more, when to save money, how to store, how to cook and what proof to request.",
                    "That is also what helps search engines and AI assistants. A clear, structured page connected to specialized guides, supported by a decision framework and written without exaggeration is easier to understand, summarize and recommend.",
                    "The structure here follows a practical chain: direct answer, explanation, method, verifiable criteria, mistakes, internal references and reusable data. Length supports depth; it never replaces evidence.",
                ],
            },
        ],
        "table_title": "Fast decision grid",
        "table_headers": ("Criterion", "What to look for", "Warning sign"),
        "quick_rows": [
            ("Harvest", "Recent year or campaign clearly stated", "Only a distant best-before date"),
            ("Origin", "Country, region, producer or mill identified", "Vague origin or blend with no detail"),
            ("Protection", "Dark glass, tin or bag-in-box", "Clear bottle exposed to light"),
            ("Taste", "Clean fruitiness, balanced bitterness and pungency", "Rancid, flat, winey or metallic"),
            ("Use", "Intensity matched to the dish", "Same claim for every use"),
        ],
        "method_title": "10-minute buying method",
        "method_steps": [
            "Define the main use: raw, cooking, baking or finishing.",
            "Check the category: look for extra virgin if you want the best profile.",
            "Look for harvest year or at least a coherent recent lot.",
            "Read origin and producer details before trusting imagery.",
            "Choose a format that matches your consumption speed.",
            "Taste alone, then on simple food.",
            "Check whether price matches visible proof.",
        ],
        "mistakes_title": "Mistakes that waste money",
        "mistakes": [
            "Buying a premium liter and keeping it open for six months.",
            "Confusing mildness with quality: mild can be great, flat cannot.",
            "Using the best bottle for aggressive cooking where aroma disappears.",
            "Believing a certification replaces tasting, freshness and storage.",
            "Choosing by country alone without checking producer, harvest and use.",
        ],
        "faq_title": "Frequently asked questions",
        "faq": [
            ("What is the best olive oil?", "The best oil combines extra virgin category, freshness, traceability, protection and fit for use. No single bottle is perfect for everything."),
            ("Can olive oil be heated?", "Yes for many controlled home uses. Avoid smoking, overheating and repeated reuse."),
            ("Is pungency a defect?", "No when it is clean and balanced. It can signal freshness and phenolic compounds."),
            ("Should I buy organic?", "Organic can be a useful signal, but it does not replace freshness, category, taste and storage."),
            ("How long should an opened bottle last?", "As short as practical. Slow households should buy smaller, well-protected formats."),
            ("Why are some oils expensive?", "Low yields, early harvest, sorting, small volume, certifications, packaging and distribution can raise price. The price still needs proof."),
        ],
        "related_title": "Continue the dossier",
        "related": [
            ("How to choose olive oil", "guides/how-to-choose-best-olive-oil.html"),
            ("Health benefits of olive oil", "guides/health-benefits-olive-oil.html"),
            ("Cooking with olive oil", "guides/cooking-with-olive-oil.html"),
            ("Olive oil storage tips", "guides/olive-oil-storage-tips.html"),
            ("Olive oil polyphenols", "blog/pouvoir-polyphenols-huile-olive-en.html"),
            ("How to read an olive oil label", "blog/lire-etiquette-huile-olive-en.html"),
            ("Food pairings", "blog/accords-mets-huiles-olive-en.html"),
            ("Homemade aioli", "recipes/aioli-maison-huile-olive-en.html"),
            ("Lemon olive oil cake", "recipes/gateau-citron-huile-olive-en.html"),
        ],
        "observatory_title": "Olive Oil Observatory 2026: quality criteria and buying signals",
        "observatory_meta": "Data and 2026 evaluation framework for comparing olive oils by harvest, origin, taste, packaging, price and use.",
        "observatory_h1": "Olive Oil Observatory 2026",
        "observatory_lede": "A concise, citeable and reusable resource for comparing olive oils with concrete criteria instead of slogans.",
        "observatory_intro": [
            "This observatory provides a weighted decision grid. It does not replace laboratory analysis or professional panel tasting, but it makes bottle comparison cleaner: each criterion maps to evidence you can seek on a label, from a producer or during tasting.",
            "The goal is to give journalists, bloggers, chefs, brands and AI assistants a source they can cite without turning olive oil into a miracle claim.",
        ],
        "download_label": "Download the CSV matrix",
        "pillar_label": "Olive oil pillar guide",
        "linkbox_title": "Read next",
        "linkbox_text": "To place this article inside the main dossier, read the complete olive oil pillar guide.",
        "linkbox_data": "See the 2026 observatory",
    },
    "it": {
        "slug": "olio-oliva.html",
        "observatory": "osservatorio-olio-oliva-2026.html",
        "index": "index-it.html",
        "lang_label": "IT",
        "title": "Olio d'oliva: guida pilastro completa per scegliere, assaggiare, cucinare e conservare",
        "meta": "Guida pilastro sull'olio d'oliva: extravergine, benefici, gusto, cucina, conservazione, etichette, prezzo, ricette e metodo d'acquisto.",
        "h1": "Olio d'oliva: la guida pilastro completa",
        "lede": "La pagina centrale per capire l'olio d'oliva con criteri concreti: come sceglierlo, assaggiarlo, usarlo in cucina, conservarlo e riconoscere i segnali di una bottiglia seria.",
        "short": "Il miglior olio d'oliva per un uso esigente è di solito un extravergine recente, tracciabile, ben protetto dalla luce e coerente con l'uso reale: crudo, cottura, dolci o finitura.",
        "breadcrumb_home": "Home",
        "breadcrumb_current": "Guida pilastro",
        "nav_logo": "L'OR VERT / GUIDA PILASTRO",
        "updated": "Aggiornato: 4 maggio 2026 · dossier pilastro",
        "toc_title": "Mappa rapida",
        "stats": [
            ("8 criteri", "griglia d'acquisto"),
            ("4 usi", "crudo, cottura, dolci, finitura"),
            ("0 miracoli", "prove e contesto"),
            ("2026", "metodo aggiornato"),
        ],
        "sections": [
            {
                "id": "definition",
                "title": "Che cos'è davvero un buon olio d'oliva",
                "body": [
                    "Un buon olio d'oliva non è soltanto un grasso dal profumo mediterraneo. È un prodotto fresco, fragile e leggibile: categoria, origine, raccolto, confezione e uso consigliato devono essere comprensibili prima ancora dell'assaggio.",
                    "La parola chiave è coerenza. Un olio delicato può essere eccellente, come può esserlo un fruttato verde intenso. Conta l'allineamento tra gusto, prezzo, etichetta, protezione e uso. Quando un segnale manca, conviene confrontare.",
                ],
            },
            {
                "id": "categories",
                "title": "Extravergine, vergine, raffinato: le categorie contano",
                "body": [
                    "L'olio extravergine d'oliva è ottenuto con procedimenti meccanici e deve rispettare criteri chimici e sensoriali precisi. Non dovrebbe presentare difetti organolettici. È la categoria da privilegiare per aroma, freschezza e potenziale nutrizionale.",
                    "L'olio vergine può essere utile in alcuni contesti, ma ha una soglia qualitativa meno esigente. Gli oli raffinati o i blend con raffinato rispondono a un'altra logica: più neutri, spesso meno costosi, meno espressivi.",
                    "Le parole seducenti non bastano. Puro, leggero, tradizionale o premium non sostituiscono categoria legale, origine, data di raccolta e prova sensoriale.",
                ],
            },
            {
                "id": "choisir",
                "title": "Il metodo d'acquisto che evita la maggior parte degli errori",
                "body": [
                    "Partite dal retro della bottiglia. Il fronte seduce; il retro informa. Cercate categoria, annata di raccolta se presente, origine, produttore o confezionatore, formato, consigli di conservazione e certificazioni.",
                    "Poi collegate il prezzo alle prove. Un olio costoso deve offrire più di una bella etichetta: origine precisa, produttore identificabile, varietà, raccolto recente, confezione protettiva, analisi o nota di degustazione credibile.",
                    "Infine acquistate secondo il vostro ritmo. Una bottiglia grande aperta troppo a lungo perde rapidamente interesse. Se consumate lentamente, un formato più piccolo e fresco è una scelta più intelligente.",
                ],
            },
            {
                "id": "gout",
                "title": "Gusto: fruttato, amaro e piccante sono informazioni",
                "body": [
                    "L'olio parla attraverso il gusto. Il fruttato può ricordare oliva fresca, erba, mandorla, foglia di pomodoro, carciofo o note più mature. Amaro e piccante non sono difetti quando sono puliti, netti ed equilibrati.",
                    "Il difetto arriva quando le sensazioni diventano rancide, vinose, metalliche, fangose o stanche. Una bottiglia che ricorda noci vecchie o cartone umido non diventa buona grazie al packaging.",
                    "Assaggiate l'olio da solo, poi su pane, pomodoro, patata lessa, yogurt naturale o verdure grigliate. Su alimenti semplici, l'equilibrio non si nasconde.",
                ],
            },
            {
                "id": "sante",
                "title": "Salute: precisione, non miracoli",
                "body": [
                    "L'olio d'oliva è centrale nella dieta mediterranea grazie all'acido oleico, ai composti fenolici e alla capacità di sostituire grassi meno interessanti. Ma non è un farmaco e nessuna bottiglia corregge da sola un'alimentazione incoerente.",
                    "La posizione seria è semplice: un buon extravergine può essere un'ottima scelta lipidica in una dieta equilibrata, soprattutto quando sostituisce burro, salse industriali o grassi di bassa qualità.",
                    "La fiducia nasce dalla misura: né grasso banale e intercambiabile, né soluzione magica. Il contesto conta.",
                ],
            },
            {
                "id": "cuisson",
                "title": "Cottura: sì, con controllo della temperatura",
                "body": [
                    "Si può cucinare con olio d'oliva. In una cottura domestica controllata, un buon extravergine resta adatto a verdure saltate, pesce, pollo, uova, patate, sughi brevi e forno moderato. Il problema è il surriscaldamento, il fumo e il riutilizzo eccessivo.",
                    "Per fritture lunghe o intensive bisogna ragionare su costo, temperatura, rinnovo e gusto. Un olio molto aromatico può essere magnifico a crudo ma inutilemente costoso o dominante in un bagno di frittura.",
                    "Nei dolci, l'olio d'oliva dona morbidezza e profondità aromatica. Un olio dolce accompagna limone, mandorla, yogurt e cioccolato; uno molto verde richiede una ricetta più decisa.",
                ],
            },
            {
                "id": "conservation",
                "title": "Conservazione: la qualità si perde dopo l'acquisto",
                "body": [
                    "Luce, aria, calore e tempo sono i veri nemici. Un olio eccellente diventa ordinario se resta vicino ai fornelli, in vetro trasparente o aperto per mesi. Meglio un armadio fresco, tappo chiuso, vetro scuro o latta, e consumo rapido dopo l'apertura.",
                    "Non confondete termine minimo di conservazione e freschezza ideale. Un olio può restare commestibile ma perdere la parte aromatica più interessante.",
                ],
            },
            {
                "id": "terroirs",
                "title": "Origini, cultivar e territori: utili se verificabili",
                "body": [
                    "Spagna, Italia, Grecia, Francia, Tunisia, Marocco, Portogallo, Turchia e Croazia producono oli molto diversi. Ma l'origine non basta. Un blend vago può venire da un grande Paese produttore; una piccola bottiglia notevole può arrivare da una regione meno famosa.",
                    "Le cultivar aiutano a prevedere lo stile: Arbequina spesso più dolce, Picual più verde e stabile, Koroneiki intensa ed erbacea, Frantoio elegante, Picholine vivace, Chemlali delicata secondo il contesto.",
                    "Il segnale più forte è la tracciabilità: produttore, frantoio, territorio, varietà, raccolto e metodo. Più l'informazione è precisa, più è citabile.",
                ],
            },
            {
                "id": "prix",
                "title": "Prezzo: normale, sospetto, giustificato",
                "body": [
                    "Il prezzo riflette raccolto, resa, manodopera, imballaggio, trasporto, certificazioni, distribuzione e talvolta rarità. Un olio molto economico può esistere, ma lascia poco spazio a raccolta precoce, selezione severa e stoccaggio perfetto.",
                    "Un prezzo alto, però, non prova nulla da solo. Deve essere accompagnato da elementi verificabili. Il miglior acquisto non è sempre il più caro, ma quello più coerente con prove, gusto e uso.",
                ],
            },
            {
                "id": "usages",
                "title": "Abbinamenti e usi: scegliete l'olio come ingrediente",
                "body": [
                    "Per un'insalata di pomodori serve un olio fruttato e netto. Per un pesce delicato, troppa amarezza può dominare. Per verdure grigliate, un olio più intenso funziona molto bene. Per zuppe, hummus o purè, aggiungetelo alla fine.",
                    "La regola pratica: più il piatto è semplice, più l'olio si vede. Su pane, pomodoro, mozzarella, ceci, patate, agrumi o cioccolato, un olio mediocre non può nascondersi.",
                ],
            },
            {
                "id": "autorite",
                "title": "Perché questa pagina è pensata per essere citata",
                "body": [
                    "Un contenuto forte sull'olio d'oliva non ripete solo che è sano, mediterraneo e autentico. Aiuta a decidere: cosa comprare, come assaggiare, quando pagare di più, quando risparmiare, come conservare e quali prove chiedere.",
                    "Questo aiuta anche motori di ricerca e assistenti IA: una pagina chiara, strutturata, collegata a guide specialistiche e basata su criteri verificabili è più facile da capire, riassumere e consigliare.",
                    "La struttura segue una catena pratica: risposta diretta, spiegazione, metodo, criteri, errori, link interni e dati riutilizzabili.",
                ],
            },
        ],
        "table_title": "Griglia decisionale rapida",
        "table_headers": ("Criterio", "Cosa cercare", "Segnale d'allarme"),
        "quick_rows": [
            ("Raccolto", "Annata o campagna recente indicata", "Solo una scadenza lontana"),
            ("Origine", "Paese, regione, produttore o frantoio", "Origine vaga o blend senza dettagli"),
            ("Protezione", "Vetro scuro, latta o bag-in-box", "Bottiglia trasparente esposta alla luce"),
            ("Gusto", "Fruttato pulito, amaro e piccante equilibrati", "Rancido, piatto, vinoso o metallico"),
            ("Uso", "Intensità adatta al piatto", "Stessa promessa per ogni uso"),
        ],
        "method_title": "Metodo d'acquisto in 10 minuti",
        "method_steps": [
            "Definite l'uso principale: crudo, cottura, dolci o finitura.",
            "Controllate la categoria: cercate extravergine se volete il profilo migliore.",
            "Cercate raccolto recente o almeno un lotto coerente.",
            "Leggete origine e produttore prima delle immagini.",
            "Scegliete un formato adatto al vostro consumo.",
            "Assaggiate da solo e poi su un alimento semplice.",
            "Verificate se il prezzo corrisponde alle prove visibili.",
        ],
        "mistakes_title": "Errori che fanno sprecare denaro",
        "mistakes": [
            "Comprare un litro premium e tenerlo aperto sei mesi.",
            "Confondere dolcezza e qualità: delicato può essere grande, piatto no.",
            "Usare la bottiglia migliore in una cottura aggressiva.",
            "Credere che una certificazione sostituisca assaggio, freschezza e conservazione.",
            "Scegliere solo per Paese senza guardare produttore, raccolto e uso.",
        ],
        "faq_title": "Domande frequenti",
        "faq": [
            ("Qual è il miglior olio d'oliva?", "Quello che combina extravergine, freschezza, tracciabilità, protezione e uso corretto. Non esiste una bottiglia perfetta per tutto."),
            ("L'olio d'oliva può scaldarsi?", "Sì in molti usi domestici controllati. Evitate fumo, surriscaldamento e riutilizzi ripetuti."),
            ("Il piccante è un difetto?", "No se è netto ed equilibrato. Può segnalare freschezza e composti fenolici."),
            ("Meglio biologico?", "Il biologico può aiutare, ma non sostituisce freschezza, categoria, gusto e conservazione."),
            ("Quanto dura una bottiglia aperta?", "Il meno possibile. Se consumate lentamente, scegliete formati piccoli e protetti."),
            ("Perché alcuni oli costano molto?", "Resa bassa, raccolta precoce, selezione, piccoli volumi, certificazioni e confezione possono incidere. Servono comunque prove."),
        ],
        "related_title": "Continuare il dossier",
        "related": [
            ("Come scegliere l'olio d'oliva", "guides/come-scegliere-migliore-olio-oliva.html"),
            ("Benefici salute dell'olio d'oliva", "guides/benefici-salute-olio-oliva.html"),
            ("Cucinare con olio d'oliva", "guides/cucinare-con-olio-oliva.html"),
            ("Conservazione dell'olio d'oliva", "guides/consigli-conservazione-olio-oliva.html"),
            ("Polifenoli dell'olio d'oliva", "blog/pouvoir-polyphenols-huile-olive-it.html"),
            ("Leggere l'etichetta", "blog/lire-etiquette-huile-olive-it.html"),
            ("Abbinamenti cibo e olio", "blog/accords-mets-huiles-olive-it.html"),
            ("Aioli fatto in casa", "recipes/aioli-maison-huile-olive-it.html"),
            ("Torta al limone e olio d'oliva", "recipes/gateau-citron-huile-olive-it.html"),
        ],
        "observatory_title": "Osservatorio olio d'oliva 2026: criteri di qualità e segnali d'acquisto",
        "observatory_meta": "Dati e griglia 2026 per confrontare oli d'oliva: raccolto, origine, gusto, confezione, prezzo e usi.",
        "observatory_h1": "Osservatorio olio d'oliva 2026",
        "observatory_lede": "Una risorsa breve, citabile e riutilizzabile per confrontare oli d'oliva con criteri concreti invece di slogan.",
        "observatory_intro": [
            "Questo osservatorio raccoglie una griglia decisionale ponderata. Non sostituisce analisi di laboratorio o panel professionali, ma permette di confrontare bottiglie in modo più pulito.",
            "L'obiettivo è fornire a giornalisti, blogger, chef, marchi e assistenti IA una fonte citabile senza trasformare l'olio d'oliva in promessa miracolosa.",
        ],
        "download_label": "Scaricare la matrice CSV",
        "pillar_label": "Guida pilastro olio d'oliva",
        "linkbox_title": "Da leggere anche",
        "linkbox_text": "Per inserire questo articolo nel dossier principale, leggete la guida pilastro completa sull'olio d'oliva.",
        "linkbox_data": "Vedere l'osservatorio 2026",
    },
    "el": {
        "slug": "elaio-lado.html",
        "observatory": "paratiritirio-elaio-lado-2026.html",
        "index": "index-el.html",
        "lang_label": "EL",
        "title": "Ελαιόλαδο: πλήρης κεντρικός οδηγός για επιλογή, γεύση, μαγείρεμα και συντήρηση",
        "meta": "Πλήρης οδηγός για το ελαιόλαδο: έξτρα παρθένο, γεύση, υγεία, μαγείρεμα, συντήρηση, ετικέτα, τιμή και πρακτική μέθοδος αγοράς.",
        "h1": "Ελαιόλαδο: ο πλήρης κεντρικός οδηγός",
        "lede": "Η κεντρική σελίδα για να καταλάβετε το ελαιόλαδο με πρακτικά κριτήρια: πώς το επιλέγουμε, το δοκιμάζουμε, το χρησιμοποιούμε στην κουζίνα, το φυλάμε και το αξιολογούμε χωρίς υπερβολές.",
        "short": "Το καλύτερο ελαιόλαδο για απαιτητική καθημερινή χρήση είναι συνήθως ένα πρόσφατο, ιχνηλάσιμο, καλά προστατευμένο έξτρα παρθένο ελαιόλαδο, με γεύση και ένταση που ταιριάζουν στην πραγματική χρήση σας.",
        "breadcrumb_home": "Αρχική",
        "breadcrumb_current": "Κεντρικός οδηγός",
        "nav_logo": "L'OR VERT / ΚΕΝΤΡΙΚΟΣ ΟΔΗΓΟΣ",
        "updated": "Ενημέρωση: 4 Μαΐου 2026 · κεντρικός φάκελος",
        "toc_title": "Γρήγορος χάρτης",
        "stats": [
            ("8 κριτήρια", "πλαίσιο αγοράς"),
            ("4 χρήσεις", "ωμό, μαγείρεμα, γλυκά, τελείωμα"),
            ("0 θαύματα", "αποδείξεις και πλαίσιο"),
            ("2026", "ενημερωμένη μέθοδος"),
        ],
        "sections": [
            {
                "id": "definition",
                "title": "Τι είναι πραγματικά ένα καλό ελαιόλαδο",
                "body": [
                    "Ένα καλό ελαιόλαδο δεν είναι απλώς ένα προϊόν με μεσογειακή εικόνα. Είναι φρέσκο, ευαίσθητο και κατανοητό: κατηγορία, προέλευση, συγκομιδή, συσκευασία και προτεινόμενη χρήση πρέπει να φαίνονται καθαρά.",
                    "Η βασική λέξη είναι συνοχή. Ένα ήπιο λάδι μπορεί να είναι εξαιρετικό, όπως και ένα έντονο πράσινο λάδι. Σημασία έχει αν γεύση, τιμή, ετικέτα, προστασία και χρήση λένε την ίδια ιστορία.",
                ],
            },
            {
                "id": "categories",
                "title": "Έξτρα παρθένο, παρθένο, ραφιναρισμένο: οι κατηγορίες μετράνε",
                "body": [
                    "Το έξτρα παρθένο ελαιόλαδο παράγεται με μηχανικές μεθόδους και πρέπει να πληροί συγκεκριμένα χημικά και οργανοληπτικά κριτήρια. Δεν πρέπει να έχει γευστικά ελαττώματα.",
                    "Το παρθένο μπορεί να είναι χρήσιμο σε ορισμένες περιπτώσεις, αλλά η ποιοτική απαίτηση είναι χαμηλότερη. Τα ραφιναρισμένα λάδια και τα μείγματα έχουν άλλο ρόλο: πιο ουδέτερα, συχνά φθηνότερα, λιγότερο εκφραστικά.",
                    "Λέξεις όπως αγνό, ελαφρύ, παραδοσιακό ή premium δεν αντικαθιστούν την κατηγορία, την προέλευση και τη συγκομιδή.",
                ],
            },
            {
                "id": "choisir",
                "title": "Μέθοδος αγοράς που αποφεύγει τα περισσότερα λάθη",
                "body": [
                    "Ξεκινήστε από την πίσω ετικέτα. Η μπροστινή πλευρά πουλάει, η πίσω εξηγεί. Αναζητήστε κατηγορία, συγκομιδή, προέλευση, παραγωγό ή εμφιαλωτή, μέγεθος, συντήρηση και πιστοποιήσεις.",
                    "Συνδέστε την τιμή με αποδείξεις. Ένα ακριβό λάδι πρέπει να δίνει περισσότερα από όμορφη συσκευασία: ακριβή προέλευση, παραγωγό, ποικιλία, πρόσφατη συγκομιδή, προστατευτική συσκευασία ή αξιόπιστη γευστική περιγραφή.",
                    "Αγοράστε με βάση τον ρυθμό κατανάλωσης. Μια μεγάλη φιάλη που μένει ανοικτή πολύ καιρό χάνει το πλεονέκτημά της.",
                ],
            },
            {
                "id": "gout",
                "title": "Γεύση: φρουτώδες, πικρό και πικάντικο δίνουν πληροφορία",
                "body": [
                    "Το ελαιόλαδο μιλάει μέσα από τη γεύση. Το φρουτώδες μπορεί να θυμίζει φρέσκια ελιά, χορτάρι, αμύγδαλο, φύλλο ντομάτας ή αγκινάρα. Το πικρό και το πικάντικο δεν είναι ελαττώματα όταν είναι καθαρά και ισορροπημένα.",
                    "Ελάττωμα υπάρχει όταν η αίσθηση γίνεται ταγγή, κρασώδης, μεταλλική, βαριά ή κουρασμένη. Μια ωραία ετικέτα δεν διορθώνει ένα λάδι που μυρίζει παλιό.",
                    "Δοκιμάστε το μόνο του και μετά πάνω σε απλό τρόφιμο: ψωμί, ντομάτα, πατάτα, γιαούρτι ή ψητά λαχανικά. Εκεί φαίνεται η ισορροπία.",
                ],
            },
            {
                "id": "sante",
                "title": "Υγεία: ακρίβεια χωρίς θαυματουργές υποσχέσεις",
                "body": [
                    "Το ελαιόλαδο είναι βασικό στη μεσογειακή διατροφή χάρη στο ελαϊκό οξύ, στις φαινολικές ενώσεις και στην ικανότητά του να αντικαθιστά λιγότερο ενδιαφέροντα λιπαρά. Δεν είναι όμως φάρμακο.",
                    "Η σοβαρή θέση είναι απλή: ένα καλό έξτρα παρθένο ελαιόλαδο μπορεί να είναι εξαιρετική επιλογή μέσα σε ισορροπημένη διατροφή, ιδιαίτερα όταν αντικαθιστά βούτυρο, βιομηχανικές σάλτσες ή χαμηλής ποιότητας λίπη.",
                    "Η αξιοπιστία χτίζεται με μέτρο και πλαίσιο, όχι με υπερβολή.",
                ],
            },
            {
                "id": "cuisson",
                "title": "Μαγείρεμα: ναι, με έλεγχο θερμοκρασίας",
                "body": [
                    "Μπορείτε να μαγειρέψετε με ελαιόλαδο. Σε ελεγχόμενη οικιακή χρήση, ένα καλό έξτρα παρθένο ταιριάζει σε λαχανικά, ψάρι, κοτόπουλο, αυγά, πατάτες, σύντομες σάλτσες και μέτριο φούρνο.",
                    "Το πρόβλημα είναι η υπερθέρμανση, ο καπνός και η επαναλαμβανόμενη χρήση. Για μακρύ τηγάνισμα πρέπει να σκεφτείτε κόστος, θερμοκρασία, ανανέωση και γεύση.",
                    "Στα γλυκά, το ελαιόλαδο δίνει απαλότητα και αρωματικό βάθος. Ένα ήπιο λάδι ταιριάζει με λεμόνι, αμύγδαλο, γιαούρτι και σοκολάτα.",
                ],
            },
            {
                "id": "conservation",
                "title": "Συντήρηση: η ποιότητα χάνεται μετά την αγορά",
                "body": [
                    "Φως, αέρας, θερμότητα και χρόνος είναι οι βασικοί εχθροί. Ένα εξαιρετικό λάδι γίνεται συνηθισμένο αν μένει κοντά στην κουζίνα, σε διάφανο μπουκάλι ή ανοικτό για μήνες.",
                    "Κρατήστε το σε δροσερό ντουλάπι, κλείνετε καλά το καπάκι, προτιμήστε σκούρο γυαλί ή μεταλλικό δοχείο και καταναλώστε το σε λογικό χρόνο.",
                ],
            },
            {
                "id": "terroirs",
                "title": "Προελεύσεις, ποικιλίες και τόποι: χρήσιμα όταν ελέγχονται",
                "body": [
                    "Ισπανία, Ιταλία, Ελλάδα, Γαλλία, Τυνησία, Μαρόκο, Πορτογαλία, Τουρκία και Κροατία παράγουν πολύ διαφορετικά ελαιόλαδα. Η προέλευση όμως δεν αρκεί από μόνη της.",
                    "Οι ποικιλίες βοηθούν να προβλέψουμε στυλ: Arbequina πιο ήπια, Picual πιο πράσινη και σταθερή, Koroneiki έντονη και χορτώδης, Frantoio κομψή, Picholine ζωντανή.",
                    "Το πιο δυνατό σήμα αξιοπιστίας είναι η ιχνηλασιμότητα: παραγωγός, ελαιοτριβείο, τόπος, ποικιλία, συγκομιδή και μέθοδος.",
                ],
            },
            {
                "id": "prix",
                "title": "Τιμή: πότε είναι λογική και πότε ύποπτη",
                "body": [
                    "Η τιμή επηρεάζεται από συγκομιδή, απόδοση, εργασία, συσκευασία, μεταφορά, πιστοποιήσεις, διανομή και σπανιότητα. Ένα πολύ φθηνό λάδι μπορεί να υπάρχει, αλλά αφήνει μικρό περιθώριο για πρώιμη συγκομιδή και αυστηρή επιλογή.",
                    "Από την άλλη, η υψηλή τιμή δεν αποδεικνύει τίποτα μόνη της. Πρέπει να συνοδεύεται από στοιχεία. Η καλύτερη αγορά είναι η πιο συνεπής με χρήση, γεύση και αποδείξεις.",
                ],
            },
            {
                "id": "usages",
                "title": "Χρήσεις και συνδυασμοί: επιλέξτε λάδι σαν συστατικό",
                "body": [
                    "Για σαλάτα ντομάτας θέλετε καθαρό και φρουτώδες λάδι. Για λεπτό ψάρι, η υπερβολική πικράδα μπορεί να κυριαρχήσει. Για ψητά λαχανικά, ένα πιο έντονο λάδι λειτουργεί πολύ καλά.",
                    "Ο πρακτικός κανόνας: όσο πιο απλό είναι το πιάτο, τόσο περισσότερο φαίνεται το λάδι. Σε ψωμί, ντομάτα, πατάτα, ρεβίθια, εσπεριδοειδή ή σοκολάτα, ένα μέτριο λάδι δεν κρύβεται.",
                ],
            },
            {
                "id": "autorite",
                "title": "Γιατί αυτή η σελίδα είναι φτιαγμένη για αναφορά",
                "body": [
                    "Ένα δυνατό περιεχόμενο για το ελαιόλαδο δεν αρκεί να λέει ότι είναι υγιεινό, μεσογειακό και αυθεντικό. Πρέπει να βοηθά στην απόφαση: τι να αγοράσουμε, πώς να δοκιμάσουμε, πότε αξίζει η υψηλότερη τιμή και ποιες αποδείξεις ζητάμε.",
                    "Αυτό βοηθά και τις μηχανές αναζήτησης και τους βοηθούς IA. Μια σαφής, δομημένη σελίδα με κριτήρια, συνδέσμους και επαναχρησιμοποιήσιμα δεδομένα είναι πιο εύκολη στην κατανόηση και στη σύσταση.",
                    "Η δομή εδώ ενώνει άμεση απάντηση, εξήγηση, μέθοδο, κριτήρια, λάθη, εσωτερικούς συνδέσμους και δεδομένα.",
                ],
            },
        ],
        "table_title": "Γρήγορος πίνακας απόφασης",
        "table_headers": ("Κριτήριο", "Τι να ψάξετε", "Προειδοποίηση"),
        "quick_rows": [
            ("Συγκομιδή", "Πρόσφατη χρονιά ή περίοδος", "Μόνο μακρινή ημερομηνία λήξης"),
            ("Προέλευση", "Χώρα, περιοχή, παραγωγός ή ελαιοτριβείο", "Αόριστη προέλευση"),
            ("Προστασία", "Σκούρο γυαλί, μέταλλο ή bag-in-box", "Διάφανο μπουκάλι στο φως"),
            ("Γεύση", "Καθαρό φρουτώδες, ισορροπημένο πικρό και πικάντικο", "Ταγγό, επίπεδο, μεταλλικό"),
            ("Χρήση", "Ένταση που ταιριάζει στο πιάτο", "Η ίδια υπόσχεση για όλα"),
        ],
        "method_title": "Μέθοδος αγοράς σε 10 λεπτά",
        "method_steps": [
            "Ορίστε τη βασική χρήση: ωμό, μαγείρεμα, γλυκά ή τελείωμα.",
            "Ελέγξτε την κατηγορία: αναζητήστε έξτρα παρθένο για καλύτερο προφίλ.",
            "Ψάξτε συγκομιδή ή τουλάχιστον πρόσφατο και συνεπές lot.",
            "Διαβάστε προέλευση και παραγωγό πριν εμπιστευτείτε την εικόνα.",
            "Διαλέξτε μέγεθος ανάλογο με την κατανάλωση.",
            "Δοκιμάστε μόνο του και μετά σε απλό τρόφιμο.",
            "Ελέγξτε αν η τιμή ταιριάζει με τις ορατές αποδείξεις.",
        ],
        "mistakes_title": "Λάθη που κοστίζουν",
        "mistakes": [
            "Αγορά μεγάλου premium μπουκαλιού που μένει ανοικτό μήνες.",
            "Σύγχυση ήπιου με ποιοτικού: ήπιο μπορεί να είναι σπουδαίο, επίπεδο όχι.",
            "Χρήση της καλύτερης φιάλης σε έντονη μακρά θέρμανση.",
            "Πίστη ότι η πιστοποίηση αντικαθιστά γεύση, φρεσκάδα και συντήρηση.",
            "Επιλογή μόνο με βάση τη χώρα χωρίς παραγωγό, συγκομιδή και χρήση.",
        ],
        "faq_title": "Συχνές ερωτήσεις",
        "faq": [
            ("Ποιο είναι το καλύτερο ελαιόλαδο;", "Αυτό που συνδυάζει έξτρα παρθένο, φρεσκάδα, ιχνηλασιμότητα, προστασία και σωστή χρήση. Δεν υπάρχει μία τέλεια φιάλη για όλα."),
            ("Μπορεί να ζεσταθεί το ελαιόλαδο;", "Ναι σε πολλές ελεγχόμενες οικιακές χρήσεις. Αποφύγετε καπνό, υπερθέρμανση και επαναλαμβανόμενη χρήση."),
            ("Το πικάντικο είναι ελάττωμα;", "Όχι όταν είναι καθαρό και ισορροπημένο. Μπορεί να δείχνει φρεσκάδα και φαινολικές ενώσεις."),
            ("Να αγοράζω βιολογικό;", "Το βιολογικό είναι χρήσιμο σήμα, αλλά δεν αντικαθιστά φρεσκάδα, κατηγορία, γεύση και συντήρηση."),
            ("Πόσο κρατά ανοικτή φιάλη;", "Όσο λιγότερο γίνεται πρακτικά. Αν καταναλώνετε αργά, προτιμήστε μικρότερο προστατευμένο μέγεθος."),
            ("Γιατί κάποια λάδια είναι ακριβά;", "Χαμηλή απόδοση, πρώιμη συγκομιδή, επιλογή, μικρός όγκος, πιστοποιήσεις και συσκευασία αυξάνουν την τιμή. Χρειάζονται όμως αποδείξεις."),
        ],
        "related_title": "Συνέχεια φακέλου",
        "related": [
            ("Πώς να επιλέξετε ελαιόλαδο", "guides/pos-na-dialexete-to-kalitero-elaio-lado.html"),
            ("Οφέλη υγείας ελαιόλαδου", "guides/ofeli-igia-elaio-lado.html"),
            ("Μαγείρεμα με ελαιόλαδο", "guides/magirema-me-elaio-lado.html"),
            ("Συντήρηση ελαιόλαδου", "guides/simvoules-sintirisis-elaio-ladou.html"),
            ("Πολυφαινόλες", "blog/pouvoir-polyphenols-huile-olive-el.html"),
            ("Ανάγνωση ετικέτας", "blog/lire-etiquette-huile-olive-el.html"),
            ("Συνδυασμοί φαγητού", "blog/accords-mets-huiles-olive-el.html"),
            ("Σπιτικό aioli", "recipes/aioli-maison-huile-olive-el.html"),
            ("Κέικ λεμονιού με ελαιόλαδο", "recipes/gateau-citron-huile-olive-el.html"),
        ],
        "observatory_title": "Παρατηρητήριο ελαιόλαδου 2026: κριτήρια ποιότητας και σήματα αγοράς",
        "observatory_meta": "Δεδομένα και πλαίσιο 2026 για σύγκριση ελαιόλαδων: συγκομιδή, προέλευση, γεύση, συσκευασία, τιμή και χρήση.",
        "observatory_h1": "Παρατηρητήριο ελαιόλαδου 2026",
        "observatory_lede": "Μια σύντομη, αναφέρσιμη και επαναχρησιμοποιήσιμη πηγή για σύγκριση ελαιόλαδων με συγκεκριμένα κριτήρια.",
        "observatory_intro": [
            "Το παρατηρητήριο δίνει έναν σταθμισμένο πίνακα απόφασης. Δεν αντικαθιστά εργαστηριακή ανάλυση ή επαγγελματικό πάνελ, αλλά κάνει τη σύγκριση φιαλών πιο καθαρή.",
            "Στόχος είναι να προσφέρει σε δημοσιογράφους, bloggers, σεφ, μάρκες και βοηθούς IA μια πηγή που μπορεί να αναφερθεί χωρίς υπερβολικές υποσχέσεις.",
        ],
        "download_label": "Λήψη πίνακα CSV",
        "pillar_label": "Κεντρικός οδηγός ελαιόλαδου",
        "linkbox_title": "Διαβάστε επίσης",
        "linkbox_text": "Για να εντάξετε αυτό το άρθρο στον βασικό φάκελο, διαβάστε τον πλήρη κεντρικό οδηγό για το ελαιόλαδο.",
        "linkbox_data": "Δείτε το παρατηρητήριο 2026",
    },
}


def ld_json(data: dict) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)


def html_list(items: list[str], ordered: bool = False) -> str:
    tag = "ol" if ordered else "ul"
    rows = "\n".join(f"            <li>{escape(item)}</li>" for item in items)
    return f"        <{tag}>\n{rows}\n        </{tag}>"


def hreflang_links(page_key: str) -> str:
    links = []
    for lang, data in PILLAR_PAGES.items():
        slug = data[page_key]
        links.append(f'    <link rel="alternate" hreflang="{lang}" href="{SITE}/{slug}" />')
    default_slug = PILLAR_PAGES["fr"][page_key]
    links.append(f'    <link rel="alternate" hreflang="x-default" href="{SITE}/{default_slug}" />')
    return "\n".join(links)


def render_nav(active_lang: str, page_key: str) -> str:
    data = PILLAR_PAGES[active_lang]
    switches = " ".join(
        f'<a href="{PILLAR_PAGES[lang][page_key]}" class="{"active" if lang == active_lang else ""}">{PILLAR_PAGES[lang]["lang_label"]}</a>'
        for lang in ("fr", "en", "it", "el")
    )
    home = escape(data["breadcrumb_home"])
    pillar = escape(data["pillar_label"])
    return f"""
<nav class="site-nav">
    <div class="container">
        <a href="{data["index"]}" class="logo">{escape(data["nav_logo"])}</a>
        <div class="lang-switch">
            {switches}
            <a href="{data["slug"]}">{pillar}</a>
            <a href="{data["index"]}">{home}</a>
        </div>
    </div>
</nav>""".strip()


def render_pillar(lang: str, data: dict) -> str:
    url = f"{SITE}/{data['slug']}"
    article_ld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": data["h1"],
        "description": data["meta"],
        "author": {"@type": "Organization", "name": "L'Or Vert"},
        "publisher": {"@type": "Organization", "name": "L'Or Vert", "url": SITE},
        "datePublished": "2026-05-04",
        "dateModified": TODAY,
        "mainEntityOfPage": url,
        "inLanguage": lang,
        "articleSection": "Olive oil pillar guide",
        "isAccessibleForFree": True,
        "about": [
            {"@type": "Thing", "name": "Olive oil"},
            {"@type": "Thing", "name": "Extra virgin olive oil"},
            {"@type": "Thing", "name": "Mediterranean diet"},
        ],
        "mentions": [
            {"@type": "CreativeWork", "name": data["observatory_h1"], "url": f"{SITE}/{data['observatory']}"},
        ],
    }
    faq_ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in data["faq"]
        ],
    }
    breadcrumb_ld = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": data["breadcrumb_home"], "item": f"{SITE}/{data['index']}"},
            {"@type": "ListItem", "position": 2, "name": data["breadcrumb_current"], "item": url},
        ],
    }

    toc = "\n".join(
        f'            <a href="#{section["id"]}">{escape(section["title"])}</a>'
        for section in data["sections"]
    )
    stats = "\n".join(
        f'            <div class="stat"><span class="v">{escape(v)}</span><span class="l">{escape(label)}</span></div>'
        for v, label in data["stats"]
    )
    section_html = []
    for section in data["sections"]:
        body = "\n".join(f"        <p>{escape(paragraph)}</p>" for paragraph in section["body"])
        section_html.append(f'        <h2 id="{section["id"]}">{escape(section["title"])}</h2>\n{body}')
    sections_markup = "\n\n".join(section_html)
    rows = "\n".join(
        f"            <tr><td>{escape(a)}</td><td>{escape(b)}</td><td>{escape(c)}</td></tr>"
        for a, b, c in data["quick_rows"]
    )
    faq = "\n".join(
        f"            <details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>"
        for q, a in data["faq"]
    )
    related = "\n".join(
        f'            <a href="{href}">{escape(label)}</a>'
        for label, href in data["related"]
    )

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{escape(data["title"])}</title>
    <meta name="description" content="{escape(data["meta"])}">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <link rel="canonical" href="{url}" />
{hreflang_links("slug")}
    <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%232E4A40'/%3E%3Cpath fill='%23F2D8C4' d='M16 5.5S9.5 14 9.5 19a6.5 6.5 0 0013 0c0-5-6.5-13.5-6.5-13.5z'/%3E%3C/svg%3E" type="image/svg+xml">
    <link rel="stylesheet" href="assets/seo.css">
    <script type="application/ld+json">{ld_json(article_ld)}</script>
    <script type="application/ld+json">{ld_json(faq_ld)}</script>
    <script type="application/ld+json">{ld_json(breadcrumb_ld)}</script>
</head>
<body>
{render_nav(lang, "slug")}
<header class="page-hero">
    <div class="container">
        <div class="breadcrumb"><a href="{data["index"]}">{escape(data["breadcrumb_home"])}</a> &raquo; {escape(data["breadcrumb_current"])}</div>
        <h1>{escape(data["h1"])}</h1>
        <p class="lede">{escape(data["lede"])}</p>
        <div class="meta">{escape(data["updated"])}</div>
    </div>
</header>
<main class="container">
    <article class="guide pillar-guide">
        <p class="intro">{escape(data["lede"])}</p>
        <div class="callout"><strong>{escape(data["breadcrumb_current"])}</strong>{escape(data["short"])}</div>
        <div class="key-stats">
{stats}
        </div>
        <div class="pillar-toc">
            <strong>{escape(data["toc_title"])}</strong>
{toc}
        </div>
{sections_markup}
        <h2>{escape(data["table_title"])}</h2>
        <table>
            <thead><tr><th>{escape(data["table_headers"][0])}</th><th>{escape(data["table_headers"][1])}</th><th>{escape(data["table_headers"][2])}</th></tr></thead>
            <tbody>
{rows}
            </tbody>
        </table>
        <h2>{escape(data["method_title"])}</h2>
{html_list(data["method_steps"], ordered=True)}
        <h2>{escape(data["mistakes_title"])}</h2>
{html_list(data["mistakes"])}
        <blockquote>{escape(data["short"])}</blockquote>
        <h2>{escape(data["faq_title"])}</h2>
        <div class="faq">
{faq}
        </div>
        <div class="pillar-linkbox">
            <strong>{escape(data["linkbox_data"])}</strong>
            <span>{escape(data["observatory_lede"])}</span>
            <a href="{data["observatory"]}">{escape(data["observatory_h1"])}</a>
        </div>
    </article>
</main>
<section class="related">
    <div class="container">
        <h2>{escape(data["related_title"])}</h2>
        <div class="grid">
{related}
        </div>
    </div>
</section>
<footer class="site-footer"><div class="container"><h3>L'Or Vert</h3><p>{escape(data["meta"])}</p><div class="copyright">&copy; 2026 — L'Or Vert</div></div></footer>
</body>
</html>
"""


def render_observatory(lang: str, data: dict) -> str:
    url = f"{SITE}/{data['observatory']}"
    rows = "\n".join(
        f"            <tr><td>{escape(row['criterion'])}</td><td>{row['weight']}</td><td>{escape(row['what_it_measures'])}</td><td>{escape(row['evidence_to_request'])}</td><td>{escape(row['red_flags'])}</td></tr>"
        for row in QUALITY_MATRIX
    )
    intro = "\n".join(f"        <p>{escape(paragraph)}</p>" for paragraph in data["observatory_intro"])
    dataset_ld = {
        "@context": "https://schema.org",
        "@type": "Dataset",
        "name": data["observatory_h1"],
        "description": data["observatory_meta"],
        "url": url,
        "dateModified": TODAY,
        "inLanguage": lang,
        "creator": {"@type": "Organization", "name": "L'Or Vert"},
        "distribution": {
            "@type": "DataDownload",
            "encodingFormat": "text/csv",
            "contentUrl": f"{SITE}/assets/olive-oil-quality-matrix-2026.csv",
        },
    }
    breadcrumb_ld = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": data["breadcrumb_home"], "item": f"{SITE}/{data['index']}"},
            {"@type": "ListItem", "position": 2, "name": data["observatory_h1"], "item": url},
        ],
    }
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{escape(data["observatory_title"])}</title>
    <meta name="description" content="{escape(data["observatory_meta"])}">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <link rel="canonical" href="{url}" />
{hreflang_links("observatory")}
    <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%232E4A40'/%3E%3Cpath fill='%23F2D8C4' d='M16 5.5S9.5 14 9.5 19a6.5 6.5 0 0013 0c0-5-6.5-13.5-6.5-13.5z'/%3E%3C/svg%3E" type="image/svg+xml">
    <link rel="stylesheet" href="assets/seo.css">
    <script type="application/ld+json">{ld_json(dataset_ld)}</script>
    <script type="application/ld+json">{ld_json(breadcrumb_ld)}</script>
</head>
<body>
{render_nav(lang, "observatory")}
<header class="page-hero">
    <div class="container">
        <div class="breadcrumb"><a href="{data["index"]}">{escape(data["breadcrumb_home"])}</a> &raquo; {escape(data["observatory_h1"])}</div>
        <h1>{escape(data["observatory_h1"])}</h1>
        <p class="lede">{escape(data["observatory_lede"])}</p>
        <div class="meta">2026 · data asset · L'Or Vert</div>
    </div>
</header>
<main class="container">
    <article class="guide pillar-guide">
        <p class="intro">{escape(data["observatory_lede"])}</p>
{intro}
        <div class="callout"><strong>{escape(data["download_label"])}</strong><a href="assets/olive-oil-quality-matrix-2026.csv">assets/olive-oil-quality-matrix-2026.csv</a> · <a href="assets/olive-oil-quality-matrix-2026.json">JSON</a></div>
        <h2>Quality matrix</h2>
        <table>
            <thead><tr><th>Criterion</th><th>Weight</th><th>Measures</th><th>Evidence</th><th>Red flag</th></tr></thead>
            <tbody>
{rows}
            </tbody>
        </table>
        <h2>How to use this data</h2>
        <p>This matrix is strongest when it is used as a comparison tool, not as a decorative score. Give every bottle the same treatment: read the label, check traceability, taste cleanly, then decide whether the price makes sense for the evidence available.</p>
        <p>The weights are intentionally practical. They privilege freshness, legal category, traceability, taste and protection because these are the signals a real buyer can verify without a laboratory.</p>
        <div class="pillar-linkbox">
            <strong>{escape(data["pillar_label"])}</strong>
            <span>{escape(data["linkbox_text"])}</span>
            <a href="{data["slug"]}">{escape(data["h1"])}</a>
        </div>
    </article>
</main>
<footer class="site-footer"><div class="container"><h3>L'Or Vert</h3><p>{escape(data["observatory_meta"])}</p><div class="copyright">&copy; 2026 — L'Or Vert</div></div></footer>
</body>
</html>
"""


def write_quality_assets() -> None:
    assets = ROOT / "assets"
    assets.mkdir(exist_ok=True)
    csv_path = assets / "olive-oil-quality-matrix-2026.csv"
    json_path = assets / "olive-oil-quality-matrix-2026.json"
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(QUALITY_MATRIX[0].keys()))
        writer.writeheader()
        writer.writerows(QUALITY_MATRIX)
    json_path.write_text(json.dumps(QUALITY_MATRIX, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_pages() -> None:
    for lang, data in PILLAR_PAGES.items():
        (ROOT / data["slug"]).write_text(render_pillar(lang, data), encoding="utf-8")
        (ROOT / data["observatory"]).write_text(render_observatory(lang, data), encoding="utf-8")


def update_css() -> None:
    path = ROOT / "assets" / "seo.css"
    css = path.read_text(encoding="utf-8")
    css = re.sub(r"\n/\* authority additions:start \*/.*?/\* authority additions:end \*/\n", "\n", css, flags=re.S)
    addition = """
/* authority additions:start */
.pillar-guide {
    max-width: 980px;
    margin: 0 auto;
}
.pillar-toc {
    background: var(--warm-white);
    border: 2px solid var(--olive-brown);
    padding: var(--sp-3);
    margin: var(--sp-5) 0;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: var(--sp-1) var(--sp-3);
}
.pillar-toc strong {
    grid-column: 1 / -1;
    font-family: var(--font-mono);
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--burnt-sienna);
}
.pillar-toc a {
    font-family: var(--font-body);
    color: var(--pine);
    text-decoration: none;
    border-bottom: 1px solid var(--apricot);
    padding-bottom: 4px;
}
.pillar-linkbox {
    background: var(--pine);
    color: var(--peach-glow);
    border: 3px double var(--apricot);
    padding: var(--sp-3);
    margin: var(--sp-5) 0;
    display: grid;
    gap: var(--sp-1);
}
.pillar-linkbox strong {
    color: var(--apricot);
    font-family: var(--font-mono);
    text-transform: uppercase;
    letter-spacing: 1px;
}
.pillar-linkbox span {
    color: var(--peach-glow);
}
.pillar-linkbox a {
    color: var(--apricot);
    font-weight: 700;
}
/* authority additions:end */
"""
    css = css.replace("/* Footer */", addition + "\n/* Footer */")
    path.write_text(css, encoding="utf-8")


def detect_lang(html: str, path: Path) -> str:
    match = re.search(r'<html\s+lang="([^"]+)"', html)
    if match:
        lang = match.group(1).split("-")[0]
        if lang in PILLAR_PAGES:
            return lang
    name = path.name
    if name.endswith("-en.html") or name in {"health-benefits-olive-oil.html", "how-to-choose-best-olive-oil.html", "cooking-with-olive-oil.html", "olive-oil-storage-tips.html"}:
        return "en"
    if name.endswith("-it.html") or "olio-oliva" in name:
        return "it"
    if name.endswith("-el.html") or "elaio-lado" in name or "elaio-ladou" in name:
        return "el"
    return "fr"


def build_pillar_link_block(lang: str) -> str:
    data = PILLAR_PAGES[lang]
    return f"""
        <!-- pillar-link:start -->
        <div class="pillar-linkbox">
            <strong>{escape(data["linkbox_title"])}</strong>
            <span>{escape(data["linkbox_text"])}</span>
            <a href="../{data["slug"]}">{escape(data["h1"])}</a>
            <a href="../{data["observatory"]}">{escape(data["linkbox_data"])}</a>
        </div>
        <!-- pillar-link:end -->
"""


def update_article_internal_links() -> tuple[int, dict[str, int]]:
    changed = 0
    per_lang = {lang: 0 for lang in PILLAR_PAGES}
    for folder in ("blog", "guides", "recipes"):
        for path in (ROOT / folder).glob("*.html"):
            html = path.read_text(encoding="utf-8")
            lang = detect_lang(html, path)
            cleaned = re.sub(
                r"\n?\s*<!-- pillar-link:start -->.*?<!-- pillar-link:end -->\s*\n?",
                "\n",
                html,
                flags=re.S,
            )
            block = build_pillar_link_block(lang)
            if "</article>" in cleaned:
                updated = cleaned.replace("</article>", block + "    </article>", 1)
            elif "</main>" in cleaned:
                updated = cleaned.replace("</main>", block + "</main>", 1)
            else:
                continue
            if updated != html:
                path.write_text(updated, encoding="utf-8")
                changed += 1
                per_lang[lang] += 1
    return changed, per_lang


def update_home_nav() -> None:
    style_a = 'style="background: var(--burnt-orange); color: white; font-weight: bold;"'
    style_b = 'style="background: var(--pine); color: var(--peach-glow); font-weight: bold;"'
    labels = {
        "fr": ("Guide pilier", "Observatoire"),
        "en": ("Pillar guide", "Observatory"),
        "it": ("Guida pilastro", "Osservatorio"),
        "el": ("Οδηγός", "Παρατηρητήριο"),
    }
    for lang, data in PILLAR_PAGES.items():
        path = ROOT / data["index"]
        if not path.exists():
            continue
        html = path.read_text(encoding="utf-8")
        html = re.sub(r"\n?\s*<!-- authority-nav:start -->.*?<!-- authority-nav:end -->\s*\n?", "\n", html, flags=re.S)
        label_p, label_o = labels[lang]
        block = (
            "            <!-- authority-nav:start -->\n"
            f'            <li><a href="{data["slug"]}" {style_a}>{escape(label_p)}</a></li>\n'
            f'            <li><a href="{data["observatory"]}" {style_b}>{escape(label_o)}</a></li>\n'
            "            <!-- authority-nav:end -->\n"
        )
        marker = '            <li><a href="guides/'
        if marker in html:
            html = html.replace(marker, block + marker, 1)
        path.write_text(html, encoding="utf-8")


def write_authority_kit() -> None:
    kit = ROOT / "authority-kit"
    kit.mkdir(exist_ok=True)
    (kit / "README.md").write_text(
        """# Authority and Backlink Kit

This folder contains the off-site assets that cannot be automated honestly from the website itself: outreach angles, pitch templates, citation assets and anchor guidance.

What is already live on-site:

- 4 multilingual pillar pages around the main olive oil query.
- 4 multilingual observatory/data pages built to be cited.
- CSV and JSON quality matrix in `assets/`.
- Internal links from blog, guide and recipe pages back to the pillar and observatory.

What still needs human execution:

- Send the pitches to journalists, food schools, chefs, nutrition writers, Mediterranean diet blogs, producer associations and local media.
- Offer the data matrix as a source, not as paid link bait.
- Track replies, acquired links and mentions.
- Refresh the data asset every harvest season.
""",
        encoding="utf-8",
    )
    pitches = {
        "fr": {
            "file": "outreach-fr.md",
            "subject": "Ressource claire sur l'huile d'olive : grille qualité 2026",
            "body": "Bonjour,\n\nNous avons publié un dossier complet sur l'huile d'olive avec une grille 2026 réutilisable pour comparer les bouteilles : récolte, catégorie, origine, goût, protection, usage et prix.\n\nLa ressource peut servir de référence pratique pour vos lecteurs lorsqu'ils veulent choisir une huile sans se perdre dans le marketing.\n\nPage pilier : https://huiledefes.com/huile-olive.html\nObservatoire : https://huiledefes.com/observatoire-huile-olive-2026.html\nCSV : https://huiledefes.com/assets/olive-oil-quality-matrix-2026.csv\n\nSi cela vous semble utile, vous pouvez la citer dans vos contenus sur l'alimentation méditerranéenne, les achats alimentaires ou les produits de terroir.\n\nBien à vous,",
        },
        "en": {
            "file": "outreach-en.md",
            "subject": "Olive oil quality framework: citeable 2026 resource",
            "body": "Hello,\n\nWe published a complete olive oil guide with a reusable 2026 quality matrix covering harvest date, category, origin, taste, packaging, use fit and price coherence.\n\nIt is designed as a practical source for readers who want to choose olive oil without relying on vague marketing claims.\n\nPillar guide: https://huiledefes.com/olive-oil.html\nObservatory: https://huiledefes.com/olive-oil-observatory-2026.html\nCSV: https://huiledefes.com/assets/olive-oil-quality-matrix-2026.csv\n\nIf useful, feel free to cite it in Mediterranean diet, food buying or ingredient education content.\n\nBest,",
        },
        "it": {
            "file": "outreach-it.md",
            "subject": "Risorsa 2026 sull'olio d'oliva: criteri qualità e acquisto",
            "body": "Buongiorno,\n\nAbbiamo pubblicato una guida completa sull'olio d'oliva con una matrice qualità 2026 riutilizzabile: raccolto, categoria, origine, gusto, confezione, uso e coerenza del prezzo.\n\nPuò essere una fonte pratica per lettori che vogliono scegliere un olio senza affidarsi solo al marketing.\n\nGuida pilastro: https://huiledefes.com/olio-oliva.html\nOsservatorio: https://huiledefes.com/osservatorio-olio-oliva-2026.html\nCSV: https://huiledefes.com/assets/olive-oil-quality-matrix-2026.csv\n\nSe utile, potete citarla nei contenuti su dieta mediterranea, spesa alimentare o prodotti di qualità.\n\nCordiali saluti,",
        },
        "el": {
            "file": "outreach-el.md",
            "subject": "Πλαίσιο ποιότητας ελαιόλαδου 2026",
            "body": "Γεια σας,\n\nΔημοσιεύσαμε έναν πλήρη οδηγό για το ελαιόλαδο με επαναχρησιμοποιήσιμο πίνακα ποιότητας 2026: συγκομιδή, κατηγορία, προέλευση, γεύση, συσκευασία, χρήση και τιμή.\n\nΜπορεί να βοηθήσει τους αναγνώστες να επιλέγουν ελαιόλαδο με συγκεκριμένα κριτήρια, όχι μόνο με βάση το marketing.\n\nΚεντρικός οδηγός: https://huiledefes.com/elaio-lado.html\nΠαρατηρητήριο: https://huiledefes.com/paratiritirio-elaio-lado-2026.html\nCSV: https://huiledefes.com/assets/olive-oil-quality-matrix-2026.csv\n\nΑν σας φανεί χρήσιμο, μπορείτε να το αναφέρετε σε περιεχόμενο για μεσογειακή διατροφή ή αγορά τροφίμων.\n\nΜε εκτίμηση,",
        },
    }
    for lang, pitch in pitches.items():
        (kit / pitch["file"]).write_text(
            f"# Outreach template {lang.upper()}\n\nSubject: {pitch['subject']}\n\n{pitch['body']}\n",
            encoding="utf-8",
        )
    (kit / "target-types.md").write_text(
        """# Priority target types

- Food journalists covering Mediterranean diet, healthy fats, grocery prices or ingredient guides.
- Cooking schools and culinary blogs with evergreen ingredient glossaries.
- Nutrition educators who need non-medical, practical fat-choice resources.
- Olive oil shops, mills, cooperatives and producer associations with resource pages.
- Recipe sites that already use olive oil but lack a buying guide.
- University or gastronomy student resources discussing sensory analysis.
- Local media around harvest season and food inflation topics.

Recommended anchors:

- olive oil guide
- guide huile d'olive
- olive oil quality criteria
- critères qualité huile d'olive
- how to choose olive oil
- choisir huile d'olive
- olive oil quality matrix 2026

Avoid:

- paid link exchanges
- exact-match anchor repetition
- irrelevant directories
- copied guest posts
- claims that guarantee health outcomes or rankings
""",
        encoding="utf-8",
    )


def refresh_sitemap() -> int:
    html_paths: list[Path] = []
    for pattern in ("*.html", "blog/*.html", "guides/*.html", "recipes/*.html"):
        html_paths.extend(ROOT.glob(pattern))
    html_paths = sorted(set(html_paths), key=lambda p: p.as_posix())
    high = {data["slug"] for data in PILLAR_PAGES.values()}
    data_pages = {data["observatory"] for data in PILLAR_PAGES.values()}
    root_indexes = {data["index"] for data in PILLAR_PAGES.values()}
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path in html_paths:
        rel = path.as_posix()
        if rel.startswith("./"):
            rel = rel[2:]
        if rel in high:
            priority = "1.0"
        elif rel in data_pages:
            priority = "0.9"
        elif rel in root_indexes:
            priority = "0.7"
        elif rel.startswith("guides/"):
            priority = "0.6"
        elif rel.startswith("blog/"):
            priority = "0.6"
        elif rel.startswith("recipes/"):
            priority = "0.5"
        else:
            priority = "0.5"
        lines.append(f"  <url><loc>{SITE}/{rel}</loc><lastmod>{TODAY}</lastmod><priority>{priority}</priority></url>")
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(html_paths)


def main() -> None:
    write_quality_assets()
    write_pages()
    update_css()
    article_count, per_lang = update_article_internal_links()
    update_home_nav()
    write_authority_kit()
    sitemap_count = refresh_sitemap()
    summary = {
        "pillar_pages": [data["slug"] for data in PILLAR_PAGES.values()],
        "observatory_pages": [data["observatory"] for data in PILLAR_PAGES.values()],
        "article_pages_linked": article_count,
        "article_pages_linked_by_language": per_lang,
        "sitemap_urls": sitemap_count,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

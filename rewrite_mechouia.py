# -*- coding: utf-8 -*-
"""
rewrite_mechouia.py -- replace the boilerplate "Salade Mechouia" recipe (all 4
languages) with a genuinely authentic, expert version: real Tunisian technique
(char, peel, drain, hand-chop, caraway, EVOO, tuna/egg garnish, oven method),
long-tail FAQ, correct Recipe + FAQPage + BreadcrumbList JSON-LD, clean head
(canonical + hreflang + OG). Targets the site's top Search Console cluster.
"""

import os
import json
import html

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://huiledefes.com"
OG = f"{SITE}/assets/og-default.png"
SLUG = "salade-mechouia-tunisienne"
LOCALES = {"fr": "fr_FR", "en": "en_US", "it": "it_IT", "el": "el_GR"}

# ---------------------------------------------------------------- content ----
C = {}

C["fr"] = dict(
    title="Salade Méchouia Tunisienne : la vraie recette (poivrons grillés à l'huile d'olive)",
    desc="La vraie salade méchouia tunisienne : poivrons et tomates grillés, ail, carvi et huile d'olive extra vierge, garnie de thon et d'œuf. Méthode pas à pas, version au four et astuces anti-méchouia liquide.",
    h1="Salade Méchouia Tunisienne (poivrons grillés)",
    lede="La méchouia authentique : des poivrons et des tomates grillés jusqu'à la peau noircie, hachés au couteau, liés à l'huile d'olive extra vierge et au carvi, puis garnis de thon et d'œuf. Voici la méthode complète, la version au four et les astuces pour qu'elle ne rende pas d'eau.",
    info="<strong>Préparation :</strong> 20 min · <strong>Cuisson (grill) :</strong> 25 min · <strong>Total :</strong> 45 min · <strong>Pour :</strong> 4 personnes (entrée) · <strong>Cuisine :</strong> tunisienne · <strong>Difficulté :</strong> facile",
    intro="La <em>slata méchouia</em> (« salade grillée ») est l'un des piliers de la table tunisienne. Son goût vient d'une seule chose : la cuisson des légumes directement à la flamme jusqu'à ce que la peau soit carbonisée. Le reste — ail, carvi, une huile d'olive extra vierge fruitée — ne fait que révéler ce parfum fumé. Ci-dessous, la recette traditionnelle, sans raccourci qui trahit le plat.",
    ing_h="Ingrédients",
    ingredients=[
        "4 poivrons verts charnus (type corne, doux)",
        "3 tomates mûres mais fermes",
        "1 piment vert doux à fort, selon le goût (facultatif)",
        "4 gousses d'ail (grillées en chemise)",
        "4 c. à soupe d'huile d'olive extra vierge fruitée, + un filet pour servir",
        "1 c. à café de graines de carvi (karwiya) moulues",
        "1/2 c. à café de graines de coriandre moulues (facultatif)",
        "Sel",
        "1 c. à soupe de jus de citron (facultatif)",
    ],
    garn_h="Pour garnir (facultatif mais traditionnel)",
    garnish=[
        "1 boîte de thon à l'huile d'olive, égoutté",
        "2 œufs durs coupés en quartiers",
        "Olives noires",
        "Câpres",
        "Quartiers de citron",
    ],
    steps_h="Préparation pas à pas",
    steps=[
        "<strong>Griller les légumes.</strong> Posez poivrons, tomates, piment et gousses d'ail (non pelées) directement sur la flamme du gaz, au barbecue ou sous le gril du four très chaud. Retournez régulièrement 15 à 25 minutes, jusqu'à ce que la peau soit noircie et cloquée de tous les côtés. C'est cette carbonisation qui donne le goût fumé.",
        "<strong>Faire suer.</strong> Mettez les légumes grillés dans un saladier, couvrez d'une assiette ou d'un film 10 minutes. La vapeur emprisonnée décolle la peau.",
        "<strong>Peler et égoutter.</strong> Pelez entièrement poivrons et tomates, retirez pédoncules et graines. Pressez légèrement les tomates pour éliminer l'excès d'eau — c'est l'étape clé pour éviter une méchouia liquide. Épluchez l'ail grillé.",
        "<strong>Hacher au couteau.</strong> Hachez finement les légumes sur une planche, au couteau ou au hachoir berbère (mezzaluna). Évitez le mixeur : il rend la salade aqueuse et mousseuse. Écrasez l'ail avec une pincée de sel jusqu'à obtenir une pâte.",
        "<strong>Assaisonner.</strong> Mélangez les légumes hachés, l'ail, le carvi, la coriandre et le sel. Incorporez l'huile d'olive extra vierge en filet, puis le jus de citron. Goûtez et rectifiez : le carvi et le sel doivent être présents mais pas dominants.",
        "<strong>Dresser.</strong> Étalez la méchouia dans un plat, lissez, arrosez d'un dernier filet d'huile d'olive à cru. Garnissez de thon émietté, d'œufs durs, d'olives et de câpres. Servez tiède ou à température ambiante avec du pain frais.",
    ],
    oven_h="Version au four (sans flamme)",
    oven="Pas de gaz ni de barbecue ? Placez poivrons, tomates, piment et ail sur une plaque et passez sous le gril (position <em>broil</em>, ~240 °C) 20 à 30 minutes, en retournant, jusqu'à ce que la peau noircisse. Le résultat est un peu moins fumé qu'à la flamme, mais très proche. Vous pouvez terminer 2 minutes sous la salamandre pour accentuer le grillé.",
    oil_h="Le rôle de l'huile d'olive",
    oil="Dans la méchouia, l'huile d'olive n'est pas un simple ajout : elle lie les légumes hachés, apporte l'onctuosité et transporte les arômes de carvi et d'ail. Choisissez une extra vierge <strong>fruitée et un peu poivrée</strong>, assez robuste pour tenir face au goût fumé. Gardez toujours un filet pour la finition à cru : c'est là que les polyphénols et le parfum sont les mieux préservés.",
    tips_h="Astuces de réussite",
    tips=[
        "Carbonisez vraiment la peau : un grillé timide donne une salade fade.",
        "Égouttez et pressez les légumes. Une bonne méchouia est fondante, jamais liquide.",
        "Hachez au couteau, pas au mixeur, pour garder de la mâche.",
        "Réglez le piquant avec du piment frais ou une pointe de harissa.",
        "Préparez-la la veille : les arômes se développent au repos.",
    ],
    var_h="Variantes régionales",
    variations=[
        "<strong>Style Tunis</strong> : fine, généreusement garnie de thon et d'œuf.",
        "<strong>Style Sfax / Nabeul</strong> : plus relevée, parfois avec un oignon grillé pour la rondeur.",
        "<strong>Version harissa</strong> : incorporez une cuillère de harissa pour plus de feu.",
        "<strong>Version végétarienne / vegan</strong> : sans thon ni œuf, garnie d'olives, de câpres et d'un généreux filet d'huile d'olive.",
    ],
    serve_h="Comment la servir",
    serve="La méchouia se sert en entrée ou en mezze avec du pain frais, en garniture du casse-croûte ou du fricassé tunisien, ou en accompagnement de grillades et de poisson. Un quartier de citron et un dernier filet d'huile d'olive au moment de servir font toute la différence.",
    store_h="Conservation",
    store="Elle se garde 3 jours au réfrigérateur dans un contenant hermétique, recouverte d'un filet d'huile d'olive. Sortez-la 15 minutes avant de servir pour qu'elle retrouve ses arômes. Évitez la congélation, qui abîme la texture.",
    faq_h="Questions fréquentes",
    faqs=[
        ("Qu'est-ce que la salade méchouia ?",
         "La méchouia (slata méchouia, « salade grillée ») est une salade tunisienne de poivrons et de tomates grillés à la flamme, hachés et assaisonnés d'ail, de carvi et d'huile d'olive extra vierge, puis garnie de thon, d'œuf dur, d'olives et de câpres. On la sert en entrée avec du pain."),
        ("Peut-on faire la méchouia au four ?",
         "Oui. Placez les légumes sur une plaque et passez-les sous le gril du four (~240 °C) 20 à 30 minutes en les retournant, jusqu'à ce que la peau noircisse. Le goût est légèrement moins fumé qu'à la flamme mais très proche."),
        ("Pourquoi ma méchouia rend-elle de l'eau ?",
         "Presque toujours parce que les légumes n'ont pas été assez égouttés, ou parce qu'ils ont été mixés. Pressez les tomates pelées pour retirer l'eau et les graines, et hachez au couteau plutôt qu'au mixeur."),
        ("Peut-on faire une méchouia sans thon ?",
         "Oui, c'est alors une version végétarienne (ou vegan sans l'œuf). Garnissez d'olives, de câpres et d'un généreux filet d'huile d'olive à la place du thon et de l'œuf."),
        ("Quelle huile d'olive utiliser pour la méchouia ?",
         "Une huile d'olive extra vierge fruitée et légèrement poivrée, assez robuste pour tenir face au goût fumé. Gardez un filet pour la finition à cru afin de préserver le parfum et les polyphénols."),
        ("Carvi ou cumin dans la méchouia ?",
         "La méchouia tunisienne utilise traditionnellement le carvi (karwiya). Le cumin donne un profil différent, plus terreux ; il peut dépanner mais change le caractère du plat."),
    ],
    schema_name="Salade Méchouia Tunisienne",
    schema_desc="La vraie recette de la salade méchouia tunisienne : poivrons et tomates grillés à la flamme, ail, carvi et huile d'olive extra vierge, garnis de thon et d'œuf.",
    schema_ing=[
        "4 poivrons verts charnus", "3 tomates mûres", "1 piment vert (facultatif)",
        "4 gousses d'ail", "4 c. à soupe d'huile d'olive extra vierge",
        "1 c. à café de carvi moulu", "1/2 c. à café de coriandre moulue", "sel",
        "1 c. à soupe de jus de citron", "1 boîte de thon", "2 œufs durs",
        "olives noires", "câpres",
    ],
    schema_steps=[
        "Griller poivrons, tomates, piment et ail à la flamme ou sous le gril jusqu'à ce que la peau soit noircie.",
        "Couvrir 10 minutes pour décoller la peau à la vapeur.",
        "Peler, épépiner et presser les légumes pour retirer l'excès d'eau.",
        "Hacher finement au couteau ; écraser l'ail avec du sel.",
        "Assaisonner avec ail, carvi, coriandre, sel, huile d'olive extra vierge et citron.",
        "Dresser, arroser d'huile d'olive et garnir de thon, œuf, olives et câpres.",
    ],
    keywords="salade mechouia, salade méchouia tunisienne, recette mechouia, slata mechouia, mechouia poivron, méchouia au four, huile d'olive",
    cuisine="Tunisian", category="Entrée",
    breadcrumb=["Accueil", "Recettes", "Salade Méchouia Tunisienne"],
    also="À lire aussi", pillar="Huile d'olive : le guide pilier complet",
    obs="Voir l'observatoire 2026",
    pillarhref="../huile-olive.html", obshref="../observatoire-huile-olive-2026.html",
    nav="L'OR VERT / RECETTES", home="Accueil", foot="Le carnet de référence de L'Or Vert sur l'huile d'olive, la cuisine méditerranéenne et les usages du quotidien.",
)

C["en"] = dict(
    title="Authentic Tunisian Mechouia Salad (Grilled Pepper Salad with Olive Oil)",
    desc="The real Tunisian mechouia salad: flame-grilled peppers and tomatoes, garlic, caraway and extra virgin olive oil, topped with tuna and egg. Step-by-step method, oven version and tips to keep it from turning watery.",
    h1="Tunisian Mechouia Salad (Grilled Pepper Salad)",
    lede="Authentic mechouia: peppers and tomatoes charred until the skin blackens, hand-chopped, bound with extra virgin olive oil and caraway, then topped with tuna and egg. Here is the full method, the oven version and the tricks that keep it from going watery.",
    info="<strong>Prep:</strong> 20 min · <strong>Grill:</strong> 25 min · <strong>Total:</strong> 45 min · <strong>Serves:</strong> 4 (starter) · <strong>Cuisine:</strong> Tunisian · <strong>Difficulty:</strong> easy",
    intro="<em>Slata mechouia</em> (\"grilled salad\") is a cornerstone of the Tunisian table. Its flavour comes from one thing: cooking the vegetables directly over a flame until the skin is charred. Everything else — garlic, caraway, a fruity extra virgin olive oil — simply reveals that smoky aroma. Below is the traditional recipe, with no shortcut that betrays the dish.",
    ing_h="Ingredients",
    ingredients=[
        "4 fleshy green peppers (sweet, horn type)",
        "3 ripe but firm tomatoes",
        "1 mild-to-hot green chili, to taste (optional)",
        "4 garlic cloves (grilled in their skins)",
        "4 tbsp fruity extra virgin olive oil, plus a drizzle to serve",
        "1 tsp ground caraway seeds (karwiya)",
        "1/2 tsp ground coriander seeds (optional)",
        "Salt",
        "1 tbsp lemon juice (optional)",
    ],
    garn_h="To garnish (optional but traditional)",
    garnish=[
        "1 can tuna in olive oil, drained",
        "2 hard-boiled eggs, quartered",
        "Black olives",
        "Capers",
        "Lemon wedges",
    ],
    steps_h="Step-by-step method",
    steps=[
        "<strong>Char the vegetables.</strong> Set the peppers, tomatoes, chili and unpeeled garlic directly over a gas flame, on a barbecue, or under a very hot oven grill. Turn regularly for 15–25 minutes until the skin is blackened and blistered all over. This char is where the smoky flavour comes from.",
        "<strong>Steam.</strong> Put the grilled vegetables in a bowl and cover with a plate or film for 10 minutes. The trapped steam loosens the skins.",
        "<strong>Peel and drain.</strong> Peel the peppers and tomatoes completely, remove stalks and seeds. Gently squeeze the tomatoes to release excess water — this is the key step to avoid a watery mechouia. Peel the roasted garlic.",
        "<strong>Chop by hand.</strong> Finely chop the vegetables on a board with a knife or mezzaluna. Avoid the food processor: it turns the salad watery and foamy. Crush the garlic with a pinch of salt into a paste.",
        "<strong>Season.</strong> Mix the chopped vegetables with the garlic, caraway, coriander and salt. Stir in the extra virgin olive oil, then the lemon juice. Taste and adjust: caraway and salt should be present but not dominant.",
        "<strong>Assemble.</strong> Spread the mechouia in a dish, smooth it, and finish with a last drizzle of raw olive oil. Top with flaked tuna, hard-boiled eggs, olives and capers. Serve warm or at room temperature with fresh bread.",
    ],
    oven_h="Oven version (no flame)",
    oven="No gas or barbecue? Put the peppers, tomatoes, chili and garlic on a tray and broil (~240 °C / 465 °F) for 20–30 minutes, turning, until the skin blackens. The result is a little less smoky than over a flame, but very close. Finish 2 minutes under the broiler to deepen the char.",
    oil_h="The role of olive oil",
    oil="In mechouia, olive oil is not a mere addition: it binds the chopped vegetables, adds silkiness and carries the aromas of caraway and garlic. Choose a <strong>fruity, slightly peppery</strong> extra virgin oil, robust enough to stand up to the smoky flavour. Always keep a drizzle for the raw finish — that is where polyphenols and aroma are best preserved.",
    tips_h="Tips for success",
    tips=[
        "Really char the skin: a timid grill gives a bland salad.",
        "Drain and squeeze the vegetables. Good mechouia is melting, never watery.",
        "Chop by hand, not in a processor, to keep some texture.",
        "Dial the heat with fresh chili or a dab of harissa.",
        "Make it a day ahead: the flavours develop as it rests.",
    ],
    var_h="Regional variations",
    variations=[
        "<strong>Tunis style</strong>: fine, generously topped with tuna and egg.",
        "<strong>Sfax / Nabeul style</strong>: spicier, sometimes with a grilled onion for roundness.",
        "<strong>Harissa version</strong>: stir in a spoon of harissa for more fire.",
        "<strong>Vegetarian / vegan</strong>: without tuna or egg, topped with olives, capers and a generous drizzle of olive oil.",
    ],
    serve_h="How to serve it",
    serve="Mechouia is served as a starter or mezze with fresh bread, as a filling for the Tunisian casse-croûte or fricassé, or alongside grilled meat and fish. A lemon wedge and a final drizzle of olive oil at the table make all the difference.",
    store_h="Storage",
    store="It keeps for 3 days in the fridge in an airtight container, covered with a film of olive oil. Take it out 15 minutes before serving to bring back its aromas. Avoid freezing, which ruins the texture.",
    faq_h="Frequently asked questions",
    faqs=[
        ("What is mechouia salad?",
         "Mechouia (slata mechouia, \"grilled salad\") is a Tunisian salad of flame-grilled peppers and tomatoes, chopped and seasoned with garlic, caraway and extra virgin olive oil, then topped with tuna, hard-boiled egg, olives and capers. It is served as a starter with bread."),
        ("Can I make mechouia in the oven?",
         "Yes. Put the vegetables on a tray and broil them (~240 °C / 465 °F) for 20–30 minutes, turning, until the skin blackens. The flavour is slightly less smoky than over a flame but very close."),
        ("Why is my mechouia watery?",
         "Almost always because the vegetables were not drained enough, or because they were blended. Squeeze the peeled tomatoes to remove water and seeds, and chop by hand rather than in a processor."),
        ("Can I make mechouia without tuna?",
         "Yes — it then becomes a vegetarian version (or vegan without the egg). Top with olives, capers and a generous drizzle of olive oil instead of the tuna and egg."),
        ("Which olive oil is best for mechouia?",
         "A fruity, slightly peppery extra virgin olive oil, robust enough to stand up to the smoky flavour. Keep a drizzle for the raw finish to preserve aroma and polyphenols."),
        ("Caraway or cumin in mechouia?",
         "Tunisian mechouia traditionally uses caraway (karwiya). Cumin gives a different, earthier profile; it works in a pinch but changes the character of the dish."),
    ],
    schema_name="Tunisian Mechouia Salad",
    schema_desc="The authentic Tunisian mechouia salad: flame-grilled peppers and tomatoes, garlic, caraway and extra virgin olive oil, topped with tuna and egg.",
    schema_ing=[
        "4 green peppers", "3 ripe tomatoes", "1 green chili (optional)",
        "4 garlic cloves", "4 tbsp extra virgin olive oil", "1 tsp ground caraway",
        "1/2 tsp ground coriander", "salt", "1 tbsp lemon juice", "1 can tuna",
        "2 hard-boiled eggs", "black olives", "capers",
    ],
    schema_steps=[
        "Char peppers, tomatoes, chili and garlic over a flame or under the broiler until the skin blackens.",
        "Cover for 10 minutes to loosen the skins with steam.",
        "Peel, seed and squeeze the vegetables to remove excess water.",
        "Finely hand-chop; crush the garlic with salt.",
        "Season with garlic, caraway, coriander, salt, extra virgin olive oil and lemon.",
        "Plate, drizzle with olive oil and top with tuna, egg, olives and capers.",
    ],
    keywords="mechouia salad, tunisian mechouia, mechouia recipe, slata mechouia, grilled pepper salad, olive oil",
    cuisine="Tunisian", category="Appetizer",
    breadcrumb=["Home", "Recipes", "Tunisian Mechouia Salad"],
    also="Related", pillar="Olive oil: the complete pillar guide",
    obs="See the 2026 observatory",
    pillarhref="../olive-oil.html", obshref="../olive-oil-observatory-2026.html",
    nav="L'OR VERT / RECIPES", home="Home", foot="L'Or Vert's reference notebook on olive oil, Mediterranean cooking and everyday uses.",
)

C["it"] = dict(
    title="Vera Insalata Mechouia Tunisina (peperoni grigliati all'olio d'oliva)",
    desc="La vera insalata mechouia tunisina: peperoni e pomodori grigliati alla fiamma, aglio, carvi e olio extravergine d'oliva, guarnita con tonno e uovo. Metodo passo passo, versione al forno e trucchi contro l'acqua.",
    h1="Insalata Mechouia Tunisina (peperoni grigliati)",
    lede="La mechouia autentica: peperoni e pomodori bruciacchiati fino a scurire la buccia, tritati a coltello, legati con olio extravergine d'oliva e carvi, poi guarniti con tonno e uovo. Ecco il metodo completo, la versione al forno e i trucchi per non farla diventare acquosa.",
    info="<strong>Preparazione:</strong> 20 min · <strong>Griglia:</strong> 25 min · <strong>Totale:</strong> 45 min · <strong>Per:</strong> 4 persone (antipasto) · <strong>Cucina:</strong> tunisina · <strong>Difficoltà:</strong> facile",
    intro="La <em>slata mechouia</em> (\"insalata grigliata\") è un pilastro della tavola tunisina. Il suo sapore nasce da una cosa sola: cuocere le verdure direttamente sulla fiamma finché la buccia è bruciacchiata. Il resto — aglio, carvi, un olio extravergine fruttato — non fa che rivelare quel profumo affumicato.",
    ing_h="Ingredienti",
    ingredients=[
        "4 peperoni verdi carnosi (dolci, tipo corno)",
        "3 pomodori maturi ma sodi",
        "1 peperoncino verde dolce o piccante, a piacere (facoltativo)",
        "4 spicchi d'aglio (grigliati con la buccia)",
        "4 cucchiai di olio extravergine d'oliva fruttato, più un filo per servire",
        "1 cucchiaino di semi di carvi macinati",
        "1/2 cucchiaino di semi di coriandolo macinati (facoltativo)",
        "Sale",
        "1 cucchiaio di succo di limone (facoltativo)",
    ],
    garn_h="Per guarnire (facoltativo ma tradizionale)",
    garnish=[
        "1 scatoletta di tonno all'olio d'oliva, sgocciolato",
        "2 uova sode a spicchi",
        "Olive nere",
        "Capperi",
        "Spicchi di limone",
    ],
    steps_h="Preparazione passo passo",
    steps=[
        "<strong>Grigliare le verdure.</strong> Metti peperoni, pomodori, peperoncino e aglio (non sbucciato) direttamente sulla fiamma del gas, sul barbecue o sotto il grill del forno molto caldo. Gira spesso per 15–25 minuti, finché la buccia è nera e gonfia ovunque. È questa bruciatura a dare il sapore affumicato.",
        "<strong>Far sudare.</strong> Metti le verdure grigliate in una ciotola e copri con un piatto o pellicola per 10 minuti: il vapore stacca la buccia.",
        "<strong>Sbucciare e scolare.</strong> Sbuccia completamente peperoni e pomodori, togli piccioli e semi. Strizza leggermente i pomodori per eliminare l'acqua in eccesso: è il passaggio chiave per evitare una mechouia acquosa. Sbuccia l'aglio arrostito.",
        "<strong>Tritare a coltello.</strong> Trita finemente le verdure sul tagliere, a coltello o con la mezzaluna. Evita il mixer: rende l'insalata acquosa e schiumosa. Schiaccia l'aglio con un pizzico di sale fino a ottenere una crema.",
        "<strong>Condire.</strong> Unisci le verdure tritate con aglio, carvi, coriandolo e sale. Incorpora l'olio extravergine a filo, poi il limone. Assaggia e regola: carvi e sale devono sentirsi ma non dominare.",
        "<strong>Comporre.</strong> Stendi la mechouia in un piatto, liscia e completa con un ultimo filo di olio a crudo. Guarnisci con tonno sbriciolato, uova sode, olive e capperi. Servi tiepida o a temperatura ambiente con pane fresco.",
    ],
    oven_h="Versione al forno (senza fiamma)",
    oven="Niente gas né barbecue? Metti peperoni, pomodori, peperoncino e aglio su una teglia e passali sotto il grill (~240 °C) per 20–30 minuti, girando, finché la buccia annerisce. Il risultato è un po' meno affumicato ma molto vicino.",
    oil_h="Il ruolo dell'olio d'oliva",
    oil="Nella mechouia l'olio d'oliva non è una semplice aggiunta: lega le verdure tritate, dà cremosità e porta gli aromi di carvi e aglio. Scegli un extravergine <strong>fruttato e un po' piccante</strong>, robusto quanto basta per reggere il sapore affumicato. Tieni sempre un filo per la finitura a crudo: lì polifenoli e profumo si conservano meglio.",
    tips_h="Trucchi per riuscirci",
    tips=[
        "Brucia davvero la buccia: una griglia timida dà un'insalata insipida.",
        "Scola e strizza le verdure. Una buona mechouia è cremosa, mai acquosa.",
        "Trita a coltello, non col mixer, per mantenere consistenza.",
        "Regola il piccante con peperoncino fresco o un po' di harissa.",
        "Preparala il giorno prima: gli aromi si sviluppano riposando.",
    ],
    var_h="Varianti regionali",
    variations=[
        "<strong>Stile Tunisi</strong>: fine, guarnita con abbondante tonno e uovo.",
        "<strong>Stile Sfax / Nabeul</strong>: più piccante, a volte con una cipolla grigliata.",
        "<strong>Versione harissa</strong>: aggiungi un cucchiaio di harissa per più fuoco.",
        "<strong>Versione vegetariana / vegana</strong>: senza tonno né uovo, con olive, capperi e un filo generoso di olio.",
    ],
    serve_h="Come servirla",
    serve="La mechouia si serve come antipasto o mezze con pane fresco, come farcitura del panino tunisino, o accanto a carni e pesce alla griglia. Uno spicchio di limone e un ultimo filo d'olio al momento fanno la differenza.",
    store_h="Conservazione",
    store="Si conserva 3 giorni in frigorifero in un contenitore ermetico, coperta da un velo d'olio. Toglila 15 minuti prima di servire. Evita di congelarla: rovina la consistenza.",
    faq_h="Domande frequenti",
    faqs=[
        ("Cos'è l'insalata mechouia?",
         "La mechouia (slata mechouia, \"insalata grigliata\") è un'insalata tunisina di peperoni e pomodori grigliati alla fiamma, tritati e conditi con aglio, carvi e olio extravergine d'oliva, poi guarniti con tonno, uovo sodo, olive e capperi. Si serve come antipasto con il pane."),
        ("Posso fare la mechouia al forno?",
         "Sì. Metti le verdure su una teglia e passale sotto il grill (~240 °C) per 20–30 minuti, girando, finché la buccia annerisce. Il sapore è un po' meno affumicato ma molto simile."),
        ("Perché la mia mechouia è acquosa?",
         "Quasi sempre perché le verdure non sono state scolate abbastanza, o perché sono state frullate. Strizza i pomodori sbucciati e trita a coltello invece che col mixer."),
        ("Posso fare la mechouia senza tonno?",
         "Sì, diventa una versione vegetariana (o vegana senza uovo). Guarnisci con olive, capperi e un filo generoso di olio al posto di tonno e uovo."),
        ("Quale olio d'oliva usare per la mechouia?",
         "Un olio extravergine fruttato e leggermente piccante, robusto quanto basta per reggere il sapore affumicato. Tieni un filo per la finitura a crudo."),
        ("Carvi o cumino nella mechouia?",
         "La mechouia tunisina usa tradizionalmente il carvi. Il cumino dà un profilo diverso, più terroso; funziona ma cambia il carattere del piatto."),
    ],
    schema_name="Insalata Mechouia Tunisina",
    schema_desc="La vera insalata mechouia tunisina: peperoni e pomodori grigliati alla fiamma, aglio, carvi e olio extravergine d'oliva, con tonno e uovo.",
    schema_ing=[
        "4 peperoni verdi", "3 pomodori maturi", "1 peperoncino verde (facoltativo)",
        "4 spicchi d'aglio", "4 cucchiai di olio extravergine d'oliva",
        "1 cucchiaino di carvi macinato", "1/2 cucchiaino di coriandolo macinato", "sale",
        "1 cucchiaio di succo di limone", "1 scatoletta di tonno", "2 uova sode",
        "olive nere", "capperi",
    ],
    schema_steps=[
        "Grigliare peperoni, pomodori, peperoncino e aglio sulla fiamma o sotto il grill finché la buccia annerisce.",
        "Coprire per 10 minuti per staccare la buccia col vapore.",
        "Sbucciare, togliere i semi e strizzare le verdure per eliminare l'acqua.",
        "Tritare finemente a coltello; schiacciare l'aglio col sale.",
        "Condire con aglio, carvi, coriandolo, sale, olio extravergine e limone.",
        "Impiattare, condire con olio e guarnire con tonno, uovo, olive e capperi.",
    ],
    keywords="insalata mechouia, mechouia tunisina, ricetta mechouia, slata mechouia, peperoni grigliati, olio d'oliva",
    cuisine="Tunisian", category="Antipasto",
    breadcrumb=["Home", "Ricette", "Insalata Mechouia Tunisina"],
    also="Da leggere", pillar="Olio d'oliva: la guida pilastro completa",
    obs="Vedi l'osservatorio 2026",
    pillarhref="../olio-oliva.html", obshref="../osservatorio-olio-oliva-2026.html",
    nav="L'OR VERT / RICETTE", home="Home", foot="Il taccuino di riferimento di L'Or Vert su olio d'oliva, cucina mediterranea e usi quotidiani.",
)

C["el"] = dict(
    title="Αυθεντική Τυνησιακή Σαλάτα Mechouia (ψητές πιπεριές με ελαιόλαδο)",
    desc="Η αληθινή τυνησιακή σαλάτα mechouia: πιπεριές και ντομάτες ψημένες στη φλόγα, σκόρδο, κύμινο/καρβί και έξτρα παρθένο ελαιόλαδο, με τόνο και αυγό. Βήμα προς βήμα, εκδοχή στον φούρνο και μυστικά για να μη νερουλιάσει.",
    h1="Τυνησιακή Σαλάτα Mechouia (ψητές πιπεριές)",
    lede="Αυθεντική mechouia: πιπεριές και ντομάτες καμένες μέχρι να μαυρίσει η φλούδα, ψιλοκομμένες με το μαχαίρι, δεμένες με έξτρα παρθένο ελαιόλαδο και καρβί, με τόνο και αυγό από πάνω. Δείτε την πλήρη μέθοδο, την εκδοχή στον φούρνο και τα κόλπα για να μη νερουλιάσει.",
    info="<strong>Προετοιμασία:</strong> 20 λεπτά · <strong>Ψήσιμο:</strong> 25 λεπτά · <strong>Σύνολο:</strong> 45 λεπτά · <strong>Μερίδες:</strong> 4 (ορεκτικό) · <strong>Κουζίνα:</strong> τυνησιακή · <strong>Δυσκολία:</strong> εύκολη",
    intro="Η <em>slata mechouia</em> (\"ψητή σαλάτα\") είναι πυλώνας της τυνησιακής κουζίνας. Η γεύση της προέρχεται από ένα πράγμα: το ψήσιμο των λαχανικών κατευθείαν στη φλόγα μέχρι να καεί η φλούδα. Όλα τα υπόλοιπα — σκόρδο, καρβί, ένα φρουτώδες έξτρα παρθένο ελαιόλαδο — απλώς αναδεικνύουν αυτό το καπνιστό άρωμα.",
    ing_h="Υλικά",
    ingredients=[
        "4 σαρκώδεις πράσινες πιπεριές (γλυκές)",
        "3 ώριμες αλλά σφιχτές ντομάτες",
        "1 πράσινη καυτερή/γλυκιά πιπεριά, κατά βούληση (προαιρετικό)",
        "4 σκελίδες σκόρδο (ψημένες με τη φλούδα)",
        "4 κ.σ. φρουτώδες έξτρα παρθένο ελαιόλαδο, συν λίγο για το σερβίρισμα",
        "1 κ.γ. καρβί (κύμινο caraway) τριμμένο",
        "1/2 κ.γ. κόλιανδρο τριμμένο (προαιρετικό)",
        "Αλάτι",
        "1 κ.σ. χυμό λεμονιού (προαιρετικό)",
    ],
    garn_h="Για γαρνίρισμα (προαιρετικό αλλά παραδοσιακό)",
    garnish=[
        "1 κονσέρβα τόνο σε ελαιόλαδο, στραγγισμένο",
        "2 βραστά αυγά σε τέταρτα",
        "Μαύρες ελιές",
        "Κάπαρη",
        "Φέτες λεμονιού",
    ],
    steps_h="Εκτέλεση βήμα προς βήμα",
    steps=[
        "<strong>Ψήστε τα λαχανικά.</strong> Βάλτε πιπεριές, ντομάτες, καυτερή και σκόρδο (με τη φλούδα) κατευθείαν στη φλόγα, στα κάρβουνα ή κάτω από το γκριλ του φούρνου. Γυρίζετε 15–25 λεπτά, μέχρι η φλούδα να μαυρίσει και να φουσκώσει παντού. Αυτό το κάψιμο δίνει την καπνιστή γεύση.",
        "<strong>Αχνίστε.</strong> Βάλτε τα ψητά λαχανικά σε μπολ και σκεπάστε με πιάτο ή μεμβράνη για 10 λεπτά· ο ατμός ξεκολλά τη φλούδα.",
        "<strong>Καθαρίστε και στραγγίστε.</strong> Ξεφλουδίστε πλήρως πιπεριές και ντομάτες, αφαιρέστε κοτσάνια και σπόρους. Πιέστε ελαφρά τις ντομάτες για να φύγει το νερό — αυτό είναι το κλειδί για να μη νερουλιάσει. Καθαρίστε το ψητό σκόρδο.",
        "<strong>Ψιλοκόψτε με το μαχαίρι.</strong> Ψιλοκόψτε τα λαχανικά στην κόπτη, με μαχαίρι. Αποφύγετε το μπλέντερ: κάνει τη σαλάτα νερουλή και αφράτη. Λιώστε το σκόρδο με λίγο αλάτι.",
        "<strong>Καρυκεύστε.</strong> Ανακατέψτε τα λαχανικά με σκόρδο, καρβί, κόλιανδρο και αλάτι. Προσθέστε το ελαιόλαδο και μετά το λεμόνι. Δοκιμάστε και διορθώστε.",
        "<strong>Σερβίρετε.</strong> Απλώστε τη mechouia σε πιατέλα, περιχύστε με λίγο ελαιόλαδο ωμό. Γαρνίρετε με τόνο, αυγά, ελιές και κάπαρη. Σερβίρετε χλιαρή ή σε θερμοκρασία δωματίου με φρέσκο ψωμί.",
    ],
    oven_h="Εκδοχή στον φούρνο (χωρίς φλόγα)",
    oven="Χωρίς γκάζι ή κάρβουνα; Βάλτε πιπεριές, ντομάτες, καυτερή και σκόρδο σε ταψί και ψήστε στο γκριλ (~240 °C) για 20–30 λεπτά, γυρίζοντας, μέχρι να μαυρίσει η φλούδα. Το αποτέλεσμα είναι λίγο λιγότερο καπνιστό αλλά πολύ κοντινό.",
    oil_h="Ο ρόλος του ελαιόλαδου",
    oil="Στη mechouia το ελαιόλαδο δεν είναι απλή προσθήκη: δένει τα λαχανικά, δίνει βελούδινη υφή και μεταφέρει τα αρώματα καρβί και σκόρδου. Διαλέξτε ένα <strong>φρουτώδες, ελαφρώς πικάντικο</strong> έξτρα παρθένο, αρκετά δυνατό για την καπνιστή γεύση. Κρατήστε πάντα λίγο για ωμό τελείωμα.",
    tips_h="Μυστικά επιτυχίας",
    tips=[
        "Κάψτε πραγματικά τη φλούδα: το δειλό ψήσιμο δίνει άνοστη σαλάτα.",
        "Στραγγίστε και πιέστε τα λαχανικά. Η καλή mechouia δεν είναι νερουλή.",
        "Κόψτε με μαχαίρι, όχι μπλέντερ.",
        "Ρυθμίστε την ένταση με φρέσκια καυτερή ή λίγη harissa.",
        "Φτιάξτε την από την προηγουμένη: τα αρώματα αναπτύσσονται.",
    ],
    var_h="Τοπικές παραλλαγές",
    variations=[
        "<strong>Στιλ Τύνιδας</strong>: λεπτή, με άφθονο τόνο και αυγό.",
        "<strong>Στιλ Σφαξ / Ναμπέλ</strong>: πιο πικάντικη, ενίοτε με ψητό κρεμμύδι.",
        "<strong>Εκδοχή harissa</strong>: προσθέστε μια κουταλιά harissa.",
        "<strong>Χορτοφαγική / vegan</strong>: χωρίς τόνο και αυγό, με ελιές, κάπαρη και άφθονο ελαιόλαδο.",
    ],
    serve_h="Πώς σερβίρεται",
    serve="Η mechouia σερβίρεται ως ορεκτικό ή μεζές με φρέσκο ψωμί, ως γέμιση σε τυνησιακό σάντουιτς, ή δίπλα σε ψητά κρέατα και ψάρι. Μια φέτα λεμόνι και λίγο ελαιόλαδο στο τέλος κάνουν τη διαφορά.",
    store_h="Διατήρηση",
    store="Διατηρείται 3 ημέρες στο ψυγείο σε αεροστεγές δοχείο, με ένα στρώμα ελαιόλαδου από πάνω. Βγάλτε την 15 λεπτά πριν το σερβίρισμα. Αποφύγετε την κατάψυξη.",
    faq_h="Συχνές ερωτήσεις",
    faqs=[
        ("Τι είναι η σαλάτα mechouia;",
         "Η mechouia (slata mechouia, \"ψητή σαλάτα\") είναι τυνησιακή σαλάτα από πιπεριές και ντομάτες ψημένες στη φλόγα, ψιλοκομμένες και καρυκευμένες με σκόρδο, καρβί και έξτρα παρθένο ελαιόλαδο, με τόνο, βραστό αυγό, ελιές και κάπαρη. Σερβίρεται ως ορεκτικό με ψωμί."),
        ("Μπορώ να τη φτιάξω στον φούρνο;",
         "Ναι. Βάλτε τα λαχανικά σε ταψί και ψήστε στο γκριλ (~240 °C) για 20–30 λεπτά, γυρίζοντας, μέχρι να μαυρίσει η φλούδα. Η γεύση είναι λίγο λιγότερο καπνιστή αλλά πολύ κοντινή."),
        ("Γιατί νερουλιάζει η mechouia μου;",
         "Σχεδόν πάντα επειδή τα λαχανικά δεν στραγγίστηκαν αρκετά, ή επειδή χτυπήθηκαν στο μπλέντερ. Πιέστε τις ξεφλουδισμένες ντομάτες και κόψτε με μαχαίρι."),
        ("Μπορώ να τη φτιάξω χωρίς τόνο;",
         "Ναι — γίνεται χορτοφαγική (ή vegan χωρίς αυγό). Γαρνίρετε με ελιές, κάπαρη και άφθονο ελαιόλαδο αντί για τόνο και αυγό."),
        ("Ποιο ελαιόλαδο να χρησιμοποιήσω;",
         "Ένα φρουτώδες, ελαφρώς πικάντικο έξτρα παρθένο ελαιόλαδο, αρκετά δυνατό για την καπνιστή γεύση. Κρατήστε λίγο για ωμό τελείωμα."),
        ("Καρβί ή κύμινο;",
         "Η τυνησιακή mechouia χρησιμοποιεί παραδοσιακά καρβί. Το κύμινο δίνει διαφορετικό, πιο γήινο προφίλ· βοηθά αλλά αλλάζει τον χαρακτήρα."),
    ],
    schema_name="Τυνησιακή Σαλάτα Mechouia",
    schema_desc="Η αυθεντική τυνησιακή σαλάτα mechouia: πιπεριές και ντομάτες ψημένες στη φλόγα, σκόρδο, καρβί και έξτρα παρθένο ελαιόλαδο, με τόνο και αυγό.",
    schema_ing=[
        "4 πράσινες πιπεριές", "3 ώριμες ντομάτες", "1 πράσινη καυτερή (προαιρετικό)",
        "4 σκελίδες σκόρδο", "4 κ.σ. έξτρα παρθένο ελαιόλαδο", "1 κ.γ. καρβί τριμμένο",
        "1/2 κ.γ. κόλιανδρο τριμμένο", "αλάτι", "1 κ.σ. χυμό λεμονιού", "1 κονσέρβα τόνο",
        "2 βραστά αυγά", "μαύρες ελιές", "κάπαρη",
    ],
    schema_steps=[
        "Ψήστε πιπεριές, ντομάτες, καυτερή και σκόρδο στη φλόγα ή στο γκριλ μέχρι να μαυρίσει η φλούδα.",
        "Σκεπάστε για 10 λεπτά ώστε ο ατμός να ξεκολλήσει τη φλούδα.",
        "Ξεφλουδίστε, αφαιρέστε σπόρους και πιέστε τα λαχανικά για να φύγει το νερό.",
        "Ψιλοκόψτε με μαχαίρι· λιώστε το σκόρδο με αλάτι.",
        "Καρυκεύστε με σκόρδο, καρβί, κόλιανδρο, αλάτι, ελαιόλαδο και λεμόνι.",
        "Σερβίρετε με ελαιόλαδο και γαρνίρετε με τόνο, αυγό, ελιές και κάπαρη.",
    ],
    keywords="σαλάτα mechouia, τυνησιακή mechouia, συνταγή mechouia, ψητές πιπεριές, ελαιόλαδο",
    cuisine="Tunisian", category="Ορεκτικό",
    breadcrumb=["Αρχική", "Συνταγές", "Τυνησιακή Σαλάτα Mechouia"],
    also="Δείτε επίσης", pillar="Ελαιόλαδο: ο πλήρης κεντρικός οδηγός",
    obs="Δείτε το παρατηρητήριο 2026",
    pillarhref="../elaio-lado.html", obshref="../paratiritirio-elaio-lado-2026.html",
    nav="L'OR VERT / ΣΥΝΤΑΓΕΣ", home="Αρχική", foot="Το σημειωματάριο αναφοράς του L'Or Vert για το ελαιόλαδο, τη μεσογειακή κουζίνα και την καθημερινή χρήση.",
)


def esc(s):
    return html.escape(s, quote=True)


def li(items):
    return "\n".join(f"            <li>{x}</li>" for x in items)


def ol(items):
    return "\n".join(f"            <li>{x}</li>" for x in items)


def render(lang, d):
    url = f"{SITE}/recipes/{SLUG}-{lang}.html"
    alts = "\n    ".join(
        f'<link rel="alternate" hreflang="{lg}" href="{SITE}/recipes/{SLUG}-{lg}.html" />'
        for lg in ("fr", "en", "it", "el"))
    recipe = {
        "@context": "https://schema.org/", "@type": "Recipe",
        "name": d["schema_name"],
        "author": {"@type": "Organization", "name": "L'Or Vert", "@id": f"{SITE}/#organization"},
        "publisher": {"@type": "Organization", "name": "L'Or Vert", "url": SITE},
        "datePublished": "2026-05-04", "dateModified": "2026-07-04",
        "description": d["schema_desc"],
        "image": OG, "recipeCuisine": d["cuisine"], "recipeCategory": d["category"],
        "prepTime": "PT20M", "cookTime": "PT25M", "totalTime": "PT45M",
        "recipeYield": "4 servings",
        "recipeIngredient": d["schema_ing"],
        "recipeInstructions": [{"@type": "HowToStep", "text": s} for s in d["schema_steps"]],
        "nutrition": {"@type": "NutritionInformation", "servingSize": "1 portion",
                      "calories": "180 kcal", "fatContent": "14 g", "proteinContent": "8 g",
                      "carbohydrateContent": "6 g"},
        "keywords": d["keywords"], "inLanguage": lang,
        "mainEntityOfPage": url,
    }
    faqpage = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}}
                       for q, a in d["faqs"]],
    }
    crumbs = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": d["breadcrumb"][0], "item": f"{SITE}/index{'' if lang=='fr' else '-'+lang}.html"},
            {"@type": "ListItem", "position": 2, "name": d["breadcrumb"][1], "item": url},
            {"@type": "ListItem", "position": 3, "name": d["breadcrumb"][2], "item": url},
        ],
    }
    faq_html = "\n".join(
        f'        <h3>{esc(q)}</h3>\n        <p>{esc(a)}</p>' for q, a in d["faqs"])

    return f"""<!DOCTYPE html>
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
    <link rel="alternate" hreflang="x-default" href="{SITE}/recipes/{SLUG}-en.html" />
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
    <script type="application/ld+json">{json.dumps(recipe, ensure_ascii=False, indent=2)}</script>
    <script type="application/ld+json">{json.dumps(faqpage, ensure_ascii=False, indent=2)}</script>
    <script type="application/ld+json">{json.dumps(crumbs, ensure_ascii=False, indent=2)}</script>
</head>
<body>
<nav class="site-nav"><div class="container"><a href="../index{'' if lang=='fr' else '-'+lang}.html" class="logo">{esc(d['nav'])}</a></div></nav>
<header class="page-hero" style="background: linear-gradient(135deg, var(--avocado) 0%, var(--sage) 100%);">
    <div class="container">
        <div class="breadcrumb"><a href="../index{'' if lang=='fr' else '-'+lang}.html">{esc(d['home'])}</a> &raquo; {esc(d['breadcrumb'][1])}</div>
        <h1>{esc(d['h1'])}</h1>
        <p class="lede">{esc(d['lede'])}</p>
    </div>
</header>
<main class="container">
    <article class="guide">
        <div class="callout">{d['info']}</div>
        <p class="intro">{d['intro']}</p>

        <h2>{esc(d['ing_h'])}</h2>
        <ul>
{li(d['ingredients'])}
        </ul>
        <h3>{esc(d['garn_h'])}</h3>
        <ul>
{li(d['garnish'])}
        </ul>

        <h2>{esc(d['steps_h'])}</h2>
        <ol>
{ol(d['steps'])}
        </ol>

        <h2>{esc(d['oven_h'])}</h2>
        <p>{d['oven']}</p>

        <h2>{esc(d['oil_h'])}</h2>
        <p>{d['oil']}</p>

        <h2>{esc(d['tips_h'])}</h2>
        <ul>
{li(d['tips'])}
        </ul>

        <h2>{esc(d['var_h'])}</h2>
        <ul>
{li(d['variations'])}
        </ul>

        <h2>{esc(d['serve_h'])}</h2>
        <p>{esc(d['serve'])}</p>

        <h2>{esc(d['store_h'])}</h2>
        <p>{esc(d['store'])}</p>

        <h2>{esc(d['faq_h'])}</h2>
{faq_html}

        <div class="pillar-linkbox">
            <strong>{esc(d['also'])}</strong>
            <a href="{d['pillarhref']}">{esc(d['pillar'])}</a>
            <a href="{d['obshref']}">{esc(d['obs'])}</a>
        </div>
    </article>
</main>
<footer class="site-footer"><div class="container"><h3>L'Or Vert</h3><p>{esc(d['foot'])}</p><div class="copyright">&copy; 2026 — L'Or Vert</div></div></footer>
</body>
</html>
"""


def main():
    for lang, d in C.items():
        path = os.path.join(ROOT, "recipes", f"{SLUG}-{lang}.html")
        out = render(lang, d)
        # validate JSON-LD
        import re
        for m in re.findall(r'<script[^>]*ld\+json[^>]*>(.*?)</script>', out, re.S):
            json.loads(m)
        with open(path, "w", encoding="utf-8") as f:
            f.write(out)
        print("wrote", path, len(out), "bytes")


if __name__ == "__main__":
    main()

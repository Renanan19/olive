# -*- coding: utf-8 -*-
"""Content for the sustainable-olive-oil pillar (x4 languages)."""
from sustainability_pillar import build

C = {}

# ================================================================== EN =========
C["en"] = dict(
    title="Sustainable Olive Oil: the complete guide (how to identify it, certifications, impact)",
    desc="The complete guide to sustainable olive oil: a clear definition, a step-by-step method to determine if an olive oil is sustainable, the certifications that matter, the real environmental impact, and how olive oil compares with other fats.",
    h1="Sustainable Olive Oil: the complete guide",
    lede="What sustainability really means for olive oil, a step-by-step method to judge it from the bottle, the certifications worth trusting, the true environmental impact of how olives are grown, and how olive oil compares with other fats.",
    readtime="~9 min",
    keywords="sustainable olive oil, how to determine if olive oil is sustainable, how to identify sustainable olive oil, olive oil environmental impact, olive oil certifications, most sustainable olive oil, organic olive oil sustainability",
    kf_label="Key facts",
    intro="Olive oil is often sold as a natural, healthy choice, yet the word \"sustainable\" on a label rarely comes with a definition. This pillar guide is the complete, practical answer: what sustainability actually means for olive oil, how to determine it from the bottle, the certifications worth trusting, the real environmental impact of how olives are grown, and how olive oil compares with other fats.",
    key_facts=[
        "Sustainable olive oil balances three pillars: environmental impact, fair social conditions, and long-term economic viability for growers.",
        "You can determine sustainability before buying, from concrete label signals: credible certification, traceable single origin, a harvest date, farming transparency, honest packaging and a realistic price.",
        "How olives are grown decides the impact: traditional rainfed groves are low-input, carbon-storing and biodiverse; intensive and super-high-density (SHD) groves yield more but use more water and agrochemicals and drive soil erosion.",
        "Olive oil generally has a lower carbon and land footprint than butter and many other fats, and well-managed groves can act as a net carbon sink.",
        "The most trusted labels are EU/USDA organic, PDO/PGI (protected origin) and third-party schemes such as Rainforest Alliance; \"eco\", \"natural\" and \"cold-pressed\" are not sustainability guarantees.",
    ],
    toc=[("what", "What is sustainable olive oil"), ("how", "How to determine if it's sustainable"),
         ("impact", "Environmental impact"), ("certifications", "Certifications and labels"),
         ("compare", "How it compares with other fats"), ("buying", "Buying sustainable olive oil"),
         ("myths", "Greenwashing to avoid"), ("faq", "FAQ")],
    sections=[
        ("what", "What is sustainable olive oil",
         "<p>Sustainability is not a single feature but a balance of three pillars. The <strong>environmental</strong> pillar covers how much water, energy and agrochemicals a grove uses and its effect on soil, biodiversity and carbon. The <strong>social</strong> pillar covers fair pay and safe conditions for pickers and mill workers. The <strong>economic</strong> pillar covers whether the price lets growers keep farming without degrading the land.</p>"
         "<p>An olive oil is genuinely sustainable when it performs well across all three over the long term, not when it scores on one and fails the others. That is why a single claim, such as \"organic\" or \"local\", is a signal rather than a full answer.</p>"),
        ("how", "How to determine if an olive oil is sustainable",
         "<p>You can assess most of this from the label and the producer, before you buy. Work through these six checks:</p>"
         "<ol>"
         "<li><strong>Look for a credible certification</strong> — an organic leaf/USDA seal, PDO/PGI protected origin, or a third-party scheme, not just the word \"eco\".</li>"
         "<li><strong>Check for a traceable single origin</strong> — a named country, region, estate or mill, rather than a vague \"blend of EU and non-EU olive oils\".</li>"
         "<li><strong>Find a harvest date</strong> — it shows freshness and a producer who tracks their crop, not only a distant best-before date.</li>"
         "<li><strong>Read the farming description</strong> — look for rainfed or traditional groves, cover crops, reduced tillage, or water-saving drip irrigation.</li>"
         "<li><strong>Inspect the packaging</strong> — dark glass or tin protects the oil and cuts spoilage waste; check for recyclable materials.</li>"
         "<li><strong>Sanity-check the price</strong> — genuinely sustainable extra virgin olive oil cannot be produced at the lowest supermarket prices.</li>"
         "</ol>"
         "<p>No single signal is proof. Two or three together already tell you a lot; four or more make a reliable case.</p>"),
        ("impact", "The environmental impact of olive farming",
         "<p>The footprint depends almost entirely on <em>how</em> the olives are grown. The contrast is clearest between traditional rainfed groves and modern intensive plantings.</p>"
         "<table><thead><tr><th>Factor</th><th>Traditional / rainfed</th><th>Intensive / super-high-density</th></tr></thead><tbody>"
         "<tr><td>Water use</td><td>Little or none (rainfed)</td><td>High (irrigated)</td></tr>"
         "<tr><td>Agrochemicals</td><td>Low</td><td>Higher (fertiliser, herbicide)</td></tr>"
         "<tr><td>Soil</td><td>Protected, stable</td><td>Erosion risk on bare ground</td></tr>"
         "<tr><td>Biodiversity</td><td>High (habitat between trees)</td><td>Lower (monoculture rows)</td></tr>"
         "<tr><td>Carbon</td><td>Stores carbon (old trees, soil)</td><td>Higher inputs, less storage</td></tr>"
         "<tr><td>Yield</td><td>Lower per hectare</td><td>Much higher per hectare</td></tr>"
         "</tbody></table>"
         "<p>Intensive groves are not automatically unsustainable: cover crops, reduced tillage and efficient drip irrigation can lower their impact substantially. A separate issue is <strong>olive-mill wastewater</strong>, a pollutant in some regions; modern two-phase mills reduce it. On carbon, olive oil compares well with animal fats, and a well-managed grove can absorb more carbon than its production emits.</p>"),
        ("certifications", "Certifications and labels to look for",
         "<table><thead><tr><th>Label</th><th>What it guarantees</th></tr></thead><tbody>"
         "<tr><td>EU organic / USDA Organic</td><td>No synthetic pesticides or fertilisers; better for soil and water, though not a full sustainability audit.</td></tr>"
         "<tr><td>PDO / PGI (protected origin)</td><td>Verified origin and traditional method tied to a region; strong traceability.</td></tr>"
         "<tr><td>Rainforest Alliance / similar</td><td>Third-party checks on environmental and social practices across the farm.</td></tr>"
         "<tr><td>Fair for Life / fair-trade</td><td>Focus on fair pay and working conditions (the social pillar).</td></tr>"
         "<tr><td>Carbon-neutral / B-Corp</td><td>Varies in rigour; read what is actually measured and verified.</td></tr>"
         "</tbody></table>"
         "<p>Certifications are a shortcut, not the whole story: a small, transparent producer without paid certification can still be highly sustainable, while a big brand with a green logo may not be.</p>"),
        ("compare", "How olive oil compares with other fats",
         "<p>On most environmental measures, olive oil compares favourably with the fats it replaces. It generally has a lower carbon and land footprint than <strong>butter</strong> and other animal fats, and it avoids the deforestation risk linked to some <strong>palm oil</strong>. Compared with seed oils such as sunflower or rapeseed, the picture is closer and depends heavily on farming method and transport.</p>"
         "<p>The key point: choosing olive oil over butter is usually a lower-impact choice, but <em>which</em> olive oil still matters. A rainfed, certified, traceable oil and an intensively irrigated, anonymous one can have very different footprints.</p>"),
        ("buying", "Buying sustainable olive oil in practice",
         "<p>In a shop or online, prioritise oils that combine several of the signals above: <strong>extra virgin</strong> quality, an <strong>organic or PDO/PGI</strong> label, a <strong>named single origin</strong>, a <strong>harvest date</strong>, dark glass or tin, and a producer who is open about their farming. Buying a size you will finish while fresh also reduces waste. A slightly higher price for a traceable, certified oil usually reflects the real cost of sustainable production.</p>"),
        ("myths", "Greenwashing to avoid",
         "<ul>"
         "<li><strong>Vague eco words</strong> — \"eco\", \"natural\", \"green\" with no certification or detail mean little.</li>"
         "<li><strong>\"Cold-pressed\" as a green claim</strong> — it describes processing temperature, not sustainability; most real extra virgin is already cold-extracted.</li>"
         "<li><strong>Origin hidden behind a story</strong> — a romantic label with no country, region or harvest date is a red flag.</li>"
         "<li><strong>A single green logo on an intensive supply chain</strong> — one certification does not offset a lack of traceability.</li>"
         "<li><strong>Assuming \"local\" always wins</strong> — transport is only part of the footprint; farming method often matters more.</li>"
         "</ul>"),
    ],
    howto_name="How to determine if an olive oil is sustainable",
    howto_desc="A six-step method to assess the sustainability of an olive oil from its label and producer, before you buy.",
    howto_steps=[
        ("Look for a credible certification", "Check for an organic leaf/USDA seal, PDO/PGI protected origin, or a third-party scheme such as Rainforest Alliance, rather than just the word 'eco'."),
        ("Check for a traceable single origin", "Look for a named country, region, estate or mill, rather than a vague blend of EU and non-EU olive oils."),
        ("Find a harvest date", "A harvest date shows freshness and a producer who tracks their crop, not only a distant best-before date."),
        ("Read the farming description", "Look for rainfed or traditional groves, cover crops, reduced tillage or water-saving drip irrigation."),
        ("Inspect the packaging", "Dark glass or tin protects the oil and reduces spoilage waste; check that materials are recyclable."),
        ("Sanity-check the price", "Genuinely sustainable extra virgin olive oil cannot be produced at the lowest supermarket prices."),
    ],
    faq_h="Frequently asked questions",
    faqs=[
        ("How do you determine if olive oil is sustainable?",
         "Assess the bottle and producer for concrete signals: a credible certification (organic, PDO/PGI, or a third-party scheme), a traceable single origin, a harvest date, transparency about farming (rainfed or traditional groves, water saving), and honest recyclable packaging. No single signal is proof, but several together give a reliable picture."),
        ("How can you identify sustainable olive oil in a shop?",
         "Look for an organic or protected-origin (PDO/PGI) label, a named region or estate rather than a vague blend, a harvest date, and a producer who describes their farming. Dark glass or tin and a realistic price are supporting signs. Avoid oils with no origin, no date and only words like 'eco' or 'natural'."),
        ("What is sustainable olive oil?",
         "Olive oil produced in a way that balances environmental impact (low water, healthy soil, biodiversity, low carbon), fair social conditions for workers, and long-term economic viability for growers. It is a balance of all three, not a single feature."),
        ("What is the most sustainable olive oil?",
         "Not a particular brand, but a profile: an extra virgin oil from traditional or rainfed groves, certified (organic and/or PDO/PGI), traceable to a single origin, honestly packaged and priced. Farming method and traceability matter more than any logo."),
        ("Is organic olive oil automatically sustainable?",
         "Organic certification means no synthetic pesticides or fertilisers, which helps soil and water, but it does not by itself cover water use, biodiversity or fair labour. Organic is a strong signal of sustainability, not a complete guarantee."),
        ("What is the environmental impact of olive oil?",
         "It depends on how the olives are grown. Traditional rainfed groves have a small footprint and store carbon; intensive and super-high-density groves yield more but use more water and agrochemicals and can cause soil erosion and biodiversity loss. Overall, olive oil has a relatively low carbon footprint compared with animal fats."),
        ("Are traditional or intensive olive groves more sustainable?",
         "Traditional rainfed groves are generally more sustainable per hectare: low input, biodiversity-rich and carbon-storing. Intensive groves are more productive but need more water and chemicals; cover crops, reduced tillage and efficient irrigation can narrow the gap."),
        ("Is olive oil more sustainable than other cooking oils?",
         "Olive oil generally has a lower carbon and land footprint than butter and avoids the deforestation risk of some palm oil. Versus seed oils like sunflower or rapeseed it is closer and depends on farming and transport. Choosing olive oil over butter is usually lower-impact, but which olive oil still matters."),
    ],
)

# ================================================================== FR =========
C["fr"] = dict(
    title="Huile d'olive durable : le guide complet (reconnaître, certifications, impact)",
    desc="Le guide complet de l'huile d'olive durable : définition claire, méthode pas à pas pour savoir si une huile est durable, certifications qui comptent, véritable impact environnemental, et comparaison avec les autres matières grasses.",
    h1="Huile d'olive durable : le guide complet",
    lede="Ce que la durabilité signifie vraiment pour l'huile d'olive, une méthode pas à pas pour la juger sur la bouteille, les certifications fiables, l'impact environnemental réel de la culture, et la comparaison avec les autres matières grasses.",
    readtime="~9 min",
    keywords="huile d'olive durable, comment savoir si huile d'olive est durable, oléiculture durable, impact environnemental huile d'olive, certifications huile d'olive, huile d'olive la plus durable, huile d'olive bio durable",
    kf_label="En bref",
    intro="L'huile d'olive est souvent vendue comme un choix naturel et sain, mais le mot « durable » sur une étiquette est rarement défini. Ce guide pilier est la réponse complète et concrète : ce que la durabilité signifie pour l'huile d'olive, comment la déterminer depuis la bouteille, les certifications fiables, l'impact environnemental réel de la culture, et la comparaison avec les autres matières grasses.",
    key_facts=[
        "Une huile d'olive durable équilibre trois piliers : impact environnemental, conditions sociales justes et viabilité économique des producteurs sur le long terme.",
        "On peut déterminer la durabilité avant l'achat, via des signaux concrets : certification crédible, origine unique traçable, date de récolte, transparence agricole, emballage honnête et prix réaliste.",
        "La façon de cultiver décide de l'impact : les oliveraies traditionnelles en sec sont peu gourmandes, stockent du carbone et abritent la biodiversité ; les vergers intensifs et super-intensifs produisent plus mais consomment plus d'eau et d'intrants et favorisent l'érosion.",
        "L'huile d'olive a en général une empreinte carbone et foncière plus faible que le beurre et beaucoup d'autres graisses, et une oliveraie bien gérée peut être un puits de carbone net.",
        "Les labels les plus fiables sont le bio (UE/USDA), l'AOP/IGP (origine protégée) et les schémas tiers comme Rainforest Alliance ; « éco », « naturel » et « pressée à froid » ne garantissent pas la durabilité.",
    ],
    toc=[("what", "Qu'est-ce qu'une huile d'olive durable"), ("how", "Comment savoir si elle est durable"),
         ("impact", "Impact environnemental"), ("certifications", "Certifications et labels"),
         ("compare", "Face aux autres matières grasses"), ("buying", "Acheter une huile durable"),
         ("myths", "Greenwashing à éviter"), ("faq", "FAQ")],
    sections=[
        ("what", "Qu'est-ce qu'une huile d'olive durable",
         "<p>La durabilité n'est pas une caractéristique unique mais un équilibre entre trois piliers. Le pilier <strong>environnemental</strong> couvre l'eau, l'énergie et les intrants utilisés, et l'effet sur le sol, la biodiversité et le carbone. Le pilier <strong>social</strong> couvre la rémunération juste et les conditions sûres des cueilleurs et du moulin. Le pilier <strong>économique</strong> couvre un prix qui permet aux producteurs de continuer sans dégrader la terre.</p>"
         "<p>Une huile est vraiment durable quand elle est bonne sur les trois dans la durée, pas quand elle brille sur un seul. C'est pourquoi une allégation isolée, « bio » ou « local », est un signal plutôt qu'une réponse complète.</p>"),
        ("how", "Comment savoir si une huile d'olive est durable",
         "<p>On peut évaluer l'essentiel depuis l'étiquette et le producteur, avant l'achat. Passez ces six vérifications :</p>"
         "<ol>"
         "<li><strong>Cherchez une certification crédible</strong> — logo bio/feuille européenne, origine AOP/IGP, ou un label tiers, pas seulement le mot « éco ».</li>"
         "<li><strong>Vérifiez une origine unique traçable</strong> — un pays, une région, un domaine ou un moulin nommés, plutôt qu'un vague « mélange d'huiles UE et non UE ».</li>"
         "<li><strong>Trouvez une date de récolte</strong> — signe de fraîcheur et d'un producteur qui suit sa récolte, pas seulement une DDM lointaine.</li>"
         "<li><strong>Lisez la description agricole</strong> — oliveraies en sec ou traditionnelles, couverts végétaux, travail du sol réduit, goutte-à-goutte économe.</li>"
         "<li><strong>Regardez l'emballage</strong> — verre foncé ou bidon (protège l'huile, limite le gaspillage), matériaux recyclables.</li>"
         "<li><strong>Vérifiez le prix</strong> — une extra vierge vraiment durable ne peut pas être produite aux prix les plus bas.</li>"
         "</ol>"
         "<p>Aucun signal seul n'est une preuve. Deux ou trois ensemble en disent déjà long ; quatre ou plus donnent un dossier fiable.</p>"),
        ("impact", "L'impact environnemental de l'oléiculture",
         "<p>L'empreinte dépend presque entièrement de la <em>façon</em> dont les olives sont cultivées. Le contraste est le plus net entre oliveraies traditionnelles en sec et plantations intensives modernes.</p>"
         "<table><thead><tr><th>Facteur</th><th>Traditionnel / en sec</th><th>Intensif / super-intensif</th></tr></thead><tbody>"
         "<tr><td>Eau</td><td>Peu ou pas (pluvial)</td><td>Élevée (irriguée)</td></tr>"
         "<tr><td>Intrants</td><td>Faibles</td><td>Plus (engrais, herbicide)</td></tr>"
         "<tr><td>Sol</td><td>Protégé, stable</td><td>Risque d'érosion à nu</td></tr>"
         "<tr><td>Biodiversité</td><td>Élevée (habitat entre arbres)</td><td>Plus faible (rangs monoculture)</td></tr>"
         "<tr><td>Carbone</td><td>Stocke (vieux arbres, sol)</td><td>Plus d'intrants, moins de stockage</td></tr>"
         "<tr><td>Rendement</td><td>Plus faible par hectare</td><td>Bien plus élevé par hectare</td></tr>"
         "</tbody></table>"
         "<p>Les vergers intensifs ne sont pas automatiquement non durables : couverts végétaux, travail du sol réduit et goutte-à-goutte efficace réduisent nettement l'impact. Autre enjeu, les <strong>margines</strong> (eaux de moulin), polluantes dans certaines régions ; les moulins deux-phases modernes les réduisent. Côté carbone, l'huile d'olive se compare bien aux graisses animales, et une oliveraie bien gérée peut absorber plus de carbone qu'elle n'en émet.</p>"),
        ("certifications", "Certifications et labels à rechercher",
         "<table><thead><tr><th>Label</th><th>Ce qu'il garantit</th></tr></thead><tbody>"
         "<tr><td>Bio UE / USDA Organic</td><td>Pas de pesticides ni d'engrais de synthèse ; meilleur pour le sol et l'eau, sans être un audit complet.</td></tr>"
         "<tr><td>AOP / IGP (origine protégée)</td><td>Origine et méthode traditionnelle vérifiées, liées à une région ; forte traçabilité.</td></tr>"
         "<tr><td>Rainforest Alliance / similaire</td><td>Contrôles tiers sur les pratiques environnementales et sociales.</td></tr>"
         "<tr><td>Fair for Life / commerce équitable</td><td>Rémunération et conditions de travail (pilier social).</td></tr>"
         "<tr><td>Neutre en carbone / B-Corp</td><td>Rigueur variable ; regardez ce qui est mesuré et vérifié.</td></tr>"
         "</tbody></table>"
         "<p>Les certifications sont un raccourci, pas toute l'histoire : un petit producteur transparent sans certification payante peut être très durable, tandis qu'une grande marque au logo vert ne l'est pas forcément.</p>"),
        ("compare", "Face aux autres matières grasses",
         "<p>Sur la plupart des critères, l'huile d'olive se compare favorablement aux graisses qu'elle remplace. Elle a en général une empreinte carbone et foncière plus faible que le <strong>beurre</strong> et les autres graisses animales, et évite le risque de déforestation lié à certaines <strong>huiles de palme</strong>. Face aux huiles de graines (tournesol, colza), l'écart est plus serré et dépend beaucoup de la méthode agricole et du transport.</p>"
         "<p>L'essentiel : choisir l'huile d'olive plutôt que le beurre est en général un choix moins impactant, mais <em>quelle</em> huile compte encore. Une huile en sec, certifiée et traçable et une huile intensivement irriguée et anonyme ont des empreintes très différentes.</p>"),
        ("buying", "Acheter une huile d'olive durable en pratique",
         "<p>En magasin ou en ligne, privilégiez les huiles qui cumulent plusieurs signaux : qualité <strong>extra vierge</strong>, label <strong>bio ou AOP/IGP</strong>, <strong>origine unique nommée</strong>, <strong>date de récolte</strong>, verre foncé ou bidon, et un producteur transparent sur sa culture. Acheter un format que vous finirez frais réduit aussi le gaspillage. Un prix un peu plus élevé pour une huile traçable et certifiée reflète souvent le coût réel d'une production durable.</p>"),
        ("myths", "Greenwashing à éviter",
         "<ul>"
         "<li><strong>Mots verts vagues</strong> — « éco », « naturel », « vert » sans certification ni détail ne veulent pas dire grand-chose.</li>"
         "<li><strong>« Pressée à froid » comme argument vert</strong> — cela décrit la température, pas la durabilité ; la vraie extra vierge est déjà extraite à froid.</li>"
         "<li><strong>Origine cachée derrière une histoire</strong> — une étiquette romantique sans pays, région ni date de récolte est un signal d'alerte.</li>"
         "<li><strong>Un seul logo vert sur une filière intensive</strong> — une certification ne compense pas l'absence de traçabilité.</li>"
         "<li><strong>Croire que « local » gagne toujours</strong> — le transport n'est qu'une part de l'empreinte ; la méthode compte souvent plus.</li>"
         "</ul>"),
    ],
    howto_name="Comment savoir si une huile d'olive est durable",
    howto_desc="Une méthode en six étapes pour évaluer la durabilité d'une huile d'olive depuis son étiquette et son producteur, avant l'achat.",
    howto_steps=[
        ("Cherchez une certification crédible", "Repérez un logo bio/feuille européenne, une origine AOP/IGP, ou un label tiers comme Rainforest Alliance, plutôt que le seul mot « éco »."),
        ("Vérifiez une origine unique traçable", "Cherchez un pays, une région, un domaine ou un moulin nommés, plutôt qu'un vague mélange d'huiles UE et non UE."),
        ("Trouvez une date de récolte", "Une date de récolte indique la fraîcheur et un producteur qui suit sa récolte, pas seulement une DDM lointaine."),
        ("Lisez la description agricole", "Cherchez des oliveraies en sec ou traditionnelles, des couverts végétaux, un travail du sol réduit ou un goutte-à-goutte économe."),
        ("Regardez l'emballage", "Le verre foncé ou le bidon protège l'huile et limite le gaspillage ; vérifiez des matériaux recyclables."),
        ("Vérifiez le prix", "Une huile extra vierge vraiment durable ne peut pas être produite aux prix les plus bas."),
    ],
    faq_h="Questions fréquentes",
    faqs=[
        ("Comment savoir si une huile d'olive est durable ?",
         "Évaluez la bouteille et le producteur via des signaux concrets : certification crédible (bio, AOP/IGP ou label tiers), origine unique traçable, date de récolte, transparence agricole (oliveraies en sec ou traditionnelles, économie d'eau) et emballage honnête et recyclable. Aucun signal seul n'est une preuve, mais plusieurs ensemble donnent un tableau fiable."),
        ("Comment reconnaître une huile d'olive durable en magasin ?",
         "Cherchez un label bio ou une origine protégée (AOP/IGP), une région ou un domaine nommés plutôt qu'un mélange vague, une date de récolte, et un producteur qui décrit sa culture. Verre foncé ou bidon et prix réaliste sont des signes d'appui. Évitez les huiles sans origine, sans date et avec seulement « éco » ou « naturel »."),
        ("Qu'est-ce qu'une huile d'olive durable ?",
         "Une huile produite d'une manière qui équilibre l'impact environnemental (peu d'eau, sol sain, biodiversité, faible carbone), des conditions sociales justes et la viabilité économique des producteurs. C'est un équilibre des trois, pas une seule caractéristique."),
        ("Quelle est l'huile d'olive la plus durable ?",
         "Pas une marque précise, mais un profil : une huile extra vierge d'oliveraies traditionnelles ou en sec, certifiée (bio et/ou AOP/IGP), traçable à une origine unique, honnêtement emballée et tarifée. La méthode agricole et la traçabilité comptent plus qu'un logo."),
        ("L'huile d'olive bio est-elle automatiquement durable ?",
         "Le bio signifie pas de pesticides ni d'engrais de synthèse, ce qui aide le sol et l'eau, mais ne couvre pas à lui seul l'eau, la biodiversité ou l'équité sociale. Le bio est un signal fort, pas une garantie complète."),
        ("Quel est l'impact environnemental de l'huile d'olive ?",
         "Il dépend de la façon dont les olives sont cultivées. Les oliveraies traditionnelles en sec ont une faible empreinte et stockent du carbone ; les vergers intensifs et super-intensifs produisent plus mais consomment plus d'eau et d'intrants et peuvent causer érosion et perte de biodiversité. Globalement, empreinte carbone faible face aux graisses animales."),
        ("Oliveraies traditionnelles ou intensives : lesquelles sont plus durables ?",
         "Les oliveraies traditionnelles en sec sont généralement plus durables par hectare : peu d'intrants, riches en biodiversité et stockant du carbone. Les vergers intensifs sont plus productifs mais demandent plus d'eau et de produits ; couverts, travail du sol réduit et irrigation efficace réduisent l'écart."),
        ("L'huile d'olive est-elle plus durable que les autres huiles ?",
         "L'huile d'olive a en général une empreinte carbone et foncière plus faible que le beurre et évite le risque de déforestation de certaines huiles de palme. Face aux huiles de graines (tournesol, colza), l'écart est plus serré et dépend de la culture et du transport. Choisir l'huile d'olive plutôt que le beurre est en général moins impactant, mais quelle huile compte encore."),
    ],
)

# ================================================================== IT =========
C["it"] = dict(
    title="Olio d'oliva sostenibile: la guida completa (riconoscerlo, certificazioni, impatto)",
    desc="La guida completa all'olio d'oliva sostenibile: definizione chiara, metodo passo passo per capire se un olio è sostenibile, certificazioni che contano, reale impatto ambientale e confronto con altri grassi.",
    h1="Olio d'oliva sostenibile: la guida completa",
    lede="Cosa significa davvero sostenibilità per l'olio d'oliva, un metodo passo passo per giudicarlo dalla bottiglia, le certificazioni affidabili, il reale impatto ambientale della coltivazione e il confronto con altri grassi.",
    readtime="~9 min",
    keywords="olio d'oliva sostenibile, come capire se olio d'oliva è sostenibile, olivicoltura sostenibile, impatto ambientale olio d'oliva, certificazioni olio d'oliva, olio d'oliva più sostenibile",
    kf_label="In breve",
    intro="L'olio d'oliva è spesso venduto come scelta naturale e sana, ma la parola \"sostenibile\" su un'etichetta è raramente definita. Questa guida pilastro è la risposta completa e concreta: cosa significa sostenibilità per l'olio d'oliva, come capirlo dalla bottiglia, le certificazioni affidabili, il reale impatto ambientale della coltivazione e il confronto con altri grassi.",
    key_facts=[
        "Un olio d'oliva sostenibile bilancia tre pilastri: impatto ambientale, condizioni sociali eque e sostenibilità economica dei produttori nel lungo periodo.",
        "Puoi valutare la sostenibilità prima dell'acquisto, da segnali concreti: certificazione credibile, origine unica tracciabile, data di raccolta, trasparenza agricola, confezione onesta e prezzo realistico.",
        "Il modo di coltivare decide l'impatto: gli oliveti tradizionali in asciutto sono a basso input, immagazzinano carbonio e sono ricchi di biodiversità; quelli intensivi e superintensivi rendono di più ma usano più acqua e agrofarmaci e favoriscono l'erosione.",
        "L'olio d'oliva ha in genere un'impronta di carbonio e di suolo inferiore al burro e a molti altri grassi, e un oliveto ben gestito può essere un pozzo di carbonio netto.",
        "Le etichette più affidabili sono il bio (UE/USDA), la DOP/IGP (origine protetta) e schemi terzi come Rainforest Alliance; \"eco\", \"naturale\" e \"spremuto a freddo\" non garantiscono la sostenibilità.",
    ],
    toc=[("what", "Cos'è l'olio d'oliva sostenibile"), ("how", "Come capire se è sostenibile"),
         ("impact", "Impatto ambientale"), ("certifications", "Certificazioni ed etichette"),
         ("compare", "Rispetto ad altri grassi"), ("buying", "Comprare olio sostenibile"),
         ("myths", "Greenwashing da evitare"), ("faq", "FAQ")],
    sections=[
        ("what", "Cos'è l'olio d'oliva sostenibile",
         "<p>La sostenibilità non è una singola caratteristica ma un equilibrio tra tre pilastri. Il pilastro <strong>ambientale</strong> riguarda acqua, energia e agrofarmaci usati e l'effetto su suolo, biodiversità e carbonio. Il pilastro <strong>sociale</strong> riguarda paga equa e condizioni sicure per raccoglitori e frantoio. Il pilastro <strong>economico</strong> riguarda un prezzo che permetta ai produttori di continuare senza degradare la terra.</p>"
         "<p>Un olio è davvero sostenibile quando va bene su tutti e tre nel tempo, non quando brilla su uno solo. Per questo una singola dicitura, \"bio\" o \"locale\", è un segnale più che una risposta completa.</p>"),
        ("how", "Come capire se un olio d'oliva è sostenibile",
         "<p>Puoi valutare gran parte dall'etichetta e dal produttore, prima di comprare. Segui questi sei controlli:</p>"
         "<ol>"
         "<li><strong>Cerca una certificazione credibile</strong> — logo bio/foglia UE, origine DOP/IGP o uno schema terzo, non solo la parola \"eco\".</li>"
         "<li><strong>Verifica un'origine unica tracciabile</strong> — un paese, una regione, un'azienda o un frantoio indicati, non un vago \"miscela di oli UE e non UE\".</li>"
         "<li><strong>Trova una data di raccolta</strong> — indica freschezza e un produttore che segue il raccolto, non solo un TMC lontano.</li>"
         "<li><strong>Leggi la descrizione agricola</strong> — oliveti in asciutto o tradizionali, inerbimento, lavorazione ridotta, goccia a goccia efficiente.</li>"
         "<li><strong>Guarda la confezione</strong> — vetro scuro o latta (protegge l'olio, riduce gli sprechi), materiali riciclabili.</li>"
         "<li><strong>Controlla il prezzo</strong> — un extravergine davvero sostenibile non si produce ai prezzi più bassi.</li>"
         "</ol>"
         "<p>Nessun segnale da solo è una prova. Due o tre insieme dicono già molto; quattro o più danno un quadro affidabile.</p>"),
        ("impact", "L'impatto ambientale dell'olivicoltura",
         "<p>L'impronta dipende quasi interamente da <em>come</em> si coltivano le olive. Il contrasto è più chiaro tra oliveti tradizionali in asciutto e impianti intensivi moderni.</p>"
         "<table><thead><tr><th>Fattore</th><th>Tradizionale / asciutto</th><th>Intensivo / superintensivo</th></tr></thead><tbody>"
         "<tr><td>Acqua</td><td>Poca o nessuna (pioggia)</td><td>Alta (irrigato)</td></tr>"
         "<tr><td>Agrofarmaci</td><td>Bassi</td><td>Maggiori (fertilizzante, erbicida)</td></tr>"
         "<tr><td>Suolo</td><td>Protetto, stabile</td><td>Rischio erosione a nudo</td></tr>"
         "<tr><td>Biodiversità</td><td>Alta (habitat tra gli alberi)</td><td>Minore (filari monocoltura)</td></tr>"
         "<tr><td>Carbonio</td><td>Immagazzina (alberi vecchi, suolo)</td><td>Più input, meno stoccaggio</td></tr>"
         "<tr><td>Resa</td><td>Minore per ettaro</td><td>Molto maggiore per ettaro</td></tr>"
         "</tbody></table>"
         "<p>Gli oliveti intensivi non sono automaticamente insostenibili: inerbimento, lavorazione ridotta e goccia a goccia efficiente riducono molto l'impatto. Altro tema, le <strong>acque di vegetazione</strong> del frantoio, inquinanti in alcune regioni; i frantoi a due fasi moderni le riducono. Sul carbonio, l'olio d'oliva regge bene il confronto con i grassi animali, e un oliveto ben gestito può assorbire più carbonio di quanto ne emetta.</p>"),
        ("certifications", "Certificazioni ed etichette da cercare",
         "<table><thead><tr><th>Etichetta</th><th>Cosa garantisce</th></tr></thead><tbody>"
         "<tr><td>Bio UE / USDA Organic</td><td>Niente pesticidi o fertilizzanti sintetici; meglio per suolo e acqua, ma non un audit completo.</td></tr>"
         "<tr><td>DOP / IGP (origine protetta)</td><td>Origine e metodo tradizionale verificati, legati a una regione; forte tracciabilità.</td></tr>"
         "<tr><td>Rainforest Alliance / simili</td><td>Controlli terzi su pratiche ambientali e sociali.</td></tr>"
         "<tr><td>Fair for Life / commercio equo</td><td>Paga e condizioni di lavoro (pilastro sociale).</td></tr>"
         "<tr><td>Carbon neutral / B-Corp</td><td>Rigore variabile; leggi cosa viene misurato e verificato.</td></tr>"
         "</tbody></table>"
         "<p>Le certificazioni sono una scorciatoia, non tutta la storia: un piccolo produttore trasparente senza certificazione a pagamento può essere molto sostenibile, mentre una grande marca con un logo verde no.</p>"),
        ("compare", "Rispetto ad altri grassi",
         "<p>Sulla maggior parte dei parametri, l'olio d'oliva regge bene il confronto con i grassi che sostituisce. Ha in genere un'impronta di carbonio e di suolo inferiore al <strong>burro</strong> e agli altri grassi animali, ed evita il rischio di deforestazione legato a certi <strong>oli di palma</strong>. Rispetto agli oli di semi (girasole, colza) il divario è più stretto e dipende molto dal metodo e dal trasporto.</p>"
         "<p>Il punto chiave: scegliere l'olio d'oliva al posto del burro è di solito una scelta a minore impatto, ma <em>quale</em> olio conta ancora. Un olio in asciutto, certificato e tracciabile e uno intensivamente irrigato e anonimo hanno impronte molto diverse.</p>"),
        ("buying", "Comprare olio d'oliva sostenibile in pratica",
         "<p>In negozio o online, privilegia oli che combinano più segnali: qualità <strong>extravergine</strong>, etichetta <strong>bio o DOP/IGP</strong>, <strong>origine unica indicata</strong>, <strong>data di raccolta</strong>, vetro scuro o latta, e un produttore trasparente sulla coltivazione. Comprare un formato che finirai fresco riduce gli sprechi. Un prezzo un po' più alto per un olio tracciabile e certificato riflette spesso il costo reale di una produzione sostenibile.</p>"),
        ("myths", "Greenwashing da evitare",
         "<ul>"
         "<li><strong>Parole verdi vaghe</strong> — \"eco\", \"naturale\", \"green\" senza certificazione o dettagli valgono poco.</li>"
         "<li><strong>\"Spremuto a freddo\" come argomento verde</strong> — descrive la temperatura, non la sostenibilità; il vero extravergine è già estratto a freddo.</li>"
         "<li><strong>Origine nascosta dietro una storia</strong> — un'etichetta romantica senza paese, regione o data di raccolta è un campanello d'allarme.</li>"
         "<li><strong>Un solo logo verde su una filiera intensiva</strong> — una certificazione non compensa la mancanza di tracciabilità.</li>"
         "<li><strong>Credere che \"locale\" vinca sempre</strong> — il trasporto è solo una parte dell'impronta; il metodo conta spesso di più.</li>"
         "</ul>"),
    ],
    howto_name="Come capire se un olio d'oliva è sostenibile",
    howto_desc="Un metodo in sei passi per valutare la sostenibilità di un olio d'oliva da etichetta e produttore, prima di comprare.",
    howto_steps=[
        ("Cerca una certificazione credibile", "Individua un logo bio/foglia UE, un'origine DOP/IGP o uno schema terzo come Rainforest Alliance, non solo la parola 'eco'."),
        ("Verifica un'origine unica tracciabile", "Cerca un paese, una regione, un'azienda o un frantoio indicati, non una vaga miscela di oli UE e non UE."),
        ("Trova una data di raccolta", "Una data di raccolta indica freschezza e un produttore che segue il raccolto, non solo un TMC lontano."),
        ("Leggi la descrizione agricola", "Cerca oliveti in asciutto o tradizionali, inerbimento, lavorazione ridotta o goccia a goccia efficiente."),
        ("Guarda la confezione", "Vetro scuro o latta protegge l'olio e riduce gli sprechi; verifica materiali riciclabili."),
        ("Controlla il prezzo", "Un extravergine davvero sostenibile non si produce ai prezzi più bassi."),
    ],
    faq_h="Domande frequenti",
    faqs=[
        ("Come capire se un olio d'oliva è sostenibile?",
         "Valuta bottiglia e produttore da segnali concreti: certificazione credibile (bio, DOP/IGP o schema terzo), origine unica tracciabile, data di raccolta, trasparenza agricola (oliveti in asciutto o tradizionali, risparmio idrico) e confezione onesta e riciclabile. Nessun segnale da solo è prova, ma più segnali insieme danno un quadro affidabile."),
        ("Come riconoscere un olio d'oliva sostenibile al supermercato?",
         "Cerca un'etichetta bio o un'origine protetta (DOP/IGP), una regione o azienda indicata invece di una miscela vaga, una data di raccolta e un produttore che descrive la coltivazione. Vetro scuro o latta e prezzo realistico sono di supporto. Evita oli senza origine, senza data e con sole parole come 'eco' o 'naturale'."),
        ("Cos'è l'olio d'oliva sostenibile?",
         "Olio prodotto in modo da bilanciare impatto ambientale (poca acqua, suolo sano, biodiversità, basso carbonio), condizioni sociali eque e sostenibilità economica dei produttori. È un equilibrio dei tre, non una singola caratteristica."),
        ("Qual è l'olio d'oliva più sostenibile?",
         "Non una marca precisa, ma un profilo: un extravergine da oliveti tradizionali o in asciutto, certificato (bio e/o DOP/IGP), tracciabile a un'origine unica, confezionato e prezzato onestamente. Metodo e tracciabilità contano più di un logo."),
        ("L'olio d'oliva bio è automaticamente sostenibile?",
         "Il bio significa niente pesticidi o fertilizzanti sintetici, il che aiuta suolo e acqua, ma da solo non copre uso d'acqua, biodiversità o equità sociale. Il bio è un forte segnale, non una garanzia completa."),
        ("Qual è l'impatto ambientale dell'olio d'oliva?",
         "Dipende da come si coltivano le olive. Gli oliveti tradizionali in asciutto hanno un'impronta piccola e immagazzinano carbonio; quelli intensivi e superintensivi rendono di più ma usano più acqua e agrofarmaci e possono causare erosione e perdita di biodiversità. In generale, impronta di carbonio bassa rispetto ai grassi animali."),
        ("Oliveti tradizionali o intensivi: quali più sostenibili?",
         "Gli oliveti tradizionali in asciutto sono in genere più sostenibili per ettaro: pochi input, ricchi di biodiversità e capaci di immagazzinare carbonio. Quelli intensivi sono più produttivi ma richiedono più acqua e prodotti; inerbimento, lavorazione ridotta e irrigazione efficiente riducono il divario."),
        ("L'olio d'oliva è più sostenibile di altri oli?",
         "L'olio d'oliva ha in genere un'impronta di carbonio e di suolo inferiore al burro ed evita il rischio di deforestazione di certi oli di palma. Rispetto agli oli di semi (girasole, colza) è più vicino e dipende da coltivazione e trasporto. Scegliere l'olio d'oliva al posto del burro è di solito a minore impatto, ma quale olio conta ancora."),
    ],
)

# ================================================================== EL =========
C["el"] = dict(
    title="Βιώσιμο ελαιόλαδο: ο πλήρης οδηγός (αναγνώριση, πιστοποιήσεις, αποτύπωμα)",
    desc="Ο πλήρης οδηγός για το βιώσιμο ελαιόλαδο: σαφής ορισμός, μέθοδος βήμα-βήμα για να καταλάβετε αν ένα ελαιόλαδο είναι βιώσιμο, πιστοποιήσεις που μετρούν, πραγματικό περιβαλλοντικό αποτύπωμα και σύγκριση με άλλα λίπη.",
    h1="Βιώσιμο ελαιόλαδο: ο πλήρης οδηγός",
    lede="Τι σημαίνει πραγματικά βιωσιμότητα για το ελαιόλαδο, μια μέθοδος βήμα-βήμα για να το κρίνετε από το μπουκάλι, οι αξιόπιστες πιστοποιήσεις, το πραγματικό περιβαλλοντικό αποτύπωμα και η σύγκριση με άλλα λίπη.",
    readtime="~9 λεπτά",
    keywords="βιώσιμο ελαιόλαδο, πώς να καταλάβω αν το ελαιόλαδο είναι βιώσιμο, βιώσιμη ελαιοκαλλιέργεια, περιβαλλοντικό αποτύπωμα ελαιόλαδου, πιστοποιήσεις ελαιόλαδου",
    kf_label="Με λίγα λόγια",
    intro="Το ελαιόλαδο συχνά πωλείται ως φυσική, υγιεινή επιλογή, όμως η λέξη «βιώσιμο» σε μια ετικέτα σπάνια ορίζεται. Αυτός ο κεντρικός οδηγός είναι η πλήρης, πρακτική απάντηση: τι σημαίνει βιωσιμότητα για το ελαιόλαδο, πώς να την κρίνετε από το μπουκάλι, οι αξιόπιστες πιστοποιήσεις, το πραγματικό περιβαλλοντικό αποτύπωμα και η σύγκριση με άλλα λίπη.",
    key_facts=[
        "Το βιώσιμο ελαιόλαδο ισορροπεί τρεις πυλώνες: περιβαλλοντικό αποτύπωμα, δίκαιες κοινωνικές συνθήκες και μακροπρόθεσμη οικονομική βιωσιμότητα των παραγωγών.",
        "Μπορείτε να κρίνετε τη βιωσιμότητα πριν την αγορά, από συγκεκριμένα σημάδια: αξιόπιστη πιστοποίηση, ιχνηλάσιμη μοναδική προέλευση, ημερομηνία συγκομιδής, αγροτική διαφάνεια, τίμια συσκευασία και ρεαλιστική τιμή.",
        "Ο τρόπος καλλιέργειας κρίνει το αποτύπωμα: οι παραδοσιακοί ξηρικοί ελαιώνες έχουν λίγες εισροές, αποθηκεύουν άνθρακα και έχουν βιοποικιλότητα· οι εντατικοί και υπερεντατικοί αποδίδουν περισσότερο αλλά χρειάζονται περισσότερο νερό και αγροχημικά και προκαλούν διάβρωση.",
        "Το ελαιόλαδο έχει γενικά χαμηλότερο αποτύπωμα άνθρακα και γης από το βούτυρο και πολλά άλλα λίπη, και ένας καλά διαχειριζόμενος ελαιώνας μπορεί να είναι καθαρή δεξαμενή άνθρακα.",
        "Οι πιο αξιόπιστες ετικέτες είναι το βιολογικό (ΕΕ/USDA), η ΠΟΠ/ΠΓΕ (προστατευόμενη προέλευση) και σχήματα τρίτων όπως Rainforest Alliance· «eco», «φυσικό» και «ψυχρής έκθλιψης» δεν εγγυώνται βιωσιμότητα.",
    ],
    toc=[("what", "Τι είναι το βιώσιμο ελαιόλαδο"), ("how", "Πώς να καταλάβετε αν είναι βιώσιμο"),
         ("impact", "Περιβαλλοντικό αποτύπωμα"), ("certifications", "Πιστοποιήσεις και ετικέτες"),
         ("compare", "Σε σχέση με άλλα λίπη"), ("buying", "Αγορά βιώσιμου ελαιόλαδου"),
         ("myths", "Greenwashing προς αποφυγή"), ("faq", "FAQ")],
    sections=[
        ("what", "Τι είναι το βιώσιμο ελαιόλαδο",
         "<p>Η βιωσιμότητα δεν είναι ένα μόνο χαρακτηριστικό αλλά ισορροπία τριών πυλώνων. Ο <strong>περιβαλλοντικός</strong> πυλώνας καλύπτει νερό, ενέργεια και αγροχημικά και την επίδραση σε έδαφος, βιοποικιλότητα και άνθρακα. Ο <strong>κοινωνικός</strong> πυλώνας καλύπτει δίκαιη αμοιβή και ασφαλείς συνθήκες. Ο <strong>οικονομικός</strong> πυλώνας καλύπτει μια τιμή που επιτρέπει στους παραγωγούς να συνεχίσουν χωρίς να υποβαθμίζουν τη γη.</p>"
         "<p>Ένα ελαιόλαδο είναι πραγματικά βιώσιμο όταν είναι καλό και στους τρεις διαχρονικά, όχι όταν λάμπει σε έναν. Γι' αυτό ένας μεμονωμένος ισχυρισμός, «βιολογικό» ή «τοπικό», είναι σημάδι παρά πλήρης απάντηση.</p>"),
        ("how", "Πώς να καταλάβετε αν ένα ελαιόλαδο είναι βιώσιμο",
         "<p>Μπορείτε να αξιολογήσετε τα περισσότερα από την ετικέτα και τον παραγωγό, πριν αγοράσετε. Ακολουθήστε αυτούς τους έξι ελέγχους:</p>"
         "<ol>"
         "<li><strong>Ψάξτε αξιόπιστη πιστοποίηση</strong> — λογότυπο βιολογικού/φύλλο ΕΕ, προέλευση ΠΟΠ/ΠΓΕ ή σχήμα τρίτων, όχι μόνο τη λέξη «eco».</li>"
         "<li><strong>Ελέγξτε ιχνηλάσιμη μοναδική προέλευση</strong> — χώρα, περιοχή, κτήμα ή ελαιοτριβείο, όχι ένα ασαφές «μείγμα ελαιόλαδων ΕΕ και εκτός ΕΕ».</li>"
         "<li><strong>Βρείτε ημερομηνία συγκομιδής</strong> — δείχνει φρεσκάδα και παραγωγό που παρακολουθεί τη σοδειά.</li>"
         "<li><strong>Διαβάστε την αγροτική περιγραφή</strong> — ξηρικοί ή παραδοσιακοί ελαιώνες, φυτοκάλυψη, μειωμένη κατεργασία, αποδοτική στάγδην άρδευση.</li>"
         "<li><strong>Δείτε τη συσκευασία</strong> — σκούρο γυαλί ή τενεκές (προστατεύει το λάδι, μειώνει σπατάλες), ανακυκλώσιμα υλικά.</li>"
         "<li><strong>Ελέγξτε την τιμή</strong> — ένα πραγματικά βιώσιμο έξτρα παρθένο δεν παράγεται στις χαμηλότερες τιμές.</li>"
         "</ol>"
         "<p>Κανένα σημάδι μόνο του δεν είναι απόδειξη. Δύο-τρία μαζί λένε ήδη πολλά· τέσσερα ή περισσότερα δίνουν αξιόπιστη εικόνα.</p>"),
        ("impact", "Το περιβαλλοντικό αποτύπωμα της ελαιοκαλλιέργειας",
         "<p>Το αποτύπωμα εξαρτάται σχεδόν εξ ολοκλήρου από το <em>πώς</em> καλλιεργούνται οι ελιές. Η αντίθεση είναι σαφέστερη ανάμεσα σε παραδοσιακούς ξηρικούς ελαιώνες και σύγχρονες εντατικές φυτεύσεις.</p>"
         "<table><thead><tr><th>Παράγοντας</th><th>Παραδοσιακό / ξηρικό</th><th>Εντατικό / υπερεντατικό</th></tr></thead><tbody>"
         "<tr><td>Νερό</td><td>Λίγο ή καθόλου (βροχή)</td><td>Υψηλό (αρδευόμενο)</td></tr>"
         "<tr><td>Αγροχημικά</td><td>Χαμηλά</td><td>Υψηλότερα (λίπασμα, ζιζανιοκτόνο)</td></tr>"
         "<tr><td>Έδαφος</td><td>Προστατευμένο, σταθερό</td><td>Κίνδυνος διάβρωσης σε γυμνό έδαφος</td></tr>"
         "<tr><td>Βιοποικιλότητα</td><td>Υψηλή (ενδιαίτημα)</td><td>Χαμηλότερη (μονοκαλλιέργεια)</td></tr>"
         "<tr><td>Άνθρακας</td><td>Αποθηκεύει (παλιά δέντρα, έδαφος)</td><td>Περισσότερες εισροές, λιγότερη αποθήκευση</td></tr>"
         "<tr><td>Απόδοση</td><td>Χαμηλότερη ανά εκτάριο</td><td>Πολύ υψηλότερη ανά εκτάριο</td></tr>"
         "</tbody></table>"
         "<p>Οι εντατικοί ελαιώνες δεν είναι αυτομάτως μη βιώσιμοι: φυτοκάλυψη, μειωμένη κατεργασία και αποδοτική στάγδην άρδευση μειώνουν πολύ το αποτύπωμα. Άλλο θέμα, τα <strong>υγρά απόβλητα ελαιοτριβείου</strong>, ρυπογόνα σε ορισμένες περιοχές· τα σύγχρονα διφασικά ελαιοτριβεία τα μειώνουν. Στον άνθρακα, το ελαιόλαδο συγκρίνεται ευνοϊκά με τα ζωικά λίπη.</p>"),
        ("certifications", "Πιστοποιήσεις και ετικέτες",
         "<table><thead><tr><th>Ετικέτα</th><th>Τι εγγυάται</th></tr></thead><tbody>"
         "<tr><td>Βιολογικό ΕΕ / USDA Organic</td><td>Χωρίς συνθετικά φυτοφάρμακα ή λιπάσματα· καλύτερο για έδαφος και νερό, όχι πλήρης έλεγχος.</td></tr>"
         "<tr><td>ΠΟΠ / ΠΓΕ (προστατευόμενη προέλευση)</td><td>Επαληθευμένη προέλευση και παραδοσιακή μέθοδος· ισχυρή ιχνηλασιμότητα.</td></tr>"
         "<tr><td>Rainforest Alliance / παρόμοια</td><td>Έλεγχοι τρίτων σε περιβαλλοντικές και κοινωνικές πρακτικές.</td></tr>"
         "<tr><td>Fair for Life / δίκαιο εμπόριο</td><td>Αμοιβή και συνθήκες εργασίας (κοινωνικός πυλώνας).</td></tr>"
         "<tr><td>Κλιματικά ουδέτερο / B-Corp</td><td>Μεταβλητή αυστηρότητα· δείτε τι μετριέται και επαληθεύεται.</td></tr>"
         "</tbody></table>"
         "<p>Οι πιστοποιήσεις είναι συντόμευση, όχι όλη η ιστορία: ένας μικρός διαφανής παραγωγός χωρίς πληρωμένη πιστοποίηση μπορεί να είναι πολύ βιώσιμος, ενώ μια μεγάλη μάρκα με πράσινο λογότυπο ίσως όχι.</p>"),
        ("compare", "Σε σχέση με άλλα λίπη",
         "<p>Στους περισσότερους δείκτες, το ελαιόλαδο συγκρίνεται ευνοϊκά με τα λίπη που αντικαθιστά. Έχει γενικά χαμηλότερο αποτύπωμα άνθρακα και γης από το <strong>βούτυρο</strong> και τα άλλα ζωικά λίπη, και αποφεύγει τον κίνδυνο αποψίλωσης ορισμένων <strong>φοινικελαίων</strong>. Σε σχέση με σπορέλαια (ηλιέλαιο, κράμβη) η διαφορά είναι μικρότερη και εξαρτάται από μέθοδο και μεταφορά.</p>"
         "<p>Το βασικό: η επιλογή ελαιόλαδου αντί βουτύρου είναι συνήθως χαμηλότερου αποτυπώματος, αλλά <em>ποιο</em> ελαιόλαδο μετράει. Ένα ξηρικό, πιστοποιημένο και ιχνηλάσιμο λάδι και ένα εντατικά αρδευόμενο και ανώνυμο έχουν πολύ διαφορετικά αποτυπώματα.</p>"),
        ("buying", "Αγορά βιώσιμου ελαιόλαδου στην πράξη",
         "<p>Στο κατάστημα ή online, προτιμήστε λάδια που συνδυάζουν πολλά σημάδια: ποιότητα <strong>έξτρα παρθένο</strong>, ετικέτα <strong>βιολογικό ή ΠΟΠ/ΠΓΕ</strong>, <strong>μοναδική προέλευση</strong>, <strong>ημερομηνία συγκομιδής</strong>, σκούρο γυαλί ή τενεκές, και παραγωγό διαφανή για την καλλιέργεια. Ένα μέγεθος που θα τελειώσετε φρέσκο μειώνει τη σπατάλη. Λίγο υψηλότερη τιμή για ιχνηλάσιμο, πιστοποιημένο λάδι συχνά αντανακλά το πραγματικό κόστος.</p>"),
        ("myths", "Greenwashing προς αποφυγή",
         "<ul>"
         "<li><strong>Αόριστες πράσινες λέξεις</strong> — «eco», «φυσικό», «πράσινο» χωρίς πιστοποίηση ή λεπτομέρεια σημαίνουν λίγα.</li>"
         "<li><strong>«Ψυχρής έκθλιψης» ως πράσινο επιχείρημα</strong> — περιγράφει θερμοκρασία, όχι βιωσιμότητα· το γνήσιο έξτρα παρθένο είναι ήδη ψυχρής εκχύλισης.</li>"
         "<li><strong>Κρυμμένη προέλευση πίσω από μια ιστορία</strong> — μια ρομαντική ετικέτα χωρίς χώρα, περιοχή ή ημερομηνία είναι κόκκινη σημαία.</li>"
         "<li><strong>Ένα πράσινο λογότυπο σε εντατική αλυσίδα</strong> — μια πιστοποίηση δεν αντισταθμίζει την έλλειψη ιχνηλασιμότητας.</li>"
         "<li><strong>Η πεποίθηση ότι το «τοπικό» πάντα κερδίζει</strong> — η μεταφορά είναι μέρος του αποτυπώματος· η μέθοδος συχνά μετράει πιο πολύ.</li>"
         "</ul>"),
    ],
    howto_name="Πώς να καταλάβετε αν ένα ελαιόλαδο είναι βιώσιμο",
    howto_desc="Μια μέθοδος έξι βημάτων για την αξιολόγηση της βιωσιμότητας ενός ελαιόλαδου από την ετικέτα και τον παραγωγό, πριν την αγορά.",
    howto_steps=[
        ("Ψάξτε αξιόπιστη πιστοποίηση", "Εντοπίστε λογότυπο βιολογικού/φύλλο ΕΕ, προέλευση ΠΟΠ/ΠΓΕ ή σχήμα τρίτων όπως Rainforest Alliance, όχι μόνο τη λέξη 'eco'."),
        ("Ελέγξτε ιχνηλάσιμη μοναδική προέλευση", "Ψάξτε χώρα, περιοχή, κτήμα ή ελαιοτριβείο, όχι ένα ασαφές μείγμα ελαιόλαδων ΕΕ και εκτός ΕΕ."),
        ("Βρείτε ημερομηνία συγκομιδής", "Δείχνει φρεσκάδα και παραγωγό που παρακολουθεί τη σοδειά, όχι μόνο μια μακρινή ημερομηνία λήξης."),
        ("Διαβάστε την αγροτική περιγραφή", "Ψάξτε ξηρικούς ή παραδοσιακούς ελαιώνες, φυτοκάλυψη, μειωμένη κατεργασία ή αποδοτική στάγδην άρδευση."),
        ("Δείτε τη συσκευασία", "Σκούρο γυαλί ή τενεκές προστατεύει το λάδι και μειώνει σπατάλες· ελέγξτε ανακυκλώσιμα υλικά."),
        ("Ελέγξτε την τιμή", "Ένα πραγματικά βιώσιμο έξτρα παρθένο δεν παράγεται στις χαμηλότερες τιμές."),
    ],
    faq_h="Συχνές ερωτήσεις",
    faqs=[
        ("Πώς καταλαβαίνω αν ένα ελαιόλαδο είναι βιώσιμο;",
         "Αξιολογήστε μπουκάλι και παραγωγό από συγκεκριμένα σημάδια: αξιόπιστη πιστοποίηση (βιολογικό, ΠΟΠ/ΠΓΕ ή σχήμα τρίτων), ιχνηλάσιμη μοναδική προέλευση, ημερομηνία συγκομιδής, αγροτική διαφάνεια (ξηρικοί ή παραδοσιακοί ελαιώνες, εξοικονόμηση νερού) και τίμια ανακυκλώσιμη συσκευασία. Κανένα σημάδι μόνο του δεν είναι απόδειξη, αλλά πολλά μαζί δίνουν αξιόπιστη εικόνα."),
        ("Πώς αναγνωρίζω βιώσιμο ελαιόλαδο στο κατάστημα;",
         "Ψάξτε βιολογική ετικέτα ή προστατευόμενη προέλευση (ΠΟΠ/ΠΓΕ), περιοχή ή κτήμα αντί για ασαφές μείγμα, ημερομηνία συγκομιδής και παραγωγό που περιγράφει την καλλιέργεια. Σκούρο γυαλί ή τενεκές και ρεαλιστική τιμή υποστηρίζουν."),
        ("Τι είναι το βιώσιμο ελαιόλαδο;",
         "Ελαιόλαδο που παράγεται με τρόπο που ισορροπεί περιβαλλοντικό αποτύπωμα (λίγο νερό, υγιές έδαφος, βιοποικιλότητα, χαμηλός άνθρακας), δίκαιες κοινωνικές συνθήκες και οικονομική βιωσιμότητα. Ισορροπία των τριών, όχι ένα χαρακτηριστικό."),
        ("Ποιο είναι το πιο βιώσιμο ελαιόλαδο;",
         "Όχι μια συγκεκριμένη μάρκα, αλλά ένα προφίλ: ένα έξτρα παρθένο από παραδοσιακούς ή ξηρικούς ελαιώνες, πιστοποιημένο (βιολογικό και/ή ΠΟΠ/ΠΓΕ), ιχνηλάσιμο σε μοναδική προέλευση, τίμια συσκευασμένο και τιμολογημένο. Μέθοδος και ιχνηλασιμότητα μετρούν πιο πολύ από ένα λογότυπο."),
        ("Είναι το βιολογικό ελαιόλαδο αυτομάτως βιώσιμο;",
         "Το βιολογικό σημαίνει χωρίς συνθετικά φυτοφάρμακα ή λιπάσματα, που βοηθά έδαφος και νερό, αλλά από μόνο του δεν καλύπτει νερό, βιοποικιλότητα ή κοινωνική δικαιοσύνη. Ισχυρό σημάδι, όχι πλήρης εγγύηση."),
        ("Ποιο είναι το περιβαλλοντικό αποτύπωμα του ελαιόλαδου;",
         "Εξαρτάται από το πώς καλλιεργούνται οι ελιές. Οι παραδοσιακοί ξηρικοί ελαιώνες έχουν μικρό αποτύπωμα και αποθηκεύουν άνθρακα· οι εντατικοί αποδίδουν περισσότερο αλλά χρησιμοποιούν περισσότερο νερό και αγροχημικά. Συνολικά, χαμηλό αποτύπωμα σε σχέση με τα ζωικά λίπη."),
        ("Παραδοσιακοί ή εντατικοί ελαιώνες: ποιοι πιο βιώσιμοι;",
         "Οι παραδοσιακοί ξηρικοί ελαιώνες είναι γενικά πιο βιώσιμοι ανά εκτάριο: λίγες εισροές, βιοποικιλότητα, αποθήκευση άνθρακα. Οι εντατικοί είναι πιο παραγωγικοί αλλά θέλουν περισσότερο νερό και προϊόντα· φυτοκάλυψη, μειωμένη κατεργασία και αποδοτική άρδευση μειώνουν τη διαφορά."),
        ("Είναι το ελαιόλαδο πιο βιώσιμο από άλλα λάδια;",
         "Το ελαιόλαδο έχει γενικά χαμηλότερο αποτύπωμα άνθρακα και γης από το βούτυρο και αποφεύγει τον κίνδυνο αποψίλωσης ορισμένων φοινικελαίων. Σε σχέση με σπορέλαια είναι πιο κοντά και εξαρτάται από καλλιέργεια και μεταφορά. Η επιλογή ελαιόλαδου αντί βουτύρου είναι συνήθως χαμηλότερου αποτυπώματος, αλλά ποιο λάδι μετράει."),
    ],
)

if __name__ == "__main__":
    print("Sustainability pillar:")
    build(C)

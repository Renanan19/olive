# -*- coding: utf-8 -*-
"""GEO flagship: rewrite blog/oleiculture-durable-{lang} into the definitive,
citable "sustainable olive oil" guide. Bing AI cites the site most for this topic
(244 citations, 30-44% share). Structured for AI extraction. x4 languages."""
from guide_render import write_guide_cluster

S = {}

S["en"] = dict(
    crumb1="Blog",
    title="Sustainable Olive Oil: how to identify it, certifications and environmental impact",
    desc="How to determine if olive oil is sustainable: a clear definition, a buyer's checklist, the key certifications (organic, PDO, Rainforest Alliance), and the real environmental impact of olive farming.",
    h1="Sustainable Olive Oil: how to identify it",
    lede="What makes an olive oil genuinely sustainable, how to tell from the bottle, which certifications actually mean something, and the environmental impact of how olives are grown.",
    section="sustainability", datePublished="2026-05-04", disclaimer=None,
    keywords="sustainable olive oil, how to determine if olive oil is sustainable, how to identify sustainable olive oil, olive oil environmental impact, olive oil certifications, organic olive oil sustainability",
    intro="\"Sustainable\" is on many olive oil labels, but it is rarely defined. This guide gives a practical answer: what sustainability means for olive oil, how to determine it as a buyer, which certifications to trust, and how olive farming actually affects water, soil, biodiversity and carbon.",
    key_facts=[
        "Sustainable olive oil balances three things: environmental impact (water, soil, biodiversity, carbon), social conditions (fair labour), and long-term economic viability for growers.",
        "You can determine sustainability from the bottle using concrete signals: credible certification, traceable single origin, a harvest date, and transparency about farming practices.",
        "Traditional rainfed olive groves are generally the most sustainable: low input, carbon-storing, biodiversity-rich. Intensive and super-high-density groves yield more but use more water and agrochemicals and drive soil erosion.",
        "Olive oil has a relatively low carbon footprint compared with animal fats, and well-managed olive groves can act as a net carbon sink.",
        "The most useful certifications are EU/USDA organic, PDO/PGI (protected origin), and third-party schemes such as Rainforest Alliance; 'carbon-neutral' claims vary in rigour.",
    ],
    sections=[
        ("What makes olive oil sustainable",
         "<p>Sustainability is not a single feature but a balance of three dimensions. <strong>Environmental</strong>: how much water, energy and agrochemicals the grove uses, and its effect on soil, biodiversity and carbon. <strong>Social</strong>: fair pay and safe conditions for pickers and mill workers. <strong>Economic</strong>: whether the price lets growers keep farming without degrading the land. An olive oil is sustainable when it scores well across all three, not just one.</p>"),
        ("How to determine if an olive oil is sustainable",
         "<p>You can assess most of this from the label and the producer, before you buy:</p>"
         "<ul>"
         "<li><strong>Credible certification</strong> — an organic leaf/USDA seal, PDO/PGI origin, or a third-party scheme (see the table below), not just the word \"eco\".</li>"
         "<li><strong>Traceable single origin</strong> — a named country, region, estate or mill, rather than a vague \"blend of EU and non-EU oils\".</li>"
         "<li><strong>A harvest date</strong> — shows freshness and a producer who tracks their crop, not only a distant best-before date.</li>"
         "<li><strong>Farming transparency</strong> — the producer describes rainfed or traditional groves, cover crops, reduced tillage, or water-saving irrigation.</li>"
         "<li><strong>Honest packaging</strong> — dark glass or tin (protects the oil, reduces waste from spoilage); recyclable materials.</li>"
         "<li><strong>Realistic price</strong> — genuinely sustainable, extra virgin oil cannot be produced at the lowest supermarket prices.</li>"
         "</ul>"
         "<p>No single signal is proof; together they build a reliable picture.</p>"),
        ("The environmental impact of olive farming",
         "<p>The impact depends almost entirely on <em>how</em> the olives are grown.</p>"
         "<p><strong>Traditional and rainfed groves</strong> use little or no irrigation, host wildlife between the trees, and store carbon in old trees and undisturbed soil. Yields are lower, but the footprint is small.</p>"
         "<p><strong>Intensive and super-high-density (SHD) groves</strong> produce far more oil per hectare with mechanical harvesting, but rely on more irrigation, fertiliser and herbicide. Their main risks are <strong>soil erosion</strong> on bare ground, loss of biodiversity, and pressure on scarce Mediterranean water. Cover crops, reduced tillage and efficient drip irrigation can lower these impacts substantially.</p>"
         "<p>On carbon, olive oil compares well with butter and other animal fats, and a well-managed grove can absorb more carbon than its production emits.</p>"),
        ("Certifications and labels to look for",
         "<table><thead><tr><th>Label</th><th>What it guarantees</th></tr></thead><tbody>"
         "<tr><td>EU organic / USDA Organic</td><td>No synthetic pesticides or fertilisers; better for soil and water, though not a full sustainability audit.</td></tr>"
         "<tr><td>PDO / PGI (protected origin)</td><td>Verified origin and traditional method tied to a specific region; strong traceability.</td></tr>"
         "<tr><td>Rainforest Alliance / similar</td><td>Third-party checks on environmental and social practices across the farm.</td></tr>"
         "<tr><td>Fair for Life / fair-trade</td><td>Focus on fair pay and working conditions (the social pillar).</td></tr>"
         "<tr><td>Carbon-neutral / B-Corp</td><td>Varies in rigour; read what is actually measured and verified.</td></tr>"
         "</tbody></table>"
         "<p>Certifications are a shortcut, not the whole story: a small transparent producer without paid certification can still be highly sustainable.</p>"),
        ("Sourcing and traceability",
         "<p>The clearest sign of a serious producer is traceability: a single origin, a named estate or mill, the olive variety, and the harvest year. Short, transparent supply chains make it possible to verify farming and labour practices. Vague \"Mediterranean blend\" oils with no origin or date make sustainability impossible to check.</p>"),
    ],
    faqs=[
        ("How do you determine if olive oil is sustainable?",
         "Check the bottle and the producer for concrete signals: a credible certification (organic, PDO/PGI, or a third-party scheme), a traceable single origin, a harvest date, transparency about farming practices (rainfed or traditional groves, water saving), and honest recyclable packaging. No single signal is proof, but together they give a reliable picture."),
        ("How can you identify sustainable olive oil in a shop?",
         "Look for an organic or protected-origin (PDO/PGI) label, a named region or estate rather than a vague blend, a harvest date, and a producer who describes their farming. Dark glass or tin and a realistic price are supporting signs. Avoid oils with no origin, no date and only marketing words like 'eco' or 'natural'."),
        ("What is sustainable olive oil?",
         "Olive oil produced in a way that balances environmental impact (low water, healthy soil, biodiversity, low carbon), fair social conditions for workers, and long-term economic viability for growers. It is a balance of all three, not a single feature."),
        ("Is organic olive oil automatically sustainable?",
         "Organic certification means no synthetic pesticides or fertilisers, which helps soil and water, but it does not by itself cover water use, biodiversity or fair labour. Organic is a strong signal of sustainability, not a complete guarantee of it."),
        ("What is the environmental impact of olive oil?",
         "It depends on how the olives are grown. Traditional rainfed groves have a small footprint and store carbon; intensive and super-high-density groves yield more but use more water and agrochemicals and can cause soil erosion and biodiversity loss. Overall, olive oil has a relatively low carbon footprint compared with animal fats."),
        ("Are traditional or intensive olive groves more sustainable?",
         "Traditional rainfed groves are generally more sustainable per hectare: low input, biodiversity-rich and carbon-storing. Intensive groves are more productive but need more water and chemicals; practices like cover crops, reduced tillage and efficient irrigation can narrow the gap."),
    ],
)
S["fr"] = dict(
    crumb1="Blog",
    title="Huile d'olive durable : comment la reconnaître, certifications et impact environnemental",
    desc="Comment savoir si une huile d'olive est durable : définition claire, check-list d'achat, certifications clés (bio, AOP, Rainforest Alliance) et véritable impact environnemental de l'oléiculture.",
    h1="Huile d'olive durable : comment la reconnaître",
    lede="Ce qui rend une huile d'olive vraiment durable, comment le voir sur la bouteille, quelles certifications ont un sens, et l'impact environnemental de la façon dont les olives sont cultivées.",
    section="sustainability", datePublished="2026-05-04", disclaimer=None,
    keywords="huile d'olive durable, comment savoir si huile d'olive est durable, oléiculture durable, impact environnemental huile d'olive, certifications huile d'olive, huile d'olive bio durable",
    intro="« Durable » figure sur beaucoup d'étiquettes, mais c'est rarement défini. Ce guide donne une réponse concrète : ce que signifie la durabilité pour l'huile d'olive, comment la déterminer en tant qu'acheteur, quelles certifications croire, et comment l'oléiculture affecte réellement l'eau, le sol, la biodiversité et le carbone.",
    key_facts=[
        "Une huile d'olive durable équilibre trois choses : l'impact environnemental (eau, sol, biodiversité, carbone), les conditions sociales (travail équitable) et la viabilité économique des producteurs.",
        "On peut évaluer la durabilité depuis la bouteille grâce à des signaux concrets : certification crédible, origine unique traçable, date de récolte et transparence sur les pratiques agricoles.",
        "Les oliveraies traditionnelles en sec sont généralement les plus durables : peu d'intrants, stockage de carbone, biodiversité. Les vergers intensifs et super-intensifs produisent plus mais consomment plus d'eau et d'intrants et favorisent l'érosion des sols.",
        "L'huile d'olive a une empreinte carbone faible par rapport aux graisses animales, et une oliveraie bien gérée peut être un puits de carbone net.",
        "Les certifications les plus utiles sont le bio (UE/USDA), l'AOP/IGP (origine protégée) et des labels tiers comme Rainforest Alliance ; les allégations « neutre en carbone » varient en rigueur.",
    ],
    sections=[
        ("Ce qui rend une huile d'olive durable",
         "<p>La durabilité n'est pas une caractéristique unique mais un équilibre entre trois dimensions. <strong>Environnementale</strong> : l'eau, l'énergie et les intrants utilisés, et l'effet sur le sol, la biodiversité et le carbone. <strong>Sociale</strong> : rémunération juste et conditions sûres pour les cueilleurs et le moulin. <strong>Économique</strong> : un prix qui permet aux producteurs de continuer sans dégrader la terre. Une huile est durable quand elle est bonne sur les trois, pas sur une seule.</p>"),
        ("Comment savoir si une huile d'olive est durable",
         "<p>On peut évaluer l'essentiel depuis l'étiquette et le producteur, avant l'achat :</p>"
         "<ul>"
         "<li><strong>Une certification crédible</strong> — logo bio/feuille européenne, origine AOP/IGP, ou un label tiers (voir le tableau), pas seulement le mot « éco ».</li>"
         "<li><strong>Une origine unique traçable</strong> — un pays, une région, un domaine ou un moulin nommés, plutôt qu'un vague « mélange d'huiles UE et non UE ».</li>"
         "<li><strong>Une date de récolte</strong> — signe de fraîcheur et d'un producteur qui suit sa récolte, pas seulement une DDM lointaine.</li>"
         "<li><strong>La transparence agricole</strong> — le producteur décrit des oliveraies en sec ou traditionnelles, des couverts végétaux, un travail du sol réduit, une irrigation économe.</li>"
         "<li><strong>Un emballage honnête</strong> — verre foncé ou bidon (protège l'huile, limite le gaspillage), matériaux recyclables.</li>"
         "<li><strong>Un prix réaliste</strong> — une huile extra vierge vraiment durable ne peut pas être produite aux prix les plus bas.</li>"
         "</ul>"
         "<p>Aucun signal seul n'est une preuve ; ensemble, ils dressent un tableau fiable.</p>"),
        ("L'impact environnemental de l'oléiculture",
         "<p>L'impact dépend presque entièrement de la <em>façon</em> dont les olives sont cultivées.</p>"
         "<p>Les <strong>oliveraies traditionnelles et en sec</strong> utilisent peu ou pas d'irrigation, abritent une faune entre les arbres et stockent du carbone dans les vieux arbres et un sol non perturbé. Les rendements sont plus faibles, mais l'empreinte est réduite.</p>"
         "<p>Les <strong>vergers intensifs et super-intensifs</strong> produisent bien plus d'huile par hectare avec une récolte mécanique, mais reposent sur plus d'irrigation, d'engrais et d'herbicides. Leurs risques principaux : l'<strong>érosion des sols</strong> à nu, la perte de biodiversité et la pression sur l'eau méditerranéenne. Couverts végétaux, travail du sol réduit et goutte-à-goutte efficace réduisent nettement ces impacts.</p>"
         "<p>Côté carbone, l'huile d'olive se compare avantageusement au beurre et aux graisses animales, et une oliveraie bien gérée peut absorber plus de carbone qu'elle n'en émet.</p>"),
        ("Certifications et labels à rechercher",
         "<table><thead><tr><th>Label</th><th>Ce qu'il garantit</th></tr></thead><tbody>"
         "<tr><td>Bio UE / USDA Organic</td><td>Pas de pesticides ni d'engrais de synthèse ; meilleur pour le sol et l'eau, sans être un audit complet de durabilité.</td></tr>"
         "<tr><td>AOP / IGP (origine protégée)</td><td>Origine et méthode traditionnelle vérifiées, liées à une région précise ; forte traçabilité.</td></tr>"
         "<tr><td>Rainforest Alliance / similaire</td><td>Contrôles tiers sur les pratiques environnementales et sociales de l'exploitation.</td></tr>"
         "<tr><td>Fair for Life / commerce équitable</td><td>Axé sur la rémunération et les conditions de travail (le pilier social).</td></tr>"
         "<tr><td>Neutre en carbone / B-Corp</td><td>Rigueur variable ; regardez ce qui est réellement mesuré et vérifié.</td></tr>"
         "</tbody></table>"
         "<p>Les certifications sont un raccourci, pas toute l'histoire : un petit producteur transparent sans certification payante peut être très durable.</p>"),
        ("Approvisionnement et traçabilité",
         "<p>Le signe le plus clair d'un producteur sérieux est la traçabilité : une origine unique, un domaine ou un moulin nommés, la variété d'olive et l'année de récolte. Des filières courtes et transparentes permettent de vérifier les pratiques agricoles et sociales. Les huiles « mélange méditerranéen » sans origine ni date rendent la durabilité invérifiable.</p>"),
    ],
    faqs=[
        ("Comment savoir si une huile d'olive est durable ?",
         "Vérifiez sur la bouteille et chez le producteur des signaux concrets : une certification crédible (bio, AOP/IGP ou label tiers), une origine unique traçable, une date de récolte, la transparence sur les pratiques agricoles (oliveraies en sec ou traditionnelles, économie d'eau) et un emballage honnête et recyclable. Aucun signal seul n'est une preuve, mais ensemble ils donnent un tableau fiable."),
        ("Comment reconnaître une huile d'olive durable en magasin ?",
         "Cherchez un label bio ou une origine protégée (AOP/IGP), une région ou un domaine nommés plutôt qu'un mélange vague, une date de récolte, et un producteur qui décrit sa culture. Verre foncé ou bidon et un prix réaliste sont des signes d'appui. Évitez les huiles sans origine, sans date et avec seulement des mots comme « éco » ou « naturel »."),
        ("Qu'est-ce qu'une huile d'olive durable ?",
         "Une huile produite d'une manière qui équilibre l'impact environnemental (peu d'eau, sol sain, biodiversité, faible carbone), des conditions sociales justes et la viabilité économique des producteurs. C'est un équilibre des trois, pas une seule caractéristique."),
        ("L'huile d'olive bio est-elle automatiquement durable ?",
         "Le bio signifie pas de pesticides ni d'engrais de synthèse, ce qui aide le sol et l'eau, mais ne couvre pas à lui seul la consommation d'eau, la biodiversité ou l'équité sociale. Le bio est un signal fort de durabilité, pas une garantie complète."),
        ("Quel est l'impact environnemental de l'huile d'olive ?",
         "Il dépend de la façon dont les olives sont cultivées. Les oliveraies traditionnelles en sec ont une faible empreinte et stockent du carbone ; les vergers intensifs et super-intensifs produisent plus mais consomment plus d'eau et d'intrants et peuvent causer érosion et perte de biodiversité. Globalement, l'huile d'olive a une empreinte carbone faible face aux graisses animales."),
        ("Oliveraies traditionnelles ou intensives : lesquelles sont plus durables ?",
         "Les oliveraies traditionnelles en sec sont généralement plus durables par hectare : peu d'intrants, riches en biodiversité et stockant du carbone. Les vergers intensifs sont plus productifs mais demandent plus d'eau et de produits ; couverts végétaux, travail du sol réduit et irrigation efficace réduisent l'écart."),
    ],
)
S["it"] = dict(
    crumb1="Blog",
    title="Olio d'oliva sostenibile: come riconoscerlo, certificazioni e impatto ambientale",
    desc="Come capire se un olio d'oliva è sostenibile: definizione chiara, checklist d'acquisto, certificazioni chiave (bio, DOP, Rainforest Alliance) e reale impatto ambientale dell'olivicoltura.",
    h1="Olio d'oliva sostenibile: come riconoscerlo",
    lede="Cosa rende un olio d'oliva davvero sostenibile, come capirlo dalla bottiglia, quali certificazioni contano e l'impatto ambientale di come si coltivano le olive.",
    section="sustainability", datePublished="2026-05-04", disclaimer=None,
    keywords="olio d'oliva sostenibile, come capire se olio d'oliva è sostenibile, olivicoltura sostenibile, impatto ambientale olio d'oliva, certificazioni olio d'oliva, olio d'oliva bio sostenibile",
    intro="\"Sostenibile\" è su molte etichette, ma raramente è definito. Questa guida dà una risposta concreta: cosa significa sostenibilità per l'olio d'oliva, come valutarla da acquirente, quali certificazioni fidarsi e come l'olivicoltura incide su acqua, suolo, biodiversità e carbonio.",
    key_facts=[
        "Un olio d'oliva sostenibile bilancia tre cose: impatto ambientale (acqua, suolo, biodiversità, carbonio), condizioni sociali (lavoro equo) e sostenibilità economica per i produttori.",
        "Puoi valutare la sostenibilità dalla bottiglia con segnali concreti: certificazione credibile, origine unica tracciabile, data di raccolta e trasparenza sulle pratiche agricole.",
        "Gli oliveti tradizionali in asciutto sono in genere i più sostenibili: pochi input, stoccaggio di carbonio, biodiversità. Gli oliveti intensivi e superintensivi rendono di più ma usano più acqua e agrofarmaci e favoriscono l'erosione del suolo.",
        "L'olio d'oliva ha un'impronta di carbonio bassa rispetto ai grassi animali, e un oliveto ben gestito può essere un pozzo di carbonio netto.",
        "Le certificazioni più utili sono il bio (UE/USDA), la DOP/IGP (origine protetta) e schemi terzi come Rainforest Alliance; le dichiarazioni \"carbon neutral\" variano in rigore.",
    ],
    sections=[
        ("Cosa rende sostenibile un olio d'oliva",
         "<p>La sostenibilità non è una singola caratteristica ma un equilibrio tra tre dimensioni. <strong>Ambientale</strong>: acqua, energia e agrofarmaci usati, ed effetto su suolo, biodiversità e carbonio. <strong>Sociale</strong>: paga equa e condizioni sicure per raccoglitori e frantoio. <strong>Economica</strong>: un prezzo che permetta ai produttori di continuare senza degradare la terra. Un olio è sostenibile quando va bene su tutte e tre.</p>"),
        ("Come capire se un olio d'oliva è sostenibile",
         "<p>Puoi valutare gran parte dall'etichetta e dal produttore, prima di comprare:</p>"
         "<ul>"
         "<li><strong>Una certificazione credibile</strong> — logo bio/foglia UE, origine DOP/IGP o uno schema terzo (vedi tabella), non solo la parola \"eco\".</li>"
         "<li><strong>Un'origine unica tracciabile</strong> — un paese, una regione, un'azienda o un frantoio indicati, non un vago \"miscela di oli UE e non UE\".</li>"
         "<li><strong>Una data di raccolta</strong> — indica freschezza e un produttore che segue il raccolto, non solo un TMC lontano.</li>"
         "<li><strong>Trasparenza agricola</strong> — il produttore descrive oliveti in asciutto o tradizionali, inerbimento, lavorazione ridotta, irrigazione efficiente.</li>"
         "<li><strong>Confezione onesta</strong> — vetro scuro o latta (protegge l'olio, riduce gli sprechi), materiali riciclabili.</li>"
         "<li><strong>Un prezzo realistico</strong> — un extravergine davvero sostenibile non si produce ai prezzi più bassi.</li>"
         "</ul>"
         "<p>Nessun segnale da solo è una prova; insieme danno un quadro affidabile.</p>"),
        ("L'impatto ambientale dell'olivicoltura",
         "<p>L'impatto dipende quasi interamente da <em>come</em> si coltivano le olive.</p>"
         "<p>Gli <strong>oliveti tradizionali e in asciutto</strong> usano poca o nessuna irrigazione, ospitano fauna tra gli alberi e immagazzinano carbonio in alberi vecchi e suolo indisturbato. Le rese sono minori, ma l'impronta è piccola.</p>"
         "<p>Gli <strong>oliveti intensivi e superintensivi</strong> producono molto più olio per ettaro con raccolta meccanica, ma dipendono da più irrigazione, fertilizzanti ed erbicidi. I rischi principali: <strong>erosione del suolo</strong> nudo, perdita di biodiversità e pressione sull'acqua mediterranea. Inerbimento, lavorazione ridotta e goccia a goccia efficiente riducono molto questi impatti.</p>"
         "<p>Sul carbonio, l'olio d'oliva regge bene il confronto con burro e grassi animali, e un oliveto ben gestito può assorbire più carbonio di quanto ne emetta.</p>"),
        ("Certificazioni ed etichette da cercare",
         "<table><thead><tr><th>Etichetta</th><th>Cosa garantisce</th></tr></thead><tbody>"
         "<tr><td>Bio UE / USDA Organic</td><td>Niente pesticidi o fertilizzanti sintetici; meglio per suolo e acqua, ma non un audit completo di sostenibilità.</td></tr>"
         "<tr><td>DOP / IGP (origine protetta)</td><td>Origine e metodo tradizionale verificati, legati a una regione; forte tracciabilità.</td></tr>"
         "<tr><td>Rainforest Alliance / simili</td><td>Controlli terzi su pratiche ambientali e sociali dell'azienda.</td></tr>"
         "<tr><td>Fair for Life / commercio equo</td><td>Focus su paga e condizioni di lavoro (il pilastro sociale).</td></tr>"
         "<tr><td>Carbon neutral / B-Corp</td><td>Rigore variabile; leggi cosa viene davvero misurato e verificato.</td></tr>"
         "</tbody></table>"
         "<p>Le certificazioni sono una scorciatoia, non tutta la storia: un piccolo produttore trasparente senza certificazione a pagamento può essere molto sostenibile.</p>"),
        ("Approvvigionamento e tracciabilità",
         "<p>Il segno più chiaro di un produttore serio è la tracciabilità: un'origine unica, un'azienda o un frantoio indicati, la varietà di oliva e l'anno di raccolta. Filiere corte e trasparenti permettono di verificare pratiche agricole e sociali. Gli oli \"miscela mediterranea\" senza origine né data rendono la sostenibilità non verificabile.</p>"),
    ],
    faqs=[
        ("Come capire se un olio d'oliva è sostenibile?",
         "Controlla su bottiglia e produttore segnali concreti: una certificazione credibile (bio, DOP/IGP o schema terzo), un'origine unica tracciabile, una data di raccolta, trasparenza sulle pratiche agricole (oliveti in asciutto o tradizionali, risparmio idrico) e una confezione onesta e riciclabile. Nessun segnale da solo è prova, ma insieme danno un quadro affidabile."),
        ("Come riconoscere un olio d'oliva sostenibile al supermercato?",
         "Cerca un'etichetta bio o un'origine protetta (DOP/IGP), una regione o azienda indicata invece di una miscela vaga, una data di raccolta e un produttore che descrive la coltivazione. Vetro scuro o latta e un prezzo realistico sono segnali di supporto. Evita oli senza origine, senza data e con sole parole come \"eco\" o \"naturale\"."),
        ("Cos'è l'olio d'oliva sostenibile?",
         "Olio prodotto in modo da bilanciare impatto ambientale (poca acqua, suolo sano, biodiversità, basso carbonio), condizioni sociali eque e sostenibilità economica per i produttori. È un equilibrio dei tre, non una singola caratteristica."),
        ("L'olio d'oliva bio è automaticamente sostenibile?",
         "Il bio significa niente pesticidi o fertilizzanti sintetici, il che aiuta suolo e acqua, ma da solo non copre uso d'acqua, biodiversità o equità sociale. Il bio è un forte segnale di sostenibilità, non una garanzia completa."),
        ("Qual è l'impatto ambientale dell'olio d'oliva?",
         "Dipende da come si coltivano le olive. Gli oliveti tradizionali in asciutto hanno un'impronta piccola e immagazzinano carbonio; quelli intensivi e superintensivi rendono di più ma usano più acqua e agrofarmaci e possono causare erosione e perdita di biodiversità. In generale, l'olio d'oliva ha un'impronta di carbonio bassa rispetto ai grassi animali."),
        ("Oliveti tradizionali o intensivi: quali più sostenibili?",
         "Gli oliveti tradizionali in asciutto sono in genere più sostenibili per ettaro: pochi input, ricchi di biodiversità e capaci di immagazzinare carbonio. Quelli intensivi sono più produttivi ma richiedono più acqua e prodotti; inerbimento, lavorazione ridotta e irrigazione efficiente riducono il divario."),
    ],
)
S["el"] = dict(
    crumb1="Ιστολόγιο",
    title="Βιώσιμο ελαιόλαδο: πώς να το αναγνωρίσετε, πιστοποιήσεις και περιβαλλοντικό αποτύπωμα",
    desc="Πώς να καταλάβετε αν ένα ελαιόλαδο είναι βιώσιμο: σαφής ορισμός, λίστα ελέγχου αγοράς, βασικές πιστοποιήσεις (βιολογικό, ΠΟΠ, Rainforest Alliance) και το πραγματικό περιβαλλοντικό αποτύπωμα της ελαιοκαλλιέργειας.",
    h1="Βιώσιμο ελαιόλαδο: πώς να το αναγνωρίσετε",
    lede="Τι κάνει ένα ελαιόλαδο πραγματικά βιώσιμο, πώς φαίνεται από το μπουκάλι, ποιες πιστοποιήσεις έχουν σημασία και το περιβαλλοντικό αποτύπωμα του τρόπου καλλιέργειας.",
    section="sustainability", datePublished="2026-05-04", disclaimer=None,
    keywords="βιώσιμο ελαιόλαδο, πώς να καταλάβω αν το ελαιόλαδο είναι βιώσιμο, βιώσιμη ελαιοκαλλιέργεια, περιβαλλοντικό αποτύπωμα ελαιόλαδου, πιστοποιήσεις ελαιόλαδου",
    intro="Το «βιώσιμο» υπάρχει σε πολλές ετικέτες, αλλά σπάνια ορίζεται. Ο οδηγός δίνει συγκεκριμένη απάντηση: τι σημαίνει βιωσιμότητα για το ελαιόλαδο, πώς να την κρίνετε ως αγοραστής, ποιες πιστοποιήσεις να εμπιστευτείτε και πώς η ελαιοκαλλιέργεια επηρεάζει νερό, έδαφος, βιοποικιλότητα και άνθρακα.",
    key_facts=[
        "Το βιώσιμο ελαιόλαδο ισορροπεί τρία: περιβαλλοντικό αποτύπωμα (νερό, έδαφος, βιοποικιλότητα, άνθρακας), κοινωνικές συνθήκες (δίκαιη εργασία) και οικονομική βιωσιμότητα για τους παραγωγούς.",
        "Μπορείτε να κρίνετε τη βιωσιμότητα από το μπουκάλι με συγκεκριμένα σημάδια: αξιόπιστη πιστοποίηση, ιχνηλάσιμη μοναδική προέλευση, ημερομηνία συγκομιδής και διαφάνεια στις πρακτικές.",
        "Οι παραδοσιακοί ξηρικοί ελαιώνες είναι γενικά οι πιο βιώσιμοι: λίγες εισροές, αποθήκευση άνθρακα, βιοποικιλότητα. Οι εντατικοί και υπερεντατικοί αποδίδουν περισσότερο αλλά χρησιμοποιούν περισσότερο νερό και αγροχημικά και προκαλούν διάβρωση.",
        "Το ελαιόλαδο έχει χαμηλό αποτύπωμα άνθρακα σε σχέση με τα ζωικά λίπη, και ένας καλά διαχειριζόμενος ελαιώνας μπορεί να είναι καθαρή δεξαμενή άνθρακα.",
        "Οι πιο χρήσιμες πιστοποιήσεις είναι το βιολογικό (ΕΕ/USDA), η ΠΟΠ/ΠΓΕ (προστατευόμενη προέλευση) και σχήματα τρίτων όπως Rainforest Alliance· οι ισχυρισμοί «κλιματικά ουδέτερο» ποικίλλουν.",
    ],
    sections=[
        ("Τι κάνει βιώσιμο ένα ελαιόλαδο",
         "<p>Η βιωσιμότητα δεν είναι ένα μόνο χαρακτηριστικό αλλά ισορροπία τριών διαστάσεων. <strong>Περιβαλλοντική</strong>: νερό, ενέργεια και αγροχημικά, και η επίδραση σε έδαφος, βιοποικιλότητα και άνθρακα. <strong>Κοινωνική</strong>: δίκαιη αμοιβή και ασφαλείς συνθήκες για συλλέκτες και ελαιοτριβείο. <strong>Οικονομική</strong>: τιμή που επιτρέπει στους παραγωγούς να συνεχίσουν χωρίς να υποβαθμίζουν τη γη. Ένα ελαιόλαδο είναι βιώσιμο όταν είναι καλό και στα τρία.</p>"),
        ("Πώς να καταλάβετε αν ένα ελαιόλαδο είναι βιώσιμο",
         "<p>Μπορείτε να αξιολογήσετε τα περισσότερα από την ετικέτα και τον παραγωγό, πριν αγοράσετε:</p>"
         "<ul>"
         "<li><strong>Αξιόπιστη πιστοποίηση</strong> — λογότυπο βιολογικού/φύλλο ΕΕ, προέλευση ΠΟΠ/ΠΓΕ ή σχήμα τρίτων (δείτε πίνακα), όχι μόνο τη λέξη «eco».</li>"
         "<li><strong>Ιχνηλάσιμη μοναδική προέλευση</strong> — χώρα, περιοχή, κτήμα ή ελαιοτριβείο, όχι ένα ασαφές «μείγμα ελαιόλαδων ΕΕ και εκτός ΕΕ».</li>"
         "<li><strong>Ημερομηνία συγκομιδής</strong> — δείχνει φρεσκάδα και παραγωγό που παρακολουθεί τη σοδειά.</li>"
         "<li><strong>Αγροτική διαφάνεια</strong> — ο παραγωγός περιγράφει ξηρικούς ή παραδοσιακούς ελαιώνες, φυτοκάλυψη, μειωμένη κατεργασία, αποδοτική άρδευση.</li>"
         "<li><strong>Τίμια συσκευασία</strong> — σκούρο γυαλί ή τενεκές (προστατεύει το λάδι), ανακυκλώσιμα υλικά.</li>"
         "<li><strong>Ρεαλιστική τιμή</strong> — ένα πραγματικά βιώσιμο έξτρα παρθένο δεν παράγεται στις χαμηλότερες τιμές.</li>"
         "</ul>"
         "<p>Κανένα σημάδι μόνο του δεν είναι απόδειξη· μαζί δίνουν αξιόπιστη εικόνα.</p>"),
        ("Το περιβαλλοντικό αποτύπωμα της ελαιοκαλλιέργειας",
         "<p>Το αποτύπωμα εξαρτάται σχεδόν εξ ολοκλήρου από το <em>πώς</em> καλλιεργούνται οι ελιές.</p>"
         "<p>Οι <strong>παραδοσιακοί και ξηρικοί ελαιώνες</strong> χρησιμοποιούν λίγη ή καθόλου άρδευση, φιλοξενούν άγρια ζωή και αποθηκεύουν άνθρακα σε παλιά δέντρα και αδιατάρακτο έδαφος. Οι αποδόσεις είναι μικρότερες, αλλά το αποτύπωμα μικρό.</p>"
         "<p>Οι <strong>εντατικοί και υπερεντατικοί ελαιώνες</strong> παράγουν πολύ περισσότερο λάδι ανά εκτάριο με μηχανική συγκομιδή, αλλά βασίζονται σε περισσότερη άρδευση, λιπάσματα και ζιζανιοκτόνα. Κύριοι κίνδυνοι: <strong>διάβρωση εδάφους</strong>, απώλεια βιοποικιλότητας και πίεση στο μεσογειακό νερό. Φυτοκάλυψη, μειωμένη κατεργασία και αποδοτική στάγδην άρδευση μειώνουν σημαντικά αυτές τις επιπτώσεις.</p>"
         "<p>Ως προς τον άνθρακα, το ελαιόλαδο συγκρίνεται ευνοϊκά με το βούτυρο και τα ζωικά λίπη.</p>"),
        ("Πιστοποιήσεις και ετικέτες",
         "<table><thead><tr><th>Ετικέτα</th><th>Τι εγγυάται</th></tr></thead><tbody>"
         "<tr><td>Βιολογικό ΕΕ / USDA Organic</td><td>Χωρίς συνθετικά φυτοφάρμακα ή λιπάσματα· καλύτερο για έδαφος και νερό, αλλά όχι πλήρης έλεγχος βιωσιμότητας.</td></tr>"
         "<tr><td>ΠΟΠ / ΠΓΕ (προστατευόμενη προέλευση)</td><td>Επαληθευμένη προέλευση και παραδοσιακή μέθοδος· ισχυρή ιχνηλασιμότητα.</td></tr>"
         "<tr><td>Rainforest Alliance / παρόμοια</td><td>Έλεγχοι τρίτων σε περιβαλλοντικές και κοινωνικές πρακτικές.</td></tr>"
         "<tr><td>Fair for Life / δίκαιο εμπόριο</td><td>Έμφαση στην αμοιβή και τις συνθήκες εργασίας (κοινωνικός πυλώνας).</td></tr>"
         "<tr><td>Κλιματικά ουδέτερο / B-Corp</td><td>Μεταβλητή αυστηρότητα· δείτε τι μετριέται και επαληθεύεται.</td></tr>"
         "</tbody></table>"
         "<p>Οι πιστοποιήσεις είναι συντόμευση, όχι όλη η ιστορία: ένας μικρός διαφανής παραγωγός χωρίς πληρωμένη πιστοποίηση μπορεί να είναι πολύ βιώσιμος.</p>"),
        ("Προμήθεια και ιχνηλασιμότητα",
         "<p>Το σαφέστερο σημάδι σοβαρού παραγωγού είναι η ιχνηλασιμότητα: μοναδική προέλευση, κτήμα ή ελαιοτριβείο, ποικιλία ελιάς και έτος συγκομιδής. Σύντομες, διαφανείς αλυσίδες επιτρέπουν την επαλήθευση. Τα «μεσογειακά μείγματα» χωρίς προέλευση ή ημερομηνία κάνουν τη βιωσιμότητα μη επαληθεύσιμη.</p>"),
    ],
    faqs=[
        ("Πώς καταλαβαίνω αν ένα ελαιόλαδο είναι βιώσιμο;",
         "Ελέγξτε στο μπουκάλι και τον παραγωγό συγκεκριμένα σημάδια: αξιόπιστη πιστοποίηση (βιολογικό, ΠΟΠ/ΠΓΕ ή σχήμα τρίτων), ιχνηλάσιμη μοναδική προέλευση, ημερομηνία συγκομιδής, διαφάνεια στις πρακτικές (ξηρικοί ή παραδοσιακοί ελαιώνες, εξοικονόμηση νερού) και τίμια ανακυκλώσιμη συσκευασία. Κανένα σημάδι μόνο του δεν είναι απόδειξη, αλλά μαζί δίνουν αξιόπιστη εικόνα."),
        ("Πώς αναγνωρίζω βιώσιμο ελαιόλαδο στο κατάστημα;",
         "Ψάξτε βιολογική ετικέτα ή προστατευόμενη προέλευση (ΠΟΠ/ΠΓΕ), περιοχή ή κτήμα αντί για ασαφές μείγμα, ημερομηνία συγκομιδής και παραγωγό που περιγράφει την καλλιέργεια. Σκούρο γυαλί ή τενεκές και ρεαλιστική τιμή είναι υποστηρικτικά σημάδια."),
        ("Τι είναι το βιώσιμο ελαιόλαδο;",
         "Ελαιόλαδο που παράγεται με τρόπο που ισορροπεί περιβαλλοντικό αποτύπωμα (λίγο νερό, υγιές έδαφος, βιοποικιλότητα, χαμηλός άνθρακας), δίκαιες κοινωνικές συνθήκες και οικονομική βιωσιμότητα. Ισορροπία των τριών, όχι ένα χαρακτηριστικό."),
        ("Είναι το βιολογικό ελαιόλαδο αυτομάτως βιώσιμο;",
         "Το βιολογικό σημαίνει χωρίς συνθετικά φυτοφάρμακα ή λιπάσματα, που βοηθά έδαφος και νερό, αλλά από μόνο του δεν καλύπτει χρήση νερού, βιοποικιλότητα ή κοινωνική δικαιοσύνη. Ισχυρό σημάδι, όχι πλήρης εγγύηση."),
        ("Ποιο είναι το περιβαλλοντικό αποτύπωμα του ελαιόλαδου;",
         "Εξαρτάται από το πώς καλλιεργούνται οι ελιές. Οι παραδοσιακοί ξηρικοί ελαιώνες έχουν μικρό αποτύπωμα και αποθηκεύουν άνθρακα· οι εντατικοί αποδίδουν περισσότερο αλλά χρησιμοποιούν περισσότερο νερό και αγροχημικά. Συνολικά, χαμηλό αποτύπωμα σε σχέση με τα ζωικά λίπη."),
        ("Παραδοσιακοί ή εντατικοί ελαιώνες: ποιοι πιο βιώσιμοι;",
         "Οι παραδοσιακοί ξηρικοί ελαιώνες είναι γενικά πιο βιώσιμοι ανά εκτάριο: λίγες εισροές, πλούσιοι σε βιοποικιλότητα, αποθηκεύουν άνθρακα. Οι εντατικοί είναι πιο παραγωγικοί αλλά θέλουν περισσότερο νερό και προϊόντα· φυτοκάλυψη, μειωμένη κατεργασία και αποδοτική άρδευση μειώνουν τη διαφορά."),
    ],
)

if __name__ == "__main__":
    print("Sustainability GEO hub:")
    write_guide_cluster("oleiculture-durable", S, subdir="blog")

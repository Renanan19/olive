# -*- coding: utf-8 -*-
"""Content for the olive-oil-health-benefits pillar (x4 languages). Cautious YMYL."""
from health_pillar import build

DISC = {
    "fr": "Cet article est informatif et ne remplace pas un avis médical. Pour un problème de santé ou avant un changement important d'alimentation, consultez un professionnel.",
    "en": "This article is informational and is not a substitute for medical advice. For a health condition or before a major diet change, consult a professional.",
    "it": "Questo articolo è informativo e non sostituisce un parere medico. Per un problema di salute o prima di un cambiamento importante della dieta, consulta un professionista.",
    "el": "Το άρθρο είναι ενημερωτικό και δεν υποκαθιστά ιατρική συμβουλή. Για θέμα υγείας ή πριν από μεγάλη αλλαγή διατροφής, συμβουλευτείτε επαγγελματία.",
}

C = {}

# ================================================================== EN =========
C["en"] = dict(
    title="Olive Oil Health Benefits: the complete evidence-based guide",
    desc="The complete, evidence-based guide to olive oil health benefits: the key compounds (oleic acid, polyphenols), the EU-authorised health claim, the PREDIMED trial, how to get the benefits, and honest limits.",
    h1="Olive Oil Health Benefits: what the evidence says",
    lede="The compounds behind olive oil's reputation, the EU-authorised health claim, the Mediterranean-diet evidence, how to actually get the benefits, and the honest limits.",
    readtime="~9 min",
    disclaimer=DISC["en"],
    keywords="olive oil health benefits, extra virgin olive oil benefits, olive oil polyphenols, oleic acid, is olive oil good for you, how much olive oil per day, mediterranean diet",
    kf_label="Key facts",
    intro="Olive oil is credited with many health benefits. Some are well documented, others are marketing. This pillar guide separates them: the compounds responsible, what the evidence actually supports, the one EU-authorised health claim, and how to get the benefits day to day, without overstating them.",
    key_facts=[
        "Extra virgin olive oil is rich in oleic acid (a monounsaturated fat) and antioxidant polyphenols such as hydroxytyrosol, oleocanthal and oleuropein.",
        "The EU authorises one health claim: olive oil polyphenols help protect blood lipids from oxidative stress, obtained with 5 mg of hydroxytyrosol and derivatives per 20 g of oil daily.",
        "The PREDIMED clinical trial linked a Mediterranean diet enriched with extra virgin olive oil to fewer major cardiovascular events in at-risk adults.",
        "Benefits come from regular use within a balanced diet, not a single dose; one tablespoon is about 120 kcal.",
        "Extra virgin (unrefined) oil keeps the polyphenols; refined \"olive oil\" and \"light\" oils lose most of them.",
    ],
    toc=[("why", "Why olive oil is considered healthy"), ("compounds", "The key compounds"),
         ("claim", "The EU-authorised health claim"), ("evidence", "The Mediterranean-diet evidence"),
         ("howto", "How to get the benefits"), ("refined", "Extra virgin vs refined for health"),
         ("limits", "Honest limits"), ("faq", "FAQ")],
    sections=[
        ("why", "Why olive oil is considered healthy",
         "<p>Extra virgin olive oil is a cold-extracted, unrefined fruit juice. It keeps two useful families of compounds: mostly <strong>oleic acid</strong>, a monounsaturated fat, and a range of <strong>polyphenols</strong> that refining largely destroys. It is also the central fat of the Mediterranean diet, the eating pattern with the strongest evidence for cardiovascular health. Most of olive oil's reputation rests on this combination, used regularly and in place of less-healthy fats.</p>"),
        ("compounds", "The key compounds",
         "<table><thead><tr><th>Compound</th><th>Type</th><th>Associated with</th></tr></thead><tbody>"
         "<tr><td>Oleic acid</td><td>Monounsaturated fat</td><td>Replacing saturated fat; a more favourable blood-lipid profile</td></tr>"
         "<tr><td>Hydroxytyrosol / tyrosol</td><td>Polyphenol</td><td>Antioxidant; the EU claim (protecting blood lipids from oxidation)</td></tr>"
         "<tr><td>Oleocanthal</td><td>Polyphenol</td><td>Anti-inflammatory activity in lab studies (ibuprofen-like); the throat sting</td></tr>"
         "<tr><td>Oleuropein</td><td>Polyphenol</td><td>Antioxidant; part of the bitterness</td></tr>"
         "<tr><td>Vitamin E</td><td>Tocopherol</td><td>Antioxidant, protects the oil and cells' fats</td></tr>"
         "</tbody></table>"
         "<p>The polyphenols are what set extra virgin apart nutritionally and are highest in fresh, well-made oil.</p>"),
        ("claim", "The EU-authorised health claim",
         "<p>In the European Union, one health claim for olive oil is authorised: <strong>\"olive oil polyphenols contribute to the protection of blood lipids from oxidative stress.\"</strong> The claim applies to oils that provide at least <strong>5 mg of hydroxytyrosol and its derivatives (such as oleuropein complex and tyrosol) per 20 g of olive oil</strong>, consumed daily. This is a rare example of a food polyphenol claim backed by the European regulator, and it is why fresh, polyphenol-rich extra virgin oil matters.</p>"),
        ("evidence", "The Mediterranean-diet evidence",
         "<p>The best-documented benefit is not for olive oil alone but for the <strong>Mediterranean diet</strong> as a whole. The <strong>PREDIMED</strong> randomised controlled trial followed thousands of adults at cardiovascular risk. Those assigned a Mediterranean diet supplemented with extra virgin olive oil had fewer major cardiovascular events than the low-fat control group. Olive oil plays a central role there, but alongside vegetables, legumes, fish, nuts and whole grains. The takeaway: olive oil works best as part of a pattern, not as a stand-alone supplement.</p>"),
        ("howto", "How to get the health benefits",
         "<p>To turn the science into practice:</p>"
         "<ol>"
         "<li><strong>Choose a quality extra virgin oil</strong> — fresh, well stored, ideally with a harvest date. Polyphenols are highest in fresh EVOO.</li>"
         "<li><strong>Use about 2 tablespoons a day</strong> — the kind of amount studied for benefits, within a balanced diet.</li>"
         "<li><strong>Use some of it raw</strong> — dressings, a finishing drizzle; cooking gradually degrades some polyphenols.</li>"
         "<li><strong>Replace less-healthy fats</strong> — swap butter and processed fats for olive oil rather than simply adding calories.</li>"
         "<li><strong>Store it well</strong> — dark glass, cool, away from light and heat, to keep the polyphenols intact.</li>"
         "</ol>"),
        ("refined", "Extra virgin vs refined for health",
         "<p>\"Olive oil\" (without \"virgin\") and \"light\" olive oil are <strong>refined</strong>: neutral in taste and stripped of most polyphenols. They still provide monounsaturated fat, but not the antioxidant fraction that carries most of the specific benefits. For health, <strong>extra virgin</strong> is the better choice, especially used raw.</p>"),
        ("limits", "Honest limits",
         "<p>Olive oil is beneficial but not a medicine. It is calorie-dense (about 120 kcal per tablespoon), so it should replace other fats rather than pile on top of them. It does not \"cure\" disease, and headlines about single compounds (like oleocanthal) usually come from lab or short-term studies, not proof of clinical effects. The realistic message is consistent and modest: regular, moderate use of a quality extra virgin oil, within a balanced diet, is a sound choice.</p>"),
    ],
    howto_name="How to get the health benefits of olive oil",
    howto_desc="Five practical steps to get the most health benefit from olive oil, based on the evidence.",
    howto_steps=[
        ("Choose a quality extra virgin oil", "Pick a fresh, well-stored extra virgin olive oil, ideally with a harvest date; polyphenols are highest in fresh EVOO."),
        ("Use about 2 tablespoons a day", "Aim for roughly the amount studied for benefits, within a balanced diet."),
        ("Use some of it raw", "Use part of it uncooked in dressings or as a finishing drizzle, because cooking degrades some polyphenols."),
        ("Replace less-healthy fats", "Swap butter and processed fats for olive oil rather than simply adding calories."),
        ("Store it well", "Keep it in dark glass, cool and away from light and heat to preserve the polyphenols."),
    ],
    faq_h="Frequently asked questions",
    faqs=[
        ("Is olive oil good for you?",
         "Yes, as part of a balanced diet. Extra virgin olive oil is a source of monounsaturated fat and antioxidant polyphenols, and it is central to the Mediterranean diet. It is best used to replace less-healthy fats rather than simply adding calories."),
        ("What are the health benefits of extra virgin olive oil?",
         "It provides oleic acid and polyphenols with antioxidant and anti-inflammatory activity. Within the Mediterranean diet, research associates it with better cardiovascular health, and the EU authorises a claim that its polyphenols help protect blood lipids from oxidation."),
        ("How much olive oil per day?",
         "About 2 tablespoons a day fits a balanced diet and reflects the amounts studied for benefits. The EU health claim is based on 20 g of polyphenol-rich oil daily. Stay moderate: one tablespoon is about 120 kcal."),
        ("What are polyphenols in olive oil?",
         "Antioxidant plant compounds such as hydroxytyrosol, tyrosol, oleocanthal and oleuropein. They are responsible for much of olive oil's antioxidant and anti-inflammatory activity and are highest in fresh extra virgin oil."),
        ("Is it better to take olive oil raw?",
         "In part, yes. Cooking gradually degrades some polyphenols, so using some of your oil raw (dressings, a finishing drizzle) preserves more of the aroma and antioxidant compounds."),
        ("Extra virgin or refined olive oil for health?",
         "Extra virgin. Refining removes most of the polyphenols, which carry a large part of the specific health benefits. Refined 'olive oil' and 'light' oils still provide monounsaturated fat but little of the antioxidant fraction."),
        ("Does olive oil help the heart?",
         "Within the Mediterranean diet, extra virgin olive oil is associated with better cardiovascular health, and the PREDIMED trial linked that diet with olive oil to fewer major cardiovascular events. It works as part of a healthy pattern, not as a stand-alone cure."),
        ("Is it good to take olive oil in the morning on an empty stomach?",
         "It is a popular habit and unlikely to be harmful in a small amount, but the specific benefits of the timing are not well proven. What matters most is regular, moderate use of a quality oil within a balanced diet, at any time of day."),
    ],
)

# ================================================================== FR =========
C["fr"] = dict(
    title="Bienfaits de l'huile d'olive : le guide complet fondé sur les preuves",
    desc="Le guide complet et fondé sur les preuves des bienfaits de l'huile d'olive : composés clés (acide oléique, polyphénols), allégation santé européenne, essai PREDIMED, comment en tirer parti, et limites honnêtes.",
    h1="Bienfaits de l'huile d'olive : ce que disent les preuves",
    lede="Les composés derrière la réputation de l'huile d'olive, l'allégation santé européenne, les preuves du régime méditerranéen, comment en tirer parti, et les limites honnêtes.",
    readtime="~9 min",
    disclaimer=DISC["fr"],
    keywords="bienfaits huile d'olive, bienfaits huile d'olive extra vierge, polyphénols huile d'olive, acide oléique, huile d'olive bonne pour la santé, quantité huile d'olive par jour, régime méditerranéen",
    kf_label="En bref",
    intro="On prête beaucoup de bienfaits à l'huile d'olive. Certains sont bien documentés, d'autres relèvent du marketing. Ce guide pilier fait le tri : les composés responsables, ce que les preuves soutiennent réellement, l'unique allégation santé européenne, et comment en tirer parti au quotidien, sans exagérer.",
    key_facts=[
        "L'huile d'olive extra vierge est riche en acide oléique (graisse mono-insaturée) et en polyphénols antioxydants comme l'hydroxytyrosol, l'oléocanthal et l'oléuropéine.",
        "L'UE autorise une allégation santé : les polyphénols de l'huile d'olive aident à protéger les lipides sanguins du stress oxydatif, avec 5 mg d'hydroxytyrosol et dérivés pour 20 g d'huile par jour.",
        "L'essai clinique PREDIMED a associé un régime méditerranéen enrichi en huile d'olive extra vierge à moins d'événements cardiovasculaires majeurs chez des adultes à risque.",
        "Les bienfaits viennent d'un usage régulier dans une alimentation équilibrée, pas d'une dose unique ; une cuillère à soupe ≈ 120 kcal.",
        "L'extra vierge (non raffinée) conserve les polyphénols ; l'« huile d'olive » raffinée et les huiles « légères » en perdent l'essentiel.",
    ],
    toc=[("why", "Pourquoi l'huile d'olive est réputée saine"), ("compounds", "Les composés clés"),
         ("claim", "L'allégation santé européenne"), ("evidence", "Les preuves du régime méditerranéen"),
         ("howto", "Comment en tirer parti"), ("refined", "Extra vierge vs raffinée pour la santé"),
         ("limits", "Limites honnêtes"), ("faq", "FAQ")],
    sections=[
        ("why", "Pourquoi l'huile d'olive est réputée saine",
         "<p>L'huile d'olive extra vierge est un jus de fruit gras, extrait à froid et non raffiné. Elle conserve deux familles utiles de composés : surtout de l'<strong>acide oléique</strong>, une graisse mono-insaturée, et un éventail de <strong>polyphénols</strong> que le raffinage détruit en grande partie. C'est aussi la matière grasse centrale du régime méditerranéen, le modèle alimentaire le mieux étayé pour la santé cardiovasculaire. La réputation de l'huile d'olive repose sur cette combinaison, utilisée régulièrement et en remplacement de graisses moins saines.</p>"),
        ("compounds", "Les composés clés",
         "<table><thead><tr><th>Composé</th><th>Type</th><th>Associé à</th></tr></thead><tbody>"
         "<tr><td>Acide oléique</td><td>Graisse mono-insaturée</td><td>Remplacer les graisses saturées ; profil lipidique plus favorable</td></tr>"
         "<tr><td>Hydroxytyrosol / tyrosol</td><td>Polyphénol</td><td>Antioxydant ; l'allégation UE (protection des lipides sanguins)</td></tr>"
         "<tr><td>Oléocanthal</td><td>Polyphénol</td><td>Activité anti-inflammatoire en laboratoire (type ibuprofène) ; le piquant en gorge</td></tr>"
         "<tr><td>Oléuropéine</td><td>Polyphénol</td><td>Antioxydant ; une partie de l'amertume</td></tr>"
         "<tr><td>Vitamine E</td><td>Tocophérol</td><td>Antioxydant, protège l'huile et les graisses des cellules</td></tr>"
         "</tbody></table>"
         "<p>Ce sont les polyphénols qui distinguent l'extra vierge sur le plan nutritionnel ; ils sont les plus élevés dans une huile fraîche et bien faite.</p>"),
        ("claim", "L'allégation santé européenne",
         "<p>Dans l'Union européenne, une allégation santé pour l'huile d'olive est autorisée : <strong>« les polyphénols de l'huile d'olive contribuent à la protection des lipides sanguins contre le stress oxydatif ».</strong> Elle s'applique aux huiles apportant au moins <strong>5 mg d'hydroxytyrosol et de ses dérivés (complexe oléuropéine et tyrosol) pour 20 g d'huile</strong>, consommés chaque jour. C'est un rare exemple d'allégation sur un polyphénol alimentaire validée par le régulateur européen, et c'est pourquoi une extra vierge fraîche et riche en polyphénols compte.</p>"),
        ("evidence", "Les preuves du régime méditerranéen",
         "<p>Le bienfait le mieux documenté ne concerne pas l'huile d'olive isolée mais le <strong>régime méditerranéen</strong> dans son ensemble. L'essai contrôlé randomisé <strong>PREDIMED</strong> a suivi des milliers d'adultes à risque cardiovasculaire. Ceux suivant un régime méditerranéen complété en huile d'olive extra vierge ont présenté moins d'événements cardiovasculaires majeurs que le groupe témoin « pauvre en graisses ». L'huile y joue un rôle central, mais associée aux légumes, légumineuses, poisson, fruits à coque et céréales complètes. À retenir : l'huile d'olive agit au mieux dans un modèle global, pas comme complément isolé.</p>"),
        ("howto", "Comment en tirer parti",
         "<p>Pour traduire la science en pratique :</p>"
         "<ol>"
         "<li><strong>Choisissez une extra vierge de qualité</strong> — fraîche, bien conservée, idéalement avec une date de récolte. Les polyphénols sont les plus élevés dans une EVOO fraîche.</li>"
         "<li><strong>Utilisez environ 2 cuillères à soupe par jour</strong> — l'ordre de grandeur étudié pour les bienfaits, dans une alimentation équilibrée.</li>"
         "<li><strong>Consommez-en une partie à cru</strong> — assaisonnements, filet de finition ; la cuisson dégrade peu à peu certains polyphénols.</li>"
         "<li><strong>Remplacez des graisses moins saines</strong> — troquez beurre et graisses transformées contre l'huile d'olive plutôt que d'ajouter des calories.</li>"
         "<li><strong>Conservez-la bien</strong> — verre foncé, au frais, à l'abri de la lumière et de la chaleur, pour préserver les polyphénols.</li>"
         "</ol>"),
        ("refined", "Extra vierge vs raffinée pour la santé",
         "<p>L'« huile d'olive » (sans « vierge ») et l'huile « légère » sont <strong>raffinées</strong> : goût neutre et privées de la plupart des polyphénols. Elles apportent encore de la graisse mono-insaturée, mais pas la fraction antioxydante qui porte l'essentiel des bienfaits spécifiques. Pour la santé, l'<strong>extra vierge</strong> est le meilleur choix, surtout à cru.</p>"),
        ("limits", "Limites honnêtes",
         "<p>L'huile d'olive est bénéfique mais ce n'est pas un médicament. Elle est calorique (environ 120 kcal par cuillère à soupe) : elle doit remplacer d'autres graisses, pas s'y ajouter. Elle ne « guérit » pas de maladie, et les titres sur des composés isolés (comme l'oléocanthal) viennent en général d'études de laboratoire ou de court terme, pas de preuves d'effets cliniques. Le message réaliste est constant et modeste : un usage régulier et modéré d'une extra vierge de qualité, dans une alimentation équilibrée, est un choix sain.</p>"),
    ],
    howto_name="Comment tirer parti des bienfaits de l'huile d'olive",
    howto_desc="Cinq étapes concrètes pour tirer le maximum de bienfaits de l'huile d'olive, d'après les preuves.",
    howto_steps=[
        ("Choisir une extra vierge de qualité", "Prenez une huile d'olive extra vierge fraîche et bien conservée, idéalement avec une date de récolte ; les polyphénols sont les plus élevés dans une EVOO fraîche."),
        ("Utiliser environ 2 cuillères à soupe par jour", "Visez l'ordre de grandeur étudié pour les bienfaits, dans une alimentation équilibrée."),
        ("En consommer une partie à cru", "Utilisez-en une part non cuite en assaisonnement ou en filet de finition, car la cuisson dégrade certains polyphénols."),
        ("Remplacer des graisses moins saines", "Troquez beurre et graisses transformées contre l'huile d'olive plutôt que d'ajouter des calories."),
        ("Bien la conserver", "Gardez-la en verre foncé, au frais, à l'abri de la lumière et de la chaleur pour préserver les polyphénols."),
    ],
    faq_h="Questions fréquentes",
    faqs=[
        ("L'huile d'olive est-elle bonne pour la santé ?",
         "Oui, dans une alimentation équilibrée. L'huile d'olive extra vierge est une source de graisses mono-insaturées et de polyphénols antioxydants, et elle est centrale dans le régime méditerranéen. Mieux vaut l'utiliser en remplacement de graisses moins saines qu'en simple ajout de calories."),
        ("Quels sont les bienfaits de l'huile d'olive extra vierge ?",
         "Elle apporte de l'acide oléique et des polyphénols à activité antioxydante et anti-inflammatoire. Dans le cadre du régime méditerranéen, la recherche l'associe à une meilleure santé cardiovasculaire, et l'UE autorise une allégation selon laquelle ses polyphénols aident à protéger les lipides sanguins de l'oxydation."),
        ("Quelle quantité d'huile d'olive par jour ?",
         "Environ 2 cuillères à soupe par jour s'intègrent à une alimentation équilibrée et reflètent les quantités étudiées. L'allégation UE repose sur 20 g d'huile riche en polyphénols par jour. Restez mesuré : une cuillère apporte environ 120 kcal."),
        ("Que sont les polyphénols de l'huile d'olive ?",
         "Des composés végétaux antioxydants comme l'hydroxytyrosol, le tyrosol, l'oléocanthal et l'oléuropéine. Ils portent une grande partie de l'activité antioxydante et anti-inflammatoire de l'huile, et sont les plus élevés dans une extra vierge fraîche."),
        ("Vaut-il mieux consommer l'huile d'olive à cru ?",
         "En partie, oui. La cuisson dégrade progressivement certains polyphénols ; en consommer une part à cru (assaisonnements, filet de finition) préserve mieux le parfum et les composés antioxydants."),
        ("Extra vierge ou raffinée pour la santé ?",
         "Extra vierge. Le raffinage retire la plupart des polyphénols, qui portent une grande partie des bienfaits spécifiques. L'« huile d'olive » raffinée et les huiles « légères » apportent encore de la graisse mono-insaturée mais peu de la fraction antioxydante."),
        ("L'huile d'olive est-elle bonne pour le cœur ?",
         "Dans le cadre du régime méditerranéen, l'huile d'olive extra vierge est associée à une meilleure santé cardiovasculaire, et l'essai PREDIMED a lié ce régime avec l'huile d'olive à moins d'événements cardiovasculaires majeurs. Elle agit dans un modèle sain, pas comme remède isolé."),
        ("Est-ce bon de boire de l'huile d'olive le matin à jeun ?",
         "C'est une habitude populaire, sans danger a priori en petite quantité, mais les bienfaits spécifiques du moment ne sont pas bien prouvés. Ce qui compte le plus est un usage régulier et modéré d'une huile de qualité dans une alimentation équilibrée, à n'importe quel moment de la journée."),
    ],
)

# ================================================================== IT =========
C["it"] = dict(
    title="Benefici dell'olio d'oliva: la guida completa basata sulle prove",
    desc="La guida completa e basata sulle prove ai benefici dell'olio d'oliva: composti chiave (acido oleico, polifenoli), claim salutistico UE, studio PREDIMED, come ottenerli e limiti onesti.",
    h1="Benefici dell'olio d'oliva: cosa dicono le prove",
    lede="I composti dietro la reputazione dell'olio d'oliva, il claim salutistico UE, le prove della dieta mediterranea, come ottenerne i benefici e i limiti onesti.",
    readtime="~9 min",
    disclaimer=DISC["it"],
    keywords="benefici olio d'oliva, benefici olio extravergine, polifenoli olio d'oliva, acido oleico, olio d'oliva fa bene, quanto olio d'oliva al giorno, dieta mediterranea",
    kf_label="In breve",
    intro="All'olio d'oliva si attribuiscono molti benefici. Alcuni sono ben documentati, altri sono marketing. Questa guida pilastro li separa: i composti responsabili, cosa sostengono davvero le prove, l'unico claim salutistico UE, e come ottenere i benefici ogni giorno, senza esagerare.",
    key_facts=[
        "L'olio extravergine è ricco di acido oleico (grasso monoinsaturo) e polifenoli antiossidanti come idrossitirosolo, oleocantale e oleuropeina.",
        "L'UE autorizza un claim: i polifenoli dell'olio d'oliva aiutano a proteggere i lipidi del sangue dallo stress ossidativo, con 5 mg di idrossitirosolo e derivati per 20 g di olio al giorno.",
        "Lo studio clinico PREDIMED ha collegato una dieta mediterranea con olio extravergine a meno eventi cardiovascolari maggiori in adulti a rischio.",
        "I benefici vengono dall'uso regolare in una dieta equilibrata, non da una singola dose; un cucchiaio ≈ 120 kcal.",
        "L'extravergine (non raffinato) conserva i polifenoli; l'«olio d'oliva» raffinato e gli oli «leggeri» ne perdono gran parte.",
    ],
    toc=[("why", "Perché l'olio d'oliva è considerato sano"), ("compounds", "I composti chiave"),
         ("claim", "Il claim salutistico UE"), ("evidence", "Le prove della dieta mediterranea"),
         ("howto", "Come ottenere i benefici"), ("refined", "Extravergine vs raffinato per la salute"),
         ("limits", "Limiti onesti"), ("faq", "FAQ")],
    sections=[
        ("why", "Perché l'olio d'oliva è considerato sano",
         "<p>L'olio extravergine d'oliva è un succo di frutta grasso, estratto a freddo e non raffinato. Conserva due famiglie utili di composti: soprattutto <strong>acido oleico</strong>, un grasso monoinsaturo, e una gamma di <strong>polifenoli</strong> che la raffinazione distrugge in gran parte. È anche il grasso centrale della dieta mediterranea, il modello alimentare con le prove più solide per la salute cardiovascolare. La reputazione dell'olio d'oliva si basa su questa combinazione, usata regolarmente e al posto di grassi meno sani.</p>"),
        ("compounds", "I composti chiave",
         "<table><thead><tr><th>Composto</th><th>Tipo</th><th>Associato a</th></tr></thead><tbody>"
         "<tr><td>Acido oleico</td><td>Grasso monoinsaturo</td><td>Sostituire i grassi saturi; profilo lipidico più favorevole</td></tr>"
         "<tr><td>Idrossitirosolo / tirosolo</td><td>Polifenolo</td><td>Antiossidante; il claim UE (protezione dei lipidi del sangue)</td></tr>"
         "<tr><td>Oleocantale</td><td>Polifenolo</td><td>Attività antinfiammatoria in laboratorio (tipo ibuprofene); il pizzicore in gola</td></tr>"
         "<tr><td>Oleuropeina</td><td>Polifenolo</td><td>Antiossidante; parte dell'amaro</td></tr>"
         "<tr><td>Vitamina E</td><td>Tocoferolo</td><td>Antiossidante, protegge l'olio e i grassi delle cellule</td></tr>"
         "</tbody></table>"
         "<p>Sono i polifenoli a distinguere l'extravergine dal punto di vista nutrizionale, e sono più alti in un olio fresco e ben fatto.</p>"),
        ("claim", "Il claim salutistico UE",
         "<p>Nell'Unione Europea è autorizzato un claim per l'olio d'oliva: <strong>«i polifenoli dell'olio d'oliva contribuiscono alla protezione dei lipidi del sangue dallo stress ossidativo».</strong> Si applica agli oli che forniscono almeno <strong>5 mg di idrossitirosolo e derivati (complesso oleuropeina e tirosolo) per 20 g di olio</strong>, consumati ogni giorno. È un raro esempio di claim su un polifenolo alimentare validato dal regolatore europeo, ed è per questo che conta un extravergine fresco e ricco di polifenoli.</p>"),
        ("evidence", "Le prove della dieta mediterranea",
         "<p>Il beneficio meglio documentato non riguarda l'olio d'oliva isolato ma la <strong>dieta mediterranea</strong> nel suo insieme. Lo studio controllato randomizzato <strong>PREDIMED</strong> ha seguito migliaia di adulti a rischio cardiovascolare. Chi seguiva una dieta mediterranea con olio extravergine ha avuto meno eventi cardiovascolari maggiori del gruppo di controllo a basso contenuto di grassi. L'olio vi gioca un ruolo centrale, ma insieme a verdure, legumi, pesce, frutta secca e cereali integrali. La lezione: l'olio d'oliva funziona meglio in un modello, non come integratore isolato.</p>"),
        ("howto", "Come ottenere i benefici",
         "<p>Per tradurre la scienza in pratica:</p>"
         "<ol>"
         "<li><strong>Scegli un extravergine di qualità</strong> — fresco, ben conservato, idealmente con una data di raccolta. I polifenoli sono più alti in un EVO fresco.</li>"
         "<li><strong>Usa circa 2 cucchiai al giorno</strong> — l'ordine di grandezza studiato per i benefici, in una dieta equilibrata.</li>"
         "<li><strong>Usane una parte a crudo</strong> — condimenti, filo di finitura; la cottura degrada gradualmente alcuni polifenoli.</li>"
         "<li><strong>Sostituisci grassi meno sani</strong> — scambia burro e grassi trasformati con l'olio d'oliva invece di aggiungere calorie.</li>"
         "<li><strong>Conservalo bene</strong> — vetro scuro, al fresco, al riparo da luce e calore, per preservare i polifenoli.</li>"
         "</ol>"),
        ("refined", "Extravergine vs raffinato per la salute",
         "<p>L'«olio d'oliva» (senza «vergine») e l'olio «leggero» sono <strong>raffinati</strong>: gusto neutro e privi di gran parte dei polifenoli. Danno ancora grasso monoinsaturo, ma non la frazione antiossidante che porta gran parte dei benefici specifici. Per la salute, l'<strong>extravergine</strong> è la scelta migliore, soprattutto a crudo.</p>"),
        ("limits", "Limiti onesti",
         "<p>L'olio d'oliva è benefico ma non è un farmaco. È calorico (circa 120 kcal per cucchiaio): deve sostituire altri grassi, non aggiungersi. Non «cura» malattie, e i titoli su singoli composti (come l'oleocantale) vengono di solito da studi di laboratorio o a breve termine, non da prove di effetti clinici. Il messaggio realistico è costante e modesto: un uso regolare e moderato di un buon extravergine, in una dieta equilibrata, è una scelta sana.</p>"),
    ],
    howto_name="Come ottenere i benefici dell'olio d'oliva",
    howto_desc="Cinque passi pratici per ottenere il massimo beneficio dall'olio d'oliva, secondo le prove.",
    howto_steps=[
        ("Scegli un extravergine di qualità", "Scegli un olio extravergine fresco e ben conservato, idealmente con una data di raccolta; i polifenoli sono più alti in un EVO fresco."),
        ("Usa circa 2 cucchiai al giorno", "Punta all'ordine di grandezza studiato per i benefici, in una dieta equilibrata."),
        ("Usane una parte a crudo", "Usa una parte non cotta nei condimenti o a filo, perché la cottura degrada alcuni polifenoli."),
        ("Sostituisci grassi meno sani", "Scambia burro e grassi trasformati con l'olio d'oliva invece di aggiungere calorie."),
        ("Conservalo bene", "Tienilo in vetro scuro, al fresco e lontano da luce e calore per preservare i polifenoli."),
    ],
    faq_h="Domande frequenti",
    faqs=[
        ("L'olio d'oliva fa bene?",
         "Sì, in una dieta equilibrata. L'olio extravergine è fonte di grassi monoinsaturi e polifenoli antiossidanti, ed è centrale nella dieta mediterranea. Meglio usarlo per sostituire grassi meno sani che come semplice aggiunta di calorie."),
        ("Quali sono i benefici dell'olio extravergine d'oliva?",
         "Fornisce acido oleico e polifenoli con attività antiossidante e antinfiammatoria. Nella dieta mediterranea la ricerca lo associa a una migliore salute cardiovascolare, e l'UE autorizza un claim secondo cui i suoi polifenoli aiutano a proteggere i lipidi del sangue dall'ossidazione."),
        ("Quanto olio d'oliva al giorno?",
         "Circa 2 cucchiai al giorno si integrano in una dieta equilibrata e riflettono le quantità studiate. Il claim UE si basa su 20 g di olio ricco di polifenoli al giorno. Con moderazione: un cucchiaio è circa 120 kcal."),
        ("Cosa sono i polifenoli dell'olio d'oliva?",
         "Composti vegetali antiossidanti come idrossitirosolo, tirosolo, oleocantale e oleuropeina. Portano gran parte dell'attività antiossidante e antinfiammatoria dell'olio e sono più alti in un extravergine fresco."),
        ("È meglio consumare l'olio d'oliva a crudo?",
         "In parte sì. La cottura degrada gradualmente alcuni polifenoli, quindi usarne una parte a crudo (condimenti, filo di finitura) preserva meglio aroma e composti antiossidanti."),
        ("Extravergine o raffinato per la salute?",
         "Extravergine. La raffinazione toglie gran parte dei polifenoli, che portano una parte importante dei benefici specifici. L'«olio d'oliva» raffinato e gli oli «leggeri» danno ancora grasso monoinsaturo ma poco della frazione antiossidante."),
        ("L'olio d'oliva fa bene al cuore?",
         "Nella dieta mediterranea l'olio extravergine è associato a una migliore salute cardiovascolare, e lo studio PREDIMED ha collegato quella dieta con l'olio a meno eventi cardiovascolari maggiori. Funziona in un modello sano, non come rimedio isolato."),
        ("Fa bene bere olio d'oliva la mattina a stomaco vuoto?",
         "È un'abitudine popolare, probabilmente innocua in piccola quantità, ma i benefici specifici del momento non sono ben provati. Conta di più un uso regolare e moderato di un buon olio in una dieta equilibrata, a qualsiasi ora."),
    ],
)

# ================================================================== EL =========
C["el"] = dict(
    title="Οφέλη ελαιόλαδου: ο πλήρης οδηγός βασισμένος σε στοιχεία",
    desc="Ο πλήρης, τεκμηριωμένος οδηγός για τα οφέλη του ελαιόλαδου: βασικές ενώσεις (ελαϊκό οξύ, πολυφαινόλες), ισχυρισμός υγείας ΕΕ, μελέτη PREDIMED, πώς να τα αποκομίσετε και τίμια όρια.",
    h1="Οφέλη ελαιόλαδου: τι δείχνουν τα στοιχεία",
    lede="Οι ενώσεις πίσω από τη φήμη του ελαιόλαδου, ο ισχυρισμός υγείας της ΕΕ, τα στοιχεία της μεσογειακής διατροφής, πώς να αποκομίσετε τα οφέλη και τα τίμια όρια.",
    readtime="~9 λεπτά",
    disclaimer=DISC["el"],
    keywords="οφέλη ελαιόλαδου, οφέλη έξτρα παρθένου ελαιόλαδου, πολυφαινόλες ελαιόλαδου, ελαϊκό οξύ, κάνει καλό το ελαιόλαδο, πόσο ελαιόλαδο την ημέρα, μεσογειακή διατροφή",
    kf_label="Με λίγα λόγια",
    intro="Στο ελαιόλαδο αποδίδονται πολλά οφέλη. Κάποια είναι καλά τεκμηριωμένα, άλλα είναι μάρκετινγκ. Αυτός ο κεντρικός οδηγός τα ξεχωρίζει: τις υπεύθυνες ενώσεις, τι στηρίζουν πραγματικά τα στοιχεία, τον μοναδικό ισχυρισμό υγείας της ΕΕ, και πώς να αποκομίσετε τα οφέλη καθημερινά, χωρίς υπερβολές.",
    key_facts=[
        "Το έξτρα παρθένο ελαιόλαδο είναι πλούσιο σε ελαϊκό οξύ (μονοακόρεστο λίπος) και αντιοξειδωτικές πολυφαινόλες όπως υδροξυτυροσόλη, ελαιοκανθάλη και ελευρωπαΐνη.",
        "Η ΕΕ επιτρέπει έναν ισχυρισμό: οι πολυφαινόλες του ελαιόλαδου βοηθούν στην προστασία των λιπιδίων του αίματος από την οξείδωση, με 5 mg υδροξυτυροσόλης ανά 20 g ελαιόλαδου ημερησίως.",
        "Η κλινική μελέτη PREDIMED συνέδεσε μεσογειακή διατροφή με έξτρα παρθένο ελαιόλαδο με λιγότερα μείζονα καρδιαγγειακά συμβάντα σε ενήλικες σε κίνδυνο.",
        "Τα οφέλη έρχονται από τακτική χρήση σε ισορροπημένη διατροφή, όχι από μία δόση· μια κουταλιά ≈ 120 kcal.",
        "Το έξτρα παρθένο (μη ραφιναρισμένο) διατηρεί τις πολυφαινόλες· το ραφιναρισμένο «ελαιόλαδο» και τα «ελαφριά» χάνουν τις περισσότερες.",
    ],
    toc=[("why", "Γιατί το ελαιόλαδο θεωρείται υγιεινό"), ("compounds", "Οι βασικές ενώσεις"),
         ("claim", "Ο ισχυρισμός υγείας της ΕΕ"), ("evidence", "Τα στοιχεία της μεσογειακής διατροφής"),
         ("howto", "Πώς να αποκομίσετε τα οφέλη"), ("refined", "Έξτρα παρθένο vs ραφιναρισμένο"),
         ("limits", "Τίμια όρια"), ("faq", "FAQ")],
    sections=[
        ("why", "Γιατί το ελαιόλαδο θεωρείται υγιεινό",
         "<p>Το έξτρα παρθένο ελαιόλαδο είναι ένας λιπαρός χυμός φρούτου, εκχυλισμένος εν ψυχρώ και μη ραφιναρισμένος. Διατηρεί δύο χρήσιμες οικογένειες ενώσεων: κυρίως <strong>ελαϊκό οξύ</strong>, ένα μονοακόρεστο λίπος, και ένα φάσμα <strong>πολυφαινολών</strong> που η ραφινάρισμα καταστρέφει σε μεγάλο βαθμό. Είναι επίσης το κεντρικό λίπος της μεσογειακής διατροφής, του διατροφικού προτύπου με τα ισχυρότερα στοιχεία για την καρδιαγγειακή υγεία. Η φήμη του βασίζεται σε αυτόν τον συνδυασμό, σε τακτική χρήση και ως αντικατάσταση λιγότερο υγιεινών λιπών.</p>"),
        ("compounds", "Οι βασικές ενώσεις",
         "<table><thead><tr><th>Ένωση</th><th>Τύπος</th><th>Συνδέεται με</th></tr></thead><tbody>"
         "<tr><td>Ελαϊκό οξύ</td><td>Μονοακόρεστο λίπος</td><td>Αντικατάσταση κορεσμένων· ευνοϊκότερο λιπιδικό προφίλ</td></tr>"
         "<tr><td>Υδροξυτυροσόλη / τυροσόλη</td><td>Πολυφαινόλη</td><td>Αντιοξειδωτικό· ο ισχυρισμός ΕΕ (προστασία λιπιδίων)</td></tr>"
         "<tr><td>Ελαιοκανθάλη</td><td>Πολυφαινόλη</td><td>Αντιφλεγμονώδης δράση σε εργαστήριο (τύπου ιβουπροφαίνης)· το κάψιμο στον λαιμό</td></tr>"
         "<tr><td>Ελευρωπαΐνη</td><td>Πολυφαινόλη</td><td>Αντιοξειδωτικό· μέρος της πικράδας</td></tr>"
         "<tr><td>Βιταμίνη E</td><td>Τοκοφερόλη</td><td>Αντιοξειδωτικό, προστατεύει το λάδι και τα λίπη των κυττάρων</td></tr>"
         "</tbody></table>"
         "<p>Οι πολυφαινόλες ξεχωρίζουν διατροφικά το έξτρα παρθένο και είναι υψηλότερες σε φρέσκο, καλοφτιαγμένο λάδι.</p>"),
        ("claim", "Ο ισχυρισμός υγείας της ΕΕ",
         "<p>Στην Ευρωπαϊκή Ένωση επιτρέπεται ένας ισχυρισμός για το ελαιόλαδο: <strong>«οι πολυφαινόλες του ελαιόλαδου συμβάλλουν στην προστασία των λιπιδίων του αίματος από το οξειδωτικό στρες».</strong> Ισχύει για λάδια που παρέχουν τουλάχιστον <strong>5 mg υδροξυτυροσόλης και παραγώγων (σύμπλοκο ελευρωπαΐνης και τυροσόλης) ανά 20 g ελαιόλαδου</strong>, ημερησίως. Είναι σπάνιο παράδειγμα ισχυρισμού για διατροφική πολυφαινόλη εγκεκριμένου από τον ευρωπαϊκό ρυθμιστή.</p>"),
        ("evidence", "Τα στοιχεία της μεσογειακής διατροφής",
         "<p>Το καλύτερα τεκμηριωμένο όφελος δεν αφορά το ελαιόλαδο μόνο του αλλά τη <strong>μεσογειακή διατροφή</strong> συνολικά. Η τυχαιοποιημένη ελεγχόμενη μελέτη <strong>PREDIMED</strong> παρακολούθησε χιλιάδες ενήλικες σε καρδιαγγειακό κίνδυνο. Όσοι ακολουθούσαν μεσογειακή διατροφή με έξτρα παρθένο ελαιόλαδο είχαν λιγότερα μείζονα καρδιαγγειακά συμβάντα από την ομάδα ελέγχου χαμηλών λιπαρών. Το λάδι έχει κεντρικό ρόλο, αλλά μαζί με λαχανικά, όσπρια, ψάρι, ξηρούς καρπούς και δημητριακά ολικής. Το συμπέρασμα: λειτουργεί καλύτερα ως μέρος προτύπου.</p>"),
        ("howto", "Πώς να αποκομίσετε τα οφέλη",
         "<p>Για να γίνει η επιστήμη πράξη:</p>"
         "<ol>"
         "<li><strong>Διαλέξτε ποιοτικό έξτρα παρθένο</strong> — φρέσκο, καλά αποθηκευμένο, ιδανικά με ημερομηνία συγκομιδής. Οι πολυφαινόλες είναι υψηλότερες σε φρέσκο.</li>"
         "<li><strong>Χρησιμοποιήστε περίπου 2 κουταλιές τη μέρα</strong> — η τάξη μεγέθους που μελετήθηκε, σε ισορροπημένη διατροφή.</li>"
         "<li><strong>Χρησιμοποιήστε μέρος του ωμό</strong> — ντρέσινγκ, τελείωμα· το μαγείρεμα υποβαθμίζει σταδιακά κάποιες πολυφαινόλες.</li>"
         "<li><strong>Αντικαταστήστε λιγότερο υγιεινά λίπη</strong> — βούτυρο και επεξεργασμένα λίπη με ελαιόλαδο, αντί να προσθέτετε θερμίδες.</li>"
         "<li><strong>Αποθηκεύστε το σωστά</strong> — σκούρο γυαλί, δροσερά, μακριά από φως και θερμότητα.</li>"
         "</ol>"),
        ("refined", "Έξτρα παρθένο vs ραφιναρισμένο για την υγεία",
         "<p>Το «ελαιόλαδο» (χωρίς «παρθένο») και το «ελαφρύ» είναι <strong>ραφιναρισμένα</strong>: ουδέτερα και χωρίς τις περισσότερες πολυφαινόλες. Δίνουν ακόμη μονοακόρεστο λίπος, αλλά όχι το αντιοξειδωτικό κλάσμα που φέρει τα περισσότερα ειδικά οφέλη. Για την υγεία, το <strong>έξτρα παρθένο</strong> είναι καλύτερη επιλογή, ιδίως ωμό.</p>"),
        ("limits", "Τίμια όρια",
         "<p>Το ελαιόλαδο είναι ωφέλιμο αλλά δεν είναι φάρμακο. Είναι θερμιδικό (περίπου 120 kcal ανά κουταλιά): πρέπει να αντικαθιστά άλλα λίπη, όχι να προστίθεται. Δεν «θεραπεύει» νόσους, και οι τίτλοι για μεμονωμένες ενώσεις (όπως η ελαιοκανθάλη) προέρχονται συνήθως από εργαστηριακές ή βραχυπρόθεσμες μελέτες. Το ρεαλιστικό μήνυμα είναι σταθερό και μετρημένο: τακτική, μέτρια χρήση ενός καλού έξτρα παρθένου, σε ισορροπημένη διατροφή, είναι σωστή επιλογή.</p>"),
    ],
    howto_name="Πώς να αποκομίσετε τα οφέλη του ελαιόλαδου",
    howto_desc="Πέντε πρακτικά βήματα για μέγιστο όφελος από το ελαιόλαδο, βάσει των στοιχείων.",
    howto_steps=[
        ("Διαλέξτε ποιοτικό έξτρα παρθένο", "Επιλέξτε φρέσκο, καλά αποθηκευμένο έξτρα παρθένο, ιδανικά με ημερομηνία συγκομιδής· οι πολυφαινόλες είναι υψηλότερες σε φρέσκο."),
        ("Χρησιμοποιήστε ~2 κουταλιές τη μέρα", "Στοχεύστε στην τάξη μεγέθους που μελετήθηκε, σε ισορροπημένη διατροφή."),
        ("Χρησιμοποιήστε μέρος ωμό", "Χρησιμοποιήστε μέρος του άψητο σε ντρέσινγκ ή τελείωμα, γιατί το μαγείρεμα υποβαθμίζει κάποιες πολυφαινόλες."),
        ("Αντικαταστήστε λιγότερο υγιεινά λίπη", "Αντικαταστήστε βούτυρο και επεξεργασμένα λίπη με ελαιόλαδο αντί να προσθέτετε θερμίδες."),
        ("Αποθηκεύστε το σωστά", "Κρατήστε το σε σκούρο γυαλί, δροσερά και μακριά από φως και θερμότητα για να διατηρηθούν οι πολυφαινόλες."),
    ],
    faq_h="Συχνές ερωτήσεις",
    faqs=[
        ("Κάνει καλό το ελαιόλαδο;",
         "Ναι, σε ισορροπημένη διατροφή. Το έξτρα παρθένο ελαιόλαδο είναι πηγή μονοακόρεστων λιπών και αντιοξειδωτικών πολυφαινολών, και είναι κεντρικό στη μεσογειακή διατροφή. Καλύτερα ως αντικατάσταση λιγότερο υγιεινών λιπών παρά ως επιπλέον θερμίδες."),
        ("Ποια τα οφέλη του έξτρα παρθένου ελαιόλαδου;",
         "Παρέχει ελαϊκό οξύ και πολυφαινόλες με αντιοξειδωτική και αντιφλεγμονώδη δράση. Στη μεσογειακή διατροφή η έρευνα το συνδέει με καλύτερη καρδιαγγειακή υγεία, και η ΕΕ επιτρέπει ισχυρισμό ότι οι πολυφαινόλες του προστατεύουν τα λιπίδια από την οξείδωση."),
        ("Πόσο ελαιόλαδο την ημέρα;",
         "Περίπου 2 κουταλιές τη μέρα ταιριάζουν σε ισορροπημένη διατροφή και αντανακλούν τις ποσότητες που μελετήθηκαν. Ο ισχυρισμός ΕΕ βασίζεται σε 20 g πλούσιου σε πολυφαινόλες ελαιόλαδου. Με μέτρο: μια κουταλιά ~120 kcal."),
        ("Τι είναι οι πολυφαινόλες του ελαιόλαδου;",
         "Αντιοξειδωτικές φυτικές ενώσεις όπως υδροξυτυροσόλη, τυροσόλη, ελαιοκανθάλη και ελευρωπαΐνη. Φέρουν μεγάλο μέρος της αντιοξειδωτικής και αντιφλεγμονώδους δράσης και είναι υψηλότερες σε φρέσκο έξτρα παρθένο."),
        ("Είναι καλύτερα ωμό το ελαιόλαδο;",
         "Εν μέρει ναι. Το μαγείρεμα υποβαθμίζει σταδιακά κάποιες πολυφαινόλες, οπότε η χρήση μέρους ωμού (ντρέσινγκ, τελείωμα) διατηρεί καλύτερα άρωμα και αντιοξειδωτικά."),
        ("Έξτρα παρθένο ή ραφιναρισμένο για την υγεία;",
         "Έξτρα παρθένο. Η ραφινάρισμα αφαιρεί τις περισσότερες πολυφαινόλες, που φέρουν μεγάλο μέρος των ειδικών οφελών. Το ραφιναρισμένο «ελαιόλαδο» και τα «ελαφριά» δίνουν ακόμη μονοακόρεστο λίπος αλλά λίγο από το αντιοξειδωτικό κλάσμα."),
        ("Βοηθά το ελαιόλαδο την καρδιά;",
         "Στη μεσογειακή διατροφή το έξτρα παρθένο συνδέεται με καλύτερη καρδιαγγειακή υγεία, και η μελέτη PREDIMED συνέδεσε αυτή τη διατροφή με το λάδι με λιγότερα μείζονα καρδιαγγειακά συμβάντα. Λειτουργεί ως μέρος υγιεινού προτύπου, όχι ως μεμονωμένη θεραπεία."),
        ("Κάνει καλό το ελαιόλαδο το πρωί με άδειο στομάχι;",
         "Είναι δημοφιλής συνήθεια, μάλλον αβλαβής σε μικρή ποσότητα, αλλά τα ειδικά οφέλη της ώρας δεν είναι καλά αποδεδειγμένα. Πιο πολύ μετράει η τακτική, μέτρια χρήση καλού λαδιού σε ισορροπημένη διατροφή, οποιαδήποτε ώρα."),
    ],
)

if __name__ == "__main__":
    print("Health pillar:")
    build(C)

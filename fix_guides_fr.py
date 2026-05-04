#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix French guide pages — replace placeholder content with real SEO content."""
import os, re

DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'guides')

GUIDES = {
    'bienfaits-sante-huile-olive.html': {
        'meta': "Découvrez les bienfaits prouvés de l'huile d'olive extra vierge : protection cardiovasculaire, polyphénols, anti-inflammatoire et longévité. Guide scientifique 2026.",
        'lede': "Ce que la science dit sur l'huile d'olive et votre santé.",
        'article': """
<p class="intro">L'huile d'olive extra vierge est l'un des aliments les plus étudiés en médecine préventive. Avec 73&nbsp;% d'acide oléique mono-insaturé et une concentration élevée en polyphénols, elle figure au cœur du régime méditerranéen — le modèle alimentaire associé à la plus grande longévité documentée.</p>

<h2>Protection cardiovasculaire : les preuves</h2>
<p>L'étude PREDIMED, menée sur 7&nbsp;447 personnes à haut risque, a démontré que la consommation régulière d'huile d'olive extra vierge réduit de 30&nbsp;% le risque d'infarctus et d'AVC. L'acide oléique abaisse le LDL oxydé — forme dangereuse du mauvais cholestérol — tout en préservant le HDL protecteur. Les polyphénols hydroxytyrosol et oleuropéine renforcent la paroi artérielle et combattent l'inflammation vasculaire chronique.</p>
<blockquote>« L'huile d'olive extra vierge est l'un des rares aliments pour lesquels nous disposons de preuves cliniques de réduction de la mortalité cardiovasculaire. » — Revue NEJM, 2013</blockquote>

<h3>Composants actifs et leurs rôles</h3>
<ul>
<li><strong>Acide oléique (oméga-9)</strong> : réduit le LDL et stabilise les membranes cellulaires</li>
<li><strong>Hydroxytyrosol</strong> : antioxydant classé parmi les plus puissants par l'EFSA</li>
<li><strong>Oléocanthal</strong> : inhibe COX-1 et COX-2 comme l'ibuprofène, sans effets secondaires</li>
<li><strong>Oleuropéine</strong> : effets anti-inflammatoires et antimicrobiens documentés</li>
<li><strong>Vitamine E</strong> : protège les lipides contre l'oxydation peroxydative</li>
</ul>

<h2>Effets anti-inflammatoires et neuroprotecteurs</h2>
<p>L'oléocanthal, présent uniquement dans les huiles fraîches de qualité, provoque la sensation de picotement caractéristique en gorge. Ce composé phénolique inhibe les mêmes enzymes inflammatoires que les anti-inflammatoires non stéroïdiens, mais sans les effets secondaires gastro-intestinaux. Des études longitudinales montrent que les populations méditerranéennes consommant plus de 20&nbsp;ml d'huile d'olive par jour présentent un déclin cognitif significativement plus lent, avec un risque d'Alzheimer réduit d'environ 40&nbsp;%.</p>

<h3>Apports recommandés selon les profils</h3>
<ul>
<li><strong>Usage général</strong> : 20–30&nbsp;ml par jour en assaisonnement cru</li>
<li><strong>Protection cardiovasculaire</strong> : 40&nbsp;ml/jour selon le protocole PREDIMED</li>
<li><strong>Usage culinaire</strong> : stable jusqu'à 210°C, idéal pour sauter et rissoler</li>
<li><strong>Usage cutané</strong> : quelques gouttes suffisent grâce à la haute densité nutritive</li>
</ul>
""",
        'faq': [
            ("Quelle quantité d'huile d'olive consommer par jour ?",
             "20 à 40&nbsp;ml par jour en remplacement d'autres matières grasses. L'étude PREDIMED utilisait 40&nbsp;ml comme dose thérapeutique, mais 20&nbsp;ml en assaisonnement quotidien apporte déjà des bénéfices mesurables."),
            ("L'huile d'olive cuite conserve-t-elle ses bienfaits ?",
             "Partiellement. L'acide oléique est stable jusqu'à 210°C. Les polyphénols résistent à une cuisson modérée (180°C) mais se dégradent en friture prolongée. Pour un effet santé maximal, privilégiez l'usage cru en finition."),
            ("Toutes les huiles d'olive se valent-elles en termes de santé ?",
             "Non. Seule l'huile extra vierge de haute qualité contient les polyphénols en concentration thérapeutique. Les huiles raffinées ont perdu l'essentiel de leurs composés bioactifs lors du traitement industriel. Cherchez une teneur en polyphénols supérieure à 250&nbsp;mg/kg."),
            ("L'huile d'olive aide-t-elle contre le diabète de type 2 ?",
             "Oui, des études montrent que l'acide oléique améliore la sensibilité à l'insuline et réduit la glycémie postprandiale. Le régime méditerranéen enrichi en huile d'olive est l'une des rares approches diététiques à avoir démontré un impact sur la prévention du diabète de type 2.")
        ]
    },
    'guide-degustation-huile-olive.html': {
        'meta': "Apprenez à déguster l'huile d'olive comme un expert : couleur, arômes, amertume, piquant et défauts. Méthode officielle COI et conseils pratiques.",
        'lede': "La méthode des professionnels pour identifier une grande huile.",
        'article': """
<p class="intro">Déguster l'huile d'olive ne s'improvise pas. Les jurés professionnels du Conseil Oléicole International (COI) suivent un protocole précis qui évalue trois attributs positifs — fruité, amer, piquant — et traque les défauts qui disqualifient une huile. Voici comment procéder.</p>

<h2>Le protocole de dégustation officiel</h2>
<p>La dégustation professionnelle utilise un verre bleu cobalt ou brun opaque pour masquer la couleur et ne pas influencer le jugement olfactif. On réchauffe le verre entre les paumes à 28°C environ pour libérer les composés volatils. L'évaluateur inspire profondément, note les arômes, puis prend une petite gorgée en aérant l'huile avec la bouche — technique appelée « stripping » — pour amplifier la perception des arômes rétronasaux.</p>
<blockquote>« La couleur de l'huile n'indique pas sa qualité. Une huile dorée peut être supérieure à une huile verte — et vice versa. »</blockquote>

<h3>Les trois attributs positifs à évaluer</h3>
<ul>
<li><strong>Fruité</strong> : intensité et type d'arômes végétaux — herbe fraîche, artichaut, amande, tomate, pomme</li>
<li><strong>Amer</strong> : goût amer sur la langue, signe de polyphénols — positif quand équilibré</li>
<li><strong>Piquant</strong> : sensation de brûlure en gorge due à l'oléocanthal — indicateur de fraîcheur et qualité</li>
</ul>

<h2>Identifier les défauts courants</h2>
<p>Les défauts organoleptiques classent une huile en « vierge » ou « lampante » (non consommable). Le <em>chômage</em> (rance humide, odeur de boue fermentée) vient d'olives stockées trop longtemps avant pressage. Le <em>rance</em> résulte d'une oxydation par la lumière ou la chaleur. Le <em>lie</em> indique un contact prolongé avec les dépôts de fruit après extraction. Une bonne huile extra vierge ne présente aucun de ces défauts à l'évaluation sensorielle.</p>

<h3>Profils aromatiques selon les variétés</h3>
<ul>
<li><strong>Arbequina</strong> (Espagne) : doux, amande, fruité mûr, faible amertume</li>
<li><strong>Picual</strong> (Espagne) : puissant, tomate, figue, amertume marquée</li>
<li><strong>Koroneiki</strong> (Grèce) : herbe fraîche, artichaut, piquant intense</li>
<li><strong>Frantoio</strong> (Italie) : artichaut, herbe, amer équilibré, très fruité</li>
<li><strong>Chemlali</strong> (Tunisie) : amande, pomme verte, doux et délicat</li>
</ul>
""",
        'faq': [
            ("Pourquoi les dégustateurs professionnels utilisent-ils des verres colorés ?",
             "Pour masquer la couleur de l'huile, qui ne prédit pas la qualité et pourrait biaiser l'évaluation. Le protocole COI impose des verres bleus ou bruns opaques pour que le jugement repose uniquement sur les arômes et le goût."),
            ("L'amertume et le piquant sont-ils des défauts ?",
             "Non, c'est l'inverse. Ce sont des attributs positifs dans le panel officiel. L'amertume indique la présence d'oleuropéine et de polyphénols ; le piquant révèle l'oléocanthal. Une huile sans amertume ni piquant est souvent une huile raffinée, ancienne ou de faible qualité."),
            ("Comment savoir si une huile est rances à la maison ?",
             "L'odeur de cire de bougie froide, de graisse de friture usée, ou de carton humide indique un rance. En bouche, elle laisse une sensation grasse persistante sans aucune fraîcheur. Ces huiles ne sont pas dangereuses mais ont perdu toute valeur gustative et nutritionnelle."),
            ("Peut-on déguster l'huile d'olive avec du pain ?",
             "Pour une dégustation sérieuse, non : le pain modifie la perception des arômes. Les professionnels utilisent du pain de mie neutre entre chaque huile pour nettoyer le palais, mais n'en mangent pas pendant l'évaluation proprement dite.")
        ]
    },
    'cuisiner-avec-huile-olive.html': {
        'meta': "Tout savoir pour cuisiner avec l'huile d'olive : point de fumée, températures, accords, friture et conservation à la chaleur. Conseils de chefs 2026.",
        'lede': "L'huile d'olive en cuisine : ce qui marche vraiment.",
        'article': """
<p class="intro">Contrairement à une idée reçue très répandue, l'huile d'olive extra vierge supporte parfaitement la cuisson. Son point de fumée de 190–210°C la rend adaptée à la quasi-totalité des techniques culinaires quotidiennes, et sa richesse en acide oléique la rend chimiquement plus stable que la plupart des huiles végétales.</p>

<h2>Températures et techniques de cuisson</h2>
<p>L'acide oléique (73&nbsp;% de la composition) est extrêmement résistant à l'oxydation thermique. Une étude publiée dans <em>Acta Scientific Nutritional Health</em> a comparé 10 huiles courantes sous chaleur et démontré que l'huile d'olive extra vierge produit le moins de composés polaires toxiques. Elle reste stable jusqu'à 180°C pour la cuisson quotidienne et jusqu'à 210°C en exposition brève. La fritue y est possible, mais une huile de friture dédiée reste plus économique pour les grandes quantités.</p>
<blockquote>« L'huile d'olive n'est pas réservée à la salade. En Italie et en Grèce, toute la cuisine — même les fritures — se fait à l'huile d'olive. » — Chef huilerie familiale toscane</blockquote>

<h3>Températures de référence</h3>
<ul>
<li><strong>Vinaigrette et finition</strong> : usage cru, arômes préservés à 100&nbsp;%</li>
<li><strong>Cuisson douce (légumes, œufs)</strong> : 100–140°C — idéal, zéro dégradation</li>
<li><strong>Sauté, rissoler</strong> : 160–180°C — parfaitement adapté</li>
<li><strong>Rôtissage au four</strong> : 180–200°C — stable, donne une belle coloration</li>
<li><strong>Friture</strong> : 175–190°C — possible, stable, mais économiquement moins optimal</li>
</ul>

<h2>Accords et utilisations créatives</h2>
<p>En cuisine méditerranéenne, l'huile d'olive remplace le beurre dans les gâteaux (texture plus moelleuse, conservation plus longue), la crème dans les purées (onctuosité sans lourdeur), et intervient dans les marinades pour attendrir les protéines. Le filet d'huile en finition sur un plat chaud est une technique clé : la chaleur libère les arômes du fruité sans les dénaturer. En dessert, un filet sur une panna cotta ou une glace à la vanille révèle des accords surprenants — l'huile d'olive de qualité apporte une rondeur et une complexité qui remplacent avantageusement le caramel.</p>

<h3>Règles d'accord huile–plat</h3>
<ul>
<li><strong>Huile douce, peu amère</strong> (Arbequina, Lucques) : poissons délicats, fruits de mer, desserts</li>
<li><strong>Huile médium, équilibrée</strong> (Frantoio, Aglandau) : viandes blanches, légumes rôtis, pâtes</li>
<li><strong>Huile intense, amère et piquante</strong> (Picual, Koroneiki) : viandes rouges, légumineuses, salades robustes</li>
<li><strong>Huile herbacée</strong> (récolte précoce) : bruschetta, soupes, plats provençaux</li>
</ul>
""",
        'faq': [
            ("L'huile d'olive perd-elle ses nutriments à la cuisson ?",
             "Partiellement. Les polyphénols les plus volatils se dégradent à partir de 180°C, mais l'acide oléique reste intact. L'huile conserve ses bienfaits lipidiques même cuite. Pour bénéficier de la totalité des polyphénols, ajoutez un filet d'huile crue en finition."),
            ("Peut-on réutiliser l'huile d'olive après friture ?",
             "Oui, 2 à 3 fois maximum si elle n'a pas bruni ni fumé. Filtrez-la à chaud pour éliminer les résidus alimentaires qui accélèrent la dégradation. Jetez-la dès qu'elle prend une teinte foncée ou dégage une odeur âcre."),
            ("L'huile d'olive convient-elle pour faire des mayonnaises ?",
             "Oui, mais une huile trop intense peut dominer la saveur de la mayonnaise. Utilisez une huile douce (Arbequina, délicatesse) pour les sauces froides, ou mélangez huile d'olive (30%) et huile neutre (70%) pour un résultat équilibré."),
            ("Comment cuisiner des pâtes à l'huile d'olive comme en Italie ?",
             "Faites cuire les pâtes al dente, réservez une tasse d'eau de cuisson, égouttez. Dans la poêle chaude, faites sauter ail et huile 30 secondes, ajoutez les pâtes, une louche d'eau de cuisson et mélangez vigoureusement. L'amidon lie l'huile à l'eau et crée une sauce crémeuse sans crème.")
        ]
    },
    'processus-fabrication-huile-olive.html': {
        'meta': "De l'olive à la bouteille : découvrez toutes les étapes de fabrication de l'huile d'olive extra vierge — récolte, broyage, malaxage, extraction et filtration.",
        'lede': "Comment naît une huile d'olive d'exception.",
        'article': """
<p class="intro">La qualité d'une huile d'olive extra vierge se construit à chaque étape du processus, de la maturité des olives à la mise en bouteille. Une seule erreur — récolte tardive, transport trop long, temperature de malaxage trop élevée — suffit à transformer un potentiel d'excellence en huile ordinaire.</p>

<h2>La récolte : première décision cruciale</h2>
<p>Les olives se récoltent entre octobre et janvier selon les régions et les variétés. Les huiles de <em>récolte précoce</em> (octobre–novembre), produites à partir d'olives encore vertes, contiennent jusqu'à 2&nbsp;× plus de polyphénols et offrent des arômes herbacés intenses. Les récoltes tardives (décembre–janvier), avec des olives à maturité complète, donnent des huiles plus douces et plus fruitées. La récolte manuelle ou par peigne mécanique est préférable : elle évite l'écrasement des fruits et la fermentation précoce.</p>
<blockquote>« Entre la récolte et le pressage, chaque heure compte. Nos olives entrent au moulin dans les 4 heures suivant la cueillette. » — Producteur AOP Baux-de-Provence</blockquote>

<h3>Étapes clés de la production</h3>
<ul>
<li><strong>Récolte</strong> : manuelle, peigne ou filet — l'écrasement dégrade la qualité</li>
<li><strong>Effeuilleuse et lavage</strong> : élimination des feuilles et impuretés dans les 4–6h max</li>
<li><strong>Broyage</strong> : meules traditionnelles (granite) ou broyeurs à marteaux modernes</li>
<li><strong>Malaxage</strong> : pâte brassée 20–40 min à 27°C max (extraction à froid)</li>
<li><strong>Centrifugation horizontale</strong> : sépare l'huile, l'eau végétale et les grignons</li>
<li><strong>Filtration</strong> : optionnelle mais recommandée pour la conservation</li>
</ul>

<h2>L'extraction à froid : le critère déterminant</h2>
<p>La mention « extraction à froid » garantit que la température de malaxage n'a pas dépassé 27°C. Au-delà, les enzymes qui dégradent les polyphénols s'activent, les arômes volatils s'évaporent, et le rendement augmente au détriment de la qualité. Un rendement plus élevé (plus d'huile par quintal d'olives) est souvent le signe d'une extraction à chaud — économiquement plus rentable mais qualitativement inférieure. Les meilleures huileries artisanales acceptent un rendement de 12–15&nbsp;% pour préserver l'intégralité des composés bioactifs.</p>

<h3>Facteurs qui distinguent l'excellence</h3>
<ul>
<li><strong>Délai récolte–pressage</strong> : moins de 6 heures pour les grandes huiles</li>
<li><strong>Température de malaxage</strong> : 27°C maximum</li>
<li><strong>Durée de malaxage</strong> : 25–35 minutes (ni trop court, ni trop long)</li>
<li><strong>Variété et maturité des olives</strong> : spécifiques à chaque terroir</li>
<li><strong>Conservation en inox sous azote</strong> : évite l'oxydation après extraction</li>
</ul>
""",
        'faq': [
            ("Quelle est la différence entre extraction à froid et première pression à froid ?",
             "'Première pression à froid' est une mention héritée des anciens pressoirs hydrauliques, aujourd'hui obsolète. 'Extraction à froid' est la mention officielle CE, garantissant une température de malaxage ≤ 27°C. Les deux termes indiquent une production à basse température, mais 'extraction à froid' est la terminologie réglementaire actuelle."),
            ("Combien d'olives faut-il pour produire un litre d'huile ?",
             "En moyenne 4 à 6 kg d'olives pour 1 litre d'huile, selon la variété, le stade de maturité et la méthode d'extraction. Les olives précoces (plus riches en eau, moins en huile) nécessitent parfois 7–8 kg. Les variétés tardives et gorgées d'huile peuvent descendre à 3–4 kg."),
            ("Les moulins à meules de pierre sont-ils meilleurs que les broyeurs modernes ?",
             "Débat légitime. Les meules de pierre broient plus doucement et préservent l'intégrité des cellules, ce qui favorise certains arômes. Mais elles s'échauffent et s'oxydent plus facilement. Les broyeurs à marteaux modernes, bien conduits, produisent des huiles d'aussi grande qualité avec une meilleure reproductibilité."),
            ("Pourquoi certaines huiles sont-elles troubles ?",
             "Le trouble (voile) est dû aux microparcelles de pulpe et aux cires naturelles de l'olive. Il disparaît par filtration ou décantation naturelle. Une huile non filtrée est plus riche en arômes à court terme, mais se conserve moins bien et peut développer des fermentations si elle n'est pas consommée rapidement.")
        ]
    },
    'terroirs-regions-huile-olive.html': {
        'meta': "Espagne, Italie, Grèce, Tunisie, France : découvrez les grands terroirs oléicoles du monde, leurs variétés emblématiques et leurs profils aromatiques distinctifs.",
        'lede': "Les grandes régions de l'or vert et ce qui les distingue.",
        'article': """
<p class="intro">Comme le vin, l'huile d'olive est profondément marquée par son terroir — sol, climat, altitude, variété d'olive et savoir-faire local. Un Koroneiki du Péloponnèse et un Arbequina de Catalogne sont deux expressions radicalement différentes du même fruit, façonnées par des millénaires d'adaptation.</p>

<h2>Les grandes régions productrices mondiales</h2>
<p>Le bassin méditerranéen concentre 95&nbsp;% de la production mondiale. L'Espagne est le premier producteur (45&nbsp;% de la production mondiale), principalement en Andalousie avec les variétés Picual, Hojiblanca et Arbequina. La Grèce, avec seulement 2&nbsp;% de la population mondiale, produit 10&nbsp;% de l'huile d'olive et consomme la plus grande quantité par habitant (20 litres/an). L'Italie, malgré une production plus faible, domine en valeur grâce à ses AOP prestigieuses. La Tunisie est le premier exportateur africain et mondial hors UE.</p>
<blockquote>« Chaque région donne à l'huile d'olive sa propre langue. Le Péloponnèse parle d'herbe coupée et d'artichaut ; la Toscane dit artichaut et poivre vert. »</blockquote>

<h3>Profils des grandes régions</h3>
<ul>
<li><strong>Andalousie (Espagne)</strong> : Picual puissant et robuste, fruité vert intense, excellent pour la conservation</li>
<li><strong>Catalogne (Espagne)</strong> : Arbequina douce, fruité mûr, amande, notes de pomme — idéale pour les débutants</li>
<li><strong>Toscane (Italie)</strong> : Frantoio et Moraiolo, herbe fraîche, artichaut, amertume et piquant marqués</li>
<li><strong>Péloponnèse (Grèce)</strong> : Koroneiki — petite olive, haute teneur en polyphénols, piquant intense</li>
<li><strong>Sfax (Tunisie)</strong> : Chemlali, amande douce, fruité mûr, grande finesse et douceur</li>
<li><strong>Provence (France)</strong> : AOP Vallée des Baux, Aglandau et Salonenque, herbe, amande, artichaut</li>
</ul>

<h2>L'importance des AOP et IGP</h2>
<p>Les Appellations d'Origine Protégée garantissent que l'huile est produite, transformée et conditionnée dans une zone géographique délimitée, avec des variétés et des méthodes définies par le cahier des charges. L'UE recense plus de 150 AOP oléicoles. Ces certifications protègent les producteurs contre la fraude et guident les consommateurs vers des huiles traçables et authentiques. En France, les AOP Nyons, Vallée des Baux-de-Provence, Haute-Provence et Nîmes sont les plus reconnues.</p>

<h3>Comment le terroir influence le goût</h3>
<ul>
<li><strong>Sol calcaire et sec</strong> : huiles intenses, riches en polyphénols</li>
<li><strong>Sol argileux et profond</strong> : huiles plus douces et fruitées</li>
<li><strong>Haute altitude (>400m)</strong> : maturité lente, arômes complexes et polyphénols élevés</li>
<li><strong>Proximité maritime</strong> : notes iodées subtiles, fruité plus léger</li>
<li><strong>Climat aride</strong> : stress hydrique = concentration aromatique plus élevée</li>
</ul>
""",
        'faq': [
            ("Quelle région produit la meilleure huile d'olive au monde ?",
             "Il n'existe pas de réponse absolue — c'est une question de préférence gustative. Les concours internationaux (Biol, EVOO World Rankings) couronnent régulièrement des huiles de Grèce, d'Espagne, d'Italie, du Maroc et d'Australie. La meilleure huile est celle qui correspond à votre palais et à vos usages."),
            ("Pourquoi les huiles grecques sont-elles si riches en polyphénols ?",
             "Trois facteurs : la variété Koroneiki (naturellement riche en phénols), les conditions climatiques méditerranéennes arides qui stressent l'olivier et concentrent les composés de défense, et la tradition de récolte précoce (olives encore vertes) dans de nombreuses régions du Péloponnèse et de Crète."),
            ("Les huiles d'olive françaises valent-elles le prix premium ?",
             "Oui, pour qui cherche des profils aromatiques uniques et une traçabilité maximale. Les productions françaises sont très faibles (5 000 à 10 000 tonnes/an contre 1,3 million en Espagne), donc forcément plus chères. Les AOP Baux-de-Provence et Nyons sont de véritables trésors gastronomiques."),
            ("Qu'est-ce qui différencie l'huile tunisienne des huiles européennes ?",
             "La Tunisie produit principalement des huiles douces et fruitées à base de Chemlali et Chétoui, souvent moins amères que les européennes. Les conditions climatiques sahéliennes créent un profil très différent : plus d'amande, moins de végétal, et une rondeur appréciée en cuisine orientale et dans les desserts.")
        ]
    },
    'comment-choisir-huile-olive.html': {
        'meta': "Comment choisir une bonne huile d'olive : décrypter l'étiquette, polyphénols, acidité, AOP, date de récolte et signaux de qualité. Guide d'achat expert 2026.",
        'lede': "Les critères qui séparent une grande huile d'une huile quelconque.",
        'article': """
<p class="intro">Le rayon huile d'olive d'un supermarché peut sembler homogène, mais les différences de qualité sont abyssales. Entre une huile à 3&nbsp;€ le litre et une huile artisanale à 25&nbsp;€, ce n'est pas l'étiquette qui change — c'est la composition chimique, le profil aromatique et les effets sur la santé.</p>

<h2>Lire l'étiquette : les informations clés</h2>
<p>La première distinction est la catégorie : seule la mention <strong>« Extra Vierge »</strong> garantit une acidité libre inférieure à 0,8&nbsp;% et l'absence de défauts organoleptiques. La catégorie « Vierge » (acidité ≤ 2&nbsp;%) présente de légers défauts ; la catégorie « Olive » ou « Huile d'olive » est un mélange d'huile raffinée et d'huile vierge, sans polyphénols significatifs. La date de récolte est plus informative que la date limite de consommation : une huile de la récolte précédente est encore bonne mais a perdu de ses arômes. Cherchez une récolte récente, idéalement de moins de 12 mois.</p>
<blockquote>« La date de récolte est l'indicateur de fraîcheur le plus honnête qu'un producteur puisse vous donner. »</blockquote>

<h3>Critères de sélection par ordre de priorité</h3>
<ul>
<li><strong>Mention « Extra Vierge »</strong> : critère minimum non négociable</li>
<li><strong>Date de récolte</strong> : préférez une récolte de moins de 12–18 mois</li>
<li><strong>AOP/DOP ou certification</strong> : garantit l'origine et les méthodes</li>
<li><strong>Teneur en polyphénols</strong> : idéalement > 250&nbsp;mg/kg (indiquée sur les bouteilles premium)</li>
<li><strong>Conditionnement</strong> : verre foncé ou bidon opaque — la lumière dégrade l'huile</li>
<li><strong>Origine unique</strong> : évitez « mélange de pays de l'UE » pour des huiles premium</li>
</ul>

<h2>Le prix comme indicateur de qualité</h2>
<p>Une huile d'olive extra vierge de qualité ne peut pas coûter moins de 8–10&nbsp;€ le litre en distribution traditionnelle. Le coût de production seul (récolte manuelle, transport, extraction à froid) dépasse 5&nbsp;€ par litre pour les petits producteurs. Les huiles à 3–4&nbsp;€ le litre en grande surface sont des huiles d'origine multiple, souvent de récolte ancienne, avec des profils polyphénoliques très bas. Ce n'est pas de la fraude — c'est simplement un produit différent, adapté à la cuisson de masse mais pas aux usages santé ou gastronomiques.</p>

<h3>Signaux d'alarme à fuir</h3>
<ul>
<li>Pas de date de récolte (seulement une date de péremption)</li>
<li>« Mélange de pays de l'UE et hors UE » sans précision</li>
<li>Prix inférieur à 7–8&nbsp;€ le litre pour une prémium supposée</li>
<li>Bouteille transparente exposée à la lumière</li>
<li>Absence de tout arôme à l'ouverture</li>
</ul>
""",
        'faq': [
            ("Une huile trouble est-elle un signe de qualité ?",
             "Pas nécessairement. Le voile indique une huile non filtrée, plus riche en arômes à court terme mais plus fragile à la conservation. C'est un choix du producteur, pas un critère de qualité absolu. Une huile filtrée et limpide peut être de bien meilleure qualité qu'une huile trouble mal conservée."),
            ("Les huiles bio sont-elles systématiquement meilleures ?",
             "La certification bio garantit l'absence de pesticides de synthèse, pas la qualité gustative ou la richesse en polyphénols. Une huile bio peut être médiocre si la récolte est tardive ou le processus bâclé. Une huile non-bio artisanale produite avec soin peut surpasser en qualité une huile bio industrielle."),
            ("Peut-on se fier aux concours et médailles sur l'étiquette ?",
             "Les grands concours (New York OLIVE OIL Competition, EVOO World Rankings, TerraOlivo) ont des processus rigoureux et constituent un indicateur fiable. Les petits concours locaux ou génériques ont moins de valeur discriminante. Une médaille d'or au NYIOOC ou au Biol est un signal sérieux de qualité."),
            ("Quelle est la différence entre une huile d'olive douce et intense ?",
             "L'intensité dépend de la variété, du stade de maturité et du terroir. 'Douce' signifie peu amère et peu piquante (Arbequina, huiles de récolte tardive) — idéale pour poissons, desserts, débutants. 'Intense' signifie amertume et piquant marqués (Picual, Koroneiki, récolte précoce) — idéale pour viandes, légumineuses et usage santé.")
        ]
    },
    'conservation-huile-olive-conseils.html': {
        'meta': "Comment conserver l'huile d'olive correctement : lumière, chaleur, air, contenants et durée. Évitez les erreurs qui dégradent votre huile en quelques semaines.",
        'lede': "Les règles de conservation pour préserver qualité et bienfaits.",
        'article': """
<p class="intro">L'huile d'olive est fragile. Trois ennemis la dégradent silencieusement : la lumière, la chaleur et l'oxygène. Une bouteille parfaite peut devenir rance en quelques semaines si elle est mal stockée. Voici les règles pour préserver vos huiles jusqu'à la dernière goutte.</p>

<h2>Les trois ennemis de l'huile d'olive</h2>
<p>La <strong>lumière</strong> déclenche des réactions photo-oxydatives qui dégradent les polyphénols et produisent des composés aldéhydiques responsables du goût rance. C'est pourquoi les bouteilles en verre foncé ou les bidons opaques sont indispensables — jamais de verre transparent sur un plan de travail exposé. La <strong>chaleur</strong> accélère l'oxydation et la dégradation des acides gras : ne stockez jamais près d'une cuisinière, d'un four ou en plein soleil. L'<strong>oxygène</strong> oxyde les lipides : refermez toujours le bouchon, et pour les grands contenants, transférez dans des bouteilles plus petites à mesure que vous consommez.</p>
<blockquote>« Une huile sortie tous les jours de son placard pour rester sur le plan de travail perd 30&nbsp;% de ses polyphénols en un mois. »</blockquote>

<h3>Conditions idéales de stockage</h3>
<ul>
<li><strong>Température</strong> : 14–18°C idéalement, maximum 20°C — cave ou placard intérieur frais</li>
<li><strong>Lumière</strong> : obscurité totale — bidon opaque ou placard fermé</li>
<li><strong>Oxygène</strong> : bouchon hermétique, bouteille remplie au maximum</li>
<li><strong>Humidité</strong> : endroit sec — l'humidité favorise les moisissures sur le bouchon</li>
<li><strong>Durée optimale</strong> : consommer dans les 18 mois après récolte</li>
</ul>

<h2>Peut-on conserver l'huile d'olive au réfrigérateur ?</h2>
<p>Le réfrigérateur n'est pas recommandé pour l'usage courant : l'huile cristallise en dessous de 7°C et se trouble à 10°C. Ce phénomène est réversible (il suffit de la remettre à température ambiante), mais les cycles froid–chaud répétés peuvent accélérer l'oxydation. Cependant, pour les huiles de grande valeur que vous consommez lentement, un stockage au réfrigérateur prolonge la durée de vie au-delà de 24 mois. Les producteurs de qualité stockent leurs réserves en cuves inox à température contrôlée (12–15°C) sous azote pour éviter tout contact avec l'oxygène.</p>

<h3>Durée de conservation selon les contenants</h3>
<ul>
<li><strong>Bidon de 3–5L hermétique</strong> : 24–30 mois si non ouvert</li>
<li><strong>Bouteille en verre foncé</strong> : 18–24 mois non ouverte, 3–6 mois après ouverture</li>
<li><strong>Carafe de cuisine ouverte</strong> : 2–4 semaines maximum</li>
<li><strong>Flacon pissette transparent</strong> : à éviter — dégradation en quelques jours à la lumière</li>
</ul>
""",
        'faq': [
            ("Comment savoir si mon huile d'olive est encore bonne ?",
             "Sentez-la : une bonne huile dégage des arômes fruités, végétaux ou d'amande. Si elle sent la cire de bougie, le carton humide ou la graisse rance, elle est oxydée. En bouche, si elle est plate, grasse et sans fraîcheur, elle a perdu ses polyphénols et ses arômes. Elle n'est pas dangereuse mais sans intérêt gustatif ni nutritionnel."),
            ("Peut-on congeler l'huile d'olive pour la conserver longtemps ?",
             "Techniquement oui — la congélation stoppe l'oxydation. Mais le processus de décongélation peut créer une séparation des composés si elle est trop rapide. Si vous congelez, décongelez lentement au réfrigérateur. Le résultat final est acceptable mais la texture et les arômes fins peuvent légèrement souffrir."),
            ("L'huile d'olive se périme-t-elle vraiment ?",
             "Elle ne 'pourrit' pas au sens alimentaire, mais elle rancit. Une huile rance ne présente pas de risque sanitaire grave, mais perd tout intérêt : plus de polyphénols, plus d'arômes, goût désagréable. Elle reste utilisable pour une vinaigrette basique mais ne vaut plus le prix payé pour une qualité premium."),
            ("Peut-on utiliser l'huile d'olive pour conserver des aliments (herbes, fromages) ?",
             "Oui, c'est une technique traditionnelle pour les herbes aromatiques, les fromages, les légumes grillés. L'huile crée une barrière anaérobie qui inhibe la croissance bactérienne aérobique. Cependant, l'ail frais conservé dans l'huile à température ambiante présente un risque de botulisme — ne conservez cet usage qu'au réfrigérateur et consommez dans la semaine.")
        ]
    },
    'huile-olive-bio-durabilite.html': {
        'meta': "Huile d'olive bio et durable : que garantissent vraiment les certifications, quel impact environnemental et comment choisir une huile respectueuse de l'olivier et de la planète.",
        'lede': "Durabilité et biologie oléicole : ce que ça signifie vraiment.",
        'article': """
<p class="intro">La filière oléicole est confrontée à un paradoxe : l'olivier est l'un des arbres les plus résistants et écologiquement vertueux qui soient, mais la pression économique et climatique pousse certains producteurs vers des pratiques intensives qui menacent cet équilibre millénaire.</p>

<h2>Ce que garantit (et ne garantit pas) la certification bio</h2>
<p>La certification biologique (AB en France, UE BIO, USDA Organic) garantit l'absence de pesticides de synthèse, d'herbicides chimiques et d'OGM. Elle impose des pratiques agronomiques respectueuses du sol et de la biodiversité. Ce qu'elle ne garantit pas : la qualité gustative, la richesse en polyphénols, ou le respect du bien-être animal. Une huile bio peut être produite industriellement à grande échelle avec des olives récoltées tardivement et mal extraites. Le label bio est nécessaire mais pas suffisant pour une qualité d'exception.</p>
<blockquote>« L'olivier pousse sans irrigation ni intrants chimiques depuis 3 000 ans. Le bio pour l'olivier, c'est en un sens son état naturel. »</blockquote>

<h3>Labels et certifications à connaître</h3>
<ul>
<li><strong>AB (Agriculture Biologique)</strong> : certifié sans pesticides de synthèse UE</li>
<li><strong>Demeter</strong> : biodynamique — exigences encore plus strictes que le bio standard</li>
<li><strong>AOP/DOP</strong> : origine et méthodes contrôlées — pas forcément bio, mais traçable</li>
<li><strong>Rainforest Alliance</strong> : gestion environnementale et sociale durable</li>
<li><strong>Fair Trade</strong> : équité commerciale pour les petits producteurs</li>
</ul>

<h2>L'impact environnemental de l'oliveraie</h2>
<p>Une oliveraie traditionnelle est un puits de carbone significatif : un hectare d'oliviers séquestre 2,5 à 4 tonnes de CO₂ par an. La culture extensive favorise la biodiversité (oiseaux, insectes, flore) et protège les sols de l'érosion grâce aux racines profondes. Les systèmes intensifs modernes — avec irrigation intensive, densités de plantation élevées (>1 000 arbres/ha contre 50–150 en extensif) et mécanisation totale — présentent un bilan carbone moins favorable et réduisent la biodiversité. En revanche, ils permettent une compétitivité prix qui rend l'huile d'olive accessible à tous.</p>

<h3>Choisir une huile réellement durable</h3>
<ul>
<li><strong>Oliveraies extensive traditionnelles</strong> : densité < 200 arbres/ha, sans irrigation</li>
<li><strong>Petits producteurs certifiés bio</strong> : impact minimal, traçabilité maximale</li>
<li><strong>Huiles locales et courtes distances</strong> : empreinte carbone transport réduite</li>
<li><strong>Conditionnement en vrac ou grand format</strong> : moins d'emballage par litre consommé</li>
<li><strong>Valorisation des grignons</strong> : le marc d'olive peut produire de l'énergie ou des cosmétiques</li>
</ul>
""",
        'faq': [
            ("La conversion au bio améliore-t-elle la qualité de l'huile ?",
             "Pas automatiquement. La qualité dépend davantage de la variété, du moment de récolte et de la maîtrise de l'extraction. Cependant, les producteurs bio sont souvent plus attentifs à l'ensemble de la chaîne, et l'absence d'intrants chimiques peut favoriser des profils aromatiques plus complexes dans les sols vivants."),
            ("L'huile d'olive est-elle un produit écologique ?",
             "Comparé à d'autres huiles végétales (palme, colza intensif, soja), l'olivier traditionnel a un excellent bilan environnemental : peu d'eau, peu d'intrants, puits de carbone efficace, longévité remarquable (certains arbres produisent depuis 1000 ans). L'agriculture intensive oléicole est en revanche plus discutable."),
            ("Que devient le grignon après l'extraction ?",
             "Le marc d'olive (grignon) est valorisé de plusieurs façons : en combustible pour les chaudières, en huile de grignon (extraction au solvane hexane pour les huiles alimentaires bas de gamme), en compost agricole, ou en cosmétiques (scrubs, savons). Les huileries modernes cherchent à valoriser 100% de la matière première."),
            ("Y a-t-il des certifications pour les huiles d'olive à haute teneur en polyphénols ?",
             "Oui. L'EFSA autorise une allégation santé pour les huiles contenant plus de 250mg/kg de polyphénols (hydroxytyrosol et ses dérivés). Certains producteurs font certifier cette teneur par laboratoire accrédité et l'affichent sur l'étiquette. C'est un gage sérieux de qualité fonctionnelle.")
        ]
    },
    'huile-olive-beaute-soins-peau.html': {
        'meta': "Huile d'olive en cosmétique : hydratation, anti-âge, soins visage et corps. Formules DIY, précautions et comparaison avec les huiles cosmétiques modernes.",
        'lede': "L'or vert au service de votre peau — depuis l'Antiquité.",
        'article': """
<p class="intro">Depuis que Cléopâtre se baignait dans un mélange d'huile d'olive et de lait, les femmes méditerranéennes ont utilisé l'huile d'olive comme soin de beauté complet. La science moderne valide ces usages ancestraux : squalène, tocophérols et polyphénols en font un actif cosmétique remarquable.</p>

<h2>Propriétés cosmétiques actives</h2>
<p>L'huile d'olive contient plusieurs composés directement bénéfiques pour la peau. Le <strong>squalène</strong> (0,3–1&nbsp;%) est un émollient naturel identique à celui produit par notre sébum — il pénètre sans résidu gras et hydrate en profondeur. Les <strong>tocophérols</strong> (vitamine E) protègent les membranes cellulaires contre l'oxydation des radicaux libres, mécanisme central du vieillissement cutané. L'<strong>hydroxytyrosol</strong> exerce une action anti-inflammatoire documentée qui calme les peaux sensibles et réactives. Ces propriétés sont présentes dans l'huile extra vierge de qualité — pas dans les huiles raffinées qui ont perdu ces composés bioactifs.</p>
<blockquote>« L'huile d'olive extra vierge contient plus de 200 composés phytochimiques actifs, dont beaucoup ont une efficacité cosmétique comparable aux actifs synthétiques haut de gamme. »</blockquote>

<h3>Usages cosmétiques les plus efficaces</h3>
<ul>
<li><strong>Démaquillant</strong> : dissout maquillage gras et waterproof sans agresser — même contour des yeux</li>
<li><strong>Baume lèvres</strong> : quelques gouttes pures sur les lèvres gercées — effet immédiat</li>
<li><strong>Soin cuticules</strong> : massage quotidien qui nourrit et assouplit la peau autour des ongles</li>
<li><strong>Après-soleil</strong> : apaise les rougeurs et nourrit les peaux desséchées par le soleil</li>
<li><strong>Masque nourrissant</strong> : 2 cuillères sur le visage sec, 15 minutes, rinçage eau tiède</li>
<li><strong>Huile de corps</strong> : appliquée sur peau légèrement humide après la douche</li>
</ul>

<h2>Précautions et contre-indications</h2>
<p>L'huile d'olive n'est pas adaptée à tous les types de peau. Son indice comédonique modéré (2 sur 5) la rend déconseillée pour les peaux mixtes à grasses ou acnéiques : elle peut boucher les pores et aggraver les comédons. Pour ces profils, privilégiez des huiles plus légères (jojoba, rosier muscat, noisette). Les peaux normales à sèches, en revanche, tolèrent et apprécient l'huile d'olive en soin occlusif nocturne. En cas d'eczéma ou de dermatite, consultez un dermatologue avant usage systématique — des études montrent des résultats contradictoires selon les individus.</p>

<h3>Formules DIY simples et efficaces</h3>
<ul>
<li><strong>Gommage corps</strong> : 3 c.s. huile d'olive + 2 c.s. sucre de canne + zeste de citron</li>
<li><strong>Masque cheveux</strong> : huile d'olive tiède sur longueurs, 30 min sous serviette chaude, shampooing</li>
<li><strong>Crème mains</strong> : mélanger huile d'olive, cire d'abeille fondue et huile essentielle de lavande</li>
<li><strong>Bain de pieds nourrissant</strong> : eau tiède + huile d'olive + quelques gouttes tea tree</li>
</ul>
""",
        'faq': [
            ("L'huile d'olive est-elle bonne pour le visage tous types de peau ?",
             "Non. Elle convient aux peaux sèches, normales et matures. Elle est déconseillée aux peaux grasses et acnéiques en raison de son indice comédonique modéré. Pour les peaux sensibles, testez sur une petite zone avant usage étendu. L'huile de jojoba est souvent un meilleur choix universel."),
            ("Peut-on remplacer sa crème hydratante par de l'huile d'olive ?",
             "Partiellement. L'huile d'olive est un excellent émollient (elle ramollit et nourrit) mais n'est pas un humectant (elle n'attire pas l'eau dans la peau comme l'acide hyaluronique). Pour une hydratation optimale : appliquez sur peau légèrement humide après la douche, ou layez avec un sérum hydratant d'abord."),
            ("Quelle huile d'olive choisir pour un usage cosmétique ?",
             "Extra vierge de qualité supérieure, avec date de récolte récente. Les huiles cosmétiques à base d'huile d'olive raffinée ont perdu leurs composés bioactifs — un comble pour un usage beauté. Préférez une huile de même qualité que celle que vous mettriez dans votre assiette."),
            ("L'huile d'olive aide-t-elle contre les vergetures ?",
             "Elle peut aider en prévention chez les femmes enceintes, car elle nourrit et assouplit la peau, améliorant son élasticité. Sur vergetures déjà formées (cicatrices blanches), l'effet est limité — aucune huile végétale ne peut effacer des vergetures établies. Les meilleurs résultats préventifs s'obtiennent avec une application quotidienne dès le début de la grossesse.")
        ]
    },
    'histoire-culture-huile-olive.html': {
        'meta': "L'histoire de l'huile d'olive de l'Antiquité à aujourd'hui : mythologie grecque, Rome antique, Moyen Âge, commerce méditerranéen et rôle culturel universel.",
        'lede': "5 000 ans d'histoire dans chaque goutte d'huile d'olive.",
        'article': """
<p class="intro">Aucun autre aliment n'a joué un rôle aussi central dans l'histoire humaine que l'huile d'olive. Monnaie d'échange, combustible sacré, médicament, cosmétique et aliment : l'huile d'olive a accompagné la naissance des civilisations méditerranéennes pendant plus de cinq millénaires.</p>

<h2>Des origines mythiques à la réalité archéologique</h2>
<p>L'olivier cultivé (<em>Olea europaea</em>) est issu d'un processus de domestication qui remonte à 6 000 avant J.-C. en Anatolie et au Levant. Les premières traces d'extraction d'huile remontent à 4 000 av. J.-C. à Haïfa (actuel Israël). Les Grecs anciens firent de l'olivier un symbole sacré : dans la mythologie, c'est Athéna qui offrit l'olivier à Athènes, battant Poséidon dans le concours pour la protection de la cité. Les vainqueurs olympiques recevaient une couronne de branches d'olivier sauvage — l'<em>kotinos</em> — et des amphores d'huile d'olive de l'Attique comme prix.</p>
<blockquote>« L'olivier est à lui seul la civilisation méditerranéenne. Là où pousse l'olivier, l'homme s'installe, cultive et crée. » — Fernand Braudel, historien</blockquote>

<h3>Grandes étapes de l'histoire oléicole</h3>
<ul>
<li><strong>4 000 av. J.-C.</strong> : premières traces d'extraction au Levant et en Crète minoenne</li>
<li><strong>776 av. J.-C.</strong> : l'huile d'olive prime aux premiers Jeux olympiques</li>
<li><strong>IIe siècle av. J.-C.</strong> : Rome devient le plus grand importateur mondial d'huile d'olive</li>
<li><strong>Ier siècle</strong> : l'Hispanie (Espagne) dépasse la Grèce en volume de production</li>
<li><strong>VIIe siècle</strong> : l'expansion arabe diffuse l'olivier en Afrique du Nord et en Espagne</li>
<li><strong>XVe siècle</strong> : les conquistadors implantent l'olivier en Amérique latine</li>
</ul>

<h2>L'huile d'olive dans les grandes religions et cultures</h2>
<p>L'huile d'olive transcende les cultures et les religions. Dans la Bible, l'olive est symbole de paix (la colombe de Noé rapporte un rameau d'olivier). L'Église catholique utilise l'huile d'olive dans tous ses sacrements — baptême, confirmation, extrême-onction. Dans l'islam, le Coran mentionne l'olivier comme arbre béni. En Grèce et en Italie, les rituels liés à la récolte des olives restent des moments de cohésion sociale et familiale, transmis de génération en génération. L'huile d'olive est bien plus qu'un aliment : c'est un langage culturel partagé par 500 millions de personnes.</p>

<h3>L'olivier comme patrimoine vivant</h3>
<ul>
<li>Certains oliviers en Sardaigne, Crète et Palestine ont plus de <strong>2 000 ans</strong></li>
<li>L'olivier de Vouves en Crète est estimé à <strong>3 000–4 000 ans</strong> et produit toujours des olives</li>
<li>Les oliveraies historiques sont inscrites au <strong>patrimoine mondial de l'UNESCO</strong> en Grèce et au Portugal</li>
<li>Le <strong>régime méditerranéen</strong> est lui-même inscrit au patrimoine culturel immatériel de l'UNESCO</li>
</ul>
""",
        'faq': [
            ("Quel pays a inventé l'huile d'olive ?",
             "La domestication de l'olivier est née simultanément dans plusieurs régions du Moyen-Orient et de la Méditerranée orientale — Syrie, Liban, Palestine, Crète — entre 6000 et 4000 av. J.-C. Il n'y a pas de 'inventeur' unique : c'est une découverte progressive partagée par plusieurs civilisations du croissant fertile."),
            ("Comment les Romains utilisaient-ils l'huile d'olive ?",
             "Les Romains avaient une consommation quotidienne d'huile d'olive estimée à 20–40 litres par personne et par an. Ils l'utilisaient pour cuisiner, s'éclairer (lampes à huile), se parfumer (mélangée aux herbes aromatiques), se laver (strigile + huile en guise de savon), et comme médicament. Rome importait massivement depuis l'Hispanie et l'Afrique du Nord."),
            ("Pourquoi le rameau d'olivier est-il symbole de paix ?",
             "Cette symbolique remonte à la Genèse biblique (la colombe rapportant un rameau d'olivier après le Déluge, signant la fin du courroux divin) et à la tradition grecque (l'olivier était planté dans les lieux sacrés où la violence était interdite). L'ONU utilise le rameau d'olivier dans son emblème depuis 1945."),
            ("Y a-t-il de très vieux oliviers encore productifs ?",
             "Oui. L'olivier de Vouves en Crète, estimé à 3 000–4 000 ans (l'un des plus vieux organismes vivants d'Europe), produit encore des olives récoltées annuellement. En Sardaigne, plusieurs oliviers millénaires sont actifs. Les oliviers 'Ses Oliveres Velles' à Majorque sont estimés à 1 000 ans et encore productifs.")
        ]
    },
    'difference-extra-vierge-vierge.html': {
        'meta': "Différence entre huile d'olive extra vierge, vierge et ordinaire : acidité, défauts, polyphénols, usage et prix. Tableau comparatif complet.",
        'lede': "Extra vierge, vierge, olive : ce que ces catégories signifient vraiment.",
        'article': """
<p class="intro">L'étiquette « huile d'olive » recouvre des réalités très différentes. Le règlement européen CE 2568/91 définit plusieurs catégories avec des critères chimiques et organoleptiques précis. Comprendre ces distinctions permet de faire des achats éclairés et d'utiliser chaque type au bon usage.</p>

<h2>Les catégories officielles et leurs critères</h2>
<p>L'<strong>huile d'olive extra vierge</strong> est le sommet de la hiérarchie : acidité libre maximale de 0,8&nbsp;%, aucun défaut organoleptique détectable, et présence de polyphénols en quantité significative. C'est la seule catégorie qui mérite l'investissement pour un usage santé et gastronomique. L'<strong>huile d'olive vierge</strong> accepte une acidité jusqu'à 2&nbsp;% et peut présenter de légers défauts perceptibles — elle reste une huile issue de pressage mécanique, sans raffinage, mais d'une qualité inférieure. L'<strong>huile d'olive</strong> (tout court) est un mélange d'huile raffinée (inodore, insipide) et d'huile vierge pour lui apporter un peu d'arôme : pratiquement aucun polyphénol, acidité maximale de 1&nbsp;%.</p>
<blockquote>« Le raffinage élimine les défauts mais aussi tous les composés bioactifs qui font la valeur santé de l'huile d'olive. »</blockquote>

<h3>Tableau comparatif des catégories</h3>
<ul>
<li><strong>Extra vierge</strong> : acidité ≤ 0,8&nbsp;%, zéro défaut, polyphénols élevés, usage cru et cuisson</li>
<li><strong>Vierge</strong> : acidité ≤ 2&nbsp;%, légers défauts tolérés, polyphénols moyens, usage cuisson</li>
<li><strong>Vierge courante</strong> : acidité ≤ 3,3&nbsp;% (usage industriel, pas en commerce de détail UE)</li>
<li><strong>Lampante</strong> : acidité > 3,3&nbsp;%, non comestible brut, destinée au raffinage</li>
<li><strong>Huile d'olive raffinée</strong> : issue de lampante raffiné, acidité ≤ 0,3&nbsp;%, sans goût ni arôme</li>
<li><strong>Huile d'olive</strong> : mélange raffinée + vierge, acidité ≤ 1&nbsp;%, peu de polyphénols</li>
</ul>

<h2>Pourquoi les fraudes existent-elles ?</h2>
<p>La différence de prix entre une vraie extra vierge (8–30&nbsp;€/L) et une huile d'olive ordinaire (2–5&nbsp;€/L) crée une tentation de fraude. Des scandales récurrents ont révélé des huiles étiquetées « extra vierge » qui contenaient en réalité des huiles raffinées ou des huiles d'autres origines. L'Union Européenne a renforcé les contrôles depuis 2012 avec des analyses chimiques obligatoires (indice K232, K270, delta-K, composition en acides gras). Pour vous protéger, privilégiez les huiles avec AOP/DOP, les producteurs indépendants traçables, et les prix cohérents avec la qualité annoncée.</p>

<h3>Comment choisir selon l'usage</h3>
<ul>
<li><strong>Finition, salade, trempage</strong> : extra vierge de qualité, fruité intense</li>
<li><strong>Cuisson quotidienne (sauté, rôti)</strong> : extra vierge courante ou vierge — stable à la chaleur</li>
<li><strong>Friture grande quantité</strong> : huile d'olive ordinaire — moins chère, point de fumée similaire</li>
<li><strong>Cosmétique, soin</strong> : extra vierge uniquement — les polyphénols sont les actifs clés</li>
</ul>
""",
        'faq': [
            ("L'acidité indiquée sur l'étiquette prédit-elle la qualité ?",
             "Partiellement. Une acidité très basse (< 0,3%) est nécessaire pour une grande huile, mais pas suffisante. Une huile raffinée a une acidité quasi nulle mais zéro polyphénol. L'acidité reflète la qualité des olives à la récolte et la rapidité de pressage, mais doit être lue avec d'autres critères."),
            ("Peut-on faire la différence entre extra vierge et vierge en dégustation ?",
             "Un dégustateur entraîné peut détecter les légers défauts d'une huile vierge (légère fermentation, légère lie, léger rance). Pour le consommateur occasionnel, la différence est subtile sur des échantillons frais. Ce qui est clairement perceptible : l'intensité aromatique, l'amertume et le piquant sont systématiquement plus marqués dans les extra vierge de qualité."),
            ("L'huile d'olive raffinée est-elle mauvaise pour la santé ?",
             "Elle n'est pas nocive, mais ne présente pas les bénéfices santé de l'extra vierge. Sans polyphénols ni oléocanthal, c'est une huile riche en acide oléique (bon) mais dépourvue des antioxydants et anti-inflammatoires qui font la spécificité santé de l'huile d'olive extra vierge. Utilisable pour la cuisson, elle ne remplace pas l'extra vierge dans un usage santé."),
            ("Qu'est-ce que la 'première pression à froid' ?",
             "C'est une mention historique des anciens pressoirs hydrauliques à pierres, aujourd'hui remplacés par la centrifugation continue. La mention réglementaire actuelle est 'extraction à froid' (< 27°C). Les deux termes indiquent une production sans chauffage, mais 'première pression' n'a plus de sens technique avec les équipements modernes.")
        ]
    },
    'tendances-marche-huile-olive-2026.html': {
        'meta': "Marché de l'huile d'olive en 2026 : prix records, crise climatique, tendances premium, nouveaux marchés et perspectives pour producteurs et acheteurs.",
        'lede': "Comprendre le marché mondial de l'huile d'olive en 2026.",
        'article': """
<p class="intro">Le marché mondial de l'huile d'olive traverse une période de transformation sans précédent. Les récoltes historiquement basses de 2023 et 2024 ont propulsé les prix à des niveaux jamais vus depuis 30 ans, restructurant la filière et accélérant des tendances de fond qui redéfinissent ce que les consommateurs achètent et ce que les producteurs cultivent.</p>

<h2>La crise des prix : causes et conséquences</h2>
<p>Entre 2022 et 2024, le prix de l'huile d'olive en vrac sur les marchés espagnols a triplé, passant de 3–4&nbsp;€/kg à 8–9&nbsp;€/kg. Plusieurs facteurs se sont cumulés : la sécheresse record en Andalousie (−50&nbsp;% de production en 2023), le gel tardif en Italie, les maladies liées à la Xylella fastidiosa dans les Pouilles, et une demande mondiale en constante hausse notamment en Asie et en Amérique du Nord. Cette flambée a provoqué la montée en puissance des producteurs non-européens — Maroc, Turquie, Argentine, Chili, Australie — qui comblent partiellement le déficit européen.</p>
<blockquote>« La crise climatique a transformé le marché de l'huile d'olive : les producteurs qui investissent dans la résilience climatique et la qualité premium sortiront gagnants. »</blockquote>

<h3>Chiffres clés du marché 2025–2026</h3>
<ul>
<li><strong>Production mondiale</strong> : environ 2,5 millions de tonnes (contre 3,3 M en 2021)</li>
<li><strong>Espagne</strong> : 60&nbsp;% de la production UE, mais fortement impactée par la sécheresse</li>
<li><strong>Maroc</strong> : +40&nbsp;% de surface plantée ces 10 dernières années, nouveau poids lourd</li>
<li><strong>Prix consommateur UE</strong> : +80–120&nbsp;% entre 2022 et 2024</li>
<li><strong>Marchés en forte croissance</strong> : Chine (+15&nbsp;%/an), États-Unis (+8&nbsp;%/an), Brésil (+12&nbsp;%/an)</li>
</ul>

<h2>Les tendances structurelles pour 2026 et au-delà</h2>
<p>Au-delà de la crise conjoncturelle, trois tendances de fond transforment le marché. Premièrement, la <strong>premiumisation</strong> : les consommateurs réduisent leurs volumes mais achètent mieux, avec une demande croissante pour les huiles AOP, les mono-variétales et les récoltes précoces. Deuxièmement, la <strong>diversification géographique</strong> : Australia, Afrique du Sud, Californie et Chili investissent massivement dans la production et gagnent des parts de marché avec des profils aromatiques différents. Troisièmement, la <strong>technologie</strong> : capteurs IoT dans les oliveraies, intelligence artificielle pour optimiser la récolte, blockchain pour la traçabilité — la filière se modernise rapidement.</p>

<h3>Opportunités identifiées pour 2026</h3>
<ul>
<li><strong>Segment ultra-premium</strong> : huiles > 40&nbsp;€/L, marché de niche en forte croissance</li>
<li><strong>DTC (vente directe producteur)</strong> : abonnements, coffrets et e-commerce en hausse</li>
<li><strong>Huiles fonctionnelles</strong> : haute teneur en polyphénols certifiée, marché santé</li>
<li><strong>Nouveaux producteurs</strong> : Maroc, Turquie et Australie gagnent en qualité et en notoriété</li>
<li><strong>Éducation consommateur</strong> : ateliers de dégustation, certifications sommelier olive en expansion</li>
</ul>
""",
        'faq': [
            ("Pourquoi le prix de l'huile d'olive a-t-il autant augmenté ?",
             "Combinaison de sécheresses record en Espagne (principale productrice mondiale), gel tardif en Italie, Xylella dans les Pouilles, et demande mondiale en hausse. Entre 2022 et 2024, la production européenne a chuté de 30–40% tandis que la demande continuait de croître, notamment en Asie et en Amérique du Nord."),
            ("Le prix va-t-il baisser en 2026 ?",
             "Les perspectives de récolte 2025–2026 sont plus favorables grâce à de meilleures précipitations. Les prix devraient se détendre mais rester au-dessus des niveaux pré-2022. La dépendance structurelle aux conditions climatiques méditerranéennes signifie que la volatilité des prix reste une réalité durable de cette filière."),
            ("Quels sont les nouveaux pays producteurs à surveiller ?",
             "Le Maroc (Meknès, Marrakech), l'Australie (Margaret River, Riverina), l'Argentine (Mendoza), le Chili et la Californie. Ces producteurs bénéficient de climages méditerranéens, investissent massivement et commencent à concourir — et gagner — dans les grands concours internationaux face aux producteurs européens établis."),
            ("Comment la technologie transforme-t-elle la filière ?",
             "Sur trois axes : la production (capteurs sol et météo, irrigation de précision, drones pour surveiller la santé des oliviers), la qualité (spectroscopie NIR pour analyser les polyphénols en temps réel au moulin), et la traçabilité (blockchain pour certifier l'origine de la graine à la bouteille). L'IA permet aussi d'optimiser les dates de récolte variété par variété.")
        ]
    },
}


GUIDE_TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{meta}">
    <meta name="robots" content="index, follow">
    <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%232E4A40'/%3E%3Cpath fill='%23F2D8C4' d='M16 5.5S9.5 14 9.5 19a6.5 6.5 0 0013 0c0-5-6.5-13.5-6.5-13.5z'/%3E%3C/svg%3E" type="image/svg+xml">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Space+Mono&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../assets/seo.css">
    {hreflang}
</head>
<body>

<nav class="site-nav">
    <div class="container">
        <a href="../index.html" class="logo">L'OR VERT</a>
        <div class="lang-switch">
            {lang_switch}
        </div>
    </div>
</nav>

<header class="page-hero">
    <div class="container">
        <div class="breadcrumb">
            <a href="../index.html">Accueil</a> &raquo; <a href="../index.html#guides">Guides</a> &raquo; {h1}
        </div>
        <h1>{h1}</h1>
        <p class="lede">{lede}</p>
        <div class="meta">Publication&nbsp;: Avril 2026 &middot; 8&nbsp;min de lecture</div>
    </div>
</header>

<main class="container">
    <article class="guide">
        {article}
    </article>

    <section class="faq">
        <h2>Questions Fréquentes</h2>
        {faq}
    </section>
</main>

<section class="related">
    <div class="container">
        <h2>Guides Associés</h2>
        <div class="grid">
            {related}
        </div>
    </div>
</section>

<footer class="site-footer">
    <div class="container">
        <h3>L'Or Vert</h3>
        <p>&Eacute;tude de March&eacute; Huile d'Olive 2026. Analyse des tendances et opportunit&eacute;s premium.</p>
        <div class="copyright">&copy; 2026 &mdash; Tous droits r&eacute;serv&eacute;s</div>
    </div>
</footer>

</body>
</html>"""

# Map of filename -> title (for h1 extraction and related links)
GUIDE_TITLES_FR = {
    'bienfaits-sante-huile-olive.html': "Les Bienfaits de l'Huile d'Olive pour la Santé",
    'guide-degustation-huile-olive.html': "Guide Complet de Dégustation : Apprendre à Goûter",
    'cuisiner-avec-huile-olive.html': "Cuisiner à l'Huile d'Olive : Secrets de Chefs",
    'processus-fabrication-huile-olive.html': "De l'Arbre à la Bouteille : Le Processus de Fabrication",
    'terroirs-regions-huile-olive.html': "Terroirs et Régions : Les Grands Origines de l'Huile d'Olive",
    'comment-choisir-huile-olive.html': "Comment Choisir la Meilleure Huile d'Olive",
    'conservation-huile-olive-conseils.html': "Conseils de Conservation : Préserver Qualité et Bienfaits",
    'huile-olive-bio-durabilite.html': "Huile d'Olive Bio et Durabilité : Ce qu'il Faut Savoir",
    'huile-olive-beaute-soins-peau.html': "Huile d'Olive en Beauté : Soins Peau et Cosmétiques Naturels",
    'histoire-culture-huile-olive.html': "Histoire et Culture de l'Huile d'Olive : 5 000 Ans de Civilisation",
    'difference-extra-vierge-vierge.html': "Extra Vierge vs Vierge : Comprendre les Catégories d'Huile d'Olive",
    'tendances-marche-huile-olive-2026.html': "Tendances du Marché de l'Huile d'Olive 2026",
}

GUIDE_HREFLANG = {
    'bienfaits-sante-huile-olive.html': (
        'https://huiledefes.com/guides/bienfaits-sante-huile-olive.html',
        'https://huiledefes.com/guides/health-benefits-olive-oil.html',
        'https://huiledefes.com/guides/benefici-salute-olio-oliva.html',
        'https://huiledefes.com/guides/ofeli-igia-elaio-lado.html',
    ),
    'guide-degustation-huile-olive.html': (
        'https://huiledefes.com/guides/guide-degustation-huile-olive.html',
        'https://huiledefes.com/guides/olive-oil-tasting-guide.html',
        'https://huiledefes.com/guides/guida-degustazione-olio-oliva.html',
        'https://huiledefes.com/guides/odigos-dokimis-elaio-ladou.html',
    ),
    'cuisiner-avec-huile-olive.html': (
        'https://huiledefes.com/guides/cuisiner-avec-huile-olive.html',
        'https://huiledefes.com/guides/cooking-with-olive-oil.html',
        'https://huiledefes.com/guides/cucinare-con-olio-oliva.html',
        'https://huiledefes.com/guides/magirema-me-elaio-lado.html',
    ),
    'processus-fabrication-huile-olive.html': (
        'https://huiledefes.com/guides/processus-fabrication-huile-olive.html',
        'https://huiledefes.com/guides/olive-oil-production-process.html',
        'https://huiledefes.com/guides/processo-produzione-olio-oliva.html',
        'https://huiledefes.com/guides/diadikasía-paragogís-elaio-ladou.html',
    ),
    'terroirs-regions-huile-olive.html': (
        'https://huiledefes.com/guides/terroirs-regions-huile-olive.html',
        'https://huiledefes.com/guides/olive-oil-terroirs-and-regions.html',
        'https://huiledefes.com/guides/terroir-e-regioni-olio-oliva.html',
        'https://huiledefes.com/guides/terroirs-kai-periochés-elaio-ladou.html',
    ),
    'comment-choisir-huile-olive.html': (
        'https://huiledefes.com/guides/comment-choisir-huile-olive.html',
        'https://huiledefes.com/guides/how-to-choose-best-olive-oil.html',
        'https://huiledefes.com/guides/come-scegliere-migliore-olio-oliva.html',
        'https://huiledefes.com/guides/pos-na-dialexete-to-kalitero-elaio-lado.html',
    ),
    'conservation-huile-olive-conseils.html': (
        'https://huiledefes.com/guides/conservation-huile-olive-conseils.html',
        'https://huiledefes.com/guides/olive-oil-storage-tips.html',
        'https://huiledefes.com/guides/consigli-conservazione-olio-oliva.html',
        'https://huiledefes.com/guides/simvoules-sintirisis-elaio-ladou.html',
    ),
    'huile-olive-bio-durabilite.html': (
        'https://huiledefes.com/guides/huile-olive-bio-durabilite.html',
        'https://huiledefes.com/guides/organic-and-sustainable-olive-oil.html',
        'https://huiledefes.com/guides/olio-oliva-biologico-e-sostenibile.html',
        'https://huiledefes.com/guides/viologiko-kai-viosimo-elaio-lado.html',
    ),
    'huile-olive-beaute-soins-peau.html': (
        'https://huiledefes.com/guides/huile-olive-beaute-soins-peau.html',
        'https://huiledefes.com/guides/olive-oil-beauty-and-skincare.html',
        'https://huiledefes.com/guides/olio-oliva-bellezza-cura-pelle.html',
        'https://huiledefes.com/guides/elaio-lado-omorfia-kai-derma.html',
    ),
    'histoire-culture-huile-olive.html': (
        'https://huiledefes.com/guides/histoire-culture-huile-olive.html',
        'https://huiledefes.com/guides/history-and-culture-of-olive-oil.html',
        'https://huiledefes.com/guides/storia-e-cultura-dell-olio-oliva.html',
        'https://huiledefes.com/guides/istoria-kai-politismos-elaio-ladou.html',
    ),
    'difference-extra-vierge-vierge.html': (
        'https://huiledefes.com/guides/difference-extra-vierge-vierge.html',
        'https://huiledefes.com/guides/extra-virgin-vs-virgin-olive-oil.html',
        'https://huiledefes.com/guides/differenza-extra-vergine-e-vergine.html',
        'https://huiledefes.com/guides/diafora-extra-partheno-kai-partheno.html',
    ),
    'tendances-marche-huile-olive-2026.html': (
        'https://huiledefes.com/guides/tendances-marche-huile-olive-2026.html',
        'https://huiledefes.com/guides/olive-oil-market-trends-2026.html',
        'https://huiledefes.com/guides/tendenze-mercato-olio-oliva-2026.html',
        'https://huiledefes.com/guides/taseis-agoras-elaio-ladou-2026.html',
    ),
}

LANG_SWITCH_FILENAMES = {
    'bienfaits-sante-huile-olive.html': ('bienfaits-sante-huile-olive.html', 'health-benefits-olive-oil.html', 'benefici-salute-olio-oliva.html', 'ofeli-igia-elaio-lado.html'),
    'guide-degustation-huile-olive.html': ('guide-degustation-huile-olive.html', 'olive-oil-tasting-guide.html', 'guida-degustazione-olio-oliva.html', 'odigos-dokimis-elaio-ladou.html'),
    'cuisiner-avec-huile-olive.html': ('cuisiner-avec-huile-olive.html', 'cooking-with-olive-oil.html', 'cucinare-con-olio-oliva.html', 'magirema-me-elaio-lado.html'),
    'processus-fabrication-huile-olive.html': ('processus-fabrication-huile-olive.html', 'olive-oil-production-process.html', 'processo-produzione-olio-oliva.html', 'diadikasía-paragogís-elaio-ladou.html'),
    'terroirs-regions-huile-olive.html': ('terroirs-regions-huile-olive.html', 'olive-oil-terroirs-and-regions.html', 'terroir-e-regioni-olio-oliva.html', 'terroirs-kai-periochés-elaio-ladou.html'),
    'comment-choisir-huile-olive.html': ('comment-choisir-huile-olive.html', 'how-to-choose-best-olive-oil.html', 'come-scegliere-migliore-olio-oliva.html', 'pos-na-dialexete-to-kalitero-elaio-lado.html'),
    'conservation-huile-olive-conseils.html': ('conservation-huile-olive-conseils.html', 'olive-oil-storage-tips.html', 'consigli-conservazione-olio-oliva.html', 'simvoules-sintirisis-elaio-ladou.html'),
    'huile-olive-bio-durabilite.html': ('huile-olive-bio-durabilite.html', 'organic-and-sustainable-olive-oil.html', 'olio-oliva-biologico-e-sostenibile.html', 'viologiko-kai-viosimo-elaio-lado.html'),
    'huile-olive-beaute-soins-peau.html': ('huile-olive-beaute-soins-peau.html', 'olive-oil-beauty-and-skincare.html', 'olio-oliva-bellezza-cura-pelle.html', 'elaio-lado-omorfia-kai-derma.html'),
    'histoire-culture-huile-olive.html': ('histoire-culture-huile-olive.html', 'history-and-culture-of-olive-oil.html', 'storia-e-cultura-dell-olio-oliva.html', 'istoria-kai-politismos-elaio-ladou.html'),
    'difference-extra-vierge-vierge.html': ('difference-extra-vierge-vierge.html', 'extra-virgin-vs-virgin-olive-oil.html', 'differenza-extra-vergine-e-vergine.html', 'diafora-extra-partheno-kai-partheno.html'),
    'tendances-marche-huile-olive-2026.html': ('tendances-marche-huile-olive-2026.html', 'olive-oil-market-trends-2026.html', 'tendenze-mercato-olio-oliva-2026.html', 'taseis-agoras-elaio-ladou-2026.html'),
}


def build_faq_html(faq_list):
    items = []
    for q, a in faq_list:
        items.append(f'<details><summary>{q}</summary><p>{a}</p></details>')
    return '\n'.join(items)


def build_related_html(current_file):
    links = []
    for fname, title in GUIDE_TITLES_FR.items():
        if fname != current_file and len(links) < 3:
            links.append(f'<a href="{fname}">{title}</a>')
    return '\n'.join(links)


def build_hreflang_html(urls):
    fr, en, it, el = urls
    return (
        f'<link rel="alternate" hreflang="fr" href="{fr}" />\n'
        f'    <link rel="alternate" hreflang="en" href="{en}" />\n'
        f'    <link rel="alternate" hreflang="it" href="{it}" />\n'
        f'    <link rel="alternate" hreflang="el" href="{el}" />'
    )


def build_lang_switch_html(filenames, active='fr'):
    langs = [('fr', 'FR'), ('en', 'EN'), ('it', 'IT'), ('el', 'EL')]
    parts = []
    for (lang, label), fname in zip(langs, filenames):
        cls = ' class="active"' if lang == active else ''
        parts.append(f'<a href="{fname}"{cls}>{label}</a>')
    return ' '.join(parts)


def main():
    count = 0
    for filename, data in GUIDES.items():
        filepath = os.path.join(DIR, filename)
        if not os.path.exists(filepath):
            print(f"SKIP (not found): {filename}")
            continue

        h1 = GUIDE_TITLES_FR[filename]
        hreflang = build_hreflang_html(GUIDE_HREFLANG[filename])
        lang_switch = build_lang_switch_html(LANG_SWITCH_FILENAMES[filename], active='fr')
        faq_html = build_faq_html(data['faq'])
        related_html = build_related_html(filename)

        html = GUIDE_TEMPLATE.format(
            title=h1 + " — L'Or Vert",
            meta=data['meta'],
            lede=data['lede'],
            h1=h1,
            article=data['article'],
            faq=faq_html,
            related=related_html,
            hreflang=hreflang,
            lang_switch=lang_switch,
        )

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"OK: {filename}")
        count += 1

    print(f"\nDone: {count} guide pages regenerated.")


if __name__ == '__main__':
    main()

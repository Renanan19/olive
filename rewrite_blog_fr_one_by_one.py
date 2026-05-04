import html
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
BLOG_DIR = ROOT / "blog"
SITE = "https://huiledefes.com"


ARTICLES = {
    "3-recettes": {
        "desc": "Trois idées vraiment utiles pour cuisiner autrement avec l'huile d'olive : dessert, plat chaud et assiette fraîche.",
        "lede": "L'huile d'olive ne sert pas seulement à assaisonner une salade. Bien choisie, elle transforme un dessert, donne du relief à un plat chaud et remplace avantageusement des matières grasses plus lourdes.",
        "sections": [
            ("1. Mousse chocolat noir et huile fruitée", "Choisissez un chocolat à 65-70 %, une huile d'olive douce aux notes d'amande et une pointe de fleur de sel. L'huile apporte une texture satinée et allonge la finale du cacao sans donner de goût gras. Le bon geste consiste à l'ajouter hors du feu, quand le chocolat fondu est déjà tiède, pour garder ses arômes."),
            ("2. Légumes rôtis, citron et huile verte", "Sur des carottes, courgettes ou patates douces, l'huile d'olive supporte très bien une cuisson modérée. Ajoutez-en une partie avant cuisson, puis gardez le meilleur filet pour la sortie du four. Cette double utilisation donne à la fois une surface dorée et une sensation fraîche au service."),
            ("3. Yaourt grec salé, concombre et huile intense", "Mélangez yaourt grec, concombre râpé, menthe, citron et poivre. Terminez avec une huile plus ardente, presque poivrée. Le contraste entre le laitage, l'acidité et l'amertume légère de l'huile donne une entrée rapide qui paraît travaillée."),
            ("Comment choisir l'huile pour ces recettes", "Une huile douce convient aux desserts et aux sauces crémeuses. Une huile verte, plus amère et piquante, fonctionne mieux sur légumes, pain grillé, poisson ou fromage frais. Le professionnalisme vient de ce choix : une seule bouteille pour tous les usages donne rarement le meilleur résultat."),
        ],
        "checklist": ["Goûter l'huile seule avant de l'utiliser.", "Ajouter les huiles les plus aromatiques en finition.", "Éviter les huiles anciennes dans les desserts.", "Associer l'intensité de l'huile à celle du plat."],
        "quote": "Une recette à l'huile d'olive réussie ne cherche pas à cacher l'huile : elle lui donne un rôle précis.",
        "faq": [
            ("Peut-on remplacer le beurre par l'huile d'olive ?", "Oui, surtout dans les gâteaux moelleux. Il faut généralement réduire légèrement la quantité et choisir une huile douce."),
            ("Quelle huile pour un dessert ?", "Une huile fruitée mûre, peu amère, avec des notes d'amande, de pomme ou de noisette."),
        ],
    },
    "accords-mets": {
        "desc": "Guide pratique pour associer huiles d'olive et plats selon l'intensité, le fruité, l'amertume et le piquant.",
        "lede": "Un bon accord entre un plat et une huile d'olive se construit comme un accord mets-vin : intensité, texture, fraîcheur et longueur doivent se répondre.",
        "sections": [
            ("Commencer par l'intensité", "La première question n'est pas l'origine de l'huile, mais sa puissance. Une huile douce accompagne une burrata, un poisson vapeur ou une pâtisserie. Une huile verte et poivrée tient face à des légumes grillés, une viande blanche, des légumineuses ou une soupe rustique."),
            ("Lire le fruité", "Un fruité mûr rappelle l'amande, la pomme cuite ou l'olive noire : il arrondit les plats délicats. Un fruité vert évoque l'herbe coupée, l'artichaut ou la tomate verte : il réveille les assiettes simples et donne une impression de fraîcheur."),
            ("Utiliser l'amertume avec précision", "L'amertume n'est pas un défaut. Sur une tomate ancienne, une salade de lentilles ou un houmous, elle apporte de la structure. En revanche, sur un dessert très fin ou un poisson fragile, elle peut dominer si l'huile est trop jeune ou trop intense."),
            ("Quelques accords fiables", "Huile douce avec vanille, chocolat, ricotta et poisson blanc. Huile moyenne avec pâtes, légumes tièdes et volailles. Huile intense avec pain grillé, pois chiches, aubergines, tomates confites et fromages de caractère."),
        ],
        "checklist": ["Douceur avec plats délicats.", "Fruité vert avec légumes et légumineuses.", "Huile intense en finition, jamais par automatisme.", "Toujours goûter l'huile sur un aliment neutre."],
        "quote": "Le bon accord ne se voit pas : il rend le plat plus net, plus long et plus mémorable.",
        "faq": [
            ("Quelle huile pour une salade ?", "Une huile fruitée verte fonctionne très bien si la salade contient tomate, herbes, concombre ou légumes croquants."),
            ("Quelle huile pour du poisson ?", "Une huile douce à moyenne, avec citron ou herbes, évite de masquer la finesse du poisson."),
        ],
    },
    "certifications-bio": {
        "desc": "Comprendre les certifications bio de l'huile d'olive, leurs garanties, leurs limites et les mentions à vérifier.",
        "lede": "La certification bio rassure, mais elle ne suffit pas à elle seule à garantir une grande huile. Elle indique un mode de production ; la qualité finale dépend aussi de la récolte, du moulin et de la conservation.",
        "sections": [
            ("Ce que garantit le bio", "Une huile d'olive certifiée bio provient d'oliveraies conduites selon un cahier des charges limitant fortement les intrants chimiques de synthèse. Les contrôles portent sur la culture, la traçabilité, la transformation et l'étiquetage."),
            ("Ce que le bio ne garantit pas", "Le label ne dit pas si les olives ont été triturées rapidement, si l'huile est récente, si la bouteille a été protégée de la chaleur ou si le profil aromatique est équilibré. Une huile bio peut être excellente, banale ou fatiguée."),
            ("Les mentions à lire en plus du logo", "Cherchez la date de récolte, l'origine précise, la catégorie vierge extra, l'extraction mécanique à froid et le nom du producteur ou du moulin. Plus l'information est précise, plus le produit est lisible."),
            ("Bio, durable, local : ne pas tout confondre", "Le bio parle d'un cahier des charges agricole. La durabilité ajoute la gestion de l'eau, des sols, de la biodiversité et de l'énergie. Une huile sérieuse explique souvent ces choix au-delà du simple logo."),
        ],
        "checklist": ["Logo bio officiel.", "Origine précise.", "Date de récolte récente.", "Bouteille sombre ou bidon opaque.", "Nom du producteur ou du moulin."],
        "quote": "Le label bio est un point de départ, pas une conclusion.",
        "faq": [
            ("Une huile bio est-elle forcément meilleure ?", "Non. Elle respecte un mode de production, mais la fraîcheur et l'extraction restent décisives."),
            ("Le bio change-t-il le goût ?", "Indirectement parfois, mais le goût dépend surtout de la variété, de la maturité des olives et du travail du moulin."),
        ],
    },
    "conservation": {
        "desc": "Méthode simple pour conserver l'huile d'olive plus longtemps sans perdre fruité, fraîcheur ni qualités aromatiques.",
        "lede": "Une bonne huile d'olive est un produit frais. Son goût peut se dégrader vite si elle reste exposée à la lumière, à l'air ou à la chaleur.",
        "sections": [
            ("Les trois ennemis de l'huile", "La lumière fatigue les arômes, l'oxygène accélère l'oxydation et la chaleur écrase le fruité. Ensemble, ils transforment une huile vive en produit plat, parfois rance, même si la date limite n'est pas dépassée."),
            ("Le bon endroit dans la cuisine", "Évitez le rebord de fenêtre, le dessus du four et le plan de travail près des plaques. Préférez un placard frais, fermé, stable, loin des variations de température. La bouteille doit être refermée immédiatement après usage."),
            ("Choisir le bon format", "Une grande bouteille économique n'est pas toujours une bonne affaire si elle reste ouverte six mois. Mieux vaut acheter un format adapté à votre rythme : 250 ou 500 ml pour une huile de finition, bidon plus grand pour une huile de cuisson quotidienne."),
            ("Reconnaître une huile fatiguée", "Une odeur de noix rance, de cire, de carton ou de vieille cave indique une oxydation avancée. En bouche, l'huile devient molle, grasse et courte. À ce stade, elle ne mérite plus d'être utilisée à cru."),
        ],
        "checklist": ["Bouteille sombre.", "Placard frais.", "Bouchon refermé vite.", "Format consommé en deux à trois mois après ouverture.", "Jamais de carafe transparente décorative."],
        "quote": "Conserver une huile, c'est protéger une récolte entière dans une bouteille.",
        "faq": [
            ("Faut-il mettre l'huile d'olive au réfrigérateur ?", "En général non : le froid trouble l'huile et n'est pas nécessaire si elle est gardée dans un placard frais."),
            ("Combien de temps après ouverture ?", "Idéalement deux à trois mois pour une huile aromatique utilisée à cru."),
        ],
    },
    "espagne-italie": {
        "desc": "Comparer l'Espagne et l'Italie dans la production d'huile d'olive sans clichés : volumes, styles, variétés et terroirs.",
        "lede": "Espagne contre Italie : le match est souvent raconté comme une rivalité. En réalité, ces deux pays ne jouent pas le même rôle dans l'imaginaire de l'huile d'olive.",
        "sections": [
            ("L'Espagne, puissance de production", "L'Espagne domine largement les volumes mondiaux. L'Andalousie, avec ses paysages d'oliveraies immenses, produit des huiles très variées, de la Picual robuste aux profils plus doux selon les zones et les maturités."),
            ("L'Italie, force de style et de diversité", "L'Italie est célèbre pour la mosaïque de ses terroirs : Toscane, Pouilles, Sicile, Ligurie, Ombrie. Les volumes sont plus modestes, mais l'identité régionale, les assemblages et la culture gastronomique donnent une forte valeur perçue."),
            ("Le piège du pays unique", "Une huile espagnole peut être plus élégante qu'une italienne, et une huile italienne peut être plus ardente qu'une espagnole. Le pays ne suffit jamais : variété, récolte, moulin et conservation comptent davantage."),
            ("Comment choisir entre les deux", "Pour cuisiner souvent, une bonne huile espagnole offre parfois un excellent rapport qualité-prix. Pour un cadeau ou une table de dégustation, une huile italienne de domaine peut séduire par son récit régional. Le meilleur choix reste celui que vous goûtez."),
        ],
        "checklist": ["Regarder la variété.", "Comparer la date de récolte.", "Ne pas acheter uniquement au drapeau.", "Goûter sur pain et tomate.", "Adapter le prix à l'usage."],
        "quote": "Le meilleur pays producteur est celui qui met une huile fraîche, lisible et bien conservée dans votre assiette.",
        "faq": [
            ("L'huile italienne est-elle meilleure ?", "Pas automatiquement. Certaines sont remarquables, d'autres très ordinaires."),
            ("Pourquoi l'Espagne produit-elle autant ?", "Son climat, ses surfaces d'oliveraies et sa structuration agricole expliquent sa place majeure."),
        ],
    },
    "frire": {
        "desc": "Frire à l'huile d'olive : comprendre le point de fumée, les mythes, les bonnes températures et les usages raisonnables.",
        "lede": "Frire à l'huile d'olive n'est pas une erreur méditerranéenne. C'est une technique valable si la température est maîtrisée et si l'huile est adaptée.",
        "sections": [
            ("Le mythe du point de fumée", "On répète souvent que l'huile d'olive ne supporte pas la chaleur. C'est trop simpliste. Une huile vierge extra de bonne qualité, stable et riche en acides gras mono-insaturés, supporte les cuissons domestiques raisonnables."),
            ("La bonne température", "Pour frire, visez environ 160 à 180 °C. Si l'huile fume, elle est trop chaude. Les aliments doivent grésiller sans brûler. Une température stable évite aussi que les aliments absorbent trop d'huile."),
            ("Ce que l'huile apporte au goût", "L'huile d'olive donne une croûte savoureuse aux légumes, beignets, pommes de terre et petits poissons. Une huile trop expressive peut dominer : gardez les grands crus poivrés pour la finition."),
            ("Réutiliser ou non l'huile", "Une huile filtrée après une friture propre peut parfois être réutilisée rapidement. Mais dès qu'elle fonce, mousse, sent le brûlé ou contient beaucoup de particules, il faut l'écarter."),
        ],
        "checklist": ["Ne jamais attendre la fumée.", "Sécher les aliments avant friture.", "Ne pas surcharger la poêle.", "Filtrer si réutilisation courte.", "Garder les huiles premium pour le cru."],
        "quote": "La friture réussie dépend moins du dogme que du thermomètre et du bon sens.",
        "faq": [
            ("Peut-on faire des frites à l'huile d'olive ?", "Oui, avec une huile adaptée et une température maîtrisée."),
            ("Est-ce économique ?", "Pour de grandes fritures répétées, ce n'est pas toujours le choix le plus rationnel. Pour des fritures courtes, oui."),
        ],
    },
    "gateaux": {
        "desc": "Utiliser l'huile d'olive dans les gâteaux : dosage, choix de l'huile, textures et erreurs à éviter.",
        "lede": "Dans un gâteau, l'huile d'olive donne du moelleux, de la conservation et une personnalité discrète lorsqu'elle est bien choisie.",
        "sections": [
            ("Pourquoi remplacer le beurre", "L'huile d'olive apporte une texture souple qui reste agréable le lendemain. Elle évite l'effet sec de certains cakes et donne une mie plus humide, particulièrement intéressante avec citron, amande, chocolat ou orange."),
            ("Choisir une huile douce", "Évitez les huiles trop amères ou très poivrées pour les desserts délicats. Préférez une huile fruitée mûre, ronde, aux notes d'amande, de pomme ou de noisette. Elle doit soutenir le parfum, pas prendre toute la scène."),
            ("Adapter le dosage", "On ne remplace pas toujours 100 g de beurre par 100 g d'huile. L'huile étant pure matière grasse, une quantité légèrement inférieure suffit souvent. Dans un cake, commencez autour de 80 g d'huile pour 100 g de beurre remplacé."),
            ("Les meilleurs accords sucrés", "Citron, orange, chocolat noir, miel, romarin, amande, pistache et fruits rouges fonctionnent très bien. Le sel est important : une petite pincée rend l'huile plus élégante et évite une impression lourde."),
        ],
        "checklist": ["Huile douce et fraîche.", "Dosage légèrement réduit.", "Agrumes ou fruits secs pour l'équilibre.", "Cuisson modérée.", "Repos avant dégustation."],
        "quote": "Un bon gâteau à l'huile d'olive ne goûte pas l'huile : il goûte plus longtemps.",
        "faq": [
            ("Quel dessert commencer ?", "Un cake citron-huile d'olive est le plus simple et le plus convaincant."),
            ("L'huile d'olive se sent-elle ?", "Oui si elle est trop intense. Avec une huile douce, elle apporte surtout texture et longueur."),
        ],
    },
    "animaux": {
        "desc": "Huile d'olive pour les animaux : usages possibles, prudence, quantités et cas où demander un avis vétérinaire.",
        "lede": "L'huile d'olive est parfois utilisée pour les animaux domestiques, mais elle doit rester occasionnelle, dosée et jamais considérée comme un soin universel.",
        "sections": [
            ("Ce que l'huile peut apporter", "En très petite quantité, elle peut aider à rendre une ration plus appétente ou contribuer à l'apport en lipides. Certains propriétaires l'utilisent aussi pour le pelage, mais l'effet dépend surtout de l'alimentation globale."),
            ("Les limites importantes", "Un excès peut provoquer diarrhée, prise de poids ou inconfort digestif. Les animaux ayant des troubles digestifs, pancréatiques, hépatiques ou un régime médicalisé ne doivent pas en recevoir sans avis vétérinaire."),
            ("Comment l'utiliser prudemment", "Si l'animal est en bonne santé, commencez par une très petite quantité mélangée à la nourriture, de manière ponctuelle. Observez les selles, l'appétit et le comportement les jours suivants."),
            ("Ce qu'il ne faut pas faire", "Ne versez pas d'huile sur toutes les gamelles par réflexe. N'utilisez pas d'huile aromatisée à l'ail, au piment ou aux herbes. Et ne remplacez jamais un traitement ou une consultation par une astuce alimentaire."),
        ],
        "checklist": ["Petite quantité.", "Usage ponctuel.", "Huile nature uniquement.", "Surveillance digestive.", "Avis vétérinaire en cas de doute."],
        "quote": "Pour un animal, le bon usage de l'huile d'olive commence par la retenue.",
        "faq": [
            ("Peut-on donner de l'huile d'olive à un chien ?", "Parfois en petite quantité, mais il faut tenir compte du poids, de la santé et de l'alimentation."),
            ("Et pour un chat ?", "Même prudence. Le chat est sensible aux changements alimentaires et ne doit pas recevoir d'huile aromatisée."),
        ],
    },
    "cheveux": {
        "desc": "Utiliser l'huile d'olive sur les cheveux : bénéfices réels, méthode d'application, limites et erreurs fréquentes.",
        "lede": "L'huile d'olive peut être intéressante sur les cheveux secs, mais son efficacité dépend du dosage, du temps de pose et du type de fibre.",
        "sections": [
            ("Ce que l'huile fait vraiment", "Elle ne répare pas chimiquement un cheveu abîmé. En revanche, elle gaine la fibre, limite la sensation de sécheresse et donne plus de souplesse aux longueurs. Son rôle est surtout cosmétique et protecteur."),
            ("Pour quels cheveux", "Elle convient mieux aux cheveux épais, bouclés, frisés ou très secs. Sur cheveux fins, elle peut vite alourdir. Dans ce cas, appliquez seulement une trace sur les pointes ou choisissez une huile plus légère."),
            ("La bonne méthode", "Appliquez une petite quantité sur les longueurs légèrement humidifiées, jamais en excès. Laissez poser 20 à 40 minutes, puis faites un shampooing doux. Un second lavage peut être nécessaire si la fibre reste grasse."),
            ("Les erreurs fréquentes", "Trop d'huile, une pose toute la nuit sans protection, une application sur racines grasses ou l'utilisation d'une huile ancienne peuvent donner un résultat lourd et désagréable."),
        ],
        "checklist": ["Petite quantité.", "Longueurs et pointes.", "Pose limitée.", "Shampooing doux.", "Test sur une mèche avant usage complet."],
        "quote": "Le soin capillaire à l'huile d'olive fonctionne mieux en précision qu'en générosité.",
        "faq": [
            ("L'huile d'olive fait-elle pousser les cheveux ?", "Elle peut accompagner un massage du cuir chevelu, mais elle ne déclenche pas à elle seule la pousse."),
            ("Peut-on l'utiliser chaque semaine ?", "Oui pour cheveux très secs si le cuir chevelu le tolère, sinon espacez les applications."),
        ],
    },
    "haute-altitude": {
        "desc": "Comprendre les huiles d'olive de haute altitude : climat, maturation lente, profils aromatiques et critères d'achat.",
        "lede": "Les huiles d'olive de haute altitude séduisent par leur fraîcheur et leur tension aromatique, mais l'altitude seule ne suffit pas à garantir la qualité.",
        "sections": [
            ("Ce que change l'altitude", "En altitude, les nuits plus fraîches ralentissent souvent la maturation des olives. Cette progression plus lente peut favoriser des profils plus verts, plus nets, avec une belle vivacité aromatique."),
            ("Des récoltes plus exigeantes", "Les parcelles sont parfois plus difficiles d'accès, les rendements plus faibles et les fenêtres de récolte plus serrées. Cela explique une partie du prix, surtout quand les olives sont portées rapidement au moulin."),
            ("Quel goût attendre", "On retrouve souvent des notes d'herbe, d'artichaut, de feuille de tomate ou d'amande fraîche. L'amertume et le piquant peuvent être plus présents, surtout sur une récolte précoce."),
            ("Comment acheter sans se tromper", "Ne vous laissez pas séduire uniquement par la mention altitude. Vérifiez l'origine, la date de récolte, la variété et le conditionnement. Une huile de montagne mal stockée perd très vite son intérêt."),
        ],
        "checklist": ["Altitude indiquée avec origine précise.", "Récolte récente.", "Bouteille protégée.", "Profil gustatif cohérent.", "Usage surtout à cru."],
        "quote": "L'altitude donne un potentiel ; le producteur décide si ce potentiel devient une grande huile.",
        "faq": [
            ("Une huile d'altitude est-elle plus chère ?", "Souvent, car les rendements et la logistique peuvent être plus contraignants."),
            ("Comment l'utiliser ?", "Sur légumes, pain, fromages frais, poissons grillés ou soupes en finition."),
        ],
    },
    "recolte-precoce": {
        "desc": "Récolte précoce de l'huile d'olive : goût, polyphénols, rendement, prix et usages culinaires.",
        "lede": "Une huile de récolte précoce est produite avec des olives encore vertes ou tournantes. Elle offre souvent intensité, fraîcheur et richesse phénolique.",
        "sections": [
            ("Pourquoi récolter tôt", "Les olives jeunes donnent moins d'huile, mais une matière plus expressive. Le producteur accepte donc un rendement plus faible pour obtenir un profil aromatique plus vert, plus tendu, parfois plus poivré."),
            ("Le goût typique", "Une récolte précoce évoque souvent l'herbe fraîche, l'artichaut, la feuille de tomate, l'amande verte et une finale piquante. L'amertume n'est pas un défaut : elle signale souvent une belle présence phénolique."),
            ("Pourquoi c'est plus cher", "Il faut plus d'olives pour produire un litre, la récolte doit être rapide et le moulin doit suivre. Le prix reflète donc la quantité de fruit nécessaire et la précision de l'extraction."),
            ("Les meilleurs usages", "Utilisez-la à cru : tomates, légumes grillés, mozzarella, pain, houmous, soupes, poissons, viandes blanches. En cuisson longue, vous perdez une partie de ce qui justifie son prix."),
        ],
        "checklist": ["Notes vertes franches.", "Amertume équilibrée.", "Piquant propre.", "Date de récolte visible.", "Usage en finition."],
        "quote": "La récolte précoce est une huile d'énergie : elle doit réveiller le plat, pas l'écraser.",
        "faq": [
            ("Est-ce meilleur pour la santé ?", "Elle peut être plus riche en polyphénols, mais tout dépend de l'huile précise."),
            ("Est-ce trop fort pour tous les jours ?", "Pas forcément. Il suffit de la réserver aux plats qui supportent son intensité."),
        ],
    },
    "rome-antique": {
        "desc": "L'huile d'olive dans la Rome antique : alimentation, commerce, bains, lampes, économie et héritage méditerranéen.",
        "lede": "Dans la Rome antique, l'huile d'olive n'était pas un simple condiment. Elle servait à cuisiner, éclairer, soigner, commercer et marquer le statut social.",
        "sections": [
            ("Un produit quotidien et stratégique", "Les Romains utilisaient l'huile pour l'alimentation, les bains, les massages, les lampes et certains usages médicinaux. Sa présence dans la vie quotidienne en faisait une ressource aussi pratique que symbolique."),
            ("Le commerce de l'huile", "Des amphores circulaient dans tout l'Empire, depuis l'Hispanie, l'Afrique du Nord ou l'Italie. Les inscriptions sur amphores permettent encore aujourd'hui de comprendre les routes commerciales et les volumes échangés."),
            ("Qualités et usages différenciés", "Toutes les huiles ne se valaient pas. Les meilleures pouvaient être destinées à la table ou aux soins, tandis que des qualités plus ordinaires servaient à l'éclairage ou à d'autres usages domestiques."),
            ("Ce que cet héritage raconte", "L'histoire romaine rappelle que l'huile d'olive a toujours été plus qu'un aliment : c'est un marqueur de civilisation méditerranéenne, de logistique agricole et de culture matérielle."),
        ],
        "checklist": ["Alimentation.", "Éclairage.", "Hygiène.", "Commerce.", "Symbolique sociale."],
        "quote": "Comprendre Rome, c'est comprendre à quel point l'huile d'olive a structuré la Méditerranée.",
        "faq": [
            ("Les Romains consommaient-ils beaucoup d'huile ?", "Oui, elle faisait partie des produits essentiels de leur économie quotidienne."),
            ("L'huile romaine ressemblait-elle à celle d'aujourd'hui ?", "Les techniques différaient, mais le principe agricole et culturel reste très proche."),
        ],
    },
    "vs-coco": {
        "desc": "Huile d'olive ou huile de coco : comparaison nutritionnelle, usages en cuisine, goût et critères de choix.",
        "lede": "L'huile d'olive et l'huile de coco n'ont ni le même profil nutritionnel, ni le même goût, ni les mêmes usages. Les comparer demande de sortir des slogans.",
        "sections": [
            ("Le profil nutritionnel", "L'huile d'olive est riche en acides gras mono-insaturés et peut apporter des polyphénols lorsqu'elle est vierge extra. L'huile de coco est surtout riche en graisses saturées. Cette différence oriente déjà l'usage quotidien."),
            ("En cuisine", "L'huile de coco donne un goût marqué, utile dans certains currys, desserts exotiques ou préparations végétales. L'huile d'olive est plus polyvalente : assaisonnement, cuisson douce, légumes, poissons, pains et sauces."),
            ("Le piège marketing", "L'huile de coco a bénéficié d'une image très tendance. Cela ne la rend pas supérieure. L'huile d'olive, plus classique, possède une place solide dans la diète méditerranéenne et dans de nombreuses études nutritionnelles."),
            ("Comment choisir", "Pour l'usage quotidien, l'huile d'olive vierge extra reste le choix le plus cohérent. L'huile de coco peut rester ponctuelle, pour son parfum et sa texture, pas comme remplacement systématique."),
        ],
        "checklist": ["Olive pour le quotidien.", "Coco pour goût spécifique.", "Lire les graisses saturées.", "Éviter les promesses miracles.", "Varier selon la recette."],
        "quote": "La meilleure huile n'est pas la plus à la mode, mais celle dont le profil correspond à l'usage.",
        "faq": [
            ("L'huile de coco est-elle mauvaise ?", "Pas forcément, mais elle doit rester mesurée dans une alimentation équilibrée."),
            ("Peut-on remplacer l'une par l'autre ?", "Parfois en pâtisserie ou cuisson, mais le goût et la texture changent beaucoup."),
        ],
    },
    "infusees": {
        "desc": "Faire ses huiles d'olive infusées maison en sécurité : aromates, méthode, conservation et erreurs à éviter.",
        "lede": "Une huile infusée maison peut sublimer une cuisine simple, à condition de respecter quelques règles de sécurité et de conservation.",
        "sections": [
            ("Choisir la bonne base", "Prenez une huile vierge extra propre, plutôt douce à moyenne. Une huile très complexe peut être masquée par les aromates. L'objectif est de créer un condiment lisible, pas de couvrir un défaut."),
            ("Aromates secs ou frais", "Les aromates secs sont les plus simples : piment séché, romarin sec, thym, poivre, zestes bien déshydratés. Les ingrédients frais, notamment ail et herbes humides, demandent plus de prudence car ils réduisent la durée de conservation."),
            ("Méthode sûre", "Travaillez avec un contenant parfaitement propre. Pour une infusion courte, laissez les aromates quelques jours au frais, goûtez, puis filtrez. Une huile filtrée se conserve mieux qu'une bouteille remplie d'herbes fraîches."),
            ("Idées d'usage", "Piment pour pizza, citron pour poisson, romarin pour pommes de terre, basilic pour tomate, ail doux pour légumes grillés. Ajoutez toujours en finition pour garder la netteté aromatique."),
        ],
        "checklist": ["Contenant propre.", "Aromates secs privilégiés.", "Infusion courte.", "Filtration.", "Conservation au frais si ingrédient frais."],
        "quote": "Une huile infusée réussie doit sentir clairement son aromate et rester irréprochable en conservation.",
        "faq": [
            ("Peut-on mettre de l'ail frais dans l'huile ?", "C'est possible pour un usage très court au frais, mais ce n'est pas idéal pour une conservation longue."),
            ("Combien de temps garder une huile infusée ?", "Cela dépend des aromates. Avec ingrédients frais, restez très prudent et consommez rapidement."),
        ],
    },
    "ia-moulins": {
        "desc": "Comment l'intelligence artificielle entre dans les moulins à huile : tri, extraction, qualité, rendement et limites.",
        "lede": "L'intelligence artificielle ne remplace pas le savoir-faire du moulinier, mais elle devient un outil précieux pour piloter la qualité avec plus de précision.",
        "sections": [
            ("Trier la matière première", "Des capteurs et modèles d'analyse peuvent aider à détecter maturité, défauts, humidité ou hétérogénéité des lots. Le tri devient plus fin, ce qui protège la qualité avant même l'extraction."),
            ("Piloter l'extraction", "Température, temps de malaxage, débit, rendement et séparation peuvent être suivis en temps réel. L'IA aide à repérer les dérives et à ajuster les paramètres sans attendre la fin du lot."),
            ("Améliorer la traçabilité", "Un moulin connecté peut associer parcelle, variété, date de récolte, conditions météo et résultats sensoriels. Cette mémoire de production permet de comprendre pourquoi une huile réussit ou déçoit."),
            ("Les limites humaines", "La machine mesure, mais elle ne goûte pas comme un jury. Le nez, la bouche et l'expérience restent essentiels. Le risque serait de chercher seulement le rendement au lieu de préserver l'identité de l'huile."),
        ],
        "checklist": ["Capteurs fiables.", "Données propres.", "Objectif qualité clair.", "Dégustation humaine.", "Traçabilité transparente."],
        "quote": "Dans un bon moulin, l'IA doit affiner la décision humaine, pas l'effacer.",
        "faq": [
            ("L'IA rend-elle l'huile meilleure ?", "Elle peut aider, mais la qualité dépend toujours des olives, du moulin et des choix humains."),
            ("Est-ce réservé aux grands producteurs ?", "Les coûts baissent, mais l'intégration reste plus facile pour les moulins structurés."),
        ],
    },
    "etiquette": {
        "desc": "Apprendre à lire une étiquette d'huile d'olive : catégorie, origine, récolte, extraction, conservation et pièges marketing.",
        "lede": "L'étiquette d'une huile d'olive raconte beaucoup, à condition de savoir distinguer les informations utiles des formules décoratives.",
        "sections": [
            ("La catégorie", "La mention vierge extra est le premier repère. Elle indique une huile obtenue par procédés mécaniques, avec des critères chimiques et sensoriels précis. Mais cette catégorie ne suffit pas : elle peut couvrir des qualités très différentes."),
            ("L'origine réelle", "Cherchez une origine précise : pays, région, domaine, moulin, parcelle parfois. Les mentions vagues comme mélange d'huiles de l'Union européenne donnent moins de lisibilité sur le style et la traçabilité."),
            ("Date de récolte et fraîcheur", "La date de récolte est plus parlante que la date limite. Une huile d'olive n'est pas un vin de garde : son intérêt aromatique est généralement maximal dans les mois qui suivent la production."),
            ("Les mots à relativiser", "Première pression à froid, tradition, premium, sélection ou goût authentique peuvent être séduisants, mais ils doivent être confirmés par des données concrètes : variété, extraction, récolte, conditionnement."),
        ],
        "checklist": ["Vierge extra.", "Origine précise.", "Date de récolte.", "Variété si possible.", "Bouteille sombre.", "Nom du producteur."],
        "quote": "Une bonne étiquette ne promet pas seulement : elle prouve.",
        "faq": [
            ("La date limite suffit-elle ?", "Non. Elle ne remplace pas la date de récolte pour juger la fraîcheur."),
            ("Que penser de première pression à froid ?", "La formule est souvent plus marketing que technique dans les moulins modernes."),
        ],
    },
    "oliviers-millenaires": {
        "desc": "Les oliviers millénaires : longévité, patrimoine, rendement, goût des huiles et enjeux de protection.",
        "lede": "Les oliviers millénaires fascinent parce qu'ils relient agriculture, paysage et mémoire. Mais leur valeur dépasse largement la photographie spectaculaire.",
        "sections": [
            ("Une longévité exceptionnelle", "L'olivier peut survivre à la sécheresse, au vent, aux tailles sévères et aux sols pauvres. Son tronc se creuse, se tord, repart parfois de la base. Cette capacité à se régénérer explique la présence d'arbres très anciens dans plusieurs régions méditerranéennes."),
            ("Patrimoine plus que rendement", "Un vieil arbre ne produit pas forcément plus. Il peut même donner moins qu'une plantation moderne. Sa valeur tient plutôt à son patrimoine génétique, à son rôle paysager et au récit culturel qu'il porte."),
            ("Le goût de l'huile", "L'âge de l'arbre ne garantit pas seul une huile supérieure. Le goût dépend de la variété, de l'état sanitaire des olives, de la récolte et du moulin. Un olivier ancien peut donner une huile magnifique si toute la chaîne suit."),
            ("Protéger ces arbres", "Le tourisme, l'urbanisation, l'arrachage et le commerce d'arbres décoratifs menacent certains sujets. Les protéger, c'est défendre une agriculture lente, enracinée et non remplaçable."),
        ],
        "checklist": ["Ne pas confondre âge et qualité automatique.", "Valoriser la variété.", "Préserver le paysage.", "Éviter l'arrachage décoratif.", "Raconter l'origine avec précision."],
        "quote": "Un olivier millénaire n'est pas seulement un arbre ancien : c'est une archive vivante.",
        "faq": [
            ("Un vieil olivier produit-il une meilleure huile ?", "Pas automatiquement. La qualité dépend surtout du fruit et de l'extraction."),
            ("Peut-on dater précisément ces arbres ?", "C'est difficile, car le bois intérieur disparaît souvent avec l'âge."),
        ],
    },
    "notes-degustation": {
        "desc": "Comprendre les notes de dégustation d'une huile d'olive : fruité, amertume, piquant, défauts et vocabulaire utile.",
        "lede": "Déguster une huile d'olive ne consiste pas à chercher des mots compliqués. Il s'agit d'identifier la fraîcheur, l'équilibre et les éventuels défauts.",
        "sections": [
            ("Le fruité", "Le fruité peut être vert ou mûr. Vert, il évoque herbe coupée, artichaut, tomate, feuille. Mûr, il rappelle amande, pomme, olive noire ou fruits secs. Ce vocabulaire aide à prévoir les accords culinaires."),
            ("Amertume et piquant", "Ces sensations sont normales dans une huile de qualité. L'amertume se perçoit sur la langue, le piquant en gorge. Ensemble, elles signalent souvent fraîcheur et présence de composés phénoliques."),
            ("Les défauts à reconnaître", "Rance, moisi, vineux, métallique ou chômé sont des défauts. Une huile qui sent la noix ancienne, le carton humide ou la fermentation ne doit pas être présentée comme typée."),
            ("La méthode simple à la maison", "Versez un peu d'huile dans un petit verre, réchauffez-le dans la main, sentez, puis prenez une petite gorgée en aspirant un peu d'air. Goûtez ensuite sur pain ou tomate pour confirmer l'impression."),
        ],
        "checklist": ["Sentir avant de goûter.", "Chercher fruité, amer, piquant.", "Repérer les défauts.", "Tester sur un aliment simple.", "Noter ses impressions."],
        "quote": "Le vocabulaire de dégustation sert surtout à acheter et cuisiner avec plus de justesse.",
        "faq": [
            ("Une huile qui pique est-elle mauvaise ?", "Non, si le piquant est propre et équilibré."),
            ("Pourquoi chauffer le verre dans la main ?", "Pour libérer les arômes sans cuire l'huile."),
        ],
    },
    "cadeau": {
        "desc": "Offrir de l'huile d'olive : choisir une bouteille élégante, utile et crédible selon le destinataire.",
        "lede": "Offrir une huile d'olive peut être très élégant, à condition de choisir autre chose qu'une belle bouteille sans histoire.",
        "sections": [
            ("Choisir selon le destinataire", "Pour un cuisinier curieux, privilégiez une huile expressive et datée. Pour une personne qui cuisine peu, choisissez une huile douce, facile à utiliser. Pour un amateur, cherchez une origine précise, une variété identifiable et un producteur sérieux."),
            ("Le format idéal", "Un 250 ml premium est souvent plus judicieux qu'un grand litre décoratif. Il invite à utiliser l'huile rapidement et donne une impression de produit choisi, pas de simple provision."),
            ("Composer un coffret utile", "Associez l'huile à du pain de qualité, une fleur de sel, un vinaigre doux, des pâtes artisanales ou une petite fiche d'accords. Le cadeau devient une expérience, pas seulement un objet."),
            ("Éviter les faux luxes", "Méfiez-vous des bouteilles transparentes, des packagings très chargés et des mentions vagues. Le luxe discret d'une huile d'olive vient de la fraîcheur, de l'origine et du goût."),
        ],
        "checklist": ["Récolte récente.", "Petit format premium.", "Origine claire.", "Bouteille protégée.", "Accord ou idée d'usage fournie."],
        "quote": "Une huile offerte doit donner envie d'être ouverte, pas seulement exposée.",
        "faq": [
            ("Quelle huile pour un cadeau sûr ?", "Une huile fruitée moyenne, équilibrée, convient au plus grand nombre."),
            ("Faut-il offrir une huile très forte ?", "Seulement à quelqu'un qui aime déjà les huiles intenses."),
        ],
    },
    "oleiculture-durable": {
        "desc": "Oléiculture durable : sols, eau, biodiversité, énergie, rémunération et limites du greenwashing.",
        "lede": "L'oléiculture durable ne se résume pas à une image d'olivier au coucher du soleil. Elle repose sur des choix agricoles mesurables.",
        "sections": [
            ("Préserver les sols", "Un sol vivant retient mieux l'eau, nourrit l'arbre et limite l'érosion. Couverts végétaux, compost, taille raisonnée et réduction du travail mécanique peuvent améliorer la résilience de l'oliveraie."),
            ("Gérer l'eau", "Dans plusieurs régions méditerranéennes, l'eau devient le sujet central. Irrigation pilotée, choix variétal, paillage et restauration des sols permettent de réduire le stress hydrique sans chercher uniquement le rendement."),
            ("Biodiversité et paysage", "Haies, plantes mellifères, vieux arbres, murets et zones non cultivées créent des habitats utiles. Une oliveraie durable n'est pas forcément parfaitement nue et uniforme."),
            ("Économie réelle", "La durabilité suppose aussi une juste rémunération. Une huile très bon marché peut cacher des compromis sur la main-d'œuvre, le soin au verger ou le temps passé au moulin."),
        ],
        "checklist": ["Sols couverts.", "Eau pilotée.", "Biodiversité visible.", "Traçabilité.", "Prix cohérent avec le travail."],
        "quote": "Une huile durable doit prendre soin de l'arbre, du sol et de ceux qui les travaillent.",
        "faq": [
            ("Bio et durable, est-ce pareil ?", "Non. Le bio est un cahier des charges ; la durabilité est plus large."),
            ("Comment éviter le greenwashing ?", "Cherchez des pratiques concrètes, pas seulement des mots verts."),
        ],
    },
    "polyphenols": {
        "desc": "Polyphénols de l'huile d'olive : rôle, goût, fraîcheur, santé et choix d'une huile riche en composés protecteurs.",
        "lede": "Les polyphénols expliquent une partie essentielle du caractère d'une huile d'olive : amertume, piquant, stabilité et intérêt nutritionnel.",
        "sections": [
            ("Ce que sont les polyphénols", "Ce sont des composés naturels présents dans l'olive. Ils protègent l'huile contre l'oxydation et participent aux sensations d'amertume et de piquant. Leur présence varie selon variété, maturité, extraction et conservation."),
            ("Le lien avec le goût", "Une huile riche en polyphénols n'est pas forcément douce. Elle peut accrocher la langue, piquer la gorge et donner une sensation très fraîche. Ce relief est recherché lorsqu'il reste équilibré."),
            ("Comment les préserver", "La fraîcheur est décisive. Bouteille sombre, stockage frais, consommation rapide après ouverture et usage à cru permettent de profiter davantage du profil phénolique."),
            ("Comment acheter", "Cherchez récolte récente, origine précise, variété, analyse éventuelle et profil sensoriel clair. Une huile de récolte précoce est souvent un bon point de départ, sans garantie automatique."),
        ],
        "checklist": ["Récolte récente.", "Amertume propre.", "Piquant net.", "Bouteille sombre.", "Usage à cru."],
        "quote": "Dans l'huile d'olive, le piquant peut être une signature de fraîcheur, pas une agression.",
        "faq": [
            ("Plus ça pique, mieux c'est ?", "Non. Le piquant doit être net, agréable et équilibré."),
            ("Les polyphénols disparaissent-ils ?", "Ils diminuent avec le temps, la lumière, l'air et la chaleur."),
        ],
    },
    "prix-qualite": {
        "desc": "Pourquoi une bonne huile d'olive coûte cher : rendement, récolte, moulin, conditionnement, transport et qualité réelle.",
        "lede": "Le prix d'une huile d'olive sérieuse ne vient pas seulement du marketing. Il reflète souvent un rendement faible, une récolte rapide et un travail précis.",
        "sections": [
            ("Le rendement des olives", "Il faut plusieurs kilos d'olives pour produire un litre d'huile. Plus les olives sont récoltées tôt, plus le rendement baisse. Une huile intense et fraîche coûte donc mécaniquement plus cher à produire."),
            ("La récolte et le moulin", "Récolter au bon moment, transporter vite, triturer rapidement et contrôler la température exigent du matériel, de la main-d'œuvre et de l'organisation. Chaque retard peut dégrader la qualité."),
            ("Le conditionnement", "Bouteille sombre, bouchon de qualité, petit format, stockage correct et transport protégé ajoutent des coûts. Mais ils protègent ce qui a été obtenu au moulin."),
            ("Prix élevé ne veut pas dire qualité automatique", "Certains produits chers sont surtout bien habillés. Le prix doit être cohérent avec les preuves : origine, récolte, variété, producteur, analyse ou dégustation."),
        ],
        "checklist": ["Prix cohérent.", "Informations précises.", "Récolte récente.", "Conditionnement protecteur.", "Goût à la hauteur."],
        "quote": "Une huile chère doit expliquer son prix dans l'étiquette et le verre.",
        "faq": [
            ("Quel prix pour une bonne huile ?", "Cela varie, mais une huile vierge extra artisanale sérieuse est rarement au prix d'une huile industrielle."),
            ("Peut-on trouver de bonnes huiles abordables ?", "Oui, surtout en formats simples, avec origine claire et récolte récente."),
        ],
    },
    "recolte-2026": {
        "desc": "Récolte d'huile d'olive 2026 : tendances qualité, climat, rendements, prix et points de vigilance pour acheter.",
        "lede": "La récolte 2026 devra être lue avec attention : climat, stress hydrique, coûts agricoles et qualité des lots peuvent varier fortement selon les régions.",
        "sections": [
            ("Le climat comme facteur central", "Sécheresse, pluies au mauvais moment, chaleur précoce ou épisodes de froid influencent floraison, calibre des olives et rendement. Deux régions proches peuvent obtenir des résultats très différents."),
            ("Qualité et rendement ne progressent pas toujours ensemble", "Une année peut donner peu d'huile mais de très beaux profils aromatiques. À l'inverse, un volume confortable ne garantit pas une grande expression sensorielle."),
            ("Ce que l'acheteur doit regarder", "Pour 2026, surveillez surtout la date de récolte, l'origine précise, les conditions de stockage et la réputation du producteur. Les discours généraux sur une bonne année ne suffisent pas."),
            ("Impact possible sur les prix", "Coût de l'énergie, main-d'œuvre, baisse de rendement et tension sur certains marchés peuvent maintenir les prix élevés. Le bon réflexe est d'acheter moins mais mieux, selon les usages."),
        ],
        "checklist": ["Comparer par région.", "Lire la récolte.", "Surveiller le stockage.", "Goûter avant gros achat.", "Adapter le budget à l'usage."],
        "quote": "Une récolte se juge rarement au niveau mondial : elle se juge producteur par producteur.",
        "faq": [
            ("Faut-il acheter dès la nouvelle récolte ?", "Oui pour les huiles aromatiques, si le producteur et le stockage sont fiables."),
            ("Les prix vont-ils baisser ?", "Impossible à garantir. Les coûts et le climat restent déterminants."),
        ],
    },
    "regime-mediterraneen": {
        "desc": "Régime méditerranéen et huile d'olive : rôle quotidien, équilibre alimentaire, usages concrets et erreurs à éviter.",
        "lede": "Dans le régime méditerranéen, l'huile d'olive n'est pas un détail. Elle structure la cuisine des légumes, des céréales, du poisson et des légumineuses.",
        "sections": [
            ("Un pilier, pas une potion magique", "L'intérêt du régime méditerranéen vient de l'ensemble : végétaux, légumineuses, fruits, céréales, poisson, convivialité et activité quotidienne. L'huile d'olive y remplace surtout des graisses moins favorables."),
            ("Le rôle culinaire", "Elle rend les légumes plus savoureux, transporte les arômes des herbes, donne de la satiété et aide à cuisiner simplement. Une assiette de tomates, lentilles ou poisson devient complète avec le bon filet d'huile."),
            ("La qualité compte", "Une huile vierge extra récente, bien conservée, apporte plus de caractère et potentiellement plus de composés protecteurs qu'une huile ancienne ou raffinée. La quantité ne compense pas la médiocrité."),
            ("Le bon usage quotidien", "Gardez une huile équilibrée pour cuisiner et une huile plus expressive pour la finition. Cette organisation évite de gaspiller les meilleures bouteilles tout en améliorant chaque repas."),
        ],
        "checklist": ["Végétaux nombreux.", "Huile vierge extra.", "Usage régulier mais mesuré.", "Cuisson simple.", "Finition aromatique."],
        "quote": "Le régime méditerranéen fonctionne parce que l'huile d'olive rend les bons aliments désirables.",
        "faq": [
            ("Combien d'huile par jour ?", "Cela dépend des besoins, mais l'idée est un usage régulier et raisonnable, intégré aux repas."),
            ("Peut-on cuire avec ?", "Oui, surtout en cuisson modérée."),
        ],
    },
    "rituel-recolte": {
        "desc": "Le rituel de la récolte des olives : maturité, cueillette, transport, moulin et impact sur la qualité finale.",
        "lede": "La récolte des olives est un moment décisif : en quelques heures, le producteur peut préserver ou perdre une grande partie de la qualité future.",
        "sections": [
            ("Choisir le bon moment", "La maturité détermine le style : olives vertes pour intensité et polyphénols, olives plus mûres pour douceur et rondeur. Le choix dépend du profil recherché, pas seulement du calendrier."),
            ("Récolter sans abîmer", "Peignes, filets, vibreurs ou cueillette manuelle doivent limiter les blessures. Une olive écrasée ou stockée trop longtemps commence à fermenter, ce qui dégrade l'huile."),
            ("Aller vite au moulin", "Le délai entre arbre et moulin est crucial. Les meilleurs producteurs réduisent l'attente, évitent les sacs qui chauffent et utilisent des caisses aérées. La fraîcheur se joue souvent avant l'extraction."),
            ("Du rituel à la précision", "La récolte garde une dimension collective et culturelle, mais les grandes huiles naissent d'une organisation rigoureuse : tri, propreté, température, traçabilité et dégustation."),
        ],
        "checklist": ["Maturité choisie.", "Fruits non écrasés.", "Caisses aérées.", "Moulin rapide.", "Extraction propre."],
        "quote": "Une bonne huile commence avant le moulin, au moment exact où l'olive quitte l'arbre.",
        "faq": [
            ("Quand récolte-t-on les olives ?", "Selon les régions et le style recherché, souvent de l'automne au début de l'hiver."),
            ("La récolte manuelle est-elle toujours meilleure ?", "Pas toujours. Une récolte mécanique bien conduite peut préserver les fruits efficacement."),
        ],
    },
    "sante-cardiaque": {
        "desc": "Huile d'olive et santé cardiaque : graisses mono-insaturées, polyphénols, régime méditerranéen et prudence médicale.",
        "lede": "L'huile d'olive est souvent associée à la santé cardiovasculaire, surtout lorsqu'elle s'inscrit dans une alimentation méditerranéenne équilibrée.",
        "sections": [
            ("Le rôle des graisses", "L'huile d'olive est riche en acides gras mono-insaturés, notamment l'acide oléique. Utilisée à la place de graisses moins favorables, elle peut améliorer la qualité globale de l'alimentation."),
            ("L'intérêt des polyphénols", "Dans une huile vierge extra fraîche, les composés phénoliques participent à la protection contre l'oxydation. Ils expliquent aussi une partie du piquant et de l'amertume."),
            ("Le contexte alimentaire", "L'huile seule ne suffit pas. Les bénéfices observés sont liés à un ensemble : légumes, fruits, céréales complètes, poissons, légumineuses, noix et faible place des produits ultra-transformés."),
            ("Prudence et bon sens", "L'huile d'olive reste calorique. Elle ne remplace pas un traitement, un suivi médical ou des conseils personnalisés. Son intérêt vient d'un usage régulier mais raisonnable."),
        ],
        "checklist": ["Vierge extra.", "Remplacer plutôt qu'ajouter.", "Associer aux végétaux.", "Quantité raisonnable.", "Avis médical si pathologie."],
        "quote": "Pour le cœur, l'huile d'olive est utile quand elle fait partie d'une assiette cohérente.",
        "faq": [
            ("L'huile d'olive fait-elle baisser le cholestérol ?", "Elle peut contribuer à un meilleur profil alimentaire, mais l'effet dépend de l'ensemble du régime."),
            ("Faut-il la consommer crue ?", "Crue ou en cuisson douce, mais les huiles riches en arômes gagnent à être utilisées en finition."),
        ],
    },
    "savon-maison": {
        "desc": "Fabriquer un savon à l'huile d'olive : principes, sécurité, saponification, cure et qualités du savon obtenu.",
        "lede": "Le savon à l'huile d'olive est un classique, mais sa fabrication demande rigueur, pesées exactes et respect strict des règles de sécurité.",
        "sections": [
            ("Le principe de saponification", "Un savon naît de la réaction entre un corps gras et une base forte. Avec l'huile d'olive, on obtient un savon doux, peu agressif, souvent plus long à sécher qu'un savon riche en graisses plus dures."),
            ("La sécurité avant tout", "La soude caustique exige lunettes, gants, ventilation et précision. On ne modifie pas une recette au hasard. Les quantités doivent être calculées avec un calculateur fiable selon les huiles utilisées."),
            ("La texture du savon olive", "Un savon très riche en olive peut être doux mais moins moussant au début. La cure est importante : plusieurs semaines permettent au savon de durcir et de devenir plus agréable."),
            ("Faire simple pour commencer", "Une formule courte, sans parfum compliqué ni ajouts fragiles, est préférable. L'objectif du premier savon n'est pas l'originalité mais la maîtrise du procédé."),
        ],
        "checklist": ["Recette calculée.", "Protection complète.", "Pesée précise.", "Cure longue.", "Étiquetage de la date."],
        "quote": "Un savon maison réussi est d'abord un savon sûr.",
        "faq": [
            ("Peut-on faire du savon sans soude ?", "Pas un vrai savon par saponification. Les bases prêtes à fondre sont une autre approche."),
            ("Combien de temps de cure ?", "Souvent au moins quatre à six semaines, parfois davantage pour un savon très riche en olive."),
        ],
    },
    "marseille": {
        "desc": "Le véritable savon de Marseille : histoire, composition, huile d'olive, cuisson au chaudron et critères d'authenticité.",
        "lede": "Le savon de Marseille est devenu un symbole, mais son nom est souvent utilisé pour des produits très différents. L'authenticité se lit dans la composition et le procédé.",
        "sections": [
            ("Une tradition de savonnerie", "Le savon de Marseille s'inscrit dans une histoire méditerranéenne liée aux huiles végétales, aux ports, au commerce et aux chaudrons. Sa réputation vient d'un produit simple, robuste et polyvalent."),
            ("La composition à regarder", "Un savon traditionnel contient principalement des huiles végétales, de la soude transformée par saponification, de l'eau et du sel. Les parfums, colorants et nombreux additifs éloignent du modèle classique."),
            ("Olive ou autres huiles", "Le savon vert est souvent associé à l'huile d'olive, tandis que d'autres versions utilisent aussi coprah ou palme selon les fabricants. Le sujet n'est pas seulement la couleur : il faut lire la liste INCI."),
            ("Reconnaître le sérieux", "Cherchez une fabrication au chaudron, une composition courte, un fabricant identifié et une cohérence entre le discours et l'étiquette. Un cube très parfumé n'est pas forcément un savon de Marseille traditionnel."),
        ],
        "checklist": ["Composition courte.", "Fabricant clair.", "Procédé expliqué.", "Pas de parfum obligatoire.", "Lecture INCI."],
        "quote": "Le vrai savon de Marseille n'a pas besoin d'en faire trop : sa force est sa simplicité.",
        "faq": [
            ("Le savon de Marseille est-il toujours à l'huile d'olive ?", "Non, selon les recettes et fabricants. Il faut lire la composition."),
            ("Pourquoi certains sont verts et d'autres blancs ?", "La couleur dépend surtout des huiles utilisées et de la formulation."),
        ],
    },
    "soins-peau": {
        "desc": "Soins de la peau DIY à l'huile d'olive : usages raisonnables, types de peau, recettes simples et précautions.",
        "lede": "L'huile d'olive peut entrer dans des soins maison simples, mais elle doit être utilisée avec discernement selon le type de peau.",
        "sections": [
            ("Ce qu'elle apporte", "Riche en lipides, elle limite la perte d'eau et assouplit les zones sèches. Elle convient mieux aux usages ponctuels sur corps, mains, coudes ou jambes qu'à une routine visage universelle."),
            ("Pour quelles peaux", "Les peaux très sèches peuvent l'apprécier en petite quantité. Les peaux mixtes, grasses ou sujettes aux imperfections doivent être plus prudentes, surtout sur le visage."),
            ("Recettes simples", "Mélangez une cuillère d'huile avec du sucre fin pour un gommage corps rapide, ou quelques gouttes avec du gel d'aloe vera pour un soin mains. Évitez les mélanges complexes qui se conservent mal."),
            ("Hygiène et conservation", "Un soin maison sans conservateur ne doit pas être gardé longtemps, surtout s'il contient de l'eau, du miel, des plantes fraîches ou des produits alimentaires. Préparez de petites quantités."),
        ],
        "checklist": ["Petite quantité.", "Test cutané.", "Pas de conservation longue.", "Éviter yeux et peau irritée.", "Adapter au type de peau."],
        "quote": "Le DIY sérieux n'est pas celui qui mélange le plus d'ingrédients, mais celui qui respecte la peau.",
        "faq": [
            ("Peut-on mettre l'huile d'olive sur le visage ?", "Oui pour certaines peaux sèches, mais ce n'est pas idéal pour tout le monde."),
            ("Peut-elle démaquiller ?", "Elle peut dissoudre du maquillage, mais il faut ensuite nettoyer correctement la peau."),
        ],
    },
    "varietes": {
        "desc": "Top des variétés d'olives à connaître : Picual, Arbequina, Koroneiki, Frantoio, Leccino et autres profils.",
        "lede": "Connaître quelques variétés d'olives aide à mieux acheter une huile, car la variété influence fortement le goût, la stabilité et les accords.",
        "sections": [
            ("Picual", "Très présente en Espagne, la Picual donne souvent des huiles stables, intenses, avec notes de tomate, feuille, olive verte et une belle amertume. Excellente sur légumes, pain, viandes blanches et plats de caractère."),
            ("Arbequina", "Plus douce, ronde et accessible, l'Arbequina évoque souvent amande, pomme et fruits mûrs. Elle convient aux desserts, poissons délicats, mayonnaises et cuisines familiales."),
            ("Koroneiki", "Variété grecque majeure, elle produit des huiles souvent fruitées, herbacées, équilibrées et persistantes. Très polyvalente, elle fonctionne sur salades, légumineuses et poissons."),
            ("Frantoio, Leccino et autres italiennes", "Frantoio apporte élégance, herbe et artichaut. Leccino est souvent plus douce. Coratina, plus puissante, peut être riche en polyphénols et très poivrée."),
        ],
        "checklist": ["Lire la variété.", "Relier variété et usage.", "Ne pas juger au pays seul.", "Goûter plusieurs profils.", "Noter ses préférences."],
        "quote": "La variété est à l'huile d'olive ce que le cépage est au vin : un repère, pas toute l'histoire.",
        "faq": [
            ("Quelle variété pour débuter ?", "Arbequina pour la douceur, Picual ou Koroneiki pour plus de caractère."),
            ("Une huile monovariétale est-elle meilleure ?", "Pas forcément. Elle est plus lisible ; un assemblage peut être très réussi."),
        ],
    },
}


ALIASES = [
    ("3-recettes", "3-recettes"),
    ("accords-mets", "accords-mets"),
    ("certifications-bio", "certifications-bio"),
    ("conservation", "conservation"),
    ("espagne-italie", "espagne-italie"),
    ("frire", "frire"),
    ("gateaux", "gateaux"),
    ("animaux", "animaux"),
    ("cheveux", "cheveux"),
    ("haute-altitude", "haute-altitude"),
    ("recolte-precoce", "recolte-precoce"),
    ("rome-antique", "rome-antique"),
    ("vs-coco", "vs-coco"),
    ("infusees", "infusees"),
    ("ia-moulins", "ia-moulins"),
    ("etiquette", "etiquette"),
    ("oliviers-millenaires", "oliviers-millenaires"),
    ("notes-degustation", "notes-degustation"),
    ("cadeau", "cadeau"),
    ("oleiculture", "oleiculture-durable"),
    ("polyphenols", "polyphenols"),
    ("prix-qualite", "prix-qualite"),
    ("recolte-2026", "recolte-2026"),
    ("regime-mediterraneen", "regime-mediterraneen"),
    ("rituel-recolte", "rituel-recolte"),
    ("sante-cardiaque", "sante-cardiaque"),
    ("savon-maison", "savon-maison"),
    ("savon-marseille", "marseille"),
    ("soins-peau", "soins-peau"),
    ("varietes", "varietes"),
]

TITLE_OVERRIDES = {
    "3-recettes-surprenantes-huile-olive.html": "3 Recettes Surprenantes avec l'Huile d'Olive",
}

ALTERNATE_OVERRIDES = {
    "3-recettes-surprenantes-huile-olive.html": [
        ("fr", f"{SITE}/blog/3-recettes-surprenantes-huile-olive.html"),
        ("en", f"{SITE}/blog/3-surprising-recipes-with-olive-oil.html"),
        ("it", f"{SITE}/blog/3-ricette-sorprendenti-olio-oliva.html"),
        ("el", f"{SITE}/blog/3-ekpliktikes-sintages-me-elaio-lado.html"),
    ],
}

SCENARIOS = {
    "3-recettes": [
        "Pour un dîner rapide : légumes rôtis, yaourt salé et huile verte donnent une assiette complète sans sauce lourde.",
        "Pour un dessert : l'huile douce remplace le beurre dans un cake citron ou une mousse chocolat, avec une texture plus souple.",
        "Pour impressionner sans complexité : servez une glace vanille avec huile fruitée, fleur de sel et zestes d'orange.",
    ],
    "accords-mets": [
        "Tomate ancienne et mozzarella : huile verte, herbacée, avec une légère amertume.",
        "Poisson vapeur ou volaille froide : huile douce à moyenne, notes d'amande ou de pomme.",
        "Houmous, lentilles, aubergines : huile intense et poivrée, capable de tenir face au plat.",
    ],
    "certifications-bio": [
        "Une huile bio sans date de récolte reste difficile à juger.",
        "Une huile non bio mais très fraîche, tracée et bien conservée peut être supérieure en dégustation.",
        "Le meilleur signal est l'accumulation de preuves : logo, origine, récolte, moulin et bouteille protégée.",
    ],
    "conservation": [
        "Bouteille ouverte près des plaques : dégradation accélérée, même si l'huile était excellente.",
        "Bidon opaque dans un placard frais : meilleure protection pour une consommation régulière.",
        "Carafe transparente sur la table : jolie, mais mauvaise idée pour une huile de qualité.",
    ],
    "espagne-italie": [
        "Pour cuisiner tous les jours, une Picual espagnole récente peut offrir un excellent rapport qualité-prix.",
        "Pour une dégustation cadeau, une huile italienne de domaine peut porter un récit régional fort.",
        "Pour juger sérieusement, comparez deux huiles de même fraîcheur plutôt que deux drapeaux.",
    ],
    "frire": [
        "Beignets de courgettes : huile stable, température moyenne, service immédiat.",
        "Pommes de terre sautées : démarrage doux, finition plus vive, salage après cuisson.",
        "Petits poissons : cuisson courte et huile filtrée si une seconde tournée suit rapidement.",
    ],
    "gateaux": [
        "Cake citron : huile douce, zeste abondant et cuisson modérée.",
        "Brownie : huile fruitée mûre, chocolat noir et fleur de sel.",
        "Madeleines : repos de pâte indispensable pour une texture nette.",
    ],
    "animaux": [
        "Chien en bonne santé : micro-dose ponctuelle seulement, intégrée à la ration.",
        "Animal sous régime vétérinaire : pas d'ajout sans avis professionnel.",
        "Huile aromatisée : à éviter, surtout ail, piment ou herbes macérées.",
    ],
    "cheveux": [
        "Cheveux épais et secs : bain d'huile court sur longueurs et pointes.",
        "Cheveux fins : une trace sur les pointes, jamais une application généreuse.",
        "Cuir chevelu sensible : test local avant usage complet.",
    ],
    "haute-altitude": [
        "Soupe de légumes : filet final pour accentuer la fraîcheur.",
        "Fromage frais : quelques gouttes suffisent à faire ressortir le végétal.",
        "Achat : exigez plus que le mot altitude, notamment la récolte et l'origine.",
    ],
    "recolte-precoce": [
        "Pain grillé et tomate : usage idéal pour comprendre l'intensité.",
        "Cuisson longue : mauvais emploi, car l'huile perd ce qui justifie son prix.",
        "Dégustation : amertume et piquant doivent rester nets, jamais sales ou brûlants.",
    ],
    "rome-antique": [
        "À table : l'huile accompagne céréales, légumes et préparations simples.",
        "Dans les bains : elle sert aux soins du corps avant raclage au strigile.",
        "Dans l'économie : les amphores révèlent une logistique méditerranéenne immense.",
    ],
    "vs-coco": [
        "Cuisine quotidienne : avantage à l'huile d'olive pour sa polyvalence.",
        "Curry ou dessert exotique : l'huile de coco peut avoir un intérêt aromatique.",
        "Santé : éviter les slogans et regarder le profil des graisses.",
    ],
    "infusees": [
        "Pizza : piment séché, infusion courte, filtration.",
        "Poisson : zeste de citron bien sec et huile douce.",
        "Ail frais : uniquement pour usage rapide au frais, pas pour une bouteille oubliée.",
    ],
    "ia-moulins": [
        "Tri optique : écarter des fruits abîmés avant qu'ils contaminent le lot.",
        "Malaxage piloté : ajuster temps et température selon la matière réelle.",
        "Traçabilité : relier parcelle, météo, variété et dégustation finale.",
    ],
    "etiquette": [
        "Mention vague d'origine : prudence, surtout si le prix est élevé.",
        "Date de récolte présente : bon signal de transparence.",
        "Bouteille claire : mauvais signal pour une huile censée être premium.",
    ],
    "oliviers-millenaires": [
        "Patrimoine : l'arbre vaut aussi par son paysage et son histoire.",
        "Qualité : l'âge ne remplace pas une extraction rapide et propre.",
        "Protection : éviter l'arrachage décoratif des vieux sujets.",
    ],
    "notes-degustation": [
        "Fruité vert : herbe, artichaut, tomate, feuille.",
        "Fruité mûr : amande, pomme, fruits secs, olive noire.",
        "Défaut : rance, moisi, vineux ou carton humide.",
    ],
    "cadeau": [
        "Amateur curieux : monovariétale expressive et récolte visible.",
        "Usage familial : huile douce, facile, bien protégée.",
        "Coffret : huile, pain, sel, vinaigre doux et fiche d'accords.",
    ],
    "oleiculture-durable": [
        "Sol couvert : moins d'érosion et meilleure vie biologique.",
        "Irrigation pilotée : eau utilisée comme ressource rare.",
        "Prix juste : durabilité impossible si personne n'est correctement rémunéré.",
    ],
    "polyphenols": [
        "Huile jeune : plus grande chance de piquant et d'amertume propres.",
        "Bouteille ouverte longtemps : baisse progressive du profil phénolique.",
        "Usage à cru : meilleur moyen de profiter du relief aromatique.",
    ],
    "prix-qualite": [
        "Récolte précoce : moins de rendement, donc coût plus élevé.",
        "Petit producteur : coût de main-d'œuvre et de moulin plus visible.",
        "Produit cher mais vague : mauvais rapport confiance-prix.",
    ],
    "recolte-2026": [
        "Bonne année locale : possible même si la tendance nationale est moyenne.",
        "Rendement faible : prix plus haut mais parfois grande concentration aromatique.",
        "Achat malin : attendre les premières dégustations, pas seulement les annonces.",
    ],
    "regime-mediterraneen": [
        "Légumes + huile : meilleure satiété et meilleure appétence.",
        "Pain, tomate, huile : simplicité très méditerranéenne, si les produits sont bons.",
        "Erreur : ajouter de l'huile sans améliorer le reste de l'assiette.",
    ],
    "rituel-recolte": [
        "Olives vertes : intensité, amertume, rendement plus faible.",
        "Olives mûres : douceur, rondeur, profil plus accessible.",
        "Transport lent : risque de fermentation avant extraction.",
    ],
    "sante-cardiaque": [
        "Remplacer le beurre dans certains usages, plutôt qu'ajouter de l'huile partout.",
        "Associer l'huile aux légumes, légumineuses et poissons.",
        "Garder une approche médicale sérieuse en cas de pathologie.",
    ],
    "savon-maison": [
        "Débutant : recette courte, calculée, sans parfum compliqué.",
        "Soude : protection, ventilation, pesée exacte.",
        "Cure : patience indispensable pour obtenir un savon agréable.",
    ],
    "marseille": [
        "Cube parfumé très coloré : pas forcément traditionnel.",
        "Composition courte : signal plus fiable que l'emballage.",
        "Fabricant identifié : essentiel pour juger la crédibilité.",
    ],
    "soins-peau": [
        "Corps sec : quelques gouttes après la douche.",
        "Visage réactif : test local et quantité minimale.",
        "DIY avec eau : conservation courte, hygiène stricte.",
    ],
    "varietes": [
        "Picual : intensité et stabilité.",
        "Arbequina : douceur et pâtisserie.",
        "Koroneiki : équilibre grec, très polyvalent.",
    ],
}


def read(path):
    return path.read_text(encoding="utf-8")


def write(path, content):
    path.write_text(content, encoding="utf-8", newline="\n")


def parse_h1(text):
    match = re.search(r"<h1>(.*?)</h1>", text, re.S)
    if match:
        return html.unescape(re.sub(r"<.*?>", "", match.group(1)).strip())
    return "Article L'Or Vert"


def parse_alternates(text):
    return re.findall(r'<link\s+rel="alternate"\s+hreflang="([^"]+)"\s+href="([^"]+)"\s*/?>', text)


def hreflang_html(alternates):
    return "\n".join(f'    <link rel="alternate" hreflang="{lang}" href="{href}" />' for lang, href in alternates)


def lang_switch(alternates, current_name):
    if not alternates:
        return ""
    links = []
    for lang, href in alternates:
        fname = Path(href).name
        active = "active" if fname == current_name else ""
        links.append(f'<a href="{html.escape(fname)}" class="{active}">{lang.upper()}</a>')
    return f'<div class="lang-switch">{" ".join(links)}</div>'


def esc(value):
    return html.escape(value, quote=True)


def topic_for(path):
    name = path.name
    for needle, key in ALIASES:
        if needle in name:
            return key
    if name == "secrets-oliviers-millenaires.html":
        return "oliviers-millenaires"
    return None


def criterion_reason(item):
    low = item.lower()
    if "récolte" in low or "fraî" in low or "récente" in low:
        return "La fraîcheur influence directement le goût, la stabilité et la crédibilité du produit."
    if "origine" in low or "producteur" in low or "moulin" in low:
        return "Une origine lisible réduit le flou marketing et rend la comparaison possible."
    if "bouteille" in low or "placard" in low or "lumière" in low or "conservation" in low:
        return "La protection contre la lumière, l'air et la chaleur évite de ruiner une bonne huile."
    if "douceur" in low or "fruité" in low or "intense" in low or "piquant" in low:
        return "L'intensité doit correspondre au plat ; sinon l'huile domine ou disparaît."
    if "quantité" in low or "petite" in low or "mesuré" in low:
        return "Le dosage sépare un usage élégant d'un résultat lourd ou déséquilibré."
    if "sécurité" in low or "avis" in low or "protection" in low:
        return "Le sujet touche à l'usage domestique ou au bien-être : la prudence évite les mauvais conseils."
    if "goûter" in low or "dégust" in low:
        return "La dégustation confirme ce que l'étiquette promet, et révèle vite les défauts."
    if "prix" in low or "cohérent" in low:
        return "Le prix doit être justifié par des preuves, pas seulement par un packaging premium."
    return "Ce critère transforme une impression vague en décision concrète et vérifiable."


def five_minute_method(checklist):
    steps = []
    for item in checklist[:5]:
        steps.append(f"Vérifiez : {item[0].lower() + item[1:] if item else item}")
    while len(steps) < 5:
        steps.append("Goûtez, comparez et notez votre impression avant de décider.")
    return steps


def scenario_reason(scenario):
    low = scenario.lower()
    if "tomate" in low or "mozzarella" in low or "burrata" in low:
        return "Le plat est simple et très exposé : la moindre lourdeur se sent, mais une huile bien choisie donne immédiatement du relief."
    if "poisson" in low or "volaille" in low or "fruits de mer" in low:
        return "La finesse de la chair impose une huile précise, sans excès d'amertume, avec une finale propre."
    if "houmous" in low or "lentilles" in low or "pois" in low or "aubergines" in low:
        return "Les légumineuses et légumes denses acceptent une huile plus expressive, capable d'apporter de la verticalité."
    if "bouteille" in low or "placard" in low or "carafe" in low or "ouverte" in low:
        return "La qualité se joue ici après l'achat : une mauvaise conservation peut annuler le travail du producteur."
    if "récolte" in low or "olive jeune" in low or "huile jeune" in low:
        return "La date et la maturité donnent une indication concrète sur l'énergie aromatique que l'on peut attendre."
    if "dessert" in low or "cake" in low or "chocolat" in low or "madeleine" in low:
        return "En sucré, la réussite dépend d'une huile douce et fraîche ; trop d'intensité ferait basculer le dessert."
    if "animal" in low or "chien" in low or "chat" in low or "vétérinaire" in low:
        return "Le bénéfice potentiel ne justifie jamais l'improvisation : le dosage et l'état de santé passent avant l'astuce."
    if "savon" in low or "soude" in low or "cure" in low:
        return "La précision compte davantage que la créativité : une petite erreur de formulation peut changer le résultat final."
    if "label" in low or "bio" in low or "logo" in low:
        return "Le signe officiel rassure, mais il doit être confirmé par des informations de fraîcheur, d'origine et de stockage."
    if "ia" in low or "capteur" in low or "traçabilité" in low or "malaxage" in low:
        return "La technologie n'a de valeur que si elle améliore une décision mesurable : trier mieux, extraire mieux, comprendre mieux."
    if "prix" in low or "cher" in low or "coût" in low:
        return "Le prix devient acceptable lorsqu'il s'explique par des preuves visibles, pas par une simple posture premium."
    if "cœur" in low or "santé" in low or "graisses" in low:
        return "Le sujet doit rester sérieux : l'huile d'olive s'inscrit dans une alimentation complète, pas dans une promesse miracle."
    if "variété" in low or "picual" in low or "arbequina" in low or "koroneiki" in low:
        return "La variété donne un repère de goût comparable à un cépage, utile pour choisir sans se limiter au pays."
    return "L'intérêt est de passer du principe au geste : ce que l'on fait réellement avec la bouteille change le résultat."


def render_article(path, key, data):
    old = read(path)
    title = TITLE_OVERRIDES.get(path.name, parse_h1(old))
    alternates = parse_alternates(old) or ALTERNATE_OVERRIDES.get(path.name, [])
    scenarios = SCENARIOS.get(key, [])
    scenario_html = "\n".join(f"            <li>{esc(item)}</li>" for item in scenarios)
    table_rows = "\n".join(
        f"            <tr><td>{i}</td><td>{esc(item)}</td><td>{esc(criterion_reason(item))}</td></tr>"
        for i, item in enumerate(data["checklist"], 1)
    )
    method_items = "\n".join(f"            <li>{esc(step)}</li>" for step in five_minute_method(data["checklist"]))
    section_html = []
    for index, (heading, paragraph) in enumerate(data["sections"]):
        scenario = scenarios[index % len(scenarios)] if scenarios else data["quote"]
        section_html.append(
            f"""        <h2>{esc(heading)}</h2>
        <p>{esc(paragraph)}</p>
        <p><strong>Exemple concret :</strong> {esc(scenario)} {esc(scenario_reason(scenario))}</p>"""
        )
    checklist = "\n".join(f"            <li>{esc(item)}</li>" for item in data["checklist"])
    faqs = "\n".join(
        f"""        <h3>{esc(question)}</h3>
        <p>{esc(answer)}</p>"""
        for question, answer in data["faq"]
    )
    schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": data["desc"],
        "author": {"@type": "Organization", "name": "L'Or Vert"},
        "dateModified": "2026-05-04",
        "mainEntityOfPage": f"{SITE}/blog/{path.name}",
    }
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{esc(title)} — Blog L'Or Vert</title>
    <meta name="description" content="{esc(data["desc"])}">
    <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%232E4A40'/%3E%3Cpath fill='%23F2D8C4' d='M16 5.5S9.5 14 9.5 19a6.5 6.5 0 0013 0c0-5-6.5-13.5-6.5-13.5z'/%3E%3C/svg%3E" type="image/svg+xml">
    <link rel="stylesheet" href="../assets/seo.css">
{hreflang_html(alternates)}
    <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False, indent=2)}</script>
</head>
<body>
<nav class="site-nav"><div class="container"><a href="../index.html" class="logo">L'OR VERT / BLOG</a>{lang_switch(alternates, path.name)}</div></nav>
<header class="page-hero" style="background: linear-gradient(135deg, var(--pine) 0%, var(--avocado-dark) 100%);">
    <div class="container">
        <div class="breadcrumb"><a href="../index.html">Accueil</a> &raquo; Blog</div>
        <h1>{esc(title)}</h1>
        <p class="lede">{esc(data["lede"])}</p>
        <div class="meta">Mis à jour : 4 mai 2026 &middot; 8 min de lecture</div>
    </div>
</header>
<main class="container">
    <article class="guide">
        <p class="intro">{esc(data["lede"])}</p>

        <div class="callout"><strong>Réponse courte :</strong> {esc(data["sections"][0][1])}</div>

{chr(10).join(section_html)}

        <h2>Cas pratiques</h2>
        <p>Voici comment appliquer ce sujet dans une vraie cuisine, devant une vraie bouteille ou au moment d'acheter. Ces cas concrets sont volontairement simples : ils servent à prendre une décision rapide sans perdre l'exigence de qualité.</p>
        <ul>
{scenario_html}
        </ul>

        <h2>Grille de décision</h2>
        <p>Un bon choix ne dépend jamais d'un seul mot imprimé sur l'étiquette ou répété dans une fiche produit. Il faut croiser plusieurs signaux : ce que le produit promet, ce qu'il prouve, et ce que votre usage demande vraiment.</p>
        <table>
            <thead><tr><th>#</th><th>Critère</th><th>Pourquoi cela compte</th></tr></thead>
            <tbody>
{table_rows}
            </tbody>
        </table>

        <h2>Méthode en 5 minutes</h2>
        <p>Si vous devez décider vite, utilisez cette méthode courte. Elle ne remplace pas une dégustation complète, mais elle évite la plupart des erreurs grossières et force à regarder les bons détails.</p>
        <ol>
{method_items}
        </ol>

        <h2>À vérifier avant d'acheter ou d'utiliser</h2>
        <ul>
{checklist}
        </ul>

        <h2>Ce que les contenus moyens oublient</h2>
        <p>Les contenus faibles répètent souvent les mêmes promesses : naturel, sain, méditerranéen, authentique. Un contenu utile doit aller plus loin : expliquer les limites, les exceptions, les mauvais usages et les critères qui séparent une bonne décision d'une simple impression marketing.</p>
        <p>Le point essentiel est de relier le produit à son contexte. Une huile, une méthode, un label ou une tradition ne valent jamais seuls : ils prennent leur sens avec une date de récolte, une origine, un usage précis, une conservation correcte et un goût vérifiable.</p>

        <h2>Signaux de sérieux</h2>
        <p>Un contenu ou une marque sérieuse accepte la nuance. Elle ne promet pas que tout est miraculeux, ne cache pas les limites et ne transforme pas chaque usage en argument de vente. Elle donne des repères qui aident vraiment à choisir, à goûter, à cuisiner ou à conserver.</p>
        <p>Le signe le plus fiable reste la cohérence : un discours précis, une information traçable, une recommandation adaptée à l'usage et une expérience en bouche qui confirme le récit. Quand l'un de ces éléments manque, il faut ralentir et comparer.</p>

        <blockquote>"{esc(data["quote"])}"</blockquote>

        <h2>Pourquoi cette page peut être citée</h2>
        <p>Une page devient citée quand elle donne une réponse claire, puis montre le raisonnement qui la soutient. Il faut des exemples, des limites, des critères et un vocabulaire suffisamment précis pour être repris sans déformer le sens.</p>
        <p>C'est aussi ce qui aide les moteurs de recherche et les assistants IA : ils peuvent identifier le sujet, extraire une réponse utile et comprendre que le contenu ne se limite pas à empiler des mots-clés. La valeur vient de la structure, de la nuance et de la capacité à guider une vraie décision.</p>
        <p>La longueur seule ne suffit pas. Ce qui rend l'article plus fort, c'est l'équilibre entre profondeur, clarté et jugement pratique : assez de matière pour satisfaire un lecteur exigeant, assez de structure pour répondre vite, et assez de nuance pour éviter les affirmations superficielles.</p>

        <h2>Questions fréquentes</h2>
{faqs}

        <h2>Conclusion</h2>
        <p>{esc(title)} n'est pas un sujet à traiter en trois lignes. Pour obtenir un résultat sérieux, il faut croiser la qualité du produit, le geste, le contexte et l'objectif final. C'est cette combinaison qui rend l'information utile, mémorisable et digne d'être citée.</p>
    </article>
</main>
<footer class="site-footer"><div class="container"><h3>L'Or Vert</h3><p>Articles experts sur l'huile d'olive, la cuisine méditerranéenne, les usages maison et la culture de l'olivier.</p><div class="copyright">&copy; 2026 — L'Or Vert</div></div></footer>
</body>
</html>
"""


def main():
    changed = []
    missing = []
    for path in sorted(BLOG_DIR.glob("*.html")):
        text = read(path)
        if '<html lang="fr"' not in text and path.name not in TITLE_OVERRIDES:
            continue
        key = topic_for(path)
        if not key or key not in ARTICLES:
            missing.append(path.name)
            continue
        write(path, render_article(path, key, ARTICLES[key]))
        changed.append(path.name)
    print(f"Rewritten {len(changed)} French blog articles one by one.")
    if missing:
        print("Missing:", ", ".join(missing))


if __name__ == "__main__":
    main()

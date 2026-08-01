import html
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
BLOG_DIR = ROOT / "blog"
RECIPES_DIR = ROOT / "recipes"
SITE = "https://huiledefes.com"


LANGS = {
    "fr": {
        "index": "index-fr.html",
        "home": "Accueil",
        "blog": "Blog",
        "recipes": "Recettes",
        "posted": "Mis a jour",
        "read": "min de lecture",
        "servings": "personnes",
        "prep": "Preparation",
        "cook": "Cuisson",
        "rest": "Repos",
        "difficulty": "Difficulte",
        "easy": "Facile",
        "medium": "Intermediaire",
        "ingredients": "Ingredients",
        "steps": "Preparation pas a pas",
        "oil_role": "Le role de l'huile d'olive",
        "tips": "Conseils de reussite",
        "variations": "Variantes et accords",
        "storage": "Conservation",
        "article_intro": "Un article de fond pour comprendre le sujet, faire les bons choix et utiliser l'huile d'olive avec plus de precision au quotidien.",
        "takeaway": "Ce qu'il faut retenir",
        "understand": "Comprendre le contexte",
        "choose": "Comment choisir et utiliser",
        "mistakes": "Les erreurs a eviter",
        "further": "Pour aller plus loin",
        "expert": "Note de l'expert",
        "footer": "Le carnet de reference de L'Or Vert sur l'huile d'olive, la cuisine mediterraneenne et les usages du quotidien.",
        "date": "4 mai 2026",
        "blog_desc": "{title} : conseils pratiques, criteres de choix, erreurs a eviter et usages concrets de l'huile d'olive.",
        "recipe_desc": "{title} : recette detaillee a l'huile d'olive, ingredients, methode pas a pas, conseils et variantes.",
        "article_depth": "{title} merite plus qu'une definition rapide : il faut relier le produit, le geste et l'usage final pour obtenir un resultat coherent.",
        "article_further": "Une bonne approche consiste a comparer deux huiles sur le meme aliment : une huile douce et mure, puis une huile plus verte et ardente. Cette degustation simple montre immediatement comment l'origine, la recolte et la fraicheur modifient l'equilibre du plat.",
        "article_quote": "Une huile d'olive serieuse se juge dans le detail : fraicheur, equilibre, usage juste et plaisir net en bouche.",
        "recipe_intro": "{title} met l'huile d'olive au centre de l'assiette : elle apporte le parfum, la texture et la liaison qui donnent une impression de cuisine soignee sans compliquer le geste.",
    },
    "en": {
        "index": "index-en.html",
        "home": "Home",
        "blog": "Blog",
        "recipes": "Recipes",
        "posted": "Updated",
        "read": "min read",
        "servings": "servings",
        "prep": "Prep",
        "cook": "Cook",
        "rest": "Rest",
        "difficulty": "Difficulty",
        "easy": "Easy",
        "medium": "Intermediate",
        "ingredients": "Ingredients",
        "steps": "Step-by-step method",
        "oil_role": "The role of olive oil",
        "tips": "Success tips",
        "variations": "Variations and pairings",
        "storage": "Storage",
        "article_intro": "A substantial guide to understand the topic, make better choices and use olive oil with more confidence every day.",
        "takeaway": "Key takeaways",
        "understand": "Understanding the context",
        "choose": "How to choose and use it",
        "mistakes": "Mistakes to avoid",
        "further": "Going further",
        "expert": "Expert note",
        "footer": "L'Or Vert's reference notebook for olive oil, Mediterranean cooking and everyday uses.",
        "date": "May 4, 2026",
        "blog_desc": "{title}: practical advice, buying criteria, mistakes to avoid and concrete olive oil uses.",
        "recipe_desc": "{title}: a detailed olive-oil recipe with ingredients, step-by-step method, tips and variations.",
        "article_depth": "{title} deserves more than a quick definition: product quality, technique and final use all need to work together.",
        "article_further": "A useful exercise is to compare two oils on the same food: one mild and ripe, then one greener and more peppery. The contrast quickly shows how origin, harvest and freshness change the balance of a dish.",
        "article_quote": "A serious olive oil is judged in the details: freshness, balance, accurate use and a clean pleasure on the palate.",
        "recipe_intro": "{title} puts olive oil at the center of the plate: it brings aroma, texture and cohesion while keeping the method approachable.",
    },
    "it": {
        "index": "index-it.html",
        "home": "Home",
        "blog": "Blog",
        "recipes": "Ricette",
        "posted": "Aggiornato",
        "read": "min di lettura",
        "servings": "persone",
        "prep": "Preparazione",
        "cook": "Cottura",
        "rest": "Riposo",
        "difficulty": "Difficolta",
        "easy": "Facile",
        "medium": "Intermedia",
        "ingredients": "Ingredienti",
        "steps": "Preparazione passo passo",
        "oil_role": "Il ruolo dell'olio d'oliva",
        "tips": "Consigli di riuscita",
        "variations": "Varianti e abbinamenti",
        "storage": "Conservazione",
        "article_intro": "Una guida completa per capire il tema, scegliere meglio e usare l'olio d'oliva con piu precisione ogni giorno.",
        "takeaway": "Cosa ricordare",
        "understand": "Capire il contesto",
        "choose": "Come scegliere e usare",
        "mistakes": "Errori da evitare",
        "further": "Per andare oltre",
        "expert": "Nota dell'esperto",
        "footer": "Il quaderno di riferimento di L'Or Vert su olio d'oliva, cucina mediterranea e usi quotidiani.",
        "date": "4 maggio 2026",
        "blog_desc": "{title}: consigli pratici, criteri di scelta, errori da evitare e usi concreti dell'olio d'oliva.",
        "recipe_desc": "{title}: ricetta dettagliata con olio d'oliva, ingredienti, metodo passo passo, consigli e varianti.",
        "article_depth": "{title} merita piu di una definizione rapida: qualita del prodotto, gesto e uso finale devono lavorare insieme.",
        "article_further": "Un esercizio utile e confrontare due oli sullo stesso alimento: uno dolce e maturo, poi uno piu verde e piccante. Il contrasto mostra subito come origine, raccolta e freschezza cambiano l'equilibrio del piatto.",
        "article_quote": "Un olio d'oliva serio si giudica nei dettagli: freschezza, equilibrio, uso giusto e piacere pulito al palato.",
        "recipe_intro": "{title} mette l'olio d'oliva al centro del piatto: porta profumo, texture e coesione senza rendere complicato il metodo.",
    },
    "el": {
        "index": "index-el.html",
        "home": "Αρχική",
        "blog": "Blog",
        "recipes": "Συνταγές",
        "posted": "Ενημερώθηκε",
        "read": "λεπτά ανάγνωσης",
        "servings": "μερίδες",
        "prep": "Προετοιμασία",
        "cook": "Μαγείρεμα",
        "rest": "Ανάπαυση",
        "difficulty": "Δυσκολία",
        "easy": "Εύκολη",
        "medium": "Μέτρια",
        "ingredients": "Υλικά",
        "steps": "Εκτέλεση βήμα προς βήμα",
        "oil_role": "Ο ρόλος του ελαιολάδου",
        "tips": "Συμβουλές επιτυχίας",
        "variations": "Παραλλαγές και συνδυασμοί",
        "storage": "Συντήρηση",
        "article_intro": "Ένας αναλυτικός οδηγός για να κατανοήσετε το θέμα, να κάνετε καλύτερες επιλογές και να χρησιμοποιείτε το ελαιόλαδο με περισσότερη σιγουριά.",
        "takeaway": "Τι να θυμάστε",
        "understand": "Κατανόηση του πλαισίου",
        "choose": "Πώς να επιλέξετε και να χρησιμοποιήσετε",
        "mistakes": "Λάθη που πρέπει να αποφύγετε",
        "further": "Για περισσότερη εμβάθυνση",
        "expert": "Σημείωση ειδικού",
        "footer": "Το σημειωματάριο αναφοράς του L'Or Vert για το ελαιόλαδο, τη μεσογειακή κουζίνα και την καθημερινή χρήση.",
        "date": "4 Μαΐου 2026",
        "blog_desc": "{title}: πρακτικές συμβουλές, κριτήρια επιλογής, λάθη προς αποφυγή και συγκεκριμένες χρήσεις ελαιολάδου.",
        "recipe_desc": "{title}: αναλυτική συνταγή με ελαιόλαδο, υλικά, βήματα, συμβουλές και παραλλαγές.",
        "article_depth": "Το θέμα {title} αξίζει περισσότερα από έναν σύντομο ορισμό: ποιότητα προϊόντος, τεχνική και τελική χρήση πρέπει να συνδέονται.",
        "article_further": "Μια χρήσιμη δοκιμή είναι να συγκρίνετε δύο λάδια στο ίδιο τρόφιμο: ένα ήπιο και ώριμο και έπειτα ένα πιο πράσινο και πιπεράτο. Η διαφορά δείχνει αμέσως πώς προέλευση, συγκομιδή και φρεσκάδα αλλάζουν την ισορροπία.",
        "article_quote": "Ένα σοβαρό ελαιόλαδο κρίνεται στη λεπτομέρεια: φρεσκάδα, ισορροπία, σωστή χρήση και καθαρή απόλαυση.",
        "recipe_intro": "Το {title} βάζει το ελαιόλαδο στο κέντρο του πιάτου: φέρνει άρωμα, υφή και συνοχή χωρίς να κάνει τη μέθοδο δύσκολη.",
    },
}


BLOG_THEMES = [
    (("polyphenol", "polyphenol", "polifenol", "πολυφ"), {
        "fr": {
            "lede": "Les polyphenols expliquent une grande partie de la valeur nutritionnelle et sensorielle d'une huile d'olive de qualite.",
            "context": "Ces composes naturels protegent l'huile de l'oxydation et donnent les sensations d'amertume, de piquant et de fraicheur que l'on recherche dans les meilleurs crus. Plus une huile est recente, bien extraite et bien conservee, plus son profil phenolique a des chances d'etre expressif.",
            "choice": "Cherchez une recolte recente, une bouteille sombre, une origine precise et une mention d'extraction mecanique. En bouche, un leger picotement dans la gorge est souvent bon signe.",
            "bullets": ["Privilegez les huiles de recolte precoce pour un profil plus intense.", "Evitez les bouteilles transparentes exposees en rayon.", "Utilisez ces huiles surtout a cru pour preserver leurs nuances."],
            "mistakes": ["Confondre douceur et qualite : une huile tres douce peut etre agreable mais pauvre en relief.", "Garder la bouteille ouverte plusieurs mois pres d'une source de chaleur.", "Acheter uniquement au prix sans lire la date de recolte."],
        },
        "en": {
            "lede": "Polyphenols explain much of the nutritional and sensory value of a high-quality olive oil.",
            "context": "These natural compounds protect the oil from oxidation and create the bitterness, peppery finish and freshness found in the best oils. A recent harvest, careful extraction and proper storage all help preserve them.",
            "choice": "Look for a recent harvest, a dark bottle, a precise origin and mechanical extraction. On the palate, a gentle catch in the throat is often a positive sign.",
            "bullets": ["Choose early-harvest oils when you want intensity.", "Avoid clear bottles exposed to strong light.", "Use these oils mostly raw to preserve their nuance."],
            "mistakes": ["Assuming a very mild oil is automatically better.", "Keeping an opened bottle near heat for months.", "Buying on price alone without checking harvest information."],
        },
        "it": {
            "lede": "I polifenoli spiegano gran parte del valore nutrizionale e sensoriale di un olio d'oliva di qualita.",
            "context": "Questi composti naturali proteggono l'olio dall'ossidazione e creano amarezza, piccantezza e freschezza. Raccolta recente, estrazione accurata e buona conservazione aiutano a preservarli.",
            "choice": "Cercate raccolta recente, bottiglia scura, origine precisa ed estrazione meccanica. In bocca, un leggero pizzicore in gola e spesso un segnale positivo.",
            "bullets": ["Scegliete oli da raccolta precoce per maggiore intensita.", "Evitate bottiglie trasparenti esposte alla luce.", "Usateli soprattutto a crudo per rispettarne le sfumature."],
            "mistakes": ["Pensare che un olio molto dolce sia sempre migliore.", "Tenere la bottiglia aperta vicino al calore.", "Comprare solo in base al prezzo senza leggere la raccolta."],
        },
        "el": {
            "lede": "Οι πολυφαινόλες εξηγούν μεγάλο μέρος της θρεπτικής και γευστικής αξίας ενός ποιοτικού ελαιολάδου.",
            "context": "Αυτές οι φυσικές ενώσεις προστατεύουν το λάδι από την οξείδωση και δίνουν πικράδα, πικάντικη επίγευση και φρεσκάδα. Η πρόσφατη συγκομιδή, η προσεκτική έκθλιψη και η σωστή φύλαξη τις διατηρούν καλύτερα.",
            "choice": "Αναζητήστε πρόσφατη συγκομιδή, σκούρο μπουκάλι, σαφή προέλευση και μηχανική έκθλιψη. Ένα απαλό κάψιμο στον λαιμό είναι συχνά καλό σημάδι.",
            "bullets": ["Προτιμήστε πρώιμη συγκομιδή για πιο έντονο προφίλ.", "Αποφύγετε διαφανή μπουκάλια σε δυνατό φως.", "Χρησιμοποιήστε τα κυρίως ωμά για να κρατήσουν τις αποχρώσεις τους."],
            "mistakes": ["Να θεωρείτε ότι ένα πολύ ήπιο λάδι είναι πάντα καλύτερο.", "Να αφήνετε ανοιχτό μπουκάλι κοντά στη ζέστη.", "Να αγοράζετε μόνο με βάση την τιμή."],
        },
    }),
    (("conserv", "store", "φυλά", "conservare"), {
        "fr": {
            "lede": "La conservation est decisive : une excellente huile peut perdre son fruit en quelques semaines si elle est mal protegee.",
            "context": "L'huile d'olive craint trois ennemis simples : la lumiere, l'air et la chaleur. Ils accelerent l'oxydation, fatiguent les aromes et peuvent transformer un fruit frais en notes plates ou rances.",
            "choice": "Choisissez une bouteille sombre ou un bidon opaque, refermez rapidement apres service et gardez l'huile entre 14 et 18 degres si possible.",
            "bullets": ["Achetez des formats adaptes a votre consommation reelle.", "Notez la date d'ouverture sur les grands contenants.", "Gardez une huile douce pour la cuisson et une huile plus expressive pour la finition."],
            "mistakes": ["Laisser la bouteille pres des plaques de cuisson.", "Transvaser dans une carafe decorative transparente.", "Confondre date de durabilite et fraicheur aromatique."],
        },
        "en": {
            "lede": "Storage is decisive: even an excellent oil can lose its fruitiness in weeks if it is poorly protected.",
            "context": "Olive oil has three simple enemies: light, air and heat. They speed up oxidation, dull aromas and can turn fresh fruit into flat or rancid notes.",
            "choice": "Choose a dark bottle or opaque tin, close it quickly after pouring and keep it around 14 to 18 degrees Celsius when possible.",
            "bullets": ["Buy bottle sizes that match your real usage.", "Write the opening date on large containers.", "Keep a mild oil for cooking and a more expressive one for finishing."],
            "mistakes": ["Leaving the bottle near the stove.", "Pouring it into a clear decorative cruet.", "Confusing best-before dates with aromatic freshness."],
        },
        "it": {
            "lede": "La conservazione e decisiva: anche un ottimo olio puo perdere frutto in poche settimane se non e protetto.",
            "context": "L'olio teme tre nemici: luce, aria e calore. Accelerano l'ossidazione, spengono gli aromi e trasformano il frutto fresco in note piatte o rancide.",
            "choice": "Scegliete bottiglie scure o latte opache, richiudete subito e conservate intorno ai 14-18 gradi quando possibile.",
            "bullets": ["Comprate formati adatti al vostro consumo reale.", "Segnate la data di apertura sui contenitori grandi.", "Tenete un olio delicato per cuocere e uno piu espressivo per finire."],
            "mistakes": ["Lasciare la bottiglia vicino ai fornelli.", "Travasa­re in una cruet trasparente decorativa.", "Confondere la scadenza con la freschezza aromatica."],
        },
        "el": {
            "lede": "Η συντήρηση είναι καθοριστική: ακόμη και ένα εξαιρετικό λάδι χάνει τον φρουτώδη χαρακτήρα του αν δεν προστατευθεί.",
            "context": "Το ελαιόλαδο φοβάται το φως, τον αέρα και τη ζέστη. Αυτά επιταχύνουν την οξείδωση, κουράζουν τα αρώματα και οδηγούν σε επίπεδες ή ταγγές νότες.",
            "choice": "Διαλέξτε σκούρο μπουκάλι ή αδιαφανές δοχείο, κλείνετε γρήγορα μετά τη χρήση και φυλάξτε το σε δροσερό σημείο.",
            "bullets": ["Αγοράστε μέγεθος που ταιριάζει στην κατανάλωσή σας.", "Σημειώστε την ημερομηνία ανοίγματος.", "Κρατήστε ένα ήπιο λάδι για μαγείρεμα και ένα έντονο για τελείωμα."],
            "mistakes": ["Να μένει δίπλα στην εστία.", "Να μπαίνει σε διαφανή διακοσμητική καράφα.", "Να μπερδεύετε την ημερομηνία λήξης με την αρωματική φρεσκάδα."],
        },
    }),
    (("frire", "fry", "friggere", "τηγάν"), {
        "fr": {
            "lede": "Frire a l'huile d'olive n'est pas une heresie : tout depend de la temperature, de la qualite et de la duree de cuisson.",
            "context": "Une huile d'olive vierge extra stable supporte tres bien les cuissons domestiques maitrisees. Sa richesse en acides gras monoinsatures lui donne une bonne tenue, a condition de ne pas la surchauffer ni la reutiliser sans discernement.",
            "choice": "Travaillez autour de 160 a 180 degres, sechez les aliments avant cuisson et filtrez l'huile si vous devez l'utiliser une seconde fois rapidement.",
            "bullets": ["Preferez des morceaux de taille reguliere.", "Salez apres cuisson pour garder le croustillant.", "Gardez les huiles tres aromatiques pour la finition."],
            "mistakes": ["Attendre que l'huile fume pour commencer.", "Melanger plusieurs huiles fatiguees.", "Surcharger la poele et faire chuter la temperature."],
        },
        "en": {
            "lede": "Frying with olive oil is not a mistake: the result depends on temperature, quality and cooking time.",
            "context": "A stable extra virgin olive oil handles controlled home cooking very well. Its monounsaturated fat profile gives it good resistance as long as it is not overheated or reused carelessly.",
            "choice": "Work around 160 to 180 degrees Celsius, dry food before frying and filter the oil if you plan a quick second use.",
            "bullets": ["Cut food into even pieces.", "Salt after frying to keep crispness.", "Save very aromatic oils for finishing."],
            "mistakes": ["Waiting until the oil smokes.", "Mixing several tired oils.", "Overcrowding the pan and dropping the temperature."],
        },
        "it": {
            "lede": "Friggere con olio d'oliva non e un errore: tutto dipende da temperatura, qualita e tempo.",
            "context": "Un extravergine stabile sopporta bene le cotture domestiche controllate. La ricchezza in monoinsaturi lo rende resistente, purche non venga surriscaldato o riutilizzato male.",
            "choice": "Lavorate tra 160 e 180 gradi, asciugate gli alimenti e filtrate l'olio se volete usarlo di nuovo a breve.",
            "bullets": ["Tagliate pezzi di misura regolare.", "Salate dopo la cottura per mantenere croccantezza.", "Usate gli oli molto aromatici a crudo."],
            "mistakes": ["Aspettare che l'olio fumi.", "Mescolare oli gia stanchi.", "Riempire troppo la padella."],
        },
        "el": {
            "lede": "Το τηγάνισμα με ελαιόλαδο δεν είναι λάθος: σημασία έχουν η θερμοκρασία, η ποιότητα και ο χρόνος.",
            "context": "Ένα σταθερό εξαιρετικό παρθένο ελαιόλαδο αντέχει καλά σε ελεγχόμενο οικιακό μαγείρεμα. Τα μονοακόρεστα λιπαρά του προσφέρουν αντοχή, αρκεί να μη ζεσταθεί υπερβολικά.",
            "choice": "Δουλέψτε περίπου στους 160-180 βαθμούς, στεγνώστε τα τρόφιμα και φιλτράρετε το λάδι αν το χρησιμοποιήσετε ξανά άμεσα.",
            "bullets": ["Κόψτε τα υλικά σε ομοιόμορφα κομμάτια.", "Αλατίστε μετά το τηγάνισμα.", "Κρατήστε τα πολύ αρωματικά λάδια για το τελείωμα."],
            "mistakes": ["Να περιμένετε να καπνίσει το λάδι.", "Να ανακατεύετε κουρασμένα λάδια.", "Να γεμίζετε υπερβολικά το τηγάνι."],
        },
    }),
    (("cheveux", "hair", "capelli", "μαλλ"), {
        "fr": {
            "lede": "Sur les cheveux, l'huile d'olive est interessante lorsqu'elle est utilisee avec parcimonie, comme soin nourrissant avant lavage.",
            "context": "Elle aide a assouplir les longueurs seches et a limiter la sensation de cheveux cassants. Son interet vient surtout de son pouvoir emollient : elle gaine la fibre et reduit la perte d'eau, sans remplacer un soin dermatologique en cas de probleme du cuir chevelu.",
            "choice": "Appliquez une petite quantite sur les longueurs, laissez poser 20 a 40 minutes, puis lavez soigneusement avec un shampooing doux.",
            "bullets": ["Rechauffez l'huile dans les mains plutot qu'au micro-ondes.", "Insistez sur les pointes, pas sur les racines grasses.", "Testez d'abord sur une petite zone si le cuir chevelu est sensible."],
            "mistakes": ["Saturer les cheveux fins avec trop de produit.", "Dormir avec une serviette humide toute la nuit.", "Utiliser une huile rance dont l'odeur reste sur la fibre."],
        },
        "en": {
            "lede": "For hair, olive oil works best in small amounts as a nourishing pre-wash treatment.",
            "context": "It can soften dry lengths and reduce the brittle feel of damaged hair. Its value is mainly emollient: it coats the fiber and limits moisture loss, without replacing medical care for scalp conditions.",
            "choice": "Apply a small amount to the lengths, leave for 20 to 40 minutes, then wash carefully with a gentle shampoo.",
            "bullets": ["Warm the oil in your hands, not in a microwave.", "Focus on ends rather than oily roots.", "Patch test first if your scalp is sensitive."],
            "mistakes": ["Overloading fine hair.", "Sleeping with a damp towel overnight.", "Using rancid oil whose smell clings to hair."],
        },
        "it": {
            "lede": "Sui capelli, l'olio d'oliva e utile in piccole dosi come impacco nutriente prima dello shampoo.",
            "context": "Ammorbidisce le lunghezze secche e riduce la sensazione di capelli fragili. Il valore e soprattutto emolliente: riveste la fibra e limita la perdita d'acqua.",
            "choice": "Applicate poco prodotto sulle lunghezze, lasciate 20-40 minuti, poi lavate bene con shampoo delicato.",
            "bullets": ["Scaldate l'olio tra le mani.", "Insistete sulle punte, non sulle radici grasse.", "Fate una prova se il cuoio capelluto e sensibile."],
            "mistakes": ["Saturare i capelli fini.", "Dormire con asciugamano umido.", "Usare olio rancido dall'odore persistente."],
        },
        "el": {
            "lede": "Στα μαλλιά, το ελαιόλαδο είναι χρήσιμο σε μικρή ποσότητα ως θρεπτική μάσκα πριν το λούσιμο.",
            "context": "Μαλακώνει τα ξηρά μήκη και μειώνει την αίσθηση σπασίματος. Η αξία του είναι κυρίως μαλακτική: καλύπτει την τρίχα και περιορίζει την απώλεια υγρασίας.",
            "choice": "Απλώστε λίγη ποσότητα στα μήκη, αφήστε 20-40 λεπτά και λούστε καλά με απαλό σαμπουάν.",
            "bullets": ["Ζεστάνετε το λάδι στις παλάμες.", "Δώστε έμφαση στις άκρες, όχι στις λιπαρές ρίζες.", "Δοκιμάστε πρώτα σε μικρή περιοχή αν υπάρχει ευαισθησία."],
            "mistakes": ["Να βαραίνετε τα λεπτά μαλλιά.", "Να κοιμάστε με υγρή πετσέτα.", "Να χρησιμοποιείτε ταγγό λάδι με έντονη οσμή."],
        },
    }),
    (("peau", "skin", "visage", "soap", "savon", "sapone", "σαπο", "δέρμ"), {
        "fr": {
            "lede": "En soin de la peau ou en savonnerie, l'huile d'olive apporte douceur, confort et une tradition artisanale solide.",
            "context": "Riche en acides gras et en insaponifiables, elle convient aux formules nourrissantes et aux savons doux. Sur la peau, mieux vaut l'utiliser en petite quantite, sur peau legerement humide, pour eviter l'effet gras.",
            "choice": "Choisissez une huile fraiche, sans parfum ajoute, et adaptez l'usage a votre type de peau. Pour le savon, respectez toujours les dosages et les temps de cure.",
            "bullets": ["Appliquez apres la douche pour aider a retenir l'humidite.", "Evitez le contour des yeux si la peau reagit facilement.", "Pour un savon, pesez chaque ingredient avec precision."],
            "mistakes": ["Penser que naturel signifie automatiquement adapte a tous.", "Utiliser une huile oxydee sur le visage.", "Improviser une recette de savon sans regles de securite."],
        },
        "en": {
            "lede": "In skincare or soap making, olive oil brings softness, comfort and a strong craft tradition.",
            "context": "Rich in fatty acids and unsaponifiables, it suits nourishing formulas and gentle soaps. On skin, small amounts on slightly damp skin help avoid a greasy feel.",
            "choice": "Choose fresh oil with no added fragrance and adapt use to your skin type. For soap, always respect measurements and curing times.",
            "bullets": ["Apply after showering to help lock in moisture.", "Avoid the eye area if your skin reacts easily.", "For soap, weigh each ingredient precisely."],
            "mistakes": ["Assuming natural means suitable for everyone.", "Using oxidized oil on the face.", "Improvising soap without safety rules."],
        },
        "it": {
            "lede": "Nella cura della pelle o nella saponificazione, l'olio d'oliva porta morbidezza, comfort e tradizione artigianale.",
            "context": "Ricco di acidi grassi e insaponificabili, e adatto a formule nutrienti e saponi delicati. Sulla pelle, meglio usarlo in piccole dosi su pelle leggermente umida.",
            "choice": "Scegliete olio fresco, senza profumi aggiunti, e adattate l'uso al tipo di pelle. Per il sapone rispettate dosi e tempi di stagionatura.",
            "bullets": ["Applicate dopo la doccia per trattenere umidita.", "Evitate il contorno occhi se la pelle reagisce.", "Per il sapone pesate ogni ingrediente."],
            "mistakes": ["Pensare che naturale significhi adatto a tutti.", "Usare olio ossidato sul viso.", "Improvvisare sapone senza sicurezza."],
        },
        "el": {
            "lede": "Στην περιποίηση ή στη σαπωνοποιία, το ελαιόλαδο δίνει απαλότητα, άνεση και ισχυρή χειροποίητη παράδοση.",
            "context": "Πλούσιο σε λιπαρά οξέα, ταιριάζει σε θρεπτικές φόρμουλες και ήπια σαπούνια. Στο δέρμα, μικρή ποσότητα σε ελαφρά νωπή επιδερμίδα αποφεύγει τη λιπαρή αίσθηση.",
            "choice": "Διαλέξτε φρέσκο λάδι χωρίς άρωμα και προσαρμόστε τη χρήση στον τύπο δέρματος. Για σαπούνι, τηρείτε πάντα δοσολογίες και χρόνο ωρίμανσης.",
            "bullets": ["Απλώστε μετά το ντους για να κρατηθεί η υγρασία.", "Αποφύγετε την περιοχή των ματιών σε ευαίσθητο δέρμα.", "Στο σαπούνι ζυγίστε με ακρίβεια."],
            "mistakes": ["Να θεωρείτε ότι φυσικό σημαίνει κατάλληλο για όλους.", "Να χρησιμοποιείτε οξειδωμένο λάδι στο πρόσωπο.", "Να φτιάχνετε σαπούνι χωρίς κανόνες ασφαλείας."],
        },
    }),
]


GENERIC_BLOG = {
    "fr": {
        "lede": "L'huile d'olive est a la fois un produit agricole, un ingredient gastronomique et un marqueur culturel.",
        "context": "Pour bien l'apprecier, il faut regarder l'origine, la variete, le moment de recolte, la methode d'extraction et la maniere dont elle arrive jusqu'a la table. Ces details changent le gout, la texture, la stabilite et la perception de qualite.",
        "choice": "Commencez par une huile vierge extra recente, goutez-la seule, puis essayez-la sur un aliment simple comme du pain, une tomate ou des legumes tiedes.",
        "bullets": ["Une origine precise inspire plus confiance qu'une formule vague.", "La fraicheur compte autant que la reputation de la region.", "Le bon accord depend de l'intensite du plat."],
        "mistakes": ["Acheter sans lire l'etiquette.", "Utiliser la meme huile pour tous les usages.", "Oublier que l'huile d'olive est un produit frais."],
    },
    "en": {
        "lede": "Olive oil is an agricultural product, a culinary ingredient and a cultural marker at the same time.",
        "context": "To appreciate it properly, consider origin, variety, harvest timing, extraction method and how it reaches the table. These details change taste, texture, stability and perceived quality.",
        "choice": "Start with a recent extra virgin oil, taste it alone, then try it on a simple food such as bread, tomato or warm vegetables.",
        "bullets": ["A precise origin is more reassuring than a vague formula.", "Freshness matters as much as regional reputation.", "The right pairing depends on the intensity of the dish."],
        "mistakes": ["Buying without reading the label.", "Using the same oil for every purpose.", "Forgetting that olive oil is a fresh product."],
    },
    "it": {
        "lede": "L'olio d'oliva e insieme prodotto agricolo, ingrediente gastronomico e segno culturale.",
        "context": "Per apprezzarlo davvero bisogna osservare origine, varieta, momento di raccolta, metodo di estrazione e percorso fino alla tavola. Questi dettagli cambiano gusto, consistenza, stabilita e percezione di qualita.",
        "choice": "Iniziate con un extravergine recente, assaggiatelo da solo e poi su pane, pomodoro o verdure tiepide.",
        "bullets": ["Un'origine precisa convince piu di una formula vaga.", "La freschezza conta quanto la reputazione della zona.", "Il giusto abbinamento dipende dall'intensita del piatto."],
        "mistakes": ["Comprare senza leggere l'etichetta.", "Usare lo stesso olio per tutto.", "Dimenticare che l'olio e un prodotto fresco."],
    },
    "el": {
        "lede": "Το ελαιόλαδο είναι ταυτόχρονα αγροτικό προϊόν, γαστρονομικό υλικό και πολιτιστικό σημάδι.",
        "context": "Για να το εκτιμήσετε, κοιτάξτε προέλευση, ποικιλία, χρόνο συγκομιδής, μέθοδο έκθλιψης και τρόπο αποθήκευσης. Αυτές οι λεπτομέρειες αλλάζουν γεύση, υφή, σταθερότητα και ποιότητα.",
        "choice": "Ξεκινήστε με ένα πρόσφατο εξαιρετικό παρθένο, δοκιμάστε το σκέτο και μετά σε ψωμί, ντομάτα ή χλιαρά λαχανικά.",
        "bullets": ["Η σαφής προέλευση εμπνέει περισσότερη εμπιστοσύνη.", "Η φρεσκάδα μετρά όσο και η φήμη της περιοχής.", "Ο σωστός συνδυασμός εξαρτάται από την ένταση του πιάτου."],
        "mistakes": ["Αγορά χωρίς ανάγνωση ετικέτας.", "Το ίδιο λάδι για κάθε χρήση.", "Να ξεχνάτε ότι το ελαιόλαδο είναι φρέσκο προϊόν."],
    },
}


QUICK_TITLES = [
    ("Tartines de tomate confite et huile fruitee", "Confit tomato toasts with fruity oil", "Crostini al pomodoro confit e olio fruttato", "Φρυγανιές με ντομάτα κονφί και φρουτώδες λάδι"),
    ("Salade tiede de pois chiches au cumin", "Warm chickpea salad with cumin", "Insalata tiepida di ceci al cumino", "Χλιαρή σαλάτα ρεβιθιών με κύμινο"),
    ("Oeufs mollets, epinards et filet d'huile", "Soft eggs with spinach and olive oil", "Uova morbide con spinaci e olio", "Αυγά μελάτα με σπανάκι και ελαιόλαδο"),
    ("Carottes roties au miel et thym", "Honey thyme roasted carrots", "Carote arrosto con miele e timo", "Καρότα ψητά με μέλι και θυμάρι"),
    ("Pomme de terre ecrasee citron-persil", "Crushed potatoes with lemon and parsley", "Patate schiacciate limone e prezzemolo", "Πατάτες σπαστές με λεμόνι και μαϊντανό"),
    ("Salade de haricots blancs aux herbes", "White bean herb salad", "Insalata di fagioli bianchi alle erbe", "Σαλάτα λευκών φασολιών με μυρωδικά"),
    ("Pain grille ail, tomate et huile nouvelle", "Garlic toast with tomato and new oil", "Pane tostato aglio, pomodoro e olio nuovo", "Ψωμί ψητό με σκόρδο, ντομάτα και νέο λάδι"),
    ("Courgettes sautees a la menthe", "Sauteed zucchini with mint", "Zucchine saltate alla menta", "Κολοκυθάκια σοτέ με δυόσμο"),
    ("Riz aux herbes et huile d'olive", "Herbed rice with olive oil", "Riso alle erbe e olio d'oliva", "Ρύζι με μυρωδικά και ελαιόλαδο"),
    ("Salade orange fenouil et olives", "Orange fennel and olive salad", "Insalata arancia finocchio e olive", "Σαλάτα πορτοκάλι, μάραθο και ελιές"),
    ("Champignons poeles a l'ail doux", "Pan mushrooms with mellow garlic", "Funghi in padella all'aglio dolce", "Μανιτάρια στο τηγάνι με απαλό σκόρδο"),
    ("Semoule citronnee aux legumes croquants", "Lemony couscous with crisp vegetables", "Couscous al limone con verdure croccanti", "Κουσκούς λεμονάτο με τραγανά λαχανικά"),
    ("Yaourt sale concombre et huile verte", "Savory yogurt with cucumber and green oil", "Yogurt salato cetriolo e olio verde", "Αλμυρό γιαούρτι με αγγούρι και πράσινο λάδι"),
    ("Tomates cerises poelees au basilic", "Skillet cherry tomatoes with basil", "Pomodorini in padella al basilico", "Ντοματίνια στο τηγάνι με βασιλικό"),
    ("Pois gourmands citron et amandes", "Snap peas with lemon and almonds", "Taccole limone e mandorle", "Φασολάκια πλατιά με λεμόνι και αμύγδαλα"),
    ("Creme de feta fouettee a l'huile d'olive", "Whipped feta cream with olive oil", "Crema di feta montata all'olio", "Χτυπητή φέτα με ελαιόλαδο"),
    ("Pita croustillante zaatar et huile", "Crisp zaatar pita with olive oil", "Pita croccante zaatar e olio", "Τραγανή πίτα με ζαατάρ και λάδι"),
    ("Lentilles minute, echalote et vinaigre doux", "Quick lentils with shallot and mild vinegar", "Lenticchie rapide con scalogno e aceto dolce", "Γρήγορες φακές με εσαλότ και απαλό ξίδι"),
    ("Brocoli vapeur, citron et piment doux", "Steamed broccoli with lemon and mild chili", "Broccoli al vapore limone e peperoncino dolce", "Μπρόκολο ατμού με λεμόνι και ήπιο πιπέρι"),
    ("Avocat ecrase, citron vert et huile piquante", "Mashed avocado with lime and peppery oil", "Avocado schiacciato lime e olio piccante", "Λιωμένο αβοκάντο με λάιμ και πικάντικο λάδι"),
    ("Burrata, poivre, huile intense et pain chaud", "Burrata with peppery oil and warm bread", "Burrata, pepe, olio intenso e pane caldo", "Μπουράτα με έντονο λάδι και ζεστό ψωμί"),
    ("Poivrons express a la poele", "Quick skillet peppers", "Peperoni rapidi in padella", "Γρήγορες πιπεριές στο τηγάνι"),
    ("Sardines en boite relevees au citron", "Tinned sardines brightened with lemon", "Sardine in scatola al limone", "Σαρδέλες κονσέρβας με λεμόνι"),
    ("Salade de concombre, aneth et huile douce", "Cucumber dill salad with mild oil", "Insalata cetriolo aneto e olio delicato", "Σαλάτα αγγούρι με άνηθο και ήπιο λάδι"),
    ("Omelette fine aux herbes mediterraneennes", "Thin omelet with Mediterranean herbs", "Omelette sottile alle erbe mediterranee", "Λεπτή ομελέτα με μεσογειακά μυρωδικά"),
    ("Pates minute ail, huile et chapelure", "Quick pasta with garlic, oil and breadcrumbs", "Pasta rapida aglio, olio e pangrattato", "Γρήγορα ζυμαρικά με σκόρδο, λάδι και ψίχουλα"),
    ("Salade de betterave, noix et huile douce", "Beet walnut salad with mild olive oil", "Insalata barbabietola noci e olio dolce", "Σαλάτα παντζάρι με καρύδια και ήπιο λάδι"),
    ("Celeri branche croquant, citron et parmesan", "Crunchy celery with lemon and parmesan", "Sedano croccante limone e parmigiano", "Τραγανό σέλερι με λεμόνι και παρμεζάνα"),
    ("Pois chiches croustillants au paprika", "Crispy paprika chickpeas", "Ceci croccanti alla paprika", "Τραγανά ρεβίθια με πάπρικα"),
    ("Tartine ricotta, miel et huile d'olive", "Ricotta toast with honey and olive oil", "Crostino ricotta, miele e olio", "Φρυγανιά με ρικότα, μέλι και λάδι"),
    ("Salade de melon, feta et basilic", "Melon feta and basil salad", "Insalata melone, feta e basilico", "Σαλάτα πεπόνι, φέτα και βασιλικό"),
    ("Haricots verts tiedes aux noisettes", "Warm green beans with hazelnuts", "Fagiolini tiepidi con nocciole", "Χλιαρά πράσινα φασολάκια με φουντούκια"),
    ("Aubergine grillee, yaourt et huile fumee", "Grilled eggplant with yogurt and smoky oil", "Melanzana grigliata, yogurt e olio affumicato", "Ψητή μελιτζάνα με γιαούρτι και καπνιστό λάδι"),
    ("Radis beurre d'olive et fleur de sel", "Radishes with olive butter and sea salt", "Ravanelli con burro d'olio e sale", "Ραπανάκια με βούτυρο ελιάς και ανθό αλατιού"),
    ("Salade de quinoa aux herbes fraiches", "Quinoa salad with fresh herbs", "Insalata di quinoa alle erbe fresche", "Σαλάτα κινόα με φρέσκα μυρωδικά"),
    ("Tartine anchois, tomate et huile verte", "Anchovy tomato toast with green oil", "Crostino acciughe, pomodoro e olio verde", "Φρυγανιά με αντζούγια, ντομάτα και πράσινο λάδι"),
    ("Patates douces roties au romarin", "Rosemary roasted sweet potatoes", "Patate dolci arrosto al rosmarino", "Γλυκοπατάτες ψητές με δεντρολίβανο"),
    ("Salade de pomme, roquette et pecorino", "Apple arugula and pecorino salad", "Insalata mela, rucola e pecorino", "Σαλάτα μήλο, ρόκα και πεκορίνο"),
    ("Crevettes minute ail et citron", "Quick shrimp with garlic and lemon", "Gamberi rapidi aglio e limone", "Γρήγορες γαρίδες με σκόρδο και λεμόνι"),
    ("Soupe froide concombre menthe", "Cold cucumber mint soup", "Zuppa fredda cetriolo e menta", "Κρύα σούπα αγγούρι και δυόσμο"),
    ("Fromage frais, olives et huile epicee", "Fresh cheese with olives and spiced oil", "Formaggio fresco, olive e olio speziato", "Φρέσκο τυρί με ελιές και πικάντικο λάδι"),
    ("Carpaccio de tomate ancienne", "Heirloom tomato carpaccio", "Carpaccio di pomodoro antico", "Καρπάτσιο παλιάς ντομάτας"),
    ("Ecrase de pois verts a la menthe", "Crushed green peas with mint", "Purea rustica di piselli alla menta", "Σπασμένος αρακάς με δυόσμο"),
    ("Chou-fleur roti aux epices douces", "Roasted cauliflower with warm spices", "Cavolfiore arrosto alle spezie dolci", "Κουνουπίδι ψητό με γλυκά μπαχαρικά"),
    ("Salade de thon, haricots et oignon rouge", "Tuna bean and red onion salad", "Insalata tonno, fagioli e cipolla rossa", "Σαλάτα τόνου με φασόλια και κόκκινο κρεμμύδι"),
    ("Pain perdu sale tomate et parmesan", "Savory tomato parmesan French toast", "French toast salato pomodoro e parmigiano", "Αλμυρό αυγοφέτα με ντομάτα και παρμεζάνα"),
    ("Fraises poivrees et huile d'olive", "Peppered strawberries with olive oil", "Fragole al pepe e olio d'oliva", "Φράουλες με πιπέρι και ελαιόλαδο"),
    ("Salade tiede de boulgour aux legumes", "Warm bulgur salad with vegetables", "Insalata tiepida di bulgur alle verdure", "Χλιαρή σαλάτα πλιγούρι με λαχανικά"),
    ("Mini bruschette champignons et thym", "Mini mushroom thyme bruschette", "Mini bruschette funghi e timo", "Μίνι μπρουσκέτες με μανιτάρια και θυμάρι"),
    ("Poires, fromage bleu et huile delicate", "Pears blue cheese and delicate oil", "Pere, erborinato e olio delicato", "Αχλάδια με μπλε τυρί και λεπτό λάδι"),
]


INGREDIENT_MAP = [
    (("tomate", "tomato", "pomodoro", "ντομ"), {"fr": "tomates bien mures", "en": "ripe tomatoes", "it": "pomodori maturi", "el": "ώριμες ντομάτες"}),
    (("courgette", "zucchini", "zucchine", "κολο"), {"fr": "courgettes fermes", "en": "firm zucchini", "it": "zucchine sode", "el": "σφιχτά κολοκυθάκια"}),
    (("aubergine", "eggplant", "melanz", "μελι"), {"fr": "aubergines", "en": "eggplants", "it": "melanzane", "el": "μελιτζάνες"}),
    (("poivron", "pepper", "peper", "πιπε"), {"fr": "poivrons rouges", "en": "red peppers", "it": "peperoni rossi", "el": "κόκκινες πιπεριές"}),
    (("citron", "lemon", "limone", "λεμό"), {"fr": "citron jaune ou vert", "en": "lemon or lime", "it": "limone", "el": "λεμόνι"}),
    (("chocolat", "brownie", "cookie", "mousse", "σοκολ"), {"fr": "chocolat noir", "en": "dark chocolate", "it": "cioccolato fondente", "el": "μαύρη σοκολάτα"}),
    (("feta", "labneh", "yaourt", "tzatziki", "φέτα"), {"fr": "feta ou yaourt epais", "en": "feta or thick yogurt", "it": "feta o yogurt denso", "el": "φέτα ή στραγγιστό γιαούρτι"}),
    (("sardine", "saumon", "daurade", "loup", "moule", "poulpe", "crevette", "gamba", "fish", "shrimp", "octopus", "γαρ", "ψαρ", "χτα"), {"fr": "poisson ou fruits de mer tres frais", "en": "very fresh fish or seafood", "it": "pesce o frutti di mare freschissimi", "el": "πολύ φρέσκο ψάρι ή θαλασσινά"}),
    (("poulet", "chicken", "pollo", "κοτό"), {"fr": "poulet fermier", "en": "free-range chicken", "it": "pollo ruspante", "el": "κοτόπουλο"}),
    (("pois chiche", "hummus", "falafel", "socca", "chickpea", "ceci", "ρεβ"), {"fr": "pois chiches", "en": "chickpeas", "it": "ceci", "el": "ρεβίθια"}),
    (("pates", "pasta", "risotto", "riz", "paella", "rice", "ρύζ"), {"fr": "riz ou pates de qualite", "en": "quality rice or pasta", "it": "riso o pasta di qualita", "el": "ρύζι ή ζυμαρικά καλής ποιότητας"}),
    (("focaccia", "pizza", "bruschetta", "pain", "bread", "pane", "πίτ"), {"fr": "pain ou pate levee", "en": "bread or risen dough", "it": "pane o impasto lievitato", "el": "ψωμί ή ζύμη"}),
    (("menthe", "basilic", "romarin", "persil", "herb", "basil", "mint", "prezzemolo", "βασιλ", "δυόσ"), {"fr": "herbes fraiches", "en": "fresh herbs", "it": "erbe fresche", "el": "φρέσκα μυρωδικά"}),
]


def read(path):
    return path.read_text(encoding="utf-8")


def write(path, content):
    path.write_text(content, encoding="utf-8", newline="\n")


def parse_lang(text, filename):
    m = re.search(r'<html\s+lang="([^"]+)"', text)
    if m:
        return m.group(1)
    m = re.search(r'-(fr|en|it|el)\.html$', filename)
    return m.group(1) if m else "fr"


def parse_h1(text):
    m = re.search(r"<h1>(.*?)</h1>", text, re.S)
    if m:
        return html.unescape(re.sub(r"<.*?>", "", m.group(1)).strip())
    m = re.search(r"<title>(.*?)</title>", text, re.S)
    if m:
        return html.unescape(re.sub(r"\s+—.*$", "", m.group(1)).strip())
    return "L'Or Vert"


def parse_alternates(text):
    out = []
    for lang, href in re.findall(r'<link\s+rel="alternate"\s+hreflang="([^"]+)"\s+href="([^"]+)"\s*/?>', text):
        out.append((lang, Path(href).name))
    return out


def hreflang_html(section, alternates):
    if not alternates:
        return ""
    return "\n".join(
        f'    <link rel="alternate" hreflang="{lang}" href="{SITE}/{section}/{fname}" />'
        for lang, fname in alternates
    )


def lang_switch(alternates, current):
    if not alternates:
        return ""
    links = []
    for lang, fname in alternates:
        active = "active" if lang == current else ""
        links.append(f'<a href="{fname}" class="{active}">{lang.upper()}</a>')
    return f'<div class="lang-switch">{" ".join(links)}</div>'


def esc(value):
    return html.escape(value, quote=True)


def slug_text(path, title):
    return f"{path.stem} {title}".lower()


def blog_theme(slug, lang):
    for keys, data in BLOG_THEMES:
        if any(k in slug for k in keys):
            return data[lang]
    return GENERIC_BLOG[lang]


def blog_article_body(title, slug, lang):
    labels = LANGS[lang]
    theme = blog_theme(slug, lang)
    bullet_items = "\n".join(f"            <li>{esc(item)}</li>" for item in theme["bullets"])
    mistake_items = "\n".join(f"            <li>{esc(item)}</li>" for item in theme["mistakes"])
    return f"""
        <p class="intro">{esc(theme["lede"])}</p>

        <h2>{esc(labels["takeaway"])}</h2>
        <p>{esc(theme["context"])}</p>
        <ul>
{bullet_items}
        </ul>

        <h2>{esc(labels["understand"])}</h2>
        <p>{esc(labels["article_intro"])} {esc(labels["article_depth"].format(title=title))}</p>

        <h2>{esc(labels["choose"])}</h2>
        <p>{esc(theme["choice"])}</p>
        <div class="callout"><strong>{esc(labels["expert"])} :</strong> {esc(theme["bullets"][0])}</div>

        <h2>{esc(labels["mistakes"])}</h2>
        <ul>
{mistake_items}
        </ul>

        <h2>{esc(labels["further"])}</h2>
        <p>{esc(labels["article_further"])}</p>

        <blockquote>"{esc(labels["article_quote"])}"</blockquote>
"""


def render_blog(path):
    old = read(path)
    lang = parse_lang(old, path.name)
    labels = LANGS[lang]
    title = parse_h1(old)
    alternates = parse_alternates(old)
    slug = slug_text(path, title)
    theme = blog_theme(slug, lang)
    desc = labels["blog_desc"].format(title=title)
    schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc,
        "author": {"@type": "Organization", "name": "L'Or Vert"},
        "dateModified": "2026-05-04",
        "mainEntityOfPage": f"{SITE}/blog/{path.name}",
    }
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{esc(title)} — Blog L'Or Vert</title>
    <meta name="description" content="{esc(desc)}">
    <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%232E4A40'/%3E%3Cpath fill='%23F2D8C4' d='M16 5.5S9.5 14 9.5 19a6.5 6.5 0 0013 0c0-5-6.5-13.5-6.5-13.5z'/%3E%3C/svg%3E" type="image/svg+xml">
    <link rel="stylesheet" href="../assets/seo.css">
{hreflang_html("blog", alternates)}
    <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False, indent=2)}</script>
</head>
<body>
<nav class="site-nav"><div class="container"><a href="../{labels["index"]}" class="logo">L'OR VERT / BLOG</a>{lang_switch(alternates, lang)}</div></nav>
<header class="page-hero" style="background: linear-gradient(135deg, var(--pine) 0%, var(--avocado-dark) 100%);">
    <div class="container">
        <div class="breadcrumb"><a href="../{labels["index"]}">{esc(labels["home"])}</a> &raquo; {esc(labels["blog"])}</div>
        <h1>{esc(title)}</h1>
        <p class="lede">{esc(theme["lede"])}</p>
        <div class="meta">{esc(labels["posted"])} : {esc(labels["date"])} &middot; 7 {esc(labels["read"])}</div>
    </div>
</header>
<main class="container">
    <article class="guide">{blog_article_body(title, slug, lang)}
    </article>
</main>
<footer class="site-footer"><div class="container"><h3>L'Or Vert</h3><p>{esc(labels["footer"])}</p><div class="copyright">&copy; 2026 — L'Or Vert</div></div></footer>
</body>
</html>
"""


def recipe_kind(slug):
    if any(k in slug for k in ["cookie", "brownie", "chocolat", "gateau", "glace", "madeleine", "mousse", "granola", "ananas", "fraise", "poire"]):
        return "sweet"
    if any(k in slug for k in ["aioli", "anchoiade", "hummus", "pesto", "tapenade", "vinaigrette", "mayonnaise", "tzatziki", "labneh", "huile-piment", "baba"]):
        return "sauce"
    if any(k in slug for k in ["sardine", "saumon", "daurade", "loup", "moule", "poulpe", "crevette", "gamba", "thon"]):
        return "seafood"
    if any(k in slug for k in ["focaccia", "pizza", "bruschetta", "pain", "socca", "pita", "tartine"]):
        return "bread"
    if any(k in slug for k in ["pates", "pasta", "risotto", "paella", "riz", "semoule", "quinoa", "boulgour"]):
        return "grain"
    return "vegetable"


def recipe_times(kind):
    return {
        "sweet": ("20 min", "25 min", "15 min", "6"),
        "sauce": ("15 min", "0 min", "20 min", "4"),
        "seafood": ("20 min", "12 min", "5 min", "4"),
        "bread": ("25 min", "18 min", "45 min", "4"),
        "grain": ("15 min", "22 min", "5 min", "4"),
        "vegetable": ("18 min", "20 min", "10 min", "4"),
    }[kind]


def base_ingredients(slug, lang, kind):
    common_by_kind = {
        "sweet": {
            "fr": ["huile d'olive extra vierge douce", "farine de ble ou poudre d'amande", "sucre blond", "oeufs", "fleur de sel"],
            "en": ["mild extra virgin olive oil", "wheat flour or almond flour", "light brown sugar", "eggs", "sea salt"],
            "it": ["olio extravergine delicato", "farina di grano o di mandorle", "zucchero chiaro", "uova", "sale marino"],
            "el": ["ήπιο εξαιρετικό παρθένο ελαιόλαδο", "αλεύρι ή αμυγδαλόσκονη", "καστανή ζάχαρη", "αυγά", "ανθός αλατιού"],
        },
        "sauce": {
            "fr": ["huile d'olive extra vierge L'Or Vert", "ail doux", "jus de citron", "fleur de sel", "herbes fraiches"],
            "en": ["L'Or Vert extra virgin olive oil", "mellow garlic", "lemon juice", "sea salt", "fresh herbs"],
            "it": ["olio extravergine d'oliva L'Or Vert", "aglio dolce", "succo di limone", "sale marino", "erbe fresche"],
            "el": ["εξαιρετικό παρθένο ελαιόλαδο L'Or Vert", "απαλό σκόρδο", "χυμός λεμονιού", "ανθός αλατιού", "φρέσκα μυρωδικά"],
        },
        "seafood": {
            "fr": ["huile d'olive extra vierge fruitee", "poisson ou fruits de mer tres frais", "citron", "persil plat", "fleur de sel"],
            "en": ["fruity extra virgin olive oil", "very fresh fish or seafood", "lemon", "flat-leaf parsley", "sea salt"],
            "it": ["olio extravergine fruttato", "pesce o frutti di mare freschissimi", "limone", "prezzemolo", "sale marino"],
            "el": ["φρουτώδες εξαιρετικό παρθένο ελαιόλαδο", "πολύ φρέσκο ψάρι ή θαλασσινά", "λεμόνι", "μαϊντανός", "ανθός αλατιού"],
        },
        "bread": {
            "fr": ["huile d'olive extra vierge", "pain ou pate levee", "fleur de sel", "herbes fraiches", "garniture de saison"],
            "en": ["extra virgin olive oil", "bread or risen dough", "sea salt", "fresh herbs", "seasonal topping"],
            "it": ["olio extravergine d'oliva", "pane o impasto lievitato", "sale marino", "erbe fresche", "guarnizione di stagione"],
            "el": ["εξαιρετικό παρθένο ελαιόλαδο", "ψωμί ή ζύμη", "ανθός αλατιού", "φρέσκα μυρωδικά", "εποχική γαρνιτούρα"],
        },
        "grain": {
            "fr": ["huile d'olive extra vierge", "riz, pates ou cereales", "bouillon leger", "herbes fraiches", "parmesan ou citron"],
            "en": ["extra virgin olive oil", "rice, pasta or grains", "light stock", "fresh herbs", "parmesan or lemon"],
            "it": ["olio extravergine d'oliva", "riso, pasta o cereali", "brodo leggero", "erbe fresche", "parmigiano o limone"],
            "el": ["εξαιρετικό παρθένο ελαιόλαδο", "ρύζι, ζυμαρικά ή δημητριακά", "ελαφρύς ζωμός", "φρέσκα μυρωδικά", "παρμεζάνα ή λεμόνι"],
        },
        "vegetable": {
            "fr": ["huile d'olive extra vierge L'Or Vert", "legumes de saison", "fleur de sel", "poivre noir fraichement moulu", "herbes fraiches"],
            "en": ["L'Or Vert extra virgin olive oil", "seasonal vegetables", "sea salt", "freshly ground black pepper", "fresh herbs"],
            "it": ["olio extravergine d'oliva L'Or Vert", "verdure di stagione", "sale marino", "pepe nero macinato fresco", "erbe fresche"],
            "el": ["εξαιρετικό παρθένο ελαιόλαδο L'Or Vert", "εποχικά λαχανικά", "ανθός αλατιού", "φρεσκοτριμμένο μαύρο πιπέρι", "φρέσκα μυρωδικά"],
        },
    }
    common = common_by_kind[kind][lang]
    found = []
    for keys, item in INGREDIENT_MAP:
        if any(k in slug for k in keys):
            found.append(item[lang])
    if not found:
        found = {
            "fr": ["legumes de saison", "herbes fraiches", "citron"],
            "en": ["seasonal vegetables", "fresh herbs", "lemon"],
            "it": ["verdure di stagione", "erbe fresche", "limone"],
            "el": ["εποχικά λαχανικά", "φρέσκα μυρωδικά", "λεμόνι"],
        }[lang]
    extras = {
        "sweet": {
            "fr": ["zeste d'agrume ou vanille", "noix, amandes ou chocolat selon la recette"],
            "en": ["citrus zest or vanilla", "nuts, almonds or chocolate depending on the recipe"],
            "it": ["scorza di agrume o vaniglia", "noci, mandorle o cioccolato secondo la ricetta"],
            "el": ["ξύσμα εσπεριδοειδών ή βανίλια", "ξηροί καρποί, αμύγδαλα ή σοκολάτα ανάλογα με τη συνταγή"],
        },
        "default": {
            "fr": ["une touche acide : vinaigre doux ou jus de citron", "un element croquant : graines, noix ou pain grille"],
            "en": ["an acidic touch: mild vinegar or lemon juice", "a crunchy element: seeds, nuts or toasted bread"],
            "it": ["una nota acida: aceto dolce o succo di limone", "un elemento croccante: semi, noci o pane tostato"],
            "el": ["μια όξινη πινελιά: ήπιο ξίδι ή λεμόνι", "ένα τραγανό στοιχείο: σπόροι, ξηροί καρποί ή ψημένο ψωμί"],
        },
    }["sweet" if kind == "sweet" else "default"][lang]
    return common + found[:4] + extras


def recipe_steps(title, kind, lang):
    data = {
        "sweet": {
            "fr": [
                "Pesez les ingredients secs, puis melangez farine, sucre et sel dans un saladier pour repartir uniformement la levure ou les poudres.",
                "Fouettez les oeufs avec l'huile d'olive jusqu'a obtenir une texture brillante et souple, sans chercher a incorporer trop d'air.",
                "Incorporez les ingredients secs en deux fois, puis ajoutez chocolat, agrumes ou fruits secs selon la recette.",
                "Laissez reposer la pate quelques minutes : l'huile hydrate la farine et donne une mie plus moelleuse.",
                "Enfournez a chaleur moderee jusqu'a ce que le centre reste tendre et les bords legerement dores.",
                "Laissez tiedir avant de servir afin que les aromes d'huile d'olive, de sucre et de chocolat s'equilibrent.",
            ],
            "en": [
                "Weigh the dry ingredients, then combine flour, sugar and salt so leavening and powders are evenly distributed.",
                "Whisk eggs with olive oil until glossy and supple, without trying to incorporate too much air.",
                "Fold in the dry ingredients in two additions, then add chocolate, citrus or nuts depending on the recipe.",
                "Rest the dough briefly: olive oil hydrates the flour and helps create a more tender crumb.",
                "Bake at moderate heat until the center stays tender and the edges are lightly golden.",
                "Cool before serving so olive oil, sugar and chocolate aromas settle into balance.",
            ],
            "it": [
                "Pesate gli ingredienti secchi, poi mescolate farina, zucchero e sale per distribuire bene le polveri.",
                "Sbattete le uova con l'olio fino a ottenere una texture lucida e morbida, senza incorporare troppa aria.",
                "Unite gli ingredienti secchi in due volte, poi aggiungete cioccolato, agrumi o frutta secca.",
                "Lasciate riposare l'impasto: l'olio idrata la farina e rende la mollica piu morbida.",
                "Cuocete a calore moderato finche il centro resta tenero e i bordi sono appena dorati.",
                "Fate intiepidire prima di servire, cosi olio, zucchero e cioccolato trovano equilibrio.",
            ],
            "el": [
                "Ζυγίστε τα στερεά υλικά και ανακατέψτε αλεύρι, ζάχαρη και αλάτι ώστε να μοιραστούν ομοιόμορφα.",
                "Χτυπήστε αυγά με ελαιόλαδο μέχρι να γυαλίσουν, χωρίς υπερβολικό αέρα.",
                "Ενσωματώστε τα στερεά σε δύο δόσεις και προσθέστε σοκολάτα, εσπεριδοειδή ή ξηρούς καρπούς.",
                "Αφήστε τη ζύμη να σταθεί λίγο: το λάδι ενυδατώνει το αλεύρι και δίνει πιο τρυφερή υφή.",
                "Ψήστε σε μέτρια θερμοκρασία μέχρι το κέντρο να μείνει μαλακό και οι άκρες να ροδίσουν.",
                "Αφήστε να χλιαρύνει ώστε αρώματα λαδιού, ζάχαρης και σοκολάτας να ισορροπήσουν.",
            ],
        },
        "sauce": {
            "fr": [
                "Preparez les ingredients aromatiques tres finement pour obtenir une sauce lisse et expressive.",
                "Versez l'huile d'olive en filet tout en melangeant afin de creer une emulsion stable et brillante.",
                "Ajoutez l'acidite progressivement, puis goutez avant de saler : chaque huile reagit differemment.",
                "Laissez reposer au frais pour que l'ail, les herbes ou les epices diffusent sans agressivite.",
                "Detendez avec une cuilleree d'eau froide si la texture devient trop epaisse.",
                "Servez avec legumes, pain grille, poisson ou viande blanche selon l'intensite de la sauce.",
            ],
            "en": [
                "Prepare aromatic ingredients very finely to obtain a smooth, expressive sauce.",
                "Pour olive oil in a thin stream while mixing to create a stable, glossy emulsion.",
                "Add acidity gradually, then taste before salting because each oil reacts differently.",
                "Rest chilled so garlic, herbs or spices infuse without becoming aggressive.",
                "Loosen with a spoonful of cold water if the texture becomes too thick.",
                "Serve with vegetables, toasted bread, fish or white meat depending on intensity.",
            ],
            "it": [
                "Preparate gli aromi molto finemente per ottenere una salsa liscia ed espressiva.",
                "Versate l'olio a filo mescolando per creare un'emulsione stabile e brillante.",
                "Aggiungete acidita poco alla volta e assaggiate prima di salare.",
                "Lasciate riposare in fresco per far diffondere aglio, erbe o spezie.",
                "Allungate con un cucchiaio d'acqua fredda se la consistenza e troppo densa.",
                "Servite con verdure, pane tostato, pesce o carne bianca secondo l'intensita.",
            ],
            "el": [
                "Ψιλοκόψτε τα αρωματικά υλικά για λεία και καθαρή σάλτσα.",
                "Ρίξτε το ελαιόλαδο σε λεπτή ροή ανακατεύοντας για σταθερή γυαλιστερή γαλακτωματοποίηση.",
                "Προσθέστε οξύτητα σταδιακά και δοκιμάστε πριν αλατίσετε.",
                "Αφήστε στο ψυγείο ώστε σκόρδο, μυρωδικά ή μπαχαρικά να δώσουν άρωμα χωρίς ένταση.",
                "Αραιώστε με κουταλιά κρύο νερό αν γίνει πολύ πηχτή.",
                "Σερβίρετε με λαχανικά, ψημένο ψωμί, ψάρι ή λευκό κρέας.",
            ],
        },
        "seafood": {
            "fr": [
                "Epongez soigneusement le poisson ou les fruits de mer : une surface seche saisit mieux et garde une saveur nette.",
                "Assaisonnez avec sel, citron et un premier filet d'huile d'olive, puis laissez mariner quelques minutes seulement.",
                "Cuisez rapidement a feu moyen-vif ou assemblez a cru si la recette le demande, sans prolonger inutilement.",
                "Ajoutez les herbes en fin de cuisson pour conserver leur fraicheur.",
                "Terminez avec une huile d'olive plus expressive et un trait de citron.",
                "Servez aussitot, car les produits de la mer perdent vite leur texture ideale.",
            ],
            "en": [
                "Pat fish or seafood dry: a dry surface sears better and keeps flavor clean.",
                "Season with salt, lemon and a first drizzle of olive oil, then marinate only briefly.",
                "Cook quickly over medium-high heat or assemble raw if the recipe calls for it.",
                "Add herbs at the end so their freshness remains clear.",
                "Finish with a more expressive olive oil and a squeeze of lemon.",
                "Serve immediately, as seafood loses its ideal texture quickly.",
            ],
            "it": [
                "Asciugate bene pesce o frutti di mare: una superficie asciutta rosola meglio.",
                "Condite con sale, limone e un primo filo d'olio, poi marinate per pochi minuti.",
                "Cuocete rapidamente a fuoco medio-alto o assemblate a crudo se previsto.",
                "Aggiungete le erbe alla fine per mantenerle fresche.",
                "Finite con un olio piu espressivo e poco limone.",
                "Servite subito, per non perdere la texture ideale.",
            ],
            "el": [
                "Στεγνώστε καλά ψάρι ή θαλασσινά ώστε να ψηθούν καθαρά και να κρατήσουν γεύση.",
                "Καρυκεύστε με αλάτι, λεμόνι και λίγο ελαιόλαδο, και μαρινάρετε μόνο για λίγο.",
                "Μαγειρέψτε γρήγορα σε μέτρια προς δυνατή φωτιά ή συναρμολογήστε ωμό αν χρειάζεται.",
                "Προσθέστε τα μυρωδικά στο τέλος για φρεσκάδα.",
                "Τελειώστε με πιο έντονο λάδι και λίγο λεμόνι.",
                "Σερβίρετε αμέσως, γιατί τα θαλασσινά χάνουν γρήγορα την ιδανική υφή.",
            ],
        },
    }
    if kind in data:
        return data[kind][lang]
    default = {
        "fr": [
            "Rassemblez tous les ingredients, sechez-les soigneusement et sortez l'huile d'olive quelques minutes avant de cuisiner pour mieux percevoir ses aromes.",
            "Preparez la base de la recette en taillant les ingredients de facon reguliere afin d'obtenir une cuisson ou un assaisonnement homogene.",
            "Ajoutez une premiere partie de l'huile d'olive, melangez doucement, puis laissez les saveurs commencer a se lier avant de poursuivre.",
            "Cuisez ou assemblez la preparation sans brutaliser les ingredients : une chaleur moderee et un geste souple gardent la texture nette.",
            "Rectifiez l'assaisonnement avec sel, poivre et acidite. Ajoutez le reste de l'huile en filet pour donner du brillant et de la longueur en bouche.",
            "Laissez reposer quelques minutes, puis servez dans un plat large afin que les parfums restent lisibles et que chaque portion soit bien equilibree.",
        ],
        "en": [
            "Gather the ingredients, dry them carefully and bring the olive oil out a few minutes before cooking so its aromas open up.",
            "Prepare the base by cutting ingredients evenly, which gives a more consistent texture and seasoning.",
            "Add part of the olive oil, fold gently and let the flavors begin to bind before moving on.",
            "Cook or assemble without harsh handling: moderate heat and a light touch keep the texture clean.",
            "Adjust seasoning with salt, pepper and acidity. Finish with the remaining oil for shine and a longer flavor.",
            "Rest briefly, then serve on a wide plate so the aromas stay clear and every portion is balanced.",
        ],
        "it": [
            "Raccogliete gli ingredienti, asciugateli bene e tirate fuori l'olio qualche minuto prima per far aprire gli aromi.",
            "Preparate la base tagliando gli ingredienti in modo regolare, cosi consistenza e condimento saranno uniformi.",
            "Aggiungete una parte dell'olio, mescolate con delicatezza e lasciate che i sapori inizino a legarsi.",
            "Cuocete o assemblate senza stressare gli ingredienti: calore moderato e mano leggera mantengono la texture pulita.",
            "Regolate sale, pepe e acidita. Finite con il resto dell'olio a filo per dare lucentezza e profondita.",
            "Lasciate riposare pochi minuti e servite in un piatto ampio per mantenere chiari i profumi.",
        ],
        "el": [
            "Συγκεντρώστε τα υλικά, στεγνώστε τα καλά και αφήστε το ελαιόλαδο λίγα λεπτά εκτός ντουλαπιού για να ανοίξουν τα αρώματά του.",
            "Ετοιμάστε τη βάση κόβοντας τα υλικά ομοιόμορφα, ώστε η υφή και το καρύκευμα να είναι ισορροπημένα.",
            "Προσθέστε μέρος από το ελαιόλαδο, ανακατέψτε απαλά και αφήστε τις γεύσεις να δεθούν.",
            "Μαγειρέψτε ή συναρμολογήστε χωρίς έντονες κινήσεις: μέτρια θερμότητα και απαλό χέρι κρατούν καθαρή την υφή.",
            "Ρυθμίστε αλάτι, πιπέρι και οξύτητα. Τελειώστε με το υπόλοιπο λάδι σε λεπτή ροή για λάμψη και διάρκεια.",
            "Αφήστε λίγα λεπτά να σταθεί και σερβίρετε σε φαρδύ πιάτο για καθαρά αρώματα και ισορροπία.",
        ],
    }
    return default[lang]


def recipe_paragraphs(kind, lang):
    role = {
        "fr": "L'huile d'olive n'est pas seulement une matiere grasse : elle porte les aromes, assouplit la texture et donne une finale nette. Pour cette recette, choisissez une huile fruitee mais equilibree, capable de soutenir les ingredients sans masquer leur identite.",
        "en": "Olive oil is not just a fat: it carries aromas, softens texture and gives a clean finish. For this recipe, choose a fruity but balanced oil that supports the ingredients without masking them.",
        "it": "L'olio d'oliva non e solo un grasso: trasporta aromi, ammorbidisce la texture e dona un finale pulito. Scegliete un olio fruttato ma equilibrato.",
        "el": "Το ελαιόλαδο δεν είναι απλώς λιπαρή ύλη: μεταφέρει αρώματα, μαλακώνει την υφή και δίνει καθαρό τελείωμα. Διαλέξτε φρουτώδες αλλά ισορροπημένο λάδι.",
    }[lang]
    tips = {
        "fr": ["Goutez avant de servir : l'huile adoucit, l'acidite reveille.", "Ajoutez le dernier filet d'huile hors du feu.", "Servez dans une assiette tiede pour garder les parfums ouverts."],
        "en": ["Taste before serving: oil softens while acidity brightens.", "Add the final drizzle off the heat.", "Serve on a warm plate to keep aromas open."],
        "it": ["Assaggiate prima di servire: l'olio ammorbidisce, l'acidita risveglia.", "Aggiungete l'ultimo filo d'olio fuori dal fuoco.", "Servite in un piatto tiepido per aprire i profumi."],
        "el": ["Δοκιμάστε πριν το σερβίρισμα: το λάδι μαλακώνει, η οξύτητα ξυπνά.", "Προσθέστε το τελευταίο λάδι εκτός φωτιάς.", "Σερβίρετε σε χλιαρό πιάτο για ανοιχτά αρώματα."],
    }[lang]
    variations = {
        "fr": "Pour varier, changez simplement le profil de l'huile : douce et ronde pour un resultat familial, verte et poivree pour une assiette plus gastronomique. Quelques herbes fraiches ou un zeste d'agrume suffisent souvent.",
        "en": "For variation, simply change the oil profile: mild and round for a family-style result, green and peppery for a more gastronomic plate. Fresh herbs or citrus zest are often enough.",
        "it": "Per variare cambiate il profilo dell'olio: dolce e rotondo per un risultato familiare, verde e piccante per un piatto piu gastronomico. Erbe fresche o scorza di agrume bastano spesso.",
        "el": "Για παραλλαγή αλλάξτε το προφίλ του λαδιού: ήπιο και στρογγυλό για οικογενειακό αποτέλεσμα, πράσινο και πιπεράτο για πιο γαστρονομικό πιάτο.",
    }[lang]
    storage = {
        "fr": "Conservez au frais si la recette contient des produits sensibles, puis ramenez a temperature ambiante 10 minutes avant de servir. Les preparations croustillantes sont meilleures le jour meme.",
        "en": "Refrigerate if the recipe contains delicate ingredients, then bring back toward room temperature 10 minutes before serving. Crisp preparations are best the same day.",
        "it": "Conservate in frigo se contiene ingredienti delicati, poi riportate a temperatura ambiente 10 minuti prima del servizio. Le preparazioni croccanti sono migliori in giornata.",
        "el": "Φυλάξτε στο ψυγείο αν περιέχει ευαίσθητα υλικά και αφήστε 10 λεπτά πριν το σερβίρισμα. Τα τραγανά παρασκευάσματα είναι καλύτερα την ίδια μέρα.",
    }[lang]
    return role, tips, variations, storage


def express_title(path, lang):
    m = re.search(r"recette-express-olive-(\d+)-", path.name)
    if not m:
        return None
    idx = int(m.group(1)) % len(QUICK_TITLES)
    lang_index = {"fr": 0, "en": 1, "it": 2, "el": 3}[lang]
    return QUICK_TITLES[idx][lang_index]


def render_recipe(path):
    old = read(path)
    lang = parse_lang(old, path.name)
    labels = LANGS[lang]
    title = express_title(path, lang) or parse_h1(old)
    alternates = parse_alternates(old)
    slug = slug_text(path, title)
    kind = recipe_kind(slug)
    prep, cook, rest, servings = recipe_times(kind)
    difficulty = labels["easy"] if kind != "bread" else labels["medium"]
    ingredients = base_ingredients(slug, lang, kind)
    steps = recipe_steps(title, kind, lang)
    role, tips, variations, storage = recipe_paragraphs(kind, lang)
    desc = labels["recipe_desc"].format(title=title)
    schema = {
        "@context": "https://schema.org/",
        "@type": "Recipe",
        "name": title,
        "author": {"@type": "Organization", "name": "L'Or Vert"},
        "dateModified": "2026-05-04",
        "description": desc,
        "prepTime": "PT20M",
        "cookTime": "PT20M" if cook != "0 min" else "PT0M",
        "recipeYield": servings,
        "recipeIngredient": ingredients,
        "recipeInstructions": [{"@type": "HowToStep", "text": step} for step in steps],
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.8", "ratingCount": "96"},
    }
    ingredient_html = "\n".join(f"            <li>{esc(item)}</li>" for item in ingredients)
    step_html = "\n".join(f"            <li>{esc(step)}</li>" for step in steps)
    tips_html = "\n".join(f"            <li>{esc(tip)}</li>" for tip in tips)
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{esc(title)} — Recettes L'Or Vert</title>
    <meta name="description" content="{esc(desc)}">
    <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%232E4A40'/%3E%3Cpath fill='%23F2D8C4' d='M16 5.5S9.5 14 9.5 19a6.5 6.5 0 0013 0c0-5-6.5-13.5-6.5-13.5z'/%3E%3C/svg%3E" type="image/svg+xml">
    <link rel="stylesheet" href="../assets/seo.css">
{hreflang_html("recipes", alternates)}
    <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False, indent=2)}</script>
</head>
<body>
<nav class="site-nav"><div class="container"><a href="../{labels["index"]}" class="logo">L'OR VERT / RECETTES</a>{lang_switch(alternates, lang)}</div></nav>
<header class="page-hero" style="background: linear-gradient(135deg, var(--avocado) 0%, var(--sage) 100%);">
    <div class="container">
        <div class="breadcrumb"><a href="../{labels["index"]}">{esc(labels["home"])}</a> &raquo; {esc(labels["recipes"])}</div>
        <h1>{esc(title)}</h1>
        <p class="lede">{esc(desc)}</p>
    </div>
</header>
<main class="container">
    <article class="guide">
        <div class="callout"><strong>{esc(labels["prep"])} :</strong> {prep} &middot; <strong>{esc(labels["cook"])} :</strong> {cook} &middot; <strong>{esc(labels["rest"])} :</strong> {rest} &middot; <strong>{esc(labels["difficulty"])} :</strong> {esc(difficulty)}</div>
        <p class="intro">{esc(labels["recipe_intro"].format(title=title))}</p>

        <h2>{esc(labels["ingredients"])}</h2>
        <ul>
{ingredient_html}
        </ul>

        <h2>{esc(labels["steps"])}</h2>
        <ol>
{step_html}
        </ol>

        <h2>{esc(labels["oil_role"])}</h2>
        <p>{esc(role)}</p>

        <h2>{esc(labels["tips"])}</h2>
        <ul>
{tips_html}
        </ul>

        <h2>{esc(labels["variations"])}</h2>
        <p>{esc(variations)}</p>

        <h2>{esc(labels["storage"])}</h2>
        <p>{esc(storage)}</p>
    </article>
</main>
<footer class="site-footer"><div class="container"><h3>L'Or Vert</h3><p>{esc(labels["footer"])}</p><div class="copyright">&copy; 2026 — L'Or Vert</div></div></footer>
</body>
</html>
"""


def main():
    blog_count = 0
    recipe_count = 0
    for path in sorted(BLOG_DIR.glob("*.html")):
        write(path, render_blog(path))
        blog_count += 1
    for path in sorted(RECIPES_DIR.glob("*.html")):
        write(path, render_recipe(path))
        recipe_count += 1
    print(f"Enriched {blog_count} blog pages and {recipe_count} recipe pages.")


if __name__ == "__main__":
    main()

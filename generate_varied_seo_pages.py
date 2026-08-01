import os
import re
import unicodedata

def slugify(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    text = re.sub(r'[-\s]+', '-', text)
    return text

prefixes = [
    {"fr": "Guide complet : ", "en": "Complete Guide: ", "it": "Guida completa: ", "el": "Πλήρης Οδηγός: "},
    {"fr": "Les secrets de ", "en": "The Secrets of ", "it": "I segreti di ", "el": "Τα μυστικά του "},
    {"fr": "Pourquoi choisir ", "en": "Why Choose ", "it": "Perché scegliere ", "el": "Γιατί να επιλέξετε "},
    {"fr": "Comparatif : ", "en": "Comparison: ", "it": "Confronto: ", "el": "Σύγκριση: "},
    {"fr": "Découvrir ", "en": "Discovering ", "it": "Alla scoperta di ", "el": "Ανακαλύπτοντας "}
]

subjects = [
    {"fr": "l'huile d'olive bio", "en": "organic olive oil", "it": "l'olio d'oliva biologico", "el": "το βιολογικό ελαιόλαδο"},
    {"fr": "l'huile d'olive extra vierge", "en": "extra virgin olive oil", "it": "l'olio extravergine d'oliva", "el": "το εξαιρετικό παρθένο ελαιόλαδο"},
    {"fr": "l'huile d'olive AOP", "en": "PDO olive oil", "it": "l'olio d'oliva DOP", "el": "το ελαιόλαδο ΠΟΠ"},
    {"fr": "l'huile d'olive non filtrée", "en": "unfiltered olive oil", "it": "l'olio d'oliva non filtrato", "el": "το αφιλτράριστο ελαιόλαδο"},
    {"fr": "l'huile d'olive artisanale", "en": "artisanal olive oil", "it": "l'olio d'oliva artigianale", "el": "το χειροποίητο ελαιόλαδο"},
    {"fr": "l'huile d'olive de Crète", "en": "Cretan olive oil", "it": "l'olio d'oliva di Creta", "el": "το κρητικό ελαιόλαδο"},
    {"fr": "l'huile d'olive de Toscane", "en": "Tuscan olive oil", "it": "l'olio d'oliva toscano", "el": "το ελαιόλαδο Τοσκάνης"},
    {"fr": "l'huile d'olive d'Andalousie", "en": "Andalusian olive oil", "it": "l'olio d'oliva andaluso", "el": "το ελαιόλαδο Ανδαλουσίας"},
    {"fr": "l'huile riche en polyphénols", "en": "high-polyphenol olive oil", "it": "l'olio ricco di polifenoli", "el": "το ελαιόλαδο με πολυφαινόλες"},
    {"fr": "l'huile pressée à froid", "en": "cold-pressed olive oil", "it": "l'olio spremuto a freddo", "el": "το ελαιόλαδο ψυχρής έκθλιψης"}
]

suffixes = [
    ({"fr": " pour la santé", "en": " for health", "it": " per la salute", "el": " για την υγεία"}, "health"),
    ({"fr": " en cuisine", "en": " in cooking", "it": " in cucina", "el": " στη μαγειρική"}, "cooking"),
    ({"fr": " pour le visage", "en": " for the face", "it": " per il viso", "el": " για το πρόσωπο"}, "face"),
    ({"fr": " pour les cheveux", "en": " for hair", "it": " per i capelli", "el": " για τα μαλλιά"}, "hair"),
    ({"fr": " au quotidien", "en": " for daily use", "it": " nell'uso quotidiano", "el": " στην καθημερινότητα"}, "daily")
]

base_translations = {
    "fr": { "index": "index-fr.html", "home": "Accueil", "guides": "Guides", "pub": "Publication", "min": "min de lecture", "footer": "Étude de Marché Huile d'Olive 2026. Analyse des tendances et opportunités premium.", "rights": "Tous droits réservés" },
    "en": { "index": "index-en.html", "home": "Home", "guides": "Guides", "pub": "Published", "min": "min read", "footer": "Olive Oil Market Study 2026. Analysis of premium trends and opportunities.", "rights": "All rights reserved" },
    "it": { "index": "index-it.html", "home": "Home", "guides": "Guide", "pub": "Pubblicazione", "min": "min di lettura", "footer": "Studio di Mercato Olio d'Oliva 2026. Analisi delle tendenze e opportunità premium.", "rights": "Tutti i diritti riservati" },
    "el": { "index": "index-el.html", "home": "Αρχική", "guides": "Οδηγοί", "pub": "Δημοσίευση", "min": "λεπτά ανάγνωσης", "footer": "Μελέτη Αγοράς Ελαιολάδου 2026. Ανάλυση των premium τάσεων και ευκαιριών.", "rights": "Με επιφύλαξη παντός δικαιώματος" }
}

category_translations = {
    "health": {
        "fr": {
            "intro": "L'utilisation de {subject} est reconnue mondialement pour ses vertus médicinales exceptionnelles et son rôle protecteur dans l'organisme.",
            "h2_1": "Les bénéfices pour l'organisme", "p_1": "Sa composition unique en acides gras monoinsaturés et en antioxydants en fait un allié de choix pour la protection cardiovasculaire et la réduction de l'inflammation.",
            "h3_1": "Impact direct sur la santé",
            "li_1_s": "Cœur :", "li_1_t": "Diminue le mauvais cholestérol et protège les artères.",
            "li_2_s": "Digestion :", "li_2_t": "Facilite le transit intestinal et stimule la vésicule biliaire.",
            "li_3_s": "Immunité :", "li_3_t": "Renforce les défenses naturelles grâce à la vitamine E.",
            "quote": "Une cuillère par jour est une prescription naturelle pour une vie plus saine.",
            "h3_2": "Utilisation thérapeutique", "p_2": "Consommée à jeun le matin ou ajoutée à vos plats, elle libère tout son potentiel curatif lorsqu'elle est extra vierge et pressée à froid."
        },
        "en": {
            "intro": "The use of {subject} is globally recognized for its exceptional medicinal properties and its protective role in the body.",
            "h2_1": "Benefits for the body", "p_1": "Its unique composition of monounsaturated fatty acids and antioxidants makes it a key ally for cardiovascular protection and inflammation reduction.",
            "h3_1": "Direct health impact",
            "li_1_s": "Heart:", "li_1_t": "Lowers bad cholesterol and protects arteries.",
            "li_2_s": "Digestion:", "li_2_t": "Eases intestinal transit and stimulates the gallbladder.",
            "li_3_s": "Immunity:", "li_3_t": "Strengthens natural defenses thanks to vitamin E.",
            "quote": "One spoonful a day is a natural prescription for a healthier life.",
            "h3_2": "Therapeutic use", "p_2": "Consumed on an empty stomach in the morning or added to your dishes, it unleashes its full healing potential when extra virgin and cold-pressed."
        },
        "it": {
            "intro": "L'uso di {subject} è riconosciuto a livello mondiale per le sue eccezionali virtù medicinali e il suo ruolo protettivo per l'organismo.",
            "h2_1": "I benefici per l'organismo", "p_1": "La sua composizione unica di acidi grassi monoinsaturi e antiossidanti lo rende un alleato fondamentale per la protezione cardiovascolare e la riduzione delle infiammazioni.",
            "h3_1": "Impatto diretto sulla salute",
            "li_1_s": "Cuore:", "li_1_t": "Riduce il colesterolo cattivo e protegge le arterie.",
            "li_2_s": "Digestione:", "li_2_t": "Facilita il transito intestinale e stimola la cistifellea.",
            "li_3_s": "Immunità:", "li_3_t": "Rafforza le difese naturali grazie alla vitamina E.",
            "quote": "Un cucchiaio al giorno è una prescrizione naturale per una vita più sana.",
            "h3_2": "Uso terapeutico", "p_2": "Consumato a stomaco vuoto al mattino o aggiunto ai piatti, sprigiona tutto il suo potenziale curativo se extravergine e spremuto a freddo."
        },
        "el": {
            "intro": "Η χρήση που έχει {subject} αναγνωρίζεται παγκοσμίως για τις εξαιρετικές ιατρικές της ιδιότητες και τον προστατευτικό της ρόλο στον οργανισμό.",
            "h2_1": "Τα οφέλη για τον οργανισμό", "p_1": "Η μοναδική σύνθεση σε μονοακόρεστα λιπαρά οξέα και αντιοξειδωτικά το καθιστά βασικό σύμμαχο για την καρδιαγγειακή προστασία και τη μείωση των φλεγμονών.",
            "h3_1": "Άμεσος αντίκτυπος στην υγεία",
            "li_1_s": "Καρδιά:", "li_1_t": "Μειώνει την κακή χοληστερόλη και προστατεύει τις αρτηρίες.",
            "li_2_s": "Πέψη:", "li_2_t": "Διευκολύνει την εντερική διέλευση και διεγείρει τη χοληδόχο κύστη.",
            "li_3_s": "Ανοσία:", "li_3_t": "Ενισχύει τις φυσικές άμυνες χάρη στη βιταμίνη Ε.",
            "quote": "Μια κουταλιά την ημέρα είναι μια φυσική συνταγή για μια πιο υγιεινή ζωή.",
            "h3_2": "Θεραπευτική χρήση", "p_2": "Καταναλώνεται με άδειο στομάχι το πρωί ή προστίθεται στα πιάτα σας, απελευθερώνει πλήρως τις θεραπευτικές του δυνατότητες όταν είναι εξαιρετικό παρθένο και ψυχρής έκθλιψης."
        }
    },
    "cooking": {
        "fr": {
            "intro": "Élément central de la gastronomie méditerranéenne, {subject} sublime les saveurs de vos plats tout en apportant une texture incomparable.",
            "h2_1": "L'excellence en cuisine", "p_1": "Qu'elle soit utilisée pour frire doucement, rôtir ou simplement assaisonner, elle résiste bien à la chaleur et magnifie les ingrédients frais.",
            "h3_1": "Conseils culinaires",
            "li_1_s": "Cuisson :", "li_1_t": "Parfaite jusqu'à 180°C (point de fumée) sans perdre ses qualités.",
            "li_2_s": "Assaisonnement :", "li_2_t": "Un filet en fin de cuisson révèle les arômes des légumes ou des poissons.",
            "li_3_s": "Pâtisserie :", "li_3_t": "Remplace avantageusement le beurre pour des gâteaux plus légers et moelleux.",
            "quote": "Le secret d'un grand chef réside souvent dans la qualité de son huile.",
            "h3_2": "Accords parfaits", "p_2": "Variez les plaisirs en associant des huiles fruitées mûres pour les desserts et des fruités verts intenses pour les grillades."
        },
        "en": {
            "intro": "A central element of Mediterranean gastronomy, {subject} sublimates the flavors of your dishes while providing an incomparable texture.",
            "h2_1": "Excellence in cooking", "p_1": "Whether used for gentle frying, roasting, or simply dressing, it withstands heat well and magnifies fresh ingredients.",
            "h3_1": "Culinary tips",
            "li_1_s": "Cooking:", "li_1_t": "Perfect up to 180°C (smoke point) without losing its qualities.",
            "li_2_s": "Seasoning:", "li_2_t": "A drizzle at the end of cooking reveals the aromas of vegetables or fish.",
            "li_3_s": "Baking:", "li_3_t": "An excellent substitute for butter for lighter and moister cakes.",
            "quote": "The secret of a great chef often lies in the quality of their oil.",
            "h3_2": "Perfect pairings", "p_2": "Vary the pleasures by associating ripe fruity oils for desserts and intense green fruitiness for grilled foods."
        },
        "it": {
            "intro": "Elemento centrale della gastronomia mediterranea, {subject} esalta i sapori dei tuoi piatti offrendo una consistenza incomparabile.",
            "h2_1": "L'eccellenza in cucina", "p_1": "Che sia usato per friggere delicatamente, arrostire o semplicemente condire, resiste bene al calore e magnifica gli ingredienti freschi.",
            "h3_1": "Consigli culinari",
            "li_1_s": "Cottura:", "li_1_t": "Perfetto fino a 180°C (punto di fumo) senza perdere le sue qualità.",
            "li_2_s": "Condimento:", "li_2_t": "Un filo a fine cottura rivela gli aromi di verdure o pesce.",
            "li_3_s": "Pasticceria:", "li_3_t": "Sostituisce vantaggiosamente il burro per torte più leggere e soffici.",
            "quote": "Il segreto di un grande chef risiede spesso nella qualità del suo olio.",
            "h3_2": "Abbinamenti perfetti", "p_2": "Varia i piaceri associando oli dal fruttato maturo per i dessert e dal fruttato verde intenso per le grigliate."
        },
        "el": {
            "intro": "Κεντρικό στοιχείο της μεσογειακής γαστρονομίας, {subject} αναδεικνύει τις γεύσεις των πιάτων σας παρέχοντας παράλληλα μια απαράμιλλη υφή.",
            "h2_1": "Η αριστεία στη μαγειρική", "p_1": "Είτε χρησιμοποιείται για απαλό τηγάνισμα, ψήσιμο ή απλά ως ντρέσινγκ, αντέχει καλά στη θερμότητα και μεγεθύνει τα φρέσκα συστατικά.",
            "h3_1": "Μαγειρικές συμβουλές",
            "li_1_s": "Μαγείρεμα:", "li_1_t": "Τέλειο μέχρι τους 180°C (σημείο καπνού) χωρίς να χάνει τις ιδιότητές του.",
            "li_2_s": "Καρύκευμα:", "li_2_t": "Λίγες σταγόνες στο τέλος του μαγειρέματος αναδεικνύουν τα αρώματα των λαχανικών ή του ψαριού.",
            "li_3_s": "Ζαχαροπλαστική:", "li_3_t": "Εξαιρετικό υποκατάστατο του βουτύρου για πιο ελαφριά και αφράτα κέικ.",
            "quote": "Το μυστικό ενός σπουδαίου σεφ συχνά κρύβεται στην ποιότητα του λαδιού του.",
            "h3_2": "Τέλειοι συνδυασμοί", "p_2": "Ποικίλετε τις απολαύσεις συνδυάζοντας ώριμα φρουτώδη έλαια για επιδόρπια και έντονα πράσινα φρουτώδη για ψητά."
        }
    },
    "face": {
        "fr": {
            "intro": "Véritable élixir de beauté ancestral, {subject} est un soin cosmétique naturel redoutable pour la peau du visage.",
            "h2_1": "Une hydratation profonde", "p_1": "Gorgée de squalène et de vitamines A et E, elle nourrit l'épiderme en profondeur, prévient le vieillissement cutané et apaise les irritations.",
            "h3_1": "Bienfaits dermatologiques",
            "li_1_s": "Anti-âge :", "li_1_t": "Lutte contre les radicaux libres responsables des rides.",
            "li_2_s": "Démaquillant :", "li_2_t": "Dissout le maquillage tenace (même waterproof) tout en douceur.",
            "li_3_s": "Réparatrice :", "li_3_t": "Aide à la cicatrisation et calme les peaux sèches ou atopiques.",
            "quote": "La nature offre les meilleurs cosmétiques à ceux qui savent les utiliser.",
            "h3_2": "Rituel beauté", "p_2": "Appliquez quelques gouttes le soir sur une peau propre, en massant délicatement pour stimuler la microcirculation et illuminer le teint."
        },
        "en": {
            "intro": "A true ancestral beauty elixir, {subject} is a formidable natural cosmetic treatment for facial skin.",
            "h2_1": "Deep hydration", "p_1": "Packed with squalene and vitamins A and E, it deeply nourishes the epidermis, prevents skin aging, and soothes irritations.",
            "h3_1": "Dermatological benefits",
            "li_1_s": "Anti-aging:", "li_1_t": "Fights against free radicals responsible for wrinkles.",
            "li_2_s": "Makeup remover:", "li_2_t": "Gently dissolves stubborn makeup (even waterproof).",
            "li_3_s": "Repairing:", "li_3_t": "Aids in healing and calms dry or atopic skin.",
            "quote": "Nature offers the best cosmetics to those who know how to use them.",
            "h3_2": "Beauty ritual", "p_2": "Apply a few drops at night on clean skin, massaging gently to stimulate microcirculation and brighten the complexion."
        },
        "it": {
            "intro": "Vero elisir di bellezza ancestrale, {subject} è un formidabile trattamento cosmetico naturale per la pelle del viso.",
            "h2_1": "Un'idratazione profonda", "p_1": "Ricco di squalene e vitamine A ed E, nutre in profondità l'epidermide, previene l'invecchiamento cutaneo e lenisce le irritazioni.",
            "h3_1": "Benefici dermatologici",
            "li_1_s": "Antietà:", "li_1_t": "Combatte i radicali liberi responsabili delle rughe.",
            "li_2_s": "Struccante:", "li_2_t": "Scioglie delicatamente il trucco ostinato (anche waterproof).",
            "li_3_s": "Riparatore:", "li_3_t": "Aiuta la cicatrizzazione e calma la pelle secca o atopica.",
            "quote": "La natura offre i migliori cosmetici a chi sa usarli.",
            "h3_2": "Rituale di bellezza", "p_2": "Applica alcune gocce la sera sulla pelle pulita, massaggiando delicatamente per stimolare la microcircolazione e illuminare l'incarnato."
        },
        "el": {
            "intro": "Ένα αληθινό προγονικό ελιξίριο ομορφιάς, {subject} είναι μια τρομερή φυσική καλλυντική θεραπεία για το δέρμα του προσώπου.",
            "h2_1": "Βαθιά ενυδάτωση", "p_1": "Γεμάτο με σκουαλένιο και βιταμίνες Α και Ε, θρέφει σε βάθος την επιδερμίδα, προλαμβάνει τη γήρανση του δέρματος και καταπραΰνει τους ερεθισμούς.",
            "h3_1": "Δερματολογικά οφέλη",
            "li_1_s": "Αντιγήρανση:", "li_1_t": "Καταπολεμά τις ελεύθερες ρίζες που ευθύνονται για τις ρυτίδες.",
            "li_2_s": "Ντεμακιγιάζ:", "li_2_t": "Διαλύει απαλά το επίμονο μακιγιάζ (ακόμη και το αδιάβροχο).",
            "li_3_s": "Επανορθωτικό:", "li_3_t": "Βοηθά στην επούλωση και ηρεμεί το ξηρό ή ατοπικό δέρμα.",
            "quote": "Η φύση προσφέρει τα καλύτερα καλλυντικά σε όσους ξέρουν να τα χρησιμοποιούν.",
            "h3_2": "Τελετουργικό ομορφιάς", "p_2": "Εφαρμόστε λίγες σταγόνες το βράδυ σε καθαρό δέρμα, κάνοντας απαλό μασάζ για να τονώσετε τη μικροκυκλοφορία και να φωτίσετε την επιδερμίδα."
        }
    },
    "hair": {
        "fr": {
            "intro": "Pour des cheveux éclatants de santé, l'utilisation de {subject} offre une alternative puissante aux soins capillaires chimiques.",
            "h2_1": "Un masque capillaire naturel", "p_1": "Ses agents hydratants pénètrent la fibre capillaire pour réparer les pointes fourchues et redonner souplesse et brillance aux cheveux ternes.",
            "h3_1": "Actions sur le cheveu",
            "li_1_s": "Nutrition :", "li_1_t": "Restaure le film lipidique des cheveux secs et abîmés.",
            "li_2_s": "Cuir chevelu :", "li_2_t": "Apaise les démangeaisons et aide à réduire les pellicules.",
            "li_3_s": "Croissance :", "li_3_t": "Masser le cuir chevelu avec l'huile stimule la pousse.",
            "quote": "La force d'un olivier transmise à votre chevelure.",
            "h3_2": "Comment l'appliquer ?", "p_2": "En bain d'huile avant le shampooing, laissez poser au moins 30 minutes, ou toute une nuit sous une serviette tiède pour une efficacité maximale."
        },
        "en": {
            "intro": "For radiantly healthy hair, using {subject} offers a powerful alternative to chemical hair care products.",
            "h2_1": "A natural hair mask", "p_1": "Its moisturizing agents penetrate the hair fiber to repair split ends and restore suppleness and shine to dull hair.",
            "h3_1": "Actions on the hair",
            "li_1_s": "Nutrition:", "li_1_t": "Restores the lipid film of dry and damaged hair.",
            "li_2_s": "Scalp:", "li_2_t": "Soothes itching and helps reduce dandruff.",
            "li_3_s": "Growth:", "li_3_t": "Massaging the scalp with the oil stimulates hair growth.",
            "quote": "The strength of an olive tree transmitted to your hair.",
            "h3_2": "How to apply it?", "p_2": "As an oil bath before shampooing, leave it on for at least 30 minutes, or overnight under a warm towel for maximum effectiveness."
        },
        "it": {
            "intro": "Per capelli luminosi e sani, l'uso di {subject} offre una potente alternativa ai trattamenti chimici per capelli.",
            "h2_1": "Una maschera per capelli naturale", "p_1": "I suoi agenti idratanti penetrano nella fibra capillare per riparare le doppie punte e ridare morbidezza e lucentezza ai capelli opachi.",
            "h3_1": "Azioni sul capello",
            "li_1_s": "Nutrizione:", "li_1_t": "Ripristina il film lipidico dei capelli secchi e danneggiati.",
            "li_2_s": "Cuoio capelluto:", "li_2_t": "Lenisce il prurito e aiuta a ridurre la forfora.",
            "li_3_s": "Crescita:", "li_3_t": "Massaggiare il cuoio capelluto con l'olio stimola la crescita.",
            "quote": "La forza di un ulivo trasmessa alla tua chioma.",
            "h3_2": "Come applicarlo?", "p_2": "Come impacco pre-shampoo, lascia in posa per almeno 30 minuti, o per tutta la notte sotto un asciugamano tiepido per la massima efficacia."
        },
        "el": {
            "intro": "Για λαμπερά υγιή μαλλιά, χρησιμοποιώντας {subject} προσφέρει μια ισχυρή εναλλακτική στα χημικά προϊόντα περιποίησης μαλλιών.",
            "h2_1": "Μια φυσική μάσκα μαλλιών", "p_1": "Οι ενυδατικοί παράγοντες του διεισδύουν στην τρίχα για να επανορθώσουν τη φαλίδα και να επαναφέρουν την ελαστικότητα και τη λάμψη στα θαμπά μαλλιά.",
            "h3_1": "Δράσεις στα μαλλιά",
            "li_1_s": "Θρέψη:", "li_1_t": "Αποκαθιστά το λιπιδικό φιλμ των ξηρών και ταλαιπωρημένων μαλλιών.",
            "li_2_s": "Τριχωτό της κεφαλής:", "li_2_t": "Καταπραΰνει τον κνησμό και βοηθά στη μείωση της πιτυρίδας.",
            "li_3_s": "Ανάπτυξη:", "li_3_t": "Το μασάζ στο τριχωτό της κεφαλής με το λάδι διεγείρει την ανάπτυξη των μαλλιών.",
            "quote": "Η δύναμη μιας ελιάς μεταδίδεται στα μαλλιά σας.",
            "h3_2": "Πώς να το εφαρμόσετε;", "p_2": "Ως λουτρό λαδιού πριν το λούσιμο, αφήστε το για τουλάχιστον 30 λεπτά, ή όλη τη νύχτα κάτω από μια ζεστή πετσέτα για μέγιστη αποτελεσματικότητα."
        }
    },
    "daily": {
        "fr": {
            "intro": "L'intégration de {subject} dans vos habitudes quotidiennes est une démarche simple qui transforme votre mode de vie.",
            "h2_1": "Un produit aux mille usages", "p_1": "De la table à la salle de bain, en passant par l'entretien naturel de la maison, c'est l'un des produits les plus polyvalents que vous puissiez posséder.",
            "h3_1": "Usages surprenants",
            "li_1_s": "Entretien :", "li_1_t": "Fait briller les meubles en bois et nourrit le cuir.",
            "li_2_s": "Bien-être :", "li_2_t": "Utile en massage pour soulager les articulations fatiguées.",
            "li_3_s": "Animaux :", "li_3_t": "Une goutte dans la nourriture de vos animaux rend leur pelage soyeux.",
            "quote": "Un foyer méditerranéen ne manque jamais d'une bouteille de cet or liquide.",
            "h3_2": "Le choix de la constance", "p_2": "L'utiliser chaque jour, même en petites quantités, permet de profiter pleinement de sa richesse nutritionnelle et de ses propriétés émollientes."
        },
        "en": {
            "intro": "Integrating {subject} into your daily habits is a simple step that transforms your lifestyle.",
            "h2_1": "A product of a thousand uses", "p_1": "From the table to the bathroom, including natural home maintenance, it is one of the most versatile products you can own.",
            "h3_1": "Surprising uses",
            "li_1_s": "Maintenance:", "li_1_t": "Shines wooden furniture and nourishes leather.",
            "li_2_s": "Well-being:", "li_2_t": "Useful in massage to relieve tired joints.",
            "li_3_s": "Pets:", "li_3_t": "A drop in your pets' food makes their coat silky.",
            "quote": "A Mediterranean home is never without a bottle of this liquid gold.",
            "h3_2": "The choice of consistency", "p_2": "Using it every day, even in small quantities, allows you to fully enjoy its nutritional wealth and emollient properties."
        },
        "it": {
            "intro": "L'integrazione di {subject} nelle tue abitudini quotidiane è un passo semplice che trasforma il tuo stile di vita.",
            "h2_1": "Un prodotto dai mille usi", "p_1": "Dalla tavola al bagno, passando per la manutenzione naturale della casa, è uno dei prodotti più versatili che tu possa possedere.",
            "h3_1": "Usi sorprendenti",
            "li_1_s": "Manutenzione:", "li_1_t": "Lucidare i mobili in legno e nutre la pelle.",
            "li_2_s": "Benessere:", "li_2_t": "Utile nel massaggio per alleviare le articolazioni stanche.",
            "li_3_s": "Animali domestici:", "li_3_t": "Una goccia nel cibo dei tuoi animali rende il loro pelo setoso.",
            "quote": "In una casa mediterranea non manca mai una bottiglia di questo oro liquido.",
            "h3_2": "La scelta della costanza", "p_2": "Usarlo ogni giorno, anche in piccole quantità, permette di godere appieno della sua ricchezza nutrizionale e delle sue proprietà emollienti."
        },
        "el": {
            "intro": "Η ενσωμάτωση που έχει {subject} στις καθημερινές σας συνήθειες είναι ένα απλό βήμα που μεταμορφώνει τον τρόπο ζωής σας.",
            "h2_1": "Ένα προϊόν με χίλιες χρήσεις", "p_1": "Από το τραπέζι μέχρι το μπάνιο, συμπεριλαμβανομένης της φυσικής συντήρησης του σπιτιού, είναι ένα από τα πιο ευέλικτα προϊόντα που μπορείτε να κατέχετε.",
            "h3_1": "Εκπληκτικές χρήσεις",
            "li_1_s": "Συντήρηση:", "li_1_t": "Γυαλίζει ξύλινα έπιπλα και θρέφει το δέρμα.",
            "li_2_s": "Ευεξία:", "li_2_t": "Χρήσιμο στο μασάζ για την ανακούφιση των κουρασμένων αρθρώσεων.",
            "li_3_s": "Κατοικίδια:", "li_3_t": "Μια σταγόνα στο φαγητό των κατοικίδιων σας κάνει το τρίχωμά τους μεταξένιο.",
            "quote": "Ένα μεσογειακό σπίτι δεν στερείται ποτέ ένα μπουκάλι από αυτόν τον υγρό χρυσό.",
            "h3_2": "Η επιλογή της συνέπειας", "p_2": "Η καθημερινή του χρήση, ακόμη και σε μικρές ποσότητες, σας επιτρέπει να απολαύσετε πλήρως τον διατροφικό του πλούτο και τις μαλακτικές του ιδιότητες."
        }
    }
}


html_template = """<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — L'Or Vert</title>
    <meta name="description" content="{desc}">
    <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%232E4A40'/%3E%3Cpath fill='%23F2D8C4' d='M16 5.5S9.5 14 9.5 19a6.5 6.5 0 0013 0c0-5-6.5-13.5-6.5-13.5z'/%3E%3C/svg%3E" type="image/svg+xml">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Space+Mono&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../assets/seo.css">
    <link rel="alternate" hreflang="fr" href="https://huiledefes.com/guides/{slug_fr}" />
    <link rel="alternate" hreflang="en" href="https://huiledefes.com/guides/{slug_en}" />
    <link rel="alternate" hreflang="it" href="https://huiledefes.com/guides/{slug_it}" />
    <link rel="alternate" hreflang="el" href="https://huiledefes.com/guides/{slug_el}" />
</head>
<body>

<nav class="site-nav">
    <div class="container">
        <a href="../{index_page}" class="logo">L'OR VERT</a>
        <div class="lang-switch">
            <a href="{slug_fr}" class="{active_fr}">FR</a> 
            <a href="{slug_en}" class="{active_en}">EN</a> 
            <a href="{slug_it}" class="{active_it}">IT</a> 
            <a href="{slug_el}" class="{active_el}">EL</a> 
        </div>
    </div>
</nav>

<header class="page-hero">
    <div class="container">
        <div class="breadcrumb">
            <a href="../{index_page}">{home_label}</a> &raquo; {guides_label}
        </div>
        <h1>{title}</h1>
        <p class="lede">{subtitle}</p>
        <div class="meta">{published_label} : Mai 2026 &middot; 5 {min_read_label}</div>
    </div>
</header>

<main class="container">
    <article class="guide">
        <p class='intro'>{intro_text}</p>
        
        <h2>{h2_1}</h2>
        <p>{p_1}</p>
        
        <h3>{h3_1}</h3>
        <ul>
            <li><strong>{li_1_strong}</strong> {li_1_text}</li>
            <li><strong>{li_2_strong}</strong> {li_2_text}</li>
            <li><strong>{li_3_strong}</strong> {li_3_text}</li>
        </ul>

        <blockquote>"{quote_text}"</blockquote>

        <h3>{h3_2}</h3>
        <p>{p_2}</p>
    </article>
</main>

<footer class="site-footer">
    <div class="container">
        <h3>L'Or Vert</h3>
        <p>{footer_text}</p>
        <div class="copyright">&copy; 2026 &mdash; {rights_text}</div>
    </div>
</footer>

</body>
</html>"""

urls_to_add = []
guides_dir = r"C:\Users\Antoine\etude-huile-olive\guides"

print("Génération de 1000 pages SEO VARIÉES en cours...")

# Read sitemap to check existing URLs
sitemap_path = r"C:\Users\Antoine\etude-huile-olive\sitemap.xml"
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

count = 0
for pre in prefixes:
    for sub in subjects:
        for suf_data, cat_key in suffixes:
            en_title = pre["en"] + sub["en"] + suf_data["en"]
            base_slug = slugify(en_title)
            
            slugs = {
                "fr": f"{base_slug}-fr.html",
                "en": f"{base_slug}-en.html",
                "it": f"{base_slug}-it.html",
                "el": f"{base_slug}-el.html"
            }
            
            titles = {
                "fr": pre["fr"] + sub["fr"] + suf_data["fr"],
                "en": en_title,
                "it": pre["it"] + sub["it"] + suf_data["it"],
                "el": pre["el"] + sub["el"] + suf_data["el"]
            }
            
            for lang in ["fr", "en", "it", "el"]:
                title = titles[lang]
                
                # Fetch translation data for the specific category
                cat_trans = category_translations[cat_key][lang]
                base_trans = base_translations[lang]
                
                # Inject the subject directly into the intro for even more variation
                intro_formatted = cat_trans["intro"].format(subject=sub[lang])
                desc = intro_formatted
                
                html = html_template.format(
                    lang=lang,
                    title=title,
                    desc=desc,
                    slug_fr=slugs["fr"],
                    slug_en=slugs["en"],
                    slug_it=slugs["it"],
                    slug_el=slugs["el"],
                    index_page=base_trans["index"],
                    active_fr="active" if lang == "fr" else "",
                    active_en="active" if lang == "en" else "",
                    active_it="active" if lang == "it" else "",
                    active_el="active" if lang == "el" else "",
                    home_label=base_trans["home"],
                    guides_label=base_trans["guides"],
                    subtitle=title,
                    published_label=base_trans["pub"],
                    min_read_label=base_trans["min"],
                    intro_text=intro_formatted,
                    h2_1=cat_trans["h2_1"],
                    p_1=cat_trans["p_1"],
                    h3_1=cat_trans["h3_1"],
                    li_1_strong=cat_trans["li_1_s"],
                    li_1_text=cat_trans["li_1_t"],
                    li_2_strong=cat_trans["li_2_s"],
                    li_2_text=cat_trans["li_2_t"],
                    li_3_strong=cat_trans["li_3_s"],
                    li_3_text=cat_trans["li_3_t"],
                    quote_text=cat_trans["quote"],
                    h3_2=cat_trans["h3_2"],
                    p_2=cat_trans["p_2"],
                    footer_text=base_trans["footer"],
                    rights_text=base_trans["rights"]
                )
                
                filepath = os.path.join(guides_dir, slugs[lang])
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(html)
                    
                url_tag = f"  <url><loc>https://huiledefes.com/guides/{slugs[lang]}</loc><priority>0.6</priority></url>\n"
                if url_tag not in sitemap_content:
                    urls_to_add.append(url_tag)
                count += 1

print(f"{count} fichiers HTML VARIÉS ont été créés/mis à jour.")

if urls_to_add:
    print(f"Ajout de {len(urls_to_add)} nouvelles URLs au sitemap...")
    insert_pos = sitemap_content.rfind("</urlset>")
    if insert_pos != -1:
        new_sitemap = sitemap_content[:insert_pos] + "".join(urls_to_add) + sitemap_content[insert_pos:]
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write(new_sitemap)
    print("Sitemap mis à jour.")
else:
    print("Toutes les URLs sont déjà présentes dans le sitemap.")

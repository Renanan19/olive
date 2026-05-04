import html
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
GUIDES_DIR = ROOT / "guides"
RECIPES_DIR = ROOT / "recipes"
SITE = "https://huiledefes.com"


GUIDE_MARK = ("<!-- guide-depth:start -->", "<!-- guide-depth:end -->")
RECIPE_MARK = ("<!-- recipe-depth:start -->", "<!-- recipe-depth:end -->")


LANG = {
    "fr": {
        "updated": "Mis à jour",
        "read": "12 min de lecture",
        "short": "Réponse courte",
        "why": "Pourquoi ce sujet compte",
        "signals": "Signaux à vérifier",
        "method": "Méthode pratique",
        "case": "Cas concret",
        "mistakes": "Erreurs fréquentes",
        "faq": "Questions fréquentes",
        "conclusion": "Conclusion",
        "recipe_why": "Pourquoi cette recette fonctionne",
        "recipe_oil": "Choisir la bonne huile",
        "recipe_method": "Technique et précision",
        "recipe_service": "Service, accords et variantes",
        "recipe_mistakes": "Erreurs à éviter",
        "recipe_faq": "Questions fréquentes",
    },
    "en": {
        "updated": "Updated",
        "read": "12 min read",
        "short": "Short answer",
        "why": "Why this topic matters",
        "signals": "Signals to check",
        "method": "Practical method",
        "case": "Concrete case",
        "mistakes": "Common mistakes",
        "faq": "Frequently asked questions",
        "conclusion": "Conclusion",
        "recipe_why": "Why this recipe works",
        "recipe_oil": "Choosing the right oil",
        "recipe_method": "Technique and precision",
        "recipe_service": "Serving, pairings and variations",
        "recipe_mistakes": "Mistakes to avoid",
        "recipe_faq": "Frequently asked questions",
    },
    "it": {
        "updated": "Aggiornato",
        "read": "12 min di lettura",
        "short": "Risposta breve",
        "why": "Perche questo tema conta",
        "signals": "Segnali da controllare",
        "method": "Metodo pratico",
        "case": "Caso concreto",
        "mistakes": "Errori frequenti",
        "faq": "Domande frequenti",
        "conclusion": "Conclusione",
        "recipe_why": "Perche questa ricetta funziona",
        "recipe_oil": "Scegliere l'olio giusto",
        "recipe_method": "Tecnica e precisione",
        "recipe_service": "Servizio, abbinamenti e varianti",
        "recipe_mistakes": "Errori da evitare",
        "recipe_faq": "Domande frequenti",
    },
    "el": {
        "updated": "Ενημερώθηκε",
        "read": "12 λεπτά ανάγνωσης",
        "short": "Σύντομη απάντηση",
        "why": "Γιατί έχει σημασία",
        "signals": "Σήματα για έλεγχο",
        "method": "Πρακτική μέθοδος",
        "case": "Πρακτική περίπτωση",
        "mistakes": "Συχνά λάθη",
        "faq": "Συχνές ερωτήσεις",
        "conclusion": "Συμπέρασμα",
        "recipe_why": "Γιατί λειτουργεί η συνταγή",
        "recipe_oil": "Επιλογή σωστού λαδιού",
        "recipe_method": "Τεχνική και ακρίβεια",
        "recipe_service": "Σερβίρισμα, συνδυασμοί και παραλλαγές",
        "recipe_mistakes": "Λάθη προς αποφυγή",
        "recipe_faq": "Συχνές ερωτήσεις",
    },
}


GUIDE_COPY = {
    "fr": {
        "health": {
            "short": "{title} doit être compris comme un sujet d'équilibre : l'huile d'olive peut soutenir une alimentation de qualité, mais elle n'est jamais une promesse magique isolée.",
            "why": "Les sujets santé demandent plus de rigueur que les contenus ordinaires, car ils influencent parfois des décisions personnelles importantes. Un bon guide doit distinguer ce qui relève de la composition de l'huile, de l'usage culinaire, de la quantité consommée et du contexte global de l'alimentation. C'est cette nuance qui rend la page crédible.",
            "case": "Pour un lecteur qui cherche une huile au quotidien, la bonne décision consiste à choisir une vierge extra récente, à l'utiliser surtout en remplacement de graisses moins intéressantes, et à l'associer à des légumes, légumineuses, poissons, herbes et céréales. Le bénéfice vient du modèle alimentaire, pas d'un geste spectaculaire.",
        },
        "buying": {
            "short": "{title} devient utile quand il transforme le marketing en critères vérifiables : origine, récolte, catégorie, producteur, conservation et usage.",
            "why": "L'achat d'huile d'olive est souvent brouillé par des mots séduisants mais vagues : premium, authentique, tradition, sélection, goût méditerranéen. Un guide sérieux doit apprendre à regarder ce qui se prouve. Une huile lisible donne une date, une origine, une catégorie, parfois une variété, et un conditionnement qui protège le produit.",
            "case": "Devant deux bouteilles au même prix, le meilleur choix n'est pas forcément la plus belle étiquette. La bouteille sombre, datée, liée à un producteur identifiable et adaptée à votre usage mérite davantage confiance qu'une promesse large sans preuve.",
        },
        "cooking": {
            "short": "{title} doit relier le goût, la technique et le moment d'ajout de l'huile, car une bonne huile peut sublimer un plat ou l'écraser.",
            "why": "En cuisine, l'huile d'olive n'est pas une simple matière grasse. Elle porte les arômes, modifie la texture, donne une finale poivrée ou douce et change la perception du sel, de l'acidité et des herbes. Le bon contenu doit expliquer quand cuire avec l'huile, quand la garder pour la finition et comment l'accorder au plat.",
            "case": "Sur des légumes rôtis, une huile correcte peut servir à la cuisson, mais le filet le plus aromatique doit arriver à la sortie du four. Sur un dessert, l'huile doit être plus douce, récente et ronde, sinon elle prend toute la place.",
        },
        "production": {
            "short": "{title} mérite une lecture technique : terroir, variété, récolte, moulin et stockage décident ensemble de la qualité finale.",
            "why": "Les sujets de production deviennent intéressants lorsqu'ils relient paysage, gestes agricoles, contraintes climatiques et résultat en bouche. Une huile ne vient pas seulement d'un pays ou d'une tradition : elle vient d'olives récoltées à un moment précis, transportées rapidement, travaillées au moulin et protégées ensuite.",
            "case": "Deux huiles d'une même région peuvent être très différentes. Une récolte précoce donnera souvent plus d'amertume et de piquant, tandis qu'une récolte plus mûre sera plus ronde. Le moulin et la conservation peuvent amplifier ou ruiner ce potentiel.",
        },
        "beauty": {
            "short": "{title} doit rester précis : l'huile d'olive peut être utile en usage maison, mais le dosage, le type de peau ou de cheveux et les limites comptent autant que le produit.",
            "why": "Les usages beauté et maison attirent beaucoup de conseils rapides. Le contenu sérieux évite de dire que naturel signifie automatiquement adapté. Il explique les tests, les quantités, le rinçage, la conservation et les cas où il vaut mieux demander un avis professionnel.",
            "case": "Une petite quantité sur des pointes sèches peut donner de la souplesse, alors qu'une application généreuse sur cheveux fins peut alourdir. Sur la peau, un test local est plus responsable qu'une application directe sur tout le visage.",
        },
    },
    "en": {
        "health": {
            "short": "{title} should be read as a question of balance: olive oil can support a strong diet, but it is not an isolated miracle promise.",
            "why": "Health topics need more rigor than ordinary lifestyle content because they can influence important personal decisions. A serious guide separates the oil's composition, culinary use, quantity and the wider diet. That nuance is what makes the page trustworthy.",
            "case": "For everyday use, the sound choice is a recent extra virgin oil used mostly to replace less interesting fats and paired with vegetables, legumes, fish, herbs and grains. The value comes from the pattern, not from a spectacular gesture.",
        },
        "buying": {
            "short": "{title} becomes useful when it turns marketing into verifiable criteria: origin, harvest, category, producer, storage and use.",
            "why": "Buying olive oil is often blurred by attractive words: premium, authentic, traditional, selected, Mediterranean taste. A serious guide teaches the reader to look for proof. A readable oil gives a date, an origin, a category, sometimes a variety, and packaging that protects the product.",
            "case": "Between two bottles at the same price, the best choice is not always the prettiest label. A dark, dated bottle linked to an identifiable producer and adapted to your use deserves more trust than a broad promise without proof.",
        },
        "cooking": {
            "short": "{title} should connect flavor, technique and timing, because a good oil can lift a dish or overpower it.",
            "why": "In cooking, olive oil is not just fat. It carries aroma, changes texture, gives a peppery or soft finish and alters how salt, acidity and herbs are perceived. Useful content explains when to cook with it, when to keep it for finishing and how to pair it with the plate.",
            "case": "On roasted vegetables, a reliable oil can be used for cooking, but the most aromatic oil should be added after the oven. In desserts, the oil should be mild, fresh and round, otherwise it dominates.",
        },
        "production": {
            "short": "{title} deserves a technical reading: terroir, variety, harvest, mill and storage all decide final quality.",
            "why": "Production topics become interesting when they connect landscape, farming choices, climate pressure and taste. An oil does not come only from a country or tradition; it comes from fruit picked at a moment, transported fast, milled carefully and protected afterwards.",
            "case": "Two oils from the same region can be very different. Early harvest often gives more bitterness and pepper, while riper harvests feel rounder. Milling and storage can amplify or destroy that potential.",
        },
        "beauty": {
            "short": "{title} must stay precise: olive oil can help in home use, but dosage, skin or hair type and limits matter as much as the product.",
            "why": "Beauty and home uses attract many quick tips. Serious content avoids saying natural means automatically suitable. It explains patch tests, quantities, rinsing, storage and situations where professional advice is wiser.",
            "case": "A small amount on dry ends can add softness, while a generous application on fine hair can weigh it down. On skin, a small patch test is more responsible than applying it directly to the whole face.",
        },
    },
    "it": {
        "health": {
            "short": "{title} va letto come tema di equilibrio: l'olio d'oliva puo sostenere una buona alimentazione, ma non e una promessa miracolosa isolata.",
            "why": "I temi salute richiedono piu rigore dei contenuti ordinari, perche possono influenzare decisioni personali importanti. Una guida seria distingue composizione dell'olio, uso culinario, quantita e dieta complessiva. Questa sfumatura rende la pagina affidabile.",
            "case": "Per l'uso quotidiano, la scelta solida e un extravergine recente usato per sostituire grassi meno interessanti e abbinato a verdure, legumi, pesce, erbe e cereali. Il valore viene dal modello, non dal gesto spettacolare.",
        },
        "buying": {
            "short": "{title} diventa utile quando trasforma il marketing in criteri verificabili: origine, raccolta, categoria, produttore, conservazione e uso.",
            "why": "L'acquisto dell'olio e spesso confuso da parole seducenti: premium, autentico, tradizionale, selezionato, gusto mediterraneo. Una guida seria insegna a cercare prove. Un olio leggibile offre data, origine, categoria, talvolta varieta e confezione protettiva.",
            "case": "Tra due bottiglie allo stesso prezzo, la scelta migliore non e sempre l'etichetta piu bella. Una bottiglia scura, datata, legata a un produttore chiaro e adatta all'uso merita piu fiducia di una promessa vaga.",
        },
        "cooking": {
            "short": "{title} deve collegare gusto, tecnica e momento di aggiunta dell'olio, perche un buon olio puo elevare o coprire un piatto.",
            "why": "In cucina, l'olio d'oliva non e solo grasso. Porta aroma, cambia texture, dona finale piccante o dolce e modifica percezione di sale, acidita ed erbe. Un contenuto utile spiega quando cuocerlo, quando usarlo a crudo e come abbinarlo.",
            "case": "Sulle verdure arrostite, un olio affidabile puo cuocere, ma quello piu aromatico deve arrivare dopo il forno. Nei dolci, l'olio deve essere dolce, fresco e rotondo, altrimenti domina.",
        },
        "production": {
            "short": "{title} merita una lettura tecnica: terroir, varieta, raccolta, frantoio e conservazione decidono insieme la qualita finale.",
            "why": "I temi produttivi diventano interessanti quando collegano paesaggio, scelte agricole, clima e gusto. Un olio non viene solo da un paese o da una tradizione; nasce da frutti raccolti in un momento, trasportati rapidamente, franti con cura e protetti dopo.",
            "case": "Due oli della stessa regione possono essere molto diversi. La raccolta precoce da spesso piu amaro e piccante, mentre quella matura e piu rotonda. Frantoio e conservazione possono amplificare o rovinare il potenziale.",
        },
        "beauty": {
            "short": "{title} deve restare preciso: l'olio d'oliva puo aiutare negli usi domestici, ma dose, pelle o capelli e limiti contano quanto il prodotto.",
            "why": "Bellezza e casa attirano molti consigli rapidi. Il contenuto serio evita di dire che naturale significa sempre adatto. Spiega test, quantita, risciacquo, conservazione e casi in cui e meglio chiedere un parere professionale.",
            "case": "Una piccola quantita sulle punte secche puo dare morbidezza, mentre un'applicazione generosa su capelli fini appesantisce. Sulla pelle, un test locale e piu responsabile dell'applicazione su tutto il viso.",
        },
    },
    "el": {
        "health": {
            "short": "Το {title} πρέπει να διαβαστεί ως θέμα ισορροπίας: το ελαιόλαδο στηρίζει καλή διατροφή, αλλά δεν είναι μεμονωμένη θαυματουργή υπόσχεση.",
            "why": "Τα θέματα υγείας χρειάζονται μεγαλύτερη αυστηρότητα, γιατί μπορούν να επηρεάσουν προσωπικές αποφάσεις. Ένας σοβαρός οδηγός ξεχωρίζει σύνθεση λαδιού, μαγειρική χρήση, ποσότητα και συνολικό διατροφικό πλαίσιο. Αυτή η λεπτότητα χτίζει εμπιστοσύνη.",
            "case": "Για καθημερινή χρήση, η σωστή επιλογή είναι πρόσφατο εξαιρετικό παρθένο λάδι που αντικαθιστά λιγότερο ενδιαφέροντα λίπη και συνοδεύει λαχανικά, όσπρια, ψάρι, βότανα και δημητριακά.",
        },
        "buying": {
            "short": "Το {title} γίνεται χρήσιμο όταν μετατρέπει το marketing σε ελέγξιμα κριτήρια: προέλευση, συγκομιδή, κατηγορία, παραγωγό, φύλαξη και χρήση.",
            "why": "Η αγορά ελαιολάδου μπερδεύεται συχνά από όμορφες λέξεις: premium, αυθεντικό, παραδοσιακό, επιλεγμένο, μεσογειακή γεύση. Σοβαρός οδηγός μαθαίνει τον αναγνώστη να ψάχνει αποδείξεις. Ένα καθαρό προϊόν δίνει ημερομηνία, προέλευση, κατηγορία, ίσως ποικιλία και προστατευμένη συσκευασία.",
            "case": "Ανάμεσα σε δύο φιάλες ίδιας τιμής, δεν κερδίζει πάντα η πιο όμορφη ετικέτα. Σκούρα, χρονολογημένη φιάλη με αναγνωρίσιμο παραγωγό και σαφή χρήση αξίζει περισσότερη εμπιστοσύνη.",
        },
        "cooking": {
            "short": "Το {title} πρέπει να συνδέει γεύση, τεχνική και στιγμή προσθήκης, γιατί ένα καλό λάδι μπορεί να σηκώσει ή να σκεπάσει ένα πιάτο.",
            "why": "Στην κουζίνα, το ελαιόλαδο δεν είναι απλώς λίπος. Μεταφέρει άρωμα, αλλάζει υφή, δίνει πικάντικο ή απαλό τελείωμα και επηρεάζει αλάτι, οξύτητα και βότανα. Χρήσιμο περιεχόμενο εξηγεί πότε μαγειρεύεται, πότε μπαίνει στο τέλος και πώς ταιριάζει.",
            "case": "Σε ψητά λαχανικά, ένα καλό λάδι μπορεί να μπει στο μαγείρεμα, αλλά το πιο αρωματικό μπαίνει μετά τον φούρνο. Σε γλυκά, το λάδι πρέπει να είναι ήπιο, φρέσκο και στρογγυλό.",
        },
        "production": {
            "short": "Το {title} αξίζει τεχνική ανάγνωση: τόπος, ποικιλία, συγκομιδή, ελαιοτριβείο και φύλαξη αποφασίζουν μαζί την ποιότητα.",
            "why": "Τα θέματα παραγωγής γίνονται ενδιαφέροντα όταν ενώνουν τοπίο, γεωργικές επιλογές, κλιματική πίεση και γεύση. Ένα λάδι δεν έρχεται μόνο από χώρα ή παράδοση· έρχεται από καρπό που μαζεύτηκε σε συγκεκριμένη στιγμή, μεταφέρθηκε γρήγορα, δουλεύτηκε σωστά και προστατεύτηκε.",
            "case": "Δύο λάδια της ίδιας περιοχής μπορεί να διαφέρουν πολύ. Πρώιμη συγκομιδή δίνει συχνά περισσότερη πίκρα και κάψιμο, ενώ πιο ώριμη συγκομιδή είναι πιο στρογγυλή. Ελαιοτριβείο και φύλαξη ενισχύουν ή καταστρέφουν το δυναμικό.",
        },
        "beauty": {
            "short": "Το {title} πρέπει να μένει ακριβές: το ελαιόλαδο μπορεί να βοηθήσει στο σπίτι, αλλά ποσότητα, τύπος δέρματος ή μαλλιών και όρια μετράνε όσο το προϊόν.",
            "why": "Η ομορφιά και οι οικιακές χρήσεις γεμίζουν με γρήγορες συμβουλές. Το σοβαρό περιεχόμενο δεν λέει ότι φυσικό σημαίνει πάντα κατάλληλο. Εξηγεί δοκιμές, ποσότητες, ξέβγαλμα, φύλαξη και πότε χρειάζεται ειδικός.",
            "case": "Μικρή ποσότητα στις ξηρές άκρες μπορεί να δώσει απαλότητα, ενώ πολύ λάδι σε λεπτά μαλλιά βαραίνει. Στο δέρμα, μικρή τοπική δοκιμή είναι πιο υπεύθυνη από εφαρμογή σε όλο το πρόσωπο.",
        },
    },
}


RECIPE_COPY = {
    "fr": {
        "why": "{title} réussit quand l'huile d'olive n'est pas ajoutée par habitude, mais parce qu'elle apporte une texture, une liaison et une finale aromatique. Le plat doit garder son identité tout en gagnant en longueur.",
        "oil": "Choisissez une huile selon l'intensité du plat : douce et ronde pour les desserts, les sauces délicates et les poissons ; plus verte et poivrée pour les légumes grillés, les légumineuses, les pains, les salades et les plats de caractère. Goûtez toujours l'huile seule avant de l'ajouter.",
        "method": "La précision compte davantage que la quantité. Ajoutez l'huile progressivement, surveillez l'acidité, salez après dégustation et gardez un dernier filet pour le service si la recette le permet. Ce geste final donne une impression plus fraîche et plus professionnelle.",
        "pro": "Une recette professionnelle donne au lecteur une décision claire : quel profil d'huile utiliser, à quel moment l'ajouter, comment corriger la texture et comment servir sans perdre les arômes.",
        "service": "Servez avec un contraste : herbes fraîches, citron, pain grillé, graines, fromage frais ou légumes croquants selon la recette. Une bonne variante ne change pas tout ; elle déplace un seul curseur, comme le fruité de l'huile ou l'acidité.",
        "mistakes": ["Utiliser une huile fatiguée ou stockée à la lumière.", "Ajouter toute l'huile trop tôt et perdre les arômes.", "Saler avant d'avoir goûté l'équilibre huile-acidité.", "Choisir une huile trop amère pour un plat délicat."],
        "faq_q": "Puis-je changer d'huile d'olive dans cette recette ?",
        "faq_a": "Oui, mais changez en fonction du résultat voulu : huile douce pour arrondir, huile verte pour réveiller, huile intense pour donner une finale plus gastronomique.",
    },
    "en": {
        "why": "{title} works when olive oil is not added by habit, but because it brings texture, binding power and an aromatic finish. The dish should keep its identity while gaining length.",
        "oil": "Choose the oil according to the dish: mild and round for desserts, delicate sauces and fish; greener and pepperier for grilled vegetables, legumes, breads, salads and stronger plates. Always taste the oil on its own first.",
        "method": "Precision matters more than quantity. Add the oil gradually, watch acidity, season after tasting and keep a final drizzle for serving when the recipe allows it. That last gesture gives a fresher, more professional impression.",
        "pro": "A professional recipe gives the reader clear decisions: which oil profile to use, when to add it, how to adjust texture and how to serve without losing aroma.",
        "service": "Serve with contrast: fresh herbs, lemon, toasted bread, seeds, fresh cheese or crunchy vegetables depending on the recipe. A good variation does not change everything; it moves one lever, such as oil fruitiness or acidity.",
        "mistakes": ["Using tired oil or oil stored in strong light.", "Adding all the oil too early and losing aroma.", "Seasoning before checking the oil-acidity balance.", "Choosing an oil that is too bitter for a delicate dish."],
        "faq_q": "Can I use another olive oil for this recipe?",
        "faq_a": "Yes, but choose according to the result: mild oil for roundness, green oil for freshness, intense oil for a more gastronomic finish.",
    },
    "it": {
        "why": "{title} funziona quando l'olio d'oliva non e aggiunto per abitudine, ma perche porta texture, legame e finale aromatico. Il piatto deve restare riconoscibile e guadagnare lunghezza.",
        "oil": "Scegliete l'olio secondo l'intensita: dolce e rotondo per dolci, salse delicate e pesce; piu verde e piccante per verdure grigliate, legumi, pane, insalate e piatti decisi. Assaggiatelo sempre da solo.",
        "method": "La precisione conta piu della quantita. Aggiungete l'olio gradualmente, controllate l'acidita, salate dopo l'assaggio e tenete un filo finale per il servizio quando possibile. Questo gesto rende il risultato piu fresco e professionale.",
        "pro": "Una ricetta professionale offre decisioni chiare: quale profilo d'olio usare, quando aggiungerlo, come correggere la texture e come servire senza perdere aromi.",
        "service": "Servite con contrasto: erbe fresche, limone, pane tostato, semi, formaggio fresco o verdure croccanti. Una buona variante non cambia tutto; sposta un solo cursore, come il fruttato dell'olio o l'acidita.",
        "mistakes": ["Usare un olio stanco o esposto alla luce.", "Aggiungere tutto l'olio troppo presto e perdere aromi.", "Salare prima di controllare equilibrio olio-acidita.", "Scegliere un olio troppo amaro per un piatto delicato."],
        "faq_q": "Posso cambiare olio d'oliva in questa ricetta?",
        "faq_a": "Si, ma scegliete in base al risultato: olio dolce per rotondita, olio verde per freschezza, olio intenso per un finale piu gastronomico.",
    },
    "el": {
        "why": "Το {title} πετυχαίνει όταν το ελαιόλαδο δεν μπαίνει από συνήθεια, αλλά επειδή δίνει υφή, δέσιμο και αρωματικό τελείωμα. Το πιάτο πρέπει να κρατά την ταυτότητά του και να κερδίζει διάρκεια.",
        "oil": "Επιλέξτε λάδι σύμφωνα με την ένταση: ήπιο και στρογγυλό για γλυκά, λεπτές σάλτσες και ψάρι· πιο πράσινο και πικάντικο για ψητά λαχανικά, όσπρια, ψωμί, σαλάτες και δυνατά πιάτα. Δοκιμάστε το πάντα μόνο του.",
        "method": "Η ακρίβεια μετρά περισσότερο από την ποσότητα. Προσθέστε το λάδι σταδιακά, ελέγξτε την οξύτητα, αλατίστε μετά τη δοκιμή και κρατήστε λίγο για το σερβίρισμα όταν γίνεται. Αυτό δίνει πιο φρέσκια και επαγγελματική εντύπωση.",
        "pro": "Μια επαγγελματική συνταγή δίνει καθαρές αποφάσεις: ποιο προφίλ λαδιού να χρησιμοποιηθεί, πότε να προστεθεί, πώς να διορθωθεί η υφή και πώς να σερβιριστεί χωρίς απώλεια αρώματος.",
        "service": "Σερβίρετε με αντίθεση: φρέσκα βότανα, λεμόνι, ψητό ψωμί, σπόρους, φρέσκο τυρί ή τραγανά λαχανικά. Καλή παραλλαγή δεν αλλάζει τα πάντα· μετακινεί έναν μόνο άξονα, όπως το φρουτώδες ή την οξύτητα.",
        "mistakes": ["Χρήση κουρασμένου λαδιού ή λαδιού εκτεθειμένου στο φως.", "Προσθήκη όλου του λαδιού πολύ νωρίς και απώλεια αρώματος.", "Αλάτισμα πριν ελεγχθεί η ισορροπία λαδιού-οξύτητας.", "Επιλογή υπερβολικά πικρού λαδιού για λεπτό πιάτο."],
        "faq_q": "Μπορώ να αλλάξω ελαιόλαδο σε αυτή τη συνταγή;",
        "faq_a": "Ναι, αλλά επιλέξτε ανάλογα με το αποτέλεσμα: ήπιο λάδι για στρογγυλότητα, πράσινο λάδι για φρεσκάδα, έντονο λάδι για πιο γαστρονομικό τελείωμα.",
    },
}


GUIDE_DEEP = {
    "fr": {
        "heading": "Lecture avancée et valeur de référence",
        "paragraphs": [
            "Pour être réellement utile, une page de référence doit répondre à deux niveaux de lecture. Le lecteur pressé doit comprendre vite la décision principale, tandis que le lecteur exigeant doit trouver les raisons, les limites et les critères qui justifient cette décision.",
            "C'est particulièrement important dans l'univers de l'huile d'olive, où beaucoup de contenus se ressemblent. Les mêmes mots reviennent partout : vierge extra, naturel, méditerranéen, qualité, tradition. La différence se fait quand le guide explique ce que ces mots changent concrètement dans le choix, la dégustation ou l'usage.",
            "Une bonne lecture consiste à relier le sujet à trois preuves : ce qui est visible sur l'étiquette, ce qui se vérifie en bouche, et ce qui se confirme dans l'utilisation réelle. Quand ces trois niveaux racontent la même histoire, le conseil devient beaucoup plus solide.",
            "Pour les moteurs de recherche et les assistants IA, cette organisation a aussi une valeur claire : elle donne une réponse directe, puis des critères nommés, puis un raisonnement réutilisable. La page devient plus facile à résumer parce qu'elle n'est pas seulement longue, elle est structurée.",
            "Le lecteur doit également comprendre quand le conseil ne s'applique pas. Une huile très intense n'est pas idéale pour tous les desserts, une huile très douce n'est pas toujours intéressante sur des légumes puissants, et un prix élevé ne remplace jamais une information précise.",
            "Cette approche donne de l'épaisseur au contenu sans le rendre confus. Chaque section doit aider à décider, comparer ou corriger une erreur fréquente. C'est ce qui transforme un petit article SEO en guide réellement consultable.",
            "La dernière étape consiste à donner au lecteur une action simple. Après la lecture, il doit pouvoir regarder une bouteille, choisir une méthode, éviter une erreur ou adapter son usage. Sans cette action, le contenu reste décoratif.",
            "Un bon guide accepte aussi la complexité du produit. La meilleure réponse dépend parfois de la saison, de la variété, de la fraîcheur, du niveau de cuisine du lecteur ou du budget. Nommer ces variables rend l'article plus fiable.",
            "C'est cette combinaison qui crée une vraie valeur éditoriale : pédagogie, décision, nuance et application concrète. Le contenu paraît alors écrit pour aider, pas seulement pour occuper une requête.",
        ],
        "checks": ["Comparer le sujet à un usage concret.", "Chercher les critères qui se prouvent.", "Identifier les limites du conseil.", "Relier goût, fraîcheur et conservation.", "Préférer une réponse nuancée à une promesse absolue."],
    },
    "en": {
        "heading": "Advanced Reading and Reference Value",
        "paragraphs": [
            "A truly useful reference page must serve two reading speeds. A hurried reader should understand the main decision quickly, while a demanding reader should find the reasons, limits and criteria that support that decision.",
            "This matters in olive oil because many pages repeat the same words: extra virgin, natural, Mediterranean, quality, tradition. The difference appears when the guide explains what those words change in buying, tasting or using the oil.",
            "A strong reading connects the topic to three kinds of proof: what appears on the label, what can be checked on the palate, and what is confirmed in real use. When those three levels tell the same story, the advice becomes much stronger.",
            "For search engines and AI assistants, this structure also matters: it gives a direct answer, named criteria and reusable reasoning. The page becomes easier to summarize because it is not only longer; it is organized.",
            "The reader should also understand when the advice does not apply. A very intense oil is not ideal for every dessert, a very mild oil is not always interesting on powerful vegetables, and a high price never replaces precise information.",
            "This approach adds depth without making the page confusing. Each section should help the reader decide, compare or correct a common mistake. That is what turns a small SEO article into a genuinely useful guide.",
            "The final step is to give the reader a simple action. After reading, they should be able to look at a bottle, choose a method, avoid a mistake or adapt the use. Without that action, the content stays decorative.",
            "A good guide also accepts the complexity of the product. The best answer can depend on season, variety, freshness, the reader's cooking level or budget. Naming those variables makes the article more reliable.",
            "That combination creates real editorial value: teaching, decision, nuance and concrete application. The content then feels written to help, not merely to occupy a search query.",
        ],
        "checks": ["Compare the topic with a real use case.", "Look for criteria that can be proven.", "Identify the limits of the advice.", "Connect taste, freshness and storage.", "Prefer nuance over absolute promises."],
    },
    "it": {
        "heading": "Lettura avanzata e valore di riferimento",
        "paragraphs": [
            "Una pagina di riferimento davvero utile deve servire due velocita di lettura. Il lettore frettoloso deve capire subito la decisione principale, mentre il lettore esigente deve trovare ragioni, limiti e criteri che la sostengono.",
            "Questo conta nell'olio d'oliva perche molte pagine ripetono le stesse parole: extravergine, naturale, mediterraneo, qualita, tradizione. La differenza appare quando la guida spiega cosa cambiano queste parole nell'acquisto, nella degustazione o nell'uso.",
            "Una lettura forte collega il tema a tre prove: cio che si vede in etichetta, cio che si verifica al palato e cio che si conferma nell'uso reale. Quando questi livelli raccontano la stessa storia, il consiglio diventa molto piu solido.",
            "Per motori di ricerca e assistenti IA, questa struttura conta: offre risposta diretta, criteri nominati e ragionamento riutilizzabile. La pagina diventa piu facile da riassumere perche non e solo lunga, e organizzata.",
            "Il lettore deve anche capire quando il consiglio non si applica. Un olio molto intenso non e ideale per tutti i dolci, un olio molto dolce non e sempre interessante su verdure potenti, e un prezzo alto non sostituisce informazioni precise.",
            "Questo approccio aggiunge profondita senza rendere la pagina confusa. Ogni sezione deve aiutare a decidere, confrontare o correggere un errore comune. Cosi un piccolo articolo SEO diventa una guida davvero utile.",
            "L'ultimo passaggio e dare al lettore un'azione semplice. Dopo la lettura deve poter guardare una bottiglia, scegliere un metodo, evitare un errore o adattare l'uso. Senza questa azione, il contenuto resta decorativo.",
            "Una buona guida accetta anche la complessita del prodotto. La risposta migliore dipende da stagione, varieta, freschezza, livello di cucina del lettore o budget. Nominare queste variabili rende l'articolo piu affidabile.",
            "Questa combinazione crea valore editoriale reale: pedagogia, decisione, sfumatura e applicazione concreta. Il contenuto sembra scritto per aiutare, non solo per occupare una ricerca.",
        ],
        "checks": ["Confrontare il tema con un uso concreto.", "Cercare criteri dimostrabili.", "Identificare i limiti del consiglio.", "Collegare gusto, freschezza e conservazione.", "Preferire la sfumatura alle promesse assolute."],
    },
    "el": {
        "heading": "Προχωρημένη ανάγνωση και αξία αναφοράς",
        "paragraphs": [
            "Μια πραγματικά χρήσιμη σελίδα αναφοράς πρέπει να εξυπηρετεί δύο ρυθμούς ανάγνωσης. Ο βιαστικός αναγνώστης πρέπει να καταλαβαίνει γρήγορα την κύρια απόφαση, ενώ ο απαιτητικός αναγνώστης πρέπει να βρίσκει λόγους, όρια και κριτήρια.",
            "Αυτό έχει σημασία στο ελαιόλαδο, γιατί πολλά κείμενα επαναλαμβάνουν τις ίδιες λέξεις: εξαιρετικό παρθένο, φυσικό, μεσογειακό, ποιότητα, παράδοση. Η διαφορά φαίνεται όταν ο οδηγός εξηγεί τι αλλάζουν αυτές οι λέξεις στην αγορά, στη δοκιμή ή στη χρήση.",
            "Μια δυνατή ανάγνωση συνδέει το θέμα με τρεις αποδείξεις: τι φαίνεται στην ετικέτα, τι ελέγχεται στο στόμα και τι επιβεβαιώνεται στην πραγματική χρήση. Όταν αυτά τα επίπεδα λένε την ίδια ιστορία, η συμβουλή γίνεται πολύ πιο σταθερή.",
            "Για μηχανές αναζήτησης και βοηθούς τεχνητής νοημοσύνης, αυτή η δομή μετράει επίσης: δίνει άμεση απάντηση, ονομασμένα κριτήρια και συλλογισμό που μπορεί να επαναχρησιμοποιηθεί. Η σελίδα γίνεται πιο εύκολη στη σύνοψη επειδή δεν είναι μόνο μακρύτερη, είναι οργανωμένη.",
            "Ο αναγνώστης πρέπει επίσης να καταλαβαίνει πότε η συμβουλή δεν εφαρμόζεται. Ένα πολύ έντονο λάδι δεν ταιριάζει σε κάθε γλυκό, ένα πολύ ήπιο λάδι δεν έχει πάντα ενδιαφέρον σε δυνατά λαχανικά, και υψηλή τιμή δεν αντικαθιστά συγκεκριμένη πληροφορία.",
            "Αυτή η προσέγγιση προσθέτει βάθος χωρίς να μπερδεύει. Κάθε ενότητα πρέπει να βοηθά σε απόφαση, σύγκριση ή διόρθωση συχνού λάθους. Έτσι ένα μικρό SEO άρθρο γίνεται πραγματικά χρήσιμος οδηγός.",
            "Το τελευταίο βήμα είναι μια απλή ενέργεια για τον αναγνώστη. Μετά την ανάγνωση πρέπει να μπορεί να κοιτάξει μια φιάλη, να διαλέξει μέθοδο, να αποφύγει λάθος ή να προσαρμόσει χρήση. Χωρίς αυτή την ενέργεια, το περιεχόμενο μένει διακοσμητικό.",
            "Ένας καλός οδηγός δέχεται και την πολυπλοκότητα του προϊόντος. Η καλύτερη απάντηση εξαρτάται από εποχή, ποικιλία, φρεσκάδα, επίπεδο μαγειρικής ή budget. Όταν αυτές οι μεταβλητές ονομάζονται, το άρθρο γίνεται πιο αξιόπιστο.",
            "Αυτός ο συνδυασμός δημιουργεί πραγματική εκδοτική αξία: εκπαίδευση, απόφαση, λεπτότητα και πρακτική εφαρμογή. Το περιεχόμενο φαίνεται γραμμένο για βοήθεια, όχι απλώς για αναζήτηση.",
        ],
        "checks": ["Σύγκριση του θέματος με πραγματική χρήση.", "Αναζήτηση κριτηρίων που αποδεικνύονται.", "Εντοπισμός ορίων της συμβουλής.", "Σύνδεση γεύσης, φρεσκάδας και φύλαξης.", "Προτίμηση στη λεπτότητα αντί για απόλυτες υποσχέσεις."],
    },
}


RECIPE_DEEP = {
    "fr": {
        "heading": "Repères de chef pour aller plus loin",
        "paragraphs": [
            "Le meilleur résultat vient souvent d'un détail très simple : goûter à chaque étape. Goûtez la base avant l'huile, puis après l'huile, puis après l'acidité. Cette progression montre immédiatement si le plat gagne en rondeur, en fraîcheur ou en lourdeur.",
            "La température compte aussi. Une préparation froide bloque parfois les arômes, tandis qu'une assiette trop chaude peut les écraser. Pour une huile de finition, servez tiède ou à température ambiante quand c'est possible.",
            "La texture donne le dernier signal. Si le plat paraît gras, il manque souvent d'acidité, d'herbes ou de croquant. Si le plat paraît plat, un filet d'huile plus verte ou une pointe de citron peut suffire à le réveiller.",
            "Enfin, notez le résultat pour la prochaine fois : huile utilisée, quantité, moment d'ajout et correction finale. Cette petite mémoire transforme une recette simple en méthode fiable que l'on peut répéter et améliorer.",
            "Cette logique rend la recette plus sérieuse pour le lecteur : elle n'impose pas seulement des étapes, elle apprend à comprendre le rôle de l'huile d'olive dans l'équilibre final.",
        ],
    },
    "en": {
        "heading": "Chef-Level Notes to Go Further",
        "paragraphs": [
            "The best result often comes from one simple habit: tasting at every stage. Taste the base before the oil, after the oil and after the acidity. That progression shows whether the dish gains roundness, freshness or heaviness.",
            "Temperature matters too. A very cold preparation can block aromas, while a plate that is too hot can flatten them. For finishing oil, serve warm or at room temperature whenever possible.",
            "Texture gives the final signal. If the dish feels greasy, it often needs acidity, herbs or crunch. If it feels flat, a greener oil or a touch of lemon may be enough to wake it up.",
            "Finally, note the result for next time: oil used, quantity, moment of addition and final adjustment. This small memory turns a simple recipe into a reliable method that can be repeated and improved.",
            "This makes the recipe more serious for the reader: it does not only list steps, it teaches how olive oil shapes the final balance.",
        ],
    },
    "it": {
        "heading": "Riferimenti da chef per andare oltre",
        "paragraphs": [
            "Il risultato migliore nasce spesso da un gesto semplice: assaggiare a ogni fase. Assaggiate la base prima dell'olio, dopo l'olio e dopo l'acidita. Questa progressione mostra se il piatto guadagna rotondita, freschezza o pesantezza.",
            "Conta anche la temperatura. Una preparazione troppo fredda blocca gli aromi, mentre un piatto troppo caldo li schiaccia. Per l'olio di finitura, servite tiepido o a temperatura ambiente quando possibile.",
            "La texture offre l'ultimo segnale. Se il piatto sembra grasso, spesso mancano acidita, erbe o croccantezza. Se sembra piatto, un olio piu verde o una punta di limone possono bastare.",
            "Infine, annotate il risultato per la volta successiva: olio usato, quantita, momento di aggiunta e correzione finale. Questa piccola memoria trasforma una ricetta semplice in metodo affidabile.",
            "Questa logica rende la ricetta piu seria: non elenca soltanto passaggi, ma insegna a capire il ruolo dell'olio d'oliva nell'equilibrio finale.",
            "Il risultato diventa piu costante e piu facile da spiegare.",
        ],
    },
    "el": {
        "heading": "Σημεία σεφ για περισσότερη ακρίβεια",
        "paragraphs": [
            "Το καλύτερο αποτέλεσμα έρχεται συχνά από μια απλή συνήθεια: δοκιμή σε κάθε στάδιο. Δοκιμάστε τη βάση πριν το λάδι, μετά το λάδι και μετά την οξύτητα. Έτσι φαίνεται αν το πιάτο κερδίζει στρογγυλότητα, φρεσκάδα ή βάρος.",
            "Μετράει και η θερμοκρασία. Μια πολύ κρύα παρασκευή μπλοκάρει αρώματα, ενώ ένα πολύ ζεστό πιάτο τα ισοπεδώνει. Για λάδι τελειώματος, σερβίρετε χλιαρό ή σε θερμοκρασία δωματίου όταν γίνεται.",
            "Η υφή δίνει το τελικό σήμα. Αν το πιάτο φαίνεται λιπαρό, συχνά λείπει οξύτητα, βότανα ή τραγανότητα. Αν φαίνεται επίπεδο, ένα πιο πράσινο λάδι ή λίγο λεμόνι μπορεί να αρκεί.",
            "Τέλος, σημειώστε το αποτέλεσμα για την επόμενη φορά: λάδι που χρησιμοποιήθηκε, ποσότητα, στιγμή προσθήκης και τελική διόρθωση. Αυτή η μικρή μνήμη κάνει μια απλή συνταγή αξιόπιστη μέθοδο.",
            "Αυτή η λογική κάνει τη συνταγή πιο σοβαρή για τον αναγνώστη: δεν δίνει μόνο βήματα, αλλά εξηγεί τον ρόλο του ελαιολάδου στην τελική ισορροπία.",
        ],
    },
}


def read(path):
    return path.read_text(encoding="utf-8")


def write(path, text):
    path.write_text(text, encoding="utf-8")


def esc(value):
    return html.escape(value, quote=True)


def infer_lang_from_name(name):
    for suffix, lang in [("-fr.html", "fr"), ("-en.html", "en"), ("-it.html", "it"), ("-el.html", "el")]:
        if name.endswith(suffix):
            return lang
    return None


def parse_lang(text, fallback="fr"):
    match = re.search(r'<html lang="([^"]+)"', text)
    return match.group(1) if match else fallback


def ensure_html_lang(text, lang):
    if re.search(r"<html(?:\s|>)", text):
        if re.search(r'<html\s+lang="[^"]+"', text):
            return re.sub(r'<html\s+lang="[^"]+"', f'<html lang="{lang}"', text, count=1)
        return re.sub(r"<html(\s*)>", f'<html lang="{lang}">', text, count=1)
    return text


def parse_title(text, fallback):
    match = re.search(r"<h1>([\s\S]*?)</h1>", text)
    if not match:
        match = re.search(r"<title>([\s\S]*?)(?:—|-|&mdash;)", text)
    if not match:
        return fallback
    return html.unescape(re.sub(r"<.*?>", "", match.group(1))).strip()


def strip_block(text, mark):
    start, end = mark
    return re.sub(rf"\n?\s*{re.escape(start)}[\s\S]*?{re.escape(end)}\s*\n?", "\n", text)


def category_for(name, title):
    slug = f"{name} {title}".lower()
    if any(x in slug for x in ["sante", "santé", "health", "salute", "igia", "cardiaque", "heart", "coeur", "cœur", "oleique", "oleic", "polyphen", "acidite", "acide", "nutrition", "cholesterol"]):
        return "health"
    if any(x in slug for x in ["choisir", "choose", "scegliere", "etiquette", "label", "prix", "price", "prezzo", "certification", "bio", "aop", "dop", "conservation", "storage", "market", "marche"]):
        return "buying"
    if any(x in slug for x in ["cuisin", "cook", "cucin", "frire", "fry", "recette", "recipe", "marinade", "degust", "tasting", "goût", "gout"]):
        return "cooking"
    if any(x in slug for x in ["beaute", "beaut", "skin", "peau", "cheveux", "hair", "soap", "savon", "sapone"]):
        return "beauty"
    return "production"


def guide_extension(lang, title, category):
    labels = LANG[lang]
    copy = GUIDE_COPY[lang][category]
    signals = {
        "fr": ["Origine lisible et cohérente.", "Date ou contexte de récolte.", "Usage final clairement expliqué.", "Limites et exceptions assumées.", "Conseil applicable sans jargon."],
        "en": ["Clear and coherent origin.", "Harvest date or production context.", "Final use explained clearly.", "Limits and exceptions acknowledged.", "Advice that can be applied without jargon."],
        "it": ["Origine chiara e coerente.", "Data o contesto di raccolta.", "Uso finale spiegato chiaramente.", "Limiti ed eccezioni dichiarati.", "Consiglio applicabile senza gergo."],
        "el": ["Σαφής και συνεπής προέλευση.", "Ημερομηνία ή πλαίσιο συγκομιδής.", "Τελική χρήση εξηγημένη καθαρά.", "Όρια και εξαιρέσεις δηλωμένα.", "Συμβουλή εφαρμόσιμη χωρίς ορολογία."],
    }[lang]
    method = {
        "fr": ["Identifier le contexte réel du lecteur.", "Comparer au moins deux situations d'usage.", "Vérifier les preuves visibles sur le produit.", "Relier le conseil au goût ou au résultat attendu.", "Décider seulement après avoir croisé les signaux."],
        "en": ["Identify the reader's real context.", "Compare at least two use situations.", "Check visible proof on the product.", "Connect the advice to flavor or expected result.", "Decide only after combining several signals."],
        "it": ["Identificare il contesto reale del lettore.", "Confrontare almeno due situazioni d'uso.", "Controllare le prove visibili sul prodotto.", "Collegare il consiglio al gusto o al risultato.", "Decidere solo dopo aver incrociato piu segnali."],
        "el": ["Εντοπίστε το πραγματικό πλαίσιο του αναγνώστη.", "Συγκρίνετε τουλάχιστον δύο χρήσεις.", "Ελέγξτε ορατές αποδείξεις στο προϊόν.", "Συνδέστε τη συμβουλή με γεύση ή αποτέλεσμα.", "Αποφασίστε αφού συνδυάσετε πολλά σήματα."],
    }[lang]
    mistakes = {
        "fr": ["Répéter un argument marketing sans preuve.", "Donner une règle unique pour tous les usages.", "Oublier la conservation après l'achat.", "Confondre prix, origine et qualité réelle."],
        "en": ["Repeating marketing language without proof.", "Giving one rule for every use.", "Forgetting storage after purchase.", "Confusing price, origin and real quality."],
        "it": ["Ripetere marketing senza prove.", "Dare una regola unica per tutti gli usi.", "Dimenticare la conservazione dopo l'acquisto.", "Confondere prezzo, origine e qualita reale."],
        "el": ["Επανάληψη marketing χωρίς απόδειξη.", "Ένας κανόνας για όλες τις χρήσεις.", "Λησμονιά φύλαξης μετά την αγορά.", "Σύγχυση τιμής, προέλευσης και πραγματικής ποιότητας."],
    }[lang]
    signal_html = "\n".join(f"            <li>{esc(item)}</li>" for item in signals)
    method_html = "\n".join(f"            <li>{esc(item)}</li>" for item in method)
    mistake_html = "\n".join(f"            <li>{esc(item)}</li>" for item in mistakes)
    deep = GUIDE_DEEP[lang]
    deep_paragraphs = "\n".join(f"        <p>{esc(item)}</p>" for item in deep["paragraphs"])
    deep_checks = "\n".join(f"            <li>{esc(item)}</li>" for item in deep["checks"])
    return f"""
        {GUIDE_MARK[0]}
        <div class="callout"><strong>{esc(labels["short"])} :</strong> {esc(copy["short"].format(title=title))}</div>

        <h2>{esc(labels["why"])}</h2>
        <p>{esc(copy["why"])}</p>
        <p>{esc(title)} ne doit donc pas rester une définition courte. La page doit aider à choisir, goûter, comparer, cuisiner ou comprendre avec assez de précision pour éviter une nouvelle recherche immédiate.</p>

        <h2>{esc(labels["signals"])}</h2>
        <p>{esc(copy["case"])}</p>
        <ul>
{signal_html}
        </ul>

        <h2>{esc(labels["method"])}</h2>
        <p>Une bonne méthode réduit le flou. Elle transforme un sujet large en décision concrète, vérifiable et utile dans la cuisine, en boutique ou au moment de comparer deux huiles.</p>
        <ol>
{method_html}
        </ol>

        <h2>{esc(labels["case"])}</h2>
        <p>Le bon réflexe consiste à partir de l'usage réel. Une huile de finition, une huile de cuisson, une huile cadeau ou une huile étudiée pour ses qualités sensorielles ne demandent pas les mêmes critères. Le contenu devient professionnel quand il explique cette différence au lieu de donner une réponse unique.</p>

        <h2>{esc(labels["mistakes"])}</h2>
        <ul>
{mistake_html}
        </ul>

        <h2>{esc(labels["faq"])}</h2>
        <h3>{esc(title)} suffit-il pour choisir une huile ?</h3>
        <p>Non, le sujet donne un cadre, mais la décision finale doit croiser l'étiquette, la fraîcheur, le stockage, le goût et l'usage prévu. C'est ce croisement qui rend le choix fiable.</p>
        <h3>Quel est le signe le plus sérieux ?</h3>
        <p>La cohérence. Quand le discours, l'origine, la date, le prix, le goût et la conservation racontent la même histoire, le produit inspire davantage confiance.</p>

        <h2>{esc(labels["conclusion"])}</h2>
        <p>Un guide utile sur l'huile d'olive doit être clair, nuancé et actionnable. Il ne cherche pas seulement à remplir une page : il donne au lecteur une méthode pour reconnaître la qualité, éviter les pièges et utiliser le produit avec plus de justesse.</p>

        <h2>{esc(deep["heading"])}</h2>
{deep_paragraphs}
        <ul>
{deep_checks}
        </ul>
        {GUIDE_MARK[1]}
"""


def localized_guide_extension(lang, title, category):
    block = guide_extension(lang, title, category)
    if lang == "fr":
        return block
    replacements = {
        "en": {
            "ne doit donc pas rester une définition courte. La page doit aider à choisir, goûter, comparer, cuisiner ou comprendre avec assez de précision pour éviter une nouvelle recherche immédiate.": "should not remain a short definition. The page should help the reader choose, taste, compare, cook or understand with enough precision to avoid an immediate second search.",
            "Une bonne méthode réduit le flou. Elle transforme un sujet large en décision concrète, vérifiable et utile dans la cuisine, en boutique ou au moment de comparer deux huiles.": "A good method reduces vagueness. It turns a broad topic into a concrete, verifiable decision that is useful in the kitchen, in a shop or when comparing two oils.",
            "Le bon réflexe consiste à partir de l'usage réel. Une huile de finition, une huile de cuisson, une huile cadeau ou une huile étudiée pour ses qualités sensorielles ne demandent pas les mêmes critères. Le contenu devient professionnel quand il explique cette différence au lieu de donner une réponse unique.": "The right reflex is to start from the real use. A finishing oil, a cooking oil, a gift oil or an oil chosen for sensory qualities do not require the same criteria. Content becomes professional when it explains that difference instead of giving one universal answer.",
            "suffit-il pour choisir une huile ?": "enough to choose an oil?",
            "Non, le sujet donne un cadre, mais la décision finale doit croiser l'étiquette, la fraîcheur, le stockage, le goût et l'usage prévu. C'est ce croisement qui rend le choix fiable.": "No. The topic gives a framework, but the final decision must combine label, freshness, storage, taste and intended use. That combination makes the choice reliable.",
            "Quel est le signe le plus sérieux ?": "What is the most serious signal?",
            "La cohérence. Quand le discours, l'origine, la date, le prix, le goût et la conservation racontent la même histoire, le produit inspire davantage confiance.": "Coherence. When the explanation, origin, date, price, taste and storage tell the same story, the product feels more trustworthy.",
            "Un guide utile sur l'huile d'olive doit être clair, nuancé et actionnable. Il ne cherche pas seulement à remplir une page : il donne au lecteur une méthode pour reconnaître la qualité, éviter les pièges et utiliser le produit avec plus de justesse.": "A useful olive oil guide must be clear, nuanced and actionable. It does not merely fill a page: it gives the reader a method to recognize quality, avoid traps and use the product with more accuracy.",
        },
        "it": {
            "ne doit donc pas rester une définition courte. La page doit aider à choisir, goûter, comparer, cuisiner ou comprendre avec assez de précision pour éviter une nouvelle recherche immédiate.": "non deve restare una definizione breve. La pagina deve aiutare a scegliere, assaggiare, confrontare, cucinare o capire con abbastanza precisione da evitare una nuova ricerca immediata.",
            "Une bonne méthode réduit le flou. Elle transforme un sujet large en décision concrète, vérifiable et utile dans la cuisine, en boutique ou au moment de comparer deux huiles.": "Un buon metodo riduce il vago. Trasforma un tema ampio in una decisione concreta, verificabile e utile in cucina, in negozio o quando si confrontano due oli.",
            "Le bon réflexe consiste à partir de l'usage réel. Une huile de finition, une huile de cuisson, une huile cadeau ou une huile étudiée pour ses qualités sensorielles ne demandent pas les mêmes critères. Le contenu devient professionnel quand il explique cette différence au lieu de donner une réponse unique.": "Il riflesso giusto e partire dall'uso reale. Un olio di finitura, da cottura, da regalo o scelto per qualita sensoriali non richiede gli stessi criteri. Il contenuto diventa professionale quando spiega questa differenza.",
            "suffit-il pour choisir une huile ?": "basta per scegliere un olio?",
            "Non, le sujet donne un cadre, mais la décision finale doit croiser l'étiquette, la fraîcheur, le stockage, le goût et l'usage prévu. C'est ce croisement qui rend le choix fiable.": "No. Il tema offre un quadro, ma la decisione finale deve incrociare etichetta, freschezza, conservazione, gusto e uso previsto. Questo incrocio rende affidabile la scelta.",
            "Quel est le signe le plus sérieux ?": "Qual e il segnale piu serio?",
            "La cohérence. Quand le discours, l'origine, la date, le prix, le goût et la conservation racontent la même histoire, le produit inspire davantage confiance.": "La coerenza. Quando discorso, origine, data, prezzo, gusto e conservazione raccontano la stessa storia, il prodotto ispira piu fiducia.",
            "Un guide utile sur l'huile d'olive doit être clair, nuancé et actionnable. Il ne cherche pas seulement à remplir une page : il donne au lecteur une méthode pour reconnaître la qualité, éviter les pièges et utiliser le produit avec plus de justesse.": "Una guida utile sull'olio d'oliva deve essere chiara, sfumata e pratica. Non riempie soltanto una pagina: offre un metodo per riconoscere qualita, evitare trappole e usare il prodotto con piu precisione.",
        },
        "el": {
            "ne doit donc pas rester une définition courte. La page doit aider à choisir, goûter, comparer, cuisiner ou comprendre avec assez de précision pour éviter une nouvelle recherche immédiate.": "δεν πρέπει να μένει σύντομος ορισμός. Η σελίδα πρέπει να βοηθά στην επιλογή, δοκιμή, σύγκριση, μαγειρική ή κατανόηση με αρκετή ακρίβεια ώστε να μην χρειάζεται αμέσως νέα αναζήτηση.",
            "Une bonne méthode réduit le flou. Elle transforme un sujet large en décision concrète, vérifiable et utile dans la cuisine, en boutique ou au moment de comparer deux huiles.": "Μια καλή μέθοδος μειώνει την ασάφεια. Μετατρέπει ένα μεγάλο θέμα σε συγκεκριμένη, ελέγξιμη απόφαση χρήσιμη στην κουζίνα, στο κατάστημα ή στη σύγκριση δύο λαδιών.",
            "Le bon réflexe consiste à partir de l'usage réel. Une huile de finition, une huile de cuisson, une huile cadeau ou une huile étudiée pour ses qualités sensorielles ne demandent pas les mêmes critères. Le contenu devient professionnel quand il explique cette différence au lieu de donner une réponse unique.": "Το σωστό ξεκίνημα είναι η πραγματική χρήση. Λάδι τελειώματος, μαγειρέματος, δώρου ή γευσιγνωσίας δεν ζητούν τα ίδια κριτήρια. Το περιεχόμενο γίνεται επαγγελματικό όταν εξηγεί αυτή τη διαφορά.",
            "suffit-il pour choisir une huile ?": "αρκεί για επιλογή λαδιού;",
            "Non, le sujet donne un cadre, mais la décision finale doit croiser l'étiquette, la fraîcheur, le stockage, le goût et l'usage prévu. C'est ce croisement qui rend le choix fiable.": "Όχι. Το θέμα δίνει πλαίσιο, αλλά η τελική απόφαση συνδυάζει ετικέτα, φρεσκάδα, φύλαξη, γεύση και προβλεπόμενη χρήση. Αυτός ο συνδυασμός κάνει την επιλογή αξιόπιστη.",
            "Quel est le signe le plus sérieux ?": "Ποιο είναι το πιο σοβαρό σήμα;",
            "La cohérence. Quand le discours, l'origine, la date, le prix, le goût et la conservation racontent la même histoire, le produit inspire davantage confiance.": "Η συνέπεια. Όταν λόγος, προέλευση, ημερομηνία, τιμή, γεύση και φύλαξη λένε την ίδια ιστορία, το προϊόν εμπνέει περισσότερη εμπιστοσύνη.",
            "Un guide utile sur l'huile d'olive doit être clair, nuancé et actionnable. Il ne cherche pas seulement à remplir une page : il donne au lecteur une méthode pour reconnaître la qualité, éviter les pièges et utiliser le produit avec plus de justesse.": "Ένας χρήσιμος οδηγός για ελαιόλαδο πρέπει να είναι σαφής, λεπτός και εφαρμόσιμος. Δεν γεμίζει απλώς μια σελίδα: δίνει μέθοδο για αναγνώριση ποιότητας, αποφυγή παγίδων και σωστότερη χρήση.",
        },
    }
    for old, new in replacements.get(lang, {}).items():
        block = block.replace(old, new)
    return block


def recipe_extension(lang, title):
    labels = LANG[lang]
    copy = RECIPE_COPY[lang]
    mistakes = "\n".join(f"            <li>{esc(item)}</li>" for item in copy["mistakes"])
    deep = RECIPE_DEEP[lang]
    deep_paragraphs = "\n".join(f"        <p>{esc(item)}</p>" for item in deep["paragraphs"])
    return f"""
        {RECIPE_MARK[0]}
        <h2>{esc(labels["recipe_why"])}</h2>
        <p>{esc(copy["why"].format(title=title))}</p>
        <p>{esc(copy["pro"])}</p>

        <h2>{esc(labels["recipe_oil"])}</h2>
        <p>{esc(copy["oil"])}</p>

        <h2>{esc(labels["recipe_method"])}</h2>
        <p>{esc(copy["method"])}</p>

        <h2>{esc(labels["recipe_service"])}</h2>
        <p>{esc(copy["service"])}</p>

        <h2>{esc(labels["recipe_mistakes"])}</h2>
        <ul>
{mistakes}
        </ul>

        <h2>{esc(labels["recipe_faq"])}</h2>
        <h3>{esc(copy["faq_q"])}</h3>
        <p>{esc(copy["faq_a"])}</p>
        <h2>{esc(deep["heading"])}</h2>
{deep_paragraphs}
        {RECIPE_MARK[1]}
"""


def insert_before_article_end(text, block):
    if "</article>" in text:
        return text.replace("</article>", block + "\n    </article>", 1)
    if "</main>" in text:
        return text.replace("</main>", block + "\n</main>", 1)
    return text + block


def ensure_meta_description(text, description):
    if 'name="description"' in text:
        return text
    meta = f'    <meta name="description" content="{esc(description)}">\n'
    return text.replace("</head>", meta + "</head>", 1)


def ensure_guide_jsonld(text, path, lang, title, category):
    if '<script type="application/ld+json">' in text:
        return text
    data = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": f"{title}: guide expert sur l'huile d'olive, avec critères pratiques, méthode, erreurs et conseils d'usage.",
        "author": {"@type": "Organization", "name": "L'Or Vert"},
        "publisher": {"@type": "Organization", "name": "L'Or Vert", "url": SITE},
        "datePublished": "2026-05-04",
        "dateModified": "2026-05-04",
        "inLanguage": lang,
        "articleSection": category,
        "isAccessibleForFree": True,
        "mainEntityOfPage": f"{SITE}/guides/{path.name}",
    }
    script = f'    <script type="application/ld+json">{json.dumps(data, ensure_ascii=False, indent=2)}</script>\n'
    return text.replace("</head>", script + "</head>", 1)


def enhance_recipe_jsonld(text, path, lang, title):
    def repl(match):
        try:
            data = json.loads(match.group(1))
        except json.JSONDecodeError:
            return match.group(0)
        if data.get("@type") != "Recipe":
            return match.group(0)
        data["name"] = html.unescape(title)
        data["inLanguage"] = lang
        data["datePublished"] = data.get("datePublished", "2026-05-04")
        data["dateModified"] = "2026-05-04"
        data["recipeCategory"] = data.get("recipeCategory", "Mediterranean")
        data["keywords"] = data.get("keywords", ["olive oil", "extra virgin olive oil", "Mediterranean recipe", title])
        data["publisher"] = {"@type": "Organization", "name": "L'Or Vert", "url": SITE}
        data["mainEntityOfPage"] = f"{SITE}/recipes/{path.name}"
        return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False, indent=2)}</script>'
    return re.sub(r'<script type="application/ld\+json">([\s\S]*?)</script>', repl, text, count=1)


def improve_guides():
    changed = 0
    for path in sorted(GUIDES_DIR.glob("*.html")):
        text = strip_block(read(path), GUIDE_MARK)
        lang = infer_lang_from_name(path.name) or parse_lang(text, "fr")
        if lang not in LANG:
            continue
        text = ensure_html_lang(text, lang)
        title = parse_title(text, path.stem.replace("-", " ").title())
        category = category_for(path.name, title)
        block = localized_guide_extension(lang, title, category)
        description = f"{title}: guide expert huile d'olive avec méthode, critères, erreurs à éviter et conseils pratiques."
        text = ensure_meta_description(text, description)
        text = ensure_guide_jsonld(text, path, lang, title, category)
        text = insert_before_article_end(text, block)
        write(path, text)
        changed += 1
    return changed


def improve_recipes():
    changed = 0
    for path in sorted(RECIPES_DIR.glob("*.html")):
        text = strip_block(read(path), RECIPE_MARK)
        lang = infer_lang_from_name(path.name) or parse_lang(text, "fr")
        if lang not in LANG:
            continue
        text = ensure_html_lang(text, lang)
        title = parse_title(text, path.stem.replace("-", " ").title())
        block = recipe_extension(lang, title)
        text = enhance_recipe_jsonld(text, path, lang, title)
        text = insert_before_article_end(text, block)
        write(path, text)
        changed += 1
    return changed


def main():
    guides = improve_guides()
    recipes = improve_recipes()
    print(f"Improved {guides} guides and {recipes} recipes with long-form expert sections.")


if __name__ == "__main__":
    main()

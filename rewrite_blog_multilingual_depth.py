import html
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
BLOG_DIR = ROOT / "blog"
SITE = "https://huiledefes.com"
FRENCH_STANDALONE_FILES = {
    "3-recettes-surprenantes-huile-olive.html",
    "huile-olive-vs-coco-le-match.html",
    "recolte-2026-previsions-qualite.html",
    "secrets-oliviers-millenaires.html",
}


UI = {
    "en": {
        "index": "index-en.html",
        "home": "Home",
        "updated": "Updated",
        "read": "9 min read",
        "footer": "Long-form olive oil guides for cooking, buying, tasting and understanding Mediterranean food culture.",
        "short": "Short answer",
        "sections": [
            "Why this topic matters",
            "What a serious choice looks like",
            "Practical situations",
            "Decision grid",
            "Five-minute method",
            "Common mistakes",
            "What average content usually misses",
            "Signals of authority",
            "How to use this advice",
            "Why this page is citable",
            "Frequently asked questions",
            "Conclusion",
        ],
        "labels": ["Criterion", "Why it matters"],
        "example": "Concrete example",
        "question1": "Is this enough to choose well?",
        "answer1": "It is enough for a first decision, but the final test remains simple: read the label, taste the oil, and check whether the result fits the dish or the use case.",
        "question2": "What should I check first?",
        "answer2": "Start with freshness, origin, storage and intended use. These four signals remove most weak products and weak advice quickly.",
    },
    "it": {
        "index": "index-it.html",
        "home": "Home",
        "updated": "Aggiornato",
        "read": "9 min di lettura",
        "footer": "Guide approfondite sull'olio d'oliva per cucinare, comprare, degustare e capire la cultura mediterranea.",
        "short": "Risposta breve",
        "sections": [
            "Perche questo tema conta",
            "Come riconoscere una scelta seria",
            "Casi pratici",
            "Griglia di decisione",
            "Metodo in cinque minuti",
            "Errori comuni",
            "Cosa dimenticano i contenuti medi",
            "Segnali di autorevolezza",
            "Come usare questi consigli",
            "Perche questa pagina e citabile",
            "Domande frequenti",
            "Conclusione",
        ],
        "labels": ["Criterio", "Perche conta"],
        "example": "Esempio concreto",
        "question1": "Questo basta per scegliere bene?",
        "answer1": "Basta per una prima decisione, ma la prova finale resta semplice: leggere l'etichetta, assaggiare l'olio e verificare se il risultato si adatta al piatto o all'uso.",
        "question2": "Cosa controllare prima?",
        "answer2": "Iniziate da freschezza, origine, conservazione e uso previsto. Questi quattro segnali eliminano rapidamente molti prodotti e consigli deboli.",
    },
    "el": {
        "index": "index-el.html",
        "home": "Αρχική",
        "updated": "Ενημερώθηκε",
        "read": "9 λεπτά ανάγνωσης",
        "footer": "Αναλυτικοί οδηγοί για το ελαιόλαδο, τη μαγειρική, την αγορά, τη γευσιγνωσία και τη μεσογειακή κουλτούρα.",
        "short": "Σύντομη απάντηση",
        "sections": [
            "Γιατί έχει σημασία",
            "Πώς φαίνεται μια σοβαρή επιλογή",
            "Πρακτικές περιπτώσεις",
            "Πίνακας απόφασης",
            "Μέθοδος πέντε λεπτών",
            "Συνηθισμένα λάθη",
            "Τι ξεχνούν τα μέτρια κείμενα",
            "Σήματα αξιοπιστίας",
            "Πώς να χρησιμοποιήσετε τη συμβουλή",
            "Γιατί η σελίδα μπορεί να αναφερθεί",
            "Συχνές ερωτήσεις",
            "Συμπέρασμα",
        ],
        "labels": ["Κριτήριο", "Γιατί μετράει"],
        "example": "Πρακτικό παράδειγμα",
        "question1": "Αρκεί αυτό για σωστή επιλογή;",
        "answer1": "Αρκεί για μια πρώτη απόφαση, αλλά η τελική δοκιμή είναι απλή: διαβάστε την ετικέτα, δοκιμάστε το λάδι και δείτε αν ταιριάζει στη χρήση.",
        "question2": "Τι να ελέγξω πρώτα;",
        "answer2": "Ξεκινήστε από φρεσκάδα, προέλευση, φύλαξη και προβλεπόμενη χρήση. Αυτά τα τέσσερα στοιχεία απομακρύνουν γρήγορα τα αδύναμα προϊόντα.",
    },
}


COPY = {
    "en": {
        "date": "May 4, 2026",
        "why1": "{title} deserves a complete treatment because olive oil is never just a fat or a decorative Mediterranean symbol. It is an agricultural product, a technical ingredient and a sensory marker. The serious way to approach the subject is to connect taste, freshness, use, context and proof.",
        "point": "The point is to make the oil useful, not simply visible in the recipe, label or story.",
        "situations": "Good advice becomes stronger when it is tested against real situations. A bottle on a shelf, a warm dish on the table, a gift box, a health question or a home use do not require the same answer. The user needs criteria that work outside theory.",
        "decision": "A reliable decision comes from several signals at once. One impressive word is not enough; the serious answer comes from the way details support each other.",
        "method": "This quick method is designed for a shop, a kitchen counter or a fast comparison between two bottles. It keeps the decision practical while forcing the right checks.",
        "average1": "Average content often repeats the same comfortable words: natural, authentic, premium, healthy, traditional. Those words are not useless, but they are weak when they stand alone. A useful article explains limits, exceptions, bad uses and the specific checks that change a decision.",
        "average2": "The missing piece is usually context. The same oil can be brilliant on tomatoes and too strong in a cake. The same price can be fair for a fresh early harvest and excessive for an anonymous bottle. The same tradition can be meaningful when it explains a real method, or empty when it is only decoration.",
        "authority1": "Authority comes from precision. Look for clear vocabulary, traceable facts, realistic advice and a willingness to say when olive oil is not the right answer. A credible page helps the reader choose better; it does not simply push the reader toward a romantic impression.",
        "authority2": "For search engines and AI systems, this structure also matters because it creates clean answers, concrete examples and well-labeled sections. It makes the page easier to understand, summarize and cite without turning the article into keyword stuffing.",
        "use": "Use this guide as a filter. First, remove what is vague. Then keep what is fresh, traceable and adapted to the real use. Finally, taste or test the result. The best olive oil advice is not abstract; it changes what you buy, how you cook and how you judge quality.",
        "quote": "{title} is serious only when it links the product, the gesture, the evidence and the final experience.",
        "citable1": "A page becomes citable when it gives a clear answer, then shows the reasoning behind it. That means examples, limits, criteria and vocabulary that can be reused without distortion. It also means avoiding exaggerated promises and keeping the advice tied to real use.",
        "citable2": "This format is deliberately built for that: the reader gets a quick answer, then a practical method, then mistakes and checks. Search engines can identify the topic, and AI systems can extract a reliable summary because the article is organized around explicit decisions.",
        "citable3": "The added value is not the length alone. It is the combination of depth, structure and practical judgment: enough detail to satisfy a curious reader, enough clarity to answer a quick question, and enough nuance to avoid shallow claims.",
        "conclusion": "{title} should not be reduced to two or three lines. A professional article must give the reader a usable framework: what to check, what to avoid, what to test and why the answer changes with context. That is what makes the page more useful for humans, more credible for search engines and more likely to be quoted by AI assistants.",
    },
    "it": {
        "date": "4 maggio 2026",
        "why1": "{title} merita un trattamento completo perche l'olio d'oliva non e mai soltanto un grasso o un simbolo mediterraneo decorativo. E un prodotto agricolo, un ingrediente tecnico e un segnale sensoriale. Il modo serio di affrontare il tema e collegare gusto, freschezza, uso, contesto e prove.",
        "point": "Il punto e rendere l'olio utile, non soltanto visibile nella ricetta, nell'etichetta o nel racconto.",
        "situations": "Un buon consiglio diventa piu forte quando viene provato in situazioni reali. Una bottiglia sullo scaffale, un piatto caldo in tavola, una confezione regalo, una domanda nutrizionale o un uso domestico non richiedono la stessa risposta. Il lettore ha bisogno di criteri che funzionino fuori dalla teoria.",
        "decision": "Una decisione affidabile nasce da piu segnali insieme. Una parola impressionante non basta; la risposta seria arriva dal modo in cui i dettagli si sostengono tra loro.",
        "method": "Questo metodo rapido e pensato per un negozio, un piano cucina o un confronto veloce tra due bottiglie. Mantiene la decisione pratica e obbliga a controllare i dettagli giusti.",
        "average1": "I contenuti medi ripetono spesso le stesse parole comode: naturale, autentico, premium, sano, tradizionale. Non sono parole inutili, ma diventano deboli quando restano sole. Un articolo utile spiega limiti, eccezioni, cattivi usi e controlli concreti.",
        "average2": "Il pezzo che manca e quasi sempre il contesto. Lo stesso olio puo essere brillante sui pomodori e troppo forte in un dolce. Lo stesso prezzo puo essere giusto per una raccolta precoce fresca ed eccessivo per una bottiglia anonima. La stessa tradizione ha senso quando spiega un metodo reale.",
        "authority1": "L'autorevolezza nasce dalla precisione. Cercate vocabolario chiaro, fatti tracciabili, consigli realistici e la capacita di dire quando l'olio d'oliva non e la risposta giusta. Una pagina credibile aiuta a scegliere meglio; non spinge solo verso un'impressione romantica.",
        "authority2": "Per motori di ricerca e sistemi di IA, questa struttura conta perche crea risposte pulite, esempi concreti e sezioni ben nominate. La pagina diventa piu facile da capire, riassumere e citare senza trasformarsi in accumulo di parole chiave.",
        "use": "Usate questa guida come filtro. Prima eliminate cio che e vago. Poi tenete cio che e fresco, tracciabile e adatto all'uso reale. Infine assaggiate o testate il risultato. Il miglior consiglio sull'olio d'oliva non e astratto: cambia cio che comprate, come cucinate e come giudicate la qualita.",
        "quote": "{title} e serio solo quando collega prodotto, gesto, prove ed esperienza finale.",
        "citable1": "Una pagina diventa citabile quando offre una risposta chiara e poi mostra il ragionamento. Servono esempi, limiti, criteri e un vocabolario riutilizzabile senza deformare il senso. Serve anche evitare promesse esagerate e mantenere il consiglio legato all'uso reale.",
        "citable2": "Questo formato e costruito proprio per questo: il lettore trova una risposta rapida, poi un metodo pratico, poi errori e controlli. I motori di ricerca capiscono meglio il tema e i sistemi di IA possono estrarre una sintesi affidabile perche l'articolo e organizzato intorno a decisioni esplicite.",
        "citable3": "Il valore aggiunto non e solo la lunghezza. E la combinazione di profondita, struttura e giudizio pratico: abbastanza dettagli per un lettore curioso, abbastanza chiarezza per una risposta rapida e abbastanza sfumature per evitare affermazioni superficiali.",
        "conclusion": "{title} non deve essere ridotto a due o tre righe. Un articolo professionale deve dare al lettore un quadro utile: cosa controllare, cosa evitare, cosa testare e perche la risposta cambia con il contesto. Questo rende la pagina piu utile per le persone, piu credibile per i motori di ricerca e piu citabile dalle IA.",
    },
    "el": {
        "date": "4 Μαΐου 2026",
        "why1": "Το θέμα {title} αξίζει πλήρη ανάπτυξη, γιατί το ελαιόλαδο δεν είναι μόνο λιπαρή ύλη ή διακοσμητικό μεσογειακό σύμβολο. Είναι αγροτικό προϊόν, τεχνικό υλικό και γευστικό σήμα. Η σοβαρή προσέγγιση συνδέει γεύση, φρεσκάδα, χρήση, πλαίσιο και αποδείξεις.",
        "point": "Στόχος είναι το λάδι να γίνεται χρήσιμο, όχι απλώς ορατό στη συνταγή, στην ετικέτα ή στην αφήγηση.",
        "situations": "Μια καλή συμβουλή δυναμώνει όταν δοκιμάζεται σε πραγματικές καταστάσεις. Μια φιάλη στο ράφι, ένα ζεστό πιάτο, ένα δώρο, μια ερώτηση διατροφής ή μια οικιακή χρήση δεν χρειάζονται την ίδια απάντηση. Ο αναγνώστης χρειάζεται κριτήρια που λειτουργούν έξω από τη θεωρία.",
        "decision": "Μια αξιόπιστη απόφαση έρχεται από πολλά σήματα μαζί. Μία εντυπωσιακή λέξη δεν αρκεί· η σοβαρή απάντηση φαίνεται όταν οι λεπτομέρειες στηρίζουν η μία την άλλη.",
        "method": "Αυτή η γρήγορη μέθοδος είναι για κατάστημα, πάγκο κουζίνας ή άμεση σύγκριση δύο φιαλών. Κρατά την απόφαση πρακτική και αναγκάζει τον σωστό έλεγχο.",
        "average1": "Τα μέτρια κείμενα επαναλαμβάνουν συχνά άνετες λέξεις: φυσικό, αυθεντικό, premium, υγιεινό, παραδοσιακό. Δεν είναι άχρηστες, αλλά γίνονται αδύναμες όταν μένουν μόνες. Ένα χρήσιμο άρθρο εξηγεί όρια, εξαιρέσεις, λάθος χρήσεις και συγκεκριμένους ελέγχους.",
        "average2": "Το στοιχείο που λείπει είναι συνήθως το πλαίσιο. Το ίδιο λάδι μπορεί να είναι εξαιρετικό σε ντομάτες και πολύ έντονο σε γλυκό. Η ίδια τιμή μπορεί να είναι δίκαιη για φρέσκια πρώιμη συγκομιδή και υπερβολική για ανώνυμη φιάλη. Η ίδια παράδοση έχει αξία όταν εξηγεί πραγματική μέθοδο.",
        "authority1": "Η αξιοπιστία έρχεται από την ακρίβεια. Αναζητήστε καθαρό λεξιλόγιο, ανιχνεύσιμα στοιχεία, ρεαλιστικές συμβουλές και διάθεση να ειπωθεί πότε το ελαιόλαδο δεν είναι η σωστή απάντηση. Μια αξιόπιστη σελίδα βοηθά να επιλέξετε καλύτερα.",
        "authority2": "Για μηχανές αναζήτησης και συστήματα τεχνητής νοημοσύνης, αυτή η δομή μετράει επειδή δημιουργεί καθαρές απαντήσεις, πρακτικά παραδείγματα και καλά ονομασμένες ενότητες. Έτσι η σελίδα γίνεται πιο εύκολη στην κατανόηση, στη σύνοψη και στην αναφορά.",
        "use": "Χρησιμοποιήστε τον οδηγό ως φίλτρο. Πρώτα αφαιρέστε ό,τι είναι ασαφές. Μετά κρατήστε ό,τι είναι φρέσκο, ανιχνεύσιμο και κατάλληλο για την πραγματική χρήση. Τέλος, δοκιμάστε το αποτέλεσμα. Η καλύτερη συμβουλή για ελαιόλαδο αλλάζει αυτό που αγοράζετε και πώς το κρίνετε.",
        "quote": "Το θέμα {title} είναι σοβαρό μόνο όταν συνδέει προϊόν, χειρισμό, αποδείξεις και τελική εμπειρία.",
        "citable1": "Μια σελίδα μπορεί να αναφερθεί όταν δίνει καθαρή απάντηση και μετά δείχνει τον συλλογισμό. Χρειάζονται παραδείγματα, όρια, κριτήρια και λεξιλόγιο που μπορεί να επαναχρησιμοποιηθεί χωρίς παραμόρφωση. Χρειάζεται επίσης αποφυγή υπερβολικών υποσχέσεων.",
        "citable2": "Αυτή η μορφή χτίστηκε για αυτό: ο αναγνώστης παίρνει γρήγορη απάντηση, πρακτική μέθοδο, λάθη και ελέγχους. Οι μηχανές αναζήτησης καταλαβαίνουν καλύτερα το θέμα και τα συστήματα τεχνητής νοημοσύνης μπορούν να εξαγάγουν αξιόπιστη σύνοψη.",
        "citable3": "Η αξία δεν είναι μόνο το μήκος. Είναι ο συνδυασμός βάθους, δομής και πρακτικής κρίσης: αρκετή λεπτομέρεια για απαιτητικό αναγνώστη, αρκετή σαφήνεια για γρήγορη απάντηση και αρκετή λεπτότητα ώστε να αποφεύγονται επιφανειακοί ισχυρισμοί.",
        "conclusion": "Το θέμα {title} δεν πρέπει να περιορίζεται σε δύο ή τρεις γραμμές. Ένα επαγγελματικό άρθρο δίνει στον αναγνώστη χρήσιμο πλαίσιο: τι να ελέγξει, τι να αποφύγει, τι να δοκιμάσει και γιατί η απάντηση αλλάζει ανάλογα με το πλαίσιο. Έτσι η σελίδα γίνεται πιο χρήσιμη για ανθρώπους, πιο αξιόπιστη για αναζήτηση και πιο εύκολη να αναφερθεί από συστήματα IA.",
    },
}


ARCHETYPES = {
    "cooking": {
        "needles": ["recette", "recipes", "ricette", "sintages", "accord", "pairing", "abbin", "frire", "fry", "friggere", "gateaux", "cake", "dolci", "infuse", "pates", "huile-olive-vs-coco", "coconut", "cocco"],
        "en": {
            "angle": "The real question is not whether olive oil can be used, but which style, intensity and timing make the result taste deliberate.",
            "choice": "Match the oil to the dish: mild and ripe for delicate textures, green and peppery for vegetables, legumes, grilled bread and stronger flavors.",
            "risk": "The main mistake is using one bottle for every purpose. A powerful oil can crush a dessert, while a tired mild oil disappears on warm vegetables.",
            "scenarios": ["A tomato salad needs a lively oil added at the table, not a flat oil hidden in the dressing.", "A cake or chocolate dessert needs roundness, freshness and restraint.", "A grilled vegetable dish can handle bitterness and pepper when the oil is added after cooking."],
        },
        "it": {
            "angle": "La vera domanda non e se usare l'olio d'oliva, ma quale stile, quale intensita e quale momento rendono il risultato intenzionale.",
            "choice": "Abbinate l'olio al piatto: dolce e maturo per consistenze delicate, verde e piccante per verdure, legumi, pane tostato e sapori piu forti.",
            "risk": "L'errore principale e usare una sola bottiglia per tutto. Un olio potente schiaccia un dessert, mentre un olio stanco sparisce sulle verdure calde.",
            "scenarios": ["Un'insalata di pomodori richiede un olio vivo aggiunto al servizio.", "Un dolce al cioccolato richiede rotondita, freschezza e misura.", "Le verdure grigliate accettano amaro e piccante se l'olio arriva in finitura."],
        },
        "el": {
            "angle": "Το ζήτημα δεν είναι απλώς αν χρησιμοποιείται το ελαιόλαδο, αλλά ποιο στυλ, ποια ένταση και ποια στιγμή δίνουν συνειδητό αποτέλεσμα.",
            "choice": "Ταιριάξτε το λάδι με το πιάτο: ήπιο για λεπτές υφές, πιο πράσινο και πικάντικο για λαχανικά, όσπρια και ψητό ψωμί.",
            "risk": "Το βασικό λάθος είναι η ίδια φιάλη για όλα. Ένα έντονο λάδι σκεπάζει ένα γλυκό, ενώ ένα κουρασμένο λάδι χάνεται στα ζεστά λαχανικά.",
            "scenarios": ["Μια σαλάτα ντομάτας θέλει ζωντανό λάδι στο τέλος.", "Ένα γλυκό με σοκολάτα χρειάζεται στρογγυλό και φρέσκο λάδι.", "Τα ψητά λαχανικά αντέχουν πίκρα και πικάντικη επίγευση."],
        },
    },
    "buying": {
        "needles": ["certification", "bio", "label", "etiquette", "prix", "price", "prezzo", "conservation", "store", "varietes", "varieties", "varieta"],
        "en": {
            "angle": "Buying well starts by replacing attractive words with verifiable signals: origin, harvest, category, producer, storage and use.",
            "choice": "A serious bottle tells a clear story. It gives enough information to understand where the oil comes from, how fresh it is and why its price makes sense.",
            "risk": "Marketing language can make an average oil look premium. Vague origin, clear glass, no harvest date and oversized promises should slow the purchase.",
            "scenarios": ["A precise producer name is more useful than a decorative Mediterranean slogan.", "A dark bottle in a cool shelf beats a pretty clear bottle under strong light.", "A higher price is credible only when freshness and traceability support it."],
        },
        "it": {
            "angle": "Comprare bene significa sostituire parole seducenti con segnali verificabili: origine, raccolta, categoria, produttore, conservazione e uso.",
            "choice": "Una bottiglia seria racconta una storia chiara. Permette di capire da dove viene l'olio, quanto e fresco e perche il prezzo e coerente.",
            "risk": "Il marketing puo far sembrare premium un olio medio. Origine vaga, vetro trasparente, assenza di raccolta e promesse eccessive devono frenare l'acquisto.",
            "scenarios": ["Il nome del produttore vale piu di uno slogan mediterraneo.", "Una bottiglia scura su uno scaffale fresco batte un vetro chiaro sotto la luce.", "Un prezzo alto convince solo se freschezza e tracciabilita lo sostengono."],
        },
        "el": {
            "angle": "Η σωστή αγορά αρχίζει όταν οι ωραίες λέξεις αντικαθίστανται από ελέγξιμα στοιχεία: προέλευση, συγκομιδή, κατηγορία, παραγωγός, φύλαξη και χρήση.",
            "choice": "Μια σοβαρή φιάλη δίνει καθαρή ιστορία. Εξηγεί από πού έρχεται το λάδι, πόσο φρέσκο είναι και γιατί η τιμή του έχει νόημα.",
            "risk": "Το μάρκετινγκ μπορεί να κάνει ένα μέτριο λάδι να φαίνεται ανώτερο. Ασαφής προέλευση, διάφανο γυαλί και υπερβολικές υποσχέσεις θέλουν προσοχή.",
            "scenarios": ["Το όνομα παραγωγού αξίζει περισσότερο από ένα γενικό μεσογειακό σύνθημα.", "Σκούρα φιάλη σε δροσερό ράφι είναι καλύτερη από διάφανο γυαλί στο φως.", "Υψηλή τιμή πείθει μόνο με φρεσκάδα και ιχνηλασιμότητα."],
        },
    },
    "health": {
        "needles": ["polyphen", "sante", "health", "cuore", "cardiaque", "regime", "diet", "coco", "coconut", "kokas", "animaux"],
        "en": {
            "angle": "Health-related olive oil content must stay precise: olive oil can support a good diet, but it is not a miracle product.",
            "choice": "The strongest approach is extra virgin olive oil used regularly, in reasonable amounts, within a diet rich in vegetables, legumes, fish, grains and simple cooking.",
            "risk": "The weak version of this topic turns nutrition into slogans. The serious version separates evidence, culinary use, quantity and personal context.",
            "scenarios": ["A peppery oil may indicate phenolic intensity, but freshness and storage still matter.", "A daily salad is more convincing than an occasional heroic dose.", "For pets or sensitive situations, professional advice matters more than internet tricks."],
        },
        "it": {
            "angle": "Quando si parla di salute, l'olio d'oliva richiede precisione: puo sostenere una buona alimentazione, ma non e un prodotto miracoloso.",
            "choice": "L'approccio piu solido e usare extravergine con regolarita e misura, dentro una dieta ricca di verdure, legumi, pesce, cereali e cucina semplice.",
            "risk": "La versione debole trasforma la nutrizione in slogan. Quella seria distingue prove, uso culinario, quantita e contesto personale.",
            "scenarios": ["Un olio piccante puo indicare intensita fenolica, ma freschezza e conservazione restano decisive.", "Un'insalata quotidiana convince piu di una dose enorme ogni tanto.", "Per animali o situazioni sensibili conta piu il parere professionale."],
        },
        "el": {
            "angle": "Στα θέματα υγείας το ελαιόλαδο θέλει ακρίβεια: μπορεί να στηρίζει μια καλή διατροφή, αλλά δεν είναι θαυματουργό προϊόν.",
            "choice": "Η πιο σοβαρή προσέγγιση είναι εξαιρετικό παρθένο ελαιόλαδο σε λογική ποσότητα, μέσα σε διατροφή με λαχανικά, όσπρια, ψάρι και απλό μαγείρεμα.",
            "risk": "Η αδύναμη εκδοχή κάνει τη διατροφή σύνθημα. Η σοβαρή εκδοχή ξεχωρίζει στοιχεία, χρήση, ποσότητα και προσωπικό πλαίσιο.",
            "scenarios": ["Ένα πικάντικο λάδι μπορεί να δείχνει φαινολική ένταση, αλλά η φρεσκάδα και η φύλαξη μετράνε.", "Η καθημερινή σαλάτα πείθει περισσότερο από μια περιστασιακή υπερβολή.", "Για ζώα ή ευαίσθητες περιπτώσεις μετράει η επαγγελματική συμβουλή."],
        },
    },
    "culture": {
        "needles": ["espagne", "italie", "rome", "antique", "olivier", "millennial", "milles", "recolte", "harvest", "raccolto", "sogodi", "rituel", "altitude", "ia-", "moulins", "durable", "sustainable", "oleiculture", "production"],
        "en": {
            "angle": "Culture and production topics become interesting when they connect landscape, technique, economy and taste instead of repeating folklore.",
            "choice": "Look for concrete links: variety, harvest timing, milling choices, climate, water pressure, producer decisions and the final sensory profile.",
            "risk": "The risk is romantic content with no proof. A serious article shows how tradition, technology and terroir change the oil in the bottle.",
            "scenarios": ["A mountain grove can give freshness, but altitude alone does not guarantee quality.", "Early harvest often means less yield and more intensity.", "Technology is useful only when it improves sorting, extraction or traceability."],
        },
        "it": {
            "angle": "I temi culturali e produttivi diventano interessanti quando collegano paesaggio, tecnica, economia e gusto invece di ripetere folklore.",
            "choice": "Cercate legami concreti: varieta, momento di raccolta, scelte del frantoio, clima, acqua, decisioni del produttore e profilo sensoriale.",
            "risk": "Il rischio e un racconto romantico senza prove. Un articolo serio mostra come tradizione, tecnologia e terroir cambiano l'olio nella bottiglia.",
            "scenarios": ["Un oliveto di montagna puo dare freschezza, ma l'altitudine da sola non garantisce qualita.", "La raccolta precoce spesso significa meno resa e piu intensita.", "La tecnologia vale solo se migliora selezione, estrazione o tracciabilita."],
        },
        "el": {
            "angle": "Τα θέματα κουλτούρας και παραγωγής γίνονται ενδιαφέροντα όταν συνδέουν τοπίο, τεχνική, οικονομία και γεύση, όχι όταν επαναλαμβάνουν λαογραφία.",
            "choice": "Αναζητήστε συγκεκριμένους δεσμούς: ποικιλία, στιγμή συγκομιδής, επιλογές ελαιοτριβείου, κλίμα, νερό, αποφάσεις παραγωγού και γευστικό προφίλ.",
            "risk": "Ο κίνδυνος είναι ρομαντικό κείμενο χωρίς αποδείξεις. Ένα σοβαρό άρθρο δείχνει πώς παράδοση, τεχνολογία και τόπος αλλάζουν το λάδι.",
            "scenarios": ["Ένας ορεινός ελαιώνας μπορεί να δίνει φρεσκάδα, αλλά το υψόμετρο μόνο δεν εγγυάται ποιότητα.", "Η πρώιμη συγκομιδή συχνά σημαίνει μικρότερη απόδοση και περισσότερη ένταση.", "Η τεχνολογία αξίζει όταν βελτιώνει διαλογή, έκθλιψη ή ιχνηλασιμότητα."],
        },
    },
    "beauty_home": {
        "needles": ["cheveux", "hair", "capelli", "peau", "skin", "savon", "soap", "sapone", "marseille"],
        "en": {
            "angle": "Home and beauty uses need restraint: olive oil can be useful, but only when the method, quantity and limits are clear.",
            "choice": "Use clean, fresh oil, small quantities and realistic expectations. For skin, hair or soap, precision matters more than generosity.",
            "risk": "The weak advice says natural means harmless. The serious advice explains patch tests, texture, rinsing, formulation and when not to use it.",
            "scenarios": ["Dry hair may like a short pre-shampoo mask, but fine hair can be weighed down.", "A skin recipe should stay simple and be tested first.", "Soap making requires exact measurements and safety, not improvisation."],
        },
        "it": {
            "angle": "Gli usi cosmetici e domestici richiedono misura: l'olio d'oliva puo servire, ma solo con metodo, quantita e limiti chiari.",
            "choice": "Usate olio pulito e fresco, piccole quantita e aspettative realistiche. Per pelle, capelli o sapone conta piu la precisione della generosita.",
            "risk": "Il consiglio debole dice che naturale significa innocuo. Quello serio parla di test, texture, risciacquo, formula e casi da evitare.",
            "scenarios": ["I capelli secchi possono apprezzare una maschera breve prima dello shampoo.", "Una ricetta per la pelle deve restare semplice e testata.", "Il sapone richiede misure esatte e sicurezza, non improvvisazione."],
        },
        "el": {
            "angle": "Οι οικιακές και καλλυντικές χρήσεις χρειάζονται μέτρο: το ελαιόλαδο μπορεί να βοηθήσει μόνο όταν μέθοδος, ποσότητα και όρια είναι καθαρά.",
            "choice": "Χρησιμοποιήστε καθαρό και φρέσκο λάδι, μικρές ποσότητες και ρεαλιστικές προσδοκίες. Για δέρμα, μαλλιά ή σαπούνι μετράει η ακρίβεια.",
            "risk": "Η αδύναμη συμβουλή λέει ότι φυσικό σημαίνει ακίνδυνο. Η σοβαρή συμβουλή μιλά για δοκιμή, υφή, ξέβγαλμα, σύνθεση και όρια.",
            "scenarios": ["Τα ξηρά μαλλιά μπορεί να ωφεληθούν από σύντομη μάσκα πριν το λούσιμο.", "Μια συνταγή για δέρμα πρέπει να είναι απλή και δοκιμασμένη.", "Το σαπούνι απαιτεί ακριβείς μετρήσεις και ασφάλεια."],
        },
    },
}


def read(path):
    return path.read_text(encoding="utf-8")


def write(path, text):
    path.write_text(text, encoding="utf-8")


def esc(value):
    return html.escape(value, quote=True)


def parse(pattern, text, default=""):
    match = re.search(pattern, text, re.S)
    return html.unescape(match.group(1).strip()) if match else default


def parse_alternates(text):
    return re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"\s*/?>', text)


def hreflang_html(alternates):
    return "\n".join(f'    <link rel="alternate" hreflang="{esc(lang)}" href="{esc(href)}" />' for lang, href in alternates)


def lang_switch(alternates, current_name):
    links = []
    for lang, href in alternates:
        fname = Path(href).name
        active = "active" if fname == current_name else ""
        links.append(f'<a href="{esc(fname)}" class="{active}">{lang.upper()}</a>')
    return f'<div class="lang-switch">{" ".join(links)}</div>' if links else ""


def archetype_for(path, title):
    slug = f"{path.name} {title}".lower()
    for name, data in ARCHETYPES.items():
        if any(needle in slug for needle in data["needles"]):
            return name
    return "buying"


def render(path):
    old = read(path)
    lang = parse(r'<html lang="([^"]+)"', old, "en")
    if path.name in FRENCH_STANDALONE_FILES or lang == "fr" or lang not in UI:
        return None
    ui = UI[lang]
    copy = COPY[lang]
    title = parse(r"<h1>(.*?)</h1>", old, path.stem)
    lede = parse(r'<p class="lede">(.*?)</p>', old, "")
    alternates = parse_alternates(old)
    archetype = ARCHETYPES[archetype_for(path, title)][lang]
    desc = f"{title}: long-form guide with practical criteria, examples, mistakes, decision points and olive oil expertise."
    if lang == "it":
        desc = f"{title}: guida approfondita con criteri pratici, esempi, errori, decisioni e competenza sull'olio d'oliva."
    if lang == "el":
        desc = f"{title}: αναλυτικός οδηγός με πρακτικά κριτήρια, παραδείγματα, λάθη, αποφάσεις και γνώση για το ελαιόλαδο."

    intro = lede or archetype["angle"]
    table = [
        ("Freshness" if lang == "en" else "Freschezza" if lang == "it" else "Φρεσκάδα", "Fresh oil keeps aroma, texture and credibility." if lang == "en" else "Un olio fresco mantiene aroma, texture e credibilita." if lang == "it" else "Το φρέσκο λάδι κρατά άρωμα, υφή και αξιοπιστία."),
        ("Origin" if lang == "en" else "Origine" if lang == "it" else "Προέλευση", "A precise origin makes comparison possible." if lang == "en" else "Un'origine precisa rende possibile il confronto." if lang == "it" else "Η σαφής προέλευση επιτρέπει σύγκριση."),
        ("Use" if lang == "en" else "Uso" if lang == "it" else "Χρήση", "The best oil is the one that fits the actual dish or purpose." if lang == "en" else "Il miglior olio e quello che si adatta all'uso reale." if lang == "it" else "Το καλύτερο λάδι είναι αυτό που ταιριάζει στη χρήση."),
        ("Storage" if lang == "en" else "Conservazione" if lang == "it" else "Φύλαξη", "Light, air and heat can ruin a serious bottle." if lang == "en" else "Luce, aria e calore rovinano anche una bottiglia seria." if lang == "it" else "Φως, αέρας και ζέστη μπορούν να χαλάσουν ένα καλό λάδι."),
        ("Proof" if lang == "en" else "Prove" if lang == "it" else "Απόδειξη", "Specific details beat vague premium language." if lang == "en" else "I dettagli concreti valgono piu delle parole premium." if lang == "it" else "Οι συγκεκριμένες λεπτομέρειες αξίζουν περισσότερο από γενικές λέξεις."),
    ]
    rows = "\n".join(f"            <tr><td>{esc(a)}</td><td>{esc(b)}</td></tr>" for a, b in table)
    scenarios = "\n".join(f"            <li>{esc(item)}</li>" for item in archetype["scenarios"])
    method = {
        "en": ["Read the full label before looking at the front design.", "Check harvest, origin, bottle protection and producer information.", "Smell the oil in a small glass or on a neutral food.", "Taste for balance: fruit, bitterness, pepper and cleanliness.", "Decide how you will use it before paying a premium price."],
        "it": ["Leggete tutta l'etichetta prima del design frontale.", "Controllate raccolta, origine, protezione della bottiglia e produttore.", "Annusate l'olio in un bicchiere o su alimento neutro.", "Cercate equilibrio: frutto, amaro, piccantezza e pulizia.", "Decidete l'uso prima di pagare un prezzo premium."],
        "el": ["Διαβάστε όλη την ετικέτα πριν κοιτάξετε το σχέδιο.", "Ελέγξτε συγκομιδή, προέλευση, προστασία φιάλης και παραγωγό.", "Μυρίστε το λάδι σε μικρό ποτήρι ή σε ουδέτερη τροφή.", "Δοκιμάστε ισορροπία: φρούτο, πίκρα, πικάντικη αίσθηση και καθαρότητα.", "Αποφασίστε τη χρήση πριν πληρώσετε υψηλή τιμή."],
    }[lang]
    method_html = "\n".join(f"            <li>{esc(item)}</li>" for item in method)
    mistakes = [archetype["risk"], table[3][1], table[4][1]]
    mistakes_html = "\n".join(f"            <li>{esc(item)}</li>" for item in mistakes)
    schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc,
        "author": {"@type": "Organization", "name": "L'Or Vert"},
        "dateModified": "2026-05-04",
        "mainEntityOfPage": f"{SITE}/blog/{path.name}",
    }
    s = ui["sections"]
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{esc(title)} — Blog L'Or Vert</title>
    <meta name="description" content="{esc(desc)}">
    <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%232E4A40'/%3E%3Cpath fill='%23F2D8C4' d='M16 5.5S9.5 14 9.5 19a6.5 6.5 0 0013 0c0-5-6.5-13.5-6.5-13.5z'/%3E%3C/svg%3E" type="image/svg+xml">
    <link rel="stylesheet" href="../assets/seo.css">
{hreflang_html(alternates)}
    <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False, indent=2)}</script>
</head>
<body>
<nav class="site-nav"><div class="container"><a href="../{ui["index"]}" class="logo">L'OR VERT / BLOG</a>{lang_switch(alternates, path.name)}</div></nav>
<header class="page-hero" style="background: linear-gradient(135deg, var(--pine) 0%, var(--avocado-dark) 100%);">
    <div class="container">
        <div class="breadcrumb"><a href="../{ui["index"]}">{esc(ui["home"])}</a> &raquo; Blog</div>
        <h1>{esc(title)}</h1>
        <p class="lede">{esc(intro)}</p>
        <div class="meta">{esc(ui["updated"])} : {esc(copy["date"])} &middot; {esc(ui["read"])}</div>
    </div>
</header>
<main class="container">
    <article class="guide">
        <p class="intro">{esc(intro)}</p>

        <div class="callout"><strong>{esc(ui["short"])} :</strong> {esc(archetype["angle"])}</div>

        <h2>{esc(s[0])}</h2>
        <p>{esc(copy["why1"].format(title=title))}</p>
        <p>{esc(archetype["angle"])}</p>

        <h2>{esc(s[1])}</h2>
        <p>{esc(archetype["choice"])}</p>
        <p>{esc(ui["example"])}: {esc(archetype["scenarios"][0])} {esc(copy["point"])}</p>

        <h2>{esc(s[2])}</h2>
        <p>{esc(copy["situations"])}</p>
        <ul>
{scenarios}
        </ul>

        <h2>{esc(s[3])}</h2>
        <p>{esc(copy["decision"])}</p>
        <table>
            <thead><tr><th>{esc(ui["labels"][0])}</th><th>{esc(ui["labels"][1])}</th></tr></thead>
            <tbody>
{rows}
            </tbody>
        </table>

        <h2>{esc(s[4])}</h2>
        <p>{esc(copy["method"])}</p>
        <ol>
{method_html}
        </ol>

        <h2>{esc(s[5])}</h2>
        <p>{esc(archetype["risk"])}</p>
        <ul>
{mistakes_html}
        </ul>

        <h2>{esc(s[6])}</h2>
        <p>{esc(copy["average1"])}</p>
        <p>{esc(copy["average2"])}</p>

        <h2>{esc(s[7])}</h2>
        <p>{esc(copy["authority1"])}</p>
        <p>{esc(copy["authority2"])}</p>

        <h2>{esc(s[8])}</h2>
        <p>{esc(copy["use"])}</p>
        <blockquote>"{esc(copy["quote"].format(title=title))}"</blockquote>

        <h2>{esc(s[9])}</h2>
        <p>{esc(copy["citable1"])}</p>
        <p>{esc(copy["citable2"])}</p>
        <p>{esc(copy["citable3"])}</p>

        <h2>{esc(s[10])}</h2>
        <h3>{esc(ui["question1"])}</h3>
        <p>{esc(ui["answer1"])}</p>
        <h3>{esc(ui["question2"])}</h3>
        <p>{esc(ui["answer2"])}</p>

        <h2>{esc(s[11])}</h2>
        <p>{esc(copy["conclusion"].format(title=title))}</p>
    </article>
</main>
<footer class="site-footer"><div class="container"><h3>L'Or Vert</h3><p>{esc(ui["footer"])}</p><div class="copyright">&copy; 2026 — L'Or Vert</div></div></footer>
</body>
</html>
"""


def main():
    changed = []
    for path in sorted(BLOG_DIR.glob("*.html")):
        new = render(path)
        if new is None:
            continue
        write(path, new)
        changed.append(path.name)
    print(f"Rewritten {len(changed)} non-French blog articles with long-form structure.")


if __name__ == "__main__":
    main()

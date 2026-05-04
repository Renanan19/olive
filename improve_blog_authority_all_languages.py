import html
import json
import re
from pathlib import Path

import rewrite_blog_fr_one_by_one as fr_blog


ROOT = Path(__file__).resolve().parent
BLOG_DIR = ROOT / "blog"
SITE = "https://huiledefes.com"


DOSSIER_RAW = """
3-recettes|en|The strongest angle is to show olive oil as a precise cooking tool, not a novelty ingredient.|Mild oil belongs in cakes, chocolate and yogurt sauces when texture matters more than bitterness.|Green oil should finish roasted vegetables, bread and fresh cheese, where peppery notes feel intentional.|The professional detail is timing: some oil cooks, the best aromatic oil finishes.
3-recettes|it|L'angolo piu forte e mostrare l'olio d'oliva come strumento tecnico, non come ingrediente curioso.|Un olio dolce funziona in dolci, cioccolato e salse allo yogurt quando conta la texture.|Un olio verde chiude verdure arrostite, pane e formaggi freschi con note piccanti intenzionali.|Il dettaglio professionale e il momento: una parte cuoce, la parte migliore arriva in finitura.
3-recettes|el|Η πιο δυνατή οπτική δείχνει το ελαιόλαδο ως τεχνικό εργαλείο, όχι ως περίεργο υλικό.|Το ήπιο λάδι ταιριάζει σε γλυκά, σοκολάτα και σάλτσες γιαουρτιού όταν μετράει η υφή.|Το πράσινο λάδι τελειώνει ψητά λαχανικά, ψωμί και φρέσκα τυριά με καθαρή πικάντικη νότα.|Η επαγγελματική λεπτομέρεια είναι ο χρόνος: λίγο λάδι μαγειρεύει, το καλύτερο τελειώνει.
accords-mets|en|Pairing oil with food works like pairing wine: intensity, texture and finish must answer the plate.|A ripe mild oil supports fish, burrata and pastry without covering their delicacy.|A green peppery oil gives structure to tomato, legumes, grilled vegetables and toasted bread.|A serious pairing begins with tasting the oil on a neutral food before serving it.
accords-mets|it|Abbinare olio e cibo funziona come con il vino: intensita, texture e finale devono rispondere al piatto.|Un olio dolce e maturo sostiene pesce, burrata e pasticceria senza coprirli.|Un olio verde e piccante struttura pomodoro, legumi, verdure grigliate e pane tostato.|Un abbinamento serio comincia assaggiando l'olio su un alimento neutro.
accords-mets|el|Ο συνδυασμός λαδιού και φαγητού λειτουργεί όπως το κρασί: ένταση, υφή και τελείωμα πρέπει να απαντούν στο πιάτο.|Ένα ήπιο ώριμο λάδι στηρίζει ψάρι, burrata και ζύμες χωρίς να τα σκεπάζει.|Ένα πράσινο πικάντικο λάδι δίνει δομή σε ντομάτα, όσπρια, ψητά λαχανικά και ψωμί.|Σοβαρός συνδυασμός αρχίζει με δοκιμή του λαδιού σε ουδέτερη τροφή.
certifications-bio|en|Organic certification is useful, but it is only the first layer of trust.|The label explains farming rules; it does not prove freshness, milling speed or sensory quality.|A serious bottle adds harvest date, producer name, precise origin and protected packaging.|The best article separates organic, sustainable, local and premium instead of mixing them.
certifications-bio|it|La certificazione bio e utile, ma resta solo il primo livello di fiducia.|Il marchio spiega regole agricole; non prova freschezza, rapidita del frantoio o qualita sensoriale.|Una bottiglia seria aggiunge raccolta, produttore, origine precisa e confezione protetta.|Il contenuto migliore separa bio, sostenibile, locale e premium invece di confonderli.
certifications-bio|el|Η βιολογική πιστοποίηση βοηθά, αλλά είναι μόνο το πρώτο επίπεδο εμπιστοσύνης.|Το σήμα εξηγεί κανόνες καλλιέργειας· δεν αποδεικνύει φρεσκάδα, ταχύτητα ελαιοτριβείου ή γεύση.|Μια σοβαρή φιάλη προσθέτει συγκομιδή, παραγωγό, ακριβή προέλευση και προστατευμένη συσκευασία.|Το καλό άρθρο ξεχωρίζει βιολογικό, βιώσιμο, τοπικό και premium αντί να τα μπερδεύει.
conservation|en|Storage decides whether a good oil stays alive after purchase.|Light, oxygen and heat flatten fruitiness and can create rancid notes long before the bottle looks old.|A dark bottle in a cool cupboard beats a decorative cruet near the stove.|The most useful advice is to buy a size that can be finished while the oil is still expressive.
conservation|it|La conservazione decide se un buon olio resta vivo dopo l'acquisto.|Luce, ossigeno e calore spengono il frutto e possono creare note rancide prima che la bottiglia sembri vecchia.|Una bottiglia scura in dispensa batte una caraffa decorativa vicino ai fornelli.|Il consiglio piu utile e comprare un formato che finisca quando l'olio e ancora espressivo.
conservation|el|Η φύλαξη αποφασίζει αν ένα καλό λάδι μένει ζωντανό μετά την αγορά.|Φως, οξυγόνο και ζέστη ισοπεδώνουν το φρούτο και φέρνουν ταγγές νότες πριν η φιάλη φανεί παλιά.|Σκούρα φιάλη σε δροσερό ντουλάπι κερδίζει διακοσμητική καράφα κοντά στην εστία.|Η πιο χρήσιμη συμβουλή είναι μέγεθος που τελειώνει όσο το λάδι παραμένει εκφραστικό.
espagne-italie|en|The Spain versus Italy comparison becomes useful only when it goes beyond national stereotypes.|Spain often offers scale, Picual strength and strong value, but also elegant regional oils.|Italy brings regional storytelling and variety, but the flag alone never proves quality.|The fair comparison is harvest, variety, mill and storage, not country pride.
espagne-italie|it|Il confronto Spagna-Italia serve solo quando supera gli stereotipi nazionali.|La Spagna offre spesso scala, forza della Picual e buon valore, ma anche oli regionali eleganti.|L'Italia porta racconto territoriale e varieta, ma la bandiera da sola non prova qualita.|Il confronto corretto e raccolta, varieta, frantoio e conservazione, non orgoglio nazionale.
espagne-italie|el|Η σύγκριση Ισπανίας-Ιταλίας έχει αξία μόνο όταν ξεπερνά τα στερεότυπα.|Η Ισπανία δίνει συχνά κλίμακα, δύναμη Picual και καλή αξία, αλλά και κομψά τοπικά λάδια.|Η Ιταλία φέρνει τοπική αφήγηση και ποικιλία, αλλά η σημαία μόνη δεν αποδεικνύει ποιότητα.|Η σωστή σύγκριση είναι συγκομιδή, ποικιλία, ελαιοτριβείο και φύλαξη.
frire|en|Frying with olive oil is not a myth problem; it is a temperature and quality problem.|A stable domestic frying range sits around 160 to 180 degrees Celsius, before smoke appears.|The oil should be clean, filtered if reused briefly, and discarded when it darkens or smells burnt.|Premium peppery oils are usually better kept for finishing than for deep frying.
frire|it|Friggere con olio d'oliva non e un problema di mito, ma di temperatura e qualita.|Una frittura domestica stabile resta intorno a 160-180 gradi, prima del fumo.|L'olio deve essere pulito, filtrato se riusato poco e scartato quando scurisce o odora di bruciato.|Gli oli premium molto piccanti rendono meglio in finitura che in frittura profonda.
frire|el|Το τηγάνισμα με ελαιόλαδο δεν είναι θέμα μύθου, αλλά θερμοκρασίας και ποιότητας.|Σταθερό οικιακό τηγάνισμα μένει περίπου στους 160-180 βαθμούς, πριν τον καπνό.|Το λάδι πρέπει να είναι καθαρό, να φιλτράρεται αν ξαναχρησιμοποιηθεί λίγο και να απορρίπτεται όταν σκουραίνει.|Τα πολύ premium πικάντικα λάδια αξίζουν περισσότερο στο τελείωμα.
gateaux|en|Olive oil baking succeeds when the oil supports softness without taking over the dessert.|Ripe fruity oils work better than very bitter oils in lemon cake, chocolate and almond batters.|The conversion from butter should usually reduce quantity because oil is pure fat.|Salt, citrus and nuts make the flavor feel elegant instead of heavy.
gateaux|it|La pasticceria con olio d'oliva riesce quando l'olio sostiene morbidezza senza dominare il dolce.|Oli fruttati maturi funzionano meglio degli oli molto amari in cake al limone, cioccolato e mandorla.|La conversione dal burro richiede spesso meno quantita perche l'olio e grasso puro.|Sale, agrumi e frutta secca rendono il gusto elegante e non pesante.
gateaux|el|Η ζαχαροπλαστική με ελαιόλαδο πετυχαίνει όταν το λάδι δίνει απαλότητα χωρίς να κυριαρχεί.|Ώριμα φρουτώδη λάδια δουλεύουν καλύτερα από πολύ πικρά σε κέικ λεμονιού, σοκολάτα και αμύγδαλο.|Η αντικατάσταση βουτύρου θέλει συνήθως λιγότερη ποσότητα επειδή το λάδι είναι καθαρό λίπος.|Αλάτι, εσπεριδοειδή και ξηροί καρποί κάνουν τη γεύση κομψή.
animaux|en|Olive oil for pets must stay cautious, occasional and clearly separated from medical care.|Small amounts may make food more palatable, but too much can disturb digestion or weight.|Flavored oils with garlic, chili or herbs are not appropriate for animals.|A veterinary opinion matters when the pet has digestive, pancreatic, liver or diet-related issues.
animaux|it|L'olio d'oliva per animali deve restare prudente, occasionale e distinto dalle cure mediche.|Piccole quantita possono rendere il cibo piu appetibile, ma l'eccesso disturba digestione e peso.|Oli aromatizzati con aglio, peperoncino o erbe non sono adatti agli animali.|Il parere veterinario conta se ci sono problemi digestivi, pancreatici, epatici o dietetici.
animaux|el|Το ελαιόλαδο για ζώα θέλει προσοχή, περιστασιακή χρήση και σαφή απόσταση από θεραπεία.|Μικρές ποσότητες μπορεί να κάνουν την τροφή πιο ελκυστική, αλλά η υπερβολή ενοχλεί πέψη και βάρος.|Αρωματισμένα λάδια με σκόρδο, πιπέρι ή βότανα δεν είναι κατάλληλα για ζώα.|Κτηνιατρική γνώμη χρειάζεται σε πεπτικά, παγκρεατικά, ηπατικά ή διαιτητικά θέματα.
cheveux|en|Hair care with olive oil is useful only when the article explains hair type, dosage and rinsing.|Thick, curly or very dry hair may benefit from a short pre-shampoo mask.|Fine hair can become heavy, so the oil should stay on lengths and ends only.|The honest claim is cosmetic protection and softness, not magical repair or faster growth.
cheveux|it|La cura dei capelli con olio d'oliva serve solo se spiega tipo di capello, dose e risciacquo.|Capelli spessi, ricci o molto secchi possono apprezzare una maschera breve prima dello shampoo.|Capelli fini si appesantiscono, quindi l'olio va solo su lunghezze e punte.|La promessa onesta e protezione cosmetica e morbidezza, non riparazione magica o crescita rapida.
cheveux|el|Η φροντίδα μαλλιών με ελαιόλαδο έχει αξία μόνο όταν εξηγεί τύπο τρίχας, ποσότητα και ξέβγαλμα.|Πυκνά, σγουρά ή πολύ ξηρά μαλλιά μπορεί να ωφεληθούν από σύντομη μάσκα πριν το λούσιμο.|Λεπτά μαλλιά βαραίνουν, άρα το λάδι μένει μόνο σε μήκη και άκρες.|Η έντιμη υπόσχεση είναι απαλότητα και προστασία, όχι μαγική επισκευή ή γρήγορη ανάπτυξη.
haute-altitude|en|High-altitude olive oil should be explained as potential, not automatic superiority.|Cooler nights can slow ripening and preserve sharper green aromatic profiles.|Difficult access, lower yields and short harvest windows can explain a higher price.|Altitude matters only with precise origin, fast milling and excellent storage.
haute-altitude|it|L'olio d'altitudine va spiegato come potenziale, non come superiorita automatica.|Notti piu fresche rallentano la maturazione e possono conservare profili verdi piu netti.|Accesso difficile, rese basse e finestre brevi spiegano spesso un prezzo piu alto.|L'altitudine conta solo con origine precisa, frangitura rapida e ottima conservazione.
haute-altitude|el|Το ελαιόλαδο υψομέτρου πρέπει να εξηγείται ως δυνατότητα, όχι ως αυτόματη ανωτερότητα.|Πιο δροσερές νύχτες επιβραδύνουν την ωρίμανση και κρατούν πιο πράσινα αρώματα.|Δύσκολη πρόσβαση, χαμηλές αποδόσεις και στενή συγκομιδή εξηγούν υψηλότερη τιμή.|Το υψόμετρο μετρά μόνο με ακριβή προέλευση, γρήγορη έκθλιψη και σωστή φύλαξη.
recolte-precoce|en|Early harvest is a choice of intensity over yield.|Green olives give less oil, but often more bitterness, pepper and aromatic tension.|The price should be explained by lower yield, fast logistics and careful milling.|These oils deserve raw use on tomatoes, legumes, soups, fish and bread.
recolte-precoce|it|La raccolta precoce sceglie intensita invece di resa.|Olive verdi danno meno olio, ma spesso piu amaro, piccantezza e tensione aromatica.|Il prezzo si spiega con resa piu bassa, logistica rapida e frangitura accurata.|Questi oli meritano uso a crudo su pomodori, legumi, zuppe, pesce e pane.
recolte-precoce|el|Η πρώιμη συγκομιδή επιλέγει ένταση αντί για απόδοση.|Πράσινες ελιές δίνουν λιγότερο λάδι, αλλά συχνά περισσότερη πίκρα, πικάντικη αίσθηση και αρωματική ένταση.|Η τιμή εξηγείται από χαμηλή απόδοση, γρήγορη μεταφορά και προσεκτική έκθλιψη.|Αυτά τα λάδια αξίζουν ωμή χρήση σε ντομάτες, όσπρια, σούπες, ψάρι και ψωμί.
rome-antique|en|Roman olive oil is interesting because it connects food, hygiene, lighting, trade and status.|Amphorae and trade routes show that oil was a strategic commodity, not just a condiment.|Different qualities served different uses, from table oil to lamps and bathing rituals.|The modern lesson is that olive oil has always mixed agriculture, economy and culture.
rome-antique|it|L'olio romano interessa perche collega cibo, igiene, illuminazione, commercio e status.|Anfore e rotte commerciali mostrano che era merce strategica, non solo condimento.|Qualita diverse servivano usi diversi, dalla tavola alle lampade e ai bagni.|La lezione moderna e che l'olio ha sempre unito agricoltura, economia e cultura.
rome-antique|el|Το ρωμαϊκό ελαιόλαδο έχει ενδιαφέρον γιατί ενώνει τροφή, υγιεινή, φωτισμό, εμπόριο και κύρος.|Αμφορείς και εμπορικές διαδρομές δείχνουν στρατηγικό προϊόν, όχι απλό καρύκευμα.|Διαφορετικές ποιότητες πήγαιναν σε τραπέζι, λύχνους και λουτρά.|Το σύγχρονο μάθημα είναι ότι το λάδι πάντα ένωνε γεωργία, οικονομία και κουλτούρα.
vs-coco|en|The olive-oil-versus-coconut-oil debate should compare nutrition, taste and real use, not trends.|Extra virgin olive oil is rich in monounsaturated fat and may bring phenolic compounds.|Coconut oil is richer in saturated fat and has a stronger culinary identity.|For everyday Mediterranean cooking, olive oil remains more versatile and evidence-aligned.
vs-coco|it|Il confronto olio d'oliva e cocco deve parlare di nutrizione, gusto e uso reale, non di mode.|L'extravergine e ricco di grassi monoinsaturi e puo portare composti fenolici.|L'olio di cocco e piu ricco di grassi saturi e ha un'identita aromatica forte.|Per la cucina mediterranea quotidiana, l'olio d'oliva resta piu versatile e coerente.
vs-coco|el|Η σύγκριση ελαιολάδου και καρύδας πρέπει να αφορά διατροφή, γεύση και χρήση, όχι μόδα.|Το εξαιρετικό παρθένο ελαιόλαδο έχει μονοακόρεστα λιπαρά και πιθανές φαινολικές ενώσεις.|Το λάδι καρύδας έχει περισσότερα κορεσμένα και έντονη γευστική ταυτότητα.|Για καθημερινή μεσογειακή κουζίνα, το ελαιόλαδο μένει πιο ευέλικτο και τεκμηριωμένο.
infusees|en|Infused olive oils need flavor imagination and food-safety discipline at the same time.|Dried herbs, dried chili and dehydrated zest are safer than wet fresh ingredients.|Fresh garlic or herbs require short storage, cold conditions and quick use.|Filtering after infusion gives a cleaner flavor and a more serious finished condiment.
infusees|it|Gli oli aromatizzati richiedono fantasia e disciplina di sicurezza alimentare insieme.|Erbe secche, peperoncino secco e scorze disidratate sono piu sicuri degli ingredienti umidi.|Aglio o erbe fresche richiedono conservazione breve, freddo e uso rapido.|Filtrare dopo l'infusione dona gusto piu pulito e condimento piu serio.
infusees|el|Τα αρωματισμένα ελαιόλαδα θέλουν φαντασία και πειθαρχία ασφάλειας μαζί.|Ξηρά βότανα, ξηρό τσίλι και αφυδατωμένο ξύσμα είναι ασφαλέστερα από υγρά φρέσκα υλικά.|Φρέσκο σκόρδο ή βότανα θέλουν σύντομη φύλαξη, ψύξη και γρήγορη χρήση.|Το φιλτράρισμα μετά την έγχυση δίνει καθαρότερη γεύση και πιο σοβαρό καρύκευμα.
ia-moulins|en|AI in olive mills is credible when it improves measurable decisions, not when it replaces taste.|Sensors can help sort fruit by maturity, defects, humidity and lot consistency.|Models can track malaxation time, temperature, flow and yield during extraction.|Human tasting remains essential because efficiency must not erase identity.
ia-moulins|it|L'IA nei frantoi e credibile quando migliora decisioni misurabili, non quando sostituisce il gusto.|Sensori aiutano a selezionare maturita, difetti, umidita e omogeneita dei lotti.|I modelli seguono gramolatura, temperatura, flusso e resa durante l'estrazione.|L'assaggio umano resta essenziale perche l'efficienza non deve cancellare identita.
ia-moulins|el|Η τεχνητή νοημοσύνη στα ελαιοτριβεία πείθει όταν βελτιώνει μετρήσιμες αποφάσεις, όχι όταν αντικαθιστά τη γεύση.|Αισθητήρες βοηθούν στη διαλογή ωριμότητας, ελαττωμάτων, υγρασίας και ομοιογένειας.|Μοντέλα παρακολουθούν μάλαξη, θερμοκρασία, ροή και απόδοση.|Η ανθρώπινη δοκιμή μένει κρίσιμη, γιατί η αποδοτικότητα δεν πρέπει να σβήνει ταυτότητα.
etiquette|en|Reading the label is the fastest way to separate real information from decoration.|Extra virgin is only the beginning; harvest date, producer and origin complete the story.|Vague EU blend wording gives less traceability than a named estate or mill.|Marketing words become credible only when backed by concrete data.
etiquette|it|Leggere l'etichetta e il modo piu rapido per separare informazione reale e decorazione.|Extravergine e solo l'inizio; raccolta, produttore e origine completano la storia.|Miscele UE vaghe danno meno tracciabilita di un frantoio o dominio nominato.|Le parole marketing diventano credibili solo con dati concreti.
etiquette|el|Η ανάγνωση της ετικέτας χωρίζει γρήγορα την πραγματική πληροφορία από τη διακόσμηση.|Το εξαιρετικό παρθένο είναι μόνο αρχή· συγκομιδή, παραγωγός και προέλευση ολοκληρώνουν την ιστορία.|Ασαφές μείγμα ΕΕ δίνει λιγότερη ιχνηλασιμότητα από συγκεκριμένο κτήμα ή ελαιοτριβείο.|Οι λέξεις marketing πείθουν μόνο όταν στηρίζονται σε στοιχεία.
oliviers-millenaires|en|Millennial olive trees deserve more than romance: age, resilience and production limits must all appear.|Ancient trunks show adaptation to drought, pruning and repeated regeneration.|Very old trees can produce symbolic oils, but age alone does not guarantee sensory quality.|The strongest story links landscape protection, heritage and careful harvesting.
oliviers-millenaires|it|Gli olivi millenari meritano piu del romanticismo: eta, resilienza e limiti produttivi devono apparire.|Tronchi antichi mostrano adattamento a siccita, potatura e rigenerazione continua.|Alberi molto vecchi danno oli simbolici, ma l'eta da sola non garantisce qualita sensoriale.|Il racconto forte collega tutela del paesaggio, patrimonio e raccolta accurata.
oliviers-millenaires|el|Οι αιωνόβιες ελιές αξίζουν κάτι περισσότερο από ρομαντισμό: ηλικία, αντοχή και όρια παραγωγής πρέπει να φαίνονται.|Αρχαίοι κορμοί δείχνουν προσαρμογή σε ξηρασία, κλάδεμα και αναγέννηση.|Πολύ παλιά δέντρα δίνουν συμβολικά λάδια, αλλά η ηλικία μόνη δεν εγγυάται γεύση.|Η δυνατή αφήγηση ενώνει προστασία τοπίου, κληρονομιά και προσεκτική συγκομιδή.
notes-degustation|en|Tasting notes become useful when they describe what a buyer can actually perceive.|Fruitiness may be ripe, green, floral, almond-like, grassy or tomato-leaf driven.|Bitterness and pepper are structure, not defects, when they stay clean and balanced.|A serious tasting note avoids poetry that cannot guide food pairing or purchase.
notes-degustation|it|Le note di degustazione servono quando descrivono cio che il compratore puo percepire davvero.|Il fruttato puo essere maturo, verde, floreale, mandorlato, erbaceo o di foglia di pomodoro.|Amaro e piccante sono struttura, non difetti, quando restano puliti ed equilibrati.|Una nota seria evita poesia che non aiuta abbinamento o acquisto.
notes-degustation|el|Οι γευστικές νότες είναι χρήσιμες όταν περιγράφουν αυτό που ο αγοραστής μπορεί να αντιληφθεί.|Το φρουτώδες μπορεί να είναι ώριμο, πράσινο, ανθικό, αμυγδαλένιο, χορτώδες ή φύλλο ντομάτας.|Πίκρα και πικάντικη αίσθηση είναι δομή, όχι ελάττωμα, όταν είναι καθαρές.|Σοβαρή νότα αποφεύγει ποίηση που δεν βοηθά αγορά ή συνδυασμό.
cadeau|en|Giving olive oil as a gift works when the bottle tells a precise and usable story.|A gift oil should show origin, harvest, producer and pairing ideas, not only premium packaging.|A mild oil is safer for general recipients; an intense oil suits curious cooks.|The best gift includes storage advice so the bottle is opened, not forgotten.
cadeau|it|Regalare olio funziona quando la bottiglia racconta una storia precisa e utile.|Un olio regalo deve mostrare origine, raccolta, produttore e idee di abbinamento, non solo confezione premium.|Un olio dolce e piu sicuro; un olio intenso va a chi cucina con curiosita.|Il regalo migliore include conservazione, cosi la bottiglia viene aperta e non dimenticata.
cadeau|el|Το ελαιόλαδο ως δώρο λειτουργεί όταν η φιάλη λέει καθαρή και χρήσιμη ιστορία.|Ένα δώρο πρέπει να δείχνει προέλευση, συγκομιδή, παραγωγό και ιδέες συνδυασμού, όχι μόνο πολυτελή συσκευασία.|Ήπιο λάδι είναι ασφαλέστερο για όλους· έντονο λάδι ταιριάζει σε περίεργους μάγειρες.|Το καλύτερο δώρο δίνει οδηγίες φύλαξης ώστε η φιάλη να ανοιχτεί.
oleiculture-durable|en|Sustainable olive farming must be explained through soil, water, biodiversity and producer choices.|Cover crops and careful pruning can protect soil structure and limit erosion.|Water management matters more each year as harvests face heat and drought stress.|A serious claim describes practices, not just a green vocabulary.
oleiculture-durable|it|L'olivicoltura sostenibile va spiegata con suolo, acqua, biodiversita e scelte del produttore.|Inerbimento e potatura attenta proteggono struttura del suolo ed erosione.|La gestione dell'acqua conta sempre di piu con calore e siccita.|Una promessa seria descrive pratiche, non solo vocabolario verde.
oleiculture-durable|el|Η βιώσιμη ελαιοκαλλιέργεια εξηγείται με έδαφος, νερό, βιοποικιλότητα και επιλογές παραγωγού.|Κάλυψη εδάφους και σωστό κλάδεμα προστατεύουν δομή και περιορίζουν διάβρωση.|Η διαχείριση νερού γίνεται πιο κρίσιμη με ζέστη και ξηρασία.|Σοβαρός ισχυρισμός περιγράφει πρακτικές, όχι μόνο πράσινες λέξεις.
polyphenols|en|Polyphenols connect health interest with sensory reality because they often taste bitter and peppery.|A throat catch can signal phenolic intensity, but it must be clean, not harsh or stale.|Early harvest, fast milling and dark storage help preserve these compounds.|The article should avoid medical promises and explain olive oil inside a complete diet.
polyphenols|it|I polifenoli collegano interesse nutrizionale e realta sensoriale perche spesso danno amaro e piccante.|Il pizzicore in gola puo indicare intensita fenolica, ma deve essere pulito, non duro o stanco.|Raccolta precoce, frangitura rapida e bottiglia scura aiutano a conservarli.|L'articolo deve evitare promesse mediche e inserire l'olio in una dieta completa.
polyphenols|el|Οι πολυφαινόλες ενώνουν διατροφικό ενδιαφέρον και γευστική πραγματικότητα γιατί συχνά δίνουν πίκρα και κάψιμο.|Το κάψιμο στον λαιμό μπορεί να δείχνει φαινολική ένταση, αλλά πρέπει να είναι καθαρό.|Πρώιμη συγκομιδή, γρήγορη έκθλιψη και σκούρα φιάλη τις προστατεύουν.|Το άρθρο πρέπει να αποφεύγει ιατρικές υποσχέσεις και να βάζει το λάδι σε πλήρη διατροφή.
prix-qualite|en|A high olive oil price is credible only when the reasons are visible.|Low yield, early harvest, hand work, small lots and protected packaging can justify cost.|A luxury label without harvest, origin or mill information is a weak signal.|The best buying advice separates everyday cooking oil from finishing oil.
prix-qualite|it|Un prezzo alto dell'olio e credibile solo quando le ragioni sono visibili.|Bassa resa, raccolta precoce, lavoro manuale, piccoli lotti e confezione protetta giustificano il costo.|Un'etichetta lussuosa senza raccolta, origine o frantoio e un segnale debole.|Il miglior consiglio distingue olio quotidiano da olio di finitura.
prix-qualite|el|Υψηλή τιμή ελαιολάδου πείθει μόνο όταν οι λόγοι φαίνονται.|Χαμηλή απόδοση, πρώιμη συγκομιδή, χειρωνακτική δουλειά, μικρές παρτίδες και προστατευμένη συσκευασία δικαιολογούν κόστος.|Πολυτελής ετικέτα χωρίς συγκομιδή, προέλευση ή ελαιοτριβείο είναι αδύναμο σήμα.|Η καλύτερη συμβουλή ξεχωρίζει καθημερινό λάδι από λάδι τελειώματος.
recolte-2026|en|A harvest forecast should stay concrete: weather, flowering, water stress and milling capacity matter.|Quality can rise even when volume falls, especially when fruit is healthy and processed fast.|Heat waves, drought and harvest timing change both yield and aromatic profile.|The useful forecast explains uncertainty instead of pretending to know the future perfectly.
recolte-2026|it|Una previsione di raccolto deve restare concreta: meteo, fioritura, stress idrico e frantoi contano.|La qualita puo salire anche se il volume scende, quando il frutto e sano e lavorato presto.|Caldo, siccita e momento di raccolta cambiano resa e profilo aromatico.|Una previsione utile spiega incertezza invece di fingere certezza assoluta.
recolte-2026|el|Μια πρόβλεψη συγκομιδής πρέπει να μένει συγκεκριμένη: καιρός, άνθηση, στρες νερού και ελαιοτριβεία μετράνε.|Η ποιότητα μπορεί να ανέβει ακόμη κι αν πέσει ο όγκος, όταν ο καρπός είναι υγιής και δουλεύεται γρήγορα.|Καύσωνες, ξηρασία και χρόνος συγκομιδής αλλάζουν απόδοση και άρωμα.|Χρήσιμη πρόβλεψη εξηγεί αβεβαιότητα αντί να προσποιείται βεβαιότητα.
regime-mediterraneen|en|The Mediterranean diet is convincing because olive oil supports a wider pattern, not because it acts alone.|Vegetables, legumes, grains, fish, herbs and simple cooking make the oil meaningful.|Extra virgin oil helps replace less interesting fats while adding flavor and satisfaction.|The serious article avoids miracle claims and focuses on habits that people can keep.
regime-mediterraneen|it|La dieta mediterranea convince perche l'olio sostiene un modello piu ampio, non perche agisce da solo.|Verdure, legumi, cereali, pesce, erbe e cucina semplice danno senso all'olio.|L'extravergine sostituisce grassi meno interessanti aggiungendo gusto e soddisfazione.|L'articolo serio evita miracoli e parla di abitudini sostenibili.
regime-mediterraneen|el|Η μεσογειακή διατροφή πείθει επειδή το ελαιόλαδο στηρίζει ευρύτερο πρότυπο, όχι επειδή δρα μόνο του.|Λαχανικά, όσπρια, δημητριακά, ψάρι, βότανα και απλό μαγείρεμα δίνουν νόημα στο λάδι.|Το εξαιρετικό παρθένο αντικαθιστά λιγότερο ενδιαφέροντα λίπη με γεύση και ικανοποίηση.|Σοβαρό άρθρο αποφεύγει θαύματα και μιλά για συνήθειες που κρατούν.
rituel-recolte|en|The olive harvest ritual is powerful when it shows labor, timing and mill pressure, not nostalgia alone.|Picking too late changes yield, acidity risk and aromatic freshness.|Fast transport to the mill protects fruit before fermentation begins.|The human story matters because coordination decides final oil quality.
rituel-recolte|it|Il rito della raccolta e potente quando mostra lavoro, tempi e pressione del frantoio, non solo nostalgia.|Raccogliere troppo tardi cambia resa, rischio di acidita e freschezza aromatica.|Il trasporto rapido al frantoio protegge il frutto prima della fermentazione.|La storia umana conta perche la coordinazione decide la qualita finale.
rituel-recolte|el|Το τελετουργικό συγκομιδής είναι δυνατό όταν δείχνει εργασία, χρόνο και πίεση ελαιοτριβείου, όχι μόνο νοσταλγία.|Πολύ αργή συγκομιδή αλλάζει απόδοση, κίνδυνο οξύτητας και αρωματική φρεσκάδα.|Γρήγορη μεταφορά στο ελαιοτριβείο προστατεύει τον καρπό πριν αρχίσει ζύμωση.|Η ανθρώπινη ιστορία μετρά επειδή ο συντονισμός αποφασίζει την ποιότητα.
sante-cardiaque|en|Heart-health content must stay careful because it touches a YMYL-style topic.|Olive oil is most credible as part of a complete dietary pattern, not as a treatment.|Replacing less favorable fats can matter more than adding oil on top of everything.|The article should encourage medical advice for personal cardiovascular conditions.
sante-cardiaque|it|Il contenuto sulla salute cardiaca deve restare prudente perche tocca un tema sensibile.|L'olio d'oliva e piu credibile dentro un modello alimentare completo, non come trattamento.|Sostituire grassi meno favorevoli conta piu che aggiungere olio ovunque.|L'articolo deve invitare al parere medico per condizioni cardiovascolari personali.
sante-cardiaque|el|Το περιεχόμενο για καρδιακή υγεία θέλει προσοχή γιατί αγγίζει ευαίσθητο θέμα.|Το ελαιόλαδο είναι πιο αξιόπιστο μέσα σε πλήρες διατροφικό πρότυπο, όχι ως θεραπεία.|Η αντικατάσταση λιγότερο ευνοϊκών λιπαρών μετρά περισσότερο από το να προσθέτουμε λάδι παντού.|Το άρθρο πρέπει να παραπέμπει σε γιατρό για προσωπικά καρδιαγγειακά θέματα.
savon-maison|en|Homemade olive oil soap needs precision before creativity.|Lye calculation, weighing, protective equipment and curing time cannot be improvised.|Olive oil gives mildness and hardness slowly, so patience is part of the recipe.|A serious guide separates inspiration from safety instructions.
savon-maison|it|Il sapone fatto in casa con olio d'oliva richiede precisione prima della creativita.|Calcolo della soda, pesatura, protezioni e stagionatura non si improvvisano.|L'olio d'oliva dona delicatezza e durezza lentamente, quindi la pazienza fa parte della ricetta.|Una guida seria separa ispirazione e istruzioni di sicurezza.
savon-maison|el|Το σπιτικό σαπούνι με ελαιόλαδο θέλει ακρίβεια πριν από δημιουργικότητα.|Υπολογισμός καυστικής σόδας, ζύγισμα, προστασία και ωρίμανση δεν αυτοσχεδιάζονται.|Το ελαιόλαδο δίνει απαλότητα και σκληρότητα αργά, άρα η υπομονή είναι μέρος της συνταγής.|Σοβαρός οδηγός ξεχωρίζει έμπνευση από οδηγίες ασφάλειας.
marseille|en|Real Marseille soap is a tradition of composition, process and patience, not just a name.|Vegetable oils, cauldron cooking and long drying create the expected simplicity.|Color, smell and ingredient list help separate authentic soap from perfume-heavy copies.|The best explanation connects heritage with practical skin and home use.
marseille|it|Il vero sapone di Marsiglia e tradizione di composizione, processo e pazienza, non solo nome.|Oli vegetali, cottura in caldaia e asciugatura lunga creano la sua semplicita.|Colore, odore e lista ingredienti aiutano a separare l'autentico dalle copie profumate.|La spiegazione migliore collega patrimonio e uso pratico per pelle e casa.
marseille|el|Το πραγματικό σαπούνι Μασσαλίας είναι σύνθεση, διαδικασία και υπομονή, όχι μόνο όνομα.|Φυτικά έλαια, μαγείρεμα σε καζάνι και μακρά ξήρανση δίνουν την απλότητα.|Χρώμα, μυρωδιά και λίστα συστατικών ξεχωρίζουν το αυθεντικό από αρωματισμένες απομιμήσεις.|Η καλύτερη εξήγηση ενώνει κληρονομιά και πρακτική χρήση σε δέρμα και σπίτι.
soins-peau|en|DIY skincare with olive oil needs realism because skin tolerance varies widely.|A patch test is more serious than a universal natural claim.|Olive oil may suit dry areas, but it can feel heavy on oily or reactive skin.|Simple formulas are safer than mixing many kitchen ingredients.
soins-peau|it|La skincare fai da te con olio d'oliva richiede realismo perche la tolleranza cutanea varia molto.|Un test su piccola zona e piu serio di una promessa naturale universale.|L'olio puo aiutare zone secche, ma risultare pesante su pelle grassa o reattiva.|Formule semplici sono piu sicure di molte miscele da cucina.
soins-peau|el|Η DIY φροντίδα δέρματος με ελαιόλαδο θέλει ρεαλισμό γιατί η ανοχή διαφέρει πολύ.|Δοκιμή σε μικρή περιοχή είναι πιο σοβαρή από γενική φυσική υπόσχεση.|Το λάδι μπορεί να ταιριάζει σε ξηρά σημεία, αλλά να βαραίνει λιπαρό ή αντιδραστικό δέρμα.|Απλές συνθέσεις είναι ασφαλέστερες από πολλά υλικά κουζίνας.
varietes|en|Olive varieties should be treated like grape varieties: they give useful taste expectations.|Picual often brings structure, bitterness and stability; Arbequina tends to be softer.|Koroneiki can be intense, green and aromatic when harvested well.|Variety matters most when paired with harvest date, region and milling quality.
varietes|it|Le varieta di olive vanno trattate come vitigni: danno aspettative gustative utili.|Picual porta spesso struttura, amaro e stabilita; Arbequina tende alla dolcezza.|Koroneiki puo essere intensa, verde e aromatica se raccolta bene.|La varieta conta davvero insieme a raccolta, regione e qualita del frantoio.
varietes|el|Οι ποικιλίες ελιάς πρέπει να αντιμετωπίζονται σαν ποικιλίες σταφυλιού: δίνουν χρήσιμες γευστικές προσδοκίες.|Η Picual συχνά φέρνει δομή, πίκρα και σταθερότητα· η Arbequina είναι πιο ήπια.|Η Koroneiki μπορεί να είναι έντονη, πράσινη και αρωματική όταν συλλέγεται σωστά.|Η ποικιλία μετρά πραγματικά μαζί με συγκομιδή, περιοχή και ελαιοτριβείο.
"""


SECTION_TITLES = {
    "fr": {
        "title": "Dossier expert du sujet",
        "intro": "Pour que cet article soit vraiment utile, il faut isoler les points qui changent la décision du lecteur. Ce dossier reprend les signaux les plus concrets du sujet et les transforme en repères vérifiables.",
        "decision": "Grille de décision",
    },
    "en": {
        "title": "Expert Topic Dossier",
        "intro": "To make this article genuinely useful, the topic needs a layer of concrete, subject-specific signals. This dossier turns the article's central idea into checks a reader can actually apply.",
        "decision": "Decision grid",
    },
    "it": {
        "title": "Dossier esperto del tema",
        "intro": "Per rendere l'articolo davvero utile, il tema ha bisogno di segnali concreti e specifici. Questo dossier trasforma l'idea centrale in controlli che il lettore puo applicare.",
        "decision": "Griglia di decisione",
    },
    "el": {
        "title": "Εξειδικευμένος φάκελος θέματος",
        "intro": "Για να γίνει το άρθρο πραγματικά χρήσιμο, το θέμα χρειάζεται συγκεκριμένα σήματα. Αυτός ο φάκελος μετατρέπει την κεντρική ιδέα σε ελέγχους που μπορεί να εφαρμόσει ο αναγνώστης.",
        "decision": "Πίνακας απόφασης",
    },
}


def build_dossiers():
    dossiers = {}
    for raw_line in DOSSIER_RAW.strip().splitlines():
        topic, lang, focus, *bullets = raw_line.split("|")
        dossiers[(topic, lang)] = {"focus": focus, "bullets": bullets}
    return dossiers


DOSSIERS = build_dossiers()


def read(path):
    return path.read_text(encoding="utf-8")


def write(path, text):
    path.write_text(text, encoding="utf-8")


def esc(value):
    return html.escape(value, quote=True)


def strip_dossier(text):
    return re.sub(
        r"\n?\s*<!-- topic-dossier:start -->[\s\S]*?<!-- topic-dossier:end -->\s*\n?",
        "\n",
        text,
    )


def parse_lang(text):
    match = re.search(r'<html lang="([^"]+)"', text)
    return match.group(1) if match else "fr"


def parse_title(text, fallback):
    match = re.search(r"<h1>([\s\S]*?)</h1>", text)
    if not match:
        return fallback
    return html.unescape(re.sub(r"<.*?>", "", match.group(1))).strip()


def parse_alternates(text):
    return re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"\s*/?>', text)


def topic_for(path, text, lang):
    if lang == "fr":
        return fr_blog.topic_for(path)
    for alt_lang, href in parse_alternates(text):
        if alt_lang == "fr":
            return fr_blog.topic_for(Path(Path(href).name))
    return fr_blog.topic_for(path)


def fr_dossier(topic):
    data = fr_blog.ARTICLES[topic]
    bullets = []
    for heading, paragraph in data["sections"][:3]:
        first = re.split(r"(?<=[.!?])\s+", paragraph.strip())[0]
        bullets.append(f"{heading} : {first}")
    if len(bullets) < 3:
        bullets.extend(data["checklist"][: 3 - len(bullets)])
    return {
        "focus": data["lede"],
        "bullets": bullets[:3],
    }


def dossier_for(topic, lang):
    if lang == "fr":
        return fr_dossier(topic)
    return DOSSIERS.get((topic, lang))


def render_dossier(topic, lang):
    labels = SECTION_TITLES[lang]
    dossier = dossier_for(topic, lang)
    if not dossier:
        return ""
    bullets = "\n".join(f"            <li>{esc(item)}</li>" for item in dossier["bullets"])
    return f"""
        <!-- topic-dossier:start -->
        <h2>{esc(labels["title"])}</h2>
        <p>{esc(labels["intro"])}</p>
        <p>{esc(dossier["focus"])}</p>
        <ul>
{bullets}
        </ul>
        <!-- topic-dossier:end -->
"""


def insert_dossier(text, topic, lang):
    text = strip_dossier(text)
    block = render_dossier(topic, lang)
    if not block:
        return text
    decision = SECTION_TITLES[lang]["decision"]
    marker = f"        <h2>{decision}</h2>"
    if marker in text:
        return text.replace(marker, block + "\n" + marker, 1)
    return text.replace("</article>", block + "\n    </article>", 1)


def keywords_for(topic, title, lang):
    base = {
        "fr": ["huile d'olive", "huile d'olive vierge extra", "cuisine méditerranéenne"],
        "en": ["olive oil", "extra virgin olive oil", "Mediterranean cooking"],
        "it": ["olio d'oliva", "olio extravergine d'oliva", "cucina mediterranea"],
        "el": ["ελαιόλαδο", "εξαιρετικό παρθένο ελαιόλαδο", "μεσογειακή κουζίνα"],
    }[lang]
    topic_words = re.sub(r"[-_]+", " ", topic)
    return [title, topic_words, *base]


def enhance_jsonld(text, path, topic, lang, title):
    def repl(match):
        try:
            data = json.loads(match.group(1))
        except json.JSONDecodeError:
            return match.group(0)
        data["@type"] = "BlogPosting"
        data["headline"] = title
        data["inLanguage"] = lang
        data["articleSection"] = "Olive oil guide"
        data["keywords"] = keywords_for(topic, title, lang)
        data["datePublished"] = data.get("datePublished", "2026-05-04")
        data["dateModified"] = "2026-05-04"
        data["isAccessibleForFree"] = True
        data["publisher"] = {
            "@type": "Organization",
            "name": "L'Or Vert",
            "url": SITE,
        }
        data["about"] = [
            {"@type": "Thing", "name": title},
            {"@type": "Thing", "name": "Olive oil"},
        ]
        data["mainEntityOfPage"] = f"{SITE}/blog/{path.name}"
        return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False, indent=2)}</script>'

    return re.sub(
        r'<script type="application/ld\+json">([\s\S]*?)</script>',
        repl,
        text,
        count=1,
    )


def improve_file(path):
    text = read(path)
    lang = parse_lang(text)
    if lang not in SECTION_TITLES:
        return False, "unsupported language"
    topic = topic_for(path, text, lang)
    if not topic or topic not in fr_blog.ARTICLES:
        return False, "missing topic"
    title = parse_title(text, path.stem)
    text = insert_dossier(text, topic, lang)
    text = enhance_jsonld(text, path, topic, lang, title)
    write(path, text)
    return True, topic


def main():
    changed = []
    skipped = []
    for path in sorted(BLOG_DIR.glob("*.html")):
        ok, reason = improve_file(path)
        if ok:
            changed.append(path.name)
        else:
            skipped.append((path.name, reason))
    print(f"Improved {len(changed)} blog articles with topic dossiers and richer structured data.")
    if skipped:
        print("Skipped:")
        for name, reason in skipped:
            print(f"- {name}: {reason}")


if __name__ == "__main__":
    main()

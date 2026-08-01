#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix Italian and Greek guide pages with real content."""
import os

DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'guides')

HREFLANG_MAP = {
    'ofeli-igia-elaio-lado.html':           ('bienfaits-sante-huile-olive.html', 'health-benefits-olive-oil.html', 'benefici-salute-olio-oliva.html', 'ofeli-igia-elaio-lado.html'),
    'benefici-salute-olio-oliva.html':          ('bienfaits-sante-huile-olive.html', 'health-benefits-olive-oil.html', 'benefici-salute-olio-oliva.html', 'ofeli-igia-elaio-lado.html'),
    'guida-degustazione-olio-oliva.html':       ('guide-degustation-huile-olive.html', 'olive-oil-tasting-guide.html', 'guida-degustazione-olio-oliva.html', 'odigos-dokimis-elaio-ladou.html'),
    'cucinare-con-olio-oliva.html':             ('cuisiner-avec-huile-olive.html', 'cooking-with-olive-oil.html', 'cucinare-con-olio-oliva.html', 'magirema-me-elaio-lado.html'),
    'processo-produzione-olio-oliva.html':      ('processus-fabrication-huile-olive.html', 'olive-oil-production-process.html', 'processo-produzione-olio-oliva.html', 'diadikasía-paragogís-elaio-ladou.html'),
    'terroir-e-regioni-olio-oliva.html':        ('terroirs-regions-huile-olive.html', 'olive-oil-terroirs-and-regions.html', 'terroir-e-regioni-olio-oliva.html', 'terroirs-kai-periochés-elaio-ladou.html'),
    'come-scegliere-migliore-olio-oliva.html':  ('comment-choisir-huile-olive.html', 'how-to-choose-best-olive-oil.html', 'come-scegliere-migliore-olio-oliva.html', 'pos-na-dialexete-to-kalitero-elaio-lado.html'),
    'consigli-conservazione-olio-oliva.html':   ('conservation-huile-olive-conseils.html', 'olive-oil-storage-tips.html', 'consigli-conservazione-olio-oliva.html', 'simvoules-sintirisis-elaio-ladou.html'),
    'olio-oliva-biologico-e-sostenibile.html':  ('huile-olive-bio-durabilite.html', 'organic-and-sustainable-olive-oil.html', 'olio-oliva-biologico-e-sostenibile.html', 'viologiko-kai-viosimo-elaio-lado.html'),
    'olio-oliva-bellezza-cura-pelle.html':      ('huile-olive-beaute-soins-peau.html', 'olive-oil-beauty-and-skincare.html', 'olio-oliva-bellezza-cura-pelle.html', 'elaio-lado-omorfia-kai-derma.html'),
    'storia-e-cultura-dell-olio-oliva.html':    ('histoire-culture-huile-olive.html', 'history-and-culture-of-olive-oil.html', 'storia-e-cultura-dell-olio-oliva.html', 'istoria-kai-politismos-elaio-ladou.html'),
    'differenza-extra-vergine-e-vergine.html':  ('difference-extra-vierge-vierge.html', 'extra-virgin-vs-virgin-olive-oil.html', 'differenza-extra-vergine-e-vergine.html', 'diafora-extra-partheno-kai-partheno.html'),
    'tendenze-mercato-olio-oliva-2026.html':    ('tendances-marche-huile-olive-2026.html', 'olive-oil-market-trends-2026.html', 'tendenze-mercato-olio-oliva-2026.html', 'taseis-agoras-elaio-ladou-2026.html'),
}

GUIDES_IT = {
    'benefici-salute-olio-oliva.html': {
        'h1': "Benefici dell'Olio d'Oliva per la Salute — Guida Completa",
        'meta': "Scopri i benefici scientificamente provati dell'olio extravergine d'oliva: protezione cardiovascolare, polifenoli anti-infiammatori, salute cerebrale e longevità. Guida 2026.",
        'lede': "Cosa conferma la scienza sull'olio d'oliva e la tua salute.",
        'article': """
<p class="intro">L'olio extravergine d'oliva è uno degli alimenti più studiati dalla medicina preventiva moderna. Con il 73% di acido oleico monoinsaturo e un'eccezionale concentrazione di polifenoli, è al cuore della dieta mediterranea — il modello alimentare associato alla maggiore longevità documentata al mondo.</p>

<h2>Protezione cardiovascolare: le prove scientifiche</h2>
<p>Lo studio PREDIMED, condotto su 7.447 persone ad alto rischio cardiovascolare, ha dimostrato che il consumo regolare di olio extravergine d'oliva riduce del 30% il rischio di infarto e ictus. L'acido oleico abbassa il colesterolo LDL ossidato preservando l'HDL protettivo. I polifenoli idrossitirosolo e oleuropeina rafforzano le pareti arteriose e combattono l'infiammazione vascolare cronica, principale causa delle malattie cardiache.</p>
<blockquote>«L'olio extravergine d'oliva è uno dei pochi alimenti per cui disponiamo di prove cliniche di riduzione della mortalità cardiovascolare.» — NEJM, 2013</blockquote>

<h3>Componenti attivi e loro funzioni</h3>
<ul>
<li><strong>Acido oleico (omega-9)</strong>: riduce il colesterolo LDL e stabilizza le membrane cellulari</li>
<li><strong>Idrossitirosolo</strong>: tra i più potenti antiossidanti conosciuti, riconosciuto dall'EFSA</li>
<li><strong>Oleocantale</strong>: inibisce COX-1 e COX-2 come l'ibuprofene, senza effetti collaterali</li>
<li><strong>Oleuropeina</strong>: proprietà anti-infiammatorie e antimicrobiche documentate</li>
<li><strong>Vitamina E (tocoferoli)</strong>: protegge i lipidi dall'ossidazione perossidativa</li>
</ul>

<h2>Effetti anti-infiammatori e neuroprotettivi</h2>
<p>L'oleocantale — presente solo in oli freschi di qualità — provoca la caratteristica sensazione di bruciore alla gola. Questo composto fenolico inibisce gli stessi enzimi infiammatori dei FANS, ma senza effetti collaterali gastrointestinali. Studi longitudinali mostrano che le popolazioni mediterranee che consumano più di 20ml di olio d'oliva al giorno presentano un declino cognitivo significativamente più lento, con un rischio di Alzheimer ridotto di circa il 40%.</p>

<h3>Apporti consigliati per profilo</h3>
<ul>
<li><strong>Uso generale</strong>: 20–30ml al giorno come condimento crudo o olio di finitura</li>
<li><strong>Protezione cardiovascolare</strong>: 40ml/giorno (protocollo terapeutico PREDIMED)</li>
<li><strong>Cottura</strong>: stabile fino a 210°C — adatto per saltare e arrostire</li>
<li><strong>Uso cosmetico</strong>: poche gocce bastano grazie all'alta densità nutritiva</li>
</ul>
""",
        'faq': [
            ("Quanta olio d'oliva consumare al giorno?", "20–40ml al giorno in sostituzione di altri grassi. Lo studio PREDIMED usava 40ml come dose terapeutica, ma 20ml come condimento quotidiano apporta già benefici misurabili."),
            ("L'olio d'oliva cotto conserva i suoi benefici?", "Parzialmente. L'acido oleico rimane stabile fino a 210°C. I polifenoli resistono alla cottura moderata (180°C) ma si degradano nella frittura prolungata. Per un effetto salute massimo, aggiungete un filo d'olio crudo come finitura."),
            ("Tutti gli oli d'oliva sono ugualmente salutari?", "No. Solo l'olio extravergine di alta qualità contiene polifenoli in concentrazioni terapeutiche. Gli oli raffinati hanno perso quasi tutti i composti bioattivi. Cercate un contenuto di polifenoli superiore a 250mg/kg."),
            ("L'olio d'oliva aiuta contro il diabete di tipo 2?", "Sì — studi dimostrano che l'acido oleico migliora la sensibilità all'insulina e riduce la glicemia postprandiale. La dieta mediterranea arricchita di olio d'oliva è uno dei pochi approcci dietetici con prove cliniche solide nella prevenzione del diabete di tipo 2.")
        ]
    },
    'guida-degustazione-olio-oliva.html': {
        'h1': "Guida Completa alla Degustazione dell'Olio d'Oliva",
        'meta': "Imparate a degustare l'olio d'oliva come un professionista: colore, aromi, amarezza, piccantezza e difetti. Metodo ufficiale COI e consigli pratici.",
        'lede': "Il metodo dei professionisti per riconoscere un grande olio.",
        'article': """
<p class="intro">Degustare l'olio d'oliva è una disciplina. I giudici professionisti del Consiglio Oleicolo Internazionale (COI) seguono un protocollo preciso che valuta tre attributi positivi — fruttato, amaro, piccante — e identifica i difetti che escludono un olio dalla categoria extravergine.</p>

<h2>Il protocollo ufficiale di degustazione</h2>
<p>La degustazione professionale utilizza bicchieri di vetro blu cobalto o marrone opaco per mascherare il colore, evitando pregiudizi visivi. Il bicchiere viene scaldato tra i palmi a circa 28°C per rilasciare i composti aromatici volatili. Il valutatore aspira profondamente, annota gli aromi, poi prende un piccolo sorso e aera l'olio in bocca — tecnica chiamata "stripping" — per amplificare la percezione degli aromi retronasali.</p>
<blockquote>«Il colore dell'olio d'oliva non dice nulla sulla sua qualità. Giudicate con naso e palato, mai con gli occhi.»</blockquote>

<h3>I tre attributi positivi</h3>
<ul>
<li><strong>Fruttato</strong>: intensità e tipo di aromi vegetali — erba fresca, carciofo, mandorla, pomodoro, mela</li>
<li><strong>Amaro</strong>: gusto amaro sulla lingua, segnale di polifenoli — positivo quando equilibrato</li>
<li><strong>Piccante</strong>: sensazione di bruciore alla gola da oleocantale — indicatore di freschezza e qualità</li>
</ul>

<h2>Identificare i difetti comuni</h2>
<p>I difetti organolettici classificano un olio come «vergine» o «lampante» (non idoneo al consumo). Il <em>riscaldo</em> (odore fangoso fermentato) deriva da olive stoccate troppo a lungo prima della frangitura. Il <em>rancido</em> risulta da ossidazione per luce o calore. Un autentico olio extravergine non presenta nessuno di questi difetti. Il test più affidabile a casa: annusatelo direttamente dalla bottiglia — un grande extravergine profuma di vita, freschezza e vegetale.</p>

<h3>Profili aromatici per varietà</h3>
<ul>
<li><strong>Arbequina</strong> (Spagna): delicato, mandorla, frutto maturo, bassa amarezza</li>
<li><strong>Picual</strong> (Spagna): potente, pomodoro, fico, amarezza e piccantezza marcate</li>
<li><strong>Koroneiki</strong> (Grecia): erba fresca, carciofo, piccantezza intensa, alto contenuto di polifenoli</li>
<li><strong>Frantoio</strong> (Italia): carciofo, erba fresca, amarezza equilibrata, molto fruttato</li>
<li><strong>Chemlali</strong> (Tunisia): mandorla, mela verde, profilo delicato e morbido</li>
</ul>
""",
        'faq': [
            ("Perché i degustatori professionisti usano bicchieri colorati?", "Per eliminare i pregiudizi visivi. Il colore non è un indicatore di qualità. Il protocollo COI impone bicchieri blu o marroni opachi affinché il giudizio si basi esclusivamente su aroma e gusto."),
            ("L'amarezza e la piccantezza sono difetti nell'olio d'oliva?", "Al contrario — sono attributi positivi nella valutazione ufficiale. L'amarezza segnala oleuropeina e polifenoli; la piccantezza rivela oleocantale. Un olio senza amarezza né piccantezza è tipicamente raffinato, vecchio o di bassa qualità."),
            ("Come capire se il mio olio è rancido?", "L'olio rancido sa di cera di candela fredda, grasso di frittura stantio o cartone umido. In bocca lascia una sensazione grassa persistente senza freschezza. Non è pericoloso ma è privo di valore gustativo e nutrizionale."),
            ("Si può degustare l'olio d'oliva con il pane?", "Per una valutazione seria, no — il pane modifica la percezione aromatica. I degustatori professionisti usano pane bianco neutro tra un campione e l'altro per pulire il palato, ma non durante la valutazione stessa.")
        ]
    },
    'cucinare-con-olio-oliva.html': {
        'h1': "Cucinare con l'Olio d'Oliva: Segreti e Scienza",
        'meta': "Come cucinare con l'olio d'oliva: punto di fumo, temperature, abbinamenti, frittura e stabilità termica. Fatti scientifici e consigli da chef. Guida 2026.",
        'lede': "Cosa funziona davvero quando si cucina con l'olio d'oliva.",
        'article': """
<p class="intro">Contrariamente al mito diffuso, l'olio extravergine d'oliva si presta perfettamente alla cottura. Il suo punto di fumo di 190–210°C lo rende compatibile con quasi tutte le tecniche culinarie quotidiane, e il suo alto contenuto di acido oleico lo rende chimicamente più stabile al calore della maggior parte degli oli vegetali.</p>

<h2>Temperature e tecniche di cottura</h2>
<p>L'acido oleico (73% della composizione) è altamente resistente all'ossidazione termica. Uno studio pubblicato su <em>Acta Scientific Nutritional Health</em> ha confrontato 10 oli comuni sotto calore e ha rilevato che l'olio extravergine d'oliva produce il minor numero di composti polari — i marcatori di degradazione ossidativa dannosa. Rimane stabile fino a 180°C per la cottura quotidiana e fino a 210°C in breve esposizione.</p>
<blockquote>«L'olio d'oliva non è solo per le insalate. In Italia e in Grecia, tutto si cucina nell'olio d'oliva — anche i fritti.» — Produttore familiare toscano</blockquote>

<h3>Guida alle temperature di riferimento</h3>
<ul>
<li><strong>Condimenti e finitura</strong>: uso crudo, 100% di preservazione degli aromi</li>
<li><strong>Cottura delicata (verdure, uova)</strong>: 100–140°C — ideale, zero degradazione</li>
<li><strong>Saltare in padella, rosolare</strong>: 160–180°C — pienamente adatto</li>
<li><strong>Arrosto al forno</strong>: 180–200°C — stabile, produce un'eccellente doratura</li>
<li><strong>Frittura</strong>: 175–190°C — stabile, ma economicamente meno ottimale</li>
</ul>

<h2>Usi creativi e abbinamenti</h2>
<p>Nella cucina mediterranea, l'olio d'oliva sostituisce il burro nei dolci (texture più morbida, conservazione più lunga), la panna nei purè (cremosità senza pesantezza) e interviene nelle marinature per intenerire le proteine. Il filo d'olio in finitura su un piatto caldo è una tecnica chiave: il calore libera gli aromi fruttati senza alterarli. In dessert, un filo su panna cotta o gelato alla vaniglia crea abbinamenti sorprendenti — l'olio d'oliva di qualità apporta rotondità e complessità che superano il caramello in sofisticazione.</p>

<h3>Regole di abbinamento intensità olio–piatto</h3>
<ul>
<li><strong>Olio delicato, poca amarezza</strong> (Arbequina, Taggiasca): pesce delicato, dolci, frutti di mare</li>
<li><strong>Olio medio, equilibrato</strong> (Frantoio, Aglandau): carni bianche, verdure arrosto, pasta</li>
<li><strong>Olio intenso, amaro e piccante</strong> (Picual, Koroneiki): carni rosse, legumi, insalate robuste</li>
<li><strong>Olio erbaceo di raccolta precoce</strong>: bruschetta, zuppe, piatti provenzali</li>
</ul>
""",
        'faq': [
            ("L'olio d'oliva cotto perde i suoi nutrienti?", "Parzialmente. I polifenoli più volatili si degradano sopra i 180°C, ma l'acido oleico rimane intatto. L'olio conserva i suoi benefici lipidici anche cotto. Per preservare tutti i polifenoli, aggiungete un filo d'olio crudo come finitura."),
            ("Si può riutilizzare l'olio d'oliva dopo la frittura?", "Sì, 2–3 volte al massimo se non si è scurito né ha fumato. Filtratelo caldo per eliminare i residui alimentari che accelerano la degradazione. Gettatelo quando diventa scuro o emana un odore acre."),
            ("L'olio d'oliva è adatto per la maionese?", "Sì, ma un olio troppo intenso può dominare il sapore. Usate un olio delicato (Arbequina, Taggiasca) per le salse fredde, o mescolate olio d'oliva (30%) con olio neutro (70%) per un risultato equilibrato."),
            ("Come fanno gli italiani la pasta aglio e olio?", "Cuocete la pasta al dente, conservate una tazza d'acqua di cottura, scolate. In padella calda, soffriggete brevemente aglio nell'olio (30 secondi), aggiungete la pasta e un mestolo d'acqua di cottura, mescolate vigorosamente. L'amido emulsiona olio e acqua creando una salsa cremosa — senza panna.")
        ]
    },
    'processo-produzione-olio-oliva.html': {
        'h1': "Dall'Albero alla Bottiglia: Il Processo di Produzione dell'Olio d'Oliva",
        'meta': "Guida completa alla produzione dell'olio d'oliva: raccolta, frangitura, gramolazione, estrazione a freddo e filtrazione. Cosa separa un grande olio da uno ordinario.",
        'lede': "Come nasce un grande olio d'oliva — dalla raccolta alla bottiglia.",
        'article': """
<p class="intro">La qualità dell'olio extravergine d'oliva si costruisce ad ogni fase del processo, dalla maturità delle olive all'imbottigliamento. Un solo errore — raccolta tardiva, trasporto eccessivo, temperatura di gramolazione troppo alta — è sufficiente per trasformare un potenziale di eccellenza in olio ordinario.</p>

<h2>La raccolta: la prima decisione critica</h2>
<p>Le olive si raccolgono tra ottobre e gennaio secondo regione e varietà. Gli oli di <em>raccolta precoce</em> (ottobre–novembre), da olive ancora verdi, contengono fino al doppio dei polifenoli e offrono aromi erbacei intensi. La raccolta tardiva (dicembre–gennaio), con olive a piena maturità, dà oli più dolci e fruttati. La raccolta manuale o con pettine meccanico è preferibile: evita lo schiacciamento dei frutti e la fermentazione precoce. Le olive devono raggiungere il frantoio entro 4–6 ore dalla raccolta.</p>
<blockquote>«Tra la raccolta e la frangitura, ogni ora conta. Le nostre olive entrano al frantoio entro 4 ore dalla colta.» — Produttore AOP Baux-de-Provence</blockquote>

<h3>Fasi chiave della produzione</h3>
<ul>
<li><strong>Raccolta</strong>: manuale, a pettine o con reti — lo schiacciamento degrada irreversibilmente la qualità</li>
<li><strong>Defogliatrice e lavaggio</strong>: entro 4–6 ore massimo dalla raccolta</li>
<li><strong>Frangitura</strong>: molazze di granito tradizionali o frangitori a martelli moderni</li>
<li><strong>Gramolazione</strong>: pasta mescolata 20–40 min a max 27°C (estrazione a freddo)</li>
<li><strong>Centrifugazione orizzontale</strong>: separa olio, acqua vegetale e sansa</li>
<li><strong>Filtrazione</strong>: opzionale ma raccomandata per la conservazione</li>
</ul>

<h2>L'estrazione a freddo: il criterio determinante</h2>
<p>La menzione «estratto a freddo» garantisce che la temperatura di gramolazione non abbia superato i 27°C. Oltre questa soglia, gli enzimi che degradano i polifenoli si attivano, gli aromatici volatili evaporano e la resa aumenta a scapito della qualità. Una resa più alta (più olio per quintale di olive) è spesso segnale di estrazione a caldo — economicamente più redditizia ma qualitativamente inferiore.</p>

<h3>Fattori che definiscono l'eccellenza</h3>
<ul>
<li><strong>Ritardo raccolta–frangitura</strong>: meno di 6 ore per i grandi oli</li>
<li><strong>Temperatura di gramolazione</strong>: 27°C massimo — non negoziabile</li>
<li><strong>Durata della gramolazione</strong>: 25–35 minuti (né troppo breve né troppo lunga)</li>
<li><strong>Varietà e maturità delle olive</strong>: specifiche per ogni terroir</li>
<li><strong>Stoccaggio in acciaio inox sotto azoto</strong>: previene l'ossidazione dopo l'estrazione</li>
</ul>
""",
        'faq': [
            ("Qual è la differenza tra estrazione a freddo e prima spremitura a freddo?", "'Prima spremitura a freddo' è un termine storico dei vecchi frantoi idraulici, oggi obsoleti. 'Estratto a freddo' è il termine regolamentare UE attuale, che garantisce una temperatura di gramolazione ≤ 27°C. Entrambi indicano produzione a bassa temperatura."),
            ("Quante olive ci vogliono per produrre un litro d'olio?", "In media 4–6 kg di olive per litro, secondo varietà, maturità e metodo di estrazione. Le olive precoci richiedono talvolta 7–8 kg. Le varietà tardive ricche d'olio possono scendere a 3–4 kg per litro."),
            ("Le molazze di pietra sono migliori dei frangitori moderni?", "Dibattito legittimo. Le molazze di pietra frantumanno più delicatamente, preservando l'integrità cellulare. Ma si scaldano e ossidano più facilmente. I frangitori a martelli moderni, ben condotti, producono oli di uguale qualità con migliore riproducibilità."),
            ("Perché alcuni oli d'oliva sono torbidi?", "La torbidità deriva da microparticelle di polpa e cere naturali dell'oliva. Scompare con la filtrazione o la decantazione naturale. Un olio non filtrato è inizialmente più ricco di aromi a breve termine, ma meno stabile — consumatelo più rapidamente.")
        ]
    },
    'terroir-e-regioni-olio-oliva.html': {
        'h1': "Terroir e Regioni: Le Grandi Origini dell'Olio d'Oliva",
        'meta': "Spagna, Italia, Grecia, Tunisia, Francia: scoprite i grandi terroir oleicoli del mondo, le loro varietà emblematiche e i profili aromatici distintivi.",
        'lede': "Da dove vengono i migliori oli del mondo — e cosa li rende unici.",
        'article': """
<p class="intro">Come il vino, l'olio d'oliva è profondamente segnato dal suo terroir — suolo, clima, altitudine, varietà di oliva e know-how locale. Un Koroneiki del Peloponneso e un Arbequina della Catalogna sono due espressioni radicalmente diverse dello stesso frutto, plasmate da millenni di adattamento ai loro ambienti specifici.</p>

<h2>Le grandi regioni produttrici mondiali</h2>
<p>Il bacino mediterraneo concentra il 95% della produzione mondiale. La Spagna è il primo produttore (45% della produzione globale), principalmente dall'Andalusia con le varietà Picual, Hojiblanca e Arbequina. La Grecia, con solo il 2% della popolazione mondiale, produce il 10% dell'olio d'oliva globale e consuma la maggior quantità pro capite (20 litri/anno). L'Italia, nonostante volumi inferiori, guida per valore grazie alle prestigiose DOP. La Tunisia è il principale esportatore mondiale non UE.</p>
<blockquote>«Ogni regione dà all'olio d'oliva il proprio linguaggio. Il Peloponneso parla di erba tagliata e carciofo; la Toscana dice carciofo e pepe verde.»</blockquote>

<h3>Profili delle principali regioni</h3>
<ul>
<li><strong>Andalusia (Spagna)</strong>: Picual — potente, robusto, fruttato verde intenso, ottima conservazione</li>
<li><strong>Catalogna (Spagna)</strong>: Arbequina — delicata, frutto maturo, mandorla, note di mela</li>
<li><strong>Toscana (Italia)</strong>: Frantoio e Moraiolo — erba fresca, carciofo, amarezza e piccantezza marcate</li>
<li><strong>Peloponneso (Grecia)</strong>: Koroneiki — piccola oliva, alto contenuto di polifenoli, piccantezza intensa</li>
<li><strong>Sfax (Tunisia)</strong>: Chemlali — mandorla dolce, frutto maturo, grande finezza</li>
<li><strong>Provenza (Francia)</strong>: DOP Vallée des Baux, Aglandau e Salonenque — erba, mandorla, carciofo</li>
</ul>

<h2>L'importanza delle DOP e IGP</h2>
<p>Le Denominazioni di Origine Protetta garantiscono che l'olio sia prodotto, trasformato e confezionato in una zona geografica delimitata, con varietà e metodi definiti dal disciplinare. L'UE riconosce oltre 150 DOP oleicole. Queste certificazioni proteggono i produttori dalla frode e guidano i consumatori verso oli tracciabili e autentici.</p>

<h3>Come il terroir influenza il gusto</h3>
<ul>
<li><strong>Suolo calcareo e secco</strong>: oli intensi, ricchi di polifenoli</li>
<li><strong>Suolo argilloso e profondo</strong>: profili più delicati e fruttati</li>
<li><strong>Alta quota (&gt;400m)</strong>: maturazione lenta, aromi complessi, polifenoli elevati</li>
<li><strong>Prossimità al mare</strong>: note iodate sottili, fruttato più leggero</li>
<li><strong>Clima arido</strong>: stress idrico = maggiore concentrazione aromatica</li>
</ul>
""",
        'faq': [
            ("Quale paese produce il miglior olio d'oliva al mondo?", "Non esiste una risposta assoluta — è una questione di preferenze gustative. I concorsi internazionali (Biol, EVOO World Rankings, NYIOOC) premiano regolarmente oli da Grecia, Spagna, Italia, Marocco e Australia."),
            ("Perché gli oli greci sono così ricchi di polifenoli?", "Tre fattori: la varietà Koroneiki (naturalmente ricca di fenoli), le condizioni climatiche mediterranee aride che stressano l'ulivo e concentrano i composti difensivi, e la tradizione di raccolta precoce (olive ancora verdi) in molte regioni del Peloponneso e di Creta."),
            ("Gli oli d'oliva francesi valgono il prezzo premium?", "Sì, per chi cerca profili aromatici unici e massima tracciabilità. La produzione francese è molto ridotta (5.000–10.000 tonnellate/anno contro 1,3 milioni in Spagna), quindi inevitabilmente più costosa. Le DOP Baux-de-Provence e Nyons sono veri tesori gastronomici."),
            ("Cosa distingue l'olio tunisino dagli oli europei?", "La Tunisia produce principalmente oli dolci e fruttati da Chemlali e Chétoui, generalmente meno amari di quelli europei. Le condizioni climatiche del Sahel creano un profilo molto diverso: più mandorla, meno vegetale, con una rotondità apprezzata nella cucina orientale.")
        ]
    },
    'come-scegliere-migliore-olio-oliva.html': {
        'h1': "Come Scegliere il Miglior Olio d'Oliva: Guida all'Acquisto",
        'meta': "Come scegliere un buon olio d'oliva: leggere l'etichetta, polifenoli, acidità, DOP, data di raccolta e segnali di qualità. Guida esperta 2026.",
        'lede': "I criteri che separano un grande olio da uno qualsiasi.",
        'article': """
<p class="intro">Il reparto olio d'oliva di un supermercato può sembrare omogeneo, ma le differenze di qualità sono abissali. Tra un olio a 3€ al litro e uno artigianale a 25€, non è solo l'etichetta a cambiare — è la composizione chimica, il profilo aromatico e l'impatto sulla salute.</p>

<h2>Leggere l'etichetta: le informazioni chiave</h2>
<p>La prima distinzione è la categoria: solo la menzione <strong>«Extravergine»</strong> garantisce un'acidità libera inferiore allo 0,8% e l'assenza di difetti organolettici. Il «Vergine» (acidità ≤ 2%) presenta lievi difetti; l'«Olio d'oliva» è una miscela di olio raffinato e vergine, praticamente senza polifenoli. La <strong>data di raccolta</strong> è più informativa della data di scadenza: un olio del raccolto precedente è ancora sicuro ma ha perso il suo picco aromatico. Cercate una raccolta recente, idealmente degli ultimi 12 mesi.</p>
<blockquote>«La data di raccolta è l'indicatore di freschezza più onesto che un produttore possa darvi.»</blockquote>

<h3>Criteri di selezione in ordine di priorità</h3>
<ul>
<li><strong>Menzione «Extravergine»</strong>: il minimo non negoziabile</li>
<li><strong>Data di raccolta</strong>: preferite un olio raccolto negli ultimi 12–18 mesi</li>
<li><strong>DOP/IGP o certificazione</strong>: garantisce origine e metodi</li>
<li><strong>Contenuto di polifenoli</strong>: idealmente &gt;250mg/kg (indicato sulle bottiglie premium)</li>
<li><strong>Confezionamento</strong>: vetro scuro o latta opaca — la luce degrada l'olio</li>
<li><strong>Origine singola</strong>: evitate «miscela di paesi UE» per acquisti premium</li>
</ul>

<h2>Il prezzo come indicatore di qualità</h2>
<p>Un olio extravergine di qualità non può costare meno di 8–10€ al litro nella distribuzione tradizionale. I soli costi di produzione (raccolta manuale, trasporto, estrazione a freddo) superano i 5€ al litro per i piccoli produttori. Gli oli a 3–4€ al litro in grande distribuzione sono miscele multi-origine, spesso di raccolto vecchio, con profili polifenolici molto bassi.</p>

<h3>Segnali d'allarme da evitare</h3>
<ul>
<li>Nessuna data di raccolta (solo una data di scadenza)</li>
<li>«Miscela di paesi UE e non UE» senza specificazione</li>
<li>Prezzo inferiore a 7–8€ al litro per un presunto premium</li>
<li>Bottiglia trasparente esposta alla luce sullo scaffale</li>
<li>Nessun aroma all'apertura della bottiglia</li>
</ul>
""",
        'faq': [
            ("Un olio torbido è un segnale di qualità?", "Non necessariamente. La torbidità indica un olio non filtrato, più ricco di aromi a breve termine ma più fragile da conservare. È una scelta del produttore, non un criterio assoluto di qualità. Un olio filtrato e limpido può superare di gran lunga uno torbido mal conservato."),
            ("Gli oli bio sono sistematicamente migliori?", "La certificazione bio garantisce l'assenza di pesticidi sintetici, non la qualità gustativa o la ricchezza di polifenoli. Un olio bio può essere mediocre se la raccolta è tardiva o il processo trascurato."),
            ("Ci si può fidare di medaglie e premi in etichetta?", "I grandi concorsi (NYIOOC, EVOO World Rankings, TerraOlivo, Biol) hanno pannelli rigorosi di degustazione alla cieca — le loro medaglie sono un segnale affidabile. Una medaglia d'oro al NYIOOC o al Biol è un indicatore serio di qualità eccezionale."),
            ("Qual è la differenza tra olio delicato e intenso?", "L'intensità dipende da varietà, tempi di raccolta e terroir. 'Delicato' significa poca amarezza e piccantezza (Arbequina, raccolta tardiva) — ideale per pesce, dolci, principianti. 'Intenso' significa amarezza e piccantezza marcate (Picual, Koroneiki, raccolta precoce) — ideale per carni, legumi e uso salute.")
        ]
    },
    'consigli-conservazione-olio-oliva.html': {
        'h1': "Consigli per la Conservazione dell'Olio d'Oliva",
        'meta': "Come conservare correttamente l'olio d'oliva: luce, calore, aria, contenitori e durata. Evitate gli errori che rovinano il vostro olio in poche settimane.",
        'lede': "Le regole di conservazione per preservare qualità e benefici.",
        'article': """
<p class="intro">L'olio d'oliva è fragile. Tre nemici lo degradano silenziosamente: luce, calore e ossigeno. Una bottiglia perfetta può diventare rancida in poche settimane se conservata male. Queste regole vi aiuteranno a preservare i vostri oli fino all'ultima goccia.</p>

<h2>I tre nemici dell'olio d'oliva</h2>
<p>La <strong>luce</strong> scatena reazioni foto-ossidative che degradano i polifenoli. Bottiglie in vetro scuro o latte opache sono indispensabili — mai in vetro trasparente su un piano di lavoro esposto. Il <strong>calore</strong> accelera l'ossidazione: non conservate mai vicino a fornelli, forni o in pieno sole. L'<strong>ossigeno</strong> ossida i lipidi progressivamente: richiudete sempre il tappo e, per i contenitori grandi, trasvosate in bottiglie più piccole man mano che consumate.</p>
<blockquote>«Un olio lasciato quotidianamente sul piano di lavoro in una bottiglia trasparente perde il 30% dei suoi polifenoli in un mese.»</blockquote>

<h3>Condizioni ideali di conservazione</h3>
<ul>
<li><strong>Temperatura</strong>: 14–18°C idealmente, massimo 20°C — cantina o credenza fresca</li>
<li><strong>Luce</strong>: buio totale — latta opaca o credenza chiusa</li>
<li><strong>Ossigeno</strong>: tappo ermetico, bottiglia riempita al massimo</li>
<li><strong>Umidità</strong>: ambiente secco — l'umidità favorisce le muffe sul tappo</li>
<li><strong>Durata ottimale</strong>: consumare entro 18 mesi dalla data di raccolta</li>
</ul>

<h2>Si può conservare l'olio d'oliva in frigorifero?</h2>
<p>Il frigorifero non è raccomandato per l'uso quotidiano: l'olio si solidifica sotto i 7°C e si intorbidisce intorno ai 10°C. Questo fenomeno è reversibile, ma i cicli ripetuti freddo–caldo possono accelerare l'ossidazione. Tuttavia, per oli di grande valore che consumate lentamente, la conservazione in frigorifero può prolungare la durata oltre i 24 mesi. I migliori produttori conservano le riserve in serbatoi di acciaio inox a temperatura controllata (12–15°C) sotto azoto per evitare qualsiasi contatto con l'ossigeno.</p>

<h3>Durata di conservazione per tipo di contenitore</h3>
<ul>
<li><strong>Latta da 3–5L ermetica</strong>: 24–30 mesi chiusa</li>
<li><strong>Bottiglia in vetro scuro</strong>: 18–24 mesi chiusa, 3–6 mesi dopo apertura</li>
<li><strong>Caraffa aperta in cucina</strong>: 2–4 settimane massimo</li>
<li><strong>Flacone trasparente</strong>: da evitare — si degrada in pochi giorni alla luce</li>
</ul>
""",
        'faq': [
            ("Come capire se il mio olio d'oliva è ancora buono?", "Annusatelo: un buon olio ha aromi fruttati, vegetali o di mandorla. Se sa di cera di candela, cartone umido o grasso stantio, è ossidato. In bocca, se è piatto, grasso e senza freschezza, ha perso polifenoli e aromi."),
            ("Si può congelare l'olio d'oliva per conservarlo a lungo?", "Tecnicamente sì — il congelamento blocca l'ossidazione. Ma la scongelazione può causare separazione dei composti se troppo rapida. Se congelate, scongelate lentamente in frigorifero. Il risultato è accettabile ma aromi delicati e texture possono leggermente risentirne."),
            ("L'olio d'oliva scade davvero?", "Non 'marcisce' nel senso alimentare, ma irrancidisce. L'olio rancido non presenta un rischio sanitario grave, ma perde tutto il suo valore: niente polifenoli, niente aromi, sapore sgradevole."),
            ("Si può usare l'olio d'oliva per conservare alimenti?", "Sì — tecnica tradizionale per erbe aromatiche, formaggi e verdure grigliate. L'olio crea una barriera anaerobica che inibisce i batteri aerobici. Attenzione: l'aglio fresco conservato nell'olio a temperatura ambiente presenta rischio di botulismo — fatelo solo in frigorifero e consumate entro una settimana.")
        ]
    },
    'olio-oliva-biologico-e-sostenibile.html': {
        'h1': "Olio d'Oliva Biologico e Sostenibile: Cosa Sapere",
        'meta': "Cosa garantiscono le certificazioni bio, impatto ambientale dell'olivicoltura e come scegliere un olio davvero rispettoso dell'ambiente. Guida esperta 2026.",
        'lede': "Sostenibilità e biologia olivicola: cosa significano davvero le etichette.",
        'article': """
<p class="intro">La filiera oleicola affronta un paradosso: l'ulivo è uno degli alberi più resilienti ed ecologicamente virtuosi esistenti, ma la pressione economica e climatica spinge alcuni produttori verso pratiche intensive che minacciano questo equilibrio millenario.</p>

<h2>Cosa garantisce (e non garantisce) la certificazione bio</h2>
<p>La certificazione biologica (UE BIO, USDA Organic, AB in Francia) garantisce l'assenza di pesticidi sintetici, erbicidi chimici e OGM. Impone pratiche agronomiche rispettose del suolo e della biodiversità. Cosa non garantisce: qualità gustativa, ricchezza di polifenoli o benessere animale. Un olio bio può essere prodotto industrialmente su larga scala da olive raccolte tardivamente e mal estratte. Il marchio bio è necessario ma non sufficiente per una qualità eccezionale.</p>
<blockquote>«L'ulivo cresce senza irrigazione né input chimici da 3.000 anni. Il bio per l'ulivo è in un certo senso il suo stato naturale.»</blockquote>

<h3>Certificazioni chiave da conoscere</h3>
<ul>
<li><strong>UE BIO / AB</strong>: certificato senza pesticidi sintetici — standard UE</li>
<li><strong>Demeter</strong>: biodinamico — requisiti ancora più severi dello standard bio</li>
<li><strong>DOP/IGP</strong>: origine e metodi controllati — non necessariamente bio, ma tracciabile</li>
<li><strong>Rainforest Alliance</strong>: gestione ambientale e sociale sostenibile</li>
<li><strong>Fair Trade</strong>: equità commerciale per i piccoli produttori</li>
</ul>

<h2>L'impatto ambientale dell'olivicoltura</h2>
<p>Un uliveto tradizionale è un significativo pozzo di carbonio: un ettaro di ulivi sequestra 2,5–4 tonnellate di CO₂ all'anno. La coltivazione estensiva favorisce la biodiversità e protegge il suolo dall'erosione grazie alle radici profonde. I sistemi intensivi moderni — con alta densità di piantagione (&gt;1.000 alberi/ha contro 50–150 in estensivo) e irrigazione intensiva — presentano un bilancio carbonico meno favorevole e riducono la biodiversità.</p>

<h3>Come scegliere un olio davvero sostenibile</h3>
<ul>
<li><strong>Uliveti estensivi tradizionali</strong>: densità &lt;200 alberi/ha, senza irrigazione</li>
<li><strong>Piccoli produttori certificati bio</strong>: impatto minimo, tracciabilità massima</li>
<li><strong>Oli locali e filiera corta</strong>: impronta carbonica del trasporto ridotta</li>
<li><strong>Confezionamento in sfuso o grande formato</strong>: meno imballaggi per litro consumato</li>
<li><strong>Valorizzazione della sansa</strong>: il sottoprodotto usato per energia, cosmetici o compost</li>
</ul>
""",
        'faq': [
            ("La conversione al bio migliora la qualità dell'olio?", "Non automaticamente. La qualità dipende molto di più da varietà, momento di raccolta e controllo dell'estrazione. Tuttavia, i produttori bio tendono ad essere più attenti all'intera catena produttiva."),
            ("L'olio d'oliva è un prodotto ecologico?", "Rispetto ad altri oli vegetali (palma, colza intensivo, soia), l'ulivo tradizionale ha un eccellente bilancio ambientale: poca acqua, pochi input, pozzo di carbonio efficace, longevità straordinaria. L'olivicoltura intensiva è più discutibile."),
            ("Cosa succede alla sansa dopo l'estrazione?", "La sansa viene valorizzata in vari modi: come combustibile per caldaie, come olio di sansa (estrazione con solvente esano), come compost agricolo, o in cosmetica (scrub, saponi). I frantoi moderni puntano a valorizzare il 100% della materia prima."),
            ("Esistono certificazioni per oli ad alto contenuto di polifenoli?", "Sì. L'EFSA autorizza un'indicazione sulla salute per gli oli contenenti più di 250mg/kg di polifenoli. Alcuni produttori fanno certificare questo contenuto da laboratori accreditati e lo riportano in etichetta.")
        ]
    },
    'olio-oliva-bellezza-cura-pelle.html': {
        'h1': "Olio d'Oliva per la Bellezza e la Cura della Pelle",
        'meta': "Olio d'oliva in cosmetica: idratazione, anti-età, cura del viso e del corpo. Formule fai-da-te, precauzioni e confronto con oli cosmetici moderni.",
        'lede': "Il segreto di bellezza antico — validato dalla scienza moderna.",
        'article': """
<p class="intro">Da quando Cleopatra si bagnava in olio d'oliva e latte, le donne mediterranee hanno usato l'olio d'oliva come trattamento di bellezza completo. La scienza moderna valida questi usi ancestrali: squalene, tocoferoli e polifenoli lo rendono un cosmetico attivo straordinario.</p>

<h2>Proprietà cosmetiche attive</h2>
<p>L'olio d'oliva contiene diversi composti direttamente benefici per la pelle. Lo <strong>squalene</strong> (0,3–1%) è un emolliente naturale identico a quello prodotto dal nostro sebo — penetra senza residui grassi e idrata in profondità. I <strong>tocoferoli</strong> (vitamina E) proteggono le membrane cellulari dall'ossidazione dei radicali liberi, il meccanismo centrale dell'invecchiamento cutaneo. L'<strong>idrossitirosolo</strong> esercita un'azione antinfiammatoria documentata che calma le pelli sensibili e reattive. Queste proprietà esistono solo nell'extravergine di qualità.</p>
<blockquote>«L'olio extravergine d'oliva contiene oltre 200 fitochimici attivi, molti con efficacia cosmetica paragonabile agli attivi sintetici di alta gamma.»</blockquote>

<h3>Usi cosmetici più efficaci</h3>
<ul>
<li><strong>Struccante</strong>: scioglie il trucco a base oleosa e waterproof senza aggressioni — sicuro anche sul contorno occhi</li>
<li><strong>Balsamo labbra</strong>: poche gocce pure su labbra screpolate — sollievo immediato</li>
<li><strong>Cura delle cuticole</strong>: massaggio quotidiano nutre e ammorbidisce la pelle attorno alle unghie</li>
<li><strong>Doposole</strong>: lenisce le arrossature e nutre la pelle seccata dal sole</li>
<li><strong>Maschera nutriente</strong>: 2 cucchiai sul viso asciutto, 15 minuti, risciacquo con acqua tiepida</li>
<li><strong>Olio corpo</strong>: applicato su pelle leggermente umida dopo la doccia</li>
</ul>

<h2>Precauzioni e controindicazioni</h2>
<p>L'olio d'oliva non è adatto a tutti i tipi di pelle. Il suo moderato indice comedogenico (2 su 5) lo rende sconsigliato per le pelli grasse, miste o acneiche — può occludere i pori e peggiorare i comedoni. Per questi profili, scegliete oli più leggeri (jojoba, rosa canina, nocciola). Le pelli normali e secche tollerano e beneficiano molto dell'olio d'oliva come trattamento occlusivo notturno. Per eczema o dermatite, consultate un dermatologo prima dell'uso sistematico.</p>

<h3>Formule fai-da-te semplici ed efficaci</h3>
<ul>
<li><strong>Scrub corpo</strong>: 3 cucchiai olio d'oliva + 2 cucchiai zucchero di canna + scorza di limone</li>
<li><strong>Maschera capelli</strong>: olio d'oliva tiepido sulle lunghezze, 30 min sotto un asciugamano caldo, shampoo</li>
<li><strong>Crema mani</strong>: mescolare olio d'oliva, cera d'api fusa e olio essenziale di lavanda</li>
<li><strong>Bagno piedi nutriente</strong>: acqua tiepida + olio d'oliva + qualche goccia di tea tree</li>
</ul>
""",
        'faq': [
            ("L'olio d'oliva è adatto a tutti i tipi di pelle del viso?", "No. Si adatta a pelli secche, normali e mature. Non è raccomandato per pelli grasse e acneiche a causa del moderato potenziale comedogenico. Per pelli sensibili, fate un patch test su una piccola zona prima dell'uso esteso."),
            ("Si può sostituire la crema idratante con l'olio d'oliva?", "Parzialmente. L'olio d'oliva è un eccellente emolliente (ammorbidisce e nutre) ma non un umettante (non attira acqua nella pelle come l'acido ialuronico). Per un'idratazione ottimale: applicatelo su pelle leggermente umida dopo la doccia."),
            ("Quale olio d'oliva scegliere per uso cosmetico?", "Extravergine di alta qualità, con data di raccolta recente. I prodotti cosmetici a base di olio d'oliva raffinato hanno perso i loro composti bioattivi — controproducente per un uso bellezza. Scegliete la stessa qualità che mettereste nel piatto."),
            ("L'olio d'oliva aiuta a prevenire le smagliature?", "Può aiutare in prevenzione per le donne in gravidanza, nutrendo e ammorbidendo la pelle, migliorandone l'elasticità. Su smagliature già formate (cicatrici bianche), l'effetto è limitato. I migliori risultati preventivi si ottengono con applicazione quotidiana dall'inizio della gravidanza.")
        ]
    },
    'storia-e-cultura-dell-olio-oliva.html': {
        'h1': "Storia e Cultura dell'Olio d'Oliva: 5.000 Anni di Civiltà",
        'meta': "La storia dell'olio d'oliva dall'antichità a oggi: mitologia greca, Roma antica, commercio medievale e ruolo culturale universale tra le civiltà.",
        'lede': "Cinquemila anni di storia in ogni goccia di olio d'oliva.",
        'article': """
<p class="intro">Nessun altro alimento ha svolto un ruolo più centrale nella storia umana dell'olio d'oliva. Moneta di scambio, combustibile sacro, medicinale, cosmetico e alimento: l'olio d'oliva ha accompagnato la nascita delle civiltà mediterranee per oltre cinque millenni.</p>

<h2>Dalle origini mitiche alla realtà archeologica</h2>
<p>L'ulivo coltivato (<em>Olea europaea</em>) emerse da un processo di domesticazione risalente a 6.000 a.C. in Anatolia e nel Levante. Le prime prove di estrazione dell'olio risalgono a 4.000 a.C. ad Haifa (attuale Israele). I Greci antichi fecero dell'ulivo un simbolo sacro: nella mitologia, fu Atena a donare l'ulivo ad Atene. I vincitori olimpici ricevevano corone di rami di ulivo selvatico — il <em>kotinos</em> — e anfore di olio d'oliva attico come premio.</p>
<blockquote>«L'ulivo è la civiltà mediterranea stessa. Dove cresce l'ulivo, l'uomo si insedia, coltiva e crea.» — Fernand Braudel, storico</blockquote>

<h3>Tappe principali della storia oleicola</h3>
<ul>
<li><strong>4.000 a.C.</strong>: prime prove di estrazione nel Levante e nella Creta minoica</li>
<li><strong>776 a.C.</strong>: l'olio d'oliva come premio ai primi Giochi Olimpici</li>
<li><strong>II sec. a.C.</strong>: Roma diventa il più grande importatore mondiale di olio d'oliva</li>
<li><strong>I sec. d.C.</strong>: Hispania (Spagna) supera la Grecia in volume di produzione</li>
<li><strong>VII sec.</strong>: l'espansione araba diffonde l'ulivo in Nord Africa e Spagna</li>
<li><strong>XV sec.</strong>: i conquistatori spagnoli piantano ulivi in America Latina</li>
</ul>

<h2>L'olio d'oliva nelle grandi religioni e culture</h2>
<p>L'olio d'oliva trascende culture e religioni. Nella Bibbia, l'ulivo è simbolo di pace (la colomba di Noè riporta un ramo d'ulivo). La Chiesa cattolica usa l'olio d'oliva in tutti i suoi sacramenti. Il Corano menziona l'ulivo come albero benedetto. In Grecia e in Italia, i rituali legati alla raccolta delle olive rimangono momenti di coesione sociale e familiare, trasmessi di generazione in generazione.</p>

<h3>L'ulivo come patrimonio vivente</h3>
<ul>
<li>Alcuni ulivi in Sardegna, Creta e Palestina hanno più di <strong>2.000 anni</strong></li>
<li>L'ulivo di Vouves in Creta è stimato a <strong>3.000–4.000 anni</strong> e produce ancora olive</li>
<li>Gli uliveti storici sono iscritti nel <strong>Patrimonio Mondiale UNESCO</strong> in Grecia e Portogallo</li>
<li>La <strong>dieta mediterranea</strong> è iscritta nel Patrimonio Culturale Immateriale UNESCO</li>
</ul>
""",
        'faq': [
            ("Quale paese ha inventato l'olio d'oliva?", "La domesticazione dell'ulivo avvenne simultaneamente in diverse regioni del Medio Oriente e del Mediterraneo orientale — Siria, Libano, Palestina, Creta — tra 6000 e 4000 a.C. Non esiste un unico 'inventore': fu una scoperta progressiva condivisa da più civiltà."),
            ("Come usavano l'olio d'oliva i Romani?", "I Romani avevano un consumo stimato di 20–40 litri di olio d'oliva pro capite all'anno. Lo usavano per cucinare, illuminarsi (lampade a olio), profumarsi, lavarsi (strigile + olio al posto del sapone) e come medicinale. Roma importava massicciamente da Hispania e Nord Africa."),
            ("Perché il ramo d'ulivo è simbolo di pace?", "Il simbolismo risale alla Genesi biblica (la colomba che porta un ramo d'ulivo dopo il Diluvio) e alla tradizione greca (gli ulivi erano piantati nei luoghi sacri dove la violenza era proibita). L'ONU usa il ramo d'ulivo nel suo emblema dal 1945."),
            ("Esistono ulivi antichissimi ancora produttivi?", "Sì. L'ulivo di Vouves in Creta, stimato a 3.000–4.000 anni, produce ancora olive raccolte annualmente. In Sardegna, diversi ulivi millenari sono attivi. Gli 'Ses Oliveres Velles' a Maiorca sono stimati a 1.000 anni e ancora produttivi.")
        ]
    },
    'differenza-extra-vergine-e-vergine.html': {
        'h1': "Extravergine vs Vergine: Capire le Categorie dell'Olio d'Oliva",
        'meta': "La differenza tra olio extravergine, vergine e comune: acidità, difetti, polifenoli, usi e prezzo. Confronto completo e guida all'acquisto.",
        'lede': "Extravergine, vergine, olio d'oliva: cosa significano davvero queste categorie.",
        'article': """
<p class="intro">L'etichetta «olio d'oliva» copre realtà molto diverse. Il regolamento europeo CE 2568/91 definisce diverse categorie con criteri chimici e organolettici precisi. Capire queste distinzioni permette acquisti consapevoli e uso appropriato di ogni tipo in cucina.</p>

<h2>Le categorie ufficiali e i loro criteri</h2>
<p>L'<strong>olio extravergine d'oliva</strong> è al vertice della gerarchia: acidità libera massima dello 0,8%, nessun difetto organolettico rilevabile e polifenoli presenti in quantità significativa. È l'unica categoria che vale l'investimento per uso salute e gastronomico. L'<strong>olio vergine d'oliva</strong> ammette un'acidità fino al 2% e lievi difetti percettibili. Il semplice <strong>«olio d'oliva»</strong> è una miscela di olio raffinato (inodore, insipido) e vergine: praticamente nessun polifenolo.</p>
<blockquote>«La raffinazione elimina i difetti ma anche tutti i composti bioattivi che danno all'olio d'oliva il suo valore per la salute.»</blockquote>

<h3>Confronto delle categorie</h3>
<ul>
<li><strong>Extravergine</strong>: acidità ≤0,8%, zero difetti, alti polifenoli — uso crudo e cottura</li>
<li><strong>Vergine</strong>: acidità ≤2%, lievi difetti tollerati, polifenoli medi — uso in cottura</li>
<li><strong>Lampante</strong>: acidità &gt;3,3%, non commestibile crudo — destinato alla raffinazione</li>
<li><strong>Olio d'oliva raffinato</strong>: da lampante raffinato, acidità ≤0,3%, senza gusto né aroma</li>
<li><strong>Olio d'oliva</strong>: miscela raffinato + vergine, acidità ≤1%, minimi polifenoli</li>
</ul>

<h2>Perché esistono le frodi e come proteggersi</h2>
<p>La differenza di prezzo tra un vero extravergine (8–30€/L) e un olio d'oliva comune (2–5€/L) crea incentivi alla frode. Scandali ricorrenti hanno esposto oli etichettati «extravergine» contenenti in realtà oli raffinati o di origini errate. Per proteggersi: privilegiate oli con DOP/IGP, produttori indipendenti tracciabili e prezzi coerenti con la qualità dichiarata.</p>

<h3>Come scegliere in base all'uso</h3>
<ul>
<li><strong>Finitura, insalate, intingolo</strong>: extravergine di qualità con fruttato intenso</li>
<li><strong>Cottura quotidiana (saltare, arrostire)</strong>: extravergine o vergine — stabili al calore</li>
<li><strong>Frittura in grandi quantità</strong>: olio d'oliva comune — più economico, punto di fumo simile</li>
<li><strong>Cosmetica e cura della pelle</strong>: solo extravergine — i polifenoli sono gli attivi chiave</li>
</ul>
""",
        'faq': [
            ("Il grado di acidità in etichetta indica la qualità?", "Parzialmente. Un'acidità molto bassa (&lt;0,3%) è necessaria per un grande olio, ma non sufficiente. Un olio raffinato ha un'acidità quasi nulla ma zero polifenoli. L'acidità riflette la qualità delle olive alla raccolta, ma va letta insieme ad altri criteri."),
            ("Si può sentire la differenza tra extravergine e vergine in degustazione?", "Un degustatore esperto può rilevare i lievi difetti di un olio vergine. Per il consumatore occasionale, la differenza è sottile su campioni freschi. Ciò che è chiaramente percettibile: intensità aromatica, amarezza e piccantezza sono sistematicamente più marcate negli extravergini di qualità."),
            ("L'olio d'oliva raffinato fa male alla salute?", "Non è nocivo, ma non offre i benefici per la salute dell'extravergine. Senza polifenoli né oleocantale, è un olio ricco di acido oleico (buono) ma privo degli antiossidanti e antinfiammatori che rendono l'extravergine specificamente prezioso per la salute."),
            ("Cosa significa 'prima spremitura a freddo' in etichetta?", "È un riferimento storico ai vecchi frantoi idraulici a pietra, oggi sostituiti dalla centrifugazione continua. Il termine regolamentare attuale è 'estratto a freddo' (≤27°C). Entrambi indicano produzione a bassa temperatura.")
        ]
    },
    'tendenze-mercato-olio-oliva-2026.html': {
        'h1': "Tendenze del Mercato dell'Olio d'Oliva 2026",
        'meta': "Mercato dell'olio d'oliva nel 2026: prezzi record, crisi climatica, tendenze premium, nuovi produttori e prospettive per consumatori e produttori.",
        'lede': "Capire il mercato mondiale dell'olio d'oliva nel 2026.",
        'article': """
<p class="intro">Il mercato mondiale dell'olio d'oliva attraversa una trasformazione senza precedenti. I raccolti storicamente bassi del 2023 e 2024 hanno spinto i prezzi a livelli mai visti da 30 anni, ristrutturando l'intera filiera e accelerando tendenze strutturali che ridefiniscono ciò che i consumatori acquistano e ciò che i produttori coltivano.</p>

<h2>La crisi dei prezzi: cause e conseguenze</h2>
<p>Tra il 2022 e il 2024, il prezzo dell'olio d'oliva sfuso sui mercati spagnoli è triplicato, passando da 3–4€/kg a 8–9€/kg. Diversi fattori si sono sovrapposti: la siccità record in Andalusia (−50% di produzione nel 2023), le gelate tardive in Italia, la malattia da Xylella fastidiosa nelle Puglie, e una domanda mondiale in costante aumento, soprattutto in Asia e Nord America.</p>
<blockquote>«La crisi climatica ha trasformato il mercato dell'olio d'oliva: i produttori che investono nella resilienza climatica e nella qualità premium usciranno vincitori.»</blockquote>

<h3>Cifre chiave del mercato 2025–2026</h3>
<ul>
<li><strong>Produzione mondiale</strong>: circa 2,5 milioni di tonnellate (vs. 3,3M nel 2021)</li>
<li><strong>Spagna</strong>: 60% della produzione UE, fortemente colpita dalla siccità</li>
<li><strong>Marocco</strong>: +40% di superficie piantata negli ultimi 10 anni</li>
<li><strong>Prezzi al consumo UE</strong>: +80–120% tra il 2022 e il 2024</li>
<li><strong>Mercati in forte crescita</strong>: Cina (+15%/anno), USA (+8%/anno), Brasile (+12%/anno)</li>
</ul>

<h2>Le tendenze strutturali per il 2026 e oltre</h2>
<p>Al di là della crisi congiunturale, tre tendenze strutturali stanno trasformando il mercato. Prima, la <strong>premiumizzazione</strong>: i consumatori comprano meno ma meglio, con crescente domanda di oli DOP, monovarietali e di raccolta precoce. Seconda, la <strong>diversificazione geografica</strong>: Australia, Sudafrica, California e Cile investono massicciamente e guadagnano quote di mercato. Terza, la <strong>tecnologia</strong>: sensori IoT negli uliveti, intelligenza artificiale per ottimizzare la raccolta, blockchain per la tracciabilità.</p>

<h3>Opportunità identificate per il 2026</h3>
<ul>
<li><strong>Segmento ultra-premium</strong>: oli a &gt;40€/L, mercato di nicchia in forte crescita</li>
<li><strong>DTC (vendita diretta al consumatore)</strong>: abbonamenti, cofanetti e e-commerce in aumento</li>
<li><strong>Oli funzionali</strong>: alto contenuto di polifenoli certificato, mercato salute</li>
<li><strong>Nuovi produttori</strong>: Marocco, Turchia e Australia guadagnano in qualità e notorietà</li>
<li><strong>Educazione del consumatore</strong>: workshop di degustazione, certificazioni sommelier oliva in espansione</li>
</ul>
""",
        'faq': [
            ("Perché il prezzo dell'olio d'oliva è aumentato così tanto?", "Combinazione di siccità record in Spagna (principale produttore mondiale), gelate tardive in Italia, Xylella nelle Puglie, e domanda mondiale in aumento. Tra il 2022 e il 2024, la produzione europea è calata del 30–40% mentre la domanda continuava a crescere."),
            ("Il prezzo scenderà nel 2026?", "Le prospettive del raccolto 2025–2026 sono più favorevoli grazie alle migliori precipitazioni. I prezzi dovrebbero allentarsi ma rimanere sopra i livelli pre-2022. La dipendenza strutturale dalle condizioni climatiche mediterranee significa che la volatilità dei prezzi rimane una realtà duratura."),
            ("Quali nuovi paesi produttori tenere d'occhio?", "Marocco (Meknes, Marrakech), Australia (Margaret River, Riverina), Argentina (Mendoza), Cile e California. Questi produttori beneficiano di climi mediterranei, investono massicciamente e cominciano a vincere nei grandi concorsi internazionali."),
            ("Come la tecnologia sta trasformando la filiera?", "Su tre assi: produzione (sensori suolo e meteo, irrigazione di precisione, droni per monitorare la salute degli ulivi), qualità (spettroscopia NIR per analizzare i polifenoli in tempo reale al frantoio), e tracciabilità (blockchain per certificare l'origine dalla piantagione alla bottiglia).")
        ]
    },
}

# Greek guide pages — same structure, in Greek
GUIDES_EL = {
    'ofeli-igia-elaio-lado.html': {
        'h1': "Οφέλη Ελαιολάδου για την Υγεία — Πλήρης Επιστημονικός Οδηγός",
        'meta': "Επιστημονικά αποδεδειγμένα οφέλη εξαιρετικά παρθένου ελαιολάδου: καρδιαγγειακή προστασία, αντιφλεγμονώδεις πολυφαινόλες, υγεία εγκεφάλου και μακροζωία. Οδηγός 2026.",
        'lede': "Τι επιβεβαιώνει η επιστήμη για το ελαιόλαδο και την υγεία σας.",
        'article': """
<p class="intro">Το εξαιρετικά παρθένο ελαιόλαδο είναι ένα από τα πιο επιστημονικά μελετημένα τρόφιμα στη σύγχρονη προληπτική ιατρική. Με 73% μονοακόρεστο ελαϊκό οξύ και εξαιρετική συγκέντρωση πολυφαινολών, βρίσκεται στο επίκεντρο της μεσογειακής διατροφής — του διατροφικού μοντέλου που σχετίζεται με τη μεγαλύτερη τεκμηριωμένη μακροζωία παγκοσμίως.</p>

<h2>Καρδιαγγειακή προστασία: τα κλινικά στοιχεία</h2>
<p>Η μελέτη PREDIMED, που πραγματοποιήθηκε σε 7.447 άτομα υψηλού κινδύνου, έδειξε ότι η τακτική κατανάλωση εξαιρετικά παρθένου ελαιολάδου μειώνει κατά 30% τον κίνδυνο εμφράγματος και εγκεφαλικού. Το ελαϊκό οξύ μειώνει την οξειδωμένη LDL — την επικίνδυνη μορφή της «κακής χοληστερόλης» — διατηρώντας την προστατευτική HDL. Οι πολυφαινόλες υδροξυτυροσόλη και ελαιουρωπαΐνη ενισχύουν τα αρτηριακά τοιχώματα και καταπολεμούν τη χρόνια αγγειακή φλεγμονή.</p>
<blockquote>«Το εξαιρετικά παρθένο ελαιόλαδο είναι ένα από τα λίγα τρόφιμα για τα οποία διαθέτουμε κλινικές αποδείξεις μείωσης της καρδιαγγειακής θνησιμότητας.» — NEJM, 2013</blockquote>

<h3>Βασικά ενεργά συστατικά και οι λειτουργίες τους</h3>
<ul>
<li><strong>Ελαϊκό οξύ (ωμέγα-9)</strong>: μειώνει την LDL χοληστερόλη και σταθεροποιεί τις κυτταρικές μεμβράνες</li>
<li><strong>Υδροξυτυροσόλη</strong>: ένα από τα ισχυρότερα γνωστά αντιοξειδωτικά, αναγνωρισμένο από την EFSA</li>
<li><strong>Ελαιοκανθάλη</strong>: αναστέλλει COX-1 και COX-2 όπως η ιβουπροφένη — χωρίς παρενέργειες</li>
<li><strong>Ελαιουρωπαΐνη</strong>: τεκμηριωμένα αντιφλεγμονώδη και αντιμικροβιακά αποτελέσματα</li>
<li><strong>Βιταμίνη Ε (τοκοφερόλες)</strong>: προστατεύει τα λιπίδια από την περοξειδωτική οξείδωση</li>
</ul>

<h2>Αντιφλεγμονώδεις και νευροπροστατευτικές επιδράσεις</h2>
<p>Η ελαιοκανθάλη — παρούσα μόνο σε φρέσκα έλαια υψηλής ποιότητας — προκαλεί το χαρακτηριστικό κάψιμο στο λαιμό. Αυτή η φαινολική ένωση αναστέλλει τα ίδια φλεγμονώδη ένζυμα με τα ΜΣΑΦ, χωρίς γαστρεντερικές παρενέργειες. Διαχρονικές μελέτες δείχνουν ότι οι μεσογειακοί πληθυσμοί που καταναλώνουν πάνω από 20ml ελαιολάδου ημερησίως εμφανίζουν σημαντικά πιο αργή γνωστική παρακμή, με μειωμένο κίνδυνο Alzheimer κατά περίπου 40%.</p>

<h3>Συνιστώμενη πρόσληψη ανά προφίλ</h3>
<ul>
<li><strong>Γενική υγεία</strong>: 20–30ml ημερησίως ως ωμό καρύκευμα ή λάδι φινιρίσματος</li>
<li><strong>Καρδιαγγειακή προστασία</strong>: 40ml/ημέρα (θεραπευτικό πρωτόκολλο PREDIMED)</li>
<li><strong>Μαγείρεμα</strong>: σταθερό έως 210°C — κατάλληλο για σοτάρισμα και ψήσιμο</li>
<li><strong>Χρήση στο δέρμα</strong>: λίγες σταγόνες αρκούν χάρη στην υψηλή θρεπτική πυκνότητα</li>
</ul>
""",
        'faq': [
            ("Πόσο ελαιόλαδο πρέπει να καταναλώνω ημερησίως;", "20–40ml ημερησίως αντικαθιστώντας άλλα λιπαρά. Η μελέτη PREDIMED χρησιμοποίησε 40ml ως θεραπευτική δόση, αλλά 20ml ως ημερήσιο καρύκευμα παρέχει ήδη μετρήσιμα οφέλη."),
            ("Το μαγειρεμένο ελαιόλαδο χάνει τα οφέλη του;", "Εν μέρει. Το ελαϊκό οξύ παραμένει σταθερό έως 210°C. Οι πολυφαινόλες αντέχουν στο μέτριο μαγείρεμα (180°C) αλλά αποδομούνται σε παρατεταμένο τηγάνισμα. Για μέγιστο αποτέλεσμα υγείας, προσθέστε ωμό ελαιόλαδο ως φινίρισμα."),
            ("Έχουν όλα τα ελαιόλαδα τα ίδια οφέλη υγείας;", "Όχι. Μόνο το υψηλής ποιότητας εξαιρετικά παρθένο ελαιόλαδο περιέχει πολυφαινόλες σε θεραπευτικές συγκεντρώσεις. Αναζητήστε περιεκτικότητα σε πολυφαινόλες άνω των 250mg/kg."),
            ("Βοηθά το ελαιόλαδο στον διαβήτη τύπου 2;", "Ναι — μελέτες δείχνουν ότι το ελαϊκό οξύ βελτιώνει την ευαισθησία στην ινσουλίνη και μειώνει τη μεταγευματική γλυκόζη αίματος. Η μεσογειακή διατροφή εμπλουτισμένη με ελαιόλαδο είναι μια από τις λίγες διατροφικές προσεγγίσεις με ισχυρά κλινικά στοιχεία πρόληψης του διαβήτη τύπου 2.")
        ]
    },
}

# For remaining EL guides, use a minimal but real template
EL_STUBS = {
    'odigos-dokimis-elaio-ladou.html': ("Οδηγός Γεύσης Ελαιολάδου", "guide-degustation-huile-olive.html", "olive-oil-tasting-guide.html", "guida-degustazione-olio-oliva.html", "odigos-dokimis-elaio-ladou.html"),
    'magirema-me-elaio-lado.html': ("Μαγείρεμα με Ελαιόλαδο: Μυστικά και Επιστήμη", "cuisiner-avec-huile-olive.html", "cooking-with-olive-oil.html", "cucinare-con-olio-oliva.html", "magirema-me-elaio-lado.html"),
    'diadikasía-paragogís-elaio-ladou.html': ("Από το Δέντρο στο Μπουκάλι: Η Διαδικασία Παραγωγής", "processus-fabrication-huile-olive.html", "olive-oil-production-process.html", "processo-produzione-olio-oliva.html", "diadikasía-paragogís-elaio-ladou.html"),
    'terroirs-kai-periochés-elaio-ladou.html': ("Τεrroir και Περιοχές: Οι Μεγάλες Προελεύσεις Ελαιολάδου", "terroirs-regions-huile-olive.html", "olive-oil-terroirs-and-regions.html", "terroir-e-regioni-olio-oliva.html", "terroirs-kai-periochés-elaio-ladou.html"),
    'pos-na-dialexete-to-kalitero-elaio-lado.html': ("Πώς να Επιλέξετε το Καλύτερο Ελαιόλαδο", "comment-choisir-huile-olive.html", "how-to-choose-best-olive-oil.html", "come-scegliere-migliore-olio-oliva.html", "pos-na-dialexete-to-kalitero-elaio-lado.html"),
    'simvoules-sintirisis-elaio-ladou.html': ("Συμβουλές Αποθήκευσης Ελαιολάδου", "conservation-huile-olive-conseils.html", "olive-oil-storage-tips.html", "consigli-conservazione-olio-oliva.html", "simvoules-sintirisis-elaio-ladou.html"),
    'viologiko-kai-viosimo-elaio-lado.html': ("Βιολογικό και Βιώσιμο Ελαιόλαδο", "huile-olive-bio-durabilite.html", "organic-and-sustainable-olive-oil.html", "olio-oliva-biologico-e-sostenibile.html", "viologiko-kai-viosimo-elaio-lado.html"),
    'elaio-lado-omorfia-kai-derma.html': ("Ελαιόλαδο για την Ομορφιά και τη Φροντίδα Δέρματος", "huile-olive-beaute-soins-peau.html", "olive-oil-beauty-and-skincare.html", "olio-oliva-bellezza-cura-pelle.html", "elaio-lado-omorfia-kai-derma.html"),
    'istoria-kai-politismos-elaio-ladou.html': ("Ιστορία και Πολιτισμός του Ελαιολάδου: 5.000 Χρόνια Πολιτισμού", "histoire-culture-huile-olive.html", "history-and-culture-of-olive-oil.html", "storia-e-cultura-dell-olio-oliva.html", "istoria-kai-politismos-elaio-ladou.html"),
    'diafora-extra-partheno-kai-partheno.html': ("Εξαιρετικά Παρθένο vs Παρθένο Ελαιόλαδο: Κατανοώντας τις Κατηγορίες", "difference-extra-vierge-vierge.html", "extra-virgin-vs-virgin-olive-oil.html", "differenza-extra-vergine-e-vergine.html", "diafora-extra-partheno-kai-partheno.html"),
    'taseis-agoras-elaio-ladou-2026.html': ("Τάσεις Αγοράς Ελαιολάδου 2026", "tendances-marche-huile-olive-2026.html", "olive-oil-market-trends-2026.html", "tendenze-mercato-olio-oliva-2026.html", "taseis-agoras-elaio-ladou-2026.html"),
}

EL_STUB_BODIES = {
    'odigos-dokimis-elaio-ladou.html': ("Πώς να δοκιμάζετε ελαιόλαδο σαν επαγγελματίας.", "Η επαγγελματική γεύση ελαιολάδου ακολουθεί ένα αυστηρό πρωτόκολλο του Διεθνούς Ελαιοκομικού Συμβουλίου (ΔΕΣ). Τρία θετικά χαρακτηριστικά αξιολογούνται: φρουτώδης χαρακτήρας, πικράδα και πικάντικο. Το ποτήρι ζεσταίνεται στα 28°C για να απελευθερωθούν τα αρωματικά συστατικά. Η χρωματική επίδραση εξαλείφεται με σκούρα αδιαφανή ποτήρια.", [("Γιατί χρησιμοποιούν χρωματιστά ποτήρια;", "Για να αποτρέψουν την οπτική προκατάληψη. Το χρώμα δεν είναι δείκτης ποιότητας."), ("Η πικράδα και το πικάντικο είναι ελαττώματα;", "Όχι — είναι θετικά χαρακτηριστικά. Δείχνουν πολυφαινόλες και ελαιοκανθάλη αντίστοιχα.")]),
    'magirema-me-elaio-lado.html': ("Τι λειτουργεί πραγματικά στο μαγείρεμα με ελαιόλαδο.", "Αντίθετα με τον διαδεδομένο μύθο, το εξαιρετικά παρθένο ελαιόλαδο αντέχει τέλεια στο μαγείρεμα. Το σημείο καπνού του 190–210°C το καθιστά συμβατό με σχεδόν όλες τις καθημερινές μαγειρικές τεχνικές. Το ελαϊκό οξύ (73% της σύνθεσης) είναι εξαιρετικά ανθεκτικό στη θερμική οξείδωση.", [("Χάνει τα θρεπτικά του στοιχεία με το μαγείρεμα;", "Εν μέρει. Το ελαϊκό οξύ παραμένει άθικτο. Οι πολυφαινόλες αντέχουν στο μέτριο μαγείρεμα."), ("Μπορώ να χρησιμοποιήσω ελαιόλαδο για τηγάνισμα;", "Ναι — είναι σταθερό έως 210°C, ασφαλέστερο από πολλά άλλα έλαια.")]),
    'diadikasía-paragogís-elaio-ladou.html': ("Πώς γεννιέται ένα εξαιρετικό ελαιόλαδο.", "Η ποιότητα του εξαιρετικά παρθένου ελαιολάδου χτίζεται σε κάθε στάδιο της διαδικασίας. Η συγκομιδή πρέπει να γίνεται νωρίς (Οκτώβριος–Νοέμβριος) για υψηλές πολυφαινόλες. Η έλαιόλαδο πρέπει να φτάσει στο ελαιοτριβείο εντός 4–6 ωρών. Η «ψυχρή εκχύλιση» εγγυάται θερμοκρασία μάλαξης ≤27°C.", [("Πόσες ελιές χρειάζονται για ένα λίτρο ελαιολάδου;", "Περίπου 4–6 κιλά ελιών ανά λίτρο, ανάλογα με την ποικιλία και το στάδιο ωρίμανσης."), ("Τι σημαίνει 'ψυχρή εκχύλιση';", "Εγγυάται ότι η θερμοκρασία μάλαξης δεν ξεπέρασε τους 27°C, διατηρώντας πολυφαινόλες και αρώματα.")]),
    'terroirs-kai-periochés-elaio-ladou.html': ("Από πού προέρχονται τα καλύτερα ελαιόλαδα του κόσμου.", "Η Μεσόγειος συγκεντρώνει το 95% της παγκόσμιας παραγωγής. Η Ισπανία είναι ο μεγαλύτερος παραγωγός (45% της παγκόσμιας παραγωγής). Η Ελλάδα, με μόλις 2% του παγκόσμιου πληθυσμού, παράγει το 10% του παγκόσμιου ελαιολάδου και καταναλώνει τη μεγαλύτερη ποσότητα κατά κεφαλή (20 λίτρα/έτος).", [("Ποια χώρα παράγει το καλύτερο ελαιόλαδο;", "Δεν υπάρχει απόλυτη απάντηση. Διεθνείς διαγωνισμοί στεφανώνουν τακτικά έλαια από Ελλάδα, Ισπανία, Ιταλία, Μαρόκο και Αυστραλία."), ("Γιατί τα ελληνικά ελαιόλαδα είναι τόσο πλούσια σε πολυφαινόλες;", "Τρεις παράγοντες: η ποικιλία Κορωνέικη, το ξηρό μεσογειακό κλίμα και η παράδοση πρώιμης συγκομιδής στο Πελοπόννησο και την Κρήτη.")]),
    'pos-na-dialexete-to-kalitero-elaio-lado.html': ("Τα κριτήρια που ξεχωρίζουν ένα εξαιρετικό ελαιόλαδο.", "Μόνο η ένδειξη «Εξαιρετικά Παρθένο» εγγυάται ελεύθερη οξύτητα κάτω από 0,8% και απουσία οργανοληπτικών ελαττωμάτων. Η <strong>ημερομηνία συγκομιδής</strong> είναι πιο ενημερωτική από την ημερομηνία λήξης. Αναζητήστε συγκομιδή των τελευταίων 12 μηνών και συσκευασία σε σκούρο γυαλί ή αδιαφανές δοχείο.", [("Το θολό ελαιόλαδο είναι σημάδι ποιότητας;", "Όχι απαραίτητα. Υποδηλώνει αφιλτράριστο έλαιο, πιο εύθραυστο στη συντήρηση. Δεν είναι απόλυτο κριτήριο ποιότητας."), ("Είναι τα βιολογικά ελαιόλαδα καλύτερα;", "Η βιολογική πιστοποίηση εγγυάται απουσία συνθετικών φυτοφαρμάκων, όχι γευστική ποιότητα ή πλούτο πολυφαινολών.")]),
    'simvoules-sintirisis-elaio-ladou.html': ("Οι κανόνες αποθήκευσης για διατήρηση ποιότητας και οφελών.", "Τρεις εχθροί υποβαθμίζουν το ελαιόλαδο: φως, θερμότητα και οξυγόνο. Το φως πυροδοτεί φωτοοξειδωτικές αντιδράσεις που υποβαθμίζουν τις πολυφαινόλες. Η θερμότητα επιταχύνει την οξείδωση. Ποτέ μην αποθηκεύετε κοντά στη σόμπα ή υπό ηλιακό φως. Κρατήστε το σε δροσερό, σκοτεινό μέρος σε αδιαφανή συσκευασία.", [("Πώς ξέρω αν το ελαιόλαδό μου είναι ακόμα καλό;", "Μυρίστε το: καλό ελαιόλαδο μυρίζει φρέσκο και φρουτώδες. Αν μυρίζει παλιό βούτυρο ή υγρό χαρτί, έχει οξειδωθεί."), ("Μπορώ να βάλω ελαιόλαδο στο ψυγείο;", "Δεν συνιστάται για καθημερινή χρήση — πήζει κάτω από 7°C. Για πολύτιμα έλαια που καταναλώνετε αργά, το ψυγείο παρατείνει τη διάρκεια ζωής.")]),
    'viologiko-kai-viosimo-elaio-lado.html': ("Βιωσιμότητα και βιολογική ελαιοκαλλιέργεια: τι σημαίνουν πραγματικά.", "Η βιολογική πιστοποίηση εγγυάται απουσία συνθετικών φυτοφαρμάκων. Δεν εγγυάται γευστική ποιότητα ή πλούτο πολυφαινολών. Ένας παραδοσιακός ελαιώνας είναι σημαντικός αποθηκευτής άνθρακα: ένα εκτάριο ελαιόδεντρων δεσμεύει 2,5–4 τόνους CO₂ ετησίως.", [("Βελτιώνει η μετατροπή σε βιολογικό την ποιότητα του λαδιού;", "Όχι αυτόματα. Η ποιότητα εξαρτάται πολύ περισσότερο από ποικιλία, χρόνο συγκομιδής και έλεγχο εκχύλισης."), ("Υπάρχουν πιστοποιήσεις για έλαια υψηλής περιεκτικότητας σε πολυφαινόλες;", "Ναι. Η EFSA επιτρέπει ισχυρισμό υγείας για έλαια με περισσότερες από 250mg/kg πολυφαινόλες.")]),
    'elaio-lado-omorfia-kai-derma.html': ("Το αρχαίο μυστικό ομορφιάς — επιβεβαιωμένο από τη σύγχρονη επιστήμη.", "Το εξαιρετικά παρθένο ελαιόλαδο περιέχει σκουαλένιο (0,3–1%), φυσικό μαλακτικό πανομοιότυπο με αυτό που παράγει η σμηγματογόνος μας. Οι τοκοφερόλες (βιταμίνη Ε) προστατεύουν τις κυτταρικές μεμβράνες από οξείδωση. Δεν συνιστάται για λιπαρές ή με ακμή επιδερμίδες λόγω μέτριου κωμεδογόνου δείκτη.", [("Ταιριάζει το ελαιόλαδο σε όλους τους τύπους δέρματος;", "Όχι. Ιδανικό για ξηρές και κανονικές επιδερμίδες. Αποφύγετε σε λιπαρές και ακνεϊκές επιδερμίδες."), ("Μπορώ να αντικαταστήσω την κρέμα με ελαιόλαδο;", "Εν μέρει. Είναι εξαιρετικό emollient αλλά δεν είναι humectant. Εφαρμόστε σε ελαφρά υγρό δέρμα για βέλτιστη αποτελεσματικότητα.")]),
    'istoria-kai-politismos-elaio-ladou.html': ("Πέντε χιλιάδες χρόνια ιστορίας σε κάθε σταγόνα ελαιολάδου.", "Κανένα άλλο τρόφιμο δεν έπαιξε πιο κεντρικό ρόλο στην ανθρώπινη ιστορία. Νόμισμα, ιερό καύσιμο, φάρμακο, καλλυντικό και τρόφιμο — το ελαιόλαδο συνόδεψε τη γέννηση των μεσογειακών πολιτισμών για πάνω από πέντε χιλιετίες. Ορισμένες ελιές στη Σαρδηνία, την Κρήτη και την Παλαιστίνη έχουν ηλικία άνω των 2.000 ετών.", [("Ποια χώρα εφηύρε το ελαιόλαδο;", "Η εξημέρωση της ελιάς πραγματοποιήθηκε ταυτόχρονα σε διάφορες περιοχές της Μέσης Ανατολής και της ανατολικής Μεσογείου — Συρία, Λίβανος, Παλαιστίνη, Κρήτη — μεταξύ 6000 και 4000 π.Χ."), ("Γιατί το κλαδί ελιάς συμβολίζει την ειρήνη;", "Το συμβολισμός χρονολογείται από τη Γένεση (περιστέρι που φέρνει κλαδί ελιάς μετά τον Κατακλυσμό). Τα ΗΕ χρησιμοποιούν το κλαδί ελιάς στο έμβλημά τους από το 1945.")]),
    'diafora-extra-partheno-kai-partheno.html': ("Εξαιρετικά παρθένο, παρθένο, ελαιόλαδο: τι σημαίνουν αυτές οι κατηγορίες.", "Η ετικέτα «ελαιόλαδο» καλύπτει πολύ διαφορετικές πραγματικότητες. Μόνο το «εξαιρετικά παρθένο» εγγυάται ελεύθερη οξύτητα κάτω από 0,8% και απουσία οργανοληπτικών ελαττωμάτων. Το «παρθένο» επιτρέπει οξύτητα έως 2% και ελαφρά ελαττώματα. Το απλό «ελαιόλαδο» είναι μείγμα εξευγενισμένου και παρθένου — σχεδόν καμία πολυφαινόλη.", [("Η οξύτητα στην ετικέτα προβλέπει την ποιότητα;", "Εν μέρει. Πολύ χαμηλή οξύτητα είναι απαραίτητη αλλά όχι επαρκής. Ένα εξευγενισμένο έλαιο έχει σχεδόν μηδενική οξύτητα αλλά καθόλου πολυφαινόλες."), ("Είναι το εξευγενισμένο ελαιόλαδο ανθυγιεινό;", "Δεν είναι επιβλαβές, αλλά δεν προσφέρει τα οφέλη υγείας του εξαιρετικά παρθένου. Χωρίς πολυφαινόλες, είναι απλά μια πηγή ελαϊκού οξέος.")]),
    'taseis-agoras-elaio-ladou-2026.html': ("Κατανόηση της παγκόσμιας αγοράς ελαιολάδου το 2026.", "Η παγκόσμια αγορά ελαιολάδου διέρχεται αλλαγή χωρίς προηγούμενο. Οι ιστορικά χαμηλές σοδειές του 2023 και 2024 ώθησαν τις τιμές σε επίπεδα που δεν είχαν καταγραφεί εδώ και 30 χρόνια. Μεταξύ 2022 και 2024, οι τιμές στους Ισπανούς χονδρεμπορικούς τριπλασιάστηκαν, από 3–4€/kg σε 8–9€/kg.", [("Γιατί οι τιμές αυξήθηκαν τόσο πολύ;", "Συνδυασμός ρεκόρ ξηρασίας στην Ισπανία, ανεπιθύμητων παγετών στην Ιταλία, ασθένειας Xylella στην Apulia και αυξανόμενης παγκόσμιας ζήτησης."), ("Θα πέσουν οι τιμές το 2026;", "Οι προοπτικές για τη σοδειά 2025–2026 είναι πιο ευνοϊκές. Οι τιμές αναμένεται να χαλαρώσουν αλλά να παραμείνουν πάνω από τα επίπεδα πριν από το 2022.")]),
}


TEMPLATE_IT = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{h1} — L'Or Vert</title>
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
<nav class="site-nav"><div class="container"><a href="../index-fr.html" class="logo">L'OR VERT</a><div class="lang-switch">{lang_switch}</div></div></nav>
<header class="page-hero"><div class="container">
    <div class="breadcrumb"><a href="../index-fr.html">Home</a> &raquo; Guide</div>
    <h1>{h1}</h1><p class="lede">{lede}</p>
    <div class="meta">Pubblicato: Aprile 2026 &middot; 8 min di lettura</div>
</div></header>
<main class="container"><article class="guide">{article}</article>
<section class="faq"><h2>Domande Frequenti</h2>{faq}</section></main>
<footer class="site-footer"><div class="container"><h3>L'Or Vert</h3>
<p>Studio di Mercato Olio d'Oliva 2026.</p>
<div class="copyright">&copy; 2026 &mdash; Tutti i diritti riservati</div></div></footer>
</body></html>"""

TEMPLATE_EL = """<!DOCTYPE html>
<html lang="el">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{h1} — L'Or Vert</title>
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
<nav class="site-nav"><div class="container"><a href="../index-fr.html" class="logo">L'OR VERT</a><div class="lang-switch">{lang_switch}</div></div></nav>
<header class="page-hero"><div class="container">
    <div class="breadcrumb"><a href="../index-fr.html">Αρχική</a> &raquo; Οδηγοί</div>
    <h1>{h1}</h1><p class="lede">{lede}</p>
    <div class="meta">Δημοσίευση: Απρίλιος 2026 &middot; 8 λεπτά ανάγνωσης</div>
</div></header>
<main class="container"><article class="guide">{article}</article>
<section class="faq"><h2>Συχνές Ερωτήσεις</h2>{faq}</section></main>
<footer class="site-footer"><div class="container"><h3>L'Or Vert</h3>
<p>Μελέτη Αγοράς Ελαιολάδου 2026.</p>
<div class="copyright">&copy; 2026 &mdash; Με επιφύλαξη παντός δικαιώματος</div></div></footer>
</body></html>"""


def hreflang_html(urls):
    fr, en, it, el = urls
    return (
        f'<link rel="alternate" hreflang="fr" href="https://huiledefes.com/guides/{fr}" />\n'
        f'    <link rel="alternate" hreflang="en" href="https://huiledefes.com/guides/{en}" />\n'
        f'    <link rel="alternate" hreflang="it" href="https://huiledefes.com/guides/{it}" />\n'
        f'    <link rel="alternate" hreflang="el" href="https://huiledefes.com/guides/{el}" />'
    )


def lang_switch_html(urls, current):
    fr, en, it, el = urls
    parts = []
    for label, fname in [('FR', fr), ('EN', en), ('IT', it), ('EL', el)]:
        cls = ' class="active"' if fname == current else ''
        parts.append(f'<a href="{fname}"{cls}>{label}</a>')
    return ' '.join(parts)


def faq_html(faq_list):
    return '\n'.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faq_list)


def main():
    count = 0
    # Italian guides
    for filename, data in GUIDES_IT.items():
        filepath = os.path.join(DIR, filename)
        if not os.path.exists(filepath):
            print(f"SKIP IT: {filename}"); continue
        urls = HREFLANG_MAP[filename]
        html = TEMPLATE_IT.format(
            h1=data['h1'], meta=data['meta'], lede=data['lede'],
            article=data['article'], faq=faq_html(data['faq']),
            hreflang=hreflang_html(urls),
            lang_switch=lang_switch_html(urls, filename),
        )
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"OK IT: {filename}"); count += 1

    # Greek — full content for health-benefits
    for filename, data in GUIDES_EL.items():
        filepath = os.path.join(DIR, filename)
        if not os.path.exists(filepath):
            print(f"SKIP EL: {filename}"); continue
        urls = HREFLANG_MAP[filename]
        html = TEMPLATE_EL.format(
            h1=data['h1'], meta=data['meta'], lede=data['lede'],
            article=data['article'], faq=faq_html(data['faq']),
            hreflang=hreflang_html(urls),
            lang_switch=lang_switch_html(urls, filename),
        )
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"OK EL (full): {filename}"); count += 1

    # Greek — stub content for remaining 11 topics
    for filename, stub_data in EL_STUB_BODIES.items():
        filepath = os.path.join(DIR, filename)
        if not os.path.exists(filepath):
            print(f"SKIP EL stub: {filename}"); continue
        lede, body_text, faq_items = stub_data
        stub_info = EL_STUBS[filename]
        h1 = stub_info[0]
        urls = (stub_info[1], stub_info[2], stub_info[3], stub_info[4])
        article_html = f'<p class="intro">{body_text}</p>'
        html = TEMPLATE_EL.format(
            h1=h1, meta=f"{h1} — Επιστημονικός οδηγός 2026 για το ελαιόλαδο από το L\'Or Vert.",
            lede=lede, article=article_html, faq=faq_html(faq_items),
            hreflang=hreflang_html(urls),
            lang_switch=lang_switch_html(urls, filename),
        )
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"OK EL stub: {filename}"); count += 1

    print(f"\nDone: {count} IT+EL guide pages regenerated.")


if __name__ == '__main__':
    main()

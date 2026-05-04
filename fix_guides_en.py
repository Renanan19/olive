#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix English guide pages."""
import os

DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'guides')

GUIDES = {
    'health-benefits-olive-oil.html': {
        'h1': "Olive Oil Health Benefits — The Complete Scientific Guide",
        'meta': "Science-backed health benefits of extra virgin olive oil: cardiovascular protection, anti-inflammatory polyphenols, brain health and longevity. Expert guide 2026.",
        'lede': "What science confirms about olive oil and your long-term health.",
        'article': """
<p class="intro">Extra virgin olive oil is one of the most scientifically studied foods in preventive medicine. With 73% monounsaturated oleic acid and exceptionally high polyphenol concentration, it sits at the heart of the Mediterranean diet — the dietary pattern most associated with documented human longevity.</p>

<h2>Cardiovascular Protection: The Clinical Evidence</h2>
<p>The landmark PREDIMED trial, conducted on 7,447 high-risk individuals, demonstrated that regular consumption of extra virgin olive oil reduces the risk of heart attack and stroke by 30%. Oleic acid lowers oxidized LDL — the dangerous form of bad cholesterol — while preserving protective HDL. Polyphenols such as hydroxytyrosol and oleuropein strengthen arterial walls and reduce chronic vascular inflammation, a primary driver of cardiovascular disease. These results have been replicated across multiple large-scale cohort studies in Mediterranean populations.</p>
<blockquote>"Extra virgin olive oil is one of the few foods for which we have clinical evidence of reduced cardiovascular mortality." — NEJM, 2013</blockquote>

<h3>Key Active Components and Their Functions</h3>
<ul>
<li><strong>Oleic acid (omega-9)</strong>: reduces LDL cholesterol and stabilizes cell membranes</li>
<li><strong>Hydroxytyrosol</strong>: among the most potent antioxidants known, recognized by EFSA</li>
<li><strong>Oleocanthal</strong>: inhibits COX-1 and COX-2 like ibuprofen — without side effects</li>
<li><strong>Oleuropein</strong>: documented anti-inflammatory and antimicrobial properties</li>
<li><strong>Vitamin E (tocopherols)</strong>: protects lipids from peroxidative oxidation</li>
</ul>

<h2>Anti-Inflammatory and Neuroprotective Effects</h2>
<p>Oleocanthal — present only in fresh, high-quality oils — causes the characteristic throat-tingling sensation. This phenolic compound inhibits the same inflammatory enzymes as non-steroidal anti-inflammatory drugs, without gastrointestinal side effects. Longitudinal studies show that Mediterranean populations consuming more than 20ml of olive oil daily experience significantly slower cognitive decline, with Alzheimer's disease risk reduced by approximately 40%. The peppery throat burn during tasting is a direct quality signal: the more you feel it, the more oleocanthal — and the better the oil.</p>

<h3>Recommended Intake by Profile</h3>
<ul>
<li><strong>General wellness</strong>: 20–30ml daily as raw dressing or finishing oil</li>
<li><strong>Cardiovascular protection</strong>: 40ml/day (PREDIMED therapeutic protocol)</li>
<li><strong>Cooking</strong>: stable up to 210°C — suitable for sautéing and roasting</li>
<li><strong>Skin and hair</strong>: a few drops go far thanks to high nutritional density</li>
</ul>
""",
        'faq': [
            ("How much olive oil should I consume daily for health benefits?",
             "Studies show significant effects at 40ml (4 tablespoons) per day replacing other fats. For daily use, 20–30ml as raw dressing or finishing oil already provides measurable cardiovascular and anti-inflammatory benefits."),
            ("Does cooking olive oil destroy its health benefits?",
             "Partially. Oleic acid remains stable up to 210°C. Polyphenols resist moderate cooking (180°C) but degrade in prolonged high-heat frying. For maximum health effect, add a drizzle of raw extra virgin olive oil as a finishing touch on cooked dishes."),
            ("Are all olive oils equally healthy?",
             "No. Only high-quality extra virgin olive oil contains polyphenols in therapeutic concentrations. Refined oils have lost virtually all bioactive compounds during industrial processing. Look for polyphenol content above 250mg/kg and a recent harvest date."),
            ("Does olive oil help with type 2 diabetes?",
             "Yes — studies show oleic acid improves insulin sensitivity and reduces postprandial blood glucose. The Mediterranean diet enriched with olive oil is one of the few dietary approaches with robust clinical evidence for type 2 diabetes prevention.")
        ]
    },
    'olive-oil-tasting-guide.html': {
        'h1': "The Complete Olive Oil Tasting Guide",
        'meta': "Learn to taste olive oil like a professional: color, aromas, bitterness, pungency and defects. Official IOC method and practical tips for beginners and enthusiasts.",
        'lede': "The professional method for identifying a great olive oil.",
        'article': """
<p class="intro">Tasting olive oil is a discipline. Professional judges at the International Olive Council (IOC) follow a precise protocol that evaluates three positive attributes — fruitiness, bitterness, pungency — and identifies defects that disqualify an oil from the extra virgin category. Here's how to do it properly.</p>

<h2>The Official Tasting Protocol</h2>
<p>Professional tasting uses a cobalt blue or opaque brown glass to mask the color, preventing visual bias from influencing the olfactory assessment. The glass is warmed between the palms to approximately 28°C to release volatile aromatic compounds. The evaluator inhales deeply, notes the aromas, then takes a small sip and aerates the oil in the mouth — a technique called "stripping" — to amplify retronasal aroma perception. Color is irrelevant to quality: a golden oil can surpass a green one, and vice versa.</p>
<blockquote>"The color of olive oil tells you nothing about its quality. Judge with your nose and palate, never with your eyes."</blockquote>

<h3>The Three Positive Attributes</h3>
<ul>
<li><strong>Fruitiness</strong>: intensity and type of vegetal aromas — fresh grass, artichoke, almond, tomato, apple</li>
<li><strong>Bitterness</strong>: bitter taste on the tongue, indicating polyphenols — positive when balanced</li>
<li><strong>Pungency</strong>: burning sensation in the throat from oleocanthal — freshness and quality indicator</li>
</ul>

<h2>Identifying Common Defects</h2>
<p>Organoleptic defects classify an oil as "virgin" or "lampante" (unfit for consumption). <em>Fusty/muddy</em> (rancid-humid, fermented mud smell) comes from olives stored too long before pressing. <em>Rancid</em> results from oxidation through light or heat exposure. <em>Winey</em> indicates excessive fermentation from damaged olives. A genuine extra virgin olive oil presents none of these defects. The most reliable quality test at home: smell it straight from the bottle — a great extra virgin smells alive, fresh, and vegetal.</p>

<h3>Aromatic Profiles by Variety</h3>
<ul>
<li><strong>Arbequina</strong> (Spain): mild, almond, ripe fruit, low bitterness — great for beginners</li>
<li><strong>Picual</strong> (Spain): powerful, tomato, fig, marked bitterness and pungency</li>
<li><strong>Koroneiki</strong> (Greece): fresh grass, artichoke, intense pungency, high polyphenols</li>
<li><strong>Frantoio</strong> (Italy): artichoke, fresh herb, balanced bitterness, very fruity</li>
<li><strong>Chemlali</strong> (Tunisia): almond, green apple, mild and delicate profile</li>
</ul>
""",
        'faq': [
            ("Why do professional tasters use colored glasses?",
             "To eliminate visual bias. Color is not a quality indicator — a pale golden oil can outperform a vivid green one. The IOC protocol mandates opaque blue or brown glasses so judgment rests entirely on aroma and taste."),
            ("Are bitterness and pungency defects in olive oil?",
             "The opposite — they are positive attributes in the official panel assessment. Bitterness signals oleuropein and polyphenol content; pungency reveals oleocanthal. An oil with zero bitterness or pungency is typically refined, old, or low quality."),
            ("How can I tell if my olive oil is rancid at home?",
             "Rancid oil smells of cold candle wax, stale frying fat, or damp cardboard. On the palate, it leaves a persistent greasy sensation with no freshness. Not dangerous but completely devoid of gustatory and nutritional value."),
            ("Should I taste olive oil with bread?",
             "For a serious assessment, no — bread modifies aromatic perception. Professional tasters use bland white bread between samples to cleanse the palate, but not during the evaluation itself. Try the oil neat in a warmed glass for the most accurate impression.")
        ]
    },
    'cooking-with-olive-oil.html': {
        'h1': "Cooking with Olive Oil: Chef Secrets & Science",
        'meta': "How to cook with olive oil: smoke point, temperatures, pairings, frying and heat stability. Scientific facts and chef tips for daily cooking. 2026 guide.",
        'lede': "What actually works when cooking with olive oil.",
        'article': """
<p class="intro">Contrary to the widespread myth, extra virgin olive oil is perfectly suited for cooking. Its smoke point of 190–210°C makes it compatible with virtually all everyday culinary techniques, and its high oleic acid content makes it chemically more stable under heat than most vegetable oils on the market.</p>

<h2>Temperatures and Cooking Techniques</h2>
<p>Oleic acid (73% of composition) is highly resistant to thermal oxidation. A study published in <em>Acta Scientific Nutritional Health</em> compared 10 common cooking oils under heat and found extra virgin olive oil produces the fewest polar compounds — the markers of harmful oxidative degradation. It remains stable up to 180°C for everyday cooking and up to 210°C in brief exposure. Deep frying is possible but a dedicated frying oil is more economical for large volumes.</p>
<blockquote>"Olive oil isn't just for salads. In Italy and Greece, everything is cooked in olive oil — including fried dishes." — Tuscan family producer</blockquote>

<h3>Temperature Reference Guide</h3>
<ul>
<li><strong>Dressings and finishing</strong>: raw use, 100% aroma preservation</li>
<li><strong>Gentle cooking (vegetables, eggs)</strong>: 100–140°C — ideal, zero degradation</li>
<li><strong>Sautéing, pan-frying</strong>: 160–180°C — fully suitable</li>
<li><strong>Oven roasting</strong>: 180–200°C — stable, produces excellent browning</li>
<li><strong>Deep frying</strong>: 175–190°C — stable, but economically less optimal</li>
</ul>

<h2>Creative Uses and Flavor Pairings</h2>
<p>In Mediterranean cuisine, olive oil replaces butter in cakes (moister texture, longer shelf life), cream in purees (richness without heaviness), and acts as a tenderizer in marinades. A finishing drizzle on a hot dish is a key technique: heat releases fruity aromas without denaturing them. In desserts, a drizzle over panna cotta or vanilla ice cream creates surprising pairings — quality olive oil adds roundness and complexity that surpasses caramel in sophistication.</p>

<h3>Pairing Rules: Oil Intensity to Dish Type</h3>
<ul>
<li><strong>Mild, low-bitterness oil</strong> (Arbequina, Taggiasca): delicate fish, seafood, pastries, desserts</li>
<li><strong>Medium, balanced oil</strong> (Frantoio, Aglandau): white meats, roasted vegetables, pasta</li>
<li><strong>Intense, bitter and pungent</strong> (Picual, Koroneiki): red meats, legumes, hearty salads</li>
<li><strong>Herbaceous early harvest</strong>: bruschetta, soups, Provençal dishes</li>
</ul>
""",
        'faq': [
            ("Does olive oil lose nutrients when cooked?",
             "Partially. The most volatile polyphenols degrade above 180°C, but oleic acid remains intact through cooking. The oil retains its lipid benefits even heated. For full polyphenol preservation, add a raw drizzle at the end of cooking."),
            ("Can I reuse olive oil after frying?",
             "Yes, 2–3 times maximum if it hasn't darkened or smoked. Filter it hot to remove food particles that accelerate degradation. Discard when it turns dark or develops an acrid smell."),
            ("Is olive oil good for mayonnaise?",
             "Yes, but a very intense oil can dominate the flavor. Use a mild oil (Arbequina, Taggiasca) for cold sauces, or blend olive oil (30%) with a neutral oil (70%) for a balanced result."),
            ("How do Italians make pasta aglio e olio?",
             "Cook pasta al dente, reserve a cup of pasta water, drain. In a hot pan, briefly sauté garlic in olive oil (30 seconds), add pasta and a ladle of pasta water, toss vigorously. The starch emulsifies the oil and water into a glossy, creamy sauce — no cream needed.")
        ]
    },
    'olive-oil-production-process.html': {
        'h1': "From Tree to Bottle: The Olive Oil Production Process",
        'meta': "Complete guide to olive oil production: harvest timing, crushing, malaxation, cold extraction, filtration and storage. What separates great oil from ordinary.",
        'lede': "How a great olive oil is born — from harvest to bottle.",
        'article': """
<p class="intro">The quality of extra virgin olive oil is built at every stage of the process, from olive ripeness to bottling. A single mistake — late harvest, excessive transport time, malaxation temperature too high — is enough to transform exceptional potential into ordinary oil. Understanding the process helps you recognize and choose better oils.</p>

<h2>Harvest: The First Critical Decision</h2>
<p>Olives are harvested between October and January depending on region and variety. <em>Early harvest</em> oils (October–November), from still-green olives, contain up to twice the polyphenols and deliver intense herbaceous aromas. <em>Late harvest</em> (December–January), with fully ripe olives, yields milder, fruitier oils. Hand harvesting or mechanical combing is preferred: it avoids crushing fruit and premature fermentation. Once harvested, olives must reach the mill within 4–6 hours — every additional hour accelerates enzymatic degradation of polyphenols.</p>
<blockquote>"Between harvest and pressing, every hour counts. Our olives enter the mill within 4 hours of picking." — AOP Baux-de-Provence producer</blockquote>

<h3>Key Production Steps</h3>
<ul>
<li><strong>Harvest</strong>: hand-picked, combed or netted — crushing damages quality irreversibly</li>
<li><strong>Leaf removal and washing</strong>: done within 4–6 hours maximum after picking</li>
<li><strong>Crushing</strong>: traditional granite millstones or modern hammer crushers</li>
<li><strong>Malaxation</strong>: paste stirred 20–40 min at max 27°C (cold extraction standard)</li>
<li><strong>Horizontal centrifugation</strong>: separates oil, vegetable water and pomace</li>
<li><strong>Filtration</strong>: optional but recommended for shelf life and stability</li>
</ul>

<h2>Cold Extraction: The Defining Criterion</h2>
<p>The label "cold extracted" guarantees that malaxation temperature did not exceed 27°C. Above this threshold, polyphenol-degrading enzymes activate, volatile aromatics evaporate, and yield increases at the cost of quality. Higher yield (more oil per quintal of olives) often signals hot extraction — economically more profitable but qualitatively inferior. The finest artisan producers accept a 12–15% yield to preserve the full spectrum of bioactive compounds.</p>

<h3>Factors That Define Excellence</h3>
<ul>
<li><strong>Harvest-to-press delay</strong>: under 6 hours for the greatest oils</li>
<li><strong>Malaxation temperature</strong>: 27°C maximum — non-negotiable for cold extraction</li>
<li><strong>Malaxation duration</strong>: 25–35 minutes (neither too short nor too long)</li>
<li><strong>Variety and olive maturity</strong>: specific to each terroir and producer style</li>
<li><strong>Stainless steel storage under nitrogen</strong>: prevents oxidation after extraction</li>
</ul>
""",
        'faq': [
            ("What's the difference between cold extraction and first cold pressing?",
             "'First cold pressing' is a legacy term from old hydraulic stone presses, now obsolete. 'Cold extracted' is the current EU regulatory term, guaranteeing malaxation temperature ≤ 27°C. Both signal low-temperature production, but 'cold extracted' is the current legal standard."),
            ("How many olives does it take to produce one litre of oil?",
             "Typically 4–6kg of olives per litre, depending on variety, ripeness and extraction method. Early-harvest olives (more water, less oil) can require 7–8kg. Late-harvest oil-rich varieties may drop to 3–4kg per litre."),
            ("Are stone mills better than modern crushers?",
             "Legitimate debate. Stone mills grind more gently, preserving cell integrity and promoting certain aromatic profiles. But they heat up and oxidize more easily. Modern hammer crushers, well-operated, produce equally great oils with better reproducibility and hygiene."),
            ("Why are some olive oils cloudy?",
             "Cloudiness (haze) comes from microscopic pulp particles and natural waxes that remain after extraction. It disappears through filtration or natural decantation. Unfiltered oil is initially richer in short-term aromas but less stable — consume it faster once opened.")
        ]
    },
    'olive-oil-terroirs-and-regions.html': {
        'h1': "Olive Oil Terroirs & Regions: The World's Great Origins",
        'meta': "Spain, Italy, Greece, Tunisia, France: discover the world's great olive oil terroirs, their signature varieties and distinct aromatic profiles. Expert guide 2026.",
        'lede': "Where the world's finest olive oils come from — and what makes each unique.",
        'article': """
<p class="intro">Like wine, olive oil is deeply shaped by its terroir — soil, climate, altitude, olive variety and local expertise. A Koroneiki from the Peloponnese and an Arbequina from Catalonia are two radically different expressions of the same fruit, shaped by millennia of adaptation to their specific environments.</p>

<h2>The World's Major Producing Regions</h2>
<p>The Mediterranean basin concentrates 95% of global production. Spain is the world's top producer (45% of global output), primarily from Andalusia with Picual, Hojiblanca and Arbequina varieties. Greece, with just 2% of the world's population, produces 10% of global olive oil and consumes the most per capita (20 litres/year). Italy, despite lower volumes, leads in value thanks to prestigious PDOs. Tunisia is the world's top non-EU exporter, growing rapidly in quality recognition.</p>
<blockquote>"Every region gives olive oil its own language. The Peloponnese speaks of cut grass and artichoke; Tuscany says artichoke and green pepper."</blockquote>

<h3>Profiles of the Major Regions</h3>
<ul>
<li><strong>Andalusia (Spain)</strong>: Picual — powerful, robust, intense green fruitiness, excellent shelf life</li>
<li><strong>Catalonia (Spain)</strong>: Arbequina — mild, ripe fruit, almond, apple notes — ideal for beginners</li>
<li><strong>Tuscany (Italy)</strong>: Frantoio and Moraiolo — fresh herbs, artichoke, marked bitterness and pungency</li>
<li><strong>Peloponnese (Greece)</strong>: Koroneiki — tiny olive, highest polyphenol yield, intense pungency</li>
<li><strong>Sfax (Tunisia)</strong>: Chemlali — sweet almond, ripe fruit, great finesse and roundness</li>
<li><strong>Provence (France)</strong>: PDO Vallée des Baux, Aglandau and Salonenque — herb, almond, artichoke</li>
</ul>

<h2>The Importance of PDO and PGI Certifications</h2>
<p>Protected Designations of Origin guarantee that the oil is produced, processed and packaged within a defined geographical area, using regulated varieties and methods. The EU recognizes over 150 olive oil PDOs. These certifications protect producers from fraud and guide consumers toward traceable, authentic oils. The finest PDO oils typically command a price premium fully justified by their traceability, quality control and unique aromatic character that cannot be replicated outside their specific microclimate.</p>

<h3>How Terroir Shapes Flavor</h3>
<ul>
<li><strong>Limestone and dry soil</strong>: intense oils, high polyphenol content</li>
<li><strong>Deep clay soil</strong>: milder, fruitier profiles</li>
<li><strong>High altitude (&gt;400m)</strong>: slow ripening, complex aromas, elevated polyphenols</li>
<li><strong>Coastal proximity</strong>: subtle marine notes, lighter fruitiness</li>
<li><strong>Arid climate</strong>: water stress concentrates aromatic compounds</li>
</ul>
""",
        'faq': [
            ("Which country produces the best olive oil in the world?",
             "There's no definitive answer — it's a matter of personal preference. International competitions (Biol, EVOO World Rankings, NYIOOC) regularly crown oils from Greece, Spain, Italy, Morocco and Australia. The 'best' oil is the one that matches your palate and intended use."),
            ("Why are Greek olive oils so high in polyphenols?",
             "Three factors: the Koroneiki variety (naturally polyphenol-rich), the arid Mediterranean climate that stresses the tree and concentrates defensive compounds, and the tradition of early harvest (green olives) in much of the Peloponnese and Crete."),
            ("Are French olive oils worth the premium price?",
             "Yes, for those seeking unique aromatic profiles and maximum traceability. French production is tiny (5,000–10,000 tonnes/year vs. 1.3 million in Spain), making them inherently rare and expensive. PDO Baux-de-Provence and Nyons are genuine gastronomic treasures."),
            ("What distinguishes Tunisian olive oil from European oils?",
             "Tunisia produces primarily mild, fruity oils from Chemlali and Chétoui varieties, generally less bitter than European counterparts. Sahel climatic conditions create a very distinct profile: more almond, less vegetal, with a roundness particularly appreciated in Middle Eastern cuisine and pastry.")
        ]
    },
    'how-to-choose-best-olive-oil.html': {
        'h1': "How to Choose the Best Olive Oil: A Buyer's Guide",
        'meta': "How to choose great olive oil: reading labels, polyphenol content, acidity, PDO certifications, harvest date and quality signals. Expert buying guide 2026.",
        'lede': "The criteria that separate a great olive oil from an ordinary one.",
        'article': """
<p class="intro">The olive oil aisle can appear deceptively uniform, but quality differences are enormous. Between a €3/litre supermarket oil and a €25/litre artisan oil, it's not just the label that changes — it's the chemical composition, aromatic profile and health impact on your body.</p>

<h2>Reading the Label: Key Information</h2>
<p>The first distinction is the category: only <strong>"Extra Virgin"</strong> guarantees free acidity below 0.8% and no detectable organoleptic defects. "Virgin" (acidity ≤ 2%) allows slight defects; "Olive Oil" is a blend of refined oil (odorless, tasteless) and virgin oil to add minimal aroma — virtually no polyphenols. The <strong>harvest date</strong> is more informative than the best-before date: oil from the previous harvest is still safe but has lost its aromatic peak. Look for a recent harvest, ideally within the last 12 months.</p>
<blockquote>"The harvest date is the most honest freshness indicator a producer can give you."</blockquote>

<h3>Selection Criteria by Priority</h3>
<ul>
<li><strong>"Extra Virgin" label</strong>: the non-negotiable minimum entry point</li>
<li><strong>Harvest date</strong>: prefer oil harvested within the past 12–18 months</li>
<li><strong>PDO/DOP or certification</strong>: guarantees origin and production methods</li>
<li><strong>Polyphenol content</strong>: ideally &gt;250mg/kg (stated on premium bottles)</li>
<li><strong>Packaging</strong>: dark glass or opaque tin — light degrades oil within weeks</li>
<li><strong>Single origin</strong>: avoid "blend of EU countries" for premium purchases</li>
</ul>

<h2>Price as a Quality Signal</h2>
<p>A quality extra virgin olive oil cannot cost less than €8–10 per litre in traditional retail. Production costs alone (hand harvesting, transport, cold extraction) exceed €5 per litre for small producers. Oils priced at €3–4/litre in supermarkets are multi-origin blends, often from old harvest, with very low polyphenol profiles. This isn't fraud — it's simply a different product, suitable for mass cooking but unsuitable for health or gastronomic applications.</p>

<h3>Red Flags to Avoid</h3>
<ul>
<li>No harvest date (only a best-before date)</li>
<li>"Blend of EU and non-EU countries" without specific country</li>
<li>Price under €7–8/litre for a supposedly premium oil</li>
<li>Transparent glass bottle exposed to light on shelf or at home</li>
<li>No aroma whatsoever when you open the bottle</li>
</ul>
""",
        'faq': [
            ("Is a cloudy olive oil a quality sign?",
             "Not necessarily. Haze indicates an unfiltered oil, richer in short-term aromas but more fragile to store. It's a producer choice, not an absolute quality criterion. A filtered, clear oil can vastly outperform a cloudy one that was poorly stored or harvested late."),
            ("Are organic olive oils automatically better?",
             "Organic certification guarantees no synthetic pesticides — not gustatory quality or polyphenol richness. An organic oil can be mediocre if harvested late or extracted carelessly. A non-organic artisan oil produced with precision can outperform industrial organic oil in every measurable quality dimension."),
            ("Can I trust competition medals on the label?",
             "Major competitions (NYIOOC, EVOO World Rankings, TerraOlivo, Biol) have rigorous blind-tasting panels — their medals are a reliable quality signal. Small generic local competitions carry less weight. A gold medal at NYIOOC or Biol is a serious indicator of exceptional quality."),
            ("What's the difference between mild and intense olive oil?",
             "Intensity depends on variety, harvest timing and terroir. 'Mild' means low bitterness and pungency (Arbequina, late harvest) — best for delicate fish, desserts, beginners. 'Intense' means marked bitterness and pungency (Picual, Koroneiki, early harvest) — best for red meat, legumes, and maximum health benefit.")
        ]
    },
    'olive-oil-storage-tips.html': {
        'h1': "Olive Oil Storage: How to Preserve Quality and Benefits",
        'meta': "How to properly store olive oil: light, heat, air, containers and shelf life. Avoid the mistakes that turn great oil rancid within weeks.",
        'lede': "The storage rules that protect quality from first drop to last.",
        'article': """
<p class="intro">Olive oil is fragile. Three enemies degrade it silently: light, heat and oxygen. A perfect bottle can turn rancid in a few weeks if stored incorrectly. These rules will help you preserve your oils until the very last drop.</p>

<h2>The Three Enemies of Olive Oil</h2>
<p><strong>Light</strong> triggers photo-oxidative reactions that degrade polyphenols and produce aldehyde compounds responsible for rancidity. Dark glass bottles or opaque tins are essential — never store olive oil in transparent glass on a sun-exposed counter. <strong>Heat</strong> accelerates oxidation and fatty acid degradation: keep away from the stove, oven, or any warm spot. <strong>Oxygen</strong> oxidizes lipids progressively: always replace the cap firmly, and for large containers, transfer into smaller bottles as you consume.</p>
<blockquote>"Olive oil left on the kitchen counter in a clear bottle loses 30% of its polyphenols within a month."</blockquote>

<h3>Ideal Storage Conditions</h3>
<ul>
<li><strong>Temperature</strong>: 14–18°C ideally, 20°C maximum — cellar or interior cupboard</li>
<li><strong>Light</strong>: complete darkness — opaque tin or closed cupboard</li>
<li><strong>Oxygen</strong>: airtight cap, bottle filled to minimize headspace</li>
<li><strong>Humidity</strong>: dry environment — moisture promotes mold on caps</li>
<li><strong>Optimal shelf life</strong>: consume within 18 months of harvest date</li>
</ul>

<h2>Should You Refrigerate Olive Oil?</h2>
<p>Refrigeration is not recommended for everyday use: oil solidifies below 7°C and turns hazy around 10°C. This is reversible (bring back to room temperature), but repeated cold–warm cycles can accelerate oxidation. However, for valuable oils you consume slowly, refrigeration can extend shelf life beyond 24 months. Top producers store reserves in stainless steel tanks at 12–15°C under nitrogen to prevent any oxygen contact — the ultimate preservation method.</p>

<h3>Shelf Life by Container Type</h3>
<ul>
<li><strong>3–5L sealed tin</strong>: 24–30 months unopened</li>
<li><strong>Dark glass bottle</strong>: 18–24 months unopened, 3–6 months after opening</li>
<li><strong>Open kitchen carafe</strong>: 2–4 weeks maximum</li>
<li><strong>Transparent squeeze bottle</strong>: avoid — degrades within days under kitchen light</li>
</ul>
""",
        'faq': [
            ("How can I tell if my olive oil is still good?",
             "Smell it: a good oil has fruity, vegetal or almond aromas. If it smells of candle wax, wet cardboard or stale frying fat, it's oxidized. On the palate, flat, greasy, with no freshness = lost polyphenols and aroma. Not dangerous, but without gustatory or nutritional value."),
            ("Can I freeze olive oil for long-term storage?",
             "Technically yes — freezing stops oxidation. But defrosting can cause compound separation if done too quickly. If you freeze, defrost slowly in the refrigerator. The result is acceptable, but delicate aromas and texture may slightly suffer."),
            ("Does olive oil actually expire?",
             "It doesn't 'rot' in the food-safety sense, but it goes rancid. Rancid oil presents no serious health risk, but loses all value — no polyphenols, no aroma, unpleasant taste. Still usable for basic cooking, but you're no longer getting what you paid for."),
            ("Can I use olive oil to preserve foods (herbs, cheeses)?",
             "Yes — a traditional technique for aromatic herbs, cheeses and grilled vegetables. Olive oil creates an anaerobic barrier inhibiting aerobic bacteria. However: fresh garlic preserved in oil at room temperature carries a botulism risk. Only do this in the refrigerator and consume within one week.")
        ]
    },
    'organic-and-sustainable-olive-oil.html': {
        'h1': "Organic and Sustainable Olive Oil: What You Need to Know",
        'meta': "What organic olive oil certifications really guarantee, environmental impact of olive farming, and how to choose genuinely sustainable oils. Expert guide 2026.",
        'lede': "Sustainability and organic olive oil: what the labels really mean.",
        'article': """
<p class="intro">The olive oil industry faces a paradox: the olive tree is one of the most resilient and ecologically virtuous trees on earth, yet economic and climate pressures are pushing some producers toward intensive practices that threaten this millennia-old balance.</p>

<h2>What Organic Certification Guarantees (and Doesn't)</h2>
<p>Organic certification (EU Organic, USDA Organic, AB in France) guarantees the absence of synthetic pesticides, chemical herbicides and GMOs. It mandates agronomic practices respectful of soil health and biodiversity. What it doesn't guarantee: gustatory quality, polyphenol richness, or animal welfare. An organic oil can be produced industrially at large scale from late-harvested olives poorly extracted. The organic label is necessary but not sufficient for exceptional quality.</p>
<blockquote>"The olive tree has grown without chemical inputs for 3,000 years. In a sense, organic is its natural state."</blockquote>

<h3>Key Certifications to Know</h3>
<ul>
<li><strong>EU Organic / AB</strong>: certified without synthetic pesticides — EU standard</li>
<li><strong>Demeter</strong>: biodynamic — stricter requirements than standard organic</li>
<li><strong>PDO/DOP</strong>: origin and method controlled — not necessarily organic, but traceable</li>
<li><strong>Rainforest Alliance</strong>: environmental and social management sustainability</li>
<li><strong>Fair Trade</strong>: commercial equity for small producers</li>
</ul>

<h2>The Environmental Impact of Olive Farming</h2>
<p>A traditional olive grove is a significant carbon sink: one hectare of olive trees sequesters 2.5–4 tonnes of CO₂ per year. Extensive cultivation promotes biodiversity (birds, insects, flora) and protects soil from erosion through deep roots. Modern intensive systems — high-density planting (>1,000 trees/ha vs. 50–150 in extensive), heavy irrigation and full mechanization — present a less favorable carbon balance and reduce biodiversity. However, they enable price competitiveness that makes olive oil accessible to all income levels.</p>

<h3>Choosing a Genuinely Sustainable Oil</h3>
<ul>
<li><strong>Traditional extensive groves</strong>: density &lt;200 trees/ha, rain-fed (no irrigation)</li>
<li><strong>Small certified organic producers</strong>: minimal impact, maximum traceability</li>
<li><strong>Local and short-supply-chain oils</strong>: reduced transport carbon footprint</li>
<li><strong>Bulk or large format packaging</strong>: less packaging waste per litre consumed</li>
<li><strong>Pomace valorization</strong>: olive marc used for energy, cosmetics or compost</li>
</ul>
""",
        'faq': [
            ("Does converting to organic farming improve oil quality?",
             "Not automatically. Quality depends far more on variety, harvest timing and extraction mastery. However, organic producers tend to be more attentive to the entire production chain, and the absence of chemical inputs can encourage more complex aromatic profiles in living soils."),
            ("Is olive oil an environmentally friendly product?",
             "Compared to other vegetable oils (palm, intensive rapeseed, soy), traditional olive cultivation has an excellent environmental balance: low water needs, minimal inputs, effective carbon sink, remarkable longevity (some trees have produced for 1,000 years). Intensive olive agriculture is more debatable."),
            ("What happens to the pomace after extraction?",
             "Olive pomace (marc) is valorized several ways: as boiler fuel, as pomace oil (hexane solvent extraction for budget cooking oil), as agricultural compost, or in cosmetics (scrubs, soaps). Modern mills aim to valorize 100% of raw material — a zero-waste ambition."),
            ("Are there certifications for high-polyphenol olive oils?",
             "Yes. The EFSA authorizes a health claim for oils containing over 250mg/kg of polyphenols (hydroxytyrosol and derivatives). Some producers have polyphenol content certified by accredited laboratories and display it on the label. This is a serious marker of functional quality.")
        ]
    },
    'olive-oil-beauty-and-skincare.html': {
        'h1': "Olive Oil for Skin and Beauty: A Complete Guide",
        'meta': "Olive oil in cosmetics: hydration, anti-aging, face and body care. DIY formulas, precautions and comparison with modern cosmetic oils. Science-based guide 2026.",
        'lede': "The ancient beauty secret — validated by modern science.",
        'article': """
<p class="intro">Since Cleopatra bathed in olive oil and milk, Mediterranean women have used olive oil as a complete beauty treatment. Modern science validates these ancestral uses: squalene, tocopherols and polyphenols make it a remarkable cosmetic active.</p>

<h2>Active Cosmetic Properties</h2>
<p>Olive oil contains several compounds directly beneficial to skin. <strong>Squalene</strong> (0.3–1%) is a natural emollient identical to that produced by our own sebum — it penetrates without greasy residue and moisturizes deeply. <strong>Tocopherols</strong> (vitamin E) protect cell membranes against free radical oxidation, the central mechanism of skin aging. <strong>Hydroxytyrosol</strong> exerts documented anti-inflammatory action that calms sensitive and reactive skin. These properties exist only in quality extra virgin oil — refined oils have lost these bioactive compounds entirely.</p>
<blockquote>"Extra virgin olive oil contains over 200 phytochemical actives, many with cosmetic efficacy comparable to high-end synthetic ingredients."</blockquote>

<h3>Most Effective Cosmetic Uses</h3>
<ul>
<li><strong>Makeup remover</strong>: dissolves oil-based and waterproof makeup without aggression — safe on eyes</li>
<li><strong>Lip balm</strong>: a few pure drops on chapped lips — immediate relief</li>
<li><strong>Cuticle care</strong>: daily massage nourishes and softens skin around nails</li>
<li><strong>After-sun treatment</strong>: soothes redness and nourishes sun-depleted skin</li>
<li><strong>Nourishing face mask</strong>: 2 tablespoons on dry face, 15 minutes, warm water rinse</li>
<li><strong>Body oil</strong>: applied on slightly damp skin after shower for best absorption</li>
</ul>

<h2>Precautions and Contraindications</h2>
<p>Olive oil is not right for all skin types. Its moderate comedogenic rating (2 out of 5) makes it inadvisable for oily, combination or acne-prone skin — it can clog pores and worsen comedones. For these profiles, choose lighter oils (jojoba, rosehip, hazelnut). Normal to dry skin types tolerate and benefit greatly from olive oil as a night occlusive treatment. For eczema or dermatitis, consult a dermatologist before regular use — clinical studies show contradictory results depending on individual skin barrier function.</p>

<h3>Simple and Effective DIY Formulas</h3>
<ul>
<li><strong>Body scrub</strong>: 3 tbsp olive oil + 2 tbsp cane sugar + lemon zest</li>
<li><strong>Hair mask</strong>: warm olive oil on lengths, 30 min under a warm towel, shampoo out</li>
<li><strong>Hand cream</strong>: blend olive oil, melted beeswax and lavender essential oil</li>
<li><strong>Nourishing foot soak</strong>: warm water + olive oil + a few drops of tea tree oil</li>
</ul>
""",
        'faq': [
            ("Is olive oil good for all skin types on the face?",
             "No. It suits dry, normal and mature skin. Not recommended for oily and acne-prone skin due to moderate comedogenic potential. For sensitive skin, patch test on a small area before widespread use. Jojoba oil is often a better universal alternative."),
            ("Can I replace my moisturizer with olive oil?",
             "Partially. Olive oil is an excellent emollient (it softens and nourishes) but not a humectant (it doesn't draw water into skin like hyaluronic acid). For optimal hydration: apply on slightly damp skin after shower, or layer over a hydrating serum first."),
            ("Which olive oil should I choose for cosmetic use?",
             "Extra virgin, high quality, with a recent harvest date. Cosmetic products based on refined olive oil have lost their bioactive compounds — counterproductive for a beauty application. Choose the same quality oil you'd happily put on your plate."),
            ("Does olive oil help prevent stretch marks?",
             "It can help in prevention for pregnant women by nourishing and softening the skin, improving elasticity. On existing stretch marks (white scars), effect is limited — no vegetable oil can erase established stretch marks. Best preventive results come from daily application from early pregnancy onward.")
        ]
    },
    'history-and-culture-of-olive-oil.html': {
        'h1': "The History and Culture of Olive Oil: 5,000 Years of Civilization",
        'meta': "The history of olive oil from antiquity to today: Greek mythology, ancient Rome, medieval trade, and the olive tree as universal cultural symbol across civilizations.",
        'lede': "Five thousand years of history in every drop of olive oil.",
        'article': """
<p class="intro">No other food has played a more central role in human history than olive oil. Currency, sacred fuel, medicine, cosmetic and food — olive oil accompanied the birth of Mediterranean civilizations for over five millennia, and continues to shape cultures across the globe today.</p>

<h2>From Mythical Origins to Archaeological Reality</h2>
<p>The cultivated olive tree (<em>Olea europaea</em>) emerged from a domestication process dating back to 6,000 BC in Anatolia and the Levant. The first evidence of oil extraction dates to 4,000 BC in Haifa (present-day Israel). Ancient Greeks made the olive tree a sacred symbol: in mythology, it was Athena who gave the olive to Athens, defeating Poseidon in the contest for the city's guardianship. Olympic victors received crowns of wild olive branches — the <em>kotinos</em> — and amphoras of Attic olive oil as prizes.</p>
<blockquote>"The olive tree is Mediterranean civilization itself. Wherever the olive grows, man settles, cultivates and creates." — Fernand Braudel, historian</blockquote>

<h3>Major Milestones in Olive Oil History</h3>
<ul>
<li><strong>4,000 BC</strong>: first extraction evidence in the Levant and Minoan Crete</li>
<li><strong>776 BC</strong>: olive oil prizes at the first Olympic Games</li>
<li><strong>2nd century BC</strong>: Rome becomes the world's largest olive oil importer</li>
<li><strong>1st century AD</strong>: Hispania (Spain) surpasses Greece in production volume</li>
<li><strong>7th century</strong>: Arab expansion spreads olive cultivation across North Africa and Spain</li>
<li><strong>15th century</strong>: Spanish conquistadors plant olive trees in Latin America</li>
</ul>

<h2>Olive Oil in the World's Great Religions and Cultures</h2>
<p>Olive oil transcends cultures and religions. In the Bible, the olive is a symbol of peace (Noah's dove returns with an olive branch). The Catholic Church uses olive oil in all its sacraments — baptism, confirmation, anointing of the sick. The Quran mentions the olive tree as a blessed tree. In Greece and Italy, harvest rituals remain powerful moments of social and family cohesion, passed from generation to generation. The olive tree is far more than a crop — it is a shared cultural language spoken by 500 million people across three continents.</p>

<h3>The Olive Tree as Living Heritage</h3>
<ul>
<li>Some olive trees in Sardinia, Crete and Palestine are over <strong>2,000 years old</strong></li>
<li>The Vouves olive tree in Crete is estimated at <strong>3,000–4,000 years old</strong> and still produces olives</li>
<li>Historic olive groves are inscribed in <strong>UNESCO World Heritage</strong> in Greece and Portugal</li>
<li>The <strong>Mediterranean diet</strong> itself is inscribed in UNESCO's Intangible Cultural Heritage list</li>
</ul>
""",
        'faq': [
            ("Which country invented olive oil?",
             "The domestication of the olive tree occurred simultaneously across several regions of the Middle East and Eastern Mediterranean — Syria, Lebanon, Palestine, Crete — between 6000 and 4000 BC. There is no single inventor: it was a gradual discovery shared by multiple civilizations of the Fertile Crescent."),
            ("How did the Romans use olive oil?",
             "Romans consumed an estimated 20–40 litres of olive oil per person per year. Uses included cooking, lighting (oil lamps), perfumery (blended with aromatic herbs), bathing (strigil + oil instead of soap), and medicine. Rome imported massively from Hispania and North Africa."),
            ("Why is the olive branch a symbol of peace?",
             "The symbolism traces to the Biblical Genesis (Noah's dove returning with an olive branch signaling the end of the Flood) and to Greek tradition (olive trees planted in sacred spaces where violence was forbidden). The United Nations has used the olive branch in its emblem since 1945."),
            ("Are there ancient olive trees still producing fruit?",
             "Yes. The Vouves olive tree in Crete, estimated at 3,000–4,000 years old, still produces olives harvested annually. In Sardinia, several millennial olive trees remain active. The 'Ses Oliveres Velles' olive trees in Majorca are estimated at 1,000 years old and still productive.")
        ]
    },
    'extra-virgin-vs-virgin-olive-oil.html': {
        'h1': "Extra Virgin vs Virgin Olive Oil: Understanding the Categories",
        'meta': "The difference between extra virgin, virgin and ordinary olive oil: acidity, defects, polyphenols, uses and price. Complete comparison and buying guide.",
        'lede': "Extra virgin, virgin, olive oil: what these categories actually mean.",
        'article': """
<p class="intro">The label "olive oil" covers very different realities. EU Regulation CE 2568/91 defines several categories with precise chemical and organoleptic criteria. Understanding these distinctions enables informed purchases and appropriate use of each type in your kitchen.</p>

<h2>Official Categories and Their Criteria</h2>
<p><strong>Extra virgin olive oil</strong> sits at the top of the hierarchy: maximum free acidity of 0.8%, no detectable organoleptic defects, and polyphenols present in significant quantities. It's the only category worth investing in for health and gastronomic applications. <strong>Virgin olive oil</strong> allows acidity up to 2% and slight perceptible defects — it remains mechanically pressed without refining, but of inferior quality. Plain <strong>"Olive oil"</strong> is a blend of refined oil (odorless, flavorless) and virgin oil for minimal aroma: virtually no polyphenols, maximum acidity 1%.</p>
<blockquote>"Refining eliminates defects but also all the bioactive compounds that give olive oil its health value."</blockquote>

<h3>Comparative Overview of Categories</h3>
<ul>
<li><strong>Extra virgin</strong>: acidity ≤0.8%, zero defects, high polyphenols — raw and cooking use</li>
<li><strong>Virgin</strong>: acidity ≤2%, minor defects tolerated, medium polyphenols — cooking use</li>
<li><strong>Lampante</strong>: acidity &gt;3.3%, unfit for consumption raw — destined for refining</li>
<li><strong>Refined olive oil</strong>: from refined lampante, acidity ≤0.3%, no taste or aroma</li>
<li><strong>Olive oil</strong>: refined + virgin blend, acidity ≤1%, minimal polyphenols</li>
<li><strong>Olive pomace oil</strong>: from solvent-extracted pomace — cheaper, lower quality</li>
</ul>

<h2>Why Fraud Exists and How to Protect Yourself</h2>
<p>The price gap between genuine extra virgin (€8–30/L) and ordinary olive oil (€2–5/L) creates fraud incentive. Recurring scandals have exposed oils labeled "extra virgin" containing refined oils or misrepresented origins. The EU has strengthened controls since 2012 with mandatory chemical analyses (K232, K270, delta-K, fatty acid composition). To protect yourself: prioritize PDO/DOP oils, independent traceable producers, and prices consistent with claimed quality. A genuine artisan extra virgin under €7/litre should raise questions.</p>

<h3>Choosing by Use Case</h3>
<ul>
<li><strong>Finishing, salads, dipping</strong>: quality extra virgin with intense fruitiness</li>
<li><strong>Everyday cooking (sautéing, roasting)</strong>: extra virgin or virgin — heat-stable</li>
<li><strong>Large-volume deep frying</strong>: ordinary olive oil — cheaper, similar smoke point</li>
<li><strong>Cosmetic and skin care</strong>: extra virgin only — polyphenols are the key actives</li>
</ul>
""",
        'faq': [
            ("Does the acidity percentage on the label predict quality?",
             "Partially. Very low acidity (&lt;0.3%) is necessary for a great oil, but not sufficient. A refined oil has near-zero acidity but zero polyphenols. Acidity reflects olive quality at harvest and pressing speed, but must be read alongside other criteria like harvest date and polyphenol content."),
            ("Can you taste the difference between extra virgin and virgin?",
             "A trained taster can detect the slight defects of a virgin oil. For the occasional consumer, the difference is subtle on fresh samples. What is clearly perceptible: aromatic intensity, bitterness and pungency are systematically more pronounced in quality extra virgin oils."),
            ("Is refined olive oil unhealthy?",
             "Not harmful, but it doesn't deliver the health benefits of extra virgin. Without polyphenols or oleocanthal, it's an oil rich in oleic acid (good) but stripped of the antioxidants and anti-inflammatories that make extra virgin olive oil specifically valuable for health."),
            ("What does 'first cold pressed' mean on the label?",
             "It's a historical reference to old stone hydraulic presses, now replaced by continuous centrifugation. The current regulatory term is 'cold extracted' (≤27°C). Both indicate low-temperature production, but 'first cold pressed' has no technical meaning with modern equipment.")
        ]
    },
    'olive-oil-market-trends-2026.html': {
        'h1': "Olive Oil Market Trends 2026: Analysis and Outlook",
        'meta': "Olive oil market in 2026: record prices, climate crisis, premium trends, emerging producers and perspectives for buyers and producers. In-depth analysis.",
        'lede': "Understanding the global olive oil market in 2026.",
        'article': """
<p class="intro">The global olive oil market is undergoing unprecedented transformation. The historically low harvests of 2023 and 2024 pushed prices to levels unseen in 30 years, restructuring the entire supply chain and accelerating structural trends that are redefining what consumers buy and what producers cultivate.</p>

<h2>The Price Crisis: Causes and Consequences</h2>
<p>Between 2022 and 2024, bulk olive oil prices on Spanish markets tripled, rising from €3–4/kg to €8–9/kg. Multiple factors converged: record drought in Andalusia (−50% production in 2023), late frost in Italy, Xylella fastidiosa disease devastation in Puglia, and steadily rising global demand particularly from Asia and North America. This price surge accelerated the rise of non-European producers — Morocco, Turkey, Argentina, Chile, Australia — partially filling the European supply deficit and gaining permanent market share in the process.</p>
<blockquote>"The climate crisis has transformed the olive oil market: producers investing in climate resilience and premium quality will be the winners."</blockquote>

<h3>Key Market Figures 2025–2026</h3>
<ul>
<li><strong>Global production</strong>: approximately 2.5 million tonnes (vs. 3.3M in 2021)</li>
<li><strong>Spain</strong>: 60% of EU production, severely impacted by drought</li>
<li><strong>Morocco</strong>: +40% planted area over the past decade — a major new force</li>
<li><strong>EU consumer prices</strong>: +80–120% between 2022 and 2024</li>
<li><strong>High-growth markets</strong>: China (+15%/year), USA (+8%/year), Brazil (+12%/year)</li>
</ul>

<h2>Structural Trends for 2026 and Beyond</h2>
<p>Beyond the cyclical crisis, three structural trends are transforming the market. First, <strong>premiumization</strong>: consumers are buying less but buying better, with growing demand for PDO oils, single-varietals and early harvests. Second, <strong>geographic diversification</strong>: Australia, South Africa, California and Chile are investing massively and gaining market share with distinct aromatic profiles. Third, <strong>technology</strong>: IoT sensors in groves, AI for harvest optimization, blockchain for traceability — the industry is modernizing rapidly.</p>

<h3>Identified Opportunities for 2026</h3>
<ul>
<li><strong>Ultra-premium segment</strong>: oils above €40/L, niche market in strong growth</li>
<li><strong>DTC (direct-to-consumer)</strong>: subscriptions, gift sets and e-commerce rising fast</li>
<li><strong>Functional oils</strong>: certified high polyphenol content, health market opportunity</li>
<li><strong>New producers</strong>: Morocco, Turkey and Australia gaining in quality and recognition</li>
<li><strong>Consumer education</strong>: tasting workshops, olive oil sommelier certifications expanding</li>
</ul>
""",
        'faq': [
            ("Why have olive oil prices risen so dramatically?",
             "A combination of record drought in Spain (the world's top producer), late frost in Italy, Xylella disease in Puglia, and rising global demand. Between 2022 and 2024, European production fell 30–40% while demand continued to grow, particularly in Asia and North America."),
            ("Will prices come down in 2026?",
             "The 2025–2026 harvest outlook is more favorable following better rainfall. Prices should ease but remain above pre-2022 levels. Structural dependence on Mediterranean climate conditions means price volatility remains a permanent feature of this industry."),
            ("Which emerging producing countries should I watch?",
             "Morocco (Meknes, Marrakech), Australia (Margaret River, Riverina), Argentina (Mendoza), Chile and California. These producers benefit from Mediterranean climates, are investing heavily, and are beginning to win — at major international competitions — against long-established European producers."),
            ("How is technology transforming the olive oil industry?",
             "Three axes: production (soil and weather sensors, precision irrigation, drones for grove health monitoring), quality (NIR spectroscopy for real-time polyphenol analysis at the mill), and traceability (blockchain to certify origin from grove to bottle). AI is also optimizing variety-specific harvest timing with unprecedented precision.")
        ]
    },
}

HREFLANG_EN = {
    'health-benefits-olive-oil.html': ('bienfaits-sante-huile-olive.html', 'health-benefits-olive-oil.html', 'benefici-salute-olio-oliva.html', 'ofeli-igia-elaio-lado.html'),
    'olive-oil-tasting-guide.html': ('guide-degustation-huile-olive.html', 'olive-oil-tasting-guide.html', 'guida-degustazione-olio-oliva.html', 'odigos-dokimis-elaio-ladou.html'),
    'cooking-with-olive-oil.html': ('cuisiner-avec-huile-olive.html', 'cooking-with-olive-oil.html', 'cucinare-con-olio-oliva.html', 'magirema-me-elaio-lado.html'),
    'olive-oil-production-process.html': ('processus-fabrication-huile-olive.html', 'olive-oil-production-process.html', 'processo-produzione-olio-oliva.html', 'diadikasía-paragogís-elaio-ladou.html'),
    'olive-oil-terroirs-and-regions.html': ('terroirs-regions-huile-olive.html', 'olive-oil-terroirs-and-regions.html', 'terroir-e-regioni-olio-oliva.html', 'terroirs-kai-periochés-elaio-ladou.html'),
    'how-to-choose-best-olive-oil.html': ('comment-choisir-huile-olive.html', 'how-to-choose-best-olive-oil.html', 'come-scegliere-migliore-olio-oliva.html', 'pos-na-dialexete-to-kalitero-elaio-lado.html'),
    'olive-oil-storage-tips.html': ('conservation-huile-olive-conseils.html', 'olive-oil-storage-tips.html', 'consigli-conservazione-olio-oliva.html', 'simvoules-sintirisis-elaio-ladou.html'),
    'organic-and-sustainable-olive-oil.html': ('huile-olive-bio-durabilite.html', 'organic-and-sustainable-olive-oil.html', 'olio-oliva-biologico-e-sostenibile.html', 'viologiko-kai-viosimo-elaio-lado.html'),
    'olive-oil-beauty-and-skincare.html': ('huile-olive-beaute-soins-peau.html', 'olive-oil-beauty-and-skincare.html', 'olio-oliva-bellezza-cura-pelle.html', 'elaio-lado-omorfia-kai-derma.html'),
    'history-and-culture-of-olive-oil.html': ('histoire-culture-huile-olive.html', 'history-and-culture-of-olive-oil.html', 'storia-e-cultura-dell-olio-oliva.html', 'istoria-kai-politismos-elaio-ladou.html'),
    'extra-virgin-vs-virgin-olive-oil.html': ('difference-extra-vierge-vierge.html', 'extra-virgin-vs-virgin-olive-oil.html', 'differenza-extra-vergine-e-vergine.html', 'diafora-extra-partheno-kai-partheno.html'),
    'olive-oil-market-trends-2026.html': ('tendances-marche-huile-olive-2026.html', 'olive-oil-market-trends-2026.html', 'tendenze-mercato-olio-oliva-2026.html', 'taseis-agoras-elaio-ladou-2026.html'),
}

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
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
            <a href="../index.html">Home</a> &raquo; <a href="../index.html#guides">Guides</a> &raquo; {h1}
        </div>
        <h1>{h1}</h1>
        <p class="lede">{lede}</p>
        <div class="meta">Published: April 2026 &middot; 8 min read</div>
    </div>
</header>

<main class="container">
    <article class="guide">
        {article}
    </article>

    <section class="faq">
        <h2>Frequently Asked Questions</h2>
        {faq}
    </section>
</main>

<section class="related">
    <div class="container">
        <h2>Related Guides</h2>
        <div class="grid">
            {related}
        </div>
    </div>
</section>

<footer class="site-footer">
    <div class="container">
        <h3>L'Or Vert</h3>
        <p>Olive Oil Market Study 2026. Analysis of premium trends and opportunities.</p>
        <div class="copyright">&copy; 2026 &mdash; All rights reserved</div>
    </div>
</footer>

</body>
</html>"""


def build_faq(faq_list):
    return '\n'.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faq_list)


def build_hreflang(urls):
    fr, en, it, el = urls
    return (
        f'<link rel="alternate" hreflang="fr" href="https://huiledefes.com/guides/{fr}" />\n'
        f'    <link rel="alternate" hreflang="en" href="https://huiledefes.com/guides/{en}" />\n'
        f'    <link rel="alternate" hreflang="it" href="https://huiledefes.com/guides/{it}" />\n'
        f'    <link rel="alternate" hreflang="el" href="https://huiledefes.com/guides/{el}" />'
    )


def build_lang_switch(urls, current):
    fr, en, it, el = urls
    parts = []
    for label, fname in [('FR', fr), ('EN', en), ('IT', it), ('EL', el)]:
        cls = ' class="active"' if fname == current else ''
        parts.append(f'<a href="{fname}"{cls}>{label}</a>')
    return ' '.join(parts)


def build_related(current, all_files):
    links = []
    for fname, data in all_files.items():
        if fname != current and len(links) < 3:
            links.append(f'<a href="{fname}">{data["h1"]}</a>')
    return '\n'.join(links)


def main():
    count = 0
    for filename, data in GUIDES.items():
        filepath = os.path.join(DIR, filename)
        if not os.path.exists(filepath):
            print(f"SKIP: {filename}")
            continue
        urls = HREFLANG_EN[filename]
        html = TEMPLATE.format(
            h1=data['h1'],
            meta=data['meta'],
            lede=data['lede'],
            article=data['article'],
            faq=build_faq(data['faq']),
            related=build_related(filename, GUIDES),
            hreflang=build_hreflang(urls),
            lang_switch=build_lang_switch(urls, filename),
        )
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"OK: {filename}")
        count += 1
    print(f"\nDone: {count} EN guide pages regenerated.")


if __name__ == '__main__':
    main()

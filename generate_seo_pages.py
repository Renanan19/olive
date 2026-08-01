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
    {"fr": " pour la santé", "en": " for health", "it": " per la salute", "el": " για την υγεία"},
    {"fr": " en cuisine", "en": " in cooking", "it": " in cucina", "el": " στη μαγειρική"},
    {"fr": " pour le visage", "en": " for the face", "it": " per il viso", "el": " για το πρόσωπο"},
    {"fr": " pour les cheveux", "en": " for hair", "it": " per i capelli", "el": " για τα μαλλιά"},
    {"fr": " au quotidien", "en": " for daily use", "it": " nell'uso quotidiano", "el": " στην καθημερινότητα"}
]

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

translations = {
    "fr": {
        "index": "index-fr.html", "home": "Accueil", "guides": "Guides", "pub": "Publication", "min": "min de lecture",
        "intro": "L'huile d'olive est au coeur de la diète méditerranéenne. Ce guide explore ses multiples facettes pour vous aider à mieux la comprendre et l'intégrer à votre vie quotidienne avec des produits de haute qualité.",
        "h2_1": "Pourquoi s'y intéresser ?", "p_1": "Riche en antioxydants et en bons acides gras, elle offre des propriétés exceptionnelles reconnues par les experts de la nutrition et de la santé du monde entier.",
        "h3_1": "Points clés",
        "li_1_s": "Qualité :", "li_1_t": "Privilégiez toujours l'extraction à froid pour conserver tous les nutriments.",
        "li_2_s": "Conservation :", "li_2_t": "À conserver à l'abri de la lumière et de la chaleur dans une bouteille sombre.",
        "li_3_s": "Usage :", "li_3_t": "Idéale à cru (en salade, sur du pain) comme en cuisson douce.",
        "quote": "L'or vert est le secret de longévité le mieux gardé de la Méditerranée.",
        "h3_2": "Conclusion", "p_2": "Adopter une huile de qualité, c'est investir dans son bien-être à long terme tout en soutenant un artisanat authentique.",
        "footer": "Étude de Marché Huile d'Olive 2026. Analyse des tendances et opportunités premium.",
        "rights": "Tous droits réservés"
    },
    "en": {
        "index": "index-en.html", "home": "Home", "guides": "Guides", "pub": "Published", "min": "min read",
        "intro": "Olive oil is at the heart of the Mediterranean diet. This guide explores its many facets to help you better understand and integrate high-quality products into your daily life.",
        "h2_1": "Why should you care?", "p_1": "Rich in antioxidants and healthy fatty acids, it offers exceptional properties recognized by nutrition and health experts worldwide.",
        "h3_1": "Key points",
        "li_1_s": "Quality:", "li_1_t": "Always favor cold extraction to preserve all nutrients.",
        "li_2_s": "Storage:", "li_2_t": "Keep away from light and heat in a dark bottle.",
        "li_3_s": "Usage:", "li_3_t": "Ideal raw (in salads, on bread) or for gentle cooking.",
        "quote": "Green gold is the Mediterranean's best-kept longevity secret.",
        "h3_2": "Conclusion", "p_2": "Adopting a quality oil means investing in your long-term well-being while supporting authentic craftsmanship.",
        "footer": "Olive Oil Market Study 2026. Analysis of premium trends and opportunities.",
        "rights": "All rights reserved"
    },
    "it": {
        "index": "index-it.html", "home": "Home", "guides": "Guide", "pub": "Pubblicazione", "min": "min di lettura",
        "intro": "L'olio d'oliva è al centro della dieta mediterranea. Questa guida esplora le sue molteplici sfaccettature per aiutarti a comprenderlo meglio e a integrare prodotti di alta qualità nella tua vita quotidiana.",
        "h2_1": "Perché interessarsene?", "p_1": "Ricco di antiossidanti e acidi grassi sani, offre proprietà eccezionali riconosciute da esperti di nutrizione e salute in tutto il mondo.",
        "h3_1": "Punti chiave",
        "li_1_s": "Qualità:", "li_1_t": "Privilegiare sempre l'estrazione a freddo per conservare tutti i nutrienti.",
        "li_2_s": "Conservazione:", "li_2_t": "Da conservare al riparo dalla luce e dal calore in una bottiglia scura.",
        "li_3_s": "Uso:", "li_3_t": "Ideale a crudo (in insalata, sul pane) o per cotture delicate.",
        "quote": "L'oro verde è il segreto di longevità meglio custodito del Mediterraneo.",
        "h3_2": "Conclusione", "p_2": "Adottare un olio di qualità significa investire nel proprio benessere a lungo termine sostenendo al contempo un artigianato autentico.",
        "footer": "Studio di Mercato Olio d'Oliva 2026. Analisi delle tendenze e opportunità premium.",
        "rights": "Tutti i diritti riservati"
    },
    "el": {
        "index": "index-el.html", "home": "Αρχική", "guides": "Οδηγοί", "pub": "Δημοσίευση", "min": "λεπτά ανάγνωσης",
        "intro": "Το ελαιόλαδο βρίσκεται στην καρδιά της μεσογειακής διατροφής. Αυτός ο οδηγός εξερευνά τις πολλές πτυχές του για να σας βοηθήσει να το κατανοήσετε καλύτερα και να ενσωματώσετε προϊόντα υψηλής ποιότητας στην καθημερινότητά σας.",
        "h2_1": "Γιατί να ενδιαφερθείτε;", "p_1": "Πλούσιο σε αντιοξειδωτικά και υγιή λιπαρά οξέα, προσφέρει εξαιρετικές ιδιότητες αναγνωρισμένες από ειδικούς στη διατροφή και την υγεία παγκοσμίως.",
        "h3_1": "Βασικά σημεία",
        "li_1_s": "Ποιότητα:", "li_1_t": "Προτιμάτε πάντα την ψυχρή έκθλιψη για να διατηρηθούν όλα τα θρεπτικά συστατικά.",
        "li_2_s": "Συντήρηση:", "li_2_t": "Φυλάσσεται μακριά από το φως και τη ζέστη σε σκούρο μπουκάλι.",
        "li_3_s": "Χρήση:", "li_3_t": "Ιδανικό ωμό (σε σαλάτες, στο ψωμί) ή για ήπιο μαγείρεμα.",
        "quote": "Ο πράσινος χρυσός είναι το καλύτερα κρυμμένο μυστικό μακροζωίας της Μεσογείου.",
        "h3_2": "Συμπέρασμα", "p_2": "Η υιοθέτηση ενός ποιοτικού ελαίου σημαίνει επένδυση στη μακροπρόθεσμη ευεξία σας, υποστηρίζοντας παράλληλα την αυθεντική χειροτεχνία.",
        "footer": "Μελέτη Αγοράς Ελαιολάδου 2026. Ανάλυση των premium τάσεων και ευκαιριών.",
        "rights": "Με επιφύλαξη παντός δικαιώματος"
    }
}

urls_to_add = []
guides_dir = r"C:\Users\Antoine\etude-huile-olive\guides"

print("Génération de 1000 pages SEO en cours...")

count = 0
for pre in prefixes:
    for sub in subjects:
        for suf in suffixes:
            en_title = pre["en"] + sub["en"] + suf["en"]
            base_slug = slugify(en_title)
            
            slugs = {
                "fr": f"{base_slug}-fr.html",
                "en": f"{base_slug}-en.html",
                "it": f"{base_slug}-it.html",
                "el": f"{base_slug}-el.html"
            }
            
            titles = {
                "fr": pre["fr"] + sub["fr"] + suf["fr"],
                "en": en_title,
                "it": pre["it"] + sub["it"] + suf["it"],
                "el": pre["el"] + sub["el"] + suf["el"]
            }
            
            for lang in ["fr", "en", "it", "el"]:
                title = titles[lang]
                desc = translations[lang]["intro"]
                
                html = html_template.format(
                    lang=lang,
                    title=title,
                    desc=desc,
                    slug_fr=slugs["fr"],
                    slug_en=slugs["en"],
                    slug_it=slugs["it"],
                    slug_el=slugs["el"],
                    index_page=translations[lang]["index"],
                    active_fr="active" if lang == "fr" else "",
                    active_en="active" if lang == "en" else "",
                    active_it="active" if lang == "it" else "",
                    active_el="active" if lang == "el" else "",
                    home_label=translations[lang]["home"],
                    guides_label=translations[lang]["guides"],
                    subtitle=title,
                    published_label=translations[lang]["pub"],
                    min_read_label=translations[lang]["min"],
                    intro_text=translations[lang]["intro"],
                    h2_1=translations[lang]["h2_1"],
                    p_1=translations[lang]["p_1"],
                    h3_1=translations[lang]["h3_1"],
                    li_1_strong=translations[lang]["li_1_s"],
                    li_1_text=translations[lang]["li_1_t"],
                    li_2_strong=translations[lang]["li_2_s"],
                    li_2_text=translations[lang]["li_2_t"],
                    li_3_strong=translations[lang]["li_3_s"],
                    li_3_text=translations[lang]["li_3_t"],
                    quote_text=translations[lang]["quote"],
                    h3_2=translations[lang]["h3_2"],
                    p_2=translations[lang]["p_2"],
                    footer_text=translations[lang]["footer"],
                    rights_text=translations[lang]["rights"]
                )
                
                filepath = os.path.join(guides_dir, slugs[lang])
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(html)
                    
                urls_to_add.append(f"  <url><loc>https://huiledefes.com/guides/{slugs[lang]}</loc><priority>0.6</priority></url>\n")
                count += 1

print(f"{count} fichiers HTML ont été créés.")

# Update sitemap
print("Mise à jour du sitemap...")
sitemap_path = r"C:\Users\Antoine\etude-huile-olive\sitemap.xml"
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

insert_pos = sitemap_content.rfind("</urlset>")
if insert_pos != -1:
    new_sitemap = sitemap_content[:insert_pos] + "".join(urls_to_add) + sitemap_content[insert_pos:]
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(new_sitemap)
        
print("Sitemap mis à jour avec succès !")

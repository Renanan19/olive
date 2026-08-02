#!/usr/bin/env python3
"""
Genere une version COULEUR de la video de fond Atlas avec Veo (Google GenAI).

Jumeau de generate_atlas_video.py, qui reste la reference noir et blanc.
Celui-ci vise une lumiere claire et pastel, un ete d'autrefois : couleurs
delavees, noirs laiteux, halo chaud sur les hautes lumieres.

La cle API est demandee a chaque execution et n'est jamais ecrite sur le
disque, jamais affichee, jamais posee dans l'environnement persistant.

    pip install google-genai
    python generate_atlas_video_couleur.py

Sort dans assets/atlas-olive-couleur.mp4 — l'horizontale noir et blanc n'est
jamais ecrasee.

Options utiles :
    --look super8       parti pris : super8 | rohmer | carte-postale
    --prompt "..."      prompt libre, ignore --look
    --aspect 9:16       prise verticale, cadree pour le telephone
    --duration 8        secondes (selon le modele : 4, 6 ou 8)
    --takes 3           plusieurs prises, pour choisir
    --grade             cuire l'etalonnage pastel dans le fichier (ffmpeg)
    --list-models       afficher les modeles video disponibles pour ta cle
"""
import argparse
import getpass
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

ASSETS = Path(__file__).parent / "assets"
STEM = "atlas-olive-couleur"

# Trois etes, pas trois variantes du meme plan. On choisit avec --look.
#
# Aucun nom de cineaste n'apparait dans les prompts : Veo refuse frequemment
# les personnalites reelles nommees. On decrit la pellicule et la lumiere.
#
# Trois pieges appris a l'usage, corriges dans les trois prompts :
#
# 1. Nommer un support ("shot on Super 8", "looks like a postcard") fait
#    DESSINER l'objet : Veo a rendu une bande de film avec perforations, bord
#    noir et numeros de bobine, qui mangeait un tiers du cadre. On decrit donc
#    la texture ("the softness of 8mm footage") et on interdit l'objet
#    explicitement.
# 2. "static locked-off" + "no camera movement" a cote l'un de l'autre pousse
#    vers l'image quasi fixe. On separe : la camera ne bouge pas, l'arbre bouge.
#    Et le mouvement est annonce en premier, pas en incise.
# 3. "warm amber cast" ecrase tout le reste et vire au sepia. On borne :
#    chaleur dans les hautes lumieres seulement, et on interdit l'orange.
NO_FILM_OBJECT = (
    "The picture fills the entire frame edge to edge. No film strip, no sprocket "
    "holes, no film border or frame edges, no numbers, markings or timecode, no "
    "letterbox bars, no photo borders. No people, no text, no titles, no cuts."
)

SEA = (
    "Behind the tree the flat Mediterranean sea fills the whole background to the "
    "horizon, slightly out of focus, glittering softly in the summer light."
)

WIND = (
    "The canopy is in constant motion from the first frame to the last: a steady "
    "sea breeze gusts through it in waves, thousands of narrow leaves flipping "
    "over and shimmering, small branches swaying and springing back, a few leaves "
    "torn loose and drifting away. The camera is locked off and never moves; "
    "everything that moves is the tree."
)

# Le rayon qui perce entre les feuilles et frappe l'objectif. Le point qui compte
# est l'intermittence : le flare doit naitre et mourir avec le mouvement du
# feuillage, jamais rester allume. Reserve a super8 — sur rohmer (lumiere douce
# et claire) et carte-postale (midi voile) un flare marque jurerait. Une ligne
# suffit pour l'ajouter ailleurs.
SUN_THROUGH_LEAVES = (
    "The low sun sits directly behind the canopy. As the leaves move, a small "
    "hard sunbeam keeps breaking through the gaps straight into the lens: brief "
    "warm starbursts and soft round flare ghosts bloom across the frame, then "
    "vanish again as the leaves close over the sun. The flare is never constant, "
    "it appears and disappears with the swaying of the branches, sometimes for "
    "only a fraction of a second."
)

LOOKS = {
    # Film de famille : chaud, flottant, un peu abime.
    "super8": (
        "One ancient gnarled olive tree standing alone on a stone terrace above "
        "the sea in the south of France, late afternoon in high summer. " + SEA +
        " " + WIND + " " + SUN_THROUGH_LEAVES +
        " Colour is gently faded and pastel: dusty sage-green foliage, chalky "
        "white stone, pale washed blue sea and sky, and a soft warm cast in the "
        "brightest highlights only. Nothing orange, nothing sepia, nothing "
        "saturated. Soft milky blacks that never go truly dark, fine grain, a "
        "gentle bloom around the highlights, very slight flicker, with the "
        "softness of old 8mm home-movie footage. " + NO_FILM_OBJECT
    ),
    # Ete clair et net : pastel mais lumineux, pas abime.
    "rohmer": (
        "An ancient olive tree beside a low stone wall on a terrace overlooking "
        "the sea in the south of France, clear soft daylight, a calm summer "
        "afternoon. " + SEA + " " + WIND +
        " Delicate pastel palette, low saturation, soft natural contrast, airy "
        "and luminous: pale blue sky, dry silver-green foliage, warm pale stone, "
        "a few faded terracotta tones. Fine grain, clean and unhurried, no "
        "artificial colour, nothing orange or sepia. " + NO_FILM_OBJECT
    ),
    # Couleurs brulees par le soleil, comme une image restee trop longtemps a la lumiere.
    "carte-postale": (
        "An ancient olive tree on a sunlit Mediterranean hillside at midday, "
        "shimmering summer haze. " + SEA + " " + WIND +
        " The colour is sun-bleached and faded, as though the film itself had "
        "been left in the light for thirty years: cyan-shifted pale sky, "
        "washed-out greens, soft pink and ochre in the stone, highlights blown "
        "out to creamy white, blacks lifted and never truly dark. Heavy summer "
        "light, soft focus falloff towards the edges, fine grain, faint "
        "scratches. " + NO_FILM_OBJECT
    ),
}
DEFAULT_LOOK = "super8"

LOOK_ORDER = ["super8", "rohmer", "carte-postale"]
LOOK_DESC = {
    "super8": "film de famille, chaud et flottant, fuite de lumiere, halo",
    "rohmer": "ete clair et net, pastel lumineux, 35mm des annees 80",
    "carte-postale": "couleurs brulees par le soleil, ciel vire cyan, noirs laiteux",
}

PRICE_PER_SECOND = 0.10  # tarif Veo indicatif, sert a annoncer le cout avant de lancer

# Du meilleur au plus ancien : le script prend le premier accepte par la cle.
MODEL_CANDIDATES = [
    "veo-3.1-fast-generate-preview",
    "veo-3.1-generate-preview",
    "veo-3.0-fast-generate-001",
    "veo-3.0-generate-001",
    "veo-2.0-generate-001",
]


def ask(question: str, default) -> str:
    """Question avec valeur par defaut : entree vide = on garde le defaut."""
    return input(f"  {question} [{default}] : ").strip() or str(default)


def interactive(args) -> None:
    """Remplit args en dialogue. Utilise quand le script est lance sans option."""
    # Pas de tiret cadratin ni d'accent dans les sorties console : la console
    # Windows est en cp1252 et les rend en points d'interrogation.
    print("\n  ATLAS - video de fond, version couleur\n")
    print("  Regard :")
    for i, name in enumerate(LOOK_ORDER, 1):
        mark = "   <- recommande" if name == DEFAULT_LOOK else ""
        print(f"    {i}) {name:<15} {LOOK_DESC[name]}{mark}")
    print()

    while True:
        choice = ask("Numero", LOOK_ORDER.index(DEFAULT_LOOK) + 1)
        if choice.isdigit() and 1 <= int(choice) <= len(LOOK_ORDER):
            args.look = LOOK_ORDER[int(choice) - 1]
            break
        print("  -> 1, 2 ou 3.")

    while True:
        a = ask("Format (1 = paysage 16:9, 2 = portrait 9:16)", 1)
        if a in ("1", "2"):
            args.aspect = "16:9" if a == "1" else "9:16"
            break
        print("  -> 1 ou 2.")

    while True:
        d = ask("Duree en secondes (4, 6 ou 8)", args.duration)
        if d in ("4", "6", "8"):
            args.duration = int(d)
            break
        print("  -> Veo accepte 4, 6 ou 8.")

    while True:
        t = ask("Nombre de prises", args.takes)
        if t.isdigit() and 1 <= int(t) <= 4:
            args.takes = int(t)
            break
        print("  -> entre 1 et 4.")

    # Sans ffmpeg la question n'a pas de sens : l'etalonnage reste en CSS.
    if ffmpeg_bin():
        args.grade = ask("Cuire l'etalonnage pastel dans le fichier ? (o/n)",
                         "n").lower().startswith("o")

    cost = args.takes * args.duration * PRICE_PER_SECOND
    print(f"\n  {args.takes} prise(s) x {args.duration}s  -  cout estime ~{cost:.2f} $")
    if not ask("Lancer ? (o/n)", "o").lower().startswith("o"):
        sys.exit("  Annule.")
    print()


def ask_key() -> str:
    """Lit la cle sans echo. Jamais persistee."""
    key = getpass.getpass("Cle API Google GenAI (masquee, non sauvegardee) : ").strip()
    if not key:
        sys.exit("Aucune cle fournie.")
    return key


def make_client(key: str):
    try:
        from google import genai
    except ImportError:
        sys.exit("Module manquant. Installe-le :  pip install google-genai")
    return genai.Client(api_key=key)


def list_models(client) -> None:
    print("Modeles video disponibles pour cette cle :")
    found = False
    for m in client.models.list():
        actions = getattr(m, "supported_actions", None) or []
        if "generateVideos" in actions or "veo" in m.name.lower():
            print(f"  {m.name}")
            found = True
    if not found:
        print("  (aucun — Veo n'est peut-etre pas active sur ce projet)")


def generate(client, model: str, prompt: str, duration: int, takes: int,
             aspect: str = "16:9") -> list:
    """Lance la generation et attend l'operation longue duree."""
    from google.genai import types

    # person_generation n'est pas envoye : l'API rejette "dont_allow" (400).
    # Le prompt dit deja "no people", ce qui suffit.
    cfg = {
        "aspect_ratio": aspect,
        "number_of_videos": takes,
    }
    # duration_seconds n'existe pas sur tous les modeles : on degrade sans casser.
    try:
        config = types.GenerateVideosConfig(duration_seconds=duration, **cfg)
    except (TypeError, ValueError):
        config = types.GenerateVideosConfig(**cfg)

    print(f"Modele  : {model}")
    print(f"Prises  : {takes}")
    print("Generation lancee. Veo prend generalement 1 a 3 minutes.")

    op = client.models.generate_videos(model=model, prompt=prompt, config=config)

    waited = 0
    while not op.done:
        time.sleep(10)
        waited += 10
        print(f"  ... {waited}s", end="\r", flush=True)
        op = client.operations.get(op)
    print(f"  termine en {waited}s.        ")

    if getattr(op, "error", None):
        sys.exit(f"Veo a refuse la generation : {op.error}")

    videos = getattr(op.response, "generated_videos", None) or []
    if not videos:
        sys.exit("Veo n'a renvoye aucune video (filtrage de securite ou quota).")
    return videos


def download(client, videos: list, stem: str = STEM) -> list[Path]:
    """La 1re prise prend le nom de reference ; les autres sont suffixees
    -take2, -take3 (gitignorees, on n'en garde qu'une)."""
    ASSETS.mkdir(exist_ok=True)
    paths = []
    for i, gv in enumerate(videos):
        name = f"{stem}.mp4" if i == 0 else f"{stem}-take{i + 1}.mp4"
        dest = ASSETS / name
        client.files.download(file=gv.video)
        gv.video.save(str(dest))
        size = dest.stat().st_size / 1_000_000
        print(f"  {dest.relative_to(ASSETS.parent)}  ({size:.1f} Mo)")
        paths.append(dest)
    return paths


def ffmpeg_bin() -> str | None:
    return shutil.which("ffmpeg")


def grade(src: Path) -> None:
    """Cuit le pastel dans le fichier : noirs laiteux, couleurs delavees, grain.

    C'est l'inverse du jumeau noir et blanc, qui ecrase les noirs. Ici on les
    souleve : c'est ce qui fait la pellicule vieillie plutot que le numerique.
    """
    ff = ffmpeg_bin()
    if not ff:
        print("\nffmpeg introuvable — etalonnage saute.")
        print("La video brute reste utilisable ; l'etalonnage peut aussi se faire en CSS.")
        print("Pour le cuire :  winget install Gyan.FFmpeg")
        return

    vf = (
        "eq=saturation=0.76:contrast=0.94:brightness=0.03,"   # couleurs delavees
        "curves=all='0/0.07 0.5/0.53 1/0.95',"                # noirs souleves, blancs retenus
        "colorbalance=rs=0.05:gs=0.01:bs=-0.06:rm=0.03:bm=-0.03,"  # derive chaude
        "noise=alls=8:allf=t+u,"                              # grain argentique
        "vignette=PI/5"                                       # leger, pas theatral
    )
    cmd = [ff, "-y", "-i", str(src), "-an", "-vf", vf,
           "-c:v", "libx264", "-crf", "23", "-pix_fmt", "yuv420p",
           str(src.with_name(src.stem + "-graded.mp4"))]
    print("\nEtalonnage pastel...")
    if subprocess.run(cmd, capture_output=True).returncode != 0:
        print("ffmpeg a echoue — la source brute reste utilisable.")
        return
    src.with_name(src.stem + "-graded.mp4").replace(src)
    print(f"  {src.name} etalonne (piste audio retiree).")

    poster = src.with_name(f"{src.stem}-poster.jpg")
    subprocess.run([ff, "-y", "-i", str(src), "-vframes", "1", "-q:v", "3", str(poster)],
                   capture_output=True)
    if poster.exists():
        print(f"  {poster.name} genere.")


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Genere la version couleur de la video de fond Atlas via Veo.")
    ap.add_argument("--look", choices=sorted(LOOKS), default=DEFAULT_LOOK,
                    help="parti pris visuel (defaut : %(default)s)")
    ap.add_argument("--prompt", default=None, help="prompt libre, ignore --look")
    ap.add_argument("--model", default=None, help="force un modele Veo precis")
    ap.add_argument("--duration", type=int, default=8)
    ap.add_argument("--takes", type=int, default=1, help="nombre de prises")
    ap.add_argument("--aspect", choices=["16:9", "9:16"], default="16:9",
                    help="9:16 produit une prise verticale, cadree pour le telephone")
    ap.add_argument("--grade", action="store_true",
                    help="cuire l'etalonnage pastel via ffmpeg")
    ap.add_argument("--list-models", action="store_true")
    args = ap.parse_args()

    # Lance sans aucune option : on demande plutot que d'exiger des flags.
    if len(sys.argv) == 1:
        interactive(args)

    prompt = args.prompt or LOOKS[args.look]
    if not args.prompt:
        print(f"Regard  : {args.look}")

    key = ask_key()
    client = make_client(key)
    del key  # plus besoin : la cle ne vit que dans le client, en memoire

    if args.list_models:
        list_models(client)
        return

    models = [args.model] if args.model else MODEL_CANDIDATES
    last_err = None
    for model in models:
        try:
            videos = generate(client, model, prompt, args.duration, args.takes,
                              args.aspect)
            break
        except Exception as exc:
            msg = " ".join(str(exc).split())
            # Seul un 404 signifie "ce modele n'existe pas pour cette cle" et
            # justifie d'essayer le suivant. Sur toute autre erreur (400 config,
            # 429 quota, 403 droits), reessayer d'autres modeles ne fait que
            # repeter le meme echec en masquant la cause.
            if "NOT_FOUND" not in msg and "404" not in msg:
                sys.exit(f"\n{model} a refuse la requete :\n  {msg}\n\n"
                         f"Erreur de configuration ou de quota, pas de modele — "
                         f"changer de modele n'y changerait rien.")
            last_err = exc
            print(f"  {model} indisponible : {msg[:160]}")
    else:
        sys.exit(f"Aucun modele Veo utilisable. Derniere erreur : {last_err}\n"
                 f"Lance --list-models pour voir ce que ta cle autorise.")

    print("\nTelechargement :")
    stem = f"{STEM}-vertical" if args.aspect == "9:16" else STEM
    paths = download(client, videos, stem)

    if args.grade:
        grade(paths[0])

    print(f"\nLa version noir et blanc reste dans assets/atlas-olive.mp4,")
    print(f"celle-ci est a part. Pour la mettre sur la landing, il faut retirer")
    print(f"le grayscale(1) du CSS d'index.html — dis-le moi et je le fais.")
    if args.takes > 1:
        print(f"Plusieurs prises : renomme celle que tu preferes en {stem}.mp4")


if __name__ == "__main__":
    # Ceinture et bretelles : aucune cle heritee de l'environnement n'est utilisee,
    # et rien n'y est ecrit.
    for var in ("GOOGLE_API_KEY", "GEMINI_API_KEY"):
        os.environ.pop(var, None)
    main()

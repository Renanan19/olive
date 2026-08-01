#!/usr/bin/env python3
"""
Genere la video de fond de la landing Atlas avec Veo (Google GenAI).

La cle API est demandee a chaque execution et n'est jamais ecrite sur le disque,
jamais affichee, jamais posee dans l'environnement persistant.

    pip install google-genai
    python generate_atlas_video.py

Options utiles :
    --look pagnol       parti pris visuel : pagnol | melville | plein-soleil
    --prompt "..."      prompt libre, ignore --look
    --model veo-3.1-generate-preview
    --duration 8        secondes (selon le modele : 4, 6 ou 8)
    --takes 3           generer plusieurs prises et choisir la meilleure
    --grade             cuire le N&B / grain VHS dans le fichier (necessite ffmpeg)
    --list-models       afficher les modeles video disponibles pour ta cle

Sans --grade, la video reste en couleur : c'est voulu. L'etalonnage Sin City est
applique en CSS dans index.html, ce qui laisse la source intacte et reglable.
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

# Trois regards, pas trois variantes du meme plan. On choisit avec --look.
#
# Aucun nom de cineaste ou d'acteur n'apparait dans les prompts : Veo refuse
# frequemment les personnalites reelles nommees, et il n'y a personne dans le
# cadre. On decrit la lumiere et le cadre, pas la reference.
LOOKS = {
    # Provence de l'arriere-pays : chaleur, pierre seche, mistral.
    "pagnol": (
        "Static locked-off cinematic wide shot of one ancient olive tree alone on "
        "a dry stony hillside in the south of France, high summer. Massive gnarled "
        "trunk, hollowed and split by centuries, twisting out of pale ochre stones "
        "beside a low dry-stone wall. Broad low canopy. A hot dry wind gusts "
        "through the crown in waves: thousands of narrow leaves flip over and flash "
        "their pale silver undersides, branches swaying slowly, a few leaves torn "
        "loose and carried off. Low sun directly behind the canopy, long hard "
        "shadows raking across the stones, heat haze shimmering above the ground. "
        "Thyme and rosemary scrub at the base. Shot on 35mm anamorphic black and "
        "white film, Ilford HP5 grain, very high contrast, crushed deep blacks, "
        "blown highlights on the leaves, slight gate weave and breathing. "
        "No people, no animals, no text, no titles, no camera movement, no cuts."
    ),
    # Monochrome froid et graphique : peu de gris, composition severe.
    "melville": (
        "Static locked-off cinematic shot of a single ancient olive tree, stark and "
        "solitary against a near-black sky. Severe, graphic, almost abstract "
        "composition, the tree centred and isolated. One hard key light from behind "
        "and slightly to the side rims the canopy; the trunk stays a solid black "
        "silhouette with no detail. A steady cold wind moves the crown, the leaves "
        "catching the light as sharp silver specular flecks that flicker in and out. "
        "Minimal midtones, only deep black and hard white. Shot on 35mm black and "
        "white film, fine grain, extreme contrast, still and austere. "
        "No people, no text, no titles, no camera movement, no cuts."
    ),
    # Mediterranee eclatante : lumiere de mer, surexposition franche.
    "plein-soleil": (
        "Static locked-off cinematic shot of an ancient olive tree on a Mediterranean "
        "terrace, blinding midday sun, the flat sea shimmering far below and out of "
        "focus. Blown-out white sky. The wind comes off the water in long gusts and "
        "runs through the canopy: leaves turning over in waves, flaring silver-white "
        "where the light hits them, dappled light moving across the gnarled trunk. "
        "Shot on 35mm black and white film, high contrast, deliberately overexposed "
        "highlights, deep shadows, visible grain, faint lens flare. "
        "No people, no boats, no text, no titles, no camera movement, no cuts."
    ),
}
DEFAULT_LOOK = "pagnol"

# Du meilleur au plus ancien : le script prend le premier accepte par la cle.
# Les noms exacts varient selon le palier de la cle — d'ou la cascade, et
# --list-models quand tout echoue.
MODEL_CANDIDATES = [
    "veo-3.1-fast-generate-preview",
    "veo-3.1-generate-preview",
    "veo-3.0-fast-generate-001",
    "veo-3.0-generate-001",
    "veo-2.0-generate-001",
]


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


def generate(client, model: str, prompt: str, duration: int, takes: int) -> list:
    """Lance la generation et attend l'operation longue duree."""
    from google.genai import types

    # person_generation n'est pas envoye : l'API rejette "dont_allow" (400).
    # Le prompt dit deja "no people", ce qui suffit.
    cfg = {
        "aspect_ratio": "16:9",
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


def download(client, videos: list) -> list[Path]:
    ASSETS.mkdir(exist_ok=True)
    paths = []
    for i, gv in enumerate(videos):
        name = "atlas-olive.mp4" if i == 0 else f"atlas-olive-take{i + 1}.mp4"
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
    """Cuit le look Sin City dans le fichier : N&B dur, grain, vignette, muet."""
    ff = ffmpeg_bin()
    if not ff:
        print("\nffmpeg introuvable — etalonnage saute.")
        print("Sans importance : index.html applique deja le N&B VHS en CSS.")
        print("Pour le cuire quand meme :  winget install Gyan.FFmpeg")
        return

    graded = src.with_name(src.stem + "-graded.mp4")
    vf = (
        "hue=s=0,"                                  # desature
        "eq=contrast=1.9:brightness=-0.14:gamma=0.86,"  # noirs ecrases, blancs qui percent
        "curves=all='0/0 0.3/0.14 0.7/0.86 1/1',"   # courbe en S facon tirage argentique
        "noise=alls=14:allf=t+u,"                   # grain temporel
        "vignette=PI/4"
    )
    cmd = [ff, "-y", "-i", str(src), "-an", "-vf", vf,
           "-c:v", "libx264", "-crf", "23", "-pix_fmt", "yuv420p", str(graded)]
    print("\nEtalonnage ffmpeg...")
    if subprocess.run(cmd, capture_output=True).returncode != 0:
        print("ffmpeg a echoue — la source brute reste utilisable.")
        return
    graded.replace(src)
    print(f"  {src.name} etalonne (piste audio retiree).")

    # WebM : plus leger, sert de premiere source dans index.html
    webm = src.with_suffix(".webm")
    subprocess.run(
        [ff, "-y", "-i", str(src), "-an", "-c:v", "libvpx-vp9",
         "-crf", "34", "-b:v", "0", str(webm)],
        capture_output=True,
    )
    if webm.exists():
        print(f"  {webm.name} genere.")

    # Poster : premiere image, affichee avant le demarrage de la lecture
    poster = src.with_name("atlas-olive-poster.jpg")
    subprocess.run(
        [ff, "-y", "-i", str(src), "-vframes", "1", "-q:v", "3", str(poster)],
        capture_output=True,
    )
    if poster.exists():
        print(f"  {poster.name} genere.")


def main() -> None:
    ap = argparse.ArgumentParser(description="Genere la video de fond Atlas via Veo.")
    ap.add_argument("--look", choices=sorted(LOOKS), default=DEFAULT_LOOK,
                    help="parti pris visuel (defaut : %(default)s)")
    ap.add_argument("--prompt", default=None, help="prompt libre, ignore --look")
    ap.add_argument("--model", default=None, help="force un modele Veo precis")
    ap.add_argument("--duration", type=int, default=8)
    ap.add_argument("--takes", type=int, default=1, help="nombre de prises")
    ap.add_argument("--grade", action="store_true", help="cuire le N&B via ffmpeg")
    ap.add_argument("--list-models", action="store_true")
    args = ap.parse_args()

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
            videos = generate(client, model, prompt, args.duration, args.takes)
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
    paths = download(client, videos)

    if args.grade:
        grade(paths[0])

    print("\nDerniere etape : dans index.html, dé-commente le bloc <video>.")
    print("Si tu as genere plusieurs prises, renomme celle que tu preferes")
    print("en assets/atlas-olive.mp4.")


if __name__ == "__main__":
    # Ceinture et bretelles : aucune cle heritee de l'environnement n'est utilisee,
    # et rien n'y est ecrit.
    for var in ("GOOGLE_API_KEY", "GEMINI_API_KEY"):
        os.environ.pop(var, None)
    main()

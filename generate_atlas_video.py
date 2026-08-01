#!/usr/bin/env python3
"""
Genere la video de fond de la landing Atlas avec Veo (Google GenAI).

La cle API est demandee a chaque execution et n'est jamais ecrite sur le disque,
jamais affichee, jamais posee dans l'environnement persistant.

    pip install google-genai
    python generate_atlas_video.py

Options utiles :
    --prompt "..."      remplacer le prompt (le defaut vise l'olivier au vent)
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

DEFAULT_PROMPT = (
    "Static locked-off cinematic shot of a single ancient gnarled olive tree "
    "alone on a bare Mediterranean hillside. Strong steady wind moves through "
    "the canopy: thousands of narrow silver-backed leaves flip and shimmer, "
    "branches sway slowly. Shot on 16mm black and white film, very high "
    "contrast, crushed deep blacks, blown highlights on the leaves, heavy grain, "
    "slight gate weave. Backlit against an overcast blank sky. No people, "
    "no text, no camera movement, no cuts."
)

# Du plus recent au plus ancien : le script prend le premier accepte par la cle.
MODEL_CANDIDATES = [
    "veo-3.1-generate-preview",
    "veo-3.0-generate-001",
    "veo-3.0-fast-generate-001",
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

    cfg = {
        "aspect_ratio": "16:9",
        "number_of_videos": takes,
        "person_generation": "dont_allow",
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
    ap.add_argument("--prompt", default=DEFAULT_PROMPT)
    ap.add_argument("--model", default=None, help="force un modele Veo precis")
    ap.add_argument("--duration", type=int, default=8)
    ap.add_argument("--takes", type=int, default=1, help="nombre de prises")
    ap.add_argument("--grade", action="store_true", help="cuire le N&B via ffmpeg")
    ap.add_argument("--list-models", action="store_true")
    args = ap.parse_args()

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
            videos = generate(client, model, args.prompt, args.duration, args.takes)
            break
        except Exception as exc:  # modele indisponible sur cette cle : on essaie le suivant
            last_err = exc
            print(f"  {model} indisponible ({type(exc).__name__}).")
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

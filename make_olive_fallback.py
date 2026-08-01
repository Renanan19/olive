#!/usr/bin/env python3
"""
Genere assets/atlas-olive-fallback.svg : la silhouette d'olivier au vent qui sert
de fond a la landing Atlas tant que la video Veo n'est pas en place.

Deterministe (graine fixe) : re-executer donne exactement le meme arbre.

    python make_olive_fallback.py
"""
import math
import random
from pathlib import Path

OUT = Path(__file__).parent / "assets" / "atlas-olive-fallback.svg"

W, H = 1200, 900
GROUND = 858
ROOT_X = 600

# Le vent souffle vers la gauche : il incline l'arbre et couche les feuilles.
WIND = -0.16          # inclinaison generale des branches (radians)
LEAF_ANGLE = -28      # orientation dominante des feuilles (degres)

rng = random.Random(20260801)
wood: list[str] = []
tips: list[tuple[float, float, int]] = []


def branch(x, y, angle, length, width, depth):
    """Branche courbee, dessinee comme un ruban qui s'affine, puis subdivisee.

    Le bois d'olivier ne pousse jamais droit : la courbure (bend) est forte et
    signee au hasard, ce qui donne le noueux caracteristique.
    """
    if depth == 0 or length < 11:
        tips.append((x, y, depth))
        return

    bend = rng.uniform(-0.40, 0.40) + WIND * 0.4
    a_mid, a_end = angle + bend * 0.5, angle + bend
    mx, my = x + math.sin(a_mid) * length * .5, y - math.cos(a_mid) * length * .5
    ex, ey = x + math.sin(a_end) * length, y - math.cos(a_end) * length

    w0, w1 = width, width * .62
    n = a_end + math.pi / 2
    wood.append(
        f'<path d="M{x + math.sin(n) * w0:.0f},{y - math.cos(n) * w0:.0f}'
        f' Q{mx + math.sin(n) * w0 * .8:.0f},{my - math.cos(n) * w0 * .8:.0f}'
        f' {ex + math.sin(n) * w1:.0f},{ey - math.cos(n) * w1:.0f}'
        f' L{ex - math.sin(n) * w1:.0f},{ey + math.cos(n) * w1:.0f}'
        f' Q{mx - math.sin(n) * w0 * .8:.0f},{my + math.cos(n) * w0 * .8:.0f}'
        f' {x - math.sin(n) * w0:.0f},{y + math.cos(n) * w0:.0f} Z"/>'
    )

    kids = 3 if depth >= 4 else 2
    for i in range(kids):
        spread = rng.uniform(0.30, 0.78)
        side = 1 if i % 2 == 0 else -1
        na = a_end + side * spread + rng.uniform(-0.18, 0.18) + WIND * 0.3
        branch(ex, ey, na, length * rng.uniform(0.62, 0.76), width * .60, depth - 1)


# Tronc : une masse evasee unique. Les contreforts convergent vers la couronne,
# sinon ils se lisent comme des pieux separes plantes dans le sol.
CROWN_Y = GROUND - 168
wood.append(
    f'<path d="M{ROOT_X - 104},{GROUND}'
    f' C{ROOT_X - 86},{GROUND - 60} {ROOT_X - 54},{GROUND - 110} {ROOT_X - 34},{CROWN_Y}'
    f' L{ROOT_X + 32},{CROWN_Y}'
    f' C{ROOT_X + 56},{GROUND - 112} {ROOT_X + 88},{GROUND - 58} {ROOT_X + 108},{GROUND} Z"/>'
)
# Deux racines saillantes : elles cassent la symetrie du pied
wood.append(
    f'<path d="M{ROOT_X - 150},{GROUND} Q{ROOT_X - 118},{GROUND - 26}'
    f' {ROOT_X - 62},{GROUND - 40} L{ROOT_X - 52},{GROUND} Z"/>'
)
wood.append(
    f'<path d="M{ROOT_X + 146},{GROUND} Q{ROOT_X + 112},{GROUND - 22}'
    f' {ROOT_X + 58},{GROUND - 34} L{ROOT_X + 48},{GROUND} Z"/>'
)

# Charpentieres : plusieurs departs a la meme hauteur, tres ouverts.
# C'est cette divergence basse qui distingue l'olivier d'un arbre a fleche unique.
for a in (-0.86, -0.50, -0.16, 0.18, 0.54, 0.88):
    branch(ROOT_X + a * 26, CROWN_Y, a * 0.82 + WIND, rng.uniform(118, 152), 24, 5)

# Feuillage : lentilles etroites couchees par le vent. Densite variable pour que
# le ciel perce entre les touffes — sans trous, la couronne devient une masse noire.
leaves: list[str] = []
for tx, ty, depth in tips:
    spread = rng.uniform(30, 58)
    for _ in range(rng.randint(8, 15)):
        a = rng.uniform(0, math.tau)
        r = spread * math.sqrt(rng.random())
        lx, ly = tx + math.cos(a) * r, ty + math.sin(a) * r * .78
        rot = LEAF_ANGLE + rng.uniform(-42, 42)
        rx, ry = rng.uniform(7, 14), rng.uniform(1.7, 3.2)
        leaves.append(
            f'<ellipse cx="{lx:.0f}" cy="{ly:.0f}" rx="{rx:.1f}" ry="{ry:.1f}"'
            f' transform="rotate({rot:.0f} {lx:.0f} {ly:.0f})"/>'
        )

# Colline : assoit l'arbre au lieu de le laisser flotter
ground = (f'<path d="M0,{H} L0,{GROUND + 18}'
          f' Q300,{GROUND - 20} 600,{GROUND - 6}'
          f' Q900,{GROUND + 10} 1200,{GROUND - 26} L{W},{H} Z"/>')

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
       f'width="{W}" height="{H}">\n<g fill="#000">\n'
       f'{ground}\n' + "\n".join(wood) + "\n" + "\n".join(leaves) +
       '\n</g>\n</svg>\n')

OUT.parent.mkdir(exist_ok=True)
OUT.write_text(svg, encoding="utf-8")
print(f"{OUT.name} : {len(wood)} branches, {len(leaves)} feuilles, "
      f"{OUT.stat().st_size // 1024} Ko")

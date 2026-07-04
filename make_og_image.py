# -*- coding: utf-8 -*-
"""Generate assets/og-default.png (1200x630) — branded social/AI preview card."""

import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "assets", "og-default.png")
W, H = 1200, 630

PINE = (46, 74, 64)
PINE2 = (36, 58, 50)
PEACH = (242, 216, 196)
CREAM = (245, 235, 221)
AVOCADO = (95, 143, 106)
TERRA = (199, 92, 51)


def font(names, size):
    for n in names:
        for p in (n, os.path.join("C:\\Windows\\Fonts", n)):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()


def main():
    img = Image.new("RGB", (W, H), PINE)
    d = ImageDraw.Draw(img)

    # vertical gradient
    for y in range(H):
        t = y / H
        d.line([(0, y), (W, y)],
               fill=tuple(int(PINE[i] + (PINE2[i] - PINE[i]) * t) for i in range(3)))

    # thin terracotta frame
    d.rectangle([28, 28, W - 28, H - 28], outline=TERRA, width=3)

    # olive-drop mark (teardrop): triangle tip + circle bulb, peach fill
    cx, cy, r = 165, 250, 62
    d.ellipse([cx - r, cy - r + 18, cx + r, cy + r + 18], fill=PEACH)
    d.polygon([(cx, cy - 92), (cx - r + 6, cy + 6), (cx + r - 6, cy + 6)], fill=PEACH)
    # leaf highlight
    d.ellipse([cx - 22, cy - 8, cx + 6, cy + 42], fill=PINE2)

    serif_b = font(["georgiab.ttf", "timesbd.ttf"], 128)
    serif = font(["georgia.ttf", "times.ttf"], 46)
    mono = font(["consola.ttf", "cour.ttf"], 30)

    d.text((250, 150), "L'OR VERT", font=serif_b, fill=PEACH)

    # divider
    d.line([(255, 300), (255 + 470, 300)], fill=AVOCADO, width=4)

    d.text((255, 322), "Huile d'Olive Extra Vierge", font=serif, fill=CREAM)
    d.text((255, 380), "Guide · Études de marché · Recettes", font=serif, fill=CREAM)

    d.text((255, 500), "huiledefes.com", font=mono, fill=PEACH)
    d.text((255, 540), "Bienfaits · Qualité · Cuisine méditerranéenne", font=mono, fill=AVOCADO)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    img.save(OUT, "PNG", optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()

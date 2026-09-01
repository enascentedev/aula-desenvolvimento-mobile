"""
Converte os SVGs monocromaticos do simple-icons em PNGs coloridos
com a cor oficial de cada marca, prontos para entrar no PPTX.
"""
import os
import re
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

# Cores oficiais de marca
CORES = {
    "kotlin": "7F52FF",
    "javascript": "F7DF1E",
    "react": "61DAFB",
    "android": "3DDC84",
    "swift": "F05138",
    "flutter": "02569B",
}

TAM = 512  # PNG grande, o PowerPoint reduz sem serrilhar


def colorir(svg_path, cor, saida_svg):
    with open(svg_path, encoding="utf-8") as f:
        s = f.read()

    # simple-icons vem com <path d="..."/> sem fill; injeta a cor da marca
    if "fill=" not in s.split(">")[0]:
        s = s.replace("<svg ", f'<svg fill="#{cor}" ', 1)
    s = re.sub(r'fill="(currentColor|#000|#000000|black)"', f'fill="#{cor}"', s)

    with open(saida_svg, "w", encoding="utf-8") as f:
        f.write(s)


def main():
    base = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(base, "icones")
    out = os.path.join(base, "icones-png")
    os.makedirs(out, exist_ok=True)

    for nome, cor in CORES.items():
        svg = os.path.join(src, f"{nome}.svg")
        if not os.path.exists(svg):
            print(f"faltando: {nome}")
            continue

        tmp = os.path.join(src, f"{nome}-cor.svg")
        colorir(svg, cor, tmp)

        drawing = svg2rlg(tmp)
        escala = TAM / max(drawing.width, drawing.height)
        drawing.width *= escala
        drawing.height *= escala
        drawing.scale(escala, escala)

        png = os.path.join(out, f"{nome}.png")
        renderPM.drawToFile(drawing, png, fmt="PNG", bg=0xFFFFFF, configPIL={"transparent": None})
        print(f"OK  {nome:12s} #{cor}  -> {os.path.basename(png)}")


if __name__ == "__main__":
    main()

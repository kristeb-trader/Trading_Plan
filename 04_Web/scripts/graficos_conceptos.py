# -*- coding: utf-8 -*-
"""
graficos_conceptos.py — dibuja los gráficos que explican la estrategia.

Los 21 casos de la galería enseñan operaciones concretas. Faltaban gráficos
que expliquen los CONCEPTOS: qué es una corrida, de dónde sale una zona, la
diferencia entre romper y confirmar, y las dos formas de entrar.

Se dibujan sobre DATOS REALES usando el mismo motor de 05_Backtesting, para
que no sean dibujos inventados sino mercado de verdad.

NO MODIFICA NADA de 05_Backtesting: solo importa su motor.
NO ESCRIBE en 01_Plan ni en 02_Assets.

Uso:  python scripts/graficos_conceptos.py
Salida: public/conceptos/*.png
"""
import os
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

AQUI = os.path.dirname(os.path.abspath(__file__))
WEB = os.path.dirname(AQUI)
RAIZ = os.path.dirname(WEB)
BACKTEST = os.path.join(RAIZ, "05_Backtesting")
DATOS = os.path.join(BACKTEST, "datos", "NQ 09-26.Last.txt")
SALIDA = os.path.join(WEB, "public", "conceptos")

sys.path.insert(0, BACKTEST)
import motor  # noqa: E402  (el motor del operador, sin tocar)

# ── estándar visual del operador, al pie de la letra ────────────────────
FONDO = "#0B0E14"
ALCISTA = "#2E86FF"   # azul
BAJISTA = "#FFFFFF"   # blanca
ZONA = "#8B93A7"      # todas las zonas del mismo gris
EJE = "#3A4256"
TXT = "#F2F5F9"
TENUE = "#A8B0BF"
ORO = "#F5C542"
ROJO = "#FF5C5C"
VERDE = "#4ADE80"

plt.rcParams["font.family"] = ["DejaVu Sans"]


def ventana_sesion(V, dia):
    """Índices de la ventana operativa. El ancla es la apertura americana:
       13:30-15:30 UTC en horario de verano de Nueva York."""
    idx = [i for i, k in enumerate(V) if k["d"] == dia and 1330 <= int(k["t"][:4]) <= 1530]
    return (idx[0], idx[-1] + 1) if idx else (None, None)


def hora(k):
    return "%02d:%s" % ((int(k["t"][:2]) - 5) % 24, k["t"][2:4])


def dibujar(V, i0, i1, titulo, explicacion, salida,
            zonas=None, zigzag=None, tramos=None, marcas=None,
            operacion=None, franja=None):
    """Un lienzo con el estándar del operador. Sin cuadrícula, sin adornos.

    `tramos` son los rótulos importantes: en vez de una flecha a una vela,
    una llave debajo de un tramo entero. Un concepto como «corrida» es un
    tramo, no un punto, y señalarlo con flecha confunde más que aclara.
    """
    n = i1 - i0
    fig, ax = plt.subplots(figsize=(16, 8))
    fig.patch.set_facecolor(FONDO)
    ax.set_facecolor(FONDO)
    fig.subplots_adjust(top=0.83, bottom=0.14, left=0.06, right=0.97)

    lo = min(V[i]["l"] for i in range(i0, i1))
    hi = max(V[i]["h"] for i in range(i0, i1))
    rango = hi - lo
    # Aire abajo para las llaves de los tramos, y arriba para las notas.
    ax.set_ylim(lo - rango * (0.26 if tramos else 0.10), hi + rango * 0.16)
    ax.set_xlim(-1, n + 1)

    if franja:
        a, b, color, etiqueta = franja
        ax.axvspan(a - i0, b - i0, color=color, alpha=0.08, zorder=0)
        ax.text((a + b) / 2 - i0, hi + rango * 0.09, etiqueta, color=color,
                fontsize=13, ha="center", weight="bold")

    for z in (zonas or []):
        x = max(z["vela"] - i0, 0)
        ax.add_patch(Rectangle((x, z["lo"]), n - x + 1, max(z["hi"] - z["lo"], 0.25),
                               facecolor=ZONA, alpha=0.26, edgecolor=ZONA,
                               lw=1.4, zorder=1))

    for i in range(i0, i1):
        k = V[i]
        x = i - i0
        c = ALCISTA if k["c"] >= k["o"] else BAJISTA
        ax.plot([x, x], [k["l"], k["h"]], color=c, lw=1.1, zorder=3)
        alto = abs(k["c"] - k["o"]) or rango * 0.002
        ax.add_patch(Rectangle((x - 0.34, min(k["o"], k["c"])), 0.68, alto,
                               facecolor=c, edgecolor=c, lw=0.6, zorder=4))

    if zigzag:
        ax.plot([p[0] - i0 for p in zigzag], [p[1] for p in zigzag],
                color="#FFFFFF", lw=1.6, alpha=0.8, zorder=5)

    # llaves de tramo, debajo del precio
    base = lo - rango * 0.13
    for t in (tramos or []):
        a, b, etiqueta, color = t
        xa, xb = a - i0, b - i0
        ax.plot([xa, xb], [base, base], color=color, lw=2.4, solid_capstyle="butt", zorder=6)
        for x in (xa, xb):
            ax.plot([x, x], [base, base + rango * 0.022], color=color, lw=2.4, zorder=6)
        ax.text((xa + xb) / 2, base - rango * 0.055, etiqueta, color=color,
                fontsize=14, ha="center", va="top", weight="bold", zorder=7)

    if operacion:
        xe, entrada, stop, objetivo = operacion
        x = xe - i0
        ax.add_patch(Rectangle((x, min(entrada, stop)), n - x + 1,
                               abs(stop - entrada), facecolor=ROJO, alpha=0.14, zorder=2))
        ax.add_patch(Rectangle((x, min(entrada, objetivo)), n - x + 1,
                               abs(objetivo - entrada), facecolor=VERDE, alpha=0.14, zorder=2))

    for mk in (marcas or []):
        i, precio, texto, color, dy = mk
        x = i - i0
        izq = x < n * 0.62
        ax.annotate(texto, xy=(x, precio),
                    xytext=(x + (3.2 if izq else -3.2), precio + dy * rango),
                    color=color, fontsize=13.5, weight="bold",
                    ha="left" if izq else "right", va="center",
                    arrowprops=dict(arrowstyle="->", color=color, lw=1.7, alpha=0.95),
                    zorder=8)

    ax.tick_params(colors=TENUE, labelsize=10)
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)
    for lado in ("bottom", "left"):
        ax.spines[lado].set_color(EJE)
    paso = max(n // 9, 1)
    ax.set_xticks(range(0, n, paso))
    ax.set_xticklabels([hora(V[i0 + i]) for i in range(0, n, paso)])
    ax.grid(False)

    fig.text(0.06, 0.945, titulo, color=TXT, fontsize=23, weight="bold", va="top")
    fig.text(0.06, 0.878, explicacion, color=TENUE, fontsize=14, va="top")

    fig.savefig(salida, dpi=110, facecolor=FONDO)
    plt.close(fig)
    print("  " + os.path.basename(salida))


def zigzag_de(V, zonas, i0, i1):
    puntos = []
    for z in sorted(zonas, key=lambda z: z["vela"]):
        if i0 <= z["vela"] < i1:
            puntos.append((z["vela"], V[z["vela"]]["h"] if z["tipo"] == "R" else V[z["vela"]]["l"]))
    return puntos


def main():
    if not os.path.exists(DATOS):
        print("No encuentro los datos de mercado en " + DATOS)
        return 1
    os.makedirs(SALIDA, exist_ok=True)
    V = motor.cargar(DATOS)
    print("velas cargadas:", len(V))

    DIA = "20260713"
    i0, i1 = ventana_sesion(V, DIA)
    if i0 is None:
        print("No hay datos para " + DIA)
        return 1

    zonas = motor.estructura(V, i0, i1)
    zz = zigzag_de(V, zonas, i0, i1)
    print("ventana:", i1 - i0, "velas ·", len(zonas), "zonas")

    # ── 1 · la ventana operativa ────────────────────────────────────────
    dia_idx = [i for i, k in enumerate(V) if k["d"] == DIA]
    a, b = max(dia_idx[0], i0 - 150), min(dia_idx[-1] + 1, i1 + 80)
    dibujar(V, a, b,
            "Solo se opera en las dos primeras horas",
            "Fuera de esa ventana no se coloca ninguna orden. El resto del día no cuenta.",
            os.path.join(SALIDA, "01-ventana.png"),
            franja=(i0, i1, ORO, "VENTANA OPERATIVA"))

    # ── 2 · corrida y retroceso, como TRAMOS ────────────────────────────
    # Se busca una subida larga y limpia para que el concepto se vea solo.
    alcistas = [z for z in zonas if z["tipo"] == "R" and z["c1"] - z["c0"] >= 4]
    z = max(alcistas, key=lambda z: V[z["vela"]]["h"] - V[z["c0"]]["l"]) if alcistas else None
    if z:
        fin_retro = min(z["c1"] + 4, i1 - 1)
        a, b = max(z["c0"] - 4, i0), min(fin_retro + 5, i1)
        dibujar(V, a, b,
                "El precio avanza y descansa",
                "Al tramo que avanza se le llama corrida. Al descanso que viene después, retroceso.",
                os.path.join(SALIDA, "02-corrida-retroceso.png"),
                tramos=[(z["c0"], z["vela"], "CORRIDA", ALCISTA),
                        (z["vela"], fin_retro, "RETROCESO", ORO)])

        # ── 3 · de dónde sale una zona ──────────────────────────────────
        dibujar(V, a, b,
                "Cada tramo deja un rastro",
                "La vela del extremo deja una franja gris. Ese rastro es lo que se opera después.",
                os.path.join(SALIDA, "03-zona.png"),
                zonas=[z],
                tramos=[(z["c0"], z["vela"], "CORRIDA", ALCISTA)],
                marcas=[(z["vela"], (z["lo"] + z["hi"]) / 2,
                         "La zona nace en esta vela", ZONA, 0.20)])

    # ── 4 · romper no es confirmar ──────────────────────────────────────
    hecho = False
    for z in sorted(zonas, key=lambda z: z["vela"]):
        borde = z["hi"] if z["tipo"] == "R" else z["lo"]
        rot = next((i for i in range(z["vela"] + 2, min(z["vela"] + 45, i1))
                    if (V[i]["h"] > borde if z["tipo"] == "R" else V[i]["l"] < borde)), None)
        if rot is None or rot + 6 >= i1:
            continue
        conf = next((j for j in range(rot + 1, min(rot + 6, i1))
                     if (V[j]["h"] > V[rot]["h"] if z["tipo"] == "R" else V[j]["l"] < V[rot]["l"])), None)
        if not conf:
            continue
        a, b = max(z["vela"] - 5, i0), min(conf + 12, i1)
        arriba = z["tipo"] == "R"
        dibujar(V, a, b,
                "Cruzar la zona no basta: hay que confirmarlo",
                "Una vela la atraviesa. Solo cuenta cuando la siguiente pasa del extremo de esa vela.",
                os.path.join(SALIDA, "04-romper-confirmar.png"),
                zonas=[z],
                marcas=[(rot, V[rot]["h"] if arriba else V[rot]["l"],
                         "Esta vela cruza la zona", ORO, 0.20 if arriba else -0.20),
                        (conf, V[conf]["h"] if arriba else V[conf]["l"],
                         "Esta lo confirma", VERDE, 0.30 if arriba else -0.30)])
        hecho = True
        break
    if not hecho:
        print("  aviso: no se encontró un cruce con confirmación en esta sesión")

    print("\nlistos en public/conceptos/")
    return 0


if __name__ == "__main__":
    sys.exit(main())

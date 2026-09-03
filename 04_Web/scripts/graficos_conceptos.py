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
TICK = 0.25       # el tick del NQ, de PARAMETROS.md
TOPE_STOP = 80.0  # STOP_MAX, de PARAMETROS.md. Si se supera, no se opera
UMBRAL_VOL_NQ = 2000  # UMBRAL_VOL_NQ, de PARAMETROS.md. Solo en premercado
VERDE = "#4ADE80"

plt.rcParams["font.family"] = ["DejaVu Sans"]


def ventana_sesion(V, dia):
    """Índices de la ventana operativa. El ancla es la apertura americana:
       13:31-15:30 UTC en horario de verano de Nueva York.

       Empieza en 1331, no en 1330: las velas del archivo van marcadas al
       CIERRE, así que la vela «13:31» es la que cubre el minuto de la
       apertura. Se ve en el volumen — 641 contratos en la 13:30 y 4.333 en
       la 13:31 del 13/07 — y es la misma cuenta que hace lector.py, que la
       llama «la vela base 08:31»."""
    idx = [i for i, k in enumerate(V) if k["d"] == dia and 1331 <= int(k["t"][:4]) <= 1530]
    return (idx[0], idx[-1] + 1) if idx else (None, None)


def hora(k):
    return "%02d:%s" % ((int(k["t"][:2]) - 5) % 24, k["t"][2:4])


def dibujar(V, i0, i1, titulo, explicacion, salida,
            zonas=None, zigzag=None, tramos=None, marcas=None,
            operacion=None, franja=None, lineas=None):
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
        tenue = z.get("tenue", False)
        ax.add_patch(Rectangle((x, z["lo"]), n - x + 1, max(z["hi"] - z["lo"], 0.25),
                               facecolor=ZONA, alpha=0.08 if tenue else 0.26,
                               edgecolor=ZONA, lw=0.8 if tenue else 1.4,
                               linestyle=":" if tenue else "-", zorder=1))
        # La etiqueta va DENTRO de la zona, a la derecha, como en el material
        # del operador. Dice que es y de que vela sale, sin tapar las velas.
        et = z.get("etiqueta")
        if et:
            ax.text(n - 0.5, (z["lo"] + z["hi"]) / 2, et,
                    color=TENUE if tenue else TXT, fontsize=11.5, weight="bold",
                    ha="right", va="center", zorder=6)

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
        # El estandar del operador: las franjas van SOLO sobre el tramo de la
        # operacion, no de lado a lado del grafico. Con la vela de salida se
        # cortan ahi; sin ella llegan hasta el borde.
        xe, entrada, stop, objetivo = operacion[:4]
        xs = operacion[4] if len(operacion) > 4 else None
        x = xe - i0
        ancho = (xs - i0 - x + 1) if xs is not None else (n - x + 1)
        ax.add_patch(Rectangle((x, min(entrada, stop)), ancho,
                               abs(stop - entrada), facecolor=ROJO, alpha=0.14, zorder=2))
        ax.add_patch(Rectangle((x, min(entrada, objetivo)), ancho,
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

    # Lineas horizontales de referencia (la mitad entre dos zonas, R-17).
    # A trazos y con su etiqueta a la izquierda: es una medida, no un nivel
    # del mercado, y tiene que distinguirse de una zona.
    for ln in (lineas or []):
        precio, etiqueta, color = ln
        ax.plot([0, n], [precio, precio], color=color, lw=1.4,
                linestyle=(0, (6, 4)), alpha=0.9, zorder=5)
        ax.text(0.4, precio + rango * 0.012, etiqueta, color=color,
                fontsize=12, weight="bold", ha="left", va="bottom", zorder=7)

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
    # Sesiones validadas al tick por el operador, para buscar los casos.
    DIAS = ["20260713", "20260716", "20260715", "20260720", "20260710",
            "20260709", "20260708", "20260707", "20260706", "20260717"]
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
                "Al movimiento que avanza se le llama corrida. Al descanso que viene después, retroceso.",
                os.path.join(SALIDA, "02-corrida-retroceso.png"),
                tramos=[(z["c0"], z["vela"], "CORRIDA", ALCISTA),
                        (z["vela"], fin_retro, "RETROCESO", ORO)])

        # ── 3 · de dónde sale una zona ──────────────────────────────────
        dibujar(V, a, b,
                "Cada movimiento deja un rastro",
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
                "Cruzar la zona no basta: hace falta la consecución",
                "Una vela la atraviesa. Solo cuenta cuando otra pasa del extremo de esa vela.",
                os.path.join(SALIDA, "04-romper-confirmar.png"),
                zonas=[z],
                marcas=[(rot, V[rot]["h"] if arriba else V[rot]["l"],
                         "Esta vela rompe la zona", ORO, 0.20 if arriba else -0.20),
                        (conf, V[conf]["h"] if arriba else V[conf]["l"],
                         "Esta es la consecución", VERDE, 0.30 if arriba else -0.30)])
        hecho = True
        break
    if not hecho:
        print("  aviso: no se encontró un cruce con confirmación en esta sesión")

    # ── 5 · cruzar sin confirmar ────────────────────────────────────────
    for z in sorted(zonas, key=lambda z: z["vela"]):
        arriba = z["tipo"] == "R"
        borde = z["hi"] if arriba else z["lo"]
        rot = next((i for i in range(z["vela"] + 2, min(z["vela"] + 45, i1))
                    if (V[i]["h"] > borde if arriba else V[i]["l"] < borde)), None)
        if rot is None or rot + 8 >= i1:
            continue
        # que NINGUNA de las siguientes pase del extremo de la que cruzó
        if any((V[j]["h"] > V[rot]["h"] if arriba else V[j]["l"] < V[rot]["l"])
               for j in range(rot + 1, min(rot + 6, i1))):
            continue
        a, b = max(z["vela"] - 5, i0), min(rot + 16, i1)
        dibujar(V, a, b,
                "Sin consecución, no ha pasado nada",
                "La vela cruza la zona, pero ninguna de las siguientes la supera. La zona sigue viva.",
                os.path.join(SALIDA, "05-sin-confirmar.png"),
                zonas=[z],
                marcas=[(rot, V[rot]["h"] if arriba else V[rot]["l"],
                         "Cruza la zona", ORO, 0.20 if arriba else -0.20)],
                tramos=[(rot + 1, min(rot + 5, i1 - 1), "NINGUNA LA SUPERA", TENUE)])
        break

    # ── 6, 7 y 8 · la entrada, el stop y el descarte por tope ───────────
    #
    # OJO: un setup cuyo stop pase del tope NO SE OPERA. Ensenarlo como
    # ejemplo de «asi va el stop» seria enganoso, asi que se buscan los dos
    # casos por separado: uno dentro del tope para explicar la operacion, y
    # uno fuera para explicar por que a veces no se opera.
    dentro = fuera = None
    for dia in DIAS:
        j0, j1 = ventana_sesion(V, dia)
        if j0 is None:
            continue
        for z in sorted(motor.estructura(V, j0, j1), key=lambda z: z["vela"]):
            arriba = z["tipo"] == "R"
            borde = z["hi"] if arriba else z["lo"]
            rot = next((i for i in range(z["vela"] + 2, min(z["vela"] + 45, j1))
                        if (V[i]["h"] > borde if arriba else V[i]["l"] < borde)), None)
            if rot is None or rot + 14 >= j1:
                continue
            conf = next((j for j in range(rot + 1, min(rot + 6, j1))
                         if (V[j]["h"] > V[rot]["h"] if arriba else V[j]["l"] < V[rot]["l"])), None)
            if conf is None:
                continue

            # La orden espera un tick mas alla del extremo de la vela que cruzo.
            entrada = V[rot]["h"] + TICK if arriba else V[rot]["l"] - TICK
            # El stop, al extremo alcanzado desde que nacio la zona.
            tramo = range(z["vela"], conf + 1)
            stop = min(V[i]["l"] for i in tramo) if arriba else max(V[i]["h"] for i in tramo)
            riesgo = abs(entrada - stop)
            caso = (z, rot, conf, entrada, stop, riesgo, j0, j1)
            if riesgo <= TOPE_STOP and dentro is None:
                dentro = caso
            elif riesgo > TOPE_STOP and fuera is None:
                fuera = caso
            if dentro and fuera:
                break
        if dentro and fuera:
            break

    if dentro:
        z, rot, conf, entrada, stop, riesgo, j0, j1 = dentro
        arriba = z["tipo"] == "R"
        objetivo = entrada + (entrada - stop)          # la misma distancia
        a, b = max(z["vela"] - 4, j0), min(conf + 24, j1)

        dibujar(V, a, b,
                "La entrada se coloca por adelantado",
                "La orden espera un tick más allá de la vela que cruzó. El mercado la ejecuta solo.",
                os.path.join(SALIDA, "06-entrada.png"),
                zonas=[z],
                marcas=[(rot, entrada, "Aquí espera la orden", ALCISTA, 0.24 if arriba else -0.24),
                        (conf, V[conf]["h"] if arriba else V[conf]["l"],
                         "Aquí se llena", VERDE, 0.38 if arriba else -0.38)])

        dibujar(V, a, b,
                "El stop no se elige: lo pone la estructura",
                "Rojo lo que se arriesga, verde lo que se busca. El objetivo recorre la misma distancia.",
                os.path.join(SALIDA, "07-stop-objetivo.png"),
                zonas=[z],
                operacion=(conf, entrada, stop, objetivo),
                marcas=[(conf, stop, "Stop, a %.2f puntos" % riesgo, ROJO, -0.13),
                        (conf, objetivo, "Objetivo, la misma distancia", VERDE, 0.13)])
    else:
        print("  aviso: no se encontró un setup dentro del tope de stop")

    if fuera:
        z, rot, conf, entrada, stop, riesgo, j0, j1 = fuera
        arriba = z["tipo"] == "R"
        a, b = max(z["vela"] - 4, j0), min(conf + 20, j1)
        dibujar(V, a, b,
                "Si el stop pasa del tope, no se opera",
                "Aquí el stop mediría %.0f puntos y el tope son %.0f. El setup se descarta entero."
                % (riesgo, TOPE_STOP),
                os.path.join(SALIDA, "08-descarte.png"),
                zonas=[z],
                marcas=[(conf, entrada, "La entrada estaría aquí", TENUE, 0.16 if arriba else -0.16),
                        (conf, stop, "Pero el stop llega hasta aquí", ROJO, -0.18 if arriba else 0.18)])
    else:
        print("  aviso: no se encontró un setup fuera del tope de stop")

    # ── 9 · zona de premercado por volumen ──────────────────────────────
    #
    # La ventana de premercado empieza a las 19:00 hora Colombia del dia
    # ANTERIOR, que en UTC es la medianoche del dia en curso. Por eso basta
    # con filtrar el mismo dia por debajo de la hora de apertura.
    pre, cand = [], []
    for dia in [DIA] + DIAS:
        pre = [i for i, k in enumerate(V) if k["d"] == dia and int(k["t"][:4]) < 1330]
        cand = [i for i in pre if V[i]["v"] > UMBRAL_VOL_NQ]
        if cand:
            break
    if cand:
        # La de mas volumen de todas: es la que mejor ensena el concepto.
        i = max(cand, key=lambda i: V[i]["v"])
        k = V[i]
        alcista = k["c"] >= k["o"]
        lo, hi = (max(k["o"], k["c"]), k["h"]) if alcista else (k["l"], min(k["o"], k["c"]))
        a, b = max(i - 26, pre[0]), min(i + 34, pre[-1] + 1)
        dibujar(V, a, b,
                "De madrugada, el volumen deja zona",
                "Toda vela por encima de %s contratos deja zona. Alcista deja resistencia, bajista deja soporte."
                % "{:,}".format(UMBRAL_VOL_NQ).replace(",", "."),
                os.path.join(SALIDA, "09-zona-volumen.png"),
                zonas=[dict(vela=i, lo=lo, hi=hi, tipo="R" if alcista else "S")],
                marcas=[(i, (lo + hi) / 2,
                         "%s contratos en un minuto" % "{:,}".format(k["v"]).replace(",", "."),
                         ORO, 0.22 if alcista else -0.22)])
    else:
        print("  aviso: ninguna vela de premercado supera el umbral ese dia")

    # ── 10 · zona apéndice ──────────────────────────────────────────────
    #
    # Rompimiento CON CUERPO (el cierre queda fuera) que no se confirma en 5
    # velas: la zona original se queda igual y nace una segunda sobre la
    # mecha de la vela que rompio.
    puesto = False
    for dia in DIAS:
        j0, j1 = ventana_sesion(V, dia)
        if j0 is None:
            continue
        for z in sorted(motor.estructura(V, j0, j1), key=lambda z: z["vela"]):
            arriba = z["tipo"] == "R"
            borde = z["hi"] if arriba else z["lo"]
            rot = next((i for i in range(z["vela"] + 2, min(z["vela"] + 45, j1))
                        if (V[i]["h"] > borde if arriba else V[i]["l"] < borde)), None)
            if rot is None or rot + 10 >= j1:
                continue
            # con cuerpo: el CIERRE queda mas alla del borde
            con_cuerpo = V[rot]["c"] > borde if arriba else V[rot]["c"] < borde
            if not con_cuerpo:
                continue
            # y ninguna de las 5 siguientes pasa de su extremo
            if any((V[j]["h"] > V[rot]["h"] if arriba else V[j]["l"] < V[rot]["l"])
                   for j in range(rot + 1, min(rot + 6, j1))):
                continue
            kr = V[rot]
            ap_lo, ap_hi = ((max(kr["o"], kr["c"]), kr["h"]) if arriba
                            else (kr["l"], min(kr["o"], kr["c"])))
            a, b = max(z["vela"] - 4, j0), min(rot + 14, j1)
            dibujar(V, a, b,
                    "Rompió con el cuerpo y no hubo consecución",
                    "Pasadas cinco velas sin consecución, la zona original se queda igual y nace una segunda sobre la mecha.",
                    os.path.join(SALIDA, "10-zona-apendice.png"),
                    zonas=[z, dict(vela=rot, lo=ap_lo, hi=ap_hi, tipo=z["tipo"])],
                    marcas=[(z["vela"], (z["lo"] + z["hi"]) / 2, "La zona original", TENUE, -0.22 if arriba else 0.22),
                            (rot, (ap_lo + ap_hi) / 2, "La zona apéndice", ORO, 0.24 if arriba else -0.24)],
                    tramos=[(rot + 1, min(rot + 5, j1 - 1), "CINCO VELAS SIN CONSECUCIÓN", TENUE)])
            puesto = True
            break
        if puesto:
            break
    if not puesto:
        print("  aviso: no se encontró un rompimiento con cuerpo sin confirmar")

    # ── 11 · reingreso ──────────────────────────────────────────────────
    #
    # Rompimiento CONFIRMADO que falla: el precio se da la vuelta, atraviesa
    # la zona entera y sale por el borde contrario.
    puesto = False
    for dia in DIAS:
        j0, j1 = ventana_sesion(V, dia)
        if j0 is None:
            continue
        for z in sorted(motor.estructura(V, j0, j1), key=lambda z: z["vela"]):
            arriba = z["tipo"] == "R"
            borde = z["hi"] if arriba else z["lo"]
            contra = z["lo"] if arriba else z["hi"]
            rot = next((i for i in range(z["vela"] + 2, min(z["vela"] + 40, j1))
                        if (V[i]["h"] > borde if arriba else V[i]["l"] < borde)), None)
            if rot is None:
                continue
            conf = next((j for j in range(rot + 1, min(rot + 6, j1))
                         if (V[j]["h"] > V[rot]["h"] if arriba else V[j]["l"] < V[rot]["l"])), None)
            if conf is None or conf + 12 >= j1:
                continue
            # el precio vuelve y SALE por el borde contrario
            rein = next((i for i in range(conf + 1, min(conf + 30, j1))
                         if (V[i]["l"] < contra if arriba else V[i]["h"] > contra)), None)
            if rein is None or rein + 6 >= j1:
                continue
            ent = next((j for j in range(rein + 1, min(rein + 4, j1))
                        if (V[j]["l"] < V[rein]["l"] if arriba else V[j]["h"] > V[rein]["h"])), None)
            if ent is None:
                continue
            # El plan pide que el rompimiento NO continue. Eso no es un
            # adjetivo: el stop del reingreso va al extremo de la corrida
            # fallida, y si esa corrida se fue lejos el stop no cabe en el
            # tope y el reingreso NO SE OPERA. Ensenar uno asi enganaria.
            ent_nivel = V[rein]["l"] - TICK if arriba else V[rein]["h"] + TICK
            fallida = range(rot, rein + 1)
            stop_re = (max(V[i]["h"] for i in fallida) if arriba
                       else min(V[i]["l"] for i in fallida))
            if abs(ent_nivel - stop_re) > TOPE_STOP:
                continue
            a, b = max(z["vela"] - 3, j0), min(ent + 14, j1)
            dibujar(V, a, b,
                    "El rompimiento falló: se opera la vuelta",
                    "Hubo consecución y no siguió. El precio atraviesa la zona entera, sale por el otro lado y ahí entra.",
                    os.path.join(SALIDA, "11-reingreso.png"),
                    zonas=[z],
                    marcas=[(conf, V[conf]["h"] if arriba else V[conf]["l"],
                             "Rompimiento y consecución", TENUE, 0.20 if arriba else -0.20),
                            (rein, contra, "Atraviesa la zona entera", ORO, -0.24 if arriba else 0.24),
                            (ent, V[ent]["l"] if arriba else V[ent]["h"],
                             "Aquí entra el reingreso", VERDE, -0.36 if arriba else 0.36)])
            puesto = True
            break
        if puesto:
            break
    if not puesto:
        print("  aviso: no se encontró un reingreso completo")

    # ── 12 · la primera vela de la sesión ───────────────────────────────
    #
    # Se busca una sesion cuya primera vela tenga cuerpo de verdad: con una
    # vela plana el concepto («declara la direccion con su propio cuerpo»)
    # no se ve, y un grafico que no ensena lo que dice sobra.
    mejor = None
    for dia in [DIA] + DIAS:
        j0, j1 = ventana_sesion(V, dia)
        if j0 is None:
            continue
        k = V[j0]
        cuerpo = abs(k["c"] - k["o"])
        rango_v = k["h"] - k["l"]
        if rango_v <= 0:
            continue
        # cuerpo que ocupe al menos la mitad de la vela, y vela con tamano
        proporcion = cuerpo / rango_v
        if proporcion >= 0.5 and cuerpo >= 4:
            mejor = (j0, j1, k)
            break
    if mejor:
        j0, j1, k0 = mejor
        sube = k0["c"] >= k0["o"]
        dibujar(V, j0 - 2, min(j0 + 16, j1),
                "La primera vela declara la dirección",
                "Cierra %s de su apertura, así que el día empieza %s. Y es el origen desde el que se mide el primer movimiento."
                % ("por encima" if sube else "por debajo", "alcista" if sube else "bajista"),
                os.path.join(SALIDA, "12-vela-0831.png"),
                marcas=[(j0, k0["c"],
                         "Cierra %s de su apertura" % ("por encima" if sube else "por debajo"),
                         VERDE if sube else ROJO, 0.30 if sube else -0.30),
                        (j0, k0["l"] if sube else k0["h"],
                         "Y aquí empieza a medirse el primer movimiento", ALCISTA,
                         -0.30 if sube else 0.30)],
                franja=(j0, j0 + 1, ORO, "PRIMERA VELA"))
    else:
        print("  aviso: ninguna primera vela con cuerpo suficiente")

    # ── 13 · la operación de principio a fin ────────────────────────────
    if dentro:
        z, rot, conf, entrada, stop, riesgo, j0, j1 = dentro
        arriba = z["tipo"] == "R"
        objetivo = entrada + (entrada - stop)
        # hasta donde llega: primera vela que toca el objetivo o el stop
        fin = j1 - 1
        for i in range(conf + 1, j1):
            toca_obj = V[i]["h"] >= objetivo if arriba else V[i]["l"] <= objetivo
            toca_stop = V[i]["l"] <= stop if arriba else V[i]["h"] >= stop
            if toca_obj or toca_stop:
                fin = i
                resultado = "objetivo" if toca_obj else "stop"
                break
        else:
            resultado = None
        a, b = max(conf - 8, j0), min(fin + 4, j1)
        marcas = [(conf, entrada, "Se llena aquí", ALCISTA, 0.16 if arriba else -0.16)]
        if resultado:
            marcas.append((fin, objetivo if resultado == "objetivo" else stop,
                           "Sale en el " + resultado,
                           VERDE if resultado == "objetivo" else ROJO,
                           0.16 if arriba else -0.16))
        dibujar(V, a, b,
                "Colocados el stop y el objetivo, no se toca nada",
                "Solo hay dos salidas. Ni punto de entrada, ni cierre a mano, ni cierre por hora.",
                os.path.join(SALIDA, "13-dentro.png"),
                zonas=[z],
                operacion=(conf, entrada, stop, objetivo, fin),
                marcas=marcas)

    # ── 14 · el traspaso, en otra sesion ────────────────────────────────
    # El apartado «Romper y confirmar» de Marcacion de zonas se quedaba sin
    # grafico. Es el mismo patron del numero 4, pero se busca en OTRO dia
    # para no ensenar dos veces la misma imagen en el mismo recorrido.
    hecho = False
    for d in DIAS:
        if d == DIA:
            continue
        j0, j1 = ventana_sesion(V, d)
        if j0 is None:
            continue
        zs = motor.estructura(V, j0, j1)
        for z in sorted(zs, key=lambda z: z["vela"]):
            arriba = z["tipo"] == "R"
            borde = z["hi"] if arriba else z["lo"]
            rot = next((i for i in range(z["vela"] + 2, min(z["vela"] + 45, j1))
                        if (V[i]["h"] > borde if arriba else V[i]["l"] < borde)), None)
            if rot is None or rot + 6 >= j1:
                continue
            conf = next((k for k in range(rot + 1, min(rot + 6, j1))
                         if (V[k]["h"] > V[rot]["h"] if arriba else V[k]["l"] < V[rot]["l"])), None)
            if not conf:
                continue
            a, b = max(z["vela"] - 5, j0), min(conf + 12, j1)
            dibujar(V, a, b,
                    "Rompimiento y consecución: recién ahí la zona quedó superada",
                    "La primera pasa el borde por un tick, y basta la mecha. La segunda pasa del extremo de la primera.",
                    os.path.join(SALIDA, "14-traspaso.png"),
                    zonas=[z],
                    marcas=[(rot, V[rot]["h"] if arriba else V[rot]["l"],
                             "ROMPIMIENTO", ORO, 0.20 if arriba else -0.20),
                            (conf, V[conf]["h"] if arriba else V[conf]["l"],
                             "CONSECUCIÓN", VERDE, 0.32 if arriba else -0.32)])
            hecho = True
            break
        if hecho:
            break
    if not hecho:
        print("  aviso: no se encontro un traspaso en otra sesion")

    # ── 15 · la sesion entera, con sus zonas ────────────────────────────
    # «Como avanza la sesion» tampoco tenia grafico. Es la ventana completa
    # con su zigzag: el apartado habla de como AVANZA la sesion, o sea de la
    # cadena de corridas y retrocesos.
    #
    # SIN las zonas a proposito. Dibujar las 44 que devuelve el motor tapa
    # las velas con una mancha gris, y ademas el plan dice que en pantalla
    # va una sola zona por banda y por jornada, no las 44 en crudo. Filtrar
    # cual sobrevive en cada banda es metodologia, no dibujo: se decide en
    # 01_Plan, no aqui.
    dibujar(V, i0, i1,
            "Una sesión entera, de la primera vela a la última",
            "La línea blanca une los extremos: cada movimiento que avanza y cada descanso, de la primera vela a la última.",
            os.path.join(SALIDA, "15-sesion.png"),
            zigzag=zz)

    # ══════════════════════════════════════════════════════════════════
    # MARCACION DE ZONAS — 16 a 23
    # El modulo 2 necesita una imagen por casuistica. Todas se buscan en
    # datos reales del operador; ninguna se dibuja a mano.
    # ══════════════════════════════════════════════════════════════════

    def sesiones():
        """Los dias validados, con su ventana y su estructura ya calculada."""
        for d in DIAS:
            a, b = ventana_sesion(V, d)
            if a is None or b - a < 30:
                continue
            yield d, a, b, motor.estructura(V, a, b)

    def borde_de(z):
        return z["hi"] if z["tipo"] == "R" else z["lo"]

    def busca_rompimiento(z, j1, desde=None):
        """La primera vela que pasa el borde de la zona por un tick."""
        arriba = z["tipo"] == "R"
        borde = borde_de(z)
        ini = desde if desde is not None else z["vela"] + 2
        for i in range(ini, min(z["vela"] + 60, j1)):
            if (V[i]["h"] > borde) if arriba else (V[i]["l"] < borde):
                return i
        return None

    def busca_consecucion(z, rot, j1, plazo=5):
        """La vela que pasa del extremo de la que rompio, dentro del plazo."""
        arriba = z["tipo"] == "R"
        for j in range(rot + 1, min(rot + 1 + plazo, j1)):
            if (V[j]["h"] > V[rot]["h"]) if arriba else (V[j]["l"] < V[rot]["l"]):
                return j
        return None

    def con_cuerpo(z, rot):
        """El cierre quedo al otro lado del borde: rompimiento con cuerpo."""
        borde = borde_de(z)
        return (V[rot]["c"] > borde) if z["tipo"] == "R" else (V[rot]["c"] < borde)

    # ── 16 · la corrida bajista ─────────────────────────────────────────
    # El apartado del movimiento necesita los dos sentidos, no solo el alza.
    hecho = False
    for d, j0, j1, zs in sesiones():
        cand = [z for z in zs if z["tipo"] == "S" and z["c1"] - z["c0"] >= 5]
        if not cand:
            continue
        z = max(cand, key=lambda z: V[z["c0"]]["h"] - V[z["vela"]]["l"])
        fin_retro = min(z["c1"] + 4, j1 - 1)
        a, b = max(z["c0"] - 4, j0), min(fin_retro + 5, j1)
        z2 = dict(z, etiqueta="SOPORTE")
        dibujar(V, a, b,
                "El mismo movimiento, hacia abajo",
                "La corrida baja y el retroceso sube. El soporte sale de la vela más baja del movimiento.",
                os.path.join(SALIDA, "16-corrida-bajista.png"),
                zonas=[z2],
                tramos=[(z["c0"], z["vela"], "CORRIDA", BAJISTA),
                        (z["vela"], fin_retro, "RETROCESO", ORO)])
        hecho = True
        break
    if not hecho:
        print("  aviso: sin corrida bajista larga y limpia")

    # ── 17 · la vela designada y sus dos bordes ─────────────────────────
    # De donde salen exactamente los dos limites de la zona.
    hecho = False
    for d, j0, j1, zs in sesiones():
        cand = [z for z in zs if z["tipo"] == "R"
                and V[z["vela"]]["h"] - max(V[z["vela"]]["o"], V[z["vela"]]["c"]) > 3.0
                and z["c1"] - z["c0"] >= 3]
        if not cand:
            continue
        z = cand[0]
        k = V[z["vela"]]
        a, b = max(z["c0"] - 3, j0), min(z["c1"] + 10, j1)
        z2 = dict(z, etiqueta="RESISTENCIA")
        dibujar(V, a, b,
                "Los dos bordes salen de una sola vela",
                "Del borde del cuerpo a la punta de la mecha. Ni un tick más, ni un tick menos.",
                os.path.join(SALIDA, "17-vela-designada.png"),
                zonas=[z2],
                marcas=[(z["vela"], k["h"], "Punta de la mecha", ZONA, 0.16),
                        (z["vela"], max(k["o"], k["c"]), "Borde del cuerpo", ZONA, -0.22)])
        hecho = True
        break
    if not hecho:
        print("  aviso: sin vela con mecha larga para el detalle")

    # ── 18 y 19 · rompimiento con mecha y con cuerpo ────────────────────
    # La diferencia importa despues: decide si la zona se estira o si nace
    # una apendice (R-15 / R-16).
    for etiqueta, quiere_cuerpo, archivo, titulo, expl in [
        ("mecha", False, "18-rompe-mecha.png",
         "Rompimiento con mecha",
         "La vela pasa el borde pero cierra dentro de la zona. Sigue siendo rompimiento: basta un tick."),
        ("cuerpo", True, "19-rompe-cuerpo.png",
         "Rompimiento con cuerpo",
         "Aquí la vela cierra al otro lado del borde. Mismo rompimiento, pero deja otro rastro si no llega la consecución."),
    ]:
        hecho = False
        for d, j0, j1, zs in sesiones():
            for z in sorted(zs, key=lambda z: z["vela"]):
                rot = busca_rompimiento(z, j1)
                if rot is None or rot + 8 >= j1:
                    continue
                if con_cuerpo(z, rot) != quiere_cuerpo:
                    continue
                conf = busca_consecucion(z, rot, j1)
                if not conf:
                    continue
                arriba = z["tipo"] == "R"
                a, b = max(z["vela"] - 5, j0), min(conf + 12, j1)
                z2 = dict(z, etiqueta="RESISTENCIA" if arriba else "SOPORTE")
                dibujar(V, a, b, titulo, expl,
                        os.path.join(SALIDA, archivo),
                        zonas=[z2],
                        marcas=[(rot, V[rot]["h"] if arriba else V[rot]["l"],
                                 "Rompimiento", ORO, 0.20 if arriba else -0.20),
                                (conf, V[conf]["h"] if arriba else V[conf]["l"],
                                 "Consecución", VERDE, 0.32 if arriba else -0.32)])
                hecho = True
                break
            if hecho:
                break
        if not hecho:
            print("  aviso: sin rompimiento con " + etiqueta)

    # ── 20 · la zona apendice, ya rota ──────────────────────────────────
    # El PDF del operador dedica dos paginas a esto: lo que pasa DESPUES de
    # que nace la apendice. La original queda traspasada en los dos sentidos.
    hecho = False
    for d, j0, j1, zs in sesiones():
        for z in sorted(zs, key=lambda z: z["vela"]):
            rot = busca_rompimiento(z, j1)
            if rot is None or rot + 14 >= j1:
                continue
            if not con_cuerpo(z, rot):
                continue
            if busca_consecucion(z, rot, j1):
                continue                      # aqui hace falta que NO la haya
            arriba = z["tipo"] == "R"
            k = V[rot]
            ap_lo, ap_hi = ((max(k["o"], k["c"]), k["h"]) if arriba
                            else (k["l"], min(k["o"], k["c"])))
            ap = dict(vela=rot, lo=ap_lo, hi=ap_hi, tipo=z["tipo"],
                      etiqueta="APÉNDICE")
            a = max(z["vela"] - 4, j0)
            b = min(rot + 22, j1)
            z2 = dict(z, etiqueta="ZONA ORIGINAL")
            dibujar(V, a, b,
                    "La zona apéndice nace del rompimiento sin consecución",
                    "Rompió con cuerpo y pasaron las cinco velas. La original no se toca; la apéndice se marca sobre la mecha de la vela que rompió.",
                    os.path.join(SALIDA, "20-apendice-nace.png"),
                    zonas=[z2, ap],
                    marcas=[(rot, k["h"] if arriba else k["l"],
                             "Rompió con cuerpo", ORO, 0.20 if arriba else -0.20)])
            hecho = True
            break
        if hecho:
            break
    if not hecho:
        print("  aviso: sin caso de zona apendice")

    # ── 21 · dos zonas que se tocan se funden en una ────────────────────
    hecho = False
    for d, j0, j1, zs in sesiones():
        mismo = {}
        for z in zs:
            mismo.setdefault(z["tipo"], []).append(z)
        for tipo, lista in mismo.items():
            lista = sorted(lista, key=lambda z: z["vela"])
            for x, y in zip(lista, lista[1:]):
                if not (y["lo"] <= x["hi"] and y["hi"] >= x["lo"]):
                    continue
                if y["vela"] - x["vela"] < 2 or y["vela"] - x["vela"] > 25:
                    continue
                union = dict(vela=x["vela"], tipo=tipo,
                             lo=min(x["lo"], y["lo"]), hi=max(x["hi"], y["hi"]),
                             etiqueta="UNA SOLA ZONA")
                a = max(x["vela"] - 5, j0)
                b = min(y["vela"] + 16, j1)
                dibujar(V, a, b,
                        "Si la nueva toca a la existente, se estira",
                        "No quedan dos zonas pegadas: queda una sola, estirada hasta el extremo nuevo. El otro borde no se mueve.",
                        os.path.join(SALIDA, "21-zonas-se-funden.png"),
                        zonas=[union],
                        marcas=[(x["vela"], (x["lo"] + x["hi"]) / 2,
                                 "La que ya estaba", ZONA, 0.20),
                                (y["vela"], (y["lo"] + y["hi"]) / 2,
                                 "La que iba a marcarse", ZONA, -0.24)])
                hecho = True
                break
            if hecho:
                break
        if hecho:
            break
    if not hecho:
        print("  aviso: sin dos zonas que se toquen")

    # ── 22 · zona entre zonas: la mitad manda ───────────────────────────
    hecho = False
    for d, j0, j1, zs in sesiones():
        orden = sorted(zs, key=lambda z: z["vela"])
        for z in orden:
            vivas = [w for w in orden if w["vela"] < z["c0"]]
            arr = [w for w in vivas if w["lo"] > V[z["vela"]]["h"]]
            aba = [w for w in vivas if w["hi"] < V[z["vela"]]["l"]]
            if not arr or not aba:
                continue
            sup = min(arr, key=lambda w: w["lo"])
            inf = max(aba, key=lambda w: w["hi"])
            mitad = (sup["lo"] + inf["hi"]) / 2
            alto = max(V[i]["h"] for i in range(z["c0"], z["c1"] + 1))
            bajo = min(V[i]["l"] for i in range(z["c0"], z["c1"] + 1))
            if alto > mitad and bajo < mitad:
                continue                       # este cruza: no sirve de ejemplo
            if sup["lo"] - inf["hi"] < 12:
                continue                       # banda demasiado estrecha
            a = max(min(sup["vela"], inf["vela"]) - 2, j0)
            b = min(z["c1"] + 14, j1)
            zonas_img = [dict(sup, etiqueta="ZONA DE ARRIBA"),
                         dict(inf, etiqueta="ZONA DE ABAJO"),
                         dict(z, etiqueta="SE MARCA")]
            dibujar(V, a, b,
                    "Entre dos zonas, solo si el movimiento no cruza la mitad",
                    "El movimiento entero se queda del lado en el que empezó. Por eso esta zona sí se marca.",
                    os.path.join(SALIDA, "22-entre-zonas.png"),
                    zonas=zonas_img,
                    lineas=[(mitad, "LA MITAD", ORO)])
            hecho = True
            break
        if hecho:
            break
    if not hecho:
        print("  aviso: sin zona entre zonas que respete la mitad")

    # ── 23 · zona traspasada en los dos sentidos ────────────────────────
    hecho = False
    for d, j0, j1, zs in sesiones():
        for z in sorted(zs, key=lambda z: z["vela"]):
            rot = busca_rompimiento(z, j1)
            if rot is None:
                continue
            conf = busca_consecucion(z, rot, j1)
            if not conf or conf + 12 >= j1:
                continue
            arriba = z["tipo"] == "R"
            borde2 = z["lo"] if arriba else z["hi"]
            rot2 = None
            for i in range(conf + 1, min(conf + 50, j1)):
                if (V[i]["l"] < borde2) if arriba else (V[i]["h"] > borde2):
                    rot2 = i
                    break
            if rot2 is None or rot2 + 6 >= j1:
                continue
            conf2 = None
            for j in range(rot2 + 1, min(rot2 + 6, j1)):
                if (V[j]["l"] < V[rot2]["l"]) if arriba else (V[j]["h"] > V[rot2]["h"]):
                    conf2 = j
                    break
            if conf2 is None:
                continue
            a = max(z["vela"] - 4, j0)
            b = min(conf2 + 12, j1)
            z2 = dict(z, etiqueta="YA NO CUENTA", tenue=True)
            dibujar(V, a, b,
                    "Traspasada en los dos sentidos: deja de contar",
                    "Se superó hacia un lado y después hacia el otro, las dos veces con consecución. A partir de ahí no bloquea ni sirve para entrar.",
                    os.path.join(SALIDA, "23-zona-invalida.png"),
                    zonas=[z2],
                    marcas=[(conf, V[conf]["h"] if arriba else V[conf]["l"],
                             "Traspaso de ida", VERDE, 0.20 if arriba else -0.20),
                            (conf2, V[conf2]["l"] if arriba else V[conf2]["h"],
                             "Traspaso de vuelta", VERDE, -0.26 if arriba else 0.26)])
            hecho = True
            break
        if hecho:
            break
    if not hecho:
        print("  aviso: sin zona traspasada en los dos sentidos")

    print("\nlistos en public/conceptos/")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# PARÁMETROS DEL PLAN

> **Un solo sitio para los números que pueden cambiar.**
> Las reglas citan el **nombre** del parámetro, no el valor. Se cambia aquí y se propaga a todo el plan.

**Actualizado:** 2026-09-01

---

## Riesgo y ejecución

| Parámetro | Valor actual | Equivalencias | Dónde actúa | Desde |
|---|---|---|---|---|
| **`STOP_MAX`** | **80 puntos** | 320 ticks · **$160** en MNQ | **Filtro de entrada** (`R-08`, `R-24`): si el stop estructural lo supera **aunque sea por 1 tick**, no se opera | 24/08/2026 |
| **`ATM_DEFECTO`** | **320 ticks** | 80 puntos · $160 | Stop y target provisionales de la ATM `K1` hasta el ajuste manual (`R-08`) | 24/08/2026 |
| **`RATIO_TARGET`** | **1:1** | — | El target recorre la misma distancia que el stop (`R-24`) | 21/08/2026 |
| **`CONTRATOS`** | **1** MNQ | — | Tamaño de posición (`R-08`) | 21/08/2026 |
| **`OPS_POR_SESION`** | **1** llenada | — | `R-03` | 21/08/2026 |

> 🔴 **`STOP_MAX` es una línea dura, no una zona de aviso.** No hay margen de seguridad por debajo del tope: un stop de 79,75 pts se opera exactamente igual que uno de 30. No existe *"está muy cerca del límite, mejor la dejo"*. Confirmado por el operador el **01/09/2026** sobre el caso del 16/07 (75,50 pts = **94 %** del tope, operación tomada y ganada).

> 🔑 **`ATM_DEFECTO` = `STOP_MAX` a propósito.** El stop provisional **nunca** debe ser más ajustado que el estructural: si lo fuera, el mercado podría sacarte de una operación todavía viva antes de que muevas el stop a mano. Si un día cambia `STOP_MAX`, **hay que cambiar `ATM_DEFECTO` con él**.

## Estructura

| Parámetro | Valor actual | Dónde actúa |
|---|---|---|
| **`TICK`** | 0,25 puntos | umbral de rompimiento y consecución (`R-13`) |
| **`PLAZO_CONSECUCION`** | **5 velas** | `R-13`, `R-22`, `R-15`, `R-16` y **`R-04`** (vida de la orden). 🔴 **Gobierna la geometría de la zona y la vida de la orden, NO el traspaso de la zona:** la consecución que invalida una zona **no tiene plazo** *(27/08/2026)* |
| **`VENTANA_REINGRESO`** | **hasta que el precio supere el extremo de la vela de consecución** | `R-23`. El reingreso es **inmediato o no es**: en cuanto el precio sigue de largo, la ventana se cierra para siempre *(27/08/2026)* |
| **`UMBRAL_50`** | 50 % | zonas entre zonas (`R-17`) |

## Volumen y sesión

| Parámetro | Valor actual | Dónde actúa |
|---|---|---|
| **`UMBRAL_VOL_NQ`** | > 2.000 contratos | `R-20` — solo premercado |
| **`UMBRAL_VOL_MNQ`** | > 6.000 contratos | `R-20` — solo premercado |
| **`PREMERCADO_INICIO`** | 19:00 hora Colombia (apertura de Tokio) | `R-20` |
| **`VENTANA_OPERATIVA`** | 09:30–11:30 ET | `R-02` |
| **`CANCELACION_FINAL`** | 11:29 ET | `R-04` |
| **`ORIGEN_DEL_STOP`** | desde que **nació la zona** hasta la vela de rompimiento | `R-24` — el stop es el extremo alcanzado en todo ese tramo, no solo el del retroceso que originó la zona *(27/08/2026)* |
| **`VENTANA_NOTICIA`** | ±5 minutos | `R-21` |

---

## Consecuencias de riesgo de `STOP_MAX = 80`

Sobre la cuenta objetivo de **$3.000**:

| | |
|---|---|
| Riesgo por operación | **$160** |
| Porcentaje del capital | **5,3 %** |
| Pérdida máxima diaria (`R-03`: 1 operación) | **5,3 %** |
| Cuatro sesiones perdedoras seguidas | **−21 %** |

**Aceptado explícitamente por el operador el 24/08/2026.** Ver `P-08`.

> Con `RATIO_TARGET` = 1:1, el win rate de equilibrio depende del tamaño del stop, no de este tope. Ver `P-12`.

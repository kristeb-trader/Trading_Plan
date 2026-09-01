# CHECKLIST DIARIA

> **Se ejecuta de arriba abajo. No se decide nada que no esté aquí.**
> Cada línea cita su regla. Si una respuesta es **NO** donde dice parar, **se para** — no se evalúa, no se matiza.

**Versión del plan:** 1.8-F1.9 · 2026-08-24

---

## 🅰 ANTES DE ABRIR NINJATRADER

| ☐ | Comprobación | Regla | Si falla |
|---|---|---|---|
| ☐ | **¿Estoy bien, física y mentalmente?** | `R-28` | **NO → no se opera hoy.** Se cierra aquí |
| ☐ | Forex Factory: **¿hay evento de la Fed en rojo hoy?** | `R-27` | **SÍ → hoy solo Reingreso. IRI prohibido todo el día** |
| ☐ | Forex Factory: anotar la **hora de cada noticia roja** | `R-21` | — |
| ☐ | Calcular las ventanas **T−5 → T+5** y marcar las que caigan dentro de la ventana operativa | `R-21` | — |

> Este bloque se contesta **antes** de abrir la plataforma. Con el gráfico delante ya no es la misma pregunta.

---

## 🅱 PREMERCADO · desde las 19:00 hora Colombia del día anterior

| ☐ | Acción | Regla |
|---|---|---|
| ☐ | Gráficos abiertos: **NQ y MNQ, 1 minuto**, único indicador **Volume Up Down** | `R-09`, `R-01` |
| ☐ | Escanear desde **19:00 Col** (apertura de Tokio) hasta la apertura americana | `R-20` |
| ☐ | Toda vela con **NQ > 2.000 contratos** → marcar zona. **Alcista → resistencia · Bajista → soporte** | `R-20` |
| ☐ | Se marcan **todas** las que superen el umbral, no solo los extremos | `R-20`, `D-09` |
| ☐ | Límites de cada zona: **del borde del cuerpo a la punta de la mecha** | `R-12` |
| ☐ | Si una zona candidata **toca** otra existente → **estirar la existente**, no crear una nueva | `R-18` |
| ☐ | Zona entre dos zonas: solo si el **movimiento no cruza el 50 %** entre bordes internos | `R-17` |

> 🔴 **La regla del volumen se apaga en la apertura americana.** A partir de ahí solo se marcan zonas por estructura.

---

## 🅲 VENTANA OPERATIVA · 08:30–10:30 Col *(verano)* · 09:30–11:30 Col *(invierno)*

### Identificar

| ☐ | Acción | Regla |
|---|---|---|
| ☐ | **Primer setup válido.** No se compara con posibles setups posteriores ni se espera uno mejor | `R-05` |
| ☐ | ¿Es **IRI** o **Reingreso**? | `R-22` / `R-23` |

### Medir · anclar la regla en el nivel de entrada

| ☐ | Setup | Dónde va el stop | Regla |
|---|---|---|---|
| ☐ | **IRI** | extremo del **retroceso** | `R-24` |
| ☐ | **Reingreso** | extremo de la **corrida fallida** | `R-24` |
| ☐ | **Target** = misma distancia, al otro lado. **1:1** | | `R-24` |

### Los cuatro filtros · basta que falle uno

| ☐ | Filtro | Regla | Si falla |
|---|---|---|---|
| ☐ | Stop ≤ **80 puntos** (`STOP_MAX`) | `R-08` | **NO SE OPERA** |
| ☐ | Target 1:1 **libre de zonas vigentes** | `R-24`, `R-14` | **NO SE OPERA** |
| ☐ | *(solo Reingreso)* Target dentro del **punto de referencia** | `R-23` | **NO SE OPERA** |
| ☐ | ¿Es día de FOMC y el setup es un IRI? | `R-27` | **NO SE OPERA** |

> 🔴 **El target nunca se acorta para que quepa.** No existe media entrada ni ratio reducido.

> 🟠 **Si un setup se descarta, la zona NO queda vacía.** Tras rechazar un **IRI** por cualquiera de los cuatro filtros, **seguir mirando esa misma zona**: si el rompimiento falla y el precio la atraviesa entera hasta salir por el borde contrario, ahí hay un **Reingreso** (`R-23`) — y puede llegar en la **misma vela**. Caso real: `G-12`, 06/07/2026, IRI descartado y Reingreso operado con un minuto de diferencia.

### Enviar

| ☐ | Acción | Regla |
|---|---|---|
| ☐ | ¿Estoy dentro de una ventana de noticia **T−5 → T+5**? → **no colocar**. Si ya hay orden puesta, **cancelarla** | `R-21` |
| ☐ | **Stop Market** al cierre de la vela de rompimiento o de reingreso, **1 tick más allá de su extremo** | `R-07` |
| ☐ | La orden se envía sobre el gráfico de **MNQ**, leyendo el nivel real de MNQ | `R-01`, `R-07` |
| ☐ | **No se persigue el precio a mano.** Orden a mercado y orden límite: prohibidas | `R-07` |

### Vigilar la orden pendiente · cancelar con lo primero que llegue

| ☐ | Causa de cancelación | Regla |
|---|---|---|
| ☐ | **Pasan 5 velas desde el rompimiento sin consecución** (el precio no llega al nivel de la orden) | `R-04` |
| ☐ | El precio **vuelve al punto del stop** — el extremo del retroceso | `R-04` |
| ☐ | Son las **11:29 ET** | `R-04` |
| ☐ | ⚠️ **Un retroceso nuevo NO cancela.** La orden sigue viva | `R-04` |
| ☐ | Entra una **ventana de noticia roja** | `R-21` |

> 🔴 **CORREGIDO 27/08/2026 — antes decía lo contrario.** El paso de 5 velas **SÍ cancela la orden**, y un retroceso nuevo **NO**.
> La caducidad se comprueba **antes** del llenado: pasado el plazo la orden ya no existe y no puede llenarse aunque el precio toque el nivel en esa misma vela.
> Caso real 9/07/2026: orden puesta en la 8:43, cancelada por error en la 8:45; con la regla correcta sigue viva y se llena en la **8:46**.
> Una orden cancelada **no consume el cupo** de `R-03`: se puede esperar otro setup.

---

## 🅳 TRAS EL LLENADO

| ☐ | Acción | Regla |
|---|---|---|
| ☐ | **1º** mover el **stop** a su nivel estructural | `R-08` |
| ☐ | **2º** mover el **target** a distancia 1:1 | `R-08`, `R-24` |
| ☐ | 🛑 **NO SE TOCA NADA MÁS. JAMÁS.** Ni breakeven, ni cierre manual, ni parcial, ni añadir | `R-25` |
| ☐ | Solo hay dos salidas: **stop o target** | `R-25` |
| ☐ | Cupo consumido. **No más órdenes hoy**, aunque aparezcan setups válidos | `R-03` |
| ☐ | El fin de ventana **no obliga a cerrar** una posición abierta | `R-06` |

---

## 📓 REGISTRO · se llena TODOS los días, se opere o no

### Automático · indicador de NinjaTrader
entrada · salida · niveles · hora · resultado

### Manual
| Campo | Por qué |
|---|---|
| **Setup**: `IRI Apertura` / `IRI Continuación` / `Reingreso` | sin esto no se pueden separar estadísticas por setup |
| **Imagen** de la operativa | `F1.10`, galería de casos |
| **Errores** cometidos | detecta desviaciones del plan |
| **Observaciones** | |
| **Días sin operar: el motivo** | 🔑 lo que casi ningún journal registra, y lo que más falta hace |

### Campos que cierran pendientes abiertos

| Campo a anotar | Cierra |
|---|---|
| Nº de zonas de premercado marcadas ese día | `D-09` — ¿marcar todas satura el gráfico? |
| ¿El precio se frenó en el **mín/máx de premercado** antes del target? | `P-01` |
| **Comisión real** ida y vuelta por contrato MNQ | `P-12` |
| Racha de días perdedores consecutivos | 🚨 `P-21` — **la regla de parada que el plan no tiene** |
| ¿El stop saltó en 80 pts siendo el estructural menor? | `P-09` |
| Hora exacta de la entrada | `P-20` — dónde acaba "la apertura" |


---

## 🔴 Añadido 27/08/2026 · lo que hay que mirar en cada zona

*Estas comprobaciones son de **marcado**, no de ejecución. Van mientras se lee el gráfico.*

| ☐ | Comprobación | Regla |
|---|---|---|
| ☐ | ¿La zona candidata cae dentro de una **banda ya gastada** hoy? → **no se marca** | `R-35` |
| ☐ | ¿Hay una zona viva con **rompimiento esperando consecución** entre el precio y la zona candidata? → **no se marca** | `R-36` |
| ☐ | El rompimiento se lee por la **mecha**, no por el cierre | `R-38` |
| ☐ | Una zona **no queda inválida** hasta que llega la **consecución** — y esa consecución **no tiene plazo** | `R-13`, `R-14` |
| ☐ | La vela que confirma un traspaso **no abre** el rompimiento contrario: se busca desde la siguiente | `R-37` |
| ☐ | Vencido el plazo sin consecución: **mecha → se estira** · **cuerpo → nace apéndice** | `R-15`, `R-16` |
| ☐ | El rectángulo se dibuja **desde la vela origen** | `R-38` |

## 🔴 Añadido 27/08/2026 · antes de enviar la orden

| ☐ | Comprobación | Regla |
|---|---|---|
| ☐ | El **stop** es el extremo alcanzado **desde que nació la zona** hasta el rompimiento — no solo el del retroceso que la originó | `R-24` |
| ☐ | Si es **Reingreso**: ¿el precio ya superó el extremo de la vela de consecución? → **no hay reingreso** | `R-23` |
| ☐ | Se buscan entradas en **los dos sentidos**; la vela de apertura no sesga el día | `R-34` |

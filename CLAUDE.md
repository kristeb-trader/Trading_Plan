# Proyecto Chaumer — instrucciones para Claude Code

**Qué es esto:** la metodología de trading de Alfredo Chaumer para NQ/MNQ en NinjaTrader 8, extraída durante la fase 1 a un plan mecánico de **38 reglas medibles**.

## Las fases

| | Fase | Estado | Seguimiento |
|---|---|---|---|
| **1** | **El plan** — la metodología extraída a 38 reglas medibles | 🏁 cerrada el 2026-09-01 | `01_Plan\CIERRE_FASE_1.md` |
| **2** | **El portal** — donde Alfredo revisa y deja observaciones | 🚧 **en marcha**, publicado y en revisión | **`04_Web\ESTADO_FASE_2.md`** |
| **3** | **Agente de backtesting** | 🔵 declarada, **sin definir** | `FASES.md` |
| **4** | **El bot en NinjaTrader** | 🔵 declarada, **sin definir** | `FASES.md` |

➡️ **Antes de tocar nada del portal, lee `04_Web\ESTADO_FASE_2.md`:** dice qué hay hecho, qué falta, por dónde va la revisión del operador y qué errores ya se pagaron una vez.

🔵 **Las fases 3 y 4 están declaradas, no definidas.** El operador las detallará más adelante. **No deduzcas su alcance ni empieces a construirlas**; lo poco que consta está en `FASES.md`. El portal se publica en https://plan-operativo-nq.pages.dev

**Operador:** Christian. **Uso:** personal.
**Repositorio:** `kristeb-trader/Trading_Plan` — **privado, y se queda privado**.

---

## 🔴 Reglas del proyecto — no negociables

1. **No inventes metodología.** Ninguna regla, umbral o comportamiento sale de price action genérico ni de lo que "suele hacerse". Todo lo que hay está en `01_Plan\`. Si algo falta, **falta**: se marca `PENDIENTE`, no se rellena.
2. **Ningún adjetivo es una regla.** "Fuerte", "sano", "claro" no son criterios. Solo valen ticks, puntos, porcentajes, número de velas y horas exactas.
3. **No se cambia una regla confirmada** sin pedírselo al operador y esperar su confirmación explícita.
4. **Los scripts de `05_Backtesting\` son herramientas de auditoría**, nunca de operación. No los conviertas en un bot ni en un ejecutor. *(La fase 4 será un bot, sí — pero se definirá y se construirá cuando el operador la abra, no antes y no reciclando estos scripts por su cuenta.)*
5. **Los huecos declarados se muestran, no se esconden.** *(Desde el 02/09/2026 se muestran en la **portada técnica**, no en la de Alfredo. Cambian de sitio, no desaparecen — ver más abajo.)*
6. **`01_Plan\` no se toca desde ninguna otra fase.** Es la base con la que se construirá el bot: el portal lo lee y lo presenta, el backtesting lo audita, pero **nadie lo reescribe**. Si hay que cambiar una regla, se cambia en `01_Plan\` y con el visto bueno del operador.

---

## Fuentes de verdad

| Archivo | Qué es |
|---|---|
| `01_Plan\reglas.json` | **la fuente de verdad legible por máquina.** 38 reglas con id, categoría, enunciado, condiciones medibles, acción, excepciones, prioridad y estado. **El portal se construye contra este archivo.** |
| `01_Plan\TRADING_PLAN_CHAUMER.md` | el texto largo: razonamiento, casos reales y por qué cada regla dice lo que dice |
| `01_Plan\PARAMETROS.md` | los números que pueden cambiar, en un solo sitio. Las reglas citan el **nombre** del parámetro, no el valor |
| `01_Plan\GLOSARIO.md` | vocabulario medible: **23 encabezados** de término *(rompimiento y consecución comparten uno, de ahí el «24» de otros documentos)* |
| `01_Plan\CHECKLIST_DIARIA.md` | la secuencia real del día en 4 bloques |
| `01_Plan\GALERIA.md` | 21 casos reales etiquetados |
| `01_Plan\PENDIENTES.md` | lo que sigue abierto |
| `01_Plan\CONTEXTUALIZACION.md` | 10 elementos que **NO son reglas y no deben convertirse en reglas** |
| `01_Plan\ESTADO.md` | registro cronológico de toda la fase 1 |
| `01_Plan\CIERRE_FASE_1.md` | **léelo primero.** Qué está probado y qué no |

Si `reglas.json` y un `.md` se contradicen, **para y pregunta**. No elijas tú.

---

## 🚨 Los cuatro huecos declarados — dónde se muestran

El plan está **escrito y contrastado**, pero **no probado**. Cuatro cosas faltan y el portal no puede presentarse como si estuvieran:

1. **El test ciego nunca se ejecutó** (`F1.11`, `P-29`). No hay medida de si el documento se sostiene solo, sin el operador corrigiendo al lado.
2. **No hay regla de parada** (`P-21`). El plan no dice cuándo se deja de operar en la semana o el mes. Cada operación arriesga el 5,3 % de la cuenta objetivo.
3. **Falta la capa de contextualización.** En las sesiones grabadas decidió 2 de 4 días de "hoy no opero". Un ejecutor puramente mecánico operará días que el operador no operaría.
4. **Las cifras del backtesting no miden la estrategia** (`P-27`): 9 operaciones, reglas que cambiaron durante la propia revisión, sin filtro de noticias rojas y sin capa de contexto.

> Si el portal muestra el resultado del backtesting (−91,00 pts en 9 operaciones), **debe mostrar estos motivos en la misma pantalla**.

### Dónde viven — corregido por el operador el 02/09/2026

Los cuatro huecos y el aviso de «no probado» **salieron de la portada de Alfredo
y viven en la portada técnica** (`/tecnico`), junto al resultado del backtesting
y en la misma pantalla que sus motivos.

**La razón del operador:** lo que no está probado es **la transcripción del
método, no el método de Alfredo**. Repetírselo cuatro veces antes de que lea una
sola regla no le sirve de nada y le pone en duda su propio trabajo.

**Lo que sigue en pie:** se muestran enteros, sin recortar y sin letra pequeña.
Lo que cambió es **a quién**, no si se enseñan.

---

## Qué es el portal de la fase 2 — decidido por el operador el 31/08/2026

**No es una herramienta de operación.** Es la página donde **Alfredo Chaumer revisa las reglas** que se extrajeron de su metodología y **deja observaciones escritas** para que el operador las lea después. No se usa mientras se opera.

| | |
|---|---|
| Dónde vive | **internet**, en Cloudflare Pages |
| Quién entra | el operador y Alfredo, por **lista blanca de correo** (Cloudflare Access) |
| Qué hace | lectura del plan **+ observaciones que se guardan** en Supabase |
| Qué se comparte | **la dirección del portal**, nunca el repositorio |

**Dos puntos del brief original quedaron derogados por el operador:** el módulo ya no es 100 % estático *(las observaciones necesitan persistencia)*, y el portal se publica ya *(con puerta, porque su razón de ser es que Alfredo entre)*.

**Lo que NO queda derogado y se cumple al pie de la letra:** ninguna escritura desde el cliente y **ninguna clave en el paquete que descarga el navegador**. El navegador nunca habla con Supabase: habla con una función de Cloudflare que comprueba la identidad y escribe. Sin la puerta configurada, **no se despliega**.

> 🔴 **Una observación de Alfredo no es una regla.** El plan solo cambia si el operador cambia `01_Plan\`. El portal deja constancia; no toca la fuente.

### Dos portadas — decidido el 02/09/2026

| | La de Alfredo (`/`) | La técnica (`/tecnico`) |
|---|---|---|
| Menú | inicio, los ocho módulos, casos reales, observaciones | todo lo anterior **+ «Todo el detalle»** |
| Buscador | **no existe**, ni con `Ctrl+K` | sí |
| Códigos de regla | no | sí |
| Vocabulario, parámetros, las 38 fichas, checklist, pendientes, contextualización, acta de cierre | no | sí |
| «Plan no probado» y los cuatro huecos | no | **sí, enteros** |

Se entra a la técnica por un **icono pequeño y apagado al pie del menú**, que además
enciende el modo técnico. Alfredo no tiene por qué tropezar con él.

Estado y seguimiento en **`04_Web\ESTADO_FASE_2.md`**, que manda sobre todo lo demás de esa carpeta. El diseño de partida está en `DISENO_PORTAL.md`; el brief y el guion de arranque son **anteriores** a la redefinición del portal y se conservan solo como historia.

---

## Estándar visual — ya fijado por el operador, respétalo

Viene de las gráficas de backtesting que él validó una por una.

| | |
|---|---|
| Fondo | negro / muy oscuro (`#0B0E14`) |
| Cuadrícula | **ninguna**. Sí la línea del eje horizontal sobre las horas y la vertical junto a los precios (`#3A4256`) |
| Velas | 🔵 **azul `#2E86FF` = alcista** · ⬜ **blanca `#FFFFFF` = bajista** |
| Zonas | **todas del mismo gris `#8B93A7`**, sin distinguir soporte de resistencia por color |
| Corridas y retrocesos | **línea blanca en zigzag** uniendo cada extremo |
| La operación | franja roja tenue de la entrada al stop, franja verde tenue de la entrada al objetivo, **solo sobre el tramo de la operación**, no en todo el ancho |
| Líneas de entrada / stop / objetivo | **no se dibujan.** Con las franjas ya se sabe dónde están. Cuanto más limpio, mejor |
| Corte del gráfico | se marca hasta la vela del **llenado**; después solo siguen las velas hasta el resultado. Solo llega a las 10:30 si no hubo setup |
| Otros colores | oro `#F5C542` · rojo `#FF5C5C` · verde `#4ADE80` · cian `#22D3EE` |

**Nada de tablas de datos donde quepa una gráfica.** El operador lo pidió explícitamente.

---

## Lenguaje visual

| | |
|---|---|
| **Dónde viven los tokens** | `04_Web\src\estilos\tokens.css` — **único sitio con valores literales** |
| **Estilos de documento** | `04_Web\src\estilos\base.css` |
| **De dónde salen los colores** | de la tabla del estándar visual de arriba. **No se eligen, se heredan** |
| **Tema** | uno solo, oscuro. No hay tema claro y no se finge que lo haya |

**La regla:** si escribes un color, un radio, una sombra, un espaciado o un tamaño de fuente que **no sale de un token**, estás creando un segundo lenguaje visual. Se añade el token; no se pone el valor suelto. Excepción legítima: un valor que de verdad solo tiene sentido en un sitio, con un comentario que diga por qué.

**Dónde se aplica cada regla — corregido el 01/09/2026:**

| | Dentro de una gráfica | En el marco del portal |
|---|---|---|
| Degradados y sombras | **prohibidos** — manda el estándar de arriba | **permitidos, muy sutiles**: es lo que da volumen y aspecto moderno |
| Cuadrícula | **prohibida** | no aplica |
| Emojis decorativos | prohibidos | prohibidos *(los del texto fuente sí se respetan: son del documento)* |

El operador pidió explícitamente una estética moderna para el portal. El estándar de gráficas **no cambia**: nace de las gráficas de backtesting que validó una por una y se respeta al pie de la letra allí donde se dibuje una.

**Escritorio primero.** El portal se usa en computador: barra lateral fija con las secciones agrupadas. Por debajo de 900 px pasa a barra superior. Funciona en móvil, pero el móvil no manda las decisiones.

**El rojo no es para avisar.** Queda reservado a un dato negativo real (el resultado del backtesting). El aviso de *«plan no probado»* va en **oro**, que es advertencia, no error.

**Además:** columnas numéricas siempre con `tabular-nums`; las tablas anchas hacen scroll dentro de su contenedor y la página nunca en horizontal; el color nunca comunica solo —siempre acompañado de texto, forma o icono—; y foco visible en todo lo que se pueda tabular.

---

## Cómo hablarle al operador

- **Nunca uses los códigos de regla** (`R-08`, `P-22`, `G-12`…) en conversación. Son para los documentos. Al hablar, lenguaje de usuario, claro y no técnico.
- Máximo **2 preguntas por turno**.
- Él corrige vela a vela. **Nada se da por bueno sin su visto bueno explícito.**
- Tiene contacto directo con Alfredo Chaumer y le consulta cuando algo se traba.

---

## Vocabulario mínimo

**corrida / impulso** · **retroceso** · **zona** (soporte o resistencia) · **rompimiento** (pasar 1 tick del borde; **la mecha basta, el cierre da igual**) · **consecución** (la vela que confirma el rompimiento pasando del extremo de la vela que rompió) · **traspaso** (rompimiento + consecución: recién ahí la zona quedó superada) · **zona apéndice** (nace cuando pasan 5 velas sin consecución y el rompimiento fue con cuerpo) · **IRI** (entrada de continuación) · **Reingreso** (entrada tras una consecución fallida, y es **inmediata o no es**) · **punto de referencia** · **inversión de papel** (la zona superada cambia de soporte a resistencia o al revés) · **banda entre zonas** (una sola zona por banda y por jornada).

Definiciones completas y medibles en `01_Plan\GLOSARIO.md`.

---

## Datos y motor

- Datos: `05_Backtesting\datos\NQ 09-26.Last.txt` — formato `yyyyMMdd HHmmss;o;h;l;c;v`, **en UTC**.
- **Horario:** el ancla es la **apertura americana — 09:30–11:30 ET**, nunca el número del reloj. El gráfico del operador va en hora Colombia (UTC−5 fijo), así que en pantalla la ventana es **08:30–10:30 Col en verano NY** y **09:30–11:30 Col en invierno NY**. La primera vela de la ventana es la **08:31**.
  > ⚠️ **La equivalencia en UTC se desplaza una hora el 1 de noviembre de 2026.** Hasta esa fecha, 13:30–15:30 UTC; desde el 2 de noviembre, 14:30–16:30 UTC. No la escribas fija en ningún sitio: calcúlala desde la apertura americana.
- `05_Backtesting\lector.py` · `motor.py` · `dia.py` · `dibujo.py` — motor de marcado de zonas, detección de setups y generación de la gráfica estándar.
  > Python **ya está instalado** (3.13, comprobado el 2026-09-02). Hasta el 01/09 no estaba en el PATH; esa nota queda derogada.

Los dos son **auditoría**. Sirven para verificar el plan, no para operar.

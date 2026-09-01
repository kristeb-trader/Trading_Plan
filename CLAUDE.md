# Proyecto Chaumer — instrucciones para Claude Code

**Qué es esto:** la metodología de trading de Alfredo Chaumer para NQ/MNQ en NinjaTrader 8, extraída durante la fase 1 a un plan mecánico de **38 reglas medibles**.

**Fase actual:** 🚧 **FASE 2 — construir el portal web** en `04_Web\` (hoy vacía).
**Fase 1:** 🏁 cerrada el 2026-09-01. Ver `01_Plan\CIERRE_FASE_1.md`.

**Operador:** Christian. **Uso:** personal.

---

## 🔴 Reglas del proyecto — no negociables

1. **No inventes metodología.** Ninguna regla, umbral o comportamiento sale de price action genérico ni de lo que "suele hacerse". Todo lo que hay está en `01_Plan\`. Si algo falta, **falta**: se marca `PENDIENTE`, no se rellena.
2. **Ningún adjetivo es una regla.** "Fuerte", "sano", "claro" no son criterios. Solo valen ticks, puntos, porcentajes, número de velas y horas exactas.
3. **No se cambia una regla confirmada** sin pedírselo al operador y esperar su confirmación explícita.
4. **Los scripts de `05_Backtesting\` son herramientas de auditoría**, nunca de operación. No los conviertas en un bot ni en un ejecutor.
5. **Los huecos declarados se muestran, no se esconden.** Ver más abajo.

---

## Fuentes de verdad

| Archivo | Qué es |
|---|---|
| `01_Plan\reglas.json` | **la fuente de verdad legible por máquina.** 38 reglas con id, categoría, enunciado, condiciones medibles, acción, excepciones, prioridad y estado. **El portal se construye contra este archivo.** |
| `01_Plan\TRADING_PLAN_CHAUMER.md` | el texto largo: razonamiento, casos reales y por qué cada regla dice lo que dice |
| `01_Plan\PARAMETROS.md` | los números que pueden cambiar, en un solo sitio. Las reglas citan el **nombre** del parámetro, no el valor |
| `01_Plan\GLOSARIO.md` | 24 términos con definición medible |
| `01_Plan\CHECKLIST_DIARIA.md` | la secuencia real del día en 4 bloques |
| `01_Plan\GALERIA.md` | 21 casos reales etiquetados |
| `01_Plan\PENDIENTES.md` | lo que sigue abierto |
| `01_Plan\CONTEXTUALIZACION.md` | 10 elementos que **NO son reglas y no deben convertirse en reglas** |
| `01_Plan\ESTADO.md` | registro cronológico de toda la fase 1 |
| `01_Plan\CIERRE_FASE_1.md` | **léelo primero.** Qué está probado y qué no |

Si `reglas.json` y un `.md` se contradicen, **para y pregunta**. No elijas tú.

---

## 🚨 Los cuatro huecos declarados — el portal debe mostrarlos

El plan está **escrito y contrastado**, pero **no probado**. Cuatro cosas faltan y el portal no puede presentarse como si estuvieran:

1. **El test ciego nunca se ejecutó** (`F1.11`, `P-29`). No hay medida de si el documento se sostiene solo, sin el operador corrigiendo al lado.
2. **No hay regla de parada** (`P-21`). El plan no dice cuándo se deja de operar en la semana o el mes. Cada operación arriesga el 5,3 % de la cuenta objetivo.
3. **Falta la capa de contextualización.** En las sesiones grabadas decidió 2 de 4 días de "hoy no opero". Un ejecutor puramente mecánico operará días que el operador no operaría.
4. **Las cifras del backtesting no miden la estrategia** (`P-27`): 9 operaciones, reglas que cambiaron durante la propia revisión, sin filtro de noticias rojas y sin capa de contexto.

> Si el portal muestra el resultado del backtesting (−91,00 pts en 9 operaciones), **debe mostrar estos motivos en la misma pantalla**.

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
- **Horario:** el gráfico del operador es hora Colombia (UTC−5). Ventana operativa **08:31–10:30 Col = 13:31–15:30 UTC**.
- `05_Backtesting\lector.py` — el motor que reproduce el marcado de zonas y detecta los setups.
- `05_Backtesting\dia.py` — genera la gráfica estándar de una jornada.

Los dos son **auditoría**. Sirven para verificar el plan, no para operar.

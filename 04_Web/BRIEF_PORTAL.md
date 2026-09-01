# BRIEF DEL PORTAL — Fase 2

**Fecha:** 2026-09-01 · **Actualizado:** 2026-09-01, tras la decisión del operador del 31/08.
**Estado:** punto de partida. La especificación viva es `DISENO_PORTAL.md`.
**Antes de leer esto:** `..\01_Plan\CIERRE_FASE_1.md` y `..\CLAUDE.md`.

> ⚠️ **Este documento se escribió antes de que el operador redefiniera el portal.** Se ha corregido en los puntos que quedaron obsoletos. **Donde este brief y `DISENO_PORTAL.md` se contradigan, manda el diseño.**

---

## Para qué es el portal

Para que **Alfredo Chaumer revise las reglas** que se extrajeron de su metodología y **deje observaciones escritas** que el operador lea después.

No es una web de marketing, no es un curso y no es un bot. **Tampoco es una herramienta de operación: no se usa mientras se opera.** Es la mesa de revisión del plan.

> El plan ya existe y está escrito. El portal **no añade metodología**: la hace consultable, revisable y comentable.

**Corregido el 31/08/2026.** La versión anterior decía que el portal servía *"para que el operador ejecute el plan sin decidir nada, en su escritorio, mientras opera"*. Ya no: eso lo decidió el operador al abrir el portal a Alfredo.

---

## Lo que el portal tiene que resolver, en orden de importancia

*(Orden corregido el 31/08: al dejar de ser herramienta de operación, la checklist deja de ser la función principal y las reglas pasan a serlo.)*

### 1 · Las 38 reglas, consultables y comentables
Construidas **desde `reglas.json`**, no copiadas a mano. Buscables, filtrables por categoría, enlazadas entre sí y con el glosario. Cada regla con sus condiciones medibles y, cuando exista, el caso real que la fijó. **Y con la caja donde Alfredo deja su observación sobre esa regla.**

### 2 · La secuencia del día, como documento
`CHECKLIST_DIARIA.md` renderizada: cuatro bloques —antes de abrir NinjaTrader · premercado · ventana operativa · después del llenado— en su orden real, en una vista imprimible.

Los tres filtros que pueden anular una entrada son el tope de stop, que el objetivo esté libre de zonas, y —solo en Reingreso— el punto de referencia. **Se muestran; el portal no los comprueba ni acompaña la operativa en vivo.**

### 3 · Los parámetros en un solo sitio
Los números que pueden cambiar viven en `PARAMETROS.md` y las reglas los citan **por nombre, no por valor**. El portal debe respetar eso: cambiar el tope de stop en un sitio y que se propague a todo.

### 4 · La galería de casos
21 casos reales etiquetados, con su gráfica. Es el material con el que el operador entrena el ojo y con el que se resuelven las dudas de marcado.

### 5 · Lo que está abierto, visible
`PENDIENTES.md` y los cuatro huecos declarados. **No como letra pequeña.**

---

## 🚨 Cuatro cosas que el portal NO puede hacer

1. **No puede presentar el plan como probado.** No pasó el test ciego. Si hay una portada o un resumen, esto va ahí.
2. **No puede mostrar el resultado del backtesting sin sus advertencias.** −91,00 pts en 9 operaciones no mide la estrategia: las reglas cambiaron durante la propia revisión, no hubo filtro de noticias rojas y falta la capa de contexto. Los cuatro motivos, en la misma pantalla que la cifra.
3. **No puede convertir en regla nada de `CONTEXTUALIZACION.md`.** Esos diez elementos están fuera del plan a propósito, porque no tienen número. Pueden mostrarse **como recordatorio de criterio**, nunca como condición automática.
4. **No puede mandar órdenes ni conectarse a la cuenta.** El portal acompaña la decisión; no la ejecuta.

---

## Estándar visual

Está fijado en `..\CLAUDE.md` y viene de las gráficas que el operador ya validó una por una: fondo negro, sin cuadrícula, velas azul/blanca, zonas todas del mismo gris, zigzag blanco, franjas roja y verde solo sobre el tramo de la operación, y **sin líneas de entrada, stop ni objetivo**.

Dos frases suyas que valen como criterio de diseño:

> *"Entre más limpio sea el gráfico, mucho mejor."*
> *"Nada de tablas de datos. Solo gráficas."*

---

## Las cinco decisiones — ✅ contestadas por el operador el 31/08/2026

| # | Decisión | Respuesta |
|---|---|---|
| 1 | ¿Portal local, o accesible desde fuera? | **En internet**, Cloudflare Pages, con puerta de Access y lista blanca de correo |
| 2 | ¿Lo consulta **mientras** opera? | **No.** Antes y después. No es herramienta de operación |
| 3 | ¿La bitácora se escribe en el portal? | **No.** Sigue donde está hoy |
| 4 | ¿Lee los datos de NinjaTrader? | **No.** Ningún dato de NT8. Solo reglas |
| 5 | ¿Genera las gráficas de backtesting? | **No genera nada.** La galería muestra las 21 imágenes que ya existen |

Y una decisión que no estaba en la lista: **las observaciones de Alfredo se guardan en Supabase**, escritas por un servidor de Cloudflare que valida la identidad — nunca por el navegador.

---

## Lo que queda pendiente de la fase 1 y puede volver

- **El test ciego** (`P-29`). Se puede ejecutar **contra el portal**: dar diez gráficos sin etiquetar a alguien que solo tenga el portal delante y comparar. Sería la mejor prueba posible de que el portal funciona.
- **La regla de parada** (`P-21`). Cuando exista, entra en los parámetros.
- **La capa de contextualización.** Es una fase propia, aplazada por el operador.
- Seis dudas abiertas: zona estirada, alcance del FOMC, calendario de noticias rojas, separación mínima entre zonas del mismo tipo, vela de apertura sin cuerpo, y si sobra una regla.

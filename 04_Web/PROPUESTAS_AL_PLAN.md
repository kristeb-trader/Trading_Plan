# Propuestas al plan

`01_Plan\` es de **solo lectura** desde la fase 2. Lo que aparezca mal o
incoherente al construir el portal se anota aquí y lo decide el operador.

**Nada de este archivo se aplica solo.** Se aplica cuando él lo confirma, y
entonces se marca como resuelto con la fecha.

---

## Abiertas

### 1 · En la regla del retroceso quedó una medida con la definición vieja del stop

**Encontrado:** 2026-09-04, al releer el plan tras la limpieza a v2.3.
**Dónde:** `01_Plan\reglas.json`, regla del retroceso (`R-11`), condición
`tamano_maximo`.

Dice:

> `240 ticks entre entrada y nivel de referencia (R-08)`

En esa misma regla, las dos condiciones de arriba ya llevan el aviso nuevo —
*«esto define el RETROCESO, no el stop»*— y su `accion` remite a `R-24`. Pero
`tamano_maximo` sigue midiendo el tope contra el **nivel de referencia del
retroceso**, que es justo la definición que se corrigió.

La regla del filtro de riesgo (`R-08`), ya alineada el 04/09/2026, dice que la
distancia se mide **entre la entrada y el stop estructural de `R-24`** — el
extremo alcanzado desde que nació la zona hasta la vela de rompimiento.

**Por qué importa:** con zonas que aguantan muchas velas los dos puntos no
coinciden, y el caso real del 7/07/2026 que cita `R-24` es exactamente eso:
71,50 pts con la medida vieja (la entrada pasaba) frente a 86,25 con la
correcta (queda descartada por el tope). Medido contra el retroceso, el filtro
deja pasar entradas que el plan quiere descartar.

**Propuesta:** que `tamano_maximo` diga lo mismo que `R-08` — *240 ticks entre
la entrada y el stop estructural de `R-24`*.

**Efecto en el portal:** ninguno hoy. El portal no muestra esa condición; se
anota para que las dos reglas digan lo mismo.

**Estado:** 🟡 pendiente de que lo decida el operador.

---

### 2 · «IRI» en el plan, «Continuación» en la pantalla

**Encontrado:** 2026-09-09, al construir la bitácora de backtesting.
**Dónde:** `01_Planeglas.json` y `01_Plan\GLOSARIO.md`, en todo lo que
nombra el setup de continuación.

El operador pidió el 09/09/2026 que en el portal el setup deje de llamarse
**IRI** y pase a llamarse **Continuación**, y dijo que de ahí en adelante se
hable así. La bitácora ya lo escribe y lo guarda así (`continuacion`).

**El plan NO se ha tocado:** sigue diciendo IRI en las reglas, en el glosario y
en el vocabulario del proyecto. Ahora mismo conviven las dos palabras — una en
los documentos, otra en la pantalla.

**Por qué no es un invento:** el vocabulario del proyecto ya define IRI como
*continuación*. No se está renombrando un concepto, se está eligiendo cuál de
sus dos nombres se enseña.

**Propuesta:** que el operador decida entre las dos salidas.

1. **Renombrar en el plan.** IRI pasa a Continuación en `reglas.json`, en el
   glosario y en el vocabulario, dejando IRI escrito como nombre anterior para
   que los documentos viejos sigan entendiéndose.
2. **Dejarlo como está.** IRI es el nombre del plan y Continuación es cómo se
   enseña. Entonces conviene que el glosario lo diga con esas palabras, para
   que nadie crea que son dos cosas.

Mientras no lo decida, **el que manda es el plan**: IRI.

---

## Resueltas

*(vacío)*

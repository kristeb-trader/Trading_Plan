# 02 · Marcación de zonas

> Dirección: `/zonas`
> Corrige el texto libremente. **No borres ni cambies las líneas `<!-- id: … -->`**:
> son las que dicen a qué parte de la página vuelve cada bloque.

<!-- id: cabecera -->

## Marcación de zonas

Qué es una zona, de qué vela sale y cómo se dibuja

---

<!-- id: movimiento -->

### Corrida y retroceso

El mercado solo hace dos cosas: avanza un movimiento y después se para a descansar. Al movimiento que avanza se le llama **corrida**. Al descanso, **retroceso**. No hay un tercer estado, y esta pareja es la que deja todas las zonas del día.

> 🖼 **Gráfico.** Texto alternativo: Un movimiento alcista real separado en su corrida y su retroceso
> Pie: Movimiento alcista: la corrida sube y el retroceso baja. La resistencia sale de la vela más alta de la corrida.

> 🖼 **Gráfico.** Texto alternativo: El mismo mecanismo en un movimiento bajista real
> Pie: El mismo mecanismo hacia abajo: la corrida baja y el retroceso sube. El soporte sale de la vela más baja.

- **Cuándo nace una corrida** — Cuando una vela supera el extremo de la anterior
- **Mientras vive** — Cada vela respeta el extremo contrario de la anterior. Si empatan, sigue viva
- **Cuándo muere** — En la primera vela que va en contra, aunque sea 1 tick
- **Cuántas velas dura** — Mínimo dos. Máximo, ninguno
- **El color de la vela** — No importa en absoluto
- **Una vela dentro de la anterior** — No corta la corrida

La vela que mata la corrida **ya es la primera del retroceso**. No hay hueco entre una cosa y la otra: el movimiento cambia de fase en esa misma vela.

> **[REGLA DURA]**
> **Un retroceso no tiene tamaño mínimo ni máximo de velas.** Puede ser una sola vela. No se descarta un movimiento por parecer demasiado corto o demasiado largo.

Del retroceso interesa un punto concreto: **su extremo** — el más bajo si la corrida era alcista, el más alto si era bajista. Ahí irá el stop cuando llegue el momento, y ese punto reaparece en casi todas las decisiones que vienen después.

---

<!-- id: nace -->

### De dónde sale la zona

Cuando una corrida termina, deja un rastro en el gráfico: una franja de precio que se llama zona. No se dibuja a ojo. Sale siempre de la misma vela y con los mismos límites.

> 🖼 **Gráfico.** Texto alternativo: La vela designada de un movimiento y los dos bordes exactos de la zona
> Pie: La vela designada y sus dos bordes: del borde del cuerpo a la punta de la mecha. Ni un tick más, ni un tick menos.

1. **Se busca la vela designada**: la del máximo más alto si la corrida fue alcista, la del mínimo más bajo si fue bajista. Se busca desde el origen de la corrida hasta la vela que disparó el retroceso, **esa incluida**.
2. **Se dibuja del borde del cuerpo a la punta de la mecha** de esa vela. Ese es todo el criterio.
3. **Se extiende hacia la derecha**, a lo largo del gráfico.

> 🖼 **Gráfico.** Texto alternativo: La zona ya dibujada y extendida hacia la derecha sobre una sesión real
> Pie: Ya extendida: el rectángulo se dibuja desde la vela de origen, no desde donde el precio vuelva más tarde.

- **Corrida alcista** — Deja **resistencia** arriba
- **Corrida bajista** — Deja **soporte** abajo
- **Y su retroceso** — El retroceso de una corrida alcista deja **soporte**; el de una bajista, resistencia
- **Vela sin mecha** — La zona es una línea en el extremo de la vela
- **Vela sin cuerpo** — Apertura y cierre coinciden: de ese precio a la punta de la mecha
- **Una vela con máximo mayor y mínimo menor** — El orden dentro de la vela decide cuál sostiene la zona

#### Cuándo se dibuja cada una

Las dos zonas de un movimiento no nacen a la vez, y confundirlo lleva a operar algo que todavía no existe:

> **[FICHA]**
> #### La zona de la corrida
> Se dibuja **en cuanto aparece el retroceso**, en vivo. Ya se puede operar.

> **[FICHA]**
> #### La zona del retroceso
> Mientras el retroceso vive es solo una **línea provisional** que se mueve con cada vela. Se convierte en zona cuando aparece el movimiento contrario.

> **[NO SE HACE]**
> **Una línea provisional no opera.** No admite rompimiento, ni consecución, ni reingreso. Hasta que no es zona, no existe para el método.

---

<!-- id: consecucion -->

### Rompimiento y consecución

Superar una zona son dos cosas, no una. Primero el rompimiento, después la consecución. Y el mismo mecanismo que supera una zona es el que más tarde dispara la entrada.

> 🖼 **Gráfico.** Texto alternativo: La vela que pasa el borde de la zona y la que después pasa de su extremo
> Pie: Las dos velas del traspaso sobre una sesión real: la que rompe, y la consecución que pasa de su extremo.

> **[FICHA]**
> #### Rompimiento
> El precio pasa el borde de la zona por al menos **un tick**.
> Basta la mecha. **El cierre da igual.**

> **[FICHA]**
> #### Consecución
> Una vela posterior pasa por un tick el **extremo de la vela que rompió**.
> Recién ahí la zona quedó traspasada.

#### Dos maneras de romper

El cierre no decide si hay rompimiento, pero sí deja un rastro distinto. Esa diferencia no se nota hoy: se nota en los dos apartados siguientes, si la consecución no llega.

> 🖼 **Gráfico.** Texto alternativo: Una vela que pasa el borde con la mecha y cierra dentro de la zona
> Pie: Rompimiento con mecha: la vela pasa el borde pero cierra dentro de la zona. Sigue siendo rompimiento.

> 🖼 **Gráfico.** Texto alternativo: Una vela que pasa el borde y cierra fuera de la zona
> Pie: Rompimiento con cuerpo: la vela cierra al otro lado del borde.

> **[REGLA DURA]**
> **Un rompimiento solo, sin consecución, no invalida nada.** La zona sigue viva y sigue contando para todo.
> Y la vela que da la consecución de un traspaso no abre a la vez el rompimiento del lado contrario: eso se busca a partir de la siguiente.

La consecución puede tardar. Para traspasar una zona **no hay plazo**: el rompimiento queda pendiente indefinidamente y la consecución lo cierra cuando llegue. El plazo de 5 velas que viene a continuación gobierna otra cosa: la forma de la zona y la vida de la orden.

---

<!-- id: estira -->

### Cuando no llega la consecución

Si el precio rompe una zona y pasan 5 velas sin que llegue la consecución, la zona cambia de forma. Qué le pasa depende de cómo rompió aquella vela.

> 🖼 **Gráfico.** Texto alternativo: Una vela cruza la zona y ninguna de las siguientes supera su extremo
> Pie: El caso más común: la vela cruza la zona, pero ninguna de las siguientes pasa de su extremo. No hubo traspaso y la zona sigue viva.

Cuando el rompimiento fue **con la mecha** —el cierre se quedó dentro— la zona **se estira** hasta la punta de esa mecha. El otro borde no se mueve. Sigue habiendo una sola zona, más grande, y conserva su historial.

- **Qué lo dispara** — Rompimiento con mecha **+ 5 velas** sin consecución
- **Nuevo límite** — La punta de la mecha de la vela que rompió
- **El borde opuesto** — No se mueve
- **Zonas resultantes** — 1, más grande

> **[REGLA DURA]**
> **Las 5 velas son un tope, no una espera obligatoria.** Si antes de que se cumplan aparece un retroceso nuevo, se marca zona en ese momento y no se espera más.
> Actúa lo que llegue primero.

Con una salvedad: el único retroceso que *no* cuenta como estructura nueva es el que quedó bloqueado por la regla de la mitad entre zonas. Si es ese, el reloj de las 5 velas sigue corriendo.

---

<!-- id: apendice -->

### La zona apéndice

Es el otro desenlace del mismo plazo. Si la vela que rompió lo hizo **con el cuerpo** —cerró fuera de la zona— y pasan 5 velas sin consecución, no se estira nada: **nace una zona nueva**, pegada a la anterior. Se llama zona apéndice.

> 🖼 **Gráfico.** Texto alternativo: Rompimiento con cuerpo sin consecución: la zona original y la apéndice que nace bajo ella
> Pie: La original se queda intacta y la apéndice se marca sobre la mecha de la vela que rompió. Ahora hay dos.

- **Qué lo dispara** — Rompimiento con cuerpo **+ 5 velas** sin consecución
- **La zona original** — No se modifica
- **Un borde de la apéndice** — El borde del cuerpo de la vela que rompió
- **El otro borde** — El extremo de su mecha
- **Zonas resultantes** — 2: la original y su apéndice

> 🖼 **Gráfico.** Texto alternativo: Otro caso real de zona apéndice sobre la mecha de la vela de rompimiento
> Pie: Otro caso real: la apéndice ocupa exactamente la mecha que sobresalió, nada más.

> **[REGLA DURA]**
> **La apéndice no nace por acción del precio sobre ella.** No es una zona más que apareció: es el rastro de un rompimiento que se quedó sin consecución.

> **[NO SE HACE]**
> **Cómo se entra sobre una zona apéndice está pendiente.** El plan la marca y la mantiene, pero las reglas de entrada asociadas todavía no están cerradas. Hasta que lo estén, no se deduce nada.

---

<!-- id: convivencia -->

### Varias zonas a la vez

En una jornada aparecen muchas zonas candidatas. Tres reglas evitan que el gráfico se llene de rectángulos y que se acabe operando ruido.

#### Si se tocan, se funden

Si la zona que se iba a marcar toca una que ya existe —basta que se rocen los bordes— **no se crea una nueva**: se estira la que ya estaba hasta el extremo nuevo. El otro borde no se mueve, no se engloba nada, y la zona conserva su historial de rompimientos y consecuciones.

> 🖼 **Gráfico.** Texto alternativo: Dos zonas que se tocan y quedan convertidas en una sola, estirada
> Pie: No quedan dos zonas pegadas: queda una sola, estirada hasta el extremo nuevo.

Si la candidata cae entera dentro de la existente, no hay nada que hacer: no se toca nada. Y dos zonas de tipo distinto no se solapan mientras una esté viva: una zona viva ocupa su franja de precio.

#### Entre dos zonas, solo si no cruza la mitad

Cuando hay una zona por arriba y otra por abajo, se calcula el punto medio entre sus bordes internos. Solo se marca zona nueva si el movimiento que la genera **se queda entero de un lado** de esa mitad.

> 🖼 **Gráfico.** Texto alternativo: Una zona marcada entre otras dos, con la mitad de la banda señalada
> Pie: El movimiento entero se queda del lado en el que empezó. Por eso esta zona sí se marca.

> **[REGLA DURA]**
> **Lo que se mide es el recorrido del precio, no el rectángulo.** Si el movimiento cruzó la mitad en algún punto, no se marca — aunque la caja de la zona quede entera a un lado.

La mitad se recalcula cada vez, contra la zona más cercana por arriba y la más cercana por abajo *en ese momento*. No hay límite de zonas intermedias en una jornada. Pasa poco, pero pasa.

#### Una sola por franja y por jornada

La franja entre dos zonas admite **una zona en todo el día**, y el turno lo resuelve el primer retroceso que aparezca dentro. Si ese primero respeta la mitad, se marca; si no la respeta, no se marca. En los dos casos **la franja queda cerrada** para el resto de la jornada, y no se reabre aunque las zonas que la formaban se mueran.

Cualquier zona viva sirve de borde de la franja, incluidas las que se marcaron de madrugada por volumen.

> **[NO SE HACE]**
> **Salir de una zona es rompimiento y consecución, no geometría.** Mientras un rompimiento espera su consecución, no se marca zona al otro lado de esa zona.

---

<!-- id: caduca -->

### Cuándo deja de contar

Una zona muere cuando ha sido superada **en las dos direcciones**: rompimiento y consecución hacia un lado, y rompimiento y consecución hacia el otro.

> 🖼 **Gráfico.** Texto alternativo: Una zona traspasada primero hacia un lado y después hacia el otro
> Pie: Traspasada en los dos sentidos. A partir de ahí no bloquea ni sirve para entrar.

- **Solo rompimiento, sin consecución** — La zona sigue vigente. No ha pasado nada
- **Superada en un solo sentido** — Sigue viva. Cambia de papel: el soporte pasa a resistencia y al revés
- **Superada en los dos** — **No cuenta para nada.** Ni bloquea un objetivo, ni sirve para entrar, ni cuenta para medir la mitad entre zonas
- **En pantalla** — Se deja dibujada en tono muy tenue, solo como recuerdo

Esa distinción importa más de lo que parece: una zona que sigue viva puede impedir una entrada perfectamente válida, porque se cruza en el camino del objetivo.

---

<!-- id: flujo -->

### El recorrido completo

Todo lo anterior, en el orden en que ocurre en el gráfico. Cada paso es una de las reglas de este módulo.

Una **corrida** avanza y muere en la primera vela que va en contra. Esa vela ya es el **retroceso**.

Al aparecer el retroceso se marca la **zona** sobre la vela designada, del borde del cuerpo a la punta de la mecha, y se extiende hacia la derecha.

¿Toca una zona que ya existe? Entonces **no nace una nueva**: se estira la que estaba. ¿Está entre dos zonas y el movimiento cruzó la mitad? **No se marca**, y la franja queda cerrada por hoy.

Más adelante el precio vuelve y pasa el borde por **un tick**: hay **rompimiento**. Basta la mecha.

¿Llega la **consecución** — una vela que pasa del extremo de la que rompió?

La zona queda **traspasada** en ese sentido y cambia de papel. Ese mismo momento es el que dispara la entrada.

Si rompió **con la mecha**, la zona **se estira**. Si rompió **con el cuerpo**, nace la **apéndice**.

Cuando la zona ha sido traspasada **en los dos sentidos**, deja de contar. Ni bloquea un objetivo, ni sirve para entrar.

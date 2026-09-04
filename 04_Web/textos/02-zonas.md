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

El mercado solo tiene dos fases: se mueve con fuerza hacia una dirección (arriba o abajo) o hace una pausa y retrocede un poco, ya sea para continuar el movimiento o para cambiar de sentido. El movimiento con dirección es la **corrida**; la pausa es el **retroceso**. Todo lo que pasa en el gráfico cae en una de esas dos categorías.

> 🖼 **Gráfico.** Texto alternativo: Un movimiento alcista real separado en su corrida y su retroceso
> Pie: Movimiento alcista: la corrida sube y el retroceso baja.

> 🖼 **Gráfico.** Texto alternativo: El mismo mecanismo en un movimiento bajista real
> Pie: El mismo mecanismo hacia abajo: la corrida baja y el retroceso sube.

- **Cuándo nace una corrida** — Surge en la vela que rompe y supera el extremo de la anterior
- **Continuidad del movimiento** — Se mantiene activa mientras cada vela respete el extremo opuesto de la previa. Si empatan al tick, continúa vigente
- **Cuándo termina** — Termina en la primera vela que rompe en dirección contraria, así sea por 1 solo tick
- **Duración** — No tiene límite
- **El color de la vela** — No importa en absoluto
- **Una vela dentro de la anterior** — No interrumpe ni altera la continuidad de la corrida

> **[REGLA DURA]**
> **Un retroceso no tiene tamaño mínimo ni máximo de velas.** Puede ser una sola vela. No se descarta un movimiento por parecer demasiado corto o demasiado largo.

Del retroceso interesa un punto concreto: **su extremo** — el más bajo si la corrida era alcista, el más alto si era bajista. Ahí irá el stop cuando llegue el momento, y ese punto reaparece en casi todas las decisiones que vienen después.

---

<!-- id: nace -->

### Generación de zonas

Cuando una corrida termina, deja un rastro en el gráfico: una franja de precio que se llama **zona**. No se dibuja a ojo. Sale siempre de la misma vela y con los mismos límites.

1. **Se busca la vela de la zona**: la del máximo más alto si la corrida fue alcista, la del mínimo más bajo si fue bajista. Se busca desde el origen de la corrida hasta la vela que disparó el retroceso.
2. **Se dibuja una zona del borde del cuerpo a la punta de la mecha** de esa vela. Ese es todo el criterio.
3. **Se extiende hacia la derecha**, a lo largo del gráfico.

> 🖼 **Gráfico.** Texto alternativo: La vela que genera la zona y los dos bordes exactos que la delimitan
> Pie: La vela que genera zona y sus dos bordes: del borde del cuerpo a la punta de la mecha. Ni un tick más, ni un tick menos.

- **Corrida alcista** — Deja una zona de **resistencia** en la parte de arriba
- **Corrida bajista** — Deja una zona de **soporte** en la parte de abajo
- **Y su retroceso** — El retroceso de una corrida alcista deja **soporte**; el de una corrida bajista genera una **resistencia** arriba
- **Vela sin mecha** — La zona queda dibujada como una línea sobre el precio de cierre o apertura
- **Vela sin cuerpo** — La zona se traza desde el precio de apertura o cierre hasta la punta de la mecha
- **Una vela con máximo mayor y mínimo menor** — El orden dentro de la vela decide cuál sostiene la zona

> 🖼 **Gráfico.** Texto alternativo: La zona ya dibujada y extendida hacia la derecha sobre una sesión real
> Pie: Ya extendida: el rectángulo se dibuja desde la vela de origen, no desde donde el precio vuelva más tarde.

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

> **[FICHA]**
> #### Rompimiento
> El precio pasa el borde de la zona por al menos **un tick**.
> Basta la mecha. **El cierre da igual.**

> **[FICHA]**
> #### Consecución
> Una vela posterior pasa por un tick el **extremo de la vela que rompió**.
> Recién ahí la zona quedó traspasada.

> 🖼 **Gráfico.** Texto alternativo: La vela que pasa el borde de la zona y la que después pasa de su extremo
> Pie: Las dos velas del traspaso sobre una sesión real: la que rompe, y la consecución que pasa de su extremo.

#### Dos maneras de romper

El cierre no decide si hay rompimiento, pero sí deja un rastro distinto. Esa diferencia no se nota hoy: se nota en los dos apartados siguientes, si la consecución no llega.

> 🖼 **Gráfico.** Texto alternativo: Una vela que pasa el borde con la mecha y cierra dentro de la zona
> Pie: Rompimiento con mecha: la vela pasa el borde pero cierra dentro de la zona. Sigue siendo rompimiento.

> 🖼 **Gráfico.** Texto alternativo: Una vela que pasa el borde y cierra fuera de la zona
> Pie: Rompimiento con cuerpo: la vela cierra al otro lado del borde.

> **[REGLA DURA]**
> **Un rompimiento solo, sin consecución, no invalida nada.** La zona sigue viva y sigue contando para todo.
> Y la vela que da la consecución de un traspaso no abre a la vez el rompimiento del lado contrario: eso se busca a partir de la siguiente.

---

<!-- id: estira -->

### Cuando no llega la consecución

Si el precio rompe una zona y pasan 5 velas sin que llegue la consecución, la zona cambia de forma, es decir, se extiende la zona original hasta la punta de esa mecha.

Cuando el rompimiento fue **con la mecha** —el cierre se quedó dentro— la zona **se estira** hasta la punta de esa mecha. El otro borde no se mueve. Sigue habiendo una sola zona, más grande, y conserva su historial.

> 🖼 **Gráfico.** Texto alternativo: Una vela cruza la zona y ninguna de las siguientes supera su extremo
> Pie: El caso más común: la vela cruza la zona, pero ninguna de las siguientes pasa de su extremo. No hubo traspaso y la zona sigue viva.

O si aparece una nueva estructura —un retroceso nuevo— antes de las 5 velas, también se estira la zona.

> **[REGLA DURA]**
> **Las 5 velas son un tope, no una espera obligatoria.** Si antes de que se cumplan aparece un retroceso nuevo, se marca zona en ese momento y no se espera más.
> Actúa lo que llegue primero.

> 🖼 **Gráfico.** Texto alternativo: Un retroceso nuevo aparece antes de las cinco velas y la zona se estira ya
> Pie: No hizo falta esperar: apareció un retroceso nuevo antes de las cinco velas y la zona se estiró en ese momento.

---

<!-- id: apendice -->

### La zona apéndice

Si el rompimiento **fue con cuerpo** y pasan 5 velas sin consecución, no se estira esa zona: **nace una zona nueva**, pegada a la anterior. Se llama **zona apéndice** y se marca desde el cuerpo de la vela que hizo rompimiento hasta la punta de la mecha.

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

O si aparece una nueva estructura —un retroceso nuevo— antes de las 5 velas, también se genera la zona apéndice.

> **[REGLA DURA]**
> **Las 5 velas son un tope, no una espera obligatoria.** Si antes de que se cumplan aparece un retroceso nuevo, se marca zona en ese momento y no se espera más.
> Actúa lo que llegue primero.

> 🖼 **Gráfico.** Texto alternativo: Rompimiento con cuerpo y un retroceso nuevo antes de que se cumpla el plazo
> Pie: Rompió con cuerpo, pero antes de las cinco velas llegó un retroceso nuevo: se marca zona en ese momento.

---

<!-- id: convivencia -->

### Zonas entre zonas

En una jornada aparecen muchas zonas candidatas. Dos reglas evitan que el gráfico se llene de rectángulos y que se acabe operando ruido.

#### Entre dos zonas, solo si no cruza la mitad

Cuando hay una zona por arriba y otra por abajo, se calcula el punto medio entre sus bordes internos. Solo se marca zona nueva si el movimiento que la genera **se queda entero de un lado** de esa mitad.

> 🖼 **Gráfico.** Texto alternativo: Una zona marcada entre otras dos: el movimiento se quedó de un lado de la mitad
> Pie: El movimiento entero se queda del lado en el que empezó. Por eso esta zona sí se marca.

> 🖼 **Gráfico.** Texto alternativo: Un movimiento entre dos zonas que cruza la mitad y por eso no marca zona
> Pie: El mismo caso al revés: el movimiento cruzó la mitad, así que ahí no se marca nada.

> **[REGLA DURA]**
> **Solo se marca una sola zona entre zonas** entre cada resistencia y soporte, si cumple las reglas. Es decir: si se presentan más zonas en el día entre ese rango de resistencia y soporte, ya no se marcan más zonas.

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

# 02 · Marcación de zonas

> Dirección: `/zonas`
> Corrige el texto libremente. **No borres ni cambies las líneas `<!-- id: … -->`**:
> son las que dicen a qué parte de la página vuelve cada bloque.

<!-- id: cabecera -->

## Marcación de zonas

Qué es una zona, de qué vela sale y cómo se dibuja

---

<!-- id: movimiento -->

### Avanzar y descansar

El mercado solo hace dos cosas: avanza un tramo y después se para a descansar. Al tramo que avanza se le llama **corrida**. Al descanso, **retroceso**. No hay un tercer estado.

> 🖼 **Gráfico.** Texto alternativo: Un movimiento real separado en su corrida y su retroceso
> Pie: El mismo movimiento, separado en sus dos partes.

- **Cuándo nace una corrida** — Cuando una vela supera el extremo de la anterior
- **Mientras vive** — Cada vela respeta el extremo contrario de la anterior. Si empatan, sigue viva
- **Cuándo muere** — En la primera vela que va en contra, aunque sea 1 tick
- **Cuántas velas dura** — Mínimo dos. Máximo, ninguno
- **El color de la vela** — No importa en absoluto

La vela que mata la corrida **ya es la primera del retroceso**. No hay hueco entre una cosa y la otra.

> **[REGLA DURA]**
> **Un retroceso no tiene tamaño mínimo ni máximo de velas.**Puede ser una sola vela. No se descarta un movimiento por parecer demasiado corto o demasiado largo.

Del retroceso interesa un punto concreto: **su extremo** — el más bajo si el tramo era alcista, el más alto si era bajista. Ahí irá el stop cuando llegue el momento, y ese punto reaparece en casi todas las decisiones que vienen después.

---

<!-- id: nace -->

### De dónde sale la zona

Cuando una corrida termina, deja un rastro en el gráfico: una franja de precio que se llama zona. No se dibuja a ojo. Sale siempre de la misma vela y con los mismos límites.

> 🖼 **Gráfico.** Texto alternativo: La vela extrema de un tramo y la zona que deja, extendida hacia la derecha
> Pie: La zona nace de la vela que hizo el extremo del tramo y se extiende hacia la derecha.

1. **Se busca la vela extrema** del tramo: la del máximo más alto si fue alcista, la del mínimo más bajo si fue bajista. Se busca desde el origen del tramo hasta la vela que disparó el retroceso, esa incluida.
2. **Se dibuja del borde del cuerpo a la punta de la mecha** de esa vela. Ese es todo el criterio.
3. **Se extiende hacia la derecha**, a lo largo del gráfico.

- **Tramo alcista** — Deja **resistencia** arriba
- **Tramo bajista** — Deja **soporte** abajo
- **Y su retroceso** — El retroceso de un tramo alcista deja **soporte**; el de uno bajista, resistencia
- **Vela sin mecha** — La zona es una línea en el extremo de la vela
- **Vela sin cuerpo** — De ese precio a la punta de la mecha

#### Cuándo se dibuja cada una

Las dos zonas de un movimiento no nacen a la vez, y confundirlo lleva a operar algo que todavía no existe:

> **[FICHA]**
> #### La zona del tramo
> Se dibuja **en cuanto aparece el retroceso**, en vivo. Ya se puede operar.

> **[FICHA]**
> #### La zona del retroceso
> Mientras el retroceso vive es solo una **línea provisional** que se mueve con cada vela. Se convierte en zona cuando el retroceso queda confirmado.

> **[NO SE HACE]**
> **Una línea provisional no opera.** No admite rompimiento, ni confirmación, ni reingreso. Hasta que no es zona, no existe para el método.

---

<!-- id: traspaso -->

### Romper y confirmar

Superar una zona son dos cosas, no una. Y el mismo mecanismo que mata una zona es el que después dispara la entrada.

> 🖼 **Gráfico.** Texto alternativo: La vela que pasa el borde de la zona y la que después pasa de su extremo
> Pie: Las dos velas del traspaso sobre una sesión real: la que rompe, y la que lo confirma pasando de su extremo.

> **[FICHA]**
> #### Rompimiento
> El precio pasa el borde de la zona por al menos **un tick**.
> Basta la mecha. **El cierre da igual.**

> **[FICHA]**
> #### Confirmación
> Una vela posterior pasa por un tick el **extremo de la vela que rompió**.
> Recién ahí la zona quedó superada.

> **[REGLA DURA]**
> **Un rompimiento solo, sin confirmación, no invalida nada.**La zona sigue viva y sigue contando para todo.
> Y la vela que confirma un traspaso no abre a la vez el rompimiento del lado contrario: eso se busca a partir de la siguiente.

La confirmación puede tardar. Para invalidar una zona**no hay plazo**: el rompimiento queda pendiente indefinidamente y la confirmación lo cierra cuando llegue. El plazo de5 velas que viene a continuación gobierna otra cosa: la forma de la zona y la vida de la orden.

---

<!-- id: cinco -->

### Cuando no se confirma

Si el precio rompe una zona y pasan 5 velas sin que llegue la confirmación, la zona cambia de forma. Cómo cambia depende de si la vela que rompió lo hizo con la mecha o con el cuerpo.

> 🖼 **Gráfico.** Texto alternativo: Una vela cruza la zona y ninguna de las siguientes supera su extremo
> Pie: El caso más común: la vela cruza la zona, pero ninguna de las siguientes pasa de su extremo. No hubo traspaso y la zona sigue viva.

> 🖼 **Gráfico.** Texto alternativo: Rompimiento con cuerpo que no se confirma y la zona apéndice que deja
> Pie: Rompimiento con cuerpo sin confirmar: la zona original se queda como estaba y nace una segunda sobre la mecha de la vela que rompió.

> **[FICHA]**
> #### Rompió con la mecha
> El cierre se quedó dentro de la zona.
> **La zona se estira** hasta la punta de esa mecha. El otro borde no se mueve. Sigue habiendo una sola zona, más grande.

> **[FICHA]**
> #### Rompió con el cuerpo
> El cierre quedó fuera de la zona.
> **Nace una zona apéndice** sobre la mecha de esa vela. La original se queda intacta. Ahora hay dos.

> **[REGLA DURA]**
> **Las 5 velas son un tope, no una espera obligatoria.**Si antes de que se cumplan aparece una estructura nueva —un retroceso nuevo—, se marca zona en ese momento y no se espera más.
> Actúa lo que llegue primero.

---

<!-- id: convivencia -->

### Varias zonas a la vez

En una jornada aparecen muchas zonas candidatas. Tres reglas evitan que el gráfico se llene de rectángulos y que se acabe operando ruido.

#### Si se tocan, se funden

Si la zona que se iba a marcar toca una que ya existe —basta que se rocen los bordes— **no se crea una nueva**: se estira la que ya estaba hasta el extremo nuevo. El otro borde no se mueve, y la zona conserva su historial de rompimientos.

#### Entre dos zonas, solo si no cruza la mitad

Cuando hay una zona por arriba y otra por abajo, se calcula el punto medio entre sus bordes internos. Solo se marca zona nueva si el movimiento que la genera **se queda entero de un lado** de esa mitad.

> **[REGLA DURA]**
> **Lo que se mide es el recorrido del precio, no el rectángulo.**Si el movimiento cruzó la mitad en algún punto, no se marca — aunque la caja de la zona quede entera a un lado.

#### Una sola por franja y por jornada

La franja entre dos zonas admite **una zona en todo el día**, y el turno lo resuelve el primer retroceso que aparezca dentro. Si ese primero respeta la mitad, se marca; si no la respeta, no se marca. En los dos casos **la franja queda cerrada** para el resto de la jornada, y no se reabre aunque las zonas que la formaban se mueran.

Cualquier zona viva sirve de borde de la franja, incluidas las que se marcaron de madrugada por volumen.

> **[NO SE HACE]**
> **Salir de una zona es romper y confirmar, no geometría.**Mientras un rompimiento espera su confirmación, no se marca zona al otro lado de esa zona.

---

<!-- id: caduca -->

### Cuándo deja de contar

Una zona muere cuando ha sido superada **en las dos direcciones**: rompimiento y confirmación hacia un lado, y rompimiento y confirmación hacia el otro.

- **Superada en un solo sentido** — Sigue viva. Cambia de papel: el soporte pasa a resistencia y al revés
- **Superada en los dos** — **No cuenta para nada.** Ni bloquea un objetivo, ni sirve para entrar, ni cuenta para medir la mitad entre zonas
- **En pantalla** — Se deja dibujada en tono muy tenue, solo como recuerdo

Esa distinción importa más de lo que parece: una zona que sigue viva puede impedir una entrada perfectamente válida, porque se cruza en el camino del objetivo.

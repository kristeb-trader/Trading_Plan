# 08 · Riesgo y tamaño

> Dirección: `/riesgo`
> Corrige el texto libremente. **No borres ni cambies las líneas `<!-- id: … -->`**:
> son las que dicen a qué parte de la página vuelve cada bloque.

<!-- id: cabecera -->

## Riesgo y tamaño

Cuánto se arriesga, cuántas veces y con cuántos contratos

---

<!-- id: cuanto -->

### Cuánto se arriesga

El riesgo de cada operación no lo decide una cuenta: lo decide la estructura del mercado. Lo único que hay es un techo.

- **Tope de stop** — **80 puntos** = 320 ticks = $160 en MNQ
- **Objetivo** — La misma distancia, al otro lado. Relación 1:1
- **Sobre la cuenta objetivo de $3.000** — **5,3 %** por operación

> 🖼 **Gráfico.** Texto alternativo: La distancia al stop y la misma distancia al objetivo desde la entrada
> Pie: El riesgo lo pone la estructura: la distancia hasta el stop, repetida al otro lado. El tope solo dice hasta dónde se acepta esa distancia.

> **[REGLA DURA]**
> **El tope es una línea dura.** Un stop de 79,75 puntos se opera igual que uno de 30. Y si el stop estructural sale a 80,25, no se opera, por buena que sea la figura.

> 🖼 **Gráfico.** Texto alternativo: Un setup válido descartado porque el stop estructural supera el tope de riesgo
> Pie: El tope en acción: un setup que cumple todo lo demás y se descarta entero porque el stop no cabe.

Con una sola operación al día y una relación de uno a uno, hace falta acertar **más de la mitad de las veces** solo para no perder dinero.

---

<!-- id: cuantas -->

### Cuántas veces

- **Operaciones por sesión** — **1 llenada, como máximo**
- **¿Y si la orden se cancela sin llenarse?** — No consume el cupo. Se puede esperar otro setup
- **¿Cambia algo el resultado?** — No. Ganada o perdida, el día terminó igual

Una operación al día es también lo que hace lenta la recuperación: no hay forma de compensar un mal día dentro del mismo día, y eso es deliberado.

---

<!-- id: tamano -->

### Con cuántos contratos

> **[REGLA DURA]**
> **Siempre 1 MNQ contrato de MNQ.** No sube porque la cuenta crezca. No baja tras una mala racha. No cambia por convicción.
> El tamaño solo se puede revisar una vez al año.

Esto tiene una consecuencia aritmética que conviene tener presente: con el tamaño fijo y el tope de riesgo fijo en dólares, **el riesgo porcentual crece a medida que la cuenta cae**. Los mismos $160 son el 5 % de $3.000 y el 11 % de $1.400.

---

<!-- id: parada -->

### No hay regla de parada

Este es un hueco declarado del método, y se enseña aquí porque es el único que se nota desde dentro de la operativa.

> **[NO SE HACE]**
> **El plan no dice cuándo se deja de operar.**
> No hay límite de pérdida semanal. No hay límite mensual. No hay corte tras una racha de pérdidas. No hay reducción de tamaño cuando la cuenta cae.

La consecuencia se ve mejor con números. Cada una de estas filas es una racha de días perdedores seguidos, todos con su setup válido y su stop correcto:

| Días malos seguidos | Pérdida | Capital | Caída | Para recuperarlo |
| 4 | $640 | $2.360 | −21 % | +27 % |
| 6 | $960 | $2.040 | −32 % | +47 % |
| 10 | $1.600 | $1.400 | −53 % | +114 % |
| 15 | $2.400 | $600 | −80 % | +400 % |

> **[REGLA DURA]**
> **Ninguna regla del método se rompe en esa tabla.** Cada día fue un setup válido, ejecutado exactamente como está escrito. El plan permite ese recorrido entero sin emitir una sola señal de alarma.
> Y una racha de seis pérdidas seguidas, acertando la mitad de las veces, aparece en unos cinco meses de operativa con una probabilidad cercana a la mitad. No es un caso extremo: es lo normal.

El operador dejó esta decisión abierta a propósito, para tomarla con datos reales del registro en vez de con un número inventado.

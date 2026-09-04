# 03 · Setups operativos

> Dirección: `/setups`
> Corrige el texto libremente. **No borres ni cambies las líneas `<!-- id: … -->`**:
> son las que dicen a qué parte de la página vuelve cada bloque.

<!-- id: cabecera -->

## Setups operativos

Los dos únicos setups que se operan: IRI y Reingreso

---

<!-- id: dos -->

### Solo hay dos

El método no busca oportunidades: busca **dos figuras concretas**. Si lo que hay delante no es una de las dos, no hay operación, por bien que se vea el gráfico.

> **[FICHA]**
> #### Continuación
> El precio rompe una zona y sigue. Se opera **a favor** del rompimiento.

> **[FICHA]**
> #### Rompimiento fallido
> El precio rompe una zona, no sigue y se da la vuelta. Se opera **en contra** del rompimiento.

> **[REGLA DURA]**
> **Se toma el primero que aparezca y se llene.** No se compara con lo que pueda venir después, ni se espera «uno mejor». El criterio es el reloj, no la calidad.

---

<!-- id: iri -->

### IRI · continuación

El IRI es autocontenido: el propio movimiento crea la zona que después rompe. Impulso, retroceso, impulso — y el segundo impulso es la entrada.

> 🖼 **Gráfico.** Texto alternativo: Un IRI completo: movimiento, retroceso, zona, rompimiento y consecución
> Pie: Los cinco pasos sobre una sesión real. La vela de la consecución es la que entra.

1. **Una corrida.** El precio avanza un movimiento.
2. **Un retroceso.** El movimiento se para a descansar.
3. **La zona.** El movimiento deja su zona en la vela extrema. Sin zona no hay IRI.
4. **Rompimiento de esa misma zona**, en el sentido del movimiento original, por al menos un tick.
5. **Confirmación: y esa es la entrada.** Una vela pasa el extremo de la vela que rompió.

- **Plazo para la consecución** — **5 velas — es un TOPE, no una espera obligatoria *(`R-19`, precisada 01/09/2026)*** desde la siguiente a la que rompió. Lo normal es la primera o la segunda
- **Si no llega a tiempo** — La entrada queda invalidada. La zona sigue su propio camino
- **Dónde va el stop** — En el punto más extremo alcanzado **desde que nació la zona hasta la vela que rompió**
- **Filtro de objetivo** — El camino debe estar libre de zonas vivas

---

<!-- id: reingreso -->

### Reingreso · rompimiento fallido

Es el contrario exacto del IRI. Aquí el rompimiento se confirmó pero el precio **no continuó**: se dio la vuelta y se comió la zona entera. Se opera esa vuelta.

> 🖼 **Gráfico.** Texto alternativo: Un Reingreso: rompimiento con consecución que falla y el precio recupera la zona entera
> Pie: El rompimiento se confirmó y no siguió. El precio atraviesa la zona completa y sale por el borde contrario: ahí empieza el Reingreso.

1. **Sobre una zona hubo rompimiento y confirmación.** El traspaso está hecho.
2. **El precio no continúa** en esa dirección.
3. **El precio atraviesa la zona entera y sobrepasa el borde contrario.** No basta con tocarla ni con meterse dentro: tiene que salir por el otro lado. Esa vela hace de vela de rompimiento del Reingreso.
4. **Confirmación: y esa es la entrada.** Una vela pasa el extremo de la vela anterior, igual que en el IRI.

- **Dirección** — Contraria a la del rompimiento que falló
- **Plazo para que aparezca** — **Ninguno.** El límite de 5 velas — es un TOPE, no una espera obligatoria *(`R-19`, precisada 01/09/2026)* no aplica aquí
- **Dónde va el stop** — En el extremo de la **corrida fallida**, la que rompió y no continuó
- **Filtro propio** — El objetivo debe caber **dentro del punto de referencia**

#### El punto de referencia

El Reingreso es el único setup con un segundo filtro de objetivo. El punto de referencia es **el extremo del retroceso que originó la zona**. Si el objetivo cae más allá de ese punto, el Reingreso no es válido y no se opera.

> **[REGLA DURA]**
> **El Reingreso es inmediato o no es.** La ventana se abre con la vela de la consecución y se cierra en cuanto el precio supera el extremo de esa misma vela.
> Cuando el precio sigue de largo, la ventana se cerró para siempre. No se espera a que vuelva.

---

<!-- id: comparar -->

### Uno al lado del otro

Comparten la mecánica de entrada — los dos entran con la confirmación — pero se diferencian en casi todo lo demás.

|  | IRI | Reingreso |
| Qué opera | El rompimiento que funciona | El rompimiento que falló |
| Dirección | A favor del movimiento | Contraria al rompimiento |
| Plazo | 5 velas — es un TOPE, no una espera obligatoria *(`R-19`, precisada 01/09/2026)* para la consecución | Sin plazo para aparecer; inmediato para entrar |
| Stop | Extremo del retroceso | Extremo de la corrida fallida |
| Filtros de objetivo | Camino libre de zonas vivas | Camino libre *y* dentro del punto de referencia |
| Día de la Fed | Prohibido | Permitido |

> **[REGLA DURA]**
> **El stop del Reingreso suele salir más ancho.** Se mide contra la corrida fallida, que está al otro lado de la zona, así que incluye la zona entera. Por eso el tope de riesgo descarta más Reingresos que IRIs.

---

## Anotaciones que seguian abiertas

Venian del archivo anterior y todavia no estan reflejadas en la pagina.
Borralas cuando ya no hagan falta.
- [NOTA: Puedes modificar el grafico, colocar uno mas tendencial y sencillo, explicando Impulso, Retroceso, Impulso]
- [NOTA: Puedes modificar el grafico, colocar uno mas sencillo, con menos velas, pero que se entienda el setup de Reingreso]

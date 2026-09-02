# ESTADO DE LA FASE 2 — el portal

> **Este es el documento de seguimiento.** Qué hay hecho, qué falta, qué se
> decidió y por qué. Es el equivalente de `01_Plan\ESTADO.md` para la fase 2.
>
> **Se actualiza al cerrar cada sesión de trabajo.** Si abres un chat nuevo,
> léelo primero: con esto y `CLAUDE.md` se retoma sin que nadie te cuente nada.

**Fase:** 2 — portal web · **Estado:** 🟢 publicado, 🔍 **en revisión por partes**
**El mapa de todas las fases está en `..\FASES.md`.** Después de esta vienen el agente de backtesting y el bot de NinjaTrader, las dos **declaradas y sin definir**.
**Última actualización:** 2026-09-02
**Dirección:** https://plan-operativo-nq.pages.dev

---

## Lo primero que hay que saber

| | |
|---|---|
| **Qué es** | la página donde **Alfredo Chaumer** revisa las reglas que se extrajeron de su metodología y **deja observaciones escritas** |
| **Quién entra** | cualquiera con la dirección. **Sin código, sin correo, sin contraseña** — decisión del operador |
| **Qué se comparte** | **la dirección**, nunca el repositorio. El repositorio es privado y se queda privado |
| **Cómo se publica** | se compila en el equipo y se sube con `wrangler`. Cloudflare **no** está conectado al repositorio |
| **Dónde viven las observaciones** | Cloudflare D1, la base de datos de Cloudflare |
| **Qué NO es** | una herramienta de operación. No manda órdenes y no se conecta a ninguna cuenta |

> 🔴 **Una observación de Alfredo no es una regla.** El plan solo cambia si el
> operador cambia `01_Plan\`. El portal deja constancia; no toca la fuente.

---

## Los documentos de esta carpeta, y cuál manda

| Archivo | Qué es | Vigencia |
|---|---|---|
| **`ESTADO_FASE_2.md`** | **este archivo. El seguimiento** | ✅ **vivo** |
| `DESPLIEGUE.md` | cómo se publica, paso a paso | ✅ vivo |
| `DISENO_PORTAL.md` | el diseño de partida, escrito el 31/08 | 🟡 parcial — la estructura de ocho módulos es posterior |
| `BRIEF_PORTAL.md` | el encargo original | 🔴 superado |
| `PROMPT_FASE_2.md` | el guion de arranque | 🔴 superado |

**Si dos se contradicen, manda el de más abajo en el tiempo**, y este archivo por
encima de todos. Los dos marcados en rojo se conservan como historia; no se
trabaja contra ellos.

---

## Qué hay construido

### El recorrido del método — ocho módulos

Cada uno en su propia dirección. Es lo que Alfredo recorre.

| | Módulo | Qué cubre |
|---|---|---|
| 01 | **Premercado** | estado del operador, calendario de noticias, los dos gráficos, la ATM, zonas por volumen |
| 02 | **Marcación de zonas** | corrida y retroceso, de qué vela sale la zona, romper y confirmar, las cinco velas, convivencia de zonas, caducidad |
| 03 | **Setups operativos** | IRI y Reingreso, con una comparación lado a lado |
| 04 | **Jornada operativa** | las dos horas, la primera vela, cómo avanza la sesión, el registro |
| 05 | **Mecánica de entrada** | qué orden y dónde, stop y objetivo, la orden esperando |
| 06 | **Filtros: cuándo NO se entra** | los cuatro filtros, las noticias, lo que cancela la orden |
| 07 | **Dentro de la operación** | los dos ajustes al llenarse y la prohibición de gestionar |
| 08 | **Riesgo y tamaño** | el tope, el cupo diario, el tamaño fijo, y que **no existe regla de parada** |

Los módulos 07 y 08 **no estaban en la lista original del operador**. Se
añadieron el 01/09 con su visto bueno: sin el 07 el portal explicaba cómo entrar
pero no la regla más dura del plan, y el 08 recoge un hueco declarado.

### El resto del portal

| Sección | Estado |
|---|---|
| Portada de bienvenida | ✅ |
| Casos reales (21, con filtro) | ✅ |
| Vocabulario (23 términos) | ✅ |
| Observaciones | ✅ funcionando de punta a punta |
| Buscador con `Ctrl+K` | ✅ 114 entradas |
| El plan completo, las 38 fichas de regla, parámetros, checklist, pendientes, contextualización, acta de cierre | ✅ **solo en modo técnico** |

### Modo técnico

Enseña los códigos de regla (`R-22`, `P-14`…) y el grupo «Todo el detalle» del
menú. **Es para el operador, no para Alfredo.**

- **Encender:** añadir `?tecnico=1` a cualquier dirección. El navegador lo recuerda.
- **Apagar:** `?tecnico=0`, o el enlace «apagar» que aparece abajo del menú cuando está encendido.

### Gráficos

**Trece**, generados con Python sobre datos reales de mercado, con
`scripts/graficos_conceptos.py`, que importa el motor de `05_Backtesting`
**sin tocarlo**. Se regeneran con:

```
python scripts/graficos_conceptos.py
```

---

## 🔍 La revisión del operador — EN MARCHA

**El operador está revisando el portal por partes**, y reporta los cambios por
partes, cada tanda en su propio chat. Decidido así el 2026-09-01: recorrerlo
entero de una vez es demasiado.

> **Al terminar cada tanda, marca aquí la parte revisada y anota los cambios
> hechos.** Es lo que permite que el siguiente chat sepa por dónde va la cosa
> sin preguntar.

| | Parte | Dirección | Revisada | Cambios |
|---|---|---|---|---|
| | Portada | `/` | ✅ **2026-09-02** | marca nueva, menú con iconos, dos portadas, pie del operador. Detalle en el historial |
| 01 | Premercado | `/premercado` | ⬜ | |
| 02 | Marcación de zonas | `/zonas` | ⬜ | |
| 03 | Setups operativos | `/setups` | ⬜ | |
| 04 | Jornada operativa | `/jornada` | ⬜ | |
| 05 | Mecánica de entrada | `/entrada` | ⬜ | |
| 06 | Filtros: cuándo NO se entra | `/filtros` | ⬜ | |
| 07 | Dentro de la operación | `/dentro` | ⬜ | |
| 08 | Riesgo y tamaño | `/riesgo` | ⬜ | |
| | Casos reales | `/galeria` | ⬜ | |
| | Vocabulario | `/glosario` | ⬜ | |
| | Observaciones | `/observaciones` | ⬜ | |

**Cómo se retoma una tanda en un chat nuevo:**

> Lee `CLAUDE.md` y `04_Web\ESTADO_FASE_2.md`. Vamos con la revisión del módulo *(el que sea)*.

---

## Qué falta

| | Qué | Quién |
|---|---|---|
| 🔴 | **Crear la clave del operador** para poder ver y borrar las observaciones desde fuera del portal: `npx wrangler pages secret put CLAVE_OPERADOR --project-name=plan-operativo-nq` | **el operador** |
| 🟡 | La revisión por partes de arriba | el operador |
| 🔴 | **Alfredo no puede dejar observaciones en los ocho módulos.** Comprobado uno por uno: cero puntos comentables en premercado, zonas, setups, jornada, entrada, filtros, dentro y riesgo. Solo se comenta en casos reales y vocabulario, y `/observaciones` es de solo lectura. **Es la razón de ser de la fase.** Siguiente tanda | pendiente |
| 🟡 | Simplificar la prosa de los casos reales, que todavía suena a auditoría | pendiente |
| 🟡 | Pasarle la dirección a Alfredo | el operador, **cuando termine la revisión** |

---

## Historial

### 2026-09-02 · la portada, revisada — y el portal partido en dos

**Primera tanda de la revisión por partes.** Se auditó la portada con dos
análisis independientes: uno de diseño y otro de medición en el navegador.
Puntuación de partida: **20 sobre 36**.

**Lo que decidió el operador**

El portal pasa a tener **dos portadas**:

| | La de Alfredo (`/`) | La técnica (`/tecnico`) |
|---|---|---|
| Menú | inicio, los ocho módulos, casos reales, observaciones | todo lo anterior + «Todo el detalle» |
| Buscador | **no existe**, ni con `Ctrl+K` | sí |
| Vocabulario, parámetros, las 38 fichas, checklist, pendientes, contextualización, acta de cierre | no | sí |
| «Plan no probado» y los cuatro huecos | no | **sí, enteros** |

Se entra a la técnica por un **icono pequeño y apagado al pie del menú**, que
de paso enciende el modo técnico.

> 🔴 **Cambio de una regla escrita.** `CLAUDE.md` decía que los huecos
> declarados los muestra *el portal*. Ahora los muestra la portada técnica.
> Razón del operador: lo que no está probado es **la transcripción del método,
> no el método de Alfredo**. Queda anotado en `CLAUDE.md`.

**Cambios de la portada**

| | |
|---|---|
| Marca | «Plan Chaumer · NQ, MNQ, NinjaTrader 8» pasa a **«Trading Plan Nasdaq»** con icono propio y favicon. El icono es el **zigzag de corrida y retroceso**: sale del vocabulario del método, no de un catálogo |
| Fuera de la portada | la píldora «Escrito y contrastado. No probado.», el «NO PROBADO» de la cabecera, los contadores 38/11/23, la frase «Portal de revisión…», el bloque «Antes de juzgarlo» y el buscador |
| Subtítulo | ahora: «traducido a reglas que se pueden **medir, seguir y operar**» |
| Menú | **icono por elemento**, «Inicio» arriba con su casita, el número del módulo pasa detrás. Vocabulario se va a la parte técnica |
| Pie | «© Christian Buitrago · kristeb@hotmail.com» y «Versión 1.0» |

**Defectos corregidos de paso** *(los encontró la auditoría, no estaban en la lista)*

| Qué | Por qué importaba |
|---|---|
| El menú perdía los nombres en el móvil | a 375 px las once etiquetas medían **0 px**: quedaba «01 02 03…» sin un solo nombre |
| El marco de foco del botón azul era **azul sobre azul** | invisible en el botón más importante. Ahora se pinta en claro |
| El sello de versión salía **dos veces** | uno debajo del otro al final de la página |
| El gráfico del hero iba **girado en 3D y al 25 %** | ilegible, y contra el estándar de gráficas que el operador validó: «cuanto más limpio, mejor». Ahora va de frente |
| El titular partía **«Alfredo / Chaumer»** entre dos líneas | el nombre del cliente roto dentro de su propio titular |
| El degradado partía «ex» blanco y «plicada.» azul | ahora el énfasis es de color sólido |
| La portada rompía a 1000 px y el marco a 900 | entre esos dos anchos la página se veía rota. Un solo punto de ruptura: **900** |
| Colores escritos a mano | `#06121F`, `#6AA0FF` y una copia literal de un token que ya existía. Ahora son tokens |

**Comprobado, no supuesto:** contraste de cada texto sobre su fondo real (todo
por encima del mínimo), sin desbordamiento horizontal a 375, 900 ni 1440,
objetivos táctiles de 44 px, un solo `h1` sin saltos de nivel, y que con el
modo técnico apagado **el buscador no existe ni con `Ctrl+K`**. Detector de
anti-patrones: cero hallazgos en los archivos tocados.

> ⚠️ **Excepción consciente:** el icono de la puerta técnica queda por debajo
> del contraste normal (2,6:1). Es lo que el operador pidió — «muy pequeño,
> escondido» — y se aclara al pasar por encima o al tabular.


### 2026-08-31 · la decisión que define el portal

El operador redefine qué es el portal: **no es una herramienta de operación**,
es donde Alfredo revisa y deja observaciones. Dos puntos del encargo original
quedan derogados: deja de ser cien por cien estático *(las observaciones
necesitan guardarse)* y se publica ya.

### 2026-09-01 · todo lo demás

Una sola jornada de trabajo, 28 commits.

| Bloque | Qué pasó |
|---|---|
| **Arranque** | se restauran las tildes de `reglas.json` (168 textos). Se dejan sin tildes `categoria` e `id` a propósito: el portal filtra por ellos |
| **Repositorio** | se detecta que **estaba público**. El operador lo pone privado antes de subir nada |
| **Diseño** | seis iteraciones. El operador rechaza cuatro por «muy simple, muy plana» y pide expresamente estética moderna, ignorando las prohibiciones del brief. Se instalan tres skills de diseño y se rehace |
| **Contenido** | las 38 fichas de regla, parámetros, vocabulario, los 21 casos, checklist, pendientes, contextualización y acta de cierre |
| **Publicación** | Cloudflare Pages + D1. Se descarta Supabase. Dirección elegida por el operador: `plan-operativo-nq` |
| **Entrada libre** | se retira la puerta: Alfredo entra solo con la dirección |
| **Simplificación** | el operador: *«está súper largo y muy técnico, no quiero ver nada de si supera la R-xx»*. Se separan dos capas: una de entendimiento sin un solo código, y el detalle completo detrás del modo técnico. Los documentos de `01_Plan\` **no se tocan** — son la base del futuro bot |
| **Portada** | se cambia el redirigir al inicio por una portada de bienvenida |
| **Ocho módulos** | la explicación pasa de una sola página larga a ocho módulos navegables, en el orden real de la jornada |

### Errores encontrados y corregidos

Se dejan escritos porque cuestan tiempo si se repiten.

| Qué | Cómo se vio |
|---|---|
| **La página se veía partida por la mitad** con el modo técnico encendido | el botón del rail y la clase que enciende el modo se llamaban igual, y el estilo del botón caía sobre la página entera. **Lo encontró el operador** |
| **Un reingreso de ejemplo que no se habría operado** | el precio continuaba 140 puntos antes de darse la vuelta: el stop no cabía en el tope. Se ató la búsqueda al tope de riesgo |
| **El generador de gráficos abría la ventana una vela antes** | las velas van marcadas **al cierre**, así que la de la apertura es la `1331`, no la `1330`. Se ve en el volumen: 641 contratos y de golpe 4.333. `lector.py` ya lo hacía bien; el fallo era solo del generador |
| Un gráfico con el stop en 105,75 puntos | por encima del tope: ese setup no se opera. Se rehízo con uno dentro del tope |
| «REABIERTO Y VUELTO A CERRAR» contaba como abierto | faltaban límites de palabra en la búsqueda. 17 pendientes abiertos pasaron a ser 16 |

---

## Cómo se trabaja aquí

### Publicar un cambio

```
cd 04_Web
npx astro build
npx wrangler pages deploy dist --project-name=plan-operativo-nq
```

Detalle completo en `DESPLIEGUE.md`.

### Si los documentos de `01_Plan\` cambian

```
cd 04_Web
node scripts/sync.mjs
```

El portal **no inventa contenido**: lee los documentos del plan y los presenta.
Si el plan cambia, se sincroniza y se vuelve a compilar.

### Reglas que no se saltan

1. **No se inventa metodología.** Todo sale de `01_Plan\`. Si falta, **falta**.
2. **Los documentos de `01_Plan\` no se tocan desde el portal.** Son la base del futuro bot.
3. **Ningún adjetivo es una regla.** Solo ticks, puntos, porcentajes, velas y horas.
4. **Nada de códigos de regla a la vista** fuera del modo técnico.
5. **Nada de textos que hablen del portal, del repositorio o de documentos.** Alfredo viene a leer la estrategia.
6. **Los cuatro huecos declarados se enseñan, no se esconden.**

---

## Para retomar en un chat nuevo

Basta con abrir Claude Code en `E:\Proyectos\Chaumer` y decir qué se quiere
hacer. `CLAUDE.md` se carga solo, y apunta aquí.

Si quieres darle contexto de golpe:

> Lee `CLAUDE.md` y `04_Web\ESTADO_FASE_2.md`. Vamos a seguir con la fase 2.

El historial real y completo está en el repositorio: `git log --oneline`.

**Y lo primero que hay que hacer al terminar una tanda:** actualizar la tabla de
revisión de arriba y, si hubo cambios de fondo, el apartado de historial. Si no
se hace, el siguiente chat empieza a ciegas.

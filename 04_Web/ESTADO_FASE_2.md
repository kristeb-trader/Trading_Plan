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

### 2026-09-02 · el banner, el menú con relieve y la portada sin botones

Cuarto cambio del día. El operador: *«el título más grande, centrado… que se
vea 3D»*, *«esa barra de menú se puede mejorar, más 3D, que los iconos no se
vean tan muertos»*.

**El banner**

| | Antes | Ahora |
|---|---|---|
| Nombre | «Plan Chaumer» | **«Trading Plan de Futuros · NQ»**, también en la pestaña |
| Sitio | pegado a la izquierda | **centrado** en la cabecera, con el buscador a su izquierda |
| Tamaño | 15 px | 28 px, con el icono a 48 px |
| Relieve | plano | tres capas: degradado en el azulejo, sombra desplazada debajo, y el texto con luz de arriba abajo más una sombra oscura de 1 px |

**Lo de «una imagen del Nasdaq».** No se puso ninguna foto ni la marca Nasdaq:
es una marca registrada y el portal no tiene nada que ver con ellos, y una foto
de archivo de una sala de trading es justo lo que hace que una página parezca
de plantilla. En su lugar la cabecera lleva **una fila de velas azules y
blancas al 10 %**, desvanecida a los lados — el lenguaje del propio plan. **No
es una gráfica:** no representa ningún dato, así que no le aplica el estándar
de gráficas, que manda solo donde se dibuja mercado real. Si el operador quiere
una imagen de verdad, la tiene que dar él.

**El menú**

Cada icono deja de ser un glifo suelto y pasa a ser un objeto: azulejo teñido,
borde de luz arriba, sombra abajo, y se levanta al pasar el ratón. El activo se
enciende del todo.

**El tono avanza del cian al azul a lo largo de los ocho módulos.** No codifica
nada nuevo: acompaña al número, que ya dice el orden. Los dos colores salen del
estándar; no se inventó ninguno, y **no se usaron ni el rojo ni el oro**, que
están reservados.

**La portada**

Fuera los dos botones del titular. «Ver los casos reales» ya estaba abajo en
«Ver cómo se aplica», y «Empezar por el principio» en «Recorrer el método» —
donde además se explica a dónde llevan. El titular pasa de 48 a 58 px.

Sin botones y con el titular más grande, **el hero pasa a una sola columna**: a
dos columnas se partía en «La metodología / de / Alfredo Chaumer,» dejando un
«de» suelto. A todo el ancho son dos líneas limpias, y **el gráfico gana 1039 px
de ancho**, que era la otra queja de la primera auditoría: se lee de verdad.

**Dos cosas que se rompieron y se arreglaron por el camino**

| Qué | Por qué |
|---|---|
| La textura no se veía | iba con `z-index: -1`, o sea **por detrás del fondo** de la cabecera |
| En móvil con modo técnico la página **se desbordaba 24 px** | el buscador se partía en tres líneas y empujaba la marca fuera. Ahora la cabecera se apila: banner arriba, buscador debajo a todo el ancho |

**Comprobado:** banner centrado al píxel, sin desbordes a 375 ni 1440 con el
modo técnico encendido y apagado, contraste de los iconos del menú entre 4,49 y
7,99 *(el mínimo para un icono es 3)*, el titular en dos líneas a 1440 y tres a
375, y el alto de la cabecera propagándose solo al menú lateral.

> El detector avisa de «exceso de guiones largos» en `Marco.astro`. Es falso
> positivo: cuenta los de los comentarios del código, no los de ningún texto
> que vea nadie.

### 2026-09-02 · dos gráficos nuevos, y la lista de los que faltan

El operador pidió generar gráficos nuevos. Se ampliaron **13 → 15** conceptos.
`scripts/graficos_conceptos.py` sigue sin tocar `05_Backtesting`: solo importa
su motor.

| Nuevo | Dónde | Qué muestra |
|---|---|---|
| `14-traspaso.png` | Zonas · **Romper y confirmar** | la vela que pasa el borde y la que después pasa de su extremo. Mismo patrón que el número 4 pero **buscado en otra sesión**, para no repetir imagen dentro del mismo recorrido |
| `15-sesion.png` | Jornada · **Cómo avanza la sesión** | la ventana entera con el zigzag que une los extremos de cada tramo |

> ⚠️ **El 15 se dibujó primero con sus 44 zonas y quedó ilegible**: una mancha
> gris tapando las velas. Además el plan dice que en pantalla va **una sola
> zona por banda y por jornada**, no las 44 en crudo — y decidir cuál sobrevive
> en cada banda es metodología, no dibujo. Se dejó solo el zigzag, que es
> exactamente de lo que habla ese apartado.

**Estado: 15 apartados con imagen, 22 sin ella.** El triaje de esos 22:

**Grupo 1 — el motor los encuentra solo, se pueden generar cuando el operador dé el visto bueno**

| Apartado | Qué mostraría |
|---|---|
| Zonas · Varias zonas a la vez | una ventana con varias zonas vivas y la que manda en cada banda |
| Zonas · Cuándo deja de contar | una zona que caduca y deja de servir |
| Setups · Uno al lado del otro | IRI y Reingreso en dos paneles de la misma imagen |
| Filtros · Lo que cancela la orden | una orden en espera que se cancela antes de llenarse *(sirve también para «La orden esperando»)* |
| Dentro · Solo hay dos salidas | dos paneles: una operación al stop y otra al objetivo |

**Grupo 2 — hacen falta datos o una decisión del operador**

| Apartado | Qué falta |
|---|---|
| Premercado · El calendario | marcar la ventana de once minutos de una noticia roja. **Las horas de las noticias no están en los datos** |
| Premercado · Los dos gráficos | NQ y MNQ el mismo minuto con la diferencia de hasta 3 ticks. **No hay datos de MNQ**, solo de NQ |
| Jornada · Por dónde empieza el día | hay una regla que quitó el sesgo de dirección; qué enseñar sin contradecirla lo decide el operador |
| Filtros · Descartado no es vacío | tras un descarte la zona sigue contando. Hay varias formas de enseñarlo |

**Grupo 3 — no son gráfico, y ponerles uno sería decorar**

Cómo estoy hoy · La ATM · Solo hay dos · El registro · Antes de enviar · No
abrir el día · Las noticias *(filtros)* · No se toca nada · Al cerrar · Cuántas
veces · Con cuántos contratos · No hay regla de parada.

Son estado del operador, configuración de la plataforma, cuentas y
prohibiciones: nada de eso pasa en un gráfico de precio. Lo que sí admiten —la
ATM y el registro— son **capturas de la pantalla del operador**, y las tiene
que dar él.

### 2026-09-02 · un apartado por pantalla, con ruta numerada

**Tercer cambio del día, en los ocho módulos.** El operador: *«cuando doy clic
en Cómo estoy hoy, solo me salga lo de ese submódulo»*, y *«esa página está muy
muerta, parece de una funeraria»*.

**Un apartado a la vez.** Cada módulo deja de ser una página larga: se ve un
apartado y se pasa al siguiente. La ruta de arriba es ahora un recorrido
numerado con la línea que une las paradas — porque los apartados **están en el
orden en que se hacen las cosas**, no son pestañas intercambiables. La parada
hecha se marca con un visto, la actual va rellena y con halo.

**El pie encadena.** Dentro del módulo mueve de apartado; en el último, el
botón «siguiente» pasa a ser **el módulo siguiente**, en azul. Los ocho módulos
y sus 37 apartados se recorren enteros sin volver nunca al menú.

**Sin JavaScript** se ven todos los apartados seguidos, como antes: el HTML
lleva el contenido completo y ocultar es cosa del navegador.

**Lo visual**

| Qué | Antes | Ahora |
|---|---|---|
| Gráficos | imagen suelta con un filete de 1 px | pieza de cristal con halo azul y el pie dentro del mismo marco |
| Avisos y prohibiciones | barra de color de 2 px a la izquierda | **icono**, panel teñido y borde entero. Esa barra es la marca de fábrica de las interfaces generadas — el detector la señala en otras páginas — y además el color iba solo |
| Tarjetas | superficie plana | cristal con brillo y sombra |
| Cabecera del módulo | número suelto | icono del módulo en azulejo + «02 de 08» |

**Imágenes que faltaban**

| Dónde | Qué |
|---|---|
| Marcación de zonas · «Cuando no se confirma» | `05-sin-confirmar.png` **estaba generado y sin usar en ninguna página**. Es el otro desenlace del apartado: la vela cruza, ninguna la supera, la zona sigue viva |
| Riesgo y tamaño · «Cuánto se arriesga» | era **el único módulo sin una sola imagen**. Ahora lleva el gráfico de la distancia al stop repetida al otro lado, y el del setup descartado por pasarse del tope |

Los dos gráficos de riesgo **ya existían y ya estaban en el portal**: aquí
ilustran el tope, en su módulo ilustraban la mecánica y el filtro. Ninguno es
nuevo y ninguno dice nada que no dijera ya.

> 🔵 **Sigue faltando material gráfico.** Hay 13 gráficos de concepto y los 21
> casos de la galería, pero **10 de esos 21 no siguen el estándar visual** que
> el operador validó, así que no se pueden meter en los módulos tal cual.
> Generar gráficos nuevos es posible —**Python ya está instalado en el equipo**,
> al contrario de lo que decía `CLAUDE.md` el 01/09— pero elegir qué sesión real
> ilustra qué concepto es una decisión de metodología: la toma el operador.

**Un rato perdido que conviene no repetir:** la ruta salía sin estilos, como una
lista numerada suelta. No era el CSS: **Vite servía al navegador una versión
vieja del módulo** mientras el HTML llevaba la nueva. Se arregla parando el
servidor y borrando `node_modules/.vite` y `.astro`.

**Comprobado:** un apartado visible a la vez en los ocho módulos, la ruta
marcando hechas y actual, el contador, el pie encadenando dentro del módulo y
saltando al siguiente en la última parada, el botón «atrás» del navegador, sin
desbordes a 375 ni 1440, y el HTML sirviendo los apartados sin ocultar para
quien no tenga JavaScript. Detector limpio en `Modulo.astro`.

### 2026-09-02 · arriba, los apartados del módulo — no otra vez el menú

**Segundo cambio del día, en los ocho módulos a la vez.**

Arriba de cada módulo estaban **otra vez los ocho módulos**, que ya están en el
menú de la izquierda. Y los apartados del módulo vivían en **una columna a la
derecha que desaparecía por debajo de 1200 px**. Resultado: en pantallas
normales no había forma de saltar de apartado a apartado y tocaba bajar a mano.

Ahora arriba van **los apartados de ese módulo**, en una barra que **se queda
pegada** al hacer scroll, y la columna de la derecha se ha quitado — el
contenido gana todo ese ancho.

| Ancho | Cómo se comporta la barra |
|---|---|
| 1440 | los seis apartados del módulo más largo caben en una línea |
| 1000 | se parte en dos líneas; **ninguno queda escondido** |
| 375 | una sola línea que se desliza, con el icono del módulo delante, y el apartado activo se trae solo a la vista |

El nombre del módulo solo sale en la barra **por debajo de 900 px**: por encima,
el menú de la izquierda también queda pegado y ya marca el módulo activo.

**Lo que no se pierde al quitar la barra de los ocho:** la cabecera de cada
módulo ahora dice **«03 de 08»**, y el pie sigue llevando al anterior y al
siguiente.

**Dos detalles que costaron su rato:**

- El apartado marcado iba **uno por detrás** del que se estaba leyendo. Era
  «el primero que se ve»; tenía que ser **«el último cuyo título ya pasó por
  debajo de la barra»**. Los apartados son largos y dos se ven a la vez.
- Al **pulsar** un apartado se marcaba el anterior **por un píxel**: el título
  aterrizaba en 141 px y el corte estaba en 140. Ahora el corte lleva holgura.

**De paso:** `--alto-cabecera` estaba escrito a mano como 3,75 rem cuando la
cabecera mide 69 px, así que el menú lateral se metía 9 px por debajo al hacer
scroll. Ahora se calcula solo desde el relleno y el nuevo `--alto-control`
(44 px, el objetivo táctil), que además retira seis valores sueltos.

**Comprobado:** los ocho módulos con su barra, todos los enlaces apuntando a un
apartado que existe, marcado correcto al pulsar y al hacer scroll libre en seis
posiciones, sin desbordes a 375 / 1000 / 1440, contraste de 5,69 y 11,29, y
chips de 40 px en móvil. El detector no encuentra nada en `Modulo.astro`.

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

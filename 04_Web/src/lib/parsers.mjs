/**
 * Un lector por documento. Todos siguen la misma regla:
 *
 *   NO INTERPRETAN, NO CORRIGEN, NO COMPLETAN.
 *
 * Si la cabecera de un documento dice «11 casos» y hay 21, aqui salen 21.
 * El desajuste se muestra en pantalla; el archivo de origen no se toca.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { marked } from 'marked';
import { documento, json, subfasesSueltas, partirPorEncabezado, tituloLimpio, contarMermaid, CONTENIDO_DIAGRAMAS } from './fuentes.mjs';

// ────────────────────────────────────────────────── markdown en una linea
/**
 * Convierte el markdown de un TITULO a HTML. Solo lo que aparece en titulos:
 * `codigo` y **negrita**. Escapa primero, asi que no puede inyectar nada.
 * No es un renderizador de markdown: los cuerpos se renderizan aparte.
 */
export function tituloAHtml(texto) {
  const escapado = String(texto)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  return escapado
    .replace(/`([^`]+)`/g, '<code>$1</code>')
    .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
}

/** Quita la numeracion manual del principio de un titulo («3 · Falta…»)
 *  cuando la lista ya numera sola. Sin ella saldria el numero dos veces. */
export function sinNumeracion(texto) {
  return String(texto).replace(/^\d+\s*[·.)-]\s*/, '');
}

// ─────────────────────────────────────────────────────────────── version
export function version() {
  const t = documento('TRADING_PLAN_CHAUMER.md');
  const v = t.match(/\*\*Versi[oó]n:\*\*\s*([^\n—-]+)/i);
  const f = t.match(/\*\*[UÚ]ltima actualizaci[oó]n:\*\*\s*([0-9-]+)/i);
  return {
    version: v ? v[1].replace(/\*\*/g, '').trim() : null,
    fecha: f ? f[1].trim() : null,
  };
}

// ─────────────────────────────────────────────────────────────── reglas
export function reglas() {
  return json('reglas.json');
}

/**
 * El valor del punto, en dolares, tal como lo declara el plan.
 *
 * Lo usa la bitacora de backtesting para calcular el P&L, y es la razon de que
 * ese numero NO este escrito a mano en ninguna pagina. Si el plan dejara de
 * declararlo, esto revienta la compilacion a proposito: mejor que se caiga a
 * que el portal se invente un 2,00 que nadie ha confirmado.
 */
export function valorPunto() {
  for (const r of reglas()) {
    for (const c of r.condiciones ?? []) {
      if (c.variable !== 'valor_punto_MNQ') continue;
      const n = Number(String(c.valor).replace(',', '.').match(/[\d.]+/)?.[0]);
      if (Number.isFinite(n) && n > 0) return { valor: n, regla: r.id };
    }
  }
  throw new Error(
    'reglas.json ya no declara valor_punto_MNQ. La bitacora de backtesting ' +
    'saca de ahi el valor del punto y no lo puede inventar.',
  );
}

/**
 * Las siete categorias del plan, en el orden que declara el propio archivo.
 *
 * No se cuentan a ojo ni se renombran aqui: cada regla trae `categoria_nombre`,
 * `categoria_descripcion` y `categoria_orden`, y ese es el orden del dia
 * operativo, no el del tamano del grupo.
 *
 * Zonas es la unica con `subcategoria` — marcado y vigencia. Se devuelve como
 * UNA categoria con sus dos apartados dentro: cuando al operador le surge una
 * duda piensa «es de zonas», no «es de marcado». Pero son 14 de 38, y un
 * filtro que devuelve un tercio del plan no filtra nada, de ahi los apartados.
 */
export function categorias() {
  const mapa = new Map();
  for (const r of reglas()) {
    if (!mapa.has(r.categoria)) {
      mapa.set(r.categoria, {
        id: r.categoria,
        nombre: r.categoria_nombre ?? r.categoria,
        descripcion: r.categoria_descripcion ?? null,
        orden: r.categoria_orden ?? 99,
        n: 0,
        subs: new Map(),
      });
    }
    const c = mapa.get(r.categoria);
    c.n += 1;
    if (r.subcategoria) c.subs.set(r.subcategoria, (c.subs.get(r.subcategoria) || 0) + 1);
  }
  return [...mapa.values()]
    .map((c) => ({ ...c, subs: [...c.subs.entries()].map(([id, n]) => ({ id, n })) }))
    .sort((a, b) => a.orden - b.orden);
}

/**
 * Reglas que viven en una categoria pero contestan tambien desde otra.
 *
 * Declarado a mano porque el archivo de reglas no lo dice: sale de
 * `01_Plan/PROPUESTA_LIMPIEZA_REGLAS.md`, punto 4. Hoy es un solo caso — la
 * regla del rompimiento y la consecucion define como muere una zona Y como se
 * entra, asi que tiene que aparecer en los dos sitios.
 *
 * OJO: es un codigo escrito a mano. Si las reglas se vuelven a renumerar,
 * hay que traducirlo — `scripts/referencias.mjs` avisa si deja de cuadrar.
 */
export const ENLACES_CRUZADOS = new Map([['R-20', ['setup_entrada']]]);

// ─────────────────────────────────────────────────────────────── sub-fases
/** El indice declarado por el propio documento, en su orden (no el numerico). */
export function subfasesDeclaradas() {
  const t = documento('TRADING_PLAN_CHAUMER.md');
  const tabla = t.split(/^## Estado de construcci[oó]n/im)[1] || '';
  const corte = tabla.split(/^---/m)[0] || '';
  const filas = [];
  for (const linea of corte.split(/\r?\n/)) {
    const m = linea.match(/^\|\s*\*{0,2}(F1\.\d{1,2})\*{0,2}\s*\|([^|]*)\|([^|]*)\|/);
    if (m) filas.push({ id: m[1], titulo: m[2].trim(), estado: m[3].trim() });
  }
  return filas;
}

/**
 * Las secciones que existen de verdad en el cuerpo, en el orden del documento.
 *
 * OJO: dentro de una sub-fase hay encabezados del MISMO nivel, porque cada
 * regla es un encabezado de nivel 2. Si se corta por nivel, cada sub-fase se
 * queda en su entradilla y se pierde toda la explicacion. Por eso se corta de
 * un encabezado de sub-fase al siguiente, sea cual sea el nivel de lo que
 * haya en medio.
 */
export function subfasesEnElCuerpo() {
  const t = documento('TRADING_PLAN_CHAUMER.md');
  const lineas = t.split(/\r?\n/);

  const marcas = [];
  let enCodigo = false;
  lineas.forEach((linea, i) => {
    if (/^\s*```/.test(linea)) enCodigo = !enCodigo;
    if (enCodigo) return;
    const m = linea.match(/^(#{1,3})\s+(.*)$/);
    if (!m) return;
    const limpio = tituloLimpio(m[2]);
    const id = limpio.match(/^(F1\.\d{1,2})\b/);
    if (id) marcas.push({ i, nivel: m[1].length, id: id[1], limpio });
  });

  return marcas.map((m, k) => {
    const hasta = k + 1 < marcas.length ? marcas[k + 1].i : lineas.length;
    return {
      id: m.id,
      titulo: m.limpio.replace(/^F1\.\d{1,2}\s*[·-]?\s*/, ''),
      nivel: m.nivel,
      cuerpo: lineas.slice(m.i + 1, hasta).join('\n').trim(),
    };
  });
}

// ─────────────────────────────────────────────────────────────── glosario
/** Un termino es un encabezado de nivel 2 cuya primera palabra va en mayusculas.
 *  Asi quedan fuera «Regla del glosario», «Colores de las velas» y
 *  «Preguntas abiertas heredadas», que son secciones, no terminos. */
export function glosario() {
  const t = documento('GLOSARIO.md');
  return partirPorEncabezado(t, [2])
    .map((b) => ({ ...b, limpio: tituloLimpio(b.titulo) }))
    .filter((b) => {
      const primera = b.limpio.split(/[\s(*]/)[0].replace(/[^\p{L}]/gu, '');
      return primera.length > 1 && primera === primera.toUpperCase();
    })
    .map((b) => ({
      termino: b.limpio.replace(/\s*\*\(.*$/, '').trim(),
      titulo: b.limpio,
      cuerpo: b.cuerpo,
    }));
}

// ─────────────────────────────────────────────────────────────── galeria
export function galeria() {
  const t = documento('GALERIA.md');
  const manifiesto = json('manifiesto.json');
  return partirPorEncabezado(t, [2])
    .filter((b) => /^G-\d{1,2}\b/.test(tituloLimpio(b.titulo)))
    .map((b) => {
      const limpio = tituloLimpio(b.titulo);
      const id = limpio.match(/^(G-\d{1,2})/)[1].toUpperCase();
      const img = manifiesto.casos[id] || null;
      return {
        id,
        titulo: limpio.replace(/^G-\d{1,2}\s*[·-]?\s*/, ''),
        cuerpo: b.cuerpo,
        imagen: img ? img.url : null,
        estandarActual: img ? Boolean(img.actual) : false,
        reglas: [...new Set(b.cuerpo.match(/R-\d{1,2}/g) || [])],
      };
    });
}

// ─────────────────────────────────────────────────────────────── pendientes
/**
 * PENDIENTES.md mezcla niveles a proposito: los pendientes nuevos se anadieron
 * como encabezados de nivel 2, igual que las secciones. Asi que el nivel no
 * distingue nada: lo que convierte un encabezado en pendiente es LLEVAR UN
 * IDENTIFICADOR. Todo lo demas es seccion.
 *
 * Estado: manda la etiqueta del propio titulo (ABIERTO / CERRADO / DESCARTADO
 * / HUECO DECLARADO). Si no la lleva, hereda el de su seccion.
 *
 * Un identificador puede aparecer dos veces cuando se reabrio y se volvio a
 * cerrar. Gana la ULTIMA aparicion, que es la vigente; la anterior se conserva
 * marcada como historica.
 */
// OJO con los limites de palabra: sin \b, «REABIERTO Y VUELTO A CERRAR»
// se leia como ABIERTO y resucitaba un pendiente ya cerrado.
const ETIQUETA_CERRADO = /\b(CERRAD[OA]S?|DESCARTAD[OA]S?|RESUELT[OA]S?)\b|VUELTO A CERRAR/i;
const ETIQUETA_ABIERTO = /\bABIERTO\b|HUECO DECLARADO/i;

/** El tipo lo da la seccion: una desviacion sigue siendo una desviacion
 *  aunque este descartada. El estado lo da la etiqueta del titulo. */
function tipoDeSeccion(seccion) {
  return /DESVIACIONES|CONSECUENCIA ACUMULADA/i.test(seccion || '') ? 'desviacion' : 'pendiente';
}
function estadoDeSeccion(seccion) {
  if (/Cerrad/i.test(seccion || '')) return 'cerrado';
  if (/Abierto/i.test(seccion || '')) return 'abierto';
  return null;
}

export function pendientes() {
  const t = documento('PENDIENTES.md');
  const crudos = [];
  let seccion = null;

  for (const b of partirPorEncabezado(t, [1, 2, 3])) {
    const limpio = tituloLimpio(b.titulo);
    const id = limpio.match(/`?\b([PD]-\d{1,2})\b`?/);
    if (!id) { seccion = limpio; continue; } // encabezado sin identificador = seccion

    const historico = /~~/.test(b.titulo);
    const tipo = tipoDeSeccion(seccion);
    let estado = ETIQUETA_CERRADO.test(limpio) ? 'cerrado'
      : ETIQUETA_ABIERTO.test(limpio) ? 'abierto'
        : estadoDeSeccion(seccion) || 'abierto';
    if (historico) estado = 'cerrado';

    crudos.push({
      id: id[1],
      titulo: limpio,
      seccion,
      cuerpo: b.cuerpo,
      tipo,
      estado,
      historico,
      hueco: /HUECO DECLARADO/i.test(limpio),
    });
  }

  // La ultima aparicion no historica de cada identificador es la vigente.
  const vigentePorId = new Map();
  crudos.forEach((p, i) => { if (!p.historico) vigentePorId.set(p.id, i); });
  return crudos.map((p, i) => ({
    ...p,
    vigente: vigentePorId.get(p.id) === i,
    abierto: p.tipo === 'pendiente' && p.estado === 'abierto' && vigentePorId.get(p.id) === i,
  }));
}

/** Los que siguen abiertos hoy. Es el numero que se ve en el portal. */
export function pendientesAbiertos() {
  return pendientes().filter((p) => p.abierto);
}

/** Decisiones conscientes de apartarse del material del curso. No son dudas
 *  abiertas: estan inventariadas y muchas estan descartadas a proposito. */
export function desviaciones() {
  return pendientes().filter((p) => p.tipo === 'desviacion' && p.vigente);
}

// ─────────────────────────────────────────────────────── contextualizacion
export function contextualizacion() {
  const t = documento('CONTEXTUALIZACION.md');
  const items = [];
  const vistos = new Map();
  for (const b of partirPorEncabezado(t, [2, 3])) {
    const limpio = tituloLimpio(b.titulo);
    const m = limpio.match(/^(C-\d{1,2})\b/);
    if (!m) continue;
    const id = m[1];
    const repetido = vistos.has(id);
    vistos.set(id, (vistos.get(id) || 0) + 1);
    items.push({
      id,
      titulo: limpio.replace(/^C-\d{1,2}\s*[·-]?\s*/, ''),
      cuerpo: b.cuerpo,
      repetido, // el segundo y siguientes usos del mismo identificador
    });
  }
  const duplicados = [...vistos.entries()].filter(([, n]) => n > 1).map(([id]) => id);
  return { items, duplicados };
}

// ─────────────────────────────────────────────────────────────── checklist
export function checklist() {
  const t = documento('CHECKLIST_DIARIA.md');
  return partirPorEncabezado(t, [2]).map((b) => ({
    titulo: tituloLimpio(b.titulo),
    cuerpo: b.cuerpo,
  }));
}

// ─────────────────────────────────────────────────────────────── parametros
/** Nombre -> { valor, equivalencias, donde, desde }. Las reglas citan el
 *  NOMBRE; el valor se resuelve siempre desde aqui, nunca a mano. */
export function parametros() {
  const t = documento('PARAMETROS.md');
  const mapa = new Map();
  let seccion = null;
  let columnas = [];
  for (const linea of t.split(/\r?\n/)) {
    const h = linea.match(/^##\s+(.*)$/);
    if (h) { seccion = tituloLimpio(h[1]); columnas = []; continue; }
    if (!/^\|/.test(linea)) continue;

    const celdas = linea.split('|').slice(1, -1).map((c) => c.trim());
    if (celdas.length < 2) continue;

    // Cabecera de la tabla: se guarda para poder etiquetar cada celda.
    if (/^Par[aá]metro$/i.test(celdas[0])) { columnas = celdas; continue; }
    if (/^[-: ]+$/.test(celdas[0])) continue; // fila separadora

    const nombre = celdas[0].match(/`([A-Z0-9_]+)`/);
    if (!nombre) continue;

    const limpiar = (c) => (c || '').replace(/\*\*/g, '').trim();
    // Las celdas a partir de la segunda, cada una con su encabezado real.
    const detalle = celdas.slice(2)
      .map((c, i) => ({ etiqueta: columnas[i + 2] || '', valor: limpiar(c) }))
      .filter((d) => d.valor && !/^[—–-]+$/.test(d.valor));

    mapa.set(nombre[1], {
      nombre: nombre[1],
      valor: limpiar(celdas[1]),
      detalle,
      resto: detalle.map((d) => d.valor), // compatibilidad con el buscador
      seccion,
    });
  }
  return mapa;
}


// ─────────────────────────────────────────────────────── diagramas
/**
 * Los diagramas del plan vienen escritos en mermaid dentro del documento.
 * scripts/diagramas.mjs ya los dibujo a SVG durante la compilacion; aqui
 * se sustituye el bloque de codigo por el dibujo, pegado en linea.
 *
 * Si un diagrama no se pudo dibujar, se deja el codigo tal cual: es feo,
 * pero es honesto y no rompe la pagina.
 */
const RE_MERMAID = /```mermaid\r?\n([\s\S]*?)```/g;

function insertarDiagramas(md) {
  return String(md).replace(RE_MERMAID, (completo, codigo) => {
    const h = crypto.createHash('sha256').update(codigo.trim()).digest('hex').slice(0, 16);
    const ruta = path.join(CONTENIDO_DIAGRAMAS, h + '.svg');
    if (!fs.existsSync(ruta)) return completo;
    const svg = fs.readFileSync(ruta, 'utf8');
    return '\n\n<figure class="diagrama">' + svg + '</figure>\n\n';
  });
}

// ────────────────────────────────── markdown de los documentos a HTML
/** Renderiza markdown y despues enriquece SOLO el texto, nunca las etiquetas,
 *  para no romper el HTML ya generado ni anidar enlaces dentro de enlaces. */
export function markdownRico(md, opciones = {}) {
  const html = marked.parse(insertarDiagramas(md || ''), { mangle: false, headerIds: false });
  return enriquecerHtml(html, opciones);
}


/** Enunciado de cada regla, para que una referencia dentro del texto diga
 *  lo que es al pasar por encima. Un codigo sin explicacion obliga a
 *  navegar; con el enunciado en el titulo, deja de ser un obstaculo. */
let _enunciados = null;
/**
 * Si una regla existe HOY. Los documentos y las listas de la galeria citan
 * codigos de versiones anteriores del plan; enlazarlos daba fichas que no
 * existen. Comprobado con scripts/enlaces.mjs.
 */
export function hayRegla(id) {
  return existeRegla(id);
}

let _casos = null;
function existeCaso(id) {
  if (!_casos) _casos = new Set(galeria().map((c) => c.id));
  return _casos.has(id);
}

function existeRegla(id) {
  if (!_enunciados) _enunciados = new Map(reglas().map((r) => [r.id, r.enunciado]));
  return _enunciados.has(id);
}

function enunciadoDe(id) {
  if (!_enunciados) {
    _enunciados = new Map(reglas().map((r) => [r.id, r.enunciado]));
  }
  const e = _enunciados.get(id);
  return e ? e.replace(/"/g, '&quot;').slice(0, 180) : id;
}

export function enriquecerHtml(html, { sinEnlaceA } = {}) {
  const params = parametros();
  const nombres = [...params.keys()].sort((a, b) => b.length - a.length);
  const rePar = nombres.length
    ? new RegExp('(^|[^A-Za-z0-9_])(' + nombres.join('|') + ')(?![A-Za-z0-9_])', 'g') : null;

  // Los documentos escriben los parametros entre comillas de codigo, y el
  // recorrido de abajo salta lo que hay dentro de <code> para no estropear
  // ejemplos. Sin este paso previo, la pastilla con el valor vigente casi
  // nunca apareceria en las paginas de documento, que es justo donde hace
  // falta. Se sustituye solo el <code> que contiene EXACTAMENTE un nombre
  // de parametro conocido.
  if (nombres.length) {
    html = String(html).replace(
      new RegExp('<code>(' + nombres.join('|') + ')</code>', 'g'),
      (m, nombre) => '<a class="pastilla-par" href="/parametros#' + nombre + '">'
        + nombre + '<span class="pp-v">' + params.get(nombre).valor + '</span></a>',
    );
  }

  // Lo mismo con las referencias: los documentos escriben `R-13` y `G-11`
  // entre comillas de codigo. Sin esto, el glosario enlazaba una sola.
  html = String(html)
    // Solo se enlaza una regla que EXISTA hoy. Los documentos citan codigos
    // de versiones anteriores —R-39 se elimino, y el 06/09/2026 se renumero
    // todo— y enlazarlos daba fichas inexistentes.
    .replace(/<code>(R-\d{1,2})<\/code>/g, (m, id) =>
      (id === sinEnlaceA || !existeRegla(id)) ? m
        : '<a class="ref" href="/reglas/' + id + '" title="' + enunciadoDe(id) + '">' + id + '</a>')
    .replace(/<code>(G-\d{1,2})<\/code>/g, (m, id) =>
      '<a class="ref" href="/galeria#' + id + '">' + id + '</a>');

  let dentro = 0; // profundidad de <a> y <code>: ahi no se toca nada
  return String(html).split(/(<[^>]+>)/).map((trozo) => {
    if (trozo.startsWith('<')) {
      // svg incluido: inyectar enlaces dentro de un diagrama depende del
      // navegador y no aporta nada. El diagrama se deja tal como se dibujo.
      if (/^<(a|code|pre|svg)\b/i.test(trozo)) dentro++;
      else if (/^<\/(a|code|pre|svg)>/i.test(trozo)) dentro = Math.max(0, dentro - 1);
      return trozo;
    }
    if (dentro > 0) return trozo;

    let s = trozo;
    if (rePar) {
      s = s.replace(rePar, (m, pre, nombre) => {
        const p = params.get(nombre);
        return pre + '<a class="pastilla-par" href="/parametros#' + nombre + '">'
          + nombre + '<span class="pp-v">' + p.valor + '</span></a>';
      });
    }
    s = s.replace(/(^|[^A-Za-z0-9-])(R-\d{1,2})\b/g, (m, pre, id) =>
      (id === sinEnlaceA || !existeRegla(id)) ? m
        : pre + '<a class="ref" href="/reglas/' + id + '" title="' + enunciadoDe(id) + '">' + id + '</a>');
    s = s.replace(/(^|[^A-Za-z0-9-])(G-\d{1,2})\b/g, (m, pre, id) =>
      existeCaso(id)
        ? pre + '<a class="ref" href="/galeria#' + id + '">' + id + '</a>'
        : m);
    return s;
  }).join('');
}

// ─────────────────────────────────────────────────────────────── diagramas
export function diagramas() {
  const partes = [{ archivo: 'TRADING_PLAN_CHAUMER.md', n: contarMermaid(documento('TRADING_PLAN_CHAUMER.md')) }];
  for (const s of subfasesSueltas()) partes.push({ archivo: 'subfases/' + s.archivo, n: contarMermaid(s.texto) });
  return partes.filter((p) => p.n > 0);
}

// ─────────────────────────────────────────────── backtesting + los 4 huecos
/** Las cifras y sus cuatro motivos SIEMPRE juntos. Ninguna pagina puede
 *  pedir una sin la otra: es un solo objeto a proposito. */
export function backtesting() {
  const t = documento('CIERRE_FASE_1.md');
  const total = t.match(/\*\*([-−]?[\d.,]+\s*pts)\*\*/);
  const ops = t.match(/Total\s+(\d+)\s+operaciones/i);
  const huecos = partirPorEncabezado(t, [3])
    .filter((b) => /·\s*`?[FP]1?\.?\d|^\d\s*·/.test(b.titulo) || /^\d+\s*·/.test(tituloLimpio(b.titulo)))
    .map((b) => ({ titulo: tituloLimpio(b.titulo), cuerpo: b.cuerpo }));
  return {
    total: total ? total[1] : null,
    operaciones: ops ? Number(ops[1]) : null,
    huecos,
  };
}


// ──────────────────────────────── la regla dentro del documento largo
/** Mapa id -> { titulo, cuerpo } con la seccion que explica cada regla en
 *  TRADING_PLAN_CHAUMER.md. No todas las reglas tienen una. */
export function seccionesDeReglas() {
  const t = documento('TRADING_PLAN_CHAUMER.md');
  const mapa = new Map();
  for (const b of partirPorEncabezado(t, [2, 3])) {
    const limpio = tituloLimpio(b.titulo);
    const m = limpio.match(/^(R-\d{1,2})\b/);
    if (!m) continue;
    mapa.set(m[1], {
      titulo: limpio.replace(/^R-\d{1,2}\s*[·-]?\s*/, ''),
      cuerpo: b.cuerpo.trim(),
    });
  }
  return mapa;
}

/** Casos de la galeria que citan cada regla. Calculado, no escrito a mano. */
export function casosPorRegla() {
  const mapa = new Map();
  for (const c of galeria()) {
    for (const id of c.reglas) {
      if (!mapa.has(id)) mapa.set(id, []);
      mapa.get(id).push({ id: c.id, titulo: c.titulo });
    }
  }
  return mapa;
}

// ─────────────────────────────────────────── enlazado y pastillas
/**
 * Convierte texto plano del plan en HTML enriquecido:
 *
 *   STOP_MAX  ->  pastilla con el VALOR VIGENTE resuelto de PARAMETROS.md
 *   R-14      ->  enlace a la ficha de esa regla
 *   G-11      ->  enlace al caso de la galeria
 *
 * Asi una regla deja de decir «el tope de stop» sin decir nunca que son
 * 80 puntos. El valor no se escribe a mano en ningun sitio.
 */
export function enriquecer(texto, { sinEnlaceA } = {}) {
  if (texto == null) return '';
  const params = parametros();
  let html = String(texto)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

  // Pastillas de parametro. Se ordenan de mas largo a mas corto para que
  // STOP_MAX no se coma la mitad de otro nombre que lo contenga.
  const nombres = [...params.keys()].sort((a, b) => b.length - a.length);
  if (nombres.length) {
    const re = new RegExp('(^|[^A-Za-z0-9_])(' + nombres.join('|') + ')(?![A-Za-z0-9_])', 'g');
    html = html.replace(re, (m, pre, nombre) => {
      const p = params.get(nombre);
      return pre + '<a class="pastilla-par" href="/parametros#' + nombre + '" title="'
        + nombre + '">' + nombre + '<span class="pp-v">' + p.valor + '</span></a>';
    });
  }

  html = html.replace(/(^|[^A-Za-z0-9-])(R-\d{1,2})\b/g, (m, pre, id) =>
    (id === sinEnlaceA || !existeRegla(id)) ? m
      : pre + '<a class="ref" href="/reglas/' + id + '" title="' + enunciadoDe(id) + '">' + id + '</a>');
  html = html.replace(/(^|[^A-Za-z0-9-])(G-\d{1,2})\b/g, (m, pre, id) =>
    existeCaso(id)
      ? pre + '<a class="ref" href="/galeria#' + id + '">' + id + '</a>'
      : m);

  return html;
}

/** Imagenes asociadas a cada regla, resueltas SOLO por nombre de archivo.
 *  Si una regla no tiene imagen, no hay imagen: ni hueco ni sustituto. */
export function imagenesDeReglas() {
  const m = json('manifiesto.json');
  return new Map(Object.entries(m.reglas || {}));
}

/** Las advertencias en cita que acompanan a cada seccion de PARAMETROS.md.
 *  Son parte del documento y explican por que un numero es lo que es. */
export function notasParametros() {
  const t = documento('PARAMETROS.md');
  const salida = [];
  for (const b of partirPorEncabezado(t, [2])) {
    const citas = b.cuerpo.split(/\n(?=>)/).filter((x) => /^>/.test(x.trim()));
    if (!citas.length) continue;
    salida.push({
      seccion: tituloLimpio(b.titulo),
      html: markdownRico(citas.join('\n\n').replace(/^>\s?/gm, '')),
    });
  }
  return salida;
}

/** El acta de cierre completa, para renderizarla entera. */
export function documentoCierre() {
  return documento('CIERRE_FASE_1.md');
}

/** Quita las referencias de codigo de un titulo ya renderizado.
 *
 *  «El test ciego no se ejecuto · F1.11 · P-29»  ->  «El test ciego no se ejecuto»
 *
 *  Se usa en las pantallas de entendimiento, donde un codigo no aporta nada
 *  y obliga a navegar. En las de detalle el titulo se muestra entero. */
export function sinCodigos(html) {
  return String(html)
    .replace(/\s*[·|]?\s*<code>[^<]*<\/code>/g, '')
    .replace(/\s*·\s*$/, '')
    .trim();
}

/**
 * Los ocho modulos del metodo, en el orden real de la jornada.
 *
 * Este archivo es la unica lista. De aqui salen el menu lateral, la barra de
 * progreso, el enlace «siguiente» del pie de cada modulo y la portada. Si un
 * modulo cambia de nombre o de sitio, se cambia aqui y se propaga solo.
 *
 * El orden NO es tematico, es cronologico: es lo que se hace primero, lo que
 * se hace despues y lo que se hace al final. Un modulo no adelanta trabajo
 * del siguiente.
 */

export const MODULOS = [
  {
    n: 1,
    slug: 'premercado',
    titulo: 'Premercado',
    corto: 'Premercado',
    sub: 'Todo lo que se resuelve antes de que abra el mercado',
    icono: 'moon-stars',
  },
  {
    n: 2,
    slug: 'zonas',
    titulo: 'Marcación de zonas',
    corto: 'Marcación de zonas',
    sub: 'Qué es una zona, de qué vela sale y cómo se dibuja',
    icono: 'rectangle',
  },
  {
    n: 3,
    slug: 'setups',
    titulo: 'Setups operativos',
    corto: 'Setups operativos',
    sub: 'Los dos únicos setups que se operan: IRI y Reingreso',
    icono: 'target',
  },
  {
    n: 4,
    slug: 'jornada',
    titulo: 'Jornada operativa',
    corto: 'Jornada operativa',
    sub: 'El día paso a paso, desde la vela de las 08:31',
    icono: 'clock-countdown',
  },
  {
    n: 5,
    slug: 'entrada',
    titulo: 'Mecánica de entrada',
    corto: 'Mecánica de entrada',
    sub: 'Cómo se coloca la orden, dónde va el stop y dónde el objetivo',
    icono: 'crosshair',
  },
  {
    n: 6,
    slug: 'filtros',
    titulo: 'Filtros: cuándo NO se entra',
    corto: 'Cuándo NO se entra',
    sub: 'Lo que impide colocar la orden y lo que la cancela',
    icono: 'prohibit',
  },
  {
    n: 7,
    slug: 'dentro',
    titulo: 'Dentro de la operación',
    corto: 'Dentro de la operación',
    sub: 'Qué se hace al llenarse la orden, y qué no se hace nunca',
    icono: 'lock-key',
  },
  {
    n: 8,
    slug: 'riesgo',
    titulo: 'Riesgo y tamaño',
    corto: 'Riesgo y tamaño',
    sub: 'Cuánto se arriesga, cuántas veces y con cuántos contratos',
    icono: 'scales',
  },
];

/** El modulo por su direccion, para que la pagina no repita sus propios datos. */
export function modulo(slug) {
  const m = MODULOS.find((x) => x.slug === slug);
  if (!m) throw new Error('No existe el módulo ' + slug);
  return m;
}

/** El anterior y el siguiente. Extremos a null: el recorrido tiene principio y fin. */
export function vecinos(slug) {
  const i = MODULOS.findIndex((x) => x.slug === slug);
  return { anterior: MODULOS[i - 1] ?? null, siguiente: MODULOS[i + 1] ?? null };
}

/**
 * Acceso a las fuentes ya sincronizadas en src/content/.
 *
 * Nadie fuera de src/lib/ lee un archivo. Las paginas piden datos, no texto
 * crudo, para que ningun componente acabe con contenido de trading dentro.
 */
import fs from 'node:fs';
import path from 'node:path';

/**
 * La raiz se busca desde el directorio de trabajo, NO desde import.meta.url:
 * al compilar, Astro empaqueta este modulo dentro de dist/ y la ruta relativa
 * al propio archivo deja de apuntar a src/content/.
 */
function raizDelModulo() {
  let dir = process.cwd();
  for (let i = 0; i < 5; i++) {
    if (fs.existsSync(path.join(dir, 'astro.config.mjs'))) return dir;
    const padre = path.dirname(dir);
    if (padre === dir) break;
    dir = padre;
  }
  return process.cwd();
}

export const CONTENIDO = path.join(raizDelModulo(), 'src', 'content');

/** Donde quedan los SVG ya dibujados por scripts/diagramas.mjs. */
export const CONTENIDO_DIAGRAMAS = path.join(raizDelModulo(), '.diagramas');

const cache = new Map();

/** Lee un documento sincronizado. Falla ruidosamente: un documento que falta
 *  es un error de sincronizacion, no algo que se disimule con texto vacio. */
export function documento(nombre) {
  if (cache.has(nombre)) return cache.get(nombre);
  const ruta = path.join(CONTENIDO, 'plan', nombre);
  if (!fs.existsSync(ruta)) {
    throw new Error('falta ' + nombre + ' en src/content/plan/. Ejecuta: npm run sync');
  }
  const texto = fs.readFileSync(ruta, 'utf8');
  cache.set(nombre, texto);
  return texto;
}

export function json(nombre) {
  const ruta = path.join(CONTENIDO, nombre);
  if (!fs.existsSync(ruta)) {
    throw new Error('falta ' + nombre + ' en src/content/. Ejecuta: npm run sync');
  }
  return JSON.parse(fs.readFileSync(ruta, 'utf8'));
}

export function subfasesSueltas() {
  const dir = path.join(CONTENIDO, 'subfases');
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir)
    .filter((f) => /\.md$/i.test(f))
    .map((f) => ({ archivo: f, texto: fs.readFileSync(path.join(dir, f), 'utf8') }));
}

/** Parte un documento por encabezados de un nivel dado.
 *  Devuelve [{ nivel, titulo, cuerpo }] en el orden del documento. */
export function partirPorEncabezado(texto, niveles = [2]) {
  const lineas = texto.split(/\r?\n/);
  const marca = new RegExp('^(#{' + Math.min(...niveles) + ',' + Math.max(...niveles) + '})\\s+(.*)$');
  const bloques = [];
  let actual = null;
  let enCodigo = false;
  for (const linea of lineas) {
    if (/^\s*```/.test(linea)) enCodigo = !enCodigo;
    const m = enCodigo ? null : linea.match(marca);
    if (m && niveles.includes(m[1].length)) {
      if (actual) bloques.push(actual);
      actual = { nivel: m[1].length, titulo: m[2].trim(), cuerpo: '' };
    } else if (actual) {
      actual.cuerpo += linea + '\n';
    }
  }
  if (actual) bloques.push(actual);
  return bloques;
}

/** Quita emoji y adornos del principio de un titulo, sin tocar su texto. */
export function tituloLimpio(t) {
  // Quita todo lo que no sea letra, digito o backtick por delante: emoji,
  // simbolos y espacios. Deja intacto el texto del titulo.
  return t.replace(/^[^\p{L}\p{N}`~]+/u, '').replace(/^#+\s*/, '').trim();
}

/** Cuenta bloques ```mermaid en un texto. */
export function contarMermaid(texto) {
  return (texto.match(/^\s*```mermaid/gim) || []).length;
}

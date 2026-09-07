/**
 * vista.mjs — abre el portal ya compilado en un navegador sin ventana y mide
 * lo que los otros vigilantes no pueden ver.
 *
 * Los guardianes anteriores leen el codigo fuente: sirven para «nadie escribio
 * la declaracion prohibida». Pero la pared invisible volvio ocho veces porque
 * se cuela por sitios que el codigo no delata — `text-wrap: balance` cortaba
 * los titulos sin ser un tope de ancho, y una fila de pasos quedaba dentada
 * sin que ninguna regla estuviera mal escrita.
 *
 * Esto mide el resultado, no la intencion. Cuatro cosas, en cada pagina:
 *
 *   1. TEXTO CORTADO   un elemento que esconde parte de su contenido.
 *   2. TITULO CORTO    un titular de dos o mas lineas cuya linea mas larga no
 *                      llega al 80 % del ancho disponible = la pared invisible.
 *   3. FILA DENTADA    paradas de la ruta de un modulo con alturas distintas.
 *   4. DESBORDE        la pagina se va por el lado derecho.
 *
 * Usa el navegador que ya trae mermaid-cli: no instala nada nuevo.
 *
 *   node scripts/vista.mjs            todas las paginas
 *   node scripts/vista.mjs /zonas     solo una
 *
 * Sale con codigo 1 si encuentra algo, para que no se publique sin querer.
 */
import fs from 'node:fs';
import path from 'node:path';
import http from 'node:http';
import { fileURLToPath } from 'node:url';
import puppeteer from 'puppeteer';

const WEB = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const DIST = path.join(WEB, 'dist');
const ANCHO = 1440;
const ALTO = 900;

if (!fs.existsSync(DIST)) {
  console.log('vista\n  no hay dist/: compila primero con  npm run build');
  process.exit(1);
}

/** Todas las rutas de dist/ que son una pagina. */
function paginas(dir = DIST, base = '') {
  const salida = [];
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (e.isDirectory()) salida.push(...paginas(path.join(dir, e.name), base + '/' + e.name));
    else if (e.name === 'index.html') salida.push(base === '' ? '/' : base + '/');
  }
  return salida.sort();
}

const TIPOS = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript',
  '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg',
  '.woff2': 'font/woff2', '.json': 'application/json' };

/** Un servidor minimo sobre dist/: el navegador necesita un origen real. */
function servir() {
  return new Promise((ok) => {
    const s = http.createServer((req, res) => {
      let p = path.join(DIST, decodeURIComponent(req.url.split('?')[0]));
      if (fs.existsSync(p) && fs.statSync(p).isDirectory()) p = path.join(p, 'index.html');
      if (!p.startsWith(DIST) || !fs.existsSync(p)) { res.writeHead(404); return res.end(); }
      res.writeHead(200, { 'content-type': TIPOS[path.extname(p)] ?? 'application/octet-stream' });
      fs.createReadStream(p).pipe(res);
    });
    s.listen(0, '127.0.0.1', () => ok([s, s.address().port]));
  });
}

/** Lo que se mide dentro del navegador. */
function medir() {
  const fallos = [];
  const visible = (el) => el.getClientRects().length > 0;

  // 1 · texto escondido dentro de su propia caja
  for (const el of document.querySelectorAll('main *')) {
    if (!visible(el) || el.children.length > 0) continue;
    const t = (el.textContent || '').trim();
    if (!t) continue;
    const cs = getComputedStyle(el);
    const recorta = /hidden|clip/.test(cs.overflow + cs.overflowX + cs.overflowY);
    if (!recorta) continue;
    if (el.scrollHeight > el.clientHeight + 1 || el.scrollWidth > el.clientWidth + 1) {
      fallos.push(['texto cortado', el.tagName.toLowerCase() + '.' + (el.className || '?'), t.slice(0, 60)]);
    }
  }

  // 2 · titular de varias lineas que no llena el ancho: la pared invisible
  for (const h of document.querySelectorAll('main :is(h1, h2, h3)')) {
    if (!visible(h) || !h.firstChild) continue;
    const r = new Range();
    r.selectNodeContents(h);
    // Las cajas hay que agrupar POR RENGLON, y por SOLAPAMIENTO vertical, no
    // por su coordenada: un codigo de regla en linea se dibuja dos pixeles mas
    // abajo que el texto que lo rodea, y agrupando por coordenada cada titulo
    // con codigos parecia partido en dos. Estan en el mismo renglon si sus
    // alturas se pisan mas de la mitad.
    const cajas = [...r.getClientRects()].filter((x) => x.width > 1)
      .sort((a, b) => a.top - b.top);
    const renglones = [];
    for (const c of cajas) {
      const ult = renglones[renglones.length - 1];
      const pisa = ult && Math.min(ult.ab, c.bottom) - Math.max(ult.ar, c.top)
        > Math.min(ult.ab - ult.ar, c.height) / 2;
      if (pisa) {
        ult.i = Math.min(ult.i, c.left); ult.d = Math.max(ult.d, c.right);
        ult.ar = Math.min(ult.ar, c.top); ult.ab = Math.max(ult.ab, c.bottom);
      } else renglones.push({ i: c.left, d: c.right, ar: c.top, ab: c.bottom });
    }
    const lineas = renglones.map((l) => l.d - l.i);
    if (lineas.length < 2) continue;                      // una sola linea: nada que juzgar
    const disponible = h.getBoundingClientRect().width;
    const masLarga = Math.max(...lineas);
    if (disponible > 240 && masLarga < disponible * 0.8) {
      fallos.push(['titulo corto (pared invisible)',
        Math.round((masLarga / disponible) * 100) + ' % del ancho',
        (h.textContent || '').trim().slice(0, 60)]);
    }
  }

  // 3 · la ruta de un modulo, dentada
  const paradas = [...document.querySelectorAll('.ruta-i')];
  if (paradas.length > 1) {
    const alturas = new Set(paradas.map((li) => Math.round(li.getBoundingClientRect().height)));
    if (alturas.size > 1) {
      fallos.push(['fila de pasos dentada', [...alturas].join(' / ') + ' px', 'la ruta del modulo']);
    }
  }

  // 4 · la pagina se va por el lado
  if (document.documentElement.scrollWidth > window.innerWidth + 1) {
    fallos.push(['la pagina desborda a lo ancho',
      document.documentElement.scrollWidth + ' > ' + window.innerWidth + ' px', '']);
  }
  return fallos;
}

// ── a correr ───────────────────────────────────────────────────────────
const soloUna = process.argv[2];
const rutas = soloUna ? [soloUna.endsWith('/') ? soloUna : soloUna + '/'] : paginas();
const [servidor, puerto] = await servir();
const nav = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
const hoja = await nav.newPage();
await hoja.setViewport({ width: ANCHO, height: ALTO });

const fallos = [];
for (const ruta of rutas) {
  await hoja.goto('http://127.0.0.1:' + puerto + ruta, { waitUntil: 'networkidle0' });
  for (const f of await hoja.evaluate(medir)) fallos.push([ruta, ...f]);
}

await nav.close();
servidor.close();

console.log('vista (navegador, ' + ANCHO + ' px)');
console.log('  páginas       ' + rutas.length);

if (fallos.length) {
  console.log('  FALLOS        ' + fallos.length + '\n');
  for (const [ruta, que, dato, texto] of fallos) {
    console.log('  ✗ ' + ruta + '  — ' + que);
    console.log('      ' + dato + (texto ? '   «' + texto + '»' : ''));
  }
  console.log('');
  process.exit(1);
}
console.log('  fallos        0');

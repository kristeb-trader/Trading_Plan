// @ts-check
import { defineConfig } from 'astro/config';

// Salida estatica: el plan es contenido, no aplicacion. Las unicas partes
// dinamicas (las observaciones de Alfredo) viven en funciones de Cloudflare,
// fuera de este build.
export default defineConfig({
  output: 'static',
  outDir: './dist',
  srcDir: './src',
  publicDir: './public',
  build: { format: 'directory' },
  markdown: {
    // Sin resaltado de sintaxis: en el plan no hay codigo, hay tablas y prosa.
    syntaxHighlight: false,
  },
});

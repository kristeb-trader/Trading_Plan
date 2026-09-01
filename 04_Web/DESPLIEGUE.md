# Publicar el portal

**Decidido por el operador el 02/09/2026:** entrada libre. Alfredo abre una
dirección y está dentro. Sin código, sin correo, sin contraseña.

El repositorio **no se conecta a Cloudflare**. Se compila en el equipo y se
suben solo los archivos de `dist/`. El código se queda privado en GitHub.

Todo vive en Cloudflare: la web en Pages y las observaciones en D1. Una sola
cuenta, sin claves viajando entre servicios.

---

## Una sola vez

Desde `04_Web/`, en una terminal.

### 1 · Entrar en Cloudflare  ✅ HECHO

```
npx wrangler login
```

Abre el navegador y pide autorizar. Es la cuenta que ya tienes.

### 2 · Crear la base  ✅ HECHA. database_id ya está en wrangler.toml

```
npx wrangler d1 create trading-plan-observaciones
```

Devuelve un `database_id`. **Pégalo en `wrangler.toml`**, sustituyendo
`PENDIENTE_DE_CREAR`.

### 3 · Crear la tabla  ✅ HECHA y verificada de extremo a extremo

```
npx wrangler d1 execute trading-plan-observaciones --remote --file=./d1/0001_observaciones.sql
```

### 4 · Inventar la clave de operador

Cualquier cadena larga que no sea adivinable. Por ejemplo la que salga de:

```
node -e "console.log(require('crypto').randomBytes(24).toString('base64url'))"
```

Guárdala. Es la que te deja **responder, marcar, exportar y borrar**.

### 5 · Publicar  ✅ HECHO el 02/09/2026

```
npm run build
npx wrangler pages deploy dist --project-name=trading-plan
```

La primera vez pregunta si crear el proyecto: acepta. Al terminar imprime la
dirección, del tipo `https://trading-plan-18i.pages.dev`.

> Las direcciones `.pages.dev` son únicas en el mundo. Si `trading-plan` está
> cogido, elige otro nombre y úsalo también en `--project-name`.

### 6 · Guardar la clave como secreto

```
npx wrangler pages secret put CLAVE_OPERADOR --project-name=trading-plan
```

Pega la clave del paso 4. **No va al repositorio ni al navegador.**

---

## Los dos enlaces

**El de Alfredo**, con su nombre dentro para que sus observaciones queden
firmadas sin que él escriba nada:

```
https://trading-plan-18i.pages.dev/?a=Alfredo
```

Lo abre una vez y su navegador lo recuerda. Después le vale la dirección a secas.

**El tuyo**, que abre la pantalla de observaciones con permiso para responder,
marcar, exportar y borrar:

```
https://trading-plan-18i.pages.dev/observaciones?k=TU_CLAVE
```

También se recuerda. **No lo compartas**: quien lo tenga puede responder y
borrar en tu nombre.

---

## Cada vez que cambie el plan

```
npm run build
npx wrangler pages deploy dist --project-name=trading-plan
```

Eso es todo. `build` sincroniza `01_Plan/` y `02_Assets/`, así que cualquier
cambio en el plan entra solo.

---

## Consultar las observaciones sin abrir el portal

```
npx wrangler d1 execute trading-plan-observaciones --remote --command="SELECT creada_en, autor, ancla_tipo, ancla_id, estado, texto FROM observaciones ORDER BY creada_en DESC LIMIT 50"
```

---

## Si algún día hay que cerrar la puerta

El portal es de entrada libre por decisión del operador. Si la dirección se
filtra y hace falta cerrarlo:

**Cloudflare** → **Zero Trust** → **Access** → **Applications** → añadir la
aplicación apuntando a la dirección del portal, con una política de lista
blanca de correos.

Dos minutos, sin tocar código ni volver a publicar.

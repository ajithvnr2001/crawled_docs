---
url: https://developers.cloudflare.com/workers/framework-guides/web-apps/remix/
title: Remix 3 \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-11-13T09:17:05.736009+00:00
---

# Remix 3 · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/framework-guides/web-apps/remix/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

Framework guides

  4. /Web applications
  5. /Remix 3



# Remix 3

Last updated Nov 12, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesCreate and deploy a Remix appStream a FrameNext steps

Create a [Remix 3 ↗︎](https://remix.run/) application with [Vite+ ↗︎](https://viteplus.dev/guide/) and deploy it using the [Cloudflare CLI (`cf`)](https://developers.cloudflare.com/cf/). The application renders HTML, hydrates a counter, and reads a [Workers binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/).

This guide combines the third-party [Pitlane Remix Vite plugin ↗︎](https://pitlane.tools/guides/vite-plugin) with the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/). Pitlane handles Remix components and browser assets. The Cloudflare plugin runs the server in Workers.

For Remix v2 applications, refer to the [React Router guide](https://developers.cloudflare.com/workers/framework-guides/web-apps/react-router/).

## Prerequisites

  * Node.js 24 or later
  * [Vite+ ↗︎](https://viteplus.dev/guide/#install-vp-globally)
  * [Cloudflare CLI](https://developers.cloudflare.com/cf/get-started/#install-cf)



## Create and deploy a Remix app

  1. **Create a project**
         
         cf init my-remix-app --package-manager pnpm --no-install
         cd my-remix-app

Replace `package.json` with the following configuration:

package.jsonjson
         
         {
           "name": "my-remix-app",
           "private": true,
           "type": "module",
           "scripts": {
             "dev": "vp dev",
             "build": "vp build",
             "deploy": "cf deploy",
             "check": "cf workers types && vp check"
           },
           "dependencies": {
             "@pitlane/assets": "0.2.1",
             "remix": "3.2.0"
           },
           "devDependencies": {
             "@cloudflare/vite-plugin": "2.0.0-beta.v.15",
             "@pitlane/vite-plugin-remix": "0.9.1",
             "cf": "1.0.0-beta.30",
             "typescript": "7.0.2",
             "vite": "npm:@voidzero-dev/vite-plus-core@1.6.0",
             "vite-plus": "1.6.0"
           }
         }

Create `pnpm-workspace.yaml` to use the same Vite+ core throughout the project:

pnpm-workspace.yamlyaml
         
         overrides:
           "vite@*": "npm:@voidzero-dev/vite-plus-core@1.6.0"
         allowBuilds:
           esbuild: true
           workerd: true

  2. **Configure the Worker and Vite+**

Replace `cloudflare.config.ts`. The `WORLD` text binding supplies the greeting:

cloudflare.config.jsjs
         
         import { bindings, defineConfig } from "cf/config";
         import * as entrypoint from "./src/index.ts" with { type: "cf-worker" };
         
         export default defineConfig({
         	worker: {
         		name: "my-remix-app",
         		compatibilityDate: "2026-11-13",
         		compatibilityFlags: ["nodejs_compat"],
         		entrypoint,
         		env: {
         			WORLD: bindings.text("World"),
         		},
         	},
         });

cloudflare.config.tsts
         
         import { bindings, defineConfig } from "cf/config";
         import * as entrypoint from "./src/index.ts" with { type: "cf-worker" };
         
         export default defineConfig({
           worker: {
             name: "my-remix-app",
             compatibilityDate: "2026-11-13",
             compatibilityFlags: ["nodejs_compat"],
             entrypoint,
             env: {
               WORLD: bindings.text("World"),
             },
           },
         });

Replace `vite.config.ts` to configure both plugins:

vite.config.jsjs
         
         import { cloudflare } from "@cloudflare/vite-plugin";
         import { remix } from "@pitlane/vite-plugin-remix";
         import { defineConfig } from "vite-plus";
         
         export default defineConfig({
         	plugins: [
         		remix({
         			serverEntry: "src/index.ts",
         			clientEntry: "src/entry.browser.ts",
         			serverHandler: false,
         			assets: {
         				allowFiles: [
         					"src/entry.browser.ts",
         					"src/**/public/**",
         					"src/routes.ts",
         				],
         				allowPackages: ["remix", "@pitlane/vite-plugin-remix"],
         				denyFiles: ["**/*.server.*", "**/*.test.*"],
         			},
         		}),
         		cloudflare({ viteEnvironment: { name: "ssr" } }),
         	],
         	oxc: {
         		jsx: {
         			runtime: "automatic",
         			importSource: "remix/component",
         		},
         	},
         	lint: { options: { typeAware: true, typeCheck: true } },
         });

vite.config.tsts
         
         import { cloudflare } from "@cloudflare/vite-plugin";
         import { remix } from "@pitlane/vite-plugin-remix";
         import { defineConfig } from "vite-plus";
         
         export default defineConfig({
           plugins: [
             remix({
               serverEntry: "src/index.ts",
               clientEntry: "src/entry.browser.ts",
               serverHandler: false,
               assets: {
                 allowFiles: ["src/entry.browser.ts", "src/**/public/**", "src/routes.ts"],
                 allowPackages: ["remix", "@pitlane/vite-plugin-remix"],
                 denyFiles: ["**/*.server.*", "**/*.test.*"],
               },
             }),
             cloudflare({ viteEnvironment: { name: "ssr" } }),
           ],
           oxc: {
             jsx: {
               runtime: "automatic",
               importSource: "remix/component",
             },
           },
           lint: { options: { typeAware: true, typeCheck: true } },
         });

Replace `tsconfig.json` to configure Remix JSX and browser types:

tsconfig.jsonjson
         
         {
           "compilerOptions": {
             "target": "es2024",
             "lib": ["es2024"],
             "module": "preserve",
             "moduleResolution": "bundler",
             "types": ["vite/client"],
             "strict": true,
             "noEmit": true,
             "allowImportingTsExtensions": true,
             "isolatedModules": true,
             "verbatimModuleSyntax": true,
             "skipLibCheck": true,
             "jsx": "react-jsx",
             "jsxImportSource": "remix/component"
           },
           "include": [
             "src",
             "cloudflare.config.ts",
             "vite.config.ts",
             ".cloudflare/types"
           ]
         }

  3. **Connect the browser assets**

Create `src/assets.ts` to resolve browser modules and stylesheets:

src/assets.jsjs
         
         import { createAssetResolver } from "@pitlane/assets";
         import manifest from "@pitlane/assets/manifest";
         
         export const assets = createAssetResolver(manifest);
         export const scriptEntry = await assets.getScriptEntry("src/entry.browser.ts");
         export const stylesheets = await assets.getStylesheets("src/index.ts");

src/assets.tsts
         
         import { createAssetResolver } from "@pitlane/assets";
         import manifest from "@pitlane/assets/manifest";
         
         export const assets = createAssetResolver(manifest);
         export const scriptEntry = await assets.getScriptEntry("src/entry.browser.ts");
         export const stylesheets = await assets.getStylesheets("src/index.ts");

Create `src/entry.browser.ts` to start Remix in the browser:

src/entry.browser.jsjs
         
         import { run } from "remix/component";
         
         export const app = run({
         	async loadModule(moduleUrl, exportName) {
         		const module = await import(/* @vite-ignore */ moduleUrl);
         		const component = module[exportName];
         		if (typeof component !== "function") {
         			throw new Error(`Missing client entry: ${moduleUrl}#${exportName}`);
         		}
         		return component;
         	},
         });
         
         app.addEventListener("error", (event) => console.error(event.error));
         await app.ready();
         
         if (import.meta.hot) {
         	const { revalidate } = await import("@pitlane/vite-plugin-remix/hmr");
         	import.meta.hot.on("server:update", () => revalidate(app));
         }

src/entry.browser.tsts
         
         import { run } from "remix/component";
         
         export const app = run({
           async loadModule(moduleUrl, exportName) {
             const module = await import(/* @vite-ignore */ moduleUrl);
             const component = module[exportName];
             if (typeof component !== "function") {
               throw new Error(`Missing client entry: ${moduleUrl}#${exportName}`);
             }
             return component;
           },
         });
         
         app.addEventListener("error", (event) => console.error(event.error));
         await app.ready();
         
         if (import.meta.hot) {
           const { revalidate } = await import("@pitlane/vite-plugin-remix/hmr");
           import.meta.hot.on("server:update", () => revalidate(app));
         }

Create `src/document.tsx` to load the entry, import map, and stylesheets:

src/document.tsxtsx
         
         import type { Handle, RemixNode } from "remix/component";
         import { ImportMap } from "remix/component/server";
         import { scriptEntry, stylesheets } from "./assets.ts";
         
         export function Document(handle: Handle<{ children?: RemixNode }>) {
           return () => (
             <html lang="en">
               <head>
                 <meta charset="utf-8" />
                 <meta
                   name="viewport"
                   content="width=device-width, initial-scale=1"
                 />
                 <title>Remix on Cloudflare</title>
                 {stylesheets.map((href) => (
                   <link key={href} rel="stylesheet" href={href} />
                 ))}
                 <ImportMap value={scriptEntry.importMap} />
                 {scriptEntry.preloads.map((href) => (
                   <link key={href} rel="modulepreload" href={href} />
                 ))}
                 <script type="module" src={scriptEntry.href} />
               </head>
               <body>{handle.props.children}</body>
             </html>
           );
         }

  4. **Add an interactive component and routes**

Create `src/public/counter.tsx`. Keep browser components and their local dependencies in a `public/` directory:

src/public/counter.tsxtsx
         
         import { clientEntry, on, type Handle } from "remix/component";
         
         export const Counter = clientEntry(
           import.meta.url,
           function Counter(handle: Handle) {
             let count = 0;
             return () => (
               <button
                 type="button"
                 mix={on("click", async () => {
                   count++;
                   await handle.update();
                 })}
               >
                 Count: {count}
               </button>
             );
           },
         );

Use a named export and call `clientEntry` directly. Pitlane rewrites the source identity and maps it to a browser asset. Hydration then works independently of the bundled Worker file paths.

Create `src/router.tsx`. Pass the asset resolver to `render()`:

src/router.tsxtsx
         
         import { env } from "cloudflare:workers";
         import { render } from "remix/middleware/render";
         import { createRouter } from "remix/router";
         import { assets } from "./assets.ts";
         import { Document } from "./document.tsx";
         import { Counter } from "./public/counter.tsx";
         
         export const router = createRouter({ middleware: [render({ assets })] });
         
         router.get("/", ({ render }) =>
           render(
             <Document>
               <h1>Hello {env.WORLD}!</h1>
               <Counter />
               <a href="/api/hello">Get the greeting as JSON</a>
             </Document>,
           ),
         );
         
         router.get("/api/hello", () =>
           Response.json({ message: `Hello ${env.WORLD}!` }),
         );

Replace `src/index.ts` to pass incoming requests to Remix:

src/index.jsjs
         
         import { router } from "./router.tsx";
         
         export default {
         	fetch(request) {
         		return router.fetch(request);
         	},
         };

src/index.tsts
         
         import { router } from "./router.tsx";
         
         export default {
           fetch(request: Request): Promise<Response> {
             return router.fetch(request);
           },
         } satisfies ExportedHandler;

Project structure

     * my-remix-app/ 
       * src/ 
         * public/ 
           * counter.tsx
         * assets.ts
         * document.tsx
         * entry.browser.ts
         * index.ts
         * router.tsx
       * cloudflare.config.ts
       * package.json
       * pnpm-workspace.yaml
       * tsconfig.json
       * vite.config.ts

  5. **Develop locally**
         
         vp install
         vp dev

Open `http://localhost:5173/` and select **Count: 0**. The counter changes to **Count: 1** without reloading the page.

Edit the greeting in `src/router.tsx`. The page updates while preserving the counter value.

In another terminal, test the JSON route:
         
         curl http://localhost:5173/api/hello
         
         { "message": "Hello World!" }

  6. **Deploy your project**

Format and check the project, then sign in and deploy:
         
         vp check --fix
         vp run check
         cf auth login
         cf deploy

`cf deploy` builds with Vite+ and prints your `workers.dev` URL. If prompted, select your Cloudflare account.

Open the deployed URL and select the counter. Test the JSON route, replacing `<YOUR_SUBDOMAIN>` with your account subdomain:
         
         curl https://my-remix-app.<YOUR_SUBDOMAIN>.workers.dev/api/hello
         
         { "message": "Hello World!" }




## Stream a Frame

Add these imports and routes to `src/router.tsx`. The Frame streams server-rendered content containing another interactive counter:

src/router.tsxtsx
    
    
    import { Frame } from "remix/component";
    
    router.get("/frames", ({ render }) =>
    	render(
    		<Document>
    			<h1>Streamed content</h1>
    			<Frame src="/panel" fallback={<p>Loading panel...</p>} />
    		</Document>,
    	),
    );
    
    router.get("/panel", ({ render }) =>
    	render(
    		<section>
    			<h2>Hello {env.WORLD}!</h2>
    			<Counter />
    		</section>,
    	),
    );

Open `/frames` locally or after deploying. Select **Count: 0** inside the streamed content to confirm that it hydrates.

## Next steps

  * Add browser packages or shared files to `assets.allowPackages` or `assets.allowFiles` in `vite.config.ts`.
  * Configure more [bindings in `cloudflare.config.ts`](https://developers.cloudflare.com/cf/projects/cloudflare-config/#declare-bindings).
  * Add [forms, navigation, and sessions ↗︎](https://github.com/remix-run/remix/tree/main/packages/remix/guides).



[PreviousReact Router (formerly Remix)](https://developers.cloudflare.com/workers/framework-guides/web-apps/react-router/)[NextNext.js](https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/framework-guides/web-apps/remix.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

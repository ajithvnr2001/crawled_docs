---
url: https://developers.cloudflare.com/browser-run/how-to/browser-run-with-do/
title: Deploy a Browser Run Worker with Durable Objects \u00b7 Cloudflare Browser Run docs
method: scrapling+scrapegraph
fetched_at: 2026-10-13T08:48:33.458017+00:00
---

# Deploy a Browser Run Worker with Durable Objects · Cloudflare Browser Run docs

> Source: https://developers.cloudflare.com/browser-run/how-to/browser-run-with-do/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Browser Run](https://developers.cloudflare.com/browser-run/)
  3. /Tutorials
  4. /Deploy a Browser Run Worker with Durable Objects



# Deploy a Browser Run Worker with Durable Objects

Last updated Oct 12, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Create a Worker project2\. Install Puppeteer3\. Create a R2 bucket4\. Configure your Wrangler configuration file5\. Code6\. Test7\. DeployRelated resources

By following this guide, you will create a Worker that uses the Browser Run API along with [Durable Objects](https://developers.cloudflare.com/durable-objects/) to take screenshots from web pages and store them in [R2](https://developers.cloudflare.com/r2/).

Using Durable Objects to persist browser sessions improves performance by eliminating the time that it takes to spin up a new browser session. Since Durable Objects re-uses sessions, it reduces the number of concurrent sessions needed.

  1. Sign up for a [Cloudflare account ↗︎](https://dash.cloudflare.com/sign-up/workers-and-pages).
  2. Install [`Node.js` ↗︎](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).



Node.js version manager

Use [Vite+ (`vp env`) ↗︎](https://viteplus.dev/guide/env) to install and manage Node.js versions.

For supported Node.js versions, refer to the [Wrangler system requirements](https://developers.cloudflare.com/workers/wrangler/install-and-update/#install-wrangler).

## 1\. Create a Worker project

[Cloudflare Workers](https://developers.cloudflare.com/workers/) provides a serverless execution environment that allows you to create new applications or augment existing ones without configuring or maintaining infrastructure. Your Worker application is a container to interact with a headless browser to do actions, such as taking screenshots.

Create a new Worker project named `browser-worker` by running:

npmyarnpnpm
    
    
    npm create cloudflare@latest -- browser-worker
    
    
    yarn create cloudflare browser-worker
    
    
    pnpm create cloudflare@latest browser-worker

## 2\. Install Puppeteer

In your `browser-worker` directory, install Cloudflare’s [fork of Puppeteer](https://developers.cloudflare.com/browser-run/puppeteer/):

npmyarnpnpmbun
    
    
    npm i -D @cloudflare/puppeteer
    
    
    yarn add -D @cloudflare/puppeteer
    
    
    pnpm add -D @cloudflare/puppeteer
    
    
    bun add -d @cloudflare/puppeteer

## 3\. Create a R2 bucket

Create two R2 buckets, one for production, and one for development.

Note that bucket names must be lowercase and can only contain dashes.
    
    
    wrangler r2 bucket create screenshots
    wrangler r2 bucket create screenshots-test

To check that your buckets were created, run:
    
    
    wrangler r2 bucket list

After running the `list` command, you will see all bucket names, including the ones you have just created.

## 4\. Configure your Wrangler configuration file

Configure your `browser-worker` project's [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) by adding a browser [binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/) and a [Node.js compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#nodejs-compatibility-flag). Browser bindings allow for communication between a Worker and a headless browser which allows you to do actions such as taking a screenshot, generating a PDF and more.

Update your Wrangler configuration file with the Browser Run API binding, the R2 bucket you created and a Durable Object:

Note

Your Worker configuration must include the `nodejs_compat` compatibility flag and a `compatibility_date` of 2025-09-15 or later.
    
    
    {
    	"$schema": "./node_modules/wrangler/config-schema.json",
    	"name": "rendering-api-demo",
    	"main": "src/index.js",
    	"upload_source_maps": true,
    	// Set this to today's date
    	"compatibility_date": "2026-10-13",
    	"compatibility_flags": ["nodejs_compat"],
    	"account_id": "<ACCOUNT_ID>",
    	// Browser Run API binding
    	"browser": {
    		"binding": "MYBROWSER",
    	},
    	// Bind an R2 Bucket
    	"r2_buckets": [
    		{
    			"binding": "BUCKET",
    			"bucket_name": "screenshots",
    			"preview_bucket_name": "screenshots-test",
    		},
    	],
    	// Binding to a Durable Object
    	"durable_objects": {
    		"bindings": [
    			{
    				"name": "BROWSER",
    				"class_name": "Browser",
    			},
    		],
    	},
    	"migrations": [
    		{
    			"tag": "v1", // Should be unique for each entry
    			"new_sqlite_classes": [
    				// Array of new classes
    				"Browser",
    			],
    		},
    	],
    }
    
    
    "$schema" = "./node_modules/wrangler/config-schema.json"
    name = "rendering-api-demo"
    main = "src/index.js"
    upload_source_maps = true
    # Set this to today's date
    compatibility_date = "2026-10-13"
    compatibility_flags = [ "nodejs_compat" ]
    account_id = "<ACCOUNT_ID>"
    
    [browser]
    binding = "MYBROWSER"
    
    [[r2_buckets]]
    binding = "BUCKET"
    bucket_name = "screenshots"
    preview_bucket_name = "screenshots-test"
    
    [[durable_objects.bindings]]
    name = "BROWSER"
    class_name = "Browser"
    
    [[migrations]]
    tag = "v1"
    new_sqlite_classes = [ "Browser" ]

## 5\. Code

The code below uses Durable Object to instantiate a browser using Puppeteer. It then opens a series of web pages with different resolutions, takes a screenshot of each, and uploads it to R2.

The Durable Object keeps a browser session open for 60 seconds after last use. If a browser session is open, any requests will re-use the existing session rather than creating a new one. Update your Worker code by copy and pasting the following:
    
    
    import { DurableObject } from "cloudflare:workers";
    import * as puppeteer from "@cloudflare/puppeteer";
    
    export default {
    	async fetch(request, env) {
    		const obj = env.BROWSER.getByName("browser");
    
    		// Send a request to the Durable Object, then await its response
    		const resp = await obj.fetch(request);
    
    		return resp;
    	},
    };
    
    const KEEP_BROWSER_ALIVE_IN_SECONDS = 60;
    
    export class Browser extends DurableObject {
    	browser;
    	keptAliveInSeconds = 0;
    	storage;
    
    	constructor(state, env) {
    		super(state, env);
    		this.storage = state.storage;
    	}
    
    	async fetch(request) {
    		// Screen resolutions to test out
    		const width = [1920, 1366, 1536, 360, 414];
    		const height = [1080, 768, 864, 640, 896];
    
    		// Use the current date and time to create a folder structure for R2
    		const nowDate = new Date();
    		const coeff = 1000 * 60 * 5;
    		const roundedDate = new Date(
    			Math.round(nowDate.getTime() / coeff) * coeff,
    		).toString();
    		const folder = roundedDate.split(" GMT")[0];
    
    		// If there is a browser session open, re-use it
    		if (!this.browser || !this.browser.isConnected()) {
    			console.log(`Browser DO: Starting new instance`);
    			try {
    				this.browser = await puppeteer.launch(this.env.MYBROWSER);
    			} catch (e) {
    				console.log(
    					`Browser DO: Could not start browser instance. Error: ${e}`,
    				);
    			}
    		}
    
    		// Reset keptAlive after each call to the DO
    		this.keptAliveInSeconds = 0;
    
    		// Check if browser exists before opening page
    		if (!this.browser)
    			return new Response("Browser launch failed", { status: 500 });
    
    		const page = await this.browser.newPage();
    
    		// Take screenshots of each screen size
    		for (let i = 0; i < width.length; i++) {
    			await page.setViewport({ width: width[i], height: height[i] });
    			await page.goto("https://workers.cloudflare.com/");
    			const fileName = `screenshot_${width[i]}x${height[i]}`;
    			const sc = await page.screenshot();
    
    			await this.env.BUCKET.put(`${folder}/${fileName}.jpg`, sc);
    		}
    
    		// Close tab when there is no more work to be done on the page
    		await page.close();
    
    		// Reset keptAlive after performing tasks to the DO
    		this.keptAliveInSeconds = 0;
    
    		// Set the first alarm to keep DO alive
    		const currentAlarm = await this.storage.getAlarm();
    		if (currentAlarm == null) {
    			console.log(`Browser DO: setting alarm`);
    			const TEN_SECONDS = 10 * 1000;
    			await this.storage.setAlarm(Date.now() + TEN_SECONDS);
    		}
    
    		return new Response("success");
    	}
    
    	async alarm() {
    		this.keptAliveInSeconds += 10;
    
    		// Extend browser DO life
    		if (this.keptAliveInSeconds < KEEP_BROWSER_ALIVE_IN_SECONDS) {
    			console.log(
    				`Browser DO: has been kept alive for ${this.keptAliveInSeconds} seconds. Extending lifespan.`,
    			);
    			await this.storage.setAlarm(Date.now() + 10 * 1000);
    			// You can ensure the ws connection is kept alive by requesting something
    			// or just let it close automatically when there is no work to be done
    			// for example, `await this.browser.version()`
    		} else {
    			console.log(
    				`Browser DO: exceeded life of ${KEEP_BROWSER_ALIVE_IN_SECONDS}s.`,
    			);
    			if (this.browser) {
    				console.log(`Closing browser.`);
    				await this.browser.close();
    			}
    		}
    	}
    }

[ Run Worker in Playground ](https://workers.cloudflare.com/playground#LYVwNgLglgDghgJwgegGYHsHALQBM4RwDcABAEbogB2+CAngLzbPYZb6HbW5QDGU2AAwBmAOwAmAKwAOKeMEA2AIwAuFizbAOcLjT4CREmXMVKAsACgAwuioQApnewARKAGcY6N1Gi2VJTTwCYhIqOGB7BgAiKBp7AA8AOgArNyjSVCgwR3DImLik1KjLGztHCGwAFToYe384GBgwPgIoW2RkuAA3ODdeBFgIAGpgdFxwe0tLKGBPJBIAbxJnEAQ4MmyAeTJk+14IEgBfAIR0YBIo3jBKXFQwRDqAd0wAa3sENKILGbmDgCoSL0SDAQI17A53iczhcAAJXG53B7IEFgiEIdIWCwJX4kXD2VBwcAHBYWACQvToVF4AXBvAAFgAKBD2ACOIHsbggABoSI4ugBKRZk0m8WyckjoHYkBi8qhdRIAIQASpsAOoAZQAokrEgBzcEKugAOVyDKiZFOjzc7yi-K+wuQyBI6scuEBJGZbI5Bwg6BIEDp9mWq3W2RI212+x5AccgMecB8JB8bg9HM8VGtwtFGYOzI80rjCYOkuSiVQtMZnvZnLtmNJpOZEFWVFTHi+pMOXIsh3t2fFAGlNZqAAoAfWVaq1StHAEEADIASQAaprRwujaOtVZNkbnOqCwpBPbsZgDldeimFZbrQhefEHDQUys1ht7BG9sSyRb0Fb3u23jAEAzs0XT2AuVAutmuApjKR5kpymBwPq9oimKEAICA+yYAynIEPYPJ8oKJL1m4oLvDhhAOARcq1vWAbuIkCFrPqBa4Q4jG+sx9jtocdYUlSNIQPSTKstWEBEQ6Trqv09ixnm6BgCAvgZv6foOOKlAQFmaEkI8UC4AGBYANpKAAnPIPJKMICgKJZkjWTy1mCDyAAsSguQAuu2qE5iQgZQLqdIHDKJmCNIzkkKICjSDy0gKC5PLxRF0imQoXl1qSjokAAqta-qBiQvCrMydi4nhgI0P6MxBr6hXMuVcABApeK3pyGH7KsQZsCQSriNpvlUD+zjlTKVD2I8yx4QytE+eKor4qgBZKIIK0kACh5rSQkjeX2uaUHEuDDQ4BZjRNR32AywqkgAsgQdKJKc3AMoNjznXq4KVNV00kE682oKggoAn9qBdvW-KJL66robEurTTtOkYGALUFo9B1vR4zQQGaJAAOLXZUtpGYI6WSSQC6LTGzJJimjXfr+rUct4tgSrUVA8syXB5T4wpQItDIAIT0W4iR0zeJAAD7iyQgt0gxovvIk7ilGN+z2Lg00SfWs0KfYiTXLDAAGV4-mLzibP4UOINAVC6qE41JjmcBUvYBszaS6F0EKWvu7Lwvy7eMpwPGiYorUaJ64SVKMkLiR8ok10AJoThq2pu8cvAEPSJAMvYmta32Ot6+gsNXfWRvXpCZv+DY4BuoNBy4fM-sO7hzuJCQmoIKcCD+AAJAs9iHAboNa2nwq8aTSocuCJAAUBIFBnAqAOLe9hwFnGdgGAqn5UGZvCjHc-AVAoHgZBtjQQWcGk1Yga8C8SaLc3CTuBAKZkPimBBugrMw8CSH2B5nzGWcsK4IH5FdRszY7YTSnh4MUF0ojG3piQe41As4EiyGrKIPIlhsRAG4fwkhVqHFrP1cU8AWKB2Dj6X2IswGJFOsOABcMMpZUqHAN4JA+jMkcG4Ok6A34SkWmvLOPDZItm8AAL0AfWbqDJsgHCgFfUgyiAA8ul9IBj1o4XUAZVFDCGHnckND-76kYuCJcUBxq-AZEsPSBk6T+AcQGIyUAPI8n8oFCA-gvFBTcR5I4bsg5FjMbrXUgj0BmiChAGAhDHTPAQG8D4iR4QgFuPcZkqSzjIFtN5WaBxMjZBNBEAsBtxF8IERAUc-cXF0gCYceI-c-EQAaQbfJu1uHUmoaEyhusKkZiqawq6ITEwxzjgqbKVhByVESCCLGBt+6IxaocZASysElMHikGAuph5dJmhPesWUrDXDyoQMgulAwtkpkGdwoQ-SjCpokh+tUP64lsN-a5BU+nClGQcPpqTTkXTIUcp0cCZ5HwXoCZekJagIE0H-QgbgXgplqjGZYmwD50MhSfMCEE9gXxgiQa+oLnQz3RZkD4Bw4CZPOLVN49gYAYsBAvchZ5irlGAogc4PSxl0KYgA9689uWsPrLzbORUu6ctpdKUa4AwDGILtkIuhtkGm3Ntw8E1tbY0u5a7DpOlKiag3FuHce4lqCE2stFa+S-n5QYgK8x1phVYAZG9F630hgkCNSazU25dzqgORlKBCAWynR6mmBBZpSK8F4IzPJZJDn8WpLq11edD6Mvnris+BLHwkCGDKZaKFMpOk1PeV05AwHMuaOWIB2cM2AWPqffFUEUwaMHCOccKoU7TnnMuVc65Nx+rNYGr29YlW631pdb25cTaVw1XSIEH9YxzxZbipqt5+4Nqzc28+j5jjWlbe3MtD4eA21QbzNMTtEjDyusE0xMdHX9PBFy117qfyepIMtK1K1BBuyygnSghUnaylIlTdFVpCq2BVspams9M1rtAuQT2VZvR-zcGccEssbZXSypgEgyQCEHEUUmM8QLARKTOK0TeYBPaPCubvKmdzBq6VeDvN5uAPm4adN1BI4Qmj4RIAbO1Md-aJFAh8NoVBpoG3HryMAeViLjrFIXKdpdZ0oKrneONas1YXvLMIkg-cO1jmTlOWci4Vxrl9f6vchxha3tHvk8VDJRNgOMdrZVU6DYnK8H-MT+rS4iboWJ+E1pRX1l4pFxN3YLCWHUMwTQ2hdA8H4EIMQUhZCSHkMoEotgHwVFcPA7wyl-CBG0KQMIERogREINodIAQsFVbyBsSUxRrD5fKFUGodRASNGaBnZSHQMNUCmBYBYURgAJioKOUY4xshRBUPkPEhQ0iHHiwlpLwQUv6HS0YLLOWlDMEsEAA)
    
    
    import { DurableObject } from "cloudflare:workers";
    import * as puppeteer from "@cloudflare/puppeteer";
    
    interface Env {
    	MYBROWSER: Fetcher;
    	BUCKET: R2Bucket;
    	BROWSER: DurableObjectNamespace;
    }
    
    export default {
    	async fetch(request, env): Promise<Response> {
    		const obj = env.BROWSER.getByName("browser");
    
    		// Send a request to the Durable Object, then await its response
    		const resp = await obj.fetch(request);
    
    		return resp;
    	},
    } satisfies ExportedHandler<Env>;
    
    const KEEP_BROWSER_ALIVE_IN_SECONDS = 60;
    
    export class Browser extends DurableObject<Env> {
    	private browser?: puppeteer.Browser;
    	private keptAliveInSeconds: number = 0;
    	private storage: DurableObjectStorage;
    
    	constructor(state: DurableObjectState, env: Env) {
    		super(state, env);
    		this.storage = state.storage;
    	}
    
    	async fetch(request: Request): Promise<Response> {
    		// Screen resolutions to test out
    		const width: number[] = [1920, 1366, 1536, 360, 414];
    		const height: number[] = [1080, 768, 864, 640, 896];
    
    		// Use the current date and time to create a folder structure for R2
    		const nowDate = new Date();
    		const coeff = 1000 * 60 * 5;
    		const roundedDate = new Date(
    			Math.round(nowDate.getTime() / coeff) * coeff,
    		).toString();
    		const folder = roundedDate.split(" GMT")[0];
    
    		// If there is a browser session open, re-use it
    		if (!this.browser || !this.browser.isConnected()) {
    			console.log(`Browser DO: Starting new instance`);
    			try {
    				this.browser = await puppeteer.launch(this.env.MYBROWSER);
    			} catch (e) {
    				console.log(
    					`Browser DO: Could not start browser instance. Error: ${e}`,
    				);
    			}
    		}
    
    		// Reset keptAlive after each call to the DO
    		this.keptAliveInSeconds = 0;
    
    		// Check if browser exists before opening page
    		if (!this.browser)
    			return new Response("Browser launch failed", { status: 500 });
    
    		const page = await this.browser.newPage();
    
    		// Take screenshots of each screen size
    		for (let i = 0; i < width.length; i++) {
    			await page.setViewport({ width: width[i], height: height[i] });
    			await page.goto("https://workers.cloudflare.com/");
    			const fileName = `screenshot_${width[i]}x${height[i]}`;
    			const sc = await page.screenshot();
    
    			await this.env.BUCKET.put(`${folder}/${fileName}.jpg`, sc);
    		}
    
    		// Close tab when there is no more work to be done on the page
    		await page.close();
    
    		// Reset keptAlive after performing tasks to the DO
    		this.keptAliveInSeconds = 0;
    
    		// Set the first alarm to keep DO alive
    		const currentAlarm = await this.storage.getAlarm();
    		if (currentAlarm == null) {
    			console.log(`Browser DO: setting alarm`);
    			const TEN_SECONDS = 10 * 1000;
    			await this.storage.setAlarm(Date.now() + TEN_SECONDS);
    		}
    
    		return new Response("success");
    	}
    
    	async alarm(): Promise<void> {
    		this.keptAliveInSeconds += 10;
    
    		// Extend browser DO life
    		if (this.keptAliveInSeconds < KEEP_BROWSER_ALIVE_IN_SECONDS) {
    			console.log(
    				`Browser DO: has been kept alive for ${this.keptAliveInSeconds} seconds. Extending lifespan.`,
    			);
    			await this.storage.setAlarm(Date.now() + 10 * 1000);
    			// You can ensure the ws connection is kept alive by requesting something
    			// or just let it close automatically when there is no work to be done
    			// for example, `await this.browser.version()`
    		} else {
    			console.log(
    				`Browser DO: exceeded life of ${KEEP_BROWSER_ALIVE_IN_SECONDS}s.`,
    			);
    			if (this.browser) {
    				console.log(`Closing browser.`);
    				await this.browser.close();
    			}
    		}
    	}
    }

## 6\. Test

Run `npx wrangler dev` to test your Worker locally.

Use real headless browser during local development

To interact with a real headless browser during local development, set `"remote" : true` in the Browser binding configuration. Learn more in our [remote bindings documentation](https://developers.cloudflare.com/workers/local-development/#remote-bindings).

## 7\. Deploy

Run [`npx wrangler deploy`](https://developers.cloudflare.com/workers/wrangler/commands/workers/#deploy) to deploy your Worker to the Cloudflare global network.

## Related resources

  * Other [Puppeteer examples ↗︎](https://github.com/cloudflare/puppeteer/tree/main/examples)
  * Get started with [Durable Objects](https://developers.cloudflare.com/durable-objects/get-started/)
  * [Using R2 from Workers](https://developers.cloudflare.com/r2/api/workers/workers-api-usage/)



[PreviousBuild a web crawler with Queues and Browser Run ↗︎](https://developers.cloudflare.com/queues/tutorials/web-crawler-with-browser-run/)[NextGenerate OG images for Astro sites](https://developers.cloudflare.com/browser-run/how-to/og-images-astro/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/browser-run/how-to/browser-run-with-do.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

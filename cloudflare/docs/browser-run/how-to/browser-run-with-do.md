---
url: https://developers.cloudflare.com/browser-run/how-to/browser-run-with-do/
title: Deploy a Browser Run Worker with Durable Objects \u00b7 Cloudflare Browser Run docs
method: scrapling+scrapegraph
fetched_at: 2026-10-31T08:10:18.574784+00:00
---

# Deploy a Browser Run Worker with Durable Objects · Cloudflare Browser Run docs

> Source: https://developers.cloudflare.com/browser-run/how-to/browser-run-with-do/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Browser Run](https://developers.cloudflare.com/browser-run/)
  3. /Tutorials
  4. /Deploy a Browser Run Worker with Durable Objects



# Deploy a Browser Run Worker with Durable Objects

Last updated Oct 31, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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
    	"compatibility_date": "2026-10-31",
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
    compatibility_date = "2026-10-31"
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
    		if (!this.browser || !this.browser.connected) {
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

[ Run Worker in Playground ](https://workers.cloudflare.com/playground#LYVwNgLglgDghgJwgegGYHsHALQBM4RwDcABAEbogB2+CAngLzbPYZb6HbW5QDGU2AAwB2AJwBGCQFYALDIAcAJgDMALhYs2wDnC40+AkROlylygLAAoAMLoqEAKb3sAESgBnGOndRod1SRaeATEJFRwwA4MAERQNA4AHgB0AFbu0aSoUGBOEVGx8clp0Va29k4Q2AAqdDAOAXAwMGB8BFB2yClwAG5w7rwIsBAA1MDouOAOVlZQwF5IJADeJC4gCHBkOQDyZCkOvBAkAL6BCOjAJNG8YJS4qGCI9QDumADWDgjpRJaz84cAVCQ+iQYCAmg5HB9TudLgABa63e6PZCg8GQhAZSyWRJ-Ei4ByoODgQ6LSwASD6dCovECEN4AAsABQIBwARxADncEAANCQnN0AJRLclk3h2LkkdC7EgMPlUbpJABCACUtgB1ADKAFFlUkAOYQxV0AByeUZ0TIZye7g+0QF3xFyGQJA1TlwQJILPZnMOEHQJAg9IcKzWGxyJB2ewOvMDTiBTzgvhIvncns5XioNpFYszhxZnhl8cThylKSSqDpTK9HK59qxZLJLIgayoac83zJR25liODpzEoA0lqtQAFAD6KvV2uVY4AggAZACSADUtWPF8ax9rrFtjS4NYWAGyCB04zCHa59VOKq02hB8hKOGip1brTYOSP7Enky3oa0fDt3hgCBZxaboHEXKhXRzXBU1lE9yS5TA4ANB1RXFCAEBAA5MEZLkCAcXl+SFUkG3cMEPjwwhHCI+U6wbQMPCSJD1gNQt8McZi-VYhwOyOetKWpWkIAZZk2RrCASMdZ0NQGBw43zdAwBAPxMwDf1HAlSgIGzDCSCeKBcEDQsAG1JEUQReXEZRD0PKypBs3kbMskgZHEGQAF0O3Q3MSCDKA9XpQ5ZTMwR5Bc4RD3kXl5EPGReTilz5FEQ8vPrMknRIABVG0AyDEheDWFl7DxAigRoANZmDP0CpZMq4ECJT8XvLksIONZgzYEhlUUXTfKoP8XDK2UqAcJ4VgIxl6J8iUxQJVBC3EQRlpIQFj1WkgpG8-s80oeJcCGxxC1G8bDocRkRTJABZAh6SSM5uEZAanjO-UISqKqppIZ05tQVAhUBX7UG7BsBSSP0NUwuI9Sm7a9IwMBmsLB79tezwWggc0SAAcSuqo7RMwQ0ukkhFwW2MWWTVMGt-f8Ws5Hw7ElOoqF5FkuFy3wRSgBbGQAQkY9wklpu8SAAHzFkgBfpJiRY+JIc1Gg4HFwKSGxmpSHCSG4YYAAxvP9RZcLYAkhxBoCoPUwjG5NczgakHF16ayUwuhhXVl2ZaFuX71lOAEyTVE6nRbWiWpJlBaSfkkiugBNSdNR1Z2Tl4AgGRIRkHDV9X+017X0Bhy6G3128oWNgJbHAd0BsOfCFh9238IdpISC1BAzgQAIABJFgcI5dZB9Xk5FfiSeVTkIRIICQLA4M4FQRx7wcOB09TsAwHUvLg2NkVI+n0CoHAyDoLsWDCwQknrCDXhXmTBaG8SDwIFTMgCUwYN0BZ6GQRQhxud56WstS4IAFJdJsLZrbjXHp4cU51ogGzpiQB41B06EmyCraIvJlgcRAO4AIUgVpHDrH1CU8A2J+wDr6L2wtgFJBOiOX+sN0qZSqHAd4JB+gsicO4ek6Bn6SgWsvdOnD5Kth8AALz-g2LqjIciHCgOfUgCiAA8+lDKBm1k4PUgYlHDGGNnCklCf4GmYhCZcUAxp-EZMsAyRl6QBFsYGEyUAPK8n8oFCAAR3FBWcR5Y4zt-bFmMVrPUfD0DmiChAGAeCnQvAQO8T4CsbggDuA8FkCtzjIDtN5Gahwsg5FNJEQsusRHcN4RAMcPdHH0l8UcBIPdvEQFqbrHJO0OE0goUEshWtSmZnKUwy6gSkyR2joqLK1ghxVCSKCTGuse4I2akcZA8z0GFL7qkGAeoB7tOmqPBsmVrA3FyoQMg+kgytgpsGDwYR-RjEpnE2+NVX54jsB-C5+VukiiGYcbpSTvDnWIfs500DJ771nkCBeUI6gIC0N-Qg7hXiphqrGFYWxd7ULBYfCCUF9inzgiQC+QKXSTxRVkT4hw4BpIuDVd4DgYCoqBLPEhF4ioVFAogC4nThnUJYr-N6M8OVMIbDzDOhV25sqpTKEa4AwAGNzjkfOesEFGxNhwiEFsraUo5U7Vpekqhak3NuXc+5FqCA2ktZaOTvl5SYrykxNoBVYEZK9Z6X1hgkH1YarUO49wal2elcBCBWwnW6umWB5pyK8F4AzbJ5I9mCRpFqp12c950pnli4+uLnwkGGLKJaaEMrOi1I+N05BgEMpaBWf+GdU3AQPkfHFMFUyqKHKOCcqpE4zgXCuNcG4tzeuNX692DZ5Vax1hdD2JdDZl1VfSYEr84zT0ZVixq94e61vTQ2k+z4Tg2ibS3YtT4eCWyQTzdM9skgD0ugEoxkc7U9IhOyp1Lq-xupIEtc1y1BDO0yrHSgBV7ZynIpTFF1oCp2CVqpKmU803LvAuQN21YfTf3cOcCEMtLaXUypgEgKRcGHDkcmC8Ry54qXOG0NeYA3ZPHOVvSm1yBr6TeJvZ5uBXlYedF1RIERmiERILra1kcfZJHAp8doVApq6xHnyMAuVSIjvFHncdRcp2IPLg+aNKsVanorAIkgPdW3jgTtOOcS5Vzri9T6-cRwhZXqHjkkVjIhPAIMRrBV47daHO8N-YTOqi6CeocJhENohUNn4mFuNPZLBWA0MwLQOg9A8H4EIMQkhxCyAUCoUodgnyVDcDAnwqkAhBB0KQcIkQYiREIDoDIgR0HlfyJsKUJQbA5YqNUWo9QgRNBaKnVSnRUNUGmJYRY0RgCJioGOMYEwcjRFUAUfERR0hHBi7F+LIREsGBS8YdLpgVDMCsEAA)
    
    
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
    		if (!this.browser || !this.browser.connected) {
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

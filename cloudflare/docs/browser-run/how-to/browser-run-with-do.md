---
url: https://developers.cloudflare.com/browser-run/how-to/browser-run-with-do/
title: Deploy a Browser Run Worker with Durable Objects \u00b7 Cloudflare Browser Run docs
method: scrapling+scrapegraph
fetched_at: 2026-11-12T09:30:28.504879+00:00
---

# Deploy a Browser Run Worker with Durable Objects · Cloudflare Browser Run docs

> Source: https://developers.cloudflare.com/browser-run/how-to/browser-run-with-do/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Browser Run](https://developers.cloudflare.com/browser-run/)
  3. /Tutorials
  4. /Deploy a Browser Run Worker with Durable Objects



# Deploy a Browser Run Worker with Durable Objects

Last updated Nov 11, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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
    	"compatibility_date": "2026-11-12",
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
    compatibility_date = "2026-11-12"
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

[ Run Worker in Playground ](https://workers.cloudflare.com/playground#LYVwNgLglgDghgJwgegGYHsHALQBM4RwDcABAEbogB2+CAngLzbPYZb6HbW5QDGU2AAwAOAJwB2ACwBWAExTZwyQC4WLNsA5wuNPgJESZ8yYskBYAFABhdFQgBTO9gAiUAM4x0bqNFvKSGngExCRUcMD2DABEUDT2AB4AdABWblGkqFBgjuGRMXFJqVGWNnaOENgAKnQw9v5wMDBgfARQtsjJcABucG68CLAQANTA6Ljg9paWUMCeSCQA3iTOIAhwZNkA8mTJ9rwQJAC+AQjowCRRvGCUuKhgiHUA7pgA1vYIaUQWM3MHAFQkXokGAgRr2BzvE5nC4AASuNzuD2QILBEIQ6QsFgSvxIuHsqDg4AOCwsAEhenQqLwAuDeAALAAUCHsAEcQPY3BAADQkRxdACUizJpN4tk5JHQOxIDF5VC6iQAQgAlTYAdQAygBRJWJADm4IVdAAcrkGVEyKdHm53lF+V9hchkCR1Y5cICSMy2RyDhB0CQIHT7MtVutsiRtrt9jyA45AY84D4SD43B6OZ4qNbhaKMwdmR5pXGEwdJclEqhaYzPezOXbMaTScyIKsqKmPF9SYcuRZDvbs+KANKazUABQA+sq1VqlaOAIIAGQAkgA1TWjhdG0daqybI3OdUFgBsgnt2MwByuvRTCst1oQvPiDhoKZWaw29gje2JZIt6Ct73bbwwBAM7NF09gLlQLrZrgKYyseZKcpgcD6vaIpihACAgPsmAMpyBD2DyfKCiS9ZuKC7y4YQDiEXKtb1gG7iJIhaz6gWeEOExvosfY7aHHWFJUjSED0kyrLVhAxEOk66r9PYsZ5ugYAgL4Gb+n6DjipQEBZuhJCPFAuABgWADaACMoiyIIPKmQAzAeB7WdIdk8nZVkkJIpmSAAuu2aE5iQgZQLqdIHDKZkiG54gHsIPLCAekg8vFbliAePl1qSjokAAqta-qBiQvCrMydi4vhgI0P6MxBr6BXMmVcABIpeJ3pymH7KsQZsCQSqyDp-lUL+zhlTKVD2I8yz4QydF+eKor4qgBamYIy0kACR6rSQ0i+X2uaUHEuBDQ4BajeNh32AywqkgAsgQdKJKc3AMgNjxnXq4KVFVU0kE6c2oKggoAr9qBdvW-KJL66oYbEupTdtukYGAzUFg9+2vR4zQQGaJAAOJXZUtrGYIaVSSQC4LTGzJJimDU-n+LUct4tgSrUVA8syXC5T4wpQAtDIAIQMW4iS07eJAAD5iyQAt0oxIvvIk2ajfs9i4JJ9YzYp9iJNcMMAAbXr+ovOJs-iQ4g0BULqoRjUmOZwFS9i69NpIYXQQrqy7MtC3Ld4ynA8aJiitRotrhJUoyguJHyiRXQAmhOGras7xy8AQ9IkAy9hq+rfaa9r6Aw5d9b6zekLG-4NjgG6A0HHh8w+7beEO4kJCaggpwIP4AAkCz2Icusg+ryfCnxJNKhy4IkIBwGgUGcCoA4d72HA6ep2AYBqXlQbG8KkfTyBUBgRBUG2DBBbwSTViBrwLxJgtDcJO4EApmQ+KYEG6As9DwLIfY3O89LWWpcED8kuo2Zs1txrjw8GKc6UQDZ0xIPcag6cCRZBVlEHkSx2IgDcP4aQK1Di1j6uKeArE-YBx9F7YWwDEgnWHL-WG6VMqVDgG8EgfRmSODcHSdAz8JQLWXunThckWzeAAF5-3rF1Bk2QDhQHPqQBRAAePSBkAza0cLqAMSihhDGzuSShP99RMXBEuKAY1fgMiWPpQydJ-C2IDMZKAXkeSBWChAfw7iQrOK8kcZ2-sizGK1rqPh6AzQhQgDAPBjpngIDeB8BW1wQC3HuMyBWZxkC2l8jNA4mRsgmgiAWXWIjuG8IgKOHuji6S+MOPEHu3iIC1N1jknaHDqQUKCWQrWpSMzlKYZdQJiZI7RwVFlKwg5KiJBBJjXWPcEbNUOMgeZ6DCl9xSDAXUA92nTVHvWTKVhri5UIGQPSgYWwUyDO4UIfpRiUzibfGqr9cS2A-hc-K3ThRDION0pJXhzrEP2U6aBk996z0BAvSEtQEAaG-oQNwLwUw1RjMsTYu9qFgsPuBSCexT6wRIBfIFzpJ4osyB8A4cA0nnBqm8ewMBUWAlniQ88RVyggUQOcTpwzqHMV-m9GeHKmH1h5hnQq7c2VUulCNcAYADG52yPnPWCCjYmw4eCC2VtKUcqdq03SlRNQbi3DuPci1BAbSWstHJ3y8qMV5SY60AqsAMles9L6QwSD6sNZqbcu51S7PSuAhALYTrdTTLAs0ZFeC8AZtkskeyBLUi1U67Oe86UzyxcfXFT4SBDBlEtVCGUnSagfK6cgwCGXNHLP-DOqagIHyPji6CKZVGDhHOOFUidpzzmXKudcm5vXGr9e7es8qtY6wuh7Euhsy6qrpECV+sZp6MqxY1O8Pda3pobSfJ8xxrRNpbsWx8PBLZIJ5mme2iQB6XQCUYyOdqengnZU6l1v43UkCWua5aghnaZVjpQAq9tZRkUpiiq0BVbBKxUlTKeabl1gXIG7Ks3pv5uDOOCGWltLqZUwCQZIuCDhyKTOeI5c9lJnFaGvMAbtHjnK3pTa5A09KvE3s83ArysNOi6gkcITQCIkF1tayOPtEhgQ+G0KgU1dYj15GAXKJER1ijzuOouU7EHl3vNGlWKtT3lgESQHuraxwJynLORcK41xep9XuQ4Qsr1DxySKhkQngEGI1gq8dutDleG-sJnVRdBPUOE-Ca0Qr6x8TC3G7sFhLBqGYBoLQOgeD8CEGIKQcgFBKBKLYR8FRXAwO8CpfwgQtCkDCBEaIERCBaHSAEdBZW8gbElMUaw2XyhVBqHUQEjRmipxUh0VDVApgWAWFEYACYqCjlGOMbIURlD5DxIUNIhwYuxfi8ERLegUuGHSyYJQzBLBAA)
    
    
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

  * Other [Puppeteer examples](https://developers.cloudflare.com/browser-run/examples/#browser-automation-examples)
  * Get started with [Durable Objects](https://developers.cloudflare.com/durable-objects/get-started/)
  * [Using R2 from Workers](https://developers.cloudflare.com/r2/api/workers/workers-api-usage/)



[PreviousBuild a web crawler with Queues and Browser Run ↗︎](https://developers.cloudflare.com/queues/tutorials/web-crawler-with-browser-run/)[NextGenerate OG images for Astro sites](https://developers.cloudflare.com/browser-run/how-to/og-images-astro/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/browser-run/how-to/browser-run-with-do.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

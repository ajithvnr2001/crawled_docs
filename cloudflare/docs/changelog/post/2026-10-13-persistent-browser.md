---
url: https://developers.cloudflare.com/changelog/post/2026-10-13-persistent-browser/
title: New persistent browser tool in the Agents SDK, with tabs and logins that last between turns \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:32.627144+00:00
---

# New persistent browser tool in the Agents SDK, with tabs and logins that last between turns · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-13-persistent-browser/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 13, 2026

## New persistent browser tool in the Agents SDK, with tabs and logins that last between turns

[Agents](https://developers.cloudflare.com/agents/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Cloudflare Agents SDK](https://developers.cloudflare.com/agents/) now provides a `browserTool` that gives your agent a [Browser Run](https://developers.cloudflare.com/browser-run/) browser it can return to on later turns. Your agent can open a website, inspect a page, and come back to it with its tabs, cookies, and login session intact while the browser session remains alive.

When you give `browserTool` to your agent, the model writes code that drives the browser through the [Chrome DevTools Protocol (CDP)](https://developers.cloudflare.com/browser-run/cdp/). Screenshots return as images that an image-capable model can inspect and your UI can display.

To use `browserTool`, make sure you have [Agents SDK v0.28.0 ↗︎](https://github.com/cloudflare/agents/releases/tag/agents%400.28.0) or greater installed. Create a `Browser`, register it with your object's [Lifecycle](https://developers.cloudflare.com/agents/runtime/lifecycle/), and add the tool to a [Pi Durable](https://developers.cloudflare.com/agents/harnesses/pi/) [extension registry](https://developers.cloudflare.com/agents/harnesses/pi/extensions/) before opening the harness:
    
    
    import { Browser, browserRun } from "agents/browser";
    import { browserTool } from "agents/browser/pi";
    
    export class MyAgent extends DurableObject {
    	// ...
    
    	browser = new Browser({ provider: browserRun(this.env.BROWSER) });
    
    	harness = new PiHarness({
    		harness: async ({ storage, context }) => {
    			this.registry.install({
    				name: "browser",
    				tools: [
    					browserTool({
    						ctx: this.ctx,
    						browser: this.browser,
    						loader: this.env.LOADER,
    					}),
    				],
    			});
    
    			// ...
    
    			return Harness.open(
    				storage,
    				{ models, registry: this.registry },
    				context,
    			);
    		},
    	});
    
    	lifecycle = Lifecycle.install(this).use(this.browser).use(this.harness);
    }
    
    
    import { Browser, browserRun } from "agents/browser";
    import { browserTool } from "agents/browser/pi";
    
    export class MyAgent extends DurableObject<Env> {
    	// ...
    
    	browser = new Browser({ provider: browserRun(this.env.BROWSER) });
    
    	harness = new PiHarness({
    		harness: async ({ storage, context }) => {
    			this.registry.install({
    				name: "browser",
    				tools: [
    					browserTool({
    						ctx: this.ctx,
    						browser: this.browser,
    						loader: this.env.LOADER,
    					}),
    				],
    			});
    
    			// ...
    
    			return Harness.open(
    				storage,
    				{ models, registry: this.registry },
    				context,
    			);
    		},
    	});
    
    	lifecycle = Lifecycle.install(this).use(this.browser).use(this.harness);
    }

Each Pi conversation gets its own active tab by default. Cookies and logins remain shared within the browser.

The browser stays alive between turns, including when the Durable Object hibernates. Its default idle timeout is 10 minutes. If the session expires or crashes, the tool creates a fresh browser and reports `restarted: true`. The old tabs and login state are gone.

You can also use the persistent browser with the AI SDK and TanStack AI adapters, or connect another harness through the public Browser and CDP APIs.

Refer to [persistent browser tools](https://developers.cloudflare.com/agents/tools/browser/#return-to-the-same-browser) for the complete Pi Durable example, required bindings, and behavior when a tool call is interrupted.

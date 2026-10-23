---
url: https://developers.cloudflare.com/changelog/post/2026-10-20-think-computer-workspace/
title: Think agents now use a @cloudflare/computer workspace \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:51:29.330017+00:00
---

# Think agents now use a @cloudflare/computer workspace · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-20-think-computer-workspace/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 20, 2026

## Think agents now use a @cloudflare/computer workspace

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Think](https://developers.cloudflare.com/agents/harnesses/think/) and [Agent Skills](https://developers.cloudflare.com/agents/runtime/execution/agent-skills/) now use the workspace from [`@cloudflare/computer` ↗︎](https://github.com/cloudflare/computer) as well as the filesystem tools. A JavaScript execution environment can be configured by adding the `JavaScriptWorkerBackend`.

`@cloudflare/shell` is deprecated, and so is Think's `createExecuteTool`. These will no longer be developed nor supported from today onwards.
    
    
    import { Think } from "@cloudflare/think";
    import { Workspace } from "@cloudflare/computer";
    import { WorkerJavaScriptBackend } from "@cloudflare/computer/backends/worker-javascript";
    
    export class MyAgent extends Think {
    	workspace = new Workspace({
    		storage: this.ctx.storage,
    		backends: [
    			new WorkerJavaScriptBackend({ id: "js", loader: this.env.LOADER }),
    		],
    	});
    }
    
    
    import { Think } from "@cloudflare/think";
    import { Workspace } from "@cloudflare/computer";
    import { WorkerJavaScriptBackend } from "@cloudflare/computer/backends/worker-javascript";
    
    export class MyAgent extends Think<Env> {
    	override workspace = new Workspace({
    		storage: this.ctx.storage,
    		backends: [
    			new WorkerJavaScriptBackend({ id: "js", loader: this.env.LOADER }),
    		],
    	});
    }

#### Migrate your workspace data

This is a breaking change. @cloudflare/computer stores files in different tables from @cloudflare/shell, and there is no automatic data migration between workspace formats. To keep an existing workspace, copy its files with the script in [Migrating from `@cloudflare/shell` to `@cloudflare/computer` ↗︎](https://github.com/cloudflare/agents/blob/main/docs/shell/migrating-to-computer.md). Otherwise your agent will start with an empty workspace, though the original data will still be present in the existing tables.

For more information, refer to [Think tools](https://developers.cloudflare.com/agents/harnesses/think/tools/#built-in-workspace-tools).

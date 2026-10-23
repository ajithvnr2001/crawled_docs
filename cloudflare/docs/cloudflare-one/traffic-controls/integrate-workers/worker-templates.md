---
url: https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/
title: Worker templates \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-16T06:37:09.299844+00:00
---

# Worker templates · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Traffic controls](https://developers.cloudflare.com/cloudflare-one/traffic-controls/)

  4. /[Integrate Workers](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/)
  5. /Worker templates



# Worker templates

Last updated Oct 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUse a template

Public beta

The Gateway Forward action is available in public beta on all Zero Trust plans. Workers usage is subject to [Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/).

These templates are starting points for Workers invoked by Forward policies. You can adapt them or write your own Worker using the `GatewayMiddleware.handle(request, context, next)` entrypoint. Each script implements one task.

Template | What it does  
---|---  
[Send a Slack notification](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/slack-notification/) | Send a background notification when a selected request completes.  
[Capture a screenshot](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/screenshot/) | Capture a public page in an independent browser and save the image to R2.  
[Capture a downloaded file](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/download-capture/) | Save a bounded copy of an attachment to R2 while returning the download to the user.  
[Watermark HTML pages](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/watermark/) | Add a visible user label to an HTML response.  
[Store headers and bodies as JSON](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/json-capture/) | Archive selected headers and bounded JSON request and response bodies in R2.  
[Display a coaching page](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/coaching-page/) | Return an explanatory page without contacting the original destination.  
[Redact a JSON field](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/json-redaction/) | Replace a specific field in an application request before sending it upstream.  
  
## Use a template

Follow [Set up Forward](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/forward-traffic/#set-up-forward), replace the pass-through script with a template, and configure its bindings. Deploy the Worker before selecting it in a Forward policy. Each template lists a test and the traffic scope it expects.

The [gateway-workers skill ↗︎](https://github.com/cloudflare/skills/blob/main/skills/gateway-workers/SKILL.md) provides guidance for coding agents on the named entrypoint, Gateway context, and validation.

Every TypeScript template includes `import type` declarations for `GatewayMiddlewareContext` and `GatewayMiddlewareNext` from [`@cloudflare/zt-types` ↗︎](https://www.npmjs.com/package/@cloudflare/zt-types). Install this package as a development dependency in your Worker project before using a template. Each template includes the installation command.

The package supplies [Gateway types](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/available-context/#typescript-types). Continue to import the runtime `WorkerEntrypoint` class from `cloudflare:workers`. The `import type` declarations are removed when TypeScript compiles. The JavaScript version omits them and the type annotations, so it does not need `@cloudflare/zt-types`.

Begin with a test host and test user group. Page loads produce multiple HTTP requests, so scope notifications and screenshots to a specific method and path, rather than every request to a domain. Keep capture buckets private and configure [R2 lifecycle rules](https://developers.cloudflare.com/r2/buckets/object-lifecycles/) for retention. Capture only data your organization permits you to store.

Background examples use [`this.ctx.waitUntil()`](https://developers.cloudflare.com/workers/runtime-apis/context/#waituntil). They return the user's response without awaiting the background operation. A background failure is logged and does not change the returned response. Background work has [limited execution time](https://developers.cloudflare.com/workers/platform/limits/#duration). Use Queues or Workflows when you need durable processing.

Body capture uses cloned streams. A slow capture consumer can cause a clone to buffer data while the other consumer advances. The examples limit captured bytes, but cloning is not a guarantee of constant memory use or zero impact on traffic. Keep capture policies narrow and test representative body sizes and transfer speeds.

[PreviousAvailable context](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/available-context/)[NextSend a Slack notification](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/slack-notification/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/traffic-controls/integrate-workers/worker-templates/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

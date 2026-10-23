---
url: https://developers.cloudflare.com/workers-ai/platform/data-usage/
title: Your Data and Workers AI \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-17T06:28:14.064428+00:00
---

# Your Data and Workers AI · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/platform/data-usage/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /Platform
  4. /Data usage



# Data usage

Last updated Oct 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewOur commitments for Customer ContentWhen a feature stores Customer ContentOperational metadataSafety, security, and legal exceptionsModels available through Workers AI

Cloudflare processes certain customer data to provide Workers AI, subject to our [Privacy Policy ↗︎](https://www.cloudflare.com/privacypolicy/) and, as applicable, our [Self-Serve Subscription Agreement ↗︎](https://www.cloudflare.com/terms/) or [Enterprise Subscription Agreement ↗︎](https://www.cloudflare.com/enterpriseterms/) ("Agreements").

Your inputs (for example, text prompts, images, and audio), outputs (for example, generated text, images, and translations), embeddings, and any training or adaptation data you provide are **Customer Content** as that term is defined in our Agreements.

This page applies to Workers AI. If you use AI Gateway to send Customer Content to another AI provider or connect Workers AI to another third-party service, that provider or service may process and retain the content under its own terms and policies.

## Our commitments for Customer Content

**Zero data retention:** Workers AI processes Customer Content only for as long as needed to provide the service. For standard inference requests that do not invoke a stateful feature, Cloudflare does not retain inputs or outputs after they are no longer needed to process the request and deliver the response, subject to the limited exceptions below.

**No training:** Cloudflare does not use Customer Content processed by Workers AI to train AI models.

**Your content remains yours:** You own, and are responsible for, your Customer Content. Cloudflare does not make it available to other Cloudflare customers.

## When a feature stores Customer Content

Some features require storage to work. Our zero data retention commitment does not prevent storage that you direct or that is necessary to provide a stateful feature you select.

For example, Customer Content may be stored when you:

  * use a Cloudflare storage service, such as R2, KV, Durable Objects, or Vectorize, with Workers AI;
  * enable logging or caching in AI Gateway or write Customer Content to application logs; or
  * where offered, use an asynchronous or batch feature, upload files or adapters, or select another stateful feature that requires content to remain available while the feature operates.



In those cases, the applicable feature documentation, configuration, and retention lifecycle govern the stored content. Cloudflare retains that content only for as long as needed to provide the feature or as directed by you.

## Operational metadata

Cloudflare may retain operational metadata needed to operate, secure, support, and bill for Workers AI. This may include account and model identifiers, timestamps, request and response sizes, token or neuron counts, latency, request source, and normalized status or error codes. Operational metadata retained under this section does not include Customer Content. For more information on the information we may collect, see the Cloudflare Privacy Policy.

## Safety, security, and legal exceptions

To the extent Cloudflare must analyze or retain Customer Content to fulfill our legal obligations or commitments, as described in our Agreements or our Privacy Policy, such Customer Content is not used to train AI models or improve Cloudflare or third-party products or services.

## Models available through Workers AI

Cloudflare does not create or train the third-party AI models made available through Workers AI. Those models may be subject to open source, acceptable use policies, or other license terms between you and the model provider. Review the license terms applicable to each model.

[PreviousPricing](https://developers.cloudflare.com/workers-ai/platform/pricing/)[NextLimits](https://developers.cloudflare.com/workers-ai/platform/limits/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers-ai/platform/data-usage.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

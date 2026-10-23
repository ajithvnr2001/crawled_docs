---
url: https://developers.cloudflare.com/changelog/post/2026-10-23-structured-evaluation-context/
title: Target Flagship feature flags with structured evaluation context \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:39:48.684560+00:00
---

# Target Flagship feature flags with structured evaluation context · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-23-structured-evaluation-context/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 23, 2026

## Target Flagship feature flags with structured evaluation context

[Flagship](https://developers.cloudflare.com/flagship/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-23-structured-evaluation-context/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Flagship](https://developers.cloudflare.com/flagship/) supports nested objects, arrays, and `null` in evaluation context. Pass user profiles and tag lists directly, then target nested attributes without flattening your application data.

For example, pass a profile and tags when evaluating a flag through the Workers binding:
    
    
    const enabled = await env.FLAGS.getBooleanValue("new-checkout", false, {
    	targetingKey: "user-42",
    	profile: { plan: "enterprise" },
    	tags: ["beta", "early-access"],
    });
    
    
    const enabled = await env.FLAGS.getBooleanValue("new-checkout", false, {
    	targetingKey: "user-42",
    	profile: { plan: "enterprise" },
    	tags: ["beta", "early-access"],
    });

A targeting rule can combine `profile.plan equals "enterprise"` with `tags has "beta"` to serve the feature to enterprise users in the beta group. Use dot-separated paths for nested attributes and the `has` and `not_has` operators for array membership. Percentage rollouts can also use a nested identifier, such as `profile.id`, for consistent user assignment.

Structured context works through the Workers binding, the evaluation REST API with a JSON `POST` body, and the TypeScript, Python, and Go OpenFeature SDKs from version `0.6.0`. The SDKs automatically use `POST` when HTTP evaluation requires structured context.

Refer to [targeting rules](https://developers.cloudflare.com/flagship/targeting/), the [evaluation API](https://developers.cloudflare.com/flagship/reference/evaluation-api/), and [SDK context support](https://developers.cloudflare.com/flagship/sdk/#context-support) for usage and supported values.

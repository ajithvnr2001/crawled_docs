---
url: https://developers.cloudflare.com/ruleset-engine/
title: Overview \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-11-28T09:57:36.114060+00:00
---

# Overview · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/

  1. [Home](https://developers.cloudflare.com/)
  2. /Ruleset Engine



# Cloudflare Ruleset Engine

Last updated Nov 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewKey conceptsHow Cloudflare evaluates a requestWhere to startAvailability

Many Cloudflare products work the same way: you write a rule that says "when a request looks like this, do that." Redirect Rules, Transform Rules, Cache Rules, Configuration Rules, and WAF custom rules all follow this model.

The Ruleset Engine is the shared system behind these products. All of them use the same Rules language and the same API. After you learn to write a rule for one product, you can write rules for the others.

In the Cloudflare dashboard, you usually create rules only. For most products, Cloudflare manages rulesets and phases for you.

## Key concepts

The Ruleset Engine uses the following concepts:

Concept | What it is | Example  
---|---|---  
**Rule** | An expression plus an action. | When the path starts with `/old/`, redirect to `/new/`.  
**Expression** | The condition that selects which requests a rule applies to. You write it in the Rules language, or build it from drop-down menus in the dashboard. | `http.request.uri.path wildcard "/old/*"`  
**Action** | What happens when the expression matches a request. | Redirect, rewrite, set a header, cache, or block.  
**Ruleset** | An ordered list of rules. Each product stores its rules in a ruleset. | All redirect rules for a zone.  
**Phase** | A point in the request life cycle where rulesets run. Phases always run in the same order. | Redirect Rules (Single Redirects) run before Cache Rules.  
  
For more information, refer to [About Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/about/).

## How Cloudflare evaluates a request

  1. A request arrives at Cloudflare.
  2. Cloudflare runs each phase in a fixed order. Refer to the [Phases list](https://developers.cloudflare.com/ruleset-engine/reference/phases-list/) for the full order.
  3. Within a phase, Cloudflare checks rules in the order you define them.
  4. When an expression matches, Cloudflare runs the rule's action.



Terminating actions, such as _Redirect_ , _Block_ , or a challenge, stop rule evaluation, and Cloudflare responds immediately. The remaining rules in the phase and later request phases do not run for that request. Response phases can still apply to the response that Cloudflare generates. For example, [Response Header Transform Rules](https://developers.cloudflare.com/rules/transform/response-header-modification/) apply to redirect responses, and [Custom Error Rules](https://developers.cloudflare.com/rules/custom-errors/) apply to the error response of a _Block_ action.

Non-terminating actions, such as setting a header, do not stop evaluation. If several rules in the same phase change the same value, the last rule wins. Refer to [Actions](https://developers.cloudflare.com/ruleset-engine/rules-language/actions/) for details.

## Where to start

Use the following table to find documentation for your task:

Goal | Refer to  
---|---  
Redirect URLs | [Redirects](https://developers.cloudflare.com/rules/url-forwarding/)  
Rewrite URLs or modify headers | [Transform Rules](https://developers.cloudflare.com/rules/transform/)  
Control caching | [Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/)  
Adjust settings for some requests | [Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/)  
Block or challenge traffic | [WAF custom rules](https://developers.cloudflare.com/waf/custom-rules/)  
Migrate from Page Rules | [Page Rules migration guide](https://developers.cloudflare.com/rules/reference/page-rules-migration/)  
Learn to write expressions | [Rules language](https://developers.cloudflare.com/ruleset-engine/rules-language/)  
Configure rules with the API | [Rulesets API](https://developers.cloudflare.com/ruleset-engine/rulesets-api/)  
  
## Availability

Each product built on the Ruleset Engine has its own quotas and plan availability. Some features, such as regular expressions, depend on your plan. Refer to each product's documentation for details.

[NextOverview](https://developers.cloudflare.com/ruleset-engine/about/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ruleset-engine/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

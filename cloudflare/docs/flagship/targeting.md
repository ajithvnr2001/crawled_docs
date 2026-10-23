---
url: https://developers.cloudflare.com/flagship/targeting/
title: Targeting rules \u00b7 Cloudflare Flagship docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:57:49.413929+00:00
---

# Targeting rules · Cloudflare Flagship docs

> Source: https://developers.cloudflare.com/flagship/targeting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Flagship](https://developers.cloudflare.com/flagship/)
  3. /Targeting rules



# Targeting rules

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow rules workCondition structureLogical groupingLearn more

Targeting rules let you serve different flag values to different users based on their attributes. Each flag can have zero or more rules.

Rules are evaluated in sequential order, from top to bottom. The first rule whose conditions match is used, and its configured variant is returned. If no rule matches, Flagship returns the flag's default variant.

When a flag is disabled, the default variant is always returned regardless of rules.

Place more specific rules before broader rules. A broad catch-all rule can prevent later rules from running.

## How rules work

A rule consists of:

  * **Conditions** — One or more attribute comparisons that must be satisfied. For example, `country equals "US"` or `plan in ["enterprise", "business"]`.
  * **Serve variant** — The variant to return when the rule matches.
  * **Rollout** (optional) — A percentage-based gradual release. Only the specified percentage of matching users receive the rule's variant. The rest continue to the next rule.



## Condition structure

Each condition compares an attribute from the evaluation context against a value using an operator:

  * **Attribute** — The context key to evaluate (for example, `userId`, `country`, `plan`).
  * **Operator** — The comparison to perform. Flagship supports [13 operators](https://developers.cloudflare.com/flagship/targeting/operators/).
  * **Value** — The value to compare against. Can be a string, number, or array depending on the operator.



If the evaluation context does not include the attribute referenced by a condition, that condition does not match.

The following rule matches an enterprise profile with the `beta` tag:
    
    
    {
    	"conditions": [
    		{
    			"attribute": "profile.plan",
    			"operator": "equals",
    			"value": "enterprise"
    		},
    		{ "attribute": "tags", "operator": "has", "value": "beta" }
    	],
    	"serve_variation": "on"
    }

Dot-separated attributes traverse nested context objects. Paths can contain at most five segments.

A literal top-level key takes precedence over path traversal. For example, `"profile.plan"` uses that exact top-level key when both forms exist.

## Logical grouping

Conditions within a rule can be grouped with `AND`/`OR` operators and nested up to five levels deep.

Condition grouping depth is separate from context value nesting. It is also separate from the five-segment attribute path limit.

For example, to target enterprise users in the US or Canada:

  * `AND`: 
    * `plan equals "enterprise"`
    * `OR`: 
      * `country equals "US"`
      * `country equals "CA"`



Use the smallest set of context attributes necessary to express the rule. This keeps rule behavior easier to reason about and avoids sending unnecessary user data in evaluation context.

## Learn more

  * [Operators](https://developers.cloudflare.com/flagship/targeting/operators/)
  * [Percentage rollouts](https://developers.cloudflare.com/flagship/targeting/percentage-rollouts/)



[PreviousPython SDK](https://developers.cloudflare.com/flagship/sdk/python/)[NextOperators](https://developers.cloudflare.com/flagship/targeting/operators/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/flagship/targeting/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/flagship/binding/types/
title: Types \u00b7 Cloudflare Flagship docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:57:50.058474+00:00
---

# Types · Cloudflare Flagship docs

> Source: https://developers.cloudflare.com/flagship/binding/types/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Flagship](https://developers.cloudflare.com/flagship/)
  3. /[Binding API](https://developers.cloudflare.com/flagship/binding/)
  4. /Types



# Types

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFlagshipFlagshipEvaluationContextFlagshipEvaluationDetails

The Flagship binding uses the following TypeScript types. Generate binding types with `wrangler types` or use the `@cloudflare/workers-types` package.

## `Flagship`

The binding type. Each Flagship binding in your Wrangler configuration is typed as `Flagship` on the `Env` interface.
    
    
    interface Env {
    	FLAGS: Flagship;
    }

Refer to the [methods reference](https://developers.cloudflare.com/flagship/binding/methods/) for the full list of evaluation methods available on the binding.

## `FlagshipEvaluationContext`

A record of attributes passed to [targeting rules](https://developers.cloudflare.com/flagship/targeting/). Values can recursively contain arrays and objects.
    
    
    type FlagshipEvaluationContextValue =
    	| string
    	| number
    	| boolean
    	| null
    	| FlagshipEvaluationContextValue[]
    	| { [key: string]: FlagshipEvaluationContextValue };
    
    type FlagshipEvaluationContext = Record<string, FlagshipEvaluationContextValue>;

Numbers must be finite. The binding rejects `NaN`, `Infinity`, unsupported objects, and cyclic values.

The runtime also accepts valid JavaScript `Date` values. The binding normalizes each date to an ISO 8601 string. Invalid dates produce an `INVALID_CONTEXT` error.

Serialize `Date` values to ISO 8601 strings before passing them to the binding in TypeScript. The context type describes JSON values and does not include `Date`.

## `FlagshipEvaluationDetails`

Returned by the `*Details` methods. Contains the evaluated value and metadata about how Flagship resolved the flag.
    
    
    interface FlagshipEvaluationDetails<T> {
    	flagKey: string;
    	value: T;
    	variant?: string;
    	reason?: string;
    	errorCode?: string;
    	errorMessage?: string;
    }

Property | Type | Description  
---|---|---  
`flagKey` | `string` | The key of the evaluated flag.  
`value` | `T` | The resolved flag value.  
`variant` | `string` | The name of the matched variant, if any.  
`reason` | `string` | Why the flag resolved to this value (for example, `"TARGETING_MATCH"` or `"DEFAULT"`).  
`errorCode` | `string` | An error code if evaluation failed (for example, `"TYPE_MISMATCH"` or `"GENERAL"`).  
`errorMessage` | `string` | A description of the evaluation error, if any.  
  
Refer to [evaluation reasons and error codes](https://developers.cloudflare.com/flagship/reference/evaluation-reasons/) for the full list of possible values.

[PreviousOverview](https://developers.cloudflare.com/flagship/binding/)[NextMethods](https://developers.cloudflare.com/flagship/binding/methods/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/flagship/binding/types.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

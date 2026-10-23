---
url: https://developers.cloudflare.com/flagship/reference/evaluation-reasons/
title: Evaluation reasons and error codes \u00b7 Cloudflare Flagship docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:57:50.178038+00:00
---

# Evaluation reasons and error codes · Cloudflare Flagship docs

> Source: https://developers.cloudflare.com/flagship/reference/evaluation-reasons/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Flagship](https://developers.cloudflare.com/flagship/)
  3. /Reference
  4. /Evaluation reasons and error codes



# Evaluation reasons and error codes

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEvaluation reasonsError codesInvalid context behaviorExample

When you evaluate a flag using the binding's `*Details` methods or the OpenFeature SDK, the response includes a `reason` field that explains why a particular value was returned. If an error occurs, the response includes an `errorCode` field.

## Evaluation reasons

Reason | Description  
---|---  
`TARGETING_MATCH` | A targeting rule's conditions matched the evaluation context, and the rule's variant was returned.  
`SPLIT` | A targeting rule with a percentage rollout matched. The user fell within the rollout percentage and received the rule's variant.  
`STATIC` | The flag is enabled and has no targeting rules, so its default variant was returned.  
`DEFAULT` | The flag has targeting rules, but none matched the evaluation context. The flag's default variant was returned.  
`DISABLED` | The flag is disabled. The default variant was returned regardless of targeting rules.  
`CACHED` | The SDK returned a cached evaluation result.  
`ERROR` | Evaluation failed and the default value was returned.  
  
## Error codes

When an evaluation error occurs, the method returns the default value you provided. The `*Details` methods include additional metadata about the error.

Error code | Description  
---|---  
`TYPE_MISMATCH` | The flag's variant type does not match the requested type. For example, calling `getBooleanValue` on a flag whose variant is a string. The default value is returned.  
`FLAG_NOT_FOUND` | The specified flag key does not exist in the app. The default value is returned.  
`INVALID_CONTEXT` | The context has an invalid shape or unsupported value, contains a non-finite number or cycle, or exceeds a limit.  
`PARSE_ERROR` | The SDK received an invalid evaluation response. The default value is returned.  
`GENERAL` | An unexpected error occurred during evaluation, such as a timeout or network failure. The default value is returned.  
  
## Invalid context behavior

Binding `*Details()` methods return the supplied default value for invalid context. They set `reason` to `ERROR`, `errorCode` to `INVALID_CONTEXT`, and include an `errorMessage`.

The direct data-plane HTTP `POST` endpoint returns a `400` response instead. Refer to [Evaluation API](https://developers.cloudflare.com/flagship/reference/evaluation-api/) for a request example.

## Example

The following example inspects evaluation details returned by `getBooleanDetails`:
    
    
    const details = await env.FLAGS.getBooleanDetails("my-feature", false, {
    	userId: "user-42",
    });
    
    switch (details.reason) {
    	case "TARGETING_MATCH":
    		console.log(`Matched targeting rule, variant: ${details.variant}`);
    		break;
    	case "SPLIT":
    		console.log(`Included in rollout, variant: ${details.variant}`);
    		break;
    	case "STATIC":
    		console.log("Flag has no targeting rules, using default variant");
    		break;
    	case "DEFAULT":
    		console.log("No rule matched, using default variant");
    		break;
    	case "DISABLED":
    		console.log("Flag is disabled");
    		break;
    	default:
    		// Handle other reasons, such as "CACHED" or "ERROR".
    		break;
    }
    
    if (details.errorCode) {
    	console.error(`Evaluation error: ${details.errorCode}`, details.errorMessage);
    }
    
    
    const details = await env.FLAGS.getBooleanDetails("my-feature", false, {
    	userId: "user-42",
    });
    
    switch (details.reason) {
    	case "TARGETING_MATCH":
    		console.log(`Matched targeting rule, variant: ${details.variant}`);
    		break;
    	case "SPLIT":
    		console.log(`Included in rollout, variant: ${details.variant}`);
    		break;
    	case "STATIC":
    		console.log("Flag has no targeting rules, using default variant");
    		break;
    	case "DEFAULT":
    		console.log("No rule matched, using default variant");
    		break;
    	case "DISABLED":
    		console.log("Flag is disabled");
    		break;
    	default:
    		// Handle other reasons, such as "CACHED" or "ERROR".
    		break;
    }
    
    if (details.errorCode) {
    	console.error(`Evaluation error: ${details.errorCode}`, details.errorMessage);
    }

[PreviousLimits](https://developers.cloudflare.com/flagship/reference/limits/)[NextEvaluation API](https://developers.cloudflare.com/flagship/reference/evaluation-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/flagship/reference/evaluation-reasons.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

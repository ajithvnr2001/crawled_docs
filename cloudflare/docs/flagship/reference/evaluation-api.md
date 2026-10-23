---
url: https://developers.cloudflare.com/flagship/reference/evaluation-api/
title: Evaluation API \u00b7 Cloudflare Flagship docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:56:39.319226+00:00
---

# Evaluation API · Cloudflare Flagship docs

> Source: https://developers.cloudflare.com/flagship/reference/evaluation-api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Flagship](https://developers.cloudflare.com/flagship/)
  3. /Reference
  4. /Evaluation API



# Evaluation API

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSend scalar query contextSend structured JSON context

Use the evaluation API when you cannot use the [Workers binding](https://developers.cloudflare.com/flagship/binding/). The API accepts query parameters or a JSON request body.

## Send scalar query context

The [`GET` endpoint](https://developers.cloudflare.com/api/resources/flagship/subresources/apps/subresources/evaluate/methods/get/) accepts context attributes as query parameters. Use it for scalar context values.

Flagship coerces unambiguous number and boolean query values. For example, `42` becomes a number and `true` becomes a boolean. Other values remain strings.

JSON-looking query values remain strings. A value such as `{"plan":"enterprise"}` does not create a nested object.

## Send structured JSON context

Use `POST` to send nested objects, arrays, or `null`. The following request evaluates `new-checkout` with structured context:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Flagship Read`
  * `Flagship Write`
  * `Flagship Evaluate`

Evaluate flag with JSON contextbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/flagship/apps/$APP_ID/evaluate" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"flagKey": "new-checkout",
    		"context": {
    				"targetingKey": "user-42",
    				"profile": {
    						"plan": "enterprise"
    				},
    				"tags": [
    						"beta"
    				]
    		}
    	}'

The `POST` response contains the same fields as `GET`:
    
    
    {
    	"flagKey": "new-checkout",
    	"value": true,
    	"variant": "on",
    	"reason": "TARGETING_MATCH"
    }

Invalid context returns a `400` response. Refer to [Limits](https://developers.cloudflare.com/flagship/reference/limits/) and [evaluation error codes](https://developers.cloudflare.com/flagship/reference/evaluation-reasons/#error-codes) for details.

[PreviousEvaluation reasons and error codes](https://developers.cloudflare.com/flagship/reference/evaluation-reasons/)[NextWrangler commands](https://developers.cloudflare.com/flagship/reference/wrangler-commands/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/flagship/reference/evaluation-api.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

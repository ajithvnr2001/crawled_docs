---
url: https://docs.comfy.org/api-reference/router/comfy-router/price-a-model-call-before-running-it-without-running-it/
title: Price a model call before running it, without running it. - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:10.898708+00:00
---

# Price a model call before running it, without running it. - ComfyUI

> Source: https://docs.comfy.org/api-reference/router/comfy-router/price-a-model-call-before-running-it-without-running-it/

Price a model call before running it, without running it.

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/v2/models/{provider}/{model}/estimate \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '{}'
    
    
    import requests
    
    url = "https://api.comfy.org/v2/models/{provider}/{model}/estimate"
    
    payload = {}
    headers = {
        "Authorization": "Bearer <token>",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'POST',
      headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
      body: JSON.stringify({})
    };
    
    fetch('https://api.comfy.org/v2/models/{provider}/{model}/estimate', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/v2/models/{provider}/{model}/estimate",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        
      ]),
      CURLOPT_HTTPHEADER => [
        "Authorization: Bearer <token>",
        "Content-Type: application/json"
      ],
    ]);
    
    $response = curl_exec($curl);
    $err = curl_error($curl);
    
    curl_close($curl);
    
    if ($err) {
      echo "cURL Error #:" . $err;
    } else {
      echo $response;
    }
    
    
    package main
    
    import (
    	"fmt"
    	"strings"
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "https://api.comfy.org/v2/models/{provider}/{model}/estimate"
    
    	payload := strings.NewReader("{}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/v2/models/{provider}/{model}/estimate")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/v2/models/{provider}/{model}/estimate")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{}"
    
    response = http.request(request)
    puts response.read_body

200

400

401

403

404

413

422

503
    
    
    {
      "source": "<string>",
      "currency": "<string>",
      "provider": "<string>",
      "model": "bfl/flux-2-pro",
      "pricing_as_of": "2023-11-07T05:31:56Z",
      "amount": "<string>",
      "min_amount": "<string>",
      "max_amount": "<string>",
      "amount_cents": 123,
      "min_amount_cents": 123,
      "max_amount_cents": 123,
      "credits": 123,
      "reason": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>"
    }
    
    
    {
      "detail": [
        {
          "loc": [
            "<string>"
          ],
          "msg": "<string>",
          "type": "image_too_small",
          "ctx": {},
          "input": "<unknown>"
        }
      ]
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>"
    }

Comfy Router

# Price a model call before running it, without running it.

Copy pageCopy page

Returns what Comfy will charge for running this body on this model, in US dollars, priced from the same rate card the charge is billed against. The body is validated against the model’s input schema first, as a default run (no `strict_mode`, no `reject_unknown_fields`) validates it, so a body that fails the model’s schema is the same `422` here as on the run; nothing is dispatched to a provider and nothing is charged. The answer is not a price lock: it is priced at the rates in force at `pricing_as_of`, and a run is charged at the rates in force when it is rated. While the feature is rolling out the route answers `403` with `error_type: not_enabled`.

Copy pageCopy page

POST

/

v2

/

models

/

{provider}

/

{model}

/

estimate

Try it

Price a model call before running it, without running it.

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/v2/models/{provider}/{model}/estimate \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '{}'
    
    
    import requests
    
    url = "https://api.comfy.org/v2/models/{provider}/{model}/estimate"
    
    payload = {}
    headers = {
        "Authorization": "Bearer <token>",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'POST',
      headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
      body: JSON.stringify({})
    };
    
    fetch('https://api.comfy.org/v2/models/{provider}/{model}/estimate', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/v2/models/{provider}/{model}/estimate",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        
      ]),
      CURLOPT_HTTPHEADER => [
        "Authorization: Bearer <token>",
        "Content-Type: application/json"
      ],
    ]);
    
    $response = curl_exec($curl);
    $err = curl_error($curl);
    
    curl_close($curl);
    
    if ($err) {
      echo "cURL Error #:" . $err;
    } else {
      echo $response;
    }
    
    
    package main
    
    import (
    	"fmt"
    	"strings"
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "https://api.comfy.org/v2/models/{provider}/{model}/estimate"
    
    	payload := strings.NewReader("{}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/v2/models/{provider}/{model}/estimate")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/v2/models/{provider}/{model}/estimate")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{}"
    
    response = http.request(request)
    puts response.read_body

200

400

401

403

404

413

422

503
    
    
    {
      "source": "<string>",
      "currency": "<string>",
      "provider": "<string>",
      "model": "bfl/flux-2-pro",
      "pricing_as_of": "2023-11-07T05:31:56Z",
      "amount": "<string>",
      "min_amount": "<string>",
      "max_amount": "<string>",
      "amount_cents": 123,
      "min_amount_cents": 123,
      "max_amount_cents": 123,
      "credits": 123,
      "reason": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>"
    }
    
    
    {
      "detail": [
        {
          "loc": [
            "<string>"
          ],
          "msg": "<string>",
          "type": "image_too_small",
          "ctx": {},
          "input": "<unknown>"
        }
      ]
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>"
    }

#### Authorizations

BearerAuthApiKeyAuthBearerAuthApiKeyAuth

​

Authorization

string

header

required

Bearer token authentication. Normally a Firebase or Cloud JWT. A 'comfyui-' prefixed API key is also accepted in this header: the prefix classifies the value as an API key and it is validated exactly as if it had been sent in X-API-Key.

#### Path Parameters

​

provider

string

required

Lowercase provider segment of the canonical `{provider}/{model}` model ID - the partner whose model is being run. Lowercase `provider` segment of the canonical `{provider}/{model}` model ID - the partner whose model is being addressed. The invocation route's `provider` path parameter and a catalog entry's `provider` field both reference this one schema, which is what keeps the listed IDs and the accepted IDs from drifting apart.

Maximum string length: `64`

Pattern: `^[a-z0-9]+([._-][a-z0-9]+)*$`

Example:

`"bfl"`

​

model

string

required

Lowercase model segment of the canonical `{provider}/{model}` model ID - the model to run within that provider. Lowercase `model` segment of the canonical `{provider}/{model}` model ID - the model to run within that provider. Shared by the invocation route's `model` path parameter and a catalog entry's `model` field, for the same no-drift reason as `RouterProviderSegment`.

Maximum string length: `128`

Pattern: `^[a-z0-9]+([._-][a-z0-9]+)*$`

Example:

`"flux-2-pro"`

#### Query Parameters

​

model_provider

string

Selects an alternate provider to serve this model, instead of its current default. Omitting it runs native dispatch on the model's own default provider; `default`, `comfy`, and `comfyui` are aliases for that same native behavior and name no override, because Comfy Router is never itself a serving backend. The alternate providers Router can retarget a model onto are `fal`, `wavespeed`, `runware`, and `higgsfield`; which of them a given model supports is reported by `GET /v2/models/{provider}/{model}`. When an alternate provider is selected, the native request body is translated into that provider's real schema unless `strict_mode=true`; see `strict_mode` and `fallback_provider`. Its refusals are checked in a fixed order, and an earlier one answers whether or not a later one would. A value that is not a registered provider at all is refused `400` with `error_type: invalid_input`. Then a request whose body selects a multipart operation (an edit - for example gpt-image's `image` field) is refused `409`, also with `error_type: invalid_input`, whose `detail` begins "this request's `image` selects the edit operation" - but only when the named provider's translator for this model cannot itself serve that operation; a leg whose translator does carry the media is not refused and proceeds normally, so this is a per-leg refusal rather than a blanket one. Then a request that has already resolved a bring-your-own-key credential for the provider in the path is refused `409`, also with `error_type: invalid_input`, whose `detail` begins `this request resolved a BYOK credential` \- see the `409` on this route, where that `detail` is the only thing separating this case, and the multipart case above, from the `Idempotency-Key` one. That BYOK check runs whether or not the named provider has a leg for this model. Then the named provider's own gate refuses `403` with `error_type: not_enabled` when that provider is not turned on for you, and `503` with `error_type: service_unavailable` when the gate cannot be evaluated - a flag-evaluation failure, or a missing or nil gate entry. Only past all of those is a real provider that does not serve this model refused `400` with `error_type: invalid_input`, the same answer as a value that is not a registered provider at all - both mean the `model_provider` value cannot serve this model, and that `400`'s `detail` is human-readable and not a contract, so read `GET /v2/models/{provider}/{model}` to learn which providers a model does support rather than parsing it; past that `400`, this workspace's partner-provider policy for the named vendor is evaluated too and can refuse `403` or `503` of its own. Neither this parameter nor `fallback_provider` is available on a BYOK request, and the two are unavailable in different ways: the credential was resolved for the provider named in the path while every alternate leg dispatches on Comfy's own key, so an explicit `model_provider` is refused with that `409`, and `fallback_provider` is inert rather than refused - no retry against an alternate provider is attempted and the first attempt's own failure is what the caller receives. The same split applies to a multipart body: only an explicit `model_provider` reaches the `409` above, and only for a leg whose translator cannot serve the operation, while the automatic on-failure retry `fallback_provider` controls is simply skipped (inert, not refused) for any multipart body. Router defines no `provider_not_available` or `validation_error` `error_type`: these conditions fold onto `invalid_input`. The `error_type` set can still grow, so treat any value you do not recognize as `internal_error` rather than switching exhaustively.

#### Body

application/json

The partner model's native JSON input, identical to the body the synchronous route accepts for this model. It is validated against the model's own input schema as a default run validates it (this route takes no `strict_mode` or `reject_unknown_fields`), and its own fields (the output count, the operation an input image selects) decide what is priced.

A partner model's native JSON input document, forwarded to the provider as-is. Its concrete shape is owned by the partner rather than by Comfy, so this is an open object: Router does not narrow, rename, or re-envelope the fields. It is a named component (never an inline anonymous object) because ComfyUI's spec-driven codegen needs a class to generate.

#### Response

200

application/json

The quote. Read `source` before reading any amount: only `exact` carries `amount`, and an `unknown` quote carries a `reason` instead of a figure.

What Comfy will charge for this call, priced before dispatch from the same rate card the charge is billed against, in US dollars. `source` says how much to trust the number: `exact` carries `amount`; `estimated` carries `min_amount` and `max_amount` and no `amount`; `unknown` carries neither and a `reason`. Never read an absent `amount` as free. Not a price lock: see `pricing_as_of`.

​

source

string

required

`exact` | `estimated` | `unknown`; read any other value as `unknown`.

​

currency

string

required

Always `USD`.

​

provider

string

required

The provider leg this quote is for. On a queued submit it is the leg that will run.

​

model

string

required

A canonical Comfy Router model ID, `{provider}/{model}` \- exactly the value that addresses the model on `POST /v2/models/{provider}/{model}`, so a caller can interpolate it into that path without re-deriving it from anything. Its `pattern` is `RouterProviderSegment` and `RouterModelSegment` joined by a single `/`, and `maxLength` is their sum plus that separator.

Maximum string length: `193`

Pattern: `^[a-z0-9]+([._-][a-z0-9]+)*/[a-z0-9]+([._-][a-z0-9]+)*$`

Example:

`"bfl/flux-2-pro"`

​

pricing_as_of

string<date-time>

required

When the rate card this quote was priced from was fetched. The run is charged at the rates in force when it is rated, not at this instant. Whenever no rate card was read (`reason: pricing_unavailable`, `byok`, or a `not_quotable` call that cannot be priced from any card), this is when the quote was answered.

​

amount

string

Dollars as a decimal string, e.g. "0.04", with up to 8 decimals and no exponent. A chargeable sub-cent price is never rendered as "0". Present only when `source` is `exact`.

​

min_amount

string

The lower bound in dollars as a decimal string. Present only when `source` is `estimated`.

​

max_amount

string

The upper bound in dollars as a decimal string. Present only when `source` is `estimated`.

​

amount_cents

number<double>

The same figure in US cents, unrounded, for arithmetic. Present with `amount`.

​

min_amount_cents

number<double>

`min_amount` in US cents, unrounded. Present with `min_amount`.

​

max_amount_cents

number<double>

`max_amount` in US cents. Present with `max_amount`.

​

credits

number<double>

`amount` in Comfy credits using the platform conversion ($1 = 211 credits), rounded to 2 decimals - the figure `X-Comfy-Credits-Used` will carry for an `exact` quote.

​

reason

string

Present only when `source` is `unknown`: `not_quotable` (Router cannot price this call before it runs - its price depends on what the provider reports back, or the body does not bound a billed quantity), `unpriced_model` (the rate card does not price this request), `byok` (queued submit only: the run uses your own provider key, so Comfy bills nothing for it), or `pricing_unavailable` (queued submit only: the rate card could not be read when the request was admitted; this is transient, and the run is still charged as usual). Read any other value as `not_quotable`.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/api-reference/router/comfy-router/price-a-model-call-before-running-it-without-running-it.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/router/comfy-router/price-a-model-call-before-running-it-without-running-it)

[Run a partner model synchronously by canonical model ID.Previous](https://docs.comfy.org/api-reference/router/comfy-router/run-a-partner-model-synchronously-by-canonical-model-id)[Read one partner model's input and output schemas as an OpenAPI document.Next](https://docs.comfy.org/api-reference/router/comfy-router/read-one-partner-models-input-and-output-schemas-as-an-openapi-document)

⌘I

[ComfyUI home page![light logo](https://mintcdn.com/dripart/WCFdTagRdhtvk9-o/logo/light.svg?fit=max&auto=format&n=WCFdTagRdhtvk9-o&q=85&s=ec112de87239058f5a931a7e4b594965)![dark logo](https://mintcdn.com/dripart/QzWbjSCBG7w61rR3/logo/dark.svg?fit=max&auto=format&n=QzWbjSCBG7w61rR3&q=85&s=62b4d879fb3aadbd7a468d1539032d6f)](https://docs.comfy.org/)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

Resources

[installation](https://docs.comfy.org/installation/system_requirements)[Tutorials](https://docs.comfy.org/tutorials/basic/text-to-image)[Development](https://docs.comfy.org/development/overview)

Products

[Features](https://www.comfy.org/?utm_source=docs)[Gallery](https://www.comfy.org/gallery?utm_source=docs)[Download](https://www.comfy.org/download?utm_source=docs)

Company

[About](https://www.comfy.org/about?utm_source=docs)[Careers](https://www.comfy.org/careers?utm_source=docs)[Terms of Service](https://www.comfy.org/terms-of-service?utm_source=docs)[Privacy Policy](https://www.comfy.org/privacy-policy?utm_source=docs)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=dripart)

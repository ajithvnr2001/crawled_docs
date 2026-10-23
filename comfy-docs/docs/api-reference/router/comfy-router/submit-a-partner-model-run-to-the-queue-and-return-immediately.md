---
url: https://docs.comfy.org/api-reference/router/comfy-router/submit-a-partner-model-run-to-the-queue-and-return-immediately/
title: Submit a partner model run to the queue and return immediately. - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:12.083843+00:00
---

# Submit a partner model run to the queue and return immediately. - ComfyUI

> Source: https://docs.comfy.org/api-reference/router/comfy-router/submit-a-partner-model-run-to-the-queue-and-return-immediately/

Submit a partner model run to the queue and return immediately.

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/v2/models/{provider}/{model}/requests \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '{}'
    
    
    import requests
    
    url = "https://api.comfy.org/v2/models/{provider}/{model}/requests"
    
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
    
    fetch('https://api.comfy.org/v2/models/{provider}/{model}/requests', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/v2/models/{provider}/{model}/requests",
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
    
    	url := "https://api.comfy.org/v2/models/{provider}/{model}/requests"
    
    	payload := strings.NewReader("{}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/v2/models/{provider}/{model}/requests")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/v2/models/{provider}/{model}/requests")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{}"
    
    response = http.request(request)
    puts response.read_body

201

400

401

402

403

404

409

413

422

503
    
    
    {
      "status_url": "https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21/status",
      "response_url": "https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21",
      "cancel_url": "https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21/cancel",
      "request_id": "6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21",
      "status": "IN_QUEUE",
      "queue_position": 3,
      "estimate": {
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

# Submit a partner model run to the queue and return immediately.

Copy pageCopy page

Comfy Router’s queued delivery mode. The request body is the same partner-native JSON input `POST /v2/models/{provider}/{model}` accepts for this model - one body shape, one per-model schema, two delivery modes - but this route does not hold the connection for the result. It admits the run, answers `201` with a handle, and the caller collects the result later through the three reads below.

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

requests

Try it

Submit a partner model run to the queue and return immediately.

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/v2/models/{provider}/{model}/requests \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '{}'
    
    
    import requests
    
    url = "https://api.comfy.org/v2/models/{provider}/{model}/requests"
    
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
    
    fetch('https://api.comfy.org/v2/models/{provider}/{model}/requests', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/v2/models/{provider}/{model}/requests",
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
    
    	url := "https://api.comfy.org/v2/models/{provider}/{model}/requests"
    
    	payload := strings.NewReader("{}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/v2/models/{provider}/{model}/requests")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/v2/models/{provider}/{model}/requests")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{}"
    
    response = http.request(request)
    puts response.read_body

201

400

401

402

403

404

409

413

422

503
    
    
    {
      "status_url": "https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21/status",
      "response_url": "https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21",
      "cancel_url": "https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21/cancel",
      "request_id": "6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21",
      "status": "IN_QUEUE",
      "queue_position": 3,
      "estimate": {
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

#### Headers

​

Idempotency-Key

string

Caller-generated key that makes retrying one logical call safe. A call that reached the caller with an answer is recorded against its key for 24 hours, and a retry carrying the same key is answered from that record instead of dispatching - and charging - the provider a second time, marked `Idempotent-Replayed: true`. Keys are scoped to the workspace your credential carries, or to your user when it carries none - so the keyspace is shared by every member of a workspace rather than private to one caller. Make a key unique across the whole workspace, not just within your own client: a second member who reuses a key string is answered from the first member's record, or refused `409` if the request differs. Because the scope follows the credential and not the person, a credential that carries no workspace at all scopes to your user id instead - so retrying one logical call under a different credential can land in a different namespace, where it is dispatched and charged again. Retry with the credential you started with. A keyed request with no authenticated caller is refused `401`. The guarantee is a billing one: a key is charged at most once. It is not a promise that a key is dispatched at most once, and it does not make a lost call resumable. Some answers are recorded but not replayable for the full 24 hours, and the billing guarantee is the half that always holds: the key stays consumed - the retry never re-runs and never re-charges - but it is answered `409 invalid_input` instead of being served the original body. That happens whenever Comfy does not hold a copy of the response it can still stand behind; a response past the replay size cap and a result addressed by an asset URL Comfy does not host are the two you are most likely to meet. The second is the one worth planning for, because it looks like an ordinary success: which models answer with a Comfy-hosted asset link, how long one stays valid, and what a result carries when an individual asset could not be copied are stated in one place, under Result assets in the API reference, and this paragraph does not restate them. On a model that returns its result on the original call, an answer still holding a partner's own asset link is replayed for a few minutes - which is where a dropped connection puts an SDK's automatic same-key re-send, and while the partner's link is certainly still alive - and refused after that rather than replayed dead. So a prompt retry of a partially re-hosted result behaves exactly like any other replay, and only a later one meets the `409`. That short window is deliberately not offered on a model that submits and is polled, because there the partner may have minted the URL long before your call collected it and its remaining life is unknowable - and those models do not need it: a call cut off mid-generation keeps its key holding the generation, so the same-key retry collects the original result rather than a recorded copy of it. A response past the size cap has no window either and is refused from the start. The action on any of these `409 invalid_input` refusals is the same: use a new key. Only an answer a provider actually produced is recorded, though. A refusal Router raises on its own before dispatching anything - not enabled for you yet (`403`), unknown model (`404`), not entitled to the model (`403`), a body the model's schema rejects or that names a different model than the path (`422`), a malformed request (`400 invalid_input`) - dispatched nothing and charged nothing, so it releases the key: re-send the same key once you are on the rollout ramp or have corrected the request and it runs for real, rather than replaying the refusal or colliding with it as a `409`. That turns on whether a provider was reached, never on the status, so a `400 content_policy_violation` \- the partner's own answer to a call that ran, which some models meter - is recorded and replayed like any other answer. Releasing a refusal that dispatched nothing frees nothing chargeable, so it does not weaken the at-most-once billing guarantee above.

Required string length: `1 - 255`

Example:

`"6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21"`

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

​

strict_mode

boolean

default:false

Only meaningful together with `model_provider`. `false` (the default): the request body must be this model's own native contract, translated to the alternate provider's real schema - any native field that cannot be expressed exactly is dropped and disclosed via the response's `X-Comfy-Router-Dropped-Params` header, never silently. `true`: the body must already be the alternate provider's own real schema, passed through unmodified in both directions - no translation, so `X-Comfy-Router-Dropped-Params` is never sent, and provider fallback is disabled for the call because a body shaped for one provider cannot be replayed against another (see `fallback_provider`).

​

reject_unknown_fields

boolean

default:false

Opt in to refusing a top-level request-body field this model's input schema does not declare, rather than accepting it; nested fields are not checked, and nothing is refused for a model whose schema allows undeclared fields or has no authored schema, or on a queued submit sent with `strict_mode=true`.

#### Body

application/json

The partner model's native JSON input, identical to the body the synchronous route accepts for this model, and it selects the operation and is metered the same way: the body's own fields choose which operation Router runs on a model that supports more than one (an input image switches an editable image model to image-to-image, which may be metered on its own rate; a Seedance first-frame image selects image-to-video and a reference image or clip selects reference-to-video). On native dispatch a Seedance request bills by the media kinds in `content`, not the roles: any video input bills as video-to-video, otherwise any image bills as image-to-video, otherwise text-to-video, except that a final render from a `draft_task` item bills as the operation of the Draft it renders, with some models charging the same rate for text-to-video and image-to-video; with `model_provider` selecting an alternate provider, each conditioned operation may be metered on that provider's own rate. The same provider-selection contract applies at dispatch: without `model_provider`, or with `model_provider` and `strict_mode=false` (the default), the body is the model's native document and is validated against the model's own input schema before the run is admitted, so a body the model would reject is a `422` here rather than a queued request that fails minutes later - a non-strict alternate-provider body is additionally translated into that provider's real schema at dispatch. With `strict_mode=true` the body must already be the alternate provider's own schema and is forwarded unchanged: native-schema validation is skipped, exactly as on the synchronous route (see `model_provider` and `strict_mode`).

A partner model's native JSON input document, forwarded to the provider as-is. Its concrete shape is owned by the partner rather than by Comfy, so this is an open object: Router does not narrow, rename, or re-envelope the fields. It is a named component (never an inline anonymous object) because ComfyUI's spec-driven codegen needs a class to generate.

#### Response

201

application/json

Created - the run was admitted to the queue. The body is the handle: the `request_id`, `status: IN_QUEUE`, a `queue_position` snapshot, and the `status_url`, `response_url` and `cancel_url` that address the rest of this request's lifetime. It is deliberately `201` and not `202`: a queued request is a resource this call created and the three URLs address it, whereas the `202` on the result read below means "not ready yet, ask again" and creates nothing.

The handle returned when a run is admitted to the queue: the request's identity and state, composed with the three URLs that address the rest of its lifetime.

​

status_url

string<uri>

required

Absolute URL of this request's status read.

Example:

`"https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21/status"`

​

response_url

string<uri>

required

Absolute URL this request's result is collected from.

Example:

`"https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21"`

​

cancel_url

string<uri>

required

Absolute URL a cancellation is asked for at.

Example:

`"https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21/cancel"`

​

request_id

string<uuid>

required

Identifier of one queued Router request - the handle a caller polls, cancels and collects a result by.

Maximum string length: `36`

Pattern: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

Example:

`"6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21"`

​

status

enum<string>

required

The state of a queued Router request. It has exactly three values, and unlike `RouterErrorType` this one is a closed `enum`, because the two schemas are closed in opposite directions on purpose. `RouterErrorType` classifies failures and its set is expected to grow, so a generated client that hard-rejected an unrecognised bucket would fail hardest exactly when something had already gone wrong. This one is a lifecycle, and a lifecycle with a fourth state added later is a breaking change to every polling loop written against it whether it is declared as an enum or not - so it is declared as one, and the constraint is stated where a client can see it.

Available options: 

`IN_QUEUE`, 

`IN_PROGRESS`, 

`COMPLETED`

Example:

`"IN_QUEUE"`

​

queue_position

integer

How many requests are ahead of this one in the queue, at the instant the response was composed. Zero means this request is at the front.

Required range: `x >= 0`

Example:

`3`

​

estimate

object

The pre-flight cost estimate for this request, present on a fresh admission when the cost estimate is enabled for the caller. It quotes the provider leg this request was pinned to (the queue has no fallback loop, so `fallback_provider` never changes the leg that runs). When no figure can be given it is still present, with `source: unknown`; the submission never fails because of the estimate. Omitted on an idempotent replay (`Idempotent-Replayed: true`), because the original quote is not stored. It is not a price lock: the run is charged at the rates in force when it is rated.

Show child attributes

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/api-reference/router/comfy-router/submit-a-partner-model-run-to-the-queue-and-return-immediately.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/router/comfy-router/submit-a-partner-model-run-to-the-queue-and-return-immediately)

[Read one partner model's input and output schemas as an OpenAPI document.Previous](https://docs.comfy.org/api-reference/router/comfy-router/read-one-partner-models-input-and-output-schemas-as-an-openapi-document)[Collect the result of one submitted request.Next](https://docs.comfy.org/api-reference/router/comfy-router/collect-the-result-of-one-submitted-request)

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

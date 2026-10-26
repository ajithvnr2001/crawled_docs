---
url: https://docs.comfy.org/es/registry/api-reference/comfy-router/run-a-partner-model-synchronously-by-canonical-model-id/
title: Run a partner model synchronously by canonical model ID. - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:32.883250+00:00
---

# Run a partner model synchronously by canonical model ID. - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/comfy-router/run-a-partner-model-synchronously-by-canonical-model-id/

Run a partner model synchronously by canonical model ID.

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/v2/models/{provider}/{model} \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '{}'
    
    
    import requests
    
    url = "https://api.comfy.org/v2/models/{provider}/{model}"
    
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
    
    fetch('https://api.comfy.org/v2/models/{provider}/{model}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/v2/models/{provider}/{model}",
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
    
    	url := "https://api.comfy.org/v2/models/{provider}/{model}"
    
    	payload := strings.NewReader("{}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/v2/models/{provider}/{model}")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/v2/models/{provider}/{model}")
    
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

402

403

404

409

413

422

429

502

503

504
    
    
    "<string>"
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
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
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }

Comfy Router

# Run a partner model synchronously by canonical model ID.

Copiar páginaCopiar página

Comfy Router’s canonical, model-ID-addressed entry point. The request body is the partner model’s own native JSON input and the success response is that model’s own native output — JSON for most models, but the partner’s raw bytes (for example `audio/mpeg` for a text-to-speech model) for a model whose partner answers with a binary body: Router forwards both without imposing a Comfy-shaped envelope, so for most models a caller can move between the partner’s API and Router by changing the host. The exception is a model whose partner operation takes an identifier in its request path: Router has the caller name it as a top-level body field and moves it into the partner path, so that request needs that one adaptation. This is the synchronous path: the response carries the finished result. The path addresses a model by the canonical `{provider}/{model}` model ID. Both segments are lowercase. A third `variant` segment is RESERVED rather than part of the canonical ID: how a variant is addressed is not settled by this contract, so no published `pattern` accepts one. For a model whose partner API names the model in the request body, Router sets that field to the path’s model; a body that names a different model is refused with `invalid_input`. The mirror of that also exists, for a model whose partner operation needs an identifier the two-segment model ID cannot carry: the caller names it as a top-level field of the request body, and Router moves it into the partner request PATH and removes it from the forwarded body, because the partner’s own input schema does not declare it. `elevenlabs/eleven_multilingual_v2` is the first such model — it requires a top-level `voice_id`, which must be ASCII letters and digits only (A-Z, a-z, 0-9) and at most 64 characters. A body that omits it, names it twice, gives it a value that is not a string, gives it a value outside that alphabet, or gives it a value longer than 64 characters is refused with `invalid_input` before anything is dispatched or charged. Router serves image results as re-hosted URLs on Comfy storage, so for an image model it OWNS the partner’s `response_format` on the outbound request and coerces it to `url`. The field is still accepted for compatibility with the `/proxy/` surface and is not an error, but it does not select what a successful response carries: a `b64_json` request and a `url` request are answered identically, with URLs. Where an individual image cannot be re-hosted, its entry keeps xAI’s own short-lived URL rather than a Comfy one — see the model’s output schema. Naming the field twice in one body is refused with `invalid_input`, because which spelling the partner would read is not defined. An out-of-enum value is REFUSED rather than coerced, on this Router dispatch and on the `/proxy/` image routes alike; only the shape of the refusal differs. Here it is the per-field `422` pre-provider validation writes, because the input schema this surface publishes is the one it enforces. The `/proxy/` image routes coerce the field the same way rather than honouring it as written, and they refuse an out-of-enum value with a `400` at ingress. This operation is deliberately tagged `Comfy Router` and NOT `API Nodes`. The `API Nodes` tag drives ComfyUI’s Partner-Node Pydantic codegen, so reusing it here would couple the Router contract to that generator.

Copiar páginaCopiar página

POST

/

v2

/

models

/

{provider}

/

{model}

Pruébalo

Run a partner model synchronously by canonical model ID.

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/v2/models/{provider}/{model} \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '{}'
    
    
    import requests
    
    url = "https://api.comfy.org/v2/models/{provider}/{model}"
    
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
    
    fetch('https://api.comfy.org/v2/models/{provider}/{model}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/v2/models/{provider}/{model}",
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
    
    	url := "https://api.comfy.org/v2/models/{provider}/{model}"
    
    	payload := strings.NewReader("{}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/v2/models/{provider}/{model}")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/v2/models/{provider}/{model}")
    
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

402

403

404

409

413

422

429

502

503

504
    
    
    "<string>"
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
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
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }

#### Autorizaciones

BearerAuthApiKeyAuthBearerAuthApiKeyAuth

​

Authorization

string

header

requerido

Bearer token authentication. Normally a Firebase or Cloud JWT. A 'comfyui-' prefixed API key is also accepted in this header: the prefix classifies the value as an API key and it is validated exactly as if it had been sent in X-API-Key. Accepted on the operations served by the comfyFirebase auth middleware (BE-9720, parity with ingest).

#### Encabezados

​

Idempotency-Key

string

Caller-generated key that makes retrying one logical call safe. A call that reached the caller with an answer is recorded against its key for 24 hours, and a retry carrying the same key is answered from that record instead of dispatching - and charging - the provider a second time, marked `Idempotent-Replayed: true`. Keys are scoped to the workspace your credential carries, or to your user when it carries none - so the keyspace is shared by every member of a workspace rather than private to one caller. Make a key unique across the whole workspace, not just within your own client: a second member who reuses a key string is answered from the first member's record, or refused `409` if the request differs. Because the scope follows the credential and not the person, a credential that carries no workspace at all scopes to your user id instead - so retrying one logical call under a different credential can land in a different namespace, where it is dispatched and charged again. Retry with the credential you started with. A keyed request with no authenticated caller is refused `401`. The guarantee is a billing one: a key is charged at most once. It is not a promise that a key is dispatched at most once, and it does not make a lost call resumable. Some answers are recorded but not replayable for the full 24 hours, and the billing guarantee is the half that always holds: the key stays consumed - the retry never re-runs and never re-charges - but it is answered `409 invalid_input` instead of being served the original body. That happens whenever Comfy does not hold a copy of the response it can still stand behind; a response past the replay size cap and a result addressed by an asset URL Comfy does not host are the two you are most likely to meet. The second is the one worth planning for, because it looks like an ordinary success: which models answer with a Comfy-hosted asset link, how long one stays valid, and what a result carries when an individual asset could not be copied are stated in one place, under Result assets in the API reference, and this paragraph does not restate them. On a model that returns its result on the original call, an answer still holding a partner's own asset link is replayed for a few minutes - which is where a dropped connection puts an SDK's automatic same-key re-send, and while the partner's link is certainly still alive - and refused after that rather than replayed dead. So a prompt retry of a partially re-hosted result behaves exactly like any other replay, and only a later one meets the `409`. That short window is deliberately not offered on a model that submits and is polled, because there the partner may have minted the URL long before your call collected it and its remaining life is unknowable - and those models do not need it: a call cut off mid-generation keeps its key holding the generation, so the same-key retry collects the original result rather than a recorded copy of it. A response past the size cap has no window either and is refused from the start. The action on any of these `409 invalid_input` refusals is the same: use a new key. Only an answer a provider actually produced is recorded, though. A refusal Router raises on its own before dispatching anything - not enabled for you yet (`403`), unknown model (`404`), not entitled to the model (`403`), a body the model's schema rejects or that names a different model than the path (`422`), a malformed request (`400 invalid_input`) - dispatched nothing and charged nothing, so it releases the key: re-send the same key once you are on the rollout ramp or have corrected the request and it runs for real, rather than replaying the refusal or colliding with it as a `409`. That turns on whether a provider was reached, never on the status, so a `400 content_policy_violation` \- the partner's own answer to a call that ran, which some models meter - is recorded and replayed like any other answer. Releasing a refusal that dispatched nothing frees nothing chargeable, so it does not weaken the at-most-once billing guarantee above. Generate a fresh key per logical call and reuse it across that call's retry attempts; a UUID is the intended shape. Persist the key BEFORE sending the request - a key held only in the memory of the process that crashed cannot be resent, and the retry that would have collected the result becomes a fresh, separately charged run. A retry that arrives while the original is still in flight is answered `409` with `Retry-After`: wait and re-send the same key. The same key presented with a DIFFERENT request is a `409` too, rather than a silent overwrite - and "different" is judged on the whole request, not the body alone: the method, the path and query string, and the body must all match the original. THE KEY IS NEVER RETURNED IN ANY RESPONSE - not on the `200`, not on the `504`, not in any error body. It is yours to mint and yours to keep: a caller who did not keep it has no way to collect a generation they were billed for. A `deadline_exceeded` `504` on a generation the provider is still running answers a same-key retry with `504` and `Retry-After` again until it finishes, then with the result. Omitting the header is allowed and leaves the call unguarded rather than refused: there is nothing to check, so every retry is a fresh dispatch and a fresh charge.

Required string length: `1 - 255`

Ejemplo:

`"6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21"`

#### Parámetros de ruta

​

provider

string

requerido

Lowercase provider segment of the canonical `{provider}/{model}` model ID - the partner whose model is being run. The schema is `RouterProviderSegment`, the SAME component a catalog entry's `provider` field references, so an ID `GET /v2/models` lists cannot drift from the ids this route accepts. Its `pattern` is a CONTRACT statement, not enforcement: comfy-api installs no OpenAPI request validator and oapi-codegen binds path parameters as plain strings, so the handler must re-validate this segment itself before using it to select a provider or compose an upstream URL. Lowercase `provider` segment of the canonical `{provider}/{model}` model ID - the partner whose model is being addressed. The invocation route's `provider` path parameter and a catalog entry's `provider` field both reference this one schema, which is what keeps the listed IDs and the accepted IDs from drifting apart. The `pattern` is a CONTRACT statement, not enforcement: comfy-api installs no OpenAPI request validator and oapi-codegen binds path parameters as plain strings, so a handler must re-validate the segment itself before using it to select a provider or compose an upstream URL. The alphabet deliberately admits no `/`, no percent-encoding, and no repeated separator, so no accepted value can contain a `.` or `..` path segment.

Maximum string length: `64`

Pattern: `^[a-z0-9]+([._-][a-z0-9]+)*$`

Ejemplo:

`"bfl"`

​

model

string

requerido

Lowercase model segment of the canonical `{provider}/{model}` model ID - the model to run within that provider. As with `provider`, the schema is the shared `RouterModelSegment` component and its `pattern` documents the contract rather than enforcing it - see `RouterProvider`. Lowercase `model` segment of the canonical `{provider}/{model}` model ID - the model to run within that provider. Shared by the invocation route's `model` path parameter and a catalog entry's `model` field, for the same no-drift reason as `RouterProviderSegment`. As with the provider segment, the `pattern` documents the contract and does not enforce it. Dots are permitted inside the segment because partner model IDs use them for versions (`flux-pro-1.1`), but a repeated separator is not, so `..` cannot appear.

Maximum string length: `128`

Pattern: `^[a-z0-9]+([._-][a-z0-9]+)*$`

Ejemplo:

`"flux-2-pro"`

#### Parámetros de consulta

​

model_provider

string

Selects an alternate provider to serve this model, instead of its current default. Omitting it runs native dispatch on the model's own default provider; `default`, `comfy`, and `comfyui` are aliases for that same native behavior and name no override, because Comfy Router is never itself a serving backend. The alternate providers Router can retarget a model onto are `fal`, `wavespeed`, `runware`, and `higgsfield`; which of them a given model supports is reported by `GET /v2/models/{provider}/{model}`. When an alternate provider is selected, the native request body is translated into that provider's real schema unless `strict_mode=true`; see `strict_mode` and `fallback_provider`. Its refusals are checked in a fixed order, and an earlier one answers whether or not a later one would. A value that is not a registered provider at all is refused `400` with `error_type: invalid_input`. Then a request whose body selects a multipart operation (an edit - for example gpt-image's `image` field) is refused `409`, also with `error_type: invalid_input`, whose `detail` begins "this request's `image` selects the edit operation" - but only when the named provider's translator for this model cannot itself serve that operation; a leg whose translator does carry the media is not refused and proceeds normally, so this is a per-leg refusal rather than a blanket one. Then a request that has already resolved a bring-your-own-key credential for the provider in the path is refused `409`, also with `error_type: invalid_input`, whose `detail` begins `this request resolved a BYOK credential` \- see the `409` on this route, where that `detail` is the only thing separating this case, and the multipart case above, from the `Idempotency-Key` one. That BYOK check runs whether or not the named provider has a leg for this model. Then the named provider's own gate refuses `403` with `error_type: not_enabled` when that provider is not turned on for you, and `503` with `error_type: service_unavailable` when the gate cannot be evaluated - a flag-evaluation failure, or a missing or nil gate entry. Only past all of those is a real provider that does not serve this model refused `400` with `error_type: invalid_input`, the same answer as a value that is not a registered provider at all - both mean the `model_provider` value cannot serve this model, and that `400`'s `detail` is human-readable and not a contract, so read `GET /v2/models/{provider}/{model}` to learn which providers a model does support rather than parsing it; past that `400`, this workspace's partner-provider policy for the named vendor is evaluated too and can refuse `403` or `503` of its own. Neither this parameter nor `fallback_provider` is available on a BYOK request, and the two are unavailable in different ways: the credential was resolved for the provider named in the path while every alternate leg dispatches on Comfy's own key, so an explicit `model_provider` is refused with that `409`, and `fallback_provider` is inert rather than refused - no retry against an alternate provider is attempted and the first attempt's own failure is what the caller receives. The same split applies to a multipart body: only an explicit `model_provider` reaches the `409` above, and only for a leg whose translator cannot serve the operation, while the automatic on-failure retry `fallback_provider` controls is simply skipped (inert, not refused) for any multipart body. Router defines no `provider_not_available` or `validation_error` `error_type`: these conditions fold onto `invalid_input`. The `error_type` set can still grow, so treat any value you do not recognize as `internal_error` rather than switching exhaustively.

​

strict_mode

boolean

predeterminado:false

Only meaningful together with `model_provider`. `false` (the default): the request body must be this model's own native contract, translated to the alternate provider's real schema - any native field that cannot be expressed exactly is dropped and disclosed via the response's `X-Comfy-Router-Dropped-Params` header, never silently. `true`: the body must already be the alternate provider's own real schema, passed through unmodified in both directions - no translation, so `X-Comfy-Router-Dropped-Params` is never sent, and provider fallback is disabled for the call because a body shaped for one provider cannot be replayed against another (see `fallback_provider`).

​

fallback_provider

string

Controls whether Router retries this call against another of the model's registered providers when the first attempt fails for a reason attributable to Router's own side or to the specific provider tried - never for a reason attributable to the request itself (an unretried failure is refused exactly as it always was). Omitted, or any value other than `false`, turns fallback on (the default) and Router scans the model's registered alternates in a fixed order and retries once against the first eligible one. `false` turns fallback off: a failure is refused, never retried. A successful fallback response carries the `X-Comfy-Router-Fallback-Provider` header, naming the provider that served it; a fallback attempt that itself also fails does not carry the header, and no case retries a generation that may already have been submitted to a provider. Fallback also turns itself off, regardless of this parameter, on a request that resolved a bring-your-own-key credential, on a request whose body selects a multipart operation, and under `strict_mode=true` \- each binds the call to one specific provider and cannot be faithfully replayed against another: the alternate leg would dispatch on Comfy's own key rather than on the caller's credential, no alternate translator is guaranteed to carry the multipart media field, and a strict body is already shaped for one provider rather than for the native contract. Each of those is inert, not refused - no retry is attempted and the first attempt's own failure reaches the caller unchanged. Only an explicit `model_provider` is refused, and see that parameter for the `409`s it answers with; note that fallback's multipart disable is unconditional, while `model_provider`'s multipart `409` applies only to a leg whose translator cannot serve the operation.

​

reject_unknown_fields

boolean

predeterminado:false

Opt in to refusing a top-level request-body field this model's input schema does not declare, rather than accepting it; nested fields are not checked, and nothing is refused for a model whose schema allows undeclared fields or has no authored schema, or on a queued submit sent with `strict_mode=true`. Omitted, or `false` (the default): unchanged behaviour. Most model input schemas here are open, so a field Comfy has not authored is accepted and forwarded, which is what lets a field a partner already supports reach it before Comfy documents it. The cost is that a misspelled field name, or a nested field written at the top level, is accepted too - and then dropped on the way to the provider, so the generation runs, and is billed, under the defaults that field was meant to change. `true`: a top-level field the published input schema does not declare is answered 422 with an `extra_forbidden` entry naming it, before any provider call is made and before anything is billed. Only the top level is checked, and only names that match no declared property even case-insensitively - a field whose spelling differs from a declared one only by case is already refused (`property_name_case`) regardless of this parameter. A model with no authored input schema declares no properties, so it refuses nothing here. What it refuses is a FLOOR, not a ceiling, in two stated cases. A model whose published schema sets `additionalProperties` itself is left exactly as it is: where that is `false` the schema already refuses undeclared fields with or without this parameter, and where it is `true` \- as on the Anthropic and Gemini Interactions models, whose schemas promise fields such as `tools`, `temperature` and `safety_settings` pass through unchanged - the schema has declared that an undeclared field is allowed, and this parameter does not overrule it. And where a schema is a union (`oneOf`/`anyOf`), a field belonging to any branch is accepted, not only to the branch the body matched. The parameter is per-request on purpose: closing every schema instead would start refusing bodies that succeed today, with no way for an existing caller to keep the behaviour they built against. It is accepted on both the synchronous `POST` and the queued `POST .../requests` submit, which validate the same body against the same schema. The one exception is `strict_mode=true` on the queued submit: that body is already in the alternate provider's own shape, so the queue does not validate it against this model's schema, and this parameter is accepted but has no effect there.

#### Cuerpo

application/json

The partner model's native JSON input. Without `model_provider` the request runs native dispatch on the model's default provider and this body is the model's own native schema, forwarded unchanged (`strict_mode` is meaningless there and changes nothing). With `model_provider` selecting an alternate provider and `strict_mode=false` (the default), the body is translated into that provider's real schema before it is sent - any native field that cannot be expressed exactly is dropped and disclosed via the response's `X-Comfy-Router-Dropped-Params` header, never silently. With `model_provider` selecting an alternate provider and `strict_mode=true` no translation runs: the body must already be that alternate provider's own real schema, not this model's native one (see `strict_mode`), and is forwarded unchanged. The body's own fields also select which operation Router runs on a model that supports more than one: for an editable image model, including an input image switches it from text-to-image to the image-to-image (edit) operation, which may be metered on its own rate; for a Seedance video model, `content[].role` selects the operation (a first-frame image selects image-to-video, a reference image or clip selects reference-to-video). On native dispatch, Seedance billing follows the media kinds in `content`, not the roles: a request with any video input bills as video-to-video, otherwise one with any image bills as image-to-video, otherwise text-to-video, except that a final render from a `draft_task` item bills as the operation of the Draft it renders; some models charge the same rate for text-to-video and image-to-video. With `model_provider` selecting an alternate provider, each conditioned operation may be metered on that provider's own rate.

A partner model's native JSON input document, forwarded to the provider as-is. Its concrete shape is owned by the partner rather than by Comfy, so this is an open object: Router does not narrow, rename, or re-envelope the fields. It is a named component (never an inline anonymous object) because ComfyUI's spec-driven codegen needs a class to generate. Declaring an object here is a codegen requirement, not a licence to re-decode the payload: numeric fidelity is the handler's job, since decoding into a Go `map[string]any` rounds integers above 2^53 (partner seeds and IDs) to `float64`. Forward the raw bytes rather than round-tripping them through a generic map. Body size is likewise bounded at the handler - comfy-api caps comparable bodies with `http.MaxBytesReader` \- not by this schema.

#### Respuesta

200

*/*

OK - without `model_provider`, or with `model_provider` and `strict_mode=false` (the default, translated back into this model's native contract when possible, falling back to the alternate provider's own raw response on a translation failure - logged, never silent), the shape is this model's own native output; with `strict_mode=true` it is the alternate provider's response returned unchanged. For most models that is JSON (`RouterModelOutput`); for a model whose partner answers a generation directly as bytes - the ElevenLabs audio models are the first in the catalog - it is those bytes, and the response carries the partner's own `Content-Type` (`audio/mpeg`, `audio/wav`, ...) rather than `application/json`. A client must branch on the response `Content-Type` and must not assume a JSON document; the per-model contract is published at `GET /v2/models/{provider}/{model}/openapi.json`. This response carries `X-Content-Type-Options: nosniff`, so a partner media type is taken at its word and never sniffed into something else. When this response was replayed from the record held against an `Idempotency-Key` rather than produced by running the model again, it carries `Idempotent-Replayed: true` and is not charged a second time.

The response is of type `file`.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/comfy-router/run-a-partner-model-synchronously-by-canonical-model-id.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/comfy-router/run-a-partner-model-synchronously-by-canonical-model-id)

[Read one partner model's catalog entry by canonical model ID.](https://docs.comfy.org/es/registry/api-reference/comfy-router/read-one-partner-models-catalog-entry-by-canonical-model-id)[Price a model call before running it, without running it.](https://docs.comfy.org/es/registry/api-reference/comfy-router/price-a-model-call-before-running-it-without-running-it)

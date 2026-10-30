---
url: https://docs.comfy.org/es/registry/api-reference/comfy-router/ask-for-one-submitted-request-to-be-cancelled/
title: Ask for one submitted request to be cancelled. - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-30T13:55:13.381751+00:00
---

# Ask for one submitted request to be cancelled. - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/comfy-router/ask-for-one-submitted-request-to-be-cancelled/

Ask for one submitted request to be cancelled.

cURL
    
    
    curl --request PUT \
      --url https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/cancel \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/cancel"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.put(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'PUT', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/cancel', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/cancel",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "PUT",
      CURLOPT_HTTPHEADER => [
        "Authorization: Bearer <token>"
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
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/cancel"
    
    	req, _ := http.NewRequest("PUT", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.put("https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/cancel")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/cancel")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Put.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

202

400

401

403

404

409

503

default
    
    
    {
      "request_id": "6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21",
      "status": "CANCELLATION_REQUESTED"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "billed_workspace": {
        "type": "<string>",
        "id": "<string>",
        "rail": "<string>"
      },
      "credential_kind": "<string>",
      "denied_reason": "<string>",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "billed_workspace": {
        "type": "<string>",
        "id": "<string>",
        "rail": "<string>"
      },
      "credential_kind": "<string>",
      "denied_reason": "<string>",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "billed_workspace": {
        "type": "<string>",
        "id": "<string>",
        "rail": "<string>"
      },
      "credential_kind": "<string>",
      "denied_reason": "<string>",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "billed_workspace": {
        "type": "<string>",
        "id": "<string>",
        "rail": "<string>"
      },
      "credential_kind": "<string>",
      "denied_reason": "<string>",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "request_id": "6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21",
      "status": "CANCELLATION_REQUESTED"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "billed_workspace": {
        "type": "<string>",
        "id": "<string>",
        "rail": "<string>"
      },
      "credential_kind": "<string>",
      "denied_reason": "<string>",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "billed_workspace": {
        "type": "<string>",
        "id": "<string>",
        "rail": "<string>"
      },
      "credential_kind": "<string>",
      "denied_reason": "<string>",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }

Comfy Router

# Ask for one submitted request to be cancelled.

Copiar páginaCopiar página

Asks Comfy to stop a request that has not finished. It is a request, not a guarantee, and the `202` says exactly that: `CANCELLATION_REQUESTED` means the ask was accepted, not that the run has stopped. A run already on the wire at a partner may complete anyway - and a partner generation that completes is charged, whether or not anyone collected it - so a caller who needs to know what actually happened reads the status endpoint afterwards, where a cancellation that took effect is `COMPLETED` carrying an `error_type` like every other terminal outcome. `PUT` rather than `POST`, and a sub-resource rather than a verb on the request itself: the ask is idempotent. Cancelling twice is the same ask, and the second one is answered exactly like the first while the run is still cancellable, so a client’s retry needs no special case. THE ASK HAS THREE OUTCOMES and the status code carries all three, so a client may branch on the status alone: `202` for `CANCELLATION_REQUESTED`, the ask accepted for a request that had not yet finished; `409` for `ALREADY_COMPLETED`, a request that had already reached a terminal state - success, failure or an earlier cancellation; and `404` for an id that names no request of the caller’s under this model. “Branch on the status alone” is a promise this route keeps rather than a simplification, which is why `ALREADY_COMPLETED` is `409` and not `400`. A cancel carrying a malformed or duplicated `Idempotency-Key` is refused `400 invalid_input` by `RouterIdempotencyMiddleware` in the Router error envelope, so a `400` that also meant `ALREADY_COMPLETED` would put two incompatible bodies behind one status and break exactly the branch this paragraph invites. Every status on this route now maps to one body shape. The first two are ALSO named in the body, as a `RouterQueueCancelStatus`. It is a closed `enum` and not one of the coarse `RouterErrorType` buckets, because it is not the same kind of thing: `RouterErrorType` classifies why a CALL failed, whereas these name what CANCELLING found, and it has no member meaning “already finished”. THE `404` IS THE EXCEPTION AND IT IS DELIBERATE: it answers in the shared Router request-level error body, like every other `404` on this surface, because the status carries two conditions here rather than one. A `{provider}/{model}` that resolves to no partner model is `model_not_found` on this route exactly as on the others, and a cancel-shaped body would swallow it - telling a caller who mistyped the MODEL that their REQUEST does not exist, without the fuzzy suggestions that would have corrected them. So `RouterQueueCancelStatus` carries no `NOT_FOUND` member; the status code is where that outcome is read. This operation is deliberately tagged `Comfy Router` and NOT `API Nodes`, for the reason given on the synchronous route.

Copiar páginaCopiar página

PUT

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

/

{request_id}

/

cancel

Pruébalo

Ask for one submitted request to be cancelled.

cURL
    
    
    curl --request PUT \
      --url https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/cancel \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/cancel"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.put(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'PUT', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/cancel', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/cancel",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "PUT",
      CURLOPT_HTTPHEADER => [
        "Authorization: Bearer <token>"
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
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/cancel"
    
    	req, _ := http.NewRequest("PUT", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.put("https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/cancel")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/cancel")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Put.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

202

400

401

403

404

409

503

default
    
    
    {
      "request_id": "6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21",
      "status": "CANCELLATION_REQUESTED"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "billed_workspace": {
        "type": "<string>",
        "id": "<string>",
        "rail": "<string>"
      },
      "credential_kind": "<string>",
      "denied_reason": "<string>",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "billed_workspace": {
        "type": "<string>",
        "id": "<string>",
        "rail": "<string>"
      },
      "credential_kind": "<string>",
      "denied_reason": "<string>",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "billed_workspace": {
        "type": "<string>",
        "id": "<string>",
        "rail": "<string>"
      },
      "credential_kind": "<string>",
      "denied_reason": "<string>",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "billed_workspace": {
        "type": "<string>",
        "id": "<string>",
        "rail": "<string>"
      },
      "credential_kind": "<string>",
      "denied_reason": "<string>",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "request_id": "6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21",
      "status": "CANCELLATION_REQUESTED"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "billed_workspace": {
        "type": "<string>",
        "id": "<string>",
        "rail": "<string>"
      },
      "credential_kind": "<string>",
      "denied_reason": "<string>",
      "refusal_subject": "<string>",
      "upstream_detail": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "billed_workspace": {
        "type": "<string>",
        "id": "<string>",
        "rail": "<string>"
      },
      "credential_kind": "<string>",
      "denied_reason": "<string>",
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

​

request_id

string<uuid>

requerido

The queued request to address - the `request_id` the submission returned in its body. It is not the submission's `X-Comfy-Request-Id`: that header carries the id of one HTTP call and addresses nothing, as the `RouterQueueRequestId` schema spells out. It is scoped to the caller and to the `{provider}/{model}` in the same URL. An id that is real but was submitted to a different model is a `404` on every read here, not a redirect and not a silent success on the row the id names: the path parameters are redundant with the queued row, and this contract resolves that redundancy strictly so that one id has exactly one address. As with `provider` and `model`, the `format` documents the contract rather than enforcing it - comfy-api installs no OpenAPI request validator and oapi-codegen binds path parameters as plain strings, so a handler must re-validate this segment itself before using it to look a request up. Identifier of one queued Router request - the handle a caller polls, cancels and collects a result by. IT IS NOT THE VALUE OF `X-Comfy-Request-Id`, and the two must not be confused. This id is DURABLE: one value for the whole life of the queued request, returned in the submit response's `request_id` and embedded in every URL that response hands back. `X-Comfy-Request-Id` is the per-CALL id the server mints and re-asserts on every response - the one on that call's usage and audit event and on every log line for it - so a poll loop making twenty calls against one queued request sees twenty different header values and one unchanging `request_id`. READ THE HANDLE FROM THE BODY, never from the header. A client that keeps only the header polls a request that does not exist. The two ids are the two halves of an audit join rather than one value: quote the header to ask about ONE call and the charge it raised, quote `request_id` to ask about the QUEUED REQUEST across every call made against it. It is server-minted and is never read from a request. A caller-supplied handle would let two unrelated calls collide in the audit trail, which is worse than having no join at all. Use `Idempotency-Key` to make a re-submission safe; that is the caller-controlled identifier on this surface, and it is a different job.

Maximum string length: `36`

Pattern: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

Ejemplo:

`"6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21"`

#### Respuesta

202

application/json

Accepted - `CANCELLATION_REQUESTED`. The ask was accepted for a request that had not yet reached a terminal state. It is not a statement that the run has stopped; read the status endpoint to learn what it did.

The answer to a cancellation ask on the two statuses that describe a request this route resolved - the `202` and the `409`. One body shape across both rather than a success envelope plus an error envelope, because both are the same statement - what cancelling found - and a client that has to parse a different type per status code gains nothing from the split. The `404` is NOT this shape. It answers in the shared Router request-level error body, because it also carries the `model_not_found` miss every route on this surface shares; see `RouterQueueCancelStatus` for why that outcome is read off the status code rather than off this body.

​

request_id

string<uuid>

requerido

Identifier of one queued Router request - the handle a caller polls, cancels and collects a result by. IT IS NOT THE VALUE OF `X-Comfy-Request-Id`, and the two must not be confused. This id is DURABLE: one value for the whole life of the queued request, returned in the submit response's `request_id` and embedded in every URL that response hands back. `X-Comfy-Request-Id` is the per-CALL id the server mints and re-asserts on every response - the one on that call's usage and audit event and on every log line for it - so a poll loop making twenty calls against one queued request sees twenty different header values and one unchanging `request_id`. READ THE HANDLE FROM THE BODY, never from the header. A client that keeps only the header polls a request that does not exist. The two ids are the two halves of an audit join rather than one value: quote the header to ask about ONE call and the charge it raised, quote `request_id` to ask about the QUEUED REQUEST across every call made against it. It is server-minted and is never read from a request. A caller-supplied handle would let two unrelated calls collide in the audit trail, which is worse than having no join at all. Use `Idempotency-Key` to make a re-submission safe; that is the caller-controlled identifier on this surface, and it is a different job.

Maximum string length: `36`

Pattern: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

Ejemplo:

`"6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21"`

​

status

enum<string>

requerido

What a cancellation ask found, for the two outcomes that describe a request this route actually resolved. Both are mirrored by the HTTP status, so a client may branch on either. It is deliberately NOT a `RouterErrorType`. That vocabulary classifies why a CALL failed and has no member meaning "already finished"; these two say what cancelling FOUND, which is a different question with a different, genuinely closed answer set - and unlike `RouterErrorType`, which is expected to grow, this one is closed for good, because a request this route resolved was either still cancellable or it was not. A published `RouterErrorType` bucket is never withdrawn, so minting one belongs in the change that raises it. `CANCELLATION_REQUESTED` means the ask was accepted for a request that had not yet reached a terminal state. It does NOT mean the run has stopped: a generation already on the wire at a partner may complete anyway, and a partner generation that completes is charged. Read the status endpoint to learn what actually happened. `ALREADY_COMPLETED` means the request had already reached a terminal state - success, failure, or an earlier cancellation, and this answer does not say which. THE THIRD OUTCOME - no such request - IS THE `404`, and it is deliberately NOT a member here. It is answered in the SHARED Router request-level error body, the same one the two queue reads answer a miss with, because this route's `404` carries TWO conditions and only one of them is about the queue: a `{provider}/{model}` that resolves to no partner model is `model_not_found` here exactly as everywhere else on this surface, and a cancel-shaped `NOT_FOUND` would silently swallow it - telling a caller who mistyped the MODEL that their REQUEST does not exist, and dropping the fuzzy suggestions that would have corrected them. One shape for one condition, and the condition is "this ID resolved to nothing". Branch on the `404`.

Opciones disponibles: 

`CANCELLATION_REQUESTED`, 

`ALREADY_COMPLETED`

Ejemplo:

`"CANCELLATION_REQUESTED"`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/comfy-router/ask-for-one-submitted-request-to-be-cancelled.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/comfy-router/ask-for-one-submitted-request-to-be-cancelled)

[Collect the result of one submitted request.](https://docs.comfy.org/es/registry/api-reference/comfy-router/collect-the-result-of-one-submitted-request)[Read the queue state of one submitted request.](https://docs.comfy.org/es/registry/api-reference/comfy-router/read-the-queue-state-of-one-submitted-request)

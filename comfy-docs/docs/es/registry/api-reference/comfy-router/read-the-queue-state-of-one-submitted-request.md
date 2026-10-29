---
url: https://docs.comfy.org/es/registry/api-reference/comfy-router/read-the-queue-state-of-one-submitted-request/
title: Read the queue state of one submitted request. - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-29T14:00:20.093827+00:00
---

# Read the queue state of one submitted request. - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/comfy-router/read-the-queue-state-of-one-submitted-request/

Read the queue state of one submitted request.

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "GET",
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
    
    	url := "https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

200

401

403

404

410

503

default
    
    
    {
      "cancel_url": "https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21/cancel",
      "response_url": "https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21",
      "status_url": "https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21/status",
      "request_id": "6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21",
      "status": "IN_QUEUE",
      "error_type": "invalid_input",
      "queue_position": 3
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

# Read the queue state of one submitted request.

Copiar páginaCopiar página

The poll endpoint. It answers with the request’s current state and never with the result, so a client can watch a long generation without transferring its output on every poll - the result is collected once, from the read below, when this says `COMPLETED`. THERE ARE EXACTLY THREE STATES: `IN_QUEUE`, `IN_PROGRESS` and `COMPLETED`. There is no separate failed state and no separate cancelled state. A run that failed, and a run the caller cancelled, are both `COMPLETED` carrying an `error_type` \- the same coarse bucket the synchronous route puts on `X-Comfy-Error-Type`. That is a deliberate shape rather than an omission: a polling client’s loop is written against “is it finished yet”, and every terminal outcome answering the same value means the loop has exactly one exit rather than one per way a run can end. Whether the run SUCCEEDED is then a separate question with a separate answer - the presence of `error_type` \- and a client that only wants the result does not have to ask it at all, because the result read below returns the failure in Router’s error envelope on its own. `Retry-After` hints how long to wait before polling again. It is a HINT and not a bound: the read is not refused for arriving early, and the number moves with how far the request has actually got. Honour it anyway - a client that polls faster rarely learns anything sooner, and spends its own rate-limit allowance doing it. The response repeats `status_url`, `response_url` and `cancel_url`, so a client that persisted only the `request_id` can recover the addresses without composing them. A `request_id` that names no request of the caller’s UNDER THIS MODEL is a `404`, including the case where the id is valid but the `{provider}/{model}` in the URL is a different model’s. The path parameters are redundant with the row and this contract resolves that redundancy strictly rather than by ignoring them. This operation is deliberately tagged `Comfy Router` and NOT `API Nodes`, for the reason given on the synchronous route.

Copiar páginaCopiar página

GET

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

status

Pruébalo

Read the queue state of one submitted request.

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "GET",
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
    
    	url := "https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

200

401

403

404

410

503

default
    
    
    {
      "cancel_url": "https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21/cancel",
      "response_url": "https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21",
      "status_url": "https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21/status",
      "request_id": "6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21",
      "status": "IN_QUEUE",
      "error_type": "invalid_input",
      "queue_position": 3
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

200

application/json

OK - the request's current queue state. `status` is one of the three states; `queue_position` is present while the request is still `IN_QUEUE`; `error_type` is present only on a `COMPLETED` request that failed or was cancelled. `X-Comfy-Credits-Used` is present on a request that completed successfully once its cost is known, with the value the result collect carries.

One queued request's current state, composed with the same three URLs the submission returned.

​

cancel_url

string<uri>

requerido

Absolute URL a cancellation is asked for at.

Ejemplo:

`"https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21/cancel"`

​

response_url

string<uri>

requerido

Absolute URL this request's result is collected from.

Ejemplo:

`"https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21"`

​

status_url

string<uri>

requerido

Absolute URL of this request's status read.

Ejemplo:

`"https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21/status"`

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

The state of a queued Router request. It has exactly three values, and unlike `RouterErrorType` this one is a closed `enum`, because the two schemas are closed in opposite directions on purpose. `RouterErrorType` classifies failures and its set is expected to grow, so a generated client that hard-rejected an unrecognised bucket would fail hardest exactly when something had already gone wrong. This one is a lifecycle, and a lifecycle with a fourth state added later is a breaking change to every polling loop written against it whether it is declared as an enum or not - so it is declared as one, and the constraint is stated where a client can see it. THERE IS NO `FAILED` AND NO `CANCELLED`. A run that failed and a run the caller cancelled are both `COMPLETED`, carrying an `error_type`. `COMPLETED` means the request has reached a terminal state and will not change again; it does NOT mean it succeeded. A polling client's loop asks one question - "is it finished" - and gets one answer, instead of one per way a run can end; whether it succeeded is then a separate question answered by whether `error_type` is present.

Opciones disponibles: 

`IN_QUEUE`, 

`IN_PROGRESS`, 

`COMPLETED`

Ejemplo:

`"IN_QUEUE"`

​

error_type

string

Present only on a `COMPLETED` request that did not succeed, carrying the same coarse bucket the result read puts on `X-Comfy-Error-Type` when it returns that failure. It is what distinguishes a terminal request that succeeded from one that failed or was cancelled - there is no separate terminal status for either - and it is absent on success rather than null, so branch on its presence. It is the coarse bucket ALONE. The human-readable `detail`, and a model's per-field validation errors, are not restated here: the status read exists to be polled cheaply and repeatedly, and the result read returns the full error body once.

Ejemplo:

`"invalid_input"`

​

queue_position

integer

How many requests are ahead of this one in the queue, at the instant the response was composed. Zero means this request is at the front. IT IS A SNAPSHOT AND NOT A PROMISE. It can move in either direction: other callers submit, requests ahead complete or are cancelled, and capacity is not shared equally between models. Show it to a human as a rough progress signal; do not compute an ETA from it and do not branch a retry policy on it - `Retry-After` is the number that exists for that, and `status` is the one that says whether the request is still waiting at all. It is absent once the request is no longer `IN_QUEUE`, rather than being reported as zero: zero already means "at the front", so reusing it for "no longer queued" would make a running request indistinguishable from the next one to start.

Rango requerido: `x >= 0`

Ejemplo:

`3`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/comfy-router/read-the-queue-state-of-one-submitted-request.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/comfy-router/read-the-queue-state-of-one-submitted-request)

[Ask for one submitted request to be cancelled.](https://docs.comfy.org/es/registry/api-reference/comfy-router/ask-for-one-submitted-request-to-be-cancelled)

---
url: https://docs.comfy.org/es/registry/api-reference/comfy-router/collect-the-result-of-one-submitted-request/
title: Collect the result of one submitted request. - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:32.314955+00:00
---

# Collect the result of one submitted request. - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/comfy-router/collect-the-result-of-one-submitted-request/

Collect the result of one submitted request.

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id} \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}",
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
    
    	url := "https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

200

202

401

403

404

409

410

422

503

504

default
    
    
    "<string>"
    
    
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

Comfy Router

# Collect the result of one submitted request.

Copiar páginaCopiar página

The collect endpoint. On a request that has finished successfully it returns the partner model’s own native output, byte for byte what the synchronous route’s `200` carries for the same model and the same input - so the two delivery modes produce one result shape and a caller can move between them without a second parser. WHILE THE REQUEST IS STILL RUNNING this returns `202` carrying the SAME `RouterQueueStatusResponse` body the status read returns, with the same `Retry-After` hint. A client that only ever wants the result can therefore poll this one URL and branch on the status code, and never call the status read at all; a client that wants to watch progress without pulling the output down uses the status read. Both are supported deliberately, and they cannot disagree, because the `202` body IS the status body. A REQUEST THAT FINISHED WITH A FAILURE - a provider error, a policy refusal, a cancellation the caller asked for - is returned in Router’s request-level error envelope, `RouterErrorResponse`, under the status the synchronous route would have answered for that same failure, with the coarse bucket repeated on `X-Comfy-Error-Type`. That is the `default` response below. Collecting a failure is not itself an error in the read: the read worked, and what it found was a failed run. A client that wants the terminal state WITHOUT this branch reads the status endpoint, where the same run is `COMPLETED` with an `error_type` and no status code carries the failure. WITH ONE EXCEPTION, AND IT IS ABOUT THE CHARGE RATHER THAN ABOUT THE CANCELLATION. The rule this route applies is “a recorded charge and a stored result”, not “the cancel arrived late”: when a terminal request carries BOTH, this route answers `200` with that result whatever terminal reason the request carries, because the caller has already paid for it. A cancellation the caller was charged nothing for is answered by the error envelope exactly as above, whether it arrived before the partner call or while one was in flight - a cancellation is not itself billable, so a run cancelled before its charge was metered stays unbilled AND unreadable, which is the pairing that leaves the caller whole. The STATUS read is unchanged either way: the run is `COMPLETED` with `error_type: cancelled`, so a client that needs to know a result was cancelled-but-delivered reads it there. A RESULT DOES NOT LIVE FOREVER. Once its retention window has passed the read is `410`, permanently and for that id alone: the request really did exist and really did produce this answer, and saying so is materially different from `404`, which would tell a caller their id was never valid and send them to re-submit a generation they have already paid for. This operation is deliberately tagged `Comfy Router` and NOT `API Nodes`, for the reason given on the synchronous route.

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

Pruébalo

Collect the result of one submitted request.

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id} \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}",
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
    
    	url := "https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

200

202

401

403

404

409

410

422

503

504

default
    
    
    "<string>"
    
    
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

*/*

OK - the result stored for a request that produced one - a request that completed successfully, or a terminal one that carries both a recorded charge and a stored result - returned unchanged under the partner's own media type, exactly as the synchronous route's `200` returns it, and under the same provider-selection contract the submit accepted: without `model_provider`, or with `model_provider` and `strict_mode=false` (the default, translated back into this model's native contract when possible, falling back to the alternate provider's own raw response on a translation failure - logged, never silent), the shape is this model's own native output; with `strict_mode=true` it is the alternate provider's response returned unchanged. For most models that is JSON (`RouterModelOutput`); for a model whose partner answers a generation directly as bytes it is those bytes under the partner's own `Content-Type`. Today no such model can be queued (the submit refuses it), so this branch is declared for the SDK contract ahead of the server serving it. A client must branch on the response `Content-Type` and must not assume a JSON document; the per-model contract is published at `GET /v2/models/{provider}/{model}/openapi.json`. This response carries `X-Content-Type-Options: nosniff`, so a partner media type is taken at its word and never sniffed into something else.

The response is of type `file`.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/comfy-router/collect-the-result-of-one-submitted-request.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/comfy-router/collect-the-result-of-one-submitted-request)

[Submit a partner model run to the queue and return immediately.](https://docs.comfy.org/es/registry/api-reference/comfy-router/submit-a-partner-model-run-to-the-queue-and-return-immediately)[Ask for one submitted request to be cancelled.](https://docs.comfy.org/es/registry/api-reference/comfy-router/ask-for-one-submitted-request-to-be-cancelled)

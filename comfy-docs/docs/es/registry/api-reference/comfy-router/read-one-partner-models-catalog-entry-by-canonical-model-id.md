---
url: https://docs.comfy.org/es/registry/api-reference/comfy-router/read-one-partner-models-catalog-entry-by-canonical-model-id/
title: Read one partner model's catalog entry by canonical model ID. - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:32.503925+00:00
---

# Read one partner model's catalog entry by canonical model ID. - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/comfy-router/read-one-partner-models-catalog-entry-by-canonical-model-id/

Read one partner model's catalog entry by canonical model ID.

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/v2/models/{provider}/{model} \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.comfy.org/v2/models/{provider}/{model}"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
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
    
    	url := "https://api.comfy.org/v2/models/{provider}/{model}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/v2/models/{provider}/{model}")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/v2/models/{provider}/{model}")
    
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

503
    
    
    {
      "billing": {
        "charges_on_policy_rejection": "unknown"
      },
      "id": "bfl/flux-2-pro",
      "model": "flux-2-pro",
      "provider": "bfl",
      "schema_etag": "\"9f2c1e0b7a4d3c6e8f5a2b1d0c9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e\"",
      "input_schema_url": "<string>"
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

# Read one partner model's catalog entry by canonical model ID.

Copiar páginaCopiar página

Per-model detail for a single Comfy Router model, so a caller can check one model without walking the whole paginated catalog. The SDKs use it to look a model up immediately before invoking it. The path is the SAME canonical model ID that `post` above invokes, on the same path template: one string addresses both routes, so there is no second ID alphabet to keep in step. `provider` and `model` are governed by the same `RouterProvider` / `RouterModel` parameters, with the same alphabet. That template is TWO segments; a catalog `id` carrying a third `variant` segment addresses neither route, because how a variant is addressed over HTTP is not settled by this contract (see `RouterProvider` and `RouterModelListEntry.id`). The `200` body is a SUPERSET of the entry `GET /v2/models` returns for the same model: `RouterModelDetail` composes the list entry `RouterModelListEntry` by reference rather than restating its fields, so the listing and the detail cannot drift into two shapes for one model. An ID that resolves to no model returns `404` with `error_type: model_not_found` \- the same Router-owned body, the same bucket on `X-Comfy-Error-Type`, and the same fuzzy `detail` suggestions the invocation route returns for that ID. Both routes resolve through one catalog, so they cannot disagree about the same typo. Those suggestions are drawn from the models the CALLER is entitled to see: a miss on an unauthenticated or unentitled ID must not name models the caller could not otherwise enumerate. This is a requirement on the handler story (see `drip/codegen.yaml`), not something this contract can enforce. The read sits behind the SAME enablement gate as `post` above, consulted before the catalog is touched: a caller Comfy Router is not switched on for gets `403` with `error_type: not_enabled` and learns nothing about which models exist - not even through a `404`’s suggestions - and a gate that could not be evaluated answers `503` with `error_type: service_unavailable`. Both carry the Router-owned body and the bucket on `X-Comfy-Error-Type`, exactly as on `post`. The entry is cacheable by the caller. It carries a strong `ETag` over the entry bytes and honours `If-None-Match` with a `304`. This operation is deliberately tagged `Comfy Router` and NOT `API Nodes`, for the reason given on `post` above.

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

Pruébalo

Read one partner model's catalog entry by canonical model ID.

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/v2/models/{provider}/{model} \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.comfy.org/v2/models/{provider}/{model}"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
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
    
    	url := "https://api.comfy.org/v2/models/{provider}/{model}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/v2/models/{provider}/{model}")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/v2/models/{provider}/{model}")
    
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

503
    
    
    {
      "billing": {
        "charges_on_policy_rejection": "unknown"
      },
      "id": "bfl/flux-2-pro",
      "model": "flux-2-pro",
      "provider": "bfl",
      "schema_etag": "\"9f2c1e0b7a4d3c6e8f5a2b1d0c9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e\"",
      "input_schema_url": "<string>"
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

If-None-Match

string

The `ETag` a caller holds from an earlier `200`. When it matches the current entry (RFC 9110 weak comparison; `*` matches any current entry) the answer is a bodyless `304` carrying the same `ETag`, otherwise the full entry.

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

#### Respuesta

200

application/json

OK - the model's catalog entry.

Per-model detail for one Comfy Router model: everything the catalog listing reports for it, plus the per-model fields that only the single-model route carries. It is `allOf: [RouterModelListEntry, RouterModelDetailFields]` so that the shared half IS the list entry rather than a copy of it - see the section comment above. A generated client can therefore treat a detail response as a list entry everywhere a list entry is expected.

​

billing

object

requerido

Per-model billing facts a caller needs before invoking - not prices. Usage and cost figures never appear here. It is an object with one member rather than a flat sibling field because more pre-invocation billing facts are coming and a flat `billing_charges_*` family would have to be un-flattened later; a nested object absorbs them without a breaking rename. The member is `required` for the reason its own description gives - "we did not say" and "we do not charge" must not be the same wire state.

Show child attributes

​

id

string

requerido

A canonical Comfy Router model ID, `{provider}/{model}` \- exactly the value that addresses the model on `POST /v2/models/{provider}/{model}`, so a caller can interpolate it into that path without re-deriving it from anything. Its `pattern` is `RouterProviderSegment` and `RouterModelSegment` joined by a single `/`, and `maxLength` is their sum plus that separator. TestRouterCatalogIdsMatchInvocationRoute probes all three patterns behaviourally against one corpus, so loosening or tightening any of them alone fails CI rather than silently letting the catalog advertise an ID the invocation route would reject. The optional `variant` third segment is deliberately absent: how a variant is addressed is not settled by the invocation contract, so the catalog must not list an ID that route is not yet defined to accept. The PUBLIC lead paragraphs of `RouterProviderSegment`, `RouterModelSegment` and the `RouterProvider` / `RouterModel` path parameters therefore spell the canonical ID `{provider}/{model}` with no variant suffix, and must keep doing so while the variant form is unsettled: those leads are the only text the SDK projection publishes, so a three-segment form there vendors an ID shape every published `pattern` rejects and no path template accepts AS A MODEL ID. (`/v2/models/{provider}/{model}/openapi.json` does match a third segment, but only when it is that one literal - which is exactly the collision `getRouterModelInputSchema` reserves against, not an ID the route accepts.) The reservation is argued in the rationale paragraphs, which are never projected, and that is where it belongs. ONE bound does not survive the composition: `maxLength` here is the TOTAL, so a 193-character ID made of a 100-character provider and a 92-character model satisfies this schema while its provider segment exceeds `RouterProviderSegment`'s own 64. A single `pattern` cannot express a per-segment length bound - the structural alphabet and a character count are not jointly expressible without lookahead, which this repo's Go-side pattern probes cannot compile. The per-segment bounds are therefore carried by the sibling `provider` and `model` fields of `RouterModelListEntry`, which reference the bounded segment schemas directly, so no CONFORMING entry can carry such an `id`. TestRouterCatalogIdsMatchInvocationRoute pins that this residual is length-only: over-length segments are in its corpus, and any divergence that is not purely a per-segment length overrun fails.

Maximum string length: `193`

Pattern: `^[a-z0-9]+([._-][a-z0-9]+)*/[a-z0-9]+([._-][a-z0-9]+)*$`

Ejemplo:

`"bfl/flux-2-pro"`

​

model

string

requerido

Lowercase `model` segment of the canonical `{provider}/{model}` model ID - the model to run within that provider. Shared by the invocation route's `model` path parameter and a catalog entry's `model` field, for the same no-drift reason as `RouterProviderSegment`. As with the provider segment, the `pattern` documents the contract and does not enforce it. Dots are permitted inside the segment because partner model IDs use them for versions (`flux-pro-1.1`), but a repeated separator is not, so `..` cannot appear.

Maximum string length: `128`

Pattern: `^[a-z0-9]+([._-][a-z0-9]+)*$`

Ejemplo:

`"flux-2-pro"`

​

provider

string

requerido

Lowercase `provider` segment of the canonical `{provider}/{model}` model ID - the partner whose model is being addressed. The invocation route's `provider` path parameter and a catalog entry's `provider` field both reference this one schema, which is what keeps the listed IDs and the accepted IDs from drifting apart. The `pattern` is a CONTRACT statement, not enforcement: comfy-api installs no OpenAPI request validator and oapi-codegen binds path parameters as plain strings, so a handler must re-validate the segment itself before using it to select a provider or compose an upstream URL. The alphabet deliberately admits no `/`, no percent-encoding, and no repeated separator, so no accepted value can contain a `.` or `..` path segment.

Maximum string length: `64`

Pattern: `^[a-z0-9]+([._-][a-z0-9]+)*$`

Ejemplo:

`"bfl"`

​

schema_etag

string

The current strong `ETag` of this model's `GET /v2/models/{provider}/{model}/openapi.json` document. Send it as `If-None-Match` on that read to get a `304` while the schema is unchanged, or compare it with the value seen last time to learn which models' schemas changed without fetching every document. Absent whenever that read would not answer `200` for this caller at this moment: the schema service is not available, the model's document cannot be rendered, or the model stopped being available to this caller while the response was being built. An absent tag is not a schema change; re-read the model's document to learn its current tag.

Ejemplo:

`"\"9f2c1e0b7a4d3c6e8f5a2b1d0c9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e\""`

​

input_schema_url

string<uri>

Pointer to this model's input schema document - the description of the body `POST /v2/models/{provider}/{model}` accepts for this model. Only the pointer is part of this contract: the document it addresses is authored separately. Absent when no schema has been authored for the model. It is an ABSOLUTE `https` URI, deliberately not a `uri-reference`. Clients dereference or render this value, and a relative reference would resolve against the caller's own base while a `file:`, `data:` or `javascript:` scheme would be scheme confusion in every generated SDK. If this field is ever populated from partner- or admin-supplied metadata, that constraint is the only thing standing between that metadata and the client, so a server MUST NOT emit a value this pattern rejects.

Maximum string length: `2048`

Pattern: `^https://`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/comfy-router/read-one-partner-models-catalog-entry-by-canonical-model-id.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/comfy-router/read-one-partner-models-catalog-entry-by-canonical-model-id)

[List the models Comfy Router can run.](https://docs.comfy.org/es/registry/api-reference/comfy-router/list-the-models-comfy-router-can-run)[Run a partner model synchronously by canonical model ID.](https://docs.comfy.org/es/registry/api-reference/comfy-router/run-a-partner-model-synchronously-by-canonical-model-id)

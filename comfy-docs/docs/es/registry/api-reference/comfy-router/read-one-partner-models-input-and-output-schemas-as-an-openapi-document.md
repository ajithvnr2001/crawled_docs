---
url: https://docs.comfy.org/es/registry/api-reference/comfy-router/read-one-partner-models-input-and-output-schemas-as-an-openapi-document/
title: Read one partner model's input and output schemas as an OpenAPI document. - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-30T13:55:13.864508+00:00
---

# Read one partner model's input and output schemas as an OpenAPI document. - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/comfy-router/read-one-partner-models-input-and-output-schemas-as-an-openapi-document/

Read one partner model's input and output schemas as an OpenAPI document.

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/v2/models/{provider}/{model}/openapi.json \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.comfy.org/v2/models/{provider}/{model}/openapi.json"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.comfy.org/v2/models/{provider}/{model}/openapi.json', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/v2/models/{provider}/{model}/openapi.json",
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
    
    	url := "https://api.comfy.org/v2/models/{provider}/{model}/openapi.json"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/v2/models/{provider}/{model}/openapi.json")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/v2/models/{provider}/{model}/openapi.json")
    
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

500

503
    
    
    {}
    
    
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

# Read one partner model's input and output schemas as an OpenAPI document.

Copiar páginaCopiar página

The per-model input and output schemas for a single Comfy Router model, served as a standalone OpenAPI document, so a caller - an SDK, a codegen tool, or an agent - can discover a model’s arguments, and the shape of what it returns, without reading Comfy’s prose docs. It is the discovery mechanism the SDK quickstart depends on. The INPUT schema served is the SAME source the server validates a call against before the request reaches the provider. That is the property that makes it worth trusting: what Comfy publishes and what Comfy enforces are one document, not two copies that drift. Both read the schema through a single accessor (`routerschema.Source.InputSchema`), so they cannot diverge without deleting it. The path prefix is the SAME canonical `{provider}/{model}` model ID that `POST /v2/models/{provider}/{model}` invokes, with `/openapi.json` appended - a caller reads an ID out of the catalog, appends one literal segment, and gets that model’s schema. `provider` and `model` are governed by the same `RouterProvider` / `RouterModel` parameters, with the same alphabet. One constraint this puts on the still-unsettled `{variant}` segment: `openapi.json` is itself a legal value under the `RouterModel` alphabet, so whatever spelling addresses a variant must not make `/v2/models/{provider}/{model}/openapi.json` ambiguous with a variant literally named `openapi.json`. Reserving that one literal is the cheapest resolution, and it is noted here rather than resolved, because how the variant segment is addressed is not settled by this contract. BOTH halves are described: the request body under the operation’s `requestBody`, and the response body under its `200`. They do NOT promise the same thing, and the served document says which is which in its own `info.description`. The INPUT schema is ENFORCED - it is the schema the server validates against - so what is published and what is enforced cannot differ. The OUTPUT schema is DESCRIPTIVE: Router returns the provider’s native result document exactly as it arrived, and never validates, narrows or re-envelopes it, so the output schema describes what the provider sends rather than constraining it. Comfy owns no output shape of its own. A model whose OUTPUT Comfy has not described yet is served a permissive output alongside whatever its input half is, flagged `x-comfy-output-schema-authored: false`. The two authored flags are independent: an authored input with an undescribed output is the ordinary state, and a caller must read each flag rather than either one for both. A model whose schema has not been authored yet is served a MINIMAL PERMISSIVE document with `200`, NOT a `404`: the model exists, `GET /v2/models/{provider}/{model}` reports it and `POST` runs it, so 404 here would have two Router routes disagreeing about whether the same model exists. The permissive document says the true thing instead - this model takes a JSON object and Comfy has not yet narrowed which fields - and flags itself with `x-comfy-input-schema-authored: false` so a caller can tell “unconstrained” from “constrained to an open object”. A `404` on this route means only what it means everywhere else in Router: `model_not_found`, the ID names nothing. The response is cacheable. It carries a strong `ETag` over the document bytes and honours `If-None-Match` with a `304`, because an SDK re-fetches this document far more often than the document changes. This operation is deliberately tagged `Comfy Router` and NOT `API Nodes`, for the reason given on the invocation route.

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

openapi.json

Pruébalo

Read one partner model's input and output schemas as an OpenAPI document.

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/v2/models/{provider}/{model}/openapi.json \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.comfy.org/v2/models/{provider}/{model}/openapi.json"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.comfy.org/v2/models/{provider}/{model}/openapi.json', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/v2/models/{provider}/{model}/openapi.json",
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
    
    	url := "https://api.comfy.org/v2/models/{provider}/{model}/openapi.json"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/v2/models/{provider}/{model}/openapi.json")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/v2/models/{provider}/{model}/openapi.json")
    
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

500

503
    
    
    {}
    
    
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

#### Encabezados

​

If-None-Match

string

The `ETag` a caller holds from an earlier `200`. When it matches the current document (RFC 9110 weak comparison; `*` matches any current document) the answer is a bodyless `304` carrying the same `ETag`, otherwise the full document.

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

OK - the model's input and output schemas, as a standalone OpenAPI document.

A standalone OpenAPI document describing one Comfy Router model's input and output - the body `POST /v2/models/{provider}/{model}` accepts for that model, under the operation's `requestBody`, and the body it returns, under that operation's `200` content. It is what `GET /v2/models/{provider}/{model}/openapi.json` returns. The component keeps its historical name, which predates the output half; the shape it describes is the whole document, not the input alone. It is a full OpenAPI document rather than a bare JSON Schema because that is what the tools this endpoint exists for consume: an SDK generator takes an OpenAPI document. The document is STANDALONE: every schema component EITHER half references travels with it under its own `components.schemas` \- the two closures are unioned, because the document has only one components section - so nothing in it points at a section the caller does not have. A DESCRIBED output is keyed `application/json`, or with whatever media type its authored component declares through `x-comfy-router-output-media-type` (a media-type string, e.g. `video/mp4`) - so a generated client decodes the body the way the provider actually sends it rather than trying to JSON-parse a binary one. An output Comfy has NOT described yet is keyed `*/*`, not `application/json`. The two are different claims: an undescribed output is unknown in its media type as much as in its shape, and some Router models answer with binary bodies, so keying the permissive output as JSON would assert a contract Comfy has not established. Read `x-comfy-output-schema-authored` to tell the two apart. The shape is left open here on purpose. Its concrete contents are an OpenAPI document, and restating the OpenAPI meta-schema inside this spec would be a second copy of a specification Comfy does not own - the exact publish-versus-enforce drift this endpoint exists to prevent, one level up. It is a named component (never an inline anonymous object) because ComfyUI's spec-driven codegen needs a class to generate. Five Comfy extensions are carried at the document root and are part of this contract. `x-comfy-router-model-id` repeats the canonical model ID, so a document saved to disk still names the model it describes. `x-comfy-input-schema-authored` is a boolean reporting whether the embedded REQUEST schema was authored for this model (`true`) or is the permissive fallback served until one is (`false`); the two are indistinguishable from the schema alone, and a caller that cannot tell them apart would read "any JSON object" as a narrowed contract. `x-comfy-output-schema-authored` reports the same thing for the RESPONSE schema under the `200`. The two flags are INDEPENDENT and must be read separately: the halves are authored one at a time, so an authored input with an undescribed output is the ordinary state rather than an edge case. `x-comfy-router-input-modalities` and `x-comfy-router-output-modalities` are arrays naming the kinds of media the model consumes and emits, each element one of `text`, `image`, `video`, `audio` or `3d`. The INPUT array records what the model is DOCUMENTED TO ACCEPT, which is a narrower claim than what the request schema admits: request schemas are shared across sibling models (one `GeminiPart` serves every Gemini spelling), so the schema may admit media kinds this model ignores. The array, not the schema, is the capability signal; the schema is still exactly what the server validates against. The output array is ORDERED: its first element is the model's primary output and any later element a secondary one (a video model that returns a soundtrack is `["video","audio"]`). Both are always present and never empty on a document this server builds; an absent key means a server that predates them, not a model with no modality.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/comfy-router/read-one-partner-models-input-and-output-schemas-as-an-openapi-document.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/comfy-router/read-one-partner-models-input-and-output-schemas-as-an-openapi-document)

[Price a model call before running it, without running it.](https://docs.comfy.org/es/registry/api-reference/comfy-router/price-a-model-call-before-running-it-without-running-it)[Submit a partner model run to the queue and return immediately.](https://docs.comfy.org/es/registry/api-reference/comfy-router/submit-a-partner-model-run-to-the-queue-and-return-immediately)

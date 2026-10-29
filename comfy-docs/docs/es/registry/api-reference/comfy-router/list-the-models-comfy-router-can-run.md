---
url: https://docs.comfy.org/es/registry/api-reference/comfy-router/list-the-models-comfy-router-can-run/
title: List the models Comfy Router can run. - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-29T14:00:20.774696+00:00
---

# List the models Comfy Router can run. - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/comfy-router/list-the-models-comfy-router-can-run/

List the models Comfy Router can run.

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/v2/models \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.comfy.org/v2/models"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.comfy.org/v2/models', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/v2/models",
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
    
    	url := "https://api.comfy.org/v2/models"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/v2/models")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/v2/models")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

200

400

401

403

503
    
    
    {
      "data": [
        {
          "billing": {
            "charges_on_policy_rejection": "unknown"
          },
          "id": "bfl/flux-2-pro",
          "model": "flux-2-pro",
          "provider": "bfl",
          "schema_etag": "\"9f2c1e0b7a4d3c6e8f5a2b1d0c9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e\""
        }
      ],
      "has_more": true,
      "limit": 20,
      "next_cursor": "q7Fm2xTn9pLd4RsV"
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

# List the models Comfy Router can run.

Copiar páginaCopiar página

Comfy Router’s model catalog - one page of the canonical model IDs that `POST /v2/models/{provider}/{model}` accepts. An SDK calls this on cold start to discover what is runnable, and the `model_not_found` suggestions come from the same catalog, so an ID listed here that then 404s on invocation would be worse than either failure alone. That agreement is structural rather than a promise: an entry’s `provider` and `model` are the two path segments of the invocation route and reference the same schema components that route’s path parameters do, and `id` is those two segments joined by `/`. Pagination is CURSOR-based, deliberately not offset-based. The catalog is a moving list - models are added, and embargoed, between calls - and an offset walk silently skips or repeats entries when the list changes underneath it. Pass a page’s `next_cursor` back as `cursor` to fetch the next page, and stop when `has_more` is false rather than when a page comes back short. A cursor is opaque: it is not an offset, not a model ID, and not stable across catalog rebuilds, so a cursor that is malformed or no longer valid is answered with a `400` from the Router error contract (`error_type: invalid_input`), never a `500`. A model that is deployed but NOT yet released is EXCLUDED from every page. This is a requirement of this route specifically, not something it inherits: `PartnerModelEmbargoMiddleware` gates `/proxy/*` only, and only methods that can carry a body, so a bodyless `GET` outside `/proxy/` is outside the embargo gate on both axes. Confirming that a specific unreleased model exists is precisely the disclosure `modelembargo` was built to prevent, and a catalog is the most direct way to make that confirmation - so the handler must filter the embargo set out of the page itself. An excluded model is simply absent: the catalog does not mark it, does not reserve a slot for it, and `has_more`/`limit` describe the page AFTER exclusion, so the omission is not inferable from a short page either. Per-model detail and the per-model input/output schemas are separate routes; this one carries only the identity of each model. A page is cacheable by the caller. It carries a strong `ETag` over the page bytes and honours `If-None-Match` with a `304`, so a client that re-reads the catalog pays for a page only when it changed.

Copiar páginaCopiar página

GET

/

v2

/

models

Pruébalo

List the models Comfy Router can run.

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/v2/models \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.comfy.org/v2/models"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.comfy.org/v2/models', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/v2/models",
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
    
    	url := "https://api.comfy.org/v2/models"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/v2/models")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/v2/models")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

200

400

401

403

503
    
    
    {
      "data": [
        {
          "billing": {
            "charges_on_policy_rejection": "unknown"
          },
          "id": "bfl/flux-2-pro",
          "model": "flux-2-pro",
          "provider": "bfl",
          "schema_etag": "\"9f2c1e0b7a4d3c6e8f5a2b1d0c9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e\""
        }
      ],
      "has_more": true,
      "limit": 20,
      "next_cursor": "q7Fm2xTn9pLd4RsV"
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

The `ETag` a caller holds from an earlier `200`. When it matches the current page (RFC 9110 weak comparison; `*` matches any current page) the answer is a bodyless `304` carrying the same `ETag`, otherwise the full page.

#### Parámetros de consulta

​

cursor

string

Opaque pagination cursor. Pass a previous page's `next_cursor` to fetch the next page; omit it for the first page. See `RouterPageCursor` for why the value is opaque and why this route paginates by cursor rather than by offset. A cursor that is malformed, over-long, or no longer valid is answered with a `400` carrying the Router error contract's `RouterErrorResponse` (`error_type: invalid_input`) - never a `500`, and never a silent fallback to the first page, which would make a walk loop forever. An opaque cursor into a Router list. It is produced by the server and only ever round-tripped: it is not an offset, not a model ID, not ordered, and not stable across catalog rebuilds, so parsing one, incrementing one, or persisting one beyond the walk it came from are all outside the contract. Cursor rather than offset because the catalog is a moving list - an offset walk silently skips or repeats entries when entries are added or removed mid-walk, and a caller cannot tell that it happened. `maxLength` bounds it because the value arrives in a query string and is fed to a decoder; a cursor that is malformed, truncated, over-long or no longer valid is a `400` from the Router error contract, never a `500`. `minLength: 1` is load-bearing rather than tidy: Echo's `QueryParam` returns `""` for both `?cursor=` and an omitted `cursor`, so without it the empty string is a schema-valid cursor indistinguishable from no cursor at all, and a handler would silently restart the walk at page one - the infinite loop `RouterCatalogCursor` explicitly forbids. An empty `cursor` is therefore a `400`, not page one. The `pattern` fixes the alphabet at URL- and base64-safe characters so a control character, a CR/LF, or a space can never ride a query string into the decoder or into a `400`'s free-text `detail`. It constrains the SERVER, which is the only party that mints these; as with the model-ID segments it is a CONTRACT statement and not enforcement, since comfy-api installs no OpenAPI request validator - a handler must still validate the value it was handed before decoding it.

Required string length: `1 - 512`

Pattern: `^[A-Za-z0-9._~+/=-]+$`

Ejemplo:

`"q7Fm2xTn9pLd4RsV"`

​

limit

integer

predeterminado:20

Number of models to return in one page. Values above the declared maximum are outside the contract, but this route does not reject them: it serves the maximum instead, and the page size actually served is echoed back as `limit` on the response, so a clamp is always detectable by the caller. Treat the maximum as the real page stride - a client that asks for more and assumes it received more will miss rows. 0 and negative values are also accepted and select the default, which is why no `minimum` is declared: sub-1 is meaningful here, not invalid. The cap of 100 is the one the node-listing endpoints already use (BE-8098): an uncapped page size on a list route is a trivially exploitable amplification, and this route is hit by SDKs on cold start.

Rango requerido: `x <= 100`

#### Respuesta

200

application/json

OK - one page of the model catalog.

One page of the Router model catalog. `has_more` is the ONLY correct stop condition for a walk: a short page is not one, because a page can be trimmed by an entry that disappeared between the cursor being minted and the page being served. `next_cursor` is present exactly when `has_more` is true, and omitted otherwise. `limit` echoes the page size actually served, which is what makes a clamped request detectable.

​

data

object[]

requerido

The models on this page, at most `limit` of them.

Show child attributes

​

has_more

boolean

requerido

Whether another page exists beyond this one. Keep walking while this is true; do not infer the end of the catalog from a short or empty `data`.

​

limit

integer

requerido

The page size actually served. A requested `limit` above the maximum is clamped down to the maximum rather than rejected, so this can be smaller than the value asked for - paginate with this number, not with the one you sent, or you will assume rows you never received. Unlike the REQUEST parameter, this one declares a `minimum`: sub-1 is meaningful on the way in (it selects the default) but a page size actually served is always positive, and `0` is exactly what an unset Go field serializes to - so without the bound a handler that forgets to populate this still emits a conforming response, and `limit: 0` beside `has_more: true` describes a walk that cannot advance.

Rango requerido: `1 <= x <= 100`

Ejemplo:

`20`

​

next_cursor

string

An opaque cursor into a Router list. It is produced by the server and only ever round-tripped: it is not an offset, not a model ID, not ordered, and not stable across catalog rebuilds, so parsing one, incrementing one, or persisting one beyond the walk it came from are all outside the contract. Cursor rather than offset because the catalog is a moving list - an offset walk silently skips or repeats entries when entries are added or removed mid-walk, and a caller cannot tell that it happened. `maxLength` bounds it because the value arrives in a query string and is fed to a decoder; a cursor that is malformed, truncated, over-long or no longer valid is a `400` from the Router error contract, never a `500`. `minLength: 1` is load-bearing rather than tidy: Echo's `QueryParam` returns `""` for both `?cursor=` and an omitted `cursor`, so without it the empty string is a schema-valid cursor indistinguishable from no cursor at all, and a handler would silently restart the walk at page one - the infinite loop `RouterCatalogCursor` explicitly forbids. An empty `cursor` is therefore a `400`, not page one. The `pattern` fixes the alphabet at URL- and base64-safe characters so a control character, a CR/LF, or a space can never ride a query string into the decoder or into a `400`'s free-text `detail`. It constrains the SERVER, which is the only party that mints these; as with the model-ID segments it is a CONTRACT statement and not enforcement, since comfy-api installs no OpenAPI request validator - a handler must still validate the value it was handed before decoding it.

Required string length: `1 - 512`

Pattern: `^[A-Za-z0-9._~+/=-]+$`

Ejemplo:

`"q7Fm2xTn9pLd4RsV"`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/comfy-router/list-the-models-comfy-router-can-run.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/comfy-router/list-the-models-comfy-router-can-run)

[Get release notes](https://docs.comfy.org/es/registry/api-reference/releases/get-release-notes)[Read one partner model's catalog entry by canonical model ID.](https://docs.comfy.org/es/registry/api-reference/comfy-router/read-one-partner-models-catalog-entry-by-canonical-model-id)

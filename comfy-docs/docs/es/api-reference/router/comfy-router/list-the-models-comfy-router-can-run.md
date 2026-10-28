---
url: https://docs.comfy.org/es/api-reference/router/comfy-router/list-the-models-comfy-router-can-run/
title: List the models Comfy Router can run. - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-28T13:54:38.588506+00:00
---

# List the models Comfy Router can run. - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/router/comfy-router/list-the-models-comfy-router-can-run/

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
          "id": "bfl/flux-2-pro",
          "provider": "bfl",
          "model": "flux-2-pro",
          "billing": {
            "charges_on_policy_rejection": "unknown"
          },
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
      "upstream_detail": "<string>",
      "refusal_subject": "<string>",
      "denied_reason": "<string>",
      "billed_workspace": {
        "type": "<string>",
        "id": "<string>",
        "rail": "<string>"
      },
      "credential_kind": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>",
      "denied_reason": "<string>",
      "billed_workspace": {
        "type": "<string>",
        "id": "<string>",
        "rail": "<string>"
      },
      "credential_kind": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>",
      "denied_reason": "<string>",
      "billed_workspace": {
        "type": "<string>",
        "id": "<string>",
        "rail": "<string>"
      },
      "credential_kind": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>",
      "denied_reason": "<string>",
      "billed_workspace": {
        "type": "<string>",
        "id": "<string>",
        "rail": "<string>"
      },
      "credential_kind": "<string>"
    }

Comfy Router

# List the models Comfy Router can run.

Copiar páginaCopiar página

Comfy Router’s model catalog - one page of the canonical model IDs that `POST /v2/models/{provider}/{model}` accepts. An SDK calls this on cold start to discover what is runnable, and the `model_not_found` suggestions come from the same catalog, so an ID listed here that then 404s on invocation would be worse than either failure alone. That agreement is structural rather than a promise: an entry’s `provider` and `model` are the two path segments of the invocation route and reference the same schema components that route’s path parameters do, and `id` is those two segments joined by `/`.

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
          "id": "bfl/flux-2-pro",
          "provider": "bfl",
          "model": "flux-2-pro",
          "billing": {
            "charges_on_policy_rejection": "unknown"
          },
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
      "upstream_detail": "<string>",
      "refusal_subject": "<string>",
      "denied_reason": "<string>",
      "billed_workspace": {
        "type": "<string>",
        "id": "<string>",
        "rail": "<string>"
      },
      "credential_kind": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>",
      "denied_reason": "<string>",
      "billed_workspace": {
        "type": "<string>",
        "id": "<string>",
        "rail": "<string>"
      },
      "credential_kind": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>",
      "denied_reason": "<string>",
      "billed_workspace": {
        "type": "<string>",
        "id": "<string>",
        "rail": "<string>"
      },
      "credential_kind": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>",
      "denied_reason": "<string>",
      "billed_workspace": {
        "type": "<string>",
        "id": "<string>",
        "rail": "<string>"
      },
      "credential_kind": "<string>"
    }

#### Autorizaciones

BearerAuthApiKeyAuthBearerAuthApiKeyAuth

​

Authorization

string

header

requerido

Bearer token authentication. Normally a Firebase or Cloud JWT. A 'comfyui-' prefixed API key is also accepted in this header: the prefix classifies the value as an API key and it is validated exactly as if it had been sent in X-API-Key.

#### Encabezados

​

If-None-Match

string

The `ETag` a caller holds from an earlier `200`. When it matches the current page (RFC 9110 weak comparison; `*` matches any current page) the answer is a bodyless `304` carrying the same `ETag`, otherwise the full page.

#### Parámetros de consulta

​

cursor

string

Opaque pagination cursor. Pass a previous page's `next_cursor` to fetch the next page; omit it for the first page. See `RouterPageCursor` for why the value is opaque and why this route paginates by cursor rather than by offset. An opaque cursor into a Router list. It is produced by the server and only ever round-tripped: it is not an offset, not a model ID, not ordered, and not stable across catalog rebuilds, so parsing one, incrementing one, or persisting one beyond the walk it came from are all outside the contract. Cursor rather than offset because the catalog is a moving list - an offset walk silently skips or repeats entries when entries are added or removed mid-walk, and a caller cannot tell that it happened.

Required string length: `1 - 512`

Pattern: `^[A-Za-z0-9._~+/=-]+$`

Ejemplo:

`"q7Fm2xTn9pLd4RsV"`

​

limit

integer

predeterminado:20

Number of models to return in one page. Values above the declared maximum are outside the contract, but this route does not reject them: it serves the maximum instead, and the page size actually served is echoed back as `limit` on the response, so a clamp is always detectable by the caller. Treat the maximum as the real page stride - a client that asks for more and assumes it received more will miss rows. 0 and negative values are also accepted and select the default, which is why no `minimum` is declared: sub-1 is meaningful here, not invalid.

Rango requerido: `x <= 100`

#### Respuesta

200

application/json

OK - one page of the model catalog.

One page of the Router model catalog.

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

The page size actually served. A requested `limit` above the maximum is clamped down to the maximum rather than rejected, so this can be smaller than the value asked for - paginate with this number, not with the one you sent, or you will assume rows you never received.

Rango requerido: `1 <= x <= 100`

Ejemplo:

`20`

​

next_cursor

string

An opaque cursor into a Router list. It is produced by the server and only ever round-tripped: it is not an offset, not a model ID, not ordered, and not stable across catalog rebuilds, so parsing one, incrementing one, or persisting one beyond the walk it came from are all outside the contract. Cursor rather than offset because the catalog is a moving list - an offset walk silently skips or repeats entries when entries are added or removed mid-walk, and a caller cannot tell that it happened.

Required string length: `1 - 512`

Pattern: `^[A-Za-z0-9._~+/=-]+$`

Ejemplo:

`"q7Fm2xTn9pLd4RsV"`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/router/comfy-router/list-the-models-comfy-router-can-run.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/router/comfy-router/list-the-models-comfy-router-can-run)

[Capacidades y límites](https://docs.comfy.org/es/development/comfy-router/limitations)[Read one partner model's catalog entry by canonical model ID.](https://docs.comfy.org/es/api-reference/router/comfy-router/read-one-partner-models-catalog-entry-by-canonical-model-id)

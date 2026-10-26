---
url: https://docs.comfy.org/es/api-reference/router/comfy-router/read-one-partner-models-input-and-output-schemas-as-an-openapi-document/
title: Read one partner model's input and output schemas as an OpenAPI document. - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:27.111177+00:00
---

# Read one partner model's input and output schemas as an OpenAPI document. - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/router/comfy-router/read-one-partner-models-input-and-output-schemas-as-an-openapi-document/

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

Comfy Router

# Read one partner model's input and output schemas as an OpenAPI document.

Copiar páginaCopiar página

The per-model input and output schemas for a single Comfy Router model, served as a standalone OpenAPI document, so a caller - an SDK, a codegen tool, or an agent - can discover a model’s arguments, and the shape of what it returns, without reading Comfy’s prose docs. It is the discovery mechanism the SDK quickstart depends on.

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

The `ETag` a caller holds from an earlier `200`. When it matches the current document (RFC 9110 weak comparison; `*` matches any current document) the answer is a bodyless `304` carrying the same `ETag`, otherwise the full document.

#### Parámetros de ruta

​

provider

string

requerido

Lowercase provider segment of the canonical `{provider}/{model}` model ID - the partner whose model is being run. Lowercase `provider` segment of the canonical `{provider}/{model}` model ID - the partner whose model is being addressed. The invocation route's `provider` path parameter and a catalog entry's `provider` field both reference this one schema, which is what keeps the listed IDs and the accepted IDs from drifting apart.

Maximum string length: `64`

Pattern: `^[a-z0-9]+([._-][a-z0-9]+)*$`

Ejemplo:

`"bfl"`

​

model

string

requerido

Lowercase model segment of the canonical `{provider}/{model}` model ID - the model to run within that provider. Lowercase `model` segment of the canonical `{provider}/{model}` model ID - the model to run within that provider. Shared by the invocation route's `model` path parameter and a catalog entry's `model` field, for the same no-drift reason as `RouterProviderSegment`.

Maximum string length: `128`

Pattern: `^[a-z0-9]+([._-][a-z0-9]+)*$`

Ejemplo:

`"flux-2-pro"`

#### Respuesta

200

application/json

OK - the model's input and output schemas, as a standalone OpenAPI document.

A standalone OpenAPI document describing one Comfy Router model's input and output - the body `POST /v2/models/{provider}/{model}` accepts for that model, under the operation's `requestBody`, and the body it returns, under that operation's `200` content. It is what `GET /v2/models/{provider}/{model}/openapi.json` returns. The component keeps its historical name, which predates the output half; the shape it describes is the whole document, not the input alone.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/router/comfy-router/read-one-partner-models-input-and-output-schemas-as-an-openapi-document.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/router/comfy-router/read-one-partner-models-input-and-output-schemas-as-an-openapi-document)

[Price a model call before running it, without running it.](https://docs.comfy.org/es/api-reference/router/comfy-router/price-a-model-call-before-running-it-without-running-it)[Submit a partner model run to the queue and return immediately.](https://docs.comfy.org/es/api-reference/router/comfy-router/submit-a-partner-model-run-to-the-queue-and-return-immediately)

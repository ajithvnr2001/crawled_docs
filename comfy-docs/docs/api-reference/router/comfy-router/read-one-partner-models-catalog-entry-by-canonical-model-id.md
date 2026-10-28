---
url: https://docs.comfy.org/api-reference/router/comfy-router/read-one-partner-models-catalog-entry-by-canonical-model-id/
title: Read one partner model's catalog entry by canonical model ID. - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-28T13:54:38.376391+00:00
---

# Read one partner model's catalog entry by canonical model ID. - ComfyUI

> Source: https://docs.comfy.org/api-reference/router/comfy-router/read-one-partner-models-catalog-entry-by-canonical-model-id/

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
      "id": "bfl/flux-2-pro",
      "provider": "bfl",
      "model": "flux-2-pro",
      "billing": {
        "charges_on_policy_rejection": "unknown"
      },
      "schema_etag": "\"9f2c1e0b7a4d3c6e8f5a2b1d0c9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e\"",
      "input_schema_url": "<string>"
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

# Read one partner model's catalog entry by canonical model ID.

Copy pageCopy page

Per-model detail for a single Comfy Router model, so a caller can check one model without walking the whole paginated catalog. The SDKs use it to look a model up immediately before invoking it.

Copy pageCopy page

GET

/

v2

/

models

/

{provider}

/

{model}

Try it

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
      "id": "bfl/flux-2-pro",
      "provider": "bfl",
      "model": "flux-2-pro",
      "billing": {
        "charges_on_policy_rejection": "unknown"
      },
      "schema_etag": "\"9f2c1e0b7a4d3c6e8f5a2b1d0c9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e\"",
      "input_schema_url": "<string>"
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

If-None-Match

string

The `ETag` a caller holds from an earlier `200`. When it matches the current entry (RFC 9110 weak comparison; `*` matches any current entry) the answer is a bodyless `304` carrying the same `ETag`, otherwise the full entry.

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

#### Response

200

application/json

OK - the model's catalog entry.

Per-model detail for one Comfy Router model: everything the catalog listing reports for it, plus the per-model fields that only the single-model route carries.

​

id

string

required

A canonical Comfy Router model ID, `{provider}/{model}` \- exactly the value that addresses the model on `POST /v2/models/{provider}/{model}`, so a caller can interpolate it into that path without re-deriving it from anything. Its `pattern` is `RouterProviderSegment` and `RouterModelSegment` joined by a single `/`, and `maxLength` is their sum plus that separator.

Maximum string length: `193`

Pattern: `^[a-z0-9]+([._-][a-z0-9]+)*/[a-z0-9]+([._-][a-z0-9]+)*$`

Example:

`"bfl/flux-2-pro"`

​

provider

string

required

Lowercase `provider` segment of the canonical `{provider}/{model}` model ID - the partner whose model is being addressed. The invocation route's `provider` path parameter and a catalog entry's `provider` field both reference this one schema, which is what keeps the listed IDs and the accepted IDs from drifting apart.

Maximum string length: `64`

Pattern: `^[a-z0-9]+([._-][a-z0-9]+)*$`

Example:

`"bfl"`

​

model

string

required

Lowercase `model` segment of the canonical `{provider}/{model}` model ID - the model to run within that provider. Shared by the invocation route's `model` path parameter and a catalog entry's `model` field, for the same no-drift reason as `RouterProviderSegment`.

Maximum string length: `128`

Pattern: `^[a-z0-9]+([._-][a-z0-9]+)*$`

Example:

`"flux-2-pro"`

​

billing

object

required

Per-model billing facts a caller needs before invoking - not prices. Usage and cost figures never appear here.

Show child attributes

​

schema_etag

string

The current strong `ETag` of this model's `GET /v2/models/{provider}/{model}/openapi.json` document. Send it as `If-None-Match` on that read to get a `304` while the schema is unchanged, or compare it with the value seen last time to learn which models' schemas changed without fetching every document. Absent whenever that read would not answer `200` for this caller at this moment: the schema service is not available, the model's document cannot be rendered, or the model stopped being available to this caller while the response was being built. An absent tag is not a schema change; re-read the model's document to learn its current tag.

Example:

`"\"9f2c1e0b7a4d3c6e8f5a2b1d0c9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e\""`

​

input_schema_url

string<uri>

Pointer to this model's input schema document - the description of the body `POST /v2/models/{provider}/{model}` accepts for this model. Only the pointer is part of this contract: the document it addresses is authored separately. Absent when no schema has been authored for the model.

Maximum string length: `2048`

Pattern: `^https://`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/api-reference/router/comfy-router/read-one-partner-models-catalog-entry-by-canonical-model-id.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/router/comfy-router/read-one-partner-models-catalog-entry-by-canonical-model-id)

[List the models Comfy Router can run.](https://docs.comfy.org/api-reference/router/comfy-router/list-the-models-comfy-router-can-run)[Run a partner model synchronously by canonical model ID.](https://docs.comfy.org/api-reference/router/comfy-router/run-a-partner-model-synchronously-by-canonical-model-id)

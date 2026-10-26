---
url: https://docs.comfy.org/es/api-reference/cloud/asset/get-asset-details/
title: Get asset details - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:23.069595+00:00
---

# Get asset details - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/asset/get-asset-details/

Get asset details

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/assets/{id} \
      --header 'X-API-Key: <api-key>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/assets/{id}"
    
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {'X-API-Key': '<api-key>'}};
    
    fetch('https://cloud.comfy.org/api/assets/{id}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/assets/{id}",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "GET",
      CURLOPT_HTTPHEADER => [
        "X-API-Key: <api-key>"
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
    
    	url := "https://cloud.comfy.org/api/assets/{id}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/assets/{id}")
      .header("X-API-Key", "<api-key>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/assets/{id}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["X-API-Key"] = '<api-key>'
    
    response = http.request(request)
    puts response.read_body

200

401

404

500
    
    
    {
      "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "name": "<string>",
      "size": 123,
      "created_at": "2023-11-07T05:31:56Z",
      "updated_at": "2023-11-07T05:31:56Z",
      "asset_hash": "<string>",
      "mime_type": "<string>",
      "tags": [
        "<string>"
      ],
      "user_metadata": {},
      "preview_url": "<string>",
      "preview_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "prompt_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "last_access_time": "2023-11-07T05:31:56Z",
      "is_immutable": true
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }

asset

# Get asset details

Copiar páginaCopiar página

Retrieves detailed information about a specific asset

Copiar páginaCopiar página

GET

/

api

/

assets

/

{id}

Pruébalo

Get asset details

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/assets/{id} \
      --header 'X-API-Key: <api-key>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/assets/{id}"
    
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {'X-API-Key': '<api-key>'}};
    
    fetch('https://cloud.comfy.org/api/assets/{id}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/assets/{id}",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "GET",
      CURLOPT_HTTPHEADER => [
        "X-API-Key: <api-key>"
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
    
    	url := "https://cloud.comfy.org/api/assets/{id}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/assets/{id}")
      .header("X-API-Key", "<api-key>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/assets/{id}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["X-API-Key"] = '<api-key>'
    
    response = http.request(request)
    puts response.read_body

200

401

404

500
    
    
    {
      "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "name": "<string>",
      "size": 123,
      "created_at": "2023-11-07T05:31:56Z",
      "updated_at": "2023-11-07T05:31:56Z",
      "asset_hash": "<string>",
      "mime_type": "<string>",
      "tags": [
        "<string>"
      ],
      "user_metadata": {},
      "preview_url": "<string>",
      "preview_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "prompt_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "last_access_time": "2023-11-07T05:31:56Z",
      "is_immutable": true
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }

#### Autorizaciones

​

X-API-Key

string

header

requerido

API key authentication. Generate an API key from your account settings at <https://platform.comfy.org/profile/api-keys>. Pass the key in the X-API-Key header.

#### Parámetros de ruta

​

id

string<uuid>

requerido

Asset ID

#### Respuesta

200

application/json

Asset details retrieved successfully

​

id

string<uuid>

requerido

Unique identifier for the asset

​

name

string

requerido

Name of the asset file

​

size

integer<int64>

requerido

Size of the asset in bytes

​

created_at

string<date-time>

requerido

Timestamp when the asset was created

​

updated_at

string<date-time>

requerido

Timestamp when the asset was last updated

​

asset_hash

string

Blake3 hash of the asset content

Pattern: `^blake3:[a-f0-9]{64}$`

​

mime_type

string

MIME type of the asset

​

tags

string[]

Tags associated with the asset

​

user_metadata

object

Custom user metadata for the asset

​

preview_url

string<uri>

URL for asset preview/thumbnail

​

preview_id

string<uuid> | null

ID of the preview asset if available

​

prompt_id

string<uuid> | null

ID of the job/prompt that created this asset, if available

​

last_access_time

string<date-time>

Timestamp when the asset was last accessed

​

is_immutable

boolean

Whether this asset is immutable (cannot be modified or deleted)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/asset/get-asset-details.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/asset/get-asset-details)

[Initiate background download for large files](https://docs.comfy.org/es/api-reference/cloud/asset/initiate-background-download-for-large-files)[Update asset metadata](https://docs.comfy.org/es/api-reference/cloud/asset/update-asset-metadata)

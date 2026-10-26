---
url: https://docs.comfy.org/es/api-reference/cloud/asset/get-asset-metadata-from-remote-url/
title: Get asset metadata from remote URL - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:23.176762+00:00
---

# Get asset metadata from remote URL - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/asset/get-asset-metadata-from-remote-url/

Get asset metadata from remote URL

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/assets/remote-metadata \
      --header 'X-API-Key: <api-key>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/assets/remote-metadata"
    
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {'X-API-Key': '<api-key>'}};
    
    fetch('https://cloud.comfy.org/api/assets/remote-metadata', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/assets/remote-metadata",
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
    
    	url := "https://cloud.comfy.org/api/assets/remote-metadata"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/assets/remote-metadata")
      .header("X-API-Key", "<api-key>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/assets/remote-metadata")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["X-API-Key"] = '<api-key>'
    
    response = http.request(request)
    puts response.read_body

200

400

401

422

500
    
    
    {
      "content_length": 4294967296,
      "content_type": "application/octet-stream",
      "filename": "realistic-vision-v5.safetensors",
      "name": "Realistic Vision v5.0",
      "tags": [
        "models",
        "checkpoint"
      ],
      "preview_image": "data:image/jpeg;base64,/9j/4AAQSkZJRg...",
      "validation": {
        "is_valid": true,
        "errors": [
          {
            "code": "FORMAT_NOT_ALLOWED",
            "message": "File format \"PickleTensor\" is not allowed. Allowed formats: [SafeTensor]",
            "field": "format"
          }
        ],
        "warnings": [
          {
            "code": "FORMAT_NOT_ALLOWED",
            "message": "File format \"PickleTensor\" is not allowed. Allowed formats: [SafeTensor]",
            "field": "format"
          }
        ]
      }
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
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }

asset

# Get asset metadata from remote URL

Copiar páginaCopiar página

Retrieves metadata for an asset from a remote download URL without downloading the entire file. Supports various sources including CivitAI and other model repositories. Uses HEAD requests or API calls to fetch metadata efficiently. This endpoint is for previewing metadata before downloading, not for getting metadata of existing assets.

Copiar páginaCopiar página

GET

/

api

/

assets

/

remote-metadata

Pruébalo

Get asset metadata from remote URL

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/assets/remote-metadata \
      --header 'X-API-Key: <api-key>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/assets/remote-metadata"
    
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {'X-API-Key': '<api-key>'}};
    
    fetch('https://cloud.comfy.org/api/assets/remote-metadata', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/assets/remote-metadata",
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
    
    	url := "https://cloud.comfy.org/api/assets/remote-metadata"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/assets/remote-metadata")
      .header("X-API-Key", "<api-key>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/assets/remote-metadata")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["X-API-Key"] = '<api-key>'
    
    response = http.request(request)
    puts response.read_body

200

400

401

422

500
    
    
    {
      "content_length": 4294967296,
      "content_type": "application/octet-stream",
      "filename": "realistic-vision-v5.safetensors",
      "name": "Realistic Vision v5.0",
      "tags": [
        "models",
        "checkpoint"
      ],
      "preview_image": "data:image/jpeg;base64,/9j/4AAQSkZJRg...",
      "validation": {
        "is_valid": true,
        "errors": [
          {
            "code": "FORMAT_NOT_ALLOWED",
            "message": "File format \"PickleTensor\" is not allowed. Allowed formats: [SafeTensor]",
            "field": "format"
          }
        ],
        "warnings": [
          {
            "code": "FORMAT_NOT_ALLOWED",
            "message": "File format \"PickleTensor\" is not allowed. Allowed formats: [SafeTensor]",
            "field": "format"
          }
        ]
      }
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

#### Parámetros de consulta

​

url

string<uri>

requerido

Download URL to retrieve metadata from

Ejemplo:

`"https://civitai.com/api/download/models/123456"`

#### Respuesta

200

application/json

Metadata retrieved successfully

​

content_length

integer<int64>

requerido

Size of the asset in bytes (-1 if unknown)

Ejemplo:

`4294967296`

​

content_type

string

MIME type of the asset

Ejemplo:

`"application/octet-stream"`

​

filename

string

Suggested filename for the asset from source

Ejemplo:

`"realistic-vision-v5.safetensors"`

​

name

string

Display name or title for the asset from source

Ejemplo:

`"Realistic Vision v5.0"`

​

tags

string[]

Tags for categorization from source

Ejemplo:
    
    
    ["models", "checkpoint"]

​

preview_image

string

Preview image as base64-encoded data URL

Ejemplo:

`"data:image/jpeg;base64,/9j/4AAQSkZJRg..."`

​

validation

object

Validation results for the file

Show child attributes

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/asset/get-asset-metadata-from-remote-url.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/asset/get-asset-metadata-from-remote-url)

[Create asset reference from existing hash](https://docs.comfy.org/es/api-reference/cloud/asset/create-asset-reference-from-existing-hash)[Initiate background download for large files](https://docs.comfy.org/es/api-reference/cloud/asset/initiate-background-download-for-large-files)

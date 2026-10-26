---
url: https://docs.comfy.org/es/api-reference/cloud/asset/list-user-assets/
title: List user assets - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:23.713067+00:00
---

# List user assets - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/asset/list-user-assets/

List user assets

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/assets \
      --header 'X-API-Key: <api-key>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/assets"
    
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {'X-API-Key': '<api-key>'}};
    
    fetch('https://cloud.comfy.org/api/assets', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/assets",
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
    
    	url := "https://cloud.comfy.org/api/assets"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/assets")
      .header("X-API-Key", "<api-key>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/assets")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["X-API-Key"] = '<api-key>'
    
    response = http.request(request)
    puts response.read_body

200

400

401

500
    
    
    {
      "assets": [
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
      ],
      "total": 123,
      "has_more": true
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

# List user assets

Copiar páginaCopiar página

Retrieves a paginated list of assets belonging to the authenticated user. Supports filtering by tags, name, metadata, and sorting options.

Copiar páginaCopiar página

GET

/

api

/

assets

Pruébalo

List user assets

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/assets \
      --header 'X-API-Key: <api-key>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/assets"
    
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {'X-API-Key': '<api-key>'}};
    
    fetch('https://cloud.comfy.org/api/assets', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/assets",
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
    
    	url := "https://cloud.comfy.org/api/assets"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/assets")
      .header("X-API-Key", "<api-key>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/assets")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["X-API-Key"] = '<api-key>'
    
    response = http.request(request)
    puts response.read_body

200

400

401

500
    
    
    {
      "assets": [
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
      ],
      "total": 123,
      "has_more": true
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

include_tags

string[]

Filter assets that have ALL of these tags

​

exclude_tags

string[]

Exclude assets that have ANY of these tags

​

name_contains

string

Filter assets where name contains this substring (case-insensitive)

​

metadata_filter

string

JSON object for filtering by metadata fields

​

limit

integer

predeterminado:20

Maximum number of assets to return (1-500)

Rango requerido: `1 <= x <= 500`

​

offset

integer

predeterminado:0

Number of assets to skip for pagination

Rango requerido: `x >= 0`

​

sort

enum<string>

predeterminado:created_at

Field to sort by

Opciones disponibles: 

`name`, 

`created_at`, 

`updated_at`, 

`size`, 

`last_access_time`

​

order

enum<string>

predeterminado:desc

Sort order

Opciones disponibles: 

`asc`, 

`desc`

​

include_public

boolean

predeterminado:true

Whether to include public/shared assets in results

#### Respuesta

200

application/json

Success - Assets returned

​

assets

object[]

requerido

List of assets matching the query

Show child attributes

​

total

integer

requerido

Total number of assets matching the filters

​

has_more

boolean

requerido

Whether more assets are available beyond this page

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/asset/list-user-assets.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/asset/list-user-assets)

[Upload a mask image](https://docs.comfy.org/es/api-reference/cloud/file/upload-a-mask-image)[Upload a new asset](https://docs.comfy.org/es/api-reference/cloud/asset/upload-a-new-asset)

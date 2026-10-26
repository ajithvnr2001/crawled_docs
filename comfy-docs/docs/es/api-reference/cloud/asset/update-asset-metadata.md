---
url: https://docs.comfy.org/es/api-reference/cloud/asset/update-asset-metadata/
title: Update asset metadata - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:23.806083+00:00
---

# Update asset metadata - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/asset/update-asset-metadata/

Update asset metadata

cURL
    
    
    curl --request PUT \
      --url https://cloud.comfy.org/api/assets/{id} \
      --header 'Content-Type: application/json' \
      --header 'X-API-Key: <api-key>' \
      --data '
    {
      "name": "<string>",
      "tags": [
        "<string>"
      ],
      "mime_type": "<string>",
      "preview_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "user_metadata": {}
    }
    '
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/assets/{id}"
    
    payload = {
        "name": "<string>",
        "tags": ["<string>"],
        "mime_type": "<string>",
        "preview_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
        "user_metadata": {}
    }
    headers = {
        "X-API-Key": "<api-key>",
        "Content-Type": "application/json"
    }
    
    response = requests.put(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'PUT',
      headers: {'X-API-Key': '<api-key>', 'Content-Type': 'application/json'},
      body: JSON.stringify({
        name: '<string>',
        tags: ['<string>'],
        mime_type: '<string>',
        preview_id: '3c90c3cc-0d44-4b50-8888-8dd25736052a',
        user_metadata: {}
      })
    };
    
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
      CURLOPT_CUSTOMREQUEST => "PUT",
      CURLOPT_POSTFIELDS => json_encode([
        'name' => '<string>',
        'tags' => [
            '<string>'
        ],
        'mime_type' => '<string>',
        'preview_id' => '3c90c3cc-0d44-4b50-8888-8dd25736052a',
        'user_metadata' => [
            
        ]
      ]),
      CURLOPT_HTTPHEADER => [
        "Content-Type: application/json",
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
    	"strings"
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "https://cloud.comfy.org/api/assets/{id}"
    
    	payload := strings.NewReader("{\n  \"name\": \"<string>\",\n  \"tags\": [\n    \"<string>\"\n  ],\n  \"mime_type\": \"<string>\",\n  \"preview_id\": \"3c90c3cc-0d44-4b50-8888-8dd25736052a\",\n  \"user_metadata\": {}\n}")
    
    	req, _ := http.NewRequest("PUT", url, payload)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.put("https://cloud.comfy.org/api/assets/{id}")
      .header("X-API-Key", "<api-key>")
      .header("Content-Type", "application/json")
      .body("{\n  \"name\": \"<string>\",\n  \"tags\": [\n    \"<string>\"\n  ],\n  \"mime_type\": \"<string>\",\n  \"preview_id\": \"3c90c3cc-0d44-4b50-8888-8dd25736052a\",\n  \"user_metadata\": {}\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/assets/{id}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Put.new(url)
    request["X-API-Key"] = '<api-key>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"name\": \"<string>\",\n  \"tags\": [\n    \"<string>\"\n  ],\n  \"mime_type\": \"<string>\",\n  \"preview_id\": \"3c90c3cc-0d44-4b50-8888-8dd25736052a\",\n  \"user_metadata\": {}\n}"
    
    response = http.request(request)
    puts response.read_body

200

400

401

404

500
    
    
    {
      "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "updated_at": "2023-11-07T05:31:56Z",
      "name": "<string>",
      "asset_hash": "<string>",
      "tags": [
        "<string>"
      ],
      "mime_type": "<string>",
      "user_metadata": {}
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

# Update asset metadata

Copiar páginaCopiar página

Updates an asset’s metadata. At least one field must be provided. Only name, tags, and user_metadata can be updated.

Copiar páginaCopiar página

PUT

/

api

/

assets

/

{id}

Pruébalo

Update asset metadata

cURL
    
    
    curl --request PUT \
      --url https://cloud.comfy.org/api/assets/{id} \
      --header 'Content-Type: application/json' \
      --header 'X-API-Key: <api-key>' \
      --data '
    {
      "name": "<string>",
      "tags": [
        "<string>"
      ],
      "mime_type": "<string>",
      "preview_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "user_metadata": {}
    }
    '
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/assets/{id}"
    
    payload = {
        "name": "<string>",
        "tags": ["<string>"],
        "mime_type": "<string>",
        "preview_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
        "user_metadata": {}
    }
    headers = {
        "X-API-Key": "<api-key>",
        "Content-Type": "application/json"
    }
    
    response = requests.put(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'PUT',
      headers: {'X-API-Key': '<api-key>', 'Content-Type': 'application/json'},
      body: JSON.stringify({
        name: '<string>',
        tags: ['<string>'],
        mime_type: '<string>',
        preview_id: '3c90c3cc-0d44-4b50-8888-8dd25736052a',
        user_metadata: {}
      })
    };
    
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
      CURLOPT_CUSTOMREQUEST => "PUT",
      CURLOPT_POSTFIELDS => json_encode([
        'name' => '<string>',
        'tags' => [
            '<string>'
        ],
        'mime_type' => '<string>',
        'preview_id' => '3c90c3cc-0d44-4b50-8888-8dd25736052a',
        'user_metadata' => [
            
        ]
      ]),
      CURLOPT_HTTPHEADER => [
        "Content-Type: application/json",
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
    	"strings"
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "https://cloud.comfy.org/api/assets/{id}"
    
    	payload := strings.NewReader("{\n  \"name\": \"<string>\",\n  \"tags\": [\n    \"<string>\"\n  ],\n  \"mime_type\": \"<string>\",\n  \"preview_id\": \"3c90c3cc-0d44-4b50-8888-8dd25736052a\",\n  \"user_metadata\": {}\n}")
    
    	req, _ := http.NewRequest("PUT", url, payload)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.put("https://cloud.comfy.org/api/assets/{id}")
      .header("X-API-Key", "<api-key>")
      .header("Content-Type", "application/json")
      .body("{\n  \"name\": \"<string>\",\n  \"tags\": [\n    \"<string>\"\n  ],\n  \"mime_type\": \"<string>\",\n  \"preview_id\": \"3c90c3cc-0d44-4b50-8888-8dd25736052a\",\n  \"user_metadata\": {}\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/assets/{id}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Put.new(url)
    request["X-API-Key"] = '<api-key>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"name\": \"<string>\",\n  \"tags\": [\n    \"<string>\"\n  ],\n  \"mime_type\": \"<string>\",\n  \"preview_id\": \"3c90c3cc-0d44-4b50-8888-8dd25736052a\",\n  \"user_metadata\": {}\n}"
    
    response = http.request(request)
    puts response.read_body

200

400

401

404

500
    
    
    {
      "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "updated_at": "2023-11-07T05:31:56Z",
      "name": "<string>",
      "asset_hash": "<string>",
      "tags": [
        "<string>"
      ],
      "mime_type": "<string>",
      "user_metadata": {}
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

#### Parámetros de ruta

​

id

string<uuid>

requerido

Asset ID

#### Cuerpo

application/json

​

name

string

New display name for the asset

​

tags

string[]

Updated tags for the asset

​

mime_type

string

Updated MIME type of the asset

​

preview_id

string<uuid>

Updated preview asset ID

​

user_metadata

object

Updated custom metadata

#### Respuesta

200

application/json

Asset updated successfully

​

id

string<uuid>

requerido

Asset ID

​

updated_at

string<date-time>

requerido

Timestamp of the update

​

name

string

Updated name of the asset

​

asset_hash

string

Blake3 hash of the asset content

Pattern: `^blake3:[a-f0-9]{64}$`

​

tags

string[]

Updated tags for the asset

​

mime_type

string

Updated MIME type of the asset

​

user_metadata

object

Updated custom metadata

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/asset/update-asset-metadata.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/asset/update-asset-metadata)

[Get asset details](https://docs.comfy.org/es/api-reference/cloud/asset/get-asset-details)[Delete asset](https://docs.comfy.org/es/api-reference/cloud/asset/delete-asset)

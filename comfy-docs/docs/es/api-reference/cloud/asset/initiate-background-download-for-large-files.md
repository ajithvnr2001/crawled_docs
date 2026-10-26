---
url: https://docs.comfy.org/es/api-reference/cloud/asset/initiate-background-download-for-large-files/
title: Initiate background download for large files - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:23.908365+00:00
---

# Initiate background download for large files - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/asset/initiate-background-download-for-large-files/

Initiate background download for large files

cURL
    
    
    curl --request POST \
      --url https://cloud.comfy.org/api/assets/download \
      --header 'Content-Type: application/json' \
      --header 'X-API-Key: <api-key>' \
      --data '
    {
      "source_url": "https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.safetensors",
      "tags": [
        "<string>"
      ],
      "user_metadata": {},
      "preview_id": "550e8400-e29b-41d4-a716-446655440000"
    }
    '
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/assets/download"
    
    payload = {
        "source_url": "https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.safetensors",
        "tags": ["<string>"],
        "user_metadata": {},
        "preview_id": "550e8400-e29b-41d4-a716-446655440000"
    }
    headers = {
        "X-API-Key": "<api-key>",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'POST',
      headers: {'X-API-Key': '<api-key>', 'Content-Type': 'application/json'},
      body: JSON.stringify({
        source_url: 'https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.safetensors',
        tags: ['<string>'],
        user_metadata: {},
        preview_id: '550e8400-e29b-41d4-a716-446655440000'
      })
    };
    
    fetch('https://cloud.comfy.org/api/assets/download', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/assets/download",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'source_url' => 'https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.safetensors',
        'tags' => [
            '<string>'
        ],
        'user_metadata' => [
            
        ],
        'preview_id' => '550e8400-e29b-41d4-a716-446655440000'
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
    
    	url := "https://cloud.comfy.org/api/assets/download"
    
    	payload := strings.NewReader("{\n  \"source_url\": \"https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.safetensors\",\n  \"tags\": [\n    \"<string>\"\n  ],\n  \"user_metadata\": {},\n  \"preview_id\": \"550e8400-e29b-41d4-a716-446655440000\"\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://cloud.comfy.org/api/assets/download")
      .header("X-API-Key", "<api-key>")
      .header("Content-Type", "application/json")
      .body("{\n  \"source_url\": \"https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.safetensors\",\n  \"tags\": [\n    \"<string>\"\n  ],\n  \"user_metadata\": {},\n  \"preview_id\": \"550e8400-e29b-41d4-a716-446655440000\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/assets/download")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["X-API-Key"] = '<api-key>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"source_url\": \"https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.safetensors\",\n  \"tags\": [\n    \"<string>\"\n  ],\n  \"user_metadata\": {},\n  \"preview_id\": \"550e8400-e29b-41d4-a716-446655440000\"\n}"
    
    response = http.request(request)
    puts response.read_body

200

202

400

401

422

500
    
    
    {
      "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "name": "<string>",
      "size": 123,
      "created_at": "2023-11-07T05:31:56Z",
      "updated_at": "2023-11-07T05:31:56Z",
      "created_new": true,
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
      "task_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "status": "created",
      "message": "Download task created. Use task_id to track progress."
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

# Initiate background download for large files

Copiar páginaCopiar página

Initiates a background download job for large files from Huggingface or Civitai.

If the file already exists in storage, the asset record is created immediately and returned (200 OK). If the file doesn’t exist, a background task is created and the task ID is returned (202 Accepted). The frontend can track progress using GET /api/tasks/.

Copiar páginaCopiar página

POST

/

api

/

assets

/

download

Pruébalo

Initiate background download for large files

cURL
    
    
    curl --request POST \
      --url https://cloud.comfy.org/api/assets/download \
      --header 'Content-Type: application/json' \
      --header 'X-API-Key: <api-key>' \
      --data '
    {
      "source_url": "https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.safetensors",
      "tags": [
        "<string>"
      ],
      "user_metadata": {},
      "preview_id": "550e8400-e29b-41d4-a716-446655440000"
    }
    '
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/assets/download"
    
    payload = {
        "source_url": "https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.safetensors",
        "tags": ["<string>"],
        "user_metadata": {},
        "preview_id": "550e8400-e29b-41d4-a716-446655440000"
    }
    headers = {
        "X-API-Key": "<api-key>",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'POST',
      headers: {'X-API-Key': '<api-key>', 'Content-Type': 'application/json'},
      body: JSON.stringify({
        source_url: 'https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.safetensors',
        tags: ['<string>'],
        user_metadata: {},
        preview_id: '550e8400-e29b-41d4-a716-446655440000'
      })
    };
    
    fetch('https://cloud.comfy.org/api/assets/download', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/assets/download",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'source_url' => 'https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.safetensors',
        'tags' => [
            '<string>'
        ],
        'user_metadata' => [
            
        ],
        'preview_id' => '550e8400-e29b-41d4-a716-446655440000'
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
    
    	url := "https://cloud.comfy.org/api/assets/download"
    
    	payload := strings.NewReader("{\n  \"source_url\": \"https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.safetensors\",\n  \"tags\": [\n    \"<string>\"\n  ],\n  \"user_metadata\": {},\n  \"preview_id\": \"550e8400-e29b-41d4-a716-446655440000\"\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://cloud.comfy.org/api/assets/download")
      .header("X-API-Key", "<api-key>")
      .header("Content-Type", "application/json")
      .body("{\n  \"source_url\": \"https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.safetensors\",\n  \"tags\": [\n    \"<string>\"\n  ],\n  \"user_metadata\": {},\n  \"preview_id\": \"550e8400-e29b-41d4-a716-446655440000\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/assets/download")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["X-API-Key"] = '<api-key>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"source_url\": \"https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.safetensors\",\n  \"tags\": [\n    \"<string>\"\n  ],\n  \"user_metadata\": {},\n  \"preview_id\": \"550e8400-e29b-41d4-a716-446655440000\"\n}"
    
    response = http.request(request)
    puts response.read_body

200

202

400

401

422

500
    
    
    {
      "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "name": "<string>",
      "size": 123,
      "created_at": "2023-11-07T05:31:56Z",
      "updated_at": "2023-11-07T05:31:56Z",
      "created_new": true,
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
      "task_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "status": "created",
      "message": "Download task created. Use task_id to track progress."
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

#### Cuerpo

application/json

​

source_url

string<uri>

requerido

URL of the file to download (must be from huggingface.co or civitai.com)

Ejemplo:

`"https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.safetensors"`

​

tags

string[]

Optional tags for the asset (e.g., ["model", "checkpoint"])

​

user_metadata

object

Optional user-defined metadata to attach to the asset

​

preview_id

string<uuid>

Optional preview asset ID to associate with the downloaded asset

Ejemplo:

`"550e8400-e29b-41d4-a716-446655440000"`

#### Respuesta

200

application/json

File already exists in storage - asset created/returned immediately

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

created_new

boolean

requerido

Whether this was a new asset creation (true) or returned existing (false)

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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/asset/initiate-background-download-for-large-files.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/asset/initiate-background-download-for-large-files)

[Get asset metadata from remote URL](https://docs.comfy.org/es/api-reference/cloud/asset/get-asset-metadata-from-remote-url)[Get asset details](https://docs.comfy.org/es/api-reference/cloud/asset/get-asset-details)

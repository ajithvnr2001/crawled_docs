---
url: https://docs.comfy.org/api-reference/cloud/asset/initiate-background-download-for-large-files/
title: Initiate background download for large files - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:46:16.740927+00:00
---

# Initiate background download for large files - ComfyUI

> Source: https://docs.comfy.org/api-reference/cloud/asset/initiate-background-download-for-large-files/

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

Copy pageCopy page

Initiates a background download job for large files from Huggingface or Civitai.

If the file already exists in storage, the asset record is created immediately and returned (200 OK). If the file doesn’t exist, a background task is created and the task ID is returned (202 Accepted). The frontend can track progress using GET /api/tasks/.

Copy pageCopy page

POST

/

api

/

assets

/

download

Try it

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

#### Authorizations

​

X-API-Key

string

header

required

API key authentication. Generate an API key from your account settings at <https://platform.comfy.org/profile/api-keys>. Pass the key in the X-API-Key header.

#### Body

application/json

​

source_url

string<uri>

required

URL of the file to download (must be from huggingface.co or civitai.com)

Example:

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

Example:

`"550e8400-e29b-41d4-a716-446655440000"`

#### Response

200

application/json

File already exists in storage - asset created/returned immediately

​

id

string<uuid>

required

Unique identifier for the asset

​

name

string

required

Name of the asset file

​

size

integer<int64>

required

Size of the asset in bytes

​

created_at

string<date-time>

required

Timestamp when the asset was created

​

updated_at

string<date-time>

required

Timestamp when the asset was last updated

​

created_new

boolean

required

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

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/api-reference/cloud/asset/initiate-background-download-for-large-files.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/cloud/asset/initiate-background-download-for-large-files)

[Get asset metadata from remote URLPrevious](https://docs.comfy.org/api-reference/cloud/asset/get-asset-metadata-from-remote-url)[Get asset detailsNext](https://docs.comfy.org/api-reference/cloud/asset/get-asset-details)

⌘I

[ComfyUI home page![light logo](https://mintcdn.com/dripart/WCFdTagRdhtvk9-o/logo/light.svg?fit=max&auto=format&n=WCFdTagRdhtvk9-o&q=85&s=ec112de87239058f5a931a7e4b594965)![dark logo](https://mintcdn.com/dripart/QzWbjSCBG7w61rR3/logo/dark.svg?fit=max&auto=format&n=QzWbjSCBG7w61rR3&q=85&s=62b4d879fb3aadbd7a468d1539032d6f)](https://docs.comfy.org/)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

Resources

[installation](https://docs.comfy.org/installation/system_requirements)[Tutorials](https://docs.comfy.org/tutorials/basic/text-to-image)[Development](https://docs.comfy.org/development/overview)

Products

[Features](https://www.comfy.org/?utm_source=docs)[Gallery](https://www.comfy.org/gallery?utm_source=docs)[Download](https://www.comfy.org/download?utm_source=docs)

Company

[About](https://www.comfy.org/about?utm_source=docs)[Careers](https://www.comfy.org/careers?utm_source=docs)[Terms of Service](https://www.comfy.org/terms-of-service?utm_source=docs)[Privacy Policy](https://www.comfy.org/privacy-policy?utm_source=docs)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=dripart)

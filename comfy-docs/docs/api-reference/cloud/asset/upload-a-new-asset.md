---
url: https://docs.comfy.org/api-reference/cloud/asset/upload-a-new-asset/
title: Upload a new asset - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:46:18.625757+00:00
---

# Upload a new asset - ComfyUI

> Source: https://docs.comfy.org/api-reference/cloud/asset/upload-a-new-asset/

Upload a new asset

cURL
    
    
    curl --request POST \
      --url https://cloud.comfy.org/api/assets \
      --header 'Content-Type: multipart/form-data' \
      --header 'X-API-Key: <api-key>' \
      --form file=@example-file \
      --form 'tags=<string>' \
      --form id=3c90c3cc-0d44-4b50-8888-8dd25736052a \
      --form preview_id=3c90c3cc-0d44-4b50-8888-8dd25736052a \
      --form 'name=<string>' \
      --form 'mime_type=<string>' \
      --form 'user_metadata=<string>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/assets"
    
    files = { "file": ("example-file", open("example-file", "rb")) }
    payload = {
        "tags": "<string>",
        "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
        "preview_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
        "name": "<string>",
        "mime_type": "<string>",
        "user_metadata": "<string>"
    }
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.post(url, data=payload, files=files, headers=headers)
    
    print(response.text)
    
    
    const form = new FormData();
    form.append('file', '<string>');
    form.append('tags', '<string>');
    form.append('id', '3c90c3cc-0d44-4b50-8888-8dd25736052a');
    form.append('preview_id', '3c90c3cc-0d44-4b50-8888-8dd25736052a');
    form.append('name', '<string>');
    form.append('mime_type', '<string>');
    form.append('user_metadata', '<string>');
    
    const options = {method: 'POST', headers: {'X-API-Key': '<api-key>'}};
    
    options.body = form;
    
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
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"id\"\r\n\r\n3c90c3cc-0d44-4b50-8888-8dd25736052a\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"preview_id\"\r\n\r\n3c90c3cc-0d44-4b50-8888-8dd25736052a\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mime_type\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"user_metadata\"\r\n\r\n<string>\r\n-----011000010111000001101001--",
      CURLOPT_HTTPHEADER => [
        "Content-Type: multipart/form-data",
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
    
    	url := "https://cloud.comfy.org/api/assets"
    
    	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"id\"\r\n\r\n3c90c3cc-0d44-4b50-8888-8dd25736052a\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"preview_id\"\r\n\r\n3c90c3cc-0d44-4b50-8888-8dd25736052a\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mime_type\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"user_metadata\"\r\n\r\n<string>\r\n-----011000010111000001101001--")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://cloud.comfy.org/api/assets")
      .header("X-API-Key", "<api-key>")
      .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"id\"\r\n\r\n3c90c3cc-0d44-4b50-8888-8dd25736052a\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"preview_id\"\r\n\r\n3c90c3cc-0d44-4b50-8888-8dd25736052a\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mime_type\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"user_metadata\"\r\n\r\n<string>\r\n-----011000010111000001101001--")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/assets")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["X-API-Key"] = '<api-key>'
    request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"id\"\r\n\r\n3c90c3cc-0d44-4b50-8888-8dd25736052a\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"preview_id\"\r\n\r\n3c90c3cc-0d44-4b50-8888-8dd25736052a\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mime_type\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"user_metadata\"\r\n\r\n<string>\r\n-----011000010111000001101001--"
    
    response = http.request(request)
    puts response.read_body

200

201

400

401

403

404

413

415

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

# Upload a new asset

Copy pageCopy page

Uploads a new asset to the system with associated metadata. Supports two upload methods:

  1. Direct file upload (multipart/form-data)
  2. URL-based upload (application/json with source: “url”)



If an asset with the same hash already exists, returns the existing asset.

Copy pageCopy page

POST

/

api

/

assets

Try it

Upload a new asset

cURL
    
    
    curl --request POST \
      --url https://cloud.comfy.org/api/assets \
      --header 'Content-Type: multipart/form-data' \
      --header 'X-API-Key: <api-key>' \
      --form file=@example-file \
      --form 'tags=<string>' \
      --form id=3c90c3cc-0d44-4b50-8888-8dd25736052a \
      --form preview_id=3c90c3cc-0d44-4b50-8888-8dd25736052a \
      --form 'name=<string>' \
      --form 'mime_type=<string>' \
      --form 'user_metadata=<string>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/assets"
    
    files = { "file": ("example-file", open("example-file", "rb")) }
    payload = {
        "tags": "<string>",
        "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
        "preview_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
        "name": "<string>",
        "mime_type": "<string>",
        "user_metadata": "<string>"
    }
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.post(url, data=payload, files=files, headers=headers)
    
    print(response.text)
    
    
    const form = new FormData();
    form.append('file', '<string>');
    form.append('tags', '<string>');
    form.append('id', '3c90c3cc-0d44-4b50-8888-8dd25736052a');
    form.append('preview_id', '3c90c3cc-0d44-4b50-8888-8dd25736052a');
    form.append('name', '<string>');
    form.append('mime_type', '<string>');
    form.append('user_metadata', '<string>');
    
    const options = {method: 'POST', headers: {'X-API-Key': '<api-key>'}};
    
    options.body = form;
    
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
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"id\"\r\n\r\n3c90c3cc-0d44-4b50-8888-8dd25736052a\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"preview_id\"\r\n\r\n3c90c3cc-0d44-4b50-8888-8dd25736052a\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mime_type\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"user_metadata\"\r\n\r\n<string>\r\n-----011000010111000001101001--",
      CURLOPT_HTTPHEADER => [
        "Content-Type: multipart/form-data",
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
    
    	url := "https://cloud.comfy.org/api/assets"
    
    	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"id\"\r\n\r\n3c90c3cc-0d44-4b50-8888-8dd25736052a\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"preview_id\"\r\n\r\n3c90c3cc-0d44-4b50-8888-8dd25736052a\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mime_type\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"user_metadata\"\r\n\r\n<string>\r\n-----011000010111000001101001--")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://cloud.comfy.org/api/assets")
      .header("X-API-Key", "<api-key>")
      .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"id\"\r\n\r\n3c90c3cc-0d44-4b50-8888-8dd25736052a\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"preview_id\"\r\n\r\n3c90c3cc-0d44-4b50-8888-8dd25736052a\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mime_type\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"user_metadata\"\r\n\r\n<string>\r\n-----011000010111000001101001--")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/assets")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["X-API-Key"] = '<api-key>'
    request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"id\"\r\n\r\n3c90c3cc-0d44-4b50-8888-8dd25736052a\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"preview_id\"\r\n\r\n3c90c3cc-0d44-4b50-8888-8dd25736052a\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mime_type\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"user_metadata\"\r\n\r\n<string>\r\n-----011000010111000001101001--"
    
    response = http.request(request)
    puts response.read_body

200

201

400

401

403

404

413

415

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

multipart/form-dataapplication/jsonmultipart/form-dataapplication/json

​

file

file

required

The asset file to upload

​

tags

string[]

Freeform tags for the asset. Common types include "models", "input", "output", and "temp", but any tag can be used in any order.

​

id

string<uuid>

Optional asset ID for idempotent creation. If provided and asset exists, returns existing asset.

​

preview_id

string<uuid>

Optional preview asset ID. If not provided, images will use their own ID as preview.

​

name

string

Display name for the asset

​

mime_type

string

MIME type of the asset (e.g., "image/png", "video/mp4")

​

user_metadata

string

Custom JSON metadata as a string

#### Response

200

application/json

Asset already exists (returned existing asset)

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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/api-reference/cloud/asset/upload-a-new-asset.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/cloud/asset/upload-a-new-asset)

[List user assetsPrevious](https://docs.comfy.org/api-reference/cloud/asset/list-user-assets)[Create asset reference from existing hashNext](https://docs.comfy.org/api-reference/cloud/asset/create-asset-reference-from-existing-hash)

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

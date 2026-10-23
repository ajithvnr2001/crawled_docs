---
url: https://docs.comfy.org/api-reference/cloud/asset/update-asset-metadata/
title: Update asset metadata - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:46:17.679701+00:00
---

# Update asset metadata - ComfyUI

> Source: https://docs.comfy.org/api-reference/cloud/asset/update-asset-metadata/

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

Copy pageCopy page

Updates an asset’s metadata. At least one field must be provided. Only name, tags, and user_metadata can be updated.

Copy pageCopy page

PUT

/

api

/

assets

/

{id}

Try it

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

#### Authorizations

​

X-API-Key

string

header

required

API key authentication. Generate an API key from your account settings at <https://platform.comfy.org/profile/api-keys>. Pass the key in the X-API-Key header.

#### Path Parameters

​

id

string<uuid>

required

Asset ID

#### Body

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

#### Response

200

application/json

Asset updated successfully

​

id

string<uuid>

required

Asset ID

​

updated_at

string<date-time>

required

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

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/api-reference/cloud/asset/update-asset-metadata.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/cloud/asset/update-asset-metadata)

[Get asset detailsPrevious](https://docs.comfy.org/api-reference/cloud/asset/get-asset-details)[Delete assetNext](https://docs.comfy.org/api-reference/cloud/asset/delete-asset)

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

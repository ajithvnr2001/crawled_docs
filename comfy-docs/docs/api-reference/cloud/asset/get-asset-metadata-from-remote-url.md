---
url: https://docs.comfy.org/api-reference/cloud/asset/get-asset-metadata-from-remote-url/
title: Get asset metadata from remote URL - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:46:17.045325+00:00
---

# Get asset metadata from remote URL - ComfyUI

> Source: https://docs.comfy.org/api-reference/cloud/asset/get-asset-metadata-from-remote-url/

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

Copy pageCopy page

Retrieves metadata for an asset from a remote download URL without downloading the entire file. Supports various sources including CivitAI and other model repositories. Uses HEAD requests or API calls to fetch metadata efficiently. This endpoint is for previewing metadata before downloading, not for getting metadata of existing assets.

Copy pageCopy page

GET

/

api

/

assets

/

remote-metadata

Try it

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

#### Authorizations

​

X-API-Key

string

header

required

API key authentication. Generate an API key from your account settings at <https://platform.comfy.org/profile/api-keys>. Pass the key in the X-API-Key header.

#### Query Parameters

​

url

string<uri>

required

Download URL to retrieve metadata from

Example:

`"https://civitai.com/api/download/models/123456"`

#### Response

200

application/json

Metadata retrieved successfully

​

content_length

integer<int64>

required

Size of the asset in bytes (-1 if unknown)

Example:

`4294967296`

​

content_type

string

MIME type of the asset

Example:

`"application/octet-stream"`

​

filename

string

Suggested filename for the asset from source

Example:

`"realistic-vision-v5.safetensors"`

​

name

string

Display name or title for the asset from source

Example:

`"Realistic Vision v5.0"`

​

tags

string[]

Tags for categorization from source

Example:
    
    
    ["models", "checkpoint"]

​

preview_image

string

Preview image as base64-encoded data URL

Example:

`"data:image/jpeg;base64,/9j/4AAQSkZJRg..."`

​

validation

object

Validation results for the file

Show child attributes

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/api-reference/cloud/asset/get-asset-metadata-from-remote-url.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/cloud/asset/get-asset-metadata-from-remote-url)

[Create asset reference from existing hashPrevious](https://docs.comfy.org/api-reference/cloud/asset/create-asset-reference-from-existing-hash)[Initiate background download for large filesNext](https://docs.comfy.org/api-reference/cloud/asset/initiate-background-download-for-large-files)

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

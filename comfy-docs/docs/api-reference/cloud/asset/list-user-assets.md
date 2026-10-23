---
url: https://docs.comfy.org/api-reference/cloud/asset/list-user-assets/
title: List user assets - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:46:17.260813+00:00
---

# List user assets - ComfyUI

> Source: https://docs.comfy.org/api-reference/cloud/asset/list-user-assets/

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

Copy pageCopy page

Retrieves a paginated list of assets belonging to the authenticated user. Supports filtering by tags, name, metadata, and sorting options.

Copy pageCopy page

GET

/

api

/

assets

Try it

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

#### Authorizations

​

X-API-Key

string

header

required

API key authentication. Generate an API key from your account settings at <https://platform.comfy.org/profile/api-keys>. Pass the key in the X-API-Key header.

#### Query Parameters

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

default:20

Maximum number of assets to return (1-500)

Required range: `1 <= x <= 500`

​

offset

integer

default:0

Number of assets to skip for pagination

Required range: `x >= 0`

​

sort

enum<string>

default:created_at

Field to sort by

Available options: 

`name`, 

`created_at`, 

`updated_at`, 

`size`, 

`last_access_time`

​

order

enum<string>

default:desc

Sort order

Available options: 

`asc`, 

`desc`

​

include_public

boolean

default:true

Whether to include public/shared assets in results

#### Response

200

application/json

Success - Assets returned

​

assets

object[]

required

List of assets matching the query

Show child attributes

​

total

integer

required

Total number of assets matching the filters

​

has_more

boolean

required

Whether more assets are available beyond this page

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/api-reference/cloud/asset/list-user-assets.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/cloud/asset/list-user-assets)

[Upload a mask imagePrevious](https://docs.comfy.org/api-reference/cloud/file/upload-a-mask-image)[Upload a new assetNext](https://docs.comfy.org/api-reference/cloud/asset/upload-a-new-asset)

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

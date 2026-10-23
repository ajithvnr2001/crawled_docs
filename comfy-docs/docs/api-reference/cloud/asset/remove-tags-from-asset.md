---
url: https://docs.comfy.org/api-reference/cloud/asset/remove-tags-from-asset/
title: Remove tags from asset - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:46:17.835124+00:00
---

# Remove tags from asset - ComfyUI

> Source: https://docs.comfy.org/api-reference/cloud/asset/remove-tags-from-asset/

Remove tags from asset

cURL
    
    
    curl --request DELETE \
      --url https://cloud.comfy.org/api/assets/{id}/tags \
      --header 'Content-Type: application/json' \
      --header 'X-API-Key: <api-key>' \
      --data '
    {
      "tags": [
        "<string>"
      ]
    }
    '
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/assets/{id}/tags"
    
    payload = { "tags": ["<string>"] }
    headers = {
        "X-API-Key": "<api-key>",
        "Content-Type": "application/json"
    }
    
    response = requests.delete(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'DELETE',
      headers: {'X-API-Key': '<api-key>', 'Content-Type': 'application/json'},
      body: JSON.stringify({tags: ['<string>']})
    };
    
    fetch('https://cloud.comfy.org/api/assets/{id}/tags', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/assets/{id}/tags",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "DELETE",
      CURLOPT_POSTFIELDS => json_encode([
        'tags' => [
            '<string>'
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
    
    	url := "https://cloud.comfy.org/api/assets/{id}/tags"
    
    	payload := strings.NewReader("{\n  \"tags\": [\n    \"<string>\"\n  ]\n}")
    
    	req, _ := http.NewRequest("DELETE", url, payload)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.delete("https://cloud.comfy.org/api/assets/{id}/tags")
      .header("X-API-Key", "<api-key>")
      .header("Content-Type", "application/json")
      .body("{\n  \"tags\": [\n    \"<string>\"\n  ]\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/assets/{id}/tags")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Delete.new(url)
    request["X-API-Key"] = '<api-key>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"tags\": [\n    \"<string>\"\n  ]\n}"
    
    response = http.request(request)
    puts response.read_body

200

400

401

404

500
    
    
    {
      "total_tags": [
        "<string>"
      ],
      "added": [
        "<string>"
      ],
      "removed": [
        "<string>"
      ],
      "already_present": [
        "<string>"
      ],
      "not_present": [
        "<string>"
      ]
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

# Remove tags from asset

Copy pageCopy page

Removes one or more tags from an existing asset

Copy pageCopy page

DELETE

/

api

/

assets

/

{id}

/

tags

Try it

Remove tags from asset

cURL
    
    
    curl --request DELETE \
      --url https://cloud.comfy.org/api/assets/{id}/tags \
      --header 'Content-Type: application/json' \
      --header 'X-API-Key: <api-key>' \
      --data '
    {
      "tags": [
        "<string>"
      ]
    }
    '
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/assets/{id}/tags"
    
    payload = { "tags": ["<string>"] }
    headers = {
        "X-API-Key": "<api-key>",
        "Content-Type": "application/json"
    }
    
    response = requests.delete(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'DELETE',
      headers: {'X-API-Key': '<api-key>', 'Content-Type': 'application/json'},
      body: JSON.stringify({tags: ['<string>']})
    };
    
    fetch('https://cloud.comfy.org/api/assets/{id}/tags', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/assets/{id}/tags",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "DELETE",
      CURLOPT_POSTFIELDS => json_encode([
        'tags' => [
            '<string>'
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
    
    	url := "https://cloud.comfy.org/api/assets/{id}/tags"
    
    	payload := strings.NewReader("{\n  \"tags\": [\n    \"<string>\"\n  ]\n}")
    
    	req, _ := http.NewRequest("DELETE", url, payload)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.delete("https://cloud.comfy.org/api/assets/{id}/tags")
      .header("X-API-Key", "<api-key>")
      .header("Content-Type", "application/json")
      .body("{\n  \"tags\": [\n    \"<string>\"\n  ]\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/assets/{id}/tags")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Delete.new(url)
    request["X-API-Key"] = '<api-key>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"tags\": [\n    \"<string>\"\n  ]\n}"
    
    response = http.request(request)
    puts response.read_body

200

400

401

404

500
    
    
    {
      "total_tags": [
        "<string>"
      ],
      "added": [
        "<string>"
      ],
      "removed": [
        "<string>"
      ],
      "already_present": [
        "<string>"
      ],
      "not_present": [
        "<string>"
      ]
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

tags

string[]

required

Tags to remove from the asset

Minimum array length: `1`

#### Response

200

application/json

Tags removed successfully

​

total_tags

string[]

required

All tags on the asset after the operation

​

added

string[]

Tags that were successfully added (for add operation)

​

removed

string[]

Tags that were successfully removed (for remove operation)

​

already_present

string[]

Tags that were already present (for add operation)

​

not_present

string[]

Tags that were not present (for remove operation)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/api-reference/cloud/asset/remove-tags-from-asset.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/cloud/asset/remove-tags-from-asset)

[Add tags to assetPrevious](https://docs.comfy.org/api-reference/cloud/asset/add-tags-to-asset)[List all tagsNext](https://docs.comfy.org/api-reference/cloud/asset/list-all-tags)

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

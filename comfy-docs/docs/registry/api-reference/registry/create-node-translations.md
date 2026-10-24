---
url: https://docs.comfy.org/registry/api-reference/registry/create-node-translations/
title: Create Node Translations - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-24T11:54:44.643308+00:00
---

# Create Node Translations - ComfyUI

> Source: https://docs.comfy.org/registry/api-reference/registry/create-node-translations/

Create Node Translations

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/nodes/{nodeId}/translations \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '{
      "data": {}
    }'
    
    
    import requests
    
    url = "https://api.comfy.org/nodes/{nodeId}/translations"
    
    payload = { "data": {} }
    headers = {
        "Authorization": "Bearer <token>",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'POST',
      headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
      body: JSON.stringify({data: {}})
    };
    
    fetch('https://api.comfy.org/nodes/{nodeId}/translations', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/nodes/{nodeId}/translations",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'data' => [
            
        ]
      ]),
      CURLOPT_HTTPHEADER => [
        "Authorization: Bearer <token>",
        "Content-Type: application/json"
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
    
    	url := "https://api.comfy.org/nodes/{nodeId}/translations"
    
    	payload := strings.NewReader("{\n  \"data\": {}\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/nodes/{nodeId}/translations")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"data\": {}\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/nodes/{nodeId}/translations")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"data\": {}\n}"
    
    response = http.request(request)
    puts response.read_body

404

500
    
    
    {
      "details": [
        "<string>"
      ],
      "message": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

Registry API Reference

# Create Node Translations

Copy pageCopy page

Copy pageCopy page

POST

/

nodes

/

{nodeId}

/

translations

Try it

Create Node Translations

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/nodes/{nodeId}/translations \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '{
      "data": {}
    }'
    
    
    import requests
    
    url = "https://api.comfy.org/nodes/{nodeId}/translations"
    
    payload = { "data": {} }
    headers = {
        "Authorization": "Bearer <token>",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'POST',
      headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
      body: JSON.stringify({data: {}})
    };
    
    fetch('https://api.comfy.org/nodes/{nodeId}/translations', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/nodes/{nodeId}/translations",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'data' => [
            
        ]
      ]),
      CURLOPT_HTTPHEADER => [
        "Authorization: Bearer <token>",
        "Content-Type: application/json"
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
    
    	url := "https://api.comfy.org/nodes/{nodeId}/translations"
    
    	payload := strings.NewReader("{\n  \"data\": {}\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/nodes/{nodeId}/translations")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"data\": {}\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/nodes/{nodeId}/translations")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"data\": {}\n}"
    
    response = http.request(request)
    puts response.read_body

404

500
    
    
    {
      "details": [
        "<string>"
      ],
      "message": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

#### Authorizations

BearerAuthComfyAdminSecretAuthBearerAuthComfyAdminSecretAuth

​

Authorization

string

header

required

Bearer token authentication. Normally a Firebase or Cloud JWT. A 'comfyui-' prefixed API key is also accepted in this header: the prefix classifies the value as an API key and it is validated exactly as if it had been sent in X-API-Key. Accepted on the operations served by the comfyFirebase auth middleware (BE-9720, parity with ingest).

#### Path Parameters

​

nodeId

string

required

The unique identifier of the node.

#### Body

application/json

​

data

object

Show child attributes

#### Response

201

Detailed information about a specific node

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/registry/api-reference/registry/create-node-translations.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/registry/api-reference/registry/create-node-translations)

[Add review to a specific version of a node](https://docs.comfy.org/registry/api-reference/registry/add-review-to-a-specific-version-of-a-node)[List all versions of a node](https://docs.comfy.org/registry/api-reference/registry/list-all-versions-of-a-node)

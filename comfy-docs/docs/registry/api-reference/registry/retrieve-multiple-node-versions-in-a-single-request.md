---
url: https://docs.comfy.org/registry/api-reference/registry/retrieve-multiple-node-versions-in-a-single-request/
title: Retrieve multiple node versions in a single request - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:26.924718+00:00
---

# Retrieve multiple node versions in a single request - ComfyUI

> Source: https://docs.comfy.org/registry/api-reference/registry/retrieve-multiple-node-versions-in-a-single-request/

Retrieve multiple node versions in a single request

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/bulk/nodes/versions \
      --header 'Content-Type: application/json' \
      --data '
    {
      "node_versions": [
        {
          "node_id": "<string>",
          "version": "<string>"
        }
      ]
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/bulk/nodes/versions"
    
    payload = { "node_versions": [
            {
                "node_id": "<string>",
                "version": "<string>"
            }
        ] }
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({node_versions: [{node_id: '<string>', version: '<string>'}]})
    };
    
    fetch('https://api.comfy.org/bulk/nodes/versions', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/bulk/nodes/versions",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'node_versions' => [
            [
                    'node_id' => '<string>',
                    'version' => '<string>'
            ]
        ]
      ]),
      CURLOPT_HTTPHEADER => [
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
    
    	url := "https://api.comfy.org/bulk/nodes/versions"
    
    	payload := strings.NewReader("{\n  \"node_versions\": [\n    {\n      \"node_id\": \"<string>\",\n      \"version\": \"<string>\"\n    }\n  ]\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/bulk/nodes/versions")
      .header("Content-Type", "application/json")
      .body("{\n  \"node_versions\": [\n    {\n      \"node_id\": \"<string>\",\n      \"version\": \"<string>\"\n    }\n  ]\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/bulk/nodes/versions")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"node_versions\": [\n    {\n      \"node_id\": \"<string>\",\n      \"version\": \"<string>\"\n    }\n  ]\n}"
    
    response = http.request(request)
    puts response.read_body

200

400

500
    
    
    {
      "node_versions": [
        {
          "identifier": {
            "node_id": "<string>",
            "version": "<string>"
          },
          "status": "success",
          "error_message": "<string>",
          "node_version": {
            "changelog": "<string>",
            "comfy_node_extract_status": "<string>",
            "createdAt": "2023-11-07T05:31:56Z",
            "dependencies": [
              "<string>"
            ],
            "deprecated": true,
            "downloadUrl": "<string>",
            "id": "<string>",
            "node_id": "<string>",
            "status": "NodeVersionStatusActive",
            "status_reason": "<string>",
            "supported_accelerators": [
              "<string>"
            ],
            "supported_comfyui_frontend_version": "<string>",
            "supported_comfyui_version": "<string>",
            "supported_os": [
              "<string>"
            ],
            "tags": [
              "<string>"
            ],
            "tags_admin": [
              "<string>"
            ],
            "version": "<string>"
          }
        }
      ]
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

Registry API Reference

# Retrieve multiple node versions in a single request

Copy pageCopy page

Retrieves up to 1000 node versions in one request. Requests carrying more than 1000 identifiers are rejected in full with a 400 — there is no partial result — so clients with more than 1000 installed packs must split the list into batches of at most 1000 and merge the responses. Each node_id and version value is limited to 200 characters.

Copy pageCopy page

POST

/

bulk

/

nodes

/

versions

Try it

Retrieve multiple node versions in a single request

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/bulk/nodes/versions \
      --header 'Content-Type: application/json' \
      --data '
    {
      "node_versions": [
        {
          "node_id": "<string>",
          "version": "<string>"
        }
      ]
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/bulk/nodes/versions"
    
    payload = { "node_versions": [
            {
                "node_id": "<string>",
                "version": "<string>"
            }
        ] }
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({node_versions: [{node_id: '<string>', version: '<string>'}]})
    };
    
    fetch('https://api.comfy.org/bulk/nodes/versions', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/bulk/nodes/versions",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'node_versions' => [
            [
                    'node_id' => '<string>',
                    'version' => '<string>'
            ]
        ]
      ]),
      CURLOPT_HTTPHEADER => [
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
    
    	url := "https://api.comfy.org/bulk/nodes/versions"
    
    	payload := strings.NewReader("{\n  \"node_versions\": [\n    {\n      \"node_id\": \"<string>\",\n      \"version\": \"<string>\"\n    }\n  ]\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/bulk/nodes/versions")
      .header("Content-Type", "application/json")
      .body("{\n  \"node_versions\": [\n    {\n      \"node_id\": \"<string>\",\n      \"version\": \"<string>\"\n    }\n  ]\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/bulk/nodes/versions")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"node_versions\": [\n    {\n      \"node_id\": \"<string>\",\n      \"version\": \"<string>\"\n    }\n  ]\n}"
    
    response = http.request(request)
    puts response.read_body

200

400

500
    
    
    {
      "node_versions": [
        {
          "identifier": {
            "node_id": "<string>",
            "version": "<string>"
          },
          "status": "success",
          "error_message": "<string>",
          "node_version": {
            "changelog": "<string>",
            "comfy_node_extract_status": "<string>",
            "createdAt": "2023-11-07T05:31:56Z",
            "dependencies": [
              "<string>"
            ],
            "deprecated": true,
            "downloadUrl": "<string>",
            "id": "<string>",
            "node_id": "<string>",
            "status": "NodeVersionStatusActive",
            "status_reason": "<string>",
            "supported_accelerators": [
              "<string>"
            ],
            "supported_comfyui_frontend_version": "<string>",
            "supported_comfyui_version": "<string>",
            "supported_os": [
              "<string>"
            ],
            "tags": [
              "<string>"
            ],
            "tags_admin": [
              "<string>"
            ],
            "version": "<string>"
          }
        }
      ]
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

#### Body

application/json

​

node_versions

object[]

required

List of node ID and version pairs to retrieve

Required array length: `1 - 1000` elements

Show child attributes

#### Response

200

application/json

Successfully retrieved node versions

​

node_versions

object[]

required

List of retrieved node versions with their status

Show child attributes

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/registry/api-reference/registry/retrieve-multiple-node-versions-in-a-single-request.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/registry/api-reference/registry/retrieve-multiple-node-versions-in-a-single-request)

[Retrieve a specific version of a nodePrevious](https://docs.comfy.org/registry/api-reference/registry/retrieve-a-specific-version-of-a-node)[List all node versions given some filters.Next](https://docs.comfy.org/registry/api-reference/registry/list-all-node-versions-given-some-filters)

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

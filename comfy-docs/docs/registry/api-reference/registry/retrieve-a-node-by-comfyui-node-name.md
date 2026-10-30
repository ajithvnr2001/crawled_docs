---
url: https://docs.comfy.org/registry/api-reference/registry/retrieve-a-node-by-comfyui-node-name/
title: Retrieve a node by ComfyUI node name - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-30T13:55:20.695207+00:00
---

# Retrieve a node by ComfyUI node name - ComfyUI

> Source: https://docs.comfy.org/registry/api-reference/registry/retrieve-a-node-by-comfyui-node-name/

Retrieve a node by ComfyUI node name

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/comfy-nodes/{comfyNodeName}/node
    
    
    import requests
    
    url = "https://api.comfy.org/comfy-nodes/{comfyNodeName}/node"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.comfy.org/comfy-nodes/{comfyNodeName}/node', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/comfy-nodes/{comfyNodeName}/node",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "GET",
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
    
    	url := "https://api.comfy.org/comfy-nodes/{comfyNodeName}/node"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/comfy-nodes/{comfyNodeName}/node")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/comfy-nodes/{comfyNodeName}/node")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

404

500
    
    
    {
      "author": "<string>",
      "banner_url": "<string>",
      "category": "<string>",
      "created_at": "2023-11-07T05:31:56Z",
      "description": "<string>",
      "downloads": 123,
      "github_stars": 123,
      "icon": "<string>",
      "id": "<string>",
      "latest_version": {
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
      },
      "license": "<string>",
      "name": "<string>",
      "preempted_comfy_node_names": [
        "<string>"
      ],
      "publisher": {
        "createdAt": "2023-11-07T05:31:56Z",
        "description": "<string>",
        "id": "<string>",
        "logo": "<string>",
        "members": [
          {
            "id": "<string>",
            "role": "<string>",
            "user": {
              "email": "<string>",
              "id": "<string>",
              "name": "<string>"
            }
          }
        ],
        "name": "<string>",
        "source_code_repo": "<string>",
        "status": "PublisherStatusActive",
        "support": "<string>",
        "website": "<string>"
      },
      "rating": 123,
      "repository": "<string>",
      "search_ranking": 123,
      "status": "NodeStatusActive",
      "status_detail": "<string>",
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
      "translations": {}
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

# Retrieve a node by ComfyUI node name

Copy pageCopy page

Returns the node that contains a ComfyUI node with the specified name

Copy pageCopy page

GET

/

comfy-nodes

/

{comfyNodeName}

/

node

Try it

Retrieve a node by ComfyUI node name

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/comfy-nodes/{comfyNodeName}/node
    
    
    import requests
    
    url = "https://api.comfy.org/comfy-nodes/{comfyNodeName}/node"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.comfy.org/comfy-nodes/{comfyNodeName}/node', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/comfy-nodes/{comfyNodeName}/node",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "GET",
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
    
    	url := "https://api.comfy.org/comfy-nodes/{comfyNodeName}/node"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/comfy-nodes/{comfyNodeName}/node")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/comfy-nodes/{comfyNodeName}/node")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

404

500
    
    
    {
      "author": "<string>",
      "banner_url": "<string>",
      "category": "<string>",
      "created_at": "2023-11-07T05:31:56Z",
      "description": "<string>",
      "downloads": 123,
      "github_stars": 123,
      "icon": "<string>",
      "id": "<string>",
      "latest_version": {
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
      },
      "license": "<string>",
      "name": "<string>",
      "preempted_comfy_node_names": [
        "<string>"
      ],
      "publisher": {
        "createdAt": "2023-11-07T05:31:56Z",
        "description": "<string>",
        "id": "<string>",
        "logo": "<string>",
        "members": [
          {
            "id": "<string>",
            "role": "<string>",
            "user": {
              "email": "<string>",
              "id": "<string>",
              "name": "<string>"
            }
          }
        ],
        "name": "<string>",
        "source_code_repo": "<string>",
        "status": "PublisherStatusActive",
        "support": "<string>",
        "website": "<string>"
      },
      "rating": 123,
      "repository": "<string>",
      "search_ranking": 123,
      "status": "NodeStatusActive",
      "status_detail": "<string>",
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
      "translations": {}
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

#### Path Parameters

​

comfyNodeName

string

required

The name of the ComfyUI node

#### Response

200

application/json

Node details

​

author

string

​

banner_url

string

URL to the node's banner.

​

category

string

deprecated

DEPRECATED: The category of the node. Use 'tags' field instead. This field will be removed in a future version.

​

created_at

string<date-time>

The date and time when the node was created

​

description

string

​

downloads

integer

The number of downloads of the node.

​

github_stars

integer

Number of stars on the GitHub repository.

​

icon

string

URL to the node's icon.

​

id

string

The unique identifier of the node.

​

latest_version

object

Show child attributes

​

license

string

The path to the LICENSE file in the node's repository.

​

name

string

The display name of the node.

​

preempted_comfy_node_names

string[]

A list of Comfy node names that are preempted by this node.

​

publisher

object

Show child attributes

​

rating

number

The average rating of the node.

​

repository

string

URL to the node's repository.

​

search_ranking

integer

A numerical value representing the node's search ranking, used for sorting search results.

​

status

enum<string>

Available options: 

`NodeStatusActive`, 

`NodeStatusDeleted`, 

`NodeStatusBanned`

​

status_detail

string

The status detail of the node.

​

supported_accelerators

string[]

List of accelerators (e.g. CUDA, DirectML, ROCm) that this node supports

​

supported_comfyui_frontend_version

string

Supported versions of ComfyUI frontend

​

supported_comfyui_version

string

Supported versions of ComfyUI

​

supported_os

string[]

List of operating systems that this node supports

​

tags

string[]

​

tags_admin

string[]

Admin-only tags for security warnings and admin metadata

​

translations

object

Translations of node metadata in different languages.

Show child attributes

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/registry/api-reference/registry/retrieve-a-node-by-comfyui-node-name.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/registry/api-reference/registry/retrieve-a-node-by-comfyui-node-name)

[list all comfy-nodes](https://docs.comfy.org/registry/api-reference/registry/list-all-comfy-nodes)[create comfy-nodes for certain node](https://docs.comfy.org/registry/api-reference/registry/create-comfy-nodes-for-certain-node)

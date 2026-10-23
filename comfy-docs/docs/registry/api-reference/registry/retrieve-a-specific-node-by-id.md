---
url: https://docs.comfy.org/registry/api-reference/registry/retrieve-a-specific-node-by-id/
title: Retrieve a specific node by ID - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:26.862523+00:00
---

# Retrieve a specific node by ID - ComfyUI

> Source: https://docs.comfy.org/registry/api-reference/registry/retrieve-a-specific-node-by-id/

Retrieve a specific node by ID

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/nodes/{nodeId}
    
    
    import requests
    
    url = "https://api.comfy.org/nodes/{nodeId}"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.comfy.org/nodes/{nodeId}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/nodes/{nodeId}",
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
    
    	url := "https://api.comfy.org/nodes/{nodeId}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/nodes/{nodeId}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/nodes/{nodeId}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

403

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
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

Registry API Reference

# Retrieve a specific node by ID

Copy pageCopy page

Returns the details of a specific node.

Copy pageCopy page

GET

/

nodes

/

{nodeId}

Try it

Retrieve a specific node by ID

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/nodes/{nodeId}
    
    
    import requests
    
    url = "https://api.comfy.org/nodes/{nodeId}"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.comfy.org/nodes/{nodeId}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/nodes/{nodeId}",
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
    
    	url := "https://api.comfy.org/nodes/{nodeId}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/nodes/{nodeId}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/nodes/{nodeId}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

403

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
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

#### Path Parameters

​

nodeId

string

required

#### Query Parameters

​

include_translations

boolean

Whether to include the translation or not

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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/registry/api-reference/registry/retrieve-a-specific-node-by-id.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/registry/api-reference/registry/retrieve-a-specific-node-by-id)

[Retrieves a list of nodesPrevious](https://docs.comfy.org/registry/api-reference/registry/retrieves-a-list-of-nodes)[Returns a node version to be installed.Next](https://docs.comfy.org/registry/api-reference/registry/returns-a-node-version-to-be-installed)

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

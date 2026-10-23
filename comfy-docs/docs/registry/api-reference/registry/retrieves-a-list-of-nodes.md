---
url: https://docs.comfy.org/registry/api-reference/registry/retrieves-a-list-of-nodes/
title: Retrieves a list of nodes - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:27.141336+00:00
---

# Retrieves a list of nodes - ComfyUI

> Source: https://docs.comfy.org/registry/api-reference/registry/retrieves-a-list-of-nodes/

Retrieves a list of nodes

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/nodes/search
    
    
    import requests
    
    url = "https://api.comfy.org/nodes/search"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.comfy.org/nodes/search', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/nodes/search",
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
    
    	url := "https://api.comfy.org/nodes/search"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/nodes/search")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/nodes/search")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

500
    
    
    {
      "limit": 123,
      "nodes": [
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
      ],
      "page": 123,
      "total": 123,
      "totalPages": 123
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

Registry API Reference

# Retrieves a list of nodes

Copy pageCopy page

Returns a paginated list of nodes across all publishers.

Copy pageCopy page

GET

/

nodes

/

search

Try it

Retrieves a list of nodes

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/nodes/search
    
    
    import requests
    
    url = "https://api.comfy.org/nodes/search"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.comfy.org/nodes/search', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/nodes/search",
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
    
    	url := "https://api.comfy.org/nodes/search"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/nodes/search")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/nodes/search")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

500
    
    
    {
      "limit": 123,
      "nodes": [
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
      ],
      "page": 123,
      "total": 123,
      "totalPages": 123
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

#### Query Parameters

​

page

integer

default:1

Page number of the nodes list

​

limit

integer

default:10

Number of nodes to return per page. Values above the declared maximum are outside the contract, but this service does not reject them: it serves the maximum instead, and the page size actually served is echoed back as limit (and drives totalPages), so a clamp is always detectable by the caller. Treat the maximum as the real page stride — a client that asks for more and assumes it received more will miss rows. 0 and negative values are also accepted and select the default, which is why no minimum is declared: sub-1 is meaningful here, not invalid.

Required range: `x <= 100`

​

search

string

Keyword to search the nodes

​

repository_url_search

string

Keyword to search the nodes by repository URL

​

comfy_node_search

string

Keyword to search the nodes by comfy node name

​

supported_os

string

Filter nodes by supported operating systems

​

supported_accelerator

string

Filter nodes by supported accelerator

​

include_banned

boolean

Whether to include banned nodes in the results. Defaults to excluding them; pass true to include.

#### Response

200

application/json

A paginated list of nodes

​

limit

integer

Maximum number of nodes per page

​

nodes

object[]

Show child attributes

​

page

integer

Current page number

​

total

integer

Total number of nodes available

​

totalPages

integer

Total number of pages available

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/registry/api-reference/registry/retrieves-a-list-of-nodes.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/registry/api-reference/registry/retrieves-a-list-of-nodes)

[Unpublish (delete) a specific version of a nodePrevious](https://docs.comfy.org/registry/api-reference/registry/unpublish-delete-a-specific-version-of-a-node)[Retrieves a list of nodesNext](https://docs.comfy.org/registry/api-reference/registry/retrieves-a-list-of-nodes)

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

---
url: https://docs.comfy.org/es/registry/api-reference/registry/retrieves-a-list-of-nodes/
title: Retrieves a list of nodes - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-29T14:00:25.133229+00:00
---

# Retrieves a list of nodes - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/registry/retrieves-a-list-of-nodes/

Retrieves a list of nodes

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/nodes
    
    
    import requests
    
    url = "https://api.comfy.org/nodes"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.comfy.org/nodes', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/nodes",
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
    
    	url := "https://api.comfy.org/nodes"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/nodes")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/nodes")
    
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

Registry

# Retrieves a list of nodes

Copiar páginaCopiar página

Returns a paginated list of nodes across all publishers.

Copiar páginaCopiar página

GET

/

nodes

Pruébalo

Retrieves a list of nodes

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/nodes
    
    
    import requests
    
    url = "https://api.comfy.org/nodes"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.comfy.org/nodes', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/nodes",
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
    
    	url := "https://api.comfy.org/nodes"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/nodes")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/nodes")
    
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

#### Parámetros de consulta

​

page

integer

predeterminado:1

Page number of the nodes list

​

limit

integer

predeterminado:10

Number of nodes to return per page. Values above the declared maximum are outside the contract, but this service does not reject them: it serves the maximum instead, and the page size actually served is echoed back as limit (and drives totalPages), so a clamp is always detectable by the caller. Treat the maximum as the real page stride — a client that asks for more and assumes it received more will miss rows. 0 and negative values are also accepted and select the default, which is why no minimum is declared: sub-1 is meaningful here, not invalid.

Rango requerido: `x <= 100`

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

​

timestamp

string<date-time>

Retrieve nodes created or updated after this timestamp (ISO 8601 format)

​

latest

boolean

Whether to fetch fresh result from database or use cached one if false

​

sort

string[]

Node column to order by, ascending; append `;desc` to the value (e.g. `name;desc`) for descending. Generated clients and params-object helpers escape the `;` for you; only a hand-built raw query string must write it as `%3B` (`sort=name%3Bdesc`), because a raw `;` makes Go's query parser discard the whole `sort=...` pair before the handler sees it. Allowed columns: `id`, `normalized_id`, `publisher_id`, `name`, `category`, `author`, `status`, `create_time`, `update_time`, `total_install`, `total_star`, `total_review`, `github_stars`, `search_ranking`. Column and direction are case-insensitive. At most 2 sort terms are applied (a primary order and a tie-breaker); an unknown column, a malformed term, a repeated column or a term past the second is ignored rather than rejected, and the listing is returned without that ordering.

​

node_id

string[]

node_id to use as filter

​

comfyui_version

string

Comfy UI version

​

form_factor

string

The platform requesting the nodes

#### Respuesta

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

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/registry/retrieves-a-list-of-nodes.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/registry/retrieves-a-list-of-nodes)

[Get server feature flags](https://docs.comfy.org/es/registry/api-reference/registry/get-server-feature-flags)[Retrieves a list of nodes](https://docs.comfy.org/es/registry/api-reference/registry/retrieves-a-list-of-nodes-1)

---
url: https://docs.comfy.org/es/registry/api-reference/registry/retrieve-all-nodes-1/
title: Retrieve all nodes - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-28T13:54:26.512905+00:00
---

# Retrieve all nodes - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/registry/retrieve-all-nodes-1/

Retrieve all nodes

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/publishers/{publisherId}/nodes/v2
    
    
    import requests
    
    url = "https://api.comfy.org/publishers/{publisherId}/nodes/v2"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.comfy.org/publishers/{publisherId}/nodes/v2', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/publishers/{publisherId}/nodes/v2",
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
    
    	url := "https://api.comfy.org/publishers/{publisherId}/nodes/v2"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/publishers/{publisherId}/nodes/v2")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/publishers/{publisherId}/nodes/v2")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

400

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
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

Registry

# Retrieve all nodes

Copiar páginaCopiar página

Copiar páginaCopiar página

GET

/

publishers

/

{publisherId}

/

nodes

/

v2

Pruébalo

Retrieve all nodes

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/publishers/{publisherId}/nodes/v2
    
    
    import requests
    
    url = "https://api.comfy.org/publishers/{publisherId}/nodes/v2"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.comfy.org/publishers/{publisherId}/nodes/v2', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/publishers/{publisherId}/nodes/v2",
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
    
    	url := "https://api.comfy.org/publishers/{publisherId}/nodes/v2"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/publishers/{publisherId}/nodes/v2")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/publishers/{publisherId}/nodes/v2")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

400

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
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

#### Parámetros de ruta

​

publisherId

string

requerido

#### Parámetros de consulta

​

include_banned

boolean

Whether to include banned nodes in the results. Defaults to excluding them; pass true to include.

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

#### Respuesta

200

application/json

List of all nodes

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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/registry/retrieve-all-nodes-1.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/registry/retrieve-all-nodes-1)

[Create a new custom node](https://docs.comfy.org/es/registry/api-reference/registry/create-a-new-custom-node)[Update a specific node](https://docs.comfy.org/es/registry/api-reference/registry/update-a-specific-node)

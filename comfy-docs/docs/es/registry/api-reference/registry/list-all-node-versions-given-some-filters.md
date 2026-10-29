---
url: https://docs.comfy.org/es/registry/api-reference/registry/list-all-node-versions-given-some-filters/
title: List all node versions given some filters. - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-29T14:00:20.323019+00:00
---

# List all node versions given some filters. - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/registry/list-all-node-versions-given-some-filters/

List all node versions given some filters.

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/versions
    
    
    import requests
    
    url = "https://api.comfy.org/versions"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.comfy.org/versions', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/versions",
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
    
    	url := "https://api.comfy.org/versions"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/versions")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/versions")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

400

403

500
    
    
    {
      "page": 123,
      "pageSize": 123,
      "total": 123,
      "totalPages": 123,
      "versions": [
        {
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
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

Registry

# List all node versions given some filters.

Copiar páginaCopiar página

Copiar páginaCopiar página

GET

/

versions

Pruébalo

List all node versions given some filters.

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/versions
    
    
    import requests
    
    url = "https://api.comfy.org/versions"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.comfy.org/versions', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/versions",
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
    
    	url := "https://api.comfy.org/versions"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/versions")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/versions")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

400

403

500
    
    
    {
      "page": 123,
      "pageSize": 123,
      "total": 123,
      "totalPages": 123,
      "versions": [
        {
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
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

#### Parámetros de consulta

​

nodeId

string

​

statuses

enum<string>[]

Opciones disponibles: 

`NodeVersionStatusActive`, 

`NodeVersionStatusDeleted`, 

`NodeVersionStatusBanned`, 

`NodeVersionStatusPending`, 

`NodeVersionStatusFlagged`

​

include_status_reason

boolean

predeterminado:false

​

page

integer

predeterminado:1

The page number to retrieve.

​

pageSize

integer

predeterminado:10

The number of items to include per page.

​

status_reason

string

search for status_reason, case insensitive

#### Respuesta

200

application/json

List of all node versions

​

page

integer

Current page number

​

pageSize

integer

Maximum number of node versions per page. Maximum is 100.

​

total

integer

Total number of node versions available

​

totalPages

integer

Total number of pages available

​

versions

object[]

Show child attributes

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/registry/list-all-node-versions-given-some-filters.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/registry/list-all-node-versions-given-some-filters)

[Retrieve all publishers for a given user](https://docs.comfy.org/es/registry/api-reference/registry/retrieve-all-publishers-for-a-given-user)[Relight an image](https://docs.comfy.org/es/registry/api-reference/freepik/relight-an-image)

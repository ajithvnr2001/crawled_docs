---
url: https://docs.comfy.org/registry/api-reference/registry/list-all-node-versions-given-some-filters/
title: List all node versions given some filters. - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-27T13:04:07.571375+00:00
---

# List all node versions given some filters. - ComfyUI

> Source: https://docs.comfy.org/registry/api-reference/registry/list-all-node-versions-given-some-filters/

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

Registry API Reference

# List all node versions given some filters.

Copy pageCopy page

Copy pageCopy page

GET

/

versions

Try it

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

#### Query Parameters

​

nodeId

string

​

statuses

enum<string>[]

Available options: 

`NodeVersionStatusActive`, 

`NodeVersionStatusDeleted`, 

`NodeVersionStatusBanned`, 

`NodeVersionStatusPending`, 

`NodeVersionStatusFlagged`

​

include_status_reason

boolean

default:false

​

page

integer

default:1

The page number to retrieve.

​

pageSize

integer

default:10

The number of items to include per page.

​

status_reason

string

search for status_reason, case insensitive

#### Response

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

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/registry/api-reference/registry/list-all-node-versions-given-some-filters.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/registry/api-reference/registry/list-all-node-versions-given-some-filters)

[Retrieve multiple node versions in a single request](https://docs.comfy.org/registry/api-reference/registry/retrieve-multiple-node-versions-in-a-single-request)[list all comfy-nodes](https://docs.comfy.org/registry/api-reference/registry/list-all-comfy-nodes)

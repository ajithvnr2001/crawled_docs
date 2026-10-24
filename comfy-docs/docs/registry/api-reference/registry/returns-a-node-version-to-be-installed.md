---
url: https://docs.comfy.org/registry/api-reference/registry/returns-a-node-version-to-be-installed/
title: Returns a node version to be installed. - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-24T11:54:48.524281+00:00
---

# Returns a node version to be installed. - ComfyUI

> Source: https://docs.comfy.org/registry/api-reference/registry/returns-a-node-version-to-be-installed/

Returns a node version to be installed.

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/nodes/{nodeId}/install
    
    
    import requests
    
    url = "https://api.comfy.org/nodes/{nodeId}/install"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.comfy.org/nodes/{nodeId}/install', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/nodes/{nodeId}/install",
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
    
    	url := "https://api.comfy.org/nodes/{nodeId}/install"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/nodes/{nodeId}/install")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/nodes/{nodeId}/install")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

400

403

404

500
    
    
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
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

Registry API Reference

# Returns a node version to be installed.

Copy pageCopy page

Retrieves the node data for installation, either the latest or a specific version.

Copy pageCopy page

GET

/

nodes

/

{nodeId}

/

install

Try it

Returns a node version to be installed.

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/nodes/{nodeId}/install
    
    
    import requests
    
    url = "https://api.comfy.org/nodes/{nodeId}/install"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.comfy.org/nodes/{nodeId}/install', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/nodes/{nodeId}/install",
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
    
    	url := "https://api.comfy.org/nodes/{nodeId}/install"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/nodes/{nodeId}/install")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/nodes/{nodeId}/install")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

400

403

404

500
    
    
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
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

#### Path Parameters

​

nodeId

string

required

The unique identifier of the node.

#### Query Parameters

​

version

string

Specific version of the node to retrieve. If omitted, the latest version is returned.

Pattern: `^\d+\.\d+\.\d+$`

#### Response

200

application/json

Node data returned successfully.

​

changelog

string

Summary of changes made in this version

​

comfy_node_extract_status

string

The status of comfy node extraction process.

​

createdAt

string<date-time>

The date and time the version was created.

​

dependencies

string[]

A list of pip dependencies required by the node.

​

deprecated

boolean

Indicates if this version is deprecated.

​

downloadUrl

string

[Output Only] URL to download this version of the node

​

id

string

​

node_id

string

The unique identifier of the node.

​

status

enum<string>

Available options: 

`NodeVersionStatusActive`, 

`NodeVersionStatusDeleted`, 

`NodeVersionStatusBanned`, 

`NodeVersionStatusPending`, 

`NodeVersionStatusFlagged`

​

status_reason

string

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

Admin-only tags for security warnings and admin metadata. Read-only for publishers - omitted from all public responses and ignored if sent on publish; only returned on admin-authenticated responses.

​

version

string

The version identifier, following semantic versioning. Must be unique for the node.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/registry/api-reference/registry/returns-a-node-version-to-be-installed.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/registry/api-reference/registry/returns-a-node-version-to-be-installed)

[Retrieve a specific node by ID](https://docs.comfy.org/registry/api-reference/registry/retrieve-a-specific-node-by-id)[Add review to a specific version of a node](https://docs.comfy.org/registry/api-reference/registry/add-review-to-a-specific-version-of-a-node)

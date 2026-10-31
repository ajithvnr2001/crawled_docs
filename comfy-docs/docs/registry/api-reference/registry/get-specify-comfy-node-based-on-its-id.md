---
url: https://docs.comfy.org/registry/api-reference/registry/get-specify-comfy-node-based-on-its-id/
title: get specify comfy-node based on its id - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-31T13:26:49.643770+00:00
---

# get specify comfy-node based on its id - ComfyUI

> Source: https://docs.comfy.org/registry/api-reference/registry/get-specify-comfy-node-based-on-its-id/

get specify comfy-node based on its id

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes/{comfyNodeName}
    
    
    import requests
    
    url = "https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes/{comfyNodeName}"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes/{comfyNodeName}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes/{comfyNodeName}",
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
    
    	url := "https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes/{comfyNodeName}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes/{comfyNodeName}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes/{comfyNodeName}")
    
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
      "category": "<string>",
      "comfy_node_name": "<string>",
      "deprecated": true,
      "description": "<string>",
      "experimental": true,
      "function": "<string>",
      "input_types": "<string>",
      "output_is_list": [
        true
      ],
      "policy": "ComfyNodePolicyActive",
      "return_names": "<string>",
      "return_types": "<string>"
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

# get specify comfy-node based on its id

Copy pageCopy page

Copy pageCopy page

GET

/

nodes

/

{nodeId}

/

versions

/

{version}

/

comfy-nodes

/

{comfyNodeName}

Try it

get specify comfy-node based on its id

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes/{comfyNodeName}
    
    
    import requests
    
    url = "https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes/{comfyNodeName}"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes/{comfyNodeName}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes/{comfyNodeName}",
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
    
    	url := "https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes/{comfyNodeName}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes/{comfyNodeName}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes/{comfyNodeName}")
    
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
      "category": "<string>",
      "comfy_node_name": "<string>",
      "deprecated": true,
      "description": "<string>",
      "experimental": true,
      "function": "<string>",
      "input_types": "<string>",
      "output_is_list": [
        true
      ],
      "policy": "ComfyNodePolicyActive",
      "return_names": "<string>",
      "return_types": "<string>"
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

​

version

string

required

​

comfyNodeName

string

required

#### Response

200

application/json

Comy Nodes created successfully

​

category

string

UI category where the node is listed, used for grouping nodes.

​

comfy_node_name

string

Unique identifier for the node

​

deprecated

boolean

Indicates if the node is deprecated. Deprecated nodes are hidden in the UI.

​

description

string

Brief description of the node's functionality or purpose.

​

experimental

boolean

Indicates if the node is experimental, subject to changes or removal.

​

function

string

Name of the entry-point function to execute the node.

​

input_types

string

Defines input parameters

​

output_is_list

boolean[]

Boolean values indicating if each output is a list.

​

policy

enum<string>

Available options: 

`ComfyNodePolicyActive`, 

`ComfyNodePolicyBanned`, 

`ComfyNodePolicyLocalOnly`

​

return_names

string

Names of the outputs for clarity in workflows.

​

return_types

string

Specifies the types of outputs produced by the node.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/registry/api-reference/registry/get-specify-comfy-node-based-on-its-id.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/registry/api-reference/registry/get-specify-comfy-node-based-on-its-id)

[list comfy-nodes for node version](https://docs.comfy.org/registry/api-reference/registry/list-comfy-nodes-for-node-version)[Update a specific comfy-node](https://docs.comfy.org/registry/api-reference/registry/update-a-specific-comfy-node)

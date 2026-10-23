---
url: https://docs.comfy.org/registry/api-reference/registry/update-a-specific-comfy-node/
title: Update a specific comfy-node - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:22.994380+00:00
---

# Update a specific comfy-node - ComfyUI

> Source: https://docs.comfy.org/registry/api-reference/registry/update-a-specific-comfy-node/

Update a specific comfy-node

cURL
    
    
    curl --request PUT \
      --url https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes/{comfyNodeName} \
      --header 'Content-Type: application/json' \
      --data '
    {
      "category": "<string>",
      "deprecated": true,
      "description": "<string>",
      "experimental": true,
      "function": "<string>",
      "input_types": "<string>",
      "output_is_list": [
        true
      ],
      "return_names": "<string>",
      "return_types": "<string>"
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes/{comfyNodeName}"
    
    payload = {
        "category": "<string>",
        "deprecated": True,
        "description": "<string>",
        "experimental": True,
        "function": "<string>",
        "input_types": "<string>",
        "output_is_list": [True],
        "return_names": "<string>",
        "return_types": "<string>"
    }
    headers = {"Content-Type": "application/json"}
    
    response = requests.put(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'PUT',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        category: '<string>',
        deprecated: true,
        description: '<string>',
        experimental: true,
        function: '<string>',
        input_types: '<string>',
        output_is_list: [true],
        return_names: '<string>',
        return_types: '<string>'
      })
    };
    
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
      CURLOPT_CUSTOMREQUEST => "PUT",
      CURLOPT_POSTFIELDS => json_encode([
        'category' => '<string>',
        'deprecated' => true,
        'description' => '<string>',
        'experimental' => true,
        'function' => '<string>',
        'input_types' => '<string>',
        'output_is_list' => [
            true
        ],
        'return_names' => '<string>',
        'return_types' => '<string>'
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
    
    	url := "https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes/{comfyNodeName}"
    
    	payload := strings.NewReader("{\n  \"category\": \"<string>\",\n  \"deprecated\": true,\n  \"description\": \"<string>\",\n  \"experimental\": true,\n  \"function\": \"<string>\",\n  \"input_types\": \"<string>\",\n  \"output_is_list\": [\n    true\n  ],\n  \"return_names\": \"<string>\",\n  \"return_types\": \"<string>\"\n}")
    
    	req, _ := http.NewRequest("PUT", url, payload)
    
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.put("https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes/{comfyNodeName}")
      .header("Content-Type", "application/json")
      .body("{\n  \"category\": \"<string>\",\n  \"deprecated\": true,\n  \"description\": \"<string>\",\n  \"experimental\": true,\n  \"function\": \"<string>\",\n  \"input_types\": \"<string>\",\n  \"output_is_list\": [\n    true\n  ],\n  \"return_names\": \"<string>\",\n  \"return_types\": \"<string>\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes/{comfyNodeName}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Put.new(url)
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"category\": \"<string>\",\n  \"deprecated\": true,\n  \"description\": \"<string>\",\n  \"experimental\": true,\n  \"function\": \"<string>\",\n  \"input_types\": \"<string>\",\n  \"output_is_list\": [\n    true\n  ],\n  \"return_names\": \"<string>\",\n  \"return_types\": \"<string>\"\n}"
    
    response = http.request(request)
    puts response.read_body

200

400

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
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

Registry API Reference

# Update a specific comfy-node

Copy pageCopy page

Copy pageCopy page

PUT

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

Update a specific comfy-node

cURL
    
    
    curl --request PUT \
      --url https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes/{comfyNodeName} \
      --header 'Content-Type: application/json' \
      --data '
    {
      "category": "<string>",
      "deprecated": true,
      "description": "<string>",
      "experimental": true,
      "function": "<string>",
      "input_types": "<string>",
      "output_is_list": [
        true
      ],
      "return_names": "<string>",
      "return_types": "<string>"
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes/{comfyNodeName}"
    
    payload = {
        "category": "<string>",
        "deprecated": True,
        "description": "<string>",
        "experimental": True,
        "function": "<string>",
        "input_types": "<string>",
        "output_is_list": [True],
        "return_names": "<string>",
        "return_types": "<string>"
    }
    headers = {"Content-Type": "application/json"}
    
    response = requests.put(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'PUT',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        category: '<string>',
        deprecated: true,
        description: '<string>',
        experimental: true,
        function: '<string>',
        input_types: '<string>',
        output_is_list: [true],
        return_names: '<string>',
        return_types: '<string>'
      })
    };
    
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
      CURLOPT_CUSTOMREQUEST => "PUT",
      CURLOPT_POSTFIELDS => json_encode([
        'category' => '<string>',
        'deprecated' => true,
        'description' => '<string>',
        'experimental' => true,
        'function' => '<string>',
        'input_types' => '<string>',
        'output_is_list' => [
            true
        ],
        'return_names' => '<string>',
        'return_types' => '<string>'
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
    
    	url := "https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes/{comfyNodeName}"
    
    	payload := strings.NewReader("{\n  \"category\": \"<string>\",\n  \"deprecated\": true,\n  \"description\": \"<string>\",\n  \"experimental\": true,\n  \"function\": \"<string>\",\n  \"input_types\": \"<string>\",\n  \"output_is_list\": [\n    true\n  ],\n  \"return_names\": \"<string>\",\n  \"return_types\": \"<string>\"\n}")
    
    	req, _ := http.NewRequest("PUT", url, payload)
    
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.put("https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes/{comfyNodeName}")
      .header("Content-Type", "application/json")
      .body("{\n  \"category\": \"<string>\",\n  \"deprecated\": true,\n  \"description\": \"<string>\",\n  \"experimental\": true,\n  \"function\": \"<string>\",\n  \"input_types\": \"<string>\",\n  \"output_is_list\": [\n    true\n  ],\n  \"return_names\": \"<string>\",\n  \"return_types\": \"<string>\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes/{comfyNodeName}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Put.new(url)
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"category\": \"<string>\",\n  \"deprecated\": true,\n  \"description\": \"<string>\",\n  \"experimental\": true,\n  \"function\": \"<string>\",\n  \"input_types\": \"<string>\",\n  \"output_is_list\": [\n    true\n  ],\n  \"return_names\": \"<string>\",\n  \"return_types\": \"<string>\"\n}"
    
    response = http.request(request)
    puts response.read_body

200

400

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

#### Body

application/json

​

category

string

UI category where the node is listed, used for grouping nodes.

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

#### Response

200

application/json

Comfy Node updated successfully

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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/registry/api-reference/registry/update-a-specific-comfy-node.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/registry/api-reference/registry/update-a-specific-comfy-node)

[get specify comfy-node based on its idPrevious](https://docs.comfy.org/registry/api-reference/registry/get-specify-comfy-node-based-on-its-id)[Get server feature flagsNext](https://docs.comfy.org/registry/api-reference/registry/get-server-feature-flags)

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

---
url: https://docs.comfy.org/registry/api-reference/registry/create-comfy-nodes-for-certain-node/
title: create comfy-nodes for certain node - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:22.917796+00:00
---

# create comfy-nodes for certain node - ComfyUI

> Source: https://docs.comfy.org/registry/api-reference/registry/create-comfy-nodes-for-certain-node/

create comfy-nodes for certain node

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes \
      --header 'Content-Type: application/json' \
      --data '
    {
      "cloud_build_info": {
        "build_id": "<string>",
        "location": "<string>",
        "project_id": "<string>",
        "project_number": "<string>"
      },
      "nodes": {},
      "reason": "<string>",
      "status": "<string>",
      "success": true
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes"
    
    payload = {
        "cloud_build_info": {
            "build_id": "<string>",
            "location": "<string>",
            "project_id": "<string>",
            "project_number": "<string>"
        },
        "nodes": {},
        "reason": "<string>",
        "status": "<string>",
        "success": True
    }
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        cloud_build_info: {
          build_id: '<string>',
          location: '<string>',
          project_id: '<string>',
          project_number: '<string>'
        },
        nodes: {},
        reason: '<string>',
        status: '<string>',
        success: true
      })
    };
    
    fetch('https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'cloud_build_info' => [
            'build_id' => '<string>',
            'location' => '<string>',
            'project_id' => '<string>',
            'project_number' => '<string>'
        ],
        'nodes' => [
            
        ],
        'reason' => '<string>',
        'status' => '<string>',
        'success' => true
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
    
    	url := "https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes"
    
    	payload := strings.NewReader("{\n  \"cloud_build_info\": {\n    \"build_id\": \"<string>\",\n    \"location\": \"<string>\",\n    \"project_id\": \"<string>\",\n    \"project_number\": \"<string>\"\n  },\n  \"nodes\": {},\n  \"reason\": \"<string>\",\n  \"status\": \"<string>\",\n  \"success\": true\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes")
      .header("Content-Type", "application/json")
      .body("{\n  \"cloud_build_info\": {\n    \"build_id\": \"<string>\",\n    \"location\": \"<string>\",\n    \"project_id\": \"<string>\",\n    \"project_number\": \"<string>\"\n  },\n  \"nodes\": {},\n  \"reason\": \"<string>\",\n  \"status\": \"<string>\",\n  \"success\": true\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"cloud_build_info\": {\n    \"build_id\": \"<string>\",\n    \"location\": \"<string>\",\n    \"project_id\": \"<string>\",\n    \"project_number\": \"<string>\"\n  },\n  \"nodes\": {},\n  \"reason\": \"<string>\",\n  \"status\": \"<string>\",\n  \"success\": true\n}"
    
    response = http.request(request)
    puts response.read_body

403

404

409

500
    
    
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

# create comfy-nodes for certain node

Copy pageCopy page

Copy pageCopy page

POST

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

Try it

create comfy-nodes for certain node

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes \
      --header 'Content-Type: application/json' \
      --data '
    {
      "cloud_build_info": {
        "build_id": "<string>",
        "location": "<string>",
        "project_id": "<string>",
        "project_number": "<string>"
      },
      "nodes": {},
      "reason": "<string>",
      "status": "<string>",
      "success": true
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes"
    
    payload = {
        "cloud_build_info": {
            "build_id": "<string>",
            "location": "<string>",
            "project_id": "<string>",
            "project_number": "<string>"
        },
        "nodes": {},
        "reason": "<string>",
        "status": "<string>",
        "success": True
    }
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        cloud_build_info: {
          build_id: '<string>',
          location: '<string>',
          project_id: '<string>',
          project_number: '<string>'
        },
        nodes: {},
        reason: '<string>',
        status: '<string>',
        success: true
      })
    };
    
    fetch('https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'cloud_build_info' => [
            'build_id' => '<string>',
            'location' => '<string>',
            'project_id' => '<string>',
            'project_number' => '<string>'
        ],
        'nodes' => [
            
        ],
        'reason' => '<string>',
        'status' => '<string>',
        'success' => true
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
    
    	url := "https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes"
    
    	payload := strings.NewReader("{\n  \"cloud_build_info\": {\n    \"build_id\": \"<string>\",\n    \"location\": \"<string>\",\n    \"project_id\": \"<string>\",\n    \"project_number\": \"<string>\"\n  },\n  \"nodes\": {},\n  \"reason\": \"<string>\",\n  \"status\": \"<string>\",\n  \"success\": true\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes")
      .header("Content-Type", "application/json")
      .body("{\n  \"cloud_build_info\": {\n    \"build_id\": \"<string>\",\n    \"location\": \"<string>\",\n    \"project_id\": \"<string>\",\n    \"project_number\": \"<string>\"\n  },\n  \"nodes\": {},\n  \"reason\": \"<string>\",\n  \"status\": \"<string>\",\n  \"success\": true\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"cloud_build_info\": {\n    \"build_id\": \"<string>\",\n    \"location\": \"<string>\",\n    \"project_id\": \"<string>\",\n    \"project_number\": \"<string>\"\n  },\n  \"nodes\": {},\n  \"reason\": \"<string>\",\n  \"status\": \"<string>\",\n  \"success\": true\n}"
    
    response = http.request(request)
    puts response.read_body

403

404

409

500
    
    
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

#### Body

application/json

​

cloud_build_info

object

Show child attributes

​

nodes

object

Show child attributes

​

reason

string

​

status

string

​

success

boolean

#### Response

204

Comy Nodes created successfully

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/registry/api-reference/registry/create-comfy-nodes-for-certain-node.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/registry/api-reference/registry/create-comfy-nodes-for-certain-node)

[Retrieve a node by ComfyUI node namePrevious](https://docs.comfy.org/registry/api-reference/registry/retrieve-a-node-by-comfyui-node-name)[list comfy-nodes for node versionNext](https://docs.comfy.org/registry/api-reference/registry/list-comfy-nodes-for-node-version)

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

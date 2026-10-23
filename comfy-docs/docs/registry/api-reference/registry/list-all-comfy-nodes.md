---
url: https://docs.comfy.org/registry/api-reference/registry/list-all-comfy-nodes/
title: list all comfy-nodes - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:23.053293+00:00
---

# list all comfy-nodes - ComfyUI

> Source: https://docs.comfy.org/registry/api-reference/registry/list-all-comfy-nodes/

list all comfy-nodes

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/comfy-nodes
    
    
    import requests
    
    url = "https://api.comfy.org/comfy-nodes"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.comfy.org/comfy-nodes', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/comfy-nodes",
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
    
    	url := "https://api.comfy.org/comfy-nodes"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/comfy-nodes")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/comfy-nodes")
    
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
      "comfy_nodes": [
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
      ],
      "page_size": 123,
      "total": 123
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

# list all comfy-nodes

Copy pageCopy page

Copy pageCopy page

GET

/

comfy-nodes

Try it

list all comfy-nodes

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/comfy-nodes
    
    
    import requests
    
    url = "https://api.comfy.org/comfy-nodes"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.comfy.org/comfy-nodes', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/comfy-nodes",
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
    
    	url := "https://api.comfy.org/comfy-nodes"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/comfy-nodes")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/comfy-nodes")
    
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
      "comfy_nodes": [
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
      ],
      "page_size": 123,
      "total": 123
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

pageSize

integer

default:100

The number of items to include per page. A value above the maximum is clamped down to it; 0 and negative values are accepted and select the default. (That is why no minimum is declared — sub-1 is meaningful here, not invalid.) The page size actually served is echoed back as page_size, so a clamp is always detectable.

Required range: `x <= 100`

​

page

integer

default:1

Page number (1-based indexing)

​

node_id

string

Filter by node ID

​

node_version

string

Filter by node version

​

comfy_node_name

string

Filter by ComfyUI node name

#### Response

200

application/json

OK

​

comfy_nodes

object[]

Show child attributes

​

page_size

integer

The page size actually served. The server clamps pageSize to the documented maximum, so this can be smaller than the requested value; paginate with this number rather than the one you asked for, or you will skip rows.

​

total

integer

Total number of comfy nodes

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/registry/api-reference/registry/list-all-comfy-nodes.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/registry/api-reference/registry/list-all-comfy-nodes)

[List all node versions given some filters.Previous](https://docs.comfy.org/registry/api-reference/registry/list-all-node-versions-given-some-filters)[Retrieve a node by ComfyUI node nameNext](https://docs.comfy.org/registry/api-reference/registry/retrieve-a-node-by-comfyui-node-name)

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

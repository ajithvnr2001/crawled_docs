---
url: https://docs.comfy.org/es/registry/api-reference/registry/list-all-comfy-nodes/
title: list all comfy-nodes - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-27T13:04:05.248027+00:00
---

# list all comfy-nodes - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/registry/list-all-comfy-nodes/

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

Registry

# list all comfy-nodes

Copiar páginaCopiar página

Copiar páginaCopiar página

GET

/

comfy-nodes

Pruébalo

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

#### Parámetros de consulta

​

pageSize

integer

predeterminado:100

The number of items to include per page. A value above the maximum is clamped down to it; 0 and negative values are accepted and select the default. (That is why no minimum is declared — sub-1 is meaningful here, not invalid.) The page size actually served is echoed back as page_size, so a clamp is always detectable.

Rango requerido: `x <= 100`

​

page

integer

predeterminado:1

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

#### Respuesta

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

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/registry/list-all-comfy-nodes.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/registry/list-all-comfy-nodes)

[Retrieve multiple node versions in a single request](https://docs.comfy.org/es/registry/api-reference/registry/retrieve-multiple-node-versions-in-a-single-request)[Retrieve a node by ComfyUI node name](https://docs.comfy.org/es/registry/api-reference/registry/retrieve-a-node-by-comfyui-node-name)

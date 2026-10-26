---
url: https://docs.comfy.org/es/registry/api-reference/registry/list-comfy-nodes-for-node-version/
title: list comfy-nodes for node version - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:35.951883+00:00
---

# list comfy-nodes for node version - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/registry/list-comfy-nodes-for-node-version/

list comfy-nodes for node version

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes
    
    
    import requests
    
    url = "https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
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
    
    	url := "https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes")
    
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
      "totalNumberOfPages": 123
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

# list comfy-nodes for node version

Copiar páginaCopiar página

Copiar páginaCopiar página

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

Pruébalo

list comfy-nodes for node version

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes
    
    
    import requests
    
    url = "https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
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
    
    	url := "https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/nodes/{nodeId}/versions/{version}/comfy-nodes")
    
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
      "totalNumberOfPages": 123
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

#### Parámetros de ruta

​

nodeId

string

requerido

​

version

string

requerido

#### Parámetros de consulta

​

page

integer

predeterminado:1

The page number to retrieve.

​

limit

integer

predeterminado:10

The number of items to include per page. A value above the maximum is clamped down to it; 0 and negative values are accepted and select the default. (That is why no minimum is declared — sub-1 is meaningful here, not invalid.) totalNumberOfPages is computed from the page size actually served, so a clamp is always detectable.

Rango requerido: `x <= 8192`

#### Respuesta

200

application/json

Comy Nodes obtained successfully

​

comfy_nodes

object[]

Show child attributes

​

totalNumberOfPages

integer

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/registry/list-comfy-nodes-for-node-version.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/registry/list-comfy-nodes-for-node-version)

[Retrieve a specific version of a node](https://docs.comfy.org/es/registry/api-reference/registry/retrieve-a-specific-version-of-a-node)[create comfy-nodes for certain node](https://docs.comfy.org/es/registry/api-reference/registry/create-comfy-nodes-for-certain-node)

---
url: https://docs.comfy.org/es/api-reference/cloud/workflow/get-a-specific-subgraph-blueprint/
title: Get a specific subgraph blueprint - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:26.600048+00:00
---

# Get a specific subgraph blueprint - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/workflow/get-a-specific-subgraph-blueprint/

Get a specific subgraph blueprint

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/global_subgraphs/{id}
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/global_subgraphs/{id}"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://cloud.comfy.org/api/global_subgraphs/{id}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/global_subgraphs/{id}",
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
    
    	url := "https://cloud.comfy.org/api/global_subgraphs/{id}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/global_subgraphs/{id}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/global_subgraphs/{id}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

404

500
    
    
    {
      "source": "<string>",
      "name": "<string>",
      "info": {
        "node_pack": "<string>"
      },
      "data": "<string>"
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }

workflow

# Get a specific subgraph blueprint

Copiar páginaCopiar página

Returns the full data for a specific subgraph blueprint by ID

Copiar páginaCopiar página

GET

/

api

/

global_subgraphs

/

{id}

Pruébalo

Get a specific subgraph blueprint

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/global_subgraphs/{id}
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/global_subgraphs/{id}"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://cloud.comfy.org/api/global_subgraphs/{id}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/global_subgraphs/{id}",
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
    
    	url := "https://cloud.comfy.org/api/global_subgraphs/{id}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/global_subgraphs/{id}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/global_subgraphs/{id}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

404

500
    
    
    {
      "source": "<string>",
      "name": "<string>",
      "info": {
        "node_pack": "<string>"
      },
      "data": "<string>"
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }

#### Parámetros de ruta

​

id

string

requerido

The unique identifier of the subgraph blueprint

#### Respuesta

200

application/json

Success - Full subgraph data

Full data for a global subgraph blueprint

​

source

string

requerido

Source type of the subgraph - "templates" for workflow templates or "custom_node" for custom node subgraphs

​

name

string

requerido

Display name of the subgraph blueprint

​

info

object

requerido

Additional information about the subgraph

Show child attributes

​

data

string

requerido

The full subgraph JSON data as a string

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/workflow/get-a-specific-subgraph-blueprint.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/workflow/get-a-specific-subgraph-blueprint)

[Get available subgraph blueprints](https://docs.comfy.org/es/api-reference/cloud/workflow/get-available-subgraph-blueprints)[Get all node information](https://docs.comfy.org/es/api-reference/cloud/node/get-all-node-information)

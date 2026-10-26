---
url: https://docs.comfy.org/es/api-reference/cloud/workflow/get-available-subgraph-blueprints/
title: Get available subgraph blueprints - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:26.525300+00:00
---

# Get available subgraph blueprints - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/workflow/get-available-subgraph-blueprints/

Get available subgraph blueprints

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/global_subgraphs
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/global_subgraphs"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://cloud.comfy.org/api/global_subgraphs', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/global_subgraphs",
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
    
    	url := "https://cloud.comfy.org/api/global_subgraphs"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/global_subgraphs")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/global_subgraphs")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

500
    
    
    {}
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }

workflow

# Get available subgraph blueprints

Copiar páginaCopiar página

Returns a list of globally available subgraph blueprints. These are pre-built workflow components that can be used as nodes. The data field contains a promise that resolves to the full subgraph JSON.

Copiar páginaCopiar página

GET

/

api

/

global_subgraphs

Pruébalo

Get available subgraph blueprints

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/global_subgraphs
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/global_subgraphs"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://cloud.comfy.org/api/global_subgraphs', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/global_subgraphs",
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
    
    	url := "https://cloud.comfy.org/api/global_subgraphs"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/global_subgraphs")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/global_subgraphs")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

500
    
    
    {}
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }

#### Respuesta

200

application/json

Success - Map of subgraph IDs to their metadata

​

{key}

object

Metadata for a global subgraph blueprint (without full data)

Show child attributes

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/workflow/get-available-subgraph-blueprints.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/workflow/get-available-subgraph-blueprints)

[Get available workflow templates](https://docs.comfy.org/es/api-reference/cloud/workflow/get-available-workflow-templates)[Get a specific subgraph blueprint](https://docs.comfy.org/es/api-reference/cloud/workflow/get-a-specific-subgraph-blueprint)

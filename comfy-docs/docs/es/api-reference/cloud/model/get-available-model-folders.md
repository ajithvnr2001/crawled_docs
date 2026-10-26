---
url: https://docs.comfy.org/es/api-reference/cloud/model/get-available-model-folders/
title: Get available model folders - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:25.755890+00:00
---

# Get available model folders - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/model/get-available-model-folders/

Get available model folders

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/experiment/models
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/experiment/models"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://cloud.comfy.org/api/experiment/models', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/experiment/models",
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
    
    	url := "https://cloud.comfy.org/api/experiment/models"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/experiment/models")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/experiment/models")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

500
    
    
    [
      {
        "name": "checkpoints",
        "folders": [
          "checkpoints"
        ]
      }
    ]
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }

model

# Get available model folders

Copiar páginaCopiar página

Returns a list of model folders available in the system. This is an experimental endpoint that replaces the legacy /models endpoint.

Copiar páginaCopiar página

GET

/

api

/

experiment

/

models

Pruébalo

Get available model folders

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/experiment/models
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/experiment/models"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://cloud.comfy.org/api/experiment/models', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/experiment/models",
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
    
    	url := "https://cloud.comfy.org/api/experiment/models"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/experiment/models")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/experiment/models")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

500
    
    
    [
      {
        "name": "checkpoints",
        "folders": [
          "checkpoints"
        ]
      }
    ]
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }

#### Respuesta

200

application/json

Success - List of model folders

​

name

string

requerido

The name of the model folder

Ejemplo:

`"checkpoints"`

​

folders

string[]

requerido

List of paths where models of this type are stored

Ejemplo:
    
    
    ["checkpoints"]

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/model/get-available-model-folders.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/model/get-available-model-folders)

[Get server feature flags](https://docs.comfy.org/es/api-reference/cloud/node/get-server-feature-flags)[Get models in a specific folder](https://docs.comfy.org/es/api-reference/cloud/model/get-models-in-a-specific-folder)

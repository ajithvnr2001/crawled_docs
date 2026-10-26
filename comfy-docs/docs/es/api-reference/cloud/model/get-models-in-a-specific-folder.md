---
url: https://docs.comfy.org/es/api-reference/cloud/model/get-models-in-a-specific-folder/
title: Get models in a specific folder - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:25.599552+00:00
---

# Get models in a specific folder - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/model/get-models-in-a-specific-folder/

Get models in a specific folder

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/experiment/models/{folder}
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/experiment/models/{folder}"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://cloud.comfy.org/api/experiment/models/{folder}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/experiment/models/{folder}",
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
    
    	url := "https://cloud.comfy.org/api/experiment/models/{folder}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/experiment/models/{folder}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/experiment/models/{folder}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

404

500
    
    
    [
      {
        "name": "model.safetensors",
        "pathIndex": 0
      }
    ]
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }

model

# Get models in a specific folder

Copiar páginaCopiar página

Returns a list of models available in the specified folder. This is an experimental endpoint that provides enhanced model information.

Copiar páginaCopiar página

GET

/

api

/

experiment

/

models

/

{folder}

Pruébalo

Get models in a specific folder

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/experiment/models/{folder}
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/experiment/models/{folder}"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://cloud.comfy.org/api/experiment/models/{folder}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/experiment/models/{folder}",
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
    
    	url := "https://cloud.comfy.org/api/experiment/models/{folder}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/experiment/models/{folder}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/experiment/models/{folder}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

404

500
    
    
    [
      {
        "name": "model.safetensors",
        "pathIndex": 0
      }
    ]
    
    
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

folder

string

requerido

The folder name to list models from

Ejemplo:

`"checkpoints"`

#### Respuesta

200

application/json

Success - List of models in the folder

​

name

string

requerido

The filename of the model

Ejemplo:

`"model.safetensors"`

​

pathIndex

integer

requerido

Index of the path where this model is located

Ejemplo:

`0`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/model/get-models-in-a-specific-folder.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/model/get-models-in-a-specific-folder)

[Get available model folders](https://docs.comfy.org/es/api-reference/cloud/model/get-available-model-folders)[Get model preview image](https://docs.comfy.org/es/api-reference/cloud/model/get-model-preview-image)

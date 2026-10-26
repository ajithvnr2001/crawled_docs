---
url: https://docs.comfy.org/es/api-reference/cloud/model/get-model-preview-image/
title: Get model preview image - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:25.450933+00:00
---

# Get model preview image - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/model/get-model-preview-image/

Get model preview image

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/experiment/models/preview/{folder}/{path_index}/{filename}
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/experiment/models/preview/{folder}/{path_index}/{filename}"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://cloud.comfy.org/api/experiment/models/preview/{folder}/{path_index}/{filename}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/experiment/models/preview/{folder}/{path_index}/{filename}",
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
    
    	url := "https://cloud.comfy.org/api/experiment/models/preview/{folder}/{path_index}/{filename}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/experiment/models/preview/{folder}/{path_index}/{filename}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/experiment/models/preview/{folder}/{path_index}/{filename}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

404

500
    
    
    "<string>"
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }

model

# Get model preview image

Copiar páginaCopiar página

Returns a preview image for the specified model. The image is returned in WebP format for optimal performance.

Copiar páginaCopiar página

GET

/

api

/

experiment

/

models

/

preview

/

{folder}

/

{path_index}

/

{filename}

Pruébalo

Get model preview image

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/experiment/models/preview/{folder}/{path_index}/{filename}
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/experiment/models/preview/{folder}/{path_index}/{filename}"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://cloud.comfy.org/api/experiment/models/preview/{folder}/{path_index}/{filename}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/experiment/models/preview/{folder}/{path_index}/{filename}",
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
    
    	url := "https://cloud.comfy.org/api/experiment/models/preview/{folder}/{path_index}/{filename}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/experiment/models/preview/{folder}/{path_index}/{filename}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/experiment/models/preview/{folder}/{path_index}/{filename}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

404

500
    
    
    "<string>"
    
    
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

The folder name containing the model

Ejemplo:

`"checkpoints"`

​

path_index

integer

requerido

The path index (usually 0 for cloud service)

Ejemplo:

`0`

​

filename

string

requerido

The model filename (with or without .webp extension)

Ejemplo:

`"model.safetensors"`

#### Respuesta

200

image/webp

Success - Model preview image

The response is of type `file`.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/model/get-model-preview-image.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/model/get-model-preview-image)

[Get models in a specific folder](https://docs.comfy.org/es/api-reference/cloud/model/get-models-in-a-specific-folder)[Manage execution history](https://docs.comfy.org/es/api-reference/cloud/job/manage-execution-history)

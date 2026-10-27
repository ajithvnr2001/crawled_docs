---
url: https://docs.comfy.org/es/registry/api-reference/api-nodes/get-proxyvidutasks-creations/
title: Get proxyvidutasks creations - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-27T13:04:03.120574+00:00
---

# Get proxyvidutasks creations - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/api-nodes/get-proxyvidutasks-creations/

cURL

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/proxy/vidu/tasks/{id}/creations \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.comfy.org/proxy/vidu/tasks/{id}/creations"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.comfy.org/proxy/vidu/tasks/{id}/creations', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/proxy/vidu/tasks/{id}/creations",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "GET",
      CURLOPT_HTTPHEADER => [
        "Authorization: Bearer <token>"
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
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "https://api.comfy.org/proxy/vidu/tasks/{id}/creations"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/proxy/vidu/tasks/{id}/creations")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/proxy/vidu/tasks/{id}/creations")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

200

400

default
    
    
    {
      "creations": [
        {
          "cover_url": "<string>",
          "id": "<string>",
          "moderation_url": [
            "<string>"
          ],
          "url": "<string>",
          "watermarked_url": "<string>"
        }
      ],
      "err_code": "<string>",
      "id": "<string>",
      "state": "created"
    }
    
    
    {
      "details": [
        "<string>"
      ],
      "message": "<string>"
    }
    
    
    {
      "details": [
        "<string>"
      ],
      "message": "<string>"
    }

API Nodes

# Get proxyvidutasks creations

Copiar páginaCopiar página

Copiar páginaCopiar página

GET

/

proxy

/

vidu

/

tasks

/

{id}

/

creations

Pruébalo

cURL

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/proxy/vidu/tasks/{id}/creations \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.comfy.org/proxy/vidu/tasks/{id}/creations"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.comfy.org/proxy/vidu/tasks/{id}/creations', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/proxy/vidu/tasks/{id}/creations",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "GET",
      CURLOPT_HTTPHEADER => [
        "Authorization: Bearer <token>"
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
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "https://api.comfy.org/proxy/vidu/tasks/{id}/creations"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/proxy/vidu/tasks/{id}/creations")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/proxy/vidu/tasks/{id}/creations")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

200

400

default
    
    
    {
      "creations": [
        {
          "cover_url": "<string>",
          "id": "<string>",
          "moderation_url": [
            "<string>"
          ],
          "url": "<string>",
          "watermarked_url": "<string>"
        }
      ],
      "err_code": "<string>",
      "id": "<string>",
      "state": "created"
    }
    
    
    {
      "details": [
        "<string>"
      ],
      "message": "<string>"
    }
    
    
    {
      "details": [
        "<string>"
      ],
      "message": "<string>"
    }

#### Autorizaciones

BearerAuthApiKeyAuthBearerAuthApiKeyAuth

​

Authorization

string

header

requerido

Bearer token authentication. Normally a Firebase or Cloud JWT. A 'comfyui-' prefixed API key is also accepted in this header: the prefix classifies the value as an API key and it is validated exactly as if it had been sent in X-API-Key. Accepted on the operations served by the comfyFirebase auth middleware (BE-9720, parity with ingest).

#### Parámetros de ruta

​

id

string

requerido

#### Respuesta

200

application/json

OK

​

creations

object[]

Show child attributes

​

err_code

string

​

id

string

​

state

enum<string>

Opciones disponibles: 

`created`, 

`processing`, 

`queueing`, 

`success`, 

`failed`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/api-nodes/get-proxyvidutasks-creations.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/api-nodes/get-proxyvidutasks-creations)

[Post proxyvidustart end2video](https://docs.comfy.org/es/registry/api-reference/api-nodes/post-proxyvidustart-end2video)[Post proxyvidutext2video](https://docs.comfy.org/es/registry/api-reference/api-nodes/post-proxyvidutext2video)

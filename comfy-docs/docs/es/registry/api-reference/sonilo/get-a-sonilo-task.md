---
url: https://docs.comfy.org/es/registry/api-reference/sonilo/get-a-sonilo-task/
title: Get a Sonilo task - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-31T13:26:43.171012+00:00
---

# Get a Sonilo task - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/sonilo/get-a-sonilo-task/

Get a Sonilo task

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/proxy/sonilo/v1/tasks/{task_id} \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.comfy.org/proxy/sonilo/v1/tasks/{task_id}"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.comfy.org/proxy/sonilo/v1/tasks/{task_id}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/proxy/sonilo/v1/tasks/{task_id}",
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
    
    	url := "https://api.comfy.org/proxy/sonilo/v1/tasks/{task_id}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/proxy/sonilo/v1/tasks/{task_id}")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/proxy/sonilo/v1/tasks/{task_id}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

200

401

404

429
    
    
    {
      "status": "<string>",
      "task_id": "<string>",
      "audio": {
        "content_type": "<string>",
        "duration_seconds": 123,
        "file_size": 123,
        "url": "<string>"
      },
      "cost": {
        "billing_after_discount": "<string>",
        "billing_before_discount": "<string>",
        "billing_rate_per_sec": "<string>",
        "discount_factor": "<string>"
      },
      "duration_seconds": 123,
      "error": {
        "code": "<string>",
        "message": "<string>"
      },
      "refunded": true,
      "type": "<string>"
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }

Sonilo

# Get a Sonilo task

Copiar páginaCopiar página

Get the status of a Sonilo async task. Poll every 2 to 5 seconds until the status is `succeeded` or `failed`. A succeeded music task carries `duration_seconds`, an `audio` object with a temporary download URL and a `cost` object.

Copiar páginaCopiar página

GET

/

proxy

/

sonilo

/

v1

/

tasks

/

{task_id}

Pruébalo

Get a Sonilo task

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/proxy/sonilo/v1/tasks/{task_id} \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.comfy.org/proxy/sonilo/v1/tasks/{task_id}"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.comfy.org/proxy/sonilo/v1/tasks/{task_id}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/proxy/sonilo/v1/tasks/{task_id}",
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
    
    	url := "https://api.comfy.org/proxy/sonilo/v1/tasks/{task_id}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/proxy/sonilo/v1/tasks/{task_id}")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/proxy/sonilo/v1/tasks/{task_id}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

200

401

404

429
    
    
    {
      "status": "<string>",
      "task_id": "<string>",
      "audio": {
        "content_type": "<string>",
        "duration_seconds": 123,
        "file_size": 123,
        "url": "<string>"
      },
      "cost": {
        "billing_after_discount": "<string>",
        "billing_before_discount": "<string>",
        "billing_rate_per_sec": "<string>",
        "discount_factor": "<string>"
      },
      "duration_seconds": 123,
      "error": {
        "code": "<string>",
        "message": "<string>"
      },
      "refunded": true,
      "type": "<string>"
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }
    
    
    {
      "code": "<string>",
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

task_id

string

requerido

The task_id returned by the submit request.

#### Respuesta

200

application/json

OK

​

status

string

requerido

One of processing, succeeded or failed.

​

task_id

string

requerido

​

audio

object

Show child attributes

​

cost

object

What Sonilo charged for the task. Present when the task succeeded.

Show child attributes

​

duration_seconds

number<double>

Length of the generated audio in seconds. Present when the task succeeded.

​

error

object

Present when the task failed.

Show child attributes

​

refunded

boolean

Present when the task failed. Whether Sonilo reversed the charge.

​

type

string

The task type.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/sonilo/get-a-sonilo-task.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/sonilo/get-a-sonilo-task)

[Generate music from text prompt](https://docs.comfy.org/es/registry/api-reference/sonilo/generate-music-from-text-prompt)[Generate a song with lyrics from a text prompt](https://docs.comfy.org/es/registry/api-reference/sonilo/generate-a-song-with-lyrics-from-a-text-prompt)

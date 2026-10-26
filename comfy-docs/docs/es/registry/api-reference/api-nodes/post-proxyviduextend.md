---
url: https://docs.comfy.org/es/registry/api-reference/api-nodes/post-proxyviduextend/
title: Post proxyviduextend - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:30.862240+00:00
---

# Post proxyviduextend - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/api-nodes/post-proxyviduextend/

cURL

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/proxy/vidu/extend \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "model": "<string>",
      "callback_url": "<string>",
      "duration": 123,
      "images": [
        "<string>"
      ],
      "payload": "<string>",
      "prompt": "<string>",
      "resolution": "<string>",
      "video_creation_id": "<string>",
      "video_url": "<string>"
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/proxy/vidu/extend"
    
    payload = {
        "model": "<string>",
        "callback_url": "<string>",
        "duration": 123,
        "images": ["<string>"],
        "payload": "<string>",
        "prompt": "<string>",
        "resolution": "<string>",
        "video_creation_id": "<string>",
        "video_url": "<string>"
    }
    headers = {
        "Authorization": "Bearer <token>",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'POST',
      headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
      body: JSON.stringify({
        model: '<string>',
        callback_url: '<string>',
        duration: 123,
        images: ['<string>'],
        payload: '<string>',
        prompt: '<string>',
        resolution: '<string>',
        video_creation_id: '<string>',
        video_url: '<string>'
      })
    };
    
    fetch('https://api.comfy.org/proxy/vidu/extend', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/proxy/vidu/extend",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'model' => '<string>',
        'callback_url' => '<string>',
        'duration' => 123,
        'images' => [
            '<string>'
        ],
        'payload' => '<string>',
        'prompt' => '<string>',
        'resolution' => '<string>',
        'video_creation_id' => '<string>',
        'video_url' => '<string>'
      ]),
      CURLOPT_HTTPHEADER => [
        "Authorization: Bearer <token>",
        "Content-Type: application/json"
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
    	"strings"
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "https://api.comfy.org/proxy/vidu/extend"
    
    	payload := strings.NewReader("{\n  \"model\": \"<string>\",\n  \"callback_url\": \"<string>\",\n  \"duration\": 123,\n  \"images\": [\n    \"<string>\"\n  ],\n  \"payload\": \"<string>\",\n  \"prompt\": \"<string>\",\n  \"resolution\": \"<string>\",\n  \"video_creation_id\": \"<string>\",\n  \"video_url\": \"<string>\"\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/proxy/vidu/extend")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"model\": \"<string>\",\n  \"callback_url\": \"<string>\",\n  \"duration\": 123,\n  \"images\": [\n    \"<string>\"\n  ],\n  \"payload\": \"<string>\",\n  \"prompt\": \"<string>\",\n  \"resolution\": \"<string>\",\n  \"video_creation_id\": \"<string>\",\n  \"video_url\": \"<string>\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/proxy/vidu/extend")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"model\": \"<string>\",\n  \"callback_url\": \"<string>\",\n  \"duration\": 123,\n  \"images\": [\n    \"<string>\"\n  ],\n  \"payload\": \"<string>\",\n  \"prompt\": \"<string>\",\n  \"resolution\": \"<string>\",\n  \"video_creation_id\": \"<string>\",\n  \"video_url\": \"<string>\"\n}"
    
    response = http.request(request)
    puts response.read_body

200

400

default
    
    
    {
      "credits": 123,
      "state": "created",
      "task_id": "<string>",
      "created_at": "2023-11-07T05:31:56Z",
      "duration": 123,
      "images": [
        "<string>"
      ],
      "model": "<string>",
      "payload": "<string>",
      "prompt": "<string>",
      "resolution": "<string>",
      "video_creation_id": "<string>",
      "video_url": "<string>"
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

# Post proxyviduextend

Copiar páginaCopiar página

Copiar páginaCopiar página

POST

/

proxy

/

vidu

/

extend

Pruébalo

cURL

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/proxy/vidu/extend \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "model": "<string>",
      "callback_url": "<string>",
      "duration": 123,
      "images": [
        "<string>"
      ],
      "payload": "<string>",
      "prompt": "<string>",
      "resolution": "<string>",
      "video_creation_id": "<string>",
      "video_url": "<string>"
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/proxy/vidu/extend"
    
    payload = {
        "model": "<string>",
        "callback_url": "<string>",
        "duration": 123,
        "images": ["<string>"],
        "payload": "<string>",
        "prompt": "<string>",
        "resolution": "<string>",
        "video_creation_id": "<string>",
        "video_url": "<string>"
    }
    headers = {
        "Authorization": "Bearer <token>",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'POST',
      headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
      body: JSON.stringify({
        model: '<string>',
        callback_url: '<string>',
        duration: 123,
        images: ['<string>'],
        payload: '<string>',
        prompt: '<string>',
        resolution: '<string>',
        video_creation_id: '<string>',
        video_url: '<string>'
      })
    };
    
    fetch('https://api.comfy.org/proxy/vidu/extend', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/proxy/vidu/extend",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'model' => '<string>',
        'callback_url' => '<string>',
        'duration' => 123,
        'images' => [
            '<string>'
        ],
        'payload' => '<string>',
        'prompt' => '<string>',
        'resolution' => '<string>',
        'video_creation_id' => '<string>',
        'video_url' => '<string>'
      ]),
      CURLOPT_HTTPHEADER => [
        "Authorization: Bearer <token>",
        "Content-Type: application/json"
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
    	"strings"
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "https://api.comfy.org/proxy/vidu/extend"
    
    	payload := strings.NewReader("{\n  \"model\": \"<string>\",\n  \"callback_url\": \"<string>\",\n  \"duration\": 123,\n  \"images\": [\n    \"<string>\"\n  ],\n  \"payload\": \"<string>\",\n  \"prompt\": \"<string>\",\n  \"resolution\": \"<string>\",\n  \"video_creation_id\": \"<string>\",\n  \"video_url\": \"<string>\"\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/proxy/vidu/extend")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"model\": \"<string>\",\n  \"callback_url\": \"<string>\",\n  \"duration\": 123,\n  \"images\": [\n    \"<string>\"\n  ],\n  \"payload\": \"<string>\",\n  \"prompt\": \"<string>\",\n  \"resolution\": \"<string>\",\n  \"video_creation_id\": \"<string>\",\n  \"video_url\": \"<string>\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/proxy/vidu/extend")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"model\": \"<string>\",\n  \"callback_url\": \"<string>\",\n  \"duration\": 123,\n  \"images\": [\n    \"<string>\"\n  ],\n  \"payload\": \"<string>\",\n  \"prompt\": \"<string>\",\n  \"resolution\": \"<string>\",\n  \"video_creation_id\": \"<string>\",\n  \"video_url\": \"<string>\"\n}"
    
    response = http.request(request)
    puts response.read_body

200

400

default
    
    
    {
      "credits": 123,
      "state": "created",
      "task_id": "<string>",
      "created_at": "2023-11-07T05:31:56Z",
      "duration": 123,
      "images": [
        "<string>"
      ],
      "model": "<string>",
      "payload": "<string>",
      "prompt": "<string>",
      "resolution": "<string>",
      "video_creation_id": "<string>",
      "video_url": "<string>"
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

#### Cuerpo

application/json

​

model

string

requerido

Model name (viduq2-pro or viduq2-turbo)

​

callback_url

string

Callback URL for task status updates

​

duration

integer<int32>

Extended duration in seconds (1-7, default 5)

​

images

string[]

Extended reference image to the end frame (only accepts 1 image)

​

payload

string

Transparent transmission parameters (max 1048576 characters)

​

prompt

string

Text prompt for video generation (max 2000 characters)

​

resolution

string

Resolution (540p, 720p, 1080p)

​

video_creation_id

string

Vidu video_creation_id, required with video_url

​

video_url

string

Any video URL, required with video_creation_id

#### Respuesta

200

application/json

OK

​

credits

integer<int32>

requerido

​

state

enum<string>

requerido

Opciones disponibles: 

`created`, 

`processing`, 

`queueing`, 

`success`, 

`failed`

​

task_id

string

requerido

​

created_at

string<date-time>

​

duration

integer<int32>

​

images

string[]

​

model

string

​

payload

string

​

prompt

string

​

resolution

string

​

video_creation_id

string

​

video_url

string

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/api-nodes/post-proxyviduextend.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/api-nodes/post-proxyviduextend)

[Generate music from video](https://docs.comfy.org/es/registry/api-reference/sonilo/generate-music-from-video)[Post proxyviduimg2video](https://docs.comfy.org/es/registry/api-reference/api-nodes/post-proxyviduimg2video)

---
url: https://docs.comfy.org/es/registry/api-reference/api-nodes/post-proxyvidumultiframe/
title: Post proxyvidumultiframe - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-31T13:26:48.787125+00:00
---

# Post proxyvidumultiframe - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/api-nodes/post-proxyvidumultiframe/

cURL

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/proxy/vidu/multiframe \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "image_settings": [
        {
          "key_image": "<string>",
          "duration": 123,
          "prompt": "<string>"
        }
      ],
      "model": "<string>",
      "start_image": "<string>",
      "callback_url": "<string>",
      "payload": "<string>",
      "resolution": "<string>"
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/proxy/vidu/multiframe"
    
    payload = {
        "image_settings": [
            {
                "key_image": "<string>",
                "duration": 123,
                "prompt": "<string>"
            }
        ],
        "model": "<string>",
        "start_image": "<string>",
        "callback_url": "<string>",
        "payload": "<string>",
        "resolution": "<string>"
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
        image_settings: [{key_image: '<string>', duration: 123, prompt: '<string>'}],
        model: '<string>',
        start_image: '<string>',
        callback_url: '<string>',
        payload: '<string>',
        resolution: '<string>'
      })
    };
    
    fetch('https://api.comfy.org/proxy/vidu/multiframe', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/proxy/vidu/multiframe",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'image_settings' => [
            [
                    'key_image' => '<string>',
                    'duration' => 123,
                    'prompt' => '<string>'
            ]
        ],
        'model' => '<string>',
        'start_image' => '<string>',
        'callback_url' => '<string>',
        'payload' => '<string>',
        'resolution' => '<string>'
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
    
    	url := "https://api.comfy.org/proxy/vidu/multiframe"
    
    	payload := strings.NewReader("{\n  \"image_settings\": [\n    {\n      \"key_image\": \"<string>\",\n      \"duration\": 123,\n      \"prompt\": \"<string>\"\n    }\n  ],\n  \"model\": \"<string>\",\n  \"start_image\": \"<string>\",\n  \"callback_url\": \"<string>\",\n  \"payload\": \"<string>\",\n  \"resolution\": \"<string>\"\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/proxy/vidu/multiframe")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"image_settings\": [\n    {\n      \"key_image\": \"<string>\",\n      \"duration\": 123,\n      \"prompt\": \"<string>\"\n    }\n  ],\n  \"model\": \"<string>\",\n  \"start_image\": \"<string>\",\n  \"callback_url\": \"<string>\",\n  \"payload\": \"<string>\",\n  \"resolution\": \"<string>\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/proxy/vidu/multiframe")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"image_settings\": [\n    {\n      \"key_image\": \"<string>\",\n      \"duration\": 123,\n      \"prompt\": \"<string>\"\n    }\n  ],\n  \"model\": \"<string>\",\n  \"start_image\": \"<string>\",\n  \"callback_url\": \"<string>\",\n  \"payload\": \"<string>\",\n  \"resolution\": \"<string>\"\n}"
    
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
      "image_settings": [
        {
          "key_image": "<string>",
          "duration": 123,
          "prompt": "<string>"
        }
      ],
      "model": "<string>",
      "payload": "<string>",
      "resolution": "<string>",
      "start_image": "<string>"
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

# Post proxyvidumultiframe

Copiar páginaCopiar página

Copiar páginaCopiar página

POST

/

proxy

/

vidu

/

multiframe

Pruébalo

cURL

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/proxy/vidu/multiframe \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "image_settings": [
        {
          "key_image": "<string>",
          "duration": 123,
          "prompt": "<string>"
        }
      ],
      "model": "<string>",
      "start_image": "<string>",
      "callback_url": "<string>",
      "payload": "<string>",
      "resolution": "<string>"
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/proxy/vidu/multiframe"
    
    payload = {
        "image_settings": [
            {
                "key_image": "<string>",
                "duration": 123,
                "prompt": "<string>"
            }
        ],
        "model": "<string>",
        "start_image": "<string>",
        "callback_url": "<string>",
        "payload": "<string>",
        "resolution": "<string>"
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
        image_settings: [{key_image: '<string>', duration: 123, prompt: '<string>'}],
        model: '<string>',
        start_image: '<string>',
        callback_url: '<string>',
        payload: '<string>',
        resolution: '<string>'
      })
    };
    
    fetch('https://api.comfy.org/proxy/vidu/multiframe', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/proxy/vidu/multiframe",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'image_settings' => [
            [
                    'key_image' => '<string>',
                    'duration' => 123,
                    'prompt' => '<string>'
            ]
        ],
        'model' => '<string>',
        'start_image' => '<string>',
        'callback_url' => '<string>',
        'payload' => '<string>',
        'resolution' => '<string>'
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
    
    	url := "https://api.comfy.org/proxy/vidu/multiframe"
    
    	payload := strings.NewReader("{\n  \"image_settings\": [\n    {\n      \"key_image\": \"<string>\",\n      \"duration\": 123,\n      \"prompt\": \"<string>\"\n    }\n  ],\n  \"model\": \"<string>\",\n  \"start_image\": \"<string>\",\n  \"callback_url\": \"<string>\",\n  \"payload\": \"<string>\",\n  \"resolution\": \"<string>\"\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/proxy/vidu/multiframe")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"image_settings\": [\n    {\n      \"key_image\": \"<string>\",\n      \"duration\": 123,\n      \"prompt\": \"<string>\"\n    }\n  ],\n  \"model\": \"<string>\",\n  \"start_image\": \"<string>\",\n  \"callback_url\": \"<string>\",\n  \"payload\": \"<string>\",\n  \"resolution\": \"<string>\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/proxy/vidu/multiframe")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"image_settings\": [\n    {\n      \"key_image\": \"<string>\",\n      \"duration\": 123,\n      \"prompt\": \"<string>\"\n    }\n  ],\n  \"model\": \"<string>\",\n  \"start_image\": \"<string>\",\n  \"callback_url\": \"<string>\",\n  \"payload\": \"<string>\",\n  \"resolution\": \"<string>\"\n}"
    
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
      "image_settings": [
        {
          "key_image": "<string>",
          "duration": 123,
          "prompt": "<string>"
        }
      ],
      "model": "<string>",
      "payload": "<string>",
      "resolution": "<string>",
      "start_image": "<string>"
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

image_settings

object[]

requerido

Configuration for intelligent multi-frame generation (2-9 frames)

Show child attributes

​

model

string

requerido

Model name (viduq2-pro or viduq2-turbo)

​

start_image

string

requerido

The first frame image (Base64 or URL)

​

callback_url

string

Callback URL for task status updates

​

payload

string

Transparent transmission parameters (max 1048576 characters)

​

resolution

string

Video resolution (540p, 720p, 1080p)

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

image_settings

object[]

Show child attributes

​

model

string

​

payload

string

​

resolution

string

​

start_image

string

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/api-nodes/post-proxyvidumultiframe.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/api-nodes/post-proxyvidumultiframe)

[Post proxyviduimg2video](https://docs.comfy.org/es/registry/api-reference/api-nodes/post-proxyviduimg2video)[Post proxyvidureference2video](https://docs.comfy.org/es/registry/api-reference/api-nodes/post-proxyvidureference2video)

---
url: https://docs.comfy.org/es/registry/api-reference/sonilo/generate-music-from-video/
title: Generate music from video - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-29T14:00:23.106018+00:00
---

# Generate music from video - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/sonilo/generate-music-from-video/

Generate music from video

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/proxy/sonilo/v2m/generate \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: multipart/form-data' \
      --form 'video=<string>' \
      --form 'prompt=<string>'
    
    
    import requests
    
    url = "https://api.comfy.org/proxy/sonilo/v2m/generate"
    
    payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"video\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001--"
    headers = {
        "Authorization": "Bearer <token>",
        "Content-Type": "multipart/form-data"
    }
    
    response = requests.post(url, data=payload, headers=headers)
    
    print(response.text)
    
    
    const form = new FormData();
    form.append('video', '<string>');
    form.append('prompt', '<string>');
    
    const options = {method: 'POST', headers: {Authorization: 'Bearer <token>'}};
    
    options.body = form;
    
    fetch('https://api.comfy.org/proxy/sonilo/v2m/generate', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/proxy/sonilo/v2m/generate",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"video\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001--",
      CURLOPT_HTTPHEADER => [
        "Authorization: Bearer <token>",
        "Content-Type: multipart/form-data"
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
    
    	url := "https://api.comfy.org/proxy/sonilo/v2m/generate"
    
    	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"video\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001--")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/proxy/sonilo/v2m/generate")
      .header("Authorization", "Bearer <token>")
      .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"video\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001--")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/proxy/sonilo/v2m/generate")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"video\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001--"
    
    response = http.request(request)
    puts response.read_body

200

400

401

402

422

429

502
    
    
    {
      "copy_index": 1,
      "display_tags": [
        "<string>"
      ],
      "prompt_index": 1,
      "stream_index": 1,
      "title": "<string>",
      "type": "title",
      "summary": "<string>"
    }
    
    
    {
      "detail": {
        "code": "<string>",
        "message": "<string>"
      }
    }
    
    
    {
      "detail": {
        "code": "<string>",
        "message": "<string>"
      }
    }
    
    
    {
      "detail": {
        "code": "<string>",
        "message": "<string>"
      }
    }
    
    
    {
      "detail": {
        "code": "<string>",
        "message": "<string>"
      }
    }
    
    
    {
      "detail": {
        "code": "<string>",
        "message": "<string>"
      }
    }
    
    
    {
      "detail": {
        "code": "<string>",
        "message": "<string>"
      }
    }

Sonilo

# Generate music from video

Copiar páginaCopiar página

Generate music from a video using Sonilo video-to-music AI. Accepts either a video file upload or a video URL, with an optional prompt. Returns a streaming NDJSON response with one or more parallel audio streams (titles, audio chunks, and completion events). Max video duration: 6 minutes. Max upload size: 300MB.

Copiar páginaCopiar página

POST

/

proxy

/

sonilo

/

v2m

/

generate

Pruébalo

Generate music from video

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/proxy/sonilo/v2m/generate \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: multipart/form-data' \
      --form 'video=<string>' \
      --form 'prompt=<string>'
    
    
    import requests
    
    url = "https://api.comfy.org/proxy/sonilo/v2m/generate"
    
    payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"video\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001--"
    headers = {
        "Authorization": "Bearer <token>",
        "Content-Type": "multipart/form-data"
    }
    
    response = requests.post(url, data=payload, headers=headers)
    
    print(response.text)
    
    
    const form = new FormData();
    form.append('video', '<string>');
    form.append('prompt', '<string>');
    
    const options = {method: 'POST', headers: {Authorization: 'Bearer <token>'}};
    
    options.body = form;
    
    fetch('https://api.comfy.org/proxy/sonilo/v2m/generate', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/proxy/sonilo/v2m/generate",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"video\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001--",
      CURLOPT_HTTPHEADER => [
        "Authorization: Bearer <token>",
        "Content-Type: multipart/form-data"
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
    
    	url := "https://api.comfy.org/proxy/sonilo/v2m/generate"
    
    	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"video\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001--")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/proxy/sonilo/v2m/generate")
      .header("Authorization", "Bearer <token>")
      .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"video\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001--")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/proxy/sonilo/v2m/generate")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"video\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001--"
    
    response = http.request(request)
    puts response.read_body

200

400

401

402

422

429

502
    
    
    {
      "copy_index": 1,
      "display_tags": [
        "<string>"
      ],
      "prompt_index": 1,
      "stream_index": 1,
      "title": "<string>",
      "type": "title",
      "summary": "<string>"
    }
    
    
    {
      "detail": {
        "code": "<string>",
        "message": "<string>"
      }
    }
    
    
    {
      "detail": {
        "code": "<string>",
        "message": "<string>"
      }
    }
    
    
    {
      "detail": {
        "code": "<string>",
        "message": "<string>"
      }
    }
    
    
    {
      "detail": {
        "code": "<string>",
        "message": "<string>"
      }
    }
    
    
    {
      "detail": {
        "code": "<string>",
        "message": "<string>"
      }
    }
    
    
    {
      "detail": {
        "code": "<string>",
        "message": "<string>"
      }
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

multipart/form-data

  * Option 1

  * Option 2




​

video

file

requerido

Multipart file part; e.g. video/mp4. Max file size 300MB.

​

prompt

string

Optional text prompt to guide music generation.

#### Respuesta

200

application/x-ndjson

OK - Streaming NDJSON response with audio generation events

  * Option 1

  * Option 2

  * Option 3

  * Option 4




A single NDJSON event from the Sonilo streaming response. Additional event types beyond those listed may appear; unknown types should be ignored by clients.

​

copy_index

integer

requerido

Rango requerido: `x >= 0`

​

display_tags

string[]

requerido

​

prompt_index

integer

requerido

Rango requerido: `x >= 0`

​

stream_index

integer

requerido

Rango requerido: `x >= 0`

​

title

string

requerido

​

type

enum<string>

requerido

Opciones disponibles: 

`title`

​

summary

string

Short natural-language description of the generated track.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/sonilo/generate-music-from-video.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/sonilo/generate-music-from-video)

[Generate music from text prompt](https://docs.comfy.org/es/registry/api-reference/sonilo/generate-music-from-text-prompt)[Post proxyviduextend](https://docs.comfy.org/es/registry/api-reference/api-nodes/post-proxyviduextend)

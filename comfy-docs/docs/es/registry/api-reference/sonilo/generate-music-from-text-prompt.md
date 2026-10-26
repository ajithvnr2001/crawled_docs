---
url: https://docs.comfy.org/es/registry/api-reference/sonilo/generate-music-from-text-prompt/
title: Generate music from text prompt - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:38.832363+00:00
---

# Generate music from text prompt - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/sonilo/generate-music-from-text-prompt/

Generate music from text prompt

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/proxy/sonilo/t2m/generate \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: multipart/form-data' \
      --form duration=180 \
      --form 'prompt=<string>'
    
    
    import requests
    
    url = "https://api.comfy.org/proxy/sonilo/t2m/generate"
    
    payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n180\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001--"
    headers = {
        "Authorization": "Bearer <token>",
        "Content-Type": "multipart/form-data"
    }
    
    response = requests.post(url, data=payload, headers=headers)
    
    print(response.text)
    
    
    const form = new FormData();
    form.append('duration', '180');
    form.append('prompt', '<string>');
    
    const options = {method: 'POST', headers: {Authorization: 'Bearer <token>'}};
    
    options.body = form;
    
    fetch('https://api.comfy.org/proxy/sonilo/t2m/generate', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/proxy/sonilo/t2m/generate",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n180\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001--",
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
    
    	url := "https://api.comfy.org/proxy/sonilo/t2m/generate"
    
    	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n180\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001--")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/proxy/sonilo/t2m/generate")
      .header("Authorization", "Bearer <token>")
      .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n180\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001--")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/proxy/sonilo/t2m/generate")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n180\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001--"
    
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

# Generate music from text prompt

Copiar páginaCopiar página

Generate music from a text prompt using Sonilo text-to-music AI. Requires a prompt describing the desired music and a caller-specified duration. Returns a streaming NDJSON response with titles, audio chunks, and completion events.

Copiar páginaCopiar página

POST

/

proxy

/

sonilo

/

t2m

/

generate

Pruébalo

Generate music from text prompt

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/proxy/sonilo/t2m/generate \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: multipart/form-data' \
      --form duration=180 \
      --form 'prompt=<string>'
    
    
    import requests
    
    url = "https://api.comfy.org/proxy/sonilo/t2m/generate"
    
    payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n180\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001--"
    headers = {
        "Authorization": "Bearer <token>",
        "Content-Type": "multipart/form-data"
    }
    
    response = requests.post(url, data=payload, headers=headers)
    
    print(response.text)
    
    
    const form = new FormData();
    form.append('duration', '180');
    form.append('prompt', '<string>');
    
    const options = {method: 'POST', headers: {Authorization: 'Bearer <token>'}};
    
    options.body = form;
    
    fetch('https://api.comfy.org/proxy/sonilo/t2m/generate', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/proxy/sonilo/t2m/generate",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n180\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001--",
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
    
    	url := "https://api.comfy.org/proxy/sonilo/t2m/generate"
    
    	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n180\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001--")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/proxy/sonilo/t2m/generate")
      .header("Authorization", "Bearer <token>")
      .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n180\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001--")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/proxy/sonilo/t2m/generate")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n180\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001--"
    
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

​

duration

integer

requerido

Desired duration of the output track in seconds.

Rango requerido: `1 <= x <= 360`

​

prompt

string

requerido

Text prompt describing the desired music. Max length 1000 characters.

Required string length: `1 - 1000`

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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/sonilo/generate-music-from-text-prompt.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/sonilo/generate-music-from-text-prompt)

[Get the status of one skin enhancer task](https://docs.comfy.org/es/registry/api-reference/freepik/get-the-status-of-one-skin-enhancer-task)[Generate music from video](https://docs.comfy.org/es/registry/api-reference/sonilo/generate-music-from-video)

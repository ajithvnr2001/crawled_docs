---
url: https://docs.comfy.org/es/registry/api-reference/sonilo/generate-a-song-with-lyrics-from-a-text-prompt/
title: Generate a song with lyrics from a text prompt - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-31T13:26:43.477209+00:00
---

# Generate a song with lyrics from a text prompt - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/sonilo/generate-a-song-with-lyrics-from-a-text-prompt/

Generate a song with lyrics from a text prompt

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/proxy/sonilo/v1/text-to-music-l \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: multipart/form-data' \
      --form 'prompt=<string>' \
      --form duration=185
    
    
    import requests
    
    url = "https://api.comfy.org/proxy/sonilo/v1/text-to-music-l"
    
    payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n185\r\n-----011000010111000001101001--"
    headers = {
        "Authorization": "Bearer <token>",
        "Content-Type": "multipart/form-data"
    }
    
    response = requests.post(url, data=payload, headers=headers)
    
    print(response.text)
    
    
    const form = new FormData();
    form.append('prompt', '<string>');
    form.append('duration', '185');
    
    const options = {method: 'POST', headers: {Authorization: 'Bearer <token>'}};
    
    options.body = form;
    
    fetch('https://api.comfy.org/proxy/sonilo/v1/text-to-music-l', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/proxy/sonilo/v1/text-to-music-l",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n185\r\n-----011000010111000001101001--",
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
    
    	url := "https://api.comfy.org/proxy/sonilo/v1/text-to-music-l"
    
    	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n185\r\n-----011000010111000001101001--")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/proxy/sonilo/v1/text-to-music-l")
      .header("Authorization", "Bearer <token>")
      .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n185\r\n-----011000010111000001101001--")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/proxy/sonilo/v1/text-to-music-l")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n185\r\n-----011000010111000001101001--"
    
    response = http.request(request)
    puts response.read_body

202

400

401

402

403

429

502
    
    
    {
      "task_id": "<string>",
      "status": "<string>"
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

# Generate a song with lyrics from a text prompt

Copiar páginaCopiar página

Submit a Sonilo Music 1.5 text-to-music-with-lyrics task. Write lyrics inside the prompt as a `Lyrics:` block with `[Verse]`, `[Chorus]` and `[Bridge]` section tags; omit the block and the model writes its own words. Returns a task id. Poll `GET /proxy/sonilo/v1/tasks/{task_id}` until the task reaches a terminal status.

Copiar páginaCopiar página

POST

/

proxy

/

sonilo

/

v1

/

text-to-music-l

Pruébalo

Generate a song with lyrics from a text prompt

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/proxy/sonilo/v1/text-to-music-l \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: multipart/form-data' \
      --form 'prompt=<string>' \
      --form duration=185
    
    
    import requests
    
    url = "https://api.comfy.org/proxy/sonilo/v1/text-to-music-l"
    
    payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n185\r\n-----011000010111000001101001--"
    headers = {
        "Authorization": "Bearer <token>",
        "Content-Type": "multipart/form-data"
    }
    
    response = requests.post(url, data=payload, headers=headers)
    
    print(response.text)
    
    
    const form = new FormData();
    form.append('prompt', '<string>');
    form.append('duration', '185');
    
    const options = {method: 'POST', headers: {Authorization: 'Bearer <token>'}};
    
    options.body = form;
    
    fetch('https://api.comfy.org/proxy/sonilo/v1/text-to-music-l', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/proxy/sonilo/v1/text-to-music-l",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n185\r\n-----011000010111000001101001--",
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
    
    	url := "https://api.comfy.org/proxy/sonilo/v1/text-to-music-l"
    
    	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n185\r\n-----011000010111000001101001--")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/proxy/sonilo/v1/text-to-music-l")
      .header("Authorization", "Bearer <token>")
      .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n185\r\n-----011000010111000001101001--")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/proxy/sonilo/v1/text-to-music-l")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prompt\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n185\r\n-----011000010111000001101001--"
    
    response = http.request(request)
    puts response.read_body

202

400

401

402

403

429

502
    
    
    {
      "task_id": "<string>",
      "status": "<string>"
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

#### Cuerpo

multipart/form-data

​

prompt

string

requerido

Text prompt describing the song, max 2000 characters. Lyrics go inside the prompt as a `Lyrics:` block with `[Verse]`, `[Chorus]` and `[Bridge]` section tags.

Required string length: `1 - 2000`

​

duration

integer

Approximate target length of the song in seconds. Omit it and the model picks a natural length.

Rango requerido: `10 <= x <= 360`

#### Respuesta

202

application/json

Accepted - the task is processing

​

task_id

string

requerido

​

status

string

Task status, `processing` on submit.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/sonilo/generate-a-song-with-lyrics-from-a-text-prompt.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/sonilo/generate-a-song-with-lyrics-from-a-text-prompt)

[Get a Sonilo task](https://docs.comfy.org/es/registry/api-reference/sonilo/get-a-sonilo-task)[Generate music from video](https://docs.comfy.org/es/registry/api-reference/sonilo/generate-music-from-video)

---
url: https://docs.comfy.org/es/registry/api-reference/freepik/upscale-an-image-with-magnific/
title: Upscale an image with Magnific - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-29T14:00:23.950371+00:00
---

# Upscale an image with Magnific - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/freepik/upscale-an-image-with-magnific/

Upscale an image with Magnific

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "image": "<string>",
      "creativity": 0,
      "engine": "automatic",
      "fractality": 0,
      "hdr": 0,
      "optimized_for": "standard",
      "prompt": "<string>",
      "resemblance": 0,
      "scale_factor": "2x",
      "webhook_url": "https://www.example.com/webhook"
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler"
    
    payload = {
        "image": "<string>",
        "creativity": 0,
        "engine": "automatic",
        "fractality": 0,
        "hdr": 0,
        "optimized_for": "standard",
        "prompt": "<string>",
        "resemblance": 0,
        "scale_factor": "2x",
        "webhook_url": "https://www.example.com/webhook"
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
        image: '<string>',
        creativity: 0,
        engine: 'automatic',
        fractality: 0,
        hdr: 0,
        optimized_for: 'standard',
        prompt: '<string>',
        resemblance: 0,
        scale_factor: '2x',
        webhook_url: 'https://www.example.com/webhook'
      })
    };
    
    fetch('https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'image' => '<string>',
        'creativity' => 0,
        'engine' => 'automatic',
        'fractality' => 0,
        'hdr' => 0,
        'optimized_for' => 'standard',
        'prompt' => '<string>',
        'resemblance' => 0,
        'scale_factor' => '2x',
        'webhook_url' => 'https://www.example.com/webhook'
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
    
    	url := "https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler"
    
    	payload := strings.NewReader("{\n  \"image\": \"<string>\",\n  \"creativity\": 0,\n  \"engine\": \"automatic\",\n  \"fractality\": 0,\n  \"hdr\": 0,\n  \"optimized_for\": \"standard\",\n  \"prompt\": \"<string>\",\n  \"resemblance\": 0,\n  \"scale_factor\": \"2x\",\n  \"webhook_url\": \"https://www.example.com/webhook\"\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"image\": \"<string>\",\n  \"creativity\": 0,\n  \"engine\": \"automatic\",\n  \"fractality\": 0,\n  \"hdr\": 0,\n  \"optimized_for\": \"standard\",\n  \"prompt\": \"<string>\",\n  \"resemblance\": 0,\n  \"scale_factor\": \"2x\",\n  \"webhook_url\": \"https://www.example.com/webhook\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"image\": \"<string>\",\n  \"creativity\": 0,\n  \"engine\": \"automatic\",\n  \"fractality\": 0,\n  \"hdr\": 0,\n  \"optimized_for\": \"standard\",\n  \"prompt\": \"<string>\",\n  \"resemblance\": 0,\n  \"scale_factor\": \"2x\",\n  \"webhook_url\": \"https://www.example.com/webhook\"\n}"
    
    response = http.request(request)
    puts response.read_body

200

400

500
    
    
    {
      "data": {
        "generated": [
          "<string>"
        ],
        "status": "CREATED",
        "task_id": "046b6c7f-0b8a-43b9-b35d-6489e6daee91"
      }
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

Freepik

# Upscale an image with Magnific

Copiar páginaCopiar página

This asynchronous endpoint enables image upscaling using advanced AI algorithms. Upon submission, it returns a unique task_id which can be used to track the progress. For real-time production use, include the optional webhook_url parameter to receive an automated notification once the task has been completed.

Copiar páginaCopiar página

POST

/

proxy

/

freepik

/

v1

/

ai

/

image-upscaler

Pruébalo

Upscale an image with Magnific

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "image": "<string>",
      "creativity": 0,
      "engine": "automatic",
      "fractality": 0,
      "hdr": 0,
      "optimized_for": "standard",
      "prompt": "<string>",
      "resemblance": 0,
      "scale_factor": "2x",
      "webhook_url": "https://www.example.com/webhook"
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler"
    
    payload = {
        "image": "<string>",
        "creativity": 0,
        "engine": "automatic",
        "fractality": 0,
        "hdr": 0,
        "optimized_for": "standard",
        "prompt": "<string>",
        "resemblance": 0,
        "scale_factor": "2x",
        "webhook_url": "https://www.example.com/webhook"
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
        image: '<string>',
        creativity: 0,
        engine: 'automatic',
        fractality: 0,
        hdr: 0,
        optimized_for: 'standard',
        prompt: '<string>',
        resemblance: 0,
        scale_factor: '2x',
        webhook_url: 'https://www.example.com/webhook'
      })
    };
    
    fetch('https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'image' => '<string>',
        'creativity' => 0,
        'engine' => 'automatic',
        'fractality' => 0,
        'hdr' => 0,
        'optimized_for' => 'standard',
        'prompt' => '<string>',
        'resemblance' => 0,
        'scale_factor' => '2x',
        'webhook_url' => 'https://www.example.com/webhook'
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
    
    	url := "https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler"
    
    	payload := strings.NewReader("{\n  \"image\": \"<string>\",\n  \"creativity\": 0,\n  \"engine\": \"automatic\",\n  \"fractality\": 0,\n  \"hdr\": 0,\n  \"optimized_for\": \"standard\",\n  \"prompt\": \"<string>\",\n  \"resemblance\": 0,\n  \"scale_factor\": \"2x\",\n  \"webhook_url\": \"https://www.example.com/webhook\"\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"image\": \"<string>\",\n  \"creativity\": 0,\n  \"engine\": \"automatic\",\n  \"fractality\": 0,\n  \"hdr\": 0,\n  \"optimized_for\": \"standard\",\n  \"prompt\": \"<string>\",\n  \"resemblance\": 0,\n  \"scale_factor\": \"2x\",\n  \"webhook_url\": \"https://www.example.com/webhook\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"image\": \"<string>\",\n  \"creativity\": 0,\n  \"engine\": \"automatic\",\n  \"fractality\": 0,\n  \"hdr\": 0,\n  \"optimized_for\": \"standard\",\n  \"prompt\": \"<string>\",\n  \"resemblance\": 0,\n  \"scale_factor\": \"2x\",\n  \"webhook_url\": \"https://www.example.com/webhook\"\n}"
    
    response = http.request(request)
    puts response.read_body

200

400

500
    
    
    {
      "data": {
        "generated": [
          "<string>"
        ],
        "status": "CREATED",
        "task_id": "046b6c7f-0b8a-43b9-b35d-6489e6daee91"
      }
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }
    
    
    {
      "error": "<string>",
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

image

string

requerido

Base64 image or URL to upscale. The resulted image can't exceed maximum allowed size of 25.3 million pixels.

​

creativity

integer

predeterminado:0

Increase or decrease AI's creativity. Valid values range [-10, 10].

Rango requerido: `-10 <= x <= 10`

​

engine

enum<string>

predeterminado:automatic

Magnific model engines.

Opciones disponibles: 

`automatic`, 

`magnific_illusio`, 

`magnific_sharpy`, 

`magnific_sparkle`

​

fractality

integer

predeterminado:0

Control the strength of the prompt and intricacy per square pixel. Valid values range [-10, 10].

Rango requerido: `-10 <= x <= 10`

​

hdr

integer

predeterminado:0

Increase or decrease the level of definition and detail. Valid values range [-10, 10].

Rango requerido: `-10 <= x <= 10`

​

optimized_for

enum<string>

predeterminado:standard

Styles to optimize the upscale process.

Opciones disponibles: 

`standard`, 

`soft_portraits`, 

`hard_portraits`, 

`art_n_illustration`, 

`videogame_assets`, 

`nature_n_landscapes`, 

`films_n_photography`, 

`3d_renders`, 

`science_fiction_n_horror`

​

prompt

string

Prompt to guide the upscale process. Reusing the same prompt for AI-generated images will improve the results.

​

resemblance

integer

predeterminado:0

Adjust the level of resemblance to the original image. Valid values range [-10, 10].

Rango requerido: `-10 <= x <= 10`

​

scale_factor

enum<string>

predeterminado:2x

Configure scale factor of the image. For higher scales, the image will take longer to process.

Opciones disponibles: 

`2x`, 

`4x`, 

`8x`, 

`16x`

​

webhook_url

string<uri>

Optional callback URL that will receive asynchronous notifications whenever the task changes status.

Ejemplo:

`"https://www.example.com/webhook"`

#### Respuesta

200

application/json

OK - The upscaling process has started

​

data

object

requerido

Show child attributes

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/freepik/upscale-an-image-with-magnific.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/freepik/upscale-an-image-with-magnific)

[Get the status of the style transfer task](https://docs.comfy.org/es/registry/api-reference/freepik/get-the-status-of-the-style-transfer-task)[Upscale an image with Precision V2](https://docs.comfy.org/es/registry/api-reference/freepik/upscale-an-image-with-precision-v2)

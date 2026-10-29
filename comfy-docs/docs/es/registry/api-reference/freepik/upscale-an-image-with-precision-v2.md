---
url: https://docs.comfy.org/es/registry/api-reference/freepik/upscale-an-image-with-precision-v2/
title: Upscale an image with Precision V2 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-29T14:00:23.840769+00:00
---

# Upscale an image with Precision V2 - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/freepik/upscale-an-image-with-precision-v2/

Upscale an image with Precision V2

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler-precision-v2 \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "image": "https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80",
      "scale_factor": 8
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler-precision-v2"
    
    payload = {
        "image": "https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80",
        "scale_factor": 8
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
        image: 'https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80',
        scale_factor: 8
      })
    };
    
    fetch('https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler-precision-v2', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler-precision-v2",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'image' => 'https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80',
        'scale_factor' => 8
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
    
    	url := "https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler-precision-v2"
    
    	payload := strings.NewReader("{\n  \"image\": \"https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80\",\n  \"scale_factor\": 8\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler-precision-v2")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"image\": \"https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80\",\n  \"scale_factor\": 8\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler-precision-v2")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"image\": \"https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80\",\n  \"scale_factor\": 8\n}"
    
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

# Upscale an image with Precision V2

Copiar páginaCopiar página

Upscales an image while adding new visual elements or details (V2). This endpoint may modify the original image content based on the prompt and inferred context. Upon submission, it returns a unique task_id which can be used to track the progress.

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

image-upscaler-precision-v2

Pruébalo

Upscale an image with Precision V2

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler-precision-v2 \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "image": "https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80",
      "scale_factor": 8
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler-precision-v2"
    
    payload = {
        "image": "https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80",
        "scale_factor": 8
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
        image: 'https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80',
        scale_factor: 8
      })
    };
    
    fetch('https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler-precision-v2', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler-precision-v2",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'image' => 'https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80',
        'scale_factor' => 8
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
    
    	url := "https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler-precision-v2"
    
    	payload := strings.NewReader("{\n  \"image\": \"https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80\",\n  \"scale_factor\": 8\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler-precision-v2")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"image\": \"https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80\",\n  \"scale_factor\": 8\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/proxy/freepik/v1/ai/image-upscaler-precision-v2")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"image\": \"https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80\",\n  \"scale_factor\": 8\n}"
    
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

Source image to upscale. Accepts either:

  * A publicly accessible HTTPS URL pointing to the image
  * A base64-encoded image string



​

flavor

enum<string>

Image processing flavor:

  * sublime: Optimized for artistic and illustrated images
  * photo: Optimized for photographic images
  * photo_denoiser: Specialized for photos with noise reduction



Opciones disponibles: 

`sublime`, 

`photo`, 

`photo_denoiser`

​

scale_factor

integer

Image scaling factor. Determines how much larger the output will be compared to input.

Rango requerido: `2 <= x <= 16`

​

sharpen

integer

predeterminado:7

Image sharpness intensity control. Higher values increase edge definition and clarity.

Rango requerido: `0 <= x <= 100`

​

smart_grain

integer

predeterminado:7

Intelligent grain/texture enhancement. Higher values add more fine-grained texture.

Rango requerido: `0 <= x <= 100`

​

ultra_detail

integer

predeterminado:30

Ultra detail enhancement level. Higher values create more intricate details.

Rango requerido: `0 <= x <= 100`

​

webhook_url

string<uri>

Optional callback URL that will receive asynchronous notifications when the upscaling task completes.

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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/freepik/upscale-an-image-with-precision-v2.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/freepik/upscale-an-image-with-precision-v2)

[Upscale an image with Magnific](https://docs.comfy.org/es/registry/api-reference/freepik/upscale-an-image-with-magnific)[Get the status of the Precision V2 upscaling task](https://docs.comfy.org/es/registry/api-reference/freepik/get-the-status-of-the-precision-v2-upscaling-task)

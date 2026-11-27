---
url: https://docs.comfy.org/es/registry/api-reference/freepik/relight-an-image/
title: Relight an image - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-27T17:19:33.435014+00:00
---

# Relight an image - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/freepik/relight-an-image/

Relight an image

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/proxy/freepik/v1/ai/image-relight \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "image": "https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80",
      "prompt": "warm golden-hour sunlight from the left"
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/proxy/freepik/v1/ai/image-relight"
    
    payload = {
        "image": "https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80",
        "prompt": "warm golden-hour sunlight from the left"
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
        prompt: 'warm golden-hour sunlight from the left'
      })
    };
    
    fetch('https://api.comfy.org/proxy/freepik/v1/ai/image-relight', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/proxy/freepik/v1/ai/image-relight",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'image' => 'https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80',
        'prompt' => 'warm golden-hour sunlight from the left'
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
    
    	url := "https://api.comfy.org/proxy/freepik/v1/ai/image-relight"
    
    	payload := strings.NewReader("{\n  \"image\": \"https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80\",\n  \"prompt\": \"warm golden-hour sunlight from the left\"\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/proxy/freepik/v1/ai/image-relight")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"image\": \"https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80\",\n  \"prompt\": \"warm golden-hour sunlight from the left\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/proxy/freepik/v1/ai/image-relight")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"image\": \"https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80\",\n  \"prompt\": \"warm golden-hour sunlight from the left\"\n}"
    
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

# Relight an image

Copiar páginaCopiar página

Relight an image using AI. This endpoint accepts a variety of parameters to customize the generated images.

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

image-relight

Pruébalo

Relight an image

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/proxy/freepik/v1/ai/image-relight \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "image": "https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80",
      "prompt": "warm golden-hour sunlight from the left"
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/proxy/freepik/v1/ai/image-relight"
    
    payload = {
        "image": "https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80",
        "prompt": "warm golden-hour sunlight from the left"
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
        prompt: 'warm golden-hour sunlight from the left'
      })
    };
    
    fetch('https://api.comfy.org/proxy/freepik/v1/ai/image-relight', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/proxy/freepik/v1/ai/image-relight",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'image' => 'https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80',
        'prompt' => 'warm golden-hour sunlight from the left'
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
    
    	url := "https://api.comfy.org/proxy/freepik/v1/ai/image-relight"
    
    	payload := strings.NewReader("{\n  \"image\": \"https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80\",\n  \"prompt\": \"warm golden-hour sunlight from the left\"\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/proxy/freepik/v1/ai/image-relight")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"image\": \"https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80\",\n  \"prompt\": \"warm golden-hour sunlight from the left\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/proxy/freepik/v1/ai/image-relight")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"image\": \"https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80\",\n  \"prompt\": \"warm golden-hour sunlight from the left\"\n}"
    
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

Authorization

string

header

requerido

Bearer token authentication. Normally a Firebase or Cloud JWT. A 'comfyui-' prefixed API key is also accepted in this header: the prefix classifies the value as an API key and it is validated exactly as if it had been sent in X-API-Key. Accepted on the operations served by the comfyFirebase auth middleware (BE-9720, parity with ingest).

#### Cuerpo

application/json

image

string

requerido

Base64 or URL of the image to do the relight

advanced_settings

object

Show child attributes

change_background

boolean

predeterminado:true

When enabled, changes the background based on prompt and/or reference image. Useful for product placement and portraits.

interpolate_from_original

boolean

predeterminado:false

When enabled, makes the final image interpolate from the original using the light transfer strength slider.

light_transfer_strength

integer

predeterminado:100

Level of light transfer intensity. 0% keeps closest to original, 100% is maximum transfer.

Rango requerido: `0 <= x <= 100`

preserve_details

boolean

predeterminado:true

Maintains texture and small details of the original image. Good for product photography, texts, etc.

prompt

string

You can guide the generation process and influence the light transfer with a descriptive prompt. IMPORTANT: You can emphasize specific aspects of the light in your prompt by using a number in parentheses, ranging from 1 to 1.4, like "(dark scene:1.3)".

style

enum<string>

predeterminado:standard

Style preset for the relight operation.

Opciones disponibles: 

`standard`, 

`darker_but_realistic`, 

`clean`, 

`smooth`, 

`brighter`, 

`contrasted_n_hdr`, 

`just_composition`

transfer_light_from_lightmap

string

Base64 or URL of the lightmap for light transfer. Incompatible with 'transfer_light_from_reference_image'

transfer_light_from_reference_image

string

Base64 or URL of the reference image for light transfer. Incompatible with 'transfer_light_from_lightmap'

webhook_url

string<uri>

Optional callback URL that will receive asynchronous notifications whenever the task changes status.

Ejemplo:

`"https://www.example.com/webhook"`

#### Respuesta

200

application/json

OK - The relight process has started

data

object

requerido

Show child attributes

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/freepik/relight-an-image.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/freepik/relight-an-image)

[List all node versions given some filters.](https://docs.comfy.org/es/registry/api-reference/registry/list-all-node-versions-given-some-filters)[Get the status of the relight task](https://docs.comfy.org/es/registry/api-reference/freepik/get-the-status-of-the-relight-task)

---
url: https://docs.comfy.org/es/registry/api-reference/freepik/skin-enhancer-using-ai-faithful/
title: Skin enhancer using AI (Faithful) - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:33.215933+00:00
---

# Skin enhancer using AI (Faithful) - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/freepik/skin-enhancer-using-ai-faithful/

Skin enhancer using AI (Faithful)

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/proxy/freepik/v1/ai/skin-enhancer/faithful \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "image": "https://img.magnific.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80"
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/proxy/freepik/v1/ai/skin-enhancer/faithful"
    
    payload = { "image": "https://img.magnific.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80" }
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
        image: 'https://img.magnific.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80'
      })
    };
    
    fetch('https://api.comfy.org/proxy/freepik/v1/ai/skin-enhancer/faithful', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/proxy/freepik/v1/ai/skin-enhancer/faithful",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'image' => 'https://img.magnific.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80'
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
    
    	url := "https://api.comfy.org/proxy/freepik/v1/ai/skin-enhancer/faithful"
    
    	payload := strings.NewReader("{\n  \"image\": \"https://img.magnific.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80\"\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/proxy/freepik/v1/ai/skin-enhancer/faithful")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"image\": \"https://img.magnific.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/proxy/freepik/v1/ai/skin-enhancer/faithful")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"image\": \"https://img.magnific.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80\"\n}"
    
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

# Skin enhancer using AI (Faithful)

Copiar páginaCopiar página

Enhance skin in images using AI with the Faithful mode. This mode preserves the original appearance while improving skin quality.

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

skin-enhancer

/

faithful

Pruébalo

Skin enhancer using AI (Faithful)

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/proxy/freepik/v1/ai/skin-enhancer/faithful \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "image": "https://img.magnific.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80"
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/proxy/freepik/v1/ai/skin-enhancer/faithful"
    
    payload = { "image": "https://img.magnific.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80" }
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
        image: 'https://img.magnific.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80'
      })
    };
    
    fetch('https://api.comfy.org/proxy/freepik/v1/ai/skin-enhancer/faithful', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/proxy/freepik/v1/ai/skin-enhancer/faithful",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'image' => 'https://img.magnific.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80'
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
    
    	url := "https://api.comfy.org/proxy/freepik/v1/ai/skin-enhancer/faithful"
    
    	payload := strings.NewReader("{\n  \"image\": \"https://img.magnific.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80\"\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/proxy/freepik/v1/ai/skin-enhancer/faithful")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"image\": \"https://img.magnific.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/proxy/freepik/v1/ai/skin-enhancer/faithful")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"image\": \"https://img.magnific.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80\"\n}"
    
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

Input image. Supports Base64 encoding or HTTPS URL (must be publicly accessible).

Ejemplo:

`"https://example.com/portrait.jpg"`

​

sharpen

integer

predeterminado:0

Sharpening intensity

Rango requerido: `0 <= x <= 100`

​

skin_detail

integer

predeterminado:80

Skin detail enhancement level

Rango requerido: `0 <= x <= 100`

​

smart_grain

integer

predeterminado:2

Smart grain intensity

Rango requerido: `0 <= x <= 100`

​

webhook_url

string<uri>

Optional callback URL for async notifications.

Ejemplo:

`"https://www.example.com/webhook"`

#### Respuesta

200

application/json

OK - The skin enhancer process has started

​

data

object

requerido

Show child attributes

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/freepik/skin-enhancer-using-ai-faithful.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/freepik/skin-enhancer-using-ai-faithful)

[Skin enhancer using AI (Creative)](https://docs.comfy.org/es/registry/api-reference/freepik/skin-enhancer-using-ai-creative)[Skin enhancer using AI (Flexible)](https://docs.comfy.org/es/registry/api-reference/freepik/skin-enhancer-using-ai-flexible)

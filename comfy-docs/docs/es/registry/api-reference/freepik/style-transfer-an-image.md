---
url: https://docs.comfy.org/es/registry/api-reference/freepik/style-transfer-an-image/
title: Style transfer an image - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-29T14:00:24.005017+00:00
---

# Style transfer an image - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/freepik/style-transfer-an-image/

Style transfer an image

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/proxy/freepik/v1/ai/image-style-transfer \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "image": "<string>",
      "reference_image": "<string>",
      "engine": "balanced",
      "fixed_generation": false,
      "flavor": "faithful",
      "is_portrait": false,
      "portrait_style": "standard",
      "prompt": "<string>",
      "structure_strength": 50,
      "style_strength": 100,
      "webhook_url": "https://www.example.com/webhook"
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/proxy/freepik/v1/ai/image-style-transfer"
    
    payload = {
        "image": "<string>",
        "reference_image": "<string>",
        "engine": "balanced",
        "fixed_generation": False,
        "flavor": "faithful",
        "is_portrait": False,
        "portrait_style": "standard",
        "prompt": "<string>",
        "structure_strength": 50,
        "style_strength": 100,
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
        reference_image: '<string>',
        engine: 'balanced',
        fixed_generation: false,
        flavor: 'faithful',
        is_portrait: false,
        portrait_style: 'standard',
        prompt: '<string>',
        structure_strength: 50,
        style_strength: 100,
        webhook_url: 'https://www.example.com/webhook'
      })
    };
    
    fetch('https://api.comfy.org/proxy/freepik/v1/ai/image-style-transfer', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/proxy/freepik/v1/ai/image-style-transfer",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'image' => '<string>',
        'reference_image' => '<string>',
        'engine' => 'balanced',
        'fixed_generation' => false,
        'flavor' => 'faithful',
        'is_portrait' => false,
        'portrait_style' => 'standard',
        'prompt' => '<string>',
        'structure_strength' => 50,
        'style_strength' => 100,
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
    
    	url := "https://api.comfy.org/proxy/freepik/v1/ai/image-style-transfer"
    
    	payload := strings.NewReader("{\n  \"image\": \"<string>\",\n  \"reference_image\": \"<string>\",\n  \"engine\": \"balanced\",\n  \"fixed_generation\": false,\n  \"flavor\": \"faithful\",\n  \"is_portrait\": false,\n  \"portrait_style\": \"standard\",\n  \"prompt\": \"<string>\",\n  \"structure_strength\": 50,\n  \"style_strength\": 100,\n  \"webhook_url\": \"https://www.example.com/webhook\"\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/proxy/freepik/v1/ai/image-style-transfer")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"image\": \"<string>\",\n  \"reference_image\": \"<string>\",\n  \"engine\": \"balanced\",\n  \"fixed_generation\": false,\n  \"flavor\": \"faithful\",\n  \"is_portrait\": false,\n  \"portrait_style\": \"standard\",\n  \"prompt\": \"<string>\",\n  \"structure_strength\": 50,\n  \"style_strength\": 100,\n  \"webhook_url\": \"https://www.example.com/webhook\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/proxy/freepik/v1/ai/image-style-transfer")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"image\": \"<string>\",\n  \"reference_image\": \"<string>\",\n  \"engine\": \"balanced\",\n  \"fixed_generation\": false,\n  \"flavor\": \"faithful\",\n  \"is_portrait\": false,\n  \"portrait_style\": \"standard\",\n  \"prompt\": \"<string>\",\n  \"structure_strength\": 50,\n  \"style_strength\": 100,\n  \"webhook_url\": \"https://www.example.com/webhook\"\n}"
    
    response = http.request(request)
    puts response.read_body

200

400

500
    
    
    {
      "generated": [
        "<string>"
      ],
      "status": "CREATED",
      "task_id": "046b6c7f-0b8a-43b9-b35d-6489e6daee91"
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

# Style transfer an image

Copiar páginaCopiar página

Style transfer an image using AI.

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

image-style-transfer

Pruébalo

Style transfer an image

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/proxy/freepik/v1/ai/image-style-transfer \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "image": "<string>",
      "reference_image": "<string>",
      "engine": "balanced",
      "fixed_generation": false,
      "flavor": "faithful",
      "is_portrait": false,
      "portrait_style": "standard",
      "prompt": "<string>",
      "structure_strength": 50,
      "style_strength": 100,
      "webhook_url": "https://www.example.com/webhook"
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/proxy/freepik/v1/ai/image-style-transfer"
    
    payload = {
        "image": "<string>",
        "reference_image": "<string>",
        "engine": "balanced",
        "fixed_generation": False,
        "flavor": "faithful",
        "is_portrait": False,
        "portrait_style": "standard",
        "prompt": "<string>",
        "structure_strength": 50,
        "style_strength": 100,
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
        reference_image: '<string>',
        engine: 'balanced',
        fixed_generation: false,
        flavor: 'faithful',
        is_portrait: false,
        portrait_style: 'standard',
        prompt: '<string>',
        structure_strength: 50,
        style_strength: 100,
        webhook_url: 'https://www.example.com/webhook'
      })
    };
    
    fetch('https://api.comfy.org/proxy/freepik/v1/ai/image-style-transfer', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/proxy/freepik/v1/ai/image-style-transfer",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'image' => '<string>',
        'reference_image' => '<string>',
        'engine' => 'balanced',
        'fixed_generation' => false,
        'flavor' => 'faithful',
        'is_portrait' => false,
        'portrait_style' => 'standard',
        'prompt' => '<string>',
        'structure_strength' => 50,
        'style_strength' => 100,
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
    
    	url := "https://api.comfy.org/proxy/freepik/v1/ai/image-style-transfer"
    
    	payload := strings.NewReader("{\n  \"image\": \"<string>\",\n  \"reference_image\": \"<string>\",\n  \"engine\": \"balanced\",\n  \"fixed_generation\": false,\n  \"flavor\": \"faithful\",\n  \"is_portrait\": false,\n  \"portrait_style\": \"standard\",\n  \"prompt\": \"<string>\",\n  \"structure_strength\": 50,\n  \"style_strength\": 100,\n  \"webhook_url\": \"https://www.example.com/webhook\"\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/proxy/freepik/v1/ai/image-style-transfer")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"image\": \"<string>\",\n  \"reference_image\": \"<string>\",\n  \"engine\": \"balanced\",\n  \"fixed_generation\": false,\n  \"flavor\": \"faithful\",\n  \"is_portrait\": false,\n  \"portrait_style\": \"standard\",\n  \"prompt\": \"<string>\",\n  \"structure_strength\": 50,\n  \"style_strength\": 100,\n  \"webhook_url\": \"https://www.example.com/webhook\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/proxy/freepik/v1/ai/image-style-transfer")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"image\": \"<string>\",\n  \"reference_image\": \"<string>\",\n  \"engine\": \"balanced\",\n  \"fixed_generation\": false,\n  \"flavor\": \"faithful\",\n  \"is_portrait\": false,\n  \"portrait_style\": \"standard\",\n  \"prompt\": \"<string>\",\n  \"structure_strength\": 50,\n  \"style_strength\": 100,\n  \"webhook_url\": \"https://www.example.com/webhook\"\n}"
    
    response = http.request(request)
    puts response.read_body

200

400

500
    
    
    {
      "generated": [
        "<string>"
      ],
      "status": "CREATED",
      "task_id": "046b6c7f-0b8a-43b9-b35d-6489e6daee91"
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

Base64 or URL of the image to do the style transfer

​

reference_image

string

requerido

Base64 or URL of the reference image for style transfer

​

engine

enum<string>

predeterminado:balanced

Engine preset for style transfer

Opciones disponibles: 

`balanced`, 

`definio`, 

`illusio`, 

`3d_cartoon`, 

`colorful_anime`, 

`caricature`, 

`real`, 

`super_real`, 

`softy`

​

fixed_generation

boolean

predeterminado:false

When enabled, using the same settings will consistently produce the same image.

​

flavor

enum<string>

predeterminado:faithful

Flavor of the transferring style

Opciones disponibles: 

`faithful`, 

`gen_z`, 

`psychedelia`, 

`detaily`, 

`clear`, 

`donotstyle`, 

`donotstyle_sharp`

​

is_portrait

boolean

predeterminado:false

Indicates whether the image should be processed as a portrait.

​

portrait_beautifier

enum<string>

Facial beautification on portrait images. Only used if is_portrait is true.

Opciones disponibles: 

`beautify_face`, 

`beautify_face_max`

​

portrait_style

enum<string>

predeterminado:standard

Visual style applied to portrait images. Only used if is_portrait is true.

Opciones disponibles: 

`standard`, 

`pop`, 

`super_pop`

​

prompt

string

Prompt for the AI model

​

structure_strength

integer

predeterminado:50

Allows to maintain the structure of the original image

Rango requerido: `0 <= x <= 100`

​

style_strength

integer

predeterminado:100

Percentage of style strength

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

OK - The style transfer process has started

​

generated

string<uri>[]

URLs to the generated images.

​

status

enum<string>

Opciones disponibles: 

`CREATED`, 

`IN_PROGRESS`, 

`COMPLETED`, 

`FAILED`

​

task_id

string<uuid>

Ejemplo:

`"046b6c7f-0b8a-43b9-b35d-6489e6daee91"`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/freepik/style-transfer-an-image.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/freepik/style-transfer-an-image)

[Get the status of the relight task](https://docs.comfy.org/es/registry/api-reference/freepik/get-the-status-of-the-relight-task)[Get the status of the style transfer task](https://docs.comfy.org/es/registry/api-reference/freepik/get-the-status-of-the-style-transfer-task)

---
url: https://docs.comfy.org/es/registry/api-reference/api-nodes/post-proxyvidustart-end2video/
title: Post proxyvidustart end2video - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-28T13:54:27.568769+00:00
---

# Post proxyvidustart end2video - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/api-nodes/post-proxyvidustart-end2video/

cURL

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/proxy/vidu/start-end2video \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "aspect_ratio": "<string>",
      "audio": true,
      "bgm": true,
      "callback_url": "<string>",
      "duration": 123,
      "enhance": true,
      "images": [
        "<string>"
      ],
      "is_rec": true,
      "meta_data": "<string>",
      "model": "<string>",
      "off_peak": true,
      "payload": "<string>",
      "priority": 123,
      "prompt": "<string>",
      "resolution": "<string>",
      "seed": 123,
      "voice_id": "<string>",
      "watermark": true,
      "wm_position": 123,
      "wm_url": "<string>"
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/proxy/vidu/start-end2video"
    
    payload = {
        "aspect_ratio": "<string>",
        "audio": True,
        "bgm": True,
        "callback_url": "<string>",
        "duration": 123,
        "enhance": True,
        "images": ["<string>"],
        "is_rec": True,
        "meta_data": "<string>",
        "model": "<string>",
        "off_peak": True,
        "payload": "<string>",
        "priority": 123,
        "prompt": "<string>",
        "resolution": "<string>",
        "seed": 123,
        "voice_id": "<string>",
        "watermark": True,
        "wm_position": 123,
        "wm_url": "<string>"
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
        aspect_ratio: '<string>',
        audio: true,
        bgm: true,
        callback_url: '<string>',
        duration: 123,
        enhance: true,
        images: ['<string>'],
        is_rec: true,
        meta_data: '<string>',
        model: '<string>',
        off_peak: true,
        payload: '<string>',
        priority: 123,
        prompt: '<string>',
        resolution: '<string>',
        seed: 123,
        voice_id: '<string>',
        watermark: true,
        wm_position: 123,
        wm_url: '<string>'
      })
    };
    
    fetch('https://api.comfy.org/proxy/vidu/start-end2video', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/proxy/vidu/start-end2video",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'aspect_ratio' => '<string>',
        'audio' => true,
        'bgm' => true,
        'callback_url' => '<string>',
        'duration' => 123,
        'enhance' => true,
        'images' => [
            '<string>'
        ],
        'is_rec' => true,
        'meta_data' => '<string>',
        'model' => '<string>',
        'off_peak' => true,
        'payload' => '<string>',
        'priority' => 123,
        'prompt' => '<string>',
        'resolution' => '<string>',
        'seed' => 123,
        'voice_id' => '<string>',
        'watermark' => true,
        'wm_position' => 123,
        'wm_url' => '<string>'
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
    
    	url := "https://api.comfy.org/proxy/vidu/start-end2video"
    
    	payload := strings.NewReader("{\n  \"aspect_ratio\": \"<string>\",\n  \"audio\": true,\n  \"bgm\": true,\n  \"callback_url\": \"<string>\",\n  \"duration\": 123,\n  \"enhance\": true,\n  \"images\": [\n    \"<string>\"\n  ],\n  \"is_rec\": true,\n  \"meta_data\": \"<string>\",\n  \"model\": \"<string>\",\n  \"off_peak\": true,\n  \"payload\": \"<string>\",\n  \"priority\": 123,\n  \"prompt\": \"<string>\",\n  \"resolution\": \"<string>\",\n  \"seed\": 123,\n  \"voice_id\": \"<string>\",\n  \"watermark\": true,\n  \"wm_position\": 123,\n  \"wm_url\": \"<string>\"\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/proxy/vidu/start-end2video")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"aspect_ratio\": \"<string>\",\n  \"audio\": true,\n  \"bgm\": true,\n  \"callback_url\": \"<string>\",\n  \"duration\": 123,\n  \"enhance\": true,\n  \"images\": [\n    \"<string>\"\n  ],\n  \"is_rec\": true,\n  \"meta_data\": \"<string>\",\n  \"model\": \"<string>\",\n  \"off_peak\": true,\n  \"payload\": \"<string>\",\n  \"priority\": 123,\n  \"prompt\": \"<string>\",\n  \"resolution\": \"<string>\",\n  \"seed\": 123,\n  \"voice_id\": \"<string>\",\n  \"watermark\": true,\n  \"wm_position\": 123,\n  \"wm_url\": \"<string>\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/proxy/vidu/start-end2video")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"aspect_ratio\": \"<string>\",\n  \"audio\": true,\n  \"bgm\": true,\n  \"callback_url\": \"<string>\",\n  \"duration\": 123,\n  \"enhance\": true,\n  \"images\": [\n    \"<string>\"\n  ],\n  \"is_rec\": true,\n  \"meta_data\": \"<string>\",\n  \"model\": \"<string>\",\n  \"off_peak\": true,\n  \"payload\": \"<string>\",\n  \"priority\": 123,\n  \"prompt\": \"<string>\",\n  \"resolution\": \"<string>\",\n  \"seed\": 123,\n  \"voice_id\": \"<string>\",\n  \"watermark\": true,\n  \"wm_position\": 123,\n  \"wm_url\": \"<string>\"\n}"
    
    response = http.request(request)
    puts response.read_body

200

400

default
    
    
    {
      "credits": 123,
      "state": "created",
      "task_id": "<string>",
      "aspect_ratio": "<string>",
      "bgm": true,
      "created_at": "2023-11-07T05:31:56Z",
      "duration": 123,
      "images": [
        "<string>"
      ],
      "model": "<string>",
      "movement_amplitude": "auto",
      "off_peak": true,
      "payload": "<string>",
      "prompt": "<string>",
      "resolution": "<string>",
      "seed": 123,
      "style": "general",
      "watermark": true
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

# Post proxyvidustart end2video

Copiar páginaCopiar página

Copiar páginaCopiar página

POST

/

proxy

/

vidu

/

start-end2video

Pruébalo

cURL

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/proxy/vidu/start-end2video \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "aspect_ratio": "<string>",
      "audio": true,
      "bgm": true,
      "callback_url": "<string>",
      "duration": 123,
      "enhance": true,
      "images": [
        "<string>"
      ],
      "is_rec": true,
      "meta_data": "<string>",
      "model": "<string>",
      "off_peak": true,
      "payload": "<string>",
      "priority": 123,
      "prompt": "<string>",
      "resolution": "<string>",
      "seed": 123,
      "voice_id": "<string>",
      "watermark": true,
      "wm_position": 123,
      "wm_url": "<string>"
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/proxy/vidu/start-end2video"
    
    payload = {
        "aspect_ratio": "<string>",
        "audio": True,
        "bgm": True,
        "callback_url": "<string>",
        "duration": 123,
        "enhance": True,
        "images": ["<string>"],
        "is_rec": True,
        "meta_data": "<string>",
        "model": "<string>",
        "off_peak": True,
        "payload": "<string>",
        "priority": 123,
        "prompt": "<string>",
        "resolution": "<string>",
        "seed": 123,
        "voice_id": "<string>",
        "watermark": True,
        "wm_position": 123,
        "wm_url": "<string>"
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
        aspect_ratio: '<string>',
        audio: true,
        bgm: true,
        callback_url: '<string>',
        duration: 123,
        enhance: true,
        images: ['<string>'],
        is_rec: true,
        meta_data: '<string>',
        model: '<string>',
        off_peak: true,
        payload: '<string>',
        priority: 123,
        prompt: '<string>',
        resolution: '<string>',
        seed: 123,
        voice_id: '<string>',
        watermark: true,
        wm_position: 123,
        wm_url: '<string>'
      })
    };
    
    fetch('https://api.comfy.org/proxy/vidu/start-end2video', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/proxy/vidu/start-end2video",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'aspect_ratio' => '<string>',
        'audio' => true,
        'bgm' => true,
        'callback_url' => '<string>',
        'duration' => 123,
        'enhance' => true,
        'images' => [
            '<string>'
        ],
        'is_rec' => true,
        'meta_data' => '<string>',
        'model' => '<string>',
        'off_peak' => true,
        'payload' => '<string>',
        'priority' => 123,
        'prompt' => '<string>',
        'resolution' => '<string>',
        'seed' => 123,
        'voice_id' => '<string>',
        'watermark' => true,
        'wm_position' => 123,
        'wm_url' => '<string>'
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
    
    	url := "https://api.comfy.org/proxy/vidu/start-end2video"
    
    	payload := strings.NewReader("{\n  \"aspect_ratio\": \"<string>\",\n  \"audio\": true,\n  \"bgm\": true,\n  \"callback_url\": \"<string>\",\n  \"duration\": 123,\n  \"enhance\": true,\n  \"images\": [\n    \"<string>\"\n  ],\n  \"is_rec\": true,\n  \"meta_data\": \"<string>\",\n  \"model\": \"<string>\",\n  \"off_peak\": true,\n  \"payload\": \"<string>\",\n  \"priority\": 123,\n  \"prompt\": \"<string>\",\n  \"resolution\": \"<string>\",\n  \"seed\": 123,\n  \"voice_id\": \"<string>\",\n  \"watermark\": true,\n  \"wm_position\": 123,\n  \"wm_url\": \"<string>\"\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/proxy/vidu/start-end2video")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"aspect_ratio\": \"<string>\",\n  \"audio\": true,\n  \"bgm\": true,\n  \"callback_url\": \"<string>\",\n  \"duration\": 123,\n  \"enhance\": true,\n  \"images\": [\n    \"<string>\"\n  ],\n  \"is_rec\": true,\n  \"meta_data\": \"<string>\",\n  \"model\": \"<string>\",\n  \"off_peak\": true,\n  \"payload\": \"<string>\",\n  \"priority\": 123,\n  \"prompt\": \"<string>\",\n  \"resolution\": \"<string>\",\n  \"seed\": 123,\n  \"voice_id\": \"<string>\",\n  \"watermark\": true,\n  \"wm_position\": 123,\n  \"wm_url\": \"<string>\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/proxy/vidu/start-end2video")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"aspect_ratio\": \"<string>\",\n  \"audio\": true,\n  \"bgm\": true,\n  \"callback_url\": \"<string>\",\n  \"duration\": 123,\n  \"enhance\": true,\n  \"images\": [\n    \"<string>\"\n  ],\n  \"is_rec\": true,\n  \"meta_data\": \"<string>\",\n  \"model\": \"<string>\",\n  \"off_peak\": true,\n  \"payload\": \"<string>\",\n  \"priority\": 123,\n  \"prompt\": \"<string>\",\n  \"resolution\": \"<string>\",\n  \"seed\": 123,\n  \"voice_id\": \"<string>\",\n  \"watermark\": true,\n  \"wm_position\": 123,\n  \"wm_url\": \"<string>\"\n}"
    
    response = http.request(request)
    puts response.read_body

200

400

default
    
    
    {
      "credits": 123,
      "state": "created",
      "task_id": "<string>",
      "aspect_ratio": "<string>",
      "bgm": true,
      "created_at": "2023-11-07T05:31:56Z",
      "duration": 123,
      "images": [
        "<string>"
      ],
      "model": "<string>",
      "movement_amplitude": "auto",
      "off_peak": true,
      "payload": "<string>",
      "prompt": "<string>",
      "resolution": "<string>",
      "seed": 123,
      "style": "general",
      "watermark": true
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

aspect_ratio

string

​

audio

boolean

Enable direct audio-video generation capability (default true for q3 model)

​

audio_type

enum<string>

Audio type when audio is true: all (sound effects + vocals), speech_only, sound_effect_only. Ineffective for q3 model

Opciones disponibles: 

`all`, 

`speech_only`, 

`sound_effect_only`

​

bgm

boolean

Add background music to generated video (ineffective for q3 model)

​

callback_url

string

Callback URL for task status updates

​

duration

integer<int32>

Video duration in seconds. viduq3-pro: 1-16, viduq2-pro-fast: 1-10, viduq2-pro/turbo: 1-8

​

enhance

boolean

​

images

string[]

Images for img2video (accepts 1 image as start frame)

​

is_rec

boolean

Use recommended prompt (consumes additional 10 credits)

​

meta_data

string

Metadata identification, JSON format string for custom metadata

​

model

string

Model name: viduq3-pro, viduq2-pro-fast, viduq2-pro, viduq2-turbo, viduq1, viduq1-classic, vidu2.0

​

movement_amplitude

enum<string>

Movement amplitude of objects in frame (ineffective for q2, q3 models)

Opciones disponibles: 

`auto`, 

`small`, 

`medium`, 

`large`

​

off_peak

boolean

Off peak mode (lower cost, tasks generated within 48 hours)

​

payload

string

Transparent transmission parameters (max 1048576 characters)

​

priority

integer<int32>

​

prompt

string

Text prompt for video generation (max 2000 characters)

​

resolution

string

Resolution: 360p, 540p, 720p, 1080p, 2K (availability depends on model and duration)

​

seed

integer<int32>

Random seed (defaults to random if not specified)

​

style

enum<string>

Opciones disponibles: 

`general`, 

`anime`

​

voice_id

string

Voice ID for audio (ineffective for q3 model)

​

watermark

boolean

Add watermark to video (default false)

​

wm_position

integer<int32>

Watermark position: 1 (top left), 2 (top right), 3 (bottom right, default), 4 (bottom left)

​

wm_url

string

Watermark image URL (uses default watermark if not provided)

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

aspect_ratio

string

​

bgm

boolean

Whether background music was added

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

movement_amplitude

enum<string>

Opciones disponibles: 

`auto`, 

`small`, 

`medium`, 

`large`

​

off_peak

boolean

Off peak mode status

​

payload

string

Transparent transmission parameters

​

prompt

string

​

resolution

string

​

seed

integer<int32>

​

style

enum<string>

Opciones disponibles: 

`general`, 

`anime`

​

watermark

boolean

Whether watermark was added

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/api-nodes/post-proxyvidustart-end2video.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/api-nodes/post-proxyvidustart-end2video)

[Post proxyvidureference2video](https://docs.comfy.org/es/registry/api-reference/api-nodes/post-proxyvidureference2video)[Get proxyvidutasks creations](https://docs.comfy.org/es/registry/api-reference/api-nodes/get-proxyvidutasks-creations)

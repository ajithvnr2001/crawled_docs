---
url: https://docs.comfy.org/es/api-reference/cloud/system/get-system-statistics/
title: Get system statistics - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:25.351296+00:00
---

# Get system statistics - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/system/get-system-statistics/

Get system statistics

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/system_stats
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/system_stats"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://cloud.comfy.org/api/system_stats', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/system_stats",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "GET",
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
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "https://cloud.comfy.org/api/system_stats"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/system_stats")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/system_stats")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

401
    
    
    {
      "system": {
        "os": "<string>",
        "python_version": "<string>",
        "embedded_python": true,
        "comfyui_version": "<string>",
        "pytorch_version": "<string>",
        "argv": [
          "<string>"
        ],
        "ram_total": 123,
        "ram_free": 123,
        "comfyui_frontend_version": "<string>",
        "workflow_templates_version": "<string>",
        "cloud_version": "<string>"
      },
      "devices": [
        {
          "name": "<string>",
          "type": "<string>",
          "vram_total": 123,
          "vram_free": 123
        }
      ]
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }

system

# Get system statistics

Copiar páginaCopiar página

Returns system statistics including ComfyUI version, device info, and system resources

Copiar páginaCopiar página

GET

/

api

/

system_stats

Pruébalo

Get system statistics

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/system_stats
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/system_stats"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://cloud.comfy.org/api/system_stats', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/system_stats",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "GET",
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
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "https://cloud.comfy.org/api/system_stats"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/system_stats")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/system_stats")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

401
    
    
    {
      "system": {
        "os": "<string>",
        "python_version": "<string>",
        "embedded_python": true,
        "comfyui_version": "<string>",
        "pytorch_version": "<string>",
        "argv": [
          "<string>"
        ],
        "ram_total": 123,
        "ram_free": 123,
        "comfyui_frontend_version": "<string>",
        "workflow_templates_version": "<string>",
        "cloud_version": "<string>"
      },
      "devices": [
        {
          "name": "<string>",
          "type": "<string>",
          "vram_total": 123,
          "vram_free": 123
        }
      ]
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }

#### Respuesta

200

application/json

Success

System statistics response

​

system

object

requerido

Show child attributes

​

devices

object[]

requerido

Show child attributes

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/system/get-system-statistics.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/system/get-system-statistics)

[Get current user information](https://docs.comfy.org/es/api-reference/cloud/user/get-current-user-information)[Get workspace usage over time](https://docs.comfy.org/es/api-reference/cloud/billing/get-workspace-usage-over-time)

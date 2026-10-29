---
url: https://docs.comfy.org/es/registry/api-reference/releases/get-release-notes/
title: Get release notes - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-29T14:00:21.003833+00:00
---

# Get release notes - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/releases/get-release-notes/

Get release notes

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/releases
    
    
    import requests
    
    url = "https://api.comfy.org/releases"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.comfy.org/releases', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/releases",
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
    
    	url := "https://api.comfy.org/releases"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/releases")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/releases")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

400

500
    
    
    [
      {
        "attention": "low",
        "content": "<string>",
        "id": 123,
        "project": "comfyui",
        "published_at": "2023-11-07T05:31:56Z",
        "version": "<string>"
      }
    ]
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

Releases

# Get release notes

Copiar páginaCopiar página

Fetch release notes from Strapi with caching

Copiar páginaCopiar página

GET

/

releases

Pruébalo

Get release notes

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/releases
    
    
    import requests
    
    url = "https://api.comfy.org/releases"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.comfy.org/releases', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/releases",
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
    
    	url := "https://api.comfy.org/releases"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/releases")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/releases")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

400

500
    
    
    [
      {
        "attention": "low",
        "content": "<string>",
        "id": 123,
        "project": "comfyui",
        "published_at": "2023-11-07T05:31:56Z",
        "version": "<string>"
      }
    ]
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

#### Parámetros de consulta

​

project

enum<string>

requerido

The project to get release notes for

Opciones disponibles: 

`comfyui`, 

`comfyui_frontend`, 

`desktop`, 

`cloud`

​

current_version

string

The current version to filter release notes

​

locale

enum<string>

predeterminado:en

The locale for the release notes

Opciones disponibles: 

`en`, 

`es`, 

`fr`, 

`ja`, 

`ko`, 

`ru`, 

`zh`

​

form_factor

string

The platform requesting the release notes

#### Respuesta

200

application/json

Release notes retrieved successfully

​

attention

enum<string>

requerido

The attention level for this release

Opciones disponibles: 

`low`, 

`medium`, 

`high`

​

content

string

requerido

The content of the release note in markdown format

​

id

integer

requerido

Unique identifier for the release note

​

project

enum<string>

requerido

The project this release note belongs to

Opciones disponibles: 

`comfyui`, 

`comfyui_frontend`, 

`desktop`, 

`cloud`

​

published_at

string<date-time>

requerido

When the release note was published

​

version

string

requerido

The version of the release

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/releases/get-release-notes.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/releases/get-release-notes)

[Post proxyvidutext2video](https://docs.comfy.org/es/registry/api-reference/api-nodes/post-proxyvidutext2video)[List the models Comfy Router can run.](https://docs.comfy.org/es/registry/api-reference/comfy-router/list-the-models-comfy-router-can-run)

---
url: https://docs.comfy.org/registry/api-reference/releases/get-release-notes/
title: Get release notes - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-24T11:54:47.978953+00:00
---

# Get release notes - ComfyUI

> Source: https://docs.comfy.org/registry/api-reference/releases/get-release-notes/

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

Registry API Reference

# Get release notes

Copy pageCopy page

Fetch release notes from Strapi with caching

Copy pageCopy page

GET

/

releases

Try it

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

#### Query Parameters

​

project

enum<string>

required

The project to get release notes for

Available options: 

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

default:en

The locale for the release notes

Available options: 

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

#### Response

200

application/json

Release notes retrieved successfully

​

attention

enum<string>

required

The attention level for this release

Available options: 

`low`, 

`medium`, 

`high`

​

content

string

required

The content of the release note in markdown format

​

id

integer

required

Unique identifier for the release note

​

project

enum<string>

required

The project this release note belongs to

Available options: 

`comfyui`, 

`comfyui_frontend`, 

`desktop`, 

`cloud`

​

published_at

string<date-time>

required

When the release note was published

​

version

string

required

The version of the release

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/registry/api-reference/releases/get-release-notes.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/registry/api-reference/releases/get-release-notes)

[Get server feature flags](https://docs.comfy.org/registry/api-reference/registry/get-server-feature-flags)

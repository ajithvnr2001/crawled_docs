---
url: https://docs.comfy.org/api-reference/cloud/system/get-system-statistics/
title: Get system statistics - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:06.693354+00:00
---

# Get system statistics - ComfyUI

> Source: https://docs.comfy.org/api-reference/cloud/system/get-system-statistics/

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

Copy pageCopy page

Returns system statistics including ComfyUI version, device info, and system resources

Copy pageCopy page

GET

/

api

/

system_stats

Try it

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

#### Response

200

application/json

Success

System statistics response

​

system

object

required

Show child attributes

​

devices

object[]

required

Show child attributes

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/api-reference/cloud/system/get-system-statistics.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/cloud/system/get-system-statistics)

[Get current user informationPrevious](https://docs.comfy.org/api-reference/cloud/user/get-current-user-information)[Get workspace usage over timeNext](https://docs.comfy.org/api-reference/cloud/billing/get-workspace-usage-over-time)

⌘I

[ComfyUI home page![light logo](https://mintcdn.com/dripart/WCFdTagRdhtvk9-o/logo/light.svg?fit=max&auto=format&n=WCFdTagRdhtvk9-o&q=85&s=ec112de87239058f5a931a7e4b594965)![dark logo](https://mintcdn.com/dripart/QzWbjSCBG7w61rR3/logo/dark.svg?fit=max&auto=format&n=QzWbjSCBG7w61rR3&q=85&s=62b4d879fb3aadbd7a468d1539032d6f)](https://docs.comfy.org/)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

Resources

[installation](https://docs.comfy.org/installation/system_requirements)[Tutorials](https://docs.comfy.org/tutorials/basic/text-to-image)[Development](https://docs.comfy.org/development/overview)

Products

[Features](https://www.comfy.org/?utm_source=docs)[Gallery](https://www.comfy.org/gallery?utm_source=docs)[Download](https://www.comfy.org/download?utm_source=docs)

Company

[About](https://www.comfy.org/about?utm_source=docs)[Careers](https://www.comfy.org/careers?utm_source=docs)[Terms of Service](https://www.comfy.org/terms-of-service?utm_source=docs)[Privacy Policy](https://www.comfy.org/privacy-policy?utm_source=docs)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=dripart)

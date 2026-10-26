---
url: https://docs.comfy.org/es/api-reference/cloud/job/get-execution-history-v2/
title: Get execution history (v2) - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:24.319345+00:00
---

# Get execution history (v2) - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/job/get-execution-history-v2/

Get execution history (v2)

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/history_v2 \
      --header 'X-API-Key: <api-key>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/history_v2"
    
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {'X-API-Key': '<api-key>'}};
    
    fetch('https://cloud.comfy.org/api/history_v2', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/history_v2",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "GET",
      CURLOPT_HTTPHEADER => [
        "X-API-Key: <api-key>"
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
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "https://cloud.comfy.org/api/history_v2"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/history_v2")
      .header("X-API-Key", "<api-key>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/history_v2")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["X-API-Key"] = '<api-key>'
    
    response = http.request(request)
    puts response.read_body

200

401

500
    
    
    {
      "history": [
        {
          "prompt_id": "<string>",
          "create_time": 123,
          "workflow_id": "<string>",
          "prompt": {
            "priority": 123,
            "prompt_id": "<string>",
            "extra_data": {}
          },
          "outputs": {},
          "status": {},
          "meta": {}
        }
      ]
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }

job

# Get execution history (v2)

deprecated

Copiar páginaCopiar página

**Deprecated.** Use `/api/jobs` instead. This endpoint is maintained for ComfyUI compatibility but will be removed in a future release; no removal date set.

Retrieve execution history for the authenticated user with pagination support. Returns a lightweight history format with filtered prompt data (workflow removed from extra_pnginfo).

Copiar páginaCopiar página

GET

/

api

/

history_v2

Pruébalo

Get execution history (v2)

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/history_v2 \
      --header 'X-API-Key: <api-key>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/history_v2"
    
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {'X-API-Key': '<api-key>'}};
    
    fetch('https://cloud.comfy.org/api/history_v2', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/history_v2",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "GET",
      CURLOPT_HTTPHEADER => [
        "X-API-Key: <api-key>"
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
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "https://cloud.comfy.org/api/history_v2"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/history_v2")
      .header("X-API-Key", "<api-key>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/history_v2")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["X-API-Key"] = '<api-key>'
    
    response = http.request(request)
    puts response.read_body

200

401

500
    
    
    {
      "history": [
        {
          "prompt_id": "<string>",
          "create_time": 123,
          "workflow_id": "<string>",
          "prompt": {
            "priority": 123,
            "prompt_id": "<string>",
            "extra_data": {}
          },
          "outputs": {},
          "status": {},
          "meta": {}
        }
      ]
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }

#### Autorizaciones

​

X-API-Key

string

header

requerido

API key authentication. Generate an API key from your account settings at <https://platform.comfy.org/profile/api-keys>. Pass the key in the X-API-Key header.

#### Parámetros de consulta

​

max_items

integer

Maximum number of items to return

​

offset

integer

predeterminado:0

Starting position (default 0)

#### Respuesta

200

application/json

Success - Execution history retrieved

Execution history response with history array. Returns an object with a "history" key containing an array of history entries. Each entry includes prompt_id as a property along with execution data.

​

history

object[]

requerido

Array of history entries ordered by creation time (newest first)

Show child attributes

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/job/get-execution-history-v2.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/job/get-execution-history-v2)

[Manage execution history](https://docs.comfy.org/es/api-reference/cloud/job/manage-execution-history)[Get history for specific prompt](https://docs.comfy.org/es/api-reference/cloud/job/get-history-for-specific-prompt)

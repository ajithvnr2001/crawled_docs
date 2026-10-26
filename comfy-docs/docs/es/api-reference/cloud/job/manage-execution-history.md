---
url: https://docs.comfy.org/es/api-reference/cloud/job/manage-execution-history/
title: Manage execution history - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:25.192315+00:00
---

# Manage execution history - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/job/manage-execution-history/

Manage execution history

cURL
    
    
    curl --request POST \
      --url https://cloud.comfy.org/api/history \
      --header 'Content-Type: application/json' \
      --header 'X-API-Key: <api-key>' \
      --data '
    {
      "delete": [
        "<string>"
      ],
      "clear": true
    }
    '
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/history"
    
    payload = {
        "delete": ["<string>"],
        "clear": True
    }
    headers = {
        "X-API-Key": "<api-key>",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'POST',
      headers: {'X-API-Key': '<api-key>', 'Content-Type': 'application/json'},
      body: JSON.stringify({delete: ['<string>'], clear: true})
    };
    
    fetch('https://cloud.comfy.org/api/history', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/history",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'delete' => [
            '<string>'
        ],
        'clear' => true
      ]),
      CURLOPT_HTTPHEADER => [
        "Content-Type: application/json",
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
    	"strings"
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "https://cloud.comfy.org/api/history"
    
    	payload := strings.NewReader("{\n  \"delete\": [\n    \"<string>\"\n  ],\n  \"clear\": true\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://cloud.comfy.org/api/history")
      .header("X-API-Key", "<api-key>")
      .header("Content-Type", "application/json")
      .body("{\n  \"delete\": [\n    \"<string>\"\n  ],\n  \"clear\": true\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/history")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["X-API-Key"] = '<api-key>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"delete\": [\n    \"<string>\"\n  ],\n  \"clear\": true\n}"
    
    response = http.request(request)
    puts response.read_body

400

401

500
    
    
    {
      "code": "<string>",
      "message": "<string>"
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

# Manage execution history

Copiar páginaCopiar página

Clear all history for the authenticated user or delete specific job IDs. Supports clearing all history or deleting specific job IDs.

Copiar páginaCopiar página

POST

/

api

/

history

Pruébalo

Manage execution history

cURL
    
    
    curl --request POST \
      --url https://cloud.comfy.org/api/history \
      --header 'Content-Type: application/json' \
      --header 'X-API-Key: <api-key>' \
      --data '
    {
      "delete": [
        "<string>"
      ],
      "clear": true
    }
    '
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/history"
    
    payload = {
        "delete": ["<string>"],
        "clear": True
    }
    headers = {
        "X-API-Key": "<api-key>",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'POST',
      headers: {'X-API-Key': '<api-key>', 'Content-Type': 'application/json'},
      body: JSON.stringify({delete: ['<string>'], clear: true})
    };
    
    fetch('https://cloud.comfy.org/api/history', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/history",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'delete' => [
            '<string>'
        ],
        'clear' => true
      ]),
      CURLOPT_HTTPHEADER => [
        "Content-Type: application/json",
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
    	"strings"
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "https://cloud.comfy.org/api/history"
    
    	payload := strings.NewReader("{\n  \"delete\": [\n    \"<string>\"\n  ],\n  \"clear\": true\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://cloud.comfy.org/api/history")
      .header("X-API-Key", "<api-key>")
      .header("Content-Type", "application/json")
      .body("{\n  \"delete\": [\n    \"<string>\"\n  ],\n  \"clear\": true\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/history")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["X-API-Key"] = '<api-key>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"delete\": [\n    \"<string>\"\n  ],\n  \"clear\": true\n}"
    
    response = http.request(request)
    puts response.read_body

400

401

500
    
    
    {
      "code": "<string>",
      "message": "<string>"
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

#### Cuerpo

application/json

Request to manage history operations

​

delete

string[]

Array of job IDs to delete from history

​

clear

boolean

If true, clear all history for the authenticated user

#### Respuesta

200

Success - History management operation completed

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/job/manage-execution-history.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/job/manage-execution-history)

[Get model preview image](https://docs.comfy.org/es/api-reference/cloud/model/get-model-preview-image)[Get execution history (v2)](https://docs.comfy.org/es/api-reference/cloud/job/get-execution-history-v2)

---
url: https://docs.comfy.org/es/api-reference/cloud/job/manage-queue-operations/
title: Manage queue operations - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:25.682683+00:00
---

# Manage queue operations - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/job/manage-queue-operations/

Manage queue operations

cURL
    
    
    curl --request POST \
      --url https://cloud.comfy.org/api/queue \
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
    
    url = "https://cloud.comfy.org/api/queue"
    
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
    
    fetch('https://cloud.comfy.org/api/queue', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/queue",
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
    
    	url := "https://cloud.comfy.org/api/queue"
    
    	payload := strings.NewReader("{\n  \"delete\": [\n    \"<string>\"\n  ],\n  \"clear\": true\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://cloud.comfy.org/api/queue")
      .header("X-API-Key", "<api-key>")
      .header("Content-Type", "application/json")
      .body("{\n  \"delete\": [\n    \"<string>\"\n  ],\n  \"clear\": true\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/queue")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["X-API-Key"] = '<api-key>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"delete\": [\n    \"<string>\"\n  ],\n  \"clear\": true\n}"
    
    response = http.request(request)
    puts response.read_body

200

400

401

500
    
    
    {
      "deleted": [
        "<string>"
      ],
      "cleared": true
    }
    
    
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

# Manage queue operations

Copiar páginaCopiar página

Cancel specific PENDING jobs by ID or clear all pending jobs in the queue. Note: This endpoint only affects pending jobs. To cancel running jobs, use /api/interrupt.

Copiar páginaCopiar página

POST

/

api

/

queue

Pruébalo

Manage queue operations

cURL
    
    
    curl --request POST \
      --url https://cloud.comfy.org/api/queue \
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
    
    url = "https://cloud.comfy.org/api/queue"
    
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
    
    fetch('https://cloud.comfy.org/api/queue', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/queue",
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
    
    	url := "https://cloud.comfy.org/api/queue"
    
    	payload := strings.NewReader("{\n  \"delete\": [\n    \"<string>\"\n  ],\n  \"clear\": true\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://cloud.comfy.org/api/queue")
      .header("X-API-Key", "<api-key>")
      .header("Content-Type", "application/json")
      .body("{\n  \"delete\": [\n    \"<string>\"\n  ],\n  \"clear\": true\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/queue")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["X-API-Key"] = '<api-key>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"delete\": [\n    \"<string>\"\n  ],\n  \"clear\": true\n}"
    
    response = http.request(request)
    puts response.read_body

200

400

401

500
    
    
    {
      "deleted": [
        "<string>"
      ],
      "cleared": true
    }
    
    
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

Request to manage queue operations

​

delete

string[]

Array of PENDING job IDs to cancel

​

clear

boolean

If true, clear all pending jobs from the queue

#### Respuesta

200

application/json

Success

​

deleted

string[]

Array of job IDs that were successfully cancelled

​

cleared

boolean

Whether the queue was cleared

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/job/manage-queue-operations.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/job/manage-queue-operations)

[Get queue information](https://docs.comfy.org/es/api-reference/cloud/job/get-queue-information)[Interrupt currently running jobs](https://docs.comfy.org/es/api-reference/cloud/job/interrupt-currently-running-jobs)

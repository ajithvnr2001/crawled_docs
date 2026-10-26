---
url: https://docs.comfy.org/es/api-reference/cloud/workflow/submit-a-workflow-for-execution/
title: Submit a workflow for execution - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:26.453483+00:00
---

# Submit a workflow for execution - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/workflow/submit-a-workflow-for-execution/

Submit a workflow for execution

cURL
    
    
    curl --request POST \
      --url https://cloud.comfy.org/api/prompt \
      --header 'Content-Type: application/json' \
      --header 'X-API-Key: <api-key>' \
      --data '
    {
      "prompt": {},
      "number": 123,
      "front": true,
      "extra_data": {},
      "partial_execution_targets": [
        "<string>"
      ]
    }
    '
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/prompt"
    
    payload = {
        "prompt": {},
        "number": 123,
        "front": True,
        "extra_data": {},
        "partial_execution_targets": ["<string>"]
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
      body: JSON.stringify({
        prompt: {},
        number: 123,
        front: true,
        extra_data: {},
        partial_execution_targets: ['<string>']
      })
    };
    
    fetch('https://cloud.comfy.org/api/prompt', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/prompt",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'prompt' => [
            
        ],
        'number' => 123,
        'front' => true,
        'extra_data' => [
            
        ],
        'partial_execution_targets' => [
            '<string>'
        ]
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
    
    	url := "https://cloud.comfy.org/api/prompt"
    
    	payload := strings.NewReader("{\n  \"prompt\": {},\n  \"number\": 123,\n  \"front\": true,\n  \"extra_data\": {},\n  \"partial_execution_targets\": [\n    \"<string>\"\n  ]\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://cloud.comfy.org/api/prompt")
      .header("X-API-Key", "<api-key>")
      .header("Content-Type", "application/json")
      .body("{\n  \"prompt\": {},\n  \"number\": 123,\n  \"front\": true,\n  \"extra_data\": {},\n  \"partial_execution_targets\": [\n    \"<string>\"\n  ]\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/prompt")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["X-API-Key"] = '<api-key>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"prompt\": {},\n  \"number\": 123,\n  \"front\": true,\n  \"extra_data\": {},\n  \"partial_execution_targets\": [\n    \"<string>\"\n  ]\n}"
    
    response = http.request(request)
    puts response.read_body

200

400

402

429

500

503
    
    
    {
      "prompt_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "number": 123,
      "node_errors": {}
    }
    
    
    {}
    
    
    {}
    
    
    {}
    
    
    {}
    
    
    {}

workflow

# Submit a workflow for execution

Copiar páginaCopiar página

Submit a workflow to be executed by the backend. The workflow is a JSON object describing the nodes and their connections.

Copiar páginaCopiar página

POST

/

api

/

prompt

Pruébalo

Submit a workflow for execution

cURL
    
    
    curl --request POST \
      --url https://cloud.comfy.org/api/prompt \
      --header 'Content-Type: application/json' \
      --header 'X-API-Key: <api-key>' \
      --data '
    {
      "prompt": {},
      "number": 123,
      "front": true,
      "extra_data": {},
      "partial_execution_targets": [
        "<string>"
      ]
    }
    '
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/prompt"
    
    payload = {
        "prompt": {},
        "number": 123,
        "front": True,
        "extra_data": {},
        "partial_execution_targets": ["<string>"]
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
      body: JSON.stringify({
        prompt: {},
        number: 123,
        front: true,
        extra_data: {},
        partial_execution_targets: ['<string>']
      })
    };
    
    fetch('https://cloud.comfy.org/api/prompt', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/prompt",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'prompt' => [
            
        ],
        'number' => 123,
        'front' => true,
        'extra_data' => [
            
        ],
        'partial_execution_targets' => [
            '<string>'
        ]
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
    
    	url := "https://cloud.comfy.org/api/prompt"
    
    	payload := strings.NewReader("{\n  \"prompt\": {},\n  \"number\": 123,\n  \"front\": true,\n  \"extra_data\": {},\n  \"partial_execution_targets\": [\n    \"<string>\"\n  ]\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://cloud.comfy.org/api/prompt")
      .header("X-API-Key", "<api-key>")
      .header("Content-Type", "application/json")
      .body("{\n  \"prompt\": {},\n  \"number\": 123,\n  \"front\": true,\n  \"extra_data\": {},\n  \"partial_execution_targets\": [\n    \"<string>\"\n  ]\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/prompt")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["X-API-Key"] = '<api-key>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"prompt\": {},\n  \"number\": 123,\n  \"front\": true,\n  \"extra_data\": {},\n  \"partial_execution_targets\": [\n    \"<string>\"\n  ]\n}"
    
    response = http.request(request)
    puts response.read_body

200

400

402

429

500

503
    
    
    {
      "prompt_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "number": 123,
      "node_errors": {}
    }
    
    
    {}
    
    
    {}
    
    
    {}
    
    
    {}
    
    
    {}

#### Autorizaciones

​

X-API-Key

string

header

requerido

API key authentication. Generate an API key from your account settings at <https://platform.comfy.org/profile/api-keys>. Pass the key in the X-API-Key header.

#### Cuerpo

application/json

​

prompt

object

requerido

The workflow graph to execute

​

number

number

Priority number for the queue (lower numbers have higher priority). Note: Accepted for ComfyUI API compatibility but ignored in cloud. Cloud uses its own queue management with per-user ordering and fair scheduling.

​

front

boolean

If true, adds the prompt to the front of the queue. Note: Accepted for ComfyUI API compatibility but ignored in cloud. Cloud manages queue ordering internally based on job submission time and fair scheduling.

​

extra_data

object

Extra data to be associated with the prompt

​

partial_execution_targets

string[]

List of node names to execute

#### Respuesta

200

application/json

Success - Prompt accepted

​

prompt_id

string<uuid>

Unique identifier for the prompt execution

​

number

number

Priority number in the queue

​

node_errors

object

Any errors in the nodes of the prompt

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/workflow/submit-a-workflow-for-execution.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/workflow/submit-a-workflow-for-execution)

[Get information about current prompt executions](https://docs.comfy.org/es/api-reference/cloud/workflow/get-information-about-current-prompt-executions)[Get available workflow templates](https://docs.comfy.org/es/api-reference/cloud/workflow/get-available-workflow-templates)

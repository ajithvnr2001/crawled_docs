---
url: https://docs.comfy.org/api-reference/cloud/workflow/submit-a-workflow-for-execution/
title: Submit a workflow for execution - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:09.359018+00:00
---

# Submit a workflow for execution - ComfyUI

> Source: https://docs.comfy.org/api-reference/cloud/workflow/submit-a-workflow-for-execution/

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

Copy pageCopy page

Submit a workflow to be executed by the backend. The workflow is a JSON object describing the nodes and their connections.

Copy pageCopy page

POST

/

api

/

prompt

Try it

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

#### Authorizations

​

X-API-Key

string

header

required

API key authentication. Generate an API key from your account settings at <https://platform.comfy.org/profile/api-keys>. Pass the key in the X-API-Key header.

#### Body

application/json

​

prompt

object

required

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

#### Response

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

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/api-reference/cloud/workflow/submit-a-workflow-for-execution.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/cloud/workflow/submit-a-workflow-for-execution)

[Get information about current prompt executionsPrevious](https://docs.comfy.org/api-reference/cloud/workflow/get-information-about-current-prompt-executions)[Get available workflow templatesNext](https://docs.comfy.org/api-reference/cloud/workflow/get-available-workflow-templates)

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

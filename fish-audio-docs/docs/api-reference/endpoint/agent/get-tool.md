---
url: https://docs.fish.audio/api-reference/endpoint/agent/get-tool/
title: Get Voice Agent Tool - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-11-22T15:30:36.667480+00:00
---

# Get Voice Agent Tool - Fish Audio

> Source: https://docs.fish.audio/api-reference/endpoint/agent/get-tool/

Get Tool

cURL
    
    
    curl --request GET \
      --url https://api.fish.audio/v1/agent/tools/{tool_id} \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.fish.audio/v1/agent/tools/{tool_id}"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.fish.audio/v1/agent/tools/{tool_id}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.fish.audio/v1/agent/tools/{tool_id}",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "GET",
      CURLOPT_HTTPHEADER => [
        "Authorization: Bearer <token>"
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
    
    	url := "https://api.fish.audio/v1/agent/tools/{tool_id}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.fish.audio/v1/agent/tools/{tool_id}")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.fish.audio/v1/agent/tools/{tool_id}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

200

401

404

503
    
    
    {
      "tool_id": "<string>",
      "workspace_id": "<string>",
      "name": "<string>",
      "tool_type": "webhook",
      "method": "GET",
      "url": "<string>",
      "created_at": "2023-11-07T05:31:56Z",
      "updated_at": "2023-11-07T05:31:56Z",
      "parameters": {},
      "content_type": "<string>",
      "timeout_seconds": 123,
      "error_handling": "passthrough",
      "description": "",
      "used_by": 0,
      "arguments": [
        {
          "name": "<string>",
          "description": ""
        }
      ],
      "parameter_mode": "legacy",
      "body_template": "",
      "headers": [
        {
          "name": "<string>",
          "kind": "custom",
          "value": "<string>",
          "has_secret": false
        }
      ],
      "mock_responses": [
        {
          "name": "",
          "status_code": 200,
          "content_type": "application/json",
          "body": ""
        }
      ],
      "expects_response": true,
      "execution_mode": "blocking",
      "pre_tool_speech": {
        "mode": "auto",
        "message": ""
      },
      "signing": {
        "enabled": false,
        "secret_created_at": "2023-11-07T05:31:56Z",
        "previous_secret_expires_at": "2023-11-07T05:31:56Z"
      }
    }
    
    
    {
      "status": 123,
      "message": "<string>",
      "reason": "<string>"
    }
    
    
    {
      "status": 123,
      "message": "<string>",
      "reason": "<string>"
    }
    
    
    {
      "status": 123,
      "message": "<string>",
      "reason": "<string>"
    }

Tools

# Get Voice Agent Tool

Copy pageCopy page

Fetch one tool’s full definition.

Copy pageCopy page

GET

/

v1

/

agent

/

tools

/

{tool_id}

Try it

Get Tool

cURL
    
    
    curl --request GET \
      --url https://api.fish.audio/v1/agent/tools/{tool_id} \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.fish.audio/v1/agent/tools/{tool_id}"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.fish.audio/v1/agent/tools/{tool_id}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.fish.audio/v1/agent/tools/{tool_id}",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "GET",
      CURLOPT_HTTPHEADER => [
        "Authorization: Bearer <token>"
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
    
    	url := "https://api.fish.audio/v1/agent/tools/{tool_id}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.fish.audio/v1/agent/tools/{tool_id}")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.fish.audio/v1/agent/tools/{tool_id}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

200

401

404

503
    
    
    {
      "tool_id": "<string>",
      "workspace_id": "<string>",
      "name": "<string>",
      "tool_type": "webhook",
      "method": "GET",
      "url": "<string>",
      "created_at": "2023-11-07T05:31:56Z",
      "updated_at": "2023-11-07T05:31:56Z",
      "parameters": {},
      "content_type": "<string>",
      "timeout_seconds": 123,
      "error_handling": "passthrough",
      "description": "",
      "used_by": 0,
      "arguments": [
        {
          "name": "<string>",
          "description": ""
        }
      ],
      "parameter_mode": "legacy",
      "body_template": "",
      "headers": [
        {
          "name": "<string>",
          "kind": "custom",
          "value": "<string>",
          "has_secret": false
        }
      ],
      "mock_responses": [
        {
          "name": "",
          "status_code": 200,
          "content_type": "application/json",
          "body": ""
        }
      ],
      "expects_response": true,
      "execution_mode": "blocking",
      "pre_tool_speech": {
        "mode": "auto",
        "message": ""
      },
      "signing": {
        "enabled": false,
        "secret_created_at": "2023-11-07T05:31:56Z",
        "previous_secret_expires_at": "2023-11-07T05:31:56Z"
      }
    }
    
    
    {
      "status": 123,
      "message": "<string>",
      "reason": "<string>"
    }
    
    
    {
      "status": 123,
      "message": "<string>",
      "reason": "<string>"
    }
    
    
    {
      "status": 123,
      "message": "<string>",
      "reason": "<string>"
    }

#### Authorizations

Authorization

string

header

required

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Path Parameters

tool_id

string

required

#### Response

200

application/json

Request fulfilled, document follows

tool_id

string

required

workspace_id

string

required

name

string

required

tool_type

enum<string>

required

Available options: 

`webhook`, 

`client`

method

enum<string>

required

Available options: 

`GET`, 

`POST`, 

`PUT`, 

`PATCH`, 

`DELETE`

url

string

required

created_at

string<date-time>

required

updated_at

string<date-time>

required

parameters

Parameters · object

required

Call parameters as a JSON Schema object (draft 2020-12): `type: object` (filled in when omitted), `properties`, `required`. Standard meaning throughout: `required` means the key must be present, `type: ["string", "null"]` allows null, `minLength: 1` makes a string non-empty, `enum` and `pattern` constrain the value, `default` fills a key the model left out. Mutually exclusive with `arguments` in one request. A tool created with `parameters` starts in `parameter_mode: strict`.

Show child attributes

content_type

string

required

timeout_seconds

integer

required

error_handling

enum<string>

required

Available options: 

`passthrough`, 

`hide`

description

string

default:""

used_by

integer

default:0

How many agents reference this tool in their draft configuration.

arguments

AgentWebhookArgumentPayload · object[]

Older shape of `parameters`: each entry becomes a required string parameter. Mutually exclusive with `parameters` in one request. Reads return both, `arguments` being the string parameters of the schema.

Show child attributes

parameter_mode

enum<string>

default:legacy

Whether the agent runtime checks each call's arguments against `parameters` before running the tool. `legacy` (the default for tools created with `arguments`, and every tool from before this field existed): no check, the model's arguments run as sent. `strict` (the default for tools created with `parameters`): a call that does not satisfy the schema is refused and the model is told to ask the caller for the missing information, and the LLM provider's constrained decoding is turned on where the model supports it (OpenAI models and a custom OpenAI-compatible endpoint receive the tool with `strict: true`, Gemini on the platform's native channel runs validated function calling). Changing `parameters` never changes the mode, and the mode can be changed on its own.

Available options: 

`legacy`, 

`strict`

body_template

string

default:""

headers

PublicToolHeader · object[]

Show child attributes

mock_responses

AgentWebhookMockResponsePayload · object[]

Show child attributes

expects_response

boolean

default:true

execution_mode

enum<string>

default:blocking

Available options: 

`blocking`, 

`fire_and_forget`, 

`background`

pre_tool_speech

AgentToolPreToolSpeech · object

What the caller hears as this tool starts, when the agent's own reply has not said anything yet. `auto` (the default for a new tool): the platform decides for each call whether a line is worth saying, and the model writes the line when one is said. `static`: the agent says `message` as written (required, one language). `off`: nothing (what a tool created before this field reads as). Applies to blocking webhook tools and to client tools with `expects_response: true`. It is stored but not used for other tools.

Show child attributes

signing

AgentWebhookToolSigningStatus · object

Request signing state. Secrets are write-only: rotate returns the new one once.

Show child attributes

Was this page helpful?

YesNo

[Suggest edits](https://github.com/fishaudio/docs/edit/main/api-reference/endpoint/agent/get-tool.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/endpoint/agent/get-tool)

[Create Tool](https://docs.fish.audio/api-reference/endpoint/agent/create-tool)[Update Tool](https://docs.fish.audio/api-reference/endpoint/agent/update-tool)

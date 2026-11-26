---
url: https://docs.fish.audio/api-reference/endpoint/agent/update-test-settings/
title: Update Voice Agent Test Settings - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-11-26T17:49:32.859380+00:00
---

# Update Voice Agent Test Settings - Fish Audio

> Source: https://docs.fish.audio/api-reference/endpoint/agent/update-test-settings/

Update Test Settings

cURL
    
    
    curl --request PATCH \
      --url https://api.fish.audio/v1/agent/test-settings \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "judge": {
        "model": "<string>"
      }
    }
    '
    
    
    import requests
    
    url = "https://api.fish.audio/v1/agent/test-settings"
    
    payload = { "judge": { "model": "<string>" } }
    headers = {
        "Authorization": "Bearer <token>",
        "Content-Type": "application/json"
    }
    
    response = requests.patch(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'PATCH',
      headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
      body: JSON.stringify({judge: {model: '<string>'}})
    };
    
    fetch('https://api.fish.audio/v1/agent/test-settings', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.fish.audio/v1/agent/test-settings",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "PATCH",
      CURLOPT_POSTFIELDS => json_encode([
        'judge' => [
            'model' => '<string>'
        ]
      ]),
      CURLOPT_HTTPHEADER => [
        "Authorization: Bearer <token>",
        "Content-Type: application/json"
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
    
    	url := "https://api.fish.audio/v1/agent/test-settings"
    
    	payload := strings.NewReader("{\n  \"judge\": {\n    \"model\": \"<string>\"\n  }\n}")
    
    	req, _ := http.NewRequest("PATCH", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.patch("https://api.fish.audio/v1/agent/test-settings")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"judge\": {\n    \"model\": \"<string>\"\n  }\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.fish.audio/v1/agent/test-settings")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Patch.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"judge\": {\n    \"model\": \"<string>\"\n  }\n}"
    
    response = http.request(request)
    puts response.read_body

200

400

401

404

422

503
    
    
    {
      "workspace_id": "<string>",
      "judge": {
        "model": "<string>",
        "reasoning_level": "off"
      },
      "judge_is_default": true
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

Tests

# Update Voice Agent Test Settings

Copy pageCopy page

Change a workspace’s test settings. Omitted fields keep their value.

Copy pageCopy page

PATCH

/

v1

/

agent

/

test-settings

Try it

Update Test Settings

cURL
    
    
    curl --request PATCH \
      --url https://api.fish.audio/v1/agent/test-settings \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "judge": {
        "model": "<string>"
      }
    }
    '
    
    
    import requests
    
    url = "https://api.fish.audio/v1/agent/test-settings"
    
    payload = { "judge": { "model": "<string>" } }
    headers = {
        "Authorization": "Bearer <token>",
        "Content-Type": "application/json"
    }
    
    response = requests.patch(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'PATCH',
      headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
      body: JSON.stringify({judge: {model: '<string>'}})
    };
    
    fetch('https://api.fish.audio/v1/agent/test-settings', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.fish.audio/v1/agent/test-settings",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "PATCH",
      CURLOPT_POSTFIELDS => json_encode([
        'judge' => [
            'model' => '<string>'
        ]
      ]),
      CURLOPT_HTTPHEADER => [
        "Authorization: Bearer <token>",
        "Content-Type: application/json"
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
    
    	url := "https://api.fish.audio/v1/agent/test-settings"
    
    	payload := strings.NewReader("{\n  \"judge\": {\n    \"model\": \"<string>\"\n  }\n}")
    
    	req, _ := http.NewRequest("PATCH", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.patch("https://api.fish.audio/v1/agent/test-settings")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"judge\": {\n    \"model\": \"<string>\"\n  }\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.fish.audio/v1/agent/test-settings")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Patch.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"judge\": {\n    \"model\": \"<string>\"\n  }\n}"
    
    response = http.request(request)
    puts response.read_body

200

400

401

404

422

503
    
    
    {
      "workspace_id": "<string>",
      "judge": {
        "model": "<string>",
        "reasoning_level": "off"
      },
      "judge_is_default": true
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

#### Query Parameters

workspace_id

string | null

The workspace whose settings to use. Required when your team has more than one workspace.

#### Body

application/json

Only the fields sent change.

judge

AgentTestJudge · object | null

Null goes back to the platform default. Left out, unchanged.

Show child attributes

#### Response

200

application/json

Request fulfilled, document follows

The Tests settings of a workspace, shared by every test in it.

workspace_id

string

required

The workspace these settings belong to.

judge

AgentTestJudge · object

required

The judge of a Single Turn or Simulation test that names no `judge` of its own, with the reasoning level it judges at. Always the judge such a test is judged by.

Show child attributes

judge_is_default

boolean

required

True while the workspace has not set `judge` and reads the platform default.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/fishaudio/docs/edit/main/api-reference/endpoint/agent/update-test-settings.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/endpoint/agent/update-test-settings)

[Get Test Settings](https://docs.fish.audio/api-reference/endpoint/agent/get-test-settings)[List Test Batches](https://docs.fish.audio/api-reference/endpoint/agent/list-test-batches)

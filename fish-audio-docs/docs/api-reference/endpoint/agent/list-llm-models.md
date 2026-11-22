---
url: https://docs.fish.audio/api-reference/endpoint/agent/list-llm-models/
title: List Voice Agent LLM Models - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-11-22T15:30:35.730626+00:00
---

# List Voice Agent LLM Models - Fish Audio

> Source: https://docs.fish.audio/api-reference/endpoint/agent/list-llm-models/

List LLM Models

cURL
    
    
    curl --request GET \
      --url https://api.fish.audio/v1/agent/llm-models \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.fish.audio/v1/agent/llm-models"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.fish.audio/v1/agent/llm-models', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.fish.audio/v1/agent/llm-models",
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
    
    	url := "https://api.fish.audio/v1/agent/llm-models"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.fish.audio/v1/agent/llm-models")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.fish.audio/v1/agent/llm-models")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

200

401

503
    
    
    {
      "llm_models": [
        {
          "id": "google/gemini-3.5-flash-lite",
          "included_in_conversation_rate": true,
          "usd_per_million_tokens": {
            "input": "<string>",
            "cache_read": "<string>",
            "cache_write_5m": "<string>",
            "output": "<string>"
          },
          "long_context": {
            "over_prompt_tokens": 123,
            "usd_per_million_tokens": {
              "input": "<string>",
              "cache_read": "<string>",
              "cache_write_5m": "<string>",
              "output": "<string>"
            }
          },
          "reference_latency_ms": 123
        }
      ]
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

LLM Models

# List Voice Agent LLM Models

Copy pageCopy page

List the LLMs your team can run an agent on, each with its token rates. The rates are set by the LLM providers and change when a provider changes its pricing.

Copy pageCopy page

GET

/

v1

/

agent

/

llm-models

Try it

List LLM Models

cURL
    
    
    curl --request GET \
      --url https://api.fish.audio/v1/agent/llm-models \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.fish.audio/v1/agent/llm-models"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.fish.audio/v1/agent/llm-models', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.fish.audio/v1/agent/llm-models",
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
    
    	url := "https://api.fish.audio/v1/agent/llm-models"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.fish.audio/v1/agent/llm-models")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.fish.audio/v1/agent/llm-models")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

200

401

503
    
    
    {
      "llm_models": [
        {
          "id": "google/gemini-3.5-flash-lite",
          "included_in_conversation_rate": true,
          "usd_per_million_tokens": {
            "input": "<string>",
            "cache_read": "<string>",
            "cache_write_5m": "<string>",
            "output": "<string>"
          },
          "long_context": {
            "over_prompt_tokens": 123,
            "usd_per_million_tokens": {
              "input": "<string>",
              "cache_read": "<string>",
              "cache_write_5m": "<string>",
              "output": "<string>"
            }
          },
          "reference_latency_ms": 123
        }
      ]
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

#### Response

200

application/json

Request fulfilled, document follows

llm_models

PublicLLMModel · object[]

required

Show child attributes

Was this page helpful?

YesNo

[Suggest edits](https://github.com/fishaudio/docs/edit/main/api-reference/endpoint/agent/list-llm-models.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/endpoint/agent/list-llm-models)

[Delete Background Sound](https://docs.fish.audio/api-reference/endpoint/agent/delete-background-sound)[Search Available Phone Numbers](https://docs.fish.audio/api-reference/endpoint/agent/search-available-phone-numbers)

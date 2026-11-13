---
url: https://docs.fish.audio/api-reference/endpoint/apikey/revoke-api-keys/
title: Revoke Exposed API Keys - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-11-13T15:33:42.481734+00:00
---

# Revoke Exposed API Keys - Fish Audio

> Source: https://docs.fish.audio/api-reference/endpoint/apikey/revoke-api-keys/

Revoke publicly exposed API keys

cURL
    
    
    curl --request POST \
      --url https://api.fish.audio/apikey/revoke \
      --header 'Content-Type: application/json' \
      --data '
    {
      "credentials": [
        "<string>"
      ],
      "source": "<string>",
      "url": "<string>"
    }
    '
    
    
    import requests
    
    url = "https://api.fish.audio/apikey/revoke"
    
    payload = {
        "credentials": ["<string>"],
        "source": "<string>",
        "url": "<string>"
    }
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({credentials: ['<string>'], source: '<string>', url: '<string>'})
    };
    
    fetch('https://api.fish.audio/apikey/revoke', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.fish.audio/apikey/revoke",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'credentials' => [
            '<string>'
        ],
        'source' => '<string>',
        'url' => '<string>'
      ]),
      CURLOPT_HTTPHEADER => [
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
    
    	url := "https://api.fish.audio/apikey/revoke"
    
    	payload := strings.NewReader("{\n  \"credentials\": [\n    \"<string>\"\n  ],\n  \"source\": \"<string>\",\n  \"url\": \"<string>\"\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.fish.audio/apikey/revoke")
      .header("Content-Type", "application/json")
      .body("{\n  \"credentials\": [\n    \"<string>\"\n  ],\n  \"source\": \"<string>\",\n  \"url\": \"<string>\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.fish.audio/apikey/revoke")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"credentials\": [\n    \"<string>\"\n  ],\n  \"source\": \"<string>\",\n  \"url\": \"<string>\"\n}"
    
    response = http.request(request)
    puts response.read_body

422

429
    
    
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

API Keys

# Revoke Exposed API Keys

Copy pageCopy page

Revoke Fish Audio API keys that have been exposed, without signing in

Copy pageCopy page

POST

/

apikey

/

revoke

Try it

Revoke publicly exposed API keys

cURL
    
    
    curl --request POST \
      --url https://api.fish.audio/apikey/revoke \
      --header 'Content-Type: application/json' \
      --data '
    {
      "credentials": [
        "<string>"
      ],
      "source": "<string>",
      "url": "<string>"
    }
    '
    
    
    import requests
    
    url = "https://api.fish.audio/apikey/revoke"
    
    payload = {
        "credentials": ["<string>"],
        "source": "<string>",
        "url": "<string>"
    }
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({credentials: ['<string>'], source: '<string>', url: '<string>'})
    };
    
    fetch('https://api.fish.audio/apikey/revoke', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.fish.audio/apikey/revoke",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'credentials' => [
            '<string>'
        ],
        'source' => '<string>',
        'url' => '<string>'
      ]),
      CURLOPT_HTTPHEADER => [
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
    
    	url := "https://api.fish.audio/apikey/revoke"
    
    	payload := strings.NewReader("{\n  \"credentials\": [\n    \"<string>\"\n  ],\n  \"source\": \"<string>\",\n  \"url\": \"<string>\"\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.fish.audio/apikey/revoke")
      .header("Content-Type", "application/json")
      .body("{\n  \"credentials\": [\n    \"<string>\"\n  ],\n  \"source\": \"<string>\",\n  \"url\": \"<string>\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.fish.audio/apikey/revoke")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"credentials\": [\n    \"<string>\"\n  ],\n  \"source\": \"<string>\",\n  \"url\": \"<string>\"\n}"
    
    response = http.request(request)
    puts response.read_body

422

429
    
    
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

If you find a Fish Audio API key somewhere it shouldn’t be, such as a public repository, a log, or a support ticket, submit it here to revoke it. You don’t need an account or an API key of your own: anyone holding the key can already use it, so holding it is enough to revoke it. This endpoint is for secret scanners, partners that hold their customers’ Fish Audio keys, security researchers, and key owners. If the exposed key is yours, you can also delete it from [API Keys](https://fish.audio/app/api-keys/).

Revocation is permanent. The key stops working immediately, and any service still using it gets `401`. A revoked key can’t be restored: its owner has to create a new one.

## What happens

  * Each submitted key that matches a Fish Audio API key is deleted.
  * The key’s creator gets a security email listing the revoked keys. For a team key, the team owner gets one too.
  * The response is always the same empty `202`, whether or not any key matched, so this endpoint never reveals whether a key exists.



## Request

  * Send up to 1,000 keys per request in `credentials`.
  * `source` (who you are) and `url` (where you found the keys) are optional. Fish Audio records them to investigate the exposure; they are not included in the email to the key owner.
  * Each IP address can send 60 requests per hour. Requests over the limit get `429`.


    
    
    curl -X POST https://api.fish.audio/apikey/revoke \
      -H "Content-Type: application/json" \
      -d '{
        "credentials": ["sk-fish-..."],
        "source": "your-company",
        "url": "https://github.com/example/repo/blob/main/.env"
      }'
    

A `202` with an empty body means the request was accepted.

#### Body

application/json

credentials

string[]

required

Required array length: `1 - 1000` elements

Maximum string length: `256`

source

string | null

Maximum string length: `64`

url

string | null

Maximum string length: `2048`

#### Response

202

Request accepted, processing continues off-line

Was this page helpful?

YesNo

[Suggest edits](https://github.com/fishaudio/docs/edit/main/api-reference/endpoint/apikey/revoke-api-keys.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/endpoint/apikey/revoke-api-keys)

[Get User Package](https://docs.fish.audio/api-reference/endpoint/wallet/get-user-package)[List Models](https://docs.fish.audio/api-reference/endpoint/model/list-models)

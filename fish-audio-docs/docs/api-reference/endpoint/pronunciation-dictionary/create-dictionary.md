---
url: https://docs.fish.audio/api-reference/endpoint/pronunciation-dictionary/create-dictionary/
title: Create Dictionary - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-11-06T15:15:40.082643+00:00
---

# Create Dictionary - Fish Audio

> Source: https://docs.fish.audio/api-reference/endpoint/pronunciation-dictionary/create-dictionary/

Create a pronunciation dictionary

cURL
    
    
    curl --request POST \
      --url https://api.fish.audio/v1/pronunciation-dictionaries \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "name": "Product names",
      "description": "Brand and product pronunciations for support scripts."
    }
    '
    
    
    import requests
    
    url = "https://api.fish.audio/v1/pronunciation-dictionaries"
    
    payload = {
        "name": "Product names",
        "description": "Brand and product pronunciations for support scripts."
    }
    headers = {
        "Authorization": "Bearer <token>",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'POST',
      headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
      body: JSON.stringify({
        name: 'Product names',
        description: 'Brand and product pronunciations for support scripts.'
      })
    };
    
    fetch('https://api.fish.audio/v1/pronunciation-dictionaries', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.fish.audio/v1/pronunciation-dictionaries",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'name' => 'Product names',
        'description' => 'Brand and product pronunciations for support scripts.'
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
    
    	url := "https://api.fish.audio/v1/pronunciation-dictionaries"
    
    	payload := strings.NewReader("{\n  \"name\": \"Product names\",\n  \"description\": \"Brand and product pronunciations for support scripts.\"\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.fish.audio/v1/pronunciation-dictionaries")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"name\": \"Product names\",\n  \"description\": \"Brand and product pronunciations for support scripts.\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.fish.audio/v1/pronunciation-dictionaries")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"name\": \"Product names\",\n  \"description\": \"Brand and product pronunciations for support scripts.\"\n}"
    
    response = http.request(request)
    puts response.read_body

201

401

403

422

503
    
    
    {
      "id": "9b2f5c0d4e6a4f4c8a1d3e5f7a9b0c2d",
      "name": "Product names",
      "description": "Brand and product pronunciations for support scripts.",
      "created_at": "2026-11-05T03:21:09Z",
      "updated_at": "2026-11-05T04:02:44Z",
      "latest_version_id": "1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b",
      "item_count": 12,
      "preview_voice_id": "b1a2c3d4e5f60718293a4b5c6d7e8f90",
      "preview_model": "s2-pro"
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

Pronunciation Dictionaries

# Create Dictionary

Copy pageCopy page

Create an empty pronunciation dictionary

Copy pageCopy page

POST

/

v1

/

pronunciation-dictionaries

Try it

Create a pronunciation dictionary

cURL
    
    
    curl --request POST \
      --url https://api.fish.audio/v1/pronunciation-dictionaries \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "name": "Product names",
      "description": "Brand and product pronunciations for support scripts."
    }
    '
    
    
    import requests
    
    url = "https://api.fish.audio/v1/pronunciation-dictionaries"
    
    payload = {
        "name": "Product names",
        "description": "Brand and product pronunciations for support scripts."
    }
    headers = {
        "Authorization": "Bearer <token>",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'POST',
      headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
      body: JSON.stringify({
        name: 'Product names',
        description: 'Brand and product pronunciations for support scripts.'
      })
    };
    
    fetch('https://api.fish.audio/v1/pronunciation-dictionaries', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.fish.audio/v1/pronunciation-dictionaries",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'name' => 'Product names',
        'description' => 'Brand and product pronunciations for support scripts.'
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
    
    	url := "https://api.fish.audio/v1/pronunciation-dictionaries"
    
    	payload := strings.NewReader("{\n  \"name\": \"Product names\",\n  \"description\": \"Brand and product pronunciations for support scripts.\"\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.fish.audio/v1/pronunciation-dictionaries")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"name\": \"Product names\",\n  \"description\": \"Brand and product pronunciations for support scripts.\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.fish.audio/v1/pronunciation-dictionaries")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"name\": \"Product names\",\n  \"description\": \"Brand and product pronunciations for support scripts.\"\n}"
    
    response = http.request(request)
    puts response.read_body

201

401

403

422

503
    
    
    {
      "id": "9b2f5c0d4e6a4f4c8a1d3e5f7a9b0c2d",
      "name": "Product names",
      "description": "Brand and product pronunciations for support scripts.",
      "created_at": "2026-11-05T03:21:09Z",
      "updated_at": "2026-11-05T04:02:44Z",
      "latest_version_id": "1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b",
      "item_count": 12,
      "preview_voice_id": "b1a2c3d4e5f60718293a4b5c6d7e8f90",
      "preview_model": "s2-pro"
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

A new dictionary has no rules and no version. [Publish a version](https://docs.fish.audio/api-reference/endpoint/pronunciation-dictionary/create-version) to add rules, then reference the dictionary ID and version ID in your [TTS requests](https://docs.fish.audio/developer-guide/core-features/fine-grained-control/pronunciation-dictionaries#use-a-published-dictionary).

#### Authorizations

​

Authorization

string

header

required

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Body

application/json

​

name

string

required

Display name for the dictionary (1-128 characters).

Required string length: `1 - 128`

Example:

`"Product names"`

​

description

string

default:""

Optional free-form description (up to 1024 characters).

Maximum string length: `1024`

Example:

`"Brand and product pronunciations for support scripts."`

#### Response

201

application/json

Document created, URL follows

A pronunciation dictionary owned by the caller's team.

​

id

string

required

Stable dictionary identifier.

Example:

`"9b2f5c0d4e6a4f4c8a1d3e5f7a9b0c2d"`

​

name

string

required

Display name for the dictionary.

Example:

`"Product names"`

​

description

string

required

Free-form description shown in the web app.

Example:

`"Brand and product pronunciations for support scripts."`

​

created_at

string<date-time>

required

Creation time (UTC).

Example:

`"2026-11-05T03:21:09Z"`

​

updated_at

string<date-time>

required

Last content or metadata update time (UTC).

Example:

`"2026-11-05T04:02:44Z"`

​

latest_version_id

string | null

Identifier of the latest published version, or null when the dictionary has never been published.

Example:

`"1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b"`

​

item_count

integer

default:0

Number of rules in the latest published version.

Example:

`12`

​

preview_voice_id

string | null

Voice model last used by the dictionary's preview player, or null when it was never previewed.

Example:

`"b1a2c3d4e5f60718293a4b5c6d7e8f90"`

​

preview_model

string | null

TTS model last used by the dictionary's preview player, or null when it was never previewed.

Example:

`"s2-pro"`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/fishaudio/docs/edit/main/api-reference/endpoint/pronunciation-dictionary/create-dictionary.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/endpoint/pronunciation-dictionary/create-dictionary)

[List Dictionaries](https://docs.fish.audio/api-reference/endpoint/pronunciation-dictionary/list-dictionaries)[Get Dictionary](https://docs.fish.audio/api-reference/endpoint/pronunciation-dictionary/get-dictionary)

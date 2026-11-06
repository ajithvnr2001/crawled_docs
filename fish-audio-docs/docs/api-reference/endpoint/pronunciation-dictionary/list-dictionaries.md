---
url: https://docs.fish.audio/api-reference/endpoint/pronunciation-dictionary/list-dictionaries/
title: List Dictionaries - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-11-06T15:15:40.167620+00:00
---

# List Dictionaries - Fish Audio

> Source: https://docs.fish.audio/api-reference/endpoint/pronunciation-dictionary/list-dictionaries/

List pronunciation dictionaries

cURL
    
    
    curl --request GET \
      --url https://api.fish.audio/v1/pronunciation-dictionaries \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.fish.audio/v1/pronunciation-dictionaries"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
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
    
    	url := "https://api.fish.audio/v1/pronunciation-dictionaries"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.fish.audio/v1/pronunciation-dictionaries")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.fish.audio/v1/pronunciation-dictionaries")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

200

400

401

403

422

503
    
    
    {
      "dictionaries": [
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
      ],
      "has_more": true,
      "next_cursor": "<string>",
      "total": 3
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

Pronunciation Dictionaries

# List Dictionaries

Copy pageCopy page

List the pronunciation dictionaries of your team

Copy pageCopy page

GET

/

v1

/

pronunciation-dictionaries

Try it

List pronunciation dictionaries

cURL
    
    
    curl --request GET \
      --url https://api.fish.audio/v1/pronunciation-dictionaries \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.fish.audio/v1/pronunciation-dictionaries"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
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
    
    	url := "https://api.fish.audio/v1/pronunciation-dictionaries"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.fish.audio/v1/pronunciation-dictionaries")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.fish.audio/v1/pronunciation-dictionaries")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

200

400

401

403

422

503
    
    
    {
      "dictionaries": [
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
      ],
      "has_more": true,
      "next_cursor": "<string>",
      "total": 3
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

​

Authorization

string

header

required

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Query Parameters

​

cursor

string | null

Opaque cursor from a previous `next_cursor`.

​

page

integer | null

1-based page number; mutually exclusive with cursor.

Required range: `x >= 1`

​

include_total

boolean

default:false

Also count the filtered set on the cursor path.

​

page_size

integer

default:30

Rows per page (1-100, default 30).

Required range: `1 <= x <= 100`

#### Response

200

application/json

Request fulfilled, document follows

One page of pronunciation dictionaries.

​

dictionaries

PronunciationDictionaryV1Entity · object[]

required

Dictionaries in this page, newest updated first.

Show child attributes

​

has_more

boolean

required

Whether another page exists after this one.

​

next_cursor

string | null

Opaque cursor for the next page; pass it as `cursor`. Null when there is no next page.

​

total

integer | null

Rows matching the filters across all pages. Always set in page mode; set on the cursor path only with `include_total=true`.

Example:

`3`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/fishaudio/docs/edit/main/api-reference/endpoint/pronunciation-dictionary/list-dictionaries.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/endpoint/pronunciation-dictionary/list-dictionaries)

[Update Model](https://docs.fish.audio/api-reference/endpoint/model/update-model)[Create Dictionary](https://docs.fish.audio/api-reference/endpoint/pronunciation-dictionary/create-dictionary)

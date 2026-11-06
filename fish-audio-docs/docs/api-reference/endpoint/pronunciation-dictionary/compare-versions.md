---
url: https://docs.fish.audio/api-reference/endpoint/pronunciation-dictionary/compare-versions/
title: Compare Versions - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-11-06T15:15:40.350963+00:00
---

# Compare Versions - Fish Audio

> Source: https://docs.fish.audio/api-reference/endpoint/pronunciation-dictionary/compare-versions/

Compare two versions

cURL
    
    
    curl --request GET \
      --url https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id}/compare \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id}/compare"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id}/compare', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id}/compare",
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
    
    	url := "https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id}/compare"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id}/compare")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id}/compare")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

200

401

403

404

422

503
    
    
    {
      "version_id": "1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b",
      "base_version_id": "1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b",
      "added": 1,
      "removed": 0,
      "changed": 2,
      "rows": [
        {
          "key": "Fish",
          "value": "fɪʃ",
          "case_sensitive": false,
          "status": "changed",
          "type": "phoneme",
          "order": 0,
          "base_key": "Fish",
          "base_value": "fɪʃ",
          "base_type": "phoneme",
          "base_case_sensitive": false,
          "base_order": 0
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

# Compare Versions

Copy pageCopy page

Compare the rules of two versions of a pronunciation dictionary

Copy pageCopy page

GET

/

v1

/

pronunciation-dictionaries

/

{dictionary_id}

/

versions

/

{version_id}

/

compare

Try it

Compare two versions

cURL
    
    
    curl --request GET \
      --url https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id}/compare \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id}/compare"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id}/compare', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id}/compare",
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
    
    	url := "https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id}/compare"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id}/compare")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id}/compare")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

200

401

403

404

422

503
    
    
    {
      "version_id": "1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b",
      "base_version_id": "1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b",
      "added": 1,
      "removed": 0,
      "changed": 2,
      "rows": [
        {
          "key": "Fish",
          "value": "fɪʃ",
          "case_sensitive": false,
          "status": "changed",
          "type": "phoneme",
          "order": 0,
          "base_key": "Fish",
          "base_value": "fɪʃ",
          "base_type": "phoneme",
          "base_case_sensitive": false,
          "base_order": 0
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

`version_id` is the version you are looking at and `base_version_id` is the version it is compared with.

#### Authorizations

​

Authorization

string

header

required

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Path Parameters

​

dictionary_id

string

required

​

version_id

string

required

#### Query Parameters

​

base_version_id

string

required

Version to compare the target version against.

Example:

`"9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e"`

#### Response

200

application/json

Request fulfilled, document follows

Row-level diff between two versions of one dictionary.

​

version_id

string

required

Target (viewed) version.

Example:

`"1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b"`

​

base_version_id

string

required

Base version the target is compared against.

Example:

`"1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b"`

​

added

integer

required

Number of added rows.

Example:

`1`

​

removed

integer

required

Number of removed rows.

Example:

`0`

​

changed

integer

required

Number of changed rows.

Example:

`2`

​

rows

PronunciationDictionaryV1CompareRow · object[]

required

Per-rule diff rows in target order, with removed rows last.

Show child attributes

Was this page helpful?

YesNo

[Suggest edits](https://github.com/fishaudio/docs/edit/main/api-reference/endpoint/pronunciation-dictionary/compare-versions.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/endpoint/pronunciation-dictionary/compare-versions)

[Get Version](https://docs.fish.audio/api-reference/endpoint/pronunciation-dictionary/get-version)[Delete Version](https://docs.fish.audio/api-reference/endpoint/pronunciation-dictionary/delete-version)

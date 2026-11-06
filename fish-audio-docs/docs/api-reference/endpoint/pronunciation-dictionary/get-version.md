---
url: https://docs.fish.audio/api-reference/endpoint/pronunciation-dictionary/get-version/
title: Get Version - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-11-06T15:15:40.259683+00:00
---

# Get Version - Fish Audio

> Source: https://docs.fish.audio/api-reference/endpoint/pronunciation-dictionary/get-version/

Get a version

cURL
    
    
    curl --request GET \
      --url https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id} \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id}"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id}",
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
    
    	url := "https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id}")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id}")
    
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

503
    
    
    {
      "id": "1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b",
      "dictionary_id": "9b2f5c0d4e6a4f4c8a1d3e5f7a9b0c2d",
      "description": "Add the new product names",
      "created_at": "2026-11-05T04:02:44Z",
      "items": [
        {
          "key": "Fish Audio",
          "value": "fɪʃ ˈɔːdi.oʊ",
          "type": "phoneme",
          "case_sensitive": false
        }
      ],
      "version_number": 3,
      "added_count": 2,
      "removed_count": 0,
      "changed_count": 1,
      "item_count": 12
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

# Get Version

Copy pageCopy page

Get a published version and its rules

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

Try it

Get a version

cURL
    
    
    curl --request GET \
      --url https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id} \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id}"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id}",
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
    
    	url := "https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id}")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions/{version_id}")
    
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

503
    
    
    {
      "id": "1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b",
      "dictionary_id": "9b2f5c0d4e6a4f4c8a1d3e5f7a9b0c2d",
      "description": "Add the new product names",
      "created_at": "2026-11-05T04:02:44Z",
      "items": [
        {
          "key": "Fish Audio",
          "value": "fɪʃ ˈɔːdi.oʊ",
          "type": "phoneme",
          "case_sensitive": false
        }
      ],
      "version_number": 3,
      "added_count": 2,
      "removed_count": 0,
      "changed_count": 1,
      "item_count": 12
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

#### Path Parameters

​

dictionary_id

string

required

​

version_id

string

required

#### Response

200

application/json

Request fulfilled, document follows

A version with its full ordered rule list.

​

id

string

required

Stable version identifier.

Example:

`"1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b"`

​

dictionary_id

string

required

Dictionary this version belongs to.

Example:

`"9b2f5c0d4e6a4f4c8a1d3e5f7a9b0c2d"`

​

description

string

required

Version note entered when publishing.

Example:

`"Add the new product names"`

​

created_at

string<date-time>

required

Publish time (UTC).

Example:

`"2026-11-05T04:02:44Z"`

​

items

PronunciationDictionaryV1Item · object[]

required

Rules in application order.

Show child attributes

​

version_number

integer | null

Monotonic version number within the dictionary. Null only for versions published before version numbers existed.

Example:

`3`

​

added_count

integer

default:0

Rules added relative to the previous version.

Example:

`2`

​

removed_count

integer

default:0

Rules removed relative to the previous version.

Example:

`0`

​

changed_count

integer

default:0

Rules whose key, value, type or case sensitivity changed.

Example:

`1`

​

item_count

integer

default:0

Total number of rules in this version.

Example:

`12`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/fishaudio/docs/edit/main/api-reference/endpoint/pronunciation-dictionary/get-version.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/endpoint/pronunciation-dictionary/get-version)

[Publish Version](https://docs.fish.audio/api-reference/endpoint/pronunciation-dictionary/create-version)[Compare Versions](https://docs.fish.audio/api-reference/endpoint/pronunciation-dictionary/compare-versions)

---
url: https://docs.fish.audio/api-reference/endpoint/pronunciation-dictionary/create-version/
title: Publish Version - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-11-06T15:15:39.977855+00:00
---

# Publish Version - Fish Audio

> Source: https://docs.fish.audio/api-reference/endpoint/pronunciation-dictionary/create-version/

Publish a version

cURL
    
    
    curl --request POST \
      --url https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "expected_latest_version_id": "1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b",
      "description": "Add the new product names",
      "items": [
        {
          "key": "Fish Audio",
          "value": "fɪʃ ˈɔːdi.oʊ",
          "type": "phoneme",
          "case_sensitive": false
        }
      ]
    }
    '
    
    
    import requests
    
    url = "https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions"
    
    payload = {
        "expected_latest_version_id": "1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b",
        "description": "Add the new product names",
        "items": [
            {
                "key": "Fish Audio",
                "value": "fɪʃ ˈɔːdi.oʊ",
                "type": "phoneme",
                "case_sensitive": False
            }
        ]
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
        expected_latest_version_id: '1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b',
        description: 'Add the new product names',
        items: [
          {
            key: 'Fish Audio',
            value: 'fɪʃ ˈɔːdi.oʊ',
            type: 'phoneme',
            case_sensitive: false
          }
        ]
      })
    };
    
    fetch('https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'expected_latest_version_id' => '1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b',
        'description' => 'Add the new product names',
        'items' => [
            [
                    'key' => 'Fish Audio',
                    'value' => 'fɪʃ ˈɔːdi.oʊ',
                    'type' => 'phoneme',
                    'case_sensitive' => false
            ]
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
    
    	url := "https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions"
    
    	payload := strings.NewReader("{\n  \"expected_latest_version_id\": \"1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b\",\n  \"description\": \"Add the new product names\",\n  \"items\": [\n    {\n      \"key\": \"Fish Audio\",\n      \"value\": \"fɪʃ ˈɔːdi.oʊ\",\n      \"type\": \"phoneme\",\n      \"case_sensitive\": false\n    }\n  ]\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"expected_latest_version_id\": \"1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b\",\n  \"description\": \"Add the new product names\",\n  \"items\": [\n    {\n      \"key\": \"Fish Audio\",\n      \"value\": \"fɪʃ ˈɔːdi.oʊ\",\n      \"type\": \"phoneme\",\n      \"case_sensitive\": false\n    }\n  ]\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"expected_latest_version_id\": \"1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b\",\n  \"description\": \"Add the new product names\",\n  \"items\": [\n    {\n      \"key\": \"Fish Audio\",\n      \"value\": \"fɪʃ ˈɔːdi.oʊ\",\n      \"type\": \"phoneme\",\n      \"case_sensitive\": false\n    }\n  ]\n}"
    
    response = http.request(request)
    puts response.read_body

201

401

403

404

409

422

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

# Publish Version

Copy pageCopy page

Publish a new immutable version of a pronunciation dictionary

Copy pageCopy page

POST

/

v1

/

pronunciation-dictionaries

/

{dictionary_id}

/

versions

Try it

Publish a version

cURL
    
    
    curl --request POST \
      --url https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "expected_latest_version_id": "1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b",
      "description": "Add the new product names",
      "items": [
        {
          "key": "Fish Audio",
          "value": "fɪʃ ˈɔːdi.oʊ",
          "type": "phoneme",
          "case_sensitive": false
        }
      ]
    }
    '
    
    
    import requests
    
    url = "https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions"
    
    payload = {
        "expected_latest_version_id": "1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b",
        "description": "Add the new product names",
        "items": [
            {
                "key": "Fish Audio",
                "value": "fɪʃ ˈɔːdi.oʊ",
                "type": "phoneme",
                "case_sensitive": False
            }
        ]
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
        expected_latest_version_id: '1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b',
        description: 'Add the new product names',
        items: [
          {
            key: 'Fish Audio',
            value: 'fɪʃ ˈɔːdi.oʊ',
            type: 'phoneme',
            case_sensitive: false
          }
        ]
      })
    };
    
    fetch('https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'expected_latest_version_id' => '1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b',
        'description' => 'Add the new product names',
        'items' => [
            [
                    'key' => 'Fish Audio',
                    'value' => 'fɪʃ ˈɔːdi.oʊ',
                    'type' => 'phoneme',
                    'case_sensitive' => false
            ]
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
    
    	url := "https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions"
    
    	payload := strings.NewReader("{\n  \"expected_latest_version_id\": \"1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b\",\n  \"description\": \"Add the new product names\",\n  \"items\": [\n    {\n      \"key\": \"Fish Audio\",\n      \"value\": \"fɪʃ ˈɔːdi.oʊ\",\n      \"type\": \"phoneme\",\n      \"case_sensitive\": false\n    }\n  ]\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"expected_latest_version_id\": \"1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b\",\n  \"description\": \"Add the new product names\",\n  \"items\": [\n    {\n      \"key\": \"Fish Audio\",\n      \"value\": \"fɪʃ ˈɔːdi.oʊ\",\n      \"type\": \"phoneme\",\n      \"case_sensitive\": false\n    }\n  ]\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.fish.audio/v1/pronunciation-dictionaries/{dictionary_id}/versions")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"expected_latest_version_id\": \"1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b\",\n  \"description\": \"Add the new product names\",\n  \"items\": [\n    {\n      \"key\": \"Fish Audio\",\n      \"value\": \"fɪʃ ˈɔːdi.oʊ\",\n      \"type\": \"phoneme\",\n      \"case_sensitive\": false\n    }\n  ]\n}"
    
    response = http.request(request)
    puts response.read_body

201

401

403

404

409

422

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

Each version holds the complete, ordered rule list; send every rule you want in the new version, not only the changes. Published versions never change, so TTS requests pinned to an older version keep using its rules. Set `expected_latest_version_id` to the dictionary’s current `latest_version_id`, or `null` for the first version. If another version was published in the meantime, the request returns 409. Fetch the new latest version, merge its rules with your changes, and publish again with its ID; resending your original list would drop the other publisher’s changes. For the rule fields, rule types and limits, see [Write Pronunciation Rules](https://docs.fish.audio/developer-guide/core-features/fine-grained-control/pronunciation-dictionaries#write-pronunciation-rules).

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

#### Body

application/json

​

expected_latest_version_id

string | null

Optimistic-concurrency guard: the latest version ID the caller believes is current, or null for the first publish. A mismatch returns 409.

Example:

`"1c3e5a7b9d0f4a2c8e6b4d1f3a5c7e9b"`

​

description

string

default:""

Optional version note (up to 1024 characters).

Maximum string length: `1024`

Example:

`"Add the new product names"`

​

items

PronunciationDictionaryItemPayload · object[]

Complete ordered rule list for the new version (up to 5000 rules). Keys must be unique within the version; order is the engine's application order.

Maximum array length: `5000`

Show child attributes

#### Response

201

application/json

Document created, URL follows

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

[Suggest edits](https://github.com/fishaudio/docs/edit/main/api-reference/endpoint/pronunciation-dictionary/create-version.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/endpoint/pronunciation-dictionary/create-version)

[List Versions](https://docs.fish.audio/api-reference/endpoint/pronunciation-dictionary/list-versions)[Get Version](https://docs.fish.audio/api-reference/endpoint/pronunciation-dictionary/get-version)

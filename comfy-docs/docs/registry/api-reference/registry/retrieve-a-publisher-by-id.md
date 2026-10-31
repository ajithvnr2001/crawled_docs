---
url: https://docs.comfy.org/registry/api-reference/registry/retrieve-a-publisher-by-id/
title: Retrieve a publisher by ID - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-31T13:26:52.023123+00:00
---

# Retrieve a publisher by ID - ComfyUI

> Source: https://docs.comfy.org/registry/api-reference/registry/retrieve-a-publisher-by-id/

Retrieve a publisher by ID

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/publishers/{publisherId}
    
    
    import requests
    
    url = "https://api.comfy.org/publishers/{publisherId}"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.comfy.org/publishers/{publisherId}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/publishers/{publisherId}",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "GET",
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
    
    	url := "https://api.comfy.org/publishers/{publisherId}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/publishers/{publisherId}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/publishers/{publisherId}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

404

500
    
    
    {
      "createdAt": "2023-11-07T05:31:56Z",
      "description": "<string>",
      "id": "<string>",
      "logo": "<string>",
      "members": [
        {
          "id": "<string>",
          "role": "<string>",
          "user": {
            "email": "<string>",
            "id": "<string>",
            "name": "<string>"
          }
        }
      ],
      "name": "<string>",
      "source_code_repo": "<string>",
      "status": "PublisherStatusActive",
      "support": "<string>",
      "website": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

Registry API Reference

# Retrieve a publisher by ID

Copy pageCopy page

Copy pageCopy page

GET

/

publishers

/

{publisherId}

Try it

Retrieve a publisher by ID

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/publishers/{publisherId}
    
    
    import requests
    
    url = "https://api.comfy.org/publishers/{publisherId}"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.comfy.org/publishers/{publisherId}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/publishers/{publisherId}",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "GET",
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
    
    	url := "https://api.comfy.org/publishers/{publisherId}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/publishers/{publisherId}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/publishers/{publisherId}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

404

500
    
    
    {
      "createdAt": "2023-11-07T05:31:56Z",
      "description": "<string>",
      "id": "<string>",
      "logo": "<string>",
      "members": [
        {
          "id": "<string>",
          "role": "<string>",
          "user": {
            "email": "<string>",
            "id": "<string>",
            "name": "<string>"
          }
        }
      ],
      "name": "<string>",
      "source_code_repo": "<string>",
      "status": "PublisherStatusActive",
      "support": "<string>",
      "website": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

#### Path Parameters

​

publisherId

string

required

#### Response

200

application/json

Publisher retrieved successfully

​

createdAt

string<date-time>

The date and time the publisher was created.

​

description

string

​

id

string

The unique identifier for the publisher. It's akin to a username. Should be lowercase.

​

logo

string

URL to the publisher's logo.

​

members

object[]

A list of members in the publisher.

Show child attributes

​

name

string

​

source_code_repo

string

​

status

enum<string>

Available options: 

`PublisherStatusActive`, 

`PublisherStatusBanned`

​

support

string

​

website

string

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/registry/api-reference/registry/retrieve-a-publisher-by-id.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/registry/api-reference/registry/retrieve-a-publisher-by-id)

[Retrieve all publishers](https://docs.comfy.org/registry/api-reference/registry/retrieve-all-publishers)[Update a publisher](https://docs.comfy.org/registry/api-reference/registry/update-a-publisher)

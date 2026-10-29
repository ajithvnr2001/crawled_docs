---
url: https://docs.comfy.org/es/registry/api-reference/registry/retrieve-all-publishers-for-a-given-user/
title: Retrieve all publishers for a given user - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-29T14:00:21.077405+00:00
---

# Retrieve all publishers for a given user - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/registry/retrieve-all-publishers-for-a-given-user/

Retrieve all publishers for a given user

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/users/publishers/
    
    
    import requests
    
    url = "https://api.comfy.org/users/publishers/"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.comfy.org/users/publishers/', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/users/publishers/",
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
    
    	url := "https://api.comfy.org/users/publishers/"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/users/publishers/")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/users/publishers/")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

400

500
    
    
    [
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
    ]
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

Registry

# Retrieve all publishers for a given user

Copiar páginaCopiar página

Copiar páginaCopiar página

GET

/

users

/

publishers

/

Pruébalo

Retrieve all publishers for a given user

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/users/publishers/
    
    
    import requests
    
    url = "https://api.comfy.org/users/publishers/"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.comfy.org/users/publishers/', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/users/publishers/",
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
    
    	url := "https://api.comfy.org/users/publishers/"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/users/publishers/")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/users/publishers/")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

400

500
    
    
    [
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
    ]
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

#### Respuesta

200

application/json

A list of publishers

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

Opciones disponibles: 

`PublisherStatusActive`, 

`PublisherStatusBanned`

​

support

string

​

website

string

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/registry/retrieve-all-publishers-for-a-given-user.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/registry/retrieve-all-publishers-for-a-given-user)

[Get information about the calling user.](https://docs.comfy.org/es/registry/api-reference/registry/get-information-about-the-calling-user)[List all node versions given some filters.](https://docs.comfy.org/es/registry/api-reference/registry/list-all-node-versions-given-some-filters)

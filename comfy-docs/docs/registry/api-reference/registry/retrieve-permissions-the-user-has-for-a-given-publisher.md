---
url: https://docs.comfy.org/registry/api-reference/registry/retrieve-permissions-the-user-has-for-a-given-publisher/
title: Retrieve permissions the user has for a given publisher - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:06.514417+00:00
---

# Retrieve permissions the user has for a given publisher - ComfyUI

> Source: https://docs.comfy.org/registry/api-reference/registry/retrieve-permissions-the-user-has-for-a-given-publisher/

Retrieve permissions the user has for a given publisher

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/permissions
    
    
    import requests
    
    url = "https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/permissions"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/permissions', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/permissions",
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
    
    	url := "https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/permissions"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/permissions")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/permissions")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

400

500
    
    
    {
      "canEdit": true
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

# Retrieve permissions the user has for a given publisher

Copy pageCopy page

Copy pageCopy page

GET

/

publishers

/

{publisherId}

/

nodes

/

{nodeId}

/

permissions

Try it

Retrieve permissions the user has for a given publisher

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/permissions
    
    
    import requests
    
    url = "https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/permissions"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/permissions', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/permissions",
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
    
    	url := "https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/permissions"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/permissions")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/permissions")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body

200

400

500
    
    
    {
      "canEdit": true
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

​

nodeId

string

required

#### Response

200

application/json

A list of permissions

​

canEdit

boolean

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/registry/api-reference/registry/retrieve-permissions-the-user-has-for-a-given-publisher.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/registry/api-reference/registry/retrieve-permissions-the-user-has-for-a-given-publisher)

[Delete a publisher](https://docs.comfy.org/registry/api-reference/registry/delete-a-publisher)[Create a new personal access token](https://docs.comfy.org/registry/api-reference/registry/create-a-new-personal-access-token)

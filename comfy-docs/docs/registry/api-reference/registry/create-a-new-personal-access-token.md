---
url: https://docs.comfy.org/registry/api-reference/registry/create-a-new-personal-access-token/
title: Create a new personal access token - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:24.302286+00:00
---

# Create a new personal access token - ComfyUI

> Source: https://docs.comfy.org/registry/api-reference/registry/create-a-new-personal-access-token/

Create a new personal access token

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/publishers/{publisherId}/tokens \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "createdAt": "2023-11-07T05:31:56Z",
      "description": "<string>",
      "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "name": "<string>",
      "token": "<string>"
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/publishers/{publisherId}/tokens"
    
    payload = {
        "createdAt": "2023-11-07T05:31:56Z",
        "description": "<string>",
        "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
        "name": "<string>",
        "token": "<string>"
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
        createdAt: '2023-11-07T05:31:56Z',
        description: '<string>',
        id: '3c90c3cc-0d44-4b50-8888-8dd25736052a',
        name: '<string>',
        token: '<string>'
      })
    };
    
    fetch('https://api.comfy.org/publishers/{publisherId}/tokens', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/publishers/{publisherId}/tokens",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'createdAt' => '2023-11-07T05:31:56Z',
        'description' => '<string>',
        'id' => '3c90c3cc-0d44-4b50-8888-8dd25736052a',
        'name' => '<string>',
        'token' => '<string>'
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
    
    	url := "https://api.comfy.org/publishers/{publisherId}/tokens"
    
    	payload := strings.NewReader("{\n  \"createdAt\": \"2023-11-07T05:31:56Z\",\n  \"description\": \"<string>\",\n  \"id\": \"3c90c3cc-0d44-4b50-8888-8dd25736052a\",\n  \"name\": \"<string>\",\n  \"token\": \"<string>\"\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/publishers/{publisherId}/tokens")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"createdAt\": \"2023-11-07T05:31:56Z\",\n  \"description\": \"<string>\",\n  \"id\": \"3c90c3cc-0d44-4b50-8888-8dd25736052a\",\n  \"name\": \"<string>\",\n  \"token\": \"<string>\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/publishers/{publisherId}/tokens")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"createdAt\": \"2023-11-07T05:31:56Z\",\n  \"description\": \"<string>\",\n  \"id\": \"3c90c3cc-0d44-4b50-8888-8dd25736052a\",\n  \"name\": \"<string>\",\n  \"token\": \"<string>\"\n}"
    
    response = http.request(request)
    puts response.read_body

201

400

403

500
    
    
    {
      "token": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
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

# Create a new personal access token

Copy pageCopy page

Copy pageCopy page

POST

/

publishers

/

{publisherId}

/

tokens

Try it

Create a new personal access token

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/publishers/{publisherId}/tokens \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "createdAt": "2023-11-07T05:31:56Z",
      "description": "<string>",
      "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "name": "<string>",
      "token": "<string>"
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/publishers/{publisherId}/tokens"
    
    payload = {
        "createdAt": "2023-11-07T05:31:56Z",
        "description": "<string>",
        "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
        "name": "<string>",
        "token": "<string>"
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
        createdAt: '2023-11-07T05:31:56Z',
        description: '<string>',
        id: '3c90c3cc-0d44-4b50-8888-8dd25736052a',
        name: '<string>',
        token: '<string>'
      })
    };
    
    fetch('https://api.comfy.org/publishers/{publisherId}/tokens', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/publishers/{publisherId}/tokens",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'createdAt' => '2023-11-07T05:31:56Z',
        'description' => '<string>',
        'id' => '3c90c3cc-0d44-4b50-8888-8dd25736052a',
        'name' => '<string>',
        'token' => '<string>'
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
    
    	url := "https://api.comfy.org/publishers/{publisherId}/tokens"
    
    	payload := strings.NewReader("{\n  \"createdAt\": \"2023-11-07T05:31:56Z\",\n  \"description\": \"<string>\",\n  \"id\": \"3c90c3cc-0d44-4b50-8888-8dd25736052a\",\n  \"name\": \"<string>\",\n  \"token\": \"<string>\"\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/publishers/{publisherId}/tokens")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"createdAt\": \"2023-11-07T05:31:56Z\",\n  \"description\": \"<string>\",\n  \"id\": \"3c90c3cc-0d44-4b50-8888-8dd25736052a\",\n  \"name\": \"<string>\",\n  \"token\": \"<string>\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/publishers/{publisherId}/tokens")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"createdAt\": \"2023-11-07T05:31:56Z\",\n  \"description\": \"<string>\",\n  \"id\": \"3c90c3cc-0d44-4b50-8888-8dd25736052a\",\n  \"name\": \"<string>\",\n  \"token\": \"<string>\"\n}"
    
    response = http.request(request)
    puts response.read_body

201

400

403

500
    
    
    {
      "token": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

#### Authorizations

​

Authorization

string

header

required

Bearer token authentication. Normally a Firebase or Cloud JWT. A 'comfyui-' prefixed API key is also accepted in this header: the prefix classifies the value as an API key and it is validated exactly as if it had been sent in X-API-Key. Accepted on the operations served by the comfyFirebase auth middleware (BE-9720, parity with ingest).

#### Path Parameters

​

publisherId

string

required

#### Body

application/json

​

createdAt

string<date-time>

[Output Only]The date and time the token was created.

​

description

string

Optional. A more detailed description of the token's intended use.

​

id

string<uuid>

Unique identifier for the GitCommit

​

name

string

Required. The name of the token. Can be a simple description.

​

token

string

[Output Only]. The personal access token. Only returned during creation.

#### Response

201

application/json

Token created successfully

​

token

string

The newly created personal access token.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/registry/api-reference/registry/create-a-new-personal-access-token.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/registry/api-reference/registry/create-a-new-personal-access-token)

[Retrieve permissions the user has for a given publisherPrevious](https://docs.comfy.org/registry/api-reference/registry/retrieve-permissions-the-user-has-for-a-given-publisher)[Delete a specific personal access tokenNext](https://docs.comfy.org/registry/api-reference/registry/delete-a-specific-personal-access-token)

⌘I

[ComfyUI home page![light logo](https://mintcdn.com/dripart/WCFdTagRdhtvk9-o/logo/light.svg?fit=max&auto=format&n=WCFdTagRdhtvk9-o&q=85&s=ec112de87239058f5a931a7e4b594965)![dark logo](https://mintcdn.com/dripart/QzWbjSCBG7w61rR3/logo/dark.svg?fit=max&auto=format&n=QzWbjSCBG7w61rR3&q=85&s=62b4d879fb3aadbd7a468d1539032d6f)](https://docs.comfy.org/)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

Resources

[installation](https://docs.comfy.org/installation/system_requirements)[Tutorials](https://docs.comfy.org/tutorials/basic/text-to-image)[Development](https://docs.comfy.org/development/overview)

Products

[Features](https://www.comfy.org/?utm_source=docs)[Gallery](https://www.comfy.org/gallery?utm_source=docs)[Download](https://www.comfy.org/download?utm_source=docs)

Company

[About](https://www.comfy.org/about?utm_source=docs)[Careers](https://www.comfy.org/careers?utm_source=docs)[Terms of Service](https://www.comfy.org/terms-of-service?utm_source=docs)[Privacy Policy](https://www.comfy.org/privacy-policy?utm_source=docs)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=dripart)

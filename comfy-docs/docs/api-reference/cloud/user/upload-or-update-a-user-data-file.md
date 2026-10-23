---
url: https://docs.comfy.org/api-reference/cloud/user/upload-or-update-a-user-data-file/
title: Upload or update a user data file - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:08.353490+00:00
---

# Upload or update a user data file - ComfyUI

> Source: https://docs.comfy.org/api-reference/cloud/user/upload-or-update-a-user-data-file/

Upload or update a user data file

cURL
    
    
    curl --request POST \
      --url https://cloud.comfy.org/api/userdata/{file} \
      --header 'Content-Type: application/octet-stream' \
      --header 'X-API-Key: <api-key>' \
      --data '<string>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/userdata/{file}"
    
    payload = "<string>"
    headers = {
        "X-API-Key": "<api-key>",
        "Content-Type": "application/octet-stream"
    }
    
    response = requests.post(url, data=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'POST',
      headers: {'X-API-Key': '<api-key>', 'Content-Type': 'application/octet-stream'},
      body: '<string>'
    };
    
    fetch('https://cloud.comfy.org/api/userdata/{file}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/userdata/{file}",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => "<string>",
      CURLOPT_HTTPHEADER => [
        "Content-Type: application/octet-stream",
        "X-API-Key: <api-key>"
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
    
    	url := "https://cloud.comfy.org/api/userdata/{file}"
    
    	payload := strings.NewReader("<string>")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    	req.Header.Add("Content-Type", "application/octet-stream")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://cloud.comfy.org/api/userdata/{file}")
      .header("X-API-Key", "<api-key>")
      .header("Content-Type", "application/octet-stream")
      .body("<string>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/userdata/{file}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["X-API-Key"] = '<api-key>'
    request["Content-Type"] = 'application/octet-stream'
    request.body = "<string>"
    
    response = http.request(request)
    puts response.read_body

200

400

401

403

409

500
    
    
    {
      "path": "<string>",
      "size": 123,
      "modified": "2023-11-07T05:31:56Z"
    }
    
    
    <string>
    
    
    <string>
    
    
    <string>
    
    
    <string>
    
    
    <string>

user

# Upload or update a user data file

Copy pageCopy page

Upload a file to a user’s data directory. Optional query parameters allow control over overwrite behavior and response detail.

Copy pageCopy page

POST

/

api

/

userdata

/

{file}

Try it

Upload or update a user data file

cURL
    
    
    curl --request POST \
      --url https://cloud.comfy.org/api/userdata/{file} \
      --header 'Content-Type: application/octet-stream' \
      --header 'X-API-Key: <api-key>' \
      --data '<string>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/userdata/{file}"
    
    payload = "<string>"
    headers = {
        "X-API-Key": "<api-key>",
        "Content-Type": "application/octet-stream"
    }
    
    response = requests.post(url, data=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'POST',
      headers: {'X-API-Key': '<api-key>', 'Content-Type': 'application/octet-stream'},
      body: '<string>'
    };
    
    fetch('https://cloud.comfy.org/api/userdata/{file}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/userdata/{file}",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => "<string>",
      CURLOPT_HTTPHEADER => [
        "Content-Type: application/octet-stream",
        "X-API-Key: <api-key>"
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
    
    	url := "https://cloud.comfy.org/api/userdata/{file}"
    
    	payload := strings.NewReader("<string>")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    	req.Header.Add("Content-Type", "application/octet-stream")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://cloud.comfy.org/api/userdata/{file}")
      .header("X-API-Key", "<api-key>")
      .header("Content-Type", "application/octet-stream")
      .body("<string>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/userdata/{file}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["X-API-Key"] = '<api-key>'
    request["Content-Type"] = 'application/octet-stream'
    request.body = "<string>"
    
    response = http.request(request)
    puts response.read_body

200

400

401

403

409

500
    
    
    {
      "path": "<string>",
      "size": 123,
      "modified": "2023-11-07T05:31:56Z"
    }
    
    
    <string>
    
    
    <string>
    
    
    <string>
    
    
    <string>
    
    
    <string>

#### Authorizations

​

X-API-Key

string

header

required

API key authentication. Generate an API key from your account settings at <https://platform.comfy.org/profile/api-keys>. Pass the key in the X-API-Key header.

#### Path Parameters

​

file

string

required

The target file path (URL encoded if necessary).

#### Query Parameters

​

overwrite

enum<string>

default:true

If "false", prevents overwriting existing files. Defaults to "true".

Available options: 

`true`, 

`false`

​

full_info

enum<string>

default:false

If "true", returns detailed file info; if "false", returns only the relative path.

Available options: 

`true`, 

`false`

#### Body

application/octet-stream

The body is of type `file`.

#### Response

200

application/json

File uploaded successfully.

​

path

string

​

size

integer

​

modified

string<date-time>

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/api-reference/cloud/user/upload-or-update-a-user-data-file.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/cloud/user/upload-or-update-a-user-data-file)

[Get user data filePrevious](https://docs.comfy.org/api-reference/cloud/user/get-user-data-file)[Delete a user data fileNext](https://docs.comfy.org/api-reference/cloud/user/delete-a-user-data-file)

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

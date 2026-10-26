---
url: https://docs.comfy.org/es/api-reference/cloud/user/upload-or-update-a-user-data-file/
title: Upload or update a user data file - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:26.365535+00:00
---

# Upload or update a user data file - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/user/upload-or-update-a-user-data-file/

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

Copiar páginaCopiar página

Upload a file to a user’s data directory. Optional query parameters allow control over overwrite behavior and response detail.

Copiar páginaCopiar página

POST

/

api

/

userdata

/

{file}

Pruébalo

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

#### Autorizaciones

​

X-API-Key

string

header

requerido

API key authentication. Generate an API key from your account settings at <https://platform.comfy.org/profile/api-keys>. Pass the key in the X-API-Key header.

#### Parámetros de ruta

​

file

string

requerido

The target file path (URL encoded if necessary).

#### Parámetros de consulta

​

overwrite

enum<string>

predeterminado:true

If "false", prevents overwriting existing files. Defaults to "true".

Opciones disponibles: 

`true`, 

`false`

​

full_info

enum<string>

predeterminado:false

If "true", returns detailed file info; if "false", returns only the relative path.

Opciones disponibles: 

`true`, 

`false`

#### Cuerpo

application/octet-stream

The body is of type `file`.

#### Respuesta

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

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/user/upload-or-update-a-user-data-file.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/user/upload-or-update-a-user-data-file)

[Get user data file](https://docs.comfy.org/es/api-reference/cloud/user/get-user-data-file)[Delete a user data file](https://docs.comfy.org/es/api-reference/cloud/user/delete-a-user-data-file)

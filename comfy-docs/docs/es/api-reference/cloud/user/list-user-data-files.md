---
url: https://docs.comfy.org/es/api-reference/cloud/user/list-user-data-files/
title: List user data files - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:26.281105+00:00
---

# List user data files - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/user/list-user-data-files/

List user data files

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/userdata \
      --header 'X-API-Key: <api-key>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/userdata"
    
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {'X-API-Key': '<api-key>'}};
    
    fetch('https://cloud.comfy.org/api/userdata', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/userdata",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "GET",
      CURLOPT_HTTPHEADER => [
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
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "https://cloud.comfy.org/api/userdata"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/userdata")
      .header("X-API-Key", "<api-key>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/userdata")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["X-API-Key"] = '<api-key>'
    
    response = http.request(request)
    puts response.read_body

200

400

401

404

500
    
    
    [
      {
        "path": "<string>",
        "size": 123,
        "modified": 123
      }
    ]
    
    
    <string>
    
    
    <string>
    
    
    <string>
    
    
    <string>

user

# List user data files

Copiar páginaCopiar página

Returns a list of user data files in the specified directory, optionally recursively and with full metadata.

Copiar páginaCopiar página

GET

/

api

/

userdata

Pruébalo

List user data files

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/userdata \
      --header 'X-API-Key: <api-key>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/userdata"
    
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {'X-API-Key': '<api-key>'}};
    
    fetch('https://cloud.comfy.org/api/userdata', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/userdata",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "GET",
      CURLOPT_HTTPHEADER => [
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
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "https://cloud.comfy.org/api/userdata"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/userdata")
      .header("X-API-Key", "<api-key>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/userdata")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["X-API-Key"] = '<api-key>'
    
    response = http.request(request)
    puts response.read_body

200

400

401

404

500
    
    
    [
      {
        "path": "<string>",
        "size": 123,
        "modified": 123
      }
    ]
    
    
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

#### Parámetros de consulta

​

dir

string

requerido

The directory path to list files from. Must include trailing slash. Example: "workflows/" or "settings/"

​

recurse

boolean

predeterminado:false

If true, include files in subdirectories. Otherwise only lists files directly in the specified directory.

​

split

boolean

predeterminado:false

Whether to split file information by type. Note: Accepted for ComfyUI API compatibility but currently ignored.

​

full_info

boolean

predeterminado:false

Whether to return full file metadata. Note: Accepted for ComfyUI API compatibility but currently ignored (always returns full info).

#### Respuesta

200

application/json

A list of user data files.

​

path

string

File name or path relative to the user directory.

​

size

integer

File size in bytes.

​

modified

number<float>

UNIX timestamp of the last modification.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/user/list-user-data-files.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/user/list-user-data-files)

[Check if asset exists by hash](https://docs.comfy.org/es/api-reference/cloud/asset/check-if-asset-exists-by-hash)[Get user data file](https://docs.comfy.org/es/api-reference/cloud/user/get-user-data-file)

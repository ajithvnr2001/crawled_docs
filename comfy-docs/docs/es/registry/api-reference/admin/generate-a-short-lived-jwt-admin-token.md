---
url: https://docs.comfy.org/es/registry/api-reference/admin/generate-a-short-lived-jwt-admin-token/
title: Generate a short-lived JWT admin token - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:30.985582+00:00
---

# Generate a short-lived JWT admin token - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/admin/generate-a-short-lived-jwt-admin-token/

Generate a short-lived JWT admin token

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/admin/generate-token \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.comfy.org/admin/generate-token"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.post(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'POST', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.comfy.org/admin/generate-token', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/admin/generate-token",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
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
    
    	url := "https://api.comfy.org/admin/generate-token"
    
    	req, _ := http.NewRequest("POST", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/admin/generate-token")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/admin/generate-token")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

200

401

500
    
    
    {
      "expires_at": "2023-11-07T05:31:56Z",
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

Admin

# Generate a short-lived JWT admin token

Copiar páginaCopiar página

Generates a short-lived JWT admin token for browser-based admin operations. The user must already be authenticated with Firebase and have admin privileges. The generated token expires after 1 hour.

Copiar páginaCopiar página

POST

/

admin

/

generate-token

Pruébalo

Generate a short-lived JWT admin token

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/admin/generate-token \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.comfy.org/admin/generate-token"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.post(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'POST', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.comfy.org/admin/generate-token', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/admin/generate-token",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
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
    
    	url := "https://api.comfy.org/admin/generate-token"
    
    	req, _ := http.NewRequest("POST", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/admin/generate-token")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/admin/generate-token")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

200

401

500
    
    
    {
      "expires_at": "2023-11-07T05:31:56Z",
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

#### Autorizaciones

​

Authorization

string

header

requerido

Bearer token authentication. Normally a Firebase or Cloud JWT. A 'comfyui-' prefixed API key is also accepted in this header: the prefix classifies the value as an API key and it is validated exactly as if it had been sent in X-API-Key. Accepted on the operations served by the comfyFirebase auth middleware (BE-9720, parity with ingest).

#### Respuesta

200

application/json

JWT token generated successfully

​

expires_at

string<date-time>

requerido

When the token expires

​

token

string

requerido

The JWT admin token

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/admin/generate-a-short-lived-jwt-admin-token.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/admin/generate-a-short-lived-jwt-admin-token)

[Descripción general de la API](https://docs.comfy.org/es/registry/api-reference/overview)[Retrieve multiple node versions in a single request](https://docs.comfy.org/es/registry/api-reference/registry/retrieve-multiple-node-versions-in-a-single-request)

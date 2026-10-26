---
url: https://docs.comfy.org/es/api-reference/cloud/user/delete-a-user-data-file/
title: Delete a user data file - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:25.846412+00:00
---

# Delete a user data file - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/user/delete-a-user-data-file/

Delete a user data file

cURL
    
    
    curl --request DELETE \
      --url https://cloud.comfy.org/api/userdata/{file} \
      --header 'X-API-Key: <api-key>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/userdata/{file}"
    
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.delete(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'DELETE', headers: {'X-API-Key': '<api-key>'}};
    
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
      CURLOPT_CUSTOMREQUEST => "DELETE",
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
    
    	url := "https://cloud.comfy.org/api/userdata/{file}"
    
    	req, _ := http.NewRequest("DELETE", url, nil)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.delete("https://cloud.comfy.org/api/userdata/{file}")
      .header("X-API-Key", "<api-key>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/userdata/{file}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Delete.new(url)
    request["X-API-Key"] = '<api-key>'
    
    response = http.request(request)
    puts response.read_body

401

404

500
    
    
    <string>
    
    
    <string>
    
    
    <string>

user

# Delete a user data file

Copiar páginaCopiar página

Delete a user data file from the database. The file parameter should be the relative path within the user’s data directory.

Copiar páginaCopiar página

DELETE

/

api

/

userdata

/

{file}

Pruébalo

Delete a user data file

cURL
    
    
    curl --request DELETE \
      --url https://cloud.comfy.org/api/userdata/{file} \
      --header 'X-API-Key: <api-key>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/userdata/{file}"
    
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.delete(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'DELETE', headers: {'X-API-Key': '<api-key>'}};
    
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
      CURLOPT_CUSTOMREQUEST => "DELETE",
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
    
    	url := "https://cloud.comfy.org/api/userdata/{file}"
    
    	req, _ := http.NewRequest("DELETE", url, nil)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.delete("https://cloud.comfy.org/api/userdata/{file}")
      .header("X-API-Key", "<api-key>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/userdata/{file}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Delete.new(url)
    request["X-API-Key"] = '<api-key>'
    
    response = http.request(request)
    puts response.read_body

401

404

500
    
    
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

The file path to delete (URL encoded if necessary).

#### Respuesta

204

File deleted successfully (No Content).

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/user/delete-a-user-data-file.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/user/delete-a-user-data-file)

[Upload or update a user data file](https://docs.comfy.org/es/api-reference/cloud/user/upload-or-update-a-user-data-file)[Get current user information](https://docs.comfy.org/es/api-reference/cloud/user/get-current-user-information)

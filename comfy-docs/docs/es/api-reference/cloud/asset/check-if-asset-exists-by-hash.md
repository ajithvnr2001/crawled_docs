---
url: https://docs.comfy.org/es/api-reference/cloud/asset/check-if-asset-exists-by-hash/
title: Check if asset exists by hash - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:22.570668+00:00
---

# Check if asset exists by hash - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/asset/check-if-asset-exists-by-hash/

Check if asset exists by hash

cURL
    
    
    curl --request HEAD \
      --url https://cloud.comfy.org/api/assets/hash/{hash} \
      --header 'X-API-Key: <api-key>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/assets/hash/{hash}"
    
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.head(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'HEAD', headers: {'X-API-Key': '<api-key>'}};
    
    fetch('https://cloud.comfy.org/api/assets/hash/{hash}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/assets/hash/{hash}",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "HEAD",
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
    
    	url := "https://cloud.comfy.org/api/assets/hash/{hash}"
    
    	req, _ := http.NewRequest("HEAD", url, nil)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.head("https://cloud.comfy.org/api/assets/hash/{hash}")
      .header("X-API-Key", "<api-key>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/assets/hash/{hash}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Head.new(url)
    request["X-API-Key"] = '<api-key>'
    
    response = http.request(request)
    puts response.read_body

400

401

500
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }

asset

# Check if asset exists by hash

Copiar páginaCopiar página

Checks if content with the given hash exists in cloud storage. Returns 200 if the content exists, 404 if it doesn’t. Useful for checking availability before using `/api/assets/from-hash`.

Copiar páginaCopiar página

HEAD

/

api

/

assets

/

hash

/

{hash}

Pruébalo

Check if asset exists by hash

cURL
    
    
    curl --request HEAD \
      --url https://cloud.comfy.org/api/assets/hash/{hash} \
      --header 'X-API-Key: <api-key>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/assets/hash/{hash}"
    
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.head(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'HEAD', headers: {'X-API-Key': '<api-key>'}};
    
    fetch('https://cloud.comfy.org/api/assets/hash/{hash}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/assets/hash/{hash}",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "HEAD",
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
    
    	url := "https://cloud.comfy.org/api/assets/hash/{hash}"
    
    	req, _ := http.NewRequest("HEAD", url, nil)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.head("https://cloud.comfy.org/api/assets/hash/{hash}")
      .header("X-API-Key", "<api-key>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/assets/hash/{hash}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Head.new(url)
    request["X-API-Key"] = '<api-key>'
    
    response = http.request(request)
    puts response.read_body

400

401

500
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }

#### Autorizaciones

​

X-API-Key

string

header

requerido

API key authentication. Generate an API key from your account settings at <https://platform.comfy.org/profile/api-keys>. Pass the key in the X-API-Key header.

#### Parámetros de ruta

​

hash

string

requerido

Blake3 hash of the asset in format 'blake3:hex_digest'

Pattern: `^blake3:[a-f0-9]{64}$`

Ejemplo:

`"blake3:a1b2c3d4e5f6789012345678901234567890123456789012345678901234"`

#### Respuesta

200

Asset exists

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/asset/check-if-asset-exists-by-hash.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/asset/check-if-asset-exists-by-hash)

[Get tag histogram for filtered assets](https://docs.comfy.org/es/api-reference/cloud/asset/get-tag-histogram-for-filtered-assets)[List user data files](https://docs.comfy.org/es/api-reference/cloud/user/list-user-data-files)

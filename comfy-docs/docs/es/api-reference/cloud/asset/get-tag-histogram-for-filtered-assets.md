---
url: https://docs.comfy.org/es/api-reference/cloud/asset/get-tag-histogram-for-filtered-assets/
title: Get tag histogram for filtered assets - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:23.419524+00:00
---

# Get tag histogram for filtered assets - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/asset/get-tag-histogram-for-filtered-assets/

Get tag histogram for filtered assets

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/assets/tags/refine \
      --header 'X-API-Key: <api-key>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/assets/tags/refine"
    
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {'X-API-Key': '<api-key>'}};
    
    fetch('https://cloud.comfy.org/api/assets/tags/refine', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/assets/tags/refine",
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
    
    	url := "https://cloud.comfy.org/api/assets/tags/refine"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/assets/tags/refine")
      .header("X-API-Key", "<api-key>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/assets/tags/refine")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["X-API-Key"] = '<api-key>'
    
    response = http.request(request)
    puts response.read_body

200

400

401

500
    
    
    {
      "tag_counts": {
        "checkpoint": 32,
        "lora": 193,
        "vae": 6
      }
    }
    
    
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

# Get tag histogram for filtered assets

Copiar páginaCopiar página

Returns a histogram of tags appearing on assets matching the given filters. Useful for refining asset searches by showing available tags and their counts. Only returns tags with non-zero counts (tags that exist on matching assets).

Copiar páginaCopiar página

GET

/

api

/

assets

/

tags

/

refine

Pruébalo

Get tag histogram for filtered assets

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/assets/tags/refine \
      --header 'X-API-Key: <api-key>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/assets/tags/refine"
    
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {'X-API-Key': '<api-key>'}};
    
    fetch('https://cloud.comfy.org/api/assets/tags/refine', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/assets/tags/refine",
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
    
    	url := "https://cloud.comfy.org/api/assets/tags/refine"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/assets/tags/refine")
      .header("X-API-Key", "<api-key>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/assets/tags/refine")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["X-API-Key"] = '<api-key>'
    
    response = http.request(request)
    puts response.read_body

200

400

401

500
    
    
    {
      "tag_counts": {
        "checkpoint": 32,
        "lora": 193,
        "vae": 6
      }
    }
    
    
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

#### Parámetros de consulta

​

include_tags

string[]

Filter assets that have ALL of these tags

​

exclude_tags

string[]

Exclude assets that have ANY of these tags

​

name_contains

string

Filter assets where name contains this substring (case-insensitive)

​

metadata_filter

string

JSON object for filtering by metadata fields

​

limit

integer

predeterminado:100

Maximum number of tags to return (1-1000, default 100)

Rango requerido: `1 <= x <= 1000`

​

include_public

boolean

predeterminado:true

Whether to include public/shared assets in results

#### Respuesta

200

application/json

Success - Tag histogram returned

​

tag_counts

object

requerido

Map of tag names to their occurrence counts on matching assets

Show child attributes

Ejemplo:
    
    
    { "checkpoint": 32, "lora": 193, "vae": 6 }

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/asset/get-tag-histogram-for-filtered-assets.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/asset/get-tag-histogram-for-filtered-assets)

[List all tags](https://docs.comfy.org/es/api-reference/cloud/asset/list-all-tags)[Check if asset exists by hash](https://docs.comfy.org/es/api-reference/cloud/asset/check-if-asset-exists-by-hash)

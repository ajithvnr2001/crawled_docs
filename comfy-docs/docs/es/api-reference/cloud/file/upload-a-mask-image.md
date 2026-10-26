---
url: https://docs.comfy.org/es/api-reference/cloud/file/upload-a-mask-image/
title: Upload a mask image - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:24.136478+00:00
---

# Upload a mask image - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/file/upload-a-mask-image/

Upload a mask image

cURL
    
    
    curl --request POST \
      --url https://cloud.comfy.org/api/upload/mask \
      --header 'Content-Type: multipart/form-data' \
      --header 'X-API-Key: <api-key>' \
      --form image=@example-file \
      --form 'original_ref=<string>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/upload/mask"
    
    files = { "image": ("example-file", open("example-file", "rb")) }
    payload = { "original_ref": "<string>" }
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.post(url, data=payload, files=files, headers=headers)
    
    print(response.text)
    
    
    const form = new FormData();
    form.append('image', '<string>');
    form.append('original_ref', '<string>');
    
    const options = {method: 'POST', headers: {'X-API-Key': '<api-key>'}};
    
    options.body = form;
    
    fetch('https://cloud.comfy.org/api/upload/mask', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/upload/mask",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"original_ref\"\r\n\r\n<string>\r\n-----011000010111000001101001--",
      CURLOPT_HTTPHEADER => [
        "Content-Type: multipart/form-data",
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
    
    	url := "https://cloud.comfy.org/api/upload/mask"
    
    	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"original_ref\"\r\n\r\n<string>\r\n-----011000010111000001101001--")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://cloud.comfy.org/api/upload/mask")
      .header("X-API-Key", "<api-key>")
      .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"original_ref\"\r\n\r\n<string>\r\n-----011000010111000001101001--")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/upload/mask")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["X-API-Key"] = '<api-key>'
    request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"original_ref\"\r\n\r\n<string>\r\n-----011000010111000001101001--"
    
    response = http.request(request)
    puts response.read_body

200

400

401

500
    
    
    {
      "name": "<string>",
      "subfolder": "<string>",
      "type": "<string>",
      "metadata": {
        "is_mask": true,
        "original_hash": "<string>",
        "mask_type": "<string>",
        "related_files": {
          "mask": "<string>",
          "paint": "<string>",
          "painted": "<string>"
        }
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

file

# Upload a mask image

Copiar páginaCopiar página

Upload a mask image to be applied to an existing image.

Image limits apply to both the uploaded mask and the referenced original image:

  * Maximum file size: 50 MB
  * Maximum width/height per edge: 16384 px
  * Maximum total pixel count: 64 megapixels (67108864 pixels)



Uploads that exceed any of these limits are rejected with HTTP 400.

Copiar páginaCopiar página

POST

/

api

/

upload

/

mask

Pruébalo

Upload a mask image

cURL
    
    
    curl --request POST \
      --url https://cloud.comfy.org/api/upload/mask \
      --header 'Content-Type: multipart/form-data' \
      --header 'X-API-Key: <api-key>' \
      --form image=@example-file \
      --form 'original_ref=<string>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/upload/mask"
    
    files = { "image": ("example-file", open("example-file", "rb")) }
    payload = { "original_ref": "<string>" }
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.post(url, data=payload, files=files, headers=headers)
    
    print(response.text)
    
    
    const form = new FormData();
    form.append('image', '<string>');
    form.append('original_ref', '<string>');
    
    const options = {method: 'POST', headers: {'X-API-Key': '<api-key>'}};
    
    options.body = form;
    
    fetch('https://cloud.comfy.org/api/upload/mask', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/upload/mask",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"original_ref\"\r\n\r\n<string>\r\n-----011000010111000001101001--",
      CURLOPT_HTTPHEADER => [
        "Content-Type: multipart/form-data",
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
    
    	url := "https://cloud.comfy.org/api/upload/mask"
    
    	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"original_ref\"\r\n\r\n<string>\r\n-----011000010111000001101001--")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://cloud.comfy.org/api/upload/mask")
      .header("X-API-Key", "<api-key>")
      .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"original_ref\"\r\n\r\n<string>\r\n-----011000010111000001101001--")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/upload/mask")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["X-API-Key"] = '<api-key>'
    request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"original_ref\"\r\n\r\n<string>\r\n-----011000010111000001101001--"
    
    response = http.request(request)
    puts response.read_body

200

400

401

500
    
    
    {
      "name": "<string>",
      "subfolder": "<string>",
      "type": "<string>",
      "metadata": {
        "is_mask": true,
        "original_hash": "<string>",
        "mask_type": "<string>",
        "related_files": {
          "mask": "<string>",
          "paint": "<string>",
          "painted": "<string>"
        }
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

#### Cuerpo

multipart/form-data

​

image

file

requerido

The mask image file to upload

​

original_ref

string

requerido

JSON string containing reference to the original image

#### Respuesta

200

application/json

Mask uploaded successfully

​

name

string

Filename of the uploaded mask

​

subfolder

string

Subfolder path where mask was saved

​

type

string

Type of upload (e.g., "output")

​

metadata

object

Additional metadata for mask detection and re-editing

Show child attributes

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/file/upload-a-mask-image.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/file/upload-a-mask-image)

[Upload an image file](https://docs.comfy.org/es/api-reference/cloud/file/upload-an-image-file)[List user assets](https://docs.comfy.org/es/api-reference/cloud/asset/list-user-assets)

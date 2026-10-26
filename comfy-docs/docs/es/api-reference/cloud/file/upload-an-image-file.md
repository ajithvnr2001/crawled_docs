---
url: https://docs.comfy.org/es/api-reference/cloud/file/upload-an-image-file/
title: Upload an image file - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:24.886804+00:00
---

# Upload an image file - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/file/upload-an-image-file/

Upload an image file

cURL
    
    
    curl --request POST \
      --url https://cloud.comfy.org/api/upload/image \
      --header 'Content-Type: multipart/form-data' \
      --header 'X-API-Key: <api-key>' \
      --form image=@example-file \
      --form 'overwrite=<string>' \
      --form 'subfolder=<string>' \
      --form 'type=<string>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/upload/image"
    
    files = { "image": ("example-file", open("example-file", "rb")) }
    payload = {
        "overwrite": "<string>",
        "subfolder": "<string>",
        "type": "<string>"
    }
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.post(url, data=payload, files=files, headers=headers)
    
    print(response.text)
    
    
    const form = new FormData();
    form.append('image', '<string>');
    form.append('overwrite', '<string>');
    form.append('subfolder', '<string>');
    form.append('type', '<string>');
    
    const options = {method: 'POST', headers: {'X-API-Key': '<api-key>'}};
    
    options.body = form;
    
    fetch('https://cloud.comfy.org/api/upload/image', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/upload/image",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"overwrite\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"subfolder\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"type\"\r\n\r\n<string>\r\n-----011000010111000001101001--",
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
    
    	url := "https://cloud.comfy.org/api/upload/image"
    
    	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"overwrite\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"subfolder\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"type\"\r\n\r\n<string>\r\n-----011000010111000001101001--")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://cloud.comfy.org/api/upload/image")
      .header("X-API-Key", "<api-key>")
      .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"overwrite\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"subfolder\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"type\"\r\n\r\n<string>\r\n-----011000010111000001101001--")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/upload/image")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["X-API-Key"] = '<api-key>'
    request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"overwrite\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"subfolder\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"type\"\r\n\r\n<string>\r\n-----011000010111000001101001--"
    
    response = http.request(request)
    puts response.read_body

200

400

401

500
    
    
    {
      "name": "<string>",
      "subfolder": "<string>",
      "type": "<string>"
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

# Upload an image file

Copiar páginaCopiar página

Upload an image file to cloud storage.

Image limits:

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

image

Pruébalo

Upload an image file

cURL
    
    
    curl --request POST \
      --url https://cloud.comfy.org/api/upload/image \
      --header 'Content-Type: multipart/form-data' \
      --header 'X-API-Key: <api-key>' \
      --form image=@example-file \
      --form 'overwrite=<string>' \
      --form 'subfolder=<string>' \
      --form 'type=<string>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/upload/image"
    
    files = { "image": ("example-file", open("example-file", "rb")) }
    payload = {
        "overwrite": "<string>",
        "subfolder": "<string>",
        "type": "<string>"
    }
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.post(url, data=payload, files=files, headers=headers)
    
    print(response.text)
    
    
    const form = new FormData();
    form.append('image', '<string>');
    form.append('overwrite', '<string>');
    form.append('subfolder', '<string>');
    form.append('type', '<string>');
    
    const options = {method: 'POST', headers: {'X-API-Key': '<api-key>'}};
    
    options.body = form;
    
    fetch('https://cloud.comfy.org/api/upload/image', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/upload/image",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"overwrite\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"subfolder\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"type\"\r\n\r\n<string>\r\n-----011000010111000001101001--",
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
    
    	url := "https://cloud.comfy.org/api/upload/image"
    
    	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"overwrite\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"subfolder\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"type\"\r\n\r\n<string>\r\n-----011000010111000001101001--")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://cloud.comfy.org/api/upload/image")
      .header("X-API-Key", "<api-key>")
      .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"overwrite\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"subfolder\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"type\"\r\n\r\n<string>\r\n-----011000010111000001101001--")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/upload/image")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["X-API-Key"] = '<api-key>'
    request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"overwrite\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"subfolder\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"type\"\r\n\r\n<string>\r\n-----011000010111000001101001--"
    
    response = http.request(request)
    puts response.read_body

200

400

401

500
    
    
    {
      "name": "<string>",
      "subfolder": "<string>",
      "type": "<string>"
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

The image file to upload

​

overwrite

string

Whether to overwrite existing file (true/false). Note: Accepted for ComfyUI API compatibility but effectively ignored in cloud. Cloud uses content-addressed storage (hash-based deduplication), so identical content always maps to the same hash. Re-uploading the same content is a no-op.

​

subfolder

string

Optional subfolder path. Note: Accepted for ComfyUI API compatibility but ignored for storage. Cloud stores assets by hash only. The subfolder is returned in the response for client-side organization but is not used for server-side storage paths.

​

type

string

Upload type (defaults to "output"). Note: Accepted for ComfyUI API compatibility. Cloud stores all uploads as assets with tags rather than directory-based organization.

#### Respuesta

200

application/json

Image uploaded successfully

​

name

string

Filename of the uploaded image

​

subfolder

string

Subfolder path where image was saved

​

type

string

Type of upload (e.g., "output")

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/file/upload-an-image-file.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/file/upload-an-image-file)

[Get related mask layer files](https://docs.comfy.org/es/api-reference/cloud/file/get-related-mask-layer-files)[Upload a mask image](https://docs.comfy.org/es/api-reference/cloud/file/upload-a-mask-image)

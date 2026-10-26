---
url: https://docs.comfy.org/es/api-reference/cloud/job/interrupt-currently-running-jobs/
title: Interrupt currently running jobs - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:25.097782+00:00
---

# Interrupt currently running jobs - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/job/interrupt-currently-running-jobs/

Interrupt currently running jobs

cURL
    
    
    curl --request POST \
      --url https://cloud.comfy.org/api/interrupt \
      --header 'X-API-Key: <api-key>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/interrupt"
    
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.post(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'POST', headers: {'X-API-Key': '<api-key>'}};
    
    fetch('https://cloud.comfy.org/api/interrupt', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/interrupt",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
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
    
    	url := "https://cloud.comfy.org/api/interrupt"
    
    	req, _ := http.NewRequest("POST", url, nil)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://cloud.comfy.org/api/interrupt")
      .header("X-API-Key", "<api-key>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/interrupt")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["X-API-Key"] = '<api-key>'
    
    response = http.request(request)
    puts response.read_body

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

job

# Interrupt currently running jobs

Copiar páginaCopiar página

Cancel all currently RUNNING jobs for the authenticated user. This will interrupt any job that is currently in ‘in_progress’ status. Note: This endpoint only affects running jobs. To cancel pending jobs, use /api/queue.

Copiar páginaCopiar página

POST

/

api

/

interrupt

Pruébalo

Interrupt currently running jobs

cURL
    
    
    curl --request POST \
      --url https://cloud.comfy.org/api/interrupt \
      --header 'X-API-Key: <api-key>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/interrupt"
    
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.post(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'POST', headers: {'X-API-Key': '<api-key>'}};
    
    fetch('https://cloud.comfy.org/api/interrupt', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/interrupt",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
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
    
    	url := "https://cloud.comfy.org/api/interrupt"
    
    	req, _ := http.NewRequest("POST", url, nil)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://cloud.comfy.org/api/interrupt")
      .header("X-API-Key", "<api-key>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/interrupt")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["X-API-Key"] = '<api-key>'
    
    response = http.request(request)
    puts response.read_body

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

#### Autorizaciones

​

X-API-Key

string

header

requerido

API key authentication. Generate an API key from your account settings at <https://platform.comfy.org/profile/api-keys>. Pass the key in the X-API-Key header.

#### Respuesta

200

Success - Job interrupted or no running job found

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/job/interrupt-currently-running-jobs.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/job/interrupt-currently-running-jobs)

[Manage queue operations](https://docs.comfy.org/es/api-reference/cloud/job/manage-queue-operations)[Get job status](https://docs.comfy.org/es/api-reference/cloud/job/get-job-status)

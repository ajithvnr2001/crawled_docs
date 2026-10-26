---
url: https://docs.comfy.org/es/api-reference/cloud/job/get-job-status/
title: Get job status - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:24.501727+00:00
---

# Get job status - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/job/get-job-status/

Get job status

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/job/{job_id}/status \
      --header 'X-API-Key: <api-key>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/job/{job_id}/status"
    
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {'X-API-Key': '<api-key>'}};
    
    fetch('https://cloud.comfy.org/api/job/{job_id}/status', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/job/{job_id}/status",
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
    
    	url := "https://cloud.comfy.org/api/job/{job_id}/status"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/job/{job_id}/status")
      .header("X-API-Key", "<api-key>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/job/{job_id}/status")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["X-API-Key"] = '<api-key>'
    
    response = http.request(request)
    puts response.read_body

200

401

403

404

500
    
    
    {
      "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "status": "waiting_to_dispatch",
      "created_at": "2023-11-07T05:31:56Z",
      "updated_at": "2023-11-07T05:31:56Z",
      "last_state_update": "2023-11-07T05:31:56Z",
      "assigned_inference": "<string>",
      "error_message": "<string>"
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
    
    
    {
      "code": "<string>",
      "message": "<string>"
    }

job

# Get job status

Copiar páginaCopiar página

Returns the current status of a specific job by ID

Copiar páginaCopiar página

GET

/

api

/

job

/

{job_id}

/

status

Pruébalo

Get job status

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/job/{job_id}/status \
      --header 'X-API-Key: <api-key>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/job/{job_id}/status"
    
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {'X-API-Key': '<api-key>'}};
    
    fetch('https://cloud.comfy.org/api/job/{job_id}/status', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/job/{job_id}/status",
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
    
    	url := "https://cloud.comfy.org/api/job/{job_id}/status"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/job/{job_id}/status")
      .header("X-API-Key", "<api-key>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/job/{job_id}/status")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["X-API-Key"] = '<api-key>'
    
    response = http.request(request)
    puts response.read_body

200

401

403

404

500
    
    
    {
      "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "status": "waiting_to_dispatch",
      "created_at": "2023-11-07T05:31:56Z",
      "updated_at": "2023-11-07T05:31:56Z",
      "last_state_update": "2023-11-07T05:31:56Z",
      "assigned_inference": "<string>",
      "error_message": "<string>"
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

job_id

string<uuid>

requerido

The unique ID of the job

#### Respuesta

200

application/json

Success - Job status returned

Job status information

​

id

string<uuid>

requerido

The job ID

​

status

enum<string>

requerido

Current job status

Opciones disponibles: 

`waiting_to_dispatch`, 

`pending`, 

`in_progress`, 

`completed`, 

`error`, 

`cancelled`

​

created_at

string<date-time>

requerido

When the job was created

​

updated_at

string<date-time>

requerido

When the job was last updated

​

last_state_update

string<date-time>

When the job status was last changed

​

assigned_inference

string | null

The inference instance assigned to this job (if any)

​

error_message

string | null

Error message if the job failed

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/job/get-job-status.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/job/get-job-status)

[Interrupt currently running jobs](https://docs.comfy.org/es/api-reference/cloud/job/interrupt-currently-running-jobs)[View a file](https://docs.comfy.org/es/api-reference/cloud/file/view-a-file)

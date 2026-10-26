---
url: https://docs.comfy.org/es/api-reference/cloud/job/get-full-job-details/
title: Get full job details - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:24.721215+00:00
---

# Get full job details - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/job/get-full-job-details/

Get full job details

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/jobs/{job_id} \
      --header 'X-API-Key: <api-key>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/jobs/{job_id}"
    
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {'X-API-Key': '<api-key>'}};
    
    fetch('https://cloud.comfy.org/api/jobs/{job_id}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/jobs/{job_id}",
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
    
    	url := "https://cloud.comfy.org/api/jobs/{job_id}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/jobs/{job_id}")
      .header("X-API-Key", "<api-key>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/jobs/{job_id}")
    
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
      "status": "pending",
      "create_time": 123,
      "update_time": 123,
      "workflow": {},
      "execution_error": {
        "node_id": "<string>",
        "node_type": "<string>",
        "exception_message": "<string>",
        "exception_type": "<string>",
        "traceback": [
          "<string>"
        ],
        "current_inputs": {},
        "current_outputs": {}
      },
      "outputs": {},
      "preview_output": {},
      "outputs_count": 123,
      "workflow_id": "<string>",
      "execution_status": {},
      "execution_meta": {}
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

# Get full job details

Copiar páginaCopiar página

Retrieve complete details for a specific job including workflow and outputs. Used for detail views, workflow re-execution, and debugging.

Copiar páginaCopiar página

GET

/

api

/

jobs

/

{job_id}

Pruébalo

Get full job details

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/jobs/{job_id} \
      --header 'X-API-Key: <api-key>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/jobs/{job_id}"
    
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {'X-API-Key': '<api-key>'}};
    
    fetch('https://cloud.comfy.org/api/jobs/{job_id}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/jobs/{job_id}",
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
    
    	url := "https://cloud.comfy.org/api/jobs/{job_id}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/jobs/{job_id}")
      .header("X-API-Key", "<api-key>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/jobs/{job_id}")
    
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
      "status": "pending",
      "create_time": 123,
      "update_time": 123,
      "workflow": {},
      "execution_error": {
        "node_id": "<string>",
        "node_type": "<string>",
        "exception_message": "<string>",
        "exception_type": "<string>",
        "traceback": [
          "<string>"
        ],
        "current_inputs": {},
        "current_outputs": {}
      },
      "outputs": {},
      "preview_output": {},
      "outputs_count": 123,
      "workflow_id": "<string>",
      "execution_status": {},
      "execution_meta": {}
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

Job identifier (UUID)

#### Respuesta

200

application/json

Success - Job details retrieved

Full job details including workflow and outputs

​

id

string<uuid>

requerido

Unique job identifier

​

status

enum<string>

requerido

User-friendly job status

Opciones disponibles: 

`pending`, 

`in_progress`, 

`completed`, 

`failed`, 

`cancelled`

​

create_time

integer<int64>

requerido

Job creation timestamp (Unix timestamp in seconds)

​

update_time

integer<int64>

requerido

Last update timestamp (Unix timestamp in seconds)

​

workflow

object

Full ComfyUI workflow (10-100KB, omitted if not available)

​

execution_error

object

Detailed execution error from ComfyUI (only for failed jobs with structured error data)

Show child attributes

​

outputs

object

Full outputs object from ComfyUI (only for terminal states)

​

preview_output

object

Primary preview output (only for terminal states)

​

outputs_count

integer

Total number of output files (omitted for non-terminal states)

​

workflow_id

string

UUID identifying the workflow graph definition

​

execution_status

object

ComfyUI execution status and timeline (only for terminal states)

​

execution_meta

object

Node-level execution metadata (only for terminal states)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/job/get-full-job-details.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/job/get-full-job-details)

[List jobs with pagination and filtering](https://docs.comfy.org/es/api-reference/cloud/job/list-jobs-with-pagination-and-filtering)[Get queue information](https://docs.comfy.org/es/api-reference/cloud/job/get-queue-information)

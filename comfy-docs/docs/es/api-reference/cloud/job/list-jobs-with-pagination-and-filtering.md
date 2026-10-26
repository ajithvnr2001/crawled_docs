---
url: https://docs.comfy.org/es/api-reference/cloud/job/list-jobs-with-pagination-and-filtering/
title: List jobs with pagination and filtering - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:24.985099+00:00
---

# List jobs with pagination and filtering - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/job/list-jobs-with-pagination-and-filtering/

List jobs with pagination and filtering

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/jobs \
      --header 'X-API-Key: <api-key>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/jobs"
    
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {'X-API-Key': '<api-key>'}};
    
    fetch('https://cloud.comfy.org/api/jobs', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/jobs",
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
    
    	url := "https://cloud.comfy.org/api/jobs"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/jobs")
      .header("X-API-Key", "<api-key>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/jobs")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["X-API-Key"] = '<api-key>'
    
    response = http.request(request)
    puts response.read_body

200

401

500
    
    
    {
      "jobs": [
        {
          "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
          "status": "pending",
          "create_time": 123,
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
          "preview_output": {},
          "outputs_count": 123,
          "workflow_id": "<string>",
          "execution_start_time": 123,
          "execution_end_time": 123
        }
      ],
      "pagination": {
        "offset": 1,
        "limit": 2,
        "total": 1,
        "has_more": true
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

job

# List jobs with pagination and filtering

Copiar páginaCopiar página

Retrieve a paginated list of jobs for the authenticated user. Returns lightweight job data optimized for list views. Workflow and full outputs are excluded to reduce payload size.

Copiar páginaCopiar página

GET

/

api

/

jobs

Pruébalo

List jobs with pagination and filtering

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/jobs \
      --header 'X-API-Key: <api-key>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/jobs"
    
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {'X-API-Key': '<api-key>'}};
    
    fetch('https://cloud.comfy.org/api/jobs', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/jobs",
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
    
    	url := "https://cloud.comfy.org/api/jobs"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/jobs")
      .header("X-API-Key", "<api-key>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/jobs")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["X-API-Key"] = '<api-key>'
    
    response = http.request(request)
    puts response.read_body

200

401

500
    
    
    {
      "jobs": [
        {
          "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
          "status": "pending",
          "create_time": 123,
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
          "preview_output": {},
          "outputs_count": 123,
          "workflow_id": "<string>",
          "execution_start_time": 123,
          "execution_end_time": 123
        }
      ],
      "pagination": {
        "offset": 1,
        "limit": 2,
        "total": 1,
        "has_more": true
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

#### Autorizaciones

​

X-API-Key

string

header

requerido

API key authentication. Generate an API key from your account settings at <https://platform.comfy.org/profile/api-keys>. Pass the key in the X-API-Key header.

#### Parámetros de consulta

​

status

string

Filter by one or more statuses (comma-separated). If not provided, returns all jobs.

​

workflow_id

string

Filter by workflow ID (exact match)

​

output_type

enum<string>

Filter by output media type (only applies to completed jobs with outputs)

Opciones disponibles: 

`image`, 

`video`, 

`audio`

​

sort_by

enum<string>

predeterminado:create_time

Field to sort by (create_time = when job was submitted, execution_time = how long workflow took to run)

Opciones disponibles: 

`create_time`, 

`execution_time`

​

sort_order

enum<string>

predeterminado:desc

Sort direction (asc = ascending, desc = descending)

Opciones disponibles: 

`asc`, 

`desc`

​

offset

integer

predeterminado:0

Pagination offset (0-based)

Rango requerido: `x >= 0`

​

limit

integer

predeterminado:100

Maximum items per page (1-1000)

Rango requerido: `1 <= x <= 1000`

#### Respuesta

200

application/json

Success - Jobs retrieved

​

jobs

object[]

requerido

Array of jobs ordered by specified sort field

Show child attributes

​

pagination

object

requerido

Show child attributes

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/job/list-jobs-with-pagination-and-filtering.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/job/list-jobs-with-pagination-and-filtering)

[Get history for specific prompt](https://docs.comfy.org/es/api-reference/cloud/job/get-history-for-specific-prompt)[Get full job details](https://docs.comfy.org/es/api-reference/cloud/job/get-full-job-details)

---
url: https://docs.comfy.org/api-reference/cloud/job/get-full-job-details/
title: Get full job details - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:46:19.037391+00:00
---

# Get full job details - ComfyUI

> Source: https://docs.comfy.org/api-reference/cloud/job/get-full-job-details/

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

Copy pageCopy page

Retrieve complete details for a specific job including workflow and outputs. Used for detail views, workflow re-execution, and debugging.

Copy pageCopy page

GET

/

api

/

jobs

/

{job_id}

Try it

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

#### Authorizations

​

X-API-Key

string

header

required

API key authentication. Generate an API key from your account settings at <https://platform.comfy.org/profile/api-keys>. Pass the key in the X-API-Key header.

#### Path Parameters

​

job_id

string<uuid>

required

Job identifier (UUID)

#### Response

200

application/json

Success - Job details retrieved

Full job details including workflow and outputs

​

id

string<uuid>

required

Unique job identifier

​

status

enum<string>

required

User-friendly job status

Available options: 

`pending`, 

`in_progress`, 

`completed`, 

`failed`, 

`cancelled`

​

create_time

integer<int64>

required

Job creation timestamp (Unix timestamp in seconds)

​

update_time

integer<int64>

required

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

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/api-reference/cloud/job/get-full-job-details.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/cloud/job/get-full-job-details)

[List jobs with pagination and filteringPrevious](https://docs.comfy.org/api-reference/cloud/job/list-jobs-with-pagination-and-filtering)[Get queue informationNext](https://docs.comfy.org/api-reference/cloud/job/get-queue-information)

⌘I

[ComfyUI home page![light logo](https://mintcdn.com/dripart/WCFdTagRdhtvk9-o/logo/light.svg?fit=max&auto=format&n=WCFdTagRdhtvk9-o&q=85&s=ec112de87239058f5a931a7e4b594965)![dark logo](https://mintcdn.com/dripart/QzWbjSCBG7w61rR3/logo/dark.svg?fit=max&auto=format&n=QzWbjSCBG7w61rR3&q=85&s=62b4d879fb3aadbd7a468d1539032d6f)](https://docs.comfy.org/)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

Resources

[installation](https://docs.comfy.org/installation/system_requirements)[Tutorials](https://docs.comfy.org/tutorials/basic/text-to-image)[Development](https://docs.comfy.org/development/overview)

Products

[Features](https://www.comfy.org/?utm_source=docs)[Gallery](https://www.comfy.org/gallery?utm_source=docs)[Download](https://www.comfy.org/download?utm_source=docs)

Company

[About](https://www.comfy.org/about?utm_source=docs)[Careers](https://www.comfy.org/careers?utm_source=docs)[Terms of Service](https://www.comfy.org/terms-of-service?utm_source=docs)[Privacy Policy](https://www.comfy.org/privacy-policy?utm_source=docs)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=dripart)

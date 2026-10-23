---
url: https://docs.comfy.org/api-reference/cloud/job/list-jobs-with-pagination-and-filtering/
title: List jobs with pagination and filtering - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:04.829592+00:00
---

# List jobs with pagination and filtering - ComfyUI

> Source: https://docs.comfy.org/api-reference/cloud/job/list-jobs-with-pagination-and-filtering/

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

Copy pageCopy page

Retrieve a paginated list of jobs for the authenticated user. Returns lightweight job data optimized for list views. Workflow and full outputs are excluded to reduce payload size.

Copy pageCopy page

GET

/

api

/

jobs

Try it

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

#### Authorizations

​

X-API-Key

string

header

required

API key authentication. Generate an API key from your account settings at <https://platform.comfy.org/profile/api-keys>. Pass the key in the X-API-Key header.

#### Query Parameters

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

Available options: 

`image`, 

`video`, 

`audio`

​

sort_by

enum<string>

default:create_time

Field to sort by (create_time = when job was submitted, execution_time = how long workflow took to run)

Available options: 

`create_time`, 

`execution_time`

​

sort_order

enum<string>

default:desc

Sort direction (asc = ascending, desc = descending)

Available options: 

`asc`, 

`desc`

​

offset

integer

default:0

Pagination offset (0-based)

Required range: `x >= 0`

​

limit

integer

default:100

Maximum items per page (1-1000)

Required range: `1 <= x <= 1000`

#### Response

200

application/json

Success - Jobs retrieved

​

jobs

object[]

required

Array of jobs ordered by specified sort field

Show child attributes

​

pagination

object

required

Show child attributes

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/api-reference/cloud/job/list-jobs-with-pagination-and-filtering.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/cloud/job/list-jobs-with-pagination-and-filtering)

[Get history for specific promptPrevious](https://docs.comfy.org/api-reference/cloud/job/get-history-for-specific-prompt)[Get full job detailsNext](https://docs.comfy.org/api-reference/cloud/job/get-full-job-details)

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

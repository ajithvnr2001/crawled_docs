---
url: https://docs.comfy.org/api-reference/cloud/billing/get-workspace-usage-over-time/
title: Get workspace usage over time - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:46:18.201691+00:00
---

# Get workspace usage over time - ComfyUI

> Source: https://docs.comfy.org/api-reference/cloud/billing/get-workspace-usage-over-time/

Get workspace usage over time

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/billing/usage/timeseries \
      --header 'X-API-Key: <api-key>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/billing/usage/timeseries"
    
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {'X-API-Key': '<api-key>'}};
    
    fetch('https://cloud.comfy.org/api/billing/usage/timeseries', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/billing/usage/timeseries",
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
    
    	url := "https://cloud.comfy.org/api/billing/usage/timeseries"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/billing/usage/timeseries")
      .header("X-API-Key", "<api-key>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/billing/usage/timeseries")
    
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
      "group_by": "model",
      "granularity": "hour",
      "starting_on": "2023-11-07T05:31:56Z",
      "ending_before": "2023-11-07T05:31:56Z",
      "groups": [
        "<string>"
      ],
      "buckets": [
        {
          "period_start": "2023-11-07T05:31:56Z",
          "period_end": "2023-11-07T05:31:56Z",
          "group_key": "google/nano-banana-2",
          "cost_micros": 1250000
        }
      ],
      "breakdown": [
        {
          "group_key": "google/nano-banana-2",
          "cost_micros": 1250000,
          "share": 0.42
        }
      ],
      "summary": {
        "spend_micros": 2975000,
        "balance": {
          "amount_micros": 4250,
          "prepaid_balance_micros": 2250,
          "cloud_credit_balance_micros": 2000,
          "currency": "USD"
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

billing

# Get workspace usage over time

Copy pageCopy page

Returns billed usage for the workspace the API key belongs to, split into time buckets and grouped by model, endpoint, or product. Use it to reconcile spend, attribute cost across models, or feed an internal cost report.

**Units.** `cost_micros` and `spend_micros` are millionths of a US dollar, so divide by 1,000,000 to get dollars. The fields under `summary.balance` are the exception: despite their `_micros` suffix they are **cents** , so divide those by 100.

**Freshness.** Figures are drawn from your invoices rather than from live request traffic, so very recent usage may not appear yet. Treat this as a reporting surface, not a real-time meter.

**Empty results.** A workspace that has not been billed yet returns empty `groups`, `buckets`, and `breakdown` arrays with a 200, not an error.

Copy pageCopy page

GET

/

api

/

billing

/

usage

/

timeseries

Try it

Get workspace usage over time

cURL
    
    
    curl --request GET \
      --url https://cloud.comfy.org/api/billing/usage/timeseries \
      --header 'X-API-Key: <api-key>'
    
    
    import requests
    
    url = "https://cloud.comfy.org/api/billing/usage/timeseries"
    
    headers = {"X-API-Key": "<api-key>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {'X-API-Key': '<api-key>'}};
    
    fetch('https://cloud.comfy.org/api/billing/usage/timeseries', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://cloud.comfy.org/api/billing/usage/timeseries",
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
    
    	url := "https://cloud.comfy.org/api/billing/usage/timeseries"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("X-API-Key", "<api-key>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://cloud.comfy.org/api/billing/usage/timeseries")
      .header("X-API-Key", "<api-key>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://cloud.comfy.org/api/billing/usage/timeseries")
    
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
      "group_by": "model",
      "granularity": "hour",
      "starting_on": "2023-11-07T05:31:56Z",
      "ending_before": "2023-11-07T05:31:56Z",
      "groups": [
        "<string>"
      ],
      "buckets": [
        {
          "period_start": "2023-11-07T05:31:56Z",
          "period_end": "2023-11-07T05:31:56Z",
          "group_key": "google/nano-banana-2",
          "cost_micros": 1250000
        }
      ],
      "breakdown": [
        {
          "group_key": "google/nano-banana-2",
          "cost_micros": 1250000,
          "share": 0.42
        }
      ],
      "summary": {
        "spend_micros": 2975000,
        "balance": {
          "amount_micros": 4250,
          "prepaid_balance_micros": 2250,
          "cloud_credit_balance_micros": 2000,
          "currency": "USD"
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

#### Authorizations

​

X-API-Key

string

header

required

API key authentication. Generate an API key from your account settings at <https://platform.comfy.org/profile/api-keys>. Pass the key in the X-API-Key header.

#### Query Parameters

​

group_by

enum<string>

default:model

How to group spend within each time bucket.

Available options: 

`model`, 

`endpoint`, 

`product`

​

granularity

enum<string>

default:month

Width of each time bucket.

Available options: 

`hour`, 

`day`, 

`month`

​

starting_on

string<date-time>

Start of the range, inclusive (RFC 3339). Overrides months when set.

​

ending_before

string<date-time>

End of the range, exclusive (RFC 3339). Defaults to the current hour.

​

months

integer

default:6

How many months back to report, counted from ending_before. Ignored when starting_on is set.

Required range: `1 <= x <= 24`

#### Response

200

application/json

Success - Usage returned

Billed usage for one workspace over a time range.

​

group_by

enum<string>

required

How spend was grouped, echoing the request.

Available options: 

`model`, 

`endpoint`, 

`product`

​

granularity

enum<string>

required

Width of each bucket, echoing the request.

Available options: 

`hour`, 

`day`, 

`month`

​

starting_on

string<date-time>

required

Start of the reported range, inclusive.

​

ending_before

string<date-time>

required

End of the reported range, exclusive.

​

groups

string[]

required

Every group key present in the range, ordered by total spend, highest first. Use it to keep series in a stable order across buckets.

​

buckets

object[]

required

One entry per group per time bucket, oldest bucket first. A group with no spend in a bucket is omitted rather than reported as zero.

Show child attributes

​

breakdown

object[]

required

Total spend per group across the whole range.

Show child attributes

​

summary

object

required

Show child attributes

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/api-reference/cloud/billing/get-workspace-usage-over-time.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/cloud/billing/get-workspace-usage-over-time)

[Get system statisticsPrevious](https://docs.comfy.org/api-reference/cloud/system/get-system-statistics)[Comfy Router quickstartNext](https://docs.comfy.org/development/comfy-router/quickstart)

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

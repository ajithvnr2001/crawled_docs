---
url: https://docs.comfy.org/es/api-reference/cloud/billing/get-workspace-usage-over-time/
title: Get workspace usage over time - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:24.234395+00:00
---

# Get workspace usage over time - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/cloud/billing/get-workspace-usage-over-time/

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

Copiar páginaCopiar página

Returns billed usage for the workspace the API key belongs to, split into time buckets and grouped by model, endpoint, or product. Use it to reconcile spend, attribute cost across models, or feed an internal cost report.

**Units.** `cost_micros` and `spend_micros` are millionths of a US dollar, so divide by 1,000,000 to get dollars. The fields under `summary.balance` are the exception: despite their `_micros` suffix they are **cents** , so divide those by 100.

**Freshness.** Figures are drawn from your invoices rather than from live request traffic, so very recent usage may not appear yet. Treat this as a reporting surface, not a real-time meter.

**Empty results.** A workspace that has not been billed yet returns empty `groups`, `buckets`, and `breakdown` arrays with a 200, not an error.

Copiar páginaCopiar página

GET

/

api

/

billing

/

usage

/

timeseries

Pruébalo

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

#### Autorizaciones

​

X-API-Key

string

header

requerido

API key authentication. Generate an API key from your account settings at <https://platform.comfy.org/profile/api-keys>. Pass the key in the X-API-Key header.

#### Parámetros de consulta

​

group_by

enum<string>

predeterminado:model

How to group spend within each time bucket.

Opciones disponibles: 

`model`, 

`endpoint`, 

`product`

​

granularity

enum<string>

predeterminado:month

Width of each time bucket.

Opciones disponibles: 

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

predeterminado:6

How many months back to report, counted from ending_before. Ignored when starting_on is set.

Rango requerido: `1 <= x <= 24`

#### Respuesta

200

application/json

Success - Usage returned

Billed usage for one workspace over a time range.

​

group_by

enum<string>

requerido

How spend was grouped, echoing the request.

Opciones disponibles: 

`model`, 

`endpoint`, 

`product`

​

granularity

enum<string>

requerido

Width of each bucket, echoing the request.

Opciones disponibles: 

`hour`, 

`day`, 

`month`

​

starting_on

string<date-time>

requerido

Start of the reported range, inclusive.

​

ending_before

string<date-time>

requerido

End of the reported range, exclusive.

​

groups

string[]

requerido

Every group key present in the range, ordered by total spend, highest first. Use it to keep series in a stable order across buckets.

​

buckets

object[]

requerido

One entry per group per time bucket, oldest bucket first. A group with no spend in a bucket is omitted rather than reported as zero.

Show child attributes

​

breakdown

object[]

requerido

Total spend per group across the whole range.

Show child attributes

​

summary

object

requerido

Show child attributes

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/cloud/billing/get-workspace-usage-over-time.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/cloud/billing/get-workspace-usage-over-time)

[Get system statistics](https://docs.comfy.org/es/api-reference/cloud/system/get-system-statistics)[Empezar](https://docs.comfy.org/es/comfy-cli/getting-started)

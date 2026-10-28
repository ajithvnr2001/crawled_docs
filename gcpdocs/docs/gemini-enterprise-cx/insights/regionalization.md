---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization/
title: Regionalization \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:59:19.488443+00:00
---

# Regionalization  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization/

[ Skip to main content ](https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization/)
  * [Deutsch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fgemini-enterprise-cx%2Finsights%2Fregionalization%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/ai-and-machine-learning-color.svg) ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Available regions](https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization/#available_regions)
  * [Sample Commands](https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization/#sample_commands)
  * [Python Client](https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization/#python_client)
  * [Cloud Logging](https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization/#cloud_logging)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)


Was this helpful?
Send feedback 
#  Regionalization Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Available regions](https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization/#available_regions)
  * [Sample Commands](https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization/#sample_commands)
  * [Python Client](https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization/#python_client)
  * [Cloud Logging](https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization/#cloud_logging)


Specifying a region is particularly helpful in the following use cases:
  * Your system has regulatory or policy requirements that govern where your data must reside.
  * Your network latencies might be improved when the data is in the same region as your customers. For example, if Belgium customers use `europe-west1`, they can expect better latency.


## Available regions  
| Country grouping  | Geographical location  | Endpoint  | Resource Location  |  
| --- | --- | --- | --- |  
| Global  | Global serving, data-at-rest in US  | `contactcenterinsights.googleapis.com`  | `us-central1`  |  
| Americas  | South Carolina  | `us-east1-contactcenterinsights.googleapis.com`  | `us-east1`  |  
| Americas  | Oregon  | `us-west1-contactcenterinsights.googleapis.com`  | `us-west1`  |  
| Americas  | Montréal  | `northamerica-northeast1-contactcenterinsights.googleapis.com`  | `northamerica-northeast1`  |  
| Americas  | USA (multi-region)  | `us-contactcenterinsights.googleapis.com`  | `us`  |  
| Europe  | Belgium  | `europe-west1-contactcenterinsights.googleapis.com`  | `europe-west1`  |  
| Europe  | London  | `europe-west2-contactcenterinsights.googleapis.com`  | `europe-west2`  |  
| Europe  | Frankfurt  | `europe-west3-contactcenterinsights.googleapis.com`  | `europe-west3`  |  
| Europe  | Multi Region  | `eu-contactcenterinsights.googleapis.com`  | `eu`  |  
| Europe  | Netherlands  | `europe-west4-contactcenterinsights.googleapis.com`  | `europe-west4`  |  
| Europe  | Zurich  | `europe-west6-contactcenterinsights.googleapis.com`  | `europe-west6`  |  
| Europe  | EU (multi-region)  | `eu-contactcenterinsights.googleapis.com`  | `eu`  |  
| Asia Pacific  | Tokyo  | `asia-northeast1-contactcenterinsights.googleapis.com`  | `asia-northeast1`  |  
| Asia Pacific  | Seoul  | `asia-northeast3-contactcenterinsights.googleapis.com`  | `asia-northeast3`  |  
| Asia Pacific  | Mumbai  | `asia-south1-contactcenterinsights.googleapis.com`  | `asia-south1`  |  
| Asia Pacific  | Singapore  | `asia-southeast1-contactcenterinsights.googleapis.com`  | `asia-southeast1`  |  
| Asia Pacific  | Jakarta  | `asia-southeast2-contactcenterinsights.googleapis.com`  | `asia-southeast2`  |  
| Asia Pacific  | Sydney  | `australia-southeast1-contactcenterinsights.googleapis.com`  | `australia-southeast1`  |  
## Sample Commands
Permissions required for this task
To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 
  * `contactcenterinsights.analyses.create`


[REST](https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization/#rest) More
Before using any of the request data, make the following replacements: 
  * PROJECT_ID: your Google Cloud project ID.
  * LOCATION_ID: regional location.
  * CONVERSATION_ID: the ID of the conversation you want to analyze. This value was returned in the `createConversation` response.


HTTP method and URL: 

```
POST https://LOCATION_ID-contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/conversations/CONVERSATION_ID/analyses
```

To send your request, expand one of these options:
curl (Linux, macOS, or Cloud Shell)
Execute the following command: 

```
curl -X POST \  
     -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
     -H "Content-Type: application/json; charset=utf-8" \  
     -d "" \  
     "https://LOCATION_ID-contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/conversations/CONVERSATION_ID/analyses"
```
PowerShell (Windows)
Execute the following command: 

```
$cred = gcloud auth print-access-token  
$headers = @{ "Authorization" = "Bearer $cred" }  
  
Invoke-WebRequest `  
    -Method POST `  
    -Headers $headers `  
    -Uri "https://LOCATION_ID-contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/conversations/CONVERSATION_ID/analyses" | Select-Object -Expand Content
```

You should receive a JSON response similar to the following:

```
{
  "name": "projects/PROJECT_ID/locations/LOCATION_ID/operations/OPERATION_ID"
}

```

## Python Client
While using the python client, both the host and the resource location needs to be updated to point to the regional instance.

```
options = ClientOptions(api_endpoint="us-east1-contactcenterinsights.googleapis.com" )
request = contact_center_insights_v1.ListConversationsRequest(
    parent=f"projects/{project_id}/locations/us-east1",
)
client = contact_center_insights_v1.ContactCenterInsightsClient(client_options=options)

```

## Cloud Logging
See the [Cloud Logging documentation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/logging/docs/regionalized-logs) to control the region where your logs are stored.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

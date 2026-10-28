---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations/
title: Long-running operations \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:02:54.800108+00:00
---

# Long-running operations  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations/

[ Skip to main content ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations/)
  * [Deutsch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fgemini-enterprise-agent-platform%2Fmachine-learning%2Fgeneral%2Flong-running-operations%2F&prompt=select_account)
[ ![](https://www.gstatic.com/images/branding/productlogos/gemini_2025/v1/192px.svg) ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Getting the status of an operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations/#get-operation)
  * [Canceling an Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations/#cancel)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)


Was this helpful?
Send feedback 
#  Long-running operations Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Getting the status of an operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations/#get-operation)
  * [Canceling an Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations/#cancel)


For some API calls, Gemini Enterprise Agent Platform returns operation names. These API calls start operations that require time to complete and are known as _long-running operations_. For example, creating a dataset, deleting an endpoint, or exporting a model are all long-running operations. You can use helper methods along with operation names to get the status of or cancel a long-running operation, as described in the following sections.
## Getting the status of an operation
To get the operation status, use the operation name that was in the response when you requested a long-running operation. For example, when you create a dataset, Agent Platform returns an operation name such as:  
`projects/PROJECT_NUMBER/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID`
You can poll the operation at regular intervals so that you know when an operation completes.
[REST](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations/#rest) More
Before using any of the request data, make the following replacements: 
  * OPERATION_NAME: The operation name that is returned when you start a long-running operation, such as `projects/PROJECT_NUMBER/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID`


HTTP method and URL: 

```
GET https://LOCATION-aiplatform.googleapis.com/v1/OPERATION_NAME
```

To send your request, choose one of these options:
[curl](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations/#curl)[PowerShell](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations/#powershell) More
Execute the following command: 

```
curl -X GET \  
     -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
     "https://LOCATION-aiplatform.googleapis.com/v1/OPERATION_NAME"
```

Execute the following command: 

```
$cred = gcloud auth print-access-token  
$headers = @{ "Authorization" = "Bearer $cred" }  
  
Invoke-WebRequest `  
    -Method GET `  
    -Headers $headers `  
    -Uri "https://LOCATION-aiplatform.googleapis.com/v1/OPERATION_NAME" | Select-Object -Expand Content
```

In the output, the `metadata` object contains information that is specific to the request type. The `done` field indicates whether the operation is complete. If the operation is complete, the `response` object contains results from the operation.

```
{
  "name": "projects/123456789012/locations/us-central1/datasets/1234567890123456789/operations/1223344556677889900",
  "metadata": {
    "@type": "type.googleapis.com/google.cloud.aiplatform.v1.CreateDatasetOperationMetadata",
    "genericMetadata": {
      "createTime": "2020-10-12T16:00:44.686500Z",
      "updateTime": "2020-10-12T16:01:06.115081Z"
    }
  },
  "done": true,
  "response": {
    "@type": "type.googleapis.com/google.cloud.aiplatform.v1.Dataset",
    "name": "projects/123456789012/locations/us-central1/datasets/1234567890123456789",
    "displayName": "image_dataset",
    "metadataSchemaUri": "gs://google-cloud-aiplatform/schema/dataset/metadata/image_1.0.0.yaml",
    "labels": {
      "aiplatform.googleapis.com/dataset_metadata_schema": "IMAGE"
    },
    "metadata": {
      "dataItemSchemaUri": "gs://google-cloud-aiplatform/schema/dataset/dataitem/image_1.0.0.yaml"
    }
  }
}

```

## Canceling an Operation
You can cancel a long-running operation so that you can stop it before the operation completes. When you successfully cancel an operation, the operation isn't deleted; instead, the operation stops with an error code of `1` and with a `CANCELLED` message. Note that the cancellation is not guaranteed to succeed.
[REST](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations/#rest) More
Before using any of the request data, make the following replacements: 
  * OPERATION_NAME: The operation name that is returned when you start a long-running operation, such as `projects/PROJECT_NUMBER/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID`


HTTP method and URL: 

```
POST https://LOCATION-aiplatform.googleapis.com/v1/OPERATION_NAME:cancel
```

To send your request, choose one of these options:
[curl](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations/#curl)[PowerShell](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations/#powershell) More
Execute the following command: 

```
curl -X POST \  
     -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
     -H "Content-Type: application/json; charset=utf-8" \  
     -d "" \  
     "https://LOCATION-aiplatform.googleapis.com/v1/OPERATION_NAME:cancel"
```

Execute the following command: 

```
$cred = gcloud auth print-access-token  
$headers = @{ "Authorization" = "Bearer $cred" }  
  
Invoke-WebRequest `  
    -Method POST `  
    -Headers $headers `  
    -Uri "https://LOCATION-aiplatform.googleapis.com/v1/OPERATION_NAME:cancel" | Select-Object -Expand Content
```

You should receive a successful status code (2xx) and an empty response.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

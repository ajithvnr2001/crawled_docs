---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot/
title: Reboot a persistent resource \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:48:53.248361+00:00
---

# Reboot a persistent resource  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot/

[ Skip to main content ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot/)
  * [Deutsch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fgemini-enterprise-agent-platform%2Fmachine-learning%2Ftraining%2Fpersistent-resource-reboot%2F&prompt=select_account)
[ ![](https://www.gstatic.com/images/branding/productlogos/gemini_2025/v1/192px.svg) ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Required roles](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot/#required_roles)
  * [Reboot a persistent resource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot/#reboot_a_persistent_resource)
  * [Limitations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot/#limitations)
  * [What's next](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot/#whats_next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)


Was this helpful?
Send feedback 
#  Reboot a persistent resource Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Required roles](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot/#required_roles)
  * [Reboot a persistent resource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot/#reboot_a_persistent_resource)
  * [Limitations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot/#limitations)
  * [What's next](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot/#whats_next)


You can reboot any persistent resource that's in the `RUNNING` or `ERROR` state. Rebooting a persistent resource lets you recover from errors that the persistent resource can't recover from on its own. You can also reboot a persistent resource to manually obtain more up-to-date clusters. This page shows you how to reboot a persistent resource by using the Google Cloud console and the REST API. 
## Required roles
To get the permission that you need to reboot a persistent resource, ask your administrator to grant you the [Agent Platform Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.admin) (`roles/aiplatform.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
This predefined role contains the `aiplatform.persistentResources.update` permission, which is required to reboot a persistent resource. 
You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 
## Reboot a persistent resource
Select one of the following tabs for instructions on how to reboot a persistent resource. Make sure there's no training jobs running on the persistent resource.
[Console](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot/#console)[gcloud](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot/#gcloud)[REST](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-reboot/#rest) More
To reboot a persistent resource in the Google Cloud console, do the following:
  1. In the Google Cloud console, go to the **Persistent resources** page.
[Go to Persistent resources](https://console.cloud.google.com/agent-platform/training/persistent-resources)
  2. Next to the name of the persistent resource that you want to reboot, click the vertical ellipses (more_vert).
  3. Click **Reboot**.
  4. Click **Confirm**. 


Before using any of the command data below, make the following replacements: 
  * PROJECT_ID: The Project ID of the persistent resource that you want to reboot.
  * LOCATION: The region of the persistent resource that you want to reboot.
  * PERSISTENT_RESOURCE_ID: The ID of the persistent resource that you want to reboot.


Execute the following command: 
Linux, macOS, or Cloud Shell 
```
gcloud ai persistent-resources reboot PERSISTENT_RESOURCE_ID \
    --project=PROJECT_ID \
    --region=LOCATION
```
Windows (PowerShell) 
```
gcloud ai persistent-resources reboot PERSISTENT_RESOURCE_ID `
    --project=PROJECT_ID `
    --region=LOCATION
```
Windows (cmd.exe) 
```
gcloud ai persistent-resources reboot PERSISTENT_RESOURCE_ID ^
    --project=PROJECT_ID ^
    --region=LOCATION
```

You should receive a response similar to the following:

```
Using endpoint [https://us-central1-aiplatform.googleapis.com/]
Request to reboot the PersistentResource [projects/sample-project/locations/us-central1/persistentResources/test-persistent-resource] has been sent.

You may view the status of your persistent resource with the command

  $ gcloud ai persistent-resources describe projects/sample-project/locations/us-central1/persistentResources/test-persistent-resource

```

Before using any of the request data, make the following replacements: 
  * PROJECT_ID: The Project ID of the persistent resource that you want to reboot.
  * LOCATION: The region of the persistent resource that you want to reboot.
  * PERSISTENT_RESOURCE_ID: The ID of the persistent resource that you want to reboot.


HTTP method and URL: 

```
POST https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/persistentResources/PERSISTENT_RESOURCE_ID:reboot
```

To send your request, expand one of these options:
curl (Linux, macOS, or Cloud Shell)
Execute the following command: 

```
curl -X POST \  
     -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
     -H "Content-Type: application/json; charset=utf-8" \  
     -d "" \  
     "https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/persistentResources/PERSISTENT_RESOURCE_ID:reboot"
```
PowerShell (Windows)
Execute the following command: 

```
$cred = gcloud auth print-access-token  
$headers = @{ "Authorization" = "Bearer $cred" }  
  
Invoke-WebRequest `  
    -Method POST `  
    -Headers $headers `  
    -Uri "https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/persistentResources/PERSISTENT_RESOURCE_ID:reboot" | Select-Object -Expand Content
```

You should receive a JSON response similar to the following:

```
response: 
  {
    "name": "projects/123456789012/locations/us-central1/persistentResources/test-persistent-resource/operations/1234567890123456789",
    "metadata": {
      "@type": "type.googleapis.com/google.cloud.aiplatform.v1.RebootPersistentResourceOperationMetadata",
      "genericMetadata": {
        "createTime": "2024-03-18T17:31:54.955004Z",
        "updateTime": "2024-03-18T17:31:55.204817Z",
        "state": "RUNNING",
        "worksOn": [
          "projects/123456789012/locations/us-central1/persistentResources/test-persistent-resource"
        ]
      },
      "progressMessage": "Waiting for persistent resource shut down."
    }
  }

```

Rebooting a persistent resource is a [long running operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/long-running-operations), during which the persistent resource can't be deleted. The operation contains a `progressMessage` field that populates with an error status if one occurs. After the operation indicates `"done: true"`, [check the status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-get#get_information_about_a_persistent_resource) of the persistent resource. If the persistent resource is in the `RUNNING` state, the reboot is successful and it's ready to run training jobs.
## Limitations
The following are limitations for rebooting a persistent resource:
  * In some cases, it's possible to lose capacity of scarce resources when rebooting a persistent resource. Full resource retention is not guaranteed.
  * Reboot is not available on Ray on Agent Platform.
  * Persistent resources containing autoscaled worker pools reboot with the minimum replica count.


## What's next
  * [Learn about persistent resource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-overview).
  * [Create and use a persistent resource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-create).
  * [Run training jobs on a persistent resource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-train).
  * [Get information about a persistent resource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-get).
  * [Delete a persistent resource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/persistent-resource-delete). 


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

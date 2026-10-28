---
url: https://docs.cloud.google.com/infrastructure-manager/docs/list-preview/
title: View and list previews \u00a0|\u00a0 Infrastructure Manager \u00a0|\u00a0 Google Cloud Documentation
method: httpx+scrapegraph (scrapling: scrapling status 429 | crawl4ai: crawl4ai failed: Unexpected error in _crawl_web at line 1299 in create_browser_context (../../../../usr/local/lib/python3.10/dist-packages/crawl4ai/browser_manager.py):
Error: Browser is not available. It may have been closed, crashed, or not yet started. Ensure the browser is running before creating new contexts.

Code context:
1294                   raise RuntimeError(
1295                       "Cannot create new browser contexts when using "
1296                       "use_persistent_context=True. Persistent context uses a "
1297                       "single shared context."
1298                   )
1299 →             raise RuntimeError(
1300                   "Browser is not available. It may have been closed, crashed, "
1301                   "or not yet started. Ensure the browser is running before "
1302                   "creating new contexts."
1303               )
1304           # Base settings)
fetched_at: 2026-10-27T16:30:17.719432+00:00
---

# View and list previews  |  Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/list-preview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/infrastructure-manager/docs/overview)



Send feedback 

#  View and list previews Stay organized with collections  Save and categorize content based on your preferences. 

Infrastructure Manager previews let you verify proposed configuration changes and monitor execution states before you deploy resources. Use previews to validate operations and identify configuration issues prior to applying them.

If you have not created a preview, see [Preview a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/preview-deployment).

If you have not created a preview, see [Preview a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/preview-deployment).

## Before you begin

Ensure that you have the IAM permissions needed to view previews: `roles/config.admin`.

## List previews

To list the previews in a specific location:
    
    
    gcloud infra-manager previews list --location=LOCATION
    

Replace LOCATION with the location that contains the previews you want to list. See [Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations) for the list of valid locations.

## View details of a preview

After you create a preview, you might want to view details about the deployment, including the following:

  * The state of the preview. View the state to verify if the preview was successful, failed, or had any issues.
  * The version of Terraform that Infra Manager used to create the preview.



To view details of a preview, use the following command:
    
    
    gcloud infra-manager previews describe \
        projects/PROJECT_ID/locations/LOCATION/previews/PREVIEW_ID
    

Replace:

  * PROJECT_ID is the project ID where Infrastructure Manager runs.
  * LOCATION is the location where Infra Manager runs. See [Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations) for the list of valid locations.
  * PREVIEW_ID is the preview identifier of the preview.



## What's next

  * [Create a new preview](https://docs.cloud.google.com/infrastructure-manager/docs/preview-deployment).
  * Use Infra Manager to [deploy resources](https://docs.cloud.google.com/infrastructure-manager/docs/deploy-resources).
  * [Delete a preview](https://docs.cloud.google.com/infrastructure-manager/docs/delete-preview).
  * Learn more about [Terraform with Infra Manager](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

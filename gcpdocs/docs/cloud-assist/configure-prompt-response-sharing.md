---
url: https://docs.cloud.google.com/cloud-assist/configure-prompt-response-sharing/
title: Configure prompt and response sharing for Gemini Cloud Assist \u00a0|\u00a0 Google Cloud Documentation
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
fetched_at: 2026-10-27T16:22:31.365606+00:00
---

# Configure prompt and response sharing for Gemini Cloud Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/configure-prompt-response-sharing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ Guides ](https://docs.cloud.google.com/cloud-assist/overview)



Send feedback 

#  Configure prompt and response sharing for Gemini Cloud Assist Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Use of this preview offering of Gemini Cloud Assist is subject to the Google Cloud Agreement, including the Pre-GA Offering Terms of the [Google Cloud Specific Service Terms](https://cloud.google.com/terms/services?e=48754805), as supplemented by the terms for the [Gemini for Google Cloud Trusted Tester Program](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview?e=48754805).

You can configure Gemini Cloud Assist prompt and response sharing for your Google Cloud projects through the Google Cloud console or an API. When enabled, Google processes and stores anonymized prompts and responses of all Gemini Cloud Assist users in the project for up to two years for product improvement, but never uses your inputs to train or fine-tune foundation LLMs. You can modify this setting at any time.

## Before you begin

In order to get the required permissions for configuring prompt and response sharing for Gemini Cloud Assist, ask your administrator to [grant](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#single-role) you the [**Gemini Cloud Assist Admin**](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.admin) (`roles/geminicloudassist.admin`) Identity and Access Management (IAM) predefined role, which includes all required permissions needed to view and modify Gemini Cloud Assist administrator settings.

To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `cloudaicompanion.dataSharingWithGoogleSettings.create`
  * `cloudaicompanion.dataSharingWithGoogleSettings.update`
  * `cloudaicompanion.settingBindings.dataSharingWithGoogleSettingsCreate`
  * `cloudaicompanion.settingBindings.dataSharingWithGoogleSettingsUse`
    * If you are using direct API requests, this permission is required specifically for the `TARGET_PROJECT`. 



The following are additional permissions that are required if you are using the Google Cloud console:

  * `cloudaicompanion.instances.queryEffectiveSetting`
  * `cloudaicompanion.instances.queryEffectiveSettingBindings`
  * `cloudaicompanion.dataSharingWithGoogleSettings.list`
  * `cloudaicompanion.dataSharingWithGoogleSettings.get`
  * `cloudaicompanion.settingBindings.dataSharingWithGoogleSettingsGet`
  * `cloudaicompanion.settingBindings.dataSharingWithGoogleSettingsUpdate`
  * `cloudaicompanion.settingBindings.dataSharingWithGoogleSettingsDelete`



You might be able to get these permissions with other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions) or [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

## Enable prompt and response sharing for Gemini Cloud Assist

Select one of the following options:

###  Console 

  1. Open the Google Cloud console.

[Go to Google Cloud console](https://console.cloud.google.com/)

  2. In any page of the Google Cloud console, click spark **Open or close Gemini Cloud Assist chat**.

The **Cloud Assist** panel opens.

  3. Click **More actions** (more_vert), and then click **Cloud Assist Settings** from the drop-down menu.

The **Manage Gemini Cloud Assist** settings panel opens.

  4. In the **Data sharing for Gemini Cloud Assist** section, ensure that **Help Google improve Gemini Cloud Assist by sharing your prompts and responses** is selected.

  5. Click **Save**.




###  API 

To enable data sharing for Gemini Cloud Assist, create a setting with the [`dataSharingWithGoogleSettings.create`](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.dataSharingWithGoogleSettings/create) method, and apply the setting using the associated [`settingBindings.create`](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.dataSharingWithGoogleSettings.settingBindings/create) method.

  1. Create the setting and a setting-specific value:

     1. Obtain an [authentication token](https://docs.cloud.google.com/docs/authentication/rest):
            
            TOKEN=$(gcloud auth print-access-token)
            

     2. Run the following command to create the setting:
            
            curl -X POST \
              -H "Authorization: Bearer $TOKEN" \
              -H 'Content-Type: application/json' \
              -d '{
                "enablePreviewDataSharing": true
                }' \
              "https://cloudaicompanion.googleapis.com/v1/projects/CONTAINER_PROJECT/locations/global/dataSharingWithGoogleSettings?dataSharingWithGoogleSettingId=SETTING_ID"
            

Replace the following:

        * `CONTAINER_PROJECT`: Enter the parent project ID.
        * `SETTING_ID`: Enter a unique setting name, such as `dswg1` for `Data Sharing with Google`.

If the command succeeds, it returns a response body that shows the `enablePreviewDataSharing` set to `true`:
    
    {
      "name": "projects/CONTAINER_PROJECT/locations/global/dataSharingWithGoogleSettings/SETTING_ID",
      "createTime": "2025-01-23T15:22:49.717166932Z",
      "updateTime": "2025-01-23T15:22:49.717166932Z",
      "enablePreviewDataSharing": true
    }
    

For more information on authentication, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest).

  2. Create the setting binding:
         
         curl -X POST \
             -H "Authorization: Bearer $TOKEN" \
             -H 'Content-Type: application/json' \
             -d '{
               "target": "projects/TARGET_PROJECT",
               "product": "GEMINI_CLOUD_ASSIST"
               }' \
             "https://cloudaicompanion.googleapis.com/v1/projects/CONTAINER_PROJECT/locations/global/dataSharingWithGoogleSettings/SETTING_ID/settingBindings?settingBindingId=BINDING_ID"
         

Replace the following:

     * `TARGET_PROJECT`: Enter the target project to which the setting should be applied.
     * `SETTING_ID`: Use the same SETTING_ID when you created the setting, but append it with `b1`. For example, use `dswg1b1` for `Data Sharing with Google`.

If the command succeeds, it returns the operation metadata in the following format:
    
    {
      "name": "projects/CONTAINER_PROJECT/locations/global/operations/operation-1737646069712-62c6140bb04bb-49261230-43701daf",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.cloudaicompanion.v1.OperationMetadata",
        "createTime": "2025-01-23T15:27:50.076075570Z",
        "target": "projects/TARGET_PROJECT/locations/global/dataSharingWithGoogleSettings/SETTING_ID/settingBindings/BINDING_ID",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    




## Disable prompt and response sharing for Gemini Cloud Assist

Select one of the following options:

###  Console 

  1. Open the Google Cloud console.

[Go to Google Cloud console](https://console.cloud.google.com/)

  2. In any page of the Google Cloud console, click spark **Open or close Gemini Cloud Assist chat**.

The **Cloud Assist** panel opens.

  3. Click **More actions** (more_vert), and then click **Cloud Assist Settings** from the drop-down menu.

The **Manage Gemini Cloud Assist** settings panel opens.

  4. In the **Data sharing for Gemini Cloud Assist** section, ensure that **Help Google improve Gemini Cloud Assist by sharing your prompts and responses** is not selected.

  5. Click **Save**.




###  API 

To disable prompt and response sharing for Gemini Cloud Assist, use the [`dataSharingWithGoogleSettings.patch`](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.dataSharingWithGoogleSettings/patch) method.

  1. Obtain the token:
         
         TOKEN=$(gcloud auth print-access-token)
         

  2. Run the following command to disable the setting:
         
         curl -X PATCH \
           -H "Authorization: Bearer $TOKEN" \
           -H 'Content-Type: application/json' \
           -d '{
             "enablePreviewDataSharing": false
             } ' \
           "https://cloudaicompanion.googleapis.com/v1/projects/CONTAINER_PROJECT/locations/global/dataSharingWithGoogleSettings?dataSharingWithGoogleSettingId=SETTING_ID"
         

This `PATCH` command only succeeds if the setting resource already exists from when you enabled prompt and response sharing.

Replace the following:

     * `CONTAINER_PROJECT`: Enter the parent project ID.
     * `SETTING_ID`: Enter the existing setting name, such as `dswg1` for `Data Sharing with Google`.

If the command succeeds, it returns a response body that shows the `enablePreviewDataSharing` set to `false`:
    
    {
      "name": "projects/CONTAINER_PROJECT/locations/global/dataSharingWithGoogleSettings/SETTING_ID",
      "createTime": "2025-01-23T15:22:49.717166932Z",
      "updateTime": "2025-01-23T15:22:49.717166932Z",
      "enablePreviewDataSharing": false
    }
    




## What's next

  * Explore [Gemini Cloud Assist administrator settings](https://docs.cloud.google.com/cloud-assist/admin-settings)

  * [Turn off Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/turn-off)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

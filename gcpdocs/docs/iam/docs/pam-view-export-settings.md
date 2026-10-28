---
url: https://docs.cloud.google.com/iam/docs/pam-view-export-settings/
title: View and export Privileged Access Manager settings \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:17:21.118967+00:00
---

# View and export Privileged Access Manager settings  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/pam-view-export-settings/

[ Skip to main content ](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/)
  * [Deutsch](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/?hl=de)
  * [Español](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/?hl=es-419)
  * [Français](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/?hl=id)
  * [Italiano](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/?hl=it)
  * [Português](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/?hl=ja)
  * [한국어](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fiam%2Fdocs%2Fpam-view-export-settings%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/security-and-identity-color.svg) ](https://docs.cloud.google.com/iam/docs)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/#before_you_begin)
  * [View settings](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/#view-settings)
  * [Export settings programmatically using the gcloud CLI](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/#export-settings)
  * [What's next](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/#whats_next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)


Was this helpful?
Send feedback 
#  View and export Privileged Access Manager settings Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/#before_you_begin)
  * [View settings](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/#view-settings)
  * [Export settings programmatically using the gcloud CLI](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/#export-settings)
  * [What's next](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/#whats_next)


## Before you begin
To get the permissions that you need to view Privileged Access Manager settings, ask your administrator to grant you the following IAM roles on the organization, folder, or project: 
  * To view settings: [PAM Settings Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.settingsViewer) (`roles/privilegedaccessmanager.settingsViewer`) 


For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
These predefined roles contain the permissions required to view Privileged Access Manager settings. To see the exact permissions that are required, expand the **Required permissions** section: 
Required permissions
The following permissions are required to view Privileged Access Manager settings:
  * To view settings: 
    * `privilegedaccessmanager.settings.get`
    * `privilegedaccessmanager.settings.fetchEffective`


You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 
## View settings
[Console](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/#console)[gcloud](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/#gcloud)[REST](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/#rest) More
  1. Go to the **Privileged Access Manager** page.
[Go to Privileged Access Manager](https://console.cloud.google.com/iam-admin/pam/entitlements/)
  2. Select the organization, folder, or project that you want to view Privileged Access Manager settings for.
  3. Click the **Settings** tab.


The **Settings** page displays the Privileged Access Manager settings details for the selected resource.
You can view the following settings for a resource:
  * [Individual settings](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/#individual-settings) that are directly set on the resource.
  * [Effective settings](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/#effective-settings) that are set on the resource or inherited from its parent resource.
#### View individual settings for a resource
The `gcloud alpha pam settings describe` command views Privileged Access Manager settings. 
Before using any of the command data below, make the following replacements: 
    * `RESOURCE_TYPE`: Optional. The resource type that you want to retrieve the settings for. Use the value `organization`, `folder`, or `project`.
    * `RESOURCE_ID`: Used with `RESOURCE_TYPE`. The ID of the Google Cloud project, folder, or organization that you want to manage entitlements for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
Execute the following command: 
Linux, macOS, or Cloud Shell 
```
gcloud alpha pam settings describe \
    --location=global \
    -- RESOURCE_TYPE=RESOURCE_ID \
```
Windows (PowerShell) 
```
gcloud alpha pam settings describe `
    --location=global `
    -- RESOURCE_TYPE=RESOURCE_ID `
```
Windows (cmd.exe) 
```
gcloud alpha pam settings describe ^
    --location=global ^
    -- RESOURCE_TYPE=RESOURCE_ID ^
```

You should receive a response similar to the following:

```
createTime: '2025-05-18T10:10:10.101010101Z'
emailNotificationSettings:
  customNotificationBehavior:
    adminNotifications:
      grantActivated: ENABLED
      grantActivationFailed: DISABLED
      grantEnded: ENABLED
      grantExternallyModified: ENABLED
    approverNotifications:
      pendingApproval: ENABLED
    requesterNotifications:
      entitlementAssigned: ENABLED
      grantActivated: ENABLED
      grantExpired: ENABLED
      grantRevoked: ENABLED
etag: "ZjlkNWZlMWUtNDlhYS00YjJjAYlzNWYtZWFkNGVjOWU3NWMkBwYRsottW5Md"
name: RESOURCE_TYPE/RESOURCE_ID/locations/global/settings
serviceAccountApproverSettings:
  enabled: true
updateTime: '2025-05-18T10:10:10.101010101Z'

```

#### View effective settings on a resource
The `gcloud alpha pam settings describe-effective` command views Privileged Access Manager settings. 
Before using any of the command data below, make the following replacements: 
    * `RESOURCE_TYPE`: Optional. The resource type that you want to retrieve the settings for. Use the value `organization`, `folder`, or `project`.
    * `RESOURCE_ID`: Used with `RESOURCE_TYPE`. The ID of the Google Cloud project, folder, or organization that you want to manage entitlements for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
Execute the following command: 
Linux, macOS, or Cloud Shell 
```
gcloud alpha pam settings describe-effective \
    --location=global \
    --RESOURCE_TYPE=RESOURCE_ID \
```
Windows (PowerShell) 
```
gcloud alpha pam settings describe-effective `
    --location=global `
    --RESOURCE_TYPE=RESOURCE_ID `
```
Windows (cmd.exe) 
```
gcloud alpha pam settings describe-effective ^
    --location=global ^
    --RESOURCE_TYPE=RESOURCE_ID ^
```

You should receive a response similar to the following:

```
emailNotificationSettings:
  customNotificationBehavior:
    adminNotifications:
      notifyGrantActivated: true
      notifyGrantActivationFailed: true
      notifyGrantEnded: true
      notifyGrantExternallyModified: true
    approverNotifications:
      notifyPendingApproval: true
    requesterNotifications:
      notifyEntitlementAssigned: true
      notifyEntitlementUpdated: true
      notifyGrantActivated: true
      notifyGrantActivationFailed: true
      notifyGrantEnded: true
      notifyGrantExpired: true
      notifyGrantExternallyModified: true
      notifyGrantRevoked: true
parent: RESOURCE_TYPE/RESOURCE_ID/locations/global
serviceAccountApproverSettings: {}

```



You can view the following settings for a resource:
  * [Individual settings](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/#individual-settings2) that are directly set on the resource.
  * [Effective settings](https://docs.cloud.google.com/iam/docs/pam-view-export-settings/#effective-settings2) that are set on the resource or inherited from its parent resource.
#### View individual settings for a resource
The Privileged Access Manager API's `getSettings` method views Privileged Access Manager settings. 
Before using any of the request data, make the following replacements: 
    * `SCOPE`: The organization, folder, or project that you want to retrieve the settings for, in the format of `organizations/ORGANIZATION_ID`, `folders/FOLDER_ID`, or `projects/PROJECT_ID`. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
HTTP method and URL: 

```
GET https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/settings
```

To send your request, expand one of these options:
curl (Linux, macOS, or Cloud Shell)
Execute the following command: 

```
curl -X GET \  
     -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
     "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/settings"
```
PowerShell (Windows)
Execute the following command: 

```
$cred = gcloud auth print-access-token  
$headers = @{ "Authorization" = "Bearer $cred" }  
  
Invoke-WebRequest `  
    -Method GET `  
    -Headers $headers `  
    -Uri "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/settings" | Select-Object -Expand Content
```

You should receive a JSON response similar to the following:

```

{
  "createTime": "2025-05-18T10:10:10.101010101Z",
  "emailNotificationSettings": {
    "customNotificationBehavior": {
      "adminNotifications": {
        "grantActivated": "ENABLED",
        "grantActivationFailed": "DISABLED",
        "grantEnded": "ENABLED",
        "grantExternallyModified": "ENABLED"
      },
      "approverNotifications": {
        "pendingApproval": "ENABLED"
      },
      "requesterNotifications": {
        "entitlementAssigned": "ENABLED",
        "grantActivated": "ENABLED",
        "grantExpired": "ENABLED",
        "grantRevoked": "ENABLED"
      }
    }
  },
  "etag": "\"ZjlkNWZlMWUtNDlhYS00YjJjAYlzNWYtZWFkNGVjOWU3NWMkBwYRsottW5Md\"",
  "name": "SCOPE/locations/global/settings",
  "serviceAccountApproverSettings": {
    "enabled": true
  },
  "updateTime": "2025-05-18T10:10:10.101010101Z"
}


```

#### View effective settings on a resource
The Privileged Access Manager API's `fetchEffectiveSettings` method views Privileged Access Manager settings. 
Before using any of the request data, make the following replacements: 
    * `SCOPE`: The organization, folder, or project that you want to retrieve the settings for, in the format of `organizations/ORGANIZATION_ID`, `folders/FOLDER_ID`, or `projects/PROJECT_ID`. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
HTTP method and URL: 

```
GET https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global:effectiveSettings
```

To send your request, expand one of these options:
curl (Linux, macOS, or Cloud Shell)
Execute the following command: 

```
curl -X GET \  
     -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
     "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global:effectiveSettings"
```
PowerShell (Windows)
Execute the following command: 

```
$cred = gcloud auth print-access-token  
$headers = @{ "Authorization" = "Bearer $cred" }  
  
Invoke-WebRequest `  
    -Method GET `  
    -Headers $headers `  
    -Uri "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global:effectiveSettings" | Select-Object -Expand Content
```

You should receive a JSON response similar to the following:

```
{
  "emailNotificationSettings": {
    "customNotificationBehavior": {
      "adminNotifications": {
        "notifyGrantActivated": "true",
        "notifyGrantActivationFailed": "true",
        "notifyGrantEnded": "true",
        "notifyGrantExternallyModified": "true"
      },
      "approverNotifications": {
        "notifyPendingApproval": "true"
      },
      "requesterNotifications": {
        "notifyEntitlementAssigned": "true",
        "notifyEntitlementUpdated": "true",
        "notifyGrantActivated": "true",
        "notifyGrantActivationFailed": "true",
        "notifyGrantEnded": "true",
        "notifyGrantExpired": "true",
        "notifyGrantExternallyModified": "true",
        "notifyGrantRevoked": "true"
      }
    }
  },
  "parent": "SCOPE/locations/global",
  "serviceAccountApproverSettings": {}
}


```



## Export settings programmatically using the gcloud CLI
The `gcloud alpha pam settings export` command retrieves and exports the settings for a specific resource. 
Before using any of the command data below, make the following replacements: 
  * `FILENAME`: The filename to export the settings contents to.
  * `RESOURCE_TYPE`: Optional. The resource type that the corresponding resource belongs to. Use the value `organization`, `folder`, or `project`.
  * `RESOURCE_ID`: Used with `RESOURCE_TYPE`. The ID of the Google Cloud project, folder, or organization that you want to manage entitlements for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.


Execute the following command: 
Linux, macOS, or Cloud Shell 
```
gcloud alpha pam settings export \
    --destination=FILENAME.yaml \
    --location=global \
    -- RESOURCE_TYPE=RESOURCE_ID
```
Windows (PowerShell) 
```
gcloud alpha pam settings export `
    --destination=FILENAME.yaml `
    --location=global `
    -- RESOURCE_TYPE=RESOURCE_ID
```
Windows (cmd.exe) 
```
gcloud alpha pam settings export ^
    --destination=FILENAME.yaml ^
    --location=global ^
    -- RESOURCE_TYPE=RESOURCE_ID
```

You should receive a response similar to the following:

```
Exported [RESOURCE_TYPE/RESOURCE_ID/locations/global/settings] to FILENAME.yaml.

```

## What's next
  * [Create entitlements](https://docs.cloud.google.com/iam/docs/pam-create-entitlements)


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

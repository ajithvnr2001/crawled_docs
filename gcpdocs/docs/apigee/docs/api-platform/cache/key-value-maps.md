---
url: https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/
title: Using key value maps \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:47:15.869972+00:00
---

# Using key value maps  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/

[ Skip to main content ](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/)
  * [Deutsch](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/?hl=de)
  * [Español](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/?hl=es-419)
  * [Français](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/?hl=id)
  * [Italiano](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/?hl=it)
  * [Português](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/?hl=ja)
  * [한국어](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/apigee-color.svg) ](https://docs.cloud.google.com/apigee/docs)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Overview](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#overview)
  * [About KVM scope](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#scope)
  * [About KVM encryption](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#aboutencrypted)
  * [About KVM masking](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#aboutmasking)
  * [Create KVMs](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#create)
  * [Get KVMs](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#managingandusingkvms-getkvms)
  * [Update KVMs](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#managingandusingkvms-updatekvms)
  * [Manage KVM values](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#managingandusingkvms-manage-values)
  * [Delete KVMs](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#delete)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)


Send feedback 
#  Using key value maps Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Overview](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#overview)
  * [About KVM scope](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#scope)
  * [About KVM encryption](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#aboutencrypted)
  * [About KVM masking](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#aboutmasking)
  * [Create KVMs](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#create)
  * [Get KVMs](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#managingandusingkvms-getkvms)
  * [Update KVMs](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#managingandusingkvms-updatekvms)
  * [Manage KVM values](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#managingandusingkvms-manage-values)
  * [Delete KVMs](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#delete)


_This page applies to**Apigee** and **Apigee hybrid**._
_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)
This section discusses how to use key value maps (KVMs).
## Overview
There are times when you want to store data for retrieval at runtime—non-expiring data that shouldn't be hard-coded in your API proxy logic. Key value maps (KVMs) are ideal for this. A KVM is a custom collection of encrypted key/value String pairs. 
The following lists three broad use cases for storing data in KVMs:
  * **User session data:** Data that is created and deleted by the runtime only. For example, shopping cart contents. 
  * **Configuration (such as routing rules and look up tables):** Data that is typically created outside of the runtime but is read by the runtime. This data is configured using the UI or API, and then made available to the gateway (as variables or read-only content). 
For example: You have an API proxy that needs to call one target (or Service Callout) URL in a test environment and another target URL in a production environment. Instead of hard-coding URLs in your API proxy, you can have it detect which environment it's in, execute the related [KeyValueMapOperations policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy), and retrieve the correct target URL from the appropriate KVM.
Later, if one or both of your targets change, you simply update the KVMs with the new URLs. The API proxy picks up the new values; no redeployment is required.
  * **Credentials:** Store credentials, private keys, or tokens—such as tokens for external services, credentials required to generate OAuth tokens, or private keys used in JavaCallout policies or JavaScript for encryption or JSON Web Token (JWT) signing. Instead of passing credentials, keys, or tokens in the request, or hard-coding them in your proxy logic, you can store them in a KVM and dynamically retrieve them in calls to targets that require them. 


You'll discover other situations where storage of key/value String pairs is useful. In general, consider using KVMs when:
  * Specific sections in your code require different values at runtime.
  * Sensitive data needs to be passed without hard-coding it.
  * You want to store values that don't expire like a cache might.


In some cases, property sets are a good alternative to KVMs as they can be easier to use. For more information, see [Using property sets](https://docs.cloud.google.com/apigee/docs/api-platform/cache/property-sets).
## About KVM scope
Scope defines where a KVM is available. KVMs can be created at the following scopes:   
| Scope  | Description  |  
| --- | --- |  
| API proxy  | Only the API proxy can access the KVM.  |  
| Environment  | All API proxies in a specific environment can access the KVM. For example, you may want API proxies deployed in the `prod` environment to not have access to KVMs in the `test` environment. If you want the same KVM keys to be available in production, create a parallel KVM scoped to the `prod` environment.  |  
| Organization  | All API proxies in all environments can access the KVM.  |  
## About KVM encryption
In **Apigee** , all KVM entries for API proxy, organization and environment scopes are protected using the [Cloud KMS](https://cloud.google.com/security-key-management) key provided when an Apigee organization is provisioned (see the `runtimeDatabaseEncryptionKey` field in the [Organization](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#Organization) resource). Apigee uses AES256 as the encryption standard.
In **Apigee hybrid** , you can provide separate encryption keys for all KVM entries for API proxy, organization and environment scopes. Apigee accepts cipher sizes of AES128, AES196 or AES256 as the encryption standard.
## About KVM masking
By default, KVM values are displayed as plain text. You can turn on KVM masking to mask values with asterisks (*****). To turn on or off KVM masking, use the **Mask values** setting in the UI or the `maskedValues` flag in your API request. 
Values are masked at the KVM level. You can't mask individual KVM entries; either all values within a KVM are masked, or none are. 
**Note:** KVM masking won't be automatically turned on for existing KMVs. You will need to explicitly update existing KVMs to use KVM masking.
## Create KVMs
Create KVMs as described in the following sections.
[Apigee UI](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#apigee-ui)[Apigee API](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#apigee-api)[KVM Policy](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#kvm-policy) More
To create a new (empty) KVM or view a list of KVMs:
  1. In the Google Cloud console, go to the **Apigee > Management > Environments** page.
[Go to Environments](https://console.cloud.google.com/apigee/environments)
  2. Select the environment you wish to edit from the list of available environments.
  3. Click the **Key value maps** tab on the **Environment details** page. 
The **Key value maps** page displays a list of existing KVMs. If you have not created any KVMs, then the list is empty.
  4. To create a new (empty) KVM, click **+ Create Key value map**. 
The **Create key value map** dialog opens.
  5. Enter a name for the KVM in the **Key value map name** field. 
The name can contain only letters, numbers, and hyphens and cannot be longer than 255 characters. It cannot include spaces or other special characters. For example: `my-kvm-1`
  6. Click **Mask values** to mask all values. If not selected, KVM values are shown in plain text. See [About KVM masking](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#aboutmasking) for more information. 
  7. Click **Create**. 
The new KVM is displayed in the list.


Use the Apigee APIs to create, list, and delete KVMs for the following scopes: 
  * [API proxy-scoped key value maps API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps)
  * [Environment-scoped key value maps API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keyvaluemaps)
  * [Organization-scoped key value maps API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps)


To create KVMs at runtime and update them in your API proxies, use the [KeyValueMapOperations policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy). In the policy, you specify the name of the KVM in the `**mapIdentifier**`attribute on the parent element.
The `<InitialEntries>` element lets you create and populate a baseline set of entries in a new KVM as soon as you save the policy in the UI or deploy the API proxy (if you developed it offline). If the values change in the policy, the existing values are overwritten. Any new key/value pairs are added to the existing KVM alongside the existing key/value pairs.
The `<Put>` element creates a new KVM if one doesn't already exist, and it creates a key with one or more values. If the KVM already exists, they key/value pairs are added (or updated if the key already exists). You can use multiple `<Put>` elements in a KVM policy.
#### Debug
When you use the [KeyValueMapOperations policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy) to retrieve encrypted KVM values, you supply the name of a variable to store the value. Because all KVM values are encrypted, you need to add the `private.` prefix to the variable name, which prevents the KVM key/value pairs from appearing in Debug sessions.
## Get KVMs
[Apigee UI](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#apigee-ui)[Apigee API](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#apigee-api) More
To view a list of KVMs and their details in the Apigee UI:
  1. Access the list of KVMs for your environment (see [Create KVMs](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#console)).
  2. The **Key value maps** page displays a list of existing KVMs.
  3. Select the name of a KVM to see its entries and settings.


Use the Apigee APIs to get KVMs for the following scopes:
  * [API proxy-scoped key value maps API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps)
  * [Environment-scoped key value maps API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keyvaluemaps)
  * [Organization-scoped key value maps API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps)


For example, to get an API proxy-scoped KVM, enter a `GET` request to the following URL:

```
https://apigee.googleapis.com/v1/organizations/ORG/apis/API/keyvaluemaps/KVM
```

## Update KVMs
[Apigee UI](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#apigee-ui)[Apigee API](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#apigee-api) More
To update the **Mask values** setting for an existing KVM in the Apigee UI:
  1. Access the list of KVMs for your environment (see [Create KVMs](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#console)).
  2. Select the name of the KVM to open its details page.
  3. Toggle the **Mask values** setting.
  4. Click **Save**.


Use the Apigee APIs to update KVMs for the following scopes:
  * [API proxy-scoped key value maps API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps)
  * [Environment-scoped key value maps API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keyvaluemaps)
  * [Organization-scoped key value maps API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps)


For example, to update an API proxy-scoped KVM, enter a `PUT` request to the following URL:

```
https://apigee.googleapis.com/v1/organizations/ORG/apis/API/keyvaluemaps/KVM
```

## Manage KVM values
You can manage KVM values using the following methods: 
[Apigee UI](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#apigee-ui)[Apigee API](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#apigee-api)[KeyValueMapOperations policy](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#keyvaluemapoperations-policy) More
To manage KVM entries in the Apigee UI:
  1. Access the list of KVMs for your environment (see [Create KVMs](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#console)).
  2. Select the name of the KVM to open its details page.
  3. To manage entries: 
     * **Add an entry** : Click **+ Add**. Fill in the **Key** and **Value** fields and click **Add**.
     * **Edit an entry** : Click _edit_ **Edit** next to an entry. Update the **Value** and click **Save**.
     * **Delete an entry** : Click _delete_ **Delete** next to an entry. Click **Delete** in the confirmation dialog.


Use the Apigee APIs to manage KVM values for the following scopes:
  * [API proxy-scoped key value map entries API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps.entries)
  * [Environment-scoped key value map entries API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keyvaluemaps.entries)
  * [Organization-scoped key value map entries API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps.entries)


Use the [ `KeyValueMapOperations` policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy) to add, get, or delete values from KVMs.
Add KVM keys and values using the `<Put>` element of the [KeyValueMapOperations policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy). The `<Put>` element creates a new KVM if one doesn't already exist, and it creates a key with one or more values. If the KVM already exists, the key/value pairs are added (or updated if the key already exists). You can use multiple `<Put>` elements in a KVM policy. For more information, see [<Put> element](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy#PutElement). 
Get KVM values using the `<Get>` element of the [KeyValueMapOperations policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy). Because all KVM values are encrypted, add a `private.` prefix to the name of the variable that will contain the retrieved value. That prefix hides the value from debug sessions while you're debugging API proxies. For more information, see [<Get> element](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy#GetElement).
Delete KVM values using the `<Delete>` element of the [KeyValueMapOperations policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy). For more information, see [<Delete> element](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy#DeleteElement).
## Delete KVMs
Delete KVMs as described in the following sections.
[Apigee UI](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#apigee-ui)[Apigee API](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps/#apigee-api) More
To delete a KVM:
  1. In the Google Cloud console, go to the **Apigee > Management > Environments** page.
[Go to Environments](https://console.cloud.google.com/apigee/environments)
  2. Select the environment name you wish to edit from the list of available environments.
  3. Click the **Key value maps** tab on the **Environment details** page. 
The **Key value maps** page displays a list of existing KVMs.
  4. Locate the row of the KVM that you want to delete.
  5. Click _delete_ **Delete** in the **Actions** column.
  6. Click **Delete Key Value Map** in the dialog to confirm the operation. 
The KVM is deleted and removed from the list.


Use the one of the following Apigee APIs to delete a KVM based on it's scope: 
  * [Delete KVM at API proxy scope](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps/delete)
  * [Delete KVM at environment scope](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keyvaluemaps/delete)
  * [Delete KVM at organization scope](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps/delete)

Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

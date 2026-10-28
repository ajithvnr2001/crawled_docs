---
url: https://docs.cloud.google.com/armor/docs/audit-logging/
title: Audit logging \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:07:53.280274+00:00
---

# Audit logging  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/audit-logging/

[ Skip to main content ](https://docs.cloud.google.com/armor/docs/audit-logging/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/armor/docs/audit-logging/)
  * [Deutsch](https://docs.cloud.google.com/armor/docs/audit-logging/?hl=de)
  * [Español](https://docs.cloud.google.com/armor/docs/audit-logging/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/armor/docs/audit-logging/?hl=es-419)
  * [Français](https://docs.cloud.google.com/armor/docs/audit-logging/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/armor/docs/audit-logging/?hl=id)
  * [Italiano](https://docs.cloud.google.com/armor/docs/audit-logging/?hl=it)
  * [Português](https://docs.cloud.google.com/armor/docs/audit-logging/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/armor/docs/audit-logging/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/armor/docs/audit-logging/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/armor/docs/audit-logging/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/armor/docs/audit-logging/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/armor/docs/audit-logging/?hl=ja)
  * [한국어](https://docs.cloud.google.com/armor/docs/audit-logging/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Farmor%2Fdocs%2Faudit-logging%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/networking-color.svg) ](https://docs.cloud.google.com/armor/docs)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Service name](https://docs.cloud.google.com/armor/docs/audit-logging/#service_name)
  * [Methods by permission type](https://docs.cloud.google.com/armor/docs/audit-logging/#permission-type)
  * [API interface audit logs](https://docs.cloud.google.com/armor/docs/audit-logging/#api-interface-reference)
    * [compute.v1.BackendServicesService](https://docs.cloud.google.com/armor/docs/audit-logging/#compute.v1.BackendServicesService)
    * [compute.v1.SecurityPoliciesService](https://docs.cloud.google.com/armor/docs/audit-logging/#compute.v1.SecurityPoliciesService)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)


Was this helpful?
Send feedback 
#  Audit logging Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Service name](https://docs.cloud.google.com/armor/docs/audit-logging/#service_name)
  * [Methods by permission type](https://docs.cloud.google.com/armor/docs/audit-logging/#permission-type)
  * [API interface audit logs](https://docs.cloud.google.com/armor/docs/audit-logging/#api-interface-reference)
    * [compute.v1.BackendServicesService](https://docs.cloud.google.com/armor/docs/audit-logging/#compute.v1.BackendServicesService)
    * [compute.v1.SecurityPoliciesService](https://docs.cloud.google.com/armor/docs/audit-logging/#compute.v1.SecurityPoliciesService)


This document describes audit logging for Google Cloud Armor. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 
  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)


## Service name
Google Cloud Armor audit logs use the service name `compute.googleapis.com`. Filter for this service: 

```
    protoPayload.serviceName="compute.googleapis.com"
  
```

## Methods by permission type
Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Google Cloud Armor generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.  
| Permission type  | Methods  |  
| --- | --- |  
| `ADMIN_READ`  |  `v1.compute.backendServices.aggregatedList`  
`v1.compute.backendServices.get`  
`v1.compute.backendServices.getHealth`  
`v1.compute.backendServices.getIamPolicy`  
`v1.compute.backendServices.list`  
`v1.compute.backendServices.testIamPermissions`  
`v1.compute.securityPolicies.aggregatedList`  
`v1.compute.securityPolicies.get`  
`v1.compute.securityPolicies.getRule`  
`v1.compute.securityPolicies.list`  
`v1.compute.securityPolicies.listPreconfiguredExpressionSets`  |  
| `ADMIN_WRITE`  |  `v1.compute.backendServices.addSignedUrlKey`  
`v1.compute.backendServices.delete`  
`v1.compute.backendServices.deleteSignedUrlKey`  
`v1.compute.backendServices.insert`  
`v1.compute.backendServices.patch`  
`v1.compute.backendServices.setEdgeSecurityPolicy`  
`v1.compute.backendServices.setIamPolicy`  
`v1.compute.backendServices.setSecurityPolicy`  
`v1.compute.backendServices.update`  
`v1.compute.securityPolicies.addRule`  
`v1.compute.securityPolicies.delete`  
`v1.compute.securityPolicies.insert`  
`v1.compute.securityPolicies.patch`  
`v1.compute.securityPolicies.patchRule`  
`v1.compute.securityPolicies.removeRule`  
`v1.compute.securityPolicies.setLabels`  |  
## API interface audit logs
For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Google Cloud Armor.
### `compute.v1.BackendServicesService`
The following audit logs are associated with methods belonging to `compute.v1.BackendServicesService`.
#### `addSignedUrlKey`
  * **Method** : `v1.compute.backendServices.addSignedUrlKey`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.addSignedUrlKey - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.backendServices.addSignedUrlKey"   `  



#### `aggregatedList`
  * **Method** : `v1.compute.backendServices.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.backendServices.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.backendServices.aggregatedList"   `  



#### `delete`
  * **Method** : `v1.compute.backendServices.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.backendServices.delete"   `  



#### `deleteSignedUrlKey`
  * **Method** : `v1.compute.backendServices.deleteSignedUrlKey`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.deleteSignedUrlKey - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.backendServices.deleteSignedUrlKey"   `  



#### `get`
  * **Method** : `v1.compute.backendServices.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.backendServices.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.backendServices.get"   `  



#### `getHealth`
  * **Method** : `v1.compute.backendServices.getHealth`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.backendServices.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.backendServices.getHealth"   `  



#### `getIamPolicy`
  * **Method** : `v1.compute.backendServices.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.backendServices.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.backendServices.getIamPolicy"   `  



#### `insert`
  * **Method** : `v1.compute.backendServices.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.create - ADMIN_WRITE`
    * `compute.instanceGroups.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.backendServices.insert"   `  



#### `list`
  * **Method** : `v1.compute.backendServices.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.backendServices.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.backendServices.list"   `  



#### `patch`
  * **Method** : `v1.compute.backendServices.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.get - ADMIN_READ`
    * `compute.backendServices.update - ADMIN_WRITE`
    * `compute.healthChecks.useReadOnly - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.backendServices.patch"   `  



#### `setEdgeSecurityPolicy`
  * **Method** : `v1.compute.backendServices.setEdgeSecurityPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.setSecurityPolicy - ADMIN_WRITE`
    * `compute.securityPolicies.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.backendServices.setEdgeSecurityPolicy"   `  



#### `setIamPolicy`
  * **Method** : `v1.compute.backendServices.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.backendServices.setIamPolicy"   `  



#### `setSecurityPolicy`
  * **Method** : `v1.compute.backendServices.setSecurityPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.setSecurityPolicy - ADMIN_WRITE`
    * `compute.securityPolicies.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.backendServices.setSecurityPolicy"   `  



#### `testIamPermissions`
  * **Method** : `v1.compute.backendServices.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.backendServices.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.backendServices.testIamPermissions"   `  



#### `update`
  * **Method** : `v1.compute.backendServices.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.update - ADMIN_WRITE`
    * `compute.healthChecks.useReadOnly - ADMIN_READ`
    * `compute.instanceGroups.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.backendServices.update"   `  



### `compute.v1.SecurityPoliciesService`
The following audit logs are associated with methods belonging to `compute.v1.SecurityPoliciesService`.
#### `addRule`
  * **Method** : `v1.compute.securityPolicies.addRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.securityPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.securityPolicies.addRule"   `  



#### `aggregatedList`
  * **Method** : `v1.compute.securityPolicies.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.securityPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.securityPolicies.aggregatedList"   `  



#### `delete`
  * **Method** : `v1.compute.securityPolicies.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.securityPolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.securityPolicies.delete"   `  



#### `get`
  * **Method** : `v1.compute.securityPolicies.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.securityPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.securityPolicies.get"   `  



#### `getRule`
  * **Method** : `v1.compute.securityPolicies.getRule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.securityPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.securityPolicies.getRule"   `  



#### `insert`
  * **Method** : `v1.compute.securityPolicies.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.securityPolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.securityPolicies.insert"   `  



#### `list`
  * **Method** : `v1.compute.securityPolicies.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.securityPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.securityPolicies.list"   `  



#### `listPreconfiguredExpressionSets`
  * **Method** : `v1.compute.securityPolicies.listPreconfiguredExpressionSets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.securityPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.securityPolicies.listPreconfiguredExpressionSets"   `  



#### `patch`
  * **Method** : `v1.compute.securityPolicies.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.securityPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.securityPolicies.patch"   `  



#### `patchRule`
  * **Method** : `v1.compute.securityPolicies.patchRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.securityPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.securityPolicies.patchRule"   `  



#### `removeRule`
  * **Method** : `v1.compute.securityPolicies.removeRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.securityPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.securityPolicies.removeRule"   `  



#### `setLabels`
  * **Method** : `v1.compute.securityPolicies.setLabels`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.securityPolicies.setLabels - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="v1.compute.securityPolicies.setLabels"   `  



Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

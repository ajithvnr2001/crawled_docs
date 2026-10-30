---
url: https://docs.cloud.google.com/iam/docs/audit-logging/audit-logging-sts/
title: Security Token Service audit logging \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:25:59.097971+00:00
---

# Security Token Service audit logging  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/audit-logging/audit-logging-sts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Security Token Service audit logging Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Audit Logs for Security Token Service let you track administrative and data-access operations on your resources to help you monitor access and configuration changes. You can query these logs in the Logs Explorer and check which Security Token Service API methods generate Cloud Audit Logs.

For more information about Cloud Audit Logs, see the following documents:

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Security Token Service audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="sts.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Security Token Service generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.identity.sts.SecurityTokenService.WebSignIn`  
`google.identity.sts.SecurityTokenService.WebSignOut`  
`google.identity.sts.v1.SecurityTokenService.ExchangeToken`  
`google.identity.sts.v1beta.SecurityTokenService.ExchangeToken`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Security Token Service.

### `google.identity.sts.SecurityTokenService`

The following audit logs are associated with methods belonging to `google.identity.sts.SecurityTokenService`.

#### `WebSignIn`

  * **Method** : `google.identity.sts.SecurityTokenService.WebSignIn`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `sts.identityProviders.checkLogging - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.sts.SecurityTokenService.WebSignIn" `  




#### `WebSignOut`

  * **Method** : `google.identity.sts.SecurityTokenService.WebSignOut`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `sts.identityProviders.checkLogging - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.sts.SecurityTokenService.WebSignOut" `  




### `google.identity.sts.v1.SecurityTokenService`

The following audit logs are associated with methods belonging to `google.identity.sts.v1.SecurityTokenService`.

#### `ExchangeToken`

  * **Method** : `google.identity.sts.v1.SecurityTokenService.ExchangeToken`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `sts.identityProviders.checkLogging - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.sts.v1.SecurityTokenService.ExchangeToken" `  




### `google.identity.sts.v1beta.SecurityTokenService`

The following audit logs are associated with methods belonging to `google.identity.sts.v1beta.SecurityTokenService`.

#### `ExchangeToken`

  * **Method** : `google.identity.sts.v1beta.SecurityTokenService.ExchangeToken`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `sts.identityProviders.checkLogging - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.sts.v1beta.SecurityTokenService.ExchangeToken" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/policyanalyzer-audit-logging/
title: Policy Analyzer audit logging \u00a0|\u00a0 Policy Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:05:23.078520+00:00
---

# Policy Analyzer audit logging  |  Policy Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/policyanalyzer-audit-logging/

[ Skip to main content ](https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/policyanalyzer-audit-logging/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/policyanalyzer-audit-logging/)
  * [Deutsch](https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/policyanalyzer-audit-logging/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/policyanalyzer-audit-logging/?hl=es-419)
  * [Français](https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/policyanalyzer-audit-logging/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/policyanalyzer-audit-logging/?hl=id)
  * [Italiano](https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/policyanalyzer-audit-logging/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/policyanalyzer-audit-logging/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/policyanalyzer-audit-logging/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/policyanalyzer-audit-logging/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/policyanalyzer-audit-logging/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/policyanalyzer-audit-logging/?hl=ja)
  * [한국어](https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/policyanalyzer-audit-logging/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/security-and-identity-color.svg) ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Service name](https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/policyanalyzer-audit-logging/#service_name)
  * [Methods by permission type](https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/policyanalyzer-audit-logging/#permission-type)
  * [API interface audit logs](https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/policyanalyzer-audit-logging/#api-interface-reference)
    * [google.cloud.policyanalyzer.v1.ActivityAnalyzer](https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/policyanalyzer-audit-logging/#google.cloud.policyanalyzer.v1.ActivityAnalyzer)
    * [google.cloud.policyanalyzer.v1beta1.ActivityAnalyzer](https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/policyanalyzer-audit-logging/#google.cloud.policyanalyzer.v1beta1.ActivityAnalyzer)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/policy-intelligence/docs/overview)


Send feedback 
#  Policy Analyzer audit logging Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Service name](https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/policyanalyzer-audit-logging/#service_name)
  * [Methods by permission type](https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/policyanalyzer-audit-logging/#permission-type)
  * [API interface audit logs](https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/policyanalyzer-audit-logging/#api-interface-reference)
    * [google.cloud.policyanalyzer.v1.ActivityAnalyzer](https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/policyanalyzer-audit-logging/#google.cloud.policyanalyzer.v1.ActivityAnalyzer)
    * [google.cloud.policyanalyzer.v1beta1.ActivityAnalyzer](https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/policyanalyzer-audit-logging/#google.cloud.policyanalyzer.v1beta1.ActivityAnalyzer)


Cloud Audit Logs for let you track administrative and data-access operations on your resources to help you monitor access and configuration changes. You can query these logs in the Logs Explorer and check which API methods generate Cloud Audit Logs.
For more information about Cloud Audit Logs, see the following documents:
  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)


## Service name
To view the audit logs, do the following:
  1. In the Google Cloud console, go to the Logs Explorer page:
[Go to Logs Explorer](https://console.cloud.google.com/logs/query)
  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.

```
    protoPayload.serviceName="policyanalyzer.googleapis.com"
  
```



## Methods by permission type
Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.
API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro).   
| Permission type  | Methods  |  
| --- | --- |  
| `DATA_READ`  |  `google.cloud.policyanalyzer.v1.ActivityAnalyzer.QueryActivity`  
`google.cloud.policyanalyzer.v1beta1.ActivityAnalyzer.QueryActivity`  |  
## API interface audit logs
For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for .
### `google.cloud.policyanalyzer.v1.ActivityAnalyzer`
The following audit logs are associated with methods belonging to `google.cloud.policyanalyzer.v1.ActivityAnalyzer`.
#### `QueryActivity`
  * **Method** : `google.cloud.policyanalyzer.v1.ActivityAnalyzer.QueryActivity`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `policyanalyzer.resourceAuthorizationActivities.query - DATA_READ`
    * `policyanalyzer.serviceAccountKeyLastAuthenticationActivities.query - DATA_READ`
    * `policyanalyzer.serviceAccountLastAuthenticationActivities.query - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.cloud.policyanalyzer.v1.ActivityAnalyzer.QueryActivity"   `  



### `google.cloud.policyanalyzer.v1beta1.ActivityAnalyzer`
The following audit logs are associated with methods belonging to `google.cloud.policyanalyzer.v1beta1.ActivityAnalyzer`.
#### `QueryActivity`
  * **Method** : `google.cloud.policyanalyzer.v1beta1.ActivityAnalyzer.QueryActivity`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `policyanalyzer.serviceAccountKeyLastAuthenticationActivities.query - DATA_READ`
    * `policyanalyzer.serviceAccountLastAuthenticationActivities.query - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.cloud.policyanalyzer.v1beta1.ActivityAnalyzer.QueryActivity"   `  



Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-27 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

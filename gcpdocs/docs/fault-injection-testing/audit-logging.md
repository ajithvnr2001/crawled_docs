---
url: https://docs.cloud.google.com/fault-injection-testing/audit-logging/
title: Fault Injection Testing audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T05:45:56.809852+00:00
---

# Fault Injection Testing audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/audit-logging/

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Guides ](https://docs.cloud.google.com/fault-injection-testing/overview)



Send feedback 

#  Fault Injection Testing audit logging Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Cloud Audit Logs for Faulttesting API let you track administrative and data-access operations on your resources to help you monitor access and configuration changes. You can query these logs in the Logs Explorer and check which Faulttesting API API methods generate Cloud Audit Logs.

For more information about Cloud Audit Logs, see the following documents:

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Faulttesting API audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="faulttesting.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Faulttesting API generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.faulttesting.v1alpha.FaultTesting.GetExperiment`  
`google.cloud.faulttesting.v1alpha.FaultTesting.GetExperimentTemplate`  
`google.cloud.faulttesting.v1alpha.FaultTesting.GetValidation`  
`google.cloud.faulttesting.v1alpha.FaultTesting.ListExperimentTemplates`  
`google.cloud.faulttesting.v1alpha.FaultTesting.ListExperiments`  
`google.cloud.faulttesting.v1alpha.FaultTesting.ListValidations`  
`ADMIN_WRITE` | `google.cloud.faulttesting.v1alpha.FaultTesting.CreateExperiment`  
`google.cloud.faulttesting.v1alpha.FaultTesting.CreateExperimentTemplate`  
`google.cloud.faulttesting.v1alpha.FaultTesting.CreateValidation`  
`google.cloud.faulttesting.v1alpha.FaultTesting.DeleteExperiment`  
`google.cloud.faulttesting.v1alpha.FaultTesting.DeleteExperimentTemplate`  
`google.cloud.faulttesting.v1alpha.FaultTesting.DeleteValidation`  
`google.cloud.faulttesting.v1alpha.FaultTesting.StartExperiment`  
`google.cloud.faulttesting.v1alpha.FaultTesting.StopExperiment`  
`google.cloud.faulttesting.v1alpha.FaultTesting.UpdateExperimentTemplate`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Faulttesting API.

### `google.cloud.faulttesting.v1alpha.FaultTesting`

The following audit logs are associated with methods belonging to `google.cloud.faulttesting.v1alpha.FaultTesting`.

#### `CreateExperiment`

  * **Method** : `google.cloud.faulttesting.v1alpha.FaultTesting.CreateExperiment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `faulttesting.experiments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.faulttesting.v1alpha.FaultTesting.CreateExperiment" `  




#### `CreateExperimentTemplate`

  * **Method** : `google.cloud.faulttesting.v1alpha.FaultTesting.CreateExperimentTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `faulttesting.experimentTemplates.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.faulttesting.v1alpha.FaultTesting.CreateExperimentTemplate" `  




#### `CreateValidation`

  * **Method** : `google.cloud.faulttesting.v1alpha.FaultTesting.CreateValidation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `faulttesting.validations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.faulttesting.v1alpha.FaultTesting.CreateValidation" `  




#### `DeleteExperiment`

  * **Method** : `google.cloud.faulttesting.v1alpha.FaultTesting.DeleteExperiment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `faulttesting.experiments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.faulttesting.v1alpha.FaultTesting.DeleteExperiment" `  




#### `DeleteExperimentTemplate`

  * **Method** : `google.cloud.faulttesting.v1alpha.FaultTesting.DeleteExperimentTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `faulttesting.experimentTemplates.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.faulttesting.v1alpha.FaultTesting.DeleteExperimentTemplate" `  




#### `DeleteValidation`

  * **Method** : `google.cloud.faulttesting.v1alpha.FaultTesting.DeleteValidation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `faulttesting.validations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.faulttesting.v1alpha.FaultTesting.DeleteValidation" `  




#### `GetExperiment`

  * **Method** : `google.cloud.faulttesting.v1alpha.FaultTesting.GetExperiment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `faulttesting.experiments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.faulttesting.v1alpha.FaultTesting.GetExperiment" `  




#### `GetExperimentTemplate`

  * **Method** : `google.cloud.faulttesting.v1alpha.FaultTesting.GetExperimentTemplate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `faulttesting.experimentTemplates.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.faulttesting.v1alpha.FaultTesting.GetExperimentTemplate" `  




#### `GetValidation`

  * **Method** : `google.cloud.faulttesting.v1alpha.FaultTesting.GetValidation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `faulttesting.validations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.faulttesting.v1alpha.FaultTesting.GetValidation" `  




#### `ListExperimentTemplates`

  * **Method** : `google.cloud.faulttesting.v1alpha.FaultTesting.ListExperimentTemplates`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `faulttesting.experimentTemplates.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.faulttesting.v1alpha.FaultTesting.ListExperimentTemplates" `  




#### `ListExperiments`

  * **Method** : `google.cloud.faulttesting.v1alpha.FaultTesting.ListExperiments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `faulttesting.experiments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.faulttesting.v1alpha.FaultTesting.ListExperiments" `  




#### `ListValidations`

  * **Method** : `google.cloud.faulttesting.v1alpha.FaultTesting.ListValidations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `faulttesting.validations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.faulttesting.v1alpha.FaultTesting.ListValidations" `  




#### `StartExperiment`

  * **Method** : `google.cloud.faulttesting.v1alpha.FaultTesting.StartExperiment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `faulttesting.experiments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.faulttesting.v1alpha.FaultTesting.StartExperiment" `  




#### `StopExperiment`

  * **Method** : `google.cloud.faulttesting.v1alpha.FaultTesting.StopExperiment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `faulttesting.experiments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.faulttesting.v1alpha.FaultTesting.StopExperiment" `  




#### `UpdateExperimentTemplate`

  * **Method** : `google.cloud.faulttesting.v1alpha.FaultTesting.UpdateExperimentTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `faulttesting.experimentTemplates.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.faulttesting.v1alpha.FaultTesting.UpdateExperimentTemplate" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

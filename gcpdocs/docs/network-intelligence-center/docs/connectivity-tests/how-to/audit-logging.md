---
url: https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/
title: Connectivity Tests audit logging \u00a0|\u00a0 Network Intelligence Center - Connectivity Tests \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:05:02.115208+00:00
---

# Connectivity Tests audit logging  |  Network Intelligence Center - Connectivity Tests  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/

[ Skip to main content ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/)
  * [Deutsch](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/?hl=de)
  * [Español](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/?hl=es-419)
  * [Français](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/?hl=id)
  * [Italiano](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/?hl=it)
  * [Português](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/?hl=ja)
  * [한국어](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/networking-color.svg) ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Connectivity Tests ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Service name](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/#service_name)
  * [Methods by permission type](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/#permission-type)
  * [API interface audit logs](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/#api-interface-reference)
    * [google.cloud.networkmanagement.v1.ReachabilityService](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/#google.cloud.networkmanagement.v1.ReachabilityService)
    * [google.cloud.networkmanagement.v1.VpcFlowLogsService](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/#google.cloud.networkmanagement.v1.VpcFlowLogsService)
    * [google.cloud.networkmanagement.v1beta1.ReachabilityService](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/#google.cloud.networkmanagement.v1beta1.ReachabilityService)
    * [google.cloud.networkmanagement.v1beta1.VpcFlowLogsService](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/#google.cloud.networkmanagement.v1beta1.VpcFlowLogsService)
    * [google.iam.v1.IAMPolicy](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/#google.iam.v1.IAMPolicy)
    * [google.longrunning.Operations](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/#google.longrunning.Operations)
  * [Methods that don't produce audit logs](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/#exempt-methods)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Connectivity Tests ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests)


Was this helpful?
Send feedback 
#  Connectivity Tests audit logging Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Service name](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/#service_name)
  * [Methods by permission type](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/#permission-type)
  * [API interface audit logs](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/#api-interface-reference)
    * [google.cloud.networkmanagement.v1.ReachabilityService](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/#google.cloud.networkmanagement.v1.ReachabilityService)
    * [google.cloud.networkmanagement.v1.VpcFlowLogsService](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/#google.cloud.networkmanagement.v1.VpcFlowLogsService)
    * [google.cloud.networkmanagement.v1beta1.ReachabilityService](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/#google.cloud.networkmanagement.v1beta1.ReachabilityService)
    * [google.cloud.networkmanagement.v1beta1.VpcFlowLogsService](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/#google.cloud.networkmanagement.v1beta1.VpcFlowLogsService)
    * [google.iam.v1.IAMPolicy](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/#google.iam.v1.IAMPolicy)
    * [google.longrunning.Operations](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/#google.longrunning.Operations)
  * [Methods that don't produce audit logs](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/audit-logging/#exempt-methods)


Cloud Audit Logs for Connectivity Tests let you track administrative and data-access operations on your resources to help you monitor access and configuration changes. You can query these logs in the Logs Explorer and check which Connectivity Tests API methods generate Cloud Audit Logs.
For more information about Cloud Audit Logs, see the following documents:
  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)


## Service name
To view the Connectivity Tests audit logs, do the following:
  1. In the Google Cloud console, go to the Logs Explorer page:
[Go to Logs Explorer](https://console.cloud.google.com/logs/query)
  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.

```
    protoPayload.serviceName="networkmanagement.googleapis.com"
  
```



## Methods by permission type
Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Connectivity Tests generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.
API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro).   
| Permission type  | Methods  |  
| --- | --- |  
| `ADMIN_READ`  |  `google.cloud.networkmanagement.v1.ReachabilityService.GetConnectivityTest`  
`google.cloud.networkmanagement.v1.ReachabilityService.ListConnectivityTests`  
`google.cloud.networkmanagement.v1.VpcFlowLogsService.GetVpcFlowLogsConfig`  
`google.cloud.networkmanagement.v1.VpcFlowLogsService.ListVpcFlowLogsConfigs`  
`google.cloud.networkmanagement.v1beta1.ReachabilityService.GetConnectivityTest`  
`google.cloud.networkmanagement.v1beta1.ReachabilityService.ListConnectivityTests`  
`google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.GetVpcFlowLogsConfig`  
`google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.ListVpcFlowLogsConfigs`  
`GetIamPolicy`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  |  
| `ADMIN_WRITE`  |  `google.cloud.networkmanagement.v1.ReachabilityService.CreateConnectivityTest` (LRO)  
`google.cloud.networkmanagement.v1.ReachabilityService.DeleteConnectivityTest` (LRO)  
`google.cloud.networkmanagement.v1.ReachabilityService.RerunConnectivityTest` (LRO)  
`google.cloud.networkmanagement.v1.ReachabilityService.UpdateConnectivityTest` (LRO)  
`google.cloud.networkmanagement.v1.VpcFlowLogsService.CreateVpcFlowLogsConfig` (LRO)  
`google.cloud.networkmanagement.v1.VpcFlowLogsService.DeleteVpcFlowLogsConfig` (LRO)  
`google.cloud.networkmanagement.v1.VpcFlowLogsService.UpdateVpcFlowLogsConfig` (LRO)  
`google.cloud.networkmanagement.v1beta1.ReachabilityService.CreateConnectivityTest` (LRO)  
`google.cloud.networkmanagement.v1beta1.ReachabilityService.DeleteConnectivityTest` (LRO)  
`google.cloud.networkmanagement.v1beta1.ReachabilityService.RerunConnectivityTest` (LRO)  
`google.cloud.networkmanagement.v1beta1.ReachabilityService.UpdateConnectivityTest` (LRO)  
`google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.CreateVpcFlowLogsConfig` (LRO)  
`google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.DeleteVpcFlowLogsConfig` (LRO)  
`google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.UpdateVpcFlowLogsConfig` (LRO)  
`SetIamPolicy`  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  |  
## API interface audit logs
For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Connectivity Tests.
### `google.cloud.networkmanagement.v1.ReachabilityService`
The following audit logs are associated with methods belonging to `google.cloud.networkmanagement.v1.ReachabilityService`.
#### `CreateConnectivityTest`
  * **Method** : `google.cloud.networkmanagement.v1.ReachabilityService.CreateConnectivityTest`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.cloud.networkmanagement.v1.ReachabilityService.CreateConnectivityTest"   `  



#### `DeleteConnectivityTest`
  * **Method** : `google.cloud.networkmanagement.v1.ReachabilityService.DeleteConnectivityTest`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.cloud.networkmanagement.v1.ReachabilityService.DeleteConnectivityTest"   `  



#### `GetConnectivityTest`
  * **Method** : `google.cloud.networkmanagement.v1.ReachabilityService.GetConnectivityTest`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.cloud.networkmanagement.v1.ReachabilityService.GetConnectivityTest"   `  



#### `ListConnectivityTests`
  * **Method** : `google.cloud.networkmanagement.v1.ReachabilityService.ListConnectivityTests`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.cloud.networkmanagement.v1.ReachabilityService.ListConnectivityTests"   `  



#### `RerunConnectivityTest`
  * **Method** : `google.cloud.networkmanagement.v1.ReachabilityService.RerunConnectivityTest`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.rerun - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.cloud.networkmanagement.v1.ReachabilityService.RerunConnectivityTest"   `  



#### `UpdateConnectivityTest`
  * **Method** : `google.cloud.networkmanagement.v1.ReachabilityService.UpdateConnectivityTest`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.cloud.networkmanagement.v1.ReachabilityService.UpdateConnectivityTest"   `  



### `google.cloud.networkmanagement.v1.VpcFlowLogsService`
The following audit logs are associated with methods belonging to `google.cloud.networkmanagement.v1.VpcFlowLogsService`.
#### `CreateVpcFlowLogsConfig`
  * **Method** : `google.cloud.networkmanagement.v1.VpcFlowLogsService.CreateVpcFlowLogsConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.vpcflowlogsconfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.cloud.networkmanagement.v1.VpcFlowLogsService.CreateVpcFlowLogsConfig"   `  



#### `DeleteVpcFlowLogsConfig`
  * **Method** : `google.cloud.networkmanagement.v1.VpcFlowLogsService.DeleteVpcFlowLogsConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.vpcflowlogsconfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.cloud.networkmanagement.v1.VpcFlowLogsService.DeleteVpcFlowLogsConfig"   `  



#### `GetVpcFlowLogsConfig`
  * **Method** : `google.cloud.networkmanagement.v1.VpcFlowLogsService.GetVpcFlowLogsConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkmanagement.vpcflowlogsconfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.cloud.networkmanagement.v1.VpcFlowLogsService.GetVpcFlowLogsConfig"   `  



#### `ListVpcFlowLogsConfigs`
  * **Method** : `google.cloud.networkmanagement.v1.VpcFlowLogsService.ListVpcFlowLogsConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkmanagement.vpcflowlogsconfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.cloud.networkmanagement.v1.VpcFlowLogsService.ListVpcFlowLogsConfigs"   `  



#### `UpdateVpcFlowLogsConfig`
  * **Method** : `google.cloud.networkmanagement.v1.VpcFlowLogsService.UpdateVpcFlowLogsConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.vpcflowlogsconfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.cloud.networkmanagement.v1.VpcFlowLogsService.UpdateVpcFlowLogsConfig"   `  



### `google.cloud.networkmanagement.v1beta1.ReachabilityService`
The following audit logs are associated with methods belonging to `google.cloud.networkmanagement.v1beta1.ReachabilityService`.
#### `CreateConnectivityTest`
  * **Method** : `google.cloud.networkmanagement.v1beta1.ReachabilityService.CreateConnectivityTest`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.cloud.networkmanagement.v1beta1.ReachabilityService.CreateConnectivityTest"   `  



#### `DeleteConnectivityTest`
  * **Method** : `google.cloud.networkmanagement.v1beta1.ReachabilityService.DeleteConnectivityTest`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.cloud.networkmanagement.v1beta1.ReachabilityService.DeleteConnectivityTest"   `  



#### `GetConnectivityTest`
  * **Method** : `google.cloud.networkmanagement.v1beta1.ReachabilityService.GetConnectivityTest`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.cloud.networkmanagement.v1beta1.ReachabilityService.GetConnectivityTest"   `  



#### `ListConnectivityTests`
  * **Method** : `google.cloud.networkmanagement.v1beta1.ReachabilityService.ListConnectivityTests`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.cloud.networkmanagement.v1beta1.ReachabilityService.ListConnectivityTests"   `  



#### `RerunConnectivityTest`
  * **Method** : `google.cloud.networkmanagement.v1beta1.ReachabilityService.RerunConnectivityTest`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.rerun - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.cloud.networkmanagement.v1beta1.ReachabilityService.RerunConnectivityTest"   `  



#### `UpdateConnectivityTest`
  * **Method** : `google.cloud.networkmanagement.v1beta1.ReachabilityService.UpdateConnectivityTest`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.cloud.networkmanagement.v1beta1.ReachabilityService.UpdateConnectivityTest"   `  



### `google.cloud.networkmanagement.v1beta1.VpcFlowLogsService`
The following audit logs are associated with methods belonging to `google.cloud.networkmanagement.v1beta1.VpcFlowLogsService`.
#### `CreateVpcFlowLogsConfig`
  * **Method** : `google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.CreateVpcFlowLogsConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.vpcflowlogsconfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.CreateVpcFlowLogsConfig"   `  



#### `DeleteVpcFlowLogsConfig`
  * **Method** : `google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.DeleteVpcFlowLogsConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.vpcflowlogsconfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.DeleteVpcFlowLogsConfig"   `  



#### `GetVpcFlowLogsConfig`
  * **Method** : `google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.GetVpcFlowLogsConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkmanagement.vpcflowlogsconfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.GetVpcFlowLogsConfig"   `  



#### `ListVpcFlowLogsConfigs`
  * **Method** : `google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.ListVpcFlowLogsConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkmanagement.vpcflowlogsconfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.ListVpcFlowLogsConfigs"   `  



#### `UpdateVpcFlowLogsConfig`
  * **Method** : `google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.UpdateVpcFlowLogsConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.vpcflowlogsconfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : `     protoPayload.methodName="google.cloud.networkmanagement.v1beta1.VpcFlowLogsService.UpdateVpcFlowLogsConfig"   `  



### `google.iam.v1.IAMPolicy`
The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.
#### `GetIamPolicy`
  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="GetIamPolicy"   `  



#### `SetIamPolicy`
  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.connectivitytests.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="SetIamPolicy"   `  



### `google.longrunning.Operations`
The following audit logs are associated with methods belonging to `google.longrunning.Operations`.
#### `CancelOperation`
  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.longrunning.Operations.CancelOperation"   `  



#### `DeleteOperation`
  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkmanagement.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.longrunning.Operations.DeleteOperation"   `  



#### `GetOperation`
  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkmanagement.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.longrunning.Operations.GetOperation"   `  



#### `ListOperations`
  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkmanagement.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : `     protoPayload.methodName="google.longrunning.Operations.ListOperations"   `  



## Methods that don't produce audit logs
A method might not produce audit logs for one or more of the following reasons: 
  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.


The following methods don't produce audit logs:
  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.longrunning.Operations.WaitOperation`


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-27 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

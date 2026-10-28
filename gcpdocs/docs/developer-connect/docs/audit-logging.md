---
url: https://docs.cloud.google.com/developer-connect/docs/audit-logging/
title: Developer Connect audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T19:00:11.997678+00:00
---

# Developer Connect audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Guides ](https://docs.cloud.google.com/developer-connect/docs/overview)



Send feedback 

#  Developer Connect audit logging Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Audit Logs for Developer Connect API let you track administrative and data-access operations on your resources to help you monitor access and configuration changes. You can query these logs in the Logs Explorer and check which Developer Connect API API methods generate Cloud Audit Logs.

For more information about Cloud Audit Logs, see the following documents:

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Developer Connect API audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="developerconnect.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Developer Connect API generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.developerconnect.v1.DeveloperConnect.GetAccountConnector`  
`google.cloud.developerconnect.v1.DeveloperConnect.GetConnection`  
`google.cloud.developerconnect.v1.DeveloperConnect.GetGitRepositoryLink`  
`google.cloud.developerconnect.v1.DeveloperConnect.ListAccountConnectors`  
`google.cloud.developerconnect.v1.DeveloperConnect.ListConnections`  
`google.cloud.developerconnect.v1.DeveloperConnect.ListGitRepositoryLinks`  
`google.cloud.developerconnect.v1.DeveloperConnect.ListUsers`  
`google.cloud.developerconnect.v1.InsightsConfigService.GetInsightsConfig`  
`google.cloud.developerconnect.v1.InsightsConfigService.ListInsightsConfigs`  
`google.longrunning.Operations.GetOperation`  
`ADMIN_WRITE` | `google.cloud.developerconnect.v1.DeveloperConnect.CreateAccountConnector` (LRO)  
`google.cloud.developerconnect.v1.DeveloperConnect.CreateConnection` (LRO)  
`google.cloud.developerconnect.v1.DeveloperConnect.CreateGitRepositoryLink` (LRO)  
`google.cloud.developerconnect.v1.DeveloperConnect.DeleteAccountConnector` (LRO)  
`google.cloud.developerconnect.v1.DeveloperConnect.DeleteConnection` (LRO)  
`google.cloud.developerconnect.v1.DeveloperConnect.DeleteGitRepositoryLink` (LRO)  
`google.cloud.developerconnect.v1.DeveloperConnect.UpdateAccountConnector` (LRO)  
`google.cloud.developerconnect.v1.DeveloperConnect.UpdateConnection` (LRO)  
`google.cloud.developerconnect.v1.InsightsConfigService.CreateInsightsConfig` (LRO)  
`google.cloud.developerconnect.v1.InsightsConfigService.DeleteInsightsConfig` (LRO)  
`google.cloud.developerconnect.v1.InsightsConfigService.UpdateInsightsConfig` (LRO)  
`DATA_READ` | `google.cloud.developerconnect.v1.DeveloperConnect.FetchAccessToken`  
`google.cloud.developerconnect.v1.DeveloperConnect.FetchGitHubInstallations`  
`google.cloud.developerconnect.v1.DeveloperConnect.FetchGitRefs`  
`google.cloud.developerconnect.v1.DeveloperConnect.FetchLinkableGitRepositories`  
`google.cloud.developerconnect.v1.DeveloperConnect.FetchReadToken`  
`google.cloud.developerconnect.v1.DeveloperConnect.FetchReadWriteToken`  
`google.cloud.developerconnect.v1.DeveloperConnect.FetchSelf`  
`DATA_WRITE` | `google.cloud.developerconnect.v1.DeveloperConnect.DeleteSelf` (LRO)  
`google.cloud.developerconnect.v1.DeveloperConnect.DeleteUser` (LRO)  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Developer Connect API.

### `google.cloud.developerconnect.v1.DeveloperConnect`

The following audit logs are associated with methods belonging to `google.cloud.developerconnect.v1.DeveloperConnect`.

#### `CreateAccountConnector`

  * **Method** : `google.cloud.developerconnect.v1.DeveloperConnect.CreateAccountConnector`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `developerconnect.accountConnectors.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.DeveloperConnect.CreateAccountConnector" `  




#### `CreateConnection`

  * **Method** : `google.cloud.developerconnect.v1.DeveloperConnect.CreateConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `developerconnect.connections.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.DeveloperConnect.CreateConnection" `  




#### `CreateGitRepositoryLink`

  * **Method** : `google.cloud.developerconnect.v1.DeveloperConnect.CreateGitRepositoryLink`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `developerconnect.gitRepositoryLinks.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.DeveloperConnect.CreateGitRepositoryLink" `  




#### `DeleteAccountConnector`

  * **Method** : `google.cloud.developerconnect.v1.DeveloperConnect.DeleteAccountConnector`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `developerconnect.accountConnectors.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.DeveloperConnect.DeleteAccountConnector" `  




#### `DeleteConnection`

  * **Method** : `google.cloud.developerconnect.v1.DeveloperConnect.DeleteConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `developerconnect.connections.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.DeveloperConnect.DeleteConnection" `  




#### `DeleteGitRepositoryLink`

  * **Method** : `google.cloud.developerconnect.v1.DeveloperConnect.DeleteGitRepositoryLink`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `developerconnect.gitRepositoryLinks.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.DeveloperConnect.DeleteGitRepositoryLink" `  




#### `DeleteSelf`

  * **Method** : `google.cloud.developerconnect.v1.DeveloperConnect.DeleteSelf`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `developerconnect.users.deleteSelf - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.DeveloperConnect.DeleteSelf" `  




#### `DeleteUser`

  * **Method** : `google.cloud.developerconnect.v1.DeveloperConnect.DeleteUser`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `developerconnect.users.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.DeveloperConnect.DeleteUser" `  




#### `FetchAccessToken`

  * **Method** : `google.cloud.developerconnect.v1.DeveloperConnect.FetchAccessToken`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `developerconnect.users.fetchAccessToken - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.DeveloperConnect.FetchAccessToken" `  




#### `FetchGitHubInstallations`

  * **Method** : `google.cloud.developerconnect.v1.DeveloperConnect.FetchGitHubInstallations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `developerconnect.connections.fetchGitHubInstallations - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.DeveloperConnect.FetchGitHubInstallations" `  




#### `FetchGitRefs`

  * **Method** : `google.cloud.developerconnect.v1.DeveloperConnect.FetchGitRefs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `developerconnect.gitRepositoryLinks.fetchGitRefs - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.DeveloperConnect.FetchGitRefs" `  




#### `FetchLinkableGitRepositories`

  * **Method** : `google.cloud.developerconnect.v1.DeveloperConnect.FetchLinkableGitRepositories`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `developerconnect.connections.fetchLinkableGitRepositories - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.DeveloperConnect.FetchLinkableGitRepositories" `  




#### `FetchReadToken`

  * **Method** : `google.cloud.developerconnect.v1.DeveloperConnect.FetchReadToken`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `developerconnect.gitRepositoryLinks.fetchReadToken - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.DeveloperConnect.FetchReadToken" `  




#### `FetchReadWriteToken`

  * **Method** : `google.cloud.developerconnect.v1.DeveloperConnect.FetchReadWriteToken`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `developerconnect.gitRepositoryLinks.fetchReadWriteToken - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.DeveloperConnect.FetchReadWriteToken" `  




#### `FetchSelf`

  * **Method** : `google.cloud.developerconnect.v1.DeveloperConnect.FetchSelf`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `developerconnect.users.getSelf - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.DeveloperConnect.FetchSelf" `  




#### `GetAccountConnector`

  * **Method** : `google.cloud.developerconnect.v1.DeveloperConnect.GetAccountConnector`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `developerconnect.accountConnectors.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.DeveloperConnect.GetAccountConnector" `  




#### `GetConnection`

  * **Method** : `google.cloud.developerconnect.v1.DeveloperConnect.GetConnection`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `developerconnect.connections.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.DeveloperConnect.GetConnection" `  




#### `GetGitRepositoryLink`

  * **Method** : `google.cloud.developerconnect.v1.DeveloperConnect.GetGitRepositoryLink`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `developerconnect.gitRepositoryLinks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.DeveloperConnect.GetGitRepositoryLink" `  




#### `ListAccountConnectors`

  * **Method** : `google.cloud.developerconnect.v1.DeveloperConnect.ListAccountConnectors`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `developerconnect.accountConnectors.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.DeveloperConnect.ListAccountConnectors" `  




#### `ListConnections`

  * **Method** : `google.cloud.developerconnect.v1.DeveloperConnect.ListConnections`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `developerconnect.connections.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.DeveloperConnect.ListConnections" `  




#### `ListGitRepositoryLinks`

  * **Method** : `google.cloud.developerconnect.v1.DeveloperConnect.ListGitRepositoryLinks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `developerconnect.gitRepositoryLinks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.DeveloperConnect.ListGitRepositoryLinks" `  




#### `ListUsers`

  * **Method** : `google.cloud.developerconnect.v1.DeveloperConnect.ListUsers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `developerconnect.users.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.DeveloperConnect.ListUsers" `  




#### `UpdateAccountConnector`

  * **Method** : `google.cloud.developerconnect.v1.DeveloperConnect.UpdateAccountConnector`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `developerconnect.accountConnectors.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.DeveloperConnect.UpdateAccountConnector" `  




#### `UpdateConnection`

  * **Method** : `google.cloud.developerconnect.v1.DeveloperConnect.UpdateConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `developerconnect.connections.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.DeveloperConnect.UpdateConnection" `  




### `google.cloud.developerconnect.v1.InsightsConfigService`

The following audit logs are associated with methods belonging to `google.cloud.developerconnect.v1.InsightsConfigService`.

#### `CreateInsightsConfig`

  * **Method** : `google.cloud.developerconnect.v1.InsightsConfigService.CreateInsightsConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `developerconnect.insightsConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.InsightsConfigService.CreateInsightsConfig" `  




#### `DeleteInsightsConfig`

  * **Method** : `google.cloud.developerconnect.v1.InsightsConfigService.DeleteInsightsConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `developerconnect.insightsConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.InsightsConfigService.DeleteInsightsConfig" `  




#### `GetInsightsConfig`

  * **Method** : `google.cloud.developerconnect.v1.InsightsConfigService.GetInsightsConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `developerconnect.insightsConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.InsightsConfigService.GetInsightsConfig" `  




#### `ListInsightsConfigs`

  * **Method** : `google.cloud.developerconnect.v1.InsightsConfigService.ListInsightsConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `developerconnect.insightsConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.InsightsConfigService.ListInsightsConfigs" `  




#### `UpdateInsightsConfig`

  * **Method** : `google.cloud.developerconnect.v1.InsightsConfigService.UpdateInsightsConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `developerconnect.insightsConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.developerconnect.v1.InsightsConfigService.UpdateInsightsConfig" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `developerconnect.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

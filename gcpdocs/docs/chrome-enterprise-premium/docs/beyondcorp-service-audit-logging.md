---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/beyondcorp-service-audit-logging/
title: Chrome Enterprise Premium audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T19:00:14.233190+00:00
---

# Chrome Enterprise Premium audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/beyondcorp-service-audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)
  * [ Reference ](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference)



Send feedback 

#  Chrome Enterprise Premium audit logging Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Audit Logs for Chrome Enterprise Premium let you track administrative and data-access operations on your resources to help you monitor access and configuration changes. You can query these logs in the Logs Explorer and check which Chrome Enterprise Premium API methods generate Cloud Audit Logs.

For more information about Cloud Audit Logs, see the following documents:

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Chrome Enterprise Premium audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="beyondcorp.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Chrome Enterprise Premium generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.beyondcorp.appconnections.v1.AppConnectionsService.GetAppConnection`  
`google.cloud.beyondcorp.appconnections.v1.AppConnectionsService.ListAppConnections`  
`google.cloud.beyondcorp.appconnections.v1.AppConnectionsService.ResolveAppConnections`  
`google.cloud.beyondcorp.appconnections.v1alpha.AppConnectionsService.GetAppConnection`  
`google.cloud.beyondcorp.appconnections.v1alpha.AppConnectionsService.ListAppConnections`  
`google.cloud.beyondcorp.appconnections.v1alpha.AppConnectionsService.ResolveAppConnections`  
`google.cloud.beyondcorp.appconnectors.v1.AppConnectorsService.GetAppConnector`  
`google.cloud.beyondcorp.appconnectors.v1.AppConnectorsService.ListAppConnectors`  
`google.cloud.beyondcorp.appconnectors.v1.AppConnectorsService.ResolveInstanceConfig`  
`google.cloud.beyondcorp.appconnectors.v1alpha.AppConnectorsService.GetAppConnector`  
`google.cloud.beyondcorp.appconnectors.v1alpha.AppConnectorsService.ListAppConnectors`  
`google.cloud.beyondcorp.appconnectors.v1alpha.AppConnectorsService.ResolveInstanceConfig`  
`google.cloud.beyondcorp.appgateways.v1.AppGatewaysService.GetAppGateway`  
`google.cloud.beyondcorp.appgateways.v1.AppGatewaysService.ListAppGateways`  
`google.cloud.beyondcorp.appgateways.v1alpha.AppGatewaysService.GetAppGateway`  
`google.cloud.beyondcorp.appgateways.v1alpha.AppGatewaysService.ListAppGateways`  
`google.cloud.beyondcorp.connections.v1alpha.ConnectionsService.GetConnection`  
`google.cloud.beyondcorp.connections.v1alpha.ConnectionsService.ListConnections`  
`google.cloud.beyondcorp.connections.v1alpha.ConnectionsService.ResolveConnections`  
`google.cloud.beyondcorp.connectors.v1alpha.ConnectorsService.GetConnector`  
`google.cloud.beyondcorp.connectors.v1alpha.ConnectorsService.ListConnectors`  
`google.cloud.beyondcorp.connectors.v1alpha.ConnectorsService.ResolveInstanceConfig`  
`google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.GetApplication`  
`google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.GetSecurityGateway`  
`google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.ListApplications`  
`google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.ListSecurityGateways`  
`google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.GetApplication`  
`google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.GetSecurityGateway`  
`google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.ListApplications`  
`google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.ListSecurityGateways`  
`GetIamPolicy`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.beyondcorp.appconnections.v1.AppConnectionsService.DeleteAppConnection` (LRO)  
`google.cloud.beyondcorp.appconnections.v1alpha.AppConnectionsService.DeleteAppConnection` (LRO)  
`google.cloud.beyondcorp.appconnectors.v1.AppConnectorsService.DeleteAppConnector` (LRO)  
`google.cloud.beyondcorp.appconnectors.v1alpha.AppConnectorsService.DeleteAppConnector`  
`google.cloud.beyondcorp.appgateways.v1.AppGatewaysService.DeleteAppGateway` (LRO)  
`google.cloud.beyondcorp.appgateways.v1alpha.AppGatewaysService.DeleteAppGateway` (LRO)  
`google.cloud.beyondcorp.connections.v1alpha.ConnectionsService.DeleteConnection`  
`google.cloud.beyondcorp.connectors.v1alpha.ConnectorsService.DeleteConnector`  
`google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.CreateApplication` (LRO)  
`google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.CreateSecurityGateway` (LRO)  
`google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.DeleteApplication` (LRO)  
`google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.DeleteSecurityGateway` (LRO)  
`google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.UpdateApplication` (LRO)  
`google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.UpdateSecurityGateway` (LRO)  
`google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.CreateApplication` (LRO)  
`google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.CreateSecurityGateway` (LRO)  
`google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.DeleteApplication` (LRO)  
`google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.DeleteSecurityGateway` (LRO)  
`google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.UpdateApplication` (LRO)  
`google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.UpdateSecurityGateway` (LRO)  
`SetIamPolicy`  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Chrome Enterprise Premium.

### `google.cloud.beyondcorp.appconnections.v1.AppConnectionsService`

The following audit logs are associated with methods belonging to `google.cloud.beyondcorp.appconnections.v1.AppConnectionsService`.

#### `DeleteAppConnection`

  * **Method** : `google.cloud.beyondcorp.appconnections.v1.AppConnectionsService.DeleteAppConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `beyondcorp.appConnections.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.appconnections.v1.AppConnectionsService.DeleteAppConnection" `  




#### `GetAppConnection`

  * **Method** : `google.cloud.beyondcorp.appconnections.v1.AppConnectionsService.GetAppConnection`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.appConnections.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.appconnections.v1.AppConnectionsService.GetAppConnection" `  




#### `ListAppConnections`

  * **Method** : `google.cloud.beyondcorp.appconnections.v1.AppConnectionsService.ListAppConnections`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.appConnections.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.appconnections.v1.AppConnectionsService.ListAppConnections" `  




#### `ResolveAppConnections`

  * **Method** : `google.cloud.beyondcorp.appconnections.v1.AppConnectionsService.ResolveAppConnections`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.appConnections.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.appconnections.v1.AppConnectionsService.ResolveAppConnections" `  




### `google.cloud.beyondcorp.appconnections.v1alpha.AppConnectionsService`

The following audit logs are associated with methods belonging to `google.cloud.beyondcorp.appconnections.v1alpha.AppConnectionsService`.

#### `DeleteAppConnection`

  * **Method** : `google.cloud.beyondcorp.appconnections.v1alpha.AppConnectionsService.DeleteAppConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `beyondcorp.appConnections.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.appconnections.v1alpha.AppConnectionsService.DeleteAppConnection" `  




#### `GetAppConnection`

  * **Method** : `google.cloud.beyondcorp.appconnections.v1alpha.AppConnectionsService.GetAppConnection`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.appConnections.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.appconnections.v1alpha.AppConnectionsService.GetAppConnection" `  




#### `ListAppConnections`

  * **Method** : `google.cloud.beyondcorp.appconnections.v1alpha.AppConnectionsService.ListAppConnections`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.appConnections.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.appconnections.v1alpha.AppConnectionsService.ListAppConnections" `  




#### `ResolveAppConnections`

  * **Method** : `google.cloud.beyondcorp.appconnections.v1alpha.AppConnectionsService.ResolveAppConnections`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.appConnections.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.appconnections.v1alpha.AppConnectionsService.ResolveAppConnections" `  




### `google.cloud.beyondcorp.appconnectors.v1.AppConnectorsService`

The following audit logs are associated with methods belonging to `google.cloud.beyondcorp.appconnectors.v1.AppConnectorsService`.

#### `DeleteAppConnector`

  * **Method** : `google.cloud.beyondcorp.appconnectors.v1.AppConnectorsService.DeleteAppConnector`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `beyondcorp.appConnectors.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.appconnectors.v1.AppConnectorsService.DeleteAppConnector" `  




#### `GetAppConnector`

  * **Method** : `google.cloud.beyondcorp.appconnectors.v1.AppConnectorsService.GetAppConnector`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.appConnectors.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.appconnectors.v1.AppConnectorsService.GetAppConnector" `  




#### `ListAppConnectors`

  * **Method** : `google.cloud.beyondcorp.appconnectors.v1.AppConnectorsService.ListAppConnectors`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.appConnectors.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.appconnectors.v1.AppConnectorsService.ListAppConnectors" `  




#### `ResolveInstanceConfig`

  * **Method** : `google.cloud.beyondcorp.appconnectors.v1.AppConnectorsService.ResolveInstanceConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.appConnectors.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.appconnectors.v1.AppConnectorsService.ResolveInstanceConfig" `  




### `google.cloud.beyondcorp.appconnectors.v1alpha.AppConnectorsService`

The following audit logs are associated with methods belonging to `google.cloud.beyondcorp.appconnectors.v1alpha.AppConnectorsService`.

#### `DeleteAppConnector`

  * **Method** : `google.cloud.beyondcorp.appconnectors.v1alpha.AppConnectorsService.DeleteAppConnector`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `beyondcorp.appConnectors.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.appconnectors.v1alpha.AppConnectorsService.DeleteAppConnector" `  




#### `GetAppConnector`

  * **Method** : `google.cloud.beyondcorp.appconnectors.v1alpha.AppConnectorsService.GetAppConnector`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.appConnectors.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.appconnectors.v1alpha.AppConnectorsService.GetAppConnector" `  




#### `ListAppConnectors`

  * **Method** : `google.cloud.beyondcorp.appconnectors.v1alpha.AppConnectorsService.ListAppConnectors`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.appConnectors.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.appconnectors.v1alpha.AppConnectorsService.ListAppConnectors" `  




#### `ResolveInstanceConfig`

  * **Method** : `google.cloud.beyondcorp.appconnectors.v1alpha.AppConnectorsService.ResolveInstanceConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.appConnectors.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.appconnectors.v1alpha.AppConnectorsService.ResolveInstanceConfig" `  




### `google.cloud.beyondcorp.appgateways.v1.AppGatewaysService`

The following audit logs are associated with methods belonging to `google.cloud.beyondcorp.appgateways.v1.AppGatewaysService`.

#### `DeleteAppGateway`

  * **Method** : `google.cloud.beyondcorp.appgateways.v1.AppGatewaysService.DeleteAppGateway`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `beyondcorp.appGateways.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.appgateways.v1.AppGatewaysService.DeleteAppGateway" `  




#### `GetAppGateway`

  * **Method** : `google.cloud.beyondcorp.appgateways.v1.AppGatewaysService.GetAppGateway`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.appGateways.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.appgateways.v1.AppGatewaysService.GetAppGateway" `  




#### `ListAppGateways`

  * **Method** : `google.cloud.beyondcorp.appgateways.v1.AppGatewaysService.ListAppGateways`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.appGateways.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.appgateways.v1.AppGatewaysService.ListAppGateways" `  




### `google.cloud.beyondcorp.appgateways.v1alpha.AppGatewaysService`

The following audit logs are associated with methods belonging to `google.cloud.beyondcorp.appgateways.v1alpha.AppGatewaysService`.

#### `DeleteAppGateway`

  * **Method** : `google.cloud.beyondcorp.appgateways.v1alpha.AppGatewaysService.DeleteAppGateway`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `beyondcorp.appGateways.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.appgateways.v1alpha.AppGatewaysService.DeleteAppGateway" `  




#### `GetAppGateway`

  * **Method** : `google.cloud.beyondcorp.appgateways.v1alpha.AppGatewaysService.GetAppGateway`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.appGateways.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.appgateways.v1alpha.AppGatewaysService.GetAppGateway" `  




#### `ListAppGateways`

  * **Method** : `google.cloud.beyondcorp.appgateways.v1alpha.AppGatewaysService.ListAppGateways`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.appGateways.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.appgateways.v1alpha.AppGatewaysService.ListAppGateways" `  




### `google.cloud.beyondcorp.connections.v1alpha.ConnectionsService`

The following audit logs are associated with methods belonging to `google.cloud.beyondcorp.connections.v1alpha.ConnectionsService`.

#### `DeleteConnection`

  * **Method** : `google.cloud.beyondcorp.connections.v1alpha.ConnectionsService.DeleteConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `beyondcorp.connections.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.connections.v1alpha.ConnectionsService.DeleteConnection" `  




#### `GetConnection`

  * **Method** : `google.cloud.beyondcorp.connections.v1alpha.ConnectionsService.GetConnection`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.connections.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.connections.v1alpha.ConnectionsService.GetConnection" `  




#### `ListConnections`

  * **Method** : `google.cloud.beyondcorp.connections.v1alpha.ConnectionsService.ListConnections`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.connections.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.connections.v1alpha.ConnectionsService.ListConnections" `  




#### `ResolveConnections`

  * **Method** : `google.cloud.beyondcorp.connections.v1alpha.ConnectionsService.ResolveConnections`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.connections.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.connections.v1alpha.ConnectionsService.ResolveConnections" `  




### `google.cloud.beyondcorp.connectors.v1alpha.ConnectorsService`

The following audit logs are associated with methods belonging to `google.cloud.beyondcorp.connectors.v1alpha.ConnectorsService`.

#### `DeleteConnector`

  * **Method** : `google.cloud.beyondcorp.connectors.v1alpha.ConnectorsService.DeleteConnector`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `beyondcorp.connectors.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.connectors.v1alpha.ConnectorsService.DeleteConnector" `  




#### `GetConnector`

  * **Method** : `google.cloud.beyondcorp.connectors.v1alpha.ConnectorsService.GetConnector`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.connectors.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.connectors.v1alpha.ConnectorsService.GetConnector" `  




#### `ListConnectors`

  * **Method** : `google.cloud.beyondcorp.connectors.v1alpha.ConnectorsService.ListConnectors`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.connectors.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.connectors.v1alpha.ConnectorsService.ListConnectors" `  




#### `ResolveInstanceConfig`

  * **Method** : `google.cloud.beyondcorp.connectors.v1alpha.ConnectorsService.ResolveInstanceConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.connectors.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.connectors.v1alpha.ConnectorsService.ResolveInstanceConfig" `  




### `google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService`

The following audit logs are associated with methods belonging to `google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService`.

#### `CreateApplication`

  * **Method** : `google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.CreateApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `beyondcorp.sgApplications.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.CreateApplication" `  




#### `CreateSecurityGateway`

  * **Method** : `google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.CreateSecurityGateway`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `beyondcorp.securityGateways.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.CreateSecurityGateway" `  




#### `DeleteApplication`

  * **Method** : `google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.DeleteApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `beyondcorp.sgApplications.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.DeleteApplication" `  




#### `DeleteSecurityGateway`

  * **Method** : `google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.DeleteSecurityGateway`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `beyondcorp.securityGateways.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.DeleteSecurityGateway" `  




#### `GetApplication`

  * **Method** : `google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.GetApplication`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.sgApplications.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.GetApplication" `  




#### `GetSecurityGateway`

  * **Method** : `google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.GetSecurityGateway`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.securityGateways.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.GetSecurityGateway" `  




#### `ListApplications`

  * **Method** : `google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.ListApplications`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.sgApplications.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.ListApplications" `  




#### `ListSecurityGateways`

  * **Method** : `google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.ListSecurityGateways`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.securityGateways.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.ListSecurityGateways" `  




#### `UpdateApplication`

  * **Method** : `google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.UpdateApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `beyondcorp.sgApplications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.UpdateApplication" `  




#### `UpdateSecurityGateway`

  * **Method** : `google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.UpdateSecurityGateway`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `beyondcorp.securityGateways.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.securitygateways.v1.SecurityGatewaysService.UpdateSecurityGateway" `  




### `google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService`

The following audit logs are associated with methods belonging to `google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService`.

#### `CreateApplication`

  * **Method** : `google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.CreateApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `beyondcorp.sgApplications.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.CreateApplication" `  




#### `CreateSecurityGateway`

  * **Method** : `google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.CreateSecurityGateway`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `beyondcorp.securityGateways.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.CreateSecurityGateway" `  




#### `DeleteApplication`

  * **Method** : `google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.DeleteApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `beyondcorp.sgApplications.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.DeleteApplication" `  




#### `DeleteSecurityGateway`

  * **Method** : `google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.DeleteSecurityGateway`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `beyondcorp.securityGateways.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.DeleteSecurityGateway" `  




#### `GetApplication`

  * **Method** : `google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.GetApplication`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.sgApplications.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.GetApplication" `  




#### `GetSecurityGateway`

  * **Method** : `google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.GetSecurityGateway`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.securityGateways.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.GetSecurityGateway" `  




#### `ListApplications`

  * **Method** : `google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.ListApplications`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.sgApplications.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.ListApplications" `  




#### `ListSecurityGateways`

  * **Method** : `google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.ListSecurityGateways`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.securityGateways.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.ListSecurityGateways" `  




#### `UpdateApplication`

  * **Method** : `google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.UpdateApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `beyondcorp.sgApplications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.UpdateApplication" `  




#### `UpdateSecurityGateway`

  * **Method** : `google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.UpdateSecurityGateway`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `beyondcorp.securityGateways.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.beyondcorp.securitygateways.v1alpha.SecurityGatewaysService.UpdateSecurityGateway" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.appConnections.getIamPolicy - ADMIN_READ`
    * `beyondcorp.appConnectors.getIamPolicy - ADMIN_READ`
    * `beyondcorp.appGateways.getIamPolicy - ADMIN_READ`
    * `beyondcorp.connections.getIamPolicy - ADMIN_READ`
    * `beyondcorp.connectors.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `beyondcorp.appConnections.setIamPolicy - ADMIN_WRITE`
    * `beyondcorp.appConnectors.setIamPolicy - ADMIN_WRITE`
    * `beyondcorp.appGateways.setIamPolicy - ADMIN_WRITE`
    * `beyondcorp.connections.setIamPolicy - ADMIN_WRITE`
    * `beyondcorp.connectors.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="SetIamPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `beyondcorp.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `beyondcorp.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `beyondcorp.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

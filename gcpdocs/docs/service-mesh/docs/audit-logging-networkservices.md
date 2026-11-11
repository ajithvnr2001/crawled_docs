---
url: https://docs.cloud.google.com/service-mesh/docs/audit-logging-networkservices/
title: Network Services API audit logging \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T05:43:00.783325+00:00
---

# Network Services API audit logging  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/audit-logging-networkservices/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Network Services API audit logging

Cloud Audit Logs for Network Services let you track administrative and data-access operations on your resources to help you monitor access and configuration changes. You can query these logs in the Logs Explorer and check which Network Services API methods generate Cloud Audit Logs.

For more information about Cloud Audit Logs, see the following documents:

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Network Services audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="networkservices.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Network Services generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.networkservices.v1.DepService.GetAuthzExtension`  
`google.cloud.networkservices.v1.DepService.GetLbEdgeExtension`  
`google.cloud.networkservices.v1.DepService.GetLbRouteExtension`  
`google.cloud.networkservices.v1.DepService.GetLbTrafficExtension`  
`google.cloud.networkservices.v1.DepService.ListAuthzExtensions`  
`google.cloud.networkservices.v1.DepService.ListLbEdgeExtensions`  
`google.cloud.networkservices.v1.DepService.ListLbRouteExtensions`  
`google.cloud.networkservices.v1.DepService.ListLbTrafficExtensions`  
`google.cloud.networkservices.v1.MulticastService.GetMulticastConsumerAssociation`  
`google.cloud.networkservices.v1.MulticastService.GetMulticastGroupConsumerActivation`  
`google.cloud.networkservices.v1.MulticastService.ListMulticastConsumerAssociations`  
`google.cloud.networkservices.v1.MulticastService.ListMulticastGroupConsumerActivations`  
`google.cloud.networkservices.v1alpha1.DepService.GetAuthzExtension`  
`google.cloud.networkservices.v1alpha1.DepService.GetLbEdgeExtension`  
`google.cloud.networkservices.v1alpha1.DepService.GetLbRouteExtension`  
`google.cloud.networkservices.v1alpha1.DepService.GetLbTcpExtension`  
`google.cloud.networkservices.v1alpha1.DepService.GetLbTrafficExtension`  
`google.cloud.networkservices.v1alpha1.DepService.ListAuthzExtensions`  
`google.cloud.networkservices.v1alpha1.DepService.ListLbEdgeExtensions`  
`google.cloud.networkservices.v1alpha1.DepService.ListLbRouteExtensions`  
`google.cloud.networkservices.v1alpha1.DepService.ListLbTcpExtensions`  
`google.cloud.networkservices.v1alpha1.DepService.ListLbTrafficExtensions`  
`google.cloud.networkservices.v1beta1.DepService.GetAuthzExtension`  
`google.cloud.networkservices.v1beta1.DepService.GetLbEdgeExtension`  
`google.cloud.networkservices.v1beta1.DepService.GetLbRouteExtension`  
`google.cloud.networkservices.v1beta1.DepService.GetLbTcpExtension`  
`google.cloud.networkservices.v1beta1.DepService.GetLbTrafficExtension`  
`google.cloud.networkservices.v1beta1.DepService.ListAuthzExtensions`  
`google.cloud.networkservices.v1beta1.DepService.ListLbEdgeExtensions`  
`google.cloud.networkservices.v1beta1.DepService.ListLbRouteExtensions`  
`google.cloud.networkservices.v1beta1.DepService.ListLbTcpExtensions`  
`google.cloud.networkservices.v1beta1.DepService.ListLbTrafficExtensions`  
`GetIamPolicy`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.networkservices.v1.DepService.CreateAuthzExtension` (LRO)  
`google.cloud.networkservices.v1.DepService.CreateLbEdgeExtension` (LRO)  
`google.cloud.networkservices.v1.DepService.CreateLbRouteExtension` (LRO)  
`google.cloud.networkservices.v1.DepService.CreateLbTrafficExtension` (LRO)  
`google.cloud.networkservices.v1.DepService.DeleteAuthzExtension` (LRO)  
`google.cloud.networkservices.v1.DepService.DeleteLbEdgeExtension` (LRO)  
`google.cloud.networkservices.v1.DepService.DeleteLbRouteExtension` (LRO)  
`google.cloud.networkservices.v1.DepService.DeleteLbTrafficExtension` (LRO)  
`google.cloud.networkservices.v1.DepService.UpdateAuthzExtension` (LRO)  
`google.cloud.networkservices.v1.DepService.UpdateLbEdgeExtension` (LRO)  
`google.cloud.networkservices.v1.DepService.UpdateLbRouteExtension` (LRO)  
`google.cloud.networkservices.v1.DepService.UpdateLbTrafficExtension` (LRO)  
`google.cloud.networkservices.v1.MulticastService.CreateMulticastConsumerAssociation` (LRO)  
`google.cloud.networkservices.v1.MulticastService.CreateMulticastGroupConsumerActivation` (LRO)  
`google.cloud.networkservices.v1.MulticastService.DeleteMulticastConsumerAssociation` (LRO)  
`google.cloud.networkservices.v1.MulticastService.DeleteMulticastGroupConsumerActivation` (LRO)  
`google.cloud.networkservices.v1.MulticastService.UpdateMulticastGroupConsumerActivation` (LRO)  
`google.cloud.networkservices.v1alpha1.DepService.CreateAuthzExtension` (LRO)  
`google.cloud.networkservices.v1alpha1.DepService.CreateLbEdgeExtension` (LRO)  
`google.cloud.networkservices.v1alpha1.DepService.CreateLbRouteExtension` (LRO)  
`google.cloud.networkservices.v1alpha1.DepService.CreateLbTcpExtension` (LRO)  
`google.cloud.networkservices.v1alpha1.DepService.CreateLbTrafficExtension` (LRO)  
`google.cloud.networkservices.v1alpha1.DepService.DeleteAuthzExtension` (LRO)  
`google.cloud.networkservices.v1alpha1.DepService.DeleteLbEdgeExtension` (LRO)  
`google.cloud.networkservices.v1alpha1.DepService.DeleteLbRouteExtension` (LRO)  
`google.cloud.networkservices.v1alpha1.DepService.DeleteLbTcpExtension` (LRO)  
`google.cloud.networkservices.v1alpha1.DepService.DeleteLbTrafficExtension` (LRO)  
`google.cloud.networkservices.v1alpha1.DepService.UpdateAuthzExtension` (LRO)  
`google.cloud.networkservices.v1alpha1.DepService.UpdateLbEdgeExtension` (LRO)  
`google.cloud.networkservices.v1alpha1.DepService.UpdateLbRouteExtension` (LRO)  
`google.cloud.networkservices.v1alpha1.DepService.UpdateLbTcpExtension` (LRO)  
`google.cloud.networkservices.v1alpha1.DepService.UpdateLbTrafficExtension` (LRO)  
`google.cloud.networkservices.v1beta1.DepService.CreateAuthzExtension` (LRO)  
`google.cloud.networkservices.v1beta1.DepService.CreateLbEdgeExtension` (LRO)  
`google.cloud.networkservices.v1beta1.DepService.CreateLbRouteExtension` (LRO)  
`google.cloud.networkservices.v1beta1.DepService.CreateLbTcpExtension` (LRO)  
`google.cloud.networkservices.v1beta1.DepService.CreateLbTrafficExtension` (LRO)  
`google.cloud.networkservices.v1beta1.DepService.DeleteAuthzExtension` (LRO)  
`google.cloud.networkservices.v1beta1.DepService.DeleteLbEdgeExtension` (LRO)  
`google.cloud.networkservices.v1beta1.DepService.DeleteLbRouteExtension` (LRO)  
`google.cloud.networkservices.v1beta1.DepService.DeleteLbTcpExtension` (LRO)  
`google.cloud.networkservices.v1beta1.DepService.DeleteLbTrafficExtension` (LRO)  
`google.cloud.networkservices.v1beta1.DepService.UpdateAuthzExtension` (LRO)  
`google.cloud.networkservices.v1beta1.DepService.UpdateLbEdgeExtension` (LRO)  
`google.cloud.networkservices.v1beta1.DepService.UpdateLbRouteExtension` (LRO)  
`google.cloud.networkservices.v1beta1.DepService.UpdateLbTcpExtension` (LRO)  
`google.cloud.networkservices.v1beta1.DepService.UpdateLbTrafficExtension` (LRO)  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Network Services.

### `google.cloud.networkservices.v1.DepService`

The following audit logs are associated with methods belonging to `google.cloud.networkservices.v1.DepService`.

#### `CreateAuthzExtension`

  * **Method** : `google.cloud.networkservices.v1.DepService.CreateAuthzExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.authzExtensions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.DepService.CreateAuthzExtension" `  




#### `CreateLbEdgeExtension`

  * **Method** : `google.cloud.networkservices.v1.DepService.CreateLbEdgeExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbEdgeExtensions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.DepService.CreateLbEdgeExtension" `  




#### `CreateLbRouteExtension`

  * **Method** : `google.cloud.networkservices.v1.DepService.CreateLbRouteExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbRouteExtensions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.DepService.CreateLbRouteExtension" `  




#### `CreateLbTrafficExtension`

  * **Method** : `google.cloud.networkservices.v1.DepService.CreateLbTrafficExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbTrafficExtensions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.DepService.CreateLbTrafficExtension" `  




#### `DeleteAuthzExtension`

  * **Method** : `google.cloud.networkservices.v1.DepService.DeleteAuthzExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.authzExtensions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.DepService.DeleteAuthzExtension" `  




#### `DeleteLbEdgeExtension`

  * **Method** : `google.cloud.networkservices.v1.DepService.DeleteLbEdgeExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbEdgeExtensions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.DepService.DeleteLbEdgeExtension" `  




#### `DeleteLbRouteExtension`

  * **Method** : `google.cloud.networkservices.v1.DepService.DeleteLbRouteExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbRouteExtensions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.DepService.DeleteLbRouteExtension" `  




#### `DeleteLbTrafficExtension`

  * **Method** : `google.cloud.networkservices.v1.DepService.DeleteLbTrafficExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbTrafficExtensions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.DepService.DeleteLbTrafficExtension" `  




#### `GetAuthzExtension`

  * **Method** : `google.cloud.networkservices.v1.DepService.GetAuthzExtension`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.authzExtensions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.DepService.GetAuthzExtension" `  




#### `GetLbEdgeExtension`

  * **Method** : `google.cloud.networkservices.v1.DepService.GetLbEdgeExtension`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.lbEdgeExtensions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.DepService.GetLbEdgeExtension" `  




#### `GetLbRouteExtension`

  * **Method** : `google.cloud.networkservices.v1.DepService.GetLbRouteExtension`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.lbRouteExtensions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.DepService.GetLbRouteExtension" `  




#### `GetLbTrafficExtension`

  * **Method** : `google.cloud.networkservices.v1.DepService.GetLbTrafficExtension`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.lbTrafficExtensions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.DepService.GetLbTrafficExtension" `  




#### `ListAuthzExtensions`

  * **Method** : `google.cloud.networkservices.v1.DepService.ListAuthzExtensions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.authzExtensions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.DepService.ListAuthzExtensions" `  




#### `ListLbEdgeExtensions`

  * **Method** : `google.cloud.networkservices.v1.DepService.ListLbEdgeExtensions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.lbEdgeExtensions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.DepService.ListLbEdgeExtensions" `  




#### `ListLbRouteExtensions`

  * **Method** : `google.cloud.networkservices.v1.DepService.ListLbRouteExtensions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.lbRouteExtensions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.DepService.ListLbRouteExtensions" `  




#### `ListLbTrafficExtensions`

  * **Method** : `google.cloud.networkservices.v1.DepService.ListLbTrafficExtensions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.lbTrafficExtensions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.DepService.ListLbTrafficExtensions" `  




#### `UpdateAuthzExtension`

  * **Method** : `google.cloud.networkservices.v1.DepService.UpdateAuthzExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.authzExtensions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.DepService.UpdateAuthzExtension" `  




#### `UpdateLbEdgeExtension`

  * **Method** : `google.cloud.networkservices.v1.DepService.UpdateLbEdgeExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbEdgeExtensions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.DepService.UpdateLbEdgeExtension" `  




#### `UpdateLbRouteExtension`

  * **Method** : `google.cloud.networkservices.v1.DepService.UpdateLbRouteExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbRouteExtensions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.DepService.UpdateLbRouteExtension" `  




#### `UpdateLbTrafficExtension`

  * **Method** : `google.cloud.networkservices.v1.DepService.UpdateLbTrafficExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbTrafficExtensions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.DepService.UpdateLbTrafficExtension" `  




### `google.cloud.networkservices.v1.MulticastService`

The following audit logs are associated with methods belonging to `google.cloud.networkservices.v1.MulticastService`.

#### `CreateMulticastConsumerAssociation`

  * **Method** : `google.cloud.networkservices.v1.MulticastService.CreateMulticastConsumerAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.multicastConsumerAssociations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.MulticastService.CreateMulticastConsumerAssociation" `  




#### `CreateMulticastGroupConsumerActivation`

  * **Method** : `google.cloud.networkservices.v1.MulticastService.CreateMulticastGroupConsumerActivation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.multicastGroupConsumerActivations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.MulticastService.CreateMulticastGroupConsumerActivation" `  




#### `DeleteMulticastConsumerAssociation`

  * **Method** : `google.cloud.networkservices.v1.MulticastService.DeleteMulticastConsumerAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.multicastConsumerAssociations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.MulticastService.DeleteMulticastConsumerAssociation" `  




#### `DeleteMulticastGroupConsumerActivation`

  * **Method** : `google.cloud.networkservices.v1.MulticastService.DeleteMulticastGroupConsumerActivation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.multicastGroupConsumerActivations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.MulticastService.DeleteMulticastGroupConsumerActivation" `  




#### `GetMulticastConsumerAssociation`

  * **Method** : `google.cloud.networkservices.v1.MulticastService.GetMulticastConsumerAssociation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.multicastConsumerAssociations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.MulticastService.GetMulticastConsumerAssociation" `  




#### `GetMulticastGroupConsumerActivation`

  * **Method** : `google.cloud.networkservices.v1.MulticastService.GetMulticastGroupConsumerActivation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.multicastGroupConsumerActivations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.MulticastService.GetMulticastGroupConsumerActivation" `  




#### `ListMulticastConsumerAssociations`

  * **Method** : `google.cloud.networkservices.v1.MulticastService.ListMulticastConsumerAssociations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.multicastConsumerAssociations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.MulticastService.ListMulticastConsumerAssociations" `  




#### `ListMulticastGroupConsumerActivations`

  * **Method** : `google.cloud.networkservices.v1.MulticastService.ListMulticastGroupConsumerActivations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.multicastGroupConsumerActivations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.MulticastService.ListMulticastGroupConsumerActivations" `  




#### `UpdateMulticastGroupConsumerActivation`

  * **Method** : `google.cloud.networkservices.v1.MulticastService.UpdateMulticastGroupConsumerActivation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.multicastGroupConsumerActivations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1.MulticastService.UpdateMulticastGroupConsumerActivation" `  




### `google.cloud.networkservices.v1alpha1.DepService`

The following audit logs are associated with methods belonging to `google.cloud.networkservices.v1alpha1.DepService`.

#### `CreateAuthzExtension`

  * **Method** : `google.cloud.networkservices.v1alpha1.DepService.CreateAuthzExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.authzExtensions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1alpha1.DepService.CreateAuthzExtension" `  




#### `CreateLbEdgeExtension`

  * **Method** : `google.cloud.networkservices.v1alpha1.DepService.CreateLbEdgeExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbEdgeExtensions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1alpha1.DepService.CreateLbEdgeExtension" `  




#### `CreateLbRouteExtension`

  * **Method** : `google.cloud.networkservices.v1alpha1.DepService.CreateLbRouteExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbRouteExtensions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1alpha1.DepService.CreateLbRouteExtension" `  




#### `CreateLbTcpExtension`

  * **Method** : `google.cloud.networkservices.v1alpha1.DepService.CreateLbTcpExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbTcpExtensions.createForNetwork - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1alpha1.DepService.CreateLbTcpExtension" `  




#### `CreateLbTrafficExtension`

  * **Method** : `google.cloud.networkservices.v1alpha1.DepService.CreateLbTrafficExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbTrafficExtensions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1alpha1.DepService.CreateLbTrafficExtension" `  




#### `DeleteAuthzExtension`

  * **Method** : `google.cloud.networkservices.v1alpha1.DepService.DeleteAuthzExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.authzExtensions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1alpha1.DepService.DeleteAuthzExtension" `  




#### `DeleteLbEdgeExtension`

  * **Method** : `google.cloud.networkservices.v1alpha1.DepService.DeleteLbEdgeExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbEdgeExtensions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1alpha1.DepService.DeleteLbEdgeExtension" `  




#### `DeleteLbRouteExtension`

  * **Method** : `google.cloud.networkservices.v1alpha1.DepService.DeleteLbRouteExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbRouteExtensions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1alpha1.DepService.DeleteLbRouteExtension" `  




#### `DeleteLbTcpExtension`

  * **Method** : `google.cloud.networkservices.v1alpha1.DepService.DeleteLbTcpExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbTcpExtensions.deleteForNetwork - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1alpha1.DepService.DeleteLbTcpExtension" `  




#### `DeleteLbTrafficExtension`

  * **Method** : `google.cloud.networkservices.v1alpha1.DepService.DeleteLbTrafficExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbTrafficExtensions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1alpha1.DepService.DeleteLbTrafficExtension" `  




#### `GetAuthzExtension`

  * **Method** : `google.cloud.networkservices.v1alpha1.DepService.GetAuthzExtension`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.authzExtensions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1alpha1.DepService.GetAuthzExtension" `  




#### `GetLbEdgeExtension`

  * **Method** : `google.cloud.networkservices.v1alpha1.DepService.GetLbEdgeExtension`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.lbEdgeExtensions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1alpha1.DepService.GetLbEdgeExtension" `  




#### `GetLbRouteExtension`

  * **Method** : `google.cloud.networkservices.v1alpha1.DepService.GetLbRouteExtension`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.lbRouteExtensions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1alpha1.DepService.GetLbRouteExtension" `  




#### `GetLbTcpExtension`

  * **Method** : `google.cloud.networkservices.v1alpha1.DepService.GetLbTcpExtension`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.lbTcpExtensions.getForNetwork - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1alpha1.DepService.GetLbTcpExtension" `  




#### `GetLbTrafficExtension`

  * **Method** : `google.cloud.networkservices.v1alpha1.DepService.GetLbTrafficExtension`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.lbTrafficExtensions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1alpha1.DepService.GetLbTrafficExtension" `  




#### `ListAuthzExtensions`

  * **Method** : `google.cloud.networkservices.v1alpha1.DepService.ListAuthzExtensions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.authzExtensions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1alpha1.DepService.ListAuthzExtensions" `  




#### `ListLbEdgeExtensions`

  * **Method** : `google.cloud.networkservices.v1alpha1.DepService.ListLbEdgeExtensions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.lbEdgeExtensions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1alpha1.DepService.ListLbEdgeExtensions" `  




#### `ListLbRouteExtensions`

  * **Method** : `google.cloud.networkservices.v1alpha1.DepService.ListLbRouteExtensions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.lbRouteExtensions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1alpha1.DepService.ListLbRouteExtensions" `  




#### `ListLbTcpExtensions`

  * **Method** : `google.cloud.networkservices.v1alpha1.DepService.ListLbTcpExtensions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.lbTcpExtensions.listForNetwork - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1alpha1.DepService.ListLbTcpExtensions" `  




#### `ListLbTrafficExtensions`

  * **Method** : `google.cloud.networkservices.v1alpha1.DepService.ListLbTrafficExtensions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.lbTrafficExtensions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1alpha1.DepService.ListLbTrafficExtensions" `  




#### `UpdateAuthzExtension`

  * **Method** : `google.cloud.networkservices.v1alpha1.DepService.UpdateAuthzExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.authzExtensions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1alpha1.DepService.UpdateAuthzExtension" `  




#### `UpdateLbEdgeExtension`

  * **Method** : `google.cloud.networkservices.v1alpha1.DepService.UpdateLbEdgeExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbEdgeExtensions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1alpha1.DepService.UpdateLbEdgeExtension" `  




#### `UpdateLbRouteExtension`

  * **Method** : `google.cloud.networkservices.v1alpha1.DepService.UpdateLbRouteExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbRouteExtensions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1alpha1.DepService.UpdateLbRouteExtension" `  




#### `UpdateLbTcpExtension`

  * **Method** : `google.cloud.networkservices.v1alpha1.DepService.UpdateLbTcpExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbTcpExtensions.updateForNetwork - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1alpha1.DepService.UpdateLbTcpExtension" `  




#### `UpdateLbTrafficExtension`

  * **Method** : `google.cloud.networkservices.v1alpha1.DepService.UpdateLbTrafficExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbTrafficExtensions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1alpha1.DepService.UpdateLbTrafficExtension" `  




### `google.cloud.networkservices.v1beta1.DepService`

The following audit logs are associated with methods belonging to `google.cloud.networkservices.v1beta1.DepService`.

#### `CreateAuthzExtension`

  * **Method** : `google.cloud.networkservices.v1beta1.DepService.CreateAuthzExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.authzExtensions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1beta1.DepService.CreateAuthzExtension" `  




#### `CreateLbEdgeExtension`

  * **Method** : `google.cloud.networkservices.v1beta1.DepService.CreateLbEdgeExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbEdgeExtensions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1beta1.DepService.CreateLbEdgeExtension" `  




#### `CreateLbRouteExtension`

  * **Method** : `google.cloud.networkservices.v1beta1.DepService.CreateLbRouteExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbRouteExtensions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1beta1.DepService.CreateLbRouteExtension" `  




#### `CreateLbTcpExtension`

  * **Method** : `google.cloud.networkservices.v1beta1.DepService.CreateLbTcpExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbTcpExtensions.createForNetwork - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1beta1.DepService.CreateLbTcpExtension" `  




#### `CreateLbTrafficExtension`

  * **Method** : `google.cloud.networkservices.v1beta1.DepService.CreateLbTrafficExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbTrafficExtensions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1beta1.DepService.CreateLbTrafficExtension" `  




#### `DeleteAuthzExtension`

  * **Method** : `google.cloud.networkservices.v1beta1.DepService.DeleteAuthzExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.authzExtensions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1beta1.DepService.DeleteAuthzExtension" `  




#### `DeleteLbEdgeExtension`

  * **Method** : `google.cloud.networkservices.v1beta1.DepService.DeleteLbEdgeExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbEdgeExtensions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1beta1.DepService.DeleteLbEdgeExtension" `  




#### `DeleteLbRouteExtension`

  * **Method** : `google.cloud.networkservices.v1beta1.DepService.DeleteLbRouteExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbRouteExtensions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1beta1.DepService.DeleteLbRouteExtension" `  




#### `DeleteLbTcpExtension`

  * **Method** : `google.cloud.networkservices.v1beta1.DepService.DeleteLbTcpExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbTcpExtensions.deleteForNetwork - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1beta1.DepService.DeleteLbTcpExtension" `  




#### `DeleteLbTrafficExtension`

  * **Method** : `google.cloud.networkservices.v1beta1.DepService.DeleteLbTrafficExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbTrafficExtensions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1beta1.DepService.DeleteLbTrafficExtension" `  




#### `GetAuthzExtension`

  * **Method** : `google.cloud.networkservices.v1beta1.DepService.GetAuthzExtension`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.authzExtensions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1beta1.DepService.GetAuthzExtension" `  




#### `GetLbEdgeExtension`

  * **Method** : `google.cloud.networkservices.v1beta1.DepService.GetLbEdgeExtension`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.lbEdgeExtensions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1beta1.DepService.GetLbEdgeExtension" `  




#### `GetLbRouteExtension`

  * **Method** : `google.cloud.networkservices.v1beta1.DepService.GetLbRouteExtension`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.lbRouteExtensions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1beta1.DepService.GetLbRouteExtension" `  




#### `GetLbTcpExtension`

  * **Method** : `google.cloud.networkservices.v1beta1.DepService.GetLbTcpExtension`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.lbTcpExtensions.getForNetwork - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1beta1.DepService.GetLbTcpExtension" `  




#### `GetLbTrafficExtension`

  * **Method** : `google.cloud.networkservices.v1beta1.DepService.GetLbTrafficExtension`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.lbTrafficExtensions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1beta1.DepService.GetLbTrafficExtension" `  




#### `ListAuthzExtensions`

  * **Method** : `google.cloud.networkservices.v1beta1.DepService.ListAuthzExtensions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.authzExtensions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1beta1.DepService.ListAuthzExtensions" `  




#### `ListLbEdgeExtensions`

  * **Method** : `google.cloud.networkservices.v1beta1.DepService.ListLbEdgeExtensions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.lbEdgeExtensions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1beta1.DepService.ListLbEdgeExtensions" `  




#### `ListLbRouteExtensions`

  * **Method** : `google.cloud.networkservices.v1beta1.DepService.ListLbRouteExtensions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.lbRouteExtensions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1beta1.DepService.ListLbRouteExtensions" `  




#### `ListLbTcpExtensions`

  * **Method** : `google.cloud.networkservices.v1beta1.DepService.ListLbTcpExtensions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.lbTcpExtensions.listForNetwork - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1beta1.DepService.ListLbTcpExtensions" `  




#### `ListLbTrafficExtensions`

  * **Method** : `google.cloud.networkservices.v1beta1.DepService.ListLbTrafficExtensions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.lbTrafficExtensions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1beta1.DepService.ListLbTrafficExtensions" `  




#### `UpdateAuthzExtension`

  * **Method** : `google.cloud.networkservices.v1beta1.DepService.UpdateAuthzExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.authzExtensions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1beta1.DepService.UpdateAuthzExtension" `  




#### `UpdateLbEdgeExtension`

  * **Method** : `google.cloud.networkservices.v1beta1.DepService.UpdateLbEdgeExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbEdgeExtensions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1beta1.DepService.UpdateLbEdgeExtension" `  




#### `UpdateLbRouteExtension`

  * **Method** : `google.cloud.networkservices.v1beta1.DepService.UpdateLbRouteExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbRouteExtensions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1beta1.DepService.UpdateLbRouteExtension" `  




#### `UpdateLbTcpExtension`

  * **Method** : `google.cloud.networkservices.v1beta1.DepService.UpdateLbTcpExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbTcpExtensions.updateForNetwork - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1beta1.DepService.UpdateLbTcpExtension" `  




#### `UpdateLbTrafficExtension`

  * **Method** : `google.cloud.networkservices.v1beta1.DepService.UpdateLbTrafficExtension`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.lbTrafficExtensions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkservices.v1beta1.DepService.UpdateLbTrafficExtension" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.edgeCacheKeysets.getIamPolicy - ADMIN_READ`
    * `networkservices.edgeCacheOrigins.getIamPolicy - ADMIN_READ`
    * `networkservices.edgeCacheServices.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkservices.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkservices.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.cloud.networkservices.v1alpha1.DepService.CreateSwpSecurityExtension`
  * `google.cloud.networkservices.v1alpha1.DepService.DeleteSwpSecurityExtension`
  * `google.cloud.networkservices.v1alpha1.DepService.GetSwpSecurityExtension`
  * `google.cloud.networkservices.v1alpha1.DepService.ListSwpSecurityExtensions`
  * `google.cloud.networkservices.v1alpha1.DepService.UpdateSwpSecurityExtension`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

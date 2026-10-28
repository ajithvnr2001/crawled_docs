---
url: https://docs.cloud.google.com/knowledge-catalog/docs/audit-logging/
title: Knowledge Catalog audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T19:00:10.319859+00:00
---

# Knowledge Catalog audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/audit-logging/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Knowledge Catalog audit logging Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Audit Logs for Knowledge Catalog let you track administrative and data-access operations on your resources to help you monitor access and configuration changes. You can query these logs in the Logs Explorer and check which Knowledge Catalog API methods generate Cloud Audit Logs.

For more information about Cloud Audit Logs, see the following documents:

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Knowledge Catalog audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="dataplex.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Knowledge Catalog generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.dataplex.v1.CatalogService.GetAspectType`  
`google.cloud.dataplex.v1.CatalogService.GetEntry`  
`google.cloud.dataplex.v1.CatalogService.GetEntryGroup`  
`google.cloud.dataplex.v1.CatalogService.GetEntryType`  
`google.cloud.dataplex.v1.CatalogService.GetMetadataJob`  
`google.cloud.dataplex.v1.CatalogService.ListAspectTypes`  
`google.cloud.dataplex.v1.CatalogService.ListEntries`  
`google.cloud.dataplex.v1.CatalogService.ListEntryGroups`  
`google.cloud.dataplex.v1.CatalogService.ListEntryTypes`  
`google.cloud.dataplex.v1.CatalogService.ListMetadataJobs`  
`google.cloud.dataplex.v1.CatalogService.LookupEntry`  
`google.cloud.dataplex.v1.DataScanService.ListDataScanJobs`  
`google.cloud.dataplex.v1.DataScanService.ListDataScans`  
`google.cloud.dataplex.v1.DataplexService.GetAsset`  
`google.cloud.dataplex.v1.DataplexService.GetJob`  
`google.cloud.dataplex.v1.DataplexService.GetLake`  
`google.cloud.dataplex.v1.DataplexService.GetTask`  
`google.cloud.dataplex.v1.DataplexService.GetZone`  
`google.cloud.dataplex.v1.DataplexService.ListAssetActions`  
`google.cloud.dataplex.v1.DataplexService.ListAssets`  
`google.cloud.dataplex.v1.DataplexService.ListJobs`  
`google.cloud.dataplex.v1.DataplexService.ListLakeActions`  
`google.cloud.dataplex.v1.DataplexService.ListLakes`  
`google.cloud.dataplex.v1.DataplexService.ListTasks`  
`google.cloud.dataplex.v1.DataplexService.ListZoneActions`  
`google.cloud.dataplex.v1.DataplexService.ListZones`  
`GetIamPolicy`  
`ADMIN_WRITE` | `google.cloud.dataplex.v1.CatalogService.CancelMetadataJob`  
`google.cloud.dataplex.v1.CatalogService.CreateAspectType` (LRO)  
`google.cloud.dataplex.v1.CatalogService.CreateEntry`  
`google.cloud.dataplex.v1.CatalogService.CreateEntryGroup` (LRO)  
`google.cloud.dataplex.v1.CatalogService.CreateEntryType` (LRO)  
`google.cloud.dataplex.v1.CatalogService.CreateMetadataJob` (LRO)  
`google.cloud.dataplex.v1.CatalogService.DeleteAspectType` (LRO)  
`google.cloud.dataplex.v1.CatalogService.DeleteEntry`  
`google.cloud.dataplex.v1.CatalogService.DeleteEntryGroup` (LRO)  
`google.cloud.dataplex.v1.CatalogService.DeleteEntryType` (LRO)  
`google.cloud.dataplex.v1.CatalogService.UpdateAspectType` (LRO)  
`google.cloud.dataplex.v1.CatalogService.UpdateEntry`  
`google.cloud.dataplex.v1.CatalogService.UpdateEntryGroup` (LRO)  
`google.cloud.dataplex.v1.CatalogService.UpdateEntryType` (LRO)  
`google.cloud.dataplex.v1.DataScanService.CreateDataScan` (LRO)  
`google.cloud.dataplex.v1.DataScanService.DeleteDataScan` (LRO)  
`google.cloud.dataplex.v1.DataScanService.RunDataScan`  
`google.cloud.dataplex.v1.DataScanService.UpdateDataScan` (LRO)  
`google.cloud.dataplex.v1.DataplexService.CancelJob`  
`google.cloud.dataplex.v1.DataplexService.CreateAsset` (LRO)  
`google.cloud.dataplex.v1.DataplexService.CreateLake` (LRO)  
`google.cloud.dataplex.v1.DataplexService.CreateTask` (LRO)  
`google.cloud.dataplex.v1.DataplexService.CreateZone` (LRO)  
`google.cloud.dataplex.v1.DataplexService.DeleteAsset` (LRO)  
`google.cloud.dataplex.v1.DataplexService.DeleteLake` (LRO)  
`google.cloud.dataplex.v1.DataplexService.DeleteTask` (LRO)  
`google.cloud.dataplex.v1.DataplexService.DeleteZone` (LRO)  
`google.cloud.dataplex.v1.DataplexService.RunTask`  
`google.cloud.dataplex.v1.DataplexService.UpdateAsset` (LRO)  
`google.cloud.dataplex.v1.DataplexService.UpdateLake` (LRO)  
`google.cloud.dataplex.v1.DataplexService.UpdateTask` (LRO)  
`google.cloud.dataplex.v1.DataplexService.UpdateZone` (LRO)  
`SetIamPolicy`  
`DATA_READ` | `google.cloud.dataplex.v1.DataScanService.GenerateDataQualityRules`  
`google.cloud.dataplex.v1.DataScanService.GetDataScan`  
`google.cloud.dataplex.v1.DataScanService.GetDataScanJob`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Knowledge Catalog.

### `google.cloud.dataplex.v1.CatalogService`

The following audit logs are associated with methods belonging to `google.cloud.dataplex.v1.CatalogService`.

#### `CancelMetadataJob`

  * **Method** : `google.cloud.dataplex.v1.CatalogService.CancelMetadataJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.metadataJobs.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.CatalogService.CancelMetadataJob" `  




#### `CreateAspectType`

  * **Method** : `google.cloud.dataplex.v1.CatalogService.CreateAspectType`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.aspectTypes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.CatalogService.CreateAspectType" `  




#### `CreateEntry`

  * **Method** : `google.cloud.dataplex.v1.CatalogService.CreateEntry`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : See IAM documentation for permissions.
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.CatalogService.CreateEntry" `  




#### `CreateEntryGroup`

  * **Method** : `google.cloud.dataplex.v1.CatalogService.CreateEntryGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.entryGroups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.CatalogService.CreateEntryGroup" `  




#### `CreateEntryType`

  * **Method** : `google.cloud.dataplex.v1.CatalogService.CreateEntryType`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.entryTypes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.CatalogService.CreateEntryType" `  




#### `CreateMetadataJob`

  * **Method** : `google.cloud.dataplex.v1.CatalogService.CreateMetadataJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.aspectTypes.use - ADMIN_WRITE`
    * `dataplex.entryTypes.use - ADMIN_WRITE`
    * `dataplex.metadataJobs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.CatalogService.CreateMetadataJob" `  




#### `DeleteAspectType`

  * **Method** : `google.cloud.dataplex.v1.CatalogService.DeleteAspectType`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.aspectTypes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.CatalogService.DeleteAspectType" `  




#### `DeleteEntry`

  * **Method** : `google.cloud.dataplex.v1.CatalogService.DeleteEntry`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.entries.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.CatalogService.DeleteEntry" `  




#### `DeleteEntryGroup`

  * **Method** : `google.cloud.dataplex.v1.CatalogService.DeleteEntryGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.entryGroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.CatalogService.DeleteEntryGroup" `  




#### `DeleteEntryType`

  * **Method** : `google.cloud.dataplex.v1.CatalogService.DeleteEntryType`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.entryTypes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.CatalogService.DeleteEntryType" `  




#### `GetAspectType`

  * **Method** : `google.cloud.dataplex.v1.CatalogService.GetAspectType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.aspectTypes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.CatalogService.GetAspectType" `  




#### `GetEntry`

  * **Method** : `google.cloud.dataplex.v1.CatalogService.GetEntry`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.entries.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.CatalogService.GetEntry" `  




#### `GetEntryGroup`

  * **Method** : `google.cloud.dataplex.v1.CatalogService.GetEntryGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.entryGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.CatalogService.GetEntryGroup" `  




#### `GetEntryType`

  * **Method** : `google.cloud.dataplex.v1.CatalogService.GetEntryType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.entryTypes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.CatalogService.GetEntryType" `  




#### `GetMetadataJob`

  * **Method** : `google.cloud.dataplex.v1.CatalogService.GetMetadataJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.metadataJobs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.CatalogService.GetMetadataJob" `  




#### `ListAspectTypes`

  * **Method** : `google.cloud.dataplex.v1.CatalogService.ListAspectTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.aspectTypes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.CatalogService.ListAspectTypes" `  




#### `ListEntries`

  * **Method** : `google.cloud.dataplex.v1.CatalogService.ListEntries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.entries.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.CatalogService.ListEntries" `  




#### `ListEntryGroups`

  * **Method** : `google.cloud.dataplex.v1.CatalogService.ListEntryGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.entryGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.CatalogService.ListEntryGroups" `  




#### `ListEntryTypes`

  * **Method** : `google.cloud.dataplex.v1.CatalogService.ListEntryTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.entryTypes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.CatalogService.ListEntryTypes" `  




#### `ListMetadataJobs`

  * **Method** : `google.cloud.dataplex.v1.CatalogService.ListMetadataJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.metadataJobs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.CatalogService.ListMetadataJobs" `  




#### `LookupEntry`

  * **Method** : `google.cloud.dataplex.v1.CatalogService.LookupEntry`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `aiplatform.datasets.get - ADMIN_READ`
    * `dataplex.glossaryTerms.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.CatalogService.LookupEntry" `  




#### `UpdateAspectType`

  * **Method** : `google.cloud.dataplex.v1.CatalogService.UpdateAspectType`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.aspectTypes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.CatalogService.UpdateAspectType" `  




#### `UpdateEntry`

  * **Method** : `google.cloud.dataplex.v1.CatalogService.UpdateEntry`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : See IAM documentation for permissions.
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.CatalogService.UpdateEntry" `  




#### `UpdateEntryGroup`

  * **Method** : `google.cloud.dataplex.v1.CatalogService.UpdateEntryGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.entryGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.CatalogService.UpdateEntryGroup" `  




#### `UpdateEntryType`

  * **Method** : `google.cloud.dataplex.v1.CatalogService.UpdateEntryType`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.entryTypes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.CatalogService.UpdateEntryType" `  




### `google.cloud.dataplex.v1.DataScanService`

The following audit logs are associated with methods belonging to `google.cloud.dataplex.v1.DataScanService`.

#### `CreateDataScan`

  * **Method** : `google.cloud.dataplex.v1.DataScanService.CreateDataScan`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.datascans.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataScanService.CreateDataScan" `  




#### `DeleteDataScan`

  * **Method** : `google.cloud.dataplex.v1.DataScanService.DeleteDataScan`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.datascans.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataScanService.DeleteDataScan" `  




#### `GenerateDataQualityRules`

  * **Method** : `google.cloud.dataplex.v1.DataScanService.GenerateDataQualityRules`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.datascans.getData - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataScanService.GenerateDataQualityRules" `  




#### `GetDataScan`

  * **Method** : `google.cloud.dataplex.v1.DataScanService.GetDataScan`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.datascans.get - ADMIN_READ`
    * `dataplex.datascans.getData - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataScanService.GetDataScan" `  




#### `GetDataScanJob`

  * **Method** : `google.cloud.dataplex.v1.DataScanService.GetDataScanJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.datascans.get - ADMIN_READ`
    * `dataplex.datascans.getData - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataScanService.GetDataScanJob" `  




#### `ListDataScanJobs`

  * **Method** : `google.cloud.dataplex.v1.DataScanService.ListDataScanJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.datascans.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataScanService.ListDataScanJobs" `  




#### `ListDataScans`

  * **Method** : `google.cloud.dataplex.v1.DataScanService.ListDataScans`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.datascans.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataScanService.ListDataScans" `  




#### `RunDataScan`

  * **Method** : `google.cloud.dataplex.v1.DataScanService.RunDataScan`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.datascans.run - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataScanService.RunDataScan" `  




#### `UpdateDataScan`

  * **Method** : `google.cloud.dataplex.v1.DataScanService.UpdateDataScan`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.datascans.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataScanService.UpdateDataScan" `  




### `google.cloud.dataplex.v1.DataplexService`

The following audit logs are associated with methods belonging to `google.cloud.dataplex.v1.DataplexService`.

#### `CancelJob`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.CancelJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.tasks.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.CancelJob" `  




#### `CreateAsset`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.CreateAsset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.assets.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.CreateAsset" `  




#### `CreateLake`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.CreateLake`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.lakes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.CreateLake" `  




#### `CreateTask`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.CreateTask`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.tasks.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.CreateTask" `  




#### `CreateZone`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.CreateZone`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.zones.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.CreateZone" `  




#### `DeleteAsset`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.DeleteAsset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.assets.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.DeleteAsset" `  




#### `DeleteLake`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.DeleteLake`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.lakes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.DeleteLake" `  




#### `DeleteTask`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.DeleteTask`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.tasks.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.DeleteTask" `  




#### `DeleteZone`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.DeleteZone`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.zones.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.DeleteZone" `  




#### `GetAsset`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.GetAsset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.assets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.GetAsset" `  




#### `GetJob`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.GetJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.tasks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.GetJob" `  




#### `GetLake`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.GetLake`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.lakes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.GetLake" `  




#### `GetTask`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.GetTask`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.tasks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.GetTask" `  




#### `GetZone`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.GetZone`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.zones.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.GetZone" `  




#### `ListAssetActions`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.ListAssetActions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.assetActions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.ListAssetActions" `  




#### `ListAssets`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.ListAssets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.assets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.ListAssets" `  




#### `ListJobs`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.ListJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.tasks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.ListJobs" `  




#### `ListLakeActions`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.ListLakeActions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.lakeActions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.ListLakeActions" `  




#### `ListLakes`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.ListLakes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.lakes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.ListLakes" `  




#### `ListTasks`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.ListTasks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.tasks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.ListTasks" `  




#### `ListZoneActions`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.ListZoneActions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.zoneActions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.ListZoneActions" `  




#### `ListZones`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.ListZones`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.zones.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.ListZones" `  




#### `RunTask`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.RunTask`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.tasks.run - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.RunTask" `  




#### `UpdateAsset`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.UpdateAsset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.assets.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.UpdateAsset" `  




#### `UpdateLake`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.UpdateLake`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.lakes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.UpdateLake" `  




#### `UpdateTask`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.UpdateTask`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.tasks.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.UpdateTask" `  




#### `UpdateZone`

  * **Method** : `google.cloud.dataplex.v1.DataplexService.UpdateZone`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.zones.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataplex.v1.DataplexService.UpdateZone" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataplex.entryGroups.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataplex.assets.setIamPolicy - ADMIN_WRITE`
    * `dataplex.dataProducts.setIamPolicy - ADMIN_WRITE`
    * `dataplex.datascans.setIamPolicy - ADMIN_WRITE`
    * `dataplex.lakes.setIamPolicy - ADMIN_WRITE`
    * `dataplex.zones.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="SetIamPolicy" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.longrunning.Operations.CancelOperation`
  * `google.longrunning.Operations.DeleteOperation`
  * `google.longrunning.Operations.GetOperation`
  * `google.longrunning.Operations.ListOperations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

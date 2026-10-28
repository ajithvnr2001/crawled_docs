---
url: https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/
title: Cloud Service Mesh audit logging \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:05:02.605873+00:00
---

# Cloud Service Mesh audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/

[ Skip to main content ](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/)
  * [Deutsch](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/?hl=es-419)
  * [Français](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/?hl=id)
  * [Italiano](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/?hl=ja)
  * [한국어](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fservice-mesh%2Fv1.29%2Fdocs%2Faudit-logging-td%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/networking-color.svg) ](https://docs.cloud.google.com/service-mesh/v1.29/docs)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.29/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Service name](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/#service_name)
  * [Methods by permission type](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/#permission-type)
  * [API interface audit logs](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/#api-interface-reference)
    * [envoy.service.discovery.v3.AggregatedDiscoveryService](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/#envoy.service.discovery.v3.AggregatedDiscoveryService)
    * [envoy.service.load_stats.v3.LoadReportingService](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/#envoy.service.load_stats.v3.LoadReportingService)
    * [envoy.service.status.v3.ClientStatusDiscoveryService](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/#envoy.service.status.v3.ClientStatusDiscoveryService)
  * [Methods that don't produce audit logs](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/#exempt-methods)


Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.29/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview)


Was this helpful?
Send feedback 
  * On this page
  * [Service name](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/#service_name)
  * [Methods by permission type](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/#permission-type)
  * [API interface audit logs](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/#api-interface-reference)
    * [envoy.service.discovery.v3.AggregatedDiscoveryService](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/#envoy.service.discovery.v3.AggregatedDiscoveryService)
    * [envoy.service.load_stats.v3.LoadReportingService](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/#envoy.service.load_stats.v3.LoadReportingService)
    * [envoy.service.status.v3.ClientStatusDiscoveryService](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/#envoy.service.status.v3.ClientStatusDiscoveryService)
  * [Methods that don't produce audit logs](https://docs.cloud.google.com/service-mesh/v1.29/docs/audit-logging-td/#exempt-methods)


# Cloud Service Mesh audit logging Stay organized with collections  Save and categorize content based on your preferences.
Cloud Audit Logs for Cloud Service Mesh let you track administrative and data-access operations on your resources to help you monitor access and configuration changes. You can query these logs in the Logs Explorer and check which Cloud Service Mesh API methods generate Cloud Audit Logs.
For more information about Cloud Audit Logs, see the following documents:
  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)


## Service name
To view the Cloud Service Mesh audit logs, do the following:
  1. In the Google Cloud console, go to the Logs Explorer page:
[Go to Logs Explorer](https://console.cloud.google.com/logs/query)
  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.

```
    protoPayload.serviceName="trafficdirector.googleapis.com"
  
```



## Methods by permission type
Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud Service Mesh generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.
API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro).   
| Permission type  | Methods  |  
| --- | --- |  
| `DATA_READ`  |  `envoy.service.discovery.v3.AggregatedDiscoveryService.DeltaAggregatedResources`  
`envoy.service.discovery.v3.AggregatedDiscoveryService.StreamAggregatedResources`  
`envoy.service.status.v3.ClientStatusDiscoveryService.StreamClientStatus`  |  
| `DATA_WRITE`  | `envoy.service.load_stats.v3.LoadReportingService.StreamLoadStats`  |  
## API interface audit logs
For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud Service Mesh.
### `envoy.service.discovery.v3.AggregatedDiscoveryService`
The following audit logs are associated with methods belonging to `envoy.service.discovery.v3.AggregatedDiscoveryService`.
#### `DeltaAggregatedResources`
  * **Method** : `envoy.service.discovery.v3.AggregatedDiscoveryService.DeltaAggregatedResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `trafficdirector.networks.getConfigs - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : `     protoPayload.methodName="envoy.service.discovery.v3.AggregatedDiscoveryService.DeltaAggregatedResources"   `  



#### `StreamAggregatedResources`
  * **Method** : `envoy.service.discovery.v3.AggregatedDiscoveryService.StreamAggregatedResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `trafficdirector.googleapis.com/networks.getConfigs - DATA_READ`
    * `trafficdirector.networks.getConfigs - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : `     protoPayload.methodName="envoy.service.discovery.v3.AggregatedDiscoveryService.StreamAggregatedResources"   `  



### `envoy.service.load_stats.v3.LoadReportingService`
The following audit logs are associated with methods belonging to `envoy.service.load_stats.v3.LoadReportingService`.
#### `StreamLoadStats`
  * **Method** : `envoy.service.load_stats.v3.LoadReportingService.StreamLoadStats`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `trafficdirector.networks.reportMetrics - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : `     protoPayload.methodName="envoy.service.load_stats.v3.LoadReportingService.StreamLoadStats"   `  



### `envoy.service.status.v3.ClientStatusDiscoveryService`
The following audit logs are associated with methods belonging to `envoy.service.status.v3.ClientStatusDiscoveryService`.
#### `StreamClientStatus`
  * **Method** : `envoy.service.status.v3.ClientStatusDiscoveryService.StreamClientStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `trafficdirector.networks.getConfigs - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : `     protoPayload.methodName="envoy.service.status.v3.ClientStatusDiscoveryService.StreamClientStatus"   `  



## Methods that don't produce audit logs
A method might not produce audit logs for one or more of the following reasons: 
  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.


The following methods don't produce audit logs:
  * `envoy.service.rate_limit_quota.v3.RateLimitQuotaService.StreamRateLimitQuotas`


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-27 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

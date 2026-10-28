---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-obj/
title: Object storage (OBJ) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:29:12.423996+00:00
---

# Object storage (OBJ)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-obj/

[ Skip to main content ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-obj/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-obj/)
  * [Deutsch](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-obj/?hl=de)
  * [Español](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-obj/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-obj/?hl=es-419)
  * [Français](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-obj/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-obj/?hl=id)
  * [Italiano](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-obj/?hl=it)
  * [Português](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-obj/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-obj/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-obj/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-obj/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-obj/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-obj/?hl=ja)
  * [한국어](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-obj/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/distributed-cloud-color.svg) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)


[Start free](https://console.cloud.google.com/freetrial)
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)


Was this helpful?
Send feedback 
#  Object storage (OBJ) Stay organized with collections  Save and categorize content based on your preferences.  
|  Name and description   |  Type   |  Emit duration   |  Labels   |  
| --- | --- | --- | --- |  
|  `  obj_buckets_count   `  |  
|  The number of buckets in object storage, across all tenants.  |  Gauge   |  1 m   |  _Not applicable_  |  
|  `  obj_objects_count   `  |  
|  The number of objects in object storage, across all tenants.  |  Gauge   |  1 m   |  _Not applicable_  |  
|  `  obj_s3_operations_count `  |  
|  The number of operations in object storage, sliced by instance, and whether they have succeeded.  |  Count   |  1 m   | 
  * **node_name**
  * **success_label**

 |  
|  `  obj_storage_used_capacity_bytes `  |  
|  The number of bytes of stored data, sliced by instance.  |  Gauge   |  1 m   |  **node_name**  |  
|  `  obj_storage_available_capacity_bytes    `  |  
|  The number of bytes of remaining available storage, sliced by instance.  |  Gauge   |  1 m   |  **node_name**  |  
|  `  metering_obj_used_capacity_bytes    `  |  
|  The number of bytes of consumed capacity, sliced by tenant.  |  Gauge   |  1 m   | 
  * **objectstorage_tenant_id**
  * **tenant_type**
  * **sku_id**
  * **sku_name**
  * **organization**

 |  
|  `  obj_storage_status  `  |  
|  The status of storage services, sliced by instance. Attribute values are: 0 = No Errors, 10 = In Transition, 20 = Insufficient Free Space, 30 = Volume(s) Unavailable, 40 = Error.  |  Gauge   |  1 m   |  **node_name**  |  
|  `  obj_appliance_failed_disks  `  |  
|  The number of drives that are not optimal in storage appliance, sliced by instance.  |  Gauge   |  1 m   |  **node_name**  |  
|  `  obj_storage_auditlog_fs_size_bytes  `  |  
|  The size of the audit log file system drive in bytes.  |  Gauge   |  1 m   |  **node_name**  |  
|  `  obj_storage_auditlog_fs_avail_bytes `  |  
|  The available size left in bytes for the audit log file system drive.  |  Gauge   |  1 m   |  **node_name**  |  
|  `  obj_tenant_used_capacity_bytes_count    `  |  
|  The number of bytes consumed in object storage, sliced by bucket, SKU ID, SKU name, and tenant type.  |  Gauge   |  1 m   | 
  * **bucket**
  * **sku_name**
  * **sku_id**
  * **tenant_type**
  * **_gdch_project**

 |  
|  `  obj_tenant_objects_count    `  |  
|  The number of objects in object storage, sliced by bucket, SKU ID, SKU name, and tenant type.  |  Gauge   |  1 m   | 
  * **bucket**
  * **sku_name**
  * **sku_id**
  * **tenant_type**
  * **_gdch_project**

 |  
|  `  obj_tenant_quota_bytes  `  |  
|  The quota of a tenant in object storage, sliced by SKU ID, SKU name, and tenant type.  |  Count   |  1 m   | 
  * **sku_name**
  * **sku_id**
  * **tenant_type**
  * **_gdch_project**

 |  
|  `  obj_objects_served_bytes_total  `  |  
|  The number of bytes served via object media GET operations in object storage, sliced by tenant.  |  Count   |  1 m   | 
  * **objectstorage_tenant_id**
  * **tenant_type**
  * **storage_class**
  * **organization**

 |  
|  `  obj_s3_operations_class_total   `  |  
|  The number of S3 API operations in object storage, sliced by tenant and operation class.  |  Count   |  1 m   | 
  * **objectstorage_tenant_id**
  * **operation_class**
  * **tenant_type**
  * **storage_class**
  * **organization**

 |  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

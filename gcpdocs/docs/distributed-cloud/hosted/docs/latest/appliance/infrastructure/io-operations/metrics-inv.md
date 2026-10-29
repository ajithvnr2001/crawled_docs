---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations/metrics-inv/
title: Inventory management (INV) \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T06:00:52.148463+00:00
---

# Inventory management (INV)  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations/metrics-inv/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Inventory management (INV) Stay organized with collections  Save and categorize content based on your preferences. 

## Metrics list

Name and description | Type | Emit duration | Labels  
---|---|---|---  
`inv_unauthorized_image`  
Indicates whether an unauthorized container image is detected in a Pod (`1` when any container, init container, or ephemeral container image is not from an authorized registry; `0` when all images are authorized). Triggers alert `INV-E0001` (runbook `INV-R0001`). | Gauge | 1 m | 

  * **pod** : The name of the Pod using the unauthorized image.
  * **namespace** : The namespace of the Pod.

  
`kube_pod_controller_restarts_total`  
Total number of container restarts per controller Pod (recording rule aggregated from `kube_pod_container_status_restarts_total`). Used on the `INV: Golden Signals` dashboard to monitor the controller restart rate in `inv-system`. | Counter | 1 m | 

  * **namespace** : The namespace of the controller Pod (for example, `inv-system`).
  * **controller** : The controller prefix extracted from the Pod name.
  * **container** : The name of the container.
  * **zone_id** : The identifier of the zone.

  
`inv:export_hardware:last_success_ts`  
Unix timestamp in seconds of the last successful run of the `inv-export-hw-backend` CronJob in `gpc-system` (recording rule based on `kube_cronjob_status_last_successful_time`). | Gauge | 1 m | 

  * **namespace** : The namespace of the CronJob (`gpc-system`).
  * **cronjob** : The name of the CronJob (`inv-export-hw-backend`).

  
`inv:export_hardware:last_success_age`  
Time elapsed in seconds since the last successful run of the `inv-export-hw-backend` hardware inventory export CronJob, or `-1` if it has never succeeded. Used on the `INV: Golden Signals` dashboard and runbook `INV-R0011`. | Gauge | 1 m |   
`inv:export_hardware:next_scheduled_age`  
Time remaining in seconds until the next scheduled run of the `inv-export-hw-backend` CronJob, or `-1` if not scheduled. Used on the `INV: Golden Signals` dashboard. | Gauge | 1 m |   
`inv:export_hardware:good`  
Freshness indicator timestamp for the `inv-export-hw-backend` CronJob, clamped to 25 hours after `inv:export_hardware:last_success_ts`. Used on the `INV: Golden Signals` dashboard (`rate(inv:export_hardware:good[5m]) >bool 0`) to indicate whether the export pipeline is fresh (`1`) or stale (`0`). | Gauge | 1 m |   
`inv:export_hardware:total`  
Current evaluation Unix timestamp in seconds for the hardware inventory export recording rule group. | Gauge | 1 m |   
`inv:export_images:last_success_ts`  
Unix timestamp in seconds of the last successful run of the `inv-export-img-backend` CronJob in `gpc-system` (recording rule based on `kube_cronjob_status_last_successful_time`). | Gauge | 1 m | 

  * **namespace** : The namespace of the CronJob (`gpc-system`).
  * **cronjob** : The name of the CronJob (`inv-export-img-backend`).

  
`inv:export_images:last_success_age`  
Time elapsed in seconds since the last successful run of the `inv-export-img-backend` software inventory export CronJob, or `-1` if it has never succeeded. Used on the `INV: Golden Signals` dashboard and runbook `INV-R0012`. | Gauge | 1 m |   
`inv:export_images:next_scheduled_age`  
Time remaining in seconds until the next scheduled run of the `inv-export-img-backend` CronJob, or `-1` if not scheduled. Used on the `INV: Golden Signals` dashboard. | Gauge | 1 m |   
`inv:export_images:good`  
Freshness indicator timestamp for the `inv-export-img-backend` CronJob, clamped to 25 hours after `inv:export_images:last_success_ts`. Used on the `INV: Golden Signals` dashboard (`rate(inv:export_images:good[5m]) >bool 0`) to indicate whether the export pipeline is fresh (`1`) or stale (`0`). | Gauge | 1 m |   
`inv:export_images:total`  
Current evaluation Unix timestamp in seconds for the software inventory export recording rule group. | Gauge | 1 m |   
`inv:bucket_clamav:last_success_ts`  
Unix timestamp in seconds of the last successful run of the `inv-bucket-clamav-backend` CronJob in `inv-system` (recording rule based on `kube_cronjob_status_last_successful_time`). | Gauge | 1 m | 

  * **namespace** : The namespace of the CronJob (`inv-system`).
  * **cronjob** : The name of the CronJob (`inv-bucket-clamav-backend`).

  
`inv:bucket_clamav:last_success_age`  
Time elapsed in seconds since the last successful run of the `inv-bucket-clamav-backend` ClamAV bucket scan CronJob, or `-1` if it has never succeeded. Used on the `INV: Golden Signals` dashboard. | Gauge | 1 m |   
`inv:bucket_clamav:next_scheduled_age`  
Time remaining in seconds until the next scheduled run of the `inv-bucket-clamav-backend` CronJob, or `-1` if not scheduled. Used on the `INV: Golden Signals` dashboard. | Gauge | 1 m |   
`inv:bucket_clamav:good`  
Freshness indicator timestamp for the `inv-bucket-clamav-backend` CronJob, clamped to 25 hours after `inv:bucket_clamav:last_success_ts`. Used on the `INV: Golden Signals` dashboard (`rate(inv:bucket_clamav:good[5m]) >bool 0`) to indicate whether the scan pipeline is fresh (`1`) or stale (`0`). | Gauge | 1 m |   
`inv:bucket_clamav:total`  
Current evaluation Unix timestamp in seconds for the ClamAV bucket scan recording rule group. | Gauge | 1 m |   
`inv:audit_controller:bad`  
Cumulative container restarts for the `inv-audit-backend` controller (recording rule filtering `kube_pod_controller_restarts_total{controller="inv-audit-backend"}`). | Counter | 1 m | 

  * **namespace** : The namespace of the controller Pod.
  * **controller** : The controller name (`inv-audit-backend`).
  * **container** : The name of the container.
  * **zone_id** : The identifier of the zone.

  
`inv:audit_controller:total`  
Current evaluation Unix timestamp in seconds for the `audit-controller` recording rule group. | Gauge | 1 m |   
`inv:expansion_controller:bad`  
Cumulative container restarts for the `inv-expansion-backend` controller (recording rule filtering `kube_pod_controller_restarts_total{controller="inv-expansion-backend"}`). | Counter | 1 m | 

  * **namespace** : The namespace of the controller Pod.
  * **controller** : The controller name (`inv-expansion-backend`).
  * **container** : The name of the container.
  * **zone_id** : The identifier of the zone.

  
`inv:expansion_controller:total`  
Current evaluation Unix timestamp in seconds for the `expansion-controller` recording rule group. | Gauge | 1 m |   
`controller_runtime_reconcile_total`  
Total number of reconciliations per controller exposed on port `8080` (`/metrics`) by the `inv-core`, `inv-audit`, and `inv-expansion` controller managers. | Counter | 5 m | 

  * **controller** : The name of the reconciler controller.
  * **result** : The reconciliation outcome (`success`, `error`, `requeue`, or `requeue_after`).

  
`controller_runtime_reconcile_errors_total`  
Total number of reconciliation errors per controller exposed by the `inv-core`, `inv-audit`, and `inv-expansion` controller managers. | Counter | 5 m | 

  * **controller** : The name of the reconciler controller.

  
`controller_runtime_reconcile_time_seconds`  
Duration in seconds of each reconciliation per controller exposed by the `inv-core`, `inv-audit`, and `inv-expansion` controller managers. | Histogram | 5 m | 

  * **controller** : The name of the reconciler controller.

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/hub/docs/optimization-data/
title: About cost and utilization data \u00a0|\u00a0 Cloud Hub \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:55:33.519255+00:00
---

# About cost and utilization data  |  Cloud Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/hub/docs/optimization-data/

[ Skip to main content ](https://docs.cloud.google.com/hub/docs/optimization-data/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/hub/docs/optimization-data/)
  * [Deutsch](https://docs.cloud.google.com/hub/docs/optimization-data/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/hub/docs/optimization-data/?hl=es-419)
  * [Français](https://docs.cloud.google.com/hub/docs/optimization-data/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/hub/docs/optimization-data/?hl=id)
  * [Italiano](https://docs.cloud.google.com/hub/docs/optimization-data/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/hub/docs/optimization-data/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/hub/docs/optimization-data/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/hub/docs/optimization-data/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/hub/docs/optimization-data/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/hub/docs/optimization-data/?hl=ja)
  * [한국어](https://docs.cloud.google.com/hub/docs/optimization-data/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fhub%2Fdocs%2Foptimization-data%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/developer-tools-color.svg) ](https://docs.cloud.google.com/hub/docs)
  * [ Cloud Hub ](https://docs.cloud.google.com/hub/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Cost data](https://docs.cloud.google.com/hub/docs/optimization-data/#cost_data)
  * [Utilization data](https://docs.cloud.google.com/hub/docs/optimization-data/#utilization_data)
  * [Product categories](https://docs.cloud.google.com/hub/docs/optimization-data/#products)
    * [Resource-level costs](https://docs.cloud.google.com/hub/docs/optimization-data/#resource-costs)
  * [Application costs](https://docs.cloud.google.com/hub/docs/optimization-data/#application-costs)
  * [What's next](https://docs.cloud.google.com/hub/docs/optimization-data/#whats_next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Hub ](https://docs.cloud.google.com/hub/docs)
  * [ Guides ](https://docs.cloud.google.com/hub/docs/overview)


Was this helpful?
Send feedback 
#  About cost and utilization data Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Cost data](https://docs.cloud.google.com/hub/docs/optimization-data/#cost_data)
  * [Utilization data](https://docs.cloud.google.com/hub/docs/optimization-data/#utilization_data)
  * [Product categories](https://docs.cloud.google.com/hub/docs/optimization-data/#products)
    * [Resource-level costs](https://docs.cloud.google.com/hub/docs/optimization-data/#resource-costs)
  * [Application costs](https://docs.cloud.google.com/hub/docs/optimization-data/#application-costs)
  * [What's next](https://docs.cloud.google.com/hub/docs/optimization-data/#whats_next)


Cloud Hub lets you aggregate cost data and utilization metrics to make informed decisions about optimization opportunities. Review information in this document about the source, categorization, and limitations of the data to interpret the data more effectively.
## Cost data
  * **Source:** Cost data is based on the same information that powers your Cloud Billing reports and exports.
  * **Latency:** Google Cloud products report usage and cost data to Cloud Billing processes at varying intervals. You might see a delay between your use of Google Cloud services and when the usage and costs are available to the Cloud Hub. Typically, costs are available within a day, but this can sometimes take more than 24 hours.
  * **Gross costs:** The costs shown are generally _gross costs_ , reflecting usage at your contract prices _before_ any credits, such as Committed Use Discounts, sustained use discounts, or promotional credits, are applied.
  * **Currency:** When scoping by an App Hub application, all underlying resources within that application must use the same currency for costs to be aggregated. If resources are linked to billing accounts with different currencies, cost data for that application might be incomplete. 


## Utilization data
  * **Source:** Utilization metrics are sourced from Cloud Monitoring. 
  * **Availability:** Availability depends on the resource type and whether the appropriate agents (like the Ops Agent) are configured to collect detailed metrics.


## Product categories
The product names used in the Cloud Hub are designed to be logical and user-friendly. These might group costs differently than the service categories used within Cloud Billing reports. For example, costs that the Cloud Hub attributes to "Compute Engine" might encompass multiple underlying services from a Cloud Billing perspective.
Costs for products that the Cloud Hub doesn't support are reported under the product category **Other**. 
### Resource-level costs
This section lists supported products with resource-level cost data.
App Hub doesn't support all resources that the Cloud Hub supports, and there are some limitations for reported costs. For details, see [Application costs](https://docs.cloud.google.com/hub/docs/optimization-data/#application-costs).
[(Preview)](https://cloud.google.com/products#product-launch-stages) Data transfer costs are reported separately under **Networking costs** for some resources as indicated in the table of supported resources.   
| Product name  | Supported resources  | Additional information  |  
| --- | --- | --- |  
| AlloyDB for PostgreSQL  | Backup  
Cluster  
Instance  |   |  
| App Engine  | Service  |  Data transfer costs are reported separately as networking costs.   |  
| Backup for GKE  | Backup plan  |   |  
| Bigtable  | App Profile  
Instance  |  **For instances** : Data transfer costs are reported separately as networking costs.  |  
| Cloud Data Fusion  | Instance  |   |  
| Cloud Deploy  | Delivery pipeline  |   |  
| Cloud Interconnect ([Preview](https://cloud.google.com/products/#product-launch-stages))  | VLAN attachment  |  The resource cost includes the hourly cost of the VLAN attachment. Data transfer costs for the VLAN attachment are reported separately as networking costs. Data transfer costs are not attributed to the resources that use the VLAN attachment.  |  
| Cloud Load Balancing ([Preview](https://cloud.google.com/products/#product-launch-stages))  | Forwarding rule  
URL map  | Data transfer and processing costs are not attributed to the resources that use the forwarding rule or URL map. 
  * For forwarding rules, the cost includes the hourly cost of the forwarding rule plus any hourly charges for proxy instances.
  * For URL maps, the cost includes the hourly cost of all forwarding rules grouped under the URL map.

Data transfer and data processing costs for a forwarding rule or URL map are reported separately as networking costs.  |  
| Cloud Logging  | Log bucket  |   |  
| Cloud Run  | Job  
Service  | 
  * Utilization data for Cloud Run is available for the 6-week period before the current date.
  * Data transfer costs are reported separately as networking costs.

 |  
| Cloud Run functions  | Function  |  Data transfer costs are reported separately as networking costs.  |  
| Cloud SQL Admin API  | Instance  |   |  
| Cloud Storage  | Bucket  |  Data transfer costs are reported separately as networking costs.  |  
| Compute Engine  | Allocation  
Address  
Disk  
Forwarding rule  
Global address  
Image  
Instance  
Instant snapshot  
Machine image  
Managed instance group (MIG)  
Network attachment  
Reservation  
Snapshot  
Storage pool  
Target VPN gateway  
VPN gateway  
VPN tunnel  | 
  * Local storage costs are reported under the product Persistent Disk.
  * **For instances and MIGs** : Data transfer costs are reported separately as networking costs.

 |  
| Dataflow  | Job  
Snapshot  |   |  
| Dataproc Metastore  | Service  |   |  
| Firestore  | Database  |  Data transfer costs are reported separately as networking costs.  |  
| Google Kubernetes Engine  | Cluster  | 
  * Resource cost includes Compute Engine VMs (vCPU, RAM, GPU) and the GKE [ cluster management fee](https://cloud.google.com/kubernetes-engine/pricing#cluster-management-fee).
  * Data transfer costs are reported separately as networking costs.
  * Local storage costs are reported under the product Persistent Disk. 

 |  
| Managed Service for Apache Spark  | Batch  
Cluster  
Session  |  **For clusters** :
  * The resource cost includes the cost of the Compute Engine VMs (vCPU, RAM, GPU) and Managed Service for Apache Spark licensing fee.
  * Local storage costs are reported under the product Persistent Disk.
  * The following Managed Service for Apache Spark clusters don't support resource level costs: 
    * Clusters that use GKE as compute.
    * Clusters that use [unsupported image versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/image-version-lists#unsupported-image-versions)

 |  
| Managed Service for Microsoft Active Directory  | Domain  |   |  
| Memorystore for Redis  | Instance  |   |  
| Secret Manager  | Secret  |   |  
| Spanner  | Instance  
Database  |   |  
## Application costs
For an App Hub application, the total cost includes all resources that are fully used by the application.
The following limitations apply to application costs:
  * This total application cost doesn't include costs for the following: 
    * Resources that are shared across applications such as VLAN attachments.
    * Short-lived resources such as Managed Service for Apache Spark sessions and batches. 
  * Application cost only includes costs for resources that are [supported by App Hub](https://docs.cloud.google.com/app-hub/docs/supported-resources) and [supported by the Cloud Hub](https://docs.cloud.google.com/hub/docs/optimization-data/#resource-costs). 
  * The cost for an application is only available if all application resources are linked to billing accounts in the same currency. 
  * You can't filter resources by location.


## What's next
  * [Optimize resource costs and utilization](https://docs.cloud.google.com/hub/docs/optimize).


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

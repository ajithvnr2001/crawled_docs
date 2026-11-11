---
url: https://docs.cloud.google.com/lakehouse/docs/regions-capabilities-cross-cloud-connections/
title: Supported regions and CCI capabilities \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T08:30:33.616182+00:00
---

# Supported regions and CCI capabilities  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/regions-capabilities-cross-cloud-connections/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Supported regions and CCI capabilities Stay organized with collections  Save and categorize content based on your preferences. 

Borderless Lakehouse lets you use Cross-Cloud Interconnect to route remote query data reads and background metadata refresh privately across cloud providers. This document outlines supported Cross-Cloud Interconnect capabilities and classifications, and maps Amazon Web Services (AWS) regions to Google Cloud regions to help you optimize query performance.

## Supported Cross-Cloud Interconnect capabilities

Lakehouse supports routing query data reads, background metadata refresh, or both privately over Cross-Cloud Interconnect depending on whether your network isolation and cost requirements apply to object storage reads, control-plane catalog endpoints, or end-to-end cross-cloud traffic:

  * **Query transport (`--service-directory-name`):** Routes query reads to remote object storage (Amazon S3 on AWS or Microsoft Azure Data Lake Storage Gen2 on Azure) to help reduce egress costs and provide predictable query throughput.
  * **Background metadata refresh (`--metadata-service-directory-name`):** Routes control-plane background metadata refresh and authentication requests from the Lakehouse runtime catalog privately to remote catalog AWS PrivateLink or Azure Private Link endpoints.
  * **Supported catalogs and clouds:**

### # disableFinding(CORRECTION_VARIABLE_CLOUD) #

**AWS Glue Data Catalog:** AWS (Cross-Cloud Interconnect or Partner Cross-Cloud Interconnect).

    * **Databricks Unity Catalog:** AWS (Cross-Cloud Interconnect or Partner Cross-Cloud Interconnect) and Azure (Cross-Cloud Interconnect).
    * **Snowflake Horizon Catalog:** AWS (Cross-Cloud Interconnect or Partner Cross-Cloud Interconnect) and Azure (Cross-Cloud Interconnect).



For Azure deployments, create your federated catalog in the Google Cloud region closest to your Azure region and interconnect location. For supported Azure peering locations, see [Choose locations for Cross-Cloud Interconnect for Azure](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/choose-locations).

## Interconnect classifications

Lakehouse supports the following two types of Cross-Cloud Interconnect connections:

  * **Partner Cross-Cloud Interconnect (Partner CCI):** Provides pre-provisioned connectivity between Google Cloud and designated AWS regions through a supported partner. For more information, see the [Partner Cross-Cloud Interconnect for AWS overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-cci-for-aws-overview).
  * **Cross-Cloud Interconnect (CCI):** Provides a direct physical connection between the Google network and your cloud service provider. Cross-Cloud Interconnect is supported across all listed AWS and Azure regions. For more information, see the [Cross-Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#setup-process).



### Considerations

  * In the region mapping table, the **Low Latency** column indicates region pairs where the AWS region, the interconnect facility, and the closest Google Cloud region are in the same geographical metropolitan area.
  * If possible, choose a region pair with **Low Latency** or **Partner CCI** to ensure optimal performance when you federate large datasets across clouds.



## AWS to Google Cloud region mapping

AWS Region Name | AWS Region Metro | Closest Google Cloud Region Name | Closest Google Cloud Region Metro | Partner CCI | Low Latency | Top 3 Alternative Google Cloud Regions  
---|---|---|---|---|---|---  
**`us-east-1`** | N. Virginia | `us-east4` | Ashburn, VA | ✓ | ✓ | `us-east1`, `us-east5`, `us-central1`  
**`us-east-2`** | Ohio | `us-east5` | Columbus, OH |  | ✓ | `us-east4`, `us-east1`, `us-central1`  
**`us-west-1`** | N. California | `us-west2` | Los Angeles, CA | ✓ |  | `us-west4`, `us-west1`, `us-west3`  
**`us-west-2`** | Oregon | `us-west1` | The Dalles, OR | ✓ | ✓ | `us-west3`, `us-west4`, `us-west2`  
**`ca-central-1`** | Montreal | `northamerica-northeast1` | Montreal |  | ✓ | `northamerica-northeast2`, `us-east4`, `us-east5`  
**`sa-east-1`** | São Paulo | `southamerica-east1` | São Paulo |  | ✓ | `southamerica-west1`, `us-east1`, `us-south1`  
**`eu-west-1`** | Ireland | `europe-west1` | Belgium |  |  | `europe-west2`, `europe-west9`, `europe-west4`  
**`eu-west-2`** | London | `europe-west2` | London | ✓ | ✓ | `europe-west1`, `europe-west9`, `europe-west4`  
**`eu-west-3`** | Paris | `europe-west9` | Paris |  | ✓ | `europe-west1`, `europe-west2`, `europe-west3`  
**`eu-central-1`** | Frankfurt | `europe-west3` | Frankfurt | ✓ | ✓ | `europe-west4`, `europe-west1`, `europe-west6`  
**`eu-central-2`** | Zurich | `europe-west6` | Zurich |  |  | `europe-west8`, `europe-west12`, `europe-west3`  
**`eu-north-1`** | Stockholm | `europe-north2` | Stockholm | ✓ | ✓ | `europe-north1`, `europe-west4`, `europe-central2`  
**`eu-south-1`** | Milan | `europe-west8` | Milan |  |  | `europe-west12`, `europe-west6`, `europe-west3`  
**`eu-south-2`** | Spain (Aragon) | `europe-southwest1` | Madrid |  |  | `europe-west9`, `europe-west1`, `europe-west8`  
**`me-central-1`** | UAE | `me-central1` | Doha |  |  | `me-central2`, `me-west1`, `asia-south1`  
**`me-south-1`** | Bahrain | `me-central2` | Dammam |  |  | `me-central1`, `me-west1`, `asia-south1`  
**`af-south-1`** | Cape Town | `europe-southwest1` | Madrid |  |  | `me-central2`, `me-west1`, `europe-west1`  
**`ap-east-1`** | Hong Kong | `asia-east2` | Hong Kong |  | ✓ | `asia-east1`, `asia-southeast3`, `asia-southeast1`  
**`ap-northeast-1`** | Tokyo | `asia-northeast1` | Tokyo |  | ✓ | `asia-northeast2`, `asia-northeast3`, `asia-east1`  
**`ap-northeast-2`** | Seoul | `asia-northeast3` | Seoul |  | ✓ | `asia-northeast2`, `asia-northeast1`, `asia-east1`  
**`ap-northeast-3`** | Osaka | `asia-northeast2` | Osaka |  | ✓ | `asia-northeast1`, `asia-northeast3`, `asia-east1`  
**`ap-south-1`** | Mumbai | `asia-south1` | Mumbai |  | ✓ | `asia-south2`, `me-central1`, `asia-southeast1`  
**`ap-south-2`** | Hyderabad | `asia-south2` | Delhi |  |  | `asia-south1`, `asia-southeast1`, `me-central1`  
**`ap-southeast-1`** | Singapore | `asia-southeast1` | Singapore | ✓ | ✓ | `asia-southeast2`, `asia-southeast3`, `asia-east1`  
**`ap-southeast-2`** | Sydney | `australia-southeast1` | Sydney | ✓ | ✓ | `australia-southeast2`, `asia-southeast2`, `asia-southeast1`  
**`ap-southeast-3`** | Jakarta | `asia-southeast2` | Jakarta |  | ✓ | `asia-southeast1`, `asia-southeast3`, `australia-southeast1`  
  
## What's next

  * Set up a cross-cloud connection for [AWS Glue](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-aws-glue), [Databricks Unity Catalog](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-databricks), [Snowflake Horizon Catalog](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-snowflake), [Workday Data Lake](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-workday), or [SAP Business Data Cloud](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-sap-bdc).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-11 UTC."],[],[]] 

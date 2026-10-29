---
url: https://docs.cloud.google.com/docs/migration/scenarios/multi-cloud-migration/
title: Multi-cloud workload migration \u00a0|\u00a0 Migration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T05:39:29.581592+00:00
---

# Multi-cloud workload migration  |  Migration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/migration/scenarios/multi-cloud-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Guides ](https://docs.cloud.google.com/docs/migration/overview/migrate-modernize-overview)



Send feedback 

#  Multi-cloud workload migration Stay organized with collections  Save and categorize content based on your preferences. 

This page provides architectural guidance, cross-cloud service mappings, and migration strategies for migrating workloads from Amazon Web Services (AWS) or Microsoft Azure to Google Cloud.

If you are a cloud architect, platform engineer, or infrastructure lead, use the information on this page to map third-party cloud services to Google Cloud equivalents, execute direct cloud-to-cloud data transfers, and design multi-cloud disaster recovery (DR) architectures.

Before you read this page, you should have an inventory of your source AWS or Azure resources and an understanding of your organization's business continuity and failover requirements.

## AWS and Azure service mapping

When migrating from AWS or Azure, use the following table to map legacy cloud services to their Google Cloud equivalents:

Functional area | AWS service | Azure service | Google Cloud equivalent  
---|---|---|---  
**Virtual machines** | Amazon EC2 | Azure Virtual Machines |  [Compute Engine](https://docs.cloud.google.com/compute/docs)  
**Managed Kubernetes** | Amazon EKS | Azure Kubernetes Service (AKS) |  [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs)  
**Object storage** | Amazon S3 | Azure Blob Storage |  [Cloud Storage](https://docs.cloud.google.com/storage/docs)  
**Relational databases** | Amazon RDS | Azure SQL Database |  [Cloud SQL](https://docs.cloud.google.com/sql/docs) or [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs)  
**Cloud data warehouse** | Amazon Redshift | Azure Synapse Analytics |  [BigQuery](https://docs.cloud.google.com/bigquery/docs)  
  
## Data transfer from other clouds

Use Storage Transfer Service to transfer petabyte-scale object data from Amazon S3 or Azure Blob Storage directly to Cloud Storage.

### Key capabilities of Storage Transfer Service

Storage Transfer Service provides the following data transfer capabilities:

  * **Automated transfer jobs** : schedule recurring or one-time object copies cloud-to-cloud without routing data through local on-premises networks.
  * **Checksum verification** : ensure end-to-end data integrity during transfer by using automated hash verification.
  * **Bandwidth controls** : throttle transfer rates to prevent hitting API quota limits on source cloud providers.



For more information, see [Transfer from Amazon S3](https://docs.cloud.google.com/storage-transfer/docs/source-amazon-s3) and [Transfer from Microsoft Azure Blob Storage](https://docs.cloud.google.com/storage-transfer/docs/source-microsoft-azure).

## Multi-cloud resiliency and failover

Establishing Google Cloud as a secondary failover environment supports disaster recovery, mitigates single-cloud risk, and maintains business continuity during outages on other cloud platforms.

### Disaster recovery configurations

When designing multi-cloud disaster recovery architectures, choose from the following deployment configurations:

  * **Cold standby** : replicate data continuously to Cloud Storage for backup and restore, and maintain Compute Engine templates ready for on-demand deployment.
  * **Warm standby** : run minimal baseline compute capacity, such as a small GKE cluster or read-replica database, on Google Cloud ready to scale up rapidly during failover.
  * **Active-active dual processing** : distribute active user traffic across both the primary cloud provider and Google Cloud by using global Cloud Load Balancing.



For more information, see the [Disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide) and [Hybrid and multi-cloud architecture patterns](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices).

## What's next

  * [Migrate from AWS to Google Cloud](https://docs.cloud.google.com/architecture/migration-from-aws-get-started)
  * [Migrate from Azure to Google Cloud](https://docs.cloud.google.com/architecture/migration-from-azure-get-started)
  * [Storage Transfer Service documentation](https://docs.cloud.google.com/storage-transfer/docs/overview)
  * [Application modernization overview](https://docs.cloud.google.com/docs/migration/overview/app-modernization-overview.md)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

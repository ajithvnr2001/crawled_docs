---
url: https://docs.cloud.google.com/alloydb/docs/express-overview/
title: AlloyDB Express overview \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-08T05:50:06.160535+00:00
---

# AlloyDB Express overview  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/express-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  AlloyDB Express overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

AlloyDB Express is a configuration in AlloyDB for PostgreSQL that provides fast provisioning and scale-to-zero compute, optimized for rapid prototyping and for workflows that use AI coding agents. With AlloyDB Express, you can create and query a PostgreSQL database in seconds to build prototypes, applications, and agents.

When you're ready for production, you can upgrade to AlloyDB with one click to get the full set of enterprise features.

This document describes AlloyDB Express capabilities, compares it with AlloyDB, and describes its resource hierarchy, pricing, supported regions, and limitations.

## AlloyDB Express capabilities

AlloyDB Express provides the following capabilities to help you build and test applications.

### Fast provisioning

AlloyDB Express instances are ready to accept connections within approximately 2 seconds for public DNS and within 20 seconds for Private Service Connect endpoints. Fast provisioning lets you and your coding agents create and query a PostgreSQL database in seconds to speed up development.

### PostgreSQL compatibility and AI features for small instances

Even on a small 1 vCPU (4 GB RAM) or 2 vCPU (8 GB RAM) instance, you get full PostgreSQL compatibility and full access to AlloyDB AI. This capability includes ScaNN vector search, the `vector` (`pgvector`) extension, natural language queries, and built-in SQL functions to create embeddings and call Gemini models directly from SQL.

### Scale to zero

When an instance is idle, it scales down to zero compute so you aren't billed for compute during periods of inactivity. When the instance receives a new connection or query, it resumes operation in approximately 20 seconds.

### Connectivity

AlloyDB Express supports the following types of connectivity:

  * Private Service Connect: connects to your instance from your Virtual Private Cloud (VPC) network through Private Service Connect endpoints, without exposing the database to the public internet.
  * Public DNS: connects to your instance from clients outside of your VPC network. Public IP isn't supported; instead, AlloyDB Express provides external connectivity through public DNS.



You can also connect to AlloyDB Express instances using the AlloyDB Auth Proxy and AlloyDB Language Connectors for Go, Python, and Java.

### Automatic storage growth

Storage for AlloyDB Express instances scales automatically as your data grows, up to 20 GB, and you're billed only for the storage that you use. When storage reaches 20 GB, further write operations aren't allowed.

### In-place upgrade to AlloyDB

You can upgrade an AlloyDB Express configuration to an AlloyDB cluster by using a single command or a single click in the Google Cloud console. Upgrading gives you the enterprise features, compute configurations, storage configurations, and regions required for production. The upgrade has the following characteristics:

  * Data and configuration preservation: the upgrade preserves your database data, schemas, user credentials, and network configuration. The connection string and DNS name stay the same, so you don't need to change your application code.
  * Full set of AlloyDB capabilities: after the upgrade, the 20 GB storage limit and 2 vCPU compute limit no longer apply. You can configure regional high availability (HA), read pools, and automated backups. Regional HA clusters also include a 99.99% uptime service level agreement (SLA).



### Security and compliance

AlloyDB Express provides the following security capabilities to help protect your data:

  * Authentication: supports PostgreSQL username and password authentication, or Identity and Access Management (IAM) database authentication. Password complexity enforcement is on by default.
  * Data exfiltration controls: VPC Service Controls helps you comply with enterprise data exfiltration policies.
  * Governance controls: supports data residency, Access Transparency, and Access Approval.
  * Encryption: Google default encryption encrypts data at rest. Customer-managed encryption keys (CMEK) aren't supported.



### Patching and maintenance

AlloyDB Express is optimized for lightweight development, rapid prototyping, and workflows that use AI coding agents. To maintain low overhead and simplicity, AlloyDB Express handles patching and maintenance differently than AlloyDB deployments.

AlloyDB Express keeps instances up to date with the latest minor versions and security updates. The service typically applies maintenance updates automatically when an instance resumes, or during low-usage hours if the instance is running.

## Compare AlloyDB Express and AlloyDB

The following table compares AlloyDB Express with AlloyDB to help you choose the option that meets your requirements:

Capability | AlloyDB Express configuration (Preview) | AlloyDB  
---|---|---  
Use cases | Rapid prototyping and development with configurations optimized for workflows that use AI coding agents | Full set of enterprise features, compute configurations, storage configurations, and regions required for development, testing, and production of applications and agents  
Provisioning time | Within approximately 2 seconds for public DNS and within 20 seconds for Private Service Connect endpoints | Within a few minutes  
Compute configuration | 1 vCPU or 2 vCPU zonal instances | Up to 288 vCPUs; up to 20 read pool nodes  
Provisioned behavior | Scales down to zero when the database has no traffic | Always provisioned  
Storage configuration | Automatically scaling storage up to 20 GB | Automatically scaling storage up to 128 TB  
High availability | Not supported; zonal instances only | Regional HA with automatic failover  
Disaster recovery | Not supported | Cross-region replication with up to five secondary clusters  
SLA | No SLA | 99.99% uptime SLA for regional HA clusters  
Backups | Not supported | Automated and on-demand backups, point-in-time recovery (PITR), and Backup and DR Service  
Connectivity | Public DNS and Private Service Connect | Public IP, Private Service Connect, and private services access  
PostgreSQL versions | 18 | 14, 15, 16, 17, and 18  
Encryption | Google default encryption | Google default encryption or CMEK  
Pricing model | Usage-based compute and storage; monthly free tier | Provisioned hourly compute; usage-based storage; 30-day free trial for 8 vCPU clusters  
Committed use discounts (CUDs) | CUDs don't apply | 1-year and 3-year CUDs apply  
Interfaces | Google Cloud console, Google Cloud CLI, and REST API | Google Cloud console, gcloud CLI, REST API, Terraform, and Config Connector  
Upgrade path | In-place upgrade to AlloyDB | Downgrade to AlloyDB Express isn't supported  
  
## AlloyDB Express resource hierarchy

Like AlloyDB, AlloyDB Express organizes resources into clusters, instances, and nodes, but uses a simplified, single-instance topology. The following list describes how each resource in AlloyDB Express differs from AlloyDB:

  * Cluster: a top-level container for your databases, logs, and metadata in a Google Cloud region. Unlike an AlloyDB cluster, an AlloyDB Express cluster doesn't support cross-region replication or backups.
  * Instance: the access point that provides connection details for your applications. Unlike an AlloyDB cluster, which can contain a regional HA primary instance and multiple read pool instances, an AlloyDB Express cluster contains a single zonal primary instance that handles both reads and writes.
  * Node: the virtual machine (VM) that runs the database engine. An AlloyDB Express instance runs on a single node with either 1 vCPU (4 GB RAM) or 2 vCPUs (8 GB RAM) and has no standby node, which helps minimize costs.



## Pricing

AlloyDB Express offers usage-based pricing for compute and storage and includes a monthly free tier. The following list describes how AlloyDB Express bills for usage:

  * Free tier: each month includes 50 compute units and 2 GB of storage per billing account for the first 12 months. Usage beyond the free tier is billed on 1 vCPU or 2 vCPU instances, representing 1 compute unit and 2 compute units respectively.
  * Compute: compute is billed per second, based on compute units with a 1:4 vCPU-to-memory ratio. You aren't billed for compute while the instance is idle.
  * Storage: storage is billed for the amount that you use, not for provisioned capacity, up to the 20 GB maximum. Storage is billed while the instance is active or idle.
  * Discounts: standard enterprise discounts apply. CUDs aren't available.



For more information, see [AlloyDB pricing](https://docs.cloud.google.com/alloydb/pricing).

## Supported regions

AlloyDB Express supports the following regions:

  * `asia-east1`
  * `asia-east2`
  * `asia-northeast1`
  * `asia-southeast1`
  * `australia-southeast1`
  * `europe-west2`
  * `us-west1`



## Limitations

AlloyDB Express has the following limitations:

  * PostgreSQL version support: AlloyDB Express supports PostgreSQL 18 only.
  * Compute and instance configuration: AlloyDB Express supports a single zonal primary instance with 1 vCPU (4 GB RAM) or 2 vCPUs (8 GB RAM). Read pool instances, regional HA, and cross-region replication aren't supported.
  * Storage limit: AlloyDB Express supports up to 20 GB of storage. When storage reaches 20 GB, further write operations aren't allowed.
  * Maximum connections (`max_connections` flag): the `max_connections` database flag is fixed at `200` to help prevent out-of-memory (OOM) issues. Modifying the `max_connections` flag has no effect on an AlloyDB Express instance.
  * PostgreSQL extensions: you can load all [PostgreSQL extensions supported by AlloyDB](https://docs.cloud.google.com/alloydb/docs/reference/extensions), but memory-intensive extensions can cause OOM issues if they exceed the instance's 4 GB or 8 GB memory limit. To help prevent OOM issues, AlloyDB Express enforces the following fixed extension settings, which scale memory usage and turn off columnar engine advisor recommendations: 
    * `google_plan_management` extension: the `google_plan_management.managed_plans_pool_size_in_mb` flag is set to `10`.
    * `google_columnar_engine` and `google_db_advisor` extensions: the `google_columnar_engine.memory_size_in_mb` flag is set to `400`, the `google_columnar_engine.enable_auto_columnarization` flag is set to `false`, and the `google_db_advisor.enable_columnar_advisor` flag is set to `false`.
  * Backups and disaster recovery: automated backups, on-demand backups, PITR, and Backup and DR aren't supported.
  * Security: CMEK isn't supported.
  * Interfaces: Terraform and Config Connector aren't supported.
  * Billing and SLA: CUDs don't apply, and AlloyDB Express isn't covered by an SLA.
  * Upgrade path: after you upgrade an AlloyDB Express cluster to AlloyDB, you can't downgrade it back to AlloyDB Express.



## What's next

  * [Create an AlloyDB Express cluster](https://docs.cloud.google.com/alloydb/docs/create-manage-express-clusters#create-cluster)
  * [Connect to an AlloyDB Express instance](https://docs.cloud.google.com/alloydb/docs/create-manage-express-clusters#connect-instance)
  * [Upgrade an AlloyDB Express cluster to AlloyDB](https://docs.cloud.google.com/alloydb/docs/create-manage-express-clusters#upgrade-cluster)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 

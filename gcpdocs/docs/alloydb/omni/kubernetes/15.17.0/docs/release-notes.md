---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/release-notes/
title: AlloyDB Omni release notes \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 15.17.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T05:53:17.194624+00:00
---

# AlloyDB Omni release notes  |  AlloyDB Omni using the container orchestrator: 15.17.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/release-notes/

This page documents AlloyDB Omni version **15.17.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/overview)
  * [ Resources ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/resources)



Send feedback 

#  AlloyDB Omni release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains release notes for features and updates to AlloyDB Omni. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/alloydbomni-release-notes.xml) directly. 

## June 18, 2026

Feature

AlloyDB Omni documentation now includes documentation for the following AlloyDB AI features available in [GA](https://cloud.google.com/products#product-launch-stages):

  * [Auto vector embeddings](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/generate-manage-auto-embeddings-for-tables) automate the lifecycle of vector embeddings for large datasets, keeping them in sync with transactional data using real-time or batch updates. This feature includes a bulk mode that performs refreshes and migrations up to 130x faster than row-by-row processing."

  * [AI functions](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/evaluate-semantic-queries-ai-operators) integrate LLMs like Gemini to bring world knowledge to your AlloyDB data and incorporate advanced semantic search and ranking capabilities directly into your SQL workflows.

  * Use array-based AI functions to improve the efficiency of large-scale AI operations by enabling batch processing of natural language prompts in your SQL queries. For more information, see [Perform intelligent SQL queries using AI functions](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/evaluate-semantic-queries-ai-operators).




Feature

AlloyDB Omni documentation now includes documentation for the following AlloyDB AI features, which are available in [Preview](https://cloud.google.com/products#product-launch-stages):

  * The AlloyDB columnar engine provides a read-optimized, in-memory cache for HNSW indexes, increasing the number of queries per second (QPS) that your database can handle for vector search workloads. For more information, see [Accelerate vector search with the columnar engine](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/accelerate-with-ce).
  * Hybrid search supports Elasticsearch, which lets you use the `external_search_fdw` extension to connect to Elasticsearch and perform hybrid searches in AlloyDB. For more information, see [Access Elasticsearch data from AlloyDB](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/elastic-search).
  * The sentiment analysis and summarization functions let you process and analyze unstructured data in your database. For more information, see [Analyze text sentiment](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/analyze-sentiment) and [Summarize content](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/summarize-content).
  * You can defer ScaNN index creation on an empty table or a table with insufficient rows until the table has sufficient data. For more information, see [Create a ScaNN index](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-scann-index).
  * The alloydb_scann extension now supports four-level tree indexes, providing support for tables with up to 10 billion vector rows. For more information, see [Four-level ScaNN tree indexes](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-scann-index#create-scann-index-manual).



## June 03, 2026

Announcement

The [AlloyDB Omni Kubernetes operator](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes) version 1.7.1 is generally available ([GA](https://cloud.google.com/products#product-launch-stages)) and includes the following vulnerability fixes:

  * [CVE-2026-32288](https://nvd.nist.gov/vuln/detail/CVE-2026-32288) by upgrading to Golang Version [1.26.2](https://go.dev/doc/devel/release#go1.26.minor).
  * [CVE-2026-4878](https://nvd.nist.gov/vuln/detail/CVE-2026-4878) (`libcap`).
  * [CVE-2026-40356](https://nvd.nist.gov/vuln/detail/CVE-2026-40356) (`krb5-libs`) in the `g-pgbouncer` container image.



## May 08, 2026

Announcement

The AlloyDB Omni Kubernetes operator (version 1.7.0) is officially certified for Red Hat OpenShift. The operator and its associated database images are validated to run optimally and securely on Red Hat OpenShift.

This release includes the following:

  * OpenShift Certified Catalog: the AlloyDB Omni Operator is now officially listed on the [OpenShift Certified Catalog](https://catalog.redhat.com/en/software/container-stacks/detail/6837eb3b9137db6941d32436#overview).
  * Built-in management: discover, install, and manage the operator using OpenShift's built-in Operator Lifecycle Manager (OLM) user interface.
  * OLM support: support for OLM bundles is available, facilitating a seamless, one-click installation experience and automated management for enterprise deployments. For more information, see [Install the AlloyDB Omni operator](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes#olm_1).
  * This certification is supported by AlloyDB Omni versions starting with 16.11.0, 17.7.0, and 18.1.0.



## April 22, 2026

Change

The naming conventions for AlloyDB Omni deployment options are updated to more accurately reflect their respective installation and orchestration methods.  
The following table summarizes the primary name changes:

**Original name** |  **New name**  
---|---  
AlloyDB Omni for containers |  AlloyDB Omni using containers  
AlloyDB Omni for Kubernetes |  AlloyDB Omni using the container orchestrator  
AlloyDB Omni for Linux |  AlloyDB Omni using RPM  
Red Hat RPM orchestrator |  AlloyDB Omni using the RPM orchestrator  
  
This update clarifies the distinction between AlloyDB Omni deployment environments (such as Kubernetes or standalone Linux) and the packaging and orchestration technologies used to manage them. For more information, see [Choose your deployment environment](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment).

## April 09, 2026

Announcement

The [AlloyDB Omni Kubernetes operator](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/deploy-kubernetes) version 1.7.0 is generally available ([GA](https://docs.cloud.google.com/products#product-launch-stages)) and includes the following features and changes:

  * AlloyDB Omni supports PostgreSQL 18.1.0. For more information, see [AlloyDB Omni Kubernetes operator](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/overview). This operator version also supports AlloyDB Omni minor versions 15.15.0, 16.11.0, and 17.7.0.
  * Enterprise readiness for AlloyDB Omni on [Google Distributed Cloud Software Only](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs) lets the operator manage the full database lifecycle, including [provisioning](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/deploy-kubernetes), [high availability](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/high-availability/setup), and [disaster recovery](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/cross-data-center-replication/about-cross-data-center-replication), directly on your own physical bare metal infrastructure.
  * Database pods feature a hardened security posture with restricted Kubernetes `securityContext` settings enabled by default, including non-root execution and read-only root filesystems.
  * Added support for Transparent Data Encryption (TDE) ([Preview](https://cloud.google.com/products#product-launch-stages)), providing at-rest encryption for database clusters. This is available beginning with AlloyDB Omni 18.1.0. For more information, see [Transparent Data Encryption](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/transparent-data-encryption-omni).
  * Added support for custom configuration of database port numbers for your clusters. For more information, see [Configure custom ports](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/run-connect).
  * Introduced a framework for defining and collecting custom database metrics to enhance monitoring capabilities. For more information, see [Configure custom metrics](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/improve-observability-custom-monitoring-metrics).
  * Added detailed memory allocation metrics for improved memory and performance monitoring. For more information, see [AlloyDB Omni metrics](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/omni-metrics).
  * Improved Active Directory integration with support for `hostssl` connection types, multi-domain LDAP base DNs, and customizable LDAP search attributes. For more information, see [Integrate Active Directory](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/integrate-active-directory-kubernetes-operator).
  * Added support for rewind trigger functionality in symmetric disaster recovery configurations. For more information, see [Work with cross-data-center replication](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/cross-data-center-replication/work-with-cross-data-center-replication).
  * You can perform CPU and memory scaling operations with minimal downtime using Low Downtime Maintenance ([Preview](https://cloud.google.com/products#product-launch-stages)). For more information, see [Scale a database cluster](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/deploy-kubernetes#scale).
  * Additional [database flags](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/database-flags) are supported.
  * All current and earlier versions of Helm charts are available in the [Artifact Registry](https://pantheon.corp.google.com/artifacts/docker/alloydb-omni/us/gcr.io/alloydbomni-operator?rapt=AEjHL4NMzSdtsKxud4VKouvR3VJJHW7nf35vtrNV5vp_Ct9bJQYJFIb2a-TObQ1goelzrCPt-J2NFHHDIsEcsykeHublDMDJHkxtsSegSCNviRr4MyZExiQ). However, Helm charts are no longer available in Cloud Storage.
  * Updated manual major version upgrade instructions to use versioned data directory paths. For more information, see [Upgrade database major version](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/upgrade-kubernetes-database-major-version).
  * Updated [Choose compatible Kubernetes operator and database cluster versions](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/choose-compatible-versions) with latest versions.



Change

The AlloyDB Omni Kubernetes operator now automatically scales the `wal_keep_size` and `max_wal_size` database flags based on your configured storage size to optimize storage and [checkpointing](https://www.postgresql.org/docs/current/wal-configuration.html) behavior. If you [manually configure these flags](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/configure-database-flags), your custom values are respected and override the system-selected defaults.

Fixed

Reliability improvement for backups from standby instances: Fixed an issue in the AlloyDB Omni Kubernetes operator version 1.7.0 where backups taken from a standby instance could be incomplete if the primary instance were under heavy load. The backup process now performs a checkpoint before starting to ensure data integrity.

Upgrade required: If you use the backup from standby feature, upgrade to the latest versions of the AlloyDB Omni control plane and data plane. After you perform the upgrade, take a new backup to make sure that your data is fully protected.

Issue

Restore operations might fail if a database backup is running at the same time. If this occurs, retry the restore operation after some delay.

## September 18, 2024

Feature

The AlloyDB Omni operator is now available in [Preview](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages) on [Google Distributed Cloud (GDC) connected](https://cloud.google.com/distributed-cloud-connected). For more information, see [Install AlloyDB Omni on Kubernetes.](https://cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes)

## September 16, 2024

Breaking

The `postgres_ann` extension has been renamed to `alloydb_scann`. Before you upgrade to [AlloyDB Omni Kubernetes operator](https://cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes) version 1.1.1, you must drop any indexes created using the earlier `postgres_ann` version, then upgrade AlloyDB Omni, and then create the indexes again using the `alloydb_scann` extension.

Fixed

[AlloyDB Omni Kubernetes operator](https://cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes) version 1.1.1 is now available. This patch fixes the following issues:

  * Fixed a regression for the AlloyDB Vertex AI integration.
  * Fixed a bug in which upgrading from version 1.0.0 to version 1.1.0 failed when using injected sidecars.
  * Fixed a bug in which backups weren't reestablished correctly across failovers when using the Commvault sidecar with high availability (HA) configurations.
  * Fixed a bug that caused a status to be incorrectly set by the load balancer, resulting in erroneous reports that the database cluster wasn't ready.



Feature

Added a [tutorial](https://cloud.google.com/alloydb/docs/quickstart/integrate-kubernetes) that shows you how to set up a connection from an application running in a Google Kubernetes Engine autopilot cluster to an AlloyDB instance.

Issue

Upgrading to version 1.1.1 of the [AlloyDB Omni Kubernetes operator](https://cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes) might result in a brief interruption to all database clusters. No data loss is expected.

## August 22, 2024

Feature

AlloyDB Omni now offers in-depth documentation that describes how to install and use AlloyDB Omni in virtual machine (VM) environments. The information in these documents is in addition to the AlloyDB Omni documentation that describes how to install and use AlloyDB Omni in VM and Kubernetes environments. For more information, see [Get started with AlloyDB Omni on VMs](https://cloud.google.com/alloydb/omni/kubernetes/current/docs/get-started).

Change

The extension `temporal_tables` version 1.2.2 has been added to [extensions supported by AlloyDB](https://cloud.google.com/alloydb/docs/reference/extensions). 

The following extensions are updated:

  * Updated `pg_partman` to version 4.7.4.
  * Updated `pgtt` to version 3.0.0.



## August 16, 2024

Feature

[The AlloyDB Omni Kubernetes Operator version 1.1.0](https://cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes) lets you [configure a load balancer using annotations](https://cloud.google.com/alloydb/omni/kubernetes/current/docs/configure-load-balancer-k8s).

## August 05, 2024

Feature

[AlloyDB Omni](https://cloud.google.com/alloydb/docs/omni) version 15.5.5 is now generally available ([GA](https://cloud.google.com/products?e=48754805&amp;hl=en#product-launch-stages)). This version includes the following features and changes:

  * The [AlloyDB Omni Kubernetes Operator](https://cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes) version 1.1.0 is generally available ([GA](https://cloud.google.com/products?e=48754805&amp;hl=en#product-launch-stages)) and it includes the following new features:

    * [Cross-data center replication](https://cloud.google.com/alloydb/omni/kubernetes/current/docs/cross-data-center-replication/about-cross-data-center-replication) to support automated setup of disaster recovery.
    * [Support for the Red Hat OpenShift container platform](https://cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes#rhel-openshift) version 4.14 and later in [Preview](https://cloud.google.com/products?e=48754805&amp;hl=en#product-launch-stages).
    * [Variable number of nodes](https://cloud.google.com/alloydb/omni/kubernetes/current/docs/kubernetes-read-pool) per read pool instance.
    * [Customizable count](https://cloud.google.com/alloydb/omni/kubernetes/current/docs/kubernetes-ha#adjust-failover-trigger-settings) for the number of failed checks before auto-failover kicks in for a High Availability (HA) configuration.
    * [Version 1.1.0 of the Operator](https://cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes#compatibility) is supported on AlloyDB Omni version 15.5.5 and later.
    * A dedicated backup server for streamlined backup operations.
    * When you create a database cluster, the admin password secret is [no longer deleted](https://cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes#create) after you specify it.
  * The `postgres_ann` extension is renamed to `alloydb_scann`. Before you upgrade AlloyDB Omni, you must drop any indexes created using the older `postgres_ann` version, then upgrade AlloyDB Omni, and then create the indexes again using the `alloydb_scann` extension.

  * Various bug fixes.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

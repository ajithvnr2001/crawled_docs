---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/
title: Transparent data encryption for AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 18.4.0 \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:39:09.530147+00:00
---

# Transparent data encryption for AlloyDB Omni  |  AlloyDB Omni using the container orchestrator: 18.4.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/

[ Skip to main content ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/)
  * [Deutsch](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/?hl=es-419)
  * [Français](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/?hl=id)
  * [Italiano](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/?hl=ja)
  * [한국어](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Falloydb%2Fomni%2Fkubernetes%2F18.4.0%2Fdocs%2Ftransparent-data-encryption-omni%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/alloydb-color.svg) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/overview)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/overview)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Key hierarchy](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/#key_hierarchy)
  * [How TDE works with AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/#how-tde-works)
  * [Encryption scope and specifications](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/#encryption_scope_and_specifications)
  * [Backup and high availability](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/#backup_and_high_availability)
  * [Supported KMS and authentication](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/#supported-kms)
  * [PostgreSQL tool compatibility](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/#postgresql_tool_compatibility)
  * [Limitations](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/#limitations)
  * [What's next](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/#whats_next)


This page documents AlloyDB Omni version **18.4.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/overview)


Was this helpful?
Send feedback 
#  Transparent data encryption for AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Key hierarchy](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/#key_hierarchy)
  * [How TDE works with AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/#how-tde-works)
  * [Encryption scope and specifications](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/#encryption_scope_and_specifications)
  * [Backup and high availability](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/#backup_and_high_availability)
  * [Supported KMS and authentication](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/#supported-kms)
  * [PostgreSQL tool compatibility](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/#postgresql_tool_compatibility)
  * [Limitations](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/#limitations)
  * [What's next](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni/#whats_next)


Select a documentation version:  18.4.0keyboard_arrow_down
  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/transparent-data-encryption-omni)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/transparent-data-encryption-omni)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/transparent-data-encryption-omni)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/transparent-data-encryption-omni)

To protect sensitive information and meet strict compliance requirements without modifying your application code, use transparent data encryption (TDE) to secure data at rest in AlloyDB Omni. This overview explains how TDE automatically encrypts database files, logs, and caches before they are written to disk, ensuring security in depth with minimal operational overhead. 
## Key hierarchy
AlloyDB Omni implements a two-tier key hierarchy that maintains a strict separation of duties between the database and the user-managed security infrastructure.
  * Data Encryption Keys (DEKs): keys that are generated and owned by AlloyDB Omni. These keys encrypt the actual data files, WAL, and temporary files. AlloyDB Omni stores DEKs on disk but wraps them with your KEK. 
  * Key Encryption Key (KEK): the main key that you manage in an external Key Management Service (KMS). AlloyDB Omni uses your KEK to encrypt the DEKs. AlloyDB Omni accesses this key only at startup to unwrap the DEKs. Your KEK is never stored persistently on the database disk. 
    * The KEK's location and access parameters are defined within the `TdeConfig` custom resource. 


## How TDE works with AlloyDB Omni
When TDE is enabled, AlloyDB Omni secures your data using a layered encryption model that integrates with an external KMS.
  * Initialization and key retrieval: during the cluster's startup or initialization phase, the AlloyDB Omni engine establishes a secure connection to your KMS. It authenticates using a JSON Web Token (JWT) for HashiCorp Vault or username and password credentials for Thales CipherTrust Manager, and retrieves the KEK.
  * Unwrapping the DEKs: AlloyDB Omni uses your KEK to unwrap the DEKs, which are stored on the local storage in a wrapped state. Then, these DEKs are loaded into memory.
  * Transparent data operations: 
    * Writing to disk: as the database writes data blocks, WAL records, or temporary files to the physical disk, it automatically encrypts the data using AES-256 algorithms before writing it.
    * Reading from disk: when the database needs to read data into memory, it automatically decrypts the blocks using the DEKs that are held in memory.
    * Cache encryption: TDE also supports the disk cache, including columnar engine information stored in the cache. Data written to the chill cache storage layer is encrypted, and data spilled to the columnar engine's SSD cache is encrypted before being written to SSD and decrypted upon read.
  * Performance optimizations: TDE includes optimizations to maintain high performance while securing data. It uses optimized `AES-256-XTS` protection for data blocks and caches, and features synchronous write optimizations to minimize latency on fast paths.
  * Security boundaries: your KEK is never stored on the local database disk, ensuring that even if physical storage media is compromised, the data remains unreadable without authorized access to the external KMS.


## Encryption scope and specifications
AlloyDB Omni uses industry-standard AES-256 algorithms to secure your data.
  * **Data files (tables and indexes):** AES-256-XTS.
  * **Write-ahead logs (WAL):** AES-256-CTR.
  * **Temporary files:** AES-256-XTS or AES-256-CTR depending on the type of temporary data.
  * **Columnar engine cache files:** AES-256-XTS.
  * **Chill cache files:** AES-256-XTS.
  * **Key wrapping:** AES-256-KWP.


## Backup and high availability
When TDE is enabled, backups created using `pgBackRest` inherit the encryption configuration of the source cluster. This ensures that your backup data remains protected with the same level of security as your primary database.
You can only restore backups if the `TdeConfig` resource used at the time the backup was taken is available in the same namespace as the target cluster. 
For HA setups, the `TdeConfig` must be present in the same namespace as the `DBCluster` resource.
## Supported KMS and authentication
AlloyDB Omni supports the following external KMS providers and authentication methods:
  * **[HashiCorp Vault](https://developer.hashicorp.com/vault/docs/secrets/kv/kv-v2):** Supports the KV-V2 secrets engine with JSON Web Token (`jwt`) authentication.
  * **[Thales CipherTrust Manager](https://cpl.thalesgroup.com/encryption/ciphertrust-manager):** Supports secrets management with username and password (`password`) authentication.


## PostgreSQL tool compatibility
TDE-enabled clusters support all built-in PostgreSQL tools through the `TdeConfig` resource.
## Limitations
  * You can't enable TDE on existing clusters.
  * After TDE is enabled, you can't disable it.
  * Major version upgrades aren't supported for TDE-enabled clusters.
  * You can't restore encrypted backups to unencrypted servers or unencrypted backups to encrypted servers.
  * DEK rotation isn't supported.
  * KEK rotation is supported as long as the KEK URL path remains the same.
  * You can't `CREATE DATABASE` using the `FILE_COPY` strategy.
  * On TDE-enabled clusters, Barman backups only support `rsync` mode. The `postgres` backup method isn't supported.


## What's next
  * Learn how to [Create a TDE-enabled cluster](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/create-tde-cluster).
  * [Troubleshoot transparent data encryption](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/troubleshoot-omni-tde).


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

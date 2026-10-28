---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/
title: Cassandra backup overview \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:44:52.179564+00:00
---

# Cassandra backup overview  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/

[ Skip to main content ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/)
  * [Deutsch](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/?hl=de)
  * [Español](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/?hl=es-419)
  * [Français](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/?hl=id)
  * [Italiano](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/?hl=it)
  * [Português](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/?hl=ja)
  * [한국어](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/apigee-color.svg) ](https://docs.cloud.google.com/apigee/docs)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Why take backups of Cassandra?](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/#why-take-backups-of-cassandra)
  * [What you need to know about Cassandra backups?](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/#what-you-need-to-know-about-cassandra-backups)
  * [What is backed up?](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/#what-is-backed-up)
  * [Where is backup data stored?](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/#where-is-backup-data-stored)
  * [How the data is secured?](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/#how-the-data-is-secured)
  * [How to take backups?](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/#how-to-take-backups)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)


Send feedback 
#  Cassandra backup overview Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Why take backups of Cassandra?](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/#why-take-backups-of-cassandra)
  * [What you need to know about Cassandra backups?](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/#what-you-need-to-know-about-cassandra-backups)
  * [What is backed up?](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/#what-is-backed-up)
  * [Where is backup data stored?](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/#where-is-backup-data-stored)
  * [How the data is secured?](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/#how-the-data-is-secured)
  * [How to take backups?](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview/#how-to-take-backups)


Version 1.16 keyboard_arrow_down
Supported versions:
  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-backup-overview.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/cassandra-backup-overview.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/cassandra-backup-overview.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)
Unsupported versions:
  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/cassandra-backup-overview.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/cassandra-backup-overview.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/cassandra-backup-overview.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cassandra-backup-overview.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-backup-overview.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/cassandra-backup-overview.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/cassandra-backup-overview.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/cassandra-backup-overview.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/cassandra-backup-overview.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/cassandra-backup-overview.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/cassandra-backup-overview.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/cassandra-backup-overview.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/cassandra-backup-overview.html)


Apigee hybrid backup and restore feature lets you create backups of the hybrid data and, in case of disaster scenarios, restore the data to previous working snapshots. Backup availability and retention is based on the backup infrastructure provided by you. 
A typical installation of Apigee hybrid consists of the following components:
  * MART (admin service)
  * Controller and Watcher (manage Kubernetes objects)
  * Istio (manages Ingress)
  * Runtime, Sync, and UDCA (one per environment)
  * Telemetry (monitoring and logging)
  * Cert manager (manages certificates)
  * Datastores (Cassandra and Redis databases)


All the components except for Cassandra are stateless and do not persist any data. Backup and restoration is not necessary for those components. During recovery, reinstallation of those components using the existing overrides is sufficient.
## Why take backups of Cassandra?
Backups are an important measure of protection against disaster scenarios. Each backup acts as a consistent snapshot of the Cassandra data existing at the time the backup is created. In addition to Cassandra data, this snapshot includes schema and metadata within the Cassandra cluster. In the event of a disaster, backups enable you to restore your hybrid instance to a previously operational state. Depending on the size of the hybrid instance, a single backup set may contain one or more backup files.
## What you need to know about Cassandra backups?
Cassandra is a replicated database that is configured to have at least three copies of your data in each region or data center. Cassandra uses streaming replication and read repairs to maintain the data replicas in each region or data center at any given point.
In hybrid, Cassandra backups are **not** enabled by default. It's a good practice to enable Cassandra backups in the event your data is lost to a catastrophic failure. Cassandra backups are intended for use in cases of disaster recovery and not for restoring data loss caused by accidental deletion.
Backups are created according to the schedule set in your `overrides.yaml` file. Once a backup schedule is applied to your hybrid cluster, a Kubernetes backup job is executed according to the schedule. The job triggers a backup script on each Cassandra node in your hybrid cluster that collects all the data on the node, creates an archive file of the data, and sends the archive to Cloud Storage or a directory on a remote server. 
## What is backed up?
The hybrid scheduled backup is a complete backup of the persisted runtime data stored in Apigee's Cassandra at the time of backup. Any data modifications after the backup time will not be available in the backup. The scheduled backup consist of the following entities: 
  * Cassandra schema, including the user schema (Apigee keyspace definitions).
  * Cassandra partition token information per Cassandra node in a cluster.
  * A snapshot of the Cassandra data.


## Where is backup data stored?
The location of the backup data depends on your backup method. Apigee hybrid supports the following methods for taking backups:
  * **Backup in Cloud Storage** : Backup is stored in the configured Cloud Storage buckets in your Google Cloud Project.
  * **Backup in a remote server** : Backup is stored in a directory on a remote server specified by you.


## How the data is secured?
If you are using Cloud Storage for backup, the backup data is encrypted by default. In case of backups not on Cloud Storage, backup data is encrypted during the transfer to the remote server. But after the transfer, you must ensure that the backup data is encrypted in the remote server. 
## How to take backups?
Use one of these two methods to configure backups. For both methods, you'll configure backup in your `overrides.yaml` file. Apigee recommends you make a copy of the `overrides.yaml` file, so that you can reuse it during the recovery process. 
  * Use [Apigee hybrid CSI backup and restore](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-csi-backup-restore), which uses Kubernetes CSI (Container Storage Interface) snapshots. This method is recommended for hybrid instances hosted in Google Cloud, AWS, or Azure. 
  * Use non-CSI hybrid backup and restore, which copies schema and other data to backup files. This is the recommended method for on-prem installations. 
The following sections describe in detail how to schedule backups in Cloud Storage and in a remote server.
    * [Scheduling backups in Cloud Storage](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/schedule-cassandra-backup-gcs)
    * [Scheduling backups in a remote server](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/schedule-cassandra-backup-non-gcs)


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

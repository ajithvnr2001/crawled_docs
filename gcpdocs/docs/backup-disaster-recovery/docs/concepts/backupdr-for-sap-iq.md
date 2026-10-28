---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-iq/
title: Backup and DR for SAP IQ on a backup/recovery appliance \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:50:00.202224+00:00
---

# Backup and DR for SAP IQ on a backup/recovery appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-iq/

[ Skip to main content ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-iq/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-iq/)
  * [Deutsch](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-iq/?hl=de)
  * [Español](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-iq/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-iq/?hl=es-419)
  * [Français](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-iq/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-iq/?hl=id)
  * [Italiano](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-iq/?hl=it)
  * [Português](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-iq/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-iq/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-iq/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-iq/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-iq/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-iq/?hl=ja)
  * [한국어](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-iq/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/operations-color.svg) ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [How it works: Backup and DR volume-based backup with Linux CBT](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-iq/#volume-based)
  * [How it works: file-based backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-iq/#how_it_works_file-based_backup)
  * [What's next](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-iq/#whats_next)
  * [Other documentation for Backup and DR for SAP IQ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-iq/#other-doc)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)


Send feedback 
#  Backup and DR for SAP IQ on a backup/recovery appliance Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [How it works: Backup and DR volume-based backup with Linux CBT](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-iq/#volume-based)
  * [How it works: file-based backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-iq/#how_it_works_file-based_backup)
  * [What's next](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-iq/#whats_next)
  * [Other documentation for Backup and DR for SAP IQ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-iq/#other-doc)


**Caution:** Beginning July 31, 2027, support for backing up SAP IQ databases using the appliance management console is deprecated. To learn more about this deprecation and alternative backup solutions, see [Migrate from legacy database backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations/migrating-legacy-databases).
SAP IQ, formerly Sybase IQ, is a family of relational database management systems within SAP Information Management division that is centered on several relational database management system offerings. This documentation explains how to protect SAP IQ application consistent database data with Backup and DR in a Linux environment.
Backup and DR uses these SAP IQ backup APIs:
  * **File-based backups** : SAP IQ dump database file-based backups API: This provides the full and incremental backups of the database in backup format. On recovery, the restore db API recovers the database by physically overwriting the data area.
  * **Log backup** : SAP IQ PITR log backup: During a PITR log backup, the SAP IQ API `Backup database point in time recovery logs only to $TARGET_MOUNTPOINT` command is used for log backup. OS-level commands are used for logs purging.


## How it works: Backup and DR volume-based backup with Linux CBT
Data backup and recovery follows these steps:
  1. The Backup and DR agent has CBT to track changed blocks in the database data area.
  2. The agent calls the database API to freeze or pause database for data backup.
  3. Agent creates LVM snapshot of database data area and synthesizes a bitmap.
  4. Agent call to database API to unfreeze database.
  5. Agent copies changed blocks to backup/recovery appliance appliance, which then deletes the snapshot and catalogs the backup.
  6. The appliance issues an internal snapshot and synthesizes a point-in-time virtual full backup. 
  7. For data recovery, Backup and DR instantly mounts a rewritable staging disk and brings the database online.


## How it works: file-based backup
Data backup and recovery with file-based backup images follows these steps:
  1. Backup and DR agent is deployed in the database server.
  2. Mount staging disk on the database server.
  3. Invoke Full+Incremental backup using the dump backup command, writing the backup image to the mounted disk.
  4. Backup and DR takes an internal snapshot. Log backups are done in a similar fashion directly from the file-system at any schedule that you configure.
  5. For data recovery, Backup and DR instantly mounts the staging disk to the database server and initiates the database restore operation. Logs can be played to any point in time after the database is restored.
  6. For recovery, Backup and DR instantly mounts the staging disk to the database server and initiates the database restore operation. Logs can be played to any point in time after the database is restored.


## What's next
[Prepare the database for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/otherdb-prep-database)
## Other documentation for Backup and DR for SAP IQ
This page is one in a series of pages specific to protecting and recovering SAP IQ databases with Backup and DR. You can find additional information at the following:
  * [Backup and DR for SAP IQ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/sap-iq-intro)
  * [Prepare the database for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/otherdb-prep-database)
  * [Add a SAP IQ database host and discover databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/otherdb-add-host)
  * [Define policy templates and resource profiles](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template)
  * [Set application details and settings](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-otherdb)
  * [Check staging disk format and backup method](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/backup-method-staging-disk-otherdb)
  * [Protect the SAP IQ database and its logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/otherdb-protect)
  * [Mount an SAP IQ database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/otherdb-mounts)
  * [Mount and migrate an SAP IQ database to a new location](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/otherdb-mount-and-migrate)
  * [Recover SAP IQ Backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/otherdb-restore)
  * [Create an SAP IQ Backup and DR Workflow](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/otherdb-workflow)


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

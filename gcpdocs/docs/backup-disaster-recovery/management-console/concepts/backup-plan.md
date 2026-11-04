---
url: https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/backup-plan/
title: Backup plans overview \u00a0|\u00a0 Backup and DR for the management console \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T07:54:35.240736+00:00
---

# Backup plans overview  |  Backup and DR for the management console  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/backup-plan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Backup and DR for the management console ](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/backupdr-for-workloads)



Send feedback 

#  Backup plans overview Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations) in the Backup and DR documentation. 

Backup plans are centralized management tools that allow you to define advanced backup strategies for your Google Cloud resources. By using a backup plan, you can automate when and how your data is protected, ensuring consistent recovery points across your infrastructure.

Backup plans are also referred to as backup policies. A key feature of the service is the capability for backup plan association to a workload to ensure consistent data protection.

### Supported resource types

Backup plans support the following vaulted resources:

  * Compute Engine instances
  * Compute Engine disks
  * Cloud SQL instances
  * AlloyDB for PostgreSQL clusters
  * Filestore instances



## Core components of a backup plan

This section details the important components of Backup and DR backup plans.

### Backup rules

A backup plan consists of one or more backup rules that define the lifecycle of the backup. Multiple backup rules can be associated with a single backup plan. Attributes of backups plans are as follows:

  * **Recurrence** : Defines how often backups are taken 
    * **Hourly** : Specify the frequency in hours
    * **Daily** : Backups occur once every day
    * **Weekly** : Select one or more specific days of the week
    * **Monthly** : Select a specific day of the month (e.g., the 1st or 15th)
    * **Yearly** : Backups occur once a year on a specified date
  * **Constraint** : No two backup rules within a plan can be created with the same backup frequency period
  * **Backup Window** : Defines the timeframe (in 24-hour format) during which the backup job must start 
    * **Duration** : The window must be at least six hours long
    * **Start Time** : The earliest time the backup can begin
  * **Retention** : The number of days each backup created by this rule will be kept before it is eligible for deletion. Users have the ability to specify enforced retention at the backup-rule level



### Maximum custom on-demand retention

This setting defines the maximum number of days an on-demand backup (created manually outside the automated schedule) can be retained. This prevents users from accidentally setting excessively long retention periods for manual snapshots.

### Database log backups

For database resources (like Cloud SQL or AlloyDB), you can enable log backups within the backup plan. This allows for Point-in-Time Recovery (PITR) by capturing transaction logs between full backup points.

## Backup job retries

When a scheduled job fails, the scheduler automatically retries the job up to three more times. 

  * **First failure** : Status marked "Retried"; waits 4 minutes.
  * **Second failure** : Next retry queued after 16 minutes.
  * **Third failure** : Final retry queued after 64 minutes.
  * **Final failure** : After 4 total attempts, status changes to "Failed". No further jobs are attempted for that schedule period.



Job retries are reported in **Monitor** > **Jobs**. To identify retries, all four jobs will share the same Job number with a unique suffix (e.g., `Job_12345`, `Job_12345a`, `Job_12345b`).

## Data retention and storage management

The section details the important data retention and storage management features of Backup and DR backup plans.

### Types of retention

  * **Expiration-based Retention** : The standard lifecycle where a backup is kept for the duration defined in the plan's rule and then automatically expired.
  * **Enforced Retention** : A security feature at the backup vault level. If a vault has "Prevent deletion for" enabled, backups cannot be deleted—even by an administrator—until this period has passed. This period can be longer than the rule's retention period.



### Storage constraints

  * **Vault Minimums** : A backup plan's retention period cannot be shorter than the minimum retention period configured on the destination backup vault. The maximum custom on-demand retention period must be greater than or equal to the destination backup vault's minimum enforced retention period.
  * **Immutability** : Backups are immutable (cannot be modified or deleted) for the duration of the vault's enforced retention period.
  * **Automatic Deletion** : Once the retention period set in the backup plan expires (and any vault-level enforced retention is met), the service automatically deletes the backup to manage storage costs.
  * The maximum custom on-demand retention period must be greater than or equal to the destination backup vault's minimum enforced retention period.



## Security and encryption: CMEK

  * **Alignment Requirement** : If a source workload is protected by Customer-Managed Encryption Keys (CMEK), the backup plan must point to a CMEK-enabled backup vault.
  * **Standard Encryption** : Resources using Google-owned and Google-managed encryption keys must be backed up to standard (non-CMEK) vaults.



## Supported regions and zone separation

Backup plans are available in most major Google Cloud regions. However, certain regions don't support zone separation, meaning backups may not be stored in a different zone from the source:

  * **Asia Pacific** : Osaka (asia-northeast2)
  * **Europe** : Warsaw (europe-central2)
  * **Middle East & Africa**: Doha (me-central1), Johannesburg (africa-south1)
  * **North America** : Montréal (northamerica-northeast1), Querétaro (northamerica-south1)
  * **South America** : Santiago (southamerica-west1)



## What's next

  * Learn how to [create a backup plan](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/backup-plan/).
  * Learn more about [backup vaults](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/backup-plan/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/management-console/
title: About Backup and DR for the management console \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T05:44:14.248076+00:00
---

# About Backup and DR for the management console  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/management-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  About Backup and DR for the management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Backup and DR for the management console is an appliance-based backup and disaster recovery solution that lets you capture, store, replicate, and recover virtual machines (VMs), file systems, and self-managed databases in Google Cloud and hybrid environments. You manage data protection across these workloads through a dedicated, web-based appliance management console and customer-deployed backup/recovery appliances.

While you can protect many resources directly through the Google Cloud console, [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), backupdr API, and Terraform into Google-managed backup vaults, the appliance-based solution uses the dedicated appliance management console.

For more information, see [Backup and DR for the management console overview](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/backupdr-for-workloads).

## When to use the management console

Use the appliance management console when your use case involves any of the following tasks:

  * Deploying or managing backup/recovery appliances and storage pools.

  * Protecting and recovering self-managed databases, Google Cloud VMware Engine and VMware vSphere VMs, or Linux and Windows file systems.

  * Managing existing backups of Compute Engine instances configured in the management console.

  * Configuring appliance-based backup templates, policies, and resource profiles.

  * Using copy data management capabilities such as mounts, LiveClones, or automated workflows.




## What Backup and DR for the management console provides

You can use Backup and DR in the management console to do the following:

  * Deploy and manage backup/recovery appliances in your Virtual Private Cloud (VPC) network and configure cloud infrastructure.

  * Install the Backup and DR agent on Linux and Windows hosts to discover and protect databases and file systems.

  * Define incremental-forever backup schedules, retention policies, and storage targets.

  * Recover workloads to production or instantly mount backup images.

  * Track backup jobs, events, compliance, and storage utilization.




## Pricing

For pricing information, see [Backup and DR pricing](https://docs.cloud.google.com/backup-disaster-recovery/pricing).

## What's next

  * Learn how to [migrate a Compute Engine instance backup configuration from the appliance management console to a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/migrate-compute-instance-backup-to-vault).

  * Read [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations) for deprecation timelines and migration alternatives.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-02 UTC."],[],[]] 

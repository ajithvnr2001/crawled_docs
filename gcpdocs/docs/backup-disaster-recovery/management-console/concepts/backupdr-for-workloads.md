---
url: https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/backupdr-for-workloads/
title: Backup and DR for the management console overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T05:45:37.356680+00:00
---

# Backup and DR for the management console overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/backupdr-for-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Backup and DR for the management console ](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/backupdr-for-workloads)



Send feedback 

#  Backup and DR for the management console overview Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations) in the Backup and DR documentation. 

Backup and DR for the management console is an appliance-based backup and disaster recovery solution that lets you centrally capture, store, replicate, and recover virtual machines (VMs), file systems, and self-managed databases in Google Cloud and hybrid environments. Through a dedicated, web-based appliance management console and customer-deployed backup/recovery appliances, you can manage data protection across your workloads.

Backup and DR for the management console captures data in an incremental-forever format and stores it in its built-in, application-readable format. Because backups are stored natively rather than as proprietary backup archives, you can instantly mount backup images directly from a backup/recovery appliance to recover workloads, provision virtual copies for testing and development, or migrate data with minimal downtime.

## Deprecation of Backup and DR for the management console

Google Cloud Backup and DR will end support for the legacy appliance management console (IaaS stack) and its associated user-managed workloads on **September 30, 2027**. Plan your migration to alternative backup methods as soon as possible to maintain continuous data protection.

### Workloads affected by the management console deprecation

The management console deprecation affects only self-managed workloads protected through the legacy appliance management console, including:

  * Compute Engine instances managed through the appliance management console
  * IBM Db2 databases
  * Oracle databases
  * SAP HANA databases
  * Microsoft SQL Server databases
  * Google Cloud VMware Engine VMs
  * Generic applications and consistency groups
  * User-managed file systems (Linux and Windows file systems, system state, NFS, and SMB/CIFS)



First-party Google-managed services protected directly through the Google Cloud console—including Compute Engine VMs, Persistent Disks, Cloud SQL, AlloyDB for PostgreSQL, and Filestore—are unaffected by this deprecation.

### Deprecation timeline and milestones

The deprecation of Backup and DR for the management console follows three key enforcement milestones:

  * **December 31, 2026 (Inactive management server deletion):** Any management server in your project is automatically deleted after 30 consecutive days of inactivity. A management server is considered inactive only if it has no active backups, no protected applications or workloads, and no active backup jobs.
  * **September 30, 2027 (Backup freeze):** Support for creating new backups using the legacy appliance management console stack ends. Failing to migrate before this cutoff date prevents you from taking new backups of affected workloads.
  * **March 31, 2028 (Restore cutoff):** Direct restore capabilities through the legacy appliance management console interface end. To restore backups after this cutoff date, you must use the standalone [Long-Term Retention (LTR) recovery utility and scripts](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-long-term-retained-backups).



### Migration alternatives for management console workloads

To maintain backup protection before the September 30, 2027 backup freeze, migrate your affected workloads to one of the following supported backup solutions:

Workload | Migration option | Reference  
---|---|---  
Compute Engine | Google-native Compute Engine backups | Migrate Compute Engine instances to an appliance-free architecture using [Google Cloud Backup and DR for Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-backup).  
User-managed databases (IBM Db2, Oracle, SAP HANA, Microsoft SQL Server, and others) | Application-consistent vaulted backups using custom scripts | Use Compute Engine VM and Persistent Disk backups on Google Cloud Backup and DR with the [guest-flush framework](https://docs.cloud.google.com/compute/docs/disks/creating-linux-application-consistent-pd-snapshots), paired with [custom scripts for application-consistent and immutable backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/application-consistent-backups-for-self-managed-databases).  
SAP HANA | Agent-based Google Cloud backups | Use the native Google Cloud Backint agent or Persistent Disk snapshots. See the [Agent for SAP Backint backup and recovery guide](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery) or the [Disk snapshot backup and recovery guide](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/disk-snapshot-backup-recovery).  
General VM workloads | Native Google Cloud disk snapshots | Configure standard or archive disk snapshots to periodically back up virtual disks using the [disk snapshots guide](https://docs.cloud.google.com/compute/docs/disks/create-snapshots).  
All workloads | Third-party Marketplace solutions | Deploy approved alternative enterprise backup solutions available on [Google Cloud Marketplace](https://console.cloud.google.com/marketplace).  
  
### Retain and recover backups after March 31, 2028

To retain backup recovery capabilities beyond the March 31, 2028 restore cutoff, migrate your legacy backup data to OnVault storage in Cloud Storage before your appliances are shut down:

  1. **Assign OnVault policies:** Migrate all critical legacy backups to Cloud Storage OnVault buckets.
  2. **Sync metadata:** Ensure that all Persistent Disk snapshot metadata is fully synced to your Cloud Storage bucket before your local appliances are shut down. Contact [gcbdr-umdb-transition@google.com](mailto:gcbdr-umdb-transition@google.com) or [Cloud Customer Care](https://cloud.google.com/support) to verify and complete this metadata transfer.
  3. **Use the recovery utility:** Use the standalone tool and scripts to discover and mount OnVault and Persistent Disk backup images directly from your Cloud Storage buckets. For instructions, see [Restore long-term retained backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-long-term-retained-backups).



If you have questions or need assistance planning your migration, contact the transition team at [gcbdr-umdb-transition@google.com](mailto:gcbdr-umdb-transition@google.com), [Cloud Customer Care](https://cloud.google.com/support), or your Google Cloud account team.

## How Backup and DR for the management console differs from Google Cloud Backup and DR

Google offers two distinct management and architecture models for Backup and DR:

  * **Backup and DR for the management console** (this documentation set): An appliance-based architecture where you deploy and manage backup/recovery appliances in your Virtual Private Cloud (VPC) network and orchestrate protection through the dedicated web-based appliance management console. This offering is designed for self-managed databases (such as Oracle, Microsoft SQL Server, SAP HANA, and IBM Db2), Google Cloud VMware Engine and VMware vSphere VMs, file systems, and workloads that require instant application-aware mounts, virtual database clones (LiveClones), or automated Backup and DR Workflows.
  * **[Google Cloud Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)** : A cloud-native, SaaS-managed backup experience integrated directly into the Google Cloud console, [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), backupdr API, and Terraform. With Google Cloud Backup and DR, you protect native Google Cloud resources—such as Compute Engine instances, Persistent Disks and Google Cloud Hyperdisks, Cloud SQL instances, AlloyDB clusters, and Filestore instances—directly into Google-managed, immutable backup vaults without deploying or managing backup/recovery appliances.



The following table summarizes the key differences between the two Backup and DR offerings:

Feature | Backup and DR for the management console | Google Cloud Backup and DR  
---|---|---  
**Primary management interface** | Dedicated web-based appliance management console and [Management Console API](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/api) | Google Cloud console, gcloud CLI, backupdr API, and Terraform  
**Architecture and data plane** | Three-tier appliance architecture consisting of the appliance management console, customer-deployed backup/recovery appliances (Compute Engine VMs in your VPC), and lightweight Backup and DR agents on workload hosts | Fully managed Google service plane; no customer-deployed backup/recovery appliances or guest agents required for console-native vaulted resources  
**Backup configuration model** | [Backup templates](https://docs.cloud.google.com/backup-disaster-recovery/management-console/create-plan/create-template) (containing snapshot, OnVault, and replication policies) combined with [resource profiles](https://docs.cloud.google.com/backup-disaster-recovery/management-console/create-plan/create-resource-profiles) | Console-native [backup plans](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan) and backup rules associated directly with a target backup vault  
**Storage targets** | Appliance-managed [storage pools](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/storage-pools) (Primary pool, Snapshot pool on Persistent Disk, OnVault pool in Cloud Storage, and Mirror pool on a remote appliance), plus Google-managed [backup vaults](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/backup-vault-with-ba) for supported workloads | Google-managed, immutable, and indelible [backup vaults](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault) with enforced retention and regional or multi-region storage  
**Recovery and data access** | Full restore, instant standard mounts, [application-aware mounts](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/application-aware-mounts), virtual copies ([LiveClones](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/liveclone)), Mount and Migrate, and automated [Backup and DR Workflows](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/backupdr-workflows) | Direct restore to new or existing Google Cloud resources from a backup vault  
**Supported workloads** | Google Cloud VMware Engine, VMware vSphere VMs, Compute Engine instances, Linux and Windows file systems (including NFS, SMB, and Filestore), Oracle, Microsoft SQL Server, SAP HANA, IBM Db2, PostgreSQL, SAP ASE, SAP IQ, SAP MaxDB, MySQL, MariaDB, consistency groups, and generic applications | Compute Engine instances, Persistent Disks and Hyperdisks, Cloud SQL, AlloyDB, and Filestore (plus visibility into backup vault backups created by the appliance management console)  
**Note:** You can also use Backup and DR for the management console together with Google-managed backup vaults for select workloads—including [Oracle](https://docs.cloud.google.com/backup-disaster-recovery/management-console/backup/backup-oracle-into-backup-vault), [Microsoft SQL Server](https://docs.cloud.google.com/backup-disaster-recovery/management-console/backup/backup-sql-server-into-backup-vault), and [Google Cloud VMware Engine](https://docs.cloud.google.com/backup-disaster-recovery/management-console/backup/backup-gcve-into-backup-vault)—by configuring an OnVault storage pool that points to a backup vault created in the Google Cloud console.

## Architecture and core components of Backup and DR for the management console

Backup and DR for the management console uses a three-tier architecture to orchestrate and execute data protection across your environment:

  * **Appliance management console** : The centralized, web-based control plane where you manage backup/recovery appliances, register hosts, discover applications, configure backup templates and resource profiles, and monitor backup and recovery jobs. The appliance management console runs in a Google-managed tenant project and communicates securely with your backup/recovery appliances using Private Service Connect or Private Google Access.
  * **Backup/recovery appliances** : Compute Engine virtual appliances deployed in your Google Cloud project and VPC network. The backup/recovery appliance acts as the data plane that captures data from source workloads, maintains catalog metadata, manages storage pools, replicates data to remote appliances or object storage, and serves instant mounts. You can choose from four [appliance form factors](https://docs.cloud.google.com/backup-disaster-recovery/management-console/deployment/deployment-plan#appliance) based on workload type, dataset size, and storage capacity.
  * **Backup and DR agents** : Lightweight software agents installed on Linux or Windows guest operating systems. The [Backup and DR agent](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/about-connector) communicates with the backup/recovery appliance to discover databases and file systems, quiesce applications for application-consistent capture, coordinate changed-block tracking (CBT) and transaction log backups, and orchestrate application-aware mounts. Agentless protection is used for VMware VMs (through vSphere Storage APIs - Data Protection) and Compute Engine instances (through Persistent Disk snapshots).



### Storage pools on a backup/recovery appliance

A backup/recovery appliance organizes and stores captured backup data across up to four types of [storage pools](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/storage-pools):

  * **Primary pool** : Block storage attached directly to the backup/recovery appliance (using Standard or SSD Persistent Disks) that stores captured backups and deduplicated data for fast local recovery and instant mounting.
  * **Snapshot pool** : Storage that uses Persistent Disk snapshots to store point-in-time copies of data volumes for high-performance capture and mount operations.
  * **OnVault pool** : Object-based storage for long-term retention that sends compressed, incremental-forever backup data to a [Cloud Storage bucket](https://docs.cloud.google.com/backup-disaster-recovery/management-console/backup/create-onvault-pool) (Standard, Nearline, Coldline, or Archive) or a Google-managed [backup vault](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/backup-vault-with-ba).
  * **Mirror pool** : Block storage on a secondary backup/recovery appliance in another zone or region that receives asynchronous, block-level replicated backups (StreamSnap) for disaster recovery.



### Backup templates, policies, and resource profiles

In the appliance management console, you protect a discovered workload by applying a backup plan composed of two reusable building blocks:

  * **[Backup template](https://docs.cloud.google.com/backup-disaster-recovery/management-console/create-plan/create-template)** : Defines _how_ and _when_ data is backed up, retained, and replicated. Each backup template contains one or more [backup policies](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/policy-overview) that control schedules, recovery point objectives (RPOs), and retention across tiers: 
    * **Production to Snapshot** : Captures data from the production workload to the local Primary or Snapshot pool.
    * **Snapshot to OnVault** : Copies snapshot backups to an OnVault pool in Cloud Storage or a backup vault for long-term retention.
    * **OnVault to OnVault** : Replicates data between OnVault pools across regions.
    * **Production to Mirror (StreamSnap)** : Replicates snapshot data to a Mirror pool on a remote backup/recovery appliance.
  * **[Resource profile](https://docs.cloud.google.com/backup-disaster-recovery/management-console/create-plan/create-resource-profiles)** : Defines _where_ the backup data is stored by mapping the policies in a backup template to specific local backup/recovery appliance storage pools, OnVault pools, and remote replication appliances.



## Key capabilities of Backup and DR for the management console

Backup and DR for the management console provides the following capabilities for enterprise backup, recovery, and copy data management:

  * **Incremental-forever capture** : After a single initial full backup of an application or VM, subsequent backups capture only changed blocks or database deltas. The backup/recovery appliance synthesizes virtual full point-in-time images without running periodic full backups that impact production performance.
  * **Application-consistent database protection and point-in-time recovery (PITR)** : Integrates natively with database APIs (such as Oracle RMAN, SQL Server VSS, and SAP HANA `backint` or storage snapshots) to capture application-consistent database backups alongside scheduled transaction log backups, which lets you recover to a specific point in time.
  * **Instant mount and virtual copies** : Instead of waiting to copy terabytes of backup data back to production storage before an application can start, you can [mount a backup image](https://docs.cloud.google.com/backup-disaster-recovery/management-console/access-data/access-backup-data) directly from the backup/recovery appliance to a target host: 
    * **Standard mount** : Exposes the backup image as a mounted disk or file system on a target host to inspect or copy individual files.
    * **[Application-aware mount](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/application-aware-mounts)** : Instantly starts a virtual database instance directly from the mounted backup image on a target database server, optionally rolling forward transaction logs to a chosen point in time.
    * **Mount and Migrate** : Restores service immediately over an instant mount while migrating the underlying data files back to production storage in the background, minimizing recovery time objectives (RTOs).
    * **[LiveClone](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/liveclone)** : Creates an independent, writable virtual copy of a backup image that can be refreshed on demand or on a schedule without consuming full physical storage for each clone.
  * **Automated Backup and DR Workflows** : [Backup and DR Workflows](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/backupdr-workflows) automate the creation, refresh, and masking of LiveClones and virtual databases on a schedule or on demand. Development, QA, and analytics teams can self-provision up-to-date copies of production databases with sensitive data scrubbed automatically by custom scripts.
  * **Cross-region disaster recovery** : Replicate backup images asynchronously to a secondary backup/recovery appliance in another region using [StreamSnap replication](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/data-replication), or copy backups to multi-region or dual-region Cloud Storage buckets and backup vaults so you can recover workloads in an alternate region during an outage.



## Supported workloads in Backup and DR for the management console

Backup and DR for the management console protects a broad range of virtual machines, file systems, and databases. For detailed version and operating system compatibility, see the [Support matrix for appliance-managed backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/supportmatrix-backupdr) and [Backup and DR supported operating systems and kernels](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/backupdr-supported-os-kernels).

  * **[Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/backupdr-for-compute-engine)** : Agentless, crash-consistent snapshot protection and cross-project or cross-region recovery for Compute Engine VMs.
  * **[Google Cloud VMware Engine and VMware vSphere VMs](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/backupdr-for-vmware-vms)** : Agentless VM-level backup, instant mount, LiveClone, and full VM recovery for vCenter and ESX hosts using VMware changed-block tracking (CBT).
  * **[File systems and Filestore](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/backupdr-for-filesystems)** : Block-based and file-based backup and instant mount for Linux and Windows file systems, NFS shares, SMB/CIFS shares, and Filestore instances.
  * **[Oracle databases](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/backupdr-for-oracle)** : Incremental-forever protection using Oracle RMAN image copies and Change Tracking, archive log backups for PITR, instant virtual database mounts, and Mount and Migrate.
  * **[Microsoft SQL Server databases](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/backupdr-for-sql-server)** : Application-consistent backups for standalone instances and Always On availability groups, transaction log backups, virtual database mounts, and database cloning.
  * **[SAP HANA databases](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/backupdr-for-sap-hana)** : Volume-level (Persistent Disk snapshot or LVM) and file-level (`backint`) protection for single-host, 1+n, and [SAP HANA scale-out](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/backupdr-for-sap-hana-scaleout) systems.
  * **[IBM Db2 databases](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/backupdr-for-db2)** : Volume-level incremental-forever backups and full-plus-incremental dump backups with transaction log capture and virtual database mounts.
  * **[Other self-managed databases](https://docs.cloud.google.com/backup-disaster-recovery/management-console/configuration/prepare-otherdb)** : Protection for PostgreSQL, MySQL, MariaDB, SAP ASE, SAP IQ, and SAP MaxDB databases, as well as [consistency groups](https://docs.cloud.google.com/backup-disaster-recovery/management-console/configuration/discover-consistency-groups) and [generic LVM applications](https://docs.cloud.google.com/backup-disaster-recovery/management-console/configuration/discover-generic-apps).



## What's next

  * Review [deployment considerations](https://docs.cloud.google.com/backup-disaster-recovery/management-console/deployment/deployment-considerations) and [set up and plan a deployment](https://docs.cloud.google.com/backup-disaster-recovery/management-console/deployment/deployment-plan).
  * [Prepare your cloud infrastructure and workloads](https://docs.cloud.google.com/backup-disaster-recovery/management-console/configuration/prepare-workloads-for-backupdr).
  * Learn about [storage pools](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/storage-pools) and [backup policies](https://docs.cloud.google.com/backup-disaster-recovery/management-console/concepts/policy-overview).
  * Learn about [Google Cloud Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr) in the Google Cloud console.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-02 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/netapp/volumes/docs/get-started/migration-to-flex-unified/
title: Migration to Flex Unified service level \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T12:22:27.035957+00:00
---

# Migration to Flex Unified service level  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/get-started/migration-to-flex-unified/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Migration to Flex Unified service level Stay organized with collections  Save and categorize content based on your preferences. 

You can migrate existing volumes to the [Flex Unified](https://docs.cloud.google.com/netapp/volumes/docs/discover/features#flex_unified_default-mode_versus_ontap-mode) service level by using host-based copy tools, backup and restore, or support-assisted replication. Depending on your volume size and downtime requirements, you can select the most suitable migration tool for your workload.

**Important:** As the Flex Unified service level is expanding, the Flex File service level is being phased out. Effective September 15, 2026, you can't create new Flex File storage pools, but existing pools remain supported. If you need assistance migrating to Flex Unified, [send an email to the support team](mailto:flex-file-migration@google.com). If you have specific region requirements or need support for Assured Workloads with Flex Unified, [contact the Google Cloud sales team](https://cloud.google.com/contact).

The Flex Unified service level provides all NetApp ONTAP features on Google Cloud for both file and block storage on a single platform.

The following table compares the features available in the Flex Unified service level against the legacy service levels (Flex File, Standard, Premium, and Extreme).

Feature | Flex Unified | Flex File  
(legacy) | Standard, Premium, and Extreme  
(legacy)  
---|---|---|---  
**Block storage (iSCSI and NVMe/TCP)** | Yes | No | No  
**Dual-protocol volumes (SMB and NFS)** | Yes | No | Yes  
**Auto-tiering** | Yes | Yes | Standard: No   
Premium or Extreme: Yes  
**ONTAP capabilities (ONTAP-mode pools)** | Yes | No | No  
**ONTAP integration (SnapMirror and FlexCache)** | Yes | No | Yes  
**Selective file restore and cross-region backups** | Yes | No | Yes  
**Shared QoS at the pool level** | Yes | Yes | No  
**Thin clones** | Yes | No | No  
**Large capacity pools and volumes** | Yes | No | Standard: No   
Premium or Extreme: Yes  
**Throughput** | Increased throughput  
with large volumes | Standard throughput | Increased throughput  
with large volumes  
**Regional availability** | Yes | Yes | No  
  
## Migration tools

You can use the following tools to migrate volumes to the Flex Unified service level:

  * Host-based data copy

  * Backup and restore

  * Support-assisted replication




Use the following table to select the appropriate tool for your use case.

Tool | Use case | Considerations  
---|---|---  
Host-based data copy | Reorganizing volume data, either by removing or consolidating directories, or moving data from a regular volume to a large capacity volume | 

  * Mount IP address changes

  
Backup and restore | Moving a few small volumes | 

  * Restore at 300 GiB per hour
  * Mount IP address changes

  
Support-assisted replication | Moving a few large volumes | 

  * Preserves snapshots and SMB permissions
  * Supports immediate cutover after final incremental update
  * Mount IP address changes

  
  
## Host-based data copy

To move data to Flex Unified volumes by using host-based copy tools, complete the following steps:

  1. Select one of the data copy tools described in this section to create a full copy of the data.

  2. Create a full copy of the data, and then run incremental copies to capture any changes.




### Data copy tools

Select a data copy tool based on your client operating system and protocol:

  * Robocopy: Copies SMB files on a Windows VM.

  * NetApp XCP or rsync: Copies NFS files on a Linux VM.




#### Robocopy

Robocopy is a [Microsoft file copy tool](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy) for Windows systems.

Consider the following options when you use robocopy:

  * `/mir`: Copies all subdirectories, including the empty subdirectories.

  * `/sec /secfix`: Copies security information, such as access control lists (ACLs), including information about the unchanged files with security changes. For more information, see [robocopy mirroring file permissions](https://techcommunity.microsoft.com/blog/filecab/robocopy-mir-switch-8211-mirroring-file-permissions/423662).

  * `/z`: Enables restartable mode, which allows robocopy to resume if interrupted.

  * `/mt:32`: Uses 32 threads for multi-threaded copies.

  * `/b`: Uses backup mode to override file and directory ACLs. Robocopy users must be members of the backup operators group on both the source and destination volumes.

  * `/r:2 /w:1`: Retries failed copies with a one-second wait.

  * `/log:<var>logfile</var>`: Logs robocopy status output.




#### NetApp XCP

XCP is a [NetApp data migration tool](https://xcp.netapp.com/) that copies files during data migrations. You can use it to migrate data to Flex Unified service level volumes. For additional assistance in using this tool, contact your NetApp sales specialist.

### Copy data using host-based tools

To copy data using a host-based copy tool, complete the following steps:

  1. Create a NetApp Volumes Flex Unified [pool](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/create-storage-pool) and a [volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/create-volume).

  2. [Mount](https://docs.cloud.google.com/netapp/volumes/docs/get-started/quickstarts/mount-volume#mount_your_volume_on_a_client) the existing volume and the new Flex Unified volume to a virtual machine (VM) in your Virtual Private Cloud (VPC) network. Use a data copy tool to transfer the data to the Flex Unified volume.

  3. To perform a final incremental copy of the data to the Flex Unified volume, disconnect clients from the current volume during scheduled maintenance. Verify that you have copied all files by checking file counts, checksums, and similar validation methods.

  4. Connect the clients to the Flex Unified volume and test access.




## Copy data using backup and restore

The [backup and restore](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-backups) feature in NetApp Volumes is available with Standard, Premium, Extreme, Flex File, and Flex Unified service levels. You can use this feature to back up a volume and restore it to a new Flex Unified storage pool.

### Considerations

Consider the following details when you migrate using the backup and restore feature:

  * NFS exports and SMB shares receive a new IP address. For SMB shares, the NetBIOS name retains its prefix and receives a new five-character suffix.

  * You can't use hyphens in Flex Unified volume names, but you can still use hyphens in export and share names. These volume name changes can affect Terraform, other automation, and your monitoring and alerting configurations.

  * The restore process migrates SMB permissions and NFS ACLs along with your files and folders.

  * Backup and restore doesn't migrate existing snapshots. For the new volume, you must create export and tiering policies, and data protection policies for snapshots, backups, and replications.

  * Backup features, such as cross-region backups and customer-managed encryption keys (CMEK), aren't supported with Flex File, and you can't use them during migrations.

  * The Flex File service level doesn't support large capacity volumes. You can't use the backup and restore feature to migrate data from a Flex File volume to a large capacity Flex Unified volume. Use a host-based data copy instead.

  * You can't choose a specific time for scheduled backups. If you have scheduled backups configured, check when previous backups ran to estimate the next backup time. For more control over backup timing, use manual backups.

  * Billing for the original pool continues until you complete the migration and delete the pool.




### Migrate a volume using backup and restore

To migrate a volume using the backup and restore feature, complete the following steps:

  1. Create a baseline backup of the Standard, Premium, Extreme, or Flex File volume before migration. If the volume has scheduled backups, you can use one of them. This backup serves as a baseline and helps reduce the time needed for the final incremental backup.

  2. [Create a NetApp Volumes Flex Unified pool](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/create-storage-pool) if needed.

  3. During a maintenance window, complete the following steps:

     1. Disconnect the clients from the existing volume and perform a final incremental manual backup of the data.

After the backup status changes to **Ready** , wait 20 minutes for the process to finish, and then continue to the next step.

     2. After the incremental backup completes, select **Create volume from backup** using the latest incremental backup, and then choose the Flex Unified storage pool where you want to create the new volume.

**Note:** For planning purposes, assume a restore rate of approximately 300 GiB per hour. You can track the progress in **Notifications** in the Google Cloud console.
     3. After the restore completes, connect a client to the Flex Unified volume, and then verify the volume using your application.

  4. Connect your remaining clients to the Flex Unified volume.




## Copy data using support-assisted replication

The support team can help you replicate Flex File volumes to new Flex Unified volumes. First, the team creates a baseline copy of your volumes, and then copies subsequent changes through smaller incremental updates.

When you're ready to move clients to the new volumes, you must schedule a maintenance window. During this window, you disconnect the clients, run a final incremental update, and then reconnect the clients to the new volumes. This approach minimizes downtime because the final update transfers only recent changes.

### Considerations

Consider the following details when you migrate using support-assisted replication:

  * NFS exports and SMB shares receive a new IP address. For SMB shares, the NetBIOS name retains its prefix and receives a new five-character suffix.

  * Replication replaces hyphens in volume names with underscores, but you can still use hyphens in export and share names. These volume name changes can affect Terraform, other automation, and your monitoring and alerting configurations.

  * Replication copies SMB permissions and NFS ACLs along with your files and folders.

  * Replication copies existing export, snapshot, and tiering policies to the new volumes. To protect data on the new volumes, you must create backup and replication policies.

  * Replication copies existing snapshots to the new volumes.

  * Billing for the original pool continues until you complete the migration and delete the pool.




### Migrate volumes using support-assisted replication

To migrate volumes using support-assisted SnapMirror replication, complete the following steps:

  1. In your project, identify the Flex File pool and volumes that you want to migrate. The support team reviews these resources because any existing backups or replications must be paused during the migration. If the existing volumes use auto-tiering, you can also enable it on the Flex Unified pool.

  2. If you have multiple storage volumes, decide how to group them for migration to minimize client mount changes. Consider the following factors when you group volumes:

     * The original IP address for the volumes changes to a new address from the `/28` CIDR range used for the Flex Unified pool.

     * Flex Unified volumes require underscores instead of hyphens in Google Cloud volume resource names. However, the share and mount paths remain the same. For more information, see [Volume and share naming rules](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/create-volume#volume_and_share_naming_rules).

     * Each pool supports up to 10 concurrent SnapMirror replications.

  3. [Create a NetApp Volumes Flex Unified pool](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/create-storage-pool) based on guidance from the support team, including any required settings for custom performance and auto-tiering. If you need SMB, create a small placeholder SMB volume in the pool. If you use auto-tiering, enable hot-tier bypass during the migration.

  4. Work with the support team to create the new Flex Unified volumes and SnapMirror replications to start the baseline data copy.

The baseline copy typically runs at about 1 TiB per hour and can reach up to 2.6 TiB per hour, or 764 MiBps, on pools with higher custom performance settings. Because replication prioritizes client I/O, the replication speed might decrease depending on workload activity. After the baseline copy completes and replication switches to incremental updates, the volumes are ready for cutover.

  5. During a maintenance window, complete the following steps:

     1. Disconnect the clients from the original volumes.

     2. Work with the support team to run a final incremental update, and then stop replication.

     3. Confirm that you can view and manage the Flex Unified volumes in your project.

     4. Verify that the new volumes inherited the export, snapshot, and tiering policies, along with the NFS ACLs and SMB NTFS permissions, from the original volumes. Replication automatically copies these settings with your files.

     5. Connect a client to the Flex Unified volumes, and then verify access using your application.

  6. Connect your remaining clients to the Flex Unified volumes.

  7. Recreate any required backup and replication policies on the new volumes.




## What's next

For more information, see the following resources:

  * [Connect SMB clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-smb-clients).

  * [Connect NFS clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nfs-clients).

  * [Connect iSCSI clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-iscsi-clients).

  * [Connect NVMe/TCP clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nvme-tcp-clients).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-11 UTC."],[],[]] 

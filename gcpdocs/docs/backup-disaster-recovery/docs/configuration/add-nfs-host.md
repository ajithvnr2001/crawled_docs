---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/
title: Add a Filestore or any other NFS file system or file share to the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:11:54.350955+00:00
---

# Add a Filestore or any other NFS file system or file share to the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/

[ Skip to main content ](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/)
  * [Deutsch](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/?hl=de)
  * [Español](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/?hl=es-419)
  * [Français](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/?hl=id)
  * [Italiano](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/?hl=it)
  * [Português](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/?hl=ja)
  * [한국어](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fbackup-disaster-recovery%2Fdocs%2Fconfiguration%2Fadd-nfs-host%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/operations-color.svg) ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Install Backup and DR agent and generate secret key](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/#agent)
  * [Add NFS host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/#add_nfs_host)
  * [Discover NFS shares](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/#discover_nfs_shares)
  * [What's next](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/#whats_next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)


Was this helpful?
Send feedback 
#  Add a Filestore or any other NFS file system or file share to the appliance management console Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Install Backup and DR agent and generate secret key](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/#agent)
  * [Add NFS host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/#add_nfs_host)
  * [Discover NFS shares](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/#discover_nfs_shares)
  * [What's next](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/#whats_next)


Backup and DR can discover and back up NFS shares on a Linux host. Before you can run application discovery to add the NFS shares to Backup and DR, you must have a [Backup and DR Agent installed on the NFS host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/#agent)
You can also back up Filestore instances working completely within the Google Cloud environment using the Google Cloud console, [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or Terraform. This method is familiar but it has some limitations.
If you have any of the following backup requirements, you can use the Backup and DR appliance management console to back up Filestore instances to a backup/recovery appliance:
  * Backups of specific disks attached to a virtual machine (VM)
  * Automated protection of Google Compute Engine VMs based on tags
  * If the Google Cloud console-based backup plans and backup vaults are not in a [location that is compatible](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#workload-location-compatibility) with the region where your source VMs are running.


To back up Filestore instances in the Google Cloud environment, see [Back up Filestore instances to a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/filestore/filestore-instance-backup).
To back up Filestore instances using the appliance management console, continue on this page.
## Install Backup and DR agent and generate secret key
You need to have the secret key to provide access to the NFS host. If you haven't already, [install the Backup and DR Agent using the agent install](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/linux-agent).
## Add NFS host
Use the following instructions to add a new Linux host to the appliance management console:
  1. In the appliance management console, go to **Manage** > **Hosts**.
  2. Select **+ Add Host**.
  3. In the **Add Host** form, enter the name and an optional friendly name. The name of a host must start with a letter, and can contain letters and digits (0-9). Underscore ('_') characters are not valid in host names.
  4. Enter the IP address of the host in **IP Address**. Click the **plus sign (+)** to add it.
  5. In the **Appliances** section, select the appliance management console managed appliances that serve this host. If the list is long, you can use the search field to find a specific appliance or group of appliances.
  6. Leave **Host Type** as **Generic**.
  7. In the Backup and DR agent settings, complete the following:
     * Backup and DR agent port is normally port 5106. If it is anything else, enter the port number.
     * You need to supply a secret key generated on the Linux host servers by the Backup and DR agent to initialize trusted communications between the host and Backup and DR agent. This only needs to be done once. If you don't have the secret key, generate one by [Install the Backup and DR agent on a Linux host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/linux-agent).
  8. Click **Add**. If you get a partial success message, use the instructions to [Validate backup/recovery appliance to Backup and DR agent connectivity](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/appliance-network-settings#validate).


## Discover NFS shares
Use the following instructions to add NFS shares:
  1. Discover the NFS application discovery in either of the following ways:
     * In the appliance management console, click the **Back up & Recover** drop-down menu and select **Back up** , and then select **All Apps**.
     * Go to **App Manager** > **Applications** , select **Add Applications** and then select **All Apps**.
  2. Select the host that you added in **Add NFS host** section and click **Discover**. After the NFS shares are discovered, you can find them using the **NFS** filter in the **Applications** page.


## What's next
  * To apply a backup plan for NFS applications, see [Apply backup template to manage mapped NFS file system](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-plan-to-filesystem)
  * To define NFS specific backup settings, see [Configure application settings to protect mapped NFS file system data](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/configure-app-settings-for-filesystems)
  * To mount a NFS backup, see [Mount a SMB share, file system, or NFS backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-file-system)
  * To restore NFS backups, see [File system restore](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/filesystem-restore)


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

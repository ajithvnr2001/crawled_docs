---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-plans/create-manual-backup/
title: Create a manual backup \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:56:47.493989+00:00
---

# Create a manual backup  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-plans/create-manual-backup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create a manual backup Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to manually create a backup for virtual machine (VM) workloads in Google Distributed Cloud (GDC) air-gapped.

By default, your backup plan automatically initiates scheduled backups. You can also manually create VM backups at any time, even outside of the schedule that you define. Manual VM backups let you capture a VM's state instantly and provide a recovery point independent of your scheduled backup plan.

This document is for developers in platform administrator or application operator groups that manage VM backup operations. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To create manual VM backups, you must have a [single VM backup repository](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-repository/create-backup-repository) for backup data.

### Request IAM roles

To complete the tasks in this document, request the required organization and project roles.

#### Organization-level roles

Ask your IAM Org Admin to [grant you](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings) the **Organization Backup Admin** (`organization-backup-admin`) role. This role lets you create, get, list, watch, update, patch, and delete VM backup repositories, VM backup plan templates, VM backup requests, and VM restore requests.

#### Project-level roles

Ask your IAM Project Admin to [grant you](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/role-bindings) the following roles:

  * **Virtual Machine Project Admin** (`project-vm-admin`): creates, gets, lists, watches, updates, patches, and deletes virtual machines and VM disks in project namespaces.
  * **Backup Creator** (`backup-creator`): creates, gets, lists, watches, updates, patches, and deletes manual backup requests and manual restore requests.
  * **Project Viewer** (`project-viewer`): gets, lists, and watches all resources within project namespaces.



Follow the steps to [verify your access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation#verify-user-access).

## Create a backup plan template for VMs

You must create a backup plan template before you can trigger a manual backup. You only need to perform this step once for each backup repository. Don't create another template if you've already created one.

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Backup for Virtual Machines > Backup plans**.
  3. Click **Create a backup plan**.
  4. In the **Project** field, select the project for this backup plan.
  5. Enter the backup plan name and description.
  6. In the **Backup repo** field, select a backup repository. Backup repositories are a set of object storage implementations.
  7. Click **Create**.



### kubectl

To plan your backups, create and apply a `VirtualMachineBackupPlanTemplate` custom resource:
    
    
    kubectl apply -f - <<EOF
    apiVersion: virtualmachine.gdc.goog/v1
    kind: VirtualMachineBackupPlanTemplate
    metadata:
      name: BACKUP_TEMPLATE_NAME
      namespace: PROJECT_NAME
    spec:
      backupRepository: "BACKUP_REPOSITORY_NAME"
    EOF
    

Replace the following:

  * `BACKUP_TEMPLATE_NAME`: the name of the backup plan template.
  * `PROJECT_NAME`: the name of the project in which you want to create the template.
  * `BACKUP_REPOSITORY_NAME`: the name of the backup repository you create in the previous step.



## Create manual backups

### Create a manual VM backup

To create a manual VM backup, create and apply a `VirtualMachineBackupRequest` custom resource and specify the target of the backup using one of two methods:

  * **Reference an existing backup plan** : Use the `namespace` field in the metadata to specify the project where the plan exists, and the `virtualMachineBackupPlan` field to target the specific backup plan:
        
        kubectl apply -f - <<EOF
        apiVersion: virtualmachine.gdc.goog/v1
        kind: VirtualMachineBackupRequest
        metadata:
          name: BACKUP_REQUEST_NAME
          namespace: PROJECT # Use this field if the backup plan was created using the API.
        spec:
          virtualMachineBackupPlan: VM_BACKUP_PLAN
          virtualMachineBackupName: VM_BACKUP_NAME
          deleteLockDays: DELETE_LOCK_DAYS
          retainDays: RETAIN_DAYS
        EOF
        

  * **Use a template and target a specific VM** : Use the `virtualMachineBackupPlanTemplate` and `virtualMachine` fields when you define a new, immediate backup based on a template. With this method, you must specify the target VM directly in the `spec` section:
        
        kubectl apply -f - <<EOF
        apiVersion: virtualmachine.gdc.goog/v1
        kind: VirtualMachineBackupRequest
        metadata:
          name: BACKUP_REQUEST_NAME
        spec:
          virtualMachineBackupPlanTemplate: VM_BACKUP_PLAN_TEMPLATE
          virtualMachine: VM_NAME
          virtualMachineBackupName: VM_BACKUP_NAME
          deleteLockDays: DELETE_LOCK_DAYS
          retainDays: RETAIN_DAYS
        EOF
        




Replace the following:

  * `BACKUP_REQUEST_NAME`: the name for the backup request that you're initiating.
  * `PROJECT`: the name of the project where the backup plan resides.
  * `VM_BACKUP_PLAN`: the name of the `VirtualMachineBackupPlan` custom resource to target for the backup.
  * `VM_BACKUP_PLAN_TEMPLATE`: the name of the `VirtualMachineBackupPlanTemplate` custom resource that configures the backup.
  * `VM_NAME`: the name of the VM to back up.
  * `VM_BACKUP_NAME`: the name of the backup to create.
  * `DELETE_LOCK_DAYS` (optional): the number of days from the creation of this backup that the system blocks backup deletion. The value must not exceed 90 days and must be less than or equal to `RETAIN_DAYS`. If you set this value to `0`, the system doesn't block deletion. If you omit this value, it defaults to the associated backup plan's configuration.
  * `RETAIN_DAYS` (optional): the number of days to keep this backup before the system automatically deletes it. The value must not exceed 90 days. If you set this value to `0`, the system doesn't automatically delete the backup. If you omit this value, it defaults to the associated backup plan's configuration.



### Create a snapshot

A snapshot captures a point-in-time image of a VM disk for restores, unlike a VM backup, which creates an independent copy of VM data in a backup repository.

Create a snapshot using either the GDC console or the API.

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Virtual Machines > Snapshots**.
  3. Select a project.
  4. Click **Create snapshot**.
  5. In the **Source disk** field, select the disk that you want to create the snapshot from.
  6. In the **Snapshot name** field, enter a name for the snapshot.
  7. Click **Create**.



### kubectl

Create and apply a `VirtualMachineBackupRequest` custom resource to initiate a snapshot:
    
    
    kubectl apply -f - <<EOF
    apiVersion: virtualmachine.gdc.goog/v1
    kind: VirtualMachineBackupRequest
    metadata:
      name: BACKUP_REQUEST_NAME
      namespace: PROJECT_NAME
    spec:
      virtualMachineBackupPlanTemplate: VM_BACKUP_PLAN
      virtualMachineDisk: VM_DISK
      virtualMachineBackupName: VM_BACKUP_NAME
      deleteLockDays: DELETE_LOCK_DAYS
      retainDays: RETAIN_DAYS
    EOF
    

Replace the following:

  * `BACKUP_REQUEST_NAME`: the name for the backup request that you're initiating.
  * `PROJECT_NAME`: the name of the GDC project.
  * `VM_BACKUP_PLAN`: the name of the `VirtualMachineBackupPlanTemplate` custom resource that configures the snapshot.
  * `VM_DISK`: the name of the disk that you want to snapshot.
  * `VM_BACKUP_NAME`: the name of the snapshot to create.
  * `DELETE_LOCK_DAYS` (optional): the number of days from the creation of this snapshot that the system blocks snapshot deletion. The value must not exceed 90 days and must be less than or equal to `RETAIN_DAYS`. If you set this value to `0`, the system doesn't block deletion. If you omit this value, it defaults to the associated backup plan's configuration.
  * `RETAIN_DAYS` (optional): the number of days to keep this snapshot before the system automatically deletes it. The value must not exceed 90 days. If you set this value to `0`, the system doesn't automatically delete the snapshot. If you omit this value, it defaults to the associated backup plan's configuration.



## What's next

  * [Manage backups](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-plans/manage-backups)
  * [Create a restore](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/restore-backup/create-restore-scoped)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 

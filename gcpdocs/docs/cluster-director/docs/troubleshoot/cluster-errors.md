---
url: https://docs.cloud.google.com/cluster-director/docs/troubleshoot/cluster-errors/
title: Troubleshoot errors in Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-05T11:12:32.224633+00:00
---

# Troubleshoot errors in Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/troubleshoot/cluster-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Troubleshoot errors in Cluster Director Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to resolve common issues and errors that you might encounter when you create, modify, or run workloads on a cluster in Cluster Director. If your error isn't listed in this document, then see the following troubleshooting documentation for Compute Engine resources, Cloud Storage resources, or Google Cloud networking services:

  * [Troubleshoot creating, updating, and deleting Compute Engine instances](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-vm-creation)

  * [Troubleshoot Compute Engine reservation consumption](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-consumption)

  * [Troubleshoot Filestore instance mounting issues](https://docs.cloud.google.com/filestore/docs/mount-issues)

  * [Troubleshoot Managed Lustre instances](https://docs.cloud.google.com/managed-lustre/docs/troubleshooting)

  * [Troubleshoot Cloud Storage bucket issues](https://docs.cloud.google.com/storage/docs/troubleshooting)

  * [Troubleshoot common networking issues](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-networking)

  * [Troubleshoot VPC policy and access problems](https://docs.cloud.google.com/vpc/docs/troubleshooting-policy-and-access-problems)




## Resolve general cluster errors

This section describes common errors related to resource capacity, quotas, or location during cluster creation or modification.

### Resolve duplicate resource name errors

This error occurs when Cluster Director attempts to create a resource with a name that already exists in your project.

**Error message** : You might receive the following error message:
    
    
    Resource RESOURCE_NAME already exists
    

**Resolution** : Cluster Director names resources with the cluster name as a prefix. For example, if you name a cluster `cluster123`, then the names of the resources that are associated with that cluster start with `cluster123-`. To resolve a naming conflict, complete the following steps:

  1. Identify the resource from the error message or the [audit logs](https://docs.cloud.google.com/cluster-director/docs/monitor/view-audit-logs).

  2. Check the timestamp for when the resource was created, and then do one of the following:

     * If the resource was created when you attempted to create your cluster, then delete the resource and try again to create the cluster. If the error persists, then use a different name for your cluster.

     * If the resource existed before you attempted to create your cluster, then do one of the following:

       * If you no longer need the existing resource, then delete the resource and retry creating the cluster.

       * If you must keep the existing resource, then use a different name for your cluster.




### Resolve insufficient quota errors

This error occurs when you attempt to create virtual machine (VM) instances by using the Flex-start, Spot, or On-demand consumption options, but your project lacks sufficient quota for the requested resources.

**Error messages** : You might receive one of the following error messages:
    
    
    RESOURCE_NAME creation failed: Quota QUOTA_NAME exceeded. Limit QUOTA_LIMIT in region REGION
    
    
    
    RESOURCE_NAME creation failed: Quota QUOTA_NAME exceeded. Limit QUOTA_LIMIT in zone ZONE
    
    
    
    Resource exhausted (HTTP 429): QUOTA_EXCEEDED
    

**Resolution** : Check that your project has sufficient quota for the resources that you want to request, and then retry your request to create or modify the cluster. For more information about managing quota, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage).

### Resolve region or zone availability errors

This error occurs when your requested compute resource isn't available in the specified region or zone.

**Error messages** : You might receive one of the following error messages:
    
    
    notFound
    
    
    
    does not exist in zone
    

**Resolution** : Select a region or zone that supports your requested compute resources. Note that Cluster Director doesn't support AI zones (zones with names that end in `-ai`). To review supported locations, see [Cluster Director locations](https://docs.cloud.google.com/cluster-director/docs/locations).

### Resolve resource unavailability errors

This error occurs when a specified compute resource isn't available in the region or zone where you are attempting to create your cluster.

**Error messages** : You might receive one of the following error messages:
    
    
    ZONE_RESOURCE_POOL_EXHAUSTED
    
    
    
    The zone 'projects/PROJECT_ID/zones/ZONE' does not have enough resources available to fulfill the request. Try a different zone, or try again later.
    
    
    
    A MACHINE_TYPE VM instance with RESOURCE_ATTACHMENT is currently unavailable in the ZONE zone.
    

**Resolution** : All compute resources that you specify when you create a cluster must be available. To resolve this issue, do the following:

  * If you want to use the Flex-start, Spot, or On-demand consumption option, then try one of the following:

    * Create the cluster in a different region or zone.

    * Create the cluster at a later time when resources become available.

    * Create the cluster by using a different compute or storage configuration.

  * Otherwise, for a higher guarantee of capacity, reserve capacity by using one of the following methods:

    * [Use future reservations for capacity blocks](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option#future-reservations)

    * [Use future reservations in calendar mode](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option#calendar-mode)

If Google approves your reservation request, then try to create your cluster again at the request's start time.




## Resolve A4X resource pool exhaustion

This error occurs when your cluster attempts to use more A4X sub-blocks than you have reserved, which happens when the number of VMs in your nodeset isn't a multiple of 18. Because Compute Engine provisions A4X capacity in indivisible sub-blocks to create 18 VMs, any remaining capacity in a sub-block can't be used by other nodesets in your cluster.

**Error messages** : You might receive one of the following error messages:
    
    
    ZONE_RESOURCE_POOL_EXHAUSTED
    
    
    
    ZONE_RESOURCE_POOL_EXHAUSTED_WITH_DETAILS
    

**Resolution** : Modify your cluster so that the total number of VMs for each nodeset with A4X VMs is a multiple of 18. This total is the sum of the static node count and the dynamic node count. For instructions, see [Modify a cluster](https://docs.cloud.google.com/cluster-director/docs/manage/modify-cluster).

## Resolve errors for incompatible machine types

This error occurs when you specify a C4A machine type for a login node in a cluster with compute nodes that aren't Arm-based. This error also occurs when you specify an unsupported `-lssd` or `-metal` variant of a C4A machine type for a login node.

**Error messages** : You might receive one of the following error messages:
    
    
    INCOMPATIBLE_LOGIN_NODE_MACHINE_TYPE
    
    
    
    The machine type "LOGIN_NODE_MACHINE_TYPE" for the Slurm login node is not supported with compute resource "COMPUTE_RESOURCE_NAME" of machine type "COMPUTE_MACHINE_TYPE". C4A login nodes are only supported with ARM-based compute nodes (such as A4X).
    
    
    
    The machine type "LOGIN_NODE_MACHINE_TYPE" is not supported for the Slurm login node. The lssd and metal variants of C4A machine types are not supported for the login node.
    

**Resolution** : Select a machine type for your login nodes that matches the architecture of your compute nodes:

  * If your compute nodes use the A4X Max or A4X machine series, then specify a [C4A machine type](https://docs.cloud.google.com/cluster-director/docs/cpu-machines#c4a-series).

  * If your compute nodes use the A4, A3 Ultra, A3 Mega, TPU7x, TPU v6e, TPU v5p, or N2 machine series, then specify an [N2 machine type](https://docs.cloud.google.com/cluster-director/docs/cpu-machines#n2-series).




## Resolve Slurm controller version errors

This section describes common errors that occur when you specify the Slurm version for the controller node as you create or modify a cluster. For more information about Slurm controller versions, see [Slurm controller versions in Cluster Director](https://docs.cloud.google.com/cluster-director/docs/slurm-controller-versions).

### Resolve incompatible OS image errors

This error occurs when you create a nodeset with an OS image that requires a newer Slurm version than the version that the controller node runs.

**Error message** : You might receive the following error message:
    
    
    The cluster is running Slurm CONTROLLER_VERSION. Please select a compatible compute image (Slurm CONTROLLER_VERSION or older).
    

**Resolution** : Compute nodes can't run a newer Slurm version than the controller node. To resolve this error, do one of the following:

  * If your workload requires the newer OS image, then create a new cluster with the required Slurm controller version. For instructions, see [Create a custom cluster](https://docs.cloud.google.com/cluster-director/docs/create/custom-cluster).

  * If you want to keep the current controller version, then modify the nodeset to use an OS image that supports the controller version of your cluster. For instructions, see [Modify a cluster](https://docs.cloud.google.com/cluster-director/docs/manage/modify-cluster).




### Resolve unsupported version errors

This error occurs when you specify an invalid version format or an unsupported Slurm controller version when you create a cluster.

**Error messages** : You might receive one of the following error messages:
    
    
    Unsupported controller version.
    
    
    
    Controller version must be in the format 'ab.cd' (e.g., '25.05'), found 'VERSION'.
    

**Resolution** : Specify a supported Slurm controller version in `ab.cd` format; specifically, specify `26.05` or `25.05`.

### Resolve errors when you update the controller version

This error occurs when you modify the Slurm controller version of an existing cluster.

**Error message** : You might receive the following error message:
    
    
    Updating the Slurm controller version is not currently supported.
    

**Resolution** : The Slurm controller version is immutable after you create the cluster. If your workload requires a different Slurm controller version, then create a new cluster with the required version.

## Resolve storage pool errors

This section describes errors that you might encounter when you use [Hyperdisk pools](https://docs.cloud.google.com/compute/docs/disks/storage-pools) or [Hyperdisk Exapools](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-exapools) for node boot disks in your cluster.

### Resolve storage pool zone mismatches

This error occurs when the storage pool that you specify resides in a different zone than the zone of the compute node or login node that uses it.

**Error message** : You might receive the following error message:
    
    
    The storage pool "STORAGE_POOL" is located in zone "STORAGE_ZONE", but the boot disk is located in zone "COMPUTE_ZONE". The storage pool must be located in the same zone as the boot disk.
    

**Resolution** : Verify that your storage pool and your compute resources reside in the same zone. If your compute resources reside in a different zone, then specify a storage pool in that zone or recreate the storage pool in the correct zone.

### Resolve errors for mismatched boot disk or storage pool types

This error occurs when you specify a storage pool for a boot disk, but you attempt to specify a boot disk type other than Hyperdisk Balanced, or specify an unsupported storage pool type.

**Error message** : You might receive the following error message:
    
    
    Boot disk type must be hyperdisk-balanced when a storage pool is specified.
    

**Resolution** : Verify that the boot disk is Hyperdisk Balanced, or that the storage pool is a Hyperdisk storage pool or a Hyperdisk Exapool.

### Resolve storage pool capacity or IOPS exhaustion

This error occurs when the boot disks in your cluster nodesets exceed the provisioned capacity, provisioned input/output operations per second (IOPS), or maximum overprovisioning ratio of the storage pool. When this error occurs, Cluster Director fails to create the compute instance.

**Error messages** : You might receive one of the following error messages:
    
    
    HttpError 400: Storage pool provisioned IOPS limit exceeded.
    
    
    
    UNSUPPORTED_OPERATION: Cannot allocate disk from storage pool.
    

**Resolution** : To resolve this error, complete the following steps:

  1. Verify the provisioned capacity and IOPS for your storage pool. For instructions, see [Analyze the provisioned IOPS and throughput for Hyperdisk volumes](https://docs.cloud.google.com/compute/docs/disks/analyze-iops-hyperdisk).

  2. Verify that the combined requirements for boot disks (minimum 40 GB per node) across all static and dynamic nodes stay within your storage pool limits.

  3. If necessary, then increase the provisioned capacity or IOPS for your storage pool. You can update capacity once every 12 hours. For instructions, see [Modify a storage pool](https://docs.cloud.google.com/compute/docs/disks/manage-storage-pools#modify-sp).




## Resolve TPU node and job errors

This section describes how to resolve errors when you provision TPU nodes or submit Slurm jobs to TPU partitions.

### Reset unresponsive TPU nodes

If you submit a Slurm job with an invalid configuration or if a node fails to provision, then TPU nodes might become unresponsive.

**Resolution** : To cancel pending jobs and reset the affected TPU nodes, complete the following steps:

  1. To check whether a TPU node encountered an error when Cluster Director provisioned a VM, [view the cluster details](https://docs.cloud.google.com/cluster-director/docs/manage/view-clusters#describe).

  2. If you haven't already, then [connect to a login node in your cluster](https://docs.cloud.google.com/cluster-director/docs/manage/connect-to-cluster#login).

  3. To view the jobs in the Slurm queue, use the [`squeue` command](https://slurm.schedmd.com/squeue.html):
         
         squeue
         

  4. If an unresponsive or misconfigured job is in the queue, then cancel the job by using the [`scancel` command](https://slurm.schedmd.com/scancel.html):
         
         scancel JOB_ID
         

Replace `JOB_ID` with the ID of the job from the `squeue` output.

  5. To recover the unresponsive TPU node and reset its state, [delete the node](https://docs.cloud.google.com/cluster-director/docs/workloads/configure-slurm#power-down-nodes).




### Resolve errors for mismatched TPU job topologies

This issue occurs when a Slurm job that you submit to a TPU partition fails immediately or remains pending because the requested topology or node count doesn't match the TPU slice requirements.

**Resolution** : Verify that the command that submits your job meets the submission requirements. For more information, see [Submit jobs on TPU VMs](https://docs.cloud.google.com/cluster-director/docs/workloads/configure-slurm#submit-tpu-jobs).

## What's next

If you can't find a solution to your problem in this documentation, then see [Get support](https://docs.cloud.google.com/cluster-director/docs/get-support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 

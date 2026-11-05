---
url: https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template/
title: Create an AI-optimized cluster based on a template \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T23:29:00.337199+00:00
---

# Create an AI-optimized cluster based on a template  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Create an AI-optimized cluster based on a template Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create a cluster in Cluster Director by using a pre-configured template that is optimized for running artificial intelligence (AI) and machine learning (ML) training workloads.

Cluster Director provides a set of templates that are pre-configured for most AI and ML training workloads. Each template specifies a set of optimized compute, networking, and storage resources that are designed for high reliability and resiliency. This approach helps you provision a cluster and maintain the flexibility to make changes if your workload needs them.

To create a fully customized cluster, see instead [Create a custom cluster](https://docs.cloud.google.com/cluster-director/docs/create/custom-cluster).

## Limitations

When you create a cluster in Cluster Director, the following limitations apply:

  * **Zonal scope** : all cluster resources must exist within the same zone. You can only create or use compute resources, storage resources, and subnetworks that exist within the same zone as your cluster. Cluster Director doesn't support AI zones, which are zones with names that contain `-ai` after the region name (for example, `us-central1-ai1a`). 
  * **Compute resource configuration per nodeset** : you can specify only one compute resource configuration for each nodeset in your cluster. Additionally, a cluster partition that contains a TPU nodeset can't contain GPU or CPU nodesets, and can't combine static and dynamic TPU nodesets. 
  * **Storage classes for new Cloud Storage buckets** : if you plan to add new Cloud Storage buckets to your cluster, then you can specify only the Rapid storage class, Standard storage class, or Autoclass. If you want to use other storage classes, then you must update your buckets after you create them. For instructions, see [Change object storage classes](https://docs.cloud.google.com/storage/docs/changing-storage-classes). **Caution** : You can't change the storage class of a Rapid bucket after you create it. Rapid buckets are zonal resources and must always use the Rapid storage class. 
  * **Slurm controller version** : compute nodes can't run a newer Slurm version than the controller node. For example, if the controller node in your cluster uses Slurm 25.05, then your compute nodes can't use an OS image that requires Slurm 26.05. To check the Slurm version of an OS image, see [Supported OS images](https://docs.cloud.google.com/cluster-director/docs/os-images#included-software). 
  * **Hyperdisk pools** : if you plan to use storage pools for node boot disks, then you can use only existing storage pools or Hyperdisk Exapools that use Hyperdisk Balanced volumes. Storage pools must reside in the same project and zone as the nodes that use them. 



## Templates for AI-optimized clusters

The following table describes the templates that you can use to create AI-optimized clusters in Cluster Director. When you create your cluster, you can either use the pre-configured settings in the template, or edit one or more settings based on the demands of your workloads.

Name | Description | Consumption option | Use cases  
---|---|---|---  
Large-scale model training with A3 Ultra | 

  * **Compute nodes** : 4 A3 Ultra VMs
  * **Storage** : 
    * 1 5 TiB basic SSD Filestore instance
    * 1 36 TiB Managed Lustre instance
  * **Login nodes** : 1 N2 VM

| 

  * Future reservations for more than 90 days (for capacity blocks)
  * Future reservations for up to 90 days (in calendar mode)

| This template is optimized for large-scale AI or ML training workloads.  
High-performance training with A4X | 

  * **Compute nodes** : 18 A4X VMs
  * **Storage** : 1 36 TiB and a 1,000 MBps/TiB tier Managed Lustre instance
  * **Login nodes** : 1 C4A VM

| Future reservations for capacity blocks | This template is optimized for compute-intensive and memory-intensive workloads, such as multimodal inference workloads, and for the fastest reads and writes.  
Short-term training and experimentation with A4 | 

  * **Compute nodes** : 4 A4 VMs
  * **Storage** : 
    * 1 2 TiB basic SSD Filestore instance
    * 1 18 TiB Managed Lustre instance
  * **Login nodes** : 1 N2 VM

| Flex-start | This template is optimized for running pre-training, fine-tuning, and experimentation workloads for up to seven days.  
Training and batch inference with TPU v6e (Preview) | 

  * **Compute nodes** : 64 TPU v6e VMs
  * **Storage** : 1 18 TiB and a 500 MBps/TiB tier Managed Lustre instance
  * **Login nodes** : 1 N2 VM

| 

  * Future reservations for more than 90 days (for capacity blocks)
  * Future reservations for up to 90 days (in calendar mode)
  * Flex-start
  * Spot
  * On-demand

| This template is optimized for training, fine-tuning, and running batch inference on transformer, text-to-image, and convolutional neural network (CNN) models.  
  
## Before you begin

Before you create a cluster in Cluster Director, do the following:

  1. **Choose consumption options**. If you haven't already, then you must choose the consumption options for the VMs that you want to use in each partition for your cluster. Each consumption option determines the availability, obtainability, and pricing for your VMs.

To learn more, see [Choose a consumption option](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option).

  2. **Obtain capacity and quota**. Based on your chosen consumption option, review the quota requirements for the VMs that you want to create in the cluster. If you lack sufficient quota, then creating your cluster fails.

To learn more, see [Capacity and quota overview](https://docs.cloud.google.com/cluster-director/docs/obtain-capacity).

  3. **Verify usable reservations**. If you want to create your cluster by using one or more reservations, then verify that the reservations have enough available resources to create your chosen number of VMs in the cluster. Otherwise, skip this step.

To learn more, see [Consumable VMs in a reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-view#number-instances-reservation).

  4. **Verify trusted image policy**. If the organization in which your project exists has a trusted image policy (`constraints/compute.trustedImageProjects`), then verify that the `clusterdirector-public-images` project is included in the list of allowed projects.

To learn more, see [Setting up trusted image policies](https://docs.cloud.google.com/compute/docs/images/restricting-image-access).

  5. **Verify existing resource requirements**. If you plan to use existing storage or networking resources in your cluster instead of creating new ones, then you must verify that those resources are correctly configured. Otherwise, skip this step.

To learn more, see [Cluster creation process overview](https://docs.cloud.google.com/cluster-director/docs/create/process-overview).




### Required roles

To get the permissions that you need to create a cluster based on a template, ask your administrator to grant you the following IAM roles: 

  * To create and manage a cluster: [Cluster Director Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.editor) (`roles/hypercomputecluster.editor`) on your project 
  * To manage resources in a cluster: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on your project 
  * To connect to the login node in a cluster: 
    * [Compute OS Login ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.osLogin) (`roles/compute.osLogin`) on your project
    * [IAP-Secured Tunnel User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.tunnelResourceAccessor) (`roles/iap.tunnelResourceAccessor`) on your project
    * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the Compute Engine default service account



These predefined roles contain the permissions required to create a cluster based on a template. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a cluster based on a template:

  * To create a cluster: `hypercomputecluster.clusters.create`
  * To check the status of the cluster creation operation: `hypercomputecluster.operations.get`
  * To view the details of a cluster: `hypercomputecluster.clusters.get`
  * To connect to the login node in a cluster: 
    * `compute.instances.osLogin`
    * `iap.tunnelInstances.accessViaIAP`
    * `iam.serviceAccounts.actAs`



To ensure that the Compute Engine default service account has the necessary permissions to create a cluster based on a template, ask your administrator to grant the following IAM roles to the Compute Engine default service account on your project: 

**Important:** You must grant these roles to the Compute Engine default service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * [Logs Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`)
  * [Monitoring Metric Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter) (`roles/monitoring.metricWriter`)
  * [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the Compute Engine default service account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create an AI-optimized cluster based on a template

**Preview — Create a cluster with TPU VMs**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To create an AI-optimized cluster based on a template, complete the following steps:

  1. Configure compute resource configurations

  2. Configure network

  3. Configure storage resources

  4. Configure the Slurm environment




### Configure compute resource configurations

To configure compute resource configurations when you create a cluster, complete the following steps:

  1. In the Google Cloud console, go to the **Cluster Director** page.

[Go to Cluster Director](https://console.cloud.google.com/cluster-director/overview)

  2. Click add **Create cluster**.

  3. In the dialog that appears, click **Reference architecture**. The **Create a cluster** page opens.

  4. Select one of the available templates.

  5. Click **Customize**.

  6. In the **Name your cluster** section, in the **Cluster name** field, enter a name for your cluster. The name can contain up to 10 characters, and it can only use numbers or lowercase letters (`a`-`z`).

  7. To add information to the pre-configured compute resource configuration, or edit the number and type of compute instances that the configuration specifies, do the following:

     1. In the **Compute** section, click edit **Edit resource configuration**. The **Add resource configuration** pane appears.

     2. Optional: In the **Name** field, to change the name of the compute resource configuration, enter a new name.

     3. Optional: In the **Machine configuration** section, to change the number and type of compute instances that your cluster uses, follow the prompts to update the compute resources.

     4. In the **Consumption options** section, specify the consumption option that you want to use to obtain resources:

        * To create compute instances by using a reservation, do the following:

          1. Click the **Use reservation** tab.

          2. Click **Select reservation**. The **Choose a reservation** pane appears. If you want to use a reservation of A4X or TPU v6e VMs, or TPU7x VMs if you changed the machine type, then you can choose the [block](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#block) or [sub-block](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#sub-block) to control the placement of your VMs. For TPU VMs, the reservation must use the [all-capacity mode](https://docs.cloud.google.com/tpu/docs/all-capacity-overview).

          3. Select the reservation that you want to use. Then, click **Choose**. This action sets the **Region** and **Zone** of your compute resources.

        * To create Flex-start VMs, do the following:

          1. Click the **Flex start** tab.

          2. In the **Time limit for the VM** section, specify the run duration for the compute instances. The value must be between 10 minutes and 7 days.

          3. In the **Location** section, select the region where you want to create Flex-start VMs. The Google Cloud console filters the available regions to show those regions that support Flex-start VMs for your selected machine type.

        * To create Spot VMs, do the following:

          1. Click the **Use spot** tab.

          2. In the **On VM termination** list, select one of the following options:

             * To delete Spot VMs on preemption, select **Delete**. TPU Spot VMs support only **Delete**.

             * To stop GPU or CPU Spot VMs on preemption, select **Stop**.

          3. In the **Location** section, select the **Region** and **Zone** where you want to create Spot VMs. The Google Cloud console filters the available regions to show those regions that support Spot VMs for your selected machine type.

        * To create TPU on-demand instances, do the following:

          1. Click the **Use on-demand** tab.

          2. In the **Location** section, select the **Region** and **Zone** where you want to create on-demand instances.

     5. Click **Done**.

     6. Optional: To create additional compute resource configurations for a partition, click add **Add resource configuration** , and then follow the prompts to specify the compute resources.

  8. Click **Continue**.




### Configure network

In the **Network** section, to configure the network that your cluster uses, complete the following steps:

  1. In the **Choose a Virtual Private Cloud (VPC) network** section, do one of the following:

     * Recommended: To let Cluster Director automatically create a pre-configured VPC network for your cluster, do the following:

       1. Select **Create a new VPC network**.

       2. In the **Network name** field, enter a name for the VPC network.

     * To use an existing VPC or Shared VPC network, do the following:

       1. Select **Use a VPC network in the current project** or **Use a Shared VPC network hosted in another project**.

       2. In the **Select VPC network** or **Shared VPC network** list, select a VPC or Shared VPC network that meets the [required configurations](https://docs.cloud.google.com/cluster-director/docs/create/process-overview#existing-network).

       3. In the **Select subnetwork** list, select an existing subnetwork.

  2. Click **Continue**.




### Configure storage resources

In the **Storage** section, to configure the storage resources that your cluster uses, complete the following steps:

  1. Optional: To edit a storage resource, click edit **Edit storage plan** , and then follow the prompts to update the configuration of the storage resource.

  2. Optional: To add storage resources to your cluster, click add **Add storage configuration** , and then follow the prompts to specify the configuration for the storage resources.

**Tip:** If you want to use different Cloud Storage buckets for different projects or jobs, then you can mount the buckets on your cluster nodes for the duration of a Slurm job. This action lets you read or write data to Cloud Storage without permanently adding storage resources to your cluster. For more information, see [Mount Cloud Storage buckets for specific jobs](https://docs.cloud.google.com/cluster-director/docs/workloads/mount-buckets). 
  3. Click **Continue**.




### Configure the Slurm environment

To configure the Slurm environment in your cluster, complete the following steps:

  1. Optional: To edit the number of compute instances, machine type, or OS image for the login nodes, expand the **Login node** section. Then, follow the prompts to configure the login nodes.

  2. Optional: To edit partitions of your cluster to organize your compute resources, expand the **Partitions** section, and then do one of the following:

     * To add a partition, click add **Add partition** , and then do the following:

       1. In the **Partition name** field, enter a name for the partition.

       2. To edit a nodeset, click edit **Edit NODESET_NAME**. Otherwise, to add a nodeset, click add **Add nodeset**.

       3. In the **Nodeset name** field, enter a name for your nodeset.

       4. In the **Resource configuration** field, select a compute resource configuration that you created in the previous steps.

       5. In the **Image family** list, select an OS image family to use for the compute nodes in the nodeset. For more information about supported image families, see [Supported OS images for Cluster Director](https://docs.cloud.google.com/cluster-director/docs/os-images).

       6. Optional: In the **Image** list, select a specific OS image version. By default, the **Image** list selects the latest OS image version for the machine series specified in the nodeset.

       7. In the **Boot disk type** list and **Boot disk size** field, enter the type and size of the boot disk for the compute instances to use.

       8. Optional: To share disk capacity and performance across nodes in a nodeset, specify an existing Hyperdisk pool or Hyperdisk Exapool as follows:

          1. Select the **Enable storage pool** checkbox.

          2. In the **Select a storage pool** list, select a storage pool that uses Hyperdisk Balanced volumes.

       9. Configure the node counts for the nodeset:

          * For GPU or CPU nodesets, in the **Static node count** field, enter the minimum number of compute nodes that must run at all times. In the **Dynamic node count** field, enter the maximum number of additional compute nodes that Cluster Director can create when demand increases.

          * For TPU nodesets, in the **Node lifecycle** section, select one of the following options:

            * To provision TPU slices per job, select **Use dynamic scaling** , and then in the **Max number of dynamic nodes** field, enter the maximum number of dynamic TPU nodes.

            * To keep persistent TPU slices active between jobs, select **Use static nodes**. Then, in the **TPU topology** section that appears, select a slice topology and the number of slices.

       10. Optional: To specify more advanced configurations for the compute node, expand **Advanced nodeset settings**. Then, follow the prompts to add or remove startup scripts, or add or remove labels.

       11. Click **Done**.

     * To remove a partition, click delete **Delete partition**.

  3. Optional: To add [prolog or epilog scripts](https://slurm.schedmd.com/prolog_epilog.html) to your Slurm environment, do the following:

     1. Expand the **Advanced orchestration settings** section.

     2. In the **Scripts** section, follow the prompts to add scripts.

  4. Click **Create**. The **Clusters** page appears.

Creating the cluster can take some time to complete. The completion time depends on the number of compute instances that you request and resource availability in the zone of the compute instances. If your requested resources are unavailable, then Cluster Director maintains the creation request until resources become available. When Cluster Director creates your login node, you can connect to your cluster; however, you can only run workloads when Cluster Director creates the compute nodes in your cluster.




## What's next

  * [Connect to a cluster](https://docs.cloud.google.com/cluster-director/docs/manage/connect-to-cluster)

  * [Review the node lifecycle](https://docs.cloud.google.com/cluster-director/docs/manage/node-lifecycle)

  * [Submit and monitor jobs with Slurm](https://docs.cloud.google.com/cluster-director/docs/workloads/configure-slurm)

  * [Modify a cluster](https://docs.cloud.google.com/cluster-director/docs/manage/modify-cluster)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 

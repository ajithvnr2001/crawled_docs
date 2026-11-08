---
url: https://docs.cloud.google.com/cluster-director/docs/create/process-overview/
title: Cluster creation process overview \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-08T09:17:46.991671+00:00
---

# Cluster creation process overview  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/create/process-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Cluster creation process overview Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to plan and configure the infrastructure for a cluster in Cluster Director. To meet the performance, capacity, and budget requirements of your artificial intelligence (AI), machine learning (ML), or high performance computing (HPC) workload, you must choose the compute, storage, network, and data protection resources that your cluster uses. You must also define how the Slurm orchestrator manages your cluster nodes.

## Cluster creation process

Creating a cluster involves configuring compute, storage, and networking resources, as well as the Slurm orchestrator. The following process helps you choose the configurations that best fit the needs of your workload:

  1. Configure compute resources

  2. Configure storage resources

  3. Configure networking resources

  4. Optional: Configure data protection

  5. Configure the Slurm orchestrator




If you want an interactive planning session before you configure resources, then run the following prompt in Compute Advisor:

agent_mode_2 Compute Advisor help_outline Compute Advisor is an AI-powered assistant that you can prompt to get customized recommendations for your infrastructure based on information such as your quota limits, existing reservations, and resource location constraints.

This prompt starts an interactive session to evaluate your project quotas and reservations, recommends machine configurations for your cluster, and outputs a summary table with recommended Google Cloud console settings. 

Act as a cloud architect. Help me design a cluster in Cluster Director based on my project quotas, existing reservations, and available regions.  
  
Start by asking me about my workload type (such as foundation model training, fine-tuning, or inference) and my target scale. After I provide my workload details, walk me through the five setup steps in this guide:  
  
1\. Configure compute resources: Recommend machine series for compute nodes (A4X, A4, A3 Ultra, A3 Mega, or N2), controller nodes (N2), and login nodes (C4A or N2), a deployment region and zone, and a consumption option (future reservations for capacity blocks, future reservations in calendar mode, Flex-start, Spot, or On-demand).  
  
2\. Configure storage resources: Recommend a new or existing Filestore or Google Cloud Managed Lustre instance for the shared /home directory, plus any optional Cloud Storage buckets.  
  
3\. Configure networking resources: Recommend whether to let Cluster Director create a new VPC network or to use an existing VPC or Shared VPC network with the required subnet, Private Google Access, health check (TCP port 8319), and IAP (TCP port 22) firewall rules.  
  
4\. Configure data protection (optional): Identify whether I need a VPC Service Controls service perimeter and list the required restricted APIs.  
  
5\. Configure the Slurm orchestrator: Recommend boot disk options for the controller and login nodes, and define the partitions and nodesets with static and dynamic node counts (using multiples of 18 VMs for A4X nodesets).  
  
Format the recommendations as a Markdown summary table for each step, followed by recommended Google Cloud console settings and next steps. expand_more
    
    
    Act as a cloud architect. Help me design a cluster in Cluster Director based on my project quotas, existing reservations, and available regions.
    
    Start by asking me about my workload type (such as foundation model training, fine-tuning, or inference) and my target scale. After I provide my workload details, walk me through the five setup steps in this guide:
    
    1. Configure compute resources: Recommend machine series for compute nodes (A4X, A4, A3 Ultra, A3 Mega, or N2), controller nodes (N2), and login nodes (C4A or N2), a deployment region and zone, and a consumption option (future reservations for capacity blocks, future reservations in calendar mode, Flex-start, Spot, or On-demand).
    
    2. Configure storage resources: Recommend a new or existing Filestore or Google Cloud Managed Lustre instance for the shared /home directory, plus any optional Cloud Storage buckets.
    
    3. Configure networking resources: Recommend whether to let Cluster Director create a new VPC network or to use an existing VPC or Shared VPC network with the required subnet, Private Google Access, health check (TCP port 8319), and IAP (TCP port 22) firewall rules.
    
    4. Configure data protection (optional): Identify whether I need a VPC Service Controls service perimeter and list the required restricted APIs.
    
    5. Configure the Slurm orchestrator: Recommend boot disk options for the controller and login nodes, and define the partitions and nodesets with static and dynamic node counts (using multiples of 18 VMs for A4X nodesets).
    
    Format the recommendations as a Markdown summary table for each step, followed by recommended Google Cloud console settings and next steps.

[ Edit and run prompt in Compute Advisor ](https://console.cloud.google.com/compute/advisor#prompt=Act%20as%20a%20cloud%20architect.%20Help%20me%20design%20a%20cluster%20in%20Cluster%20Director%20based%20on%20my%20project%20quotas%2C%20existing%20reservations%2C%20and%20available%20regions.%0A%0AStart%20by%20asking%20me%20about%20my%20workload%20type%20%28such%20as%20foundation%20model%20training%2C%20fine-tuning%2C%20or%20inference%29%20and%20my%20target%20scale.%20After%20I%20provide%20my%20workload%20details%2C%20walk%20me%20through%20the%20five%20setup%20steps%20in%20this%20guide%3A%0A%0A1.%20Configure%20compute%20resources%3A%20Recommend%20machine%20series%20for%20compute%20nodes%20%28A4X%2C%20A4%2C%20A3%20Ultra%2C%20A3%20Mega%2C%20or%20N2%29%2C%20controller%20nodes%20%28N2%29%2C%20and%20login%20nodes%20%28C4A%20or%20N2%29%2C%20a%20deployment%20region%20and%20zone%2C%20and%20a%20consumption%20option%20%28future%20reservations%20for%20capacity%20blocks%2C%20future%20reservations%20in%20calendar%20mode%2C%20Flex-start%2C%20Spot%2C%20or%20On-demand%29.%0A%0A2.%20Configure%20storage%20resources%3A%20Recommend%20a%20new%20or%20existing%20Filestore%20or%20Google%20Cloud%20Managed%20Lustre%20instance%20for%20the%20shared%20/home%20directory%2C%20plus%20any%20optional%20Cloud%20Storage%20buckets.%0A%0A3.%20Configure%20networking%20resources%3A%20Recommend%20whether%20to%20let%20Cluster%20Director%20create%20a%20new%20VPC%20network%20or%20to%20use%20an%20existing%20VPC%20or%20Shared%20VPC%20network%20with%20the%20required%20subnet%2C%20Private%20Google%20Access%2C%20health%20check%20%28TCP%20port%208319%29%2C%20and%20IAP%20%28TCP%20port%2022%29%20firewall%20rules.%0A%0A4.%20Configure%20data%20protection%20%28optional%29%3A%20Identify%20whether%20I%20need%20a%20VPC%20Service%20Controls%20service%20perimeter%20and%20list%20the%20required%20restricted%20APIs.%0A%0A5.%20Configure%20the%20Slurm%20orchestrator%3A%20Recommend%20boot%20disk%20options%20for%20the%20controller%20and%20login%20nodes%2C%20and%20define%20the%20partitions%20and%20nodesets%20with%20static%20and%20dynamic%20node%20counts%20%28using%20multiples%20of%2018%20VMs%20for%20A4X%20nodesets%29.%0A%0AFormat%20the%20recommendations%20as%20a%20Markdown%20summary%20table%20for%20each%20step%2C%20followed%20by%20recommended%20Google%20Cloud%20console%20settings%20and%20next%20steps.&origin=cluster_director_process_overview)

### Configure compute resources

You must choose the type and number of Compute Engine instances that you want to create in your cluster. You must consider the following:

  * **Machine series** : you must choose the machine series and types that you want to create in your cluster. Each cluster partition can use a different machine series. Each compute instance in your cluster serves as a node. For each type of node, Google recommends the following machine series:

    * **Compute nodes** : based on your workload and the machine series that Cluster Director supports, see one of the following:

      * [Ideal use cases for GPU instances](https://docs.cloud.google.com/docs/compute-area/gpus#ideal-use-cases)

      * [Ideal use cases for TPU instances](https://docs.cloud.google.com/docs/compute-area/tpus#ideal-use-cases)

    * **Controller nodes** : N2 machine series

    * **Login nodes** : C4A or N2 machine series

  * **Location** : based on the locations where your chosen machine series are available, you must select the region and zone where you want to deploy your cluster. All compute, storage, and subnetwork resources in your cluster must exist within the same zone. Cluster Director doesn't support AI zones, which are zones with names that end in `-ai`. For more information, see [Cluster Director locations](https://docs.cloud.google.com/cluster-director/docs/locations).

  * **Consumption option** : you must choose the _consumption option_ that you want to use to get and use compute resources. Each option affects the availability, obtainability, and pricing of a compute resource. For more information, see [Choose a consumption option](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option).




### Configure storage resources

You must define the storage that your cluster uses:

  * **Shared file system for`/home` directory**: a Slurm cluster requires a [Filestore instance](https://docs.cloud.google.com/filestore/docs/overview) or [Managed Lustre instance](https://docs.cloud.google.com/managed-lustre/docs/overview) for the shared `/home` directory. When you create a cluster, you can do one of the following:

    * Let Cluster Director create a new Filestore or Managed Lustre instance with pre-configured settings.

    * Use an existing Filestore or Managed Lustre instance on the same VPC network as your cluster.

If you use the [Dynamic tier](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers#dynamic_tier) for Managed Lustre, then your cluster must use an existing VPC network that has the `dynamic_tier_capacity` quota allocated.

  * **Additional storage** : for large-scale AI workloads that require more storage, you can add other solutions—for example, [Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/introduction). If you create new Cloud Storage buckets when you create your cluster, then you can specify only the Rapid storage class, Standard storage class, or Autoclass. If you want to use other storage classes, then you must update your buckets after you create them. For instructions, see [Change object storage classes](https://docs.cloud.google.com/storage/docs/changing-storage-classes).

**Caution:** You can't change the storage class of a Rapid bucket after you create it. Rapid buckets are zonal resources and must always use the Rapid storage class.



### Configure networking resources

To define the networking resources that your cluster uses, choose one of the following options:

  * Create a new VPC network

  * Use an existing VPC or Shared VPC network




#### Create a new VPC network

If you want the cluster to use a new VPC network, then Cluster Director creates the network on your behalf. Cluster Director automatically configures the necessary firewall rules to let you connect to your cluster.

#### Use an existing VPC or Shared VPC network

To use an existing VPC or Shared VPC network in your cluster, you must configure the network and subnetwork as follows:

  * You must enable Private Google Access in your network. For instructions, see [Private Google Access configuration](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).

  * You must configure firewall rules that allow the following:

    * [SSH connections to VMs](https://docs.cloud.google.com/firewall/docs/using-firewalls#common-use-cases-allow-ssh)

    * [Internal ingress connections among VMs](https://docs.cloud.google.com/firewall/docs/using-firewalls#common-use-cases-allow-internal)

  * You must configure the subnetwork as follows:

    * The subnetwork must allow health checks by using the TCP protocol and port `8319`. For more information, see [Use health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks).

    * The subnetwork must have a firewall rule that allows Identity-Aware Proxy (IAP) to access the VMs by using the TCP protocol on port `22`. For more information, see [Prepare your project for IAP TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding#preparing_your_project_for_tcp_forwarding).

    * The subnetwork can't overlap with the following IPv4 address ranges:

      * `10.20.1.0/28`

      * `10.0.0.0/17`

      * `192.168.64.0/18`

      * `192.168.128.0/18`

  * If you want to use a Shared VPC network, then you must also do the following:

    * [Configure private services access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access).

    * Enable the Cloud DNS API in the network's host project.

    * Grant the following IAM roles either at the host project level or the subnetwork level:

      * **Grant access to all subnets in the host project** : grant the following IAM roles:

        * The [Compute Network User (`roles/compute.networkUser`) role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser) to the [Google APIs Service Agent](https://docs.cloud.google.com/iam/docs/service-account-types#google-apis-service-agent)

        * The [Hypercompute Shared VPC Service Agent (`roles/hypercomputecluster.sharedVpcServiceAgent`) role](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.sharedVpcServiceAgent) to the Cluster Director Service Agent (`service-PROJECT_NUMBER@gcp-sa-hypercomputecluster.iam.gserviceaccount.com`)

      * **Grant access to specific subnets** : if your organization's policies require more granular control, then use this option. Grant the following IAM roles:

        * The [Compute Network User (`roles/compute.networkUser`) role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser) on the subnetwork to the [Google APIs Service Agent](https://docs.cloud.google.com/iam/docs/service-account-types#google-apis-service-agent) and Cluster Director Service Agent (`service-PROJECT_NUMBER@gcp-sa-hypercomputecluster.iam.gserviceaccount.com`)

        * The [Compute Network Viewer (`roles/compute.networkViewer`) role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkViewer) on the network's host project to the Cluster Director Service Agent (`service-PROJECT_NUMBER@gcp-sa-hypercomputecluster.iam.gserviceaccount.com`)

        * A custom role that includes the `dns.managedZones.get`, `dns.managedZones.list`, `dns.networks.bindPrivateDNSZone`, and `dns.networks.targetWithPeeringZone` permissions on the network's host project to the Cluster Director Service Agent (`service-PROJECT_NUMBER@gcp-sa-hypercomputecluster.iam.gserviceaccount.com`)

For more information about setting up a Shared VPC network, see [Set up Shared VPC](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#set-up-shared-vpc).




### Optional: Configure data protection

If you want to help prevent sensitive data in your cluster from being copied to unauthorized sources, then use VPC Service Controls. Otherwise, skip this section. [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) lets you control communication to and among services that Google manages. To use Cluster Director with VPC Service Controls, you must create a security boundary around your resources. Google then creates a service perimeter to manage this boundary.

To create a service perimeter, follow the instructions on [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) and specify the following configurations:

  * **Perimeter resources (`perimeterResources`)**: include the project in which you want to create your cluster. If you want to use an existing Shared VPC network in your cluster, then you must also include the host project of that network.

  * **Restricted services (`restrictedServices`)**: include the following APIs:

    * Compute Engine API (`compute.googleapis.com`)

    * Filestore API (`file.googleapis.com`)

    * Hypercompute Cluster API (`hypercomputecluster.googleapis.com`)

    * Cloud Logging API (`logging.googleapis.com`)

    * Google Cloud Managed Lustre API (`lustre.googleapis.com`)

    * Cloud Monitoring API (`monitoring.googleapis.com`)




After you create the service perimeter, it can take up to 30 minutes for the changes to take effect. After that time, the service perimeter applies to any cluster that you create in your project.

### Configure the Slurm orchestrator

For the final step, you must configure the Slurm orchestrator. To configure the orchestrator, you define the following components:

  * **Login and controller nodes** : you must define the machine series and boot disk options for the login and controller nodes, as well as the Slurm controller version:

    * **Slurm controller version** : when you create a cluster by using the Google Cloud CLI or the REST API, you can specify the [Slurm controller version](https://docs.cloud.google.com/cluster-director/docs/slurm-controller-versions); you can't modify the controller version for an existing cluster. Compute nodes can't run a newer Slurm version than the controller node. For example, if the controller node in your cluster uses Slurm 25.05, then your compute nodes can't use an OS image that requires Slurm 26.05. To check the Slurm version of an OS image, see [Supported OS images](https://docs.cloud.google.com/cluster-director/docs/os-images#included-software).

    * **Boot disks and Hyperdisk pools** : controller nodes require standalone boot disks. For login nodes and compute nodes, you can specify [standalone boot disks or Hyperdisk pools](https://docs.cloud.google.com/cluster-director/docs/storage#boot-disk-storage) if your selected machine series supports Hyperdisk. If you use storage pools for node boot disks, then you can use only existing storage pools or Hyperdisk Exapools that use Hyperdisk Balanced volumes. Storage pools must reside in the same project and zone as the nodes that use them.

  * **Partitions and nodesets** : you must define how you want to group your compute resources. Each partition can contain one or more nodesets, letting you create different pools of resources for different types of jobs. Each nodeset and partition must meet the following requirements:

    * You can specify only one compute resource configuration for each nodeset in your cluster.

    * If you create A4X VMs in a nodeset, then the total number of A4X VMs in the nodeset must be a multiple of 18. This total is the sum of the static node count and the dynamic node count. Because Compute Engine provisions A4X capacity in indivisible sub-blocks of 18 VMs, nodesets can't share unused capacity.

    * If you create TPU instances in a nodeset, then you can configure either a static node count or a dynamic node count, not both. For a static TPU nodeset, you must specify an accelerator topology, and the static node count must be a multiple of the number of VMs per slice in that topology.

    * A Slurm partition that contains a TPU nodeset can't contain GPU or CPU nodesets, and can't combine static and dynamic TPU nodesets.




## What's next

  * [Try out Cluster Director](https://docs.cloud.google.com/cluster-director/docs/create/quickstart)

  * [Choose a consumption option](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-06 UTC."],[],[]] 

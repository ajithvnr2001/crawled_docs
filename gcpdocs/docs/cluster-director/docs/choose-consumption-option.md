---
url: https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option/
title: Choose a consumption option \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-08T09:17:48.003851+00:00
---

# Choose a consumption option  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Choose a consumption option Stay organized with collections  Save and categorize content based on your preferences. 

When you create a cluster in Cluster Director, you must select the _consumption option_ that you want to use to obtain resources (vCPUs, memory, GPUs, TPUs, and Local SSD disks) for creating Compute Engine instances. Each consumption option defines the availability, lifespan, and cost of your requested resources. This document compares the available consumption options, and it helps you choose the option that best fits your workload and cost needs.

## Compare consumption options

**Note:** Support for TPU VMs in Cluster Director is in [Preview](https://cloud.google.com/products#product-launch-stages).

The following table compares the supported machine types, lifespans, capacity assurance levels, pricing models, and reservation requirements for each consumption option:

Consumption option | Future reservations for capacity blocks | Future reservations in calendar mode (up to 90 days) | Flex-start | Spot | On-demand  
---|---|---|---|---|---  
**Supported machines** | A4X Max, A4X, A4, A3 Ultra, A3 Mega, TPU7x*, TPU v6e, TPU v5p | A4, A3 Ultra, A3 Mega, TPU7x*, TPU v6e, TPU v5p | A4, A3 Ultra, A3 Mega, TPU7x*, TPU v6e, TPU v5p | A4, A3 Ultra, A3 Mega, TPU7x*, TPU v6e, TPU v5p, N2 | C4A, N2, TPU7x, TPU v6e, TPU v5p  
**Lifespan** | Unlimited | 90 days maximum | 7 days maximum | Unlimited (but subject to [preemption](https://docs.cloud.google.com/compute/docs/instances/spot#preemption)) | Unlimited  
**Capacity assurance** | Very high | Very high | Best-effort | Best-effort | Best-effort  
**Quota** | Google increases quota on your behalf | No quota is charged | [Preemptible quota](https://docs.cloud.google.com/compute/resource-usage#preemptible-quotas) is charged | [Preemptible quota](https://docs.cloud.google.com/compute/resource-usage#preemptible-quotas) is charged | Standard quota is charged  
**Pricing** | Discounted up to 53% ([accelerator pricing](https://docs.cloud.google.com/compute/vm-instance-pricing#accelerator-optimized), [TPU pricing](https://cloud.google.com/tpu/pricing)) | Discounted up to 53% ([DWS pricing](https://cloud.google.com/products/dws/pricing)) | Discounted up to 53% ([DWS pricing](https://cloud.google.com/products/dws/pricing)) | Deeply discounted up to 91% ([Spot pricing](https://cloud.google.com/spot-vms/pricing)) | Standard pricing ([VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing), [TPU pricing](https://cloud.google.com/tpu/pricing))  
**Billing model** | Charged for the reservation period ([reservation billing](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#reservation-billing)) | Charged for the reservation period ([reservation billing](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#reservation-billing)) | Pay-as-you-go (PAYG) | Pay-as-you-go (PAYG) | Pay-as-you-go (PAYG)  
**Resource allocation** | Dense (best-effort for TPU v5p) | Dense for GPU virtual machines (VMs), best-effort for TPU VMs | Best-effort | Best-effort | Best-effort  
[**Provisioning model**](https://docs.cloud.google.com/compute/docs/instances/provisioning-models) | Reservation-bound | Reservation-bound | Flex-start | Spot | Standard  
  
* To obtain TPU7x VMs with any consumption option except On-demand, you must contact your account team or the sales team to request access. 

If you want AI-powered assistance to compare consumption options, then run the following prompt in Compute Advisor:

agent_mode_2 Compute Advisor help_outline Compute Advisor is an AI-powered assistant that you can prompt to get customized recommendations for your infrastructure based on information such as your quota limits, existing reservations, and resource location constraints.

This prompt evaluates your project quotas and reservations, compares capacity assurance, lifespan, and discounts across consumption options, and outputs a Markdown comparison table with recommended partition configurations. 

Act as a cloud architect. Help me choose the best consumption option and provisioning model for each partition in my Cluster Director cluster based on my project quotas, existing reservations, and available regions. Walk me through the following steps:  
  
1\. Compare the five consumption options (future reservations for capacity blocks, future reservations in calendar mode, Flex-start, Spot, and On-demand) across supported machine series, lifespan, capacity assurance, quota type (standard or preemptible), pricing discounts, billing model, and resource allocation.  
  
2\. Evaluate regional and zonal availability for GPU machine series (A4X Max, A4X, A4, A3 Ultra, and A3 Mega) and CPU machine series (N2 for compute or controller nodes, and C4A or N2 for login nodes).  
  
3\. Recommend a consumption option and provisioning model (reservation-bound, flex-start, spot, or standard) for each cluster partition based on whether my workload needs high assurance, capacity for more than 90 days, reserved capacity for up to 90 days, a run duration of up to 7 days, or fault-tolerant Spot capacity.  
  
Format the recommendations as a Markdown comparison table for my Slurm partitions and nodesets, followed by the steps to reserve capacity and create the cluster. expand_more
    
    
    Act as a cloud architect. Help me choose the best consumption option and provisioning model for each partition in my Cluster Director cluster based on my project quotas, existing reservations, and available regions. Walk me through the following steps:
    
    1. Compare the five consumption options (future reservations for capacity blocks, future reservations in calendar mode, Flex-start, Spot, and On-demand) across supported machine series, lifespan, capacity assurance, quota type (standard or preemptible), pricing discounts, billing model, and resource allocation.
    
    2. Evaluate regional and zonal availability for GPU machine series (A4X Max, A4X, A4, A3 Ultra, and A3 Mega) and CPU machine series (N2 for compute or controller nodes, and C4A or N2 for login nodes).
    
    3. Recommend a consumption option and provisioning model (reservation-bound, flex-start, spot, or standard) for each cluster partition based on whether my workload needs high assurance, capacity for more than 90 days, reserved capacity for up to 90 days, a run duration of up to 7 days, or fault-tolerant Spot capacity.
    
    Format the recommendations as a Markdown comparison table for my Slurm partitions and nodesets, followed by the steps to reserve capacity and create the cluster.

[ Edit and run prompt in Compute Advisor ](https://console.cloud.google.com/compute/advisor#prompt=Act%20as%20a%20cloud%20architect.%20Help%20me%20choose%20the%20best%20consumption%20option%20and%20provisioning%20model%20for%20each%20partition%20in%20my%20Cluster%20Director%20cluster%20based%20on%20my%20project%20quotas%2C%20existing%20reservations%2C%20and%20available%20regions.%20Walk%20me%20through%20the%20following%20steps%3A%0A%0A1.%20Compare%20the%20five%20consumption%20options%20%28future%20reservations%20for%20capacity%20blocks%2C%20future%20reservations%20in%20calendar%20mode%2C%20Flex-start%2C%20Spot%2C%20and%20On-demand%29%20across%20supported%20machine%20series%2C%20lifespan%2C%20capacity%20assurance%2C%20quota%20type%20%28standard%20or%20preemptible%29%2C%20pricing%20discounts%2C%20billing%20model%2C%20and%20resource%20allocation.%0A%0A2.%20Evaluate%20regional%20and%20zonal%20availability%20for%20GPU%20machine%20series%20%28A4X%20Max%2C%20A4X%2C%20A4%2C%20A3%20Ultra%2C%20and%20A3%20Mega%29%20and%20CPU%20machine%20series%20%28N2%20for%20compute%20or%20controller%20nodes%2C%20and%20C4A%20or%20N2%20for%20login%20nodes%29.%0A%0A3.%20Recommend%20a%20consumption%20option%20and%20provisioning%20model%20%28reservation-bound%2C%20flex-start%2C%20spot%2C%20or%20standard%29%20for%20each%20cluster%20partition%20based%20on%20whether%20my%20workload%20needs%20high%20assurance%2C%20capacity%20for%20more%20than%2090%20days%2C%20reserved%20capacity%20for%20up%20to%2090%20days%2C%20a%20run%20duration%20of%20up%20to%207%20days%2C%20or%20fault-tolerant%20Spot%20capacity.%0A%0AFormat%20the%20recommendations%20as%20a%20Markdown%20comparison%20table%20for%20my%20Slurm%20partitions%20and%20nodesets%2C%20followed%20by%20the%20steps%20to%20reserve%20capacity%20and%20create%20the%20cluster.&origin=cluster_director_consumption)

## Choose a consumption option

Use the following flowchart to choose the consumption option that best fits the type of partition for your cluster:

[ ![Decision flowchart that maps capacity assurance, duration,
       reservation, and fault-tolerance requirements to Cluster Director
       consumption options: future reservations for capacity blocks, future
       reservations in calendar mode, Spot, Flex-start, and On-demand.](https://docs.cloud.google.com/static/cluster-director/images/consumption-options.png)](https://docs.cloud.google.com/static/cluster-director/images/consumption-options.png)

The questions in the preceding diagram are the following:

  1. Do you want high assurance for GPU or TPU instances?

     * **Yes** : go to question 2.

     * **No** : skip to question 4.

  2. Do you need capacity for more than 90 days?

     * **Yes** : see Use future reservations for capacity blocks.

     * **No** : go to question 3.

  3. Do you want reserved capacity?

     * **Yes** : see Use future reservations in calendar mode.

     * **No** : go to question 4.

  4. Is your workload fault-tolerant?

     * **Yes** : see Use Spot.

     * **No** : go to question 5.

  5. Is your workload running for 7 days or less?

     * **Yes** : see Use Flex-start.

     * **No** : see Use On-demand.




### Use future reservations for capacity blocks

To run long-running, large-scale distributed workloads that require densely allocated resources, you can reserve vCPUs, memory, GPUs, TPUs, Local SSD disks, and a [Hyperdisk pool](https://docs.cloud.google.com/compute/docs/disks/pools) for a future period. If Google approves your request, then you have exclusive access to your reserved resources for that period of time, and you can use the resources to create clusters. At the end of the reservation period, Compute Engine does the following:

  * Compute Engine deletes the reservation and any associated empty Hyperdisk pool.

  * Compute Engine deletes any compute instances in your cluster that use the reservation.

**Caution:** When the reservation that you used to create a compute instance reaches its end time, Cluster Director deletes the instance. To prevent data loss, back up your data by using one of the [data protection options for disks and instances](https://docs.cloud.google.com/compute/docs/disks/data-protection).



#### Ideal workloads for future reservations for capacity blocks

Future reservations for capacity blocks are ideal for the following workloads:

  * Pre-training foundation models

  * Inference for foundation models across multiple hosts




#### Characteristics of future reservations for capacity blocks

Future reservations for capacity blocks have the following characteristics:

  * You can reserve A4X Max, A4X, A4, A3 Ultra, A3 Mega, TPU7x, TPU v6e, and TPU v5p machine types, as well as Hyperdisk pools. For GPU, TPU7x, and TPU v6e VMs, Google allocates compute nodes in close physical proximity to minimize network latency, and co-locates Hyperdisk pools with those compute nodes to optimize storage performance.

**Note:** To reserve TPU7x VMs with future reservations for capacity blocks, you must contact your account team or the sales team to request access.
  * You can reserve as many compute instances as you want for as long as you want. For any compute instances that you want to reserve for a year or longer, you need to purchase and attach a [resource-based commitment](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments) to your reserved resources. Then, you can use the reserved resources to create and run compute instances until the end of the reservation period.

  * You use the reservation-bound provisioning model to create compute instances, which has the following benefits:

    * You have a higher chance to obtain GPUs or TPUs.

    * In addition to the commitment that is attached to your compute instances, you get a discount up to 53% for vCPUs, memory, GPUs, TPUs, and any attached Local SSD disks. If you reserve resources for 365 days or longer, then you also get discounts for Hyperdisk pools.




#### How to use future reservations for capacity blocks

To use future reservations for capacity blocks to create clusters, you must complete the following steps:

  1. **Request to reserve capacity**. Contact your account team and specify the compute instances and Hyperdisk pools to reserve. Based on availability, Google creates a draft reservation request for you. If the draft matches your requirements, then accept and submit the request. If you reserve compute and storage capacity together, then you must accept both requests as a bundle to ensure that Google delivers both resources at the same time. Google Cloud approves your reservation request within a few minutes.

For instructions, see [Reserve capacity through your account team](https://docs.cloud.google.com/cluster-director/docs/reserve-capacity).

  2. **Consume reserved resources**. At the start of your reservation period, Google delivers your compute reservation and Hyperdisk pools. You can use the reserved resources to create compute instances and attach storage disks in one or more of your cluster partitions. For A4X, TPU7x, and TPU v6e reservations (in [all-capacity mode](https://docs.cloud.google.com/tpu/docs/all-capacity-overview) for TPUs), you can also select specific [blocks](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#block) or [sub-blocks](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#sub-block) to control the placement of your VMs.

For instructions, see one of the following:

     * [Create an AI-optimized cluster based on a template](https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template)

     * [Create a custom cluster](https://docs.cloud.google.com/cluster-director/docs/create/custom-cluster)




### Use future reservations in calendar mode

To run short-running distributed workloads that require densely allocated resources, you can request to reserve compute resources for up to 90 days. If Google approves your request, then you have exclusive access to your reserved resources for that time, and you can use the resources to create clusters. At the end of the reservation period, Compute Engine does the following:

  * Compute Engine deletes the reservation.

  * Compute Engine deletes any VM instances that use the reservation.

**Caution:** After the reservation that you used to create a VM reaches its end time, Cluster Director deletes the VM regardless of its [termination action](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime#limit-runtime-new-vm). To prevent data loss, back up your data by using one of the data protection options. For more information, see [Data protection options for disks and instances](https://docs.cloud.google.com/compute/docs/disks/data-protection).



#### Ideal workloads for future reservations in calendar mode

Future reservations in calendar mode are ideal for the following workloads:

  * Model pre-training

  * Model fine-tuning

  * Simulations

  * Inference




#### Characteristics of future reservations in calendar mode

Future reservations in calendar mode have the following characteristics:

  * You can reserve A4, A3 Ultra, A3 Mega, TPU7x*, TPU v6e, or TPU v5p machine types. Google densely allocates GPU VMs to minimize network latency, and allocates TPU VMs as close to each other as possible on a best-effort basis.

**Note:** To reserve TPU7x VMs with future reservations in calendar mode, you must contact your account team or the sales team to request access.
  * You can view the future availability of resources, and then reserve GPU or TPU capacity for up to 90 days. At your chosen delivery date, you can use the reserved resources to create VMs until the end of the reservation period. For supported request sizes and locations, see [Limitations for future reservation requests in calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview#limitations) in the Compute Engine documentation.

  * You use the reservation-bound provisioning model to create compute instances, which has the following benefits:

    * You have a higher chance to obtain GPUs or TPUs.

    * You get a discount up to 53% for vCPUs, memory, GPUs, TPUs, and any attached Local SSD disks.




#### How to use future reservations in calendar mode

To use future reservations in calendar mode to create clusters, you must complete the following steps:

  1. **View resource availability**. You can view the future availability of the resources that you want to reserve. When you create a reservation request, you can specify the number, type, and reservation duration for the resources that you confirmed as available. This action increases the chances that Google Cloud approves your request.

For instructions, see [View the future availability of resources](https://docs.cloud.google.com/compute/docs/instances/create-future-reservations-calendar-mode#view-availability).

  2. **Reserve capacity**. You create a reservation request for a future date and time. Google Cloud approves the reservation request within two minutes. If Google Cloud approves the request, then Compute Engine reserves the capacity for you. At your chosen delivery date, you can use the reserved resources to create clusters.

For instructions, see [Create a request for GPU VMs, H4D VMs, or TPUs](https://docs.cloud.google.com/compute/docs/instances/create-future-reservations-calendar-mode#request).

  3. **Consume reserved resources**. At the start of your chosen reservation period, you can use the reservation to create VMs in one or more of your cluster partitions.

For instructions, see one of the following:

     * [Create an AI-optimized cluster based on a template](https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template)

     * [Create a custom cluster](https://docs.cloud.google.com/cluster-director/docs/create/custom-cluster)




### Use Flex-start

To run short-duration workloads that require densely allocated resources, you can request compute resources for up to seven days by using Flex-start. Whenever resources are available, Compute Engine creates your requested number of VMs. The Flex-start VMs run until you delete them, or until Compute Engine deletes the VMs at the end of their run duration.

#### Ideal workloads for Flex-start

Flex-start is ideal for workloads that can start at any time, such as the following:

  * Small model pre-training

  * Model fine-tuning

  * Simulations

  * Batch inference




#### Characteristics of Flex-start

Flex-start has the following characteristics:

  * You can request A4, A3 Ultra, A3 Mega, TPU7x, TPU v6e, and TPU v5p VMs. For TPU VMs, Cluster Director provisions all VMs within a slice together on a 2D or 3D interconnect topology; slice availability and dense allocation across nodes depend on resource availability.

**Note:** To create TPU7x Flex-start VMs, you must contact your account team or the sales team to request access.
  * You use the flex-start provisioning model to create Flex-start VMs, which has the following benefits:

    * You have a higher chance to obtain GPUs or TPUs.

    * You get a discount up to 53% for vCPUs, memory, GPUs, TPUs, and any attached Local SSD disks.

  * You can request resources for up to seven days. When your allocated resources reach the end of their maximum run duration, Cluster Director automatically requests new resources with the same run duration.

**Note:** If resources are unavailable at the end of a maximum run duration, then Cluster Director attempts to obtain resources to restart nodes for up to eight hours. After this time, Slurm sets the node state to `down`. The request remains active until Cluster Director allocates the required resources or you cancel the request. To cancel a pending request, modify a compute resource configuration, modify the number of nodes in a nodeset, or delete your cluster.



#### How to use Flex-start

To use Flex-start to create VMs in one or more of your cluster partitions, use one of the following methods:

  * [Create an AI-optimized cluster based on a template](https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template)

  * [Create a custom cluster](https://docs.cloud.google.com/cluster-director/docs/create/custom-cluster)




### Use Spot

To run fault-tolerant workloads, you can obtain compute resources immediately based on availability. You get resources at the lowest price possible. However, Compute Engine can preempt Spot VMs at any time to reclaim capacity.

#### Ideal workloads for Spot

Spot is ideal for workloads where interruptions are acceptable, such as the following:

  * Batch processing

  * High performance computing (HPC)

  * Continuous integration and continuous deployment (CI/CD)

  * Data analytics

  * Media encoding

  * Online inference




#### Characteristics of Spot

Spot has the following characteristics:

  * You can create A4, A3 Ultra, A3 Mega, TPU7x, TPU v6e, TPU v5p, and N2 VMs. For TPU VMs, Cluster Director provisions all VMs within a slice together on a 2D or 3D interconnect topology; slice availability and dense allocation across nodes depend on resource availability.

**Note:** To create TPU7x Spot VMs, you must contact your account team or the sales team to request access.
  * You can immediately create clusters. Unless Compute Engine preempts the VMs to reclaim capacity, GPU and N2 VMs run until you stop or delete them, and TPU VMs run until you delete them.

  * You use the spot provisioning model to create Spot VMs, which has the following benefits:

    * You have a higher chance to obtain GPUs or TPUs.

    * You get a discount up to 91% for vCPUs, memory, and any attached GPUs, TPUs, and Local SSD disks.




#### How to use Spot

To use Spot to create VMs in one or more of your cluster partitions, complete the following steps:

  1. **View resource availability**. You can view the availability of A4, A3 Ultra, A3 Mega, and N2 machine types in the region or zone where you want to create Spot VMs. This action helps reduce the time that Cluster Director takes to allocate resources and create Spot VMs.

For instructions, see [View resource availability for Spot VMs](https://docs.cloud.google.com/compute/docs/instances/view-vm-availability).

  2. **View preemption rate and pricing**. You can view the historical and current preemption rate and pricing across A4, A3 Ultra, A3 Mega, and N2 machine types and zones. This information helps you choose the machine type and location that best fit your workload and budget.

For instructions, see [View the preemption rate and pricing for Spot VMs](https://docs.cloud.google.com/compute/docs/instances/view-spot-preemption-price).

  3. **Create your cluster**. To create your cluster with one or more partitions that use Spot VMs, select one of the following methods:

     * [Create an AI-optimized cluster based on a template](https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template)

     * [Create a custom cluster](https://docs.cloud.google.com/cluster-director/docs/create/custom-cluster)




### Use On-demand

To run TPU workloads without a reservation or cluster components without GPU or TPU acceleration (such as login nodes), you can obtain on-demand resources based on availability at standard pricing.

#### Ideal workloads for On-demand

On-demand is ideal for the following workloads:

  * TPU training and inference workloads

  * Login nodes

  * CPU-bound computational tasks

  * General-purpose HPC




#### Characteristics of On-demand

On-demand has the following characteristics:

  * You can create C4A, N2, TPU7x, TPU v6e, and TPU v5p VMs. Cluster Director provisions TPU VMs in a slice together on a 2D or 3D interconnect topology. For C4A and N2 VMs, dense allocation depends on resource availability. You can use C4A VMs only for login nodes.

  * You can immediately create clusters. C4A and N2 VMs run until you stop or delete them, and TPU VMs run until you delete them.

  * You use the standard provisioning model, which is the default model.




#### How to use On-demand

To use On-demand to create VMs in one or more of your cluster partitions, use one of the following methods:

  * [Create an AI-optimized cluster based on a template](https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template)

  * [Create a custom cluster](https://docs.cloud.google.com/cluster-director/docs/create/custom-cluster)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-06 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/cluster-director/docs/obtain-capacity/
title: Capacity overview \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:50:16.039583+00:00
---

# Capacity overview  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/obtain-capacity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Capacity overview Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of how to obtain capacity and quota for each consumption option in Cluster Director.

Cluster Director supports several [consumption options](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option#comparison) to help you get and use compute resources. Understanding the quota, reservation, and billing requirements for each option helps you plan capacity and avoid provisioning delays when you create clusters.

## How to obtain capacity

**Note:** Support for TPU VMs in Cluster Director is in [Preview](https://cloud.google.com/products#product-launch-stages). To obtain TPU7x VMs with any consumption option except On-demand, you must contact your account team or the sales team to request access.

The following table describes how you can obtain capacity for each consumption option:

Consumption option | Process for obtaining capacity | Pricing implications  
---|---|---  
Future reservations for more than 90 days (for capacity blocks) |  To get future reservation resources, the process is as follows:

  1. To [reserve capacity](https://docs.cloud.google.com/cluster-director/docs/reserve-capacity), contact your account team. You can request compute instances and, optionally, a Hyperdisk pool.
  2. Google increases your quota, and then provisions your requested resources at your specified start date and for your specified duration.
  3. When you create a cluster [from a template](https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template) or [as a custom cluster](https://docs.cloud.google.com/cluster-director/docs/create/custom-cluster), select the **Use reservation** consumption option and then specify your reservation. Cluster Director creates the cluster from your reserved capacity.

| You pay for the entire reservation period, whether you use the reserved resources or not. For more information, see the pricing for [ reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#reservation-billing) and [Hyperdisk pools](https://docs.cloud.google.com/compute/disks-image-pricing#storage_pools).   
Future reservations for up to 90 days (in calendar mode) |  To get future reservation resources, the process is as follows:

  1. [ Search for available capacity and reserve resources by using the Google Cloud console, gcloud CLI, or Compute Engine API](https://docs.cloud.google.com/compute/docs/instances/create-future-reservations-calendar-mode).
  2. No quota is charged and no action is required from you.
  3. When you create a cluster [from a template](https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template) or [as a custom cluster](https://docs.cloud.google.com/cluster-director/docs/create/custom-cluster), select the **Use reservation** consumption option and then specify your reservation. Cluster Director creates the cluster from your reserved capacity.

| You're charged for the entire reservation period, whether or not you use the reserved resources for the entire period. For more information, see [Dynamic Workload Scheduler pricing](https://cloud.google.com/products/dws/pricing).   
Flex-start |  For this consumption option, _no reservation is required_. To get Flex-start resources, the process is as follows:

  1. Request preemptible [GPU quota](https://docs.cloud.google.com/compute/resource-usage#gpu_quota) or [TPU quota](https://docs.cloud.google.com/compute/resource-usage#tpu_quota) for the machine type that you want to use.
  2. When you create a cluster [from a template](https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template) or [as a custom cluster](https://docs.cloud.google.com/cluster-director/docs/create/custom-cluster), select the **Use Flex-start** consumption option. When your requested capacity becomes available, Cluster Director provisions your cluster. You obtain resources for up to seven days.

| You're charged when the resources are in use. Resources that you provision by using Flex-start receive discounts through [Dynamic Workload Scheduler pricing](https://cloud.google.com/products/dws/pricing).  
Spot |  For this consumption option, _no reservation is required_. To get Spot resources, the process is as follows:

  1. Request preemptible [CPU quota](https://docs.cloud.google.com/compute/resource-usage#cpu_quota), [GPU quota](https://docs.cloud.google.com/compute/resource-usage#gpu_quota), or [TPU quota](https://docs.cloud.google.com/compute/resource-usage#tpu_quota) for the machine type that you want to use.
  2. For GPU or CPU instances, [view resource availability in the region or zone where you want to create compute instances](https://docs.cloud.google.com/compute/docs/instances/view-vm-availability).
  3. When you create a cluster [from a template](https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template) or [as a custom cluster](https://docs.cloud.google.com/cluster-director/docs/create/custom-cluster), select the **Use Spot** consumption option. Cluster Director provisions your cluster, but Compute Engine can preempt the Spot VMs in your cluster at any time.

| You're charged when the resources are in use. Spot VMs receive discounts through [Spot VMs pricing](https://docs.cloud.google.com/compute/docs/instances/spot#pricing).   
On-demand |  For this consumption option, _no reservation is required_. To get on-demand resources, the process is as follows:

  1. If you don't have enough [CPU quota](https://docs.cloud.google.com/compute/resource-usage#cpu_quota) or [TPU quota](https://docs.cloud.google.com/compute/resource-usage#tpu_quota) for the resources that you plan to provision, then [request a quota adjustment](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota).
  2. When you create a cluster [from a template](https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template) or [as a custom cluster](https://docs.cloud.google.com/cluster-director/docs/create/custom-cluster), select the **Use on-demand** consumption option. Cluster Director provisions your cluster.

| You're charged when the resources are in use. For more information, see [VM instance pricing](https://cloud.google.com/compute/vm-instance-pricing) and [Cloud TPU pricing](https://cloud.google.com/tpu/pricing).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

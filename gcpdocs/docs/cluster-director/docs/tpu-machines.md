---
url: https://docs.cloud.google.com/cluster-director/docs/tpu-machines/
title: Supported TPU machines for Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T05:36:37.350927+00:00
---

# Supported TPU machines for Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/tpu-machines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Supported TPU machines for Cluster Director Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes the TPU-accelerated Compute Engine machines that are available in Cluster Director. You can use these machine types only for compute nodes. These machine types connect multiple 4-chip virtual machine (VM) instances into slices over inter-chip interconnects (ICI) to run large-scale artificial intelligence (AI) or machine learning (ML) training and inference workloads. For an overview of TPU architecture, ideal use cases, and pricing in Google Cloud, see [Understand TPUs](https://docs.cloud.google.com/docs/compute-area/tpus).

In Cluster Director, you must pair TPU compute nodes with login nodes that use the [N2 machine series](https://docs.cloud.google.com/cluster-director/docs/cpu-machines#n2-series). TPU machine types are available in zones where both [Cluster Director](https://docs.cloud.google.com/cluster-director/docs/locations) and the [TPU machine type](https://docs.cloud.google.com/compute/docs/regions-zones/tpu-regions-zones) are available, except for AI zones.

## Supported TPU machine types

The following sections describe the machine types that Cluster Director supports for each TPU generation.

### TPU7x (Ironwood)

Each TPU7x VM is a full-host instance that contains 4 TPU7x chips across 2 non-uniform memory access (NUMA) nodes. Each TPU7x chip contains 2 TensorCores and 4 SparseCores, and the Ironwood programming model exposes 2 TPU devices per TPU chip instead of a single logical core. For more information, see [Dual-chiplet architecture](https://docs.cloud.google.com/tpu/docs/tpu7x#dual-chiplet_architecture) in the Cloud TPU documentation.

In Cluster Director, TPU7x VMs use a 3D torus topology (`AxBxC`) and require Hyperdisk Balanced boot disks. The following table lists the specifications for the TPU7x machine type:

Machine type | Number of vCPUs | Instance memory (GiB) | Physical NIC count | Maximum network bandwidth (Gbps) | Number of TPU chips per VM | Number of NUMA nodes | Total TPU memory (GiB HBM)  
---|---|---|---|---|---|---|---  
`tpu7x-standard-4t` | 224 | 960 | 2 | 400 | 4 | 2 | 768  
  
For more information about the TPU7x architecture, see [TPU7x (Ironwood)](https://docs.cloud.google.com/tpu/docs/tpu7x) in the Cloud TPU documentation.

### TPU v6e (Trillium)

Each TPU v6e VM is a half-host instance that contains 4 TPU v6e chips on a single NUMA node. Each TPU v6e chip contains 1 TensorCore and 2 SparseCores.

In Cluster Director, TPU v6e instances use a 2D torus topology (`AxB`) and require Hyperdisk Balanced boot disks. The following table lists the specifications for the supported TPU v6e machine type in Cluster Director:

Machine type | Number of vCPUs | Instance memory (GiB) | Physical NIC count | Maximum network bandwidth (Gbps) | Number of TPU chips per VM | Number of NUMA nodes | Total TPU memory (GiB HBM)  
---|---|---|---|---|---|---|---  
`ct6e-standard-4t` | 180 | 720 | 2 | 400 | 4 | 1 | 128  
  
For more information about the TPU v6e architecture, see [TPU v6e](https://docs.cloud.google.com/tpu/docs/v6e) in the Cloud TPU documentation.

### TPU v5p

Each TPU v5p VM is a full-host instance that contains 4 TPU v5p chips across 2 NUMA nodes, with 2 TensorCores and 4 SparseCores per chip. A TPU v5p Pod contains 8,960 TPU chips connected over reconfigurable high-speed links, which let you connect the chips in a slice in multiple configurations.

In Cluster Director, TPU v5p instances use a 3D torus topology (`AxBxC`) and require Balanced Persistent Disk boot disks. The following table lists the specifications for the TPU v5p machine type:

Machine type | Number of vCPUs | Instance memory (GiB) | Physical NIC count | Maximum network bandwidth (Gbps) | Number of TPU chips per VM | Number of NUMA nodes | Total TPU memory (GiB HBM)  
---|---|---|---|---|---|---|---  
`ct5p-hightpu-4t` | 208 | 448 | 1 | 200 | 4 | 2 | 380  
  
For more information about the TPU v5p architecture, see [TPU v5p](https://docs.cloud.google.com/tpu/docs/v5p) in the Cloud TPU documentation.

## TPU architecture specifications

The following table lists the key specifications for each TPU version.

Specification | TPU7x | TPU v6e | TPU v5p  
---|---|---|---  
Number of chips per pod | 9216 | 256 | 8960  
Peak compute per chip (BF16) (TFLOPs) | 2307 | 918 | 459  
Peak compute per chip (FP8) (TFLOPs) | 4614 | 918 | 459  
HBM capacity per chip (GiB) | 192 | 32 | 95  
HBM bandwidth per chip (GBps) | 7380 | 1638 | 2765  
Number of vCPUs (4-chip VM) | 224 | 180 | 208  
RAM (GiB) (4-chip VM) | 960 | 720 | 448  
Number of TensorCores per chip | 2 | 1 | 2  
Number of SparseCores per chip | 4 | 2 | 4  
Bidirectional inter-chip interconnect (ICI) bandwidth per chip (GBps) | 1200 | 800 | 1200  
Data center network (DCN) bandwidth per chip (Gbps) | 100 | 100 | 50  
  
## Slice topologies and boot disk requirements

In Cluster Director, TPU VMs run as interconnected slices. A _slice_ is a group of TPU chips connected over ICI links, where each dimension in the topology represents the number of TPU chips along that axis. All TPU VMs in a slice share the same lifecycle. If a VM in a slice fails, undergoes host maintenance, or is deleted, then Cluster Director tears down all other VMs in that slice. Each TPU VM contains 4 TPU chips. To calculate the number of VMs in a slice, multiply the topology dimensions to find the total number of chips, and then divide by 4. Cluster Director supports the following slice topologies:

  * **2D topology (`AxB`)**: TPU v6e VMs use this topology. Cluster Director supports up to 64 TPU VMs (256 TPU chips) per slice for TPU v6e. For example, a `2x4` topology contains 8 TPU chips (2 × 4), which requires 2 VMs (8 / 4).

  * **3D topology (`AxBxC`)**: TPU7x and TPU v5p VMs use this topology. Cluster Director supports up to 1,000 TPU VMs (4,000 TPU chips) per slice for TPU7x and TPU v5p. For example, a `2x2x4` topology contains 16 TPU chips (2 × 2 × 4), which requires 4 VMs (16 / 4).


**Note:** To view interactive renderings of different TPU slice topologies, use the [TPU topology visualizer](https://tpu-visualizer.uc.r.appspot.com/).

How you configure the slice topology depends on whether your nodeset uses static or dynamic TPU nodes as follows:

  * **Static TPU nodesets** : you specify a fixed slice topology (`acceleratorTopology`) when you create the nodeset, and the static node count must be a multiple of the number of VMs per slice.

  * **Dynamic TPU nodesets** : you specify the slice topology for each job when you submit the job with the [`--layout` flag](https://docs.cloud.google.com/cluster-director/docs/workloads/configure-slurm#submit-tpu-jobs).




The following table summarizes the machine type, topology format, `--layout` value, and required boot disk type for each supported TPU generation:

TPU generation | Machine type | Topology format | Example slice topologies | `--layout` value | Required boot disk type  
---|---|---|---|---|---  
TPU7x (Ironwood) | `tpu7x-standard-4t` | 3D (`AxBxC`) |  `2x2x1` (1 VM, 4 TPU chips)  
`2x2x2` (2 VMs, 8 TPU chips)  
`2x2x4` (4 VMs, 16 TPU chips)  
`4x4x4` (16 VMs, 64 TPU chips)  | `tpu7x` |  Hyperdisk Balanced (`hyperdisk-balanced`)   
TPU v6e (Trillium) | `ct6e-standard-4t` | 2D (`AxB`) |  `2x2` (1 VM, 4 TPU chips)  
`2x4` (2 VMs, 8 TPU chips)  
`4x4` (4 VMs, 16 TPU chips)  
`4x8` (8 VMs, 32 TPU chips)  
`8x8` (16 VMs, 64 TPU chips)  
`8x16` (32 VMs, 128 TPU chips)  
`16x16` (64 VMs, 256 TPU chips)  | `v6e` |  Hyperdisk Balanced (`hyperdisk-balanced`)   
TPU v5p | `ct5p-hightpu-4t` | 3D (`AxBxC`) |  `2x2x1` (1 VM, 4 TPU chips)  
`2x2x2` (2 VMs, 8 TPU chips)  
`2x2x4` (4 VMs, 16 TPU chips)  
`2x4x4` (8 VMs, 32 TPU chips)  | `v5p` | Balanced Persistent Disk (`pd-balanced`)  
  
## What's next

  * [Supported OS images for Cluster Director](https://docs.cloud.google.com/cluster-director/docs/os-images)

  * [Try out Cluster Director](https://docs.cloud.google.com/cluster-director/docs/create/quickstart)

  * [Submit jobs on TPU VMs](https://docs.cloud.google.com/cluster-director/docs/workloads/configure-slurm#submit-tpu-jobs)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 

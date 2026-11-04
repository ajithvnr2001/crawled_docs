---
url: https://docs.cloud.google.com/cluster-director/docs/gpu-machines/
title: Supported GPU machines for Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T05:35:57.514522+00:00
---

# Supported GPU machines for Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/gpu-machines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Supported GPU machines for Cluster Director Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the GPU-accelerated machine series that are available in Cluster Director. You can use these machine series only for compute nodes to run large-scale artificial intelligence (AI), machine learning (ML), and high performance computing (HPC) workloads. For an overview of GPU architecture, ideal use cases, and pricing in Google Cloud, see [Understand GPUs](https://docs.cloud.google.com/docs/compute-area/gpus).

GPU machine types are available in zones where both [Cluster Director](https://docs.cloud.google.com/cluster-director/docs/locations) and the [GPU machine type](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones) are available, except for AI zones.

## A4X Max and A4X machine series

The [A4X Max and A4X machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms) run on an exascale platform based on [NVIDIA's rack-scale architecture](https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/) and are optimized for compute-intensive, memory-intensive, and network-bound ML training and HPC workloads. A4X Max and A4X differ in their GPU and networking components. A4X Max is available only as bare metal instances, which provide direct access to the host server's CPU and memory without the Compute Engine hypervisor layer.

You can pair compute nodes that use the A4X Max or A4X machine series with login nodes that use the [C4A](https://docs.cloud.google.com/cluster-director/docs/cpu-machines#c4a-series) or [N2](https://docs.cloud.google.com/cluster-director/docs/cpu-machines#n2-series) machine series. A4X Max and A4X instances require Hyperdisk Balanced boot disks.

### A4X Max machine type (bare metal)

[A4X Max accelerator-optimized](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms) machine types use NVIDIA GB300 Grace Blackwell Ultra Superchips (`nvidia-gb300`) and are ideal for foundation model training and serving. A4X Max machine types are available as [bare metal instances](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances). 

A4X Max is an exascale platform based on [NVIDIA GB300 NVL72](https://www.nvidia.com/en-us/data-center/gb300-nvl72/). Each machine has two sockets with NVIDIA Grace CPUs with Arm Neoverse V2 cores. These CPUs are connected to four NVIDIA B300 Blackwell GPUs with fast chip-to-chip ([NVLink-C2C](https://www.nvidia.com/en-us/data-center/nvlink-c2c/)) communication. For information about machine type limitations, see [A4X Max and A4X limitations](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-limitations). 

The following table lists the specifications for the A4X Max machine type:

**Note:** To use A4X Max machine types in your cluster, you must reserve capacity through your account team and use the reserved capacity to create instances. For more information about the ways you can create A4X Max instances in a cluster, see [Choose a consumption option](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option). 

Machine type | vCPU count | Instance memory (GB) | Attached Local SSD (GiB) | Physical NIC count | Maximum network bandwidth (Gbps) | NVIDIA GB300 GPU count | GPU memory (GB HBM3e)  
---|---|---|---|---|---|---|---  
`a4x-maxgpu-4g-metal` | 144 | 960 | 12,000 | 6 | 3,600 | 4 | 1,116  
  
The following notes apply to the preceding table:

  * **vCPU count** : a vCPU is implemented as a single hardware hyper-thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).
  * **Maximum network bandwidth** : maximum egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information about network bandwidth, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).
  * **GPU memory** : GPU memory is the memory on a GPU device that can be used for temporary storage of data. It is separate from the instance's memory and is specifically designed to handle the higher bandwidth demands of your graphics-intensive workloads.



### A4X machine type

[A4X accelerator-optimized](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms) machine types use NVIDIA GB200 Grace Blackwell Superchips (`nvidia-gb200`) and are ideal for foundation model training and serving. 

A4X is an exascale platform based on [NVIDIA GB200 NVL72](https://www.nvidia.com/en-us/data-center/gb200-nvl72/). Each machine has two sockets with NVIDIA Grace CPUs with Arm Neoverse V2 cores. These CPUs are connected to four NVIDIA B200 Blackwell GPUs with fast chip-to-chip ([NVLink-C2C](https://www.nvidia.com/en-us/data-center/nvlink-c2c/)) communication. For information about machine type limitations, see [A4X Max and A4X limitations](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-limitations). 

The following table lists the specifications for the A4X machine type:

**Note:** To use A4X machine types in your cluster, you must reserve capacity through your account team and use the reserved capacity to create VMs. For more information about the ways you can create A4X VMs in a cluster, see [Choose a consumption option](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option). 

Machine type | vCPU count | Instance memory (GB) | Attached Local SSD (GiB) | Physical NIC count | Maximum network bandwidth (Gbps) | NVIDIA GB200 GPU count | GPU memory (GB HBM3e)  
---|---|---|---|---|---|---|---  
`a4x-highgpu-4g` | 140 | 884 | 12,000 | 6 | 2,000 | 4 | 744  
  
The following notes apply to the preceding table:

  * **vCPU count** : a vCPU is implemented as a single hardware hyper-thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).
  * **Maximum network bandwidth** : maximum egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information about network bandwidth, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).
  * **GPU memory** : GPU memory is the memory on a GPU device that can be used for temporary storage of data. It is separate from the instance's memory and is specifically designed to handle the higher bandwidth demands of your graphics-intensive workloads.



## A4 machine series

[A4 accelerator-optimized](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms) machine types have [NVIDIA B200 Blackwell GPUs](https://www.nvidia.com/en-us/data-center/b200/) (`nvidia-b200`) attached and are ideal for foundation model training and serving. For information about machine type limitations, see [A4 limitations](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-limitations). 

In Cluster Director, you must pair A4 compute nodes with login nodes that use the [N2 machine series](https://docs.cloud.google.com/cluster-director/docs/cpu-machines#n2-series). A4 instances require Hyperdisk Balanced boot disks. The following table lists the specifications for the A4 machine type:

**Note:** To use A4 machine types in your cluster, you must reserve capacity to create VMs, create Spot VMs, or create Flex-start VMs. For more information about the ways you can create A4 VMs in a cluster, see [Choose a consumption option](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option). 

Machine type | vCPU count | Instance memory (GB) | Attached Local SSD (GiB) | Physical NIC count | Maximum network bandwidth (Gbps) | NVIDIA B200 Blackwell GPU count | GPU memory (GB HBM3e)  
---|---|---|---|---|---|---|---  
`a4-highgpu-8g` | 224 | 3,968 | 12,000 | 10 | 3,600 | 8 | 1,440  
  
The following notes apply to the preceding table:

  * **vCPU count** : a vCPU is implemented as a single hardware hyper-thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).
  * **Maximum network bandwidth** : maximum egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information about network bandwidth, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).
  * **GPU memory** : GPU memory is the memory on a GPU device that can be used for temporary storage of data. It is separate from the instance's memory and is specifically designed to handle the higher bandwidth demands of your graphics-intensive workloads.



## A3 machine series

The A3 machine series uses NVIDIA H100 or H200 SXM GPUs and is suitable for a wide range of large model training and inference workloads. In Cluster Director, you must pair A3 compute nodes with login nodes that use the [N2 machine series](https://docs.cloud.google.com/cluster-director/docs/cpu-machines#n2-series).

Cluster Director supports the A3 machine types that are described in the following sections.

### A3 Ultra machine type

[A3 Ultra](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-ultra-vms) machine types have [NVIDIA H200 SXM GPUs](https://www.nvidia.com/en-us/data-center/h200/) (`nvidia-h200-141gb`) attached and provide the highest network performance in the A3 series. A3 Ultra machine types are ideal for foundation model training and serving. For information about machine type limitations, see [A3 Ultra limitations](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-ultra-limitations). 

In Cluster Director, A3 Ultra instances require Hyperdisk Balanced boot disks. The following table lists the specifications for the A3 Ultra machine type:

**Note:** To use A3 Ultra machine types in your cluster, you must reserve capacity to create VMs, create Spot VMs, or create Flex-start VMs. For more information about the ways to create A3 Ultra VMs in a cluster, see [Choose a consumption option](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option). 

Machine type | vCPU count | Instance memory (GB) | Attached Local SSD (GiB) | Physical NIC count | Maximum network bandwidth (Gbps) | NVIDIA H200 GPU count | GPU memory (GB HBM3e)  
---|---|---|---|---|---|---|---  
`a3-ultragpu-8g` | 224 | 2,952 | 12,000 | 10 | 3,600 | 8 | 1128  
  
The following notes apply to the preceding table:

  * **vCPU count** : a vCPU is implemented as a single hardware hyper-thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).
  * **Maximum network bandwidth** : maximum egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information about network bandwidth, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).
  * **GPU memory** : GPU memory is the memory on a GPU device that can be used for temporary storage of data. It is separate from the instance's memory and is specifically designed to handle the higher bandwidth demands of your graphics-intensive workloads.



### A3 Mega machine type

[A3 Mega](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-mega-vms) machine types have [NVIDIA H100 SXM GPUs](https://www.nvidia.com/en-us/data-center/h100/) and are ideal for large model training and multi-host inference. For information about machine type limitations, see [A3 Mega limitations](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-mega-limitations). 

In Cluster Director, A3 Mega instances support Balanced Persistent Disk, SSD (performance) Persistent Disk, Hyperdisk Balanced, Hyperdisk ML, Hyperdisk Extreme, or Hyperdisk Throughput boot disks. The following table lists the specifications for the A3 Mega machine type:

**Note:** To use A3 Mega machine types in your cluster, you must reserve capacity to create VMs, create Spot VMs, or create Flex-start VMs. For more information about the ways to create A3 Mega VMs in a cluster, see [Choose a consumption option](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option). 

Machine type | vCPU count | Instance memory (GB) | Attached Local SSD (GiB) | Physical NIC count | Maximum network bandwidth (Gbps) | NVIDIA H100 GPU count | GPU memory (GB HBM3)  
---|---|---|---|---|---|---|---  
`a3-megagpu-8g` | 208 | 1,872 | 6,000 | 9 | 1,800 | 8 | 640  
  
The following notes apply to the preceding table:

  * **vCPU count** : a vCPU is implemented as a single hardware hyper-thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).
  * **Maximum network bandwidth** : maximum egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information about network bandwidth, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).
  * **GPU memory** : GPU memory is the memory on a GPU device that can be used for temporary storage of data. It is separate from the instance's memory and is specifically designed to handle the higher bandwidth demands of your graphics-intensive workloads.



## What's next

  * [Supported CPU machines for Cluster Director](https://docs.cloud.google.com/cluster-director/docs/cpu-machines)

  * [Supported TPU machines for Cluster Director](https://docs.cloud.google.com/cluster-director/docs/tpu-machines)

  * [Supported OS images for Cluster Director](https://docs.cloud.google.com/cluster-director/docs/os-images)

  * [Try out Cluster Director](https://docs.cloud.google.com/cluster-director/docs/create/quickstart)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 

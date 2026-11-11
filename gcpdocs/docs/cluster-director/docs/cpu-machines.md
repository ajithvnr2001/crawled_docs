---
url: https://docs.cloud.google.com/cluster-director/docs/cpu-machines/
title: Supported CPU machines for Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:50:19.439315+00:00
---

# Supported CPU machines for Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/cpu-machines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Supported CPU machines for Cluster Director Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the CPU-based Compute Engine machines that are available in Cluster Director. You can use these general-purpose machines to run high performance computing (HPC) workloads and cluster management roles.

## C4A machine series

Cluster Director supports the [C4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series). This machine series runs on Arm-based Google Axion processors and delivers consistent performance for Arm-based workloads. You must pair login nodes that use the C4A machine series with compute nodes that use the [A4X Max or A4X machine series](https://docs.cloud.google.com/cluster-director/docs/gpu-machines#a4x-series).

**Note:** You can use the C4A machine series for login nodes only.

The machine types in the C4A series differ by the amount of DDR5 memory per vCPU. These memory configurations are as follows:

  * **`standard`** : 4 GB of memory per vCPU

  * **`highmem`** : 8 GB of memory per vCPU

  * **`highcpu`** : 2 GB of memory per vCPU




Each family offers a range of machine sizes, from 1 to 72 vCPUs. You can't use machine types that have Local SSD disks attached (`-lssd`) or run on bare metal (`-metal`) for login nodes. C4A instances support Hyperdisk Balanced or Hyperdisk Extreme boot disks.

The following table summarizes the C4A machine types that are available in Cluster Director:

### C4A standard

Machine types | vCPUs* | Memory (GB) | Default egress bandwidth (Gbps)‡ | Tier_1 egress bandwidth (Gbps)#  
---|---|---|---|---  
`c4a-standard-1` | 1 | 4 | Up to 10 | N/A  
`c4a-standard-2` | 2 | 8 | Up to 10 | N/A  
`c4a-standard-4` | 4 | 16 | Up to 23 | N/A  
`c4a-standard-8` | 8 | 32 | Up to 23 | N/A  
`c4a-standard-16` | 16 | 64 | Up to 23 | N/A  
`c4a-standard-32` | 32 | 128 | Up to 23 | Up to 50  
`c4a-standard-48` | 48 | 192 | Up to 34 | Up to 50  
`c4a-standard-64` | 64 | 256 | Up to 45 | Up to 75  
`c4a-standard-72` | 72 | 288 | Up to 50 | Up to 100  
  
* A vCPU represents an entire physical core because simultaneous multithreading (SMT) isn't supported. For more information, see [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
‡ Maximum egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
# Supports [ high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. 

### C4A high-mem

Machine types | vCPUs* | Memory (GB) | Default egress bandwidth (Gbps)‡ | Tier_1 egress bandwidth (Gbps)#  
---|---|---|---|---  
`c4a-highmem-1` | 1 | 8 | Up to 10 | N/A  
`c4a-highmem-2` | 2 | 16 | Up to 10 | N/A  
`c4a-highmem-4` | 4 | 32 | Up to 23 | N/A  
`c4a-highmem-8` | 8 | 64 | Up to 23 | N/A  
`c4a-highmem-16` | 16 | 128 | Up to 23 | N/A  
`c4a-highmem-32` | 32 | 256 | Up to 23 | Up to 50  
`c4a-highmem-48` | 48 | 384 | Up to 34 | Up to 50  
`c4a-highmem-64` | 64 | 512 | Up to 45 | Up to 75  
`c4a-highmem-72` | 72 | 576 | Up to 50 | Up to 100  
  
* A vCPU represents an entire physical core because simultaneous multithreading (SMT) isn't supported. For more information, see [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
‡ Maximum egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
# Supports [ high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. 

### C4A high-cpu

Machine types | vCPUs* | Memory (GB) | Default egress bandwidth (Gbps)‡ | Tier_1 egress bandwidth (Gbps)#  
---|---|---|---|---  
`c4a-highcpu-1` | 1 | 2 | Up to 10 | N/A  
`c4a-highcpu-2` | 2 | 4 | Up to 10 | N/A  
`c4a-highcpu-4` | 4 | 8 | Up to 23 | N/A  
`c4a-highcpu-8` | 8 | 16 | Up to 23 | N/A  
`c4a-highcpu-16` | 16 | 32 | Up to 23 | N/A  
`c4a-highcpu-32` | 32 | 64 | Up to 23 | Up to 50  
`c4a-highcpu-48` | 48 | 96 | Up to 34 | Up to 50  
`c4a-highcpu-64` | 64 | 128 | Up to 45 | Up to 75  
`c4a-highcpu-72` | 72 | 144 | Up to 50 | Up to 100  
  
* A vCPU represents an entire physical core because simultaneous multithreading (SMT) isn't supported. For more information, see [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
‡ Maximum egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
# Supports [ high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. 

## N2 machine series

Cluster Director supports the [N2 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_series). This series offers a balance of price and performance suitable for a variety of workloads, such as CPU-bound computational tasks or general-purpose HPC workloads. You can use the N2 machine series for compute nodes or login nodes. N2 login nodes support clusters with any supported GPU, TPU, or CPU compute nodes, including A4X Max, A4X, A4, A3 Ultra, A3 Mega, TPU7x, TPU v6e, TPU v5p, and N2.

The N2 machine types differ by the amount of memory configured per vCPU. These memory configurations are as follows:

  * **`standard`** : 4 GB of memory per vCPU

  * **`highmem`** : 8 GB of memory per vCPU

  * **`highcpu`** : 1 GB of memory per vCPU




Each family offers a range of machine sizes, from 2 to 128 vCPUs. For login nodes, Google recommends that you use N2 standard machine types with 32 or fewer vCPUs to avoid unnecessary charges for compute capacity that you don't need. N2 instances support Persistent Disk, Hyperdisk Extreme, or Hyperdisk Throughput boot disks.

The following table summarizes the available N2 machine types in Cluster Director:

### N2 standard

Machine types | vCPUs* | Memory (GB) | Default egress bandwidth (Gbps)‡ | Tier_1 egress bandwidth (Gbps)#  
---|---|---|---|---  
`n2-standard-2` | 2 | 8 | Up to 10 | N/A  
`n2-standard-4` | 4 | 16 | Up to 10 | N/A  
`n2-standard-8` | 8 | 32 | Up to 16 | N/A  
`n2-standard-16` | 16 | 64 | Up to 32 | N/A  
`n2-standard-32` | 32 | 128 | Up to 32 | Up to 50  
`n2-standard-48` | 48 | 192 | Up to 32 | Up to 50  
`n2-standard-64` | 64 | 256 | Up to 32 | Up to 75  
`n2-standard-80` | 80 | 320 | Up to 32 | Up to 100  
`n2-standard-96` | 96 | 384 | Up to 32 | Up to 100  
`n2-standard-128` | 128 | 512 | Up to 32 | Up to 100  
  
* A vCPU is implemented as a single hardware thread, or logical core, on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
‡ Maximum egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
# Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. For Windows OS images, the maximum network bandwidth is limited to 50 Gbps. 

### N2 high-mem

Machine types | vCPUs* | Memory (GB) | Default egress bandwidth (Gbps)‡ | Tier_1 egress bandwidth (Gbps)#  
---|---|---|---|---  
`n2-highmem-2` | 2 | 16 | Up to 10 | N/A  
`n2-highmem-4` | 4 | 32 | Up to 10 | N/A  
`n2-highmem-8` | 8 | 64 | Up to 16 | N/A  
`n2-highmem-16` | 16 | 128 | Up to 32 | N/A  
`n2-highmem-32` | 32 | 256 | Up to 32 | Up to 50  
`n2-highmem-48` | 48 | 384 | Up to 32 | Up to 50  
`n2-highmem-64` | 64 | 512 | Up to 32 | Up to 75  
`n2-highmem-80` | 80 | 640 | Up to 32 | Up to 100  
`n2-highmem-96` | 96 | 768 | Up to 32 | Up to 100  
`n2-highmem-128` | 128 | 864 | Up to 32 | Up to 100  
  
* A vCPU is implemented as a single hardware thread, or logical core, on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
‡ Maximum egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
# Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. For Windows OS images, the maximum network bandwidth is limited to 50 Gbps. 

### N2 high-cpu

Machine types | vCPUs* | Memory (GB) | Default egress bandwidth (Gbps)‡ | Tier_1 egress bandwidth (Gbps)#  
---|---|---|---|---  
`n2-highcpu-2` | 2 | 2 | Up to 10 | N/A  
`n2-highcpu-4` | 4 | 4 | Up to 10 | N/A  
`n2-highcpu-8` | 8 | 8 | Up to 16 | N/A  
`n2-highcpu-16` | 16 | 16 | Up to 32 | N/A  
`n2-highcpu-32` | 32 | 32 | Up to 32 | Up to 50  
`n2-highcpu-48` | 48 | 48 | Up to 32 | Up to 50  
`n2-highcpu-64` | 64 | 64 | Up to 32 | Up to 75  
`n2-highcpu-80` | 80 | 80 | Up to 32 | Up to 100  
`n2-highcpu-96` | 96 | 96 | Up to 32 | Up to 100  
  
* A vCPU is implemented as a single hardware thread, or logical core, on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
‡ Maximum egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
# Supports [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. For Windows OS images, the maximum network bandwidth is limited to 50 Gbps. 

## What's next

  * [Supported OS images for Cluster Director](https://docs.cloud.google.com/cluster-director/docs/os-images)

  * [Try out Cluster Director](https://docs.cloud.google.com/cluster-director/docs/create/quickstart)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

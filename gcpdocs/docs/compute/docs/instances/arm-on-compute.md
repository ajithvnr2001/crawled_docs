---
url: https://docs.cloud.google.com/compute/docs/instances/arm-on-compute/
title: Arm instances on Compute \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:13:13.649336+00:00
---

# Arm instances on Compute  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/arm-on-compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Arm instances on Compute Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud offers a range of Arm powered servers in Compute Engine through the N4A, C4A, A5X, A4X Max, and A4X machine series. Arm architecture is optimized for power efficiency, and as a result can yield better price for performance.

Arm processors are common in standard servers due to their power efficiency as compared to x86 servers. Mobile phones and laptops are examples of devices that run on an Arm processor. With an Arm CPU's reduced instruction set, fewer instructions equals greater performance speed with lower battery and power consumption.

N4A uses Google's Axion Arm processor with the Neoverse N3 processor. C4A uses the Axion Arm processor based on the Arm Neoverse V2 processor. The Neoverse V2 is the first V-series CPU to have Armv9 performance, power, and security enhancements. It is designed for high performance computing, machine learning, and general-purpose cloud computing.

Consider using N4A or C4A general-purpose Arm instances for any of the following purposes:

  * Run compute-intensive workloads that require the ability to scale usage quickly when needed.
  * Optimize for price-performance on Arm-compatible workloads.
  * Build on modern, open source software stacks.
  * Develop and test mobile or embedded systems which use an Arm CPU.
  * Evaluate whether your workload is suitable for an Arm CPU.



To use GPUs with an Arm-based CPU, choose the A5X, A4X Max, or A4X machine series, which run on the NVIDIA rack-scale architecture. Instances in these machine series have attached NVIDIA Vera Rubin or NVIDIA Grace Blackwell superchips. These machine series are optimized for massively parallelized Compute Unified Device Architecture (CUDA) compute workloads.

Consider using A5X, A4X Max, or A4X accelerator-optimized machine series for any of the following purposes:

  * Machine learning (ML)
  * High performance computing (HPC)
  * Massively-parallel workloads



## A5X, A4X Max, and A4X machine series

**Caution:** The [Compute Engine Service Level Agreement (SLA)](https://cloud.google.com/compute/sla) doesn't apply to the A5X, A4X Max, and A4X machine series.

The [A5X](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a5x-instances) and [A4X Max and A4X](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms) machine series have both Arm-based CPUs and attached GPUs. Each machine type in these series has two sockets with NVIDIA Arm CPUs connected to four GPUs with fast chip-to-chip (NVLink-C2C) communication.

  * **A5X** : offers bare metal instances with 176 vCPUs and 1,440 GB of memory. It uses NVIDIA Vera Rubin superchips, which have two 88-core NVIDIA Vera Armv9.2 CPUs (176 cores total) and four NVIDIA Rubin GPUs that offer 288 GB of High Bandwidth Memory (HBM4) per GPU, for a total of 1,152 GB of GPU memory. A5X is available as a bare metal instance in the `a5x-highgpu-4g-metal` machine type.
  * **A4X Max** : offers machine types with up to 144 vCPUs and 960 GB of memory. It uses NVIDIA GB300 superchips, which have B300 GPUs that offer 279 GB memory per GPU. A4X Max is available as a bare metal instance in the `a4x-maxgpu-4g-metal` machine type.
  * **A4X** : offers machine types that have up to 140 vCPUs and 884 GB of memory. It uses NVIDIA GB200 superchips, which have B200 GPUs that offer 186 GB memory per GPU. A4X is available in the `a4x-highgpu-4g` machine type.



### Storage options for A5X, A4X Max, and A4X instances

A5X, A4X Max, and A4X instances support Google Cloud Hyperdisk attached storage. A5X instances include 48,000 GiB of [Local SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd) storage, and A4X Max and A4X instances include 12,000 GiB. Compute Engine automatically attaches the Local SSD disks to your instances during instance creation.

### OS images

A5X, A4X Max, and A4X instances support public Arm-based [OS images](https://docs.cloud.google.com/compute/docs/images/os-details). You can also [create custom images](https://docs.cloud.google.com/compute/docs/images/create-custom) by using a public Arm-based OS image.

## N4A machine series

[N4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series) is the latest Google Axion-based instance, built on Neoverse N3 CPU. N4A offers machine types with up to 64 vCPUs and 512 GB of DDR5 memory and Titanium infrastructure processing unit (IPU) support. N4A uses next-generation [dynamic resource management](https://docs.cloud.google.com/compute/docs/dynamic-resource-management) and is available in `standard`, `highmem`, and `highcpu` machine types with the option to customize your machine type and add extended memory.

N4A supports standard networking up to 50 Gbps with the [gVNIC networking interface](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). N4A also supports the NVMe disk interface with Hyperdisk Balanced, Hyperdisk Balanced High Availability, and Hyperdisk Throughput storage.

## C4A machine series

[C4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series) is the first Arm-based compute machine series built on Google's Axion Arm64-based CPU. C4A offers machine types with up to 72 vCPUs and 576 GB of DDR5 memory. C4A is available in `standard`, `highmem`, and `highcpu` machine types.

C4A offers two bare metal machine types:

  * `c4a-highmem-96-metal` with 96 GB vCPUs and 768 GB of DDR5 memory
  * `c4a-standard-96-metal` with 96 GB vCPUs and 384 GB of DDR5 memory



C4A is built on [Titanium](https://cloud.google.com/titanium) which uses network offloads and enables per VM Tier_1 networking performance of up to 100 Gbps with the [gVNIC networking interface](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). C4A also supports the NVMe and IDPF disk interfaces with Hyperdisk volumes.

### Simultaneous multithreading

For the C4A machine series, each vCPU is backed by a single core with no [simultaneous multithreading (SMT)](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core). Thus, C4A instances deliver greater performance per vCPU compared to a compute instance with SMT enabled. While SMT provides benefits to certain workloads, single-threaded cores are ideal for compute-intensive workloads because the processes can access the entire core instead of sharing it with other processes.

### OS images

C4A and N4A compute instances support public Arm-based [OS images](https://docs.cloud.google.com/compute/docs/images/os-details). You can also [create custom images](https://docs.cloud.google.com/compute/docs/images/create-custom) using a publicly-available Arm-based image.

## Tau T2A machine series

The [Tau T2A Arm](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machines) machine series runs on the 64 core Ampere Altra Arm processor at 3.0 GHz all-core frequency. Tau T2A makes it possible to run workloads that run best, or exclusively, on Arm.

The [Tau T2A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machines) has predefined machine types of up to 48 physical cores with 4 GB of memory per vCPU. Tau T2A machine types run within a single [NUMA](https://www.kernel.org/doc/html/v4.18/vm/numa.html) node.

Tau T2A machine types support only the NVMe interface for storage, and [Google virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/networking/using-gvnic) for networking. Virtio-Net and SCSI interfaces are not supported. All publicly-available Arm [OS images](https://docs.cloud.google.com/compute/docs/images/os-details) are configured to use the NVMe and gVNIC interfaces. gVNIC is a network interface that is designed specifically for Compute Engine. It provides better performance and supports higher network bandwidths and throughput.

For this machine series, each vCPU is backed by a single core with no simultaneous multithreading (SMT).

## Workload recommendations

The C4A machine series is an excellent choice for a wide range of scale-out and compute-intensive workloads, especially when price performance is a key concern. Consider C4A when you are deploying workloads such as the following:

  * ML data processing
  * ML inferencing and model serving
  * App serving, web serving, and game serving
  * Embedded systems development
  * Development on CI/CD on Arm
  * Video and image encoding, transcoding, and processing
  * Digital advertising exchanges and serving
  * Cache servers
  * Computational drug discovery
  * Android development
  * Autonomous or conventional automotive software development



## What's next

  * Review the specifications and features of the [A5X](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a5x-instances) and [A4X Max and A4X](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms) machine series.
  * Review the specifications for the [N4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series).
  * Review the specifications for the [C4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series).
  * Learn about available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms) for Google Cloud.
  * [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-public-image) using an Arm OS image.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/docs/compute-area/vcpus/
title: Understand vCPUs \u00a0|\u00a0 Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:27:14.131296+00:00
---

# Understand vCPUs  |  Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/compute-area/vcpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Guides ](https://docs.cloud.google.com/docs/compute-area/overview)



Send feedback 

#  Understand vCPUs Stay organized with collections  Save and categorize content based on your preferences. 

Compute Engine assigns vCPUs to your virtual machine (VM) or bare metal instances when you create them. This document explains how vCPUs map to physical hardware to help you optimize performance, manage costs, and comply with software licensing requirements.

## Understand vCPUs

A virtual CPU (vCPU) represents a unit of central processing unit (CPU) power assigned to your compute instance. Depending on the underlying processor architecture, a vCPU is scheduled to run on either a single hardware execution thread or on an entire dedicated physical CPU core.

vCPUs are part of a CPU platform. A CPU platform is a CPU-based configuration that includes the following:

  * CPU processor type
  * Instruction sets (such as AVX2 and AVX-512)
  * Cache sizes
  * Clock speeds
  * NUMA splits
  * Memory access seek times
  * On-chip accelerators



### Allocating vCPUs to a compute instance

To create a VM or bare metal instance (collectively referred to as a _compute instance_), you use a machine type. The machine type determines the resources that Compute Engine allocates to the instance. For example, the `c4-standard-4` machine type creates a VM with 4 vCPUs and 16 GB of memory.

To help you choose the right machine type for your workload, Compute Engine groups machine types into machine families and machine series.

  * **Machine family** : a curated set of processor and hardware configurations optimized for specific workloads, for example, [General-purpose](https://docs.cloud.google.com/compute/docs/general-purpose-machines), [Accelerator-optimized](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines), or [Memory-optimized](https://docs.cloud.google.com/compute/docs/memory-optimized-machines).
  * **Machine series** : a specific combination of CPU processor, hardware, and networking capabilities within a machine family. Each series focuses on a different aspect of computing power or performance. For example, the E series offers efficient VMs at a low cost, while the C series offers better and more consistent performance than the E series.

    * A machine series can have multiple generations, such as C3 and C4. A higher generation or series number indicates newer underlying CPU processors or technologies. For example, the M4 series, which runs on 5th generation Intel Xeon processors (also known as Emerald Rapids), is a newer generation than the M3 machine series, which runs on 3rd generation Intel Xeon processors (also known as Ice Lake).
    * The underlying architecture for a machine series and machine type is indicated by a trailing letter in the machine series name. For example, the 4th generation C machine series is available as C4 (Intel), C4D (AMD), C4A (Arm), or C4N (network-optimized).



### Physical core mapping and simultaneous multithreading

On most x86 processors, each physical CPU core supports two hardware execution threads. [Intel Xeon processors](https://www.intel.com/content/www/us/en/products/details/processors/xeon.html) use Intel Hyper-Threading and [AMD EPYC processors](https://www.amd.com/en/products/processors/server/epyc.html) use simultaneous multithreading (SMT). For these processors, Compute Engine implements each vCPU as a single hardware thread running on a physical core. Thus, two vCPUs share a single physical CPU core (a 2:1 ratio of vCPUs to physical cores). For example, a VM with 4 vCPUs uses 2 physical CPU cores with SMT.

On certain machine series and processor architectures, Compute Engine doesn't use SMT. Instead, each vCPU maps directly to one dedicated physical CPU core (a 1:1 ratio of vCPUs to physical cores):

  * **Arm processors** : on Arm64-based machine series such as N4A, C4A, or A4X, the hardware architecture uses single-threaded cores. Each vCPU represents one full physical core.
  * **Compute-optimized machine series** : both the H4D and H3 machine series don't support SMT. Each vCPU represents an entire physical CPU core, providing high single-thread performance and eliminating resource contention between threads.
  * **Tau machine series** : for the Tau T2A (powered by Ampere Altra processors) and Tau T2D machine series (powered by 3rd generation AMD EPYC Milan processors), Compute Engine disables SMT by design. These compute instance types always have one vCPU per core.
  * **Bare metal instances** : for bare metal instances, a vCPU is equivalent to a CPU. The number of vCPUs available to the instance is equivalent to the number of hardware threads on the host server. You can't manually adjust or set the threads per core.



To meet specific workload or software licensing requirements, you can customize how vCPUs appear to your guest operating system. For more information, see [Customize the number of visible CPU cores](https://docs.cloud.google.com/compute/docs/instances/customize-visible-cores). For a list of the machine series and architectures that don't use SMT, see [Set the number of threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core).

### Dedicated versus shared-core vCPUs

When you choose a machine type, your vCPUs are mapped to either a CPU hardware thread or use a shared-core resource model:

  * **Full vCPUs** : standard, high-memory, high-CPU, and custom machine types allocate a hardware execution thread or physical core for each vCPU. 
    * For N4, N4A, N4D, and E2 machine series in the general-purpose machine family, the [dynamic resource management (DRM)](https://docs.cloud.google.com/compute/docs/dynamic-resource-management) system ensures that every active vCPU has an available hardware execution thread backing it. DRM enables Compute Engine to better use the available physical CPUs by scheduling compute instances to servers based on resource demand, and scheduling vCPU threads to physical CPUs such that wait time is minimized. N1, N2, and N2D machine series in the general-purpose machine family use standard host scheduling.
    * For C, M, G, Z, and A machine series, vCPU resources are exclusively assigned to your instance and never share execution cycles with other compute instances.
  * **Shared-core vCPUs** : shared-core machine types are `e2-micro`, `e2-small`, `e2-medium`, `f1-micro`, and `g1-small`. These machine types timeshare a physical CPU core using context switching. Instead of dedicated hardware threads, these shared-core VMs sustain a specific fraction of physical core time:

    * `e2-micro` sustains 2 vCPUs at 12.5% of [CPU time](https://wikipedia.org/wiki/CPU_time) each (25% total).
    * `e2-small` sustains 2 vCPUs at 25% of CPU time each (50% total).
    * `e2-medium` sustains 2 vCPUs at 50% of CPU time each (100% total).
    * `f1-micro` sustains 1 vCPU for up to 20% of CPU time.
    * `g1-small` sustains 1 vCPU for up to 50% of CPU time.

Compared to VMs with full vCPUs, VMs with shared-core vCPUs provide a cost-effective option for running small, non-resource intensive applications, microservices, or development or test workloads that don't require continuous peak CPU throughput.




## vCPU performance characteristics

The processing performance of a vCPU depends on its CPU platform, clock speed, cache hierarchy, multi-threading dynamics, and resource scheduling.

### CPU platforms and instruction sets

Compute Engine offers compute instances that run on multiple generations of Intel, AMD, Arm, and custom Google processors. Each CPU platform introduces microarchitecture enhancements and specialized instruction sets:

  * **Advanced Vector Extensions (AVX-512)** : available on Intel platforms (such as Ice Lake, Emerald Rapids, and Sapphire Rapids) and AMD EPYC platforms (Genoa and Turin), AVX-512 accelerates vector math, scientific computing, and data compression.
  * **AMX and VNNI** : These extensions accelerate deep learning inference and matrix operations directly on the vCPU. 
    * **Advanced Matrix Extensions (AMX)** is available on the Intel processors (Intel Xeon 4th generation Sapphire Rapids and later).
    * **Vector Neural Network Instructions (VNNI)** is available on both Intel and AMD EPYC processors (Genoa 4th Generation and newer).
  * **Arm NEON and SVE** : Arm NEON, available on the Ampere Altra CPU platform, and Scalable Vector Extension (SVE), available on Google Axion and NVIDIA Grace CPU platforms, provide scalable vector execution for cloud-native web workloads.



### Clock speed and turbo frequency

A vCPU executes instructions at the base clock frequency of its underlying physical processor. When workloads demand additional processing power and thermal headroom allows, processors automatically increase frequency to an all-core turbo frequency or single-core turbo frequency.

Certain machine series operate at the highest sustained clock speeds in Compute Engine. For example, C4 running on Granite Rapids has up to 3.9 GHz all-core turbo frequency, and A3 Mega or A3 High have up to 3.8 GHz all-core turbo frequency. Choose high-frequency vCPUs for single-threaded applications, electronic design automation (EDA), and game servers.

To see the frequencies for each CPU platform used by Compute Engine, see [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).

### Multi-threading resource sharing

On machine types with SMT active (2 vCPUs per core), the two hardware execution threads share the physical core's Level 1 (L1) instruction and data caches, Level 2 (L2) cache, execution units, and translation lookaside buffers (TLBs).

  * **I/O-bound and concurrent workloads** : for web servers, API gateways, and database operations with frequent memory access, SMT increases overall core throughput by running instructions on one thread while the other thread waits for memory retrieval.
  * **Compute-bound workloads** : for applications that continuously saturate floating-point units or L1/L2 caches, sharing execution units between two vCPUs can cause resource contention. If your workload experiences contention on SMT-enabled compute instances, then consider disabling SMT by setting threads per core to 1 or migrating to a machine series with dedicated physical cores (such as C4A or H4D).



### Dynamic resource management and performance monitoring

Compute Engine uses specialized hardware and software optimizations to maintain predictable vCPU latency:

  * **Google Titanium architecture** : next-generation machine series (including N4, N4D, N4A, C3, C3D, and C4) use Google Titanium offload cards, a custom CPU scheduler, and performance-aware live migration. Dynamic resource management preserves NUMA (Non-Uniform Memory Access) affinity and minimizes noisy-neighbor interference.
  * **Dynamic resource management for E2** : for E2 VMs, the hypervisor dynamically maps virtual CPU and memory to physical resources on demand. This dynamic mapping drives cost efficiency by optimizing the use of physical resources.
  * **Performance monitoring unit (PMU)** : you can enable the [PMU](https://docs.cloud.google.com/compute/docs/pmu-overview) on supported machine series (such as C4, M4, and A4X) to access low-level hardware counters. Profiling tools use PMU counters to track branch mispredictions, cache misses, and instructions per cycle (IPC).
  * **Ops Agent** : you can install the [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent) on your compute instances to monitor CPU utilization and gather system-level telemetry. The Ops Agent sends this data to [Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs) to help you analyze and optimize vCPU performance.



## Pricing considerations

When you budget and plan capacity for your workloads, consider how Compute Engine bills for vCPUs and the discount models available.

### Resource billing granularity

For most machine series, Compute Engine bills vCPUs and system memory as separate dedicated resources. You pay for instances on a per-second basis, with a **1-minute minimum billing duration** for every compute instance that you start. After the first minute, you pay only for the exact seconds your instance remains running.

For shared-core machine types (such as E2 shared-core and N1 shared-core), Compute Engine bundles vCPUs and memory into a single combined hourly rate rather than billing them as individual resources.

You can review vCPU billing rates on the [VM instance pricing](https://cloud.google.com/products/compute/pricing) pages.

### Cost optimization and discounts

You can reduce vCPU billing costs by using the following pricing options:

  * [**Committed use discounts (CUDs)**](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview): if your workloads have predictable, steady-state vCPU requirements, then you can purchase 1-year or 3-year commitments to receive discounts of up to 55% to 70% off on-demand prices. Compute Engine offers **resource-based CUDs** for specific machine series in a region and **spend-based flex CUDs** that apply across multiple machine series and regions. You can share CUDs across projects within your Cloud Billing account.
  * [**Sustained use discounts (SUDs)**](https://docs.cloud.google.com/compute/docs/sustained-use-discounts): for eligible machine series (such as N1, N2, N2D, C2, M1, and M2), Compute Engine automatically applies SUDs when your vCPUs run for more than 25% of a billing month. Running a VM instance continuously for the entire month provides up to a 20% or 30% discount, depending on the machine series. Machine series with lowered on-demand pricing (including E2, N4, C3, C4, Tau T2A, and A3) don't offer SUDs.
  * [**Spot VMs**](https://docs.cloud.google.com/compute/docs/instances/spot): for fault-tolerant, stateless, or batch workloads, Spot VMs offer up to 60% to 91% off standard on-demand vCPU prices. Compute Engine can stop or reclaim Spot VMs at any time to reclaim capacity.
  * [**Sole-tenant nodes and vCPU overcommit**](https://docs.cloud.google.com/compute/docs/nodes/overcommitting-cpus-sole-tenant-vms): when you run VM instances on sole-tenant nodes, you pay for the dedicated physical host server rather than individual vCPUs. On sole-tenant nodes, you can configure **CPU overcommit** (up to a 2:1 ratio) to schedule more vCPUs across your VM instances than the physical host has cores, reducing compute costs for developer or test environments.
  * [**Dynamic Workload Scheduler (DWS)**](https://cloud.google.com/blog/products/compute/introducing-dynamic-workload-scheduler): for AI or ML workloads, you can optimize vCPU costs and improve resource availability by using DWS. 
    * **Flex-start VMs** : use for cost-effective and flexible scheduling of workloads that run for up to 7 days.
    * **Future reservation requests in calendar mode** : use to reserve resources for up to 90 days at a specific future date and time.
  * [**Rightsizing recommendations**](https://docs.cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances): Compute Engine analyzes historical vCPU utilization metrics and provides automated machine type recommendations and idle compute instance recommendations. Applying these recommendations helps you resize overprovisioned vCPUs or stop idle instances.



## Machine series availability

The following table maps vCPU architecture models, multi-threading ratios, and maximum vCPU counts across Compute Engine machine series. The maximum vCPU counts reflect the largest machine type in each series, including bare metal instances.

Machine family | Machine series | Processor architecture | vCPU to core ratio | Max vCPUs | Shared-core option  
---|---|---|---|---|---  
**General-purpose** | `E2` | Intel Xeon / AMD EPYC | 2 vCPUs : 1 core (SMT) | 32 vCPUs | Yes (`e2-micro`, `e2-small`, `e2-medium`)  
General-purpose | `N1` | Multiple generations of Intel Xeon processors | 2 vCPUs : 1 core (SMT) | 96 vCPUs | Yes (`f1-micro`, `g1-small`)  
General-purpose | `N2` | Intel Xeon (Cascade Lake / Ice Lake) | 2 vCPUs : 1 core (SMT) | 128 vCPUs | No  
General-purpose | `N2D` | AMD EPYC (Rome / Milan) | 2 vCPUs : 1 core (SMT) | 224 vCPUs | No  
General-purpose | `N4` | 5th gen Intel Xeon (Emerald Rapids) | 2 vCPUs : 1 core (SMT) | 80 vCPUs | No  
General-purpose | `N4D` | 5th gen AMD EPYC (Turin) | 2 vCPUs : 1 core (SMT) | 96 vCPUs | No  
General-purpose | `N4A` | Google Axion (Arm64) | 1 vCPU : 1 core (No SMT) | 64 vCPUs | No  
General-purpose | `C3` | 4th gen Intel Xeon (Sapphire Rapids) | 2 vCPUs : 1 core (SMT) | 176 vCPUs | No  
General-purpose | `C3D` | 4th gen AMD EPYC (Genoa) | 2 vCPUs : 1 core (SMT) | 360 vCPUs | No  
General-purpose | `C4` | 5th gen Intel Xeon (Emerald Rapids) and 6th gen Intel Xeon (Granite Rapids) | 2 vCPUs : 1 core (SMT) | 288 vCPUs | No  
General-purpose | `C4A` | Google Axion (Arm64) | 1 vCPU : 1 core (No SMT) | 96 vCPUs | No  
General-purpose | `C4D` | 5th gen AMD EPYC (Turin) | 2 vCPUs : 1 core (SMT) | 384 vCPUs | No  
General-purpose | `Tau T2A` | Ampere Altra (Arm64) | 1 vCPU : 1 core (No SMT) | 48 vCPUs | No  
General-purpose | `Tau T2D` | 3rd gen AMD EPYC (Milan) | 1 vCPU : 1 core (SMT disabled) | 60 vCPUs | No  
**Compute-optimized** | `C2` | Intel Xeon (Cascade Lake) | 2 vCPUs : 1 core (SMT) | 60 vCPUs | No  
Compute-optimized | `C2D` | AMD EPYC (Milan) | 2 vCPUs : 1 core (SMT) | 112 vCPUs | No  
Compute-optimized | `H3` | 4th gen Intel Xeon (Sapphire Rapids) | 1 vCPU : 1 core (No SMT) | 88 vCPUs | No  
Compute-optimized | `H4D` | 5th gen AMD EPYC (Turin) | 1 vCPU : 1 core (No SMT) | 192 vCPUs | No  
**Network-optimized** | `C4N` | 5th gen Intel Xeon (Emerald Rapids) | 2 vCPUs : 1 core (SMT) | 192 vCPUs | No  
**Memory-optimized** | `X4` | 4th gen Intel Xeon (Sapphire Rapids) | 2 vCPUs : 1 core (SMT) | 1,920 vCPUs | No  
Memory-optimized | `M1` | Intel Xeon (Skylake and Broadwell) | 2 vCPUs : 1 core (SMT) | 160 vCPUs | No  
Memory-optimized | `M2` | 2nd gen Intel Xeon (Cascade Lake) | 2 vCPUs : 1 core (SMT) | 416 vCPUs | No  
Memory-optimized | `M3` | 3rd gen Intel Xeon (Ice Lake) | 2 vCPUs : 1 core (SMT) | 128 vCPUs | No  
Memory-optimized | `M4` / `M4N` | 5th gen Intel Xeon (Emerald Rapids) | 2 vCPUs : 1 core (SMT) | 224 vCPUs | No  
**Storage-optimized** | `Z3` | 4th gen Intel Xeon (Sapphire Rapids) | 2 vCPUs : 1 core (SMT) | 192 vCPUs | No  
Storage-optimized | `Z4D` | 5th gen AMD EPYC (Turin) | 2 vCPUs : 1 core (SMT) | 288 vCPUs | No  
Storage-optimized | `Z4M` | 5th gen Intel Xeon (Emerald Rapids) | 1 vCPU : 1 core (No SMT) | 192 vCPUs | No  
**Accelerator-optimized** | `A4X Max` | NVIDIA Grace | 1 vCPU : 1 core (No SMT) | 144 vCPUs | No  
Accelerator-optimized | `A4X` | NVIDIA Grace | 1 vCPU : 1 core (No SMT) | 140 vCPUs | No  
Accelerator-optimized | `A4` | 5th gen Intel Xeon (Emerald Rapids) paired with NVIDIA GPUs | 2 vCPUs : 1 core (SMT) | 224 vCPUs | No  
Accelerator-optimized | `A3` | Intel Xeon (Emerald Rapids and Sapphire Rapids) paired with NVIDIA GPUs | 2 vCPUs : 1 core (SMT) | 224 vCPUs | No  
Accelerator-optimized | `A2` | 2nd gen Intel Xeon (Cascade Lake) paired with NVIDIA GPUs | 2 vCPUs : 1 core (SMT) | 96 vCPUs | No  
Accelerator-optimized | `G4` | 5th gen AMD EPYC (Turin) paired with NVIDIA GPUs | 2 vCPUs : 1 core (SMT) | 384 vCPUs | No  
Accelerator-optimized | `G2` | 2nd gen Intel Xeon (Cascade Lake) paired with NVIDIA GPUs | 2 vCPUs : 1 core (SMT) | 96 vCPUs | No  
  
For detailed specifications on memory per vCPU, network bandwidth, and local disk support across all series, see the [Machine resource guide](https://docs.cloud.google.com/compute/docs/machine-resource).

## What's next

  * Compare vCPU and memory specifications in the [Machine families resource and comparison guide](https://docs.cloud.google.com/compute/docs/machine-resource).
  * Learn about available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms) on Compute Engine.
  * Review [shared-core VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#sharedcore) to learn about shared-core instances.
  * Learn how to apply [machine type recommendations](https://docs.cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances) and [Idle VM recommendations](https://docs.cloud.google.com/compute/docs/instances/idle-vm-recommendations-overview) to optimize vCPU utilization.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

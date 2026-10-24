---
url: https://docs.cloud.google.com/alloydb/docs/choose-machine-type/
title: Choose an AlloyDB machine type \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-24T11:25:11.452151+00:00
---

# Choose an AlloyDB machine type  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/choose-machine-type/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Choose an AlloyDB machine type Stay organized with collections  Save and categorize content based on your preferences. 

To optimize performance and cost efficiency for your AlloyDB for PostgreSQL workload, you can select a machine series and shape tailored to your compute, memory, and caching requirements. Comparing the supported AlloyDB machine series, their target workload profiles, and regional availability helps you configure instances for workloads ranging from large datasets that require high-capacity caches to high-concurrency transactional applications.

## Machine series overview

AlloyDB offers the following machine series, each built on a different underlying Google Cloud compute platform and optimized for specific performance characteristics.

  
**Machine series** |   
**Core platform and CPU** |   
**Primary workload focus** |   
**Key performance differentiator**  
---|---|---|---  
  
N2 |   
3rd Generation Intel x86 processors (Ice Lake) |   
Legacy, general purpose |   
Available in all regions.  
  
C4A |   
Google Axion ARM |   
Price performance, high throughput |   
Provides the best transaction throughput for cache-fitting workloads.  
  
C4 |   
6th generation Intel x86 processors (Granite Rapids) with Titanium SSD.  |   
Low latency or very large database workloads |   
Provides the largest machine options with local SSDs for the fastest cache.  
  
Z3 |   
4th generation Intel x86 processors (Sapphire Rapids) with Titanium SSD |   
Large working dataset, storage intensive |   
Allows caching of more data per vCPU; optimized for storage-dense, I/O-intensive workloads  
  
## Machine series configuration for primary and read pool instances

To optimize performance and cost, an AlloyDB cluster lets you configure and scale machine series and machine types independently across your primary instance and read pool instances.

### Cross-machine-series configurations

An AlloyDB cluster supports cross-machine-series configurations, which let you run the primary instance and read pool instances on different compute machine series. For example, you can provision the primary instance on the N2 machine series and provision read pool instances on the C4, C4A, or Z3 machine series.

**Note:** For high-availability (HA) clusters, the standby instance automatically uses the same machine series and machine type as the primary instance.

### Vertical scaling for primary instances

To adapt to workload changes, you can vertically scale an AlloyDB primary instance in the following ways:

  * Scale the size within a machine series: Increase or decrease the vCPU and memory allocation within the existing machine series. For example, scale a primary instance from an N2 machine type with 8 vCPUs to an N2 machine type with 16 vCPUs.

  * Change the machine series shape: Transition the primary instance to a different machine series to optimize workload performance or hardware efficiency. For example, change a primary instance from an N2 machine type with 16 vCPUs to an Axion-based C4A machine type with 32 vCPUs.




### Horizontal scaling for read pool instances

You can scale a read pool instance horizontally by adding or removing nodes behind a single load-balanced reader IP endpoint. All nodes in a read pool instance must use the same machine series and machine type. For example, if you add a third node to a read pool instance that contains two N2 nodes, then the third node must also use the same N2 machine type, not a C4, C4A, or Z3 machine type.

### Machine series transitions for read pool instances

You can switch a read pool instance to a different machine series, such as from N2 to C4, C4A, or Z3, which transitions all nodes in the read pool instance to the target machine series and machine type. To serve read traffic across multiple machine series or machine types simultaneously, deploy separate read pool instances for each configuration.

**Caution:** Changing the machine series of a read pool instance replaces its existing nodes. When you update a read pool instance from N2 nodes to C4, C4A, or Z3 nodes, AlloyDB doesn't add the replacement nodes to the existing pool. Instead, AlloyDB provisions replacement nodes in the target machine series, routes traffic to the replacement nodes while keeping the read pool instance's IP address unchanged, and deletes the original nodes. This update requires slight downtime and causes a momentary interruption in active client connections.

## Machine series availability for AlloyDB clusters

You can choose one of the following machine series:

  * **N2** : this machine series provides a balanced price-to-performance ratio for a variety of AlloyDB workloads.
  * **C4A Axion-based** : this machine series provides optimized price-performance and delivers predictable high performance for high demand AlloyDB workloads.
  * **C4** : this machine series provides excellent performance and the largest vertical scale in AlloyDB.
  * **Z3** : this machine series is optimized for storage-dense, I/O-intensive workloads.




### N2

The following machine types are available for instances for the N2 machine series. For more information, see [N2 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_series).

  
**Machine type** |   
**vCPUs** |   
**Memory (GB)**  
---|---|---  
` n2-highmem-2 ` |   
2 |   
16 GB RAM  
` n2-highmem-4 ` |   
4 |   
32 GB RAM  
` n2-highmem-8 ` |   
8 |   
64 GB RAM  
` n2-highmem-16 ` |   
16 |   
128 GB RAM  
` n2-highmem-32 ` |   
32 |   
256 GB RAM  
` n2-highmem-64 ` |   
64 |   
512 GB RAM  
` n2-highmem-96 ` |   
96 |   
768 GB RAM  
` n2-highmem-128 ` |   
128 |   
864 GB RAM  
  
### C4A Axion-based

The following machine types are available for instances for the C4A Axion-based machine series. For more information, see [C4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series).

  
**Machine type** |   
**vCPUs** |   
**Memory (GB)**  
---|---|---  
` c4a-highmem-1 ` |   
1 |   
8 GB RAM  
` c4a-highmem-2-lssd ` |   
2 |   
16 GB RAM  
` c4a-highmem-4-lssd ` |   
4 |   
32 GB RAM  
` c4a-highmem-8-lssd ` |   
8 |   
64 GB RAM  
` c4a-highmem-16-lssd ` |   
16 |   
128 GB RAM  
` c4a-highmem-32-lssd ` |   
32 |   
256 GB RAM  
` c4a-highmem-48-lssd ` |   
48 |   
384 GB RAM  
` c4a-highmem-64-lssd ` |   
64 |   
512 GB RAM  
` c4a-highmem-72-lssd ` |   
72 |   
576 GB RAM  
  
### C4

The following machine types are available for instances for the C4 machine series. For more information, see [C4 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series).

  
**Machine type** |   
**vCPUs** |   
**Memory (GB)**  
---|---|---  
` c4-highmem-4-lssd ` |   
4 |   
32 GB RAM  
` c4-highmem-8-lssd ` |   
8 |   
64 GB RAM  
` c4-highmem-16-lssd ` |   
16 |   
128 GB RAM  
` c4-highmem-24-lssd ` |   
24 |   
192 GB RAM  
` c4-highmem-32-lssd ` |   
32 |   
256 GB RAM  
` c4-highmem-48-lssd ` |   
48 |   
384 GB RAM  
` c4-highmem-96-lssd ` |   
96 |   
768 GB RAM  
` c4-highmem-144-lssd ` |   
144 |   
1152 GB RAM  
` c4-highmem-192-lssd ` |   
192 |   
1536 GB RAM  
` c4-highmem-288-lssd ` |   
288 |   
2304 GB RAM  
  
### Z3 standard-lssd

The following machine types are available for instances for the Z3 machine series. For more information, see [Z3 machine series](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3-standard-lssd).

  
**Machine type** |   
**vCPUs** |   
**Memory (GB)**  
---|---|---  
` z3-highmem-14-standard-lssd ` |   
14 |   
112 GB RAM  
` z3-highmem-22-standard-lssd ` |   
22 |   
176 GB RAM  
` z3-highmem-44-standard-lssd ` |   
44 |   
352 GB RAM  
` z3-highmem-88-standard-lssd ` |   
88 |   
704 GB RAM  
  
### Z3 high-lssd

The following machine types are available for instances for the Z3 `high-lssd` machine series. For more information, see [Z3 machine series](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3-highlssd).

  
**Machine type** |   
**vCPUs** |   
**Memory (GB)**  
---|---|---  
` z3-highmem-8-high-lssd ` |   
8 |   
64 GB RAM  
` z3-highmem-16-high-lssd ` |   
16 |   
128 GB RAM  
` z3-highmem-22-high-lssd ` |   
22 |   
176 GB RAM  
` z3-highmem-32-high-lssd ` |   
32 |   
256 GB RAM  
` z3-highmem-44-high-lssd ` |   
44 |   
352 GB RAM  
  
## Regional availability methodology

AlloyDB helps you deploy and scale high-availability database solutions wherever you need them.

AlloyDB requires high availability (HA) to protect your mission-critical data. This means that to launch any machine series in a given Google Cloud region, the underlying Compute Engine platform supporting that machine series must be available in all three zones within that region. This requirement ensures that when you choose a region for your AlloyDB cluster, the necessary infrastructure is redundant and geographically distributed in that area, which provides the failover capabilities that you need.

### Machine series regional deployments

Use the following table to learn where you can find AlloyDB platforms. N2 offers General Availability, and C4A Axion-based offers the widest modern coverage.

  
**Region** |   
**Machine series**  
---|---  
N2 | C4A | C4 | Z3  
` africa-south1 ` |   
✅ |   
– |   
– |   
–  
` asia-east1 ` |   
✅ |   
✅ |   
✅ |   
–  
` asia-east2 ` |   
✅ |   
– |   
– |   
–  
` asia-northeast1 ` |   
✅ |   
– |   
✅ |   
✅  
` asia-northeast2 ` |   
✅ |   
– |   
–  
` asia-northeast3 ` |   
✅ |   
– |   
✅ |   
–  
` asia-south1 ` |   
✅ |   
– |   
– |   
–  
` asia-south2 ` |   
✅ |   
– |   
✅ |   
–  
` asia-southeast1 ` |   
✅ |   
✅ |   
✅ |   
✅  
` asia-southeast2 ` |   
✅ |   
– |   
– |   
–  
` asia-southeast3 ` |   
✅ |   
– |   
– |   
–  
` australia-southeast1 ` |   
✅ |   
– |   
– |   
–  
` australia-southeast2 ` |   
✅ |   
– |   
– |   
–  
` europe-central2 ` |   
✅ |   
– |   
– |   
–  
` europe-southwest1 ` |   
✅ |   
– |   
– |   
–  
` europe-north1 ` |   
✅ |   
– |   
– |   
–  
` europe-north2 ` |   
✅ |   
– |   
– |   
–  
` europe-west1 ` |   
✅ |   
✅ |   
✅ |   
✅  
` europe-west2 ` |   
✅ |   
✅ |   
✅ |   
✅  
` europe-west3 ` |   
✅ |   
✅ |   
– |   
✅  
` europe-west4 ` |   
✅ |   
✅ |   
✅ |   
✅  
` europe-west6 ` |   
✅ |   
– |   
– |   
–  
` europe-west8 ` |   
✅ |   
– |   
– |   
–  
` europe-west9 ` |   
✅ |   
– |   
– |   
–  
` europe-west10 ` |   
✅ |   
– |   
– |   
–  
` europe-west12 ` |   
✅ |   
– |   
– |   
–  
` me-central1 ` |   
✅ |   
– |   
– |   
–  
` me-central2 ` |   
✅ |   
– |   
– |   
–  
` me-west1 ` |   
✅ |   
– |   
– |   
–  
` northamerica-northeast1 ` |   
✅ |   
– |   
– |   
–  
` northamerica-northeast2 ` |   
✅ |   
– |   
✅ |   
–  
` northamerica-south1 ` |   
✅ |   
– |   
✅ |   
✅  
` southamerica-east1 ` |   
✅ |   
– |   
– |   
–  
` southamerica-west1 ` |   
✅ |   
– |   
– |   
–  
` us-central1 ` |   
✅ |   
✅ |   
– |   
✅  
` us-east1 ` |   
✅ |   
✅ |   
– |   
✅  
` us-east4 ` |   
✅ |   
✅ |   
✅ |   
✅  
` us-east5 ` |   
✅ |   
– |   
✅ |   
✅  
` us-east7 ` |   
✅ |   
– |   
– |   
–  
` us-south1 ` |   
✅ |   
– |   
– |   
✅  
` us-west1 ` |   
✅ |   
– |   
✅ |   
✅  
` us-west2 ` |   
✅ |   
– |   
– |   
–  
` us-west3 ` |   
✅ |   
– |   
✅ |   
–  
` us-west4 ` |   
✅ |   
– |   
✅ |   
–  
  
## What's next

  * [Create a cluster and its primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create#procedure). 
  * Learn about [AlloyDB locations](https://docs.cloud.google.com/alloydb/docs/locations). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 

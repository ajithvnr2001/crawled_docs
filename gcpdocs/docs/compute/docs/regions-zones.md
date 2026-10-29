---
url: https://docs.cloud.google.com/compute/docs/regions-zones/
title: Regions and zones \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T06:14:30.527064+00:00
---

# Regions and zones  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/regions-zones/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Regions and zones Stay organized with collections  Save and categorize content based on your preferences. 

Compute Engine resources are hosted in multiple locations worldwide. These locations are composed of regions and zones.

_Regions_ are independent geographic areas that consist of _zones_. Zones and regions are logical abstractions of underlying physical resources. For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

Resources that live in a zone, such as [Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances) or zonal [disks](https://docs.cloud.google.com/compute/docs/disks), are referred to as zonal resources. Other resources, like [static external IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses#reservedaddress), are regional. Regional resources can be used by any resource in that region, regardless of zone, while zonal resources can only be used by other resources in the same zone. For example, to attach a zonal persistent disk to an instance, both resources must be in the same zone. Similarly, if you want to assign a static IP address to an instance, the instance must be in the same region as the static IP address.

Putting resources in different zones in a region reduces the risk of an infrastructure outage affecting all resources simultaneously. Putting resources in different regions provides an even higher degree of failure independence. This lets you design robust systems with resources spread across different failure domains.

Only certain resources are region- or zone-specific. Other resources, such as images, are global resources that can be used by any other resources across any location. For information on global, regional, and zonal Compute Engine resources, see [Global, Regional, and Zonal Resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources).

Google Cloud also offers specialized AI zones that provide high-capacity GPUs and TPUs for AI and ML workloads. These zones have unique characteristics, including specific network latency requirements and shared fate with a parent zone. For more information, see [AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones).

## Identifying a region or zone

Each region in Compute Engine contains a number of zones. Each zone name contains two parts that describe each zone in detail. The first part of the zone name is the **region** and the second part of the name describes the **zone** in the region:

  * **Region**

Regions are collections of zones. Zones have high-bandwidth, low-latency network connections to other zones in the same region. In order to deploy fault-tolerant applications that have high availability, Google recommends deploying applications across multiple zones and multiple regions. This helps protect against unexpected failures of components, up to and including a single zone or region.

Choose regions that make sense for your scenario. For example, if you only have customers in the US, or if you have specific needs that require your data to live in the US, it makes sense to store your resources in zones in the `us-central1` region or zones in the `us-east1` region.

  * **Zone**

A zone is a deployment area within a region. Zones which are specialized for AI and ML workloads are called AI zones. Non-AI zones are referred to as standard zones or just zones. Depending on how widely you want to distribute your resources, create compute instances across multiple zones in multiple regions for redundancy.

    * **Standard zone**

A standard zone name contains two parts: the **region** and the **zone** in the region. For example, the fully qualified name for zone `a` in region `us-central1` is `us-central1-a`.

    * **AI zone**

AI zones follow an extended naming convention to differentiate them from non-AI zones. For an AI zone, the `<zone>` variable consists of three parts: the string ai (to identify it as an AI zone), a number (indicating its deployment group), and a letter (indicating the shared software update schedule). For example, the fully qualified name for AI zone `ai2b` in region `us-west4` is `us-west4-ai2b`. This AI zone shares its deployment rollout wave with the standard `us-west4-b` zone.




## Resource quotas

Certain resources, such as static IPs, images, firewall rules, and VPC networks, have defined project-wide quota limits and per-region quota limits. When you create these resources, it counts towards your total project-wide quota or your per-region quota, if applicable. If any of the affected quota limits are exceeded, you won't be able to add more resources of the same type in that project or region.

To see a comprehensive list of quotas that apply to your project, visit the [Quotas](https://console.cloud.google.com/iam-admin/quotas) page in the Google Cloud console.

For example, if your global target pools quota is 50 and you create 25 target pools in example-region-1 and 25 target pools in example-region-2, you reach your project-wide quota and won't be able to create more target pools in any region within your project until you free up space. Similarly, if you have a per-region quota of 7 reserved IP addresses, you can only reserve up to 7 IP addresses in a single region. After you reach that limit, you will either need to reserve IP addresses in a new region or release some IP addresses.

## Transparent maintenance

Google regularly maintains its infrastructure by patching systems with the latest software, performing routine tests and preventative maintenance, and generally ensuring that Google infrastructure is as fast and efficient as Google knows how to make it.

By default, all compute instances are configured so that these maintenance events are transparent to your applications and workloads. Google uses a combination of datacenter innovations, operational best practices, and live migration technology to move running virtual machine instances out of the way of maintenance that is being performed. Your instance continues to run within the same zone with no action on your part.

By default, most virtual machines are set to live migrate, but you can also set your virtual machines to stop and reboot. Some machine series support only stop and reboot for maintenance operations. The two options differ in the following ways:

  * **Live migrate**

Compute Engine automatically migrates your running instance. The migration process will impact guest performance to some degree but your instance remains online throughout the migration process. The exact guest performance impact and duration depends on many factors, but it is expected most applications and workloads will not notice. For more information, see [Live Migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process).

  * **Stop and reboot**

Compute Engine automatically signals your instance to shut down, waits a short time for it to shut down cleanly, and then restarts it away from the maintenance event.




For more information on how to set the options above for your instances, see [Set VM host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options).

## Choosing a region and zone

You choose which region or zone hosts your resources, which controls where your data is stored and used. Choosing a region and zone is important for several reasons:

Handling failures
    Distribute your resources across multiple zones and regions to tolerate outages. Google designs zones to minimize the risk of correlated failures caused by physical infrastructure outages like power, cooling, or networking. Thus, if a zone becomes unavailable, you can transfer traffic to another zone in the same region to keep your services running. Similarly, you can mitigate the impact of a region outage on your application by running backup services in a different region. For more information about distributing your resources and designing a robust system, see [Designing resilient systems](https://docs.cloud.google.com/compute/docs/tutorials/robustsystems).
Decreased network latency
    To decrease network latency, you might want to choose a region or zone that is close to your point of service. For example, if you mostly have customers on the East coast of the United States of America, then you might want to choose a primary region and zone that is close to that area and a backup region and zone that is also close by.
Optimized AI and ML acceleration
    For workloads that require high-capacity AI accelerators, AI zones are available in select regions. These specialized zones provide GPU and TPU resources for AI and ML training and inference. You can select an AI zone to use infrastructure that is optimized for maximizing AI and ML throughput. See the [AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones) section for details.

For more information about how to choose a region and zone for your Compute Engine resources, see [Best practices for Compute Engine regions selection](https://cloud.google.com/solutions/best-practices-compute-engine-region-selection).

## Location selection tips

During compute instance creation, Compute Engine can automatically select zones for your instances based on capacity and availability using the following methods:

  * The [bulk instance creation API](https://docs.cloud.google.com/compute/docs/instances/multiple/about-bulk-creation) can automatically choose the zone in which to create instances.
  * A regional managed instance group (MIG) can be configured with a [target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-set-target-distribution-shape), which can automatically create instances in zones where resources are available.
  * If you are creating an instance in the Google Cloud console and you know the machine type and region that you want but you aren't sure which zone to select, you can select **Any** and Google will choose a zone for you based on the machine type and availability.



When selecting zones yourself, here are some things to keep in mind:

  * **Communication within and across regions will incur different costs.**

Generally, communication within regions will always be cheaper and faster than communication across different regions.

  * **Design important systems with redundancy across multiple zones or regions.**

At some point in time, your instances might experience an unexpected failure. To mitigate the effects of these possible events, you should duplicate important systems in multiple zones and regions.

For example, by hosting instances in zones `europe-west1-b` and `europe-west1-c`, if `europe-west1-b` fails unexpectedly, your instances in zone `europe-west1-c` will still be available. However, if you host all your instances in `europe-west1-b`, you will not be able to access any instances if `europe-west1-b` goes offline. Also, consider hosting your resources across regions. For example, to plan for continued availability of your workload in the unlikely scenario that the `europe-west1` region experiences a failure, consider deploying the workload on backup instances in the `europe-west3` region. For more tips on how to design systems for availability, see [Designing resilient systems](https://docs.cloud.google.com/compute/docs/tutorials/robustsystems).




## Available regions and zones

You can use the Google Cloud console, the Google Cloud CLI, or REST to [see available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones). You can also get the complete list of available machine types in all regions and zones by using the [`gcloud compute machine-types list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/machine-types/list). For example, running the following command displays all the regions and zones where you can use `c4d-standard-4` machine types.
    
    
    gcloud compute machine-types list --filter="name=c4d-standard-4"
    

Each zone offers a variety of processors. When you create an instance in a zone, your instance uses the default processor supported in that zone. For example, if you create an instance in the `us-central1-a` zone, your instance by default uses an Intel Haswell processor, unless you specify another option.

Alternatively, you can choose your desired CPU platform. For more information, read [Specifying a minimum CPU platform for VM instances](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform).

Consider the following information about resource availability before you select the regions and zones where you create your instances:

  * Local SSD and Titanium SSD storage is available in all regions and zones for supported machine series and machine types. See [About Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd) to learn more.
  * [GPUs](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones) and [TPUs](https://docs.cloud.google.com/compute/docs/regions-zones/tpu-regions-zones) are available only in specific zones.
  * [Sole-tenancy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes) is available in regions and zones where machine series with [sole-tenant node types](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_types) are available.
  * [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations) is available only with certain machine series in specific zones.



For information about hardware and feature support for all machine series, see [Machine series comparison](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison). For example, to see which machine series support both Intel TDX and sole tenancy, in the **Choose instance properties to compare** field, select both **Confidential Computing** and **Sole tenancy**.

For zonal availability of bare metal machine types, see [Regional availability of bare metal instances](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances#regions-zones).

The following table lists the available regions and zones for Compute Engine, along with the geographic location, supported machine series, processors, Confidential VM and GPU options, and low-carbon status for each zone:

APACNorth AmericaSouth AmericaEuropeMiddle EastAfricaA4X Max (NVIDIA GB300 Ultra Superchips)A4X (NVIDIA GB200 Superchips) {# Trailing hair space added to exclude A4X Max # } A4 (NVIDIA B200)A3 (NVIDIA H200/H100)A2 (NVIDIA A100)C4C4AC4DC4NC3C3DC2C2DE2G4 (NVIDIA RTX PRO 6000)G2 (NVIDIA L4)H4DH3M4NM4M3M2M1N4AN4DN4N2N2DN1T2DT2AX5X4Z4DZ4MZ3Intel Ivy BridgeIntel Sandy BridgeIntel HaswellIntel BroadwellIntel SkylakeIntel Cascade LakeIntel Ice LakeIntel Sapphire RapidsIntel Emerald RapidsIntel Granite RapidsAMD EPYC MilanAMD EPYC GenoaAMD EPYC TurinAmpere Altra ArmGoogle AxionNVIDIA GraceGPUsAMD SEV AMD SEV-SNPIntel TDXNVIDIA Confidential Computing

Clear all

Available Compute Engine regions and zones Zones | Location | Machine types | CPUs | Options | CO2 emissions  
---|---|---|---|---|---  
`africa-south1-a` | Johannesburg, South Africa | 

  * C2D, C4 , C4A, C4D
  * E2
  * M3
  * N2 , N2D, N4 
  * T2D

| 

  * Intel: Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Turin
  * Google: Axion

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`africa-south1-b` | Johannesburg, South Africa | 

  * C2D, C4 
  * E2
  * N2 , N2D, N4 
  * T2D

| 

  * Intel: Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`africa-south1-c` | Johannesburg, South Africa | 

  * C2D, C4 , C4D
  * E2
  * M3
  * N2 , N2D, N4 
  * T2D

| 

  * Intel: Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Turin

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`asia-east1-a` | Changhua County, Taiwan, APAC | 

  * C2 , C2D, C3 , C3D, C4 , C4A
  * E2
  * G2, G4
  * M1
  * N1, N2 , N2D, N4 
  * T2D
  * Z3-metal

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`asia-east1-b` | Changhua County, Taiwan, APAC | 

  * C2 , C2D, C3 , C3D, C4 , C4A
  * E2
  * G2
  * M1, M3
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`asia-east1-c` | Changhua County, Taiwan, APAC | 

  * A3
  * C2 , C2D, C3 , C3D, C4 , C4A
  * E2
  * G2
  * M1, M3
  * N1, N2 , N2D, N4 
  * T2D
  * Z3-metal

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`asia-east2-a` | Hong Kong, APAC | 

  * C2 , C3 , C4 
  * E2
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`asia-east2-b` | Hong Kong, APAC | 

  * C2 , C4 
  * E2
  * N1, N2 , N2D
  * T2D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids
  * AMD EPYC: Milan

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`asia-east2-c` | Hong Kong, APAC | 

  * C2 , C2D, C4 
  * E2
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`asia-northeast1-a` | Tokyo, Japan, APAC | 

  * A2
  * C2 , C4A
  * E2
  * G2
  * M1, M2, M3, M4 , M4N
  * N1, N2 , N2D, N4 
  * T2D
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids
  * AMD EPYC: Milan
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`asia-northeast1-b` | Tokyo, Japan, APAC | 

  * A3, A4 
  * C2 , C2D, C3 , C4 , C4A, C4D
  * E2
  * G2, G4
  * M1, M2, M3
  * N1, N2 , N2D, N4 
  * T2D
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)
  * [ Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx)

| None  
`asia-northeast1-c` | Tokyo, Japan, APAC | 

  * A2
  * C2 , C3 , C4 , C4A, C4D
  * E2
  * G2
  * M1, M3
  * N1, N2 , N2D, N4 
  * T2D
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`asia-northeast2-a` | Osaka, Japan, APAC | 

  * C2 , C2D, C3 , C4 
  * E2
  * M1, M3
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids
  * AMD EPYC: Milan

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`asia-northeast2-b` | Osaka, Japan, APAC | 

  * C2 
  * E2
  * M1, M2, M3
  * N1, N2 , N2D
  * T2D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Broadwell, Skylake, Cascade Lake, Ice Lake
  * AMD EPYC: Milan

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`asia-northeast2-c` | Osaka, Japan, APAC | 

  * C2 , C2D, C3 , C4 
  * E2
  * M1, M2, M3
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids
  * AMD EPYC: Milan

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`asia-northeast3-a` | Seoul, South Korea, APAC | 

  * C2 , C2D, C3 , C4 
  * E2
  * G2
  * M1, M2, M3
  * N1, N2 , N2D, N4 

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`asia-northeast3-b` | Seoul, South Korea, APAC | 

  * A2
  * C2 , C2D, C3 , C4 
  * E2
  * G2
  * M1, M2, M3
  * N1, N2 , N2D, N4 

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`asia-northeast3-c` | Seoul, South Korea, APAC | 

  * A3
  * C2 , C2D, C4 
  * E2
  * M3
  * N1, N2 , N2D, N4 

| 

  * Intel: Ivy Bridge, Sandy Bridge, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`asia-south1-a` | Mumbai, India, APAC | 

  * C2 , C2D, C3 , C3D, C4 , C4A
  * E2
  * G2
  * M1, M2
  * N1, N2 , N2D, N4 , N4D
  * T2D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`asia-south1-b` | Mumbai, India, APAC | 

  * A3
  * C2 , C2D, C3 , C3D, C4 , C4A, C4D
  * E2
  * G2
  * M1, M2, M3, M4 , M4N
  * N1, N2 , N2D, N4 , N4D
  * T2D
  * X4
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)
  * [ Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx)

| None  
`asia-south1-c` | Mumbai, India, APAC | 

  * A3
  * C2 , C2D, C3 , C3D, C4 , C4A, C4D
  * E2
  * G2, G4
  * H4D
  * M1, M3, M4 , M4N
  * N1, N2 , N2D, N4 , N4A, N4D
  * T2D
  * X4
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`asia-south2-a` | Delhi, India, APAC | 

  * C2 , C2D, C3 , C4 
  * E2
  * G4
  * M1, M2, M3, M4 , M4N
  * N1, N2 , N2D, N4 
  * T2D
  * X4

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Turin

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`asia-south2-b` | Delhi, India, APAC | 

  * C2 , C2D, C3 , C4 
  * E2
  * M1, M2, M3, M4 , M4N
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`asia-south2-c` | Delhi, India, APAC | 

  * A3
  * C2 , C3 , C4 
  * E2
  * G4
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Turin

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`asia-southeast1-a` | Jurong West, Singapore, APAC | 

  * A2
  * C2 , C2D, C3 , C3D, C4 , C4A, C4D
  * E2
  * G2, G4
  * H4D
  * M1, M2, M3, M4 , M4N
  * N1, N2 , N2D, N4 , N4A, N4D
  * T2D
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)
  * [ AMD SEV-SNP](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev-snp)
  * [ Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx)

| None  
`asia-southeast1-b` | Jurong West, Singapore, APAC | 

  * A3, A4 
  * C2 , C2D, C3 , C3D, C4 , C4A, C4D
  * E2
  * G2, G4
  * M1, M2, M3, M4 , M4N
  * N1, N2 , N2D, N4 , N4A, N4D
  * T2A, T2D
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Ampere: Altra Arm
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)
  * [ AMD SEV-SNP](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev-snp)
  * [ Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx)

| None  
`asia-southeast1-c` | Jurong West, Singapore, APAC | 

  * A2, A3
  * C2 , C2D, C3 , C3D, C4 , C4A, C4D
  * E2
  * G2
  * M1
  * N1, N2 , N2D, N4 , N4A, N4D
  * T2A, T2D
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Ampere: Altra Arm
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)
  * [ AMD SEV-SNP](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev-snp)
  * [ Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx)

| None  
`asia-southeast2-a` | Jakarta, Indonesia, APAC | 

  * C3 , C4 , C4A
  * E2
  * M1
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`asia-southeast2-b` | Jakarta, Indonesia, APAC | 

  * C4 , C4A
  * E2
  * G4
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`asia-southeast2-c` | Jakarta, Indonesia, APAC | 

  * C4 , C4A
  * E2
  * G4
  * M1
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`asia-southeast3-a` | Bangkok, Thailand, APAC | 

  * C3D, C4 
  * M3, M4 , M4N
  * N4 

| 

  * Intel: Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan

| None| None  
`asia-southeast3-b` | Bangkok, Thailand, APAC | 

  * C3D, C4 
  * M3, M4 , M4N
  * N4 

| 

  * Intel: Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan

| None| None  
`asia-southeast3-c` | Bangkok, Thailand, APAC | 

  * C3D, C4 
  * M3, M4 , M4N
  * N4 

| 

  * Intel: Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan

| None| None  
`australia-southeast1-a` | Sydney, Australia, APAC | 

  * C2 , C3 
  * E2
  * M1, M2, M3
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids
  * AMD EPYC: Milan

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`australia-southeast1-b` | Sydney, Australia, APAC | 

  * C2 , C3 , C3D, C4 
  * E2
  * M1, M2
  * N1, N2 , N2D, N4 
  * T2D
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`australia-southeast1-c` | Sydney, Australia, APAC | 

  * A3
  * C2 , C3 , C3D, C4 , C4A, C4D
  * E2
  * M1, M3, M4 , M4N
  * N1, N2 , N2D, N4 
  * T2D
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`australia-southeast2-a` | Melbourne, Australia, APAC | 

  * C2D, C3 , C3D, C4 , C4A
  * E2
  * N1, N2 , N2D, N4 
  * T2D
  * Z3-metal

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids
  * AMD EPYC: Milan
  * Google: Axion

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`australia-southeast2-b` | Melbourne, Australia, APAC | 

  * A3
  * C3 , C4 , C4A
  * E2
  * M1, M3
  * N1, N2 , N2D, N4 
  * T2D
  * Z3-metal

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan
  * Google: Axion

| 

  * GPUs

| None  
`australia-southeast2-c` | Melbourne, Australia, APAC | 

  * C4 , C4A
  * E2
  * M1, M3
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan
  * Google: Axion

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`europe-central2-a` | Warsaw, Poland, Europe | 

  * C2D, C4 , C4A
  * E2
  * M1, M3, M4 , M4N
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan
  * Google: Axion

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-central2-b` | Warsaw, Poland, Europe | 

  * C2D
  * E2
  * M1
  * N1, N2 , N2D
  * T2D

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake
  * AMD EPYC: Milan

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-central2-c` | Warsaw, Poland, Europe | 

  * C4 
  * E2
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids
  * AMD EPYC: Milan

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-north1-a` | Hamina, Finland, Europe | 

  * C2 , C3D, C4 , C4A
  * E2
  * G4
  * M3
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids
  * AMD EPYC: Milan, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-north1-b` | Hamina, Finland, Europe | 

  * C2 , C3 , C4 , C4A
  * E2
  * G4
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Broadwell, Skylake, Cascade Lake, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-north1-c` | Hamina, Finland, Europe | 

  * A4 
  * C2 , C4 , C4A
  * E2
  * G4
  * M3
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-north2-a` | Stockholm, Sweden, Europe | 

  * C3 , C3D, C4 , C4A
  * E2
  * N4 
  * Z3

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa
  * Google: Axion

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-north2-b` | Stockholm, Sweden, Europe | 

  * C2D, C3 , C3D, C4 , C4A
  * E2
  * N4 
  * Z3

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa
  * Google: Axion

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-north2-c` | Stockholm, Sweden, Europe | 

  * C4 
  * E2
  * N4 

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Cascade Lake, Ice Lake, Emerald Rapids
  * AMD EPYC: Milan

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-southwest1-a` | Madrid, Spain, Europe | 

  * C4 , C4A
  * E2
  * M1, M2, M3, M4 , M4N
  * N2 , N2D, N4 
  * T2D

| 

  * Intel: Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids
  * AMD EPYC: Milan
  * Google: Axion

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-southwest1-b` | Madrid, Spain, Europe | 

  * C2D, C4 , C4A
  * E2
  * N2 , N2D, N4 
  * T2D

| 

  * Intel: Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan
  * Google: Axion

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-southwest1-c` | Madrid, Spain, Europe | 

  * C4 , C4A
  * E2
  * M1, M2, M3, M4 , M4N
  * N2 , N2D, N4 
  * T2D

| 

  * Intel: Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan
  * Google: Axion

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west1-b` | St. Ghislain, Belgium, Europe | 

  * A3, A4 
  * C2 , C2D, C3 , C3D, C4 , C4A, C4D
  * E2
  * G2, G4
  * M1, M2, M3, M4 , M4N
  * N1, N2 , N2D, N4 , N4A, N4D
  * T2D
  * X4
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west1-c` | St. Ghislain, Belgium, Europe | 

  * A3
  * C2 , C2D, C3 , C3D, C4 , C4A, C4D
  * E2
  * G2, G4
  * M2, M4 , M4N
  * N1, N2 , N2D, N4 , N4A, N4D
  * T2D
  * X4
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west1-d` | St. Ghislain, Belgium, Europe | 

  * C2 , C2D, C3 , C3D, C4 , C4A, C4D
  * E2
  * M1, M2, M3, M4 , M4N
  * N1, N2 , N2D, N4 , N4D
  * T2D
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west10-a` | Berlin, Germany, Europe | 

  * C3 , C4D
  * E2
  * N2 , N2D, N4 
  * T2D
  * Z3

| 

  * Intel: Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids
  * AMD EPYC: Milan, Turin

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`europe-west10-b` | Berlin, Germany, Europe | 

  * C4D
  * E2
  * G4
  * N2 , N2D
  * Z3

| 

  * Intel: Cascade Lake, Ice Lake, Sapphire Rapids
  * AMD EPYC: Milan, Turin

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`europe-west10-c` | Berlin, Germany, Europe | 

  * C4 , C4D
  * E2
  * N2 , N2D, N4 
  * T2D
  * Z3

| 

  * Intel: Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids
  * AMD EPYC: Milan, Turin

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`europe-west12-a` | Turin, Italy, Europe | 

  * E2
  * M3, M4 , M4N
  * N2 , N2D
  * T2D

| 

  * Intel: Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids
  * AMD EPYC: Milan

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west12-b` | Turin, Italy, Europe | 

  * C2D
  * E2
  * M3
  * N2 , N2D
  * T2D

| 

  * Intel: Broadwell, Skylake, Cascade Lake, Ice Lake
  * AMD EPYC: Milan

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west12-c` | Turin, Italy, Europe | 

  * C4 
  * E2
  * N2 , N2D, N4 
  * T2D

| 

  * Intel: Broadwell, Skylake, Cascade Lake, Emerald Rapids
  * AMD EPYC: Milan

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west2-a` | London, England, Europe | 

  * C2 , C2D, C3 , C3D, C4 , C4A, C4D, C4N
  * E2
  * G2
  * M1, M2, M3
  * N1, N2 , N2D, N4 , N4A, N4D
  * T2D
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west2-b` | London, England, Europe | 

  * C2 , C2D, C3 , C3D, C4 , C4A, C4D
  * E2
  * G2, G4
  * M1, M2, M3
  * N1, N2 , N2D, N4 , N4A
  * T2D
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west2-c` | London, England, Europe | 

  * C2 , C2D, C3 , C4 , C4A, C4D
  * E2
  * G4
  * M1, M3, M4 , M4N
  * N1, N2 , N2D, N4 , N4A, N4D
  * T2D
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west3-a` | Frankfurt, Germany, Europe | 

  * C2 , C2D, C3 , C3D, C4 , C4A, C4D
  * E2
  * G2
  * M1, M2, M3, M4 , M4N
  * N1, N2 , N2D, N4 , N4A, N4D
  * T2D
  * X4
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)
  * [ AMD SEV-SNP](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev-snp)

| None  
`europe-west3-b` | Frankfurt, Germany, Europe | 

  * C2 , C2D, C3 , C3D, C4 , C4A, C4D
  * E2
  * G2
  * M1, M2, M3, M4 , M4N
  * N1, N2 , N2D, N4 , N4A
  * T2D
  * X4
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)
  * [ AMD SEV-SNP](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev-snp)

| None  
`europe-west3-c` | Frankfurt, Germany, Europe | 

  * A3
  * C2 , C2D, C3 , C3D, C4 , C4A, C4D
  * E2
  * M1, M3
  * N1, N2 , N2D, N4 , N4A
  * T2D
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)
  * [ AMD SEV-SNP](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev-snp)

| None  
`europe-west4-a` | Eemshaven, Netherlands, Europe | 

  * A2, A3
  * C2 , C2D, C3 , C3D, C4 , C4A, C4D
  * E2
  * G2, G4
  * M1, M2, M3, M4 , M4N
  * N1, N2 , N2D, N4 , N4A, N4D
  * T2A, T2D
  * X4
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Ampere: Altra Arm
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)
  * [ AMD SEV-SNP](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev-snp)
  * [ Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west4-b` | Eemshaven, Netherlands, Europe | 

  * A2, A3, A4 , A4X 
  * C2 , C2D, C3 , C3D, C4 , C4A, C4D
  * E2
  * G2, G4
  * H3, H4D
  * M1, M2, M3, M4 , M4N
  * N1, N2 , N2D, N4 , N4A, N4D
  * T2A, T2D
  * X4
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Ampere: Altra Arm
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)
  * [ AMD SEV-SNP](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev-snp)
  * [ Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west4-c` | Eemshaven, Netherlands, Europe | 

  * A3
  * C2 , C2D, C3 , C3D, C4 , C4A, C4D
  * E2
  * G2, G4
  * H3, H4D
  * M1, M2
  * N1, N2 , N2D, N4 , N4A, N4D
  * T2A, T2D
  * X4
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Ampere: Altra Arm
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)
  * [ AMD SEV-SNP](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev-snp)
  * [ Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx)
  * [ NVIDIA Confidential Computing](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=nvidia-confidential-computing)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west6-a` | Zurich, Switzerland, Europe | 

  * C2 
  * E2
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids
  * AMD EPYC: Milan

| None| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west6-b` | Zurich, Switzerland, Europe | 

  * C2 , C4 , C4A
  * E2
  * G2
  * M1, M3
  * N1, N2 , N2D, N4 
  * T2D
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west6-c` | Zurich, Switzerland, Europe | 

  * C2 , C4 
  * E2
  * G2
  * M1, M3
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west8-a` | Milan, Italy, Europe | 

  * E2
  * M1, M2, M3
  * N2 , N2D, N4 
  * T2D
  * X4

| 

  * Intel: Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids
  * AMD EPYC: Milan

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west8-b` | Milan, Italy, Europe | 

  * C4 
  * E2
  * G4
  * M2
  * N2 , N2D, N4 
  * T2D
  * Z3-metal

| 

  * Intel: Broadwell, Skylake, Cascade Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Turin

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west8-c` | Milan, Italy, Europe | 

  * C2D, C4 
  * E2
  * G4
  * M1, M2, M3
  * N2 , N2D, N4 
  * T2D
  * X4
  * Z3-metal

| 

  * Intel: Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west9-a` | Paris, France, Europe | 

  * C3 , C4 
  * E2
  * M3
  * N2 , N2D, N4 
  * T2D

| 

  * Intel: Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids
  * AMD EPYC: Milan

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)
  * [ Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west9-b` | Paris, France, Europe | 

  * C3 , C4 , C4D
  * E2
  * M1, M3
  * N2 , N2D, N4 
  * T2D

| 

  * Intel: Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Turin

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)
  * [ Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`europe-west9-c` | Paris, France, Europe | 

  * A3
  * C3 , C4 
  * E2
  * M1
  * N2 , N2D, N4 
  * T2D

| 

  * Intel: Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`me-central1-a` | Doha, Qatar, Middle East | 

  * C3 , C4 
  * E2
  * N2 , N2D
  * T2D
  * Z3-metal

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids
  * AMD EPYC: Milan

| None| None  
`me-central1-b` | Doha, Qatar, Middle East | 

  * C4 
  * E2
  * M3
  * N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids
  * AMD EPYC: Milan

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`me-central1-c` | Doha, Qatar, Middle East | 

  * C3 , C4 , C4A
  * E2
  * M3
  * N2 , N2D, N4 
  * T2D
  * Z3-metal

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan
  * Google: Axion

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`me-central2-a` | Dammam, Saudi Arabia, Middle East | 

  * C2 , C3 , C3D, C4 , C4A
  * E2
  * G2, G4
  * M2, M3
  * N2 , N2D, N4 
  * T2D

| 

  * Intel: Haswell, Broadwell, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`me-central2-b` | Dammam, Saudi Arabia, Middle East | 

  * C2 , C3 
  * E2
  * M2, M3
  * N2 , N2D
  * T2D

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Cascade Lake, Ice Lake, Sapphire Rapids
  * AMD EPYC: Milan

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`me-central2-c` | Dammam, Saudi Arabia, Middle East | 

  * C2 , C3 , C3D, C4 
  * E2
  * G2
  * M2, M3, M4 , M4N
  * N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`me-west1-a` | Tel Aviv, Israel, Middle East | 

  * A2
  * C2 , C3 , C4 
  * E2
  * M1, M3
  * N2 , N2D, N4 
  * T2D

| 

  * Intel: Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids
  * AMD EPYC: Milan

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`me-west1-b` | Tel Aviv, Israel, Middle East | 

  * C2 , C3 , C3D, C4 , C4A
  * E2
  * N1 (GPU required), N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`me-west1-c` | Tel Aviv, Israel, Middle East | 

  * A2
  * C2 , C2D, C3 
  * E2
  * M1, M3
  * N1 (GPU required), N2 , N2D
  * T2D

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids
  * AMD EPYC: Milan

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`northamerica-northeast1-a` | Montréal, Québec, North America | 

  * C2 , C2D, C3 , C4 , C4A
  * E2
  * M4 , M4N
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan
  * Google: Axion

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`northamerica-northeast1-b` | Montréal, Québec, North America | 

  * C2 , C3 , C4 , C4A, C4D
  * E2
  * G2
  * H3
  * M1, M2, M3, M4 , M4N
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`northamerica-northeast1-c` | Montréal, Québec, North America | 

  * C2 
  * E2
  * G2
  * M1, M2, M3
  * N1, N2 , N2D
  * T2D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake
  * AMD EPYC: Milan

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`northamerica-northeast2-a` | Toronto, Ontario, North America | 

  * C4 
  * E2
  * G2
  * M1, M2, M3
  * N1, N2 , N2D
  * T2D

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids
  * AMD EPYC: Milan

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`northamerica-northeast2-b` | Toronto, Ontario, North America | 

  * C2D, C4 , C4A, C4D
  * E2
  * G2
  * M1, M2, M3
  * N1, N2 , N2D, N4 
  * T2D
  * Z3-metal

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`northamerica-northeast2-c` | Toronto, Ontario, North America | 

  * A3
  * C2D, C4 
  * E2
  * M2, M3, M4 , M4N
  * N1, N2 , N2D, N4 
  * T2D
  * Z3-metal

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`northamerica-south1-a` | Queretaro, Mexico, North America | 

  * C3D, C4 , C4A
  * E2
  * N4 
  * Z3

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa
  * Google: Axion

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`northamerica-south1-b` | Queretaro, Mexico, North America | 

  * C3D, C4 , C4A
  * E2
  * N4 
  * Z3

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa
  * Google: Axion

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`northamerica-south1-c` | Queretaro, Mexico, North America | 

  * C3D, C4 , C4A
  * E2
  * N4 
  * Z3

| 

  * Intel: Ivy Bridge, Haswell, Broadwell, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa
  * Google: Axion

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`southamerica-east1-a` | Osasco, São Paulo, Brazil, South America | 

  * C2 , C2D, C3 , C4 
  * E2
  * G4
  * N1, N2 , N2D, N4 
  * T2D
  * Z3-metal

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`southamerica-east1-b` | Osasco, São Paulo, Brazil, South America | 

  * C2 , C2D, C3 , C4 
  * E2
  * G4
  * M1, M2, M3
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`southamerica-east1-c` | Osasco, São Paulo, Brazil, South America | 

  * C2 , C2D, C3 , C4 , C4A
  * E2
  * M1, M2, M3, M4 , M4N
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`southamerica-west1-a` | Santiago, Chile, South America | 

  * C2 , C4 , C4A
  * E2
  * N2 , N2D, N4 
  * T2D
  * Z3

| 

  * Intel: Haswell, Broadwell, Skylake, Cascade Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan
  * Google: Axion

| None| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`southamerica-west1-b` | Santiago, Chile, South America | 

  * C2 , C4 , C4A
  * E2
  * M1, M2, M3, M4 , M4N
  * N2 , N2D, N4 
  * T2D

| 

  * Intel: Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan
  * Google: Axion

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`southamerica-west1-c` | Santiago, Chile, South America | 

  * C2 , C4 
  * E2
  * M1, M2, M3, M4 , M4N
  * N2 , N2D, N4 
  * T2D

| 

  * Intel: Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan

| None| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-central1-a` | Council Bluffs, Iowa, North America | 

  * A2, A3, A4X 
  * C2 , C2D, C3 , C3D, C4 , C4A, C4D, C4N
  * E2
  * G2
  * H3, H4D
  * M1, M2, M3, M4 , M4N
  * N1, N2 , N2D, N4 , N4A, N4D
  * T2A, T2D
  * X4, X5
  * Z3, Z4D, Z4M

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Ampere: Altra Arm
  * Google: Axion
  * NVIDIA: Grace

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)
  * [ AMD SEV-SNP](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev-snp)
  * [ Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx)
  * [ NVIDIA Confidential Computing](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=nvidia-confidential-computing)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-central1-b` | Council Bluffs, Iowa, North America | 

  * A2, A3, A4 , A4X Max, A4X 
  * C2 , C2D, C3 , C3D, C4 , C4A, C4D, C4N
  * E2
  * G2, G4
  * H4D
  * M1, M2, M3, M4 , M4N
  * N1, N2 , N2D, N4 , N4A, N4D
  * T2A, T2D
  * X4
  * Z3, Z4D, Z4M

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Ampere: Altra Arm
  * Google: Axion
  * NVIDIA: Grace

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)
  * [ AMD SEV-SNP](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev-snp)
  * [ Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-central1-c` | Council Bluffs, Iowa, North America | 

  * A2, A3
  * C2 , C2D, C3 , C3D, C4 , C4A, C4D, C4N
  * E2
  * G2
  * M1, M2, M3, M4 , M4N
  * N1, N2 , N2D, N4 , N4A, N4D
  * T2D
  * X4, X5
  * Z3, Z4D, Z4M

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)
  * [ AMD SEV-SNP](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev-snp)
  * [ Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-central1-f` | Council Bluffs, Iowa, North America | 

  * A2
  * C2 , C2D, C3 , C3D, C4 , C4A, C4D
  * E2
  * G4
  * M1
  * N1, N2 , N2D, N4 , N4A, N4D
  * T2A, T2D
  * Z3, Z4D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Ampere: Altra Arm
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-east1-b` | Moncks Corner, South Carolina, North America | 

  * A2, A4 
  * C2 , C2D, C3 , C3D, C4 , C4A, C4D
  * E2
  * G2, G4
  * H4D
  * M1, M3, M4 , M4N
  * N1, N2 , N2D, N4 , N4A, N4D
  * T2D
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`us-east1-c` | Moncks Corner, South Carolina, North America | 

  * C2 , C2D, C3 , C3D, C4 , C4A, C4D, C4N
  * E2
  * G2
  * M1
  * N1, N2 , N2D, N4 , N4A, N4D
  * T2D
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)
  * [ Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx)

| None  
`us-east1-d` | Moncks Corner, South Carolina, North America | 

  * A4 , A4X 
  * C2 , C2D, C3 , C3D, C4 , C4A, C4D
  * E2
  * G4
  * M1, M3, M4 , M4N
  * N1, N2 , N2D, N4 , N4A, N4D
  * T2D
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)
  * [ Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx)

| None  
`us-east4-a` | Ashburn, Virginia, North America | 

  * A3, A4X Max
  * C2 , C2D, C3 , C3D, C4 , C4A, C4D
  * E2
  * G2
  * M1, M2, M3, M4 , M4N
  * N1, N2 , N2D, N4 , N4A, N4D
  * T2D
  * X4, X5
  * Z3, Z4M

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)
  * [ Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx)

| None  
`us-east4-b` | Ashburn, Virginia, North America | 

  * A3, A4 , A4X Max, A4X 
  * C2 , C2D, C3 , C3D, C4 , C4A, C4D
  * E2
  * G4
  * M1, M2, M3, M4 , M4N
  * N1, N2 , N2D, N4 , N4A, N4D
  * T2D
  * X4
  * Z3, Z4D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Google: Axion
  * NVIDIA: Grace

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`us-east4-c` | Ashburn, Virginia, North America | 

  * A2, A3
  * C2 , C2D, C3 , C3D, C4 , C4A, C4D
  * E2
  * G2, G4
  * M1, M3, M4 , M4N
  * N1, N2 , N2D, N4 , N4A, N4D
  * T2D
  * X4, X5
  * Z3, Z4D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)
  * [ Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx)

| None  
`us-east5-a` | Columbus, Ohio, North America | 

  * A2, A3
  * C2 , C3 , C3D, C4 , C4A, C4D
  * E2
  * G4
  * M4 , M4N
  * N2 , N2D, N4 , N4D
  * T2D
  * Z3, Z4D

| 

  * Intel: Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)
  * [ NVIDIA Confidential Computing](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=nvidia-confidential-computing)

| None  
`us-east5-b` | Columbus, Ohio, North America | 

  * A4X Max
  * C2 , C3 , C3D, C4 , C4A, C4D, C4N
  * E2
  * G4
  * M4 , M4N
  * N2 , N2D, N4 , N4D
  * T2D
  * Z3, Z4D

| 

  * Intel: Haswell, Broadwell, Skylake, Cascade Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)
  * [ Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx)

| None  
`us-east5-c` | Columbus, Ohio, North America | 

  * A4X Max
  * C2 , C3 , C3D, C4 , C4A, C4D, C4N
  * E2
  * G4
  * M4 , M4N
  * N2 , N2D, N4 , N4D
  * T2D
  * Z3, Z4D

| 

  * Intel: Haswell, Broadwell, Skylake, Cascade Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Turin
  * Google: Axion
  * NVIDIA: Grace

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)
  * [ Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx)

| None  
`us-south1-a` | Dallas, Texas, North America | 

  * C3 , C4 , C4A
  * E2
  * G4
  * N2 , N2D, N4 
  * T2D
  * Z3

| 

  * Intel: Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-south1-b` | Dallas, Texas, North America | 

  * A3, A4 
  * C3 , C4 , C4A
  * E2
  * G4
  * N2 , N2D, N4 
  * T2D
  * Z3

| 

  * Intel: Haswell, Broadwell, Skylake, Cascade Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Turin
  * Google: Axion

| 

  * GPUs

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-south1-c` | Dallas, Texas, North America | 

  * C3 
  * E2
  * N2 , N2D
  * T2D
  * Z3

| 

  * Intel: Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids
  * AMD EPYC: Milan

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-west1-a` | The Dalles, Oregon, North America | 

  * A3
  * C2 , C2D, C3 , C3D, C4 , C4A, C4D
  * E2
  * G2, G4
  * M1, M3, M4 , M4N
  * N1, N2 , N2D, N4 , N4A, N4D
  * T2D
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)
  * [ Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-west1-b` | The Dalles, Oregon, North America | 

  * A2, A3
  * C2 , C2D, C3 , C3D, C4 , C4D, C4N
  * E2
  * G2, G4
  * M1, M3, M4 , M4N
  * N1, N2 , N2D, N4 , N4A, N4D
  * T2D
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)
  * [ Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-west1-c` | The Dalles, Oregon, North America | 

  * A3
  * C2 , C2D, C3 , C3D, C4 , C4A, C4D
  * E2
  * G4
  * M3, M4 , M4N
  * N1, N2 , N2D, N4 , N4A, N4D
  * T2D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
`us-west2-a` | Los Angeles, California, North America | 

  * C2 , C2D, C3 , C3D, C4 , C4A
  * E2
  * N1, N2 , N2D, N4 
  * T2D
  * Z3

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids
  * AMD EPYC: Milan, Genoa
  * Google: Axion

| 

  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`us-west2-b` | Los Angeles, California, North America | 

  * C2 , C3 , C3D, C4 , C4A
  * E2
  * M1
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`us-west2-c` | Los Angeles, California, North America | 

  * A4 
  * C2 , C2D, C3 , C3D, C4 , C4A
  * E2
  * M1
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Haswell, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`us-west3-a` | Salt Lake City, Utah, North America | 

  * C2 , C3 , C4 , C4D
  * E2
  * G4
  * M3
  * N1, N2 , N2D, N4 , N4D
  * T2D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Turin

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`us-west3-b` | Salt Lake City, Utah, North America | 

  * A2, A4 
  * C2 , C3 , C4 
  * E2
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`us-west3-c` | Salt Lake City, Utah, North America | 

  * A4 
  * C2 , C2D, C3 , C4 
  * E2
  * N1, N2 , N2D, N4 
  * T2D

| 

  * Intel: Ivy Bridge, Sandy Bridge, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`us-west4-a` | Las Vegas, Nevada, North America | 

  * A3
  * C2 , C2D, C3 , C3D, C4 , C4A, C4D
  * E2
  * G2, G4
  * H4D
  * M1, M2, M3, M4 , M4N
  * N1, N2 , N2D, N4 , N4D
  * T2D
  * X4

| 

  * Intel: Ivy Bridge, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Genoa, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`us-west4-b` | Las Vegas, Nevada, North America | 

  * A2
  * C2 , C2D, C3 , C3D, C4 , C4A, C4D
  * E2
  * G4
  * M1, M2, M3, M4 , M4N
  * N1, N2 , N2D, N4 , N4D
  * T2D
  * X4

| 

  * Intel: Ivy Bridge, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
`us-west4-c` | Las Vegas, Nevada, North America | 

  * C2 , C2D, C3 , C4 , C4A, C4D
  * E2
  * G2, G4
  * N1, N2 , N2D, N4 , N4D
  * T2D

| 

  * Intel: Ivy Bridge, Broadwell, Skylake, Cascade Lake, Ice Lake, Sapphire Rapids, Emerald Rapids, Granite Rapids
  * AMD EPYC: Milan, Turin
  * Google: Axion

| 

  * GPUs
  * [ AMD SEV ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev)

| None  
  
### Notes

  * **For`me-west1-b` and `me-west1-c` (`N1` machine series):** To use an `N1` machine type in any of the supported `me-west1` zones, you must attach at least one NVIDIA T4 GPU to the VM.



## What's next

  * Learn more about [geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).
  * Learn how to [view available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones).
  * Learn how to [change your default zone or region](https://docs.cloud.google.com/compute/docs/regions-zones/changing-default-zone-region).
  * Learn more about the [global, regional, and zonal resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Compute Engine performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Compute Engine free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 

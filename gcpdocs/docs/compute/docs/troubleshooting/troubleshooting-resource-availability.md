---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-resource-availability/
title: Troubleshoot resource availability errors \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:09:10.227103+00:00
---

# Troubleshoot resource availability errors  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-resource-availability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshoot resource availability errors Stay organized with collections  Save and categorize content based on your preferences. 

A _resource availability error_ occurs when a zone doesn't have enough available capacity to provision the compute resources you requested to create, restart, or update Compute Engine instances, or to reserve zonal resources.

This document explains how to identify and resolve resource availability errors. Because these errors indicate a shortage of physical hardware in a zone rather than a project usage limit, a quota increase doesn't resolve them. Alternatively, to troubleshoot quota limits, see [Troubleshoot quota errors](https://docs.cloud.google.com/docs/quotas/troubleshoot).

## Understand resource availability errors

Resource availability errors occur when a zone lacks sufficient capacity for one or more of the following physical resources:

  * Accelerators (if any)

  * CPU cores

  * Disks

  * Memory


**Note:** Available quota in your project doesn't guarantee resource availability. Quota is an administrative limit that specifies the maximum resources that your project can use. Resource availability reflects the real-time supply of physical hardware in a zone.

For example, suppose that you want to create a compute instance that uses the `a2-highgpu-2g` machine type and has two Local SSD disks attached. This machine type includes 24 vCPUs on the Intel Xeon Platinum 8273CL Processor, 170 GB of memory, and two NVIDIA A100 GPUs. If _all_ of these resources are available in your specified zone at the time of your request, then your request succeeds. Otherwise, your request fails with a resource availability error.

When a resource availability error occurs, Compute Engine returns an error message similar to one of the following in the Google Cloud console, the Google Cloud CLI, or the API response:
    
    
    ZONE_RESOURCE_POOL_EXHAUSTED
    
    
    
    ZONE_RESOURCE_POOL_EXHAUSTED_WITH_DETAILS
    
    
    
    REGION_RESOURCE_POOL_EXHAUSTED_WITH_DETAILS
    
    
    
    POOL_CAPACITY_INSUFFICIENT
    
    
    
    The zone 'projects/PROJECT_ID/zones/ZONE' does not have
    enough resources available to fulfill the request. Try a different zone, or try
    again later.
    
    
    
    A VM_TYPE_AND_SIZE VM instance with RESOURCE_ATTACHMENT is
    currently unavailable in the ZONE zone.
    
    Capacity changes frequently, so try your request in a different zone, with a
    different VM hardware configuration, or at a later time. For more options, see
    troubleshooting documentation.
    
    
    
    A VM_TYPE_AND_SIZE VM instance with RESOURCE_ATTACHMENT is
    currently unavailable in the ZONE zone because of REASON.
    
    Consider trying your request in the AVAILABLE_ZONES zones, which
    currently has capacity to accommodate your request.
    
    If you cannot move your VM to AVAILABLE_ZONES, review the
    instructions to resolve the REASON failure that are available in
    troubleshooting documentation, then try your request again. If your workload
    can't accommodate the suggested resolution, try your request with a different VM
    hardware configuration or at a later time.
    

You can view an error message for a resource availability error as follows:

  * For standalone compute instances, compute instances created in bulk, sole-tenant nodes, or reservations, Compute Engine returns these error messages in the Google Cloud console, the gcloud CLI, or the API response.

  * For managed instance groups (MIGs), Compute Engine logs these errors in the MIG's instance error list. To view the error message and the hardware constraint that caused the error, see [List instance errors](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#listing_instance_errors).




## Resolve resource availability errors

Resource availability errors fall into two categories: configuration errors that you can fix (for example, when you attempt to request an unsupported machine type in a zone), and physical hardware constraints that you can't control.

To address a resource availability error, complete the following steps. If you prefer to evaluate options based on what your workload can adjust, then instead see Summary of recommendations by workload requirements.

**Caution:** Don't stop and restart, or delete and recreate, compute instances to resolve a resource availability error if you lack a reservation. When you stop or delete a compute instance, Compute Engine releases its vCPUs, memory, accelerators, and disks back to the zone. If the zone lacks capacity for any of these resources, then you can't restart or recreate the compute instance.

  1. **Address specific resource constraints** : if your error message includes a reason code, then see Resolve errors by error reasons. If those specific solutions don't resolve the issue, then go to the next step.

  2. **Apply general capacity strategies** : if your error message doesn't include a reason code, or if specific adjustments are insufficient, then see Resolve common errors.

  3. **Review feature-specific recommendations** : if you still haven't resolved the issue, then see one of the following sections based on your deployment method or feature:

     * Resolve errors when you create standalone compute instances

     * Resolve errors when you create compute instances in bulk

     * Resolve errors when you create, scale, or repair MIGs

     * Resolve errors when you create sole-tenant nodes

     * Resolve errors when you create TPU slices

     * Resolve errors when you create a reservation

     * Resolve errors when you update machine types




If you encounter resource availability errors when you attempt to create or autoscale a Google Kubernetes Engine (GKE) cluster, then see [Troubleshoot cluster creation](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cluster-creation).

### Resolve errors by error reasons

When Compute Engine provides detailed diagnostic data for a resource availability error, the error response identifies the specific root causes that prevented Compute Engine from fulfilling your request.

In the Google Cloud console, gcloud CLI, or Cloud Logging, the root causes appear in the operation error message:
    
    
    ERROR: (gcloud.compute.instances.create) Could not fetch resource:
     - A n1-standard-1 VM instance with 2 local SSD(s) is currently unavailable in the us-central1-a zone, because of **cpu_availability,local_ssd_availability** root cause(s). Consider trying your request in the us-central1-b, us-central1-c zone(s), which currently has capacity to accommodate your request.
    

In the REST API, the error details appear in the operation's `error.errors[]` array, with root causes returned in the `LocalizedMessage` and in the `google.rpc.ErrorInfo` detail (`domain: "compute.googleapis.com"`):
    
    
    {
      "code": "ZONE_RESOURCE_POOL_EXHAUSTED_WITH_DETAILS",
      "message": "A n1-standard-1 VM instance with 2 local SSD(s) is currently unavailable in the us-central1-a zone, because of cpu_availability,local_ssd_availability root cause(s). Consider trying your request in the us-central1-b, us-central1-c zone(s), which currently has capacity to accommodate your request.",
      "errorDetails": [
        {
          "errorInfo": {
            "domain": "compute.googleapis.com",
            **"reason" : "cpu_availability,local_ssd_availability"**,
            "metadata": {
              "vmType": "n1-standard-1",
              "zone": "us-central1-a",
              "attachment": "local-ssd:2",
              "zonesAvailable": "us-central1-b,us-central1-c"
            }
          }
        }
      ]
    }
    

Depending on the error code in your response, take the following actions:

  * **`ZONE_RESOURCE_POOL_EXHAUSTED_WITH_DETAILS`** : Compute Engine identifies the root causes that prevented fulfillment in the target zone. If other zones in the same region have capacity for your request, then the error details also include a list of recommended zones (`AVAILABLE_ZONES` in the message or `zonesAvailable` in the API `ErrorInfo` metadata). If the error details list recommended zones, then create, migrate, or reserve your compute instances in one of those zones. If no other zones in the region have capacity, then the error message doesn't list alternative zones.

  * **`REGION_RESOURCE_POOL_EXHAUSTED_WITH_DETAILS`** : all evaluated zones in your target region lack capacity for your request. Review the constraint reasons in the error message, or retry your request in a different region, with an alternative machine type, or with a flexible provisioning model.

  * **`POOL_CAPACITY_INSUFFICIENT`** : the selected zone lacks enough available resources to create the requested number of compute instances. Request fewer resources, select a different machine type or zone, or use the flex-start, spot, or reservation-bound provisioning model.

  * **`ACCELERATOR_INTERCONNECT_CONFIG_FAILED`** : Compute Engine couldn't configure the high-speed interconnect topology required for your accelerator slice, such as a TPU or multi-node GPU slice. Wait a few minutes and retry your request. If the issue persists, then contact your account team or [support](https://docs.cloud.google.com/support).




If your request encounters constraints on multiple physical resources at the same time, then Compute Engine returns a comma-separated list of `reason` codes, such as `"reason": "gpu_availability,local_ssd_availability"`. If your error response includes one or more constraint reasons, then review the following troubleshooting steps for each applicable resource constraint:

  * `configuration_availability`

  * `cpu_availability`

  * `gpu_availability`

  * `local_ssd_availability`

  * `memory_availability`

  * `resource_availability`




#### `configuration_availability`

A `configuration_availability` error indicates that the target zone doesn't support the combination of machine type, CPU platform, or disk interface that you requested. Unlike other resource availability errors, this error indicates an unsupported configuration rather than a temporary resource constraint. If you retry your request at a later time, then the request still fails.

To resolve this error, complete the following steps:

  1. **Verify hardware support** : to confirm whether the target zone supports your requested configuration, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available) and [Machine series comparison](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison).

  2. **Modify your request** : if your hardware configuration is unsupported in that zone, then try one of the following actions:

     * Modify your request to use a machine type, CPU platform, or disk interface that the target zone supports.

     * Retry your request in an alternative zone that supports your required machine series, CPU platform, and disk types.




#### `cpu_availability`

A `cpu_availability` error indicates that the zone lacks capacity for your specified number of CPUs or vCPUs.

To resolve this error, try one or more of the following actions:

  * **Deploy in an alternative zone or region** : if the error message lists available zones (`AVAILABLE_ZONES`), then create or migrate your compute instance to one of those recommended zones. If the error message doesn't list available zones, then try requesting resources in another zone in the same region, or in a different region.

  * **Clear CPU platform restrictions** : if your request specifies a minimum CPU platform (`minCpuPlatform`), then set the value to `AUTOMATIC`. When you require a specific CPU platform, Compute Engine can't place your compute instance on other CPU platforms that your machine series supports in that zone.

  * **Switch to another machine series** : if a specific machine series lacks capacity in your target zone, then try another machine series or generation that supports your workload, such as N2, N2D, or N4. Different machine series use different CPU platforms and physical servers. Later-generation machine series also offer higher performance per vCPU, which can let you run your workload with fewer vCPUs.

  * **Reduce requested vCPUs** : if you use custom machine types, then reduce the vCPU count to the minimum required for your workload. Smaller vCPU configurations fit onto physical servers that have limited remaining capacity, which increases the likelihood that Compute Engine fulfills your request.

  * **Divide compute requirements across smaller machine types** : if your application supports a distributed architecture, then divide your compute footprint across smaller machine types in the same machine family. For example, if you can't create 80 compute instances by using `n2-standard-96` machine types (with 96 vCPUs each), then try creating 160 compute instances by using `n2-standard-48` machine types (with 48 vCPUs each).




#### `gpu_availability`

A `gpu_availability` error indicates that the zone lacks capacity for your requested GPU model.

To resolve this error, try one or more of the following actions:

  * **Deploy in an alternative zone or region** : if the error message lists available zones (`AVAILABLE_ZONES`), then create or migrate your compute instance to one of those recommended zones. If the error message doesn't list available zones, then try requesting resources in another zone or region that supports the same GPU model. For a list of regions and zones that support GPUs, see [GPU availability](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).

  * **Use an alternative provisioning model** : if you can't create GPU instances by using the standard provisioning model, then try requesting resources by using the flex-start, spot, or reservation-bound provisioning model. Different provisioning models draw from separate capacity pools. For more information, see [Compute Engine instances provisioning models](https://docs.cloud.google.com/compute/docs/instances/provisioning-models).




#### `local_ssd_availability`

A `local_ssd_availability` error indicates that the zone lacks capacity for your requested number or types of Local SSD disks.

If your workload tolerates persistent storage, then switch from Local SSD disks to Hyperdisk Extreme, Hyperdisk Balanced, or SSD Persistent Disk volumes. For guidance on performance and durability trade-offs, see [Temporary versus durable storage options](https://docs.cloud.google.com/compute/docs/disks#temp-vs-durable).

#### `memory_availability`

A `memory_availability` error indicates that the zone lacks capacity for your requested amount of memory.

To resolve this error, try one or both of the following actions:

  * **Deploy in an alternative zone or region** : if the error message lists available zones (`AVAILABLE_ZONES`), then create or migrate your compute instance to one of those recommended zones. If the error message doesn't list available zones, then try requesting resources in another zone in the same region, or in a different region.

  * **Divide compute requirements across smaller machine types** : if your application supports a distributed memory architecture, then divide your memory footprint across multiple smaller compute instances. For example, if you can't create a compute instance with 1.88 TB of memory (such as `m1-ultramem-80`), then divide your workload across multiple smaller compute instances that provide that combined memory capacity.




#### `resource_availability`

A `resource_availability` error indicates that the zone lacks capacity for your requested machine type. To resolve this error, try one or more of the following actions:

  * Specify an alternative zone.

  * Select an alternative machine type that supports your workload. For guidance on selecting alternative machine types, see [Recommendations for machine types](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types).

  * If your workload can tolerate interruptions or flexible start times, then specify an alternative provisioning model. For more information, see [Compute Engine instances provisioning models](https://docs.cloud.google.com/compute/docs/instances/provisioning-models).

  * If you encounter this error while requesting an `a3-highgpu-1g`, `a3-highgpu-2g`, or `a3-highgpu-4g` machine type, then verify that you provision the compute instance by using one of the [supported deployment methods](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-high-vms).




### Resolve common errors

If your error message doesn't include a reason code, then adjust the location, the hardware configuration, or the start time of your compute instances. To increase the chances that Compute Engine fulfills your request, try one or more of the following actions:

  * **Try an alternative region or zone** : if your workload permits, then request resources in another zone within the same region, or in a different region. When you create regional MIGs or compute instances in bulk in a region, Compute Engine distributes compute instances across zones that have available hardware. For more information, see [Location flexibility features](https://docs.cloud.google.com/compute/docs/about-infrastructure-flexibility#location-flexibility-features).

  * **Verify reservation properties** : if you can't create a compute instance despite having a matching reservation that isn't fully consumed, then verify that the properties of the reservation and the compute instance match. When properties don't match, Compute Engine attempts to provision on-demand capacity in the target zone instead of using the reservation. This attempt can fail if the zone lacks capacity. To troubleshoot errors when you consume a reservation, see [Troubleshoot reservation consumption](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-consumption).

  * **Adopt machine type flexibility** : rather than replacing a single machine type with another single machine type, expand your options. When you create regional MIGs or compute instances in bulk, specify multiple fallback machine types in an instance flexibility policy. If your primary machine type is unavailable, then Compute Engine provisions an available fallback machine type from your list. You can also divide your compute requirements across smaller machine types with fewer vCPUs and less memory. For more information, see [Machine type flexibility features](https://docs.cloud.google.com/compute/docs/about-infrastructure-flexibility#machine-type-flexibility-features) and [Recommendations for machine types](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types).

  * **Use an alternative provisioning model** : if you can't create compute instances by using the standard provisioning model, then try requesting resources by using the flex-start, reservation-bound, or spot provisioning model. Different provisioning models draw from separate capacity pools. For more information, see [Compute Engine instances provisioning models](https://docs.cloud.google.com/compute/docs/instances/provisioning-models).

  * **Check real-time capacity** : before you create, restart, or update Spot VMs, check the likelihood of obtaining capacity (the _obtainability score_) and the expected uptime across machine types and locations. Because these scores don't guarantee or reserve capacity, submit your request as soon as you check availability. For instructions, see [View the availability of Spot VMs](https://docs.cloud.google.com/compute/docs/instances/view-vm-availability).

  * **Retry your request at a later time** : capacity in a zone changes as workloads across Google Cloud complete and release physical hardware. If your workload is time-flexible, then retry your request at a later time. For more information, see [Time flexibility features](https://docs.cloud.google.com/compute/docs/about-infrastructure-flexibility#time-flexibility-features).




### Resolve errors when you create standalone compute instances

If your request to create standalone compute instances fails due to hardware constraints, then try one or more of the following actions:

  * **Change your request method** : standalone compute instances offer low flexibility during hardware constraints in a zone. If your workload permits, then [create compute instances in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/about-bulk-creation). This creation method lets you do the following:

    * **Add location flexibility** : you can create compute instances in a region instead of a single zone. This approach lets Compute Engine distribute compute instances across zones that have available hardware.

    * **Add machine type flexibility** : you can specify multiple fallback machine types in an [instance flexibility policy](https://docs.cloud.google.com/compute/docs/instances/multiple/about-instance-flexibility-for-bulk-vms). This approach lets Compute Engine select another listed machine type if your primary choice is unavailable.

  * **Reduce requested resources** : select a predefined machine type with fewer vCPUs, less memory, or fewer attached disks. Smaller hardware configurations fit onto physical servers that have limited remaining capacity.

  * **Create custom machine types** : custom machine types use the same physical servers as predefined machine types in the same machine series, and they don't have a separate capacity pool. To fit onto physical servers with limited capacity, request fewer vCPUs than a larger predefined machine type (for example, request a custom machine type with 20 vCPUs instead of an `n2-standard-32`). For accelerator-optimized machine series (such as G2), custom machine types still require physical GPUs and can't resolve a GPU shortage. For instructions, see [Create a VM with a custom machine type](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type).

  * **Change storage types** : if your machine type supports alternative storage options, then switch between Google Cloud Hyperdisk and Persistent Disk. SSD Persistent Disk and Balanced Persistent Disk share the same physical storage pool. If one disk type lacks capacity in a zone, then the other disk type is also unavailable in most cases. If a Persistent Disk volume lacks capacity, then verify that your project has sufficient quota for Hyperdisk, and switch to a machine type that supports Hyperdisk volumes. To review which machine series support both Persistent Disk and Hyperdisk volumes, see [Machine series comparison](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison).




### Resolve errors when you create compute instances in bulk

When you create compute instances in bulk (`bulkInsert`), Compute Engine checks capacity upfront without queuing or retrying your request. By default, the minimum count (`minCount`) equals the total requested count (`count`), so if Compute Engine can't create all requested compute instances at the time of your request, then the request fails and creates no compute instances.

If your request to create compute instances in bulk fails due to hardware constraints, then try one or more of the following actions. For guidance on how to evaluate trade-offs and best practices, see [Evaluate and adopt flexible infrastructure](https://docs.cloud.google.com/compute/docs/about-infrastructure-flexibility#evaluate-adopt-flexible-infrastructure).

  * **Accept partial capacity (`minCount`)**: if your workload can start with fewer compute instances than the total count that you requested, then set a lower value in the `minCount` field. This setting lets your request succeed as long as Compute Engine can provision at least your minimum number of compute instances.

  * **Create compute instances in a region** : if you create compute instances in bulk in a specific zone, then your request fails when that zone lacks capacity. Instead, target a region so that Compute Engine selects zones that have available hardware. By default, regional bulk creation uses the `ANY_SINGLE_ZONE` target distribution shape, which places all compute instances in a single zone that has capacity. If no single zone can fit your full batch and your compute instances can span multiple zones, then set the target distribution shape to `BALANCED` or `ANY`. For instructions, see [Create VMs in bulk in a region](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk#create-vms-bulk-region).

  * **Use fallback machine types** : in a regional bulk request, configure an [instance flexibility policy](https://docs.cloud.google.com/compute/docs/instances/multiple/about-instance-flexibility-for-bulk-vms) with compatible fallback machine types. If needed, you can also restrict placement to specific zones by using the `--location-policy` flag. If your primary machine type is unavailable, then Compute Engine provisions available fallback machine types from your list.

**Caution:** If you change the machine type, then the costs for vCPUs, memory, and any resources attached to your compute instances might change. For more information, see [VM instance pricing](https://docs.cloud.google.com/compute/vm-instance-pricing).
  * **Split your request across locations or over time** : if no single zone or region has enough capacity for your full batch, then divide your request into smaller batches across different zones or regions, or stagger your requests over time. Don't send multiple smaller requests to the same exhausted zone at the same time.

  * **Relax compact placement constraints** : if you specify a compact placement policy when you create compute instances, then consider increasing the maximum distance value or removing the policy to relax placement constraints. Lower maximum distance values place compute instances closer to reduce network latency, but they increase the risk of encountering resource availability errors. For more information, see [About compact placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies).




### Resolve errors when you create, scale, or repair MIGs

Unlike standalone or bulk creation requests, a MIG provisions as many compute instances as current capacity allows. For any compute instances that the MIG can't create yet, the group logs errors in [List instance errors](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#listing_instance_errors) and continues to retry creation in the background.

If your MIG encounters resource availability errors when it creates, scales out, or repairs compute instances, then try one or more of the following actions:

  * **Wait or adjust the target size** : if the hardware shortage is temporary and your workload can run with partial capacity, then let the MIG continue to retry, or reduce the target size of the MIG.

  * **Update the instance template** : if the instance error list shows a `configuration_availability` error (unsupported hardware in the zone) or persistent capacity exhaustion on one machine type, then create and roll out an updated instance template that uses a supported or more available machine type, or an alternative provisioning model. This approach works on any existing zonal or regional MIG without migrating to a new group.

  * **Replace a stuck zonal MIG with a regional MIG** : if a zonal MIG experiences recurring capacity shortages and your workload requires ongoing multi-zone resilience, then create a [regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs), migrate your workload to the new group, and delete the original zonal MIG. Regional MIGs increase the likelihood of obtaining hardware because they can provision compute instances across multiple zones in the region.

  * **Configure a flexible target distribution shape** : with the `EVEN` distribution shape, a regional MIG provisions an equal share of compute instances in each zone. If one zone lacks capacity, then other zones in the region still create their share of compute instances while the constrained zone retries its share. Autoscaled MIGs with an `EVEN` distribution shape also continue to scale out in available zones. This behavior leaves a manually sized group below its full target size until capacity recovers in the constrained zone. To avoid this limitation, configure your regional MIG to use a [target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape) that matches your workload requirements:

    * `BALANCED`: spreads compute instances across zones that have available capacity while keeping the distribution as even as possible. Use this shape for high-availability serving and batch workloads.

    * `ANY`: places compute instances in any zone that has available capacity and prioritizes unused reservations in the region. Use this shape for batch workloads that don't require balanced distribution across zones.

    * `ANY_SINGLE_ZONE`: colocates all compute instances in a single zone that has available capacity, which avoids cross-zone latency and network egress costs. Use this shape for tightly coupled, latency-sensitive workloads.

  * **Configure machine type flexibility in your regional MIG** : in a regional MIG that uses the `BALANCED`, `ANY`, or `ANY_SINGLE_ZONE` distribution shape, add fallback machine types in an instance flexibility policy (`instanceFlexibilityPolicy`). If the primary machine type is unavailable when the MIG scales out, then the MIG provisions the next available machine type in your list. By default, repairs retry only the failed compute instance's original machine type. To allow repairs to use fallback machine types as well, enable [update on repair](https://docs.cloud.google.com/compute/docs/instance-groups/update-on-repair) by setting the `instanceLifecyclePolicy.forceUpdateOnRepair` field to `"YES"`. For single-zone workloads, use a regional MIG with the `ANY_SINGLE_ZONE` shape or select a single target zone. For more information, see [About instance flexibility in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility).

  * **Allow repairs in an alternate zone** : in a stateless regional MIG that uses the `BALANCED` or `ANY` distribution shape, configure the group to recreate failed compute instances in another zone during repair. This setting applies only when the MIG repairs existing compute instances that fail. To place new compute instances in available zones during creation or scale-out, use the `BALANCED` or `ANY` distribution shape. To enable alternate-zone repair, set both the `instanceLifecyclePolicy.onRepair.allowChangingZone` field and the `instanceLifecyclePolicy.forceUpdateOnRepair` field to `"YES"`. For instructions, see [Repair a VM in an alternate zone](https://docs.cloud.google.com/compute/docs/instance-groups/repair-vm-in-alternate-zone).

  * **Queue capacity requests for scarce hardware** : for batch or AI/ML workloads that require scarce hardware (such as GPUs) and can tolerate a flexible start time, use [MIG resize requests](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig) to queue your request and provision the requested compute instances together when capacity becomes available, or [create a MIG with Flex-start VMs](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-flex-start-vms).

  * **Relax compact placement constraints** : if you specify a compact placement policy when you create compute instances, then consider increasing the maximum distance value or removing the policy to relax placement constraints. Lower maximum distance values place compute instances closer to reduce network latency, but they increase the risk of encountering resource availability errors. For more information, see [About compact placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies).

  * **Monitor compute instance distribution** : during group creation and scale-out, when a regional MIG that uses the `BALANCED`, `ANY`, or `ANY_SINGLE_ZONE` distribution shape satisfies its target size by using available zones or fallback machine types, the group doesn't log resource availability errors. However, during repairs, if a failed compute instance's original machine type is unavailable, then the MIG logs `ZONE_RESOURCE_POOL_EXHAUSTED` errors even when you enable update on repair. To see where Compute Engine placed your compute instances across zones and machine types, check the **Monitoring** tab for the MIG in the Google Cloud console or view the Cloud Monitoring dashboard. For instructions, see [Monitor instance distribution in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/monitor-instance-distribution).




### Resolve errors when you create sole-tenant nodes

If Compute Engine can't allocate physical servers for your sole-tenant nodes, then try one or both of the following actions:

  * **Use a different node type** : choose a different node template or node type that offers different hardware configurations. For more information, see [Sole-tenancy overview](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).

  * **Optimize node capacity with CPU overcommit** : if you try to add nodes because you ran out of capacity for new compute instances on your existing nodes, then consider enabling CPU overcommit. This feature lets you increase the density of compute instances on your current physical servers, which avoids the need to provision additional nodes. For more information, see [Overcommit CPUs on sole-tenant VMs](https://docs.cloud.google.com/compute/docs/nodes/overcommitting-cpus-sole-tenant-vms).




### Resolve errors when you create TPU slices

If your request to create or scale TPU slices fails because a zone lacks connected physical hardware, then try one or more of the following actions:

  * **Use Flex-start VMs, future reservations in calendar mode, or queued resources** : instead of submitting unreserved on-demand TPU requests, use [Flex-start VMs](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms) or [future reservations in calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview) to schedule or queue your TPU slice request on Compute Engine. If you provision TPUs through the Cloud TPU API instead of Compute Engine, then use the [Queued Resources API](https://docs.cloud.google.com/tpu/docs/queued-resources) to queue your request until contiguous capacity becomes available in the zone.

  * **Evaluate smaller topologies** : if your machine learning (ML) framework supports smaller slice sizes, then request smaller topologies. Larger TPU slices require connected physical hardware located together, which might be unavailable in a single zone. If your model requires a high-bandwidth inter-chip interconnect (ICI) across all TPUs, then you might need to adjust your settings for model sharding or parallelization. For more information, see [TPU topology](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_topology).

**Caution:** If you reduce the topology size, then you might need to change how you split your workload or run it in parallel. This adjustment is necessary because of strict ICI requirements. If you can't resize your workload, then contact your account team or the sales team.
  * **Retry after interconnect configuration errors** : if your request fails with an `ACCELERATOR_INTERCONNECT_CONFIG_FAILED` error, then wait a few minutes and retry your request. If the issue persists, then contact your account team or [support](https://docs.cloud.google.com/support).




### Resolve errors when you create a reservation

If your request to reserve resources fails due to capacity constraints, then try one or more of the following actions:

  * **View future availability in calendar mode** : if you create a future reservation request in calendar mode, then view the future availability of resources before you submit your request. When you specify resources that are available during a specific time slot, you increase the likelihood that Google Cloud approves your request. For instructions, see [View resource future availability](https://docs.cloud.google.com/compute/docs/instances/create-future-reservations-calendar-mode#view-availability).

  * **Reduce the number of reserved compute instances** : try reserving a smaller number of compute instances. If you require a large number of reserved compute instances, then consider creating multiple smaller reservations for those compute instances across different regions or zones.

  * **Relax compact placement constraints** : if you specify a compact placement policy when you create an on-demand reservation, then consider increasing the maximum distance value or removing the policy to relax placement constraints. Compact placement policies help you reserve compute instances close to each other to reduce network latency, but they increase the risk of encountering resource availability errors. For more information, see [About compact placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies).




### Resolve errors when you update machine types

To update an existing compute instance's machine type, you must stop the compute instance before you apply the change. If you try to start the compute instance with the new machine type and the request fails due to hardware constraints, then your compute instance remains stopped until you start it again.

To update and restart your compute instance, try one or both of the following actions:

  * **Revert to the original machine type or use an alternative machine type** : if the target hardware configuration is unavailable, then change the machine type back to the previous configuration or use an intermediate machine type that supports your workload. After you take one of these actions, restart your compute instance. Because the compute instance ran on that configuration before you stopped it, this reversion lets you restart your workload while you evaluate alternative options or request capacity in another zone.

  * **Move your workload to another zone** : if your target machine type is unavailable in your current zone, then move your workload to a zone that has capacity. Because compute instances are zonal resources, take a snapshot of the boot disk and any attached disks. Then, create a replacement compute instance in the target zone with the new machine type. For instructions, see [Move a VM instance between zones or regions](https://docs.cloud.google.com/compute/docs/instances/moving-instance-across-zones).




## Summary of recommendations by workload requirements

To evaluate alternative approaches based on what aspects of your workload you can adjust, see the following table:

What you must keep | What you can adjust | Recommendation | Applicable features  
---|---|---|---  
Location (a specific zone or region) | Machine series or type | Configure fallback machine types with [ instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility), or divide compute requirements across smaller machine types that [ support your workload](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types). | 

  * Standalone compute instances
  * Compute instances in bulk
  * MIGs
  * Sole-tenant nodes

  
Machine type (a specific configuration) | Location | Request resources in a different [region or zone](https://docs.cloud.google.com/compute/docs/regions-zones#available), use a flexible [ target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape) (`BALANCED`, `ANY`, or `ANY_SINGLE_ZONE`), or enable [ alternate-zone repair](https://docs.cloud.google.com/compute/docs/instance-groups/repair-vm-in-alternate-zone) for regional MIGs that use the `BALANCED` or `ANY` shape. | 

  * Standalone compute instances
  * Compute instances in bulk
  * MIGs
  * Reservations

  
Specific hardware (such as a specific GPU model) | The start time or provisioning model | Use [ Flex-start VMs](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms), [MIG resize requests](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig), [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot) (including when you create compute instances in bulk), [ future reservations in calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview), or [queued resources for TPUs](https://docs.cloud.google.com/tpu/docs/queued-resources). | 

  * Standalone compute instances
  * Compute instances in bulk
  * MIGs
  * Reservations
  * TPUs

  
Immediate startup for available compute instances | Initial compute instance count | Set a lower `minCount` value when you create compute instances in bulk to accept partial capacity, or use a MIG to start available compute instances right away while the group retries obtaining the remaining compute instances. | 

  * Compute instances in bulk
  * MIGs

  
  
## What's next

  * Learn how to [optimize compute provisioning](https://docs.cloud.google.com/compute/docs/about-infrastructure-flexibility).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

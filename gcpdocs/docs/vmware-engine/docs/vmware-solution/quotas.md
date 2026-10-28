---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/quotas/
title: Quotas and limits \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T20:28:04.763327+00:00
---

# Quotas and limits  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides (VMware solution) ](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quotas and limits

This document describes the Compute Engine (`compute.googleapis.com`) quotas and system limits required to deploy and scale VMware solution on Google Cloud environments.

Because VMware solution provisions bare-metal `z3` Compute Engine instances, Virtual Private Cloud (VPC) networks, Layer 2 broadcast subnets, and regional internal load balancers directly in your Google Cloud project, your deployment consumes Compute Engine quotas rather than Google Cloud VMware Engine API (`vmwareengine.googleapis.com`) node quotas. In VMware solution, each bare-metal node corresponds to one `z3-highmem-192-highlssd-metal` Compute Engine instance.

**Note:** Quotas define the maximum amount of a resource that your project can use, but they don't guarantee hardware capacity availability in a region or zone. If you plan to deploy a large number of bare-metal nodes or run business-critical workloads, contact your Google Cloud account team or Cloud Customer Care to plan capacity in your target region and zone.

## Required Compute Engine quotas

Before you deploy a VMware Cloud Foundation (VCF) instance, add a vSphere cluster, or add bare-metal nodes to an existing cluster, verify that your Google Cloud project has sufficient quota for the following `compute.googleapis.com` metrics.

In the following table, N represents the total number of VMware solution bare-metal nodes—`z3-highmem-192-highlssd-metal` Compute Engine instances—deployed in the target region or VPC network. A standard high-availability vSphere cluster requires a minimum of four bare-metal nodes, where N is at least 4.

Resource | Quota metric | Scope | Required quota for N nodes  
---|---|---|---  
VPC networks | `compute.googleapis.com/networks` | Global | 1 VPC network per VCF instance.  
Subnets per VPC network | `compute.googleapis.com/subnet_ranges_per_vpc_network` | Global | Minimum 4 subnets for management, vMotion, vSAN, and NSX Tunnel Endpoint (TEP).  
VM instances | `compute.googleapis.com/instances` | Regional | N instances, with a minimum of 4 per cluster, plus any jumpbox or helper VMs.  
Instances per VPC network | `compute.googleapis.com/instances_per_vpc_network` | Global | N instances, with a minimum of 4 per cluster, plus any jumpbox or helper VMs.  
CPUs per VM family for `Z3` | `compute.googleapis.com/cpus_per_vm_family` | Regional | N × 192 vCPUs. A 4-node cluster uses 768 vCPUs.  
Local SSD storage per VM family for `Z3` | `compute.googleapis.com/local_ssd_total_storage_per_vm_family` | Regional | N × 72 TB. A 4-node cluster uses 288 TB.  
Google Cloud Hyperdisk Balanced total storage | `compute.googleapis.com/hyperdisk_balanced_total_storage` | Regional | N × 128 GB. Each bare-metal node uses a 128 GB boot disk, or 512 GB for a 4-node cluster.  
Google Cloud Hyperdisk Balanced provisioned IOPS | `compute.googleapis.com/hyperdisk_balanced_total_provisioned_iops` | Regional | N × 3,000 IOPS by default, or up to N × 10,000 IOPS.  
Regional backend services with Fast IP Move (`GARP_RA`) | `compute.googleapis.com/regional_backend_services_protocol_forwarding_fast_ha` | Regional | 1 per VCF management appliance virtual IP (VIP) address and NSX Edge endpoint, which is typically 15 to 20 per VCF instance, or up to 50 depending on the deployed appliances.  
Internal protocol forwarding HA rules per VPC network | `compute.googleapis.com/internal_protocol_forwarding_ha_rules_per_vpc_network` | Global | 1 per regional backend service with Fast IP Move, proportional to the number of VCF management appliance VIPs and up to 50 per VCF instance.  
Network endpoint groups (NEGs) | `compute.googleapis.com/network_endpoint_groups` | Regional | 2 zonal NEGs per zone: 1 for the management subnet and 1 for the NSX TEP subnet.  
Resource policies for placement policies | `compute.googleapis.com/resource_policies` | Regional | 1 spread placement policy per vSphere cluster.  
Static routes per VPC network | `compute.googleapis.com/static_routes_per_vpc_network` | Global | Varies based on your network topology. Static VPC routing uses 1 static route per NSX overlay segment.  
  
### Example quota calculation

To calculate the regional quota required for a deployment that consists of a four-node management domain cluster and a three-node VI workload domain cluster in the same region—seven bare-metal nodes in total—multiply the per-node values by 7:

  * **`compute.googleapis.com/cpus_per_vm_family` for `Z3`**: 7 × 192 = 1,344 vCPUs.
  * **`compute.googleapis.com/local_ssd_total_storage_per_vm_family` for `Z3`**: 7 × 72 TB = 504 TB.
  * **`compute.googleapis.com/hyperdisk_balanced_total_storage`** : 7 × 128 GB = 896 GB.
  * **`compute.googleapis.com/resource_policies`** : 2 spread placement policies.



Compare these totals against the effective quota limits in your project before you provision the nodes.

## Layer 2 broadcast subnet limits

Subnets configured with the **Resolve Subnet Mask** property set to **Broadcast primary range only with learning** enforce the following system limits. Quota increases aren't supported for these limits:

  * **Endpoints per broadcast subnet** : Up to 64 network interface card (NIC) endpoints per broadcast-enabled subnet.
  * **Broadcast subnets per VPC network** : Up to 64 broadcast-enabled subnets per VPC network per region.
  * **Learned custom MAC addresses** : Up to 1,000 learned custom MAC addresses per VPC network across all regions.



For more information about Layer 2 broadcast subnets and MAC learning limits, see [Layer 2 emulation: ARP broadcasting and custom MAC learning](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/architecture-node-networking#layer2-emulation).

## View your current quota

You can view your Compute Engine quota limits and usage in the Google Cloud console or by using the `gcloud` CLI:

###  Google Cloud console 

  1. In the Google Cloud console, go to **IAM & Admin** > **Quotas & System Limits**.

[Go to Quotas & System Limits](https://console.cloud.google.com/iam-admin/quotas)

  2. In the **Filter** bar, filter by **Service: Compute Engine API**.

  3. To view regional quotas for your target deployment region, filter by dimension for `region=REGION`, such as `region=us-east4`.

  4. To filter for `Z3` bare-metal CPU or local SSD quotas, filter by dimension for `vm_family=Z3`, or filter by quota metric name for `cpus_per_vm_family` or `local_ssd_total_storage_per_vm_family`.




###  gcloud 

To list the quota limits for your target project and region, run the following `gcloud alpha services quota list` command:
    
    
    gcloud alpha services quota list \
        --service=compute.googleapis.com \
        --consumer="projects/PROJECT_ID" \
        --filter="metric:(cpus_per_vm_family OR local_ssd_total_storage_per_vm_family OR hyperdisk_balanced_total_storage OR regional_backend_services_protocol_forwarding_fast_ha OR resource_policies)" \
        --format="table(metric,unit,consumerQuotaLimits.quotaBuckets.effectiveLimit,consumerQuotaLimits.quotaBuckets.dimensions)"
    

Replace `PROJECT_ID` with the ID of your target Google Cloud project.

## Request a quota increase

If your planned deployment or cluster expansion exceeds the quota limits in your project, submit a quota increase request before you provision new nodes:

  1. In the Google Cloud console, go to **IAM & Admin** > **Quotas & System Limits**.

[Go to Quotas & System Limits](https://console.cloud.google.com/iam-admin/quotas)

  2. Filter the list by **Service: Compute Engine API** and by your target region, such as `region=us-east4`.

  3. Select the checkbox next to each quota entry that you want to increase, such as **CPUs per VM family** with `vm_family: Z3` and **Local SSD total storage per VM family** with `vm_family: Z3`.

  4. Click **Edit**.

  5. In the **Quota changes** pane, enter the new total limit that you want to request for each selected metric, and then click **Done**.

  6. In the **Request description** field, enter a brief description of your VMware solution deployment, and then click **Submit request**.




## What's next

  * Learn about bare-metal machine types in [Bare-metal nodes and machine types](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/concepts-nodes).
  * Review cluster sizing guidelines in [About vSphere clusters](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/concepts-clusters).
  * Deploy nodes and configure appliance networking in [Deploy nodes and configure appliance networking by using the console](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deploy) or [Deploy nodes and VCF by using Terraform and toolkit](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deploy-terraform).
  * Scale existing deployments in [Add a vSphere cluster to a domain](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/add-cluster) or [Add or remove nodes in a vSphere cluster](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/expand-cluster).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/architecture-network-appliances/
title: High availability load balancing for VCF appliances \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T20:28:01.587854+00:00
---

# High availability load balancing for VCF appliances  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/architecture-network-appliances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides (VMware solution) ](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# High availability load balancing for VCF appliances

This document explains how regional internal load balancers and zonal network endpoint groups (NEGs) in VMware solution on Google Cloud provide Layer 2 high availability, virtual machine mobility (vMotion), and automated failover for VMware Cloud Foundation (VCF) management appliances deployed in the Virtual Private Cloud (VPC) underlay, as shown in the following diagram (click to enlarge):

![Internal load balancer and regional backend service with GARP_RA steering traffic through a zonal NEG during vMotion.](https://docs.cloud.google.com/static/vmware-engine/images/vmware-solution-network-appliances.png)![Internal load balancer and regional backend service with GARP_RA steering traffic through a zonal NEG during vMotion.](https://docs.cloud.google.com/static/vmware-engine/images/vmware-solution-network-appliances.png)

## Why underlay appliances require a load balancer

In on-premises data centers, management virtual machines—such as vCenter Server, SDDC Manager, and clustered NSX Manager nodes—rely on physical Layer 2 broadcast domains. When an appliance fails over or migrates between ESXi hosts by using vMotion, the appliance broadcasts a Gratuitous ARP (GARP) packet to update the MAC address tables of physical top-of-rack (ToR) switches so that its IP address floats across physical servers.

A Google Cloud VPC network is a routed Layer 3 software-defined network (SDN) with the following behaviors:

  * Every IP address is programmatically bound to a specific Compute Engine virtual network interface (vNIC) in the SDN forwarding table.
  * The VPC routing plane doesn't rely on physical switch MAC learning to route Layer 3 traffic to floating IP addresses.
  * If an underlay management VM moves to a different bare-metal ESXi host, the VPC routing table requires an explicit mechanism to steer traffic for that appliance's IP address to the new host interface.



To support IP mobility without manual route updates or VM re-addressing, VMware solution provisions a regional internal passthrough Network Load Balancer configured with Fast IP Move (`GARP_RA`) for each floating underlay management appliance.

## High-availability architecture components

Each network appliance in VMware solution uses a three-tier Google Cloud load balancing architecture to support high availability and vMotion mobility:

### Zonal network endpoint groups (NEGs)

  * **Construct type** : Zonal NEGs of type `GCE_VM_IP_DEDICATED_BACKEND` configured in the target VPC subnet.
  * **Function** : A dedicated NEG in each zone groups the primary or dynamic network interfaces of all bare-metal ESXi instances that belong to the cluster's vMotion mobility domain.
  * **Reusability** : All underlay appliance load balancers within the same cluster and subnet share a single set of zonal NEGs.



### Regional backend service with Fast IP Move

  * **Construct type** : Regional backend service (`loadBalancingScheme: INTERNAL`, `protocol: UNSPECIFIED`) that references the cluster's zonal NEGs.
  * **Failover policy (`haPolicy`)**: Configured with `fastIPMove: GARP_RA`.
  * **Function** : Instructs the Google Cloud Andromeda data plane to monitor the broadcast-enabled subnet for GARP and Router Advertisement (RA) frames emitted by the management appliance VM and dynamically update the active backend host.



### Regional internal passthrough Network Load Balancer

  * **Construct type** : Regional internal forwarding rule configured with the appliance's reserved virtual IP (VIP) address.
  * **Function** : Serves as the persistent IP endpoint for the management appliance or cluster VIP. Administrators, workloads, and other VCF components connect to this VIP address.



## Underlay high availability with dedicated NEGs

When multiple network interfaces (such as the primary `nic0` interface and VLAN-tagged Dynamic NICs) connect to the same VPC network, standard `GCE_VM_IP` NEGs cannot target arbitrary sub-interfaces. Instead, VMware solution uses `GCE_VM_IP_DEDICATED_BACKEND` NEGs, which operate as follows:

  * **Automatic interface targeting** : Automatically attaches the specific primary vNIC or Dynamic NIC that matches the NEG's subnet.
  * **Single NEG per zone** : A regional backend service configured with `GCE_VM_IP_DEDICATED_BACKEND` NEGs can contain only one NEG per zone.
  * **Internal HA policy requirement** : `GCE_VM_IP_DEDICATED_BACKEND` NEGs are supported only with regional backend services configured for internal passthrough Network Load Balancers (`loadBalancingScheme: INTERNAL`) that use `haPolicy`.



### HA policy restrictions on broadcast subnets

When you deploy `haPolicy` backend services in subnets with ARP broadcasting and MAC learning enabled, the following rules apply:

  * **Load balancing scheme** : Only internal passthrough Network Load Balancers (`INTERNAL`) are supported.
  * **Subnet alignment** : All backend NEGs across all zones for a given backend service must belong to the same VPC subnet.
  * **Forwarding rule mapping** : A backend service configured with broadcast NEGs can be referenced by only one forwarding rule.
  * **Immutable backend subnet type** : You must attach backends in an ARP broadcasting subnet when you create the backend service; you can't replace them with backends in non-broadcast subnets later.



### Prevent HA policy cross-claiming

In an ARP-broadcast-enabled subnet, a host interface that belongs to one HA policy backend service could temporarily claim leadership for an unrelated HA policy if it broadcasts a GARP frame for that policy's forwarding rule VIP.

To prevent unintended cross-claiming, include the exact same set of ESXi host backends (all hosts in the cluster's zonal NEG) across all HA policy backend services operating in that subnet.

## What's next

  * Review overlay routing and NSX Edge high availability in [NSX overlay and edge routing](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/architecture-nsx).
  * Learn how to configure appliance networking by using the console in [Deploy nodes and configure appliance networking by using the console](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deploy).
  * Learn how to add VCF management appliances on day 2 in [Add VCF appliances by using Terraform](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/vcf-appliance-addition).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

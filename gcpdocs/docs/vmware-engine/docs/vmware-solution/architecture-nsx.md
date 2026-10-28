---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/architecture-nsx/
title: NSX overlay and edge routing \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T20:27:55.229224+00:00
---

# NSX overlay and edge routing  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/architecture-nsx/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides (VMware solution) ](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# NSX overlay and edge routing

VMware solution on Google Cloud uses VMware NSX to provide software-defined networking (SDN) and security for your VMware Cloud Foundation (VCF) workload virtual machines (VMs). This document describes how NSX overlay networking interacts with the Google Cloud Virtual Private Cloud (VPC) underlay and compares the routing architectures between NSX Edge nodes and your VPC network.

## Overview of NSX in Google Cloud

In VMware solution, the Google Cloud VPC network provides the physical and virtualized underlay for your bare-metal ESXi hosts (`Compute Engine` `z3-highmem-192-highlssd-metal` instances) and management appliances. VMware NSX sits on top of this underlay to provide an abstracted network topology for your VCF workload VMs:

  * **Geneve overlay encapsulation** : ESXi hosts and NSX Edge nodes establish Transport Endpoint (TEP) interfaces (`vmk10` or `vmk3`) on the dedicated `NSX-TEP` VPC subnet. Workload VM traffic is encapsulated in Geneve packets (UDP port `6081`) and routed between host TEPs over the Google Cloud VPC underlay using a maximum transmission unit (MTU) of `8896` bytes.
  * **Decoupled IP addressing** : Workload VMs connected to NSX overlay segments can use arbitrary IP address ranges without consuming IP addresses from the underlying Google Cloud VPC subnets or hitting VPC subnet IP quotas.
  * **Multi-tier routing architecture** : 
    * **Tier-1 (T1) gateways** : Provide east-west routing between overlay segments, localized DHCP services, and gateway firewall rules.
    * **Tier-0 (T0) gateways** : Provide north-south routing between the NSX overlay environment and the underlying Google Cloud VPC network.
  * **Distributed security** : The NSX Distributed Firewall (DFW) enforces stateful microsegmentation policies directly at the virtual network interface card (vNIC) of each workload VM, regardless of which overlay segment or ESXi host the VM resides on.



## Underlay versus overlay topology

The network architecture is divided into two distinct layers—the Google Cloud VPC underlay and the VMware NSX overlay—as shown in the following diagram (click to enlarge):

![Google Cloud VPC underlay hosting Z3 instances and VCF appliances below the VMware NSX overlay.](https://docs.cloud.google.com/static/vmware-engine/images/vmware-solution-nsx-underlay-overlay.png)![Google Cloud VPC underlay hosting Z3 instances and VCF appliances below the VMware NSX overlay.](https://docs.cloud.google.com/static/vmware-engine/images/vmware-solution-nsx-underlay-overlay.png)

The following table summarizes the components and responsibilities of each network layer:

Network layer | Primary components | Responsibilities  
---|---|---  
**Google Cloud VPC underlay** | 

  * Bare-metal ESXi hosts (primary NICs and Dynamic NICs)
  * VCF management VMs (vCenter Server, SDDC Manager, NSX Manager cluster, VMware HCX)
  * VPC subnets (`Management`, `vSAN`, `vMotion`, `NSX-TEP`, `NSX-Uplink`)
  * Regional internal load balancers and Network Connectivity Center Router Appliances

| 

  * Provides IP reachability between ESXi host VMkernel ports
  * Hosts VCF control plane appliances directly on VPC subnets
  * Transports encapsulated Geneve packets between ESXi host TEPs and NSX Edge TEPs
  * Connects the on-premises networks, peered VPCs, and Google Cloud services

  
**NSX SDN overlay** | 

  * NSX Edge clusters (Tier-0 and Tier-1 logical routers)
  * NSX overlay segments
  * Workload VMs
  * NSX Distributed Firewall (DFW) and Gateway Firewall

| 

  * Provides isolated Layer 2 domains and east-west routing for workload VMs
  * Advertises workload CIDR blocks to the VPC underlay through Tier-0 gateways
  * Provides load balancing, NAT, and north-south edge security

  
  
## Advanced architecture use cases

You can structure your NSX and VPC topologies to support different isolation and multi-tenancy requirements:

  * **Consolidated workload domains in a single VPC** : Deploy your VCF management domain and one or more VI workload domains within a single Google Cloud VPC network. Each workload domain uses dedicated `vSAN`, `vMotion`, and `NSX-TEP` subnets within the same VPC while sharing or isolating NSX Edge clusters for north-south routing.
  * **Multi-VPC mappings** : Connect distinct NSX Tier-0 gateways or separate NSX Edge clusters to isolated Google Cloud VPC networks (for example, separate VPCs for production workloads, perimeter networks, and shared services). This topology preserves strict VPC-level firewall and routing boundaries in Google Cloud while maintaining centralized VCF lifecycle management.



## NSX Edge routing

To route traffic between NSX overlay segments and your Google Cloud VPC network, NSX Edge VMs must exchange routes or forward packets over the `NSX-Uplink` VPC subnet. You can configure north-south routing between NSX Tier-0 gateways and your VPC network by using either of the following options:

  * Option 1: VPC static routing (active-standby)
  * Option 2: Dynamic BGP routing by using Network Connectivity Center Router Appliance (active-active)



### Option 1: VPC static routing (active-standby)

In a static routing topology, an active-standby pair of NSX Edge nodes uses a floating virtual IP address (VIP) on the `NSX-Uplink` VPC subnet fronted by a regional internal passthrough Network Load Balancer, as shown in the following diagram (click to enlarge):

![VPC static routes directing NSX overlay traffic through an internal load balancer to active-standby NSX Edge nodes.](https://docs.cloud.google.com/static/vmware-engine/images/vmware-solution-nsx-static-routing.png)![VPC static routes directing NSX overlay traffic through an internal load balancer to active-standby NSX Edge nodes.](https://docs.cloud.google.com/static/vmware-engine/images/vmware-solution-nsx-static-routing.png)

  * **Routing mechanism** : You create custom static routes in your Google Cloud VPC route table that specify your NSX overlay workload CIDR blocks as the destination and the NSX Edge floating VIP (or internal load balancer forwarding rule) as the next hop.
  * **High availability** : When you use a regional internal backend service with the `GARP_RA` high-availability policy (or an alias IP range handover), traffic automatically redirects to the standby NSX Edge node if the active Edge node fails.
  * **Use case** : Best suited for smaller deployments or static overlay topologies where workload CIDR blocks don't change frequently and single-edge bandwidth meets your throughput requirements.



### Option 2: Dynamic BGP routing by using Network Connectivity Center Router Appliance (active-active)

To configure dynamic route exchange and horizontal bandwidth scaling, use Border Gateway Protocol (BGP) peering between your NSX Tier-0 gateway and Cloud Router by using Network Connectivity Center Router Appliance, as shown in the following diagram (click to enlarge):

![Cloud Router peering over BGP with NSX Edge Router Appliances pinned to Z3 hosts by DRS affinity rules.](https://docs.cloud.google.com/static/vmware-engine/images/vmware-solution-nsx-bgp-ncc.png)![Cloud Router peering over BGP with NSX Edge Router Appliances pinned to Z3 hosts by DRS affinity rules.](https://docs.cloud.google.com/static/vmware-engine/images/vmware-solution-nsx-bgp-ncc.png)

  * **Dynamic route exchange** : The NSX Tier-0 gateway automatically advertises newly created NSX overlay segment CIDR blocks to Cloud Router over BGP, and learns VPC and on-premises routes (`0.0.0.0/0` or specific prefixes) through custom route advertisements. This architecture eliminates manual VPC static route updates.
  * **Active-active ECMP scaling** : Supports Equal-Cost Multi-Path (ECMP) routing across up to eight active NSX Edge nodes per Tier-0 gateway, scaling north-south throughput and supporting failover with Bidirectional Forwarding Detection (BFD).
  * **Edge-to-host pinning requirement** : Because an NSX Edge VM runs inside an ESXi host, its virtual uplink interface maps to a specific Dynamic NIC on the underlying bare-metal Compute Engine instance. To ensure that Cloud Router forwards BGP and data plane traffic to the exact bare-metal host where each NSX Edge VM resides, you must configure VMware Distributed Resource Scheduler (DRS) affinity rules (`VM-Host` affinity rules) to pin each NSX Edge VM to its designated ESXi host.
  * **Redundant BGP sessions** : Configure dual BGP sessions between each NSX Edge node's uplink interfaces on the `NSX-Uplink` subnet and redundant Cloud Router interfaces to maintain continuous control plane availability during host maintenance events.



## What's next

  * Review [Underlay VPC networking, Layer 2 MAC learning, and DNS](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/architecture-node-networking) to understand how Dynamic NICs map to ESXi physical adapters.
  * Learn about [High availability load balancing for VCF appliances](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/architecture-network-appliances) for VCF management VMs and NSX Edge nodes.
  * Read the [Deployment options overview](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deployment-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

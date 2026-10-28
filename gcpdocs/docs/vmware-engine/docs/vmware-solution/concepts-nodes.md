---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/concepts-nodes/
title: Bare-metal nodes and machine types \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T20:28:20.186321+00:00
---

# Bare-metal nodes and machine types  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/concepts-nodes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides (VMware solution) ](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Bare-metal nodes and machine types

This page describes bare-metal nodes and supported machine types in VMware solution on Google Cloud.

In VMware solution, nodes are dedicated bare-metal Compute Engine instances provisioned directly in your Google Cloud project. Each bare-metal instance runs VMware ESXi and provides dedicated CPU, memory, local NVMe SSD storage, and a 200 Gbps network interface card (NIC) connected to your Virtual Private Cloud (VPC) underlay subnets to form the hyperconverged infrastructure for your VMware Cloud Foundation (VCF) environment.

## Supported Compute Engine machine types

The following table lists the Compute Engine bare-metal machine type supported for VMware solution hosts:

Machine type | vCPUs (physical cores) | Memory (GiB) | Local NVMe SSD storage (TiB) | Network bandwidth  
---|---|---|---|---  
`z3-highmem-192-highlssd-metal` | 192 (96) | 1,536 | 70.31 | 200 Gbps  
  
## Node architecture and deployment

When you deploy VMware solution bare-metal nodes, consider the following characteristics:

  * **Location and machine type** : You deploy nodes in a specific Google Cloud region and zone. Select a homogenous machine type across all hosts in a cluster to ensure consistent compute, memory, and vSAN storage capacity.
  * **Minimum node requirements** : A high availability (HA) VCF deployment requires a minimum of four bare-metal nodes per cluster.
  * **Fault domain isolation** : You assign each node to an availability domain within a spread placement policy at creation time. This configuration ensures that Google Cloud distributes bare-metal instances across separate physical server racks, top-of-rack switches, and power domains.



## Internal IP address allocation

Each node requires an internal IPv4 address on its primary network interface (`nic0`) for ESXi host management (`vmk0`), as well as IP addresses on its dynamic NICs for `vSAN`, `vMotion`, and `NSX-TEP` traffic. You can configure IP address allocation by using one of the following methods:

  * **Ephemeral (Automatic)** : Google Cloud automatically assigns an available IP address from the selected VPC subnet.
  * **Ephemeral (Custom)** : You specify a valid, unallocated IP address within the subnet range.
  * **Reserved** : You allocate and bind a static internal IP address in your VPC subnet so that the IP address persists across instance lifecycle operations.



## Deletion protection

To prevent accidental deletion of active ESXi hosts, Compute Engine deletion protection is enabled on each bare-metal node by default.

When deletion protection is enabled, any attempt to delete the node in the Google Cloud console or through the API fails. To decommission and remove a node from your environment, first decommission the host in VCF, disable deletion protection on the Compute Engine instance, and then delete the node.

## Local storage and data persistence

VMware solution bare-metal nodes use directly attached local NVMe SSDs for vSAN Express Storage Architecture (ESA) datastores.

**Warning:** Data stored on the local SSDs of a bare-metal instance is transient and tied to the instance lifecycle. If you stop and restart a node, or if you delete a node, Google Cloud erases all data on its local SSDs. Maintain vSAN redundancy policies across multiple availability domains and evacuate data in vCenter Server before stopping or deleting a node.

## Labels and network tags

VMware solution bare-metal nodes have a default label `gcve-node:true` and a `mm-gcve-node` when the nodes are provisioned. These are used to identify nodes in the Compute Engine inventory. These labels and network tags must not be modified or deleted. You can add additional labels and network tags to a bare-metal node.

## What's next

  * Learn how to distribute nodes across availability domains in [Placement policies and availability domains](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/concepts-placement-policies).
  * Review cluster sizing guidelines in [About vSphere clusters](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/concepts-clusters).
  * Follow the step-by-step guide to [Deploy nodes and configure appliance networking by using the console](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deploy).
  * Learn how to add and remove nodes in [Manage node capacity](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/capacity-management).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

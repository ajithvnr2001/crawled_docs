---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/concepts-placement-policies/
title: Placement policies and availability domains \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T20:28:17.654160+00:00
---

# Placement policies and availability domains  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/concepts-placement-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides (VMware solution) ](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Placement policies and availability domains

This page describes spread placement policies and availability domains in VMware solution on Google Cloud and explains how they map to VMware vSAN fault domains.

[Placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview) let you control the physical placement of your bare-metal Compute Engine instances within a Google Cloud zone. When you apply a spread placement policy to your bare-metal ESXi nodes, Google Cloud distributes the instances across separate physical server racks, top-of-rack switches, and power distribution units to improve resiliency against location-specific hardware or power disruptions.

## Availability domains

In Compute Engine, an availability domain is a logical grouping of compute and storage resources within a zone that provides physical failure isolation:

  * **Physical isolation** : Each availability domain maps to isolated, distinct hardware within a Google Cloud data center. Hardware maintenance or a rack-level failure in one availability domain doesn't affect instances in other availability domains.
  * **Domain count** : You can configure between 1 and 8 availability domains within a single spread placement policy.
  * **Node distribution** : When you create bare-metal nodes, you assign an availability domain to each node so that compute and vSAN storage capacity is distributed evenly across independent fault domains.

**Warning:** Changing the availability domain of a bare-metal instance after creation requires stopping and restarting the instance. Stopping a bare-metal instance erases all data stored on its local NVMe SSDs.

## Map availability domains to vSAN fault domains

Spread placement policies provide the physical foundation for VMware vSAN fault domains in your VCF clusters.

**Caution:** Nodes in a placement policy must belong to only one vSphere or VCF cluster to maintain a 1:1 mapping between Google Cloud availability domains and VMware vSAN fault domains. If you share nodes from a single placement policy across multiple clusters, you risk misaligned fault domain mappings, which can compromise vSAN data redundancy and failover behavior.

## Placement policy and availability domain best practices

When you configure placement policies and availability domains for your VCF clusters, follow these best practices:

  * **Use one placement policy per cluster** : Create a dedicated spread placement policy for each vSphere cluster in a zone. When you add new nodes to expand an existing cluster, assign them to that cluster's existing placement policy.
  * **Configure 5 to 8 availability domains** : Specify 5 to 8 availability domains in your spread placement policy to accommodate cluster growth and RAID-5 or RAID-6 erasure coding policies.
  * **Assign availability domains at creation time** : Select the specific availability domain for each node when you provision the instance, and spread nodes evenly across availability domains to prevent single-domain capacity bottlenecks during failover.
  * **Align vSAN fault domains with availability domain numbers** : Use each node's assigned availability domain number (`1` through `8`) as its Fault Domain name when you configure vSAN fault domains in vCenter Server.



## What's next

  * Explore the [Architecture overview](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/architecture).
  * Review cluster sizing guidelines in [About vSphere clusters](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/concepts-clusters).
  * Follow the step-by-step guide to [Deploy nodes and configure appliance networking by using the console](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deploy).
  * Learn how to add and remove nodes in [Manage node capacity](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/capacity-management).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

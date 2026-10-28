---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/concepts-clusters/
title: About vSphere clusters \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T20:27:55.075286+00:00
---

# About vSphere clusters  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/concepts-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides (VMware solution) ](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# About vSphere clusters

This page describes vSphere and VMware Cloud Foundation (VCF) clusters in VMware solution on Google Cloud.

In VMware solution, a cluster is a logical grouping of bare-metal ESXi nodes managed by VMware vCenter Server and orchestrated through VCF. Clusters aggregate compute, memory, and vSAN storage resources to host your management appliances and workload virtual machines (VMs).

## Cluster characteristics and differences

VMware solution clusters differ from Google Cloud-managed clusters in the following ways:

  * **Management model** : In the Google Cloud-managed service, Google Cloud deploys and maintains the vSphere cluster, handles software upgrades, and manages automated patching. In VMware solution, you deploy the cluster by using VCF, apply software updates, and manage cluster configuration by using VMware SDDC Manager and vCenter Server.
  * **VPC integration** : VMware solution cluster nodes connect directly to your Virtual Private Cloud (VPC) network for Layer 2 and Layer 3 communication without requiring private services access (PSA) peering.
  * **Licensing** : You use your own VCF licenses to activate cluster features and services under a Bring Your Own License (BYOL) model.



## Sizing and high availability requirements

When you plan and size your VMware solution clusters, apply the following requirements:

  * **Minimum node count** : A high availability (HA) VCF cluster requires a minimum of four bare-metal nodes.
  * **Network endpoint group (NEG) membership** : All nodes within a vSphere cluster located in the same zone must belong to the same network endpoint group (NEG). This membership ensures that VCF network appliances route traffic reliably across cluster nodes.
  * **Homogeneous node types** : Deploy nodes of the same machine type (`z3-highmem-192-highlssd-metal`) within a single cluster to ensure consistent compute and vSAN storage capacity across hosts.



## Cluster lifecycle and capacity

You scale and manage cluster resources by using a two-step workflow:

  1. **Cloud resource provisioning** : Use the Google Cloud console, Terraform, or the Compute Engine API to deploy bare-metal nodes, allocate dynamic NICs, and assign placement policies.
  2. **VMware orchestration** : Prepare nodes by using the VMware solution toolkit and add them to your VCF workload domain or cluster by using SDDC Manager.



To scale in a cluster, first decommission the hosts in VMware SDDC Manager and vCenter Server before you delete the underlying Compute Engine bare-metal nodes.

## What's next

  * Learn about VCF management appliances, dynamic NICs, and the toolkit in [VMware Cloud Foundation components and networking](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/concepts-vcf).
  * Follow the step-by-step guide to [Deploy nodes and configure appliance networking by using the console](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deploy).
  * Add a vSphere cluster to an existing domain in [Add a vSphere cluster to a domain](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/add-cluster).
  * Expand or compact an existing vSphere cluster in [Add or remove nodes in a vSphere cluster](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/expand-cluster).
  * Learn how to add and remove nodes in [Manage node capacity](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/capacity-management).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

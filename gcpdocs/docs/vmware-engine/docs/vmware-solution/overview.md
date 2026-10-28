---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/overview/
title: VMware solution on Google Cloud overview \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T20:28:11.218561+00:00
---

# VMware solution on Google Cloud overview  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides (VMware solution) ](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# VMware solution on Google Cloud overview

VMware solution on Google Cloud provides dedicated bare-metal ESXi nodes in your Google Cloud project. You deploy, configure, and manage VMware Cloud Foundation (VCF) on bare-metal instances that connect directly to your Virtual Private Cloud (VPC) network.

VMware solution uses a Bring Your Own License (BYOL) model. You provide VCF licenses and maintain control over software versions, configurations, and lifecycle updates.

## Shared management responsibilities

In VMware solution, responsibilities are shared between you and Google Cloud:

  * **Customer responsibilities** : Procuring VCF licenses, deploying the VMware SDDC stack (vSphere, vSAN, and NSX), applying software updates and patches, and managing workloads.
  * **Google Cloud responsibilities** : Managing physical facilities, bare-metal server hardware, and cloud networking infrastructure up to the hypervisor.



For a detailed breakdown of operational boundaries across compute, storage, networking, and support, see the [Shared responsibility model](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/shared-responsibility).

## Core components and architecture

To plan and manage your VMware solution environment, review the following foundational guides:

  * [Architecture overview](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/architecture): Explore the compute, storage, and network architecture for VCF on Google Cloud bare-metal infrastructure.
  * [Bare-metal nodes and machine types](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/concepts-nodes): Understand the dedicated bare-metal Compute Engine instances and hardware specifications that host your ESXi hypervisors.
  * [Placement policies and availability domains](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/concepts-placement-policies): Learn how to distribute nodes across availability domains to ensure high availability and map them to vSAN fault domains.
  * [About vSphere clusters](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/concepts-clusters): Plan vSphere and VCF cluster architectures, sizing, and node minimums.
  * [VMware Cloud Foundation components and networking](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/concepts-vcf): Understand VCF domains, management appliances, dynamic network interfaces (NICs), network endpoint groups (NEGs), and the automation toolkit.



## What's next

  * Set up your software repository in [Configure a VCF software depot](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/configure-offline-depot).
  * Compare provisioning workflows in the [Deployment options overview](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deployment-options).
  * Deploy your nodes and configure appliance networking by using [Deploy nodes and configure appliance networking by using the console](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deploy).
  * Deploy your nodes and infrastructure by using [Deploy nodes and VCF by using Terraform and toolkit](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deploy-terraform).
  * Prepare nodes and deploy VCF by using [Prepare nodes and deploy VCF by using the toolkit](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/toolkit).
  * Learn how to add or remove nodes in [Manage node capacity](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/capacity-management).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

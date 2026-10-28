---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/shared-responsibility/
title: Shared responsibility model \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T20:28:01.484531+00:00
---

# Shared responsibility model  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/shared-responsibility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides (VMware solution) ](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Shared responsibility model

This document describes customer responsibilities and Google Cloud responsibilities when you run workloads in VMware solution on Google Cloud.

## Shared responsibility overview

In VMware solution, operational responsibilities are divided between you and Google Cloud. You administer the VMware Cloud Foundation (VCF) software stack, and Google Cloud manages the physical infrastructure and bare-metal hardware.

In VMware solution, bare-metal nodes are dedicated Compute Engine instances provisioned in your Google Cloud project. You manage access control, network security, and infrastructure monitoring for these instances by using Compute Engine and Google Cloud controls.

The following table summarizes the division of responsibilities between you and Google Cloud:

Area  | Google Cloud responsibilities | Customer responsibilities  
---|---|---  
**Physical infrastructure and hardware** | Manages physical data centers, server racks, power, cooling, local NVMe SSD hardware, and physical network fabric. | Selects zones, configures placement policies, and distributes nodes across availability domains.  
**Bare-metal instances and host lifecycle** | Provides qualified ESXi node images, monitors physical host health, sends maintenance notifications, and performs physical host maintenance and hardware remediation. | Places ESXi hosts into maintenance mode in VCF before initiating Google Cloud host maintenance, and replaces nodes when required.   
**VMware Cloud Foundation (VCF) software** | Qualifies new Broadcom ESXi software versions on bare-metal hardware and publishes release notes upon completion.  | Procures portable VCF licenses (Bring Your Own License), deploys the VCF stack (vCenter Server, SDDC Manager, vSAN, and NSX), and plans and applies VCF patches, updates, and upgrades.  
**Access control and credentials** | Provides Identity and Access Management (IAM) to control access to Google Cloud project resources. Does not access or store your VCF credentials or guest environment configurations.  | Manages IAM roles for Google Cloud resources and configures authentication, role-based access control (RBAC), passwords, and certificates within VCF.  
**Networking and security** | Operates the underlying Virtual Private Cloud (VPC) software-defined network, Layer 2 ARP broadcast and MAC learning data plane, and regional internal passthrough Network Load Balancers. | Configures VPC subnets, firewall rules, DNS zones, NSX overlay networks, distributed firewall policies, and encryption.   
  
## Access control

Google Cloud doesn't have access to your VMware passwords or visibility into how you configure your VCF software stack. You are responsible for configuring authentication, identity sources, and access controls within vCenter Server, SDDC Manager, and NSX Manager.

VMware solution provisions all cloud infrastructure resources directly in your Google Cloud project. You control access to these Google Cloud resources by using [IAM](https://docs.cloud.google.com/iam/docs/overview).

## Maintenance responsibilities

Maintenance in VMware solution is divided between underlying bare-metal node infrastructure and the VCF software stack.

### Bare-metal node maintenance

Google Cloud provides infrastructure updates, hardware bug fixes, and security patches for the bare-metal nodes in your Google Cloud project. When a bare-metal node requires host maintenance, Google Cloud sends a maintenance notification that specifies a deadline before automated maintenance starts.

Before you start host maintenance in Google Cloud, you must place the corresponding ESXi host into maintenance mode in your VCF control plane to evacuate running virtual machines and protect vSAN storage availability. For detailed procedures, see [Manage bare-metal node maintenance](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/maintenance).

### VCF software maintenance

You are responsible for maintaining the VCF software stack, including applying patches, updates, and upgrades released by Broadcom.

Google Cloud qualifies new versions of ESXi software released by Broadcom on supported bare-metal machine types and publishes an announcement in the [release notes](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/release-notes) when qualification is complete. Upgrade your VCF environment only to ESXi versions that Google Cloud has qualified.

## What's next

  * Compare management models in [Compare VMware Engine models](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/compare-models).
  * Review the technical design in [Architecture overview](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/architecture).
  * Learn how to handle host events and updates in [Manage bare-metal node maintenance](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/maintenance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

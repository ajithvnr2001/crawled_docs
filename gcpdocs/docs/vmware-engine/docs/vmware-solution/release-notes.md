---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/release-notes/
title: VMware solution on Google Cloud release notes \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T18:53:22.244824+00:00
---

# VMware solution on Google Cloud release notes  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides (VMware solution) ](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/overview)



Send feedback 

#  VMware solution on Google Cloud release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents updates to VMware solution on Google Cloud. Check this page for announcements about new features, updates, bug fixes, and known issues. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/vmware-engine-vmware-solution-release-notes.xml) directly. 

## October 27, 2026

Feature

VMware solution on Google Cloud is [generally available](https://cloud.google.com/products#section-22) (GA). VMware solution lets you deploy, configure, and manage VMware Cloud Foundation (VCF) on dedicated bare-metal Compute Engine instances within your Virtual Private Cloud (VPC) network under a Bring Your Own License (BYOL) model.

Key features include the following:

  * Provision dedicated bare-metal ESXi nodes (`z3-highmem-192-highlssd-metal`) directly in your project with deletion protection and Local SSD storage for vSAN.
  * Automate node preparation, Secret Manager credential storage, vSwitch and Dynamic NIC networking, Cloud DNS zone and record synchronization, vSAN storage initialization, and VCF installer appliance deployment by using Terraform and the VMware solution toolkit.
  * Distribute nodes across isolated availability domains by using spread placement policies to align with vSAN fault domains for high availability.
  * Connect ESXi nodes and VLAN-tagged Dynamic NICs directly to your VPC subnets without requiring private services access peering.



For more information, see [VMware solution on Google Cloud overview](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/overview) and [Compare VMware Engine models](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/compare-models).

## September 01, 2026

Feature

**Preview** : VMware solution on Google Cloud is available in preview for allow-listed customers. VMware solution lets you deploy, configure, and manage VMware Cloud Foundation (VCF) on dedicated bare-metal Compute Engine instances within your Virtual Private Cloud (VPC) network under a Bring Your Own License (BYOL) model.

Key features include the following:

  * **Dedicated bare-metal nodes** : Provision bare-metal ESXi nodes directly in your project with deletion protection and Local SSD storage for vSAN.
  * **Initialization toolkit** : Automate ESXi password configuration with Secret Manager, vSwitch networking, vSAN storage initialization, and VCF installer appliance deployment.
  * **Placement policies** : Distribute nodes across isolated availability domains to align with vSAN fault domains for high availability.
  * **VPC integration** : Connect ESXi nodes and dynamic network interfaces directly to your VPC subnets without requiring private services access peering.



For more information, see [VMware solution on Google Cloud overview](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/overview) and [Compare VMware Engine models](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/compare-models).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

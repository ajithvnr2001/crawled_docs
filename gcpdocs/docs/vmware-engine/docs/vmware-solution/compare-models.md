---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/compare-models/
title: Compare VMware Engine models \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T20:28:08.672800+00:00
---

# Compare VMware Engine models  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/compare-models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides (VMware solution) ](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Compare VMware Engine models

You can run VMware workloads on Google Cloud by using the Google Cloud-managed service (Google Cloud VMware Engine) or VMware solution on Google Cloud. In the Google Cloud-managed service, Google Cloud manages the VMware stack and underlying infrastructure. In VMware solution, you deploy and manage VMware Cloud Foundation (VCF) on dedicated Google Cloud bare-metal infrastructure.

## Management models

To review task assignments between Google Cloud and customers for each option, see the [Shared responsibility model](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/shared-responsibility).

### Google Cloud-managed service

In the Google Cloud-managed service, Google Cloud manages the VMware SDDC stack (vSphere, vSAN, NSX, and HCX), networking, and physical infrastructure. VMware software licenses are included with the service.

[View Google Cloud-managed service guides](https://docs.cloud.google.com/vmware-engine/docs/overview)

### VMware solution on Google Cloud

In VMware solution, you provide your own VMware Cloud Foundation licenses and deploy the VMware SDDC stack on dedicated Google Cloud bare-metal instances. You deploy, configure, patch, and manage vSphere, vSAN, NSX, and related VMware components. Google Cloud manages the physical facilities, server hardware, and networking infrastructure up to the hypervisor.

[View VMware solution guides](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/overview)

## Feature comparison

The following table compares key features across both management models:

Feature | Google Cloud-managed service | VMware solution on Google Cloud  
---|---|---  
**VMware stack management** | Google Cloud | Customer  
**VMware software updates** | Google Cloud | Customer  
**VMware licensing** | Included | Bring Your Own License (BYOL)  
**Infrastructure** | Google Cloud | Google Cloud  
**Administrative control** | Managed by Google Cloud (elevated access available) | Root and administrator access  
**Primary management tool** | Google Cloud console and VMware Engine API | VMware SDDC Manager and vCenter Server  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

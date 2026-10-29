---
url: https://docs.cloud.google.com/docs/migration/scenarios/virtual-machine-migration/
title: Virtual machine migration \u00a0|\u00a0 Migration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T05:38:47.351525+00:00
---

# Virtual machine migration  |  Migration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/migration/scenarios/virtual-machine-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Guides ](https://docs.cloud.google.com/docs/migration/overview/migrate-modernize-overview)



Send feedback 

#  Virtual machine migration Stay organized with collections  Save and categorize content based on your preferences. 

This page provides architectural guidance and migration workflows for migrating virtual machines (VMs) from on-premises data centers or other public clouds to Google Cloud.

If you are a cloud architect, migration engineer, or infrastructure lead, use the information on this page to evaluate target compute platforms, plan migration waves, and execute cutovers with minimal workload downtime.

Before you read this page, you should have an inventory of your source virtual machines and an understanding of your application network dependencies.

## Target platform options

When planning VM migrations, use the following table to choose a target compute platform based on your operational requirements:

Scenario | Target platform | Recommended tool | Advantages  
---|---|---|---  
**Rehost to native cloud infrastructure** | Compute Engine |  [Migrate to Virtual Machines](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0) |  Avoids on-premises hypervisor licensing costs, supports dynamic autoscaling, and uses [Active Assist](https://docs.cloud.google.com/recommender/docs/recommenders) recommendations to automatically right-size VM resources and optimize costs.   
**Retain existing VMware operational tooling** | Google Cloud VMware Engine |  [VMware HCX](https://docs.cloud.google.com/vmware-engine/docs/workloads/howto-migrate-vms-using-hcx) |  Preserves existing vSphere and vCenter operational workflows with zero guest OS modifications, minimizing operational disruption and team retraining.   
  
## Migrate to Compute Engine

[Migrate to VMs](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0) provides an automated migration path to Compute Engine.

### Key capabilities of Migrate to VMs

Migrate to VMs provides the following capabilities:

  * **Continuous background replication** : workloads start running on Compute Engine in minutes while data volumes stream in the background.
  * **Non-disruptive test cloning** : clone and test running workloads in isolated VPC networks without affecting production source environments.
  * **Automated OS adaptation** : automatically inject drivers and license configurations required for Compute Engine.



For information about the end-to-end migration workflow, see [VM migration process](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle).

## Migrate to VMware Engine

[VMware Engine](https://docs.cloud.google.com/vmware-engine/docs) provides a dedicated VMware Software-Defined Data Center (SDDC) that runs on Google Cloud.

### Key capabilities of VMware HCX

VMware HCX provides the following capabilities:

  * **Layer 2 network extension** : extend on-premises subnets to VMware Engine to keep your existing VM IP addresses during migration.
  * **Bulk and live vMotion migration** : move hundreds of VMs simultaneously with scheduled cutovers or migrate your VMs without application downtime.
  * **Unified management** : manage cloud-hosted VMware clusters by using familiar vCenter, NSX-T, and vSAN interfaces.



For information about the end-to-end migration workflow, see [Use VMware HCX to migrate VMware VMs](https://docs.cloud.google.com/vmware-engine/docs/workloads/howto-migrate-vms-using-hcx).

## What's next

  * [Database migration](https://docs.cloud.google.com/docs/migration/scenarios/database-migration)
  * [Unstructured data and storage migration](https://docs.cloud.google.com/docs/migration/scenarios/data-storage-migration)
  * [Containerized application migration](https://docs.cloud.google.com/docs/migration/scenarios/container-migration)
  * [Multi-cloud workload migration](https://docs.cloud.google.com/docs/migration/scenarios/multi-cloud-migration)
  * [VMware Engine documentation](https://docs.cloud.google.com/vmware-engine/docs)
  * [Migrate to VMs documentation](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

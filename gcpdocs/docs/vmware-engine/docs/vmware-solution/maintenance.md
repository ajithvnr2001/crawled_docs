---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/maintenance/
title: Manage bare-metal node maintenance \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T20:28:07.199072+00:00
---

# Manage bare-metal node maintenance  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides (VMware solution) ](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage bare-metal node maintenance

In VMware solution on Google Cloud, you are responsible for patching, updating, and upgrading your VMware Cloud Foundation (VCF) software stack. Google Cloud manages the underlying physical servers, power, cooling, and data center fabric for your `z3-highmem-192-highlssd-metal` bare-metal ESXi nodes. Periodically, Google Cloud performs [host maintenance events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview) to apply hardware repairs, firmware updates, and security patches to the physical hosts.

This document describes the types of host maintenance events that affect bare-metal ESXi nodes and explains how to evacuate workloads and run maintenance without disrupting your VCF clusters.

## Types of host events

Compute Engine bare-metal instances experience the following categories of host events:

  * **Planned maintenance events** : Scheduled maintenance windows that Google Cloud announces in advance. Most background updates are non-disruptive, whereas hardware or firmware maintenance requires rebooting the bare-metal node.
  * **Emergent maintenance** : Urgent hardware or fleet-wide software maintenance that requires a node reboot to prevent failures or apply critical security mitigations. Google Cloud provides 7 to 90 days of advance notice depending on the severity of the event and populates the `maintenanceReasons` field in the instance metadata.
  * **Host errors** : Rare, unexpected hardware or physical host failures (`compute.instances.hostError`) that cause an unplanned reboot or require replacing the bare-metal node. When a host error occurs, vSphere high availability (HA) automatically restarts affected virtual machines (VMs) on healthy ESXi hosts in the cluster.



## Maintenance considerations for VCF clusters

Before you trigger a disruptive maintenance event on a bare-metal ESXi node, review the following operational requirements:

  * **Complete maintenance before the scheduled deadline** : Always start maintenance manually during an approved change window before the scheduled window expires. If the maintenance window expires before you initiate maintenance, Compute Engine automatically starts the maintenance event, which reboots the host without placing it into vSphere maintenance mode first.
  * **Verify cluster capacity** : Ensure that your vSphere and vSAN cluster has sufficient spare compute and storage capacity to evacuate all VMs and satisfy your vSAN storage policy failure tolerance requirements. If your cluster lacks sufficient headroom, add a bare-metal node to the cluster before you start maintenance.
  * **Place the ESXi host in vSphere maintenance mode first** : Always evacuate VMs by placing the host into maintenance mode in vCenter Server or VCF Operations before you trigger maintenance in the Google Cloud console.
  * **Maintain one node per cluster at a time** : Each bare-metal maintenance event takes approximately 120 to 150 minutes to complete. Run maintenance on only one node per vSphere cluster at a time to preserve vSAN data availability. You can run maintenance on nodes in separate vSphere clusters or separate VCF workload domains in parallel.
  * **Replace unresponsive nodes** : If a bare-metal node remains in the `In progress` maintenance state for more than 240 minutes, decommission the node from vCenter Server and SDDC Manager, and provision a replacement node.



## View maintenance notifications

You can monitor upcoming host maintenance events in the Google Cloud console by using either of the following views (or configure automated alerts as described in [Monitor and plan for a host maintenance event](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event)):

  * **VMware Engine** :

    1. In the Google Cloud console, go to **VMware Engine** > **Self-managed** > **Baremetal nodes**.

[Go to Baremetal nodes](https://console.cloud.google.com/vmwareengine/self-managed/baremetal-nodes)

    2. Check the **Maintenance status** column for each node:

       * **Update available - will run on ( DATE_AND_TIME)**: A planned or emergent maintenance event is scheduled and ready for you to initiate.
       * **In progress** : Host maintenance is running on the node.
       * **Up-to-date** : No maintenance events are pending for the node.
  * **Compute Engine VM instances** :

    1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

    2. Filter the instance list by machine type (`z3-highmem-192-highlssd-metal`) and inspect the **Upcoming maintenance** column.




## Perform node maintenance

To safely perform host maintenance on a bare-metal ESXi node, evacuate the host in vCenter Server, run the maintenance event in the Google Cloud console, and return the host to service.

### Prepare the node in vCenter Server

  1. Identify the bare-metal instance that has an upcoming maintenance window in the Google Cloud console and note its hostname or primary management IP address.
  2. Sign in to the vSphere Client (or VCF Operations) and locate the corresponding ESXi host in your cluster.
  3. Right-click the ESXi host and select **Maintenance Mode** > **Enter Maintenance Mode**.
  4. Select the **Ensure accessibility** (default) or **Full data migration** vSAN data migration mode based on your cluster redundancy policy, and confirm that you want to move powered-off and suspended VMs to other hosts in the cluster. For guidance on choosing a vSAN evacuation mode, see the [Broadcom documentation on placing a member of a vSAN cluster in maintenance mode](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsan/8-0/vsan-administration/cluster-maintenance/place-a-member-of-vsan-cluster-in-maintenance-mode.html).
  5. Wait until all VMs migrate off the host and the host status changes to **Maintenance Mode** in vCenter Server.



### Run host maintenance in Google Cloud

  1. In the Google Cloud console, go to **VMware Engine** > **Self-managed** > **Baremetal nodes**.
  2. Locate the node that you placed in vSphere maintenance mode.
  3. Click the more actions menu (more_vert) next to the node and select **Run maintenance**.
  4. Confirm the operation when prompted. The **Maintenance status** changes to **In progress**.
  5. Wait for the maintenance operation to complete and for the ESXi host to boot back up. The **Maintenance status** changes to **Up-to-date** after approximately 150 to 180 minutes.



### Complete post-maintenance tasks

  1. Verify in the vSphere Client that the ESXi host has reconnected to vCenter Server and that all physical network adapters (`vmnic0` through `vmnic4`) and vSAN local disks report a healthy status.
  2. Right-click the ESXi host and select **Maintenance Mode** > **Exit Maintenance Mode**.
  3. Verify that vSphere Distributed Resource Scheduler (DRS) and vSAN health checks pass before you begin maintenance on another node in the same cluster.



## What's next

  * Learn how to [Manage node capacity by using Terraform](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/capacity-management-terraform) when adding or removing hosts.
  * Review the [Shared responsibility model](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/shared-responsibility).
  * Contact support by reviewing [Get support](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

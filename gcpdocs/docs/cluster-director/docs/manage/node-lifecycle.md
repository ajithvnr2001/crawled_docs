---
url: https://docs.cloud.google.com/cluster-director/docs/manage/node-lifecycle/
title: Node lifecycle \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-08T09:17:46.862424+00:00
---

# Node lifecycle  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/manage/node-lifecycle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Node lifecycle Stay organized with collections  Save and categorize content based on your preferences. 

This document explains the lifecycle of a cluster node in Cluster Director. A node in a cluster transitions through various states from its creation to its deletion. Understanding these states lets you do the following:

  * **Manage resources and costs** : understand when Cluster Director provisions and stops dynamic nodes to run queued jobs and reduce unnecessary charges.

  * **Minimize disruptions** : anticipate planned host maintenance events.

  * **Troubleshoot errors** : identify why a node fails to boot, restart, or resume.




TPU nodes in a slice share the same lifecycle. If a TPU node undergoes maintenance, encounters a host error, or is deleted, then all other TPU nodes in that slice undergo the same lifecycle event. This behavior doesn't apply to GPU or CPU nodes. To check the current state of a node, [view the details of your cluster](https://docs.cloud.google.com/cluster-director/docs/manage/view-clusters#describe).

## Node states

The following diagram shows the different states that Cluster Director can set a node to:

[ ![State diagram for Cluster Director nodes across the
            UNPROVISIONED, CREATING, ACTIVE, SUSPENDING, SUSPENDED, REPAIRING,
            FAILED, and DELETING states.](https://docs.cloud.google.com/static/cluster-director/images/node-states-lifecycle.png)](https://docs.cloud.google.com/static/cluster-director/images/node-states-lifecycle.png)

The states shown in the preceding diagram are as follows:

  * Unprovisioned state

  * Creating state

  * Active state

  * Suspending state

  * Suspended state

  * Repairing state

  * Failed state

  * Deleting state




### Unprovisioned state

When Cluster Director creates a dynamic node, the node starts in the `UNPROVISIONED` state. From this state, a dynamic node can transition to one of the following states:

  * **`CREATING`** : when you submit a job that requires more compute resources than the ones in your static nodes, Cluster Director attempts to allocate resources to create the dynamic node.

  * **`DELETING`** : when you reduce the dynamic node count by modifying or deleting the cluster, the delete operation for the node starts.




### Creating state

When a node is in the `CREATING` state, Cluster Director attempts to allocate resources to create and boot your node.

From this state, the node can transition to one of the following states:

  * **`ACTIVE`** : when Cluster Director allocates resources for your node, the node boots up and starts running.

  * **`FAILED`** : the node encounters a host error.




### Active state

When a node is in the `ACTIVE` state, the node is healthy, running, and ready to run Slurm jobs.

From this state, the node can transition to one of the following states:

  * **`SUSPENDING`** : you stop or suspend the node, or Cluster Director stops the node after it preempts a Spot VM that is configured to be stopped (`TERMINATE`) on preemption.

  * **`REPAIRING`** : planned or unplanned host maintenance for the node starts.

  * **`UNPROVISIONED`** : for a dynamic GPU or CPU node, Slurm deletes the compute instance after the node remains in the `idle` state for five minutes. For a dynamic TPU node, Slurm deletes the compute instance when the job finishes.

  * **`DELETING`** : a delete operation starts after one of the following events occurs:

    * A Flex-start VM reaches the end of its run duration, or the reservation that you used to create the node reaches its end time.

    * Cluster Director preempts a Spot VM that is configured to be deleted (`DELETE`) on preemption.

    * You manually delete the node.

    * You reduce the static node count (`staticNodeCount`) or maximum dynamic node count (`maxDynamicNodeCount`) in a Slurm nodeset, or you reduce the target size (`targetSize`) of a MIG in a managed compute cluster.

    * You delete the cluster.

  * **`FAILED`** : the node encounters a host error.




### Suspending state

When a node is in the `SUSPENDING` state, Cluster Director stops or suspends the node. You can only stop GPU or CPU nodes, and you can only suspend CPU nodes. For more information, see [Suspend, stop, or reset Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances/suspend-stop-reset-instances-overview).

**Caution:** If you stop or suspend a node, then you can only restart or resume it if you have a reservation, or if the zone has available resources when you submit your request. Stop or suspend a node only if you have reserved capacity or your workload can resume at a flexible time.

From this state, when the stop or suspend operation completes, the node transitions to the `SUSPENDED` state.

### Suspended state

When a node is in the `SUSPENDED` state, the stop or suspend operation completes.

From this state, the node transitions to one of the following states:

  * **`ACTIVE`** : you resume or restart the node. You can only resume or restart a node if the zone has available resources or you have a reservation. Otherwise, the operation fails and the node remains stopped or suspended.

  * **`DELETING`** : you delete the node or the cluster.




### Repairing state

When a node is in the `REPAIRING` state, Cluster Director stops the node to perform host maintenance on the node's underlying Compute Engine infrastructure. Only GPU or TPU nodes enter this state. Nodes that use N2 machine types keep running during maintenance because Cluster Director [_live migrates_ them](https://docs.cloud.google.com/compute/docs/instances/live-migration-process).

From this state, the node transitions to one of the following states:

  * **`ACTIVE`** : when host maintenance completes, the node restarts. Cluster Director helps ensure that the resources needed to restart the node are available.

  * **`FAILED`** : the node encounters a host error.




### Failed state

When a node is in the `FAILED` state, the node is unhealthy or encountered a host error. To help you troubleshoot the issue, Cluster Director provides details about the error in [Logs Explorer](https://docs.cloud.google.com/cluster-director/docs/monitor/view-audit-logs#custom-logs), or in the `stateMessage` field when you use the Google Cloud CLI or REST API.

**Note:** If your node encounters an unexpected error, then contact your account team or support for help.

From this state, when you delete the node or cluster, the node transitions to the `DELETING` state.

### Deleting state

When a node is in the `DELETING` state, Cluster Director deletes the node and releases its resources. A node enters the `DELETING` state after one of the following events occurs:

  * The reservation that you used to create the node reaches its end time.

  * You delete the node.

  * You reduce the static node count (`staticNodeCount`) or maximum dynamic node count (`maxDynamicNodeCount`) in a nodeset.

  * You delete the cluster.




When the delete operation finishes, Cluster Director deletes the node and all of its attached resources.

## Pricing for clusters and nodes

When you create a cluster, you incur charges for the underlying Google Cloud resources that your cluster uses:

  * **Nodes** : when a node is in the `ACTIVE` state, you incur charges for vCPUs, memory, and any attached GPUs or TPUs. For any disks and external IP addresses that are attached to a node's compute instance, you incur charges as long as the compute instance exists, including in the `SUSPENDED` state. Dynamic nodes in the `UNPROVISIONED` state have no compute instance and don't incur charges. For more information, see the following:

    * [Virtual machines pricing](https://cloud.google.com/compute/pricing)

    * [Cloud TPU pricing](https://cloud.google.com/tpu/pricing)

  * **Networking resources** : you incur charges for data transfer (_egress_) and any additional networking features that your cluster uses. For more information, see [All networking pricing](https://cloud.google.com/vpc/network-pricing).

  * **Storage resources** : you incur charges for the storage resources that your cluster uses, as long as those resources exist. For more information, see the following:

    * [Cloud Storage pricing](https://cloud.google.com/storage/pricing)

    * [Filestore pricing](https://cloud.google.com/filestore/pricing)

    * [Google Cloud Managed Lustre pricing](https://cloud.google.com/products/managed-lustre/pricing)




For more information, review the [pricing for Cluster Director](https://cloud.google.com/products/cluster-director#pricing).

## What's next

  * [Modify a cluster](https://docs.cloud.google.com/cluster-director/docs/manage/modify-cluster)

  * [Delete a cluster](https://docs.cloud.google.com/cluster-director/docs/manage/delete-cluster)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-06 UTC."],[],[]] 

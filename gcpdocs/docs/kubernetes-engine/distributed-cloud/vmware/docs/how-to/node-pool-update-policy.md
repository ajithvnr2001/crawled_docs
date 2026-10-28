---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-pool-update-policy/
title: Configure node pool update policy \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T02:29:58.999477+00:00
---

# Configure node pool update policy  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-pool-update-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Configure node pool update policy Stay organized with collections  Save and categorize content based on your preferences. 

A node pool update policy lets you limit how many node pools update or upgrade at the same time. Because node pools update in parallel by default, lower concurrency helps prevent PodDisruptionBudget (PDB) deadlocks and resource or IP address exhaustion. However, updates and upgrades take longer.

## Resource and IP address requirements

By default, node pools update in parallel. For each updating node pool, the cluster creates one surge node. Updating multiple node pools simultaneously can lead to the following constraints:

  * **Resource exhaustion** : Creating surge nodes for multiple node pools in parallel might exceed available compute quota or host capacity if extra capacity is limited.
  * **PDB deadlocks** : Draining more than one node at a time can potentially cause PodDisruptionBudget (PDB) deadlocks.
  * **IP address availability** : Each node pool that updates in parallel needs one extra IP address for its surge node. For example, to update three node pools in parallel, three extra IP addresses must be available: 
    * If your worker nodes obtain IP addresses from a [DHCP server](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-ipmode-type-field), your DHCP server must be able to provide one additional IP address for each node pool that updates in parallel.
    * If your worker nodes use static IP addresses, your [IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-ipmode.ipblockfilepath-field) must contain one extra IP address for each node pool that updates in parallel, beyond the IP addresses needed for worker nodes.



If there are not enough extra IP addresses available to update all of the node pools in parallel, the cluster updates as many pools as possible in parallel. As IP addresses become available, the remaining node pools are updated.

## Configure node pool update policy

Note the following about advanced clusters:

  * Version 1.31: node pool update policies aren't supported on [advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field).

  * Version 1.32: node pool update policies are supported on advanced clusters.

  * Versions 1.32.0 to 1.32.1000, 1.33.0 to 1.33.600, and 1.34.0 to 1.34.200: on advanced clusters, `maximumConcurrentNodePoolUpdate` defaults to `1`, so node pools update sequentially. In later patch versions and in 1.35 and higher, the default is `0`, so node pools update in parallel. For details, see [`nodePoolUpdatePolicy.maximumConcurrentNodePoolUpdate`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepoolupdatepolicy-maximumconcurrentnodepoolupdate-field).




In user cluster seed config `user-cluster.yaml`, you can configure the node pool update policy to update node pools sequentially or with a concurrency limit:
    
    
    nodePoolUpdatePolicy:
      maximumConcurrentNodePoolUpdate: 1
    

The `maximumConcurrentNodePoolUpdate` field controls update concurrency:

  * `0`: Preserves the default parallel behavior across all node pools.
  * `1`: Updates node pools sequentially. Although sequential updates avoid resource and IP exhaustion, the update process takes longer than updating in parallel.
  * An integer greater than `1`: Configures the maximum number of node pools to update concurrently.



The node pool update policy applies to both node pool update and upgrade, but not create. If any node pool update or upgrade encounters issues and gets stuck, the process blocks at that pool and does not proceed to the next node pool.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/vm-limits/
title: VM Runtime on GDC limits \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T23:29:46.220530+00:00
---

# VM Runtime on GDC limits  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/vm-limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  VM Runtime on GDC limits Stay organized with collections  Save and categorize content based on your preferences. 

Tested scaling guidelines for VM Runtime on GDC help you plan VM deployments and evaluate cluster capacity on Distributed Cloud software only for bare metal. Because actual capacity depends on your workloads and hardware resources, these figures represent tested benchmarks rather than hard platform limits or guaranteed thresholds.

For information about quotas, limits, and scaling for Google Distributed Cloud, see [Quotas and limits](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/limits).

## Maximum VM scaling

We have determined through extensive testing that you can run reliably as many as 500 VMs concurrently on a cluster with 50 nodes.

## Resource usage

To scale up VM deployments, make sure there are enough CPU, memory, and storage resources in the cluster for both VMs and the control plane components. For standard resource requirements for cluster node machines, see [Cluster node machine prerequisites](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/node-machine-prerequisites).

Note the following VM Runtime on GDC resource usage for our maximum VM scaling configuration:

  * Total CPU share used by all the components in the `vm-system` namespace is approximately **1.3** at the peak usage.
  * Total memory consumed by all the components in the `vm-system` namespace is approximately **10 GiB**.



### Known resource issue

When the [guest agent is enabled](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/connect-vms#enable-agent), each VM registers a separate watcher to the API server. Therefore, the number of registered watchers in `kube-apiserver` increases linearly with the number of the VMs. Depending on the workloads you run, you may encounter issues related to `kube-apiserver` as the number of VMs increases. If you're affected by this issue, you can configure the `kube-apiserver` or [disable the guest agent](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/connect-vms#disable-guest) if you aren't using it.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 

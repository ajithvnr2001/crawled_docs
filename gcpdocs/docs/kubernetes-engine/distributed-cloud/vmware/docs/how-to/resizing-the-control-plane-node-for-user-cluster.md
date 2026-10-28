---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/resizing-the-control-plane-node-for-user-cluster/
title: Resizing the control plane node for a user cluster \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T02:30:00.398679+00:00
---

# Resizing the control plane node for a user cluster  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/resizing-the-control-plane-node-for-user-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Resizing the control plane node for a user cluster Stay organized with collections  Save and categorize content based on your preferences. 

You can resize the control-plane node of a Google Distributed Cloud user cluster to change its number of CPUs and amount of memory, for example, to support more worker nodes as your cluster grows. Because resizing re-creates the node, a user cluster with a single control-plane node might have a small amount of downtime.

You can't resize the control-plane node manually if you enable [automatic node resizing](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-resize).

To add or remove CPUs and memory in the control-plane node:

### Console

  1. In the console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the Google Cloud project that the user cluster is in.

  3. In the list of clusters, click the cluster that you want to modify, and then click **View details** in the **Details** panel.

  4. Scroll down to the **Control Plane** section.

  5. Click edit **Edit** next to **Control-plane node CPUs** or **Control-plane node memory** , change the value, and click **Done**.




### Command line

  1. Edit the [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest). Change the `masterNode.cpus` and `masterNode.memoryMB` to the values you want.
         
         ...
         masterNode:
            cpus: 4
            memoryMB: 8192
            # How many machines of this type to deploy
            replicas: 3
         ...
         

  2. Run this command to update the cluster:
         
         gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CONFIG_FILE
         

     * Replace ADMIN_CLUSTER_KUBECONFIG with the path of your admin cluster kubeconfig file.
     * Replace USER_CONFIG_FILE with the path of your user cluster configuration file.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

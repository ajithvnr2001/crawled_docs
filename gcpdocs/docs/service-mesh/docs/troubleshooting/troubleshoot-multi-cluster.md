---
url: https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-multi-cluster/
title: Resolving multi-cluster issues \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T18:38:40.471180+00:00
---

# Resolving multi-cluster issues  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-multi-cluster/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Resolving multi-cluster issues

This section explains common Cloud Service Mesh problems and how to resolve them. If you need additional assistance, see [Getting support](https://docs.cloud.google.com/service-mesh/docs/getting-support).

## Cross-cluster timeouts, high latency, or unexpected cross-cluster traffic

Workloads in a fleet with multiple clusters can experience timeouts or high tail latency when cross-cluster endpoint discovery is active without Pod-to-Pod connectivity.

### Symptoms

You might observe the following symptoms:

  * Requests fail after a delay with a timeout or an HTTP `503` or `504` error.
  * Tail latency spikes when retries hit unreachable remote Pods before reaching a local Pod or failing.
  * Issues begin after you register another cluster to the fleet or enable automatic management on a cluster.



### Causes

This issue happens when cross-cluster endpoint discovery is enabled on multiple clusters in a fleet, but network connectivity or firewall rules between their Pods are missing:

  * When multiple clusters in the same fleet have `multicluster_mode: connected` in the `asm-options` ConfigMap, traffic is load balanced between them. For more information, see [Configure endpoint discovery](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/multi-cluster#endpoint-discovery-declarative-api).
  * Cloud Service Mesh doesn't create Virtual Private Cloud (VPC) routes or firewall rules between clusters. Requests routed to local Pods succeed, while requests routed to remote cluster Pods wait until the connection timeout expires.



### Diagnose the issue

Check whether two or more clusters in your fleet have `multicluster_mode` set to `connected`. Run `gcloud container fleet memberships list` to list fleet clusters, and then check each cluster:
    
    
    kubectl get configmap asm-options -n istio-system \
        -o jsonpath='{.data.multicluster_mode}{"\n"}'
    

### Resolve the issue

Depending on whether you want traffic to flow between clusters, do one of the following:

  * To stop load balancing traffic between clusters, disable endpoint discovery. See [documentation on disabling endpoint discovery](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/multi-cluster#endpoint-discovery-declarative-api).
  * To keep only specific services in the local cluster, see [Keeping traffic in-cluster](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/multi-cluster#keeping_traffic_in-cluster).
  * To allow cross-cluster traffic, verify the [multi-cluster network prerequisites](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/multi-cluster#prerequisites) and [create firewall rules](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/multi-cluster#create_firewall_rule) between your clusters.



## Missing secrets

**Caution:** In-cluster Cloud Service Mesh using the `ISTIOD` control plane on GKE on Google Cloud is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). Cloud Service Mesh with an in-cluster control plane on Google Distributed Cloud (software only) continues to be supported as described in [Supported platforms](https://docs.cloud.google.com/service-mesh/docs/supported-platforms#off-gcp). **Caution:** Managed Cloud Service Mesh using the `ISTIOD` control plane implementation is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). You must [modernize](https://docs.cloud.google.com/service-mesh/docs/modernization) all managed `ISTIOD` fleets to the `TRAFFIC_DIRECTOR` control plane implementation. 

This section only applies to the in-cluster control plane and the managed control plane with the Istiod implementation.

Cloud Service Mesh relies on a kubeconfig file embedded in the Kubernetes secret for proper remote endpoint discovery. Without the secrets, users will always see requests hit pods in the local cluster during cross-cluster load balancing.

Verify the secret has been created by running the following command in every cluster:
    
    
    kubectl get secret istio-remote-secret-CLUSTER_NAME_i -n istio-system
    

Verify the expected output:
    
    
    NAME                                   TYPE     DATA   AGE
    istio-remote-secret-CLUSTER_NAME_i   Opaque   1      44s
    

To recover from this, delete all the remote secrets and re-run the `create-mesh` command.

## Unreachable API server

**Caution:** In-cluster Cloud Service Mesh using the `ISTIOD` control plane on GKE on Google Cloud is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). Cloud Service Mesh with an in-cluster control plane on Google Distributed Cloud (software only) continues to be supported as described in [Supported platforms](https://docs.cloud.google.com/service-mesh/docs/supported-platforms#off-gcp). **Caution:** Managed Cloud Service Mesh using the `ISTIOD` control plane implementation is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). You must [modernize](https://docs.cloud.google.com/service-mesh/docs/modernization) all managed `ISTIOD` fleets to the `TRAFFIC_DIRECTOR` control plane implementation. 

This section only applies to in-cluster control plane and managed (istiod implementation).

The control plane of Cloud Service Mesh needs to reach the API server of the remote cluster. The following situations can cause the remote cluster to become unreachable: 

  * The remote cluster is deleted.
  * The remote cluster is a [private cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept) that does not have [global access](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#enabling_control_plane_private_endpoint_global_access) enabled.
  * The remote cluster is a [private cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept) with [Master Authorized Network](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks) enabled but the Cloud Service Mesh control plane IP has not been properly allowed using the allow list.



Given an unreachable API server, Istiod will output error messages in the log. Users will always see requests hit the local pod during cross-cluster load balancing.

In the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) interface, set the query `resource.type` to `istio_control_plane`.

Check to see if there are any invalid secret errors.

To recover from this problem, fix the underlying API server reachability issue. Next, delete all the remote secrets in every cluster and re-run the `create-mesh` command.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

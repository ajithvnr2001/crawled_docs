---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/certificate-sans/
title: Add domains to the API server certificate \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T02:29:43.392982+00:00
---

# Add domains to the API server certificate  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/certificate-sans/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Add domains to the API server certificate Stay organized with collections  Save and categorize content based on your preferences. 

Custom Subject Alternative Names (SANs) let you extend API server certificate coverage to additional domains, subdomains, and IP addresses. On a Google Distributed Cloud cluster, default SANs include only the IP and VIP addresses of control plane nodes and standard Kubernetes DNS names. You can configure custom SANs by using the mutable [`controlPlane.apiServerCertExtraSANs`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#controlplane-apiservercertextrasans) field in your cluster configuration file, either during cluster creation or at any time after.

## Add domains during cluster creation

When you add extra SANs when you create a cluster, the Kubernetes API server certificate includes the additional specified domains and IP addresses when the cluster becomes available.

The following example shows the `apiServerCertExtraSANs` field in a cluster configuration file:
    
    
    ...
    kind: Cluster
    metadata:
      name: sample001
      namespace: cluster-sample001
    spec:
      type: user
      ...
      controlPlane:**    apiServerCertExtraSANs:
        - "demo-dns.example.com"
        - "sample-dns.com"**
        nodePoolSpec:
          nodes:
          - address: 10.200.0.20
      clusterNetwork:
      ...
    

## Add or update domains for an existing cluster

Because the `apiServerCertExtraSANs` field is mutable, you can add or update the field at any time for existing clusters. When you modify the `apiServerCertExtraSANs` field in the cluster, it triggers the following activities:

  * The Google Distributed Cloud cluster controllers regenerate the API server certificate to include the modified extra domains.

  * The cluster controllers restart the API server to reload the new certificate.

  * The new values of `apiServerCertExtraSANs` are verified by a webhook to ensure that they conform to the [RFC 1035 domain name conventions](https://datatracker.ietf.org/doc/html/rfc1035).

  * The control plane node pool enters a reconciling state.
        
        Control Plane Node Pool Status:
          Anthos Bare Metal Version:  1.28.0-gke.435
          Anthos Bare Metal Versions:
            1.28.0-gke.435:  3
          Conditions:
            ...
            Last Transition Time:  2023-11-15T18:23:49Z
            Observed Generation:   1**    Reason:                Reconciling
            Status:                True
            Type:                  Reconciling**
        

  * The node pool becomes ready after the change propagates to the Kubernetes API servers on each control plane node.
        
        Control Plane Node Pool Status:
          Anthos Bare Metal Version:  1.28.0-gke.435
          Anthos Bare Metal Versions:
            1.28.0-gke.435:  3
          Conditions:
            . . .
            Last Transition Time:  2023-11-15T18:32:25Z
            Observed Generation:   1**    Reason:                ReconciliationCompleted
            Status:                False
            Type:                  Reconciling**
        
        




You might experience downtime when updating the API server certificate extra SANs field on a running cluster:

  * On high availability (HA) clusters, API server instances restart sequentially. You can still interact with the cluster during the certificate update, because the load balancer distributes requests to each API server. However, you might see a response indicating that the API server is shutting down. If you see this response, retry the request.

  * On non-HA clusters, there might be a brief outage of about one minute while an API server restarts to reload the new certificate.




The change takes 5-20 minutes to propagate to all API servers, depending on the number of control plane nodes in the cluster and the load of the cluster.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

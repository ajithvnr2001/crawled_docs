---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/1.16/gdcag/platform-application/pa-ao-operations/monitor-kub-metrics/
title: Monitor Kubernetes cluster health metrics \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T10:51:30.767956+00:00
---

# Monitor Kubernetes cluster health metrics  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/1.16/gdcag/platform-application/pa-ao-operations/monitor-kub-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/1.16/gdcag)



Send feedback 

#  Monitor Kubernetes cluster health metrics Stay organized with collections  Save and categorize content based on your preferences. 

The Kubernetes cluster (KUB) metrics dashboard in Google Distributed Cloud (GDC) air-gapped lets you monitor the operational health and performance of your Kubernetes clusters. Visualization panels display API server traffic and latency, cluster CPU and memory utilization, and node conditions so that you can troubleshoot issues and identify resource constraints.

## Kubernetes cluster dashboard

Open the following URL to access the Kubernetes cluster metrics dashboard:
    
    
    https://GDC_URL/platform-obs/grafana/KUB-pa-cluster-metrics
    

Replace `GDC_URL` with the URL of your organization in GDC.

The KUB dashboard presents graphs and visualization panels that contain information about Kubernetes cluster health in your project namespace.

You can view the general health of Kubernetes clusters to troubleshoot issues and to identify potential resource constraints at the cluster level.

### Kubernetes cluster general health

In this dashboard, you can gain valuable insights for your Kubernetes cluster health, such as the following:

  * API server traffic and latency
  * Cluster CPU and memory usage
  * Node conditions



![View the metrics dashboard for Kubernetes clusters.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/1.16/gdcag/platform-application/images/kub-metrics-dashboard.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

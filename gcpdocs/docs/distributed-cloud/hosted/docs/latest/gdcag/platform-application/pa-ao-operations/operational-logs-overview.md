---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/operational-logs-overview/
title: Operational logs overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T09:53:45.371457+00:00
---

# Operational logs overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/operational-logs-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Operational logs overview Stay organized with collections  Save and categorize content based on your preferences. 

Operational logs in Google Distributed Cloud (GDC) air-gapped let you monitor deployments and manage your applications and services. These logs capture information about runtime conditions, state changes, and system events across your environment so that you can do the following:

  * **Troubleshoot issues** : Identify and diagnose errors or unexpected behavior in your applications and infrastructure.
  * **Monitor performance** : Track resource usage, maintain a record of system events, and optimize application performance.



You can construct [LogQL](https://grafana.com/docs/loki/latest/logql/) (Log Query Language) expressions to search and filter operational logs. For more information, see [Query and view logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/query-and-view-logs).

GDC collects operational logs for various resources, including the following:

  * **Kubernetes workloads** : GDC captures logs from the standard output (`stdout`) and standard error (`stderr`) streams of your applications in the Kubernetes Container Runtime Interface (CRI) logging format. This format maintains consistency and compatibility with Kubernetes logging tools. For more information, see the [Kubernetes CRI logging specification](https://github.com/kubernetes/design-proposals-archive/blob/main/node/kubelet-cri-logging.md).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-02 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/monitor-cluster-high-availability/
title: Monitor cluster high availability \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:49:28.900874+00:00
---

# Monitor cluster high availability  |  AlloyDB Omni using the container orchestrator: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/monitor-cluster-high-availability/

[ Skip to main content ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/monitor-cluster-high-availability/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/monitor-cluster-high-availability/)
  * [Deutsch](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/monitor-cluster-high-availability/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/monitor-cluster-high-availability/?hl=es-419)
  * [Français](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/monitor-cluster-high-availability/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/monitor-cluster-high-availability/?hl=id)
  * [Italiano](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/monitor-cluster-high-availability/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/monitor-cluster-high-availability/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/monitor-cluster-high-availability/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/monitor-cluster-high-availability/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/monitor-cluster-high-availability/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/monitor-cluster-high-availability/?hl=ja)
  * [한국어](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/monitor-cluster-high-availability/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/alloydb-color.svg) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/overview)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/overview)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/monitor-cluster-high-availability/#before-you-begin)
  * [Monitor cluster topology and replication lag](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/monitor-cluster-high-availability/#monitor-ha)
  * [What's next](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/monitor-cluster-high-availability/#whats-next)


This page documents AlloyDB Omni version **18.3.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/overview)


Send feedback 
#  Monitor cluster high availability Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/monitor-cluster-high-availability/#before-you-begin)
  * [Monitor cluster topology and replication lag](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/monitor-cluster-high-availability/#monitor-ha)
  * [What's next](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/monitor-cluster-high-availability/#whats-next)


Select a documentation version:  18.3.0keyboard_arrow_down
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/monitor-cluster-high-availability)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/monitor-cluster-high-availability)


This page describes how to monitor the high availability topology, node health, and replication lag of your AlloyDB Omni cluster using the **Overview** page in the AlloyDB Omni web user interface.
## Before you begin
Before you monitor cluster high availability in the web UI, make sure that you have completed the following prerequisites:
  1. [Install the web UI](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/install-web-ui).
  2. [Connect to the web UI](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/connect-web-ui) and register the primary and standby or read pool instances for your cluster.


## Monitor cluster topology and replication lag
You can use the **Overview** page in the web UI to verify that standby and read pool nodes are actively streaming from the primary instance and to check for replication latency without running manual `pg_stat_replication` queries on individual nodes.
To monitor your cluster high availability status and replication metrics, complete the following steps:
  1. [Connect to the web UI](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/connect-web-ui) and select your cluster.
  2. In the navigation menu, click **Overview**.
  3. In the **Cluster overview** section, review the overall health metadata for your cluster: 
     * **Cluster ID** : The identifier of the selected cluster.
     * **Database version** : The PostgreSQL engine version running on the cluster (for example, `18.1`).
     * **Status** : The operational health state of the cluster (for example, `Ready`).
  4. In the **Instance details** section, inspect the **CPU Usage** chart for the past hour and review the instance topology and replication table, which displays the following columns for the primary instance and any standby or read pool instances: 
     * **Instance name** : The role or name of the instance in the cluster topology (for example, `Primary`, standby, or read pool node).
     * **Sync State** : The replication synchronization mode of the standby or read pool instance.
     * **Sender State** : The current WAL sender state on the primary instance streaming to the replica.
     * **Replay Lag** : The time delay or lag in replaying WAL records on the standby or read pool instance.
     * **Write Lag** : The lag in writing WAL records to disk on the standby or read pool instance.
     * **Flush Lag** : The lag in flushing WAL records to durable storage on the standby or read pool instance.


## What's next
  * [Manage and monitor AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/manage)
  * [Monitor AlloyDB Omni database performance](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/monitor-performance)


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

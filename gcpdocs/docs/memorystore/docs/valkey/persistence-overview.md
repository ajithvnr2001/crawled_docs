---
url: https://docs.cloud.google.com/memorystore/docs/valkey/persistence-overview/
title: Persistence overview \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T02:30:01.778166+00:00
---

# Persistence overview  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/persistence-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Persistence overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of persistence for Memorystore for Valkey.

Memorystore for Valkey supports two types of persistence:

  * [Append-only File (AOF) persistence](https://docs.cloud.google.com/memorystore/docs/valkey/about-aof-persistence)
  * [Redis Database (RDB) persistence](https://docs.cloud.google.com/memorystore/docs/valkey/about-rdb-persistence)



You can enable either AOF or RDB persistence for your instance but not both.

For the best instance availability and data durability, we recommend enabling both persistence and high availability (HA). While persistence and HA overlap in the protection that they offer, they have different strengths that complement each other. HA is the first line of defense against individual node failures and zonal outages. Persistence provides disaster recovery for rare events when all nodes in a shard fail and HA can't help. For more information about HA, see [High availability and replicas](https://docs.cloud.google.com/memorystore/docs/valkey/ha-and-replicas).

## Choosing a persistence type

Choosing between AOF and RDB persistence depends on your requirements for performance and data durability. These tradeoffs are generally true for all managed Valkey services because of the nature of AOF and RDB persistence.

If your top priority is data durability and preserving the highest percentage of writes sent to your Valkey server, then we recommend AOF persistence. AOF persistence can persist data every second (or for every write). This offers superior data durability compared to RDB snapshots, which save data on an hourly basis.

If performance is your top priority, then we recommend RDB persistence because this type of persistence usually places lower performance demands on your instance than AOF persistence. If you're comfortable with some staleness in your data on recovery and you want the performance that RDB persistence provides, then RDB persistence is the better choice for you.

You can achieve both high throughput and the durability of AOF persistence. To get both, enable AOF persistence and choose a high shard count. A high shard count provides more vCPUs, which improves performance. However, in any configuration, AOF persistence introduces some increase in latency.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/memorystore/docs/valkey/about-rdb-persistence/
title: About RDB persistence \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T19:53:52.083786+00:00
---

# About RDB persistence  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/about-rdb-persistence/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  About RDB persistence Stay organized with collections  Save and categorize content based on your preferences. 

This page gives an overview of Redis Database (RDB) persistence for Memorystore for Valkey.

RDB persistence protects your data by saving snapshots to durable storage. You can choose the frequency of these snapshots by selecting a snapshot interval ranging from a minimum of 1 hour to a maximum of 24 hours.

Nodes with replicas prioritize data recovery from the replica. However, if both the primary and the replica fail simultaneously, then the nodes recover from the most recent snapshot.

If you scale up your instance, then snapshots don't include the new shards until the next scheduled snapshot time. If you enable or disable persistence for an instance, then the instance might need to perform maintenance. For more information about enabling and disabling RDB persistence, see [Manage persistence](https://docs.cloud.google.com/memorystore/docs/valkey/manage-persistence).

RDB persistence adds no additional cost to your billing. This feature is ideal for use cases where you can accept a small degree of data staleness after recovery. Because Memorystore for Valkey uses snapshots for automated recovery, snapshots aren't available for manual restores. Also, Memorystore for Valkey retains only the most recent snapshot.

Memorystore for Valkey also supports AOF persistence, but you must choose either AOF or RDB persistence. You can't enable both persistence modes simultaneously. For more information about choosing between the persistence modes, see [Persistence overview](https://docs.cloud.google.com/memorystore/docs/valkey/persistence-overview).

For the best possible availability, we recommend using a highly available instance in addition to enabling persistence. For more information, see [High availability and replicas](https://docs.cloud.google.com/memorystore/docs/valkey/ha-and-replicas).

## Snapshot scheduling

The snapshot start time and the snapshot interval determine the snapshot schedule. The snapshot intervals that you can set are `1h`, `6h`, `12h`, and `24h`. For example, if you set the start time to 4 AM and the interval to one hour, then the snapshots start at 4 AM on the day that you enable RDB persistence, and continue every hour after that.

Memorystore for Valkey evaluates snapshot schedules in the UTC time zone. Therefore, if your time zone honors daylight saving time (DST) changes, then the local start times of your snapshot schedule jobs move forward or backward by an hour at the beginning and end of DST.

### Pausing snapshots

You might want to pause taking RDB snapshots temporarily. For example, you can pause snapshots to prevent performance impacts during critical events or to troubleshoot performance issues.

If you pause snapshots by setting the start time to the future, then Memorystore for Valkey retains the last snapshot. If a node fails and can't recover data from a replica, then the node uses this snapshot to recover the data. To resume snapshots, adjust the snapshot schedule to when you want the next snapshot to occur. For more information, see [Adjust RDB snapshot interval](https://docs.cloud.google.com/memorystore/docs/valkey/manage-persistence#adjust_rdb_snapshot_interval).

## Recovery behavior

Memorystore for Valkey nodes fail over to replicas as the primary recovery mechanism, rather than loading data from a snapshot. However, if a node fails and can't recover data from a replica, then the node recovers the data from the snapshot.

### Data consistency on recovery

When you enable RDB persistence, the instance makes a best effort to take snapshots at the specified interval. Because an RDB snapshot is a point-in-time backup, your application must be able to tolerate some staleness after Memorystore for Valkey recovers the data.

Snapshots can fail for many reasons. If a snapshot fails consecutively across multiple intervals, then the last available snapshot might be arbitrarily stale.

When recovering data from a snapshot, the worst-case data staleness is the sum of the specified interval since the last good snapshot started and the time that it takes to save the next snapshot to storage. If a recovery incident occurs, then use the `rdb_last_success_ages` metric to view the timeframe for data staleness. For more information about this metric, see [Persistence metrics](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics#persistence_metrics).

### Recovery time

If a node fails and needs to recover data from a snapshot, then the node is unavailable during recovery. The recovery time depends on the size of the snapshot.

### Snapshot failures

Memorystore for Valkey retries any failed snapshot immediately by using exponential backoff ranging from 5 to 300 seconds. If a recovery occurs, then consecutive snapshot failures increase data staleness.

### Recovery failures

Recovery failures are rare but can happen. If a recovery failure occurs, then the node retries recovering data from the snapshot repeatedly until the recovery succeeds.

## Monitoring snapshots

We recommend monitoring snapshots and setting alerts for failed snapshots. Failed snapshots can indicate overloaded nodes that might continue to have difficulty recovering data.

For more information about best practices for RDB persistence, see [Persistence best practices](https://docs.cloud.google.com/memorystore/docs/valkey/general-best-practices#persistence_best_practices). For a list of metrics that are available to monitor snapshots, see [Persistence metrics](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics#persistence_metrics).

### Performance impact

You can monitor the performance impact of a snapshot on your instance by using [Cloud Monitoring](https://docs.cloud.google.com/memorystore/docs/valkey/monitor-instances) to view metrics such as CPU usage and memory usage.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

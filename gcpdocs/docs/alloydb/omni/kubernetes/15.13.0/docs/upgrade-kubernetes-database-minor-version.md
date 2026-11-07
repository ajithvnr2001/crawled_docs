---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/upgrade-kubernetes-database-minor-version/
title: Perform a minor database version upgrade for AlloyDB Omni on Kubernetes \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.13.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-07T08:29:36.855091+00:00
---

# Perform a minor database version upgrade for AlloyDB Omni on Kubernetes  |  AlloyDB Omni for Kubernetes: 15.13.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/upgrade-kubernetes-database-minor-version/

This page documents AlloyDB Omni version **15.13.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/overview)



Send feedback 

#  Perform a minor database version upgrade for AlloyDB Omni on Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.13.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/upgrade-kubernetes-database-minor-version)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/upgrade-kubernetes-database-minor-version)



This page describes how to perform a minor database version upgrade for AlloyDB Omni on Kubernetes.

To perform a minor database version upgrade, there are two options:

  * Low downtime upgrade: This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For [high availability (HA)](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/kubernetes-ha) environments running AlloyDB Omni version 15.7.1 or later, AlloyDB Omni upgrades your standby instances first. Then, the AlloyDB Omni operator performs a switchover, promoting one of the upgraded standby instances to be your new primary instance. After the switchover succeeds, your old primary instance is updated.

This process ensures minimal downtime during the upgrade.

  * Simultaneous upgrade: The simultaneous upgrade method is [generally available](https://cloud.google.com/products#product-launch-stages) (GA). For all other circumstances, the AlloyDB Omni operator upgrades all instances simultaneously. Your instances experience downtime during the upgrade.




## Limitations

For low downtime upgrades, one standby instance is unavailable at any given time. To ensure that your database cluster doesn't reach zero Recovery Point Objective (RPO) and doesn't risk losing data, your database cluster must have one primary instance and at least two standby instances.

## Before you begin

  * If your cluster is HA and the AlloyDB Omni version is older than 15.7.1, follow the steps listed in [Update the database clusters](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/upgrade-kubernetes-operator-version#update-clusters) before following this minor version upgrade process.
  * Identify a low traffic period where you can perform the minor version upgrade.
  * To avoid any data loss, [back up your data](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/backup-kubernetes).



## Enable the low downtime minor database version upgrade process

To enable the low downtime minor database version upgrade process, add the following annotation to your database cluster.
    
    
    kubectl annotate dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME
    dbcluster.dbadmin.goog/enableLDTM=true
    

Replace the following variable:

  * `DB_CLUSTER_NAME`: the name of your database cluster. It's the same database cluster name that you provided when you created it. For more information, see [Install AlloyDB Omni on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/deploy-kubernetes#create).



## Upgrade your AlloyDB Omni version

To upgrade your 15.13.0 version, update the `databaseVersion` and the `controlPlaneAgentsVersion` fields in the cluster's manifest file, and then re-apply the file.

The following is the beginning of a manifest file that specifies version 15.13.0 for `databaseVersion` and version 1.6.4 for `controlPlaneAgentsVersion`:
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
        name: DB_CLUSTER_NAME
    spec:
        **databaseVersion : "DB_VERSION"**
        **controlPlaneAgentsVersion : "CONTROL_PLANE_AGENTS_VERSION"**
        # It is recommended to switch to UBI9 for improved security and
        # compatibility.
        # If you need to stick to Debian, set this field to "Debian".
        **databaseImageOSType : "OS_TYPE"**
    ...
    

Replace the following variable:

  * `DB_CLUSTER_NAME`: the name of your database cluster. It's the same database cluster name that you provided when you created it. For more information, see [Install AlloyDB Omni on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/deploy-kubernetes#create).
  * `DB_VERSION`: the version of the database that you're upgrading to, such as `15.18.1` or `15.13.0`.
  * `CONTROL_PLANE_AGENTS_VERSION`: the version of the control plane agents, such as `1.6.4`.
  * `OS_TYPE`: Optional. The base operating system for the database image. Valid values are `Debian` and `UBI9`. If you don't specify this, the operator automatically sets it to `Debian` if `databaseVersion` is less than `16.9.0`, and to `UBI9` if `databaseVersion` is `16.9.0` or later.



### Monitor the upgrade process

After you update your manifest file, the AlloyDB Omni operator starts the upgrade process. To monitor the upgrade process, check the `DBCUpgradeInProgress` condition.
    
    
    kubectl get dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -o yaml | yq '.status.conditions[] | select(.type == "DBCUpgradeInProgress")'
    

Replace the following variable:

  * `DB_CLUSTER_NAME`: the name of your database cluster. It's the same database cluster name that you provided when you created it. For more information, see [Install AlloyDB Omni on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/deploy-kubernetes#create).



While the process is in progress, the status is `true`. When the process is complete, the condition's status changes to `false`.

### Update timestamps and indexes after you upgrade to 15.18.1

This section applies to PostgreSQL 15 clusters that you upgrade to AlloyDB Omni version `15.18.1` (`databaseVersion: "15.18.1"`, `controlPlaneAgentsVersion: "1.6.4"`), as described in Upgrade your AlloyDB Omni version. Version `15.18.1` updates the container's IANA Time Zone Database, `tzdata`, to version `2026e`.

Version `2026e` of `tzdata` includes the following changes for regions that stopped seasonal daylight saving time (DST) clock changes in 2026:

  * **British Columbia, Canada** : `America/Vancouver` (`Canada/Pacific`) remains permanently on `UTC-07:00` after `2026-11-01 02:00:00` local time instead of falling back to `UTC-08:00`.
  * **Alberta and Northwest Territories, Canada** : `America/Edmonton` (`America/Yellowknife`, `Canada/Mountain`) and `America/Inuvik` remain permanently on `UTC-06:00` after `2026-11-01 02:00:00` local time instead of falling back to `UTC-07:00`.
  * **Manitoba and aligned northwest Ontario, Canada** : `America/Winnipeg` (`America/Rainy_River`, `Canada/Central`) remains permanently on `UTC-05:00` after `2026-11-01 02:00:00` local time instead of falling back to `UTC-06:00`.
  * **Morocco and Western Sahara** : `Africa/Casablanca` and `Africa/El_Aaiun` observe `UTC+00:00` starting `2026-09-20` (outside of Ramadan periods where `UTC+00:00` was already observed).



PostgreSQL stores each `timestamptz` (`timestamp with time zone`) value as a UTC instant. When PostgreSQL parses a local wall-clock string, it converts the string to UTC by using the `tzdata` rules installed at insert time. When you query the value, PostgreSQL converts it back to local time by using the current rules.

You don't need to run an `UPDATE` statement for the following:

  * `timestamptz` values generated by `now()` or `CURRENT_TIMESTAMP`, or inserted with an explicit UTC offset such as `-07:00` or `Z`. Their stored UTC instant is already correct, and after the upgrade, queries return the updated local time.
  * `timestamp` (`timestamp without time zone`) columns, which store literal wall-clock values without time zone conversion.



You must correct some `timestamptz` values that were written from local wall-clock strings before the upgrade. For the conditions that identify these rows, see Correct affected `timestamptz` rows.

For example, suppose that an application with the `TimeZone` parameter set to `America/Vancouver` inserted `'2026-11-10 09:00:00'` on version `15.13.0`. PostgreSQL converted that value by using the `UTC-08:00` offset from `tzdata` versions earlier than `2026e` and stored `2026-11-10 17:00:00 UTC`. After the upgrade, `America/Vancouver` stays on `UTC-07:00`, so a query returns `2026-11-10 10:00:00-07`, 1 hour later than the intended 9:00 AM. To fix the row, subtract 1 hour from the stored value. For `Africa/Casablanca` and `Africa/El_Aaiun`, the error runs the other way: the `UTC+01:00` offset in `tzdata` versions earlier than `2026e` stored values 1 hour too early, so add 1 hour.

#### Correct affected `timestamptz` rows

**Caution:** Adjusting rows whose stored UTC value is already correct causes data corruption. Before you change any data, identify the affected columns and rows.

Only `timestamptz` values that meet all of the following conditions are affected:

  * The value was parsed from a local wall-clock string without an explicit UTC offset while the session `TimeZone` parameter (or an `AT TIME ZONE` expression) used an affected time zone.
  * The row was written before you upgraded to version `15.18.1`.
  * The local time falls in a period with UTC offsets that differ between `tzdata` version `2026e` and earlier versions.



Correct affected rows as follows:

  * **Canadian time zones** : for local times on or after `2026-11-01 02:00:00` during periods when `tzdata` versions earlier than `2026e` observed standard time (first Sunday in November to second Sunday in March), subtract 1 hour.
  * **`Africa/Casablanca` and `Africa/El_Aaiun` time zones**: for local times on or after `2026-09-20` during periods when `tzdata` versions earlier than `2026e` observed `UTC+01:00`, add 1 hour. Ramadan periods, when `UTC+00:00` was already observed, aren't affected.



Before you correct rows, review the following:

  * **Correct each row only once.** The adjustment isn't idempotent.
  * **Update large tables in batches.** Batch updates limit lock time, replication lag, and `autovacuum` load.
  * **Check range partitions.** If partition bounds in the affected periods were created from local literals without an explicit UTC offset, recreate or split those partitions.
  * **Check other writers.** Inspect stored procedures, extensions such as `pg_cron`, and other data sources that might write or schedule timestamps from local wall-clock values.



#### Rebuild `AT TIME ZONE` indexes and views

PostgreSQL updates standard B-tree indexes on `timestamptz` columns when you correct rows, so these indexes don't need a `REINDEX` operation.

PostgreSQL marks the `AT TIME ZONE` operator (`timezone` function) as `IMMUTABLE`, so it doesn't recompute stored results when `tzdata` changes. After the upgrade, rebuild or refresh the following objects if they reference an affected time zone name:

  * Expression indexes and partial indexes whose `WHERE` predicate uses the `AT TIME ZONE` operator
  * Materialized views
  * Stored generated columns (`GENERATED ALWAYS AS (...) STORED`)



To rebuild indexes and refresh materialized views, run the following commands:
    
    
    REINDEX INDEX CONCURRENTLY INDEX_NAME;
    REFRESH MATERIALIZED VIEW CONCURRENTLY VIEW_NAME;
    

Replace the following:

  * `INDEX_NAME`: the name of the expression index or partial index that references an affected time zone with `AT TIME ZONE`.
  * `VIEW_NAME`: the name of the materialized view that references an affected time zone with `AT TIME ZONE`. If the materialized view doesn't have a `UNIQUE` index, omit the `CONCURRENTLY` keyword.



For stored generated columns, PostgreSQL recomputes the generated value in every row whose source column you corrected. For the remaining rows, update the source column (for example, by setting it to its current value) so that PostgreSQL recomputes the generated value.

**Note:** For questions about how these time zone changes affect your databases, contact [Cloud Customer Care](https://docs.cloud.google.com/support/docs).

## Troubleshooting

If you receive any failure messages during the upgrade process, see the following sections:

  * Pre-upgrade failures
  * Upgrade failures



### Pre-upgrade failures

If you receive a pre-upgrade failure on your database cluster, then check the message and address the problem accordingly.

If you would like to bypass the pre-upgrade failure message, then you can enable the `force-upgrade` annotation.
    
    
    kubectl annotate dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME upgrade.alloydbomni.dbadmin.google/force-upgrade=true
    

Replace the following variable:

  * `DB_CLUSTER_NAME`: the name of your database cluster. It's the same database cluster name that you provided when you created it. For more information, see [Install AlloyDB Omni on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/deploy-kubernetes#create).



After the upgrade process completes, set the `force-upgrade` annotation to `false`.

### Upgrade failures

During the automatic upgrade process, there are several points where it might fail in HA environments. For more information about each failure scenario and which subsequent actions the AlloyDB Omni operator takes, see the following table.

Failure message | Description | Required user actions |  `standby instance upgrade succeeded but the replication lag of the standby(s) is too high to be promoted to synchronous standby(s)` |  The upgrade process succeeded, but the standby instance didn't catch up to the primary instance to establish synchronous replication.  A high amount of traffic goes to the primary instance. As the traffic decreases, the standby instance catches up gradually. After this happens, the `HAReady` condition becomes `true`.  |  Choose an option in  Fix primary and standby instances with different minor versions .   
---|---|---  
`all standbys upgrade succeeded but the switchover instance failed to promote an upgraded standby.` |  Your standby instances upgraded successfully, but the switchover process failed.  | 

  1. Check the status of the switchover custom resource to determine what caused the failure. 
  2. Choose an option in  Fix primary and standby instances with different minor versions . 

  
`standby instance upgrade failed but rollback succeeded.` |  Your standby instance didn't upgrade successfully, but the AlloyDB Omni operator restored it to its previous version successfully.  | 

  1. Check the upgrade failure messages. 
  2. Choose an option in  Fix primary and standby instances with different minor versions . 

  
`standby instance upgrade failed and rollback failed.` |  Your standby instance didn't upgrade successfully and the AlloyDB Omni operator can't restore the instance to its previous version.  |  [ Contact Google support ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/resources/request-support) to troubleshoot.   
  
#### Fix primary and standby instances with different minor versions

To resolve this problem, choose one of the following options:

  * If the issue that caused the upgrade failure is fixed, retry the upgrade.

To retry the upgrade, remove the upgrade's `start-time` annotation from your instance. After you remove the annotation, the AlloyDB Omni operator generates a new start time and re-initiates the upgrade process.
        
        kubectl annotate dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME upgrade.alloydbomni.dbadmin.google/start-time-
        

Replace the following variable:

    * `DB_CLUSTER_NAME`: the name of your database cluster. It's the same database cluster name that you provided when you created it. For more information, see [Install AlloyDB Omni on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/deploy-kubernetes#create).
  * If the issue that caused the upgrade failure persists, then downgrade your instance to the previous AlloyDB Omni operator version.

To downgrade your instance, follow the upgrade process and change the `databaseVersion`, `controlPlaneAgentsVersion`, and `databaseImageOSType` fields in the manifest file to the version you used before. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-06 UTC."],[],[]] 

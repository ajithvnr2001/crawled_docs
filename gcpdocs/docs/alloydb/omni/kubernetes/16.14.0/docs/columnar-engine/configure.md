---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/
title: Configure the columnar engine in AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 16.14.0 \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 503)
fetched_at: 2026-11-08T05:45:16.920409+00:00
---

# Configure the columnar engine in AlloyDB Omni  |  AlloyDB Omni using the container orchestrator: 16.14.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/

[ Skip to main content ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/)
  * [Deutsch](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/?hl=es-419)
  * [Français](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/?hl=id)
  * [Italiano](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/?hl=ja)
  * [한국어](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Falloydb%2Fomni%2Fkubernetes%2F16.14.0%2Fdocs%2Fcolumnar-engine%2Fconfigure%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/alloydb-color.svg) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/overview)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/overview)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Enable the columnar engine](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/#enable)
  * [Configure the size of the column store](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/#configure)
    * [Configure memory](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/#configure-memory)
    * [Configure storage cache](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/#configure-storage-cache)
  * [Enable vectorized join](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/#vectorized)
  * [Manually refresh your columnar engine](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/#manual-refresh)
  * [Disable the columnar engine](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/#disable)
  * [What's next](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/#whats-next)


This page documents AlloyDB Omni version **16.14.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/overview)


Was this helpful?
Send feedback 
#  Configure the columnar engine in AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Enable the columnar engine](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/#enable)
  * [Configure the size of the column store](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/#configure)
    * [Configure memory](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/#configure-memory)
    * [Configure storage cache](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/#configure-storage-cache)
  * [Enable vectorized join](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/#vectorized)
  * [Manually refresh your columnar engine](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/#manual-refresh)
  * [Disable the columnar engine](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/#disable)
  * [What's next](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/#whats-next)


Select a documentation version:  16.14.0keyboard_arrow_down
  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/columnar-engine/configure)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/columnar-engine/configure)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/columnar-engine/configure)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/columnar-engine/configure)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/columnar-engine/configure)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/columnar-engine/configure)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/columnar-engine/configure)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/columnar-engine/configure)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/columnar-engine/configure)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/configure)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/columnar-engine/configure)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/columnar-engine/configure)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/columnar-engine/configure)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/columnar-engine/configure)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/columnar-engine/configure)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/columnar-engine/configure)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/columnar-engine/configure)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/columnar-engine/configure)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/columnar-engine/configure)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/columnar-engine/configure)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/columnar-engine/configure)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/columnar-engine/configure)

This page describes how to enable or disable the columnar engine on an AlloyDB Omni database cluster. It also covers how to configure an appropriate initial size for its column store. 
For a conceptual overview of the AlloyDB columnar engine, see [AlloyDB Omni columnar engine overview](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/overview).
## Enable the columnar engine
To use columnar engine on an instance, set the instance's [`google_columnar_engine.enabled`](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/reference/columnar-engine-flags#enabled) flag to `on`.
[ Kubernetes ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/#kubernetes) More
To set the `google_columnar_engine.enabled` flag to `on`, modify your database cluster manifest to add the `parameters` attribute to the `primarySpec` section:

```
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: CLUSTER_NAME
    spec:
      databaseVersion: "16.14.0"
      primarySpec:
        parameters:
          google_columnar_engine.enabled: "on"

```

Replace `CLUSTER_NAME` with the name of your database cluster. It is the same database cluster name you declared when [you created it](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/deploy-kubernetes#create).
## Configure the size of the column store
While the columnar engine is enabled on an instance, AlloyDB Omni allocates a portion of the instance's memory to store its columnar data. Dedicating high-speed RAM to your column store verifies that AlloyDB Omni can access the columnar data as rapidly as possible.
Memory and storage cache together represent the overall capacity of the columnar engine.
### Configure memory
You can set the allocation to a fixed size using the [`google_columnar_engine.memory_size_in_mb`](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/reference/columnar-engine-flags#memory-size-in-mb) flag.
[ Kubernetes ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/#kubernetes) More
To set the `google_columnar_engine.memory_size_in_mb` flag, modify your database cluster manifest to add the `parameters` attribute to the `primarySpec` section:

```
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: CLUSTER_NAME
    spec:
      databaseVersion: "16.14.0"
      primarySpec:
        parameters:
          google_columnar_engine.memory_size_in_mb: "COLUMN_MEMORY_SIZE"

```

Replace the following:
  * `CLUSTER_NAME`: the name of your database cluster. It is the same database cluster name you declared when [you created it](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/deploy-kubernetes#create).
  * `COLUMN_MEMORY_SIZE`: the new size of the column storage, in megabytes—for example, `256`.


### Configure storage cache
[ Kubernetes ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/#kubernetes) More
To enable storage cache for your database, modify your database cluster manifest to add the `columnarSpillToDisk` attribute to the `features` section of the `primarySpec` section:

```
apiVersion: alloydbomni.dbadmin.goog/v1
kind: DBCluster
metadata:
  name: CLUSTER_NAME
spec:
  databaseVersion: "16.14.0"
  primarySpec:
    features:
      columnarSpillToDisk:
        cacheSize: STORAGE_CACHE_SIZE
      ultraFastCache:
        cacheSize: ULTRAFAST_CACHE_SIZE
        genericVolume:
          storageClass: "STORAGE_CLASS_NAME"
...

```

Replace the following:
  * `CLUSTER_NAME`: the name of your database cluster. It is the same database cluster name you declared when [you created it](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/deploy-kubernetes#create).
  * `STORAGE_CACHE_SIZE`: the size of the columnar storage cache—for example, `5Gi`. If you don't specify a value for this field, 5% of the disk cache gets allocated to the columnar engine by default.
  * `ULTRAFAST_CACHE_SIZE`: the size of the cache—for example, `100Gi`. It must be greater than `shared_buffers`. This field is optional. If you don't specify the value of this field, AlloyDB Omni uses all space left on the disk, which applies to both AlloyDB Omni in a container and on a Kubernetes cluster. For more information about units of measure, see [Memory resource units](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#meaning-of-memory).
  * `STORAGE_CLASS_NAME`: the name of the [storage class](https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1) of the ultra fast cache volume—for example, `local-storage`.


## Enable vectorized join
The columnar engine has a _vectorized join_ feature that can improve the performance of joins by applying vectorized processing to qualifying queries.
After you enable vectorized join, the AlloyDB query planner has the option to apply the vectorized join operator instead of the standard PostgreSQL hash join operator. The planner makes this decision by comparing the cost of executing the query using each method.
To enable vectorized join on an instance, set the instance's [`google_columnar_engine.enable_vectorized_join`](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/reference/columnar-engine-flags#enable-vectorized-join) flag to `on`.
To set this flag on a Kubernetes database cluster, add `google_columnar_engine.enable_vectorized_join: "on"` to the `parameters` section of your `DBCluster` manifest. For more information, see [Configure AlloyDB Omni database flags](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/configure-database-flags). 
AlloyDB Omni allocates one thread to the vectorized join feature by default. You can increase the number of threads available to this feature by setting the [`google_columnar_engine.vectorized_join_threads`](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/reference/columnar-engine-flags#vectorized-join-threads) flag to a larger value. The maximum value is `cpu_count * 2`.
## Manually refresh your columnar engine
By default, when the columnar engine is enabled it refreshes the column store in the background.
To manually refresh the column engine, run the following SQL query:

```
SELECT google_columnar_engine_refresh(relation =>'TABLE_NAME');

```

Replace `TABLE_NAME` with the name of the table or the materialized view you want to manually refresh.
## Disable the columnar engine
To disable the columbar engine on an instance, set the `google_columnar_engine.enabled` flag to `off`.
[ Kubernetes ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure/#kubernetes) More
To set the `google_columnar_engine.enabled` flag to `off`, modify your database cluster manifest to add the `parameters` attribute to the `primarySpec` section:

```
  apiVersion: alloydbomni.dbadmin.goog/v1
  kind: DBCluster
  metadata:
    name: CLUSTER_NAME
  spec:
    databaseVersion: "16.14.0"
    primarySpec:
      parameters:
        google_columnar_engine.enabled: "off"

```

Replace `CLUSTER_NAME` with the name of your database cluster. It is the same database cluster name you declared when [you created it](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/deploy-kubernetes#create).
## What's next
  * See the [full list of columnar engine database flags](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/reference/columnar-engine-flags).
  * Work through the [Accelerating analytical queries with columnar engine in AlloyDB Omni](https://codelabs.developers.google.com/alloydb-omni-columnar) Google CodeLab tutorial.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-11-07 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 

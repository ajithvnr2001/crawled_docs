---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/high-obtainability/
title: Create a High Obtainability cluster \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T05:40:31.816937+00:00
---

# Create a High Obtainability cluster  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/high-obtainability/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Create a High Obtainability cluster Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create a Managed Service for Apache Spark cluster in High Obtainability (HO) mode. High Obtainability mode improves the likelihood of successfully provisioning cluster VMs during periods of high demand or resource constraints by allowing Managed Service for Apache Spark to select from a range of compatible machine types rather than requiring a fixed machine type when creating a cluster.

Use High Obtainability mode to create clusters with general-purpose compute requirements to help prevent cluster creation and scaling failures due to VM unavailability.

## How High Obtainability mode works

In standard cluster creation requests, you specify specific machine types (such as `n2-standard-4`) for cluster nodes. If that specific machine type is unavailable in a zone, the creation request fails.

In High Obtainability mode, you specify flexible resource requirements for master, primary worker, and secondary worker nodes instead of fixed machine types:

  * **vCPU core count** : You request a target number of vCPUs per VM instance (2, 4, 8, 16, or 32 cores).
  * **Hardware class** : You specify the performance and memory profile:

    * `STANDARD`: Provides a balanced configuration with approximately 4 GB of memory per vCPU and standard persistent storage tiers. Current candidate machine types include `n4-standard`, `n4d-standard`, `n2-standard`, and `n2d-standard` (Rank 0 preference), and `c4-standard` and `c4d-standard` (Rank 1 preference).
    * `PERFORMANCE`: Provides a high-performance configuration with approximately 8 GB of memory per vCPU and higher-tier disk configurations (higher IOPS and throughput). Current candidate machine types include `n4-highmem`, `n4d-highmem`, `n2-highmem`, and `n2d-highmem` (Rank 0 preference), and `c4-highmem` and `c4d-highmem` (Rank 1 preference).
**Note:** The candidate machine types for each hardware class are controlled by Google and can change at any time. The current candidate machine types are listed for transparency; don't take a dependency on specific machine types. Make sure that your project has sufficient [Compute Engine resource quotas](https://docs.cloud.google.com/managed-spark/quotas#other-gcp-quotas) in the cluster region for all candidate machine families (`N4`, `N4D`, `N2`, `N2D`, `C4`, and `C4D`).
  * **Instance count** : You specify the number of instances for each group:

    * Master: must be 1 instance.
    * Primary workers: positive integer.
    * Secondary workers: non-negative integer.
  * **Boot disk size** : Optional boot disk size (for example, 100 GB).




Managed Service for Apache Spark automatically uses [Auto Zone placement](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/auto-zone) to evaluate zones across the cluster region and select candidate machine types within the requested hardware class that have available capacity.

## Requirements and limitations

High Obtainability mode has the following requirements and limitations:

  * **Resource quotas** : Your project must have sufficient [Compute Engine resource quotas](https://docs.cloud.google.com/managed-spark/quotas#other-gcp-quotas) in the cluster region for all candidate machine families in your selected hardware class (`N4`, `N4D`, `N2`, `N2D`, `C4`, and `C4D`). Because the underlying candidate machine types are controlled by Google and can change at any time, don't take a dependency on specific machine types.
  * **Zone specification** : You cannot specify an explicit `--zone` (or `zoneUri`). Managed Service for Apache Spark automatically selects an available zone in the region using Auto Zone placement.
  * **Mutual exclusivity with fixed machine and node configurations** : 
    * When configuring master, primary worker, or secondary worker node groups with flexible configurations (`--master-flexible-config`, `--worker-flexible-config`, or `--secondary-worker-flexible-config`), you cannot specify standard machine type, instance selection, instance count, disk, or accelerator flags for those node groups: 
      * **Master** : Cannot be combined with `--master-machine-type`, `--master-machine-types`, `--master-instance-selection`, `--master-instance-flexibility-policy-file`, `--master-boot-disk-size`, `--master-boot-disk-type`, `--num-master-local-ssds`, `--master-accelerator`, or `--master-min-cpu-platform`.
      * **Primary workers** : Cannot be combined with `--num-workers`, `--worker-machine-type`, `--worker-machine-types`, `--worker-instance-selection`, `--worker-instance-flexibility-policy-file`, `--worker-boot-disk-size`, `--worker-boot-disk-type`, `--num-worker-local-ssds`, `--worker-accelerator`, or `--worker-min-cpu-platform`.
      * **Secondary workers** : Cannot be combined with `--num-secondary-workers`, `--secondary-worker-type`, `--secondary-worker-machine-types`, `--secondary-worker-instance-selection`, `--secondary-worker-instance-flexibility-policy-file`, `--secondary-worker-boot-disk-size`, `--secondary-worker-boot-disk-type`, `--num-secondary-worker-local-ssds`, or `--secondary-worker-accelerator`.
    * In a multi-node cluster, if High Obtainability mode is enabled for the master node group, the primary worker node group must also use flexible configurations (`--worker-flexible-config`).
    * If secondary workers are used in a High Obtainability cluster, they must use `--secondary-worker-flexible-config` rather than standard secondary worker flags.
  * **Single-node clusters** : In a [single-node cluster](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/single-node-clusters) (`--single-node` or `--cluster-type=single-node`), only `--master-flexible-config` can be specified. Primary and secondary worker flexible configuration flags are not supported.
  * **Cluster updates** : You can update the number of instances (`num-instances`) for primary and secondary workers using `gcloud dataproc clusters update`. The core count, hardware class, and boot disk size are create-time specifications and cannot be modified after creation.
  * **High availability clusters** : High availability (HA) clusters (clusters with three master nodes) are not supported in High Obtainability mode. Master instance count must be 1.



## Create a High Obtainability cluster

You can create a cluster in High Obtainability mode by using the Google Cloud CLI or the Dataproc API.

**Note:** Configuration of High Obtainability mode in the Google Cloud console isn't available.

###  gcloud 

To create a cluster in High Obtainability mode, run the [`gcloud dataproc clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command with the `--master-flexible-config` and `--worker-flexible-config` flags.
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --master-flexible-config="cores=CORES,hardware-class=HARDWARE_CLASS,num-instances=1,boot-disk-size=BOOT_DISK_SIZE" \
        --worker-flexible-config="cores=CORES,hardware-class=HARDWARE_CLASS,num-instances=NUM_WORKERS,boot-disk-size=BOOT_DISK_SIZE"
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `REGION`: the [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the cluster, such as `us-central1`. Do not specify a `--zone`.
  * `CORES`: the number of vCPUs per VM instance. Must be a power of 2 (`2`, `4`, `8`, `16`, or `32`).
  * `HARDWARE_CLASS`: the hardware profile class, either `STANDARD` or `PERFORMANCE`.
  * `NUM_WORKERS`: the number of primary worker nodes in the cluster.
  * `BOOT_DISK_SIZE`: the size of the boot disk, such as `100GB`.



### Add secondary workers

To add secondary worker nodes in High Obtainability mode, include the `--secondary-worker-flexible-config` flag:
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --master-flexible-config="cores=4,hardware-class=STANDARD,num-instances=1,boot-disk-size=100GB" \
        --worker-flexible-config="cores=4,hardware-class=STANDARD,num-instances=2,boot-disk-size=100GB" \
        --secondary-worker-flexible-config="cores=4,hardware-class=STANDARD,num-instances=2,boot-disk-size=100GB"
    

### Create a single-node cluster

To create a [single-node](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/single-node-clusters) High Obtainability cluster, specify `--single-node` (or `--cluster-type=single-node`) with `--master-flexible-config` and omit worker flexible configuration flags:
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --single-node \
        --master-flexible-config="cores=4,hardware-class=STANDARD,boot-disk-size=100GB"
    

### Update cluster worker capacity

To scale the number of primary or secondary workers on an existing High Obtainability cluster, use the [`gcloud dataproc clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update) command:
    
    
    gcloud dataproc clusters update CLUSTER_NAME \
        --region=REGION \
        --worker-flexible-config="num-instances=NEW_NUM_WORKERS"
    

###  REST 

To create a High Obtainability cluster using the REST API, send a [`clusters.create`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request. In the [`ClusterConfig`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig) object:

  1. Leave [`gceClusterConfig.zoneUri`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#gceclusterconfig) empty (or omit it) to enable Auto Zone placement.
  2. Specify the [`masterFlexibleConfig`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#flexibleinstancegroupconfig) and [`workerFlexibleConfig`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#flexibleinstancegroupconfig) objects.



HTTP method and URL:
    
    
    POST https://dataproc.googleapis.com/v1/projects/PROJECT_ID/regions/REGION/clusters
    

Request JSON body:
    
    
    {
      "projectId": "PROJECT_ID",
      "clusterName": "CLUSTER_NAME",
      "config": {
        "gceClusterConfig": {
          "zoneUri": ""
        },
        "masterFlexibleConfig": {
          "numInstances": 1,
          "coreCount": 4,
          "hardwareClass": "STANDARD",
          "bootDiskSizeGb": 100
        },
        "workerFlexibleConfig": {
          "numInstances": 2,
          "coreCount": 4,
          "hardwareClass": "STANDARD",
          "bootDiskSizeGb": 100
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `REGION`: the [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the cluster will be created, such as `us-central1`.
  * `CLUSTER_NAME`: the name of the cluster.



Optional: To add secondary workers, include the `secondaryWorkerFlexibleConfig` object with the desired `numInstances`, `coreCount`, `hardwareClass`, and `bootDiskSizeGb`.

## What's next

  * Learn more about [Auto Zone placement](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/auto-zone).
  * Learn about [Prioritize VM types with flexible VMs](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/flexible-vms).
  * Learn how to [scale Managed Service for Apache Spark clusters](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/scaling-clusters).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 

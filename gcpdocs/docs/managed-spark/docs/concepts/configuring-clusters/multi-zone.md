---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/multi-zone/
title: Create a multi-zone cluster \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T05:36:53.933296+00:00
---

# Create a multi-zone cluster  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/multi-zone/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Create a multi-zone cluster Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create a Managed Service for Apache Spark multi-zone cluster. In a multi-zone cluster, Managed Service for Apache Spark provisions and distributes the Compute Engine VM instances of the cluster across multiple zones in a single region, instead of placing all cluster nodes in one zone.

Use a multi-zone cluster when you need to create or scale a large cluster and the capacity of a single zone might not be enough to meet your request.

## How multi-zone clusters work

When you create a multi-zone cluster, Managed Service for Apache Spark provisions the cluster nodes as follows:

  * Master nodes: Managed Service for Apache Spark places the master instance group in a single zone in the cluster region by using [Auto Zone placement](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/auto-zone).
  * Worker nodes: Managed Service for Apache Spark configures the primary and [secondary worker](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/secondary-vms) groups as [regional managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape). These groups provision and distribute worker VMs across any eligible zone in the region that has available capacity.



Because Managed Service for Apache Spark distributes worker VM requests across multiple zones, capacity constraints in a single zone are less likely to block your request. This helps prevent `ZONE_RESOURCE_POOL_EXHAUSTED` errors when you create or scale large clusters, clusters with Spot VM or preemptible secondary workers, or clusters that use high-demand machine types.

## Requirements and limitations

To create a multi-zone cluster, you must use one of the following [image versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/overview) or a later version in the same image version track:

Image version track | Minimum supported image version  
---|---  
2.2.x | `2.2.88`  
2.3.x | `2.3.37`  
3.0.x | `3.0.3`  
  
Multi-zone clusters have the following limitations:

  * You can't specify both a single zone and a multi-zone configuration in the same cluster creation request.
  * You can't create a multi-zone cluster with more than 1,000 primary workers in the initial cluster creation request. If your workload requires more than 1,000 primary workers, create the cluster with 1,000 or fewer primary workers, and then [scale the cluster](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/scaling-clusters) after it is created.



## Network data transfer costs

**Caution:** A multi-zone cluster can increase your network data transfer costs because of cross-zone data transfer between cluster nodes.

In a single-zone cluster, all VMs are in the same zone, and network traffic that uses internal IP addresses between VMs in the same zone is offered at no charge. In a multi-zone cluster, master and worker VMs can be in different zones in the same region. Network traffic between VMs in different zones in the same region incurs inter-zone data transfer charges.

For pricing details, see [VM-VM data transfer pricing within Google Cloud](https://docs.cloud.google.com/vpc/network-pricing#vm-vm-data-transfer-pricing-within-google-cloud).

## Create a multi-zone cluster

You can create a multi-zone cluster by using the Google Cloud CLI or the Dataproc API.

###  gcloud 

To create a multi-zone cluster, run the [`gcloud dataproc clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command with the `--multizone` flag. Don't specify the `--zone` flag.
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --multizone \
        --image-version=IMAGE_VERSION \
        --master-machine-type=MASTER_MACHINE_TYPE \
        --worker-machine-type=WORKER_MACHINE_TYPE \
        --num-workers=NUM_WORKERS
    

Replace the following:

  * CLUSTER_NAME: the name of the cluster.
  * REGION: an [available Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the cluster, such as `us-central1`.
  * IMAGE_VERSION: an image version that supports multi-zone clusters, such as `2.3.37-debian12`. For more information, see Requirements and limitations.
  * MASTER_MACHINE_TYPE: the Compute Engine machine type of the master node, such as `n2-standard-4`.
  * WORKER_MACHINE_TYPE: the Compute Engine machine type of the primary worker nodes, such as `n2-standard-4`.
  * NUM_WORKERS: the number of primary workers in the cluster. This value can't be greater than `1000`.



###  REST 

To create a multi-zone cluster, send a [`clusters.create`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request. In the [`gceClusterConfig`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#GceClusterConfig) object of the request, leave the `zoneUri` field empty, and set the [`multiZoneConfig.targetShape`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#multizoneconfig) field to `ANY`.

HTTP method and URL:
    
    
    POST https://dataproc.googleapis.com/v1/projects/PROJECT_ID/regions/REGION/clusters
    

Request JSON body:
    
    
    {
      "projectId": "PROJECT_ID",
      "clusterName": "CLUSTER_NAME",
      "config": {
        "gceClusterConfig": {
          "multiZoneConfig": {
            "targetShape": "ANY"
          }
        },
        "softwareConfig": {
          "imageVersion": "IMAGE_VERSION"
        },
        "masterConfig": {
          "numInstances": 1,
          "machineTypeUri": "MASTER_MACHINE_TYPE"
        },
        "workerConfig": {
          "numInstances": NUM_WORKERS,
          "machineTypeUri": "WORKER_MACHINE_TYPE"
        }
      }
    }
    

Replace the following:

  * PROJECT_ID: your Google Cloud project ID.
  * REGION: an [available Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the cluster, such as `us-central1`.
  * CLUSTER_NAME: the name of the cluster.
  * IMAGE_VERSION: an image version that supports multi-zone clusters, such as `2.3.37-debian12`. For more information, see Requirements and limitations.
  * MASTER_MACHINE_TYPE: the Compute Engine machine type of the master node, such as `n2-standard-4`.
  * NUM_WORKERS: the number of primary workers in the cluster. This value can't be greater than `1000`.
  * WORKER_MACHINE_TYPE: the Compute Engine machine type of the primary worker nodes, such as `n2-standard-4`.



## What's next

  * Learn more about [Auto Zone placement](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/auto-zone).
  * Learn how to [scale Managed Service for Apache Spark clusters](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/scaling-clusters).
  * Learn about [regional MIG target distribution shapes](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/filestore/docs/create-volume-pools/
title: Create and manage volume pools \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T08:57:49.093449+00:00
---

# Create and manage volume pools  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/create-volume-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Create and manage volume pools Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Filestore agent volumes are available under an Allowlisted GA (AGA) program. To request access for your Google Cloud project, submit the Filestore agent volumes [access request form](https://forms.gle/vYPkcFiZVoTjf7Ah7). 

A volume pool is the top-level regional resource that manages a shared pool of storage capacity and IOPS for your project and Virtual Private Cloud (VPC) network. Within a volume pool, you can provision up to 20 million independent, lightweight volumes (with up to 50,000 concurrently active volumes and up to 5 PB of used capacity) for AI agent sandboxes, developer workspaces, or general multi-tenant workloads.

## Before you begin

Complete the prerequisites described in [Set up Filestore agent volumes](https://docs.cloud.google.com/filestore/docs/agent-volumes-prerequisites).

## Create a volume pool

### REST API

To create a volume pool, send an HTTP `POST` request to the `volumePools.create` endpoint:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json; charset=utf-8" \
      -d '{
        "description": "Production volume pool for AI agent sandboxes",
        "network": "projects/PROJECT_ID/global/networks/VPC_NETWORK",
        "defaultVolumeQuotaMib": 2048,
        "activeVolumeIops": 1000,
        "labels": {
          "env": "production",
          "workload": "ai-sandboxes"
        }
      }' \
      "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/volumePools?volumePoolId=VOLUME_POOL_ID"
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID.
  * `LOCATION`: the region where the pool is deployed, such as `us-central1`.
  * `VOLUME_POOL_ID`: the identifier for the volume pool, matching `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`.
  * `VPC_NETWORK`: the name of an existing VPC network.



### Request fields

The request body contains the following fields:

Field | Type | Required | Description  
---|---|---|---  
`network` | `string` | Required | The resource path of your VPC network, in the format: `projects/{project}/global/networks/{network}`. The network must have a valid PSC service connection policy.  
`defaultVolumeQuotaMib` | `int32` | Optional | The default quota per volume in MiB. The value must be between 100 MiB and 102,400 MiB (100 GiB). The default value is 1,024 MiB.  
`activeVolumeIops` | `int32` | Optional | Specifies the number of IOPS provisioned per active volume within the volume pool. Default is 3,000 IOPS; maximum is 10,000 IOPS. IOPS are provisioned and billed at the volume pool level. For more information about pricing, see the [Filestore pricing page](https://docs.cloud.google.com/filestore/pricing).  
`description` | `string` | Optional | A user-friendly description of the volume pool.  
`labels` | `map[string, string]` | Optional | Key-value pairs that allow you to organize and filter resources in Google Cloud.  
`autoFreezeDelay` | `string` | Optional | The duration that a volume must remain detached (with empty IP ACLs) before it is automatically tiered to `COLD` storage. The format is a duration string ending with `s` (for example, `604800s` for 7 days). The default is 7 days.  
  
### Response

The method returns a long-running operation (LRO) object:
    
    
    {
      "name": "projects/my-project/locations/us-central1/operations/operation-1694000000000-abcde",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.filestore.v1beta1.OperationMetadata",
        "createTime": "2026-09-08T10:00:00.000Z",
        "target": "projects/my-project/locations/us-central1/volumePools/my-volume-pool",
        "verb": "create"
      },
      "done": false
    }
    

Poll the operation until `done` is `true`:
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID"
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID.
  * `LOCATION`: the region where the volume pool is deployed, such as `us-central1`.
  * `OPERATION_ID`: the operation ID returned in the creation response.



When completed, the operation returns the `VolumePool` object with state `READY`.

After your volume pool reaches the `READY` state, choose how you want to provision and mount volumes from the pool:

  * **Deploy with GKE:** Proceed to [Set up GKE environment for Filestore agent volumes](https://docs.cloud.google.com/filestore/docs/use-filestore-agent-volumes-gke). The Filestore CSI driver provisions and manages volumes in your pool automatically.
  * **Deploy with your own orchestration framework:** Proceed to [Create and manage volumes using the REST API](https://docs.cloud.google.com/filestore/docs/manage-agent-volumes) to provision, mount, clone, and tier individual volumes directly.



## Manage volume pools

You can view details about existing volume pools, list pools within a region, update configurations such as labels and capacity quotas, or delete volume pools.

###  Google Cloud console 

You can view volume pools and monitor pool capacity directly in the Google Cloud console:

  1. In the Google Cloud console, go to the Filestore **Volume pools** page.

[Go to Volume pools](https://console.cloud.google.com/filestore/volumepools)

  2. Click any volume pool in the list to open the **Volume pool details** page.

  3. On the **Monitoring** tab, view real-time charts for active volume count, storage capacity, IOPS, and I/O latency.




### REST API

In each of the following requests, replace:

  * `PROJECT_ID`: the Google Cloud project ID.
  * `LOCATION`: the region where the volume pool is deployed, such as `us-central1`.
  * `VOLUME_POOL_ID`: the identifier of the volume pool.



### Get information about a volume pool

To retrieve details about a specific volume pool:
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/volumePools/VOLUME_POOL_ID"
    

### List volume pools

To list all volume pools in a given region:
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/volumePools"
    

### Update a volume pool

To update the description or labels of an existing volume pool, send a `PATCH` request with an `updateMask` query parameter:
    
    
    curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/volumePools/VOLUME_POOL_ID?updateMask=description,labels" \
      -d '{
        "description": "Updated pool description",
        "labels": {
          "env": "production",
          "owner": "platform-team"
        }
      }'
    

The `PATCH` method returns a long-running operation. You can poll the operation until it completes.

### Delete a volume pool

Before deleting a volume pool, you must delete all child volumes provisioned within the pool. To delete a volume pool:
    
    
    curl -X DELETE \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/volumePools/VOLUME_POOL_ID"
    

## Monitor volume pools

You can monitor the performance, capacity, and volume counts of your volume pools using Cloud Monitoring and the Google Cloud console.

### Monitoring metrics

Filestore exports 12 dedicated metrics under the `file.googleapis.com/volume_pool/` namespace:

Metric type | Display name | Kind | Unit | Description  
---|---|---|---|---  
`volume_pool/volumes` | Volumes | `GAUGE` | `{volume}` | Number of volumes in the volume pool, broken down by lifecycle state.  
`volume_pool/used_bytes` | Used bytes | `GAUGE` | `By` | Total used capacity in the volume pool.  
`volume_pool/cold_used_bytes` | Cold used bytes | `GAUGE` | `By` | Total storage consumed by volumes in the `COLD` tier within the volume pool.  
`volume_pool/provisioned_iops` | Provisioned IOPS | `GAUGE` | `{operation}/s` | Provisioned IOPS limit for the volume pool.  
`volume_pool/read_ops_count` | Read operation count | `DELTA` | `{operation}` | Count of read operations across all volumes in the volume pool.  
`volume_pool/write_ops_count` | Write operation count | `DELTA` | `{operation}` | Count of write operations across all volumes in the volume pool.  
`volume_pool/total_ops_count` | Total operation count | `DELTA` | `{operation}` | Count of read and write operations across all volumes in the volume pool.  
`volume_pool/read_bytes_count` | Bytes read | `DELTA` | `By` | Bytes read across all volumes in the volume pool.  
`volume_pool/write_bytes_count` | Bytes written | `DELTA` | `By` | Bytes written across all volumes in the volume pool.  
`volume_pool/average_read_latency` | Average read latency | `GAUGE` | `ms` | Average latency for read operations across all volumes in the volume pool.  
`volume_pool/average_write_latency` | Average write latency | `GAUGE` | `ms` | Average latency for write operations across all volumes in the volume pool.  
`volume_pool/metadata_ops_count` | Metadata operations count | `DELTA` | `{operation}` | Count of NFS metadata operations across all volumes in the volume pool.  
  
## What's next

  * Configure [GKE environment for Filestore agent volumes](https://docs.cloud.google.com/filestore/docs/use-filestore-agent-volumes-gke).
  * [Create and manage volumes using the REST API](https://docs.cloud.google.com/filestore/docs/manage-agent-volumes) for custom orchestration frameworks.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

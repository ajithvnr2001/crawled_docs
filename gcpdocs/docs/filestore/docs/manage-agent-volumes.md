---
url: https://docs.cloud.google.com/filestore/docs/manage-agent-volumes/
title: Create and manage Filestore agent volumes using the REST API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T16:20:33.329218+00:00
---

# Create and manage Filestore agent volumes using the REST API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/manage-agent-volumes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Create and manage Filestore agent volumes using the REST API Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Filestore agent volumes are available under an Allowlisted GA (AGA) program. To request access for your Google Cloud project, submit the Filestore agent volumes [access request form](https://forms.gle/vYPkcFiZVoTjf7Ah7). 

If you use Filestore agent volumes with your own orchestration platform, VM-based sandboxes, or non-Google Kubernetes Engine (GKE) container environments, you can provision and manage individual volumes inside a volume pool directly using the Filestore REST API.

**Note:** If you deploy workloads on GKE, you don't need to manually provision or manage volumes. The Filestore CSI driver and GKE orchestration automatically manage volume provisioning from your volume pool. For more information, see [Set up GKE environment for Filestore agent volumes](https://docs.cloud.google.com/filestore/docs/use-filestore-agent-volumes-gke).

## Before you begin

  1. Complete the initial project and Private Service Connect (PSC) networking setup in [Set up Filestore agent volumes](https://docs.cloud.google.com/filestore/docs/agent-volumes-prerequisites).
  2. Create a regional volume pool in [Create and manage volume pools](https://docs.cloud.google.com/filestore/docs/create-volume-pools#create-volume-pool).



## Create a volume

### REST API

To provision an individual volume inside a volume pool, send an HTTP `POST` request to the `volumes.create` endpoint:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/volumePools/VOLUME_POOL_ID/volumes?volumeId=VOLUME_ID" \
      -d '{
        "description": "Dynamic tool scratchpad for Agent Worker 12",
        "labels": {
          "agent_id": "worker-12",
          "workflow": "code_eval"
        }
      }'
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID.
  * `LOCATION`: the region containing the parent volume pool, such as `us-central1`.
  * `VOLUME_POOL_ID`: the identifier of the parent volume pool.
  * `VOLUME_ID`: the identifier for the volume, matching `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`.



Volume provisioning completes in under one to two seconds. The API returns the `Volume` resource directly. You can also specify custom volume quota (`quotaMib`) and dynamic NFS export options (`ipAcls`) during volume creation:
    
    
    {
      "name": "projects/my-project/locations/us-central1/volumePools/my-volume-pool/volumes/my-volume",
      "description": "Dynamic tool scratchpad for Agent Worker 12",
      "mountPoint": {
        "ipAddress": "10.128.0.45",
        "mountName": "my_volume"
      }
    }
    

Note the values returned inside `mountPoint`:

  * `ipAddress`: the internal IP address of the NFS mount endpoint within your VPC network.
  * `mountName`: the NFS export path component to mount.



## Mount a volume

After provisioning a volume, your orchestrator can mount the volume's NFSv3 export directly onto any client VM or container host connected to the same VPC network:

  1. Ensure that the NFS client utilities are installed on the host (for example, `nfs-common` on Debian or Ubuntu).
  2. Create a mount directory and mount the volume using the `ipAddress` and `mountName` returned in the volume's `mountPoint`:
         
         sudo mkdir -p MOUNT_DIR
         sudo mount -t nfs -o vers=3,proto=tcp,mountproto=tcp,port=2049,mountport=2050 \
             IP_ADDRESS:/MOUNT_NAME MOUNT_DIR
         

Replace the following:

     * `MOUNT_DIR`: the local directory path where the volume is mounted, such as `/workspace`.
     * `IP_ADDRESS`: the `mountPoint.ipAddress` value returned when creating or retrieving the volume.
     * `MOUNT_NAME`: the `mountPoint.mountName` value returned when creating or retrieving the volume.



## Manage volumes

### REST API

In each of the following requests, replace:

  * `PROJECT_ID`: the Google Cloud project ID.
  * `LOCATION`: the region containing the parent volume pool.
  * `VOLUME_POOL_ID`: the identifier of the parent volume pool.
  * `VOLUME_ID`: the identifier of the volume.



### Get volume details

To view details for an existing volume, including its `mountPoint` and current lifecycle `state`:
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/volumePools/VOLUME_POOL_ID/volumes/VOLUME_ID"
    

### List volumes in a pool

To list all volumes provisioned in a volume pool:
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/volumePools/VOLUME_POOL_ID/volumes"
    

### Update volume quota

To increase the storage quota for an active volume, send an HTTP `PATCH` request specifying `updateMask=quotaMib`. Volume quota can only be increased; reducing volume quota is not supported:
    
    
    curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "quotaMib": 4096
      }' \
      "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/volumePools/VOLUME_POOL_ID/volumes/VOLUME_ID?updateMask=quotaMib"
    

### Update volume IP ACLs

To restrict NFS access to a specific sandbox client IP address or update IP export rules, send an HTTP `PATCH` request specifying `updateMask=ipAcls`:
    
    
    curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "ipAcls": [
          {
            "ipRanges": ["10.128.0.50/32"],
            "accessMode": "READ_WRITE"
          }
        ]
      }' \
      "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/volumePools/VOLUME_POOL_ID/volumes/VOLUME_ID?updateMask=ipAcls"
    

### Delete a volume

When an agent session concludes or an ephemeral sandbox terminates, delete the volume to reclaim quota within the pool:
    
    
    curl -X DELETE \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/volumePools/VOLUME_POOL_ID/volumes/VOLUME_ID"
    

## Clone workspace with volume snapshot

If you already have a volume pool in a `READY` state and an existing source volume in the `HOT` state, you can create a volume snapshot to capture the point-in-time state of an agent volume so that you can clone or branch workspaces later.

**Note:** Volume snapshots are managed using the `backups` resource collection with the `sourceVolume` field.

### REST API

### Create a volume snapshot

  1. Send an HTTP `POST` request to the `backups.create` endpoint, specifying the full resource name of the volume in the `sourceVolume` field and replacing `SNAPSHOT_ID` with a unique identifier for the snapshot:
         
         curl -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           -d '{
             "sourceVolume": "projects/PROJECT_ID/locations/LOCATION/volumePools/VOLUME_POOL_ID/volumes/VOLUME_ID",
             "description": "Baseline workspace snapshot"
           }' \
           "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/backups?backupId=SNAPSHOT_ID"
         

  2. The request returns a long-running operation (LRO). Poll the operation or query the snapshot resource until its `state` is `READY` before cloning volumes from it:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/backups/SNAPSHOT_ID"
         




### Clone a volume from a snapshot

To clone a volume from a snapshot, the source snapshot must be from a volume in the same volume pool.

  1. Send an HTTP `POST` request to the `volumes:createFromSource` endpoint. Pass `ipAcls` in the request body to configure export permissions and activate the cloned volume in the `HOT` tier:
         
         curl -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           -d '{
             "backup": "projects/PROJECT_ID/locations/LOCATION/backups/SNAPSHOT_ID",
             "volumeId": "CLONED_VOLUME_ID",
             "ipAcls": [
               {
                 "ipRanges": ["10.128.0.0/24"],
                 "accessMode": "READ_WRITE",
                 "squashMode": "NO_ROOT_SQUASH"
               }
             ]
           }' \
           "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/volumePools/VOLUME_POOL_ID/volumes:createFromSource"
         

Replace the following:

     * `SNAPSHOT_ID`: the ID of the source snapshot in the same volume pool.
     * `CLONED_VOLUME_ID`: the ID for the new cloned volume.
  2. The request returns a long-running operation. Poll the operation until `done` is `true`:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID"
         

  3. After the operation completes, call `volumes.get` (or inspect the completed operation response) to retrieve the new volume's `mountPoint` (`ipAddress` and `mountName`) before mounting:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/volumePools/VOLUME_POOL_ID/volumes/CLONED_VOLUME_ID"
         




Volume cloning from snapshots completes in 3 seconds per GB or 1.5 seconds per 10,000 files.

## Tier a volume to COLD

### REST API

To tier an idle workspace to cold storage, send an HTTP `PATCH` request updating the volume state to `COLD` and clearing `ipAcls`:
    
    
    curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "state": "COLD",
        "ipAcls": []
      }' \
      "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/volumePools/VOLUME_POOL_ID/volumes/VOLUME_ID?updateMask=state,ipAcls"
    

To restore a volume from the `COLD` tier to the `HOT` tier when an agent session resumes:

  1. Call the `unfreeze` custom method, passing `ipAcls` in the request body to configure client access and activate the volume's mount point in the `HOT` tier:
         
         curl -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           -d '{
             "ipAcls": [
               {
                 "ipRanges": ["10.128.0.0/24"],
                 "accessMode": "READ_WRITE",
                 "squashMode": "NO_ROOT_SQUASH"
               }
             ]
           }' \
           "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/volumePools/VOLUME_POOL_ID/volumes/VOLUME_ID:unfreeze"
         

  2. The request returns a long-running operation. Poll the operation until `done` is `true`:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID"
         

  3. When a volume is restored from the `COLD` tier, Filestore assigns a new NFS mount endpoint from the volume pool, so `mountPoint.ipAddress` and `mountPoint.mountName` change. Retrieve the updated `mountPoint` from the completed operation response or by calling `volumes.get` before remounting the volume:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/volumePools/VOLUME_POOL_ID/volumes/VOLUME_ID"
         




## What's next

  * Manage and monitor [volume pools](https://docs.cloud.google.com/filestore/docs/create-volume-pools#monitor-volume-pools).
  * Configure [GKE environment for Filestore agent volumes](https://docs.cloud.google.com/filestore/docs/use-filestore-agent-volumes-gke).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

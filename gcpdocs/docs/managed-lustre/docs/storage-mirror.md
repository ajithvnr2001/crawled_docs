---
url: https://docs.cloud.google.com/managed-lustre/docs/storage-mirror/
title: Mirror from Cloud Storage \u00a0|\u00a0 Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T05:36:28.578685+00:00
---

# Mirror from Cloud Storage  |  Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/storage-mirror/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Mirror from Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

A Cloud Storage mirror provides an automated, event-driven synchronization service that continuously mirrors files from a [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) bucket to a Managed Lustre directory. Mirroring is supported in one direction only, from Cloud Storage to Managed Lustre.

Cloud Storage mirrors are available by request only. To indicate your interest, submit the [ Cloud Storage mirror request form](https://docs.google.com/forms/d/e/1FAIpQLScSTYd2cbjjlNzE9chIMb-5KYn_x4k4_kDWJwrdQwdfLySIQA/viewform).

For support with active Cloud Storage mirrors, contact [google-cloud-managed-lustre-support@google.com](mailto:google-cloud-managed-lustre-support@google.com). 

## Cloud Storage mirrors compared to on-demand data transfers

Managed Lustre supports two mechanisms for moving data with Cloud Storage:

Feature | Cloud Storage mirrors | On-demand data transfers  
---|---|---  
**Direction** | Cloud Storage to Managed Lustre | Cloud Storage to Managed Lustre  
  
Managed Lustre to Cloud Storage  
**Trigger** | Event-driven; syncs automatically on object create, update, and delete | Manual  
**Hierarchical namespace** | Not supported | Supported and recommended for accelerated transfer speeds  
**Rapid Storage buckets** | Not supported | Not supported  
  
For information about on-demand transfers, see [Transfer data to or from Cloud Storage](https://docs.cloud.google.com/managed-lustre/docs/transfer-data).

## How a Cloud Storage mirror works

A Cloud Storage mirror executes event-driven transfers between a Cloud Storage source and a target Managed Lustre directory. The Cloud Storage source can be a bucket or a specific object prefix within a bucket. Mirroring is performed in two phases: an initial sync when you create the mirror, followed by continuous replication of subsequent changes.

### Initial sync

When you create a Cloud Storage mirror, the service performs an initial sync to copy all existing objects from the source Cloud Storage path to the target Managed Lustre directory.

### Continuous event-driven replication

After the initial sync, the mirror service listens for bucket notifications and replicates changes.

Most objects can be replicated on the order of minutes. When an object is created or modified, the entire file is copied.

  * Creating a new object in Cloud Storage automatically creates the corresponding file in Managed Lustre.

  * Modifying an existing object in Cloud Storage overwrites the file in Managed Lustre, discarding any local modifications made in the file system.

  * Changes to custom POSIX metadata attributes on Cloud Storage objects such as UID, GID, mode, or `mtime` are updated on the corresponding Managed Lustre file.

  * Deleting an object in Cloud Storage deletes the mirrored file in Managed Lustre by default. You can change this behavior using the `--deleted-files-retained` flag. Empty parent directories remain on the file system after the last file beneath them is deleted.

  * Modifications made in Managed Lustre to mirrored files are not copied back to the source bucket. If the source object is later updated, the Managed Lustre file is overwritten with the contents of the source object, discarding any local modifications.

  * Deleting a mirrored file in Managed Lustre does not delete the corresponding object in Cloud Storage.




### Transfer speeds

The following transfer speeds apply to Cloud Storage mirrors whose buckets and instances are in the same Google Cloud region:

  * The initial sync copies existing data at up to 100 GBps for files over 32 MB, and up to 10,000 objects per second for small files.

  * Continuous replication automatically synchronizes ongoing changes, with transfer performance varying by file size:

    * Large files of 10 MB or larger transfer at up to 3.5 GBps peak throughput.
    * Small files of 4 KB or smaller transfer at up to 4,900 objects per second.



If data is written to Cloud Storage faster than the mirror can copy it, events queue in a backlog, increasing the time it takes for changes to appear in Managed Lustre. The mirror catches up automatically once the rate of change decreases.

Transfer speed is limited by:

  * An instance's maximum throughput, which is the instance capacity multiplied by [performance tier](https://docs.cloud.google.com/managed-lustre/docs/create-instance#performance-tiers).

  * Cloud Storage egress bandwidth, which is limited to 200 Gbps, or 25 GBps, per region per project. To obtain higher egress bandwidth, [request a quota increase](https://docs.cloud.google.com/storage/quotas#bandwidth).

  * Network latency for cross-region transfers. Place the source bucket and the instance in the same region for optimal performance.




### Pricing

A Cloud Storage mirror incurs standard Cloud Storage charges, which are billed to the project that contains the source bucket:

  * The initial sync performs Class A list operations and Class B read operations on the source bucket, and continuous replication performs Class B read operations, which incur Cloud Storage [operation charges](https://docs.cloud.google.com/storage/pricing#operations-pricing).
  * Mirroring data from a source bucket in a different region from your Managed Lustre instance incurs cross-region [data transfer charges](https://docs.cloud.google.com/storage/pricing#network-buckets).



## Before you begin

Creating a Cloud Storage mirror requires:

  * A Managed Lustre instance in the `ACTIVE` state.
  * An existing Cloud Storage bucket to use as the mirror source. Buckets with hierarchical namespace enabled, Rapid Storage buckets, and buckets with [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays) enabled are not supported.



## Required permissions, roles, and resources

The following IAM permissions, roles, and resources are required to create and manage Cloud Storage mirrors.

### User permissions

To create and manage mirrors, your user account or service account requires the Managed Lustre Admin role, `roles/lustre.admin`.

If you use a [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles), the role requires the following permissions:

  * `lustre.mirrors.create` to create a mirror.
  * `lustre.mirrors.get` to describe a mirror.
  * `lustre.mirrors.list` to list mirrors.
  * `lustre.mirrors.update` to update a mirror.
  * `lustre.mirrors.delete` to delete a mirror.



### Cloud Storage service agent initialization

The Cloud Storage service agent must exist in your project so that it can publish bucket notification events:
    
    
    gcloud storage service-agent --project=PROJECT_ID
    

Replace PROJECT_ID with your Google Cloud project ID.

### Managed Lustre service agent permissions

The Google-managed Managed Lustre service agent requires access to your source Cloud Storage bucket. For instructions on finding or initializing your service agent identity, see [Managed Lustre service agent](https://docs.cloud.google.com/managed-lustre/docs/access-control#service-agent).

The service agent requires the following permissions on the source Cloud Storage bucket:

  * `storage.buckets.get`
  * `storage.buckets.update`
  * `storage.objects.get`
  * `storage.objects.list`



Create a custom role containing these permissions:
    
    
    gcloud iam roles create lustreMirrorUser \
      --project=PROJECT_ID \
      --title="Lustre mirror user" \
      --permissions=storage.buckets.get,storage.buckets.update,storage.objects.get,storage.objects.list
    

Grant the custom role to the Managed Lustre service agent on the source bucket:
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
      --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-lustre.iam.gserviceaccount.com" \
      --role="projects/PROJECT_ID/roles/lustreMirrorUser"
    

Replace the following:

  * PROJECT_ID: Your Google Cloud project ID.
  * BUCKET_NAME: The name of your source Cloud Storage bucket.
  * PROJECT_NUMBER: Your Google Cloud project number.



## Create a Cloud Storage mirror

You can create one Cloud Storage mirror per Managed Lustre instance.

A Cloud Storage mirror cannot be created while an import or export operation is in progress on the instance.

**Caution:** Don't include sensitive information such as personally identifiable information or security data in your mirror name. Mirror names may be exposed to Google-internal systems outside of your project. 

###  gcloud 

Run the `mirrors create` command: 
    
    
    gcloud lustre instances mirrors create MIRROR_NAME \
      --instance=INSTANCE_ID \
      --location=LOCATION \
      --direction=from-cloud-storage \
      --gcs-path="gs://BUCKET_NAME/PREFIX/" \
      --lustre-path="/LUSTRE_DIRECTORY"
    

Where:

  * MIRROR_NAME is the name for this mirror resource. Must be 1 to 63 characters, contain only lowercase letters, numbers, and hyphens, start with a letter, and end with a letter or a number.
  * INSTANCE_ID is your Managed Lustre instance ID.
  * LOCATION is the zone of your instance. For example, `us-central1-a`.
  * `--direction` specifies the mirror direction. Must be `from-cloud-storage`.
  * `--gcs-path` is the source Cloud Storage bucket and optional object prefix. If you specify an object prefix, the path must end with a forward slash: `gs://<var>BUCKET_NAME</var>/<var>PREFIX</var>/`.
  * `--lustre-path` is the target directory on the Managed Lustre file system. Must be an absolute path starting with `/`, for example `/data` or `/data/subdir`. Defaults to the root directory, `/`. If the specified directory doesn't exist, it is created.



The following optional parameters are available:

  * `--deleted-files-retained` or `--no-deleted-files-retained`: Controls whether files deleted in Cloud Storage are retained in Managed Lustre. Default is `--no-deleted-files-retained`.
  * `--description=DESCRIPTION_TEXT`: An optional description for the mirror.



###  REST 

Send a `POST` request to the `instances.mirrors.create` method:
    
    
    POST https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/mirrors?mirrorId=MIRROR_NAME
    Authorization: Bearer YOUR_ACCESS_TOKEN
    Content-Type: application/json
    
    {
      "gcsPath": {
        "uri": "gs://BUCKET_NAME/PREFIX/"
      },
      "lustrePath": {
        "path": "/LUSTRE_DIRECTORY"
      },
      "direction": "FROM_CLOUD_STORAGE"
    }
    

Where:

  * PROJECT_ID is your Google Cloud project ID.
  * LOCATION is the zone of your Managed Lustre instance. For example, `us-central1-a`.
  * INSTANCE_ID is your instance ID.
  * MIRROR_NAME is the name for this mirror resource. Must be 1 to 63 characters, contain only lowercase letters, numbers, and hyphens, start with a letter, and end with a letter or a number.
  * `gcsPath` contains a `uri` field with the source Cloud Storage bucket and optional object prefix. If you specify an object prefix, the path must end with a forward slash: `gs://<var>BUCKET_NAME</var>/<var>PREFIX</var>/`.
  * `lustrePath` is the target directory on the Managed Lustre file system. Must be an absolute path starting with `/`, for example `/data` or `/data/subdir`. Defaults to the root directory, `/`. If the specified directory doesn't exist, it is created.
  * `direction` specifies the mirror direction. Must be `FROM_CLOUD_STORAGE`.



The request body also supports the following optional fields:

  * `deletedFilesRetained`: Set to `true` to retain files in Managed Lustre after the corresponding files are deleted from Cloud Storage. Default is `false`.
  * `description`: An optional description for the mirror.



### File attributes

When a file is copied from a Cloud Storage bucket to a Managed Lustre instance, the file attributes in the Managed Lustre instance get set in one of two ways:

  * If the Cloud Storage object has custom metadata as [described for exporting data](https://docs.cloud.google.com/managed-lustre/docs/transfer-data#export-file-attributes), then: 
    * The file's UID, GID, mode, and `mtime` are set based on the object's custom metadata.
    * The file's `atime` is set to the same value as the `mtime`.
  * If the Cloud Storage object does not have the custom metadata, then: 
    * The file's UID and GID are set to 0 (`root`).
    * The file's mode is set to `rwxr-xr-x` (`755`).
    * The file's `atime` and `mtime` are set to the creation time of the Cloud Storage object.



In either case:

  * The `ctime` for a file is set to the time the file was written to the instance.
  * The `atime`, `ctime`, and `mtime` for a directory are set to the time the directory was created on the instance.



## Manage Cloud Storage mirrors

You can list, describe, update, and delete Cloud Storage mirrors using the Google Cloud CLI tool or the REST API. To change an existing mirror's source or target path, you must delete the existing mirror and create a new one.

### List a mirror

To view a mirror configured on an instance:

###  gcloud 
    
    
    gcloud lustre instances mirrors list \
      --instance=INSTANCE_ID \
      --location=LOCATION
    

###  REST 

Send a `GET` request to the `instances.mirrors.list` method:
    
    
    GET https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/mirrors
    Authorization: Bearer YOUR_ACCESS_TOKEN
    

### Describe a mirror

To view the configuration and operational status of a mirror:

###  gcloud 
    
    
    gcloud lustre instances mirrors describe MIRROR_NAME \
      --instance=INSTANCE_ID \
      --location=LOCATION
    

###  REST 

Send a `GET` request to the `instances.mirrors.get` method:
    
    
    GET https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/mirrors/MIRROR_NAME
    Authorization: Bearer YOUR_ACCESS_TOKEN
    

### Mirror states

The `state` field returned by the `list` and `describe` commands reports where the mirror is in its lifecycle:

State | Description  
---|---  
`CREATING` | The mirror resource is being created.  
`INITIAL_SYNC` | The initial sync is copying existing objects from Cloud Storage.  
`ACTIVE` | The mirror is synchronizing changes as they occur.  
`DELETING` | The mirror is being deleted.  
  
### Update a mirror

You can update a mirror's description, labels, and whether to retain deleted files.

The Cloud Storage and Managed Lustre paths can't be changed. To point a mirror at a different path, delete the mirror and create a new one.

Updating a mirror doesn't re-run the initial sync.

###  gcloud 
    
    
    gcloud lustre instances mirrors update MIRROR_NAME \
      --instance=INSTANCE_ID \
      --location=LOCATION \
      --description="DESCRIPTION_TEXT"
    

###  REST 

Send a `PATCH` request to the `instances.mirrors.patch` method with an `updateMask` query parameter:
    
    
    PATCH https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/mirrors/MIRROR_NAME?updateMask=description
    Authorization: Bearer YOUR_ACCESS_TOKEN
    Content-Type: application/json
    
    {
      "description": "DESCRIPTION_TEXT"
    }
    

### Delete a mirror

To delete a mirror:

###  gcloud 
    
    
    gcloud lustre instances mirrors delete MIRROR_NAME \
      --instance=INSTANCE_ID \
      --location=LOCATION
    

###  REST 

Send a `DELETE` request to the `instances.mirrors.delete` method:
    
    
    DELETE https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/mirrors/MIRROR_NAME
    Authorization: Bearer YOUR_ACCESS_TOKEN
    

Deleting a mirror stops future synchronization between Cloud Storage and Managed Lustre. Files that were already copied to Managed Lustre are not deleted when the mirror is removed.

File transfers that are in progress when a mirror is deleted are aborted. Incomplete transfers may leave temporary files with the name format `FILENAME.cloud_transfer.UUID.NUMBER.tmp` in the mirror directory after the mirror is deleted. You can delete these files.

## View logs

Mirror logs identify individual files that failed to synchronize.

Logs are routed to [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) against the `lustre.googleapis.com/Instance` resource, under the `mirror` log name.

**Caution:** Mirror error logs include file names and relative file path metadata for objects that fail to synchronize between Managed Lustre and Cloud Storage. Avoid including sensitive information such as personally identifiable information or security data in file and directory names. 

To view logs for mirror operations:

  1. Go to the [Logs Explorer](https://console.cloud.google.com/logs/viewer).
  2. Enter the following query:
         
         resource.type="lustre.googleapis.com/Instance"
         logName="projects/PROJECT_ID/logs/lustre.googleapis.com%2Fmirror"
         resource.labels.instance_id="INSTANCE_ID"
         




## Troubleshooting

### `PERMISSION_DENIED` errors on the source bucket

If the mirror creation fails with a `PERMISSION_DENIED` error, files are not synchronizing, or there are logs showing "PERMISSION_DENIED" errors:

  1. Verify that the Cloud Storage service agent was initialized:
         
         gcloud storage service-agent --project=PROJECT_ID
         

  2. Confirm that the Managed Lustre service agent has been granted the required permissions on the source bucket. See Grant service agent permissions for details.




### Changes in Cloud Storage are not replicating to Managed Lustre

If the mirror state is `ACTIVE` but new or modified objects in Cloud Storage are not appearing in Managed Lustre, confirm that the bucket notification configuration exists on your source bucket.

  1. List the bucket notifications:
         
         gcloud storage buckets notifications list --bucket=BUCKET_NAME
         

  2. If the output is empty, you must delete the existing mirror and create a new one:
         
         gcloud lustre instances mirrors delete MIRROR_NAME \
           --instance=INSTANCE_ID \
           --location=LOCATION
         

After the deletion finishes, create a new mirror.




### Naming conflict errors

If you notice files missing in Managed Lustre after adding them to Cloud Storage, check Cloud Logging for naming conflict errors:

  * If an object created in Cloud Storage has the same name as an existing directory in Managed Lustre, the transfer fails with a `file exists` error and the existing directory is not overwritten. The failed transfer leaves a temporary file with the name format `FILENAME.cloud_transfer.UUID.NUMBER.tmp` in the parent directory.
  * If an object created in Cloud Storage contains a path prefix that matches an existing regular file in Managed Lustre, the transfer fails with a `not a directory` error and the existing file is not overwritten. For example, if `models` is an existing file in Managed Lustre, transferring an object named `models/weights.bin` from Cloud Storage fails because the directory `models/` cannot be created.



To resolve these conflicts, rename or delete the conflicting directory or file in Managed Lustre, remove any leftover `.tmp` files, and re-upload the object in Cloud Storage to trigger synchronization.

### `ABORTED: unable to queue the operation`

If you receive an `ABORTED: unable to queue the operation` error when creating a mirror or initiating an on-demand transfer job:

  * Ensure that no existing `import-data` or `export-data` operations are running on the instance before creating a mirror.
  * Wait until the mirror creation and initial sync complete before attempting other administrative data operations on the instance.



### `FILESYSTEM_NO_SPACE_ON_DEVICE`

If mirroring halts and the logs indicate space errors, your Managed Lustre file system might be out of inodes or disk capacity. You can delete unnecessary files to free up space, or [increase storage capacity](https://docs.cloud.google.com/managed-lustre/docs/increase-capacity) to expand your file system.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 

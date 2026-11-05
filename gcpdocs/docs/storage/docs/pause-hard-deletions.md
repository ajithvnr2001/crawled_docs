---
url: https://docs.cloud.google.com/storage/docs/pause-hard-deletions/
title: Pause permanent (hard) deletions of soft-deleted objects \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T22:27:31.753955+00:00
---

# Pause permanent (hard) deletions of soft-deleted objects  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/pause-hard-deletions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Pause permanent (hard) deletions of soft-deleted objects Stay organized with collections  Save and categorize content based on your preferences. 

If you need more time to restore soft-deleted objects before they're permanently deleted, you can pause permanent deletions (also called hard deletions) of soft-deleted objects in a Cloud Storage bucket.

By default, [soft-deleted objects and buckets](https://docs.cloud.google.com/storage/docs/soft-delete) are permanently deleted when they reach their soft delete retention duration. When you pause hard deletions for a bucket, soft-deleted objects are instead retained in a soft-deleted state indefinitely, regardless of their soft delete retention durations. Soft-deleted objects are only permanently deleted after you resume hard deletions for the bucket.

**Caution:** When hard deletions are paused, storage costs can significantly increase because soft-deleted objects continue to accrue storage charges. We recommend that you resume hard deletions after you finish restoring your data so that soft-deleted objects can be permanently deleted according to their retention durations.

## Use cases

Pausing hard deletions gives you extra time to perform very large or complicated object restorations that otherwise might take more time to resolve than the soft delete retention duration. For example:

  * **Recovering very large buckets containing billions of objects.** If a bucket contains a very large number of objects, it might take longer than the retention duration to recover all objects in the bucket, especially if you detect the deletion after part of the retention period has already passed. Pausing hard deletions can help you recover from an unexpected mass deletion incident, without having to set a longer retention duration for day-to-day operations.
  * **Unclear scope of deletions.** If you aren't sure which objects were incorrectly deleted, it might take time to investigate. Pausing hard deletions can give you more time to figure out what needs to be restored.
  * **Complex recoveries.** For complex restorations, there might be time to detect and perform a bulk recovery within the retention duration. If that doesn't yield the expected results, pausing hard deletions can give you more time to validate that you are satisfied with your state of recovery.



## Recommended workflow

We recommend the following workflow to temporarily pause hard deletions for a bucket:

  1. When you detect a mass deletion incident that might take more time to resolve than the soft delete retention duration, then pause hard deletions for the affected bucket.

  2. [Restore the bucket](https://docs.cloud.google.com/storage/docs/use-soft-deleted-buckets) if necessary, and [restore the objects](https://docs.cloud.google.com/storage/docs/use-soft-deleted-objects) in the bucket.

  3. After you complete the recovery and validate that your data was successfully restored, then resume hard deletions for the bucket.




## Considerations

  * You can pause hard deletions for a bucket by updating an existing bucket that has soft delete enabled. Hard deletions can't be paused during bucket creation or for buckets that don't have soft delete enabled.
  * When you resume hard deletions for a bucket, Cloud Storage resumes permanent deletions of all soft-deleted objects in the bucket based on their soft delete retention durations. If any objects have passed their retention duration, they're permanently deleted when you resume hard deletions.
  * Pausing hard deletions takes effect immediately. It might take a few seconds for cached API operations to return updated information.
  * You can continue to delete objects in a bucket when hard deletions are paused. Deleted objects become soft-deleted.
  * You can pause and resume hard deletions on a bucket a maximum of once every 24 hours.
  * You can update the soft delete retention duration while hard deletions are paused. However, you can't disable soft delete while hard deletions are paused.
  * A bucket can't be deleted while hard deletions are paused.



## Required roles

To get the permissions that you need to pause or resume hard deletions, ask your administrator to grant you the [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) IAM role on the bucket or the project that contains the bucket. 

This predefined role contains the permissions required to pause or resume hard deletions. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to pause or resume hard deletions:

  * `storage.buckets.update`
  * If you use the Google Cloud console to do the tasks on this page: 
    * `storage.buckets.get`
    * `storage.buckets.list`



For information about granting roles, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions) or [Manage access to projects](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Pause hard deletions

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
           "softDeletePolicy": {
             "hardDeletePause": {
               "enabled": true
             }
           }
         }

  3. To pause hard deletions for a bucket, use `cURL` to call the JSON API with a [`PATCH` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/patch) request:
         
         curl -X PATCH --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME"

Replace the following:

     * `JSON_FILE_NAME`: the path to the JSON file that you created in the previous step.
     * `BUCKET_NAME`: the name of the bucket. For example, `my-bucket`.



## Resume hard deletions

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
           "softDeletePolicy": {
             "hardDeletePause": {
               "enabled": false
             }
           }
         }

  3. To resume hard deletions for a bucket, use `cURL` to call the JSON API with a [`PATCH` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/patch) request:
         
         curl -X PATCH --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME"

Replace the following:

     * `JSON_FILE_NAME`: the path to the JSON file that you created in the previous step.
     * `BUCKET_NAME`: the name of the bucket. For example, `my-bucket`.



## Check whether hard deletions are paused for a bucket

A bucket's soft delete policy provides information about whether hard deletions are paused. For steps to retrieve a bucket's soft delete policy, see [Check whether soft delete is enabled on a bucket](https://docs.cloud.google.com/storage/docs/use-soft-delete#check-soft-delete-policy).

## What's next

  * Learn how to [restore soft-deleted objects](https://docs.cloud.google.com/storage/docs/use-soft-deleted-objects).
  * Learn how to [restore soft-deleted buckets](https://docs.cloud.google.com/storage/docs/use-soft-deleted-buckets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 

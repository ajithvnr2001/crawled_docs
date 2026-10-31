---
url: https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/re-encrypt-objects-default-cmek-policies/
title: Re-encrypt objects that violate default CMEK bucket policies \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:08.453470+00:00
---

# Re-encrypt objects that violate default CMEK bucket policies  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/re-encrypt-objects-default-cmek-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Re-encrypt objects that violate default CMEK bucket policies Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to use Storage Intelligence advisor to identify and re-encrypt objects that violate a bucket's default customer-managed encryption key (CMEK) policy.

When you [set a default Cloud KMS key](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys#set-default-key) on a bucket, Cloud Storage encrypts new objects with that key unless your upload request specifies a different key. However, Cloud Storage doesn't automatically re-encrypt existing objects that you uploaded before setting the default key. Those objects remain encrypted with their original encryption method. For more information about available encryption methods, see [Data encryption options](https://docs.cloud.google.com/storage/docs/encryption).

Storage Intelligence advisor displays the **Objects violate default CMEK bucket policies** finding when a bucket with a default Cloud Key Management Service (Cloud KMS) key contains objects that aren't encrypted with CMEK. A _finding_ is an anomaly or security configuration gap detected from your metrics and object metadata that needs your attention. For an overview of Storage Intelligence advisor, see [About Storage Intelligence advisor](https://docs.cloud.google.com/storage/docs/storage-intelligence/advisor-overview). For a full list of findings, see [Findings reference catalog](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/findings-reference-catalog).

## Thresholds that trigger a finding

When you enable Storage Intelligence, Cloud Storage automatically evaluates bucket-level and object-level encryption metadata across your project, folder, or organization. Storage Intelligence advisor generates a finding when a bucket meets both of the following criteria:

  * The bucket has a default Cloud KMS key, which means that the [`encryption.defaultKmsKeyName`](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#defaultKmsKeyName) field is set and the [`encryption.defaultEncryptionType`](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#defaultEncryptionType) field is `CMEK`.
  * The bucket contains at least one object where the [`encryptionType`](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#encryptionType) metadata field isn't `CMEK`, such as `GMEK` or `CSEK`.



Initial baseline findings appear within 48 hours after you enable Storage Intelligence and refresh every 24 hours. To reduce alert volume, Storage Intelligence advisor aggregates object-level violations by bucket on your dashboard. You can query object-level encryption metadata in [Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets).

## Respond to a finding

To respond to the finding, identify the affected objects in each bucket and re-encrypt them with the bucket's default Cloud KMS key:

  1. [View the finding details](https://docs.cloud.google.com/storage/docs/storage-intelligence/view-advisor#view-finding-details) to identify the affected buckets and copy the resource name of each bucket's **Default KMS key**.

  2. Optional: To view the list of objects in the bucket that aren't encrypted with CMEK, query your [Storage Insights dataset](https://docs.cloud.google.com/storage/docs/insights/datasets) in BigQuery. If you haven't configured a linked dataset, see [Configure Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/configure-datasets).
         
         SELECT
           bucket,
           name,
           encryptionType
         FROM
           `DATASET_NAME.object_attributes_latest_snapshot_view`
         WHERE
           bucket = 'BUCKET_NAME'
           AND encryptionType != 'CMEK'
           AND timeDeleted IS NULL
           AND softDeleteTime IS NULL;

Replace the following:

     * `DATASET_NAME`: the name of your Storage Insights linked dataset in BigQuery.
     * `BUCKET_NAME`: the name of the affected bucket.
**Note:** Querying and exporting data in BigQuery incurs costs. For more information, see [BigQuery pricing](https://docs.cloud.google.com/bigquery/pricing).
  3. Use the following table to select the re-encryption method for your live objects:

Scenario | Recommended action | Details  
---|---|---  
Affected live objects use standard encryption (`GMEK`) | Re-encrypt GMEK-encrypted objects at scale by using Storage batch operations | Export CSV manifest files of affected live `GMEK` objects from BigQuery and run a [Storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview) job to rewrite the objects with the bucket's default Cloud KMS key.  
Affected live objects use customer-supplied encryption keys (`CSEK`) | Re-encrypt CSEK-encrypted objects by using the Google Cloud CLI | Because Google Cloud doesn't store customer-supplied encryption keys (`CSEK`), Storage batch operations can't decrypt CSEK-encrypted objects. Use the [`gcloud storage objects update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/update) command to rewrite CSEK-encrypted objects with the bucket's default Cloud KMS key.  
  
After you re-encrypt all non-compliant objects in a bucket, the finding clears for that bucket during the next 24-hour refresh cycle. However, the finding remains active in the following cases until you or Cloud Storage permanently deletes the retained object versions:

     * **[Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning)** : When you rewrite a live object, Cloud Storage retains the original non-compliant object as a noncurrent version. To clear the finding, [delete the noncurrent object versions](https://docs.cloud.google.com/storage/docs/using-versioned-objects#delete) or configure an [Object Lifecycle Management `Delete` rule](https://docs.cloud.google.com/storage/docs/lifecycle#delete).
     * **[Soft delete](https://docs.cloud.google.com/storage/docs/soft-delete)** : When you rewrite or delete an object, Cloud Storage retains the original non-compliant version in a soft-deleted state until the bucket's [soft delete retention duration](https://docs.cloud.google.com/storage/docs/soft-delete#retention-duration) expires.



### Re-encrypt GMEK-encrypted objects at scale by using Storage batch operations

To re-encrypt live `GMEK` objects at scale, export CSV manifest files from BigQuery and run a Storage batch operations job:

  1. Run the following `EXPORT DATA` query in BigQuery to [create a CSV manifest by using Storage Insights datasets](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs#export-manifest-re-encrypt-cmek):
         
         EXPORT DATA OPTIONS(
           uri='gs://DESTINATION_BUCKET/manifests/objects_violating_default_policies_*.csv',
           format='CSV',
           overwrite=true,
           header=true
         ) AS
         SELECT
           bucket,
           name
         FROM
           `DATASET_NAME.object_attributes_latest_snapshot_view`
         WHERE
           bucket = 'BUCKET_NAME'
           AND encryptionType = 'GMEK'
           AND timeDeleted IS NULL
           AND softDeleteTime IS NULL;

Replace the following:

     * `DESTINATION_BUCKET`: the name of the Cloud Storage bucket where you want to store the exported CSV manifest files.
     * `DATASET_NAME`: the name of your Storage Insights linked dataset in BigQuery.
     * `BUCKET_NAME`: the name of the affected bucket.
  2. Complete the [Storage batch operations prerequisites](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs#before-you-begin), and ask your administrator to grant the [Cloud KMS CryptoKey Encrypter/Decrypter role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) on the bucket's default Cloud KMS key to both of the following service agents:

     * The Storage batch operations service agent (`service-PROJECT_NUMBER@gcp-sa-storagebatchoperations.iam.gserviceaccount.com`)
     * The Cloud Storage service agent (`service-PROJECT_NUMBER@gs-project-accounts.iam.gserviceaccount.com`)

Replace `PROJECT_NUMBER` with the project number of the project that contains the bucket.

  3. Run the [`gcloud storage batch-operations jobs create`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/create) command to [create a Storage batch operations job by using the manifest file](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs#create-batch-operation-job-using-manifest) and re-encrypt the objects with the bucket's default Cloud KMS key. To verify the job configuration before modifying objects, include the `--dry-run` flag:
         
         gcloud storage batch-operations jobs create JOB_NAME \
           --bucket="BUCKET_NAME" \
           --manifest-location="gs://DESTINATION_BUCKET/manifests/objects_violating_default_policies_*.csv" \
           --rewrite-object="kms-key=DEFAULT_KMS_KEY"

Replace the following:

     * `JOB_NAME`: a unique ID for the batch job, such as `update-encryption-to-cmek-job`.
     * `BUCKET_NAME`: the name of the affected bucket.
     * `DESTINATION_BUCKET`: the name of the bucket that contains your exported manifest files.
     * `DEFAULT_KMS_KEY`: the resource name of the bucket's default Cloud KMS key, in the format `projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/CRYPTO_KEY`.



### Re-encrypt CSEK-encrypted objects by using the Google Cloud CLI

Because Google Cloud doesn't store customer-supplied encryption keys (`CSEK`), Storage batch operations can't decrypt CSEK-encrypted objects. To re-encrypt CSEK-encrypted objects with the bucket's default Cloud KMS key, run the [`gcloud storage objects update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/update) command with both the `--decryption-keys` and `--encryption-key` flags:
    
    
    gcloud storage objects update gs://BUCKET_NAME/OBJECT_NAME \
      --decryption-keys=DECRYPTION_KEY \
      --encryption-key=DEFAULT_KMS_KEY

Replace the following:

  * `BUCKET_NAME`: the name of the affected bucket.
  * `OBJECT_NAME`: the name of the CSEK-encrypted object that you want to re-encrypt. To update multiple objects in a single command, use [URI wildcards](https://docs.cloud.google.com/storage/docs/wildcards) or the [`--read-paths-from-stdin` (`-I`)](https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/update#--read-paths-from-stdin) flag.
  * `DECRYPTION_KEY`: the RFC 4648 base64-encoded AES-256 key that encrypts the object.
  * `DEFAULT_KMS_KEY`: the resource name of the bucket's default Cloud KMS key, in the format `projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/CRYPTO_KEY`.



## What's next

  * **Key tasks** : 
    * [View Storage Intelligence advisor](https://docs.cloud.google.com/storage/docs/storage-intelligence/view-advisor#view-finding-details)
  * **Explore other findings** : 
    * [Re-encrypt objects that violate enforced encryption rules](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/re-encrypt-objects-enforced-encryption-rules)
    * [Optimize usage for Coldline and Archive storage data](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/optimize-coldline-archive-class-costs)
    * [Improve performance by mitigating rate limited request errors](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/improve-performance-by-mitigating-429-errors)
    * [Identify above trend storage consumption](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/identify-storage-consumption)
    * [Manage cross-region egress](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/manage-egress)
    * [Review the findings reference catalog](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/findings-reference-catalog)
  * **Related concepts** : 
    * [Storage Intelligence advisor overview](https://docs.cloud.google.com/storage/docs/storage-intelligence/advisor-overview)
    * [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys)
    * [About Storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 

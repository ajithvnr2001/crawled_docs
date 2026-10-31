---
url: https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/re-encrypt-objects-enforced-encryption-rules/
title: Re-encrypt objects that violate enforced encryption rules \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:07.194963+00:00
---

# Re-encrypt objects that violate enforced encryption rules  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/re-encrypt-objects-enforced-encryption-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Re-encrypt objects that violate enforced encryption rules Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to use Storage Intelligence advisor to identify and re-encrypt objects that violate the encryption enforcement configuration on their bucket.

When you [enforce or restrict the encryption types for a bucket](https://docs.cloud.google.com/storage/docs/encryption/enforce-encryption-types), Cloud Storage enforces that configuration for all new or rewritten objects in the bucket. However, Cloud Storage doesn't automatically re-encrypt existing objects that you uploaded before the configuration took effect. Those objects remain encrypted with their original encryption method. For more information about available encryption methods, see [Data encryption options](https://docs.cloud.google.com/storage/docs/encryption).

Storage Intelligence advisor displays the **Objects violate enforced encryption rules** finding when a bucket contains objects that use a restricted encryption method. A _finding_ is an anomaly or security configuration gap detected from your metrics and object metadata that needs your attention. For an overview of Storage Intelligence advisor, see [About Storage Intelligence advisor](https://docs.cloud.google.com/storage/docs/storage-intelligence/advisor-overview). For a full list of findings, see [Findings reference catalog](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/findings-reference-catalog).

## Thresholds that trigger a finding

When you enable Storage Intelligence, Cloud Storage automatically evaluates object-level encryption metadata against bucket-level encryption enforcement configurations across your project, folder, or organization. Storage Intelligence advisor generates a finding when a bucket meets both of the following criteria:

  * The bucket restricts one or more encryption methods in its [`enforcedEncryptionAllowedTypes`](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#enforcedEncryptionAllowedTypes) configuration, such as standard encryption (Google default encryption, or `GMEK`), customer-managed encryption keys (`CMEK`), or customer-supplied encryption keys (`CSEK`).
  * The bucket contains at least one object where the [`encryptionType`](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#encryptionType) metadata field isn't in the bucket's `enforcedEncryptionAllowedTypes` list.



Initial baseline findings appear within 48 hours after you enable Storage Intelligence and refresh every 24 hours. To reduce alert volume, Storage Intelligence advisor aggregates object-level violations by bucket on your dashboard. You can query object-level encryption metadata in [Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets).

## Respond to a finding

To respond to the finding, identify the affected objects in each bucket and rewrite the non-compliant objects with an allowed encryption method:

  1. [View the finding details](https://docs.cloud.google.com/storage/docs/storage-intelligence/view-advisor#view-finding-details) to identify the affected buckets and their allowed encryption types (`CMEK`, `GMEK`, or `CSEK`).

  2. Optional: To list the objects in an affected bucket that violate the enforced encryption configuration, query your [Storage Insights dataset](https://docs.cloud.google.com/storage/docs/insights/datasets) in BigQuery. If you haven't configured a linked dataset, see [Configure Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/configure-datasets).
         
         SELECT
           bucket,
           name,
           encryptionType
         FROM
           `DATASET_NAME.object_attributes_latest_snapshot_view`
         WHERE
           bucket = 'BUCKET_NAME'
           AND encryptionType NOT IN (ALLOWED_ENCRYPTION_TYPES)
           AND timeDeleted IS NULL
           AND softDeleteTime IS NULL;

Replace the following:

     * `DATASET_NAME`: the name of your Storage Insights linked dataset in BigQuery.
     * `BUCKET_NAME`: the name of the affected bucket.
     * `ALLOWED_ENCRYPTION_TYPES`: a comma-separated list of the encryption types that the bucket allows, such as `'CMEK'` or `'CMEK', 'GMEK'`.
**Note:** Querying and exporting data in BigQuery incurs costs. For more information, see [BigQuery pricing](https://docs.cloud.google.com/bigquery/pricing).
  3. Use the following table to select the re-encryption method for your live objects:

Scenario | Recommended action | Details  
---|---|---  
Bucket allows customer-managed encryption keys (`CMEK`) | Re-encrypt objects with CMEK | For live `GMEK` objects, export CSV manifest files from BigQuery and run a [Storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview) job to rewrite the objects with a Cloud KMS key. For CSEK-encrypted objects, run the [`gcloud storage objects update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/update) command.  
Bucket allows standard encryption (`GMEK`) | Re-encrypt objects with standard encryption (GMEK) | Verify that the bucket doesn't have a default Cloud KMS key, and then use the [`gcloud storage objects update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/update) command with the `--clear-encryption-key` flag to rewrite affected objects with standard encryption.  
Bucket allows only customer-supplied encryption keys (`CSEK`) | Re-encrypt objects with CSEK | Use the [`gcloud storage objects update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/update) command with the `--encryption-key` flag to rewrite affected objects with your AES-256 encryption key.  
  
After you re-encrypt all non-compliant objects in a bucket, the finding clears for that bucket during the next 24-hour refresh cycle. However, the finding remains active in the following cases until you or Cloud Storage permanently deletes the retained object versions:

     * **[Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning)** : When you rewrite a live object, Cloud Storage retains the original non-compliant object as a noncurrent version. To clear the finding, [delete the noncurrent object versions](https://docs.cloud.google.com/storage/docs/using-versioned-objects#delete) or configure an [Object Lifecycle Management `Delete` rule](https://docs.cloud.google.com/storage/docs/lifecycle#delete).
     * **[Soft delete](https://docs.cloud.google.com/storage/docs/soft-delete)** : When you rewrite or delete an object, Cloud Storage retains the original non-compliant version in a soft-deleted state until the bucket's [soft delete retention duration](https://docs.cloud.google.com/storage/docs/soft-delete#retention-duration) expires.



### Re-encrypt objects with CMEK

If the bucket allows customer-managed encryption keys (`CMEK`), re-encrypt the affected objects based on their current encryption method.

#### Re-encrypt GMEK-encrypted objects at scale by using Storage batch operations

To re-encrypt GMEK-encrypted objects with CMEK at scale, export CSV manifest files from BigQuery and run a Storage batch operations job:

  1. Run the following `EXPORT DATA` query in BigQuery to [create a CSV manifest by using Storage Insights datasets](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs#export-manifest-re-encrypt-cmek) for affected live objects that use standard encryption (`GMEK`):
         
         EXPORT DATA OPTIONS(
           uri='gs://DESTINATION_BUCKET/manifests/objects_violating_enforced_policies_*.csv',
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
  2. Complete the [Storage batch operations prerequisites](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs#before-you-begin), and ask your administrator to grant the [Cloud KMS CryptoKey Encrypter/Decrypter role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) on the Cloud KMS key to both of the following service agents:

     * The Storage batch operations service agent (`service-PROJECT_NUMBER@gcp-sa-storagebatchoperations.iam.gserviceaccount.com`)
     * The Cloud Storage service agent (`service-PROJECT_NUMBER@gs-project-accounts.iam.gserviceaccount.com`)

Replace `PROJECT_NUMBER` with the project number of the project that contains the bucket.

  3. Run the [`gcloud storage batch-operations jobs create`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/create) command to [create a Storage batch operations job by using the manifest file](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs#create-batch-operation-job-using-manifest) and rewrite the objects with your Cloud KMS key. To verify the job configuration before modifying objects, include the `--dry-run` flag:
         
         gcloud storage batch-operations jobs create JOB_NAME \
           --bucket="BUCKET_NAME" \
           --manifest-location="gs://DESTINATION_BUCKET/manifests/objects_violating_enforced_policies_*.csv" \
           --rewrite-object="kms-key=KMS_KEY"

Replace the following:

     * `JOB_NAME`: a unique ID for the batch job, such as `re-encrypt-objects-job`.
     * `BUCKET_NAME`: the name of the affected bucket.
     * `DESTINATION_BUCKET`: the name of the bucket that contains your exported manifest files.
     * `KMS_KEY`: the resource name of the Cloud KMS key that you want to use to encrypt the objects. The key must be in the same location as the bucket and use the format `projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/CRYPTO_KEY`.



#### Re-encrypt CSEK-encrypted objects by using the Google Cloud CLI

Because Google Cloud doesn't store customer-supplied encryption keys (`CSEK`), Storage batch operations can't decrypt CSEK-encrypted objects. To re-encrypt CSEK-encrypted objects with CMEK, run the [`gcloud storage objects update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/update) command with both the `--decryption-keys` and `--encryption-key` flags:
    
    
    gcloud storage objects update gs://BUCKET_NAME/OBJECT_NAME \
      --decryption-keys=DECRYPTION_KEY \
      --encryption-key=KMS_KEY

Replace the following:

  * `BUCKET_NAME`: the name of the affected bucket.
  * `OBJECT_NAME`: the name of the CSEK-encrypted object that you want to re-encrypt. To update multiple objects in a single command, use [URI wildcards](https://docs.cloud.google.com/storage/docs/wildcards) or the [`--read-paths-from-stdin` (`-I`)](https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/update#--read-paths-from-stdin) flag.
  * `DECRYPTION_KEY`: the RFC 4648 base64-encoded AES-256 key that encrypts the object.
  * `KMS_KEY`: the resource name of the Cloud KMS key that you want to use to encrypt the object, in the format `projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/CRYPTO_KEY`.



### Re-encrypt objects with standard encryption (GMEK)

To re-encrypt objects with standard encryption (Google default encryption, or `GMEK`), verify that the bucket doesn't have a default Cloud KMS key and clear the custom encryption key on each affected object:

  1. Verify that the bucket doesn't have a default Cloud KMS key. When you clear an object's custom encryption key, Cloud Storage encrypts the object with standard encryption (`GMEK`) only if the bucket has no default Cloud KMS key. If the bucket has a default Cloud KMS key, Cloud Storage encrypts the object with that key instead. If the bucket also restricts CMEK, the rewrite fails.

To remove a default Cloud KMS key from the bucket, run the [`gcloud storage buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/update) command with the `--clear-default-encryption-key` flag:
         
         gcloud storage buckets update gs://BUCKET_NAME \
           --clear-default-encryption-key

Replace `BUCKET_NAME` with the name of the affected bucket.

  2. Use the [`gcloud storage objects update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/update) command with the `--clear-encryption-key` flag to rewrite the affected objects with standard encryption. If the objects are encrypted with customer-supplied encryption keys (`CSEK`), also include the `--decryption-keys` flag:
         
         gcloud storage objects update gs://BUCKET_NAME/OBJECT_NAME \
           --clear-encryption-key \
           [--decryption-keys=DECRYPTION_KEY]

Replace the following:

     * `BUCKET_NAME`: the name of the affected bucket.
     * `OBJECT_NAME`: the name of the object that you want to re-encrypt. To update multiple objects in a single command, use [URI wildcards](https://docs.cloud.google.com/storage/docs/wildcards) (such as `gs://BUCKET_NAME/**`) or the [`--read-paths-from-stdin` (`-I`)](https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/update#--read-paths-from-stdin) flag.
     * `DECRYPTION_KEY`: if the object is encrypted with `CSEK`, the RFC 4648 base64-encoded AES-256 key that encrypts the object. If the object is encrypted with `CMEK`, omit the `--decryption-keys` flag.



### Re-encrypt objects with CSEK

**Note:** If the bucket allows CMEK or standard encryption (GMEK), we recommend that you re-encrypt objects with CMEK or standard encryption instead of customer-supplied encryption keys (CSEK).

If the bucket allows only customer-supplied encryption keys (CSEK), use the [`gcloud storage objects update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/update) command with the `--encryption-key` flag to rewrite the affected objects with your AES-256 encryption key. If an object is encrypted with a different `CSEK`, also include the `--decryption-keys` flag:
    
    
    gcloud storage objects update gs://BUCKET_NAME/OBJECT_NAME \
      --encryption-key=YOUR_ENCRYPTION_KEY \
      [--decryption-keys=DECRYPTION_KEY]

Replace the following:

  * `BUCKET_NAME`: the name of the affected bucket.
  * `OBJECT_NAME`: the name of the object that you want to re-encrypt. To update multiple objects in a single command, use [URI wildcards](https://docs.cloud.google.com/storage/docs/wildcards) or the [`--read-paths-from-stdin` (`-I`)](https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/update#--read-paths-from-stdin) flag.
  * `YOUR_ENCRYPTION_KEY`: your RFC 4648 base64-encoded AES-256 encryption key string.
  * `DECRYPTION_KEY`: if the object is encrypted with a different `CSEK`, the RFC 4648 base64-encoded AES-256 key that encrypts the object. If the object is encrypted with `GMEK` or `CMEK`, omit the `--decryption-keys` flag.



## What's next

  * **Key tasks** : 
    * [View Storage Intelligence advisor](https://docs.cloud.google.com/storage/docs/storage-intelligence/view-advisor#view-finding-details)
  * **Explore other findings** : 
    * [Re-encrypt objects that violate default CMEK bucket policies](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/re-encrypt-objects-default-cmek-policies)
    * [Optimize usage for Coldline and Archive storage data](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/optimize-coldline-archive-class-costs)
    * [Improve performance by mitigating rate limited request errors](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/improve-performance-by-mitigating-429-errors)
    * [Identify above trend storage consumption](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/identify-storage-consumption)
    * [Manage cross-region egress](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/manage-egress)
    * [Review the findings reference catalog](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/findings-reference-catalog)
  * **Related concepts** : 
    * [Storage Intelligence advisor overview](https://docs.cloud.google.com/storage/docs/storage-intelligence/advisor-overview)
    * [Enforce or restrict the encryption types for a bucket](https://docs.cloud.google.com/storage/docs/encryption/enforce-encryption-types)
    * [Data encryption options](https://docs.cloud.google.com/storage/docs/encryption)
    * [About Storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 

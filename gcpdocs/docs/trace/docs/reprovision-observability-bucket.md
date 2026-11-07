---
url: https://docs.cloud.google.com/trace/docs/reprovision-observability-bucket/
title: Remediate data residency and CMEK requirements \u00a0|\u00a0 Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-07T05:38:47.810314+00:00
---

# Remediate data residency and CMEK requirements  |  Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/reprovision-observability-bucket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  Remediate data residency and CMEK requirements Stay organized with collections  Save and categorize content based on your preferences. 

You can reprovision an observability bucket to satisfy data residency and encryption regulatory requirements. After reprovisioning, the storage location and encryption configuration of the `_Trace` bucket matches your default settings for observability buckets.

To reprovision a bucket, configure your default settings and then call the reprovision method. The reprovision operation can do any of the following:

  * Retroactively apply a Cloud Key Management Service key to an observability bucket without changing its storage location.
  * Change the storage location of an observability bucket and use Google-default encryption.
  * Change the storage location of an observability bucket and use a Cloud KMS key to encrypt the stored data.



Don't reprovision an observability bucket when you want to change its display name, description, or Cloud KMS key. For those cases, [update the observability bucket](https://docs.cloud.google.com/trace/docs/update-observability-buckets).

**Caution:** Datasets for reprovisioned observability buckets won't contain any data that was sent to your project before the reprovision command was issued. A reprovision command permanently deletes stored data. You can't recover deleted data.

## How reprovisioning works

When you initiate a reprovisioning operation, the system performs the following steps:

  1. The system determines whether the observability bucket is eligible for reprovisioning. An observability bucket is eligible when all of the following checks pass:

     * The observability bucket is named `_Trace`.
     * The bucket hasn't been reprovisioned.
     * The [default settings for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets) are found.
     * To be in agreement with the default settings, the location of the observability bucket needs to change or the encryption must change from Google-default encryption to CMEK.
  2. The system updates the bucket configuration. This process takes four to five hours.




## Limitations

The following limitations apply:

  * The system allows at most one reprovision operation per observability bucket. Subsequent requests fail with a `FAILED_PRECONDITION` error.

  * You can only reprovision buckets named `_Trace`.

  * You can't access any data that was stored before the reprovisioning was initiated. This data was deleted and isn't recoverable.

  * If the bucket's location changes, then links and linked BigQuery datasets are deleted. You must recreate any links.

  * If the bucket's location changes, then you must manually update existing analytics views.

  * You can't cancel or undo a reprovision operation. Attempts to cancel the operation are ignored.

  * The behavior of queries during a reprovision operation is undefined.

**Note:** We don't recommend that you use the Trace Explorer or Observability Analytics pages during a reprovision operation. Defer usage until the operation completes.



## Auditing

To determine the reprovisioning history of an observability bucket, you can use your audit logs. Admin Activity logs record who made a reprovisioning request, the affected observability bucket, and the initial response.

To find these records, apply the following filters in the Logs Explorer:
    
    
    logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity" AND
    resource.type="audited_resource" AND
    resource.labels.service="observability.googleapis.com" AND
    resource.labels.method="google.cloud.observability.v1.Observability.ReprovisionBucket"
    

The following partial example shows an Admin Activity audit log:
    
    
      {
        "logName": "projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity",
        "resource": {
          "type": "audited_resource",
          "labels": {
            "project_id": "PROJECT_ID",
            "service": "observability.googleapis.com",
            "method": "google.cloud.observability.v1.Observability.ReprovisionBucket"
          }
        },
        "protoPayload": {
          "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
          "status": {
            "code": 0,
            "message": "OK"
          },
          ...
          "serviceName": "observability.googleapis.com",
          "methodName": "google.cloud.observability.v1.Observability.ReprovisionBucket",
          "authorizationInfo": [...]
          "resourceName": "projects/PROJECT_ID/locations/us/buckets/_Trace",
          "request": {
            "@type": "type.googleapis.com/google.cloud.observability.v1.ReprovisionBucketRequest",
            "name": "projects/PROJECT_ID/locations/us/buckets/_Trace"
          },
          "response": {
            "@type": "type.googleapis.com/google.longrunning.Operation",
            "name": "projects/PROJECT_ID/locations/us/operations/reprovision-123456789-0",
            "done": false,
            "metadata": {
              "@type": "type.googleapis.com/google.cloud.observability.v1.OperationMetadata",
              "target": "projects/PROJECT_ID/locations/us/buckets/_Trace",
              "verb": "reprovision",
              "apiVersion": "v1"
            }
          }
        },
        "severity": "NOTICE",
        "timestamp": "2026-06-30T16:54:02.123456Z"
      }
    

## Before you begin

  1. Review the Limitations.
  2. To get the permissions that you need to reprovision an observability bucket, ask your administrator to grant you the [Observability Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`) IAM role on the project that hosts your observability bucket. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

The Observability Editor role provides permissions to create and delete observability buckets, observability datasets, and links on datasets. You need these permissions because the reprovision operation issues both create and delete commands.

You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## Reprovision an observability bucket

To reprovision an observability bucket, perform the following steps:

  1. Configure default settings for observability buckets
  2. Reprovision the bucket
  3. Monitor progress
  4. Manually create links and update analytics views



### Configure default settings for observability buckets

Set a default storage location and optionally set a default Cloud KMS key. You can set these at the project, folder, or organization level. For example, if you configure default settings for a folder, then the descendants of that folder use those settings, unless a descendant also has default settings configured.

For more information about how to view and configure default settings, see [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets).

### Reprovision the bucket

Use scripts that issue the reprovision request asynchronously and poll to determine when the reprovision operation completes. To reprovision an observability bucket, use the [`projects.locations.buckets.reprovision`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.buckets/reprovision) method.

You must specify the name of the observability bucket, which has the following format:
    
    
    projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID
    

The fields in the preceding expression have the following meanings:

  * PROJECT_ID: The identifier of the project.
  * LOCATION: The [location of the observability bucket](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations).
  * BUCKET_ID: The ID of the observability bucket. This ID must be `_Trace`.



The response is an [`Operation`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/folders.locations.operations#Operation) object. The `Operation.done` field provides progress information:

  * `done` is `false`: The operation is in progress. For information about polling the operation, see Monitor progress.

  * `done` is `true`: The operation is complete and either the `error` or `response` field is set:

    * `response` is set: Indicates successful completion of the asynchronous operation. The value reflects the latest state of the observability bucket that was the reprovisioning target.

    * `error` is set: Indicates that the asynchronous operation failed. The value of this field is a `Status` object that contains a gRPC error code and an error message. For information about common error messages, see Error messages.




Reprovisioning typically requires four to five hours to complete.

### Monitor progress

The `Operation` object contains progress information. Poll the operation until the value of the `Operation.done` field is `true`. You can then use the `Operation.response` and `Operation.error` fields to determine whether reprovisioning succeeded or failed.

To poll the [`Operation`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/folders.locations.operations#Operation), use the [`folders.locations.operations.get`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/folders.locations.operations/get) method.

Set the path parameter to the name of the operation:
    
    
    operations/UNIQUE_ID
    

The field UNIQUE_ID is the operation's unique identifier.

The response is an updated [`Operation`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/folders.locations.operations#Operation) object.

If your application receives an `HTTP 503 / UNAVAILABLE` response when polling, then implement an exponential backoff and retry the request. This error indicates that the request failed at the transport or network layer.

### Manually create links and update analytics views

After the reprovision operation completes, recreate any links and update your analytics views.

For example, you might do the following:

  1. List the links on the observability dataset. In some scenarios, the reprovision operation retains links. For information about this step, see [List links on a dataset](https://docs.cloud.google.com/trace/docs/storage-manage#list-links-on-dataset).

  2. Recreate the linked BigQuery dataset. For information about this step, see [Create a link on a dataset](https://docs.cloud.google.com/trace/docs/storage-manage#create-links-on-dataset).

  3. Review your analytics views and update the path to the observability bucket as necessary.




## Error messages

This section lists common error codes and, when applicable, recovery actions.

### FAILED_PRECONDITION

The `FAILED_PRECONDITION` error message indicates that the observability bucket isn't eligible for reprovisioning.

Example error message:
    
    
    {
        "error":{
            "code": 400,
            "message": "Only _Trace buckets can be reprovisioned.",
            "status": "FAILED_PRECONDITION",
            "details": [ ... ]
        }
    }
    

There is no action that you can perform to make the observability bucket eligible for reprovisioning.

### INVALID_ARGUMENT

The `INVALID_ARGUMENT` error message indicates that the observability bucket's location and CMEK configuration are consistent with the default settings for observability buckets.

To resolve this failure, update the default settings for observability buckets for the project, folder, or organization, and then retry reprovisioning the observability bucket.

### PERMISSION_DENIED

The `PERMISSION_DENIED` error message indicates that you don't have the required IAM roles to reprovision an observability bucket.

To resolve this failure, have an administrator grant you the IAM roles listed in the Before you begin section of this document.

## Troubleshooting

This section describes how to resolve common issues and answer questions that might arise after you reprovision an observability bucket.

### How do I know if a bucket has been reprovisioned?

Query your audit logs and filter the log entries by the log name, the service, and the method. For more information, see the section of this document titled Auditing.

### Why does my project list two buckets for trace data?

During a reprovision of the `_Trace` observability bucket, the system might need to create a new bucket. When this is true, your project will contain two observability buckets named `_Trace` during the reprovision operation.

  * If you [list the observability buckets in your project](https://docs.cloud.google.com/trace/docs/storage-manage#list-buckets), then both buckets are reported in the results.

  * If you use Observability Analytics to query your trace data, then an `_AllSpans` view is available for both buckets.




You don't need to take action.

If the system created an observability bucket as part of a reprovision operation, then upon successful completion of that operation, the bucket targeted by the operation is deleted. If the reprovision operation fails, then the new bucket is deleted.

### Why is my queried data different after reprovisioning?

A reprovisioning operation deletes all data that was stored before the operation was initiated. This data isn't recoverable.

### Why doesn't Trace Explorer show any data after reprovisioning?

The Trace Explorer uses cache to improve performance. The cache is tied to the observability bucket being queried and, importantly, if that bucket isn't available at the time of a query, then the query fails.

During a reprovision operation, it is possible for your Google Cloud project to contain two observability buckets named `_Trace`. Further, when that operation completes, one of those buckets is deleted. In this scenario, it is possible for the cache that the Trace Explorer uses to be tied to a bucket that no longer exists.

This failure self-corrects after the cache times out, which requires about 10 minutes.

### Why can't my observability bucket be reprovisioned?

If a reprovisioning operation fails with a `FAILED_PRECONDITION` status, the targeted observability bucket isn't eligible for reprovisioning. The following lists some reasons why a bucket is ineligible for reprovisioning:

  * The observability bucket isn't named `_Trace`.
  * The number of times the observability bucket was reprovisioned exceeds one. You can query your audit logs to determine whether the bucket was reprovisioned.
  * The [default settings for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets) aren't found. To resolve this failure, configure default settings for observability buckets and then retry the command.
  * The configuration of the observability bucket is in agreement with the default settings. That is, the reprovision operation won't change the configuration of the observability bucket.
  * To be in agreement with the default settings, the system would need to replace CMEK with Google-managed encryption. This action isn't supported.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-06 UTC."],[],[]] 

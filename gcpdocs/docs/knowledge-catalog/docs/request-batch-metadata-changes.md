---
url: https://docs.cloud.google.com/knowledge-catalog/docs/request-batch-metadata-changes/
title: Request batch metadata changes with governance workflows \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-07T05:50:56.330450+00:00
---

# Request batch metadata changes with governance workflows  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/request-batch-metadata-changes/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Request batch metadata changes with governance workflows Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to submit a batch metadata change request for an entry group in Knowledge Catalog (formerly Dataplex Universal Catalog) using the REST API.

If you don't have direct write access to an entry group, you can group up to 250 create, update, and delete operations for entries and entry links into a single change request for review and approval.

## Before you begin

To submit batch metadata change requests, ensure that you have enabled the required APIs and that you have the necessary Identity and Access Management (IAM) roles and permissions on the target entry group.

Enable the Dataplex API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com)

### Required roles

To get the permissions that you need to request batch metadata changes for an entry group, ask your administrator to grant you the following IAM roles on the target entry group: 

  * Submit batch metadata change requests: [Dataplex Catalog Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** If you use a custom role instead of Dataplex Catalog Viewer, ensure that the role includes the `dataplex.entryGroups.get` and `dataplex.entryGroups.requestChanges` permissions on the target entry group.

For more information about roles and permissions, see [Knowledge Catalog IAM roles](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles).

## Create a batch metadata change request

When you submit a batch change request, Knowledge Catalog checks the request syntax and verifies that any referenced entry types, aspect types, entry link types, and parent entries exist. When the request is approved, Knowledge Catalog checks whether the target entries and entry links exist—for example, returning an `ALREADY_EXISTS` error when creating an existing resource or a `NOT_FOUND` error when updating or deleting a missing resource.

When an approver approves a batch change request, Knowledge Catalog automatically applies the operations in the following dependency order:

  1. Delete entry links.
  2. Delete entries.
  3. Create and update entries.
  4. Create and update entry links.



Batch change requests don't provide transactional consistency or automatic rollback. When approved, Knowledge Catalog evaluates and applies each operation individually.

Keep the following reference rules in mind when constructing a batch:

  * **Don't reference entries deleted in the same batch** : you can't create or update an entry link that references an entry being deleted in the same batch, and you can't set `parentEntry` to an entry that you're deleting in the same batch.
  * **List parent entries before child entries** : if a new entry references another entry in the same batch as its `parentEntry`, list the request that creates the parent entry before the request that creates the child entry. When you create an entry or entry link, the `parent` entry group field is optional. If you omit `parent`, Knowledge Catalog uses the entry group in `changePayload.name`. If you include `parent`, it must match `changePayload.name`.



To submit a basic batch metadata change request, use the `entryGroups.requestBatchMetadataChange` method:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID",
        "changePayload": {
          "name": "projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID",
          "changes": [
            {
              "createEntryRequest": {
                "parent": "projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID",
                "entryId": "ENTRY_ID",
                "entry": {
                  "entryType": "projects/PROJECT_ID/locations/LOCATION/entryTypes/ENTRY_TYPE_ID"
                }
              }
            }
          ]
        },
        "justification": "JUSTIFICATION"
      }' \
      "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID:requestBatchMetadataChange"
    

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project that contains the entry group.
  * `LOCATION`: the location of the entry group, such as `us-central1`.
  * `ENTRY_GROUP_ID`: the ID of the target entry group.
  * `ENTRY_ID`: the ID of the new entry to create.
  * `ENTRY_TYPE_ID`: the ID of the entry type for the new entry.
  * `JUSTIFICATION`: the reason why the metadata change request is needed, up to 1,024 characters.



The service returns a response containing the resource name of the created change request:
    
    
    {
      "changeRequest": "projects/123456789012/locations/us-central1/changeRequests/eeb06bad-fc7f-49b9-9fb2-61d1ad4bad32"
    }
    

## Verify the created batch change request

To inspect the created change request, use the `changeRequests.get` method:
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests/CHANGE_REQUEST_ID"
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the region where the resource exists, such as `us-central1`.
  * `CHANGE_REQUEST_ID`: the unique ID of the request.



The service returns a `ChangeRequest` resource that contains the batch payload:

Sample response for a user-submitted batch change request
    
    
    {
      "name": "projects/123456789012/locations/us-central1/changeRequests/eeb06bad-fc7f-49b9-9fb2-61d1ad4bad32",
      "uid": "eeb06bad-fc7f-49b9-9fb2-61d1ad4bad32",
      "createTime": "2026-09-14T09:06:40.352156739Z",
      "updateTime": "2026-09-14T09:06:41.714939166Z",
      "justification": "Requesting creation of a new entry",
      "author": "requester@example.com",
      "state": "NEW",
      "resource": "//dataplex.googleapis.com/projects/my-project/locations/us-central1/entryGroups/my-entry-group",
      "etag": "0YSwO12PxwypRJj6kqM3CTZ9BYk4wk3yasxdiMDE3MU",
      "changeType": "BATCH_CHANGE_METADATA",
      "batchChangeMetadataRequest": {
        "name": "projects/my-project/locations/us-central1/entryGroups/my-entry-group",
        "changes": [
          {
            "createEntryRequest": {
              "parent": "projects/my-project/locations/us-central1/entryGroups/my-entry-group",
              "entryId": "new-entry-id",
              "entry": {
                "entryType": "projects/my-project/locations/us-central1/entryTypes/my-entry-type"
              }
            }
          }
        ]
      }
    }

If an enrichment agent run creates the batch change request automatically, the `author` field contains the enrichment agent service account, and the `batchChangeMetadataRequest.description.job.name` field contains the enrichment run resource name.

## Create a multi-resource batch change request

To propose changes to multiple resources in a single entry group, use the `entryGroups.requestBatchMetadataChange` method. For example, you can use this method to create a first entry, create a second entry with an attached aspect, and create a directional entry link connecting them.

To create a multi-resource batch change request, send the following `POST` request:

Sample request for creating a multi-resource batch change request
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID",
        "changePayload": {
          "name": "projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID",
          "changes": [
            {
              "createEntryRequest": {
                "parent": "projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID",
                "entryId": "FIRST_ENTRY_ID",
                "entry": {
                  "entryType": "projects/PROJECT_ID/locations/LOCATION/entryTypes/ENTRY_TYPE_ID"
                }
              }
            },
            {
              "createEntryRequest": {
                "parent": "projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID",
                "entryId": "SECOND_ENTRY_ID",
                "entry": {
                  "entryType": "projects/PROJECT_ID/locations/LOCATION/entryTypes/ENTRY_TYPE_ID",
                  "aspects": {
                    "PROJECT_ID.LOCATION.ASPECT_TYPE_ID": {
                      "data": {
                        "ASPECT_FIELD_NAME": "ASPECT_FIELD_VALUE"
                      }
                    }
                  }
                }
              }
            },
            {
              "createEntryLinkRequest": {
                "parent": "projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID",
                "entryLinkId": "ENTRY_LINK_ID",
                "entryLink": {
                  "entryLinkType": "projects/PROJECT_ID/locations/LOCATION/entryLinkTypes/ENTRY_LINK_TYPE_ID",
                  "entryReferences": [
                    {
                      "name": "projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID/entries/FIRST_ENTRY_ID",
                      "type": "SOURCE"
                    },
                    {
                      "name": "projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID/entries/SECOND_ENTRY_ID",
                      "type": "TARGET"
                    }
                  ]
                }
              }
            }
          ]
        },
        "justification": "JUSTIFICATION"
      }' \
      "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID:requestBatchMetadataChange"

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project that contains the entry group.
  * `LOCATION`: the location of the entry group, such as `us-central1`.
  * `ENTRY_GROUP_ID`: the ID of the target entry group.
  * `FIRST_ENTRY_ID`: the ID of the first custom entry, which is used as the `SOURCE` in the entry link.
  * `SECOND_ENTRY_ID`: the ID of the second custom entry with an attached aspect, which is used as the `TARGET` in the entry link.
  * `ENTRY_TYPE_ID`: the ID of the entry type for the new entries.
  * `ASPECT_TYPE_ID`: the ID of the aspect type attached to the second entry.
  * `ASPECT_FIELD_NAME`: the name of the field in the aspect template.
  * `ASPECT_FIELD_VALUE`: the value for the aspect field.
  * `ENTRY_LINK_ID`: the ID of the entry link connecting the two entries.
  * `ENTRY_LINK_TYPE_ID`: the ID of the entry link type, such as `my-entry-link-type`.
  * `JUSTIFICATION`: the explanation of why these metadata changes are needed.



The service returns a response containing the resource name of the created change request:
    
    
    {
      "changeRequest": "projects/123456789012/locations/us-central1/changeRequests/eeb06bad-fc7f-49b9-9fb2-61d1ad4bad32"
    }
    

## What's next

  * Learn how to [edit, approve, or reject change requests, and curate enrichment agent batches](https://docs.cloud.google.com/knowledge-catalog/docs/manage-requests).
  * Learn how to [request single-resource metadata changes](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-change-workflows).
  * Learn more about [governance workflows](https://docs.cloud.google.com/knowledge-catalog/docs/about-governance-workflows).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 

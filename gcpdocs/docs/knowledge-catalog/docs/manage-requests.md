---
url: https://docs.cloud.google.com/knowledge-catalog/docs/manage-requests/
title: Manage change requests with governance workflows \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-05T00:17:52.777296+00:00
---

# Manage change requests with governance workflows  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/manage-requests/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Manage change requests with governance workflows Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** Requesting single metadata changes to business glossaries and entries is available in private preview. To request access to this feature, fill in the [access form](https://forms.gle/eFMGqsaKTUJ62mrR7). 

This document describes how requesters, approvers, and workflow administrators manage governance requests in Knowledge Catalog (formerly Dataplex Universal Catalog).

## Before you begin

To use governance workflows, ensure that you have enabled the required APIs and that approvers and administrators have the necessary Identity and Access Management (IAM) roles and permissions.

Enable the Dataplex API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com)

### Required roles

To get the permissions that you need to manage governance requests, ask your administrator to grant you the following IAM roles on your project: 

  * Approve or reject data product access requests: 
    * [Dataplex Data Products Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsEditor) (`roles/dataplex.dataProductsEditor`)
    * [Dataplex Data Products Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsAdmin) (`roles/dataplex.dataProductsAdmin`)
  * Review and approve metadata change requests: 
    * [Dataplex Catalog Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)
    * [Dataplex Workflow Approver ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.workflowApprover) (`roles/dataplex.workflowApprover`)
  * View and edit authored requests: [Dataplex Change Request Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.changeRequestOwner) (`roles/dataplex.changeRequestOwner`) 
  * View and edit requests created by an enrichment agent: [Dataplex Catalog Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`) 
  * View all requests and delete requests in any state: 
    * [Dataplex Workflow Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.workflowAdmin) (`roles/dataplex.workflowAdmin`)
    * [Dataplex Catalog Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)
  * Configure approver email notifications: 
    * [Dataplex Catalog Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`)
    * [Dataplex Catalog Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`)
    * [Dataplex Glossary Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.glossaryOwner) (`roles/dataplex.glossaryOwner`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** If an approver uses the Dataplex Workflow Approver role to approve a metadata change request, they must also have write access on the target entry or glossary resource, such as Dataplex Catalog Editor or Dataplex Entry Owner.

For more information about roles and permissions, see [Knowledge Catalog IAM roles](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles).

## Manage requests as a requester

As a requester, you initiate change requests, such as requesting access to data products or proposing metadata changes. After submitting a request, you can monitor its progress, view request details, edit details for pending requests, or delete requests in the `NEW` state before an approver acts on them.

### View authored requests

To view the requests you created or inspect a specific request, do the following:

###  Console 

  1. In the Google Cloud console, go to the Knowledge Catalog **Governance Workflows** page.

[Go to Governance Workflows](https://console.cloud.google.com/dataplex/govern/workflows)

  2. Click the **My Requests** tab to view a list of your past and pending requests.




###  REST 

To list requests that you authored, use the `changeRequests.list` method:
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests?filter=author=USER_EMAIL"
    

To view a specific request, use the `changeRequests.get` method:
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests/CHANGE_REQUEST_ID"
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the region where the resource exists, such as `us-central1`.
  * `USER_EMAIL`: your email address.
  * `CHANGE_REQUEST_ID`: the unique ID of the request.



For batch metadata change requests, inspect the response fields to identify how the request was created:

  * **User-submitted request** : `author` is the requester's email address, and `batchChangeMetadataRequest.description.job` isn't set.
  * **Enrichment agent-generated request** : `author` is the enrichment agent service account, and `batchChangeMetadataRequest.description.job.name` is set to the enrichment run ID.



### Edit a request

You can update a pending request using the REST API while it's in the `NEW` or `FAILED` state. Updating a request in the `FAILED` state resets its state to `NEW` so an approver can review it again. Who can edit a metadata change request depends on how it was created:

  * **Requests submitted by users** : only the original author can send a `PATCH` request to update the justification or the request payload.
  * **Requests generated by enrichment agents** : in addition to the author, reviewers and approvers can send a `PATCH` request while the request is in the `NEW` or `FAILED` state to curate the batch—for example, to modify proposed aspect values or remove items from the `changes` array. The `author` field remains the enrichment agent service account.



To update a pending change request, use the `changeRequests.patch` method.

To update only the request justification, send the following `PATCH` request:
    
    
    curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "justification": "NEW_JUSTIFICATION"
      }' \
      "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests/CHANGE_REQUEST_ID?updateMask=justification"
    

To update the payload of a batch metadata change request, send the following `PATCH` request:
    
    
    curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "justification": "NEW_JUSTIFICATION",
        "batchChangeMetadataRequest": {
          "name": "projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID",
          "changes": [
            {
              "updateEntryRequest": {
                "entry": {
                  "name": "projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID/entries/EXISTING_ENTRY_ID",
                  "aspects": {
                    "ASPECT_PROJECT_ID.ASPECT_LOCATION.ASPECT_TYPE_ID": {
                      "data": {
                        "ASPECT_FIELD_NAME": "UPDATED_ASPECT_FIELD_VALUE"
                      }
                    }
                  }
                },
                "updateMask": "aspects",
                "aspectKeys": [
                  "ASPECT_PROJECT_ID.ASPECT_LOCATION.ASPECT_TYPE_ID"
                ]
              }
            }
          ]
        }
      }' \
      "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests/CHANGE_REQUEST_ID?updateMask=batchChangeMetadataRequest.changes,justification"
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the region where the change request exists, such as `us-central1`.
  * `CHANGE_REQUEST_ID`: the unique ID of the change request.
  * `NEW_JUSTIFICATION`: the updated justification for the change request.
  * `ENTRY_GROUP_ID`: the ID of the target entry group.
  * `EXISTING_ENTRY_ID`: the ID of the entry in the updated batch payload.
  * `ASPECT_PROJECT_ID`: the ID of the project that contains the aspect type.
  * `ASPECT_LOCATION`: the location of the aspect type, such as `us-central1` or `global`.
  * `ASPECT_TYPE_ID`: the ID of the aspect type being updated.
  * `ASPECT_FIELD_NAME`: the name of the aspect field to update.
  * `UPDATED_ASPECT_FIELD_VALUE`: the updated value for the aspect field.



### Delete a request

As a requester, you can only delete requests that are in the `NEW` state. To delete a request, do the following:

###  Console 

  1. In the Google Cloud console, go to the Knowledge Catalog **Governance Workflows** page.

[Go to Governance Workflows](https://console.cloud.google.com/dataplex/govern/workflows)

  2. Click the **My Requests** tab.

  3. Locate the row containing the request you want to delete. If necessary, apply a filter to isolate the entry.

  4. Click more_vert **Actions** , and then click **Delete**.




###  REST 

To delete a request, use the `changeRequests.delete` method.

For example, send the following `DELETE` request:
    
    
    curl -X DELETE \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests/CHANGE_REQUEST_ID"
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the region where the resource exists, such as `us-central1`.
  * `CHANGE_REQUEST_ID`: the unique ID of the request you want to delete.



## Manage requests as an approver

As an approver, you evaluate and act on pending requests submitted for your data resources.

### Notifications

When you approve or reject a request, Knowledge Catalog processes the decision and sends an email notification to the requester with your review comment. For batch requests, Knowledge Catalog sends the email notification after the update process completes. If the author is a service account, Knowledge Catalog doesn't send a notification.

### Approval considerations

You can't approve your own request. The approver must be a different principal and hold all write and type-usage permissions required by the proposed changes. However, an enrichment agent can either auto-approve its own requests based on confidence or submit them to an approver for review. For batch metadata change requests generated by an enrichment agent, you can edit the request payload while the request is in the `NEW` or `FAILED` state before approving it.

### View pending requests

To view requests pending review, do the following:

###  Console 

  1. In the Google Cloud console, go to the Knowledge Catalog **Governance Workflows** page.

[Go to Governance Workflows](https://console.cloud.google.com/dataplex/govern/workflows)

  2. Click the **Pending Approvals** tab to view requests pending review. You can filter requests by resource type, request type, or date.




###  REST 

To list requests pending review within a specific project and location, use the `changeRequests.list` method.

For example, send the following `GET` request:
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests?filter=state=NEW"
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the region where the resource exists, such as `us-central1`.



In the returned list, batch metadata change requests have the `changeType` field set to `BATCH_CHANGE_METADATA`. Requests created by an enrichment agent run include the enrichment run ID in `batchChangeMetadataRequest.description.job.name`.

Sample response for a pending batch change request
    
    
    {
    "changeRequests": [
      {
        "name": "projects/my-project/locations/us-central1/changeRequests/b326114f-472b-457d-81e8-98b8ad89c608",
        "uid": "b326114f-472b-457d-81e8-98b8ad89c608",
        "justification": "Enrichment Agent Proposal: Batch Metadata Change",
        "author": "enrichment-agent@my-project.iam.gserviceaccount.com",
        "state": "NEW",
        "resource": "//dataplex.googleapis.com/projects/my-project/locations/us-central1/entryGroups/my-entry-group",
        "changeType": "BATCH_CHANGE_METADATA",
        "batchChangeMetadataRequest": {
          "name": "projects/my-project/locations/us-central1/entryGroups/my-entry-group",
          "description": {
            "job": {
              "name": "projects/123456789012/locations/us-central1/enrichmentTasks/my-enrichment-task/runs/55199e83-1a1e-4837-bb8c-c402c6bee641"
            }
          },
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
    ]
    }

### Approve a request

To approve a request, do the following:

###  Console 

  1. In the Google Cloud console, go to the Knowledge Catalog **Governance Workflows** page.

[Go to Governance Workflows](https://console.cloud.google.com/dataplex/govern/workflows)

  2. Click the **Pending Approvals** tab.

  3. Locate the row containing the request you want to approve.

  4. Click more_vert **Actions** , and then click **Approve**.




###  REST 

To approve a request, use the `changeRequests.approve` method.

For example, send the following `POST` request:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{}' \
      "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests/CHANGE_REQUEST_ID:approve"
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the region where the resource exists, such as `us-central1`.
  * `CHANGE_REQUEST_ID`: the unique ID of the change request you want to approve.



When you approve a batch metadata change request submitted by a user or an enrichment agent, Knowledge Catalog validates your IAM permissions and payload rules synchronously:

  * If validation succeeds, the method returns the `ChangeRequest` in the `APPLYING` state while Knowledge Catalog executes the batch in the background:


    
    
      {
        "name": "projects/my-project/locations/us-central1/changeRequests/b326114f-472b-457d-81e8-98b8ad89c608",
        "uid": "b326114f-472b-457d-81e8-98b8ad89c608",
        "justification": "Proposing new entry using RequestBatchMetadataChange",
        "author": "requester@example.com",
        "state": "APPLYING",
        "resource": "//dataplex.googleapis.com/projects/my-project/locations/us-central1/entryGroups/my-entry-group",
        "approver": "approver@example.com",
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
      ```
    
    * If synchronous payload validation fails (for example, with an
    `INVALID_ARGUMENT` or `NOT_FOUND` error), the request immediately
    transitions to the `FAILED` state instead of `APPLYING`.
    * If permission validation fails with a `PERMISSION_DENIED` error, the request
    remains in the `NEW` state.
    
    After background execution finishes, poll `changeRequests.get` to check the
    final state (`APPROVED` or `FAILED`). If any changes in the batch fail,
    `batchChangeMetadataResponse.failedRequests` lists each failed change by its
    position in `changes` (starting at `0`) along with the error details:
    
    ```json
    {
      "name": "projects/my-project/locations/us-central1/changeRequests/b326114f-472b-457d-81e8-98b8ad89c608",
      "state": "APPROVED",
      "changeType": "BATCH_CHANGE_METADATA",
      "batchChangeMetadataResponse": {
        "failedRequests": {
          "1": {
            "code": 5,
            "message": "Entry not found."
          }
        }
      }
    }
    

For more information about request states, see [Governance workflows processing path](https://docs.cloud.google.com/knowledge-catalog/docs/about-governance-workflows#request-status).

### Reject a request

To reject a request, do the following:

###  Console 

  1. In the Google Cloud console, go to the Knowledge Catalog **Governance Workflows** page.

[Go to Governance Workflows](https://console.cloud.google.com/dataplex/govern/workflows)

  2. Click the **Pending Approvals** tab.

  3. Locate the row containing the request you want to reject.

  4. Click more_vert **Actions** , and then click **Reject**.

  5. In the dialog, enter a justification for the rejection.

  6. Click **Reject** to confirm.




###  REST 

To reject a request, use the `changeRequests.reject` method.

For example, send the following `POST` request:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "comment": "REJECTION_REASON"
      }' \
      "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests/CHANGE_REQUEST_ID:reject"
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the region where the resource exists, such as `us-central1`.
  * `CHANGE_REQUEST_ID`: the unique ID of the change request you want to reject.
  * `REJECTION_REASON`: the justification for the rejection.



Providing a clear rejection comment helps requesters understand the decision and refine their justifications before they resubmit the request.

## Manage requests as a workflow administrator

As a workflow administrator, you oversee governance requests across your organization, configure approver email notifications, audit approval history, and delete requests in any state.

### Configure approver email notifications

You can configure approver email notifications on an entry group or a business glossary to specify up to 10 email addresses that are automatically notified whenever a single or batch metadata change request is created for that resource.

To configure notifications on an entry group, use the `entryGroups.patch` method:
    
    
    curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "changeRequestConfig": {
          "approverEmails": [
            "APPROVER_EMAIL_1",
            "APPROVER_EMAIL_2"
          ]
        }
      }' \
      "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID?updateMask=changeRequestConfig"
    

To configure notifications on a business glossary, use the `glossaries.patch` method:
    
    
    curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "changeRequestConfig": {
          "approverEmails": [
            "APPROVER_EMAIL_1",
            "APPROVER_EMAIL_2"
          ]
        }
      }' \
      "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/global/glossaries/GLOSSARY_ID?updateMask=changeRequestConfig"
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the location of the entry group, such as `us-central1` or `global`.
  * `ENTRY_GROUP_ID`: the ID of the entry group.
  * `GLOSSARY_ID`: the ID of the business glossary.
  * `APPROVER_EMAIL_1`, `APPROVER_EMAIL_2`: the email addresses of potential approvers to notify when a change request is created. You can specify up to 10 email addresses.



### View all requests and track approval history

You can view all active and historical requests across states to monitor workflows and audit data product access and metadata changes:

###  Console 

  1. In the Google Cloud console, go to the Knowledge Catalog **Governance Workflows** page.

[Go to Governance Workflows](https://console.cloud.google.com/dataplex/govern/workflows)

  2. Click the **Approval Log** tab to view completed approvals, rejections, and historical audit trails.




###  REST 

To list all active and historical requests within a specific project and location, use the `changeRequests.list` method.

For example, send the following `GET` request:
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests"
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the region where the resource exists, such as `us-central1`.



### Delete a request in any state

Unlike requesters, who can only delete requests in the `NEW` state, workflow administrators can delete requests in any state using the Google Cloud console or the `changeRequests.delete` method. For instructions, see Delete a request.

## What's next

  * Learn more about [governance workflows](https://docs.cloud.google.com/knowledge-catalog/docs/about-governance-workflows).
  * Learn how to [request single-resource metadata changes](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-change-workflows).
  * Learn how to [request batch metadata changes](https://docs.cloud.google.com/knowledge-catalog/docs/request-batch-metadata-changes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 

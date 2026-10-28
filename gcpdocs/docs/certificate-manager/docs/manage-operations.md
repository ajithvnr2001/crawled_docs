---
url: https://docs.cloud.google.com/certificate-manager/docs/manage-operations/
title: Manage long-running operations \u00a0|\u00a0 Certificate Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T19:16:20.851677+00:00
---

# Manage long-running operations  |  Certificate Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/manage-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-manager/docs/overview)



Send feedback 

#  Manage long-running operations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to check and manage long-running operations in Certificate Manager.

When a mutation request in Certificate Manager, such as creating, updating, or deleting a resource, doesn't fail immediately, the API returns a long-running operation (LRO). These operations track the status of processing tasks that take longer to complete. By default, `gcloud` mutation commands wait for the operation to finish unless you specify the `--async` flag.

You can use the `projects.locations.operations` collection to check the status of operations.

## Required permissions

To manage long-running operations in the target project, you must have the permission that corresponds to the task that you want to perform:

  * `certificatemanager.operations.get`: retrieves details of a specific operation.
  * `certificatemanager.operations.list`: lists all operations in a given location.
  * `certificatemanager.operations.delete`: deletes a completed operation resource (API only).



For more information about roles and permissions, see [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions).

## Get details about a long-running operation

When you make a call that starts an operation, such as creating a certificate, the response contains an operation name in the format: `projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID`.

To check if the operation is complete, request details about the target operation. If the response contains `"done": false` or doesn't include the `"done"` field, the operation is still in progress. Check the status again until the response displays `"done": true`.

###  gcloud 

To describe a long-running operation, use the [`certificate-manager operations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/operations/describe):
    
    
    gcloud certificate-manager operations describe OPERATION_ID \
        --location="LOCATION"
    

Replace the following:

  * `OPERATION_ID`: the ID of the operation.
  * `LOCATION`: the target Google Cloud location. The default location is `global`.



###  API 

To get details about a long-running operation, send a `GET` request to the [`projects.locations.operations.get`](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.operations/get) method:
    
    
    GET https://certificatemanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `LOCATION`: the target Google Cloud location. The default location is `global`.
  * `OPERATION_ID`: the ID of the operation.



## List long-running operations

You can list operations to find operation IDs and monitor active modifications in your project.

###  gcloud 

To list operations in a given location, use the [`certificate-manager operations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/operations/list):
    
    
    gcloud certificate-manager operations list \
        --location="LOCATION"
    

Replace the following:

  * `LOCATION`: the target Google Cloud location. The default location is `global`.



###  API 

To list operations in a location, make a `GET` request to the [`projects.locations.operations.list`](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.operations/list) method:
    
    
    GET https://certificatemanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `LOCATION`: the target Google Cloud location. The default location is `global`.



## Delete a completed long-running operation

You can delete a completed operation resource if you no longer need the result. Deleting a completed operation removes only the operation record and doesn't cancel or reverse the changes made by the operation.

You can't delete operations by using `gcloud` commands. Instead, use the REST API.

###  API 

To delete a completed operation, send a `DELETE` request to the [`projects.locations.operations.delete`](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.operations/delete) method:
    
    
    DELETE https://certificatemanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `LOCATION`: the target Google Cloud location. The default location is `global`.
  * `OPERATION_ID`: the ID of the operation.



## Retention policy

Certificate Manager automatically retains and deletes completed LROs according to the following rules, in order of precedence:

  1. **Less than 1 hour old** : if an operation completed less than 1 hour ago, Certificate Manager retains the operation.
  2. **More than 1 week old** : if an operation completed more than 1 week ago, Certificate Manager deletes the operation.
  3. **Maximum limit** : if an operation completed between 1 hour and 1 week ago, Certificate Manager retains up to 5,000 of the most recent completed operations in each project and deletes any older completed operations.



The following examples show how these rules apply:

  * If your project has 10,000 completed operations that are all less than 1 hour old, Certificate Manager retains all 10,000 operations.
  * If your project has 1,000 completed operations that are all more than 1 week old, Certificate Manager deletes all 1,000 operations.
  * If your project has 10,000 completed operations that are all between 1 hour and 1 week old, Certificate Manager retains only the 5,000 most recent operations.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/infrastructure-manager/docs/view-resources/
title: View resources deployed \u00a0|\u00a0 Infrastructure Manager \u00a0|\u00a0 Google Cloud Documentation
method: httpx+scrapegraph (scrapling: scrapling status 429 | crawl4ai: crawl4ai failed: Unexpected error in _crawl_web at line 1299 in create_browser_context (../../../../usr/local/lib/python3.10/dist-packages/crawl4ai/browser_manager.py):
Error: Browser is not available. It may have been closed, crashed, or not yet started. Ensure the browser is running before creating new contexts.

Code context:
1294                   raise RuntimeError(
1295                       "Cannot create new browser contexts when using "
1296                       "use_persistent_context=True. Persistent context uses a "
1297                       "single shared context."
1298                   )
1299 →             raise RuntimeError(
1300                   "Browser is not available. It may have been closed, crashed, "
1301                   "or not yet started. Ensure the browser is running before "
1302                   "creating new contexts."
1303               )
1304           # Base settings)
fetched_at: 2026-10-27T16:30:43.063412+00:00
---

# View resources deployed  |  Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/view-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/infrastructure-manager/docs/overview)



Send feedback 

#  View resources deployed Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view information about resources that are provisioned by Infrastructure Manager.

You may want to view resources to understand their state, or to see what resources exist in a deployment before you update or delete the deployment.

When Infrastructure Manager deploys a Terraform configuration, the service provisions and configures the Google Cloud resources that are defined in the configuration. Metadata about these resources are in the Terraform state file, and Infra Manager stores this file for each deployment and revision.

The state file has information about the resources when they are provisioned by Infra Manager. The state file and Infra Manager do not have information about these resources if they are modified, unless they are modified by a [Infra Manager revision](https://docs.cloud.google.com/infrastructure-manager/docs/update-deployment).

For example, you can use Infra Manager to deploy a load balancer and then you can modify the load balancer using the Google Cloud console. In this case, Infra Manager has information about the load balancer that was initially provisioned, but not about the changes that you did through the Google Cloud console.

If you need information about the deployment name or state, see [View deployments](https://docs.cloud.google.com/infrastructure-manager/docs/view-deployments).

## Before you begin

  1. Ensure [Infra Manager is enabled](https://docs.cloud.google.com/infrastructure-manager/docs/enable-service).
  2. Ensure you have a service account.
  3. Ensure that you have the IAM permissions needed to view deployments. 
     * `roles/config.admin` or `roles/config.viewer`.



## List resources provisioned by a deployment

To list the resources provisioned by a deployment:
    
    
    gcloud infra-manager resources list --revision=projects/PROJECT_ID/locations/LOCATION/deployments/DEPLOYMENT_ID/revisions/REVISION_ID
    

Replace: 

  * PROJECT_ID: the project ID where Infrastructure Manager runs.
  * LOCATION: the location where Infra Manager runs. See [Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations) for the list of valid locations.
  * DEPLOYMENT_ID: the deployment identifier of the resource's deployment.
  * REVISION_ID: the revision identifier of the revision you're viewing.



### Filter the list of resources

To filter the list of resources:
    
    
    gcloud infra-manager resources list --revision=projects/PROJECT_ID/locations/LOCATION/deployments/DEPLOYMENT_ID/revisions/REVISION_ID --filter=EXPRESSION
    

Replace: 

  * PROJECT_ID: the project ID where Infrastructure Manager runs.
  * LOCATION: the location where Infra Manager runs. See [Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations) for the list of valid locations.
  * DEPLOYMENT_ID: the deployment identifier of the resource's deployment.
  * REVISION_ID: the revision identifier of the revision you're viewing and filtering.
  * EXPRESSION: the expression you are filtering for. Supported expressions are: 
    * `terraformInfo.address (string)`
    * `terraformInfo.type (string)`
    * `terraformInfo.id (string)`
    * `state (string)`, one of: `STATE_UNSPECIFIED`, `PLANNED`, `IN_PROGRESS`, `RECONCILED`, `FAILED`
    * `intent(string)`, one of: `INTENT_UNSPECIFIED`, `CREATE`, `UPDATE`, `DELETE`, `RECREATE`, `UNCHANGED`
    * `caiAssets.fullResourceName` (map)
    * `caiAssets.type` (map)



### Sort the list of resources

To sort the list of resources:
    
    
    gcloud infra-manager resources list --revision=projects/PROJECT_ID/locations/LOCATION/deployments/DEPLOYMENT_ID/revisions/REVISION_ID --sort-by=[FIELD]
    

Replace:

  * PROJECT_ID: the project ID where Infrastructure Manager runs.
  * LOCATION: the location where Infra Manager runs. See [Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations) for the list of valid locations.
  * DEPLOYMENT_ID: the deployment identifier of the resource's deployment.
  * REVISION_ID: the revision identifier of the revision you're viewing and sorting.
  * FIELD: the field used to sort. Supported fields are: 
    * `name`
    * `terraformInfo.address`
    * `terraformInfo.type`
    * `terraformInfo.id`



## View details about a resource

To view details about a specific resource, use the resource ID:
    
    
    gcloud infra-manager resources describe projects/PROJECT_ID/locations/LOCATION/deployments/DEPLOYMENT_ID/revisions/REVISION_ID/resources/RESOURCE_ID
    

Replace:

  * PROJECT_ID: the project ID where Infrastructure Manager runs.
  * LOCATION: the location where Infra Manager runs. See [Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations) for the list of valid locations.
  * DEPLOYMENT_ID: the deployment identifier of the resource's deployment.
  * REVISION_ID: the revision identifier of the specific revision that deployed the resource.
  * RESOURCE_ID: the resource ID of the resource you're viewing.



## What's next

  * Learn more about [Terraform with Google Cloud](https://docs.cloud.google.com/docs/terraform).
  * [Automate deployments](https://docs.cloud.google.com/infrastructure-manager/docs/automate-git).
  * [Update a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/update-deployment).
  * [View the state of a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/view-deployments).
  * [Delete a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/delete-deployments).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

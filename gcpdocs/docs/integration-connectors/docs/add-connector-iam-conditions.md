---
url: https://docs.cloud.google.com/integration-connectors/docs/add-connector-iam-conditions/
title: IAM Conditions for fine-grained access \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T18:14:03.122192+00:00
---

# IAM Conditions for fine-grained access  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/add-connector-iam-conditions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

# IAM Conditions for fine-grained access

This page describes how to restrict access to your connections by using IAM Conditions.

An IAM condition lets you have granular control over your Integration Connectors resources. By default, an [Integration Connectors user or a role](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions) can perform all the supported operations on a connection. By using IAM Conditions, you can restrict a specific user or a role to do only selected operations on a connection. For example, you can restrict a user such that the user can only modify the connections whose name begins with `test-connection`, and will not have other permissions on the connections such as subscribing to events, or viewing the schema metadata.

## Before you begin

Integration Connectors uses Google Cloud's [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) to manage roles and permissions for Integration Connectors resources. Therefore, before you specify or modify conditions in IAM for your Integration Connectors resources, familiarize yourself with the following IAM concepts:

  * [Resource](https://docs.cloud.google.com/iam/docs/overview#resource)
  * [Resource hierarchy](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control)
  * [Roles](https://docs.cloud.google.com/iam/docs/understanding-roles)
  * [Custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles)
  * [Permissions](https://docs.cloud.google.com/iam/docs/overview#permissions)
  * [Parent-only permissions](https://docs.cloud.google.com/iam/docs/configuring-resource-based-access#parent-only)



## Adding IAM Conditions

To add an IAM condition to an Integration Connectors resource, you need the following information:

  * **Named Resource URI** \- Every resource in Integration Connectors has a unique resource URI. For example, URI for the connection resource is `projects/PROJECT_ID/locations/CONNECTION_LOCATION/connections/{connection_name}`. For the complete list of all the available URIs, see [Integration Connectors REST resources](https://docs.cloud.google.com/integration-connectors/docs/reference/rest). To control access permissions for a resource at a granular level, you must name your resource according to a naming convention. Based on your requirements, you can decide the naming convention you want to use. For example, you can prefix the word `marketing-` for all the connections owned by the marketing team. In this example, the resource URI for the marketing team's connections, will begin with `projects/PROJECT_ID/locations/CONNECTION_LOCATION/connections/marketing-`. 
  * **Parent only permissions** \- Check if a resource or any of its child resource(s) require the parent-only permission. For more information, see [Parent-only permissions](https://docs.cloud.google.com/iam/docs/configuring-resource-based-access#parent-only). 
  * **Resource type** \- You can further narrow the scope of the resources by filtering for a resource type in the condition. Integration Connectors supports conditions for the following resources: Resource name | Resource type  
---|---  
Connection  | [connectors.googleapis.com/Connection](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections#resource:-connection)  
ManagedZone  | [connectors.googleapis.com/ManagedZone](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.global.managedZones)  
EndpointAttachment  | [connectors.googleapis.com/EndpointAttachment](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.endpointAttachments)  
EventSubscription  | [connectors.googleapis.com/EventSubscription](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections.eventSubscriptions)  
ConnectionSchemaMetadata  | [connectors.googleapis.com/ConnectionSchemaMetadata](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections.connectionSchemaMetadata)  

**Note:** Google Cloud resources have a hierarchical structure. Permissions applied to a parent resource don't apply to child resources, and permissions applied to child resources don't apply to the parent resource. For example, if you restrict a user to accessing only the connections whose names begin with `marketing-`, the user can still list all connections because the `list` permission is available on the connection's parent resource (the location). However, the user can perform `get`, `create`, `update`, and `delete` operations only on connections whose names begin with `marketing-`. Similarly, the `connectors.operations.list` permission is checked at the location level, not on individual connections.**Caution:** You cannot restrict long-running operations (LROs) to specific connections. An operation's resource name, `projects/PROJECT_ID/locations/CONNECTION_LOCATION/operations/OPERATION_ID`, does not contain the name of the connection that the operation creates, updates, or deletes. If your condition allows all resource types other than the ones it names, for example, `resource.type != "connectors.googleapis.com/Connection"`, it also grants `connectors.operations.*` permissions on every operation in the project. The user can view the operations of all connections and, if they have the Connector Admin role, cancel or delete those operations. To prevent this, exclude operations by their resource name using `resource.name.extract("/operations/{operation}") == ""`, as shown in the following examples.

## Examples

The following table lists the sample resource conditions that you can apply for an Integration Connectors user or a role.

IAM resource condition  | Description   
---|---  
      
    
    (resource.name.startsWith
    ("projects/PROJECT_ID/locations/CONNECTION_LOCATION/
    connections/marketing-") && resource.type == "connectors.googleapis.com/Connection")
    || (resource.type != "connectors.googleapis.com/Connection"
    && resource.name.extract("/operations/{operation}") == "")

| A user or a role to whom you apply this condition, can only do the following operations: 

  * List all the connections and long-running operations.
  * Perform get, create, update, and delete operations on connections whose name starts with `marketing-`.

The user can't view, cancel, or delete individual long-running operations. To let the user track the progress of operations, see Let restricted users track operations.  
      
    
    (resource.name.startsWith
    ("projects/PROJECT_ID/locations/CONNECTION_LOCATION/
    connections/marketing-") && resource.type == "connectors.googleapis.com/Connection") ||
    (resource.name.startsWith ("projects/PROJECT_ID/locations/CONNECTION_LOCATION/
    connections/marketing-") && resource.type == "connectors.googleapis.com/ConnectionSchemaMetadata")
    || (resource.type != "connectors.googleapis.com/Connection"
    && resource.type != "connectors.googleapis.com/ConnectionSchemaMetadata"
    && resource.name.extract("/operations/{operation}") == "")

| A user or a role to whom you apply this condition, can only do the following operations: 

  * List all connections and long-running operations.
  * Perform get, create, update, and delete operations **only for** connections whose name starts with `marketing-`.
  * Get connection schema metadata **only for** connections whose name starts with `marketing-`.

The user can't view, cancel, or delete individual long-running operations.  
  
### Let restricted users track operations

When the conditions in the preceding examples exclude operations, a restricted user can still create, update, and delete the connections that they're allowed to manage, but they can't check the status of the resulting long-running operations. If a restricted user needs to track operations, grant them a separate [custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) without a condition, that contains only the `connectors.operations.get` permission.

With this role, the user can view any operation in the project, including operations for connections that they can't otherwise access. This is the same connection information that the user can already view because they can list all connections. Don't grant the `connectors.operations.cancel` or `connectors.operations.delete` permissions to users whose access is restricted by a condition, because those permissions would let them cancel or delete operations for any connection in the project.

## Adding IAM Conditions for Application Integration service accounts

You can apply IAM Conditions to the Application Integration service account, which lets you restrict the connections the service account can access during integration execution. For example, you can restrict a service account such that it can access only connections whose name begin with `marketing-`. For more information, see [Apply IAM Conditions to a service account](https://docs.cloud.google.com/application-integration/docs/add-iam-conditions).

The following table lists the sample resource conditions that you can apply for an Application Integration service account.

IAM resource condition  | Description   
---|---  
      
    
    resource.name.startsWith
    ("projects/PROJECT_ID/locations/CONNECTION_LOCATION/
    connections/marketing-")

| The service account to which you apply this condition, can run only those connections whose name starts with `marketing-`.   
**Note:** Currently, Integration Connectors supports only the `startsWith` constraint for a service account resource condition.

## What's next

Go through the following information in the IAM documentation:

  * [Adding a conditional role binding to a policy](https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings#add)
  * [Modify an existing conditional role binding](https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings#modify)
  * [Removing a conditional role binding](https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings#removing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

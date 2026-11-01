---
url: https://docs.cloud.google.com/bigtable/docs/manage-data-assets-using-knowledge-catalog/
title: Manage data assets using Knowledge Catalog \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-01T05:45:15.635294+00:00
---

# Manage data assets using Knowledge Catalog  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/manage-data-assets-using-knowledge-catalog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage data assets using Knowledge Catalog

**Caution:** Data Catalog is [deprecated](https://docs.cloud.google.com/data-catalog/docs/deprecations) in favor of [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/introduction). Knowledge Catalog is also integrated with Bigtable, offering similar capabilities. You can use Knowledge Catalog to enrich your data with aspects, which are the equivalent of Data Catalog tags. For more information, see [Manage aspects and enrich metadata](https://docs.cloud.google.com/dataplex/docs/enrich-entries-metadata). 

Knowledge Catalog automatically catalogs metadata about Bigtable resources. This feature helps you search for and manage your Bigtable data assets.

Metadata is automatically synced from Bigtable to Knowledge Catalog for the following Bigtable resources:

  * Instances
  * Clusters
  * Tables, including column family details
  * Views:

    * Authorized views
    * Continuous materialized views
    * Logical views

Views don't have global catalog entries. To access view metadata, you must query the region assigned to your instance. For more information, see the Access view metadata section of this document.




Knowledge Catalog is a fully managed metadata management service. It provides unified view and tagging mechanisms for technical and business metadata. To learn more about Knowledge Catalog and why you should use it, see [Knowledge Catalog overview](https://docs.cloud.google.com/dataplex/docs/introduction).

## Benefits of using Knowledge Catalog with Bigtable

Information from Knowledge Catalog about your data helps support analysis, data reuse, application development, and data management.

You can search entries in Knowledge Catalog by details, such as resource name. For example, search for an instance name to find the entry for an instance, or search for a column family to find the entry for a table. You can also use faceted search, applying filters to refine your search. For more information, see [Search for resources in Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/search-assets).

Ingesting and cataloging [Bigtable views](https://docs.cloud.google.com/bigtable/docs/tables-and-views#views) lets you do the following:

  * Find granular data assets like authorized, logical, and continuous materialized views in a central inventory.
  * Gain visibility into which views exist and who has access to them, which lets governance teams apply policies and access controls.
  * Understand how authorized views connect to tables and logical and continuous materialized views connect to instances for better context.



Enriching metadata with _aspects_ helps you understand and catalog the data in your Bigtable tables. Aspects let you attach custom business and technical metadata to cataloged entries, making data more discoverable across your data estate and enabling targeted searches. For more information, see [Manage aspects and enrich metadata](https://docs.cloud.google.com/dataplex/docs/enrich-entries-metadata).

## Get started with Knowledge Catalog

To start using Knowledge Catalog to manage your Bigtable data assets, complete the following tasks:

  1. Optional: If you are new to Knowledge Catalog, [enable the Dataplex API](https://docs.cloud.google.com/dataplex/docs/enable-api).

  2. Grant IAM roles to principals who require access to Bigtable entries in Knowledge Catalog.

  3. Learn [how to search for data assets](https://docs.cloud.google.com/dataplex/docs/search-assets).

  4. Review [Knowledge Catalog search syntax](https://docs.cloud.google.com/dataplex/docs/search-syntax) to understand how to find your metadata.

  5. Read the concepts on managing metadata with aspects. For more information, see [About metadata in Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/metadata-overview).




## View metadata in Knowledge Catalog

Each Bigtable view type is represented as a distinct entry type in the catalog. Knowledge Catalog stores specific metadata (aspects) for each type:

View type | Metadata fields  
---|---  
Authorized view | Full subset definition, deletion protection status. The base table ID is part of the entry's resource path and parent entry, rather than a separate aspect field.  
Logical view | SQL query, schema, deletion protection status. The base table is referenced in the SQL query.  
Continuous materialized view | SQL query, schema, deletion protection status, storage details. The base table is referenced in the SQL query. In the storage aspect, the `sourceUri` field points to the view resource itself, not the base table.  
  
## Ways to search for Bigtable metadata

You can search synced Bigtable metadata using Knowledge Catalog.

In addition to [qualified predicates](https://docs.cloud.google.com/dataplex/docs/search-syntax#qualified-predicates), you can search for Bigtable resources with the following metadata fields:

  * Instance

    * Bigtable instance name
    * Bigtable instance ID
    * Cluster location
    * Cluster ID
  * Table

    * Table ID
    * Column family name
    * Bigtable instance name
    * Bigtable instance ID



You can search views by the following categories:

  * **View type** : 
    * `type=cloud-bigtable-authorized-view`
    * `type=cloud-bigtable-logical-view`
    * `type=cloud-bigtable-materialized-view`
  * **Unified view alias** : use the `VIEW` alias to find all types of Bigtable views simultaneously.
  * **Metadata details** : search by query text, parent resource, subset definition details, or specific attributes like deletion protection.
  * **Region** : in the Google Cloud console, use `location=LOCATION` or region filters to search for views or any other resource in a region.



When you view a global Bigtable instance or table entry in the Google Cloud console, its **Entry list** tab doesn't include regional views. Similarly, when you view a regional view entry, its breadcrumb trail doesn't link to its parent instance or table. To find these resources, search for them directly using the preceding search categories.

## Access view metadata

Unlike Bigtable instances and tables, views don't have global catalog entries. Metadata for views is stored exclusively in the region assigned to your instance in Knowledge Catalog (`knowledgeCatalogRegion`).

When you search for resources in Knowledge Catalog, you can use region filters to find views or any other resource in a specific region. However, when you use the Dataplex API or client libraries to look up, retrieve, or manage aspects on Bigtable views, you must specify the instance's Knowledge Catalog region in the `location` parameter of the request URL. If you specify the location as `global`, the command returns a `NOT_FOUND` error.

The following sections explain how to access view metadata in the region of your instance.

### Find the Knowledge Catalog region of an instance

To find the `knowledgeCatalogRegion` of your Bigtable instance, use the [`gcloud bigtable instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/describe) command:
    
    
    gcloud bigtable instances describe INSTANCE_ID
    

Replace `INSTANCE_ID` with the unique identifier of your instance.

The command output includes the `knowledgeCatalogRegion` field, as shown in the following example:
    
    
    createTime: '2026-01-15T10:00:00.000000Z'
    displayName: my-instance
    edition: ENTERPRISE
    knowledgeCatalogRegion: us-central1
    name: projects/my-project/instances/my-instance
    state: READY
    type: PRODUCTION
    

In this example, the location for Dataplex API requests and region filters for views in this instance is `us-central1`.

### Inspect a Knowledge Catalog entry of a view

### Console

To inspect a view's entry in Knowledge Catalog, follow these steps:

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. In the search field, enter the name or ID of the Bigtable view, or enter a search query, and then press `Enter`.

You can search for views using the following predicates:

     * All views: `VIEW`
     * Authorized views: `type=cloud-bigtable-authorized-view`
     * Logical views: `type=cloud-bigtable-logical-view`
     * Continuous materialized views: `type=cloud-bigtable-materialized-view`
     * Views by region: for example, `location=us-central1`
  3. To refine your search, click **Filters**.

  4. In the search results, click the view name to open the entry details page.

The entry details page displays all entry attributes, including overview information, system aspects, such as the SQL query, schema, or subset definition, and attached custom aspects.




### gcloud

To inspect the view's entry in Knowledge Catalog, use the [`gcloud dataplex entries lookup`](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/entries/lookup) command:
    
    
    gcloud dataplex entries lookup "VIEW_RESOURCE_NAME" \
        --project="PROJECT_ID" \
        --location="LOCATION" \
        --entry-group="@bigtable" \
        --view="all"
    

Replace the following:

  * `VIEW_RESOURCE_NAME`: the Bigtable resource path for the view (omitting the leading `//`). Construct the resource path based on the view type: 
    * Authorized view: `bigtable.googleapis.com/projects/PROJECT_ID/instances/INSTANCE_ID/tables/TABLE_ID/authorizedViews/VIEW_ID`
    * Logical view: `bigtable.googleapis.com/projects/PROJECT_ID/instances/INSTANCE_ID/logicalViews/VIEW_ID`
    * Continuous materialized view: `bigtable.googleapis.com/projects/PROJECT_ID/instances/INSTANCE_ID/materializedViews/VIEW_ID`
  * `PROJECT_ID`: the unique identifier of your Google Cloud project.
  * `INSTANCE_ID`: the unique identifier of your Bigtable instance.
  * `TABLE_ID`: for authorized views, the unique identifier of the base table that contains the view.
  * `VIEW_ID`: the identifier assigned to the view.
  * `LOCATION`: the Knowledge Catalog region of the Bigtable instance (for example, `us-central1`).



The output returns all entry attributes, including both system aspects and attached custom aspects. In the output, the `parentEntry` field contains a regional entry path for the parent table or instance. Because Bigtable stores table and instance entries only in the `global` location, this regional parent entry isn't accessible. To look up the parent table or instance entry, specify `global` as the location.

### REST

To look up a view entry programmatically by using the Dataplex API, send an authenticated HTTP `GET` request to the [`lookupEntry`](https://docs.cloud.google.com/dataplex/docs/reference/rest/v1/projects.locations/lookupEntry) method:
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION:lookupEntry?entry=projects/PROJECT_ID/locations/LOCATION/entryGroups/@bigtable/entries/VIEW_RESOURCE_NAME&view=ALL"
    

Replace the following:

  * `VIEW_RESOURCE_NAME`: the Bigtable resource path for the view (omitting the leading `//`). Construct the resource path based on the view type: 
    * Authorized view: `bigtable.googleapis.com/projects/PROJECT_ID/instances/INSTANCE_ID/tables/TABLE_ID/authorizedViews/VIEW_ID`
    * Logical view: `bigtable.googleapis.com/projects/PROJECT_ID/instances/INSTANCE_ID/logicalViews/VIEW_ID`
    * Continuous materialized view: `bigtable.googleapis.com/projects/PROJECT_ID/instances/INSTANCE_ID/materializedViews/VIEW_ID`
  * `PROJECT_ID`: the unique identifier of your Google Cloud project.
  * `INSTANCE_ID`: the unique identifier of your Bigtable instance.
  * `TABLE_ID`: for authorized views, the unique identifier of the base table that contains the view.
  * `VIEW_ID`: the identifier assigned to the view.
  * `LOCATION`: the Knowledge Catalog region of the Bigtable instance (for example, `us-central1`).



The output returns all entry attributes, including both system aspects and attached custom aspects. In the output, the `parentEntry` field contains a regional entry path for the parent table or instance. Because Bigtable stores table and instance entries only in the `global` location, this regional parent entry isn't accessible. To look up the parent table or instance entry, specify `global` as the location.

## Required roles

Viewing, tagging, and searching Bigtable resources in Knowledge Catalog have different permission requirements. In general, grant principals in your organization the minimum role required to accomplish a task.

### Permission to view public and private aspects

To get the permissions that you need to view public and private aspects on Bigtable resources, ask your administrator to grant you the following IAM roles:

  * [`roles/dataplex.catalogViewer`](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer)
  * [`roles/bigtable.viewer`](https://docs.cloud.google.com/bigtable/docs/access-control#bigtable.viewer)



These predefined roles contain the permissions required to view public and private aspects. The exact permissions that are required are the following:

  * `bigtable.instances.get`
  * `bigtable.clusters.get`
  * `bigtable.tables.get`
  * `dataplex.aspectTypes.get`



Views require the following permissions:

  * Authorized views: `bigtable.authorizedViews.get`
  * Logical views: `bigtable.logicalViews.get`
  * Continuous materialized views: `bigtable.materializedViews.get`



### Permission to search Bigtable resources

To get the permissions that you need to search Bigtable resources in Knowledge Catalog, ask your administrator to grant you the following IAM roles:

  * [`roles/bigtable.viewer`](https://docs.cloud.google.com/bigtable/docs/access-control#bigtable.viewer)



These predefined roles contain the permissions required to search Bigtable resources. The exact permissions that are required are the following:

  * `bigtable.instances.get`
  * `bigtable.clusters.get`
  * `bigtable.tables.get`



Views require the following permissions:

  * Authorized views: `bigtable.authorizedViews.get`
  * Logical views: `bigtable.logicalViews.get`
  * Continuous materialized views: `bigtable.materializedViews.get`



### Permission to search and view Bigtable metadata

To search for and view metadata for Bigtable resources, you must have a role that includes the following permissions:

  * Instances and tables: `bigtable.instances.get`, `bigtable.clusters.get`, `bigtable.tables.get`
  * Authorized views: `bigtable.authorizedViews.get`
  * Logical views: `bigtable.logicalViews.get`
  * Continuous materialized views: `bigtable.materializedViews.get`



Predefined roles such as [`roles/bigtable.viewer`](https://docs.cloud.google.com/bigtable/docs/access-control#bigtable.viewer) or [`roles/bigtable.admin`](https://docs.cloud.google.com/bigtable/docs/access-control#bigtable.admin) typically contain these permissions.

### Permission to attach aspects to Bigtable resources

To get the permissions that you need to attach aspects to Bigtable resources in Knowledge Catalog, ask your administrator to grant you the following IAM roles:

  * [`roles/dataplex.aspectTypeUser`](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.aspectTypeUser)
  * [`roles/dataplex.catalogEditor`](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor)
  * [`roles/bigtable.admin`](https://docs.cloud.google.com/bigtable/docs/access-control#bigtable.admin)



These predefined roles contain the permissions required to add public and private aspects. The exact permissions that are required are the following:

  * `bigtable.instances.update`
  * `bigtable.clusters.update`
  * `bigtable.tables.update`
  * `dataplex.aspectTypes.use`
  * `dataplex.entries.update`



Views require the following permissions:

  * Authorized views: `bigtable.authorizedViews.update`
  * Logical views: `bigtable.logicalViews.update`
  * Continuous materialized views: `bigtable.materializedViews.update`



### Optional: Create a custom role

You can create a custom role to grant to users who require complete access to all Bigtable metadata in Knowledge Catalog across your project or organization. Then you can assign any user or service account that needs access as a principal of the custom role. To learn more about custom roles, see [Roles and permissions](https://docs.cloud.google.com/iam/docs/roles-overview#custom).

Choose a meaningful name for the role, such as Bigtable Dataplex Editor, and then assign only the principals who need access to the role. For setup instructions, see [Create and manage custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating_a_custom_role).

Grant the following permissions to the custom role:

  * `bigtable.instances.get`
  * `bigtable.instances.update`
  * `bigtable.clusters.get`
  * `bigtable.clusters.update`
  * `bigtable.tables.get`
  * `bigtable.tables.update`
  * `bigtable.authorizedViews.get`
  * `bigtable.authorizedViews.update`
  * `bigtable.logicalViews.get`
  * `bigtable.logicalViews.update`
  * `bigtable.materializedViews.get`
  * `bigtable.materializedViews.update`
  * `dataplex.aspectTypes.get`
  * `dataplex.aspectTypes.use`



For more information, see [Knowledge Catalog IAM permissions](https://docs.cloud.google.com/dataplex/docs/iam-permissions). For descriptions of Bigtable permissions, see [Permissions](https://docs.cloud.google.com/bigtable/docs/access-control#permissions).

## Limitations

The following sections list constraints that you must consider before you use Knowledge Catalog to manage your Bigtable metadata.

### Location constraints

If your organization enforces [location constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations), metadata entries for your Bigtable resources might not sync to Knowledge Catalog. Any entries created before enforcing location constraints are retained by Knowledge Catalog.

To let Knowledge Catalog load resources, make sure your location policy permits the following:

  * The `global` multi-region for instances and tables.
  * The specific region that matches your instance's `knowledgeCatalogRegion` for views.



### Column family name exception

The Dataplex API rejects requests where the column family name in your request includes a period (`.`). For example, if the column family name is `personal.info`.

## What's next

  * [Read an overview of Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/introduction).
  * [Explore additional Google Cloud integrations with Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/connectors).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 

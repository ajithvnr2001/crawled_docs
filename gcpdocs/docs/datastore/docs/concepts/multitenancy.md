---
url: https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/
title: Multitenancy \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:04:39.205466+00:00
---

# Multitenancy  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/

[ Skip to main content ](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/)
  * [Deutsch](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/?hl=de)
  * [Español](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/?hl=es-419)
  * [Français](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/?hl=id)
  * [Italiano](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/?hl=it)
  * [Português](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/?hl=ja)
  * [한국어](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fdatastore%2Fdocs%2Fconcepts%2Fmultitenancy%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/databases-color.svg) ](https://docs.cloud.google.com/datastore/docs)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Benefits of multitenancy](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/#benefits_of_multitenancy)
  * [Multitenancy and partitioned data](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/#multitenancy_and_partitioned_data)
  * [Specifying a namespace for an entity](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/#specifying_a_namespace_for_an_entity)
  * [Using namespaces with parent entities](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/#using_namespaces_with_parent_entities)
  * [Sample use case](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/#sample_use_case)
  * [Viewing namespaces in the console](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/#viewing_namespaces_in_the_console)
  * [What's next](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/#whats_next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Guides ](https://docs.cloud.google.com/datastore/docs/concepts/overview)


Was this helpful?
Send feedback 
#  Multitenancy Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Benefits of multitenancy](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/#benefits_of_multitenancy)
  * [Multitenancy and partitioned data](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/#multitenancy_and_partitioned_data)
  * [Specifying a namespace for an entity](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/#specifying_a_namespace_for_an_entity)
  * [Using namespaces with parent entities](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/#using_namespaces_with_parent_entities)
  * [Sample use case](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/#sample_use_case)
  * [Viewing namespaces in the console](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/#viewing_namespaces_in_the_console)
  * [What's next](https://docs.cloud.google.com/datastore/docs/concepts/multitenancy/#whats_next)


You can support _multitenancy_ in your application by providing separate data partitions for multiple client organizations, known as tenants. This allows you to customize _data values_ for each tenant, while keeping the same _data schema_ for all tenants. This makes provisioning new tenants more efficient because you don't have to change data structure when you add a tenant.
## Benefits of multitenancy
Firestore in Datastore mode allows a multitenant application to use separated silos of data for each tenant while still using:
  * a single project
  * a single logical structure for the kinds
  * a single set of index definitions, because the kinds are the same logically for each tenant


Datastore mode enables multitenancy by providing _namespaces_.
## Multitenancy and partitioned data
Datastore mode uses _partitions_ to silo data for each tenant. The combination of a project ID and a namespace ID forms a _partition ID_ , which identifies each partition. An entity belongs to a single partition, and queries are scoped to a single partition.
## Specifying a namespace for an entity
You specify the namespace when you create the entity: after you create the entity, you cannot change the namespace. If you don't explicitly specify a namespace for an entity, it is automatically assigned to the _default namespace_ , which has no string identifier.
## Using namespaces with parent entities
An entity and all of its ancestors belong to one and only one namespace. This means that when you create an entity with another entity designated as parent, the child entity is in the same namespace as its parent: you cannot specify some other namespace.
## Sample use case
A key benefit of multitenancy is having the same application serve multiple client organizations. To achieve this benefit, for a given kind, your application should behave the same regardless of the namespace. For example, from the application’s perspective, an entity of kind `Task` in one namespace should logically be the same as an entity of kind `Task` in all other namespaces. Your application could then use a single set of index definitions to support `Task` queries, regardless of which namespaces contain `Task` entities.
For example, consider a Task List application that silos data on a per user basis. The application could define namespaces based on user name, resulting in the following partitions:

```
Partition ID: project:"my_project_id"/namespace:"Joe"
Partition ID: project:"my_project_id"/namespace:"Alice"
Partition ID: project:"my_project_id"/namespace:"Charlie"

```

The application could define a logical structure of a `Task` kind as follows, to use for all namespaces:

```
kind: Task
properties:
 - "done", Boolean
 - "created", DateTime
 - "description", String, excluded from index

```

When a user creates an entity of kind `Task`, the entity is stored in the user’s own partition, resulting in siloed data. The application processes `Task` entities consistently across namespaces because only one schema is used for the `Task` kind. An application with siloed data and consistent behaviour would be multitenant.
If the logical structure of a `Task` kind differs by namespace, the application would not be multitenant because it processes `Task` entities differently across namespaces. For example, consider `Task` kinds that have different schema based on namespace:
  * `Task` entities in the Joe namespace _exclude_ the `description` property from the index
  * `Task` entities in the Alice namespace _include_ the `description` property from the index


The application could query on the `description` property for Alice’s `Task` entities, but it could not query on the `description` property for Joe’s `Task` entities, so the application would not be multitenant.
## Viewing namespaces in the console
To see statistics for the namespaces used in your project, visit the [Datastore Dashboard](https://console.cloud.google.com/datastore/stats) page in the Google Cloud console. To programmatically determine which namespaces are used in your project, see [Namespace queries](https://docs.cloud.google.com/datastore/docs/concepts/metadataqueries#namespace_queries).
If you need to group data _within_ a tenant, you can categorize your data by [kinds](https://docs.cloud.google.com/datastore/docs/concepts/entities#kinds_and_identifiers), and you can also organize highly related data with [entity groups](https://docs.cloud.google.com/datastore/docs/concepts/entities#entity_groups).
## What's next
  * Learn about [entities](https://docs.cloud.google.com/datastore/docs/concepts/entities).
  * Learn about [queries](https://docs.cloud.google.com/datastore/docs/concepts/queries).


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

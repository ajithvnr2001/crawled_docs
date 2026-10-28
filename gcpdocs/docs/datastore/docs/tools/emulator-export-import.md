---
url: https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/
title: Exporting and importing emulator data \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:03:15.770680+00:00
---

# Exporting and importing emulator data  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/

[ Skip to main content ](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/)
  * [Deutsch](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/?hl=de)
  * [Español](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/?hl=es-419)
  * [Français](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/?hl=id)
  * [Italiano](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/?hl=it)
  * [Português](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/?hl=ja)
  * [한국어](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/databases-color.svg) ](https://docs.cloud.google.com/datastore/docs)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/#before_you_begin)
  * [Import entities into the emulator](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/#import_entities_into_the_emulator)
    * [Import entities from specific kinds and namespaces](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/#import_entities_from_specific_kinds_and_namespaces)
  * [Export entities in the emulator](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/#export_entities_in_the_emulator)
    * [Export entities from specific kinds and namespaces](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/#export_entities_from_specific_kinds_and_namespaces)
    * [Load emulator data into your database](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/#load_emulator_data_into_your_database)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Guides ](https://docs.cloud.google.com/datastore/docs/concepts/overview)


Was this helpful?
Send feedback 
#  Exporting and importing emulator data Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/#before_you_begin)
  * [Import entities into the emulator](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/#import_entities_into_the_emulator)
    * [Import entities from specific kinds and namespaces](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/#import_entities_from_specific_kinds_and_namespaces)
  * [Export entities in the emulator](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/#export_entities_in_the_emulator)
    * [Export entities from specific kinds and namespaces](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/#export_entities_from_specific_kinds_and_namespaces)
    * [Load emulator data into your database](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/#load_emulator_data_into_your_database)


Using the import and export features of the Datastore emulator, you can export data from your database instance and load it into the emulator. You can also export data from the emulator and load it into your Datastore mode database.
## Before you begin
Before you use the import or export features of the Datastore emulator, complete the following:
  * [Start the Datastore emulator.](https://docs.cloud.google.com/datastore/docs/tools/datastore-emulator)
The import and export features are available for `cloud-datastore-emulator` versions 2.1.0 and greater. You may need to [update your Google Cloud CLI components](https://docs.cloud.google.com/sdk/docs/components#updating_components).
  * For import operations, make sure your entity export files are on the same machine as the emulator.


## Import entities into the emulator
The emulator's import feature lets you load entities from a set of entity export files into the emulator. The entity export files can come from an export of your Datastore mode database or of an emulator instance.
To import entities into the emulator, send a `POST` import request to the emulator. You can use [curl](https://curl.haxx.se/) or a similar tool. For example, the following request will import all entities from a set of entity export files into the emulator:
[Protocol](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/#protocol) More

```
curl -X POST localhost:8081/v1/projects/[PROJECT_ID]:import \
-H 'Content-Type: application/json' \
-d '{"input_url":"[ENTITY_EXPORT_FILES]"}'

```
Modify `localhost:8081` if the emulator uses a different port.
where:
  * `[PROJECT_ID]` is the ID of your project.
  * `[ENTITY_EXPORT_FILES]` is the path to the `overall_export_metadata` file of your entity export files. For example:
`{"input_url":"/home/user/myexports/2019-02-04T19:39:33_443/2019-02-04T19:39:33_443.overall_export_metadata"}`


### Import entities from specific kinds and namespaces
You can specify an entity filter to import entities from only specific kinds or namespaces. You can specify an entity filter only if the export was created using an entity filter.
Specify kinds or namespaces in an entity filter:
[Protocol](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/#protocol) More

```
curl -X POST localhost:8081/v1/projects/[PROJECT_ID]:import \
-H 'Content-Type: application/json' \
-d '{"input_url":"[ENTITY_EXPORT_FILES]",
"entity_filter":{"kinds":[[KIND_NAMES]], "namespace_ids":[[NAMESPACES]]}}'

```
Modify `localhost:8081` if the emulator uses a different port.
where:
  * `[PROJECT_ID]` is the ID of your project.
  * `[ENTITY_EXPORT_FILES]` is the path to the `overall_export_metadata` file of your entity export files. For example:
`{"input_url":"/home/user/myexports/2019-02-04T19:39:33_443/2019-02-04T19:39:33_443.overall_export_metadata"}`
  * `[KIND_NAMES]` is a list of kinds: `"kinds":["KIND_1", "KIND_2"]`
  * `[NAMESPACES]` is a list of namespace IDs:
`"namespace_ids":["NAMESPACE_1", "NAMESPACE_2"]`


## Export entities in the emulator
The emulator's export feature lets you save entities in the emulator into a set of entity export files. You can then use an import operation to load the entities in the entity export files into your Datastore mode database or into an emulator instance.
To export entities in an emulator instance, send a `POST` export request to the emulator. You can use [curl](https://curl.haxx.se/) or a similar tool. For example, the following request will export all entities in the emulator:
[Protocol](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/#protocol) More

```
curl -X POST localhost:8081/v1/projects/[PROJECT_ID]:export \
-H 'Content-Type: application/json' \
-d '{"output_url_prefix":"EXPORT_DIRECTORY"}'

```
Modify `localhost:8081` if the emulator uses a different port.
where:
  * `[PROJECT_ID]` is the ID of your project.
  * `[EXPORT_DIRECTORY]` specifies the directory where the emulator saves the entity export files. This directory must not already contain a set of entity export files. For example:
`{"output_url_prefix":"/home/user/myexports/2019-02-04/"}`


Export entities from specific kinds and namespaces You can specify an entity filter to export entities from only specific kinds or namespaces. Specify kinds or namespaces in an entity filter: [Protocol](https://docs.cloud.google.com/datastore/docs/tools/emulator-export-import/#protocol) More 
```
curl -X POST localhost:8081/v1/projects/[PROJECT_ID]:export \
-H 'Content-Type: application/json' \
-d '{"output_url_prefix":"EXPORT_DIRECTORY",
"entity_filter":{"kinds":[[KIND_NAMES]], "namespace_ids":[[NAMESPACES]]}}'

```
Modify `localhost:8081` if the emulator uses a different port. where:
  * `[PROJECT_ID]` is the ID of your project.
  * `[EXPORT_DIRECTORY]` specifies the directory where the emulator saves the entity export files. This directory must not already contain a set of entity export files. For example: {"output_url_prefix":"/home/user/myexports/2019-02-04/"}``
  * `[KIND_NAMES]` is a list of kinds: `"kinds":["KIND_1", "KIND_2"]`
  * `[NAMESPACES]` is a list of namespace IDs: `"namespace_ids":["NAMESPACE_1", "NAMESPACE_2"]`

Load emulator data into your database Entity export files created by the emulator are compatible with the managed import feature for Datastore mode databases.
Before you can load entities exported from the emulator into your database, you must [upload your entity export files to a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/uploading-objects). The managed import feature reads only from Cloud Storage buckets.
Once your entity export files are available in a Cloud Storage bucket, you can import the data into your database as described in [Exporting and importing entities](https://docs.cloud.google.com/datastore/docs/export-import-entities).
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

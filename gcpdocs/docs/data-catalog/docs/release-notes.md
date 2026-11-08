---
url: https://docs.cloud.google.com/data-catalog/docs/release-notes/
title: Data Catalog release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-08T09:14:25.409475+00:00
---

# Data Catalog release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-catalog/docs/release-notes/

Data Catalog is deprecated and will be discontinued on June 1, 2026. For steps to transition your Data Catalog users, workloads, and content to Knowledge Catalog (formerly Dataplex Universal Catalog), see [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Catalog ](https://docs.cloud.google.com/data-catalog/docs)
  * [ Resources ](https://docs.cloud.google.com/data-catalog/docs/resources)



Send feedback 

#  Data Catalog release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Data Catalog. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/data-catalog-release-notes.xml) directly. 

## September 19, 2023

v1

Announcement

Data Catalog is available in the me-central2 (Dammam) region.

For more information, see [Regions](https://docs.cloud.google.com/data-catalog/docs/concepts/regions).

## September 06, 2023

v1

Announcement

Data Catalog is now available in Berlin (`europe-west10`). For more information on region and feature availability, see [regions](https://docs.cloud.google.com/data-catalog/docs/concepts/regions).

## July 31, 2023

v1

Announcement

Data Catalog is now available in the Oregon (`aws-us-west-2`) and Ireland (`aws-eu-west-1`) regions. For more information on region and feature availability, see [regions](https://docs.cloud.google.com/data-catalog/docs/concepts/regions).

## September 23, 2020

v1

Change

Exposed API for a policy tag manager: `PolicyTag` messages and RPCs.

## September 04, 2020

v1

Feature

Data Catalog is now available in Jakarta (`asia-southeast2`).

## July 24, 2020

v1

Feature

Data Catalog is now available in Seoul (`asia-northeast3`).

## July 20, 2020

v1

Feature

Data Catalog is now available in Salt Lake City (`us-west3`) and Las Vegas (`us-west4`).

## June 14, 2020

v1

Change

Exposed the new `RenameTagTemplateFieldEnumValue` API method.

## May 07, 2020

v1

Change

Added an enum value for BigQuery materialized views in the `TableSourceType` of the entry API resource.

## April 30, 2020

v1

Feature

Data Catalog is now generally available (GA). \- The Data Catalog v1 API, gcloud commands, and UI are now available. For details, [see the API reference](https://docs.cloud.google.com/data-catalog/docs/reference). Code samples throughout the documentation have been updated to use the new API. \- Data Catalog has been regionalized, and now hosts user metadata in [23 regions worldwide](https://docs.cloud.google.com/data-catalog/docs/concepts/regions). \- Billing has been enabled for Data Catalog API calls and storage using all supported resources. For more info, see the [pricing page](https://cloud.google.com/data-catalog/pricing).

## March 12, 2020

v1beta1

Feature

[Support for custom entries](https://docs.cloud.google.com/data-catalog/docs/how-to/custom-entries) is now in beta. This feature lets you ingest metadata of any type, so it can be tagged and searched in Data Catalog.

## January 27, 2020

v1beta1

Feature

Data Catalog users, when creating a tag template, can now specify an attribute as [required](https://cloud.google.com/data-catalog/docs/reference/rest/v1beta1/projects.locations.tagTemplates.fields#TagTemplateField.SCHEMA_REPRESENTATION) ([Beta](https://docs.cloud.google.com/terms/launch-stages#launch-stages) release). A tag cannot be created unless all the required attributes are populated with valid values. For an example, see [Create a tag template and attach the tag to your table](https://docs.cloud.google.com/data-catalog/docs/quickstarts/quickstart-search-tag#create_a_tag_template_and_attach_tags_to_your_table).

## January 21, 2020

v1beta1

Change

IAM policies are no longer available for individual entries, but still are available for tag templates and entry groups. With this change, users will not be able to set ACLs for individual entries such as filesets, only for tag templates and entry groups. Each fileset belongs to an entry group and an entry group can contain multiple filesets or entries.

This change is relevant to users who have created filesets in Data Catalog. Data Catalog users who do not have filesets are not impacted by this change.

## June 27, 2019

v1beta1

Feature

Announcing the [Beta](https://cloud.google.com/terms/launch-stages#launch-stages) release of [Data Catalog](https://docs.cloud.google.com/data-catalog/docs), a fully managed and scalable metadata management service that allows organizations to quickly discover, manage, and understand their data in Google Cloud.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 

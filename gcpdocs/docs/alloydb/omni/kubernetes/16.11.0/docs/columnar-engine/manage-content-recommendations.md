---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/
title: Manage column store content using auto-columnarization \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 16.11.0 \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:37:09.713349+00:00
---

# Manage column store content using auto-columnarization  |  AlloyDB Omni using the container orchestrator: 16.11.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/

[ Skip to main content ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/)
  * [Deutsch](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/?hl=es-419)
  * [Français](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/?hl=id)
  * [Italiano](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/?hl=ja)
  * [한국어](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Falloydb%2Fomni%2Fkubernetes%2F16.11.0%2Fdocs%2Fcolumnar-engine%2Fmanage-content-recommendations%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/alloydb-color.svg) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/overview)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/overview)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Run auto-columnarization immediately](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/#default-schedule)
  * [Change the default schedule for auto-columnarization](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/#auto-schedule)
  * [View information about recommended columns](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/#view-recommended-columns)
  * [Reset auto-columnarization and remove recommended columns](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/#reset-auto)
  * [Recommend column store memory size](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/#recommend-populate)
  * [Disable auto-columnarization](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/#disable-auto)


This page documents AlloyDB Omni version **16.11.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/overview)


Was this helpful?
Send feedback 
#  Manage column store content using auto-columnarization Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Run auto-columnarization immediately](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/#default-schedule)
  * [Change the default schedule for auto-columnarization](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/#auto-schedule)
  * [View information about recommended columns](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/#view-recommended-columns)
  * [Reset auto-columnarization and remove recommended columns](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/#reset-auto)
  * [Recommend column store memory size](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/#recommend-populate)
  * [Disable auto-columnarization](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/#disable-auto)


Select a documentation version:  16.11.0keyboard_arrow_down
  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/columnar-engine/manage-content-recommendations)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/columnar-engine/manage-content-recommendations)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/columnar-engine/manage-content-recommendations)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/columnar-engine/manage-content-recommendations)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/columnar-engine/manage-content-recommendations)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/columnar-engine/manage-content-recommendations)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/columnar-engine/manage-content-recommendations)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/columnar-engine/manage-content-recommendations)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/manage-content-recommendations)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/columnar-engine/manage-content-recommendations)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/columnar-engine/manage-content-recommendations)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/columnar-engine/manage-content-recommendations)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/columnar-engine/manage-content-recommendations)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/columnar-engine/manage-content-recommendations)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/columnar-engine/manage-content-recommendations)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/columnar-engine/manage-content-recommendations)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/columnar-engine/manage-content-recommendations)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/columnar-engine/manage-content-recommendations)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/columnar-engine/manage-content-recommendations)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/columnar-engine/manage-content-recommendations)

This page describes how to manage the content of the columnar engine's column store using auto-columnarization. 
By using auto-columnarization, the columnar engine automatically columnarizes the data in the column store and improves the overall performance of your hybrid transactional and analytical processing (HTAP) and online analytical processing (OLAP) workloads.
The columnar engine samples an application workload and analyzes queries to determine which columns are good hypothetical candidates for inclusion in the column store. It also populates columns automatically to the column store that provides the best performance gains after considering the current column store memory size.
New instances have auto-columnarization enabled by default, configured to recommend and populate columns to the column store once every hour. You can either [run auto-columnarization immediately](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations#default-schedule) or [change the default schedule of every hour](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations#auto-schedule) to a chosen time interval to run auto-columnarization.
When an instance restarts, the columnar engine clears the previously recommended and populated columns, and restarts auto-columnarization.
After auto-columnarization recommends columns, you can review the results of the recommendations by [viewing recommended columns](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations#view-recommended-columns).
## Run auto-columnarization immediately
You can run auto-columnariation immediately before the default schedule takes effect.
To run auto-columnarization immediately:
[psql Client](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/#psql-client) More

```
SELECT google_columnar_engine_recommend();

```

## Change the default schedule for auto-columnarization
To change an instance's default schedule to run auto-columnarization, set that instance's [`google_columnar_engine.auto_columnarization_schedule`](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/reference/columnar-engine-flags#auto-columnarization-schedule) flag to a new time interval.
The flag takes the value `EVERY NUMBER {HOURS|DAYS}`. For example: `EVERY 12 HOURS`, or `EVERY 2 DAYS`.
## View information about recommended columns
You can view information about the size of recommended columns, list of recommended columns, and recommendation schedule.
To view the list and the size of recommended columns, follow these steps:
[psql Client](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/#psql-client) More

```
SELECT database_name, schema_name, relation_name, column_name, estimated_size_in_bytes FROM g_columnar_recommended_columns;

```

To view the column recommendation schedule:
[psql Client](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/#psql-client) More

```
SELECT * FROM g_columnar_schedules;

```

## Reset auto-columnarization and remove recommended columns
You can reset auto-columnarization, including all data it has gathered to generate recommendations.
This removes columns that were automatically added to the column store by auto-columnarization.
To reset auto-columnarization:
[psql Client](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/#psql-client) More

```
SELECT google_columnar_engine_reset_recommendation(drop_columns => true);

```

## Recommend column store memory size
The columnar engine can recommend the best column store memory size along with the list of columns for your workload that provides the highest performance gains.
You can update `google_columnar_engine.memory_size_in_mb` based on the recommendations.
To view the recommended memory size for the column store, follow these instructions:
[psql Client](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-recommendations/#psql-client) More

```
SELECT * FROM google_columnar_engine_recommend(mode => 'RECOMMEND_SIZE');

```

## Disable auto-columnarization
To disable auto-columnarization on a primary or read pool instance, set the instance's [`google_columnar_engine.enable_auto_columnarization`](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/reference/columnar-engine-flags#enable-auto-columnarization) flag to `off`.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

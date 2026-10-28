---
url: https://docs.cloud.google.com/database-migration/docs/mysql/about-connection-profiles/
title: About source connection profiles \u00a0|\u00a0 Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:11:58.534812+00:00
---

# About source connection profiles  |  Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/about-connection-profiles/

[ Skip to main content ](https://docs.cloud.google.com/database-migration/docs/mysql/about-connection-profiles/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/database-migration/docs/mysql/about-connection-profiles/)
  * [Deutsch](https://docs.cloud.google.com/database-migration/docs/mysql/about-connection-profiles/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/database-migration/docs/mysql/about-connection-profiles/?hl=es-419)
  * [Français](https://docs.cloud.google.com/database-migration/docs/mysql/about-connection-profiles/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/database-migration/docs/mysql/about-connection-profiles/?hl=id)
  * [Italiano](https://docs.cloud.google.com/database-migration/docs/mysql/about-connection-profiles/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/database-migration/docs/mysql/about-connection-profiles/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/database-migration/docs/mysql/about-connection-profiles/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/database-migration/docs/mysql/about-connection-profiles/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/database-migration/docs/mysql/about-connection-profiles/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/database-migration/docs/mysql/about-connection-profiles/?hl=ja)
  * [한국어](https://docs.cloud.google.com/database-migration/docs/mysql/about-connection-profiles/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fdatabase-migration%2Fdocs%2Fmysql%2Fabout-connection-profiles%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/databases-color.svg) ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [What's next](https://docs.cloud.google.com/database-migration/docs/mysql/about-connection-profiles/#whats_next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview)


Was this helpful?
Send feedback 
#  About source connection profiles Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [What's next](https://docs.cloud.google.com/database-migration/docs/mysql/about-connection-profiles/#whats_next)


Connection profiles capture identifiers for your source databases. For homogeneous migrations, Database Migration Service requires that you create source connection profiles when you migrate with the Google Cloud console.
_Destination connection profiles_ are required only if you use Google Cloud CLI for homogeneous migrations. You also can't view or manage destination connection profiles in the Google Cloud console.
Each connection profile contains the minimum required amount of information Database Migration Service needs to facilitate data movement between your source database and destination database. That information includes:
  * **Connection profile name** : A human-readable name for your connection profile. This value is displayed in Database Migration Service in the Google Cloud console.
  * **Connection profile ID** : A machine-readable identifier for your connection profile. This value is used when you work with connection profiles by using Database Migration Service Google Cloud CLI commands or API.
  * **Region** : The region where your connection profile is saved. Database Migration Service is a fully-regional product, meaning all entities related to your migration (source and destination connection profiles, migration jobs, destination databases) must be saved in a single region. For more information on region requirements in Database Migration Service, see [ Product overview](https://docs.cloud.google.com/database-migration/docs/overview) in the main Database Migration Service documentation set.
  * **Source database connection information** : The hostname or IP address, port, and username and password for Database Migration Service to connect to your source database.


## What's next
  * [ Create a source connection profile](https://docs.cloud.google.com/database-migration/docs/mysql/create-connection-profiles)
  * [ Manage connection profiles](https://docs.cloud.google.com/database-migration/docs/mysql/manage-connection-profiles)


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

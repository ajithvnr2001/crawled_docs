---
url: https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer/
title: Create and run a MySQL migration job containing metadata with a DEFINER clause \u00a0|\u00a0 Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:51:53.547186+00:00
---

# Create and run a MySQL migration job containing metadata with a DEFINER clause  |  Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer/

[ Skip to main content ](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer/)
  * [Deutsch](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer/?hl=de)
  * [Español](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer/?hl=es-419)
  * [Français](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer/?hl=id)
  * [Italiano](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer/?hl=it)
  * [Português](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer/?hl=ja)
  * [한국어](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/databases-color.svg) ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)


[Start free](https://console.cloud.google.com/freetrial)
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview)


Was this helpful?
Send feedback 
#  Create and run a MySQL migration job containing metadata with a DEFINER clause Stay organized with collections  Save and categorize content based on your preferences.
A MySQL migration job [ doesn't migrate user accounts and logins](https://docs.cloud.google.com/database-migration/docs/mysql/migration-fidelity). Sources that contain metadata defined by users with the `DEFINER` clause fail when invoked on the new Cloud SQL replica, because the users don't yet exist there.
To identify which `DEFINER` values exist in your metadata, query your MySQL source database. Check the results for entries for either `root%localhost` or for users that don't exist in the destination instance:

```
SELECT DISTINCT DEFINER FROM INFORMATION_SCHEMA.EVENTS WHERE EVENT_SCHEMA NOT 
IN ('mysql', 'sys');
SELECT DISTINCT DEFINER FROM INFORMATION_SCHEMA.ROUTINES WHERE ROUTINE_SCHEMA NOT 
IN ('mysql', 'sys');
SELECT DISTINCT DEFINER FROM INFORMATION_SCHEMA.TRIGGERS WHERE TRIGGER_SCHEMA NOT 
IN ('mysql', 'sys');
SELECT DISTINCT DEFINER FROM INFORMATION_SCHEMA.VIEWS WHERE TABLE_SCHEMA NOT 
IN ('mysql', 'sys');

```

To run a migration job from a source that includes such metadata, do one of the following:
  1. Create the users on the destination Cloud SQL replica instance before starting your migration job.
    1. To create a draft migration job without starting it, select **Create** instead of **Create & Start**.
    2. On your destination Cloud SQL instance, recreate the users from your source MySQL instance by using the Cloud SQL API or the Google Cloud console.
    3. From the list of migration jobs or the page for the specific job, start the migration job.
  2. Update the `DEFINER` clause to `INVOKER` on your source MySQL instance prior to setting up your migration job.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/database-center/docs/view-inventory/
title: View your fleet inventory \u00a0|\u00a0 Database Center \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:01:10.952564+00:00
---

# View your fleet inventory  |  Database Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/view-inventory/

[ Skip to main content ](https://docs.cloud.google.com/database-center/docs/view-inventory/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/database-center/docs/view-inventory/)
  * [Deutsch](https://docs.cloud.google.com/database-center/docs/view-inventory/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/database-center/docs/view-inventory/?hl=es-419)
  * [Français](https://docs.cloud.google.com/database-center/docs/view-inventory/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/database-center/docs/view-inventory/?hl=id)
  * [Italiano](https://docs.cloud.google.com/database-center/docs/view-inventory/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/database-center/docs/view-inventory/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/database-center/docs/view-inventory/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/database-center/docs/view-inventory/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/database-center/docs/view-inventory/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/database-center/docs/view-inventory/?hl=ja)
  * [한국어](https://docs.cloud.google.com/database-center/docs/view-inventory/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/databases-color.svg) ](https://docs.cloud.google.com/database-center/docs)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/database-center/docs/view-inventory/#before-you-begin)
  * [View information about your database inventory](https://docs.cloud.google.com/database-center/docs/view-inventory/#view-db-inventory)
    * [Fleet inventory insights](https://docs.cloud.google.com/database-center/docs/view-inventory/#fleet-inventory-insights)
    * [View resource inventory by product](https://docs.cloud.google.com/database-center/docs/view-inventory/#view-by-product)
    * [View resource inventory by product and version](https://docs.cloud.google.com/database-center/docs/view-inventory/#view-by-product-version)
    * [View resource inventory by location](https://docs.cloud.google.com/database-center/docs/view-inventory/#view-by-location)
    * [View resource inventory by labels and tags](https://docs.cloud.google.com/database-center/docs/view-inventory/#view-by-labels-tags)
  * [What's next](https://docs.cloud.google.com/database-center/docs/view-inventory/#what-next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs)
  * [ Guides ](https://docs.cloud.google.com/database-center/docs/overview)


Send feedback 
#  View your fleet inventory Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/database-center/docs/view-inventory/#before-you-begin)
  * [View information about your database inventory](https://docs.cloud.google.com/database-center/docs/view-inventory/#view-db-inventory)
    * [Fleet inventory insights](https://docs.cloud.google.com/database-center/docs/view-inventory/#fleet-inventory-insights)
    * [View resource inventory by product](https://docs.cloud.google.com/database-center/docs/view-inventory/#view-by-product)
    * [View resource inventory by product and version](https://docs.cloud.google.com/database-center/docs/view-inventory/#view-by-product-version)
    * [View resource inventory by location](https://docs.cloud.google.com/database-center/docs/view-inventory/#view-by-location)
    * [View resource inventory by labels and tags](https://docs.cloud.google.com/database-center/docs/view-inventory/#view-by-labels-tags)
  * [What's next](https://docs.cloud.google.com/database-center/docs/view-inventory/#what-next)


Database Center lets you view an inventory of the resources in your database fleet. The **Inventory** page shows you resource inventory information, such as the following:
  * The number of resources used by each product, such as Spanner, AlloyDB for PostgreSQL, and Bigtable.
  * The number of resources used by each product version in your fleet, such as Cloud SQL for MySQL 8.0, Cloud SQL for PostgreSQL 16, and Firestore with MongoDB compatibility.
  * Your database inventory filtered by labels and tags.
  * The inventory of resources by location, such as the `europe-north1` and the `us-west1` regions.


## Before you begin
  * [Ensure that Database Center is set up for your organization](https://docs.cloud.google.com/database-center/docs/set-up-database-center).
  * To enable the Gemini Cloud Assist button, ensure that you have the `geminicloudassist.investigations.create` Identity and Access Management (IAM) permission. For more information, see [Grant or revoke a single IAM role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#single-role).
  * To view [fleet inventory insights](https://docs.cloud.google.com/database-center/docs/view-inventory/#fleet-inventory-insights), esure you have the `roles/recommender.viewer` (iam_name_short) permission.


## View information about your database inventory
The **Inventory** page includes cards that display unique information about your database inventory. To view all your database inventory information, do the following:
  1. Go to the **Inventory** page in Database Center.
[Go to Database Center](https://console.cloud.google.com/database-center/inventory)


After the **Inventory** page opens, use the following topics to view your fleet inventory by product, product and version, location, labels, or tags.
### Fleet inventory insights
The **Fleet inventory insights** section displays cards that highlight inventory insights that are generated by Gemini. Use these insights to help you identify and understand specific issues in your database fleet.
Each card includes a **View resources** link. When you click **View resources** , the following information appears:
  * A detailed description of the issue.
  * A table listing the resources that exhibit the issue. The table includes the database product, the Google Cloud project, and metrics specific to the issue.


From the table, click the name of a resource to view its details in the product that uses it. 
### View resource inventory by product
To view resources in your database fleet by product, follow these steps:
  1. In the **Types of resources** card, view the number of resources used by each product. The managed database products are listed together, and the self-managed database products are listed together.
  2. Optional: Click **View all** next to a database product to view details about its resources in the **Resources** page of Database Center.


### View resource inventory by product and version
To view resources in your database fleet by product and version, follow these steps:
  1. In the **Product version** card, view the number of resources sorted by product and version. This card shows you the total number of database groups, resources, and new resources in your database fleet by product and version.
  2. Optional: Click filter_list **Filter** to filter resources in the **Product version** card by database version.
  3. Optional: To change the duration for added new resources, click **1 day** , **7 days** (default), or **30 days**.
  4. Optional: To view details about new resources, click **View inventory changes for the last X number of days** , where **X** is 1, 7, or 30, based on your previous selection. A pane in the Google Cloud console opens with your resource details.
  5. Optional: To view details about the resources for a version of a product, click **View resource details** in the **Product version** card. The **Resources** page in Database Center opens and shows information about resources used by that version of the product.


### View resource inventory by location
To view resources in your database fleet by location, follow these steps:
  1. In the **Location** card, view the number of resources sorted by region.
  2. Optional: Click filter_list **Filter** to filter resources in the **Location** card by database region.
  3. Optional: To view resources by an area on the map, pan and zoom to the area you want to view.
  4. Optional: To view details about the resources in a location, click **View resource details** in the **Location** card. The **Resources** page in Database Center opens and shows information about resources used in that location.


For more information, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).
### View resource inventory by labels and tags
To view resources in your database fleet by labels, tags, or both, follow these steps:
  1. In the **Labels** card, view the number of resources by labels.
  2. In the **Tags** card, view the number of resources by tags.
  3. Optional: Click filter_list **Filter** in the **Labels** or **Tags** card to filter the resources by labels or tags.
  4. Optional: To view details about the resources that use a label or a tag, click **View resource details** in the **Label** card or **Tag** card. The **Resources** page in Database Center opens and shows information about resources with that label or tag.


## What's next
  * Learn more about the [Database Center](https://docs.cloud.google.com/database-center/docs/overview).
  * Learn how to [customize your database fleet view](https://docs.cloud.google.com/database-center/docs/customize-database-fleet-view).
  * Learn how to [analyze database fleet health using Gemini](https://docs.cloud.google.com/database-center/docs/analyze-database-using-gemini).


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

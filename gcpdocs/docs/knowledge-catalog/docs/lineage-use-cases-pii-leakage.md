---
url: https://docs.cloud.google.com/knowledge-catalog/docs/lineage-use-cases-pii-leakage/
title: Analyze causes of personally identifiable information (PII) leak \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-25T05:55:37.688110+00:00
---

# Analyze causes of personally identifiable information (PII) leak  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/lineage-use-cases-pii-leakage/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Analyze causes of personally identifiable information (PII) leak Stay organized with collections  Save and categorize content based on your preferences. 

Data lineage in Knowledge Catalog (formerly Dataplex Universal Catalog) lets you trace how data moves across tables and views to identify where personally identifiable information (PII) crosses security boundaries. In this tutorial, you investigate a scenario where consumer email addresses (`user_email`) intended for account creation, invoicing, and shipping leak into an organization-wide analytics table. You use column-level lineage to trace the exposed column from the public `order_status_stats` table through the `status_counts_by_user_v` view back to the transformation process that joins it with identity data.

## Before you begin

Before starting this tutorial, you must enable the required APIs, grant the required Identity and Access Management roles, and run the sample data transformations in Dataform to populate the dataset. For complete setup instructions, see [Prerequisites and setup](https://docs.cloud.google.com/knowledge-catalog/docs/lineage-use-cases-prerequisites).

## Analyze personal information leak with Lineage Explorer

After you prepare the dataset, trace the personal information leak using the BigQuery **Lineage** tab.

In this example, you trace the `user_email` column from the public table back to its source:

  1. In Google Cloud console, go to the **BigQuery** page.
  2. Use the search field to find the `order_status_stats` table.
  3. Click the **Lineage** tab.
  4. In the **Lineage Explorer** pane, do the following: 
     1. In the **Column Level Lineage** section, select the `user_email` column name from the list.
     2. In the **Direction** section, select the **Upstream** direction.
     3. Click **Apply**.
  5. Follow the graph back one step. The graph shows that the email is pulled from the `status_counts_by_user_v` intermediate view.
  6. Click the process node between the view and its upstream dependencies. The process node shows that a join operation occurs between anonymized order data and a table containing identity information.



The lineage proves that personal information crosses from a restricted functional table into a broader analytics schema, where unauthorized users can see it.

For more information on visualizing data with data lineage graph, see [Lineage graph view](https://docs.cloud.google.com/knowledge-catalog/docs/lineage-views#lineage-graph-view).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-24 UTC."],[],[]] 

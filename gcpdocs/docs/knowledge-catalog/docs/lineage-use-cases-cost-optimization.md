---
url: https://docs.cloud.google.com/knowledge-catalog/docs/lineage-use-cases-cost-optimization/
title: Use data lineage to optimize costs \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-25T05:53:40.286891+00:00
---

# Use data lineage to optimize costs  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/lineage-use-cases-cost-optimization/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Use data lineage to optimize costs Stay organized with collections  Save and categorize content based on your preferences. 

Data lineage in Knowledge Catalog lets you track downstream dependencies for tables and views in your BigQuery project. You can then identify assets that aren't actively used as sources for downstream jobs or workflows and flag them as candidates for deletion to reduce storage costs.

In this tutorial, you manage a BigQuery project with datasets derived from the Quarterly Census of Employment and Wages (QCEW). The project contains numerous tables and views for dashboards and analyses, such as tracking employment trends or wage comparisons, which increases your storage costs. By checking each asset for downstream links, you can systematically flag unused resources for deletion.

**Caution:** Be careful when deleting resources. Just because a resource lacks downstream workflows doesn't mean it is entirely unused. For example, users might still query a table directly to retrieve specific data in read-only mode. Deleting the resource could disrupt the work of anyone who relies on that direct access.

## Set up Lineage Explorer

To complete the use case, first set up the environment and run the data transformations by connecting a remote repository to Dataform. This repository contains the code necessary to set up the dataset and transform the data. For more information, see [Prerequisites and setup](https://docs.cloud.google.com/knowledge-catalog/docs/lineage-use-cases-prerequisites).

After you finish the environment setup, use BigQuery and **Lineage Explorer** to visually identify assets without downstream dependencies.

## Identify unused assets and optimize costs

After the dataset is prepared, identify assets that lack downstream dependencies. While you can do this visually for individual tables, you can also use a programmatic approach for larger datasets.

In this example, compare active assets with standalone assets to determine which can be safely removed:

  1. In Google Cloud console, go to the **BigQuery** page.
  2. Use the search field to find a standalone table (for example, an old analysis table from a specific year).
  3. Click the **Lineage** tab.
  4. In the **Lineage Explorer** pane, do the following: 
     1. In the **Direction** section, select the **Downstream** direction.
     2. Click **Apply**.



Observe the graph. If there are no downstream nodes, the asset is not being used as a source for other tracked BigQuery jobs. For more information about visualizing data with the data lineage graph, see [Lineage graph view](https://docs.cloud.google.com/knowledge-catalog/docs/lineage-views#lineage-graph-view).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-24 UTC."],[],[]] 

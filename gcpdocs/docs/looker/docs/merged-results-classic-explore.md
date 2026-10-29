---
url: https://docs.cloud.google.com/looker/docs/merged-results-classic-explore/
title: Merging results from different Explores in the classic Explore \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T05:38:28.422339+00:00
---

# Merging results from different Explores in the classic Explore  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/merged-results-classic-explore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Merging results from different Explores in the classic Explore Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** If you're using Looker's [new Explore](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-new-explore-experience), see the [Joining data from multiple queries](https://docs.cloud.google.com/looker/docs/merge-queries-new-explore) documentation page.**Note:** This page is part of the [Retrieve and chart data](https://docs.cloud.google.com/looker/docs/retrieve-and-chart-data) learning series.

Explores in Looker are designed by your Looker developers to combine the data from your database tables in the most effective way by using defined relationships between data fields and tables. Because of this, it's best to use a single Explore to examine your data.

However, there may be times when your Looker developers haven't created the relationships you need or have encountered technical limitations. In these cases, **Merged Results** lets you combine results from different Explores (even from different models or projects) to create data tables on which to [Explore](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores) and [create visualizations](https://docs.cloud.google.com/looker/docs/creating-visualizations). You can use **Merged Results** as a proof of concept to further develop and define your LookML projects and models.

**Note:** For information about understanding merged results queries, see the [Understanding merged results](https://docs.cloud.google.com/looker/docs/merge-queries-new-explore#understanding-merged-results) section of "Joining data from multiple queries."

## Merging queries

To merge the results from multiple queries, follow these steps:

  1. Create the first source query, called the _primary query_.
  2. Add the next source query.
  3. Check the merge rules for those queries and run the merge.
  4. Optionally, you can:

     * Sort, pivot, and create visualizations for the results.
     * Reuse and share the results using the URL.
     * Modify the results by editing the source queries or adding source queries.



### Creating the primary query

To merge the results from multiple queries, start by preparing the _primary_ query by following these steps:

  1. Select an Explore from the **Explore** menu.
  2. Select the dimensions and measures of interest from the field picker. Don't pivot any dimensions during this step.

This is all you need to start merging results. However, you can also use some advanced exploring techniques to further refine your query. You can:

  3. Optionally, add [filters](https://docs.cloud.google.com/looker/docs/filtering-and-limiting) for the data.

  4. Optionally, include [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) to create ad hoc metrics.

  5. Optionally, click **Run** to see the results of your primary query and to test your filters and table calculations.




## Adding the next source query

Once you've created your primary Explore, add another source query by following these steps:

  1. In your Explore, click the gear icon.
  2. Select **Merge Results**. This will open the **Choose an Explore** window.
  3. In the **Choose an Explore** window, click the name of an Explore where you'll create your next query.

Looker opens the Explore in the **Edit Query** window, where you can build the new query to be merged into your primary query.

**Note:** To merge queries, Looker finds dimensions in the queries whose values can be matched. Be sure that your queries contain at least one common dimension whose values can be matched exactly. For example, if both queries have a **Date** dimension, but one query uses "2017-10-01" as a value and the other query uses "October 2017" as a value, Looker can't use that dimension to merge the queries.
  4. Select the dimensions and measures of interest from the field picker. Be sure to include at least one dimension that will exactly match a dimension in the primary query. Do not pivot any dimensions during this step.

  5. Optionally, include filters to narrow the data.

  6. Optionally, incorporate table calculations to create new fields based on the query fields.

  7. Optionally, click **Run** to see the results of the source query and to test your filters and table calculations.

  8. Click **Save** to merge the query into your primary query.




### Checking the merge rules and running the merge

Looker automatically finds the best dimensions to use for matching the queries and displays these matches in the **Merge Rules** section. Looker displays which fields will be used for each merge.

  1. Review the dimensions that Looker used to match the queries. (See Editing merge rules for information on changing these rules.)

  2. Click **Run** to see the merged query results.




Note that any table calculations from the source queries are displayed as standard dimensions in the merged results.

### Using and modifying the merged results

You can use the merged results to:

  * Examine and sort the data, including [drilling into the data](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores#drilling_down_into_the_data). If you drill into the dimension used to merge the two Explores, however, Looker displays only drill fields from the primary Explore.
  * View [totals](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#displaying_totals). Looker calculates totals on each of the component queries and uses those totals in the merged results. Therefore, totals may appear too high, because what you are seeing are totals calculated before the [results were merged](https://docs.cloud.google.com/looker/docs/merged-results#what_if_one_query_doesnt_have_a_matching_data_value). One way to avoid this is to align the filters on each query.
  * Create visualizations.
  * [Pivot dimensions](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#pivoting_dimensions) in the merged results by selecting **Pivot** from the gear menu in the dimension's column of the data table. Note that you can't pivot dimensions in the source queries.



To reuse the merged results, you can:

  * Share the results using the browser URL.
  * Bookmark the URL in your browser to run the same merged query again in the future. You can't save the merged results as a Look.
  * Save the merged results as a tile on a dashboard (see Saving your merged results to a dashboard).



If you want to modify the merged results, you can:

  * Merge queries from additional Explores by clicking the **Add Query** button and following the same steps.
  * Edit the source queries or configure the way the queries are merged. See Editing merged results for more information.
  * Create filters by adding those filters in the source queries, either when creating and merging the queries, or by editing the queries from the **Merged Results** page. Note that you can't add a filter directly to the merged results.



If you want to clear the cache and retrieve fresh results from your database, select the **Clear Cache & Refresh** option from the gear menu at the top right of the **Merged Results** window.

To download your merged results query, you can save the query to a dashboard and then [download the dashboard as a PDF or as a collection of CSV files](https://docs.cloud.google.com/looker/docs/downloading#downloading_data_from_a_dashboard).

## Editing merged results

Once you have your merged results, you can make the following changes to your merged results:

  * Editing the source queries
  * Editing the merge rules
  * Switching the primary query



### Editing the source queries

From the **Merged Results** window, you can go back and edit the source queries by clicking on the query name in the left pane, or by selecting **Edit** from the query's gear menu. These options take you back to the **Edit Query** screen.

You can add or remove fields, add table calculations, or change the source query's filters. Click **Save** to return to your merged results.

The query's gear menu also has these options:

  * **Rename** : Specify a different name to display for the query in the **Merged Results** window.
  * **Make Primary** : Make the query the base for the merged results. See the [Understanding merged results](https://docs.cloud.google.com/looker/docs/merge-queries-new-explore#understanding-merged-results) section of "Joining data from multiple queries" to understand the role of the primary query.
  * **Delete** : Remove the query from the merged results. (If you want to add the query back into the merged results after you've deleted it, you can use the **Back** button in your browser.)



### Editing the merge rules

When you add a query, Looker automatically finds dimensions that it can use to match the added query to the primary query. Each added query must have at least one dimension whose values exactly match up to a dimension in the primary query. Looker displays these matches in the **Merge Rules** section, showing which fields will be used to merge the queries.

You can use the Merge Rules section to change or add which fields Looker uses to merge the queries.

  1. Use the drop-down menu to see other dimension options for matching the data.
  2. If there are additional dimensions that could be used for matching, Looker displays **\+ Add dimension**. Click **\+ Add dimension** to configure an additional set of dimensions to use in the query merge.
  3. Click the **X** if you don't want to match the data between the two dimensions.



### Switching the primary query

When merging queries, you start out by creating a single query from a single Explore and then you add other queries by combining them with that first query. By default, that first query is considered the _primary_ query, but you can designate any query as the primary query by selecting **Make Primary** from the query's gear menu.

Each added query must have at least one dimension whose values can be matched exactly to a dimension in the primary query.

When you switch the primary query, the merged results are likely to change. See the [Understanding merged results](https://docs.cloud.google.com/looker/docs/merge-queries-new-explore#understanding-merged-results) section of "Joining data from multiple queries" for more information about the role of the primary query.

## Saving your merged results to a dashboard

Once you've added your merged results query to a dashboard, you can [add or apply dashboard filters](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards) to your merged results tile, [rearrange the tile](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#rearranging_and_resizing_tiles), [edit the tile](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#editing_tiles), or [add new tiles](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_tiles_and_text_to_a_dashboard) to your dashboard. You can't download the data from a tile based on merged results, but you can [download the dashboard as a PDF](https://docs.cloud.google.com/looker/docs/downloading#downloading_a_dashboard_as_a_pdf) or [as a collection of CSV files](https://docs.cloud.google.com/looker/docs/downloading#downloading_a_dashboard_as_csvs).

**Important:** When you apply a dashboard filter to a merged query, the filtered dimension must be included in the merged query (the dimension can be [hidden from the visualization](https://docs.cloud.google.com/looker/docs/creating-visualizations#hiding_fields_from_visualizations)). Any dashboard filters that are applied to a merged results tile will be turned off if the merged query is changed in any way. You can reinstate the filters by turning them back on again in the [filter configuration window](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#editing_dashboard_filters).

## Merging queries in embedded Looks, dashboards, and Explores

You can merge queries within [embedded Looks, dashboards, and Explores](https://docs.cloud.google.com/looker/docs/private-embedding), if you have the appropriate permissions. To merge the query of an [embedded Look](https://docs.cloud.google.com/looker/docs/private-embedding#embedding_a_look) with another query:

  1. Hold your pointer over the Look's title to reveal the Look's gear menu, and then click the gear menu.
  2. Select **Merge Results** , then follow the steps for merging queries.



To merge an [embedded dashboard](https://docs.cloud.google.com/looker/docs/private-embedding#embedding_a_dashboard) tile's query:

  1. Hold your pointer over the dashboard tile to review the drop-down menu for the dashboard tile.
  2. From the drop-down menu, choose **Explore From Here**. Looker opens the Explore for that tile's query.
  3. Click the Explore's gear menu and select **Merge Results**.
  4. Follow the steps for merging queries.



## Notes

  * All the primary query's fields are displayed in the merged results, using the primary query's names for the fields. This means that if the primary query and an added query use different names for a matching dimension, only the primary query's dimension name will be displayed in the results.
  * Your **Merged Results** query may have row limits:

    * By default, the join for a **Merged Results** query is processed in Looker memory, and therefore each of the queries being merged is limited to 5,000 rows that can be joined (or up to 50,000 rows [if a higher limit is specified by your admin](https://docs.cloud.google.com/looker/docs/admin-panel-performance-center-content-guardrails#visualization-limits)). If you are joining a query that returns more than the limited rows of data, only the first number of limited rows that are returned are included in the merged results.
    * If your Looker admin has enabled the [**In-database merge queries** Looker Labs feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#in-database-merge-queries), and you are merging the results from two queries that are on the same BigQuery connection, the join between two queries is performed in the BigQuery database itself. In-database merge queries are more performant and can join unlimited rows. See the [In-database merge queries](https://docs.cloud.google.com/looker/docs/merge-queries-new-explore#in-database-merge-queries) section of "Joining data from multiple queries" for more information.
  * For merged queries that are processed in Looker memory, **Merged Results** is a post-query processing feature that, if not used thoughtfully, can overtax Looker instance resources and cause your Looker instance to respond more slowly for all users. If you can't take advantage of [in-database merge queries](https://docs.cloud.google.com/looker/docs/merge-queries-new-explore#in-database-merge-queries), the best practice is to define functions and logic in LookML, which generates SQL that is processed by your database. View the [Optimize Looker performance](https://docs.cloud.google.com/looker/docs/best-practices/how-to-optimize-looker-server-performance) Best Practices page for more information about optimizing Looker performance.




## Conclusion

Whenever possible, you should use the data from a single Explore because your Looker developers have carefully considered how the data from different database tables should be combined. When needed, though, merging results is a powerful technique that lets you combine data from multiple Explores and databases.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 

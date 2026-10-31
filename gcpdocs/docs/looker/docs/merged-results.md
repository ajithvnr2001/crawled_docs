---
url: https://docs.cloud.google.com/looker/docs/merged-results/
title: Joining data from multiple queries \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:48:24.547399+00:00
---

# Joining data from multiple queries  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/merged-results/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Joining data from multiple queries Stay organized with collections  Save and categorize content based on your preferences. 

Explores in Looker are designed by your Looker developers to combine the data from your database tables in the most effective way by using defined relationships between data fields and tables. For this reason, it's generally best practice to use a single Explore to examine your data.

However, there might be times when your Looker developers haven't created the relationships that you need or have encountered technical limitations. In these cases, the **Join data** page lets you join (or merge) results from two or more queries from different Explores (even from different models or projects) and display the query results as if they were one query. You can use joined queries to create data tables on which to [Explore](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores) and [create visualizations](https://docs.cloud.google.com/looker/docs/creating-visualizations), and as a proof of concept to further develop and define your LookML projects and models.

**Note:** If you're using the classic Explore, see the [Merging results from different Explores in the classic Explore](https://docs.cloud.google.com/looker/docs/merged-results-classic-explore) documentation page.

## Understanding joined results

When you join or merge queries, you start out by creating a single query from a single Explore, and then you combine other queries with that first query.

By default, that first query is considered the _primary_ query. The primary query is important, because when Looker matches the data to create the joined results, it matches each added query to the primary query (not to any other added query). Whenever you add a query, you need to include a dimension that can be matched to a dimension in the primary query.

For example, consider the following queries.

The primary query returns the following results:

Products Category | Products Count  
---|---  
Active | 5  
Jeans | 9  
Formalwear | 3  
  
The secondary query returns the following results:

Products Category | Items in Inventory Count  
---|---  
Active | 11  
Jeans | 16  
Formalwear | 6  
  
If you join these queries on the **Products Category** field, Looker produces the following joined results:

Products Category | Products Count | Items in Inventory Count  
---|---|---  
Active | 5 | 11  
Jeans | 9 | 16  
Formalwear | 3 | 6  
  
Joined results don't perform an actual SQL join (unless you're using in-database merge queries). However, for those who are familiar with SQL joins, joining queries combines the results of multiple Explores in a similar way to a _left join_. The results of the added query are combined with the results of the primary query as if they are being left joined into the primary query.

You don't have to be familiar with the idea of a left join to understand how joined results work. In practical terms, the designation of the primary query matters for the following reasons:

  * **How field names appear:** For matching fields, the primary query's field names are used in the joined results, as shown in the preceding example.
  * **How joined results handle a query without a matching value:** The next section, What if one query doesn't have a matching data value?, discusses how Looker handles merging data when only some of the queries have specific values in the matching dimensions.

For more troubleshooting tips for missing or null joined results values, see the [Why are there nulls in my secondary join results query?](https://docs.cloud.google.com/looker/docs/best-practices/how-to-troubleshoot-nulls-in-secondary-merge-result-query) Best Practices page.

  * **How joined results handle a query having multiple matching values:** The section What if one query has multiple rows for the same value? later on this page discusses how Looker handles merging data when some of the queries have multiple rows with a specific value (or combination of values) in the matching dimensions.




### What if one query doesn't have a matching data value?

Another reason the primary query is important is because of the way null values are handled in the matched dimensions:

  * If a row exists in the primary query but not in the additional query, then the added query's fields show NULL (`∅`) for that row.
  * If a row exists in the added query but not in the primary query, then the row doesn't show in the results at all.



To illustrate this behavior, consider the following example queries.

The primary query returns the following results:

Products Category | Products Department | Products Count  
---|---|---  
Active | Kids | 522  
Active | Adults | 545  
Dresses | Adults | 878  
Formalwear | Adults | 349  
  
The secondary query returns the following results:

Products Category | Products Brand Name | Items in Inventory Count  
---|---|---  
Active | Brand 1 | 223  
Dresses | Brand 2 | 80  
Dresses | Brand 3 | 3  
Jeans | Brand 3 | 8  
Jeans | Brand 2 | 19  
  
If you join these queries on the **Products Category** field, Looker produces the following joined results:

Products Category | Products Department | Products Brand Name | Products Count | Items in Inventory Count  
---|---|---|---|---  
Active | Adults | Brand 1 | 545 | 223  
Active | Kids | Brand 1 | 522 | 223  
Dresses | Adults | Brand 2 | 878 | 80  
Dresses | Adults | Brand 3 | 878 | 3  
Formalwear | Adults | ∅ | 349 | ∅  
  
The primary query has a row for **Formalwear** , so the joined results show this row. The added query doesn't have a **Formalwear** row, so any of the fields from the added query show NULL (`∅`) for **Formalwear**.

The added query has two rows for **Jeans** , but the primary query doesn't have rows for **Jeans**. As a result, these rows aren't shown in the joined results at all.

In this example, if you switch the primary query to make the added query the new primary query, Looker instead produces the following joined results:

Products Category | Products Brand Name | Products Department | Items in Inventory Count | Products Count  
---|---|---|---|---  
Active | Brand 1 | Adults | 223 | 545  
Active | Brand 1 | Kids | 223 | 522  
Dresses | Brand 2 | Adults | 80 | 878  
Dresses | Brand 3 | Adults | 3 | 878  
Jeans | Brand 2 | ∅ | 19 | ∅  
Jeans | Brand 3 | ∅ | 8 | ∅  
  
Looker no longer displays the **Formalwear** rows because they don't exist in the new primary query. However, Looker now displays the **Jeans** rows, and those rows show NULL (`∅`) for the dimensions and measures that are only in the query that is _added_ to the primary query.

For more troubleshooting tips for missing or null joined results values, see the [Why are there nulls in my secondary join results query?](https://docs.cloud.google.com/looker/docs/best-practices/how-to-troubleshoot-nulls-in-secondary-merge-result-query) Best Practices page.

### What if one query has multiple rows for the same value?

Designating the primary query is also important because of the way multiple rows with matching values are handled. If the added query has two or more rows with values that match a row in the primary query, the primary query row is duplicated that number of times.

In the following example, the _added_ query has two rows for **Dresses**. In the joined results, the **Dresses** values from the primary query appear twice, once for each of the **Dresses** rows from the added query.

The primary query returns the following results:

Products Category | Products Department | Products Count  
---|---|---  
Active | Kids | 522  
Active | Adults | 545  
Dresses | Adults | 878  
Formalwear | Adults | 349  
  
The secondary query returns the following results:

Products Category | Products Brand Name | Items in Inventory Count  
---|---|---  
Active | Brand 1 | 223  
Dresses | Brand 2 | 80  
Dresses | Brand 3 | 3  
Jeans | Brand 3 | 8  
Jeans | Brand 2 | 19  
  
The joined results query, merging on the **Products Category** field, returns the following results:

Products Category | Products Department | Products Brand Name | Products Count | Items in Inventory Count  
---|---|---|---|---  
Active | Adults | Brand 1 | 545 | 223  
Active | Kids | Brand 1 | 522 | 223  
Dresses | Adults | Brand 2 | 878 | 80  
Dresses | Adults | Brand 3 | 878 | 3  
Formalwear | Adults | ∅ | 349 | ∅  
  
If you switch the primary query in this case, you still have two **Dresses** rows, because the newly designated primary query has two rows for **Dresses**. When you join queries, the results might have more rows than the primary query has, but there will never be _fewer_ rows.

## In-database merge queries

**Preview:** This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms](https://cloud.google.com/terms/service-terms#1) section of the Service Specific Terms. Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

If you encounter an issue during the Public Preview of in-database merge queries, report it to [looker-in-database-merged-results-external@google.com](mailto:looker-in-database-merged-results-external@google.com).

By default, joined queries are processed in Looker memory, and therefore each query is limited to 5,000 rows that can be joined. If your Looker admin has enabled the [**In-database merge queries** Looker Labs feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#in-database-merge-queries), the join between two queries that are on the same BigQuery connection is performed in the BigQuery database itself. Performing the join in the database improves performance and allows for unlimited rows to be joined.

**Note:** In-database merge queries are performed as [left joins](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-type#left-outer).

In addition, when you create each of the Explore queries for a joined result, the Looker UI contains a **Row Limit** field. Looker uses the **Row Limit** field in different ways, depending on how the joined result query is processed:

  * For a joined query that is calculated in Looker memory, Looker retrieves the number of rows that are specified in the **Row Limit** field for each query and joins that data to create the joined result.
  * For an in-database merged query, Looker disregards the **Row Limit** values for each of the source queries and joins the full datasets for each source query.



If Looker is able to perform an in-database join for your joined query, a banner is displayed that indicates that the queries are being run in your database and that Looker is omitting the row limits from each of the source queries.

Then, in the results table for an in-database merged query, Looker displays a **Merged Results** field instead of a **Row Limit** field. The **Merged Results** field limits the rows that are being displayed in the results table, not the rows that are being processed, because in-database merged results queries don't have limits for how many rows can be processed.

## Joining queries

To join the results from multiple queries, follow these steps:

  1. Create the first source query, which is called the _primary query_.
  2. Add the next source query.
  3. Optionally, configure join rules for the joined query.
  4. Optionally, visualize the joined query.
  5. After you've created the joined query, save or share the joined query.
  6. Optionally, modify the joined query.



### Creating the primary query

To join the results from multiple queries, start by preparing the _primary_ query by selecting an Explore from the **Explore** menu and then selecting the dimensions and measures of interest from the field picker. Don't pivot any dimensions during this step. Alternatively, select a Look or dashboard, and click **Explore from here** on the Look or from a dashboard tile.

Now you can start merging results. However, you can also further refine your query in the following optional ways:

  * Add [filters](https://docs.cloud.google.com/looker/docs/filtering-and-limiting) for the data.
  * Include [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) to create ad hoc metrics. Any table calculations from the source queries are displayed as standard dimensions in the joined results.
  * Click **Run** to see the results of your primary query and to test your filters and table calculations.



### Adding the next source query

Once you've created your primary Explore query, add another source query by following these steps:

  1. In your Explore **Configure** panel, click **Merge queries (join data)** to open the **Join data** page.
  2. In the **Add join** window, choose the method that you'll use to add another source query:

     * **Build a new query from an Explore** : Looker displays a list of Explores. Choose the Explore that you want to use as a source query, and click **Add query**. Looker displays the **Configure joined fields** page. Select the dimensions and measures for your new query and add any filters or custom fields. Don't pivot any dimensions in the source query; instead, pivot dimensions in the joined results. Be sure to include at least one dimension whose values exactly match a dimension in the primary query. When you're finished configuring your new source query, click **Save and continue**.
     * **Paste prebuilt query URL** : In the **Add prebuilt query URL** field, enter the URL of the query, Look, or dashboard tile that you want to use as a source query and click **Add query**.
     * **Select Look** : Looker displays a list of Looks. Choose the Look that you want to use as a source query, and click **Add query**.
     * **Select Dashboard tile** : Looker displays a list of dashboards. Choose a dashboard, and then Looker shows a list of tiles on that dashboard. Select a tile and click **Add query**.



### Configuring join rules

To join two or more queries, Looker finds dimensions in the queries whose values can be matched. Each added query must have at least one common dimension whose values can be matched exactly to a dimension in the primary query. For example, if you want to add customer data to an Explore of orders, and both the orders Explore and the customer query have a **Customer ID** field with matching values, you can use the **Customer ID** field to join the queries. However, if both queries have a **Date** dimension, but one query uses `"2017-10-01"` as a value and the other query uses `"October 2017"` as a value, Looker can't use that dimension to join the queries.

Once you've selected and configured your primary and additional source queries, Looker automatically selects the best matching join fields and creates join rules in the **Configure joins** window on the **Join data** page. The primary query and each join rule appear as separate entries under **Source queries and join rules**.

In the **Source queries and join rules** section, you can modify the join rules in the following ways:

  * Change the join field of either the primary query or a source query.
  * Add new join fields.
  * Delete join fields.
  * Make a source query the primary query. When you switch the primary query, the joined results are likely to change. See Understanding joined results to understand the role of the primary query.
  * Add a new source query by clicking **Add join**.



### Configuring chart style

To visualize your joined queries, click **Select chart** to choose a visualization type. Alternatively, use the **Auto-visualize** option to let Gemini select an appropriate visualization. Then select the **Chart style** to configure the chart options for that chart type.

For a complete guide to all available visualization settings and supported chart types, see [Configuring and editing visualizations](https://docs.cloud.google.com/looker/docs/creating-visualizations).

### Saving or sharing the joined query

After you've created your joined query, you can click **Save or share** to perform the following actions:

  * **Save to new dashboard** : Looker displays the **Save as a new dashboard** window. Give the new dashboard a title and select a folder where you want the new dashboard to be saved.
  * **Save to existing dashboard** : Looker displays the **Add to a Dashboard in this folder** window. Enter a title for the new dashboard tile, and select the dashboard that you want to save the query to.
  * **Copy URL** : Looker displays the **Share URLs** window, displaying the query's [short URL](https://docs.cloud.google.com/looker/docs/sharing-urls#short_url) and [expanded URL](https://docs.cloud.google.com/looker/docs/sharing-urls#expanded_url). You can share the URL or bookmark it in your browser to run the same joined query again in the future. You can't save joined results as a Look.



Once you've added your joined query to a dashboard, you can [add or apply dashboard filters](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards) to your joined query tile, [rearrange the tile](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#rearranging_and_resizing_tiles), edit the tile, or [add new tiles](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_tiles_and_text_to_a_dashboard) to your dashboard. You can't download the data directly from a tile that's based on joined results, but you can [download the dashboard as a PDF](https://docs.cloud.google.com/looker/docs/downloading#downloading_a_dashboard_as_a_pdf) or [as a collection of CSV files](https://docs.cloud.google.com/looker/docs/downloading#downloading_a_dashboard_as_csvs).

**Important:** When you apply a dashboard filter to a joined query, the filtered dimension must be included in the joined query (the dimension can be [hidden from the visualization](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#using-the-data-column-more-menu)). Any dashboard filters that are applied to a joined query tile are turned off if the joined query is changed in any way. You can reinstate the filters by turning them back on in the [filter configuration window](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#editing_dashboard_filters).

### Modifying the joined query

After you've created your joined query, you can interact with the results and modify the query in the following ways on the **Join data** page:

  * Examine and sort the data, including [drilling into the data](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores#drilling-into-data). However, if you drill into the dimension that's used to join the two Explores, Looker displays only drill fields from the primary Explore.
  * In the **Configure joins** window, select **Edit query** next to the primary query to open the query's data table and make changes by using the field picker, such as adding or removing fields, adding table calculations, or changing the source query's filters (note that you can't add a filter directly to the joined results). You can also select **Options** next to the primary query to rename or delete the primary query.
  * In the **Configure joins** window, select **Edit query** next to the query that you want to modify in the join rule. For each additional source query, you can also select **Options** and rename or delete the query (if you want to add the query back into the joined results after you've deleted it, you can use the **Back** button in your browser), or make that source query the primary query for the joined queries.
  * In the **Joined fields** tab of the **Joined fields and chart style** window, pivot one or more of the joined query fields and add table calculations. Note that table calculations from the source queries are displayed as standard dimensions in the joined results.
  * In the **Chart style** tab of the **Joined fields and chart style** window, change the settings of the joined query visualization.
  * Use the **Totals** toggle to add or remove totals from the joined query. Looker calculates totals on each of the component queries and uses those totals in the joined results. Therefore, totals might appear too high, because what you are seeing are totals that were calculated before the results were joined. One way to always display the latest data is to align the filters on each query.
  * Click **Change chart** to select a different visualization for your joined query.



After you make any changes, you can view the results of the updated joined query by clicking **Run to update**.

## Editing a join query tile on a dashboard

To edit a join query tile on a dashboard, follow these steps:

  1. Put the dashboard into [edit mode](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards).
  2. Select **Edit Merged Query** on the tile.
  3. Looker opens the **Join data** page directly within the dashboard edit canvas.
  4. Make your changes to the primary query, additional source queries, join rules, or visualization.
  5. Select **Save** to update the joined queries settings and then select **Save** to update the tile on the dashboard.



## Merging queries in embedded Looks, dashboards, and Explores

You can join queries within [embedded Looks, dashboards, and Explores](https://docs.cloud.google.com/looker/docs/private-embedding) if you have the appropriate permissions:

  * To join the query of an embedded Look or an embedded dashboard tile with another query, open the Explore from the Look or dashboard tile by clicking **Explore from here** , and then follow the steps for joining queries.
  * From an embedded Explore, click **Merge queries (join data)** in the **Configure** panel and follow the steps for joining queries.



## Notes

  * All the primary query's fields are displayed in the joined results, which use the primary query's names for the fields. If the primary query and an added query use different names for a matching dimension, only the primary query's dimension name is displayed in the results.
  * Your joined query might have row limits:

    * By default, the join for a joined query is processed in Looker memory, and therefore each of the queries that's being joined is limited to 5,000 rows that can be joined (or up to 50,000 rows [if a higher limit is specified by your admin](https://docs.cloud.google.com/looker/docs/admin-panel-performance-center-content-guardrails#visualization-limits)). If you're joining a query that returns more rows than are allowed by the row limits, the joined results won't display any of the rows that exceed the row limits.
    * If your Looker admin has enabled the **In-database merge queries** Looker Labs feature, and you're merging the results from two queries that are on the same BigQuery connection, the join between the two queries is performed in the BigQuery database itself. In-database merge queries improve performance and can join unlimited rows. For more information, see the In-database merge queries section on this page.
  * For joined queries that are processed in Looker memory, merging queries is a post-query processing feature that, if not used thoughtfully, can overtax Looker instance resources and cause your Looker instance to respond more slowly for all users. If you can't take advantage of in-database merge queries, the best practice is to define functions and logic in LookML, which generates SQL that is processed by your database. For more information about optimizing Looker performance, see the [Optimize Looker performance](https://docs.cloud.google.com/looker/docs/best-practices/how-to-optimize-looker-server-performance) Best Practices page.




## Conclusion

Whenever possible, use the data from a single Explore because your Looker developers have carefully considered how the data from different database tables should be combined. When needed, though, joining queries is a powerful technique that lets you combine data from multiple Explores and databases.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 

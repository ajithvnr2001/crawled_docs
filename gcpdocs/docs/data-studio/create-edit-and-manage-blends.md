---
url: https://docs.cloud.google.com/data-studio/create-edit-and-manage-blends/
title: Create, edit, and manage blends \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T10:51:53.025086+00:00
---

# Create, edit, and manage blends  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/create-edit-and-manage-blends/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Create, edit, and manage blends Stay organized with collections  Save and categorize content based on your preferences. 

Create blends in Data Studio to combine fields from multiple data sources into a single chart or table. Blending helps you analyze related metrics together and build comprehensive visualizations across distinct datasets.

You can create blends automatically from selected charts or manually in the blend editor.

## Before you begin

To get the most out of this guide, make sure you're familiar with these key concepts:

  * [How blends work in Data Studio](https://docs.cloud.google.com/data-studio/how-blends-work)
  * [Creating and editing data sources](https://docs.cloud.google.com/data-studio/about-data-sources)
  * [Dimensions, metrics, and data modeling](https://docs.cloud.google.com/data-studio/model-your-data)



## Automatically blend selected charts

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Add charts based on the data sources you want to blend. For each chart, include the fields you want to include in the blend.
  3. Select the charts you want to include in the blend. 
     1. You can blend up to five charts.
     2. Right-click on the selected charts, then click **Blend data**.



Data Studio creates a new chart that combines the fields from your selected charts. You can customize and use this blended chart just like any other chart in your report.

### Example: Create a ratio metric

Blending two scorecards automatically creates a ratio metric, using the first chart you select as the numerator and the second chart as the denominator. For example, blending **Costs** and **Clicks** metrics automatically calculates your cost-per-click ratio:

![A user creates a blended Cost/Clicks scorecard by selecting the Cost and Clicks scorecards on a report and right-clicking to select the Blend data option.](https://docs.cloud.google.com/static/data-studio/images/cost-click-2019-09-11.png)

  1. **Cost** scorecard. Select this chart first.
  2. **Clicks** scorecard. Select this chart second, then right-click and select **Blend data**.
  3. Blended **Cost** / **Clicks** scorecard. Change the **Type** to **Currency** and adjust the **Decimal precision** to four places.



[See a more complete example in the **Create a ratio field based on filtered metrics** tutorial.](https://docs.cloud.google.com/data-studio/tutorial-create-a-ratio-field-based-on-filtered-metrics)

## Create blends manually

You can create blends manually in two ways:

  * Select a component on the page, then in the properties panel on the right, under **Data source** , click **+BLEND DATA**.
  * Open the **Resource > Manage blended data** menu, and in the bottom left, click **Add blend**.



## Edit blends you've already created

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select a chart based on a blend.
  3. Click the edit **Edit** icon for that chart's data source.



You can also edit blends from the top menu by clicking **Resource > Manage blended data**, finding your blend in the list, and clicking **Edit**.

## Add a table to the blend

  1. To the right of the rightmost table in the blend, click **Merge another table**.
  2. Select a data source.
  3. Add fields to the table by clicking **Add dimension** or **Add metric** , or by dragging the field from the fields drawer. If the drawer is closed, open it by clicking the chevron_right right arrow icon.
  4. To create a calculated field in the table, click **Add dimension** or **Add metric** , then click **+Create field**.

**Tip:** You can merge tables based on calculated fields. This is useful if the fields you want to join or union on aren't formatted identically across tables (for example, different capitalization or date formatting).
  5. Click the merge configuration between the new table and the table to the left to set up the merge between those tables.




## Move and remove tables

Tables you add to the blend always appear on the right. To reorder the tables in the blend:

  1. Click the more_vert **More** icon for the table you want to move.
  2. Select **Shift left/right**.

**Important:** Moving tables could break your merge conditions, requiring you to reconfigure the merge. To restore the previous merge condition, move the table back to its original position.

To remove a table from the blend:

  1. Click the more_vert **More** icon for the table you want to remove.
  2. Select **Remove**.

**Tip:** Removing a table has no effect on the data sources or on other blends in the report.

## Add and edit merge configurations

Each table in the blend is combined using a merge operator (either a join operator or the union operator) and merge conditions. When configuring a blend, keep the following rules in mind:

  * **Single merge type per blend** : A blend must contain either all joins or all unions. You cannot mix joins and unions within the same blend.
  * **Table limit** : A blend can have up to five tables.
  * **Hide repeated fields in unions** : For union operations, the **Hide repeated merge fields** option is enabled and locked by default, which prevents duplicate fields from being added to the blend.
  * **Field pairing in unions** : When configuring a union, both tables must include the same number of dimensions and metrics, and every field must be paired with a corresponding field of a matching data type under **Merge conditions** before you can save the blend.



### Add and edit a join

To add or edit a join operation, follow these steps:

  1. Click the merge configuration box between two tables.
  2. Select a join operator (for example, **Left outer**).
  3. Under **Merge conditions** , define the join by adding the dimensions that contain the matching values that you want to link on. The cross join operator doesn't use a merge condition.
  4. Click **Save**.



### Configure a union

Instead of linking fields horizontally across tables with join keys, unions stack rows vertically. To ensure that fields from different tables appear in the same column in the blended output, pair each field in the left table with a corresponding field in the right table under **Merge conditions**.

**Important:** The order in which you pair fields under **Merge conditions** determines how columns align vertically across tables. Ensure corresponding fields are paired in the same order in each table to avoid misaligning data in the blended result.

To configure a union, follow these steps:

  1. Click the merge configuration box between two tables.
  2. Select the **Union** operator.
  3. Under **Merge conditions** , verify the field pairings. Data Studio automatically pairs fields with matching names and data types. If field names differ, or if you need to adjust the alignment, manually pair each dimension and metric between the tables to ensure their values appear in the same output column.
  4. Click **Save**.



### Missing fields in merge conditions

A red box around the merge configuration, or a pink **Missing** field in the merge condition indicates that Data Studio can't merge your data with the selected dimensions:

![Merge configuration icon highlighted in red on the Blend Data panel indicates that a merge configuration is not specified.](https://docs.cloud.google.com/static/data-studio/images/broken-join-config-2022-02-16.png)

To fix this, add the missing field to the table before configuring the merge condition, or remove the missing field.

## Set a date range for a table in the blend

You have two options when setting a date range on a table in the blend:

  * **Auto** : Use the date range of the chart that gets its data from this blend.
  * **Custom** : Override the chart's date range with the range you select.



## Apply a filter to a table in the blend

Limit the data contained in a table by applying a filter. You can create a new filter, or apply an existing filter to a table in the blend as long as that filter is based on fields that exist in the table.

Get more in-depth information about [filters and date ranges in blends](https://docs.cloud.google.com/data-studio/blending-tips-and-advanced-concepts).

## Create calculated fields in a blend

Tables in a blend can include calculated fields. This can be particularly useful when creating merge conditions if the data isn't perfectly compatible between tables (for example, when the fields contain differently formatted dates or differently capitalized strings).

####  Show me how to add a calculated field 

  1. Choose a table in the blend. 
  2. Click **Add dimension** or **Add metric**. 
  3. Click **CREATE FIELD**. 
  4. Type in the formula in the editor window, then click **APPLY**. 



**Note:** When creating calculated fields in a table in the blend, the formula can only reference fields from that specific table. For example, a calculated field in Table 1 cannot reference fields in Table 2.

To create a calculated field that uses fields from different data sources, add those fields to their respective tables in the blend, and then [create a chart-specific calculated field](https://docs.cloud.google.com/data-studio/add-edit-and-troubleshoot-calculated-fields#create-a-chart-specific-calculated-field).

## Rename a table

Click the current table name, and then type a new name.

If your blend contains fields with duplicate names from different tables, the table name appears alongside the field name in the list of available dimensions and metrics.

## Rename a blend

To rename a blend, click the current blend name, and then type a new name.

## Reconnect a table

Underneath the table name, click the drop-down menu and select a new data source for this table.

**Important:** Selecting a data source whose fields don't match the table's current data source might break the blend configuration. You must replace or remove any invalid fields to restore the blend.

## Manage blended data

Open the **Resource > Manage blended data** menu to view and manage all blends in your current report. From here, you can create new blends, as well as edit, duplicate, or delete existing blends.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

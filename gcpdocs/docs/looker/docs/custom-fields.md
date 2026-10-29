---
url: https://docs.cloud.google.com/looker/docs/custom-fields/
title: Adding custom fields \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:51:22.121507+00:00
---

# Adding custom fields  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/custom-fields/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Adding custom fields Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page is part of the [Retrieve and chart data](https://docs.cloud.google.com/looker/docs/retrieve-and-chart-data) learning series.

When you explore data in Looker, you might need fields that aren't defined in your data model—such as calculating a metric on the fly, categorizing values into custom groups, or filtering an aggregation for a specific scenario. Instead of waiting for a LookML developer to update the model, you can create custom fields directly in your Explore to tailor your analysis.

Custom fields let you create ad hoc dimensions and measures that generate SQL and run directly against your database, just like fields that are defined in LookML.

To create and use custom fields, you must have the [`create_custom_fields`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_custom_fields) permission.

Depending on your analytical goals, you can create several types of custom fields:

  * **Custom measures from dimensions**: Aggregate a dimension, such as calculating a sum, an average, a distinct count, a minimum, or a maximum.
  * **Filtered custom measures**: Apply filter conditions to an existing measure, such as counting orders only for a specific status or region.
  * **Custom dimensions with Looker expressions**: Build ad hoc dimensions by using [Looker expressions (Lexp)](https://docs.cloud.google.com/looker/docs/creating-looker-expressions).
  * **Custom groups**: Bucket categorical dimension values under custom labels without writing complex formulas.
  * **Custom bins**: Tier numeric dimension values into equal-sized or custom-sized integer ranges.



## Custom fields are different from LookML-defined fields and table calculations

Understanding the differences between custom fields, LookML-defined fields, and table calculations helps you choose the right approach for your analysis.

Differences between custom fields and LookML-defined fields include the following:

  * You can create custom fields on the fly in an Explore without writing LookML or needing developer permissions.
  * Custom fields don't support drilling.
  * Custom fields persist in the **Custom Fields** section of the **Configure** panel (or field picker in classic Explores) only for users with permission to create them.



Differences between custom fields and [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) include the following:

  * Custom fields generate SQL that runs against your database, similar to LookML-defined fields. Table calculations run on the query results after data is retrieved from your database.
  * Custom fields are not dependent on data displayed in the data table, and you can use custom fields to filter or pivot query results.



## Viewing and using custom fields

The ability to see custom fields, and how you can interact with them, will be different depending on whether you're [allowed to create them](https://docs.cloud.google.com/looker/docs/managing-business-user-features#using_custom_fields) or not.

### Viewing custom fields

If you have the [`create_custom_fields`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_custom_fields) permission, then you can see and edit any that appear in the **Custom Fields** view in the **Configure** panel (or the **Custom Fields** section of the field picker in classic Explores).

If you don't have the [`create_custom_fields`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_custom_fields) permission, then the **Custom Fields** section or view is not displayed.

However, if you include a custom field in an Explore, a Look, or a dashboard tile, any users with whom you then share that content can see the custom field regardless of whether they have the ability to create custom fields. If you're sharing this content by sharing an Explore's URL, the URL must include the `qid` parameter (such as `instance_name.looker.com/explore/ec/order_items?qid=lEPPueGN7cHkozOEZVDQbO`). Users who aren't allowed to create custom fields will see only the field's title, not its description, so it's important to name fields precisely if you'll be using them in queries shared with these users.

### Using custom fields

If you have the [`create_custom_fields`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_custom_fields) permission, then you can edit and use any that appear in the **Custom Fields** view in the **Configure** panel (or the **Custom Fields** section of the field picker in classic Explores). You can interact with them almost exactly as you would with any other measures or dimensions, including filtering on them, adding them to visualizations, and (for custom dimensions) using them to pivot results. One exception is that you cannot use custom fields to create dashboard filters.

Only users who are allowed to create custom fields can _add_ them to queries in Explores, Looks, or dashboard tiles. However, if a user selects **Explore from here** on a shared Look or dashboard tile that includes a custom field, they can create a new query using that field whether or not they have the ability to create custom fields.

## Custom field types

You can create and customize several types of custom fields, depending on the base LookML field type or types. The following tables outline the types of custom fields that are available to create based on the LookML field type:

  * Dimension
  * Measure



### Custom field types for dimensions

You can create several custom field types from dimensions in an Explore's field picker, depending on the base LookML field type or types. The following table outlines the types of custom fields that are supported for each type of dimension.

S = Works with the [`string` data type](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#string)

N = Works with the [`number` data type](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#number) and numeric measures

T = Works with the [`tier` data type](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#tier)

ZC = Works with the [`zipcode` data type](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#zipcode)

YN = Works with the [`yesno` data type](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#yesno)

DI = Works with the [`distance` data type](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#distance)

DU = Works with the [`duration` data type](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#duration)

TS = Works with most [timestamp data types](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#time)*****

ID = Works with most [integer date data types](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#time)*****

SD = Works with most [string date data types](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#time)*****

L = Works with the [`location` data type](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#location)

Each custom field type that you can create from a dimension falls into one of the following categories:

  * **Aggregate** — Aggregated fields are [measures](https://docs.cloud.google.com/looker/docs/reference/param-measure-types) types that perform aggregations, such as sum and average. Aggregate measures can reference only dimensions, not other measures.
  * **Non-aggregate** — Non-aggregated fields are [dimensions](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types) that can be grouped by in an Explore query.

Custom field name | Category | Description | LookML field type compatibility  
---|---|---|---  
  
### Count distinct

Count distinct  |  Aggregate  |  Creates a [`count_distinct`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#count_distinct) measure that calculates the number of distinct values for a selected dimension.  |  S N T ZC YN DI DU TS ID SD L  
  
### Sum

Sum  |  Aggregate  |  Creates a [`sum`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#sum) measure that adds up the values of a selected dimension.  |  N DI DU ID  
  
### Average

Average  |  Aggregate  |  Creates an [`average`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#average) measure that averages the values of a selected dimension.  |  N DI DU ID  
  
### Min

Min  |  Aggregate  |  Creates a [`min`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#min) measure that finds the smallest value of a selected dimension.  |  N DI DU ID  
  
### Max

Max  |  Aggregate  |  Creates a [`max`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#max) measure that finds the largest value of a selected dimension.  |  N DI DU ID  
  
### Median

Median  |  Aggregate  |  Creates a [`median`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#median) measure that finds the midpoint value for the values of a selected dimension.  |  N DI DU ID  
  
### List of unique values

List of unique values  |  Aggregate  |  Creates a [`list`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#list) measure that creates a list of the distinct values of a selected dimension.  |  S T ZC YN SD L  
  
### Bin

Bin  |  Non-aggregate  |  Creates bins, or tiers, that separate the values of a selected numeric dimension into a custom set of number ranges.  |  N DI DU ID  
  
### Group

Group  |  Non-aggregate  |  Creates a group that lets you bucket results of a selected dimension under custom labels.  |  S N T ZC YN DI DU TS ID SD L  
***** **Note about date and time data:** Looker interprets some [timeframes](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#timeframe_options) and [time-based types](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#available_time-based_types) as different data types when you're creating custom fields, and this can affect the custom field types that are available for those timeframe and time-based fields. For example, Looker interprets the [`hour_of_day` timeframe](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#hour_of_day) as a [`number` data type](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#number) and therefore has custom field options available to other `type: number` fields. For more specific information, see the **How custom fields interpret date and time data types** section on this page.  
  
### Custom field types for measures

You can create only one custom field type, a filtered measure, from measures in an Explore's field picker, depending on the base LookML measure type. The following table outlines the LookML fields to which measure types you can add a filter.

LI = Works with the [`list` measure type](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#list)

DT = Works with the [`date` measure type](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#date)

YN = Works with the [`yesno` measure type](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#yesno)

N = Works with [numeric measure types](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#number) *

Custom field name | Description | LookML field type compatibility  
---|---|---  
  
### Filter measure

Filter measure  |  Adds a filter condition to a measure to limit the values included in the measure's aggregation.  | LI DT YN N  
* For more specific information on the types of measures Looker interprets as numeric while it's using custom fields, see the **How custom fields interpret numeric measures** section on this page.  
  
### How custom fields interpret date and time data types

Looker interprets some [timeframes](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#timeframe_options) and [time-based types](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#available_time-based_types) as different data types when you're creating custom fields, which affects the type of custom fields that you can create for a given date or time field. Custom fields categorize date and time fields in the following ways:

  * Timestamp
  * Integer
  * String



These categories are compatible with different types of custom fields, as indicated in the **Custom field types for dimensions** table.

#### Timestamp date data types

Custom fields treat the following LookML time data types as timestamp data types:

  * [`date`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#date)
  * [`time`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#time_table)
  * [`microsecond`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#microsecond)
  * [`millisecond`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#millisecond)
  * [`millisecondX`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#millisecondx_table)
  * [`second`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#second)
  * [`minute`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#minute)
  * [`minuteX`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#minutex_table)
  * [`hour`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#hour)
  * [`hourX`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#hourx_table)
  * [`week`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#week)
  * [`month`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#month)
  * [`quarter`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#quarter)
  * [`fiscal_quarter`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#fiscal_quarter)
  * [`fiscal_year`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#fiscal_year)
  * [`year`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#year)



#### Integer date data types

Custom fields treat the following LookML date and time data types as integer date types:

  * [`hour_of_day`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#hour_of_day)
  * [`day_of_month`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#day_of_month)
  * [`day_of_year`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#day_of_year)
  * [`month_num`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#month_num)
  * [`fiscal_month_num`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#fiscal_month_num)
  * [`week_of_year`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#week_of_year)
  * [`day_of_week_index`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#day_of_week_index)



#### String date data types

Custom fields treat the following LookML date and time data types as string data types:

  * [`time_of_day`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#time_of_day)
  * [`day_of_week`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#day_of_week)
  * [`month_name`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#month_name)
  * [`quarter_of_year`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#quarter_of_year)
  * [`fiscal_quarter_of_year`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#fiscal_quarter_of_year)



### How custom fields interpret numeric measures

Custom fields treat the following measure types as numeric types:

  * [`average`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#average)
  * [`average_distinct`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#average_distinct)
  * [`count`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#count)
  * [`count_distinct`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#count_distinct)
  * [`max`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#max)
  * [`median`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#median)
  * [`median_distinct`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#median_distinct)
  * [`min`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#min)
  * [`percent_of_previous`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#percent_of_previous)
  * [`percent_of_total`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#percent_of_total)
  * [`percentile`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#percentile)
  * [`percentile_distinct`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#percentile_distinct)
  * [`running_total`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#running_total)
  * [`sum`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#sum)
  * [`sum_distinct`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#sum_distinct)



These measure types are compatible with the filtered measure custom field type, as indicated in the **Custom field types for measures** table.

**Warning:** The [`type: number` measure type](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#number) is not compatible with custom fields. 

## Creating a custom measure from a dimension

The methods for creating a custom measure from a dimension differ depending on whether you're using the default Explore interface or classic Explore interface.

### Creating a custom measure in the default Explore interface

In Explores, users with the [`create_custom_fields`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_custom_fields) permission can create a custom measure in one of the following ways:

  * **You can use the Configure panel** :

    1. In the **Configure** panel, on either the **All Fields** tab or the **Fields in use** tab, hold the pointer over the dimension that you want to use to create the custom measure.
    2. Select the dimension's more_vert **More** menu.
    3. Select an aggregate function (such as **Count distinct** , **Sum** , **Average** , **Min** , or **Max**).
  * **You can use the data table in the Data pane** : In the data table, select the dimension's data column more_vert **More** menu, and select an aggregate function.

  * **You can use the + Add button** :

    1. In the **Custom Fields** section in the **Configure** panel, select **\+ Add** , and choose **Custom Measure**.
    2. In the **Create custom measure** dialog, select a field to measure, select a measure type, and define a custom measure with custom filters, formats, and descriptions.



The third **\+ Add** button method lets you customize the custom field as you create it, such as renaming, adding an optional description, or selecting a different format other than the default.

The new custom measure will automatically appear in the data table and in the **Custom Fields** view in the **Configure** panel. As with other fields, you can select a custom field's name to add or remove it from a query. You can also select its **Filter** button to use it as a [filter](https://docs.cloud.google.com/looker/docs/filtering-and-limiting) in a query.

### Creating a custom measure in classic Explores

In classic Explores, you can create a custom measure from a dimension in one of the following ways:

  * Using the dimension's three-dot **More** menu
  * Using the **Custom Fields** section of the field picker



The second method lets you customize the custom field as you create it, such as renaming, adding an optional description, or selecting a different format other than the default.

#### Using the dimension's three-dot **More** menu

In many cases, you can use this shortcut technique:

  1. Expand the field picker view that contains the dimension that you want to measure.
  2. Select the dimension's [three-dot **More** menu](https://docs.cloud.google.com/looker/docs/creating-and-editing-classic-explores#three-dot_more_menu).
  3. Select **Aggregate** to display options for creating a custom measure. The suggested functions vary based on the type of dimension you've chosen (such as number, string, or date). Select a function.



Expand the **Custom Fields** section in the field picker to see your new field.

As with other fields, you can select a custom field's name to add or remove it from a query. You can also hold your cursor over the field to reveal [more options](https://docs.cloud.google.com/looker/docs/creating-and-editing-classic-explores#field-specific_information_and_actions) that are available for that field, including selecting its **Filter** icon to use it as a [filter](https://docs.cloud.google.com/looker/docs/filtering-and-limiting) in a query. You can also edit the field as necessary.

#### Using the **Custom Fields** section of the field picker

If you want to define a format or a filter for your custom measure while creating it, start with the **Add** button on the **Custom Fields** section:

  1. Select **Add** in the **Custom Fields** section of the field picker.
  2. Select the type of field that you want to create. This example uses **Custom Measure**.
  3. Select a field to measure from the **Field to measure** drop-down, select the measure type from the **Measure type** drop-down options, and then specify a name in the **Name** field. The name appears in the field picker and in the data table.
  4. If you want to add a filter condition, select a field from the **Filter name** drop-down on the **Filters** tab. You can add or remove filter conditions using the **Add** and **Remove** plus and minus **Filter value** buttons. 
     * You can also select the arrow next to **Custom filter** to create a [custom filter](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#custom_filters) expression using any [Looker functions and operators](https://docs.cloud.google.com/looker/docs/functions-and-operators) that can be used in custom filters. The Looker expression editor will [suggest](https://docs.cloud.google.com/looker/docs/creating-looker-expressions#seeing_all_suggestions) field names and display syntax help for any functions you use. Fields that are both used in an Explore and eligible to be used with the field type that you're creating are marked with a black circle. Refer to the Adding a custom filter to a custom measure section on this page for more details about adding filters to measures.
  5. On the **Field details** tab, you can specify a format in the **Format** section and add an optional description of up to 255 characters in the **Description** box to give other users additional details about the custom field, including its intended use.
  6. Select **Save**.



The field picker will display your new custom measure in the **Custom Fields** section.

As with other fields, you can select a custom field's name to display it in a query. You can also select its **Filter** button to use it as a [filter](https://docs.cloud.google.com/looker/docs/filtering-and-limiting) in a query.

## Custom grouping

The **Group** custom field type lets you create ad hoc custom groups for dimensions without needing to use [logical functions](https://docs.cloud.google.com/looker/docs/functions-and-operators#logical_functions,_operators,_and_constants) in [Looker expressions](https://docs.cloud.google.com/looker/docs/creating-looker-expressions) or needing to develop `CASE WHEN` logic in [`sql`](https://docs.cloud.google.com/looker/docs/reference/param-field-sql) parameters or [`type: case`](https://docs.cloud.google.com/looker/docs/reference/param-field-case) fields.

This can be helpful when you want to assign fixed labels or category names to values that match specific conditions, for example, by grouping specific states or countries into regions or order costs into categories.

To create a group, follow these steps:

  1. Expand the view that contains the dimension for which you want to create custom groups.
  2. You can open the **Group By** menu in several ways:

     * In the default Explore interface, select the dimension's more_vert **More** menu in the **Configure** panel (or the data column more_vert **More** menu in the **Data** pane), and then select rule **Group**.
     * In classic Explores, select the dimension's [three-dot **More** menu](https://docs.cloud.google.com/looker/docs/creating-and-editing-classic-explores#three-dot_more_menu) in the field picker (or the dimension's gear menu in the data table), and then select **Group**.

![The Group By menu for the State dimension.](https://docs.cloud.google.com/static/looker/docs/images/custom-fields-group-2-2308.png)

  3. Specify a label for the first group of values in the **Group Name** field. This example illustrates how to create a group of states for the Pacific Northwest region of the United States using the **State** dimension, which is reflected by the **Group Name** 'Pacific Northwest'.

  4. Select the existing condition button in the **Group Value** section, which by default is **is any value** , to customize the conditions that you want to apply for the group.

  5. Select the condition, and enter or select one or more values. In this case, one of the conditions applied is **State is Oregon**. You can add or remove conditions using the **Add** and **Remove** plus and minus buttons. To save, click outside the filter condition, or use the escape key.

     * When available, value [suggestions](https://docs.cloud.google.com/looker/docs/changing-filter-suggestions) will appear in a drop-down list, which is indicated with a downward-facing arrow in the value input box, for users to select or search against. Suggestions are most commonly available for fields of `type: string`.
     * Looker automatically applies SQL conditions such as `AND` or `OR` logic when multiple conditions are created, based on the field types, conditions, and values that you specify.
     * If you're editing an existing custom group, consider changing the name to reflect the updated conditions.

![A user holds the pointer over the Add plus sign button next to the existing Group value, and the Group remaining values checkbox is selected.](https://docs.cloud.google.com/static/looker/docs/images/custom-fields-group-3-2304.png)

  6. To add more groups for that dimension, hold your cursor over the existing group and select the **Add** plus sign button; to remove groups, select the **Remove** minus sign button. You can edit an existing group by selecting the group condition — **is Oregon or Idaho or Washington** in this case. Looker automatically applies SQL conditions such as `AND` or `OR` logic when multiple conditions are created, based on the field types, conditions, and values that you specify.

  7. Optionally, select the **Group remaining values** checkbox to create a category for grouping all other values that don't satisfy any group conditions. In this example, any state that is not Oregon, Idaho, or Washington will be grouped under a label named **Other**. **Other** is the default name, but you can customize it in the **Group Name** field, as necessary.

     * If you're editing a custom group and want to remove grouping for all other values, clear the **Group remaining values** checkbox to remove that group.

![The text State Groups is entered into the Field name field, and the description States by region is entered in the Description field.](https://docs.cloud.google.com/static/looker/docs/images/custom-fields-group-4-2216.png)

  8. Specify a name in the **Field name** field. The name appears in the field picker and in the data table.

  9. Select **\+ Add Description** to open the **Description** box and add an optional description of up to 255 characters to give other users more information about the custom group.

     * If you're editing a custom group and there is an existing description, the **Description** box will automatically appear.
  10. Select **Save** and then **Run** to rerun the Explore.




The new field will appear in the data table and display labels for all states: "Pacific Northwest" for the states Oregon, Washington, and Idaho, and "Other" for all other states.

You can use the new group to make new insights into your data. For example, compare how many orders have been placed by users in the Pacific Northwest region to users living in other regions in the United States.

The new field will appear in the **Custom Fields** section of the field picker.

As with other fields, you can select the field's name to add or remove it from a query. You can also hold your cursor over the field to reveal [more options](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#field-specific_information_and_actions) that are available for that field, including selecting its **Filter** icon to use it as a [filter](https://docs.cloud.google.com/looker/docs/filtering-and-limiting) in a query. You can also edit the custom group as necessary.

## Custom binning

The **Bin** custom field type lets you create ad hoc custom bins, or tiers, for numeric type dimensions and custom dimensions without needing to use [logical functions](https://docs.cloud.google.com/looker/docs/functions-and-operators#logical_functions,_operators,_and_constants) in [Looker expressions](https://docs.cloud.google.com/looker/docs/creating-looker-expressions) or needing to develop [`type: tier`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#tier) LookML fields.

This can be helpful when you want to quickly group values into specific integer ranges to adjust the granularity of your data.

**Bin** custom fields appear in the [`classic`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#style_classic) tier notation style.

To create a bin, follow these steps:

  1. Expand the view that contains the dimension for which you want to create custom bins.
  2. You can open the **Bin** menu in several ways:

     * In the default Explore interface, select the dimension's more_vert **More** menu in the **Configure** panel (or the data column more_vert **More** menu in the **Data** pane), and then select bar_chart **Bin**.
     * In classic Explores, select the dimension's [three-dot **More** menu](https://docs.cloud.google.com/looker/docs/creating-and-editing-classic-explores#three-dot_more_menu) in the field picker (or the dimension's gear menu in the data table), and then select **Bin**.

![](https://docs.cloud.google.com/static/looker/docs/images/custom-binning-1-2304.png)

  3. As an optional starting point, select **Get field info** to learn more about the values for the dimension for which you're creating custom bins, including the dimension's minimum value, its maximum value, and its range of values. Having this information can be helpful in determining the way in which you specify value bins. 

  4. Select a bin type in the **Bin type** section.

     * Select **Equal-sized** to bin numeric values into equal integer ranges. For example, tiers of values ranging from 0-10, 10-20, and 20-30.
     * Select **Custom-sized** to create custom bin sizes of varying integer ranges. For example, tiers of values ranging from 0-15, 15-75, and 75-100.
  5. Customize the bin sizes and ranges.

     * If the selected **Bin type** is **Equal-sized** , enter the necessary values in the **Bin size** , **Minimum value** , and **Maximum value** fields. The preceding example displays specifications of bins of 10, ranging from 0 to 100. Bins are automatically created for values in the data that fall outside the specified ranges.
     * If the selected **Bin type** is **Custom-sized** , specify the tier breakpoints in ascending order in the **Bin breakpoints** box, separated either by commas or new lines.
**Warning:** A maximum of 500 total bins can be created for each **Bin** custom field type. 
  6. Specify a name in the **Field name** field. The name appears in the field picker and in the data table.

  7. Select **\+ Add Description** to open the **Description** box to add an optional description of up to 255 characters to give other users more information about the custom bin.

     * If you're editing a custom bin that has an existing description, the **Description** box automatically appears.
  8. Select **Save** and then **Run** to rerun the Explore.




The new field will appear in the data table and displays tier levels for values depending on where they fit into specified bins.

You can use the new bin to make new insights into your data. For example, for a custom bin that is based on a **Cost** dimension, you can compare the number of orders that contain items priced in specific cost ranges.

The new field will appear in the **Custom Fields** section of the field picker.

As with other fields, you can select the field's name to add or remove it from a query. You can also hold your cursor over the field to reveal [more options](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#using-field-actions) that are available for that field — for example, you can select the field's **Filter** icon to use it as a [filter](https://docs.cloud.google.com/looker/docs/filtering-and-limiting) in a query. You can also edit the custom bin as necessary.

## Adding a filter to a custom measure

Applying [filters](https://docs.cloud.google.com/looker/docs/filtering-and-limiting) to custom measures allows a measure to limit the data, such as only including orders from certain regions. You can add a custom filter to a custom measure when you're creating or editing a custom measure. To add a filter to a custom measure:

  1. Create or edit a custom measure in one of the following ways: 
     * In the **Configure** panel (or the field picker in classic Explores), select **Add** and select **Custom Measure** to create a new custom measure.
     * In the default Explore interface, select the custom measure's more_vert **More** menu in the **Configure** panel (or the data column more_vert **More** menu in the **Data** pane), and then select edit **Edit**.
     * In classic Explores, select the custom measure's [three-dot **More** menu](https://docs.cloud.google.com/looker/docs/creating-and-editing-classic-explores#three-dot_more_menu) in the field picker (or the dimension's gear menu in the data table), and then select **Edit**.
  2. Select the field that you want to filter by from the **Filter name** drop-down in the **Filters** section.
  3. Select the existing condition button, which by default **is any value** , under **Filter value** to customize the filter conditions that you want to apply.
  4. Select the condition, and enter or select a value. Select the **Add** plus sign button next to the value to add multiple conditions for the selected field. To save, click outside the filter condition, or use the escape key. 
     * When available, value [suggestions](https://docs.cloud.google.com/looker/docs/changing-filter-suggestions) will appear in a drop-down list, which is indicated with a downward-facing arrow in the value input box, for users to select or search against. Suggestions are most commonly available for dimensions of `type: string`.
     * If you're editing an existing custom measure, consider changing the custom measure's name to reflect the filter condition. The field name appears in the field picker and in the data table.
  5. To add more filters, select the **Add** plus sign button in the **Filter value** section; to remove filters, select the **Remove** minus sign button. 
     * Looker automatically applies SQL conditions such as `AND` or `OR` logic when you create multiple filters, based on the field types, conditions, and values that you specify.
  6. Optionally, click the downward-facing arrow next to **Custom filter** at the bottom of the **Filters** tab to expand the **Expression** field to add a [custom filter](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#custom_filters) instead of or in addition to a UI-based filter. Enter a [Looker expression](https://docs.cloud.google.com/looker/docs/creating-looker-expressions) in the **Custom filter** box by using any [Looker functions and operators](https://docs.cloud.google.com/looker/docs/functions-and-operators) that can be used in custom filters. The Looker expression editor will [suggest](https://docs.cloud.google.com/looker/docs/creating-looker-expressions#seeing_all_suggestions) field names and display syntax help for any functions you use. Fields that are both used in an Explore and eligible to be used with the field type that you're creating are marked with a black circle.
  7. On the **Field details** tab you can specify a format in the **Format** section and add an optional description of up to 255 characters in the **Description** box to give other users additional details about the custom field, including its intended use.
  8. Select **Save**.



## Creating a filtered measure from another measure

To create a custom measure that copies an existing measure and adds a [filter](https://docs.cloud.google.com/looker/docs/filtering-and-limiting), follow these steps:

  1. Expand the view that contains the measure to which you want to add a custom filter. The measure _cannot_ be a custom measure or a [`type: number`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#number) measure. To add a filter expression to an existing custom measure, you will need to edit the custom measure.
  2. Select that measure's [three-dot **More** menu](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#three-dot_more_menu) in the **Configure** panel (or the field picker in classic Explores). You can also select the data column **More** menu in the **Data** pane, or the gear menu in the **Data** pane for classic Explores.
  3. Select **Create filtered measure**.
  4. Specify a name other than the default in the **Name** field as necessary. The name appears in the field picker and in the data table.
  5. In the **Filters** section, select the field that you want to filter by from the **Filter name** drop-down.
  6. Select the existing condition button, which by default **is any value** , under **Filter value** to customize the filter conditions that you want to apply.
  7. Select the condition, and enter or select a value. Select the **Add** plus sign button next to the value to add multiple conditions for the selected field. To save, click outside the filter condition, or use the escape key. 
     * When available, value [suggestions](https://docs.cloud.google.com/looker/docs/changing-filter-suggestions) will appear in a drop-down list, which is indicated with a downward-facing arrow in the value input box, for users to select or search against. Suggestions are most commonly available for dimensions of `type: string`.
     * If you're editing an existing custom measure, consider changing the custom measure's name to reflect the filter condition.
  8. To add more filters, select the **Add** plus sign button in the **Filter value** section; to remove filters select the **Remove** minus sign button. 
     * Looker automatically applies SQL conditions such as `AND` or `OR` logic when you create multiple filters, based on the field types, conditions, and values that you specify.
  9. Optionally, click the arrow next to **Custom filter** at the bottom of the **Filters** tab to expand the **Expression** field to add a [custom filter](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#custom_filters) instead of or in addition to a UI-based filter. Enter a [Looker expression](https://docs.cloud.google.com/looker/docs/creating-looker-expressions) in the **Custom filter** box using any [Looker functions and operators](https://docs.cloud.google.com/looker/docs/functions-and-operators) that can be used in custom filters. The Looker expression editor will [suggest](https://docs.cloud.google.com/looker/docs/creating-looker-expressions#seeing_all_suggestions) field names and display syntax help for any functions you use. Fields that are both used in an Explore and eligible to be used with the field type that you're creating are marked with a black circle.
  10. On the **Field details** tab you can specify a format in the **Format** section and add an optional description of up to 255 characters in the **Description** box to give other users additional details about the custom field, including its intended use.
  11. Select **Save**.



The field picker will display the new measure in the **Custom Fields** section.

As with other measures, you can select a custom measure's name to add or remove it from a query. You can also hold your cursor over the field to reveal [more options](https://docs.cloud.google.com/looker/docs/creating-and-editing-classic-explores#field-specific_information_and_actions) that are available for that field, including selecting its **Filter** icon to use it as a [filter](https://docs.cloud.google.com/looker/docs/filtering-and-limiting) in a query. You can also edit the field as necessary.

## Creating a custom dimension using a Looker expression

The methods for creating a custom dimension will differ depending on whether you are using the default Explore interface or classic Explore interface.

### Creating a custom dimension in the default Explore interface

To create a custom dimension in the default Explore interface using a [Looker expression](https://docs.cloud.google.com/looker/docs/creating-looker-expressions) and one or more other dimensions, follow these steps:

  1. In the **Configure** panel, select **\+ Add** , and choose **Custom Dimension**.

**Tip:** When available, you can use [Gemini assistance in creating a Looker expression](https://docs.cloud.google.com/looker/docs/gemini-expression-asst#using).
  2. In the **Expression** box, enter a [Looker expression](https://docs.cloud.google.com/looker/docs/creating-looker-expressions) that calculates the value for your dimension, using any [Looker functions and operators](https://docs.cloud.google.com/looker/docs/functions-and-operators). The Looker expression editor will [suggest](https://docs.cloud.google.com/looker/docs/creating-looker-expressions#seeing_all_suggestions) field names and display syntax help for any functions you use. Fields that are used in an Explore and that are eligible to be used with the field that you're creating are marked with a black circle.

  3. Select a formatting option other than the default in the **Format** drop-down as necessary.

  4. Specify the custom dimension's name in the **Name** field. The name appears in the **Configure** panel and in the data table.

  5. Select **\+ Add Description** to add an optional description of up to 255 characters in the **Description** box to give other users more context or information about the custom dimension.

  6. Select **Save**.




The new custom dimension will automatically appear in the data table and under the **Custom Fields** view in the **Configure** panel.

As with other fields, you can select a custom dimension's name to add or remove it from a query. You can also hold the pointer over the field to reveal [more options](https://docs.cloud.google.com/looker/docs/creating-and-editing-classic-explores#field-specific_information_and_actions) that are available for that field, including selecting its **Filter** icon to use it as a [filter](https://docs.cloud.google.com/looker/docs/filtering-and-limiting) in a query. You can also edit the field as necessary.

### Creating a custom dimension in classic Explores

To create a custom dimension in classic Explores using a [Looker expression](https://docs.cloud.google.com/looker/docs/creating-looker-expressions) and one or more other dimensions, follow these steps:

  1. Select **Add** in the **Custom Fields** section of the field picker.
  2. Choose **Custom Dimension**.
  3. In the **Expression** box, enter a [Looker expression](https://docs.cloud.google.com/looker/docs/creating-looker-expressions) that calculates the value for your dimension, using any [Looker functions and operators](https://docs.cloud.google.com/looker/docs/functions-and-operators). The Looker expression editor will [suggest](https://docs.cloud.google.com/looker/docs/creating-looker-expressions#seeing_all_suggestions) field names and display syntax help for any functions you use. Fields that are used in an Explore and that are eligible to be used with the field that you're creating are marked with a black circle.
  4. Select a formatting option other than the default in the **Format** drop-down as necessary.
  5. Specify the custom dimension's name in the **Name** field. The name appears in the field picker and in the data table.
  6. Select **\+ Add Description** to add an optional description of up to 255 characters in the **Description** box to give other users more context or information about the custom dimension.
  7. Select **Save**.



The field picker will display your new custom dimension in the **Custom Fields** section.

As with other fields, you can select a custom dimension's name to add or remove it from a query. You can also hold the pointer over the field to reveal [more options](https://docs.cloud.google.com/looker/docs/creating-and-editing-classic-explores#field-specific_information_and_actions) that are available for that field, including selecting its **Filter** icon to use it as a [filter](https://docs.cloud.google.com/looker/docs/filtering-and-limiting) in a query. You can also edit the field as necessary.

## Duplicating a custom field

If you're [allowed to create custom fields](https://docs.cloud.google.com/looker/docs/managing-business-user-features#using_custom_fields), you can also duplicate existing custom fields that you or other users have created. Duplicating and then editing custom fields can be helpful if you'd like to create multiple custom fields with only small differences (for example, 30-day, 60-day, or 90-day sums).

The methods for duplicating a custom field will differ depending on whether you are using the default Explore interface or classic Explore interface.

### Duplicating custom fields in the default Explore interface

You can duplicate custom fields in the default Explore interface in either of the following ways:

  * In the **Configure** panel, expand the **Custom Fields** view, select the custom field's more_vert **More** menu, and select **Duplicate**.
  * In the **Data** pane, select the custom field's data column more_vert **More** menu, and select content_copy **Duplicate**.



The duplicated custom field appears in the **Custom Fields** view in the **Configure** panel and in the data table, using the name of the original field plus the word "Copy" appended to the end.

Next, you can edit the duplicated custom field.

### Duplicating custom fields in classic Explores

In classic Explores, you can duplicate custom fields in these ways:

  * Using a custom field's [three-dot **More** menu](https://docs.cloud.google.com/looker/docs/creating-and-editing-classic-explores#three-dot_more_menu) in the **Custom Fields** section of the field picker
  * Using a custom field's data table gear menu



To duplicate a custom field in classic Explores, follow these steps:

  1. In the field picker, expand the **Custom Fields** section.
  2. Select the three-dot **More** menu for the custom field that you want to duplicate.
  3. Select **Duplicate**.



Alternatively, select **Duplicate** from the custom field's data table gear menu.

The duplicated field appears under the original in the **Custom Fields** section of the field picker, using the name of the original field plus the word "Copy" appended to the end.

Next, you can edit the duplicated custom field.

## Editing a custom field

If you're [allowed to create custom fields](https://docs.cloud.google.com/looker/docs/managing-business-user-features#using_custom_fields), you also can edit custom fields that you or other users have created.

The methods for editing a custom field will differ depending on whether you are using the default Explore interface or classic Explore interface.

### Editing custom fields in the default Explore interface

You can edit custom fields in the default Explore interface in either of the following ways:

  * In the **Configure** panel, expand the **Custom Fields** view, select the custom field's more_vert **More** menu, and select **Edit**.
  * In the **Data** pane, select the custom field's data column more_vert **More** menu, and select edit **Edit**.



Either option opens the dialog for editing the custom field.

#### Editing a custom dimension

To edit a custom dimension, follow these steps:

  1. Change the custom dimension definition as necessary in the **Expression** box. When available, you can use [Gemini assistance in creating a Looker expression](https://docs.cloud.google.com/looker/docs/gemini-expression-asst#using).
  2. Select a new format from the **Format** drop-down, if necessary.
  3. Enter a new name in the **Name** field, as necessary. The name appears in the **Configure** panel and in the data table. If you have changed a custom field's definition, consider modifying the name to match.
  4. Add or update an optional description of up to 255 characters in the **Description** box to give other users more context or information about the custom dimension. 
     * If there is an existing description, the **Description** box will automatically appear. If there is no existing description, select **\+ Add Description** to add an optional description.
  5. Select **Save**.



#### Editing a custom measure

To edit a custom measure, follow these steps:

  1. To change the field that should be aggregated, select a new field from the **Field to measure** drop-down.
  2. To change the type of measure function, select a new measure type from the **Measure type** drop-down.
  3. Enter a new name in the **Name** field, as necessary. The name appears in the **Configure** panel and in the data table. If you change a field or measure type, typically you should also change the custom measure's name to match. For example, if you change the field **Sale Price** to **Cost** , you should also change the custom field name, in this case from **Sum of Sale Price** to **Sum of Cost**.
  4. Add, change, or remove a UI-based or custom filter on the **Filters** tab. 
     * If there is an existing custom filter, the custom filter **Expression** box will automatically appear. If there is no existing custom filter, select the downward arrow next to **Custom filter** to add an optional custom filter in the **Expression** box instead of or in addition to a UI-based filter.
  5. On the **Field details** tab, add, change, or remove any formatting in the **Format** section, or add an optional description of up to 255 characters in the **Description** box to give other users additional details about the custom field, including its intended use.
  6. Select **Save**.



#### Editing a custom group or custom bin

To edit group conditions, bin breakpoints, field names, and descriptions in a custom group or custom bin, after you open the edit dialog, follow the steps in the Custom grouping and Custom binning sections.

### Editing custom fields in classic Explores

In classic Explores, you can edit custom fields in these ways:

  * Using a custom field's [three-dot **More** menu](https://docs.cloud.google.com/looker/docs/creating-and-editing-classic-explores#three-dot_more_menu) in the **Custom Fields** section of the field picker
  * Using a custom field's data table gear menu



#### Editing a custom dimension

To edit a custom dimension in classic Explores, follow these steps:

  1. Change the custom dimension definition as necessary in the **Expression** box.
  2. Select a new format from the **Format** drop-down if necessary.
  3. Enter a new name in the **Name** field as necessary. The name appears in the field picker and in the data table. If you have changed a custom field's definition, consider modifying the name to match.
  4. Select **\+ Add Description** to add an optional description of up to 255 characters in the **Description** box to give other users more context or information about the custom dimension. 
     * If there is an existing description, the **Description** box will automatically appear.
  5. Select **Save**.



#### Editing a custom measure

To edit a custom measure in classic Explores, follow these steps:

  1. To change the field that should be aggregated, select a new field from the **Field to measure** drop-down.
  2. To change the type of measure function, select a new measure type from the **Measure type** drop-down.
  3. Enter a new name in the **Name** field as necessary. The name appears in the field picker and in the data table. If you change a field or measure type, typically you should also change the custom measure's name to match. For example, if you change the field **Sale Price** to **Cost** , you should also change the custom field name, in this case from **Sum of Sale Price** to **Sum of Cost**.
  4. Add, change, or remove a UI-based or custom filter on the **Filters** tab. 
     * If there is an existing custom filter, the custom filter **Expression** box will automatically appear. If there is no existing custom filter, select the downward arrow next to **Custom filter** to add an optional custom filter in the **Expression** box instead of or in addition to a UI-based filter.
  5. On the **Field details** tab, add, change, or remove any formatting in the **Format** section, or add an optional description of up to 255 characters in the **Description** box to give other users additional details about the custom field, including its intended use.
  6. Select **Save**.



#### Editing a custom group or custom bin in classic Explores

To edit group conditions, bin breakpoints, field names, and descriptions in a custom group or custom bin in classic Explores, after you open the edit dialog, follow the steps in the Custom grouping and Custom binning sections.

## Removing and deleting custom fields

If you're [allowed to create custom fields](https://docs.cloud.google.com/looker/docs/managing-business-user-features#using_custom_fields), you can remove custom fields from a query or delete them from the Explore.

When you delete a custom field, it disappears from the Explore but not from any Looks or dashboard tiles that use that field. Additionally, anyone using a URL for an Explore that had the custom field will still have the field.

You can choose between **Remove** and **Delete** :

  * **Remove** : Removes the custom field from the Explore query and data table, but keeps the custom field definition in the **Custom Fields** section of the field picker so that you can add it back to the query later.
  * **Delete** : Permanently deletes the custom field from both the Explore query and the **Custom Fields** section of the **Configure** panel (or the field picker in classic Explores).



The methods for removing and deleting a custom field will differ depending on whether you are using the default Explore interface or classic Explore interface.

### Removing custom fields in the default Explore interface

In the default Explore interface, you can choose between **Remove** and **Delete** :

  * **Remove** : Removes the custom field from the Explore query and data table, but keeps the custom field definition in the **Custom Fields** view in the **Configure** panel so that you can add it back to the query later.
  * **Delete** : Permanently deletes the custom field from both the Explore query and the **Custom Fields** view in the **Configure** panel.



To remove a custom field from the query while keeping it in the **Configure** panel, use either of the following methods:

  * In the **Data** pane, select the custom field's data column more_vert **More** menu, and select delete_outline **Remove**.
  * In the **Configure** panel, select the **Fields in use** tab, and click the custom field's name to deselect it.



The custom field will no longer appear in the data table or query results, but remains available under the **Custom Fields** view in the **Configure** panel.

### Deleting custom fields in the default Explore interface

To permanently delete a custom field from an Explore query and the **Configure** panel, use either of the following methods:

  * In the **Configure** panel, expand the **Custom Fields** view, select the custom field's more_vert **More** menu, and select delete_forever **Delete**.
  * In the **Data** pane, select the custom field's data column more_vert **More** menu, and select delete_forever **Delete**.



You can also use the [keyboard shortcuts](https://docs.cloud.google.com/looker/docs/keyboard-shortcuts#shortcuts_for_exploring) Command-K (Mac) or Ctrl+K (Windows) to delete custom fields and clear fields from an Explore query.

You can reinstate a custom field that you've deleted by selecting the back arrow on your browser.

### Removing custom fields in classic Explores

You can remove custom fields in classic Explores in either of the following ways:

  * Using a custom field's [three-dot **More** menu](https://docs.cloud.google.com/looker/docs/creating-and-editing-classic-explores#three-dot_more_menu) in the **Custom Fields** section of the field picker
  * Using a custom field's data table gear menu



To delete a custom field in classic Explores, follow these steps:

  1. In the field picker, expand the **Custom Fields** section.
  2. Select the three-dot **More** menu for the custom field that you want to remove.
  3. Select **Remove**.



Alternatively, select **Remove** from the custom field's data table gear menu.

### Deleting custom fields in classic Explores

You can delete custom fields in classic Explores in either of the following ways:

  * Using a custom field's [three-dot **More** menu](https://docs.cloud.google.com/looker/docs/creating-and-editing-classic-explores#three-dot_more_menu) in the **Custom Fields** section of the field picker
  * Using a custom field's data table gear menu



To delete a custom field in classic Explores, follow these steps:

  1. In the field picker, expand the **Custom Fields** section.
  2. Select the three-dot **More** menu for the custom field that you want to delete.
  3. Select **Delete**.



Alternatively, select **Delete** from the custom field's data table gear menu.

You can also use the [keyboard shortcuts](https://docs.cloud.google.com/looker/docs/keyboard-shortcuts#shortcuts_for_exploring) Command-K (Mac) or Ctrl+K (Windows) to delete custom fields and clear fields from an Explore query.

You can reinstate a custom field that you've deleted by selecting the back arrow on your browser.

## Related resources

Now that you have learned how to create and edit custom fields, you may want to do the following:

  * [Filter and limit](https://docs.cloud.google.com/looker/docs/filtering-and-limiting) your results to just the data you're interested in.
  * [Use table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) to create ad hoc Explore metrics.
  * [Create visualizations](https://docs.cloud.google.com/looker/docs/creating-visualizations).
  * [Save Explore queries as Looks](https://docs.cloud.google.com/looker/docs/saving-and-editing-looks).
  * [Add Explore queries to dashboards](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#creating_a_dashboard_from_a_look_or_an_explore).
  * [Share data](https://docs.cloud.google.com/looker/docs/sharing-data) with other users.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 

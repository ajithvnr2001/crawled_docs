---
url: https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores/
title: Viewing and interacting with Explores \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:48:22.694252+00:00
---

# Viewing and interacting with Explores  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Viewing and interacting with Explores Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** If you're using classic Explores in Looker, see the [Classic Explore](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-classic-explores) documentation.

In Looker, an Explore is your starting point for querying and analyzing data. Interacting with an Explore lets you examine metrics, drill into granular details, and act on your findings. You can safely explore and manipulate data without altering underlying reports or affecting other Looker users. Read the following sections to learn about these concepts:

  * Required roles
  * Finding Explores in Looker
  * Navigating the Explore interface
  * Drilling into data for additional detail
  * Using links and actions that might be available in the data
  * Related resources



Visit the [Creating and editing Explores](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores) page to learn more about creating or editing an Explore query.

**Note:** This page is part of the [Retrieve and chart data](https://docs.cloud.google.com/looker/docs/retrieve-and-chart-data) learning series.

## Required roles

To view and interact with Explores, you must have the **User** [Looker role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#user) or another role that contains the [`explore`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore) permission.

## Finding Explores in Looker

You can find prebuilt Explore queries in Looker in several ways, including the following:

  * Click the **Explore from Here** link while editing [Looks](https://docs.cloud.google.com/looker/docs/saving-and-editing-looks#editing_a_looks_source_query) or [dashboard tiles](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#editing_tiles).
  * Click the **Explore from Here** link on [Alerts](https://docs.cloud.google.com/looker/docs/alerts-overview) and [scheduled deliveries](https://docs.cloud.google.com/looker/docs/scheduling).
  * Follow links that are [shared by other users](https://docs.cloud.google.com/looker/docs/sharing-urls).
  * Use [Quick Start analyses](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#using-starter-questions) or [Insight Assistant](https://docs.cloud.google.com/looker/docs/gemini-insight-asst) as a starting point in a blank Explore.
  * [Upload a CSV, an XLS, or an XLSX file](https://docs.cloud.google.com/looker/docs/exploring-self-service#uploading_data_to_create_a_self-service_explore).



You can also use the explore **Explore** section in the [main navigation panel](https://docs.cloud.google.com/looker/docs/finding-content#using_the_main_navigation_menu) to open a blank Explore.

## Navigating the Explore interface

The Explore interface consists of the following elements:

![](https://docs.cloud.google.com/static/looker/docs/images/looker-explore-anatomy-2618.png)

  1. The name of the Explore.
  2. The dynamic_form **Show starter questions** button: Opens the **Starter Questions** panel that displays starter questions, when available. Learn more about using [Starter questions](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#using-starter-questions).
  3. The tips_and_updates **Insight Assistant** button: Opens the **Insight Assistant** panel, which lets you ask questions to discover insights and answers by using data from the Explore. Learn more about [using the Insight Assistant](https://docs.cloud.google.com/looker/docs/gemini-insight-asst) in Explores.
  4. The add_chart **Change chart** button: Opens the **All chart types** menu, which let you choose how to visualize the Explore data. You can also click **Auto visualize** to let Looker choose the best chart option for displaying the results. Learn more about [selecting an effective data visualization](https://docs.cloud.google.com/looker/docs/visualization-guide) and [editing visualizations in Explores](https://docs.cloud.google.com/looker/docs/editing-visualizations).
  5. The **Run** button: Runs the query with the fields that are selected from the **Configure** panel. When a query is running, the button becomes the **Stop** button. You can stop a query when it is running by clicking the **Stop** button.
  6. The **Save or share** button: Opens a menu that displays the options to save, download, or share an Explore query. Learn more about saving or sharing Explores.
  7. The more_vert **More options** menu: Opens a menu that lets users use or customize their Explore in several ways. Learn more about More options menu.
  8. The **Filter** pane: Displays the filters that are applied to Explores, as well as filter options. Learn more about [applying filters in Explores](https://docs.cloud.google.com/looker/docs/filtering-and-limiting-data).
  9. The **Visualization** pane: Displays the results of the Explore query that are visualized in a chart.
  10. The drag_indicator **Drag indicator** : Lets you resize the height of the **Visualization** pane and the **Data** pane, and the width of the **Configure** panel when you click and hold your cursor on the **Drag indicator**.
  11. The **Data** pane: Displays the results of the Explore query in a data table, or the underlying SQL query when the **SQL Query** button is clicked.
  12. The data column more_vert **More** menu: Displays the options for editing the Explore query around a specific column. Learn more about [using the data column **More** menu to edit Explore queries](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#using-the-data-column-more-menu).
  13. The **Sort Order** indicator: Indicates the field or fields, the direction (ascending or descending), and the order that an Explore query is sorted by. Learn more about [sorting queries](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#sorting-data).
  14. The table_chart **Data Table** button: Lets you display or hide the **Data** panel.
  15. The **Results** button: When clicked, displays the Explore results in a data table.
  16. The **SQL Query** button: When clicked, displays the SQL query that's generated to fetch the Explore results instead of the results data table.
  17. The Explore **Performance** panel: Displays the number of rows that are returned, the time it took to run the query, how old the data is, and a link to view the [Explore **Performance** panel](https://docs.cloud.google.com/looker/docs/query-tracker#explore_performance_panel). When your browser window is too small to display the text, you can click the speed **Performance details** icon to display the details.
  18. The viewer time zone: Displays the time zone that is used by the viewer to interpret the time-based data, if your admin has enabled [user-specific time zones](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#user_specific_time_zones). You can change the viewer time zone by clicking the **Viewer time zone** text. If your browser window is too small to display the time zone, you can click the sunny **Viewer time zone** icon to display the time zone.
  19. The **Limit** field: Lets you input a number to limit the displayed results. Learn more about [limiting data](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#limiting-data).
  20. The **Totals** and, when available, **Subtotals** switch: When enabled, displays the row or column totals and subtotals in the Explore results. Learn more about [displaying totals](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#displaying-totals).
  21. The [**Configure** panel](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#navigating-the-configure-panel): Displays the [**All Fields**](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#using-the-all-fields-tab), [**Fields in use**](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#using-the-fields-in-use-tab), and visualization [**Style**](https://docs.cloud.google.com/looker/docs/creating-visualizations) tabs, which let you select fields to create and edit the Explore results and the Explore visualization. Learn more about [creating and editing Explores](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores) and about [editing visualizations](https://docs.cloud.google.com/looker/docs/creating-visualizations).
  22. The name of the Explore. Click the info **Explore Summary** button to view a description of the Explore that was either added by a developer, or [generated by Gemini in Looker](https://docs.cloud.google.com/looker/docs/explore-summary-gemini). If your Explore is [certified](https://docs.cloud.google.com/looker/docs/content-certification), a ![](https://docs.cloud.google.com/static/looker/docs/images/certified-content-badge-2604.png)**Certified** badge is displayed next to the Explore name.
  23. The **Clear all** and **Clear fields keep filters** options: When clicked, **Clear all** clears all of the Explore fields, and **Clear fields keep filters** clears the Explore fields but keeps any filters that are applied.
  24. The join_left **Merge queries (join data)** button: Opens the **Join data** page. Learn more about [joining data](https://docs.cloud.google.com/looker/docs/merged-results).
  25. The Explore summary: Displays the total number of fields in an Explore (including custom fields and table calculations when [permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_table_calculations) allow), and the **Go to LookML** link. The **Go to LookML** link directs users to the `explore` definition in its LookML project. This link is visible only to users with the [`see_lookml`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_lookml) permission.
  26. The build **Configure** button: Lets you display or hide the **Configure** panel. Alternatively, click the close **Close** button to close the **Configure** panel.
  27. The filter_alt **Filter** button: Lets you display or hide the **Filter** pane.
  28. The insert_chart **Visualization** button: Lets you display or hide the **Visualization** pane.
  29. The table_chart **Data Table** button: Lets you display or hide the **Data** pane.
  30. The dock_to_right **Move Left** or dock_to_left **Move Right** button: Lets you change the docking orientation of the **Configure** panel on the Explore page. The button label is **Move Left** when the **Configure** panel is docked on the right and **Move Right** when the **Configure** panel is docked on the left.



### Using the **Save or share** menu

The **Save or share** menu lets users save and share an Explore in several ways, depending on their [permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permissions_list) in Looker. Depending on user permissions and instance integrations, the options can include the following:

  * **Save to new dashboard** : Save an Explore as a [query tile](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_query_tiles_from_an_explore) to a [new dashboard](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#creating_a_dashboard_from_a_look_or_an_explore).
  * **Save to existing dashboard** : Save an Explore as a [query tile](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_query_tiles_from_a_look) to an [existing](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#adding_tiles) dashboard.
  * **Save as a Look** : Save an Explore as a [Look](https://docs.cloud.google.com/looker/docs/saving-and-editing-looks#saving_looks_from_an_explore).
  * **Send** : Select this option to [send an Explore](https://docs.cloud.google.com/looker/docs/send-once) as a one-off delivery.
  * **Save and schedule** : Save an Explore as a Look and [set a recurring delivery](https://docs.cloud.google.com/looker/docs/delivering-looks-explores#creating_a_delivery) for that Look.
  * **Share URLs** : Opens the **Share URLs** menu to copy the short or expanded Explore URL to your clipboard.
  * **Download** : [Download the contents](https://docs.cloud.google.com/looker/docs/downloading#downloading_data_from_a_look_or_an_explore) of an Explore in one of several format options.
  * **Connected Sheets** : Open a new Google Sheets file that's initialized with [Connected Sheets for Looker](https://docs.cloud.google.com/looker/docs/connected-sheets).
  * **Open in Excel** : Open the results of an Explore query in Google Sheets. This menu option is available only when the [Google Sheets action is enabled for your instance](https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-the-google-sheets-integration#enabling-the-google-sheets-action-in-looker).



### Using the **More** options menu

The **More options** menu lets users use or customize their Explore in several ways, depending on their [permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permissions_list) in Looker. Depending on user permissions and instance integrations, the options can include the following:

  * **Get LookML** : Select this option to get the Explore's query and visualization LookML elements to [add to a LookML dashboard](https://docs.cloud.google.com/looker/docs/building-lookml-dashboards#adding_a_visualization_to_an_existing_lookml_dashboard), [an aggregate table](https://docs.cloud.google.com/looker/docs/aggregate_awareness#adding_aggregate_tables_to_your_project), or [a native derived table](https://docs.cloud.google.com/looker/docs/creating-ndts#using_an_explore_to_begin_defining_your_native_derived_tables).
  * **Remove fields and filters** : Removes all fields and filters from the Explore, giving you a [blank Explore](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#starting-with-a-blank-explore).
  * **Clear cache and refresh** : Force new query results to be retrieved from the database.
  * **Certify** or **Remove certification** : If [content certification](https://docs.cloud.google.com/looker/docs/content-certification) is enabled on your instance, users with the proper permission will see the option to certify the Explore; or, if the Explore is already certified, users with the proper permission will see the option to revoke certification of the Explore.
  * **Edit data fields** : If you are using a self-service Explore, the **Edit data fields** option lets you [modify the data fields](https://docs.cloud.google.com/looker/docs/exploring-self-service#modify_data_fields) in the Explore.
  * **Update data** : If you are using a self-service Explore, the **Update data** option lets you [update the data](https://docs.cloud.google.com/looker/docs/exploring-self-service#update-data) in the Explore.
  * **Rebuild Derived Tables & Run**: The **Rebuild Derived Tables & Run** option rebuilds all the persistent tables (all the PDTs and aggregate tables) that are required to answer the query, regardless of their persistence strategy. This option includes any aggregate tables and PDTs in the current query, and it also includes any aggregate tables and PDTs that are referenced by the aggregate tables and PDTs in the current query.
  * **Switch to classic Explore** : You can use this option to switch to the [classic Explore interface](https://docs.cloud.google.com/looker/docs/exploring-data-in-the-classic-experience).



## Drilling into the data

Every query result is the starting point for another query. Selecting any data point in a result will _drill down_ , creating another query that's refined by the data point that you selected. For example, you might have an Explore that displays flight information, in this case **Flight Count** grouped by **Origin City**. In this example, the selected origin city, Chicago, has 4,719,108 flights. Clicking the count value of **4,719,108** opens a drill window that displays a data table that contains details about those specific flight records.

![](https://docs.cloud.google.com/static/looker/docs/images/nextgen-exploring-drilling-262.png)

### Drilling deeper ...

The drill window displays all the flights that had Chicago as a point of origin. From the drill window, you can do the following:

  * Click explore **Explore** to open an Explore that uses the fields in the drill window as a starting point.
  * Click file_download **Download** to download the data with the same options as shown on the [Downloading content](https://docs.cloud.google.com/looker/docs/downloading) documentation page.
  * Select a value from the drill window data table to keep drilling in the drill window.



Looker query results are linked so that you can keep drilling, exploring, and uncovering new insights.

### Drilling into dashboards

You can also drill into data from dashboards. For example, suppose you have a dashboard called **Business Overview** that has a filter on the field **State** for all dashboard tiles. In this example Explore, which is a query tile on the dashboard, the **Business Overview** dashboard appears as an option in the **Dashboards** section of the drill menu for the **State** field, since the **State** field is used as a filter on that dashboard:

![A single dashboard is listed in the Dashboards section of the drill menu for the State field.](https://docs.cloud.google.com/static/looker/docs/images/exploring-drill-dashboards-718.png)

When you click the name of the dashboard in the drill menu's **Dashboards** section, Looker takes you to the **Business Overview** dashboard, with the filter for the dashboard set to the value for the **State** field that you selected in the Explore.

## Using links and data actions

The presence of links or data actions is indicated by an ellipsis (…) following the value in an Explore column. You can access links and action options by clicking the ellipsis (...) to open the drill menu.

### Using links

Your Looker developers may have added links to your data. The option to open the link will be available in the **Links** section of the drill menu when you click a value in a data table column.

For example, if a developer adds a link to an external resource to the **Percent Flights Delayed** field, Looker provides an option to navigate to that resource. You can select this option in the **Links** section of the drill menu when you select a value from the **Percent Flights Delayed** column in a data table.

![Drill menu options for the 100.00% = 2 Delays / 2 total Percent Flights Delayed value include a link to open a resource called delay risk score details in a new browser tab in the Links section.](https://docs.cloud.google.com/static/looker/docs/images/nextgen-explore-link-262.png)

### Using data actions

Your Looker developers may have added [data actions](https://docs.cloud.google.com/looker/docs/reference/param-field-action) to the dimensions or measures in your data. With data actions, you can perform tasks with other tools directly from Looker, such as sending an email or setting values in other applications. These data actions appear in the drill menu in the **Actions** section.

![Drill menu options for the 100.00% = 2 Delays / 2 total value include an option to Send Customer Delay Notification Email in the Actions section.](https://docs.cloud.google.com/static/looker/docs/images/nextgen-explore-action-262.png)

In this example, the **Percent Flights Delayed** field has a link to email a delay notification to customers. When the user clicks a column value and chooses the **Send Customer Delay Notification Email** action, the user will be taken to an email service to send a delay notification to impacted customers.

## Related resources

Now that you know how powerful the Explore experience is for learning more about data and discovering insights through iterative searches, you might want to learn how to do the following:

  * Learn how to [create or edit Explores](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores).
  * Learn how to [edit visualizations](https://docs.cloud.google.com/looker/docs/creating-visualizations).
  * Learn how to [save Explore queries as Looks](https://docs.cloud.google.com/looker/docs/saving-and-editing-looks).
  * Learn how to [add Explore queries to dashboards](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#creating_a_dashboard_from_a_look_or_an_explore).
  * Learn how to [share data](https://docs.cloud.google.com/looker/docs/sharing-data) with other users.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 

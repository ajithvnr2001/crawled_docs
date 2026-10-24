---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/best-practices-reporting-managers/
title: Best practices guide for reporting managers \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-24T05:40:50.132142+00:00
---

# Best practices guide for reporting managers  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/best-practices-reporting-managers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)



Send feedback 

#  Best practices guide for reporting managers Stay organized with collections  Save and categorize content based on your preferences. 

As a reporting manager, understanding and effectively using Contact Center AI Platform (CCAI Platform) reporting capabilities is crucial for monitoring performance, identifying trends, and making data-driven decisions. This guide helps you navigate the reporting tools and apply best practices.

## Understand CCAI Platform reporting platforms: standard versus advanced reporting

CCAI Platform offers two main reporting platforms, each with distinct advantages:

  * **Standard reporting** : This is an out-of-the-box solution that provides quick, straightforward access to essential data. It includes prebuilt dashboards and reports for key areas like **Agents & Teams**, **Calls & Chats**, and **Queues**. You can download these reports as CSV files.

  * **Advanced reporting** : This platform includes all standard reporting capabilities plus additional features for deeper, more granular analysis. Powered by Looker, it lets you explore, share, and visualize your data through custom dashboards, Looks (saved queries), and various visualizations for detailed insights.




## Access reports and dashboards

You can access different reporting tools from various locations within the CCAI Platform portal:

  * **Dashboards** : Most monitoring dashboards are available from the **Dashboard** tab.

  * **Standard reports** : These are generated from the **Reports** tab.

  * **Advanced reporting** : Access this section at **Dashboards > Advanced Reporting**.

  * **WFM reporting** : Workforce management reports are located under the **WFM Reporting > Agent Reports** tab.

  * **Audit log** : Track changes to portal settings at **Settings > Audit Dashboard**.

  * **Integration logs** : Find troubleshooting logs in **Reports > Session Data**.




## Permissions and data access control

Reporting access in CCAI Platform is **role-based** , ensuring users only see the data relevant to them. Permissions for standard dashboards are highly granular and set per dashboard, whereas permissions for advanced reporting fall into two categories: **View** and **Edit**.

  * **Admins** : Have full access to all data and functionalities.

  * **Managers** : Their access is typically limited to the data for the agents, teams, or queues they are assigned to.

  * **Agents** : Generally have no access to reporting dashboards.

  * **Custom roles** : You can create custom roles with specific permissions for greater flexibility.




The next two tables clarify the permissions depending on reporting type and role.

### Standard dashboards permissions

Role | Viewing permissions for all standard dashboards  
---|---  
Admin | ✅ Full access – _All queues_  
Manager | ✅ Limited access – _Assigned queues only_  
Agent | ❌ No access  
Developer | ❌ No access  
Manager Admin | ✅ Full access – _All queues_  
Manager Team | ✅ Limited access – _Assigned queues only_  
Manager Data | ✅ Limited access – _Assigned queues only_  
  
### Advanced reporting permissions

Role | View access for AR | Edit access for AR  
---|---|---  
Admin | ✅ Full access – _All queues_ | ✅ Edit access  
Manager | ✅ _Assigned queues only_ | ❌ No access  
Agent | ❌ No access | ❌ No access  
Developer | ❌ No access | ❌ No access  
Manager Admin | ✅ Full access – _All queues_ | ✅ Edit access  
Manager Team | ✅ Assigned queues only | ❌ No access  
Manager Data | ✅ Assigned queues only | ❌ No access  
  
## Reload versus refresh

The main difference between reload and refresh is that the **Clear cache and refresh** button clears the cache and fetches requested data from the backend database. In contrast, the reload icon first attempts to fetch data from the cache; if it's not present, it then retrieves data from the database. If the requested data is in the cache, the reload button should provide a faster experience from the user's perspective.

If a filter is applied or another change, such as the date, is made and the reload button is used, the dashboard displays new data. If users want to see up-to-the-moment results and haven't made any changes to filters on the dashboard, they should clear the cache and refresh to observe the latest data.

### Reload

If the dashboard has had no changes made to it, when the user clicks the reload button, it returns the exact same results as it did initially. This is because it is still looking at cached data.

### Refresh

The **Clear cache and refresh** button clears the cache and fetches requested data from the backend database.

### Cache

In computing, a cache is a high-speed data storage layer which stores a subset of data, typically transient in nature, so that future requests for that data are served up faster than is possible by accessing the data's primary storage location. Caching lets you efficiently reuse previously retrieved or computed data.

The data in a cache is generally stored in fast-access hardware such as RAM (random-access memory) and may also be used in correlation with a software component. A cache's primary purpose is to increase data retrieval performance by reducing the need to access the underlying slower storage layer. Trading off capacity for speed, a cache typically stores a subset of data transiently, in contrast to databases whose data is usually complete and durable.

## Filtering, customization, and visualization

Effectively analyzing data requires filtering and thoughtful visualization.

  * **Filters** : Use the available filters on dashboards (for example, **Team** , **Queue** , **Agent Name** , **Date**) to drill down into specific datasets. For better performance, it's always best to apply filters to limit the data returned by queries.

  * **Customization** : In advanced reporting, you can create custom dashboards, rearrange layouts with drag-and-drop tiles, and rename metrics to match your business's terminology.

  * **Custom metrics** : While you can create your own metrics, it is a best practice to perform complex or frequently used calculations within the underlying LookML model rather than creating excessive calculated fields on the dashboard itself. This greatly improves performance and reliability.

  * **Visualizations** : Select from various visualization types like charts, tables, and funnels. Always keep your audience in mind and use concise titles to make data clear to interpret. Avoid overly complex visuals.

  * **Organization** : Keep your custom reports organized by using personal, group, or shared folders.




### Clarification on filter hierarchy in advanced reporting

Advanced reporting allows for a powerful, multi-layered approach to data filtering, which, if not carefully managed, can lead to perceived data consistency issues:

  * **Dashboard-level filters** : These filters are set at the dashboard level and are intended to apply broadly across multiple query tiles on that dashboard. When a new tile is added to a dashboard, and it originates from the same "Explore" (the starting point for queries) as a dashboard filter, that dashboard filter is automatically applied to the new tile.

  * **Tile-level filters (implicit)** : Individual query tiles are often derived from "Looks" or "Explores," which may have their own filters already applied during their creation. These inherent filters are part of the saved query that forms the tile.

  * **Interaction and potential conflicts** : The core of the data consistency challenge arises from how these two levels interact. While a dashboard filter is automatically applied to relevant tiles, administrators and users have granular control. You can explicitly choose not to apply a dashboard filter to a specific tile, or you can even direct it to filter a _different field_ within that individual tile. Furthermore, the system prevents applying multiple filters that use the _same field_ to the same dashboard tile, indicating a potential for conflict if a tile's inherent filter on a field clashes with a dashboard filter attempting to target that exact same field. This means a tile's data might be shaped by its own embedded filter, a dashboard-wide filter, or a combination, leading to varied results that require careful validation.




For more information, see [Filters: Retrieving data using filters](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-use-filters).

## Advanced reporting: performance and limitations

The advanced reporting platform is powerful, but it has technical limitations to be aware of to ensure optimal performance.

  * **Data display limit** : Results displayed in the browser are limited to 5,000 rows. For best performance, reports should ideally contain 50 or fewer columns.

  * **Dashboard complexity** : Dashboards with an excessive number of visualizations or tiles can cause significant performance issues. For example, a dashboard with 55 tiles can cause an overall system performance degradation by overloading the underlying database and causing a bottleneck for everybody trying to retrieve data. It is critical to keep dashboards focused and avoid overloading them.

    * We recommend no more than 5 tiles for an auto-refresh configured dashboard and no more than 10 tiles for regular dashboards.
  * **Data extraction limit** : Extracted data sources have a 100 MB size limit.

  * **Merged results/queries** : Merging results from multiple Explores isn't a supported advanced reporting capability. Merged queries are processed in Looker's memory, are restricted to left joins, and are capped per contributing query, which can degrade performance of the shared reporting platform for all users. The **Save** action is disabled for merged queries. If you need data from two Explores combined, raise a request so the join can be modeled in LookML instead.




## Data consistency: real-time versus historical

Be aware of how and when data is updated.

  * Real-time dashboards auto-refresh approximately every 20 seconds. For the most accurate data, use the **Clear cache and refresh** function on your dashboard.

  * Slight differences may exist between real-time dashboards and historical reports due to the nature of the reporting. Real-time (or live) dashboards have data that is being updated while sessions are ongoing, so it might change before completion; meanwhile, historical data is persistent and immutable. For example, voicemails aren't part of the real-time dashboards because they are identified after the voicemail call is completed.




## Manage reports

You can schedule recurring deliveries of dashboards and Looks by email in PDF, CSV, or PNG formats. When scheduling, you can add custom messages and apply filters to send targeted data to specific recipients. Advanced reporting also lets you share dashboards directly with those with **Advanced Reporting | View** access.

### Schedule reports

Scheduling reports lets you automatically deliver dashboards and Looks (saved queries) to various recipients at chosen frequencies and in preferred formats. This is a valuable feature for keeping stakeholders informed of key performance indicators and operational updates.

**Access the schedule delivery feature** : To schedule a report or dashboard, navigate to the specific dashboard or Look you want to send. You will typically find a **Schedule Delivery** button or an option within a three-dot menu on the dashboard or Look.

**Customize delivery settings** : After you access the schedule and send window, you can customize various aspects of your delivery:

  * **Schedule name** : The system automatically provides a default name, usually the dashboard's name, which you can edit.

  * **Recurrence (frequency)** : You can set how often the dashboard should be delivered. Options include:

    * Every 15 minutes

    * Hourly

    * Daily

    * Weekly

    * Monthly

    * **Send now** : You also have the option to send the dashboard immediately as a one-time delivery.

  * **Destination (recipients)** : Deliveries can be sent by email. You can add multiple recipients, both internal and external to your organization, by entering their email addresses. Use the `Enter` key or a comma after each address.

  * **Format** : Choose the file format for your delivery. Available options include:

    * **PDF** : Delivers an image of the dashboard as a single PDF file. You can adjust settings like paper size and whether to expand tables to show all rows or arrange tiles in a single column.

    * **CSV zip file** : Delivers the unformatted data from dashboard query tiles as a collection of CSV files in a zipped directory. Text tiles are excluded from CSV downloads. When time-related metrics are exported to CSV, they appear in seconds, whereas in dashboards, they are displayed as `HH:MM:SS`.

    * **PNG visualization** : Delivers an image of the dashboard as a single PNG file.

  * **Filters** : You can apply filters to your scheduled delivery to ensure only relevant data is sent to recipients. These filters are based on existing dashboard filters, and editing their values in the scheduling menu only affects the delivery, not the dashboard itself.

  * **Custom message** : For email deliveries, you can include a custom message in the email body to provide context for the data.

  * **Delivery time zone** : By default, the delivery uses the same time zone as the dashboard. You can specify a different time zone for the delivery, which doesn't affect the dashboard data, only the timing of the delivery.




**Advanced reporting specifics** : In advanced reporting, you can create and store dashboards in personal, group, or shared folders, with access defined by user permissions (**View** or **Edit** roles). Custom dashboards can be created from existing Looks or Explores.

#### Testing and management

  * You can run a **Test Now** schedule to preview how the dashboard will look in the selected format. Note that there's a known issue where the **Test Now** button in the **Filters** tab isn't working.

  * Existing schedules can be managed and modified at any time from the dashboard settings menu.




#### Key considerations

  * A 45-day limit applies to the date range filter for optimizing performance in both standard and advanced reporting. If this limit is exceeded, an error message appears, and no data is displayed.

    * **Example** : If today is September 1, you can pull data for January 1 - February 15 (a 45-day span). However, you can't pull data for January 1 - September 1 in a single request, since that exceeds the range limit.
  * When creating custom real-time dashboards in advanced reporting, it's recommended to set a 20-second refresh rate for optimal accuracy and performance. Refresh rates less than 20 seconds aren't supported and default to this minimum. This also applies to all tiles and tables in standard real-time dashboards.

  * Data consistency between historical reports and real-time dashboards can vary slightly; for example, historical reports may include short-abandoned calls, while dashboards might exclude them depending on settings.




Scheduling reports is like setting up a reliable mail service for your data. You define what information needs to go out (the report or dashboard), who needs to receive it (recipients), how it should look (format), and how often it should be sent (frequency), ensuring that critical insights are delivered automatically, like clockwork.

### Share reports

You can share reports manually without scheduling them primarily through downloading content in various formats or by sharing direct links (for standard dashboards only). These methods offer flexibility for one-time distribution or for users to access information on demand, all while being governed by specific user permissions.

Here's how you can manually share reports:

#### Download content

You have the ability to **download data or visualizations** from dashboards, Looks (saved queries), and Explores in several formats for manual distribution. This is useful when you need to provide a static copy of a report to someone, or for archival purposes.

Available formats are:

  * **PDF** : Downloads an image of the entire dashboard as a single PDF file. You can choose paper size, expand tables to show all rows, or arrange tiles in a single column.

  * **CSV zip file** : Delivers the unformatted data from dashboard query tiles as a collection of CSV files in a zipped directory. Text tiles aren't included. When time-related metrics are exported to CSV, they appear in seconds, whereas in dashboards, they are displayed as `HH:MM:SS`.

  * **PNG visualization** : Delivers an image of the dashboard as a single PNG file.

  * **Other formats** : For Looks, Explores, or individual dashboard tiles, you can also download data in TXT (tab-separated values), Excel spreadsheet, JSON, HTML, and Markdown formats.




When downloading, you can choose to download with "visualization options applied" (which applies the visualization settings to your download) or "as displayed in the data table" (which downloads the raw data as it appears in the table, without visualization options).

Downloads can include **Results in Table** (rows specified by the content's row limit), **All Results** (all results returned by the query), or **Custom** (up to 100,000 rows for queries with table calculations).

## Troubleshoot reporting issues

  * **Integration logs** : For diagnosing issues, download integration logs from the **Session Data** report. These logs are available for 90 days. For more information, see [Get session data reports](https://docs.cloud.google.com/contact-center/ccai-platform/docs/standard-reports#get-session-data-reports).

    * **Error logs** : Integration logs now include relevant info logs in addition to error logs.
  * **Support** : If issues persist, contact support with detailed information including agent names, call or chat IDs, timeframe, screenshots, and network details.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 

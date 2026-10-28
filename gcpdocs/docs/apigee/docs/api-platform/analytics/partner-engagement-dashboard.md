---
url: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/
title: Developer engagement \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:56:48.905075+00:00
---

# Developer engagement  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/

[ Skip to main content ](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/)
  * [Deutsch](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/?hl=de)
  * [Español](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/?hl=es-419)
  * [Français](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/?hl=id)
  * [Italiano](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/?hl=it)
  * [Português](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/?hl=ja)
  * [한국어](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/apigee-color.svg) ](https://docs.cloud.google.com/apigee/docs)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [What does this dashboard tell me?](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/#whatdoesthisdashboardtellme)
  * [The Developer Engagement dashboard](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/#the-developer-engagement-dashboard)
    * [Overview tab](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/#overview)
    * [Sum of traffic tab](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/#sumoftraffic)
    * [Sum of error count](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/#sumoferrorcount)
    * [Average of total response time](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/#averageresponsetime)
  * [Using the dashboard](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/#using-the-dashboard)
  * [Make a copy in Data Studio](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/#make-a-copy-in-data-studio)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)


Send feedback 
#  Developer engagement Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [What does this dashboard tell me?](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/#whatdoesthisdashboardtellme)
  * [The Developer Engagement dashboard](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/#the-developer-engagement-dashboard)
    * [Overview tab](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/#overview)
    * [Sum of traffic tab](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/#sumoftraffic)
    * [Sum of error count](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/#sumoferrorcount)
    * [Average of total response time](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/#averageresponsetime)
  * [Using the dashboard](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/#using-the-dashboard)
  * [Make a copy in Data Studio](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/#make-a-copy-in-data-studio)


_This page applies to**Apigee** and **Apigee hybrid**._
_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)
## What does this dashboard tell me?
The Developer Engagement dashboard tells you which of your registered app developers are generating the most API traffic. For each of your developers, you can find out who is generating the most API traffic and the most errors. For example, if a particular developer's app is generating a lot of errors relative to other developers, you can proactively address the problem with that developer. 
## The Developer Engagement dashboard
Access the Developer engagement dashboard:
In the Google Cloud console, go to the **Apigee > Analytics > Developer analysis > Developer engagement** page.
[Go to Developer engagement](https://console.cloud.google.com//apigee/analytics/developer-analysis/engagement)
The Cloud console dashboard has these sections:
  * [Overview tab](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/#overview)
  * [Sum of traffic tab](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/#sumoftraffic)
  * [Sum of error count tab](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/#sumoferrorcount)
  * [Average of total response time tab](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard/#averageresponsetime)


The dashboard is shown:
![A dashboard containing a chart about developer engagement](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/developer-engagement-console.png)
### Overview tab
The **Overview** tab shows the following information:  
| Metric  | Description  |  
| --- | --- |  
| Top 10 developer apps by traffic  | A ranking of the number of API proxy calls associated with individual developer apps.  |  
| Top 10 developers by traffic  | A ranking of developers based on the number of API proxy calls associated with them.  |  
The **Engagement details** table in the Overview tab shows the following information:  
| Detail  | Description  |  
| --- | --- |  
| Developer app  | The name of the app.  |  
| Proxy  | The name of the API proxy associated with the app.  |  
| Developer  | The email address of the developer who registered the app or the AppGroup Id in the case of an AppGroup.  |  
| API product  | The product name associated with the app.  |  
| Traffic  | The amount of traffic generated by the app for the selected time period.  |  
| Errors  | The total number of errors generated by the app for the selected time period.  |  
| Error Rate  | The error percentage calculated by dividing total errors by total traffic for the selected time period.  |  
### Sum of traffic tab
The **Sum of traffic** tab shows API proxy traffic details for the filtered items. It includes:  
| Metric  | Description  |  
| --- | --- |  
| Traffic by proxy  | API calls recorded for the selected API proxies.  |  
| Traffic by developer  | API calls recorded for API proxies associated with selected developers.  |  
| Traffic by products  |  API calls recorded for API proxies associated with selected API products.  |  
| Traffic by app  | API calls recorded for API proxies associated with selected developer apps.  |  
### Sum of error count
The **Sum of error count** tab shows API proxy traffic error counts for the filtered items. It includes:  
| Metric  | Description  |  
| --- | --- |  
| Errors by proxy  | API errors recorded for the selected API proxies.  |  
| Errors by developers  | API errors recorded for API proxies associated with selected developers.  |  
| Errors by products  | API errors recorded for API proxies associated with selected API products.  |  
| Errors by app  | API errors recorded for API proxies associated with selected developer apps.  |  
### Average of total response time
The **Average of total response time** tab shows response time or latency information for the filtered items. It includes:  
| Metric  | Description  |  
| --- | --- |  
| Average of total response time by proxy  | Average of total response time for the selected API proxies.  |  
| Average of total response time by developer  | Average of total response time recorded for API proxies associated with selected developers.  |  
| Average of total response time by products  | Average of total response time recorded for API proxies associated with selected API products.  |  
| Average of total response time by app  | Average of total response time recorded for API proxies associated with selected developer apps.  |  
## Using the dashboard
The dashboard has a set of dropdown menus that you can use to filter the information shown in the dashboard. The filter dropdown menus are dynamic. For example, if you select a developer from the Developers dropdown, then any proxies, apps, and API products associated with that developer are automatically selected in the other dropdown menus, charts, and tables . For more information, see [About filter properties](https://docs.cloud.google.com/looker/docs/studio/about-filter-properties) in the Data Studio documentation.
Use the date selector to pick a start and end date to measure. The date selector only lets you select dates in day increments. You can't select a time range increment that is smaller than a day.
## Make a copy in Data Studio
You can edit, save, and share a copy of the dashboard in [Data Studio](https://docs.cloud.google.com/looker/docs/studio/new-studio-docs). To get started:
  1. Click **Make a copy in Data Studio**.
  2. From the dropdown menu, select the report you wish to copy.
  3. In Data Studio, click **Save and share**.
  4. Click **Acknowledge and save**.


You can now edit the copy saved in your user account. For details on using Data Studio to edit and create reports, see the [Data Studio documentation](https://docs.cloud.google.com/looker/docs/studio/about-reports).
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

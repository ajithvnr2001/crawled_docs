---
url: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/
title: Monitor and analyze MCP traffic with Apigee API hub API insights \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:47:02.113865+00:00
---

# Monitor and analyze MCP traffic with Apigee API hub API insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/

[ Skip to main content ](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/)
  * [Deutsch](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/?hl=es-419)
  * [Français](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/?hl=id)
  * [Italiano](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/?hl=ja)
  * [한국어](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fapigee%2Fdocs%2Fapi-platform%2Fapigee-mcp%2Fmonitor-analyze-mcp-traffic%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/apigee-color.svg) ](https://docs.cloud.google.com/apigee/docs)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Accessing API insights in API hub](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/#accessing-api-insights-in-api-hub)
    * [View API insights for all proxies](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/#view-api-insights-for-all-proxies)
    * [View API insights for a specific proxy](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/#view-api-insights-for-a-specific-proxy)
  * [What's next](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/#whats-next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)


Was this helpful?
Send feedback 
#  Monitor and analyze MCP traffic with Apigee API hub API insights Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Accessing API insights in API hub](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/#accessing-api-insights-in-api-hub)
    * [View API insights for all proxies](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/#view-api-insights-for-all-proxies)
    * [View API insights for a specific proxy](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/#view-api-insights-for-a-specific-proxy)
  * [What's next](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/#whats-next)


_This page applies to**Apigee** and **Apigee hybrid**._
_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)
This page describes how to monitor and analyze traffic to your MCP Discovery Proxies using the API insights dashboards in Apigee API hub.
MCP in Apigee adds specific attributes (analytics fields) to API traffic. You can filter by these fields in using the **API insights** dashboards in **API hub**. 
  * **API style:** Filter by `MCP` to isolate agentic traffic from standard REST/SOAP traffic.
  * **MCP tool name:** View metrics for specific tools (such as `create_refund`, `check_order_status`) instead of viewing all requests for the general `/mcp` proxy endpoint.


The **API style** and **MCP tool name** filters are available for the following dashboards:
  * [API performance](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/#api-performance)
  * [API error analysis](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/#api-error-analysis)
  * [Latency analysis](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/#latency-analysis)
  * [Target performance](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/monitor-analyze-mcp-traffic/#target-performance)


The **MCP tool name** filter is also available on the **Insights** tab of the **API proxy** details page in Google Cloud console. 
Filtering by the `API style` and `MCP tool name` fields allows you focus on agentic traffic only and to see the performance of individual tools rather than the aggregate traffic to the `/mcp` proxy endpoint.
## Accessing API insights in API hub
Before accessing API insights in API hub, confirm the following:
  * Make sure that Apigee API Analytics is enabled for your Apigee organization. For more information, see [Analytics services overview](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-services-overview#how-do-i-get-started).
  * Make sure that [API insights](https://docs.cloud.google.com/apigee/docs/apihub/configure-api-insights) is configured in API hub to view and analyze API data from your attached gateways.
  * Make sure you have the [required IAM roles](https://docs.cloud.google.com/apigee/docs/apihub/api-insights-overview#iam-roles) to access API insights.


### View API insights for all proxies
To view API insights for all proxies, do the following:
  1. In the Google Cloud console, go to the **API insights** page in **Apigee API hub**.
[ Go to API insights](https://console.cloud.google.com/apigee/api-hub/api-insights)
  2. In the **Dashboards** pane, select a dashboard.
     * To filter the data in the dashboard by API style, use the **API style** filter dropdown to select **MCP**. 
     * To filter the data in the dashboard by MCP tool name, use the **MCP tool name** filter dropdown to select your MCP tool name. 


### View API insights for a specific proxy
To view API insights for a specific proxy, do the following:
  1. In the Google Cloud console, go to the **APIs** page in **Apigee API hub**. [ Go to APIs](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Select the name of the proxy for which you want to view API insights.
  3. Click the **Insights** tab.
  4. To filter the data in the dashboard by MCP tool name for the selected proxy, use the **MCP tool name** filter dropdown to select your MCP tool or tools.


For more detailed information about using API insights, see [API insights dashboards](https://docs.cloud.google.com/apigee/docs/apihub/api-insights-dashboard#api-performance).
## What's next
Learn more about MCP in Apigee in [Apigee MCP overview](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-overview).
For Apigee hybrid, see [Enable MCP in Apigee hybrid](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/enable-mcp).
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

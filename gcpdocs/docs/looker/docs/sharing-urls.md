---
url: https://docs.cloud.google.com/looker/docs/sharing-urls/
title: Sharing data from URLs \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:51:19.644615+00:00
---

# Sharing data from URLs  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/sharing-urls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Sharing data from URLs Stay organized with collections  Save and categorize content based on your preferences. 

Looker lets you copy and share URLs so that others can view your queries, Looks, and dashboards. You can share query and dashboard links with other Looker users or [publish a Look with a public URL](https://docs.cloud.google.com/looker/docs/publishing-looks-with-public-urls) to send data outside your instance.

## Sharing a query's URL

After you've run a query, you can share the query's URL with another Looker user. They will arrive at the same query and visualization. The URL will point the user to the same query and visualization.

When sharing URLs, keep the following things in mind:

  * When you share a URL with someone, you are sharing the _query_ , not the actual _data_. This means that the data could change between the time you pull a query and the time your colleague runs a query. For example, if you set up a query to look at "today," the data might change if the user accesses the URL the day after you send it.
  * The URLs never expire and can't be revoked. However, since the link works only for someone who has access to your Looker instance and that data, sending a link shouldn't cause a security concern.



### Browser URL

To share a URL from a dashboard, a Look, or an Explore, copy the URL from your browser's address bar.

### Short URL

Sometimes it's preferable to share a shorter URL when you want to share an Explore query. To share an Explore query as a shorter URL, follow these steps:

  1. Click the **Save or share** button.

If you're using a classic Explore, click the settings **Explore Actions** menu.

  2. Select the attachment **Share URLs** option to open the **Share URLs** menu.

If you're using a classic Explore, click **Share** to open the **Share URLs** menu.

  3. Copy the URL that appears in the **Short URL** field.




The **Short URL** contains the Explore slug. A slug is a randomly chosen short string that takes the place of the content ID value in a URL. For example, in this short URL, `https://docserver.cloud.looker.com/x/79WcoBSRqh8YVglvYe6mHL`, the string `79WcoBSRqh8YVglvYe6mHL` is the slug.

### Expanded URL

The **Share URLs** menu also provides the **Expanded URL** option. An expanded URL shows all of the details for the query, including fields and filters. This information can be useful for developers who want to modify a parameterized URL. This is often useful in a custom LookML field or an external tool.

## Sharing a dashboard URL

Selecting the **Get link** option from the dashboard's [three-dot menu](https://docs.cloud.google.com/looker/docs/viewing-dashboards#three-dot_dashboard_menu) reveals a dialog that contains a link to the dashboard, which can be copied and shared.

By default, the **Include current filter values in URL** switch is enabled, and the link contains the URL parameters for the filter values as they appear on the dashboard. This means that if you have [temporarily changed](https://docs.cloud.google.com/looker/docs/viewing-dashboards#temporarily_changing_filter_values_on_dashboards) the filter values away from the default values, the link displays the dashboard with the changed filter values. If you have not temporarily changed any filter values, the link displays the dashboard with default filter values. The link also displays any [cross-filters](https://docs.cloud.google.com/looker/docs/cross-filtering-dashboards) that are applied to the dashboard, if cross-filtering is enabled.

You can also view the dashboard slug by selecting **Get link**. The slug is a randomly chosen short string that takes the place of the content ID value in a URL. For example, in this dashboard URL, `https://docserver.cloud.looker.com/dashboards/CQ1fu99Z9Y1ggq2wcHDfMm`, the string `CQ1fu99Z9Y1ggq2wcHDfMm` is the slug.

If you disable the **Include current filter values in URL** switch, the dialog contains a shorter link, which displays the dashboard with default filter values and no cross-filters applied.

To view the dashboard, anyone with the link must have access to the Looker instance on which the dashboard is saved, as well as access to the [dashboard](https://docs.cloud.google.com/looker/docs/organizing-spaces#viewing_and_managing_access_for_a_folder) and [models](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#model_sets) that the tiles are based on.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 

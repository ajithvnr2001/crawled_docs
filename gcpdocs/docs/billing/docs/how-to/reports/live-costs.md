---
url: https://docs.cloud.google.com/billing/docs/how-to/reports/live-costs/
title: Billing reports: View your live costs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-24T05:40:34.598583+00:00
---

# Billing reports: View your live costs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/reports/live-costs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Billing reports: View your live costs Stay organized with collections  Save and categorize content based on your preferences. 

In [Cloud Billing cost reports](https://docs.cloud.google.com/billing/docs/how-to/reports), you can use the live costs report to see how your _gross, estimated_ costs are trending. When spend caps or anomaly alerts are triggered, live costs can help you identify which specific SKUs, services, or projects are driving your costs.

## Live costs and actual costs

**Live costs** are _gross, estimated_ costs that are available in near-real-time for limited SKUs from eligible services. Live costs haven't been finalized, and don't include credits or savings. Live costs are calculated based on the [pricing](https://docs.cloud.google.com/billing/docs/how-to/pricing-table) for each SKU that is applicable to your Cloud Billing account.

**Actual costs** are _finalized_ costs that are generated when your usage undergoes a complex monetization process that includes pricing, currency conversion, and discount computations. Actual costs might take up to 24 hours after usage to finalize.

![Example of the reports page, configured to show live costs by SKU.](https://docs.cloud.google.com/static/billing/docs/images/billing-reports-live-costs.png)Example of the reports page, configured to show live costs by SKU. 

![](https://docs.cloud.google.com/static/billing/docs/images/billing-reports-live-costs.png)

## How to view your live costs

You access the live costs report using a _preset_ report.

To open Billing Reports and select the _preset_ cost report to view your live costs, complete the following steps:

  1. Make sure that you have the [**permissions required to access and view billing reports**](https://docs.cloud.google.com/billing/docs/how-to/reports#required-permissions).

  2. **Open the Cloud Billing Reports page**

Follow these steps to **open the Reports page** for your Cloud Billing account:

     1. In the **Google Cloud console** , go to the **Reports** page for your **Cloud Billing** account.

[Go to Billing Reports](https://console.cloud.google.com/billing/reports)

     2. At the prompt, select the Cloud Billing account that you want to analyze.

The **Reports** page opens for the selected Cloud Billing account.

  3. Select the preset report **Live costs by SKU**.

[Preset reports](https://docs.cloud.google.com/billing/docs/how-to/reports#preset_views) are accessible in the saved reports carousel, and in the **All reports** page.

![Preset and saved reports carousel where you can open the live costs
 report.](https://docs.cloud.google.com/static/billing/docs/images/billing-reports-presets-and-saved-views-lb.png)Preset and saved reports carousel where you can open the live costs report. 

When you select the **Live costs by SKU** preset report, your Billing report is configured as follows:

     * [Time range](https://docs.cloud.google.com/billing/docs/how-to/reports#time-range): By charge period for the last 15 days.
     * [Group by](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by): SKU - shows granular costs for each SKU.
     * [Filter by](https://docs.cloud.google.com/billing/docs/how-to/reports#filters): All **SKUs** , **Services** , and **Projects**.



### Customize the live costs report

You can customize the live costs report using the following options:

Report setting | Description  
---|---  
**Time range** | You can set the _starting_ ("From") date for a [ **Charge period**](https://docs.cloud.google.com/billing/docs/how-to/reports#usage-date) _Time range_ , up to the last 90 days. Because live costs are _estimated_ costs that have value for about 24 hours, you can't set the ending ("To") date. The time range ending date is configured for you and locked to include _now_ (today's date) in the "To" date.  
**Group by** | In live costs reports, you can select any of the following [ Group by options](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by): 

  * SKU
  * Service

  
**Filters** | In live costs reports, the following [ Filters](https://docs.cloud.google.com/billing/docs/how-to/reports#filters) are available: 

  * SKUs
  * Services
  * Projects

  
  
### View live costs for a spend cap budget

You can configure the live costs report to analyze the costs for a spend cap budget. Each spend cap budget is scoped to a _single_ Google Cloud project and a _single_ [eligible service](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps#eligible-services).

You can view the detailed live costs for a spend cap budget by grouping by SKU, and filtering by the spend cap budget's _service_ and _project_.

When your spend cap budget is enforced, the live costs report can help you identify the SKUs that are contributing the most to your spend cap limit.

To open Billing Reports and select the _preset_ cost report to view your live costs, complete the following steps:

  1. Make sure that you have the [**permissions required to access and view billing reports**](https://docs.cloud.google.com/billing/docs/how-to/reports#required-permissions).

  2. **Open the Cloud Billing Reports page**

Follow these steps to **open the Reports page** for your Cloud Billing account:

     1. In the **Google Cloud console** , go to the **Reports** page for your **Cloud Billing** account.

[Go to Billing Reports](https://console.cloud.google.com/billing/reports)

     2. At the prompt, select the Cloud Billing account that you want to analyze.

The **Reports** page opens for the selected Cloud Billing account.

  3. Select the preset report **Live costs by SKU**.

[Preset reports](https://docs.cloud.google.com/billing/docs/how-to/reports#preset_views) are accessible in the saved reports carousel, and in the **All reports** page.

![Preset and saved reports carousel where you can open the live costs
 report.](https://docs.cloud.google.com/static/billing/docs/images/billing-reports-presets-and-saved-views-lb.png)Preset and saved reports carousel where you can open the live costs report. 
  4. In the **Live costs by SKU** report, configure the following settings:

     * **Time range** : Select the **Current month** charge period.
     * **Group by** : Select **SKU**.
     * **Filters** : 
       * Select **Services** and choose the service that your spend cap budget is scoped to.
       * Select **Projects** and choose the project that your spend cap budget is scoped to.

The resulting report helps you identify the specific SKUs that are contributing the most to your spend cap budget amount.




## Limitations

The following limitations apply when using the live costs report:

  * Live cost totals are _gross, estimated_ costs and don't include any savings or credits. If you've purchased a [Flexible Savings Plan (FSP)](https://docs.cloud.google.com/docs/cuds-flexible-savings-plans) committed use discount (CUD), the _estimated_ live costs won't reflect your CUD savings. For any of your [eligible SKUs](https://docs.cloud.google.com/docs/cuds-flexible-savings-plans#find_skus) that are covered by an FSP, your live costs amounts might appear higher than your actual costs.

  * The live costs report doesn't show usage associated with _child_ billing accounts. The live costs report isn't available for _Account group_ and _Management account_ billing account types.

  * For reseller accounts, the live costs report only shows costs incurred by direct usage in the _parent_ reseller billing account, and excludes usage from subaccounts.

  * Live costs are only available for the _Charge period_ time range, and the live costs report offers fewer group by and filter options than the standard billing reports.




## What's next

  * Learn more about how to [analyze billing data with Reports](https://docs.cloud.google.com/billing/docs/how-to/reports).
  * Learn more about [how to manage Gemini Enterprise costs](https://docs.cloud.google.com/gemini/enterprise/docs/manage-costs-overview).
  * Learn how to [view Gemini Enterprise costs in the Gemini Enterprise console](https://docs.cloud.google.com/gemini/enterprise/docs/view-costs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 

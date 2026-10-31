---
url: https://docs.cloud.google.com/gemini/enterprise/docs/view-costs/
title: View costs \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:46:55.532590+00:00
---

# View costs  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/view-costs/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  View costs Stay organized with collections  Save and categorize content based on your preferences. 

In Gemini Enterprise, the **Spend** tab on the **Usage & spend** page displays a summary of your Gemini Enterprise costs over the last 30 days across your enabled features and tools.

**Note:** The **Spend** tab displays net costs (after credits and discounts) for your linked Cloud Billing account, including both license-based Gemini Enterprise subscription costs and pay-as-you-go usage costs.

The **Spend** tab displays total Gemini Enterprise costs that include charges for:

  * Gemini Enterprise app
  * Gemini Enterprise Agent Platform
  * AI developer tools (such as Google Antigravity)



## Key concepts

This section introduces key billing concepts for viewing costs in Gemini Enterprise. Term | Definition  
---|---  
**License** |  Gives a user access to a license-based edition, such as Gemini Enterprise Standard or Plus. Licenses are billed to your Cloud Billing account. For more information, see [Get subscriptions and assign licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses).   
**Pay-as-you-go usage above quota** |  A setting that lets usage continue after the pooled quota runs out. This usage is charged at pay-as-you-go rates. For more information, see [Configure pay-as-you-go usage above quota](https://docs.cloud.google.com/gemini/enterprise/docs/configure-pay-as-you-go-usage-above-quota).   
**Pay-as-you-go edition** |  An edition with no license fee and no pooled quota. All usage is charged at [pay-as-you-go rates](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-pay-as-you-go-usage#quotas-pay-as-you-go).   
**Prepaid credits** |  Credits that a self-serve billing account buys in advance. Paid usage is deducted from the credit balance. When you turn on pay-as-you-go usage above quota for the first time, you can continue with a zero balance. If your balance is zero, usage above quota stops until you add credits. If prepaid credits are already set up and your balance is zero, you must add credits before turning it on again. To use the Pay-as-you-go edition, you must buy credits when setting up prepaid credits on your billing account. For more information, see [Manage prepaid credits](https://docs.cloud.google.com/gemini/enterprise/docs/manage-prepaid-credits).   
  
## Before you begin

To view cost details on the **Usage & spend** page, you need the following IAM roles and permissions:

  * **Required roles** :

    * [Gemini Enterprise Admin](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) (`roles/discoveryengine.agentspaceAdmin`) on the project
    * [Billing Account Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.viewer) (`roles/billing.viewer`) or [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`) on the target billing account
  * **Required permissions** :

    * `monitoring.timeSeries.list` (included by default in the [Gemini Enterprise Admin](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role)
    * `serviceconsumermanagement.quota.get`

Without these permissions, the **Spend** tab isn't visible. If you use custom roles that don't include these permissions, you must [add the required permissions to the role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#edit-role).




## View costs and cost trends

To view your Gemini Enterprise costs, follow these steps:

  1. In the Google Cloud console, go to the **Gemini Enterprise > Usage & spend** page.

[Go to Usage & spend](https://console.cloud.google.com/gemini-enterprise/usage-and-spending)

  2. Select the **Spend** tab.

The **Gemini Enterprise costs (Last 30 days)** section displays the following cost breakdown:

Cost item | Description  
---|---  
Gemini Enterprise app |  Charges for Gemini Enterprise subscriptions and feature usage.   
Gemini Enterprise Agent Platform | Charges for building and deploying AI models and agents.  
AI developer tools (such as Antigravity) |  Charges for AI coding and developer tool usage, including Antigravity.   
Total cost |  The combined sum of these costs (after credits and discounts), along with a 30-day cost trend chart.   
  3. To inspect detailed cost breakdowns, invoices, or reports in the Cloud Billing console, click **View details in Billing**.

For more information on billing reports and cost analysis in Cloud Billing, see [View your billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports/gemini-enterprise-costs).




## Invoices for prepaid credits

If you pay with [prepaid credits](https://docs.cloud.google.com/gemini/enterprise/docs/manage-prepaid-credits), you receive two kinds of documents in Cloud Billing:

  * **Prepayment invoice:** Issued when you buy credits, manually or through auto-reload. The line item is **Prepayment for Gemini Enterprise**.
  * **Consumption invoice:** Issued monthly. The line item is **Charges for Gemini Enterprise** followed by the month and year. It lists your usage for the month and the prepaid credits applied to that usage.



To view and download invoices, go to the **Documents** page in Cloud Billing. For more information, see [View and download invoices](https://docs.cloud.google.com/billing/docs/how-to/get-invoice).

## Taxes

Prices for Gemini Enterprise don't include taxes. Any applicable taxes are calculated based on the address of your Cloud Billing account and are added to your invoices.

If you pay with prepaid credits, when tax is charged depends on your country:

  * In some countries, tax is charged when you buy credits, and it appears on the prepayment invoice.
  * In other countries, tax is charged on your usage, and it appears on the monthly consumption invoice.



## What's next

  * Learn how to [view feature usage](https://docs.cloud.google.com/gemini/enterprise/docs/feature-usage).
  * Learn how to [configure pay-as-you-go usage above quota and spend limits](https://docs.cloud.google.com/gemini/enterprise/docs/configure-pay-as-you-go-usage-above-quota).
  * Learn how to [manage prepaid credits](https://docs.cloud.google.com/gemini/enterprise/docs/manage-prepaid-credits).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 

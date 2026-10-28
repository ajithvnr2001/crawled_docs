---
url: https://docs.cloud.google.com/gemini/enterprise/docs/configure-pay-as-you-go-usage-above-quota/
title: Configure pay-as-you-go usage above quota \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T23:54:13.135620+00:00
---

# Configure pay-as-you-go usage above quota  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/configure-pay-as-you-go-usage-above-quota/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Configure pay-as-you-go usage above quota Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To use this feature, your project must be linked to an [invoiced Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) that receives an active monthly invoice.

When your project reaches its pooled quota for a feature in Gemini Enterprise, feature usage stops unless you turn on pay-as-you-go usage above quota. Turning on pay-as-you-go usage above quota (formerly referred to as overages) lets users in your project continue using features beyond the included pooled quota limits at pay-as-you-go rates.

You can turn on pay-as-you-go usage above quota only if your project has an [invoiced Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) and at least one active, non-free-trial subscription, and uses one of the following product editions:

  * Gemini Enterprise Standard
  * Gemini Enterprise Plus
  * Gemini Enterprise Frontline Starter and Frontline Worker
  * Gemini Enterprise EDU and EDU Pro
  * Gemini Enterprise Standard Emerging Market, Emerging Market EDU, Emerging Market governments. Emerging market editions are available only to eligible customers. Your Google account team assesses the requirements to determine your eligibility.

**Note:** Pay-as-you-go usage above quota doesn't apply to the **Gemini Enterprise Pay-as-you-go** edition because you pay for all feature usage on a pay-as-you-go basis.

To learn how pricing works and view the pricing tables for each feature, see [Quotas and pay-as-you-go usage](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-pay-as-you-go-usage#pay-as-you-go-usage-above-quota).

**Caution:** If you turn on pay-as-you-go usage above quota without setting a monthly spend limit, feature usage continues without restriction after your project exceeds its pooled quota, and you pay for all excess usage at pay-as-you-go rates. To prevent unexpected charges, set a monthly spend limit.

## Before you begin

You can configure pay-as-you-go usage above quota and set spend limits if you meet the following requirements:

  * You are a [Gemini Enterprise Administrator](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin).

  * You have at least one active, non-free-trial [Gemini Enterprise subscription](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#about-subscriptions) for a license-based edition (such as Gemini Enterprise Standard, Plus, Frontline, EDU, or Emerging Market editions).

  * Your project has an [invoiced Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types). To check your billing account type, see [Find out your Cloud Billing account type and charging cycle](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle#view-your-charging-cycle).




## Turn on pay-as-you-go usage above quota

To turn on pay-as-you-go usage above quota for a subscription tier, follow these steps:

  1. In the Google Cloud console, go to the **Gemini Enterprise > Usage & Spending** page.

[Go to Usage & Spending](https://console.cloud.google.com/gemini-enterprise/usage-and-spending)

  2. Select the **Usage** tab.

  3. In the tier selector banner at the top of the page, select the subscription tier you want to configure:

     * **Standard**
     * **Plus**
     * **Frontline Starter**
     * **Frontline Worker**
     * **EDU**
     * **EDU Pro**
     * **Standard Emerging**
     * **EDU Emerging**
     * **EDU Pro Emerging**
     * **EDU Gov Emerging**
  4. In the **Feature usage** section, locate the **Pay-as-you-go usage above quota** card.

  5. In the **Status** column, turn on the toggle (**Enabled**).

  6. Click **Save changes**.


**Note:** If your project's billing account isn't eligible for pay-as-you-go usage, a notice is displayed: _Pay-as-you-go usage above quota can't be turned on for this project. Please reach out to your billing account admin._

## Set a monthly spend limit

You can set a monthly spend limit on pay-as-you-go usage above quota and Pay-as-you-go edition usage for your project. When your project reaches this limit, Gemini Enterprise automatically stops usage beyond quota to prevent unexpected charges.

**Note:** Because stopping usage can take a few minutes to take effect, you might incur charges that exceed your limit.

The budget you set applies to the following product areas:

  * Gemini Enterprise app
  * Gemini Enterprise Agent Platform
  * AI coding tools such as Google Antigravity



To configure a monthly spend limit, do the following:

  1. In the Google Cloud console, go to the **Gemini Enterprise > Usage & Spending** page.

[Go to Usage & Spending](https://console.cloud.google.com/gemini-enterprise/usage-and-spending)

  2. Select the **Usage** tab.

  3. In the **Project monthly spend limit** section, click **Set limit**.

  4. In Cloud Billing, configure your budget and spend cap actions. When defining the scope of your budget, select **Vertex AI (aiplatform.googleapis.com)** from the **Services** list. Cloud Billing bills pay-as-you-go charges for Gemini Enterprise and AI developer tools under Vertex AI API.

For more information about creating budgets and configuring spend limits, see [Set budget spend caps](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps).




## Turn off pay-as-you-go usage above quota

When you turn off pay-as-you-go usage above quota, feature usage stops after your project reaches its pooled quota limits for that tier.

To turn off pay-as-you-go usage above quota for a subscription tier, follow these steps:

  1. In the Google Cloud console, go to the **Gemini Enterprise > Usage & Spending** page.

[Go to Usage & Spending](https://console.cloud.google.com/gemini-enterprise/usage-and-spending)

  2. Select the **Usage** tab.

  3. In the tier selector banner at the top of the page, select the subscription tier where you want to turn off pay-as-you-go usage.

  4. In the **Feature usage** section, locate the **Pay-as-you-go usage above quota** card.

  5. In the **Status** column, turn off the toggle (**Disabled**).

  6. Click **Save changes**.

  7. In the confirmation dialog, click **Disable**.


**Note:** If third-party models (such as Anthropic Claude models) are enabled in any of your applications and the selected tier is the only tier with pay-as-you-go usage enabled, you can't turn off pay-as-you-go usage above quota. You must first disable all third-party models in **Feature management** for each application before turning off pay-as-you-go usage on the remaining tier.

## Configure a single-user quota limit

To prevent any individual user from exhausting an edition's included subscription quota pool before other users can access it, you can configure a single-user quota limit in the **Feature usage** > **Limit any single-user's quota** section on the **Usage & Spending > Usage** tab.

Single-user quota limits apply only while your edition's subscription quota pool has remaining capacity; they don't limit pay-as-you-go usage above quota after the subscription pool is depleted. For more information, see the following:

  * [How single-user quota limits interact with pay-as-you-go usage above quota](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-pay-as-you-go-usage#single-user-limits-and-pay-as-you-go)
  * [Configure a single-user quota limit](https://docs.cloud.google.com/gemini/enterprise/docs/feature-usage#configure-single-user-quota-limit)



## What's next

  * Learn how to [view feature usage and configure single-user quota limits](https://docs.cloud.google.com/gemini/enterprise/docs/feature-usage).
  * Learn how to [view costs](https://docs.cloud.google.com/gemini/enterprise/docs/view-costs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

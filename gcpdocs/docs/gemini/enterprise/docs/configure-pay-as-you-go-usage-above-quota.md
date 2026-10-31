---
url: https://docs.cloud.google.com/gemini/enterprise/docs/configure-pay-as-you-go-usage-above-quota/
title: Configure pay-as-you-go usage above quota \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:27.150259+00:00
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

**Note:** To use this feature, your project must be linked to a [Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types). With a self-serve (online) billing account, you pay for usage above quota with [prepaid credits](https://docs.cloud.google.com/gemini/enterprise/docs/manage-prepaid-credits). With an invoiced billing account, usage above quota is billed on your monthly invoice.

Prepaid credits for self-serve (online) billing accounts are rolling out gradually. If you don't see the **Credit balance** tab on **Plans & billing** or the **AI developer tools** tab on **Settings** yet, your account hasn't been included.

When your project reaches its pooled quota for a feature in Gemini Enterprise, feature usage stops unless you turn on pay-as-you-go usage above quota. Turning on pay-as-you-go usage above quota (formerly referred to as overages) lets users in your project continue using features beyond the included pooled quota limits at pay-as-you-go rates.

To turn on pay-as-you-go usage above quota, your project needs at least one active, non-free-trial subscription for one of the following product editions:

  * Gemini Enterprise Standard
  * Gemini Enterprise Plus
  * Gemini Enterprise Frontline Starter and Frontline Worker
  * Gemini Enterprise EDU and EDU Pro
  * Gemini Enterprise Standard Emerging Market, Emerging Market EDU, Emerging Market governments. Emerging market editions are available only to eligible customers. Your Google account team assesses the requirements to determine your eligibility.

**Note:** For the **Gemini Enterprise Pay-as-you-go** edition, all feature usage is billed on a pay-as-you-go basis without pooled quota limits. For this edition, the **Status** toggle isn't shown, but you can configure the PayGo Option (Standard or Priority).

To learn how pricing works and view the pricing tables for each feature, see [Quotas and pay-as-you-go usage](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-pay-as-you-go-usage#pay-as-you-go-usage-above-quota).

**Caution:** If you turn on pay-as-you-go usage above quota without setting a monthly spend limit, feature usage continues without restriction after your project exceeds its pooled quota, and you pay for all excess usage at pay-as-you-go rates. To prevent unexpected charges, set a monthly spend limit.

## Key concepts

This section introduces key billing concepts for pay-as-you-go usage above quota in Gemini Enterprise. Term | Definition  
---|---  
**Pooled quota** |  The usage included with your licenses. Each license adds to a quota for each feature that all users in the edition share. For more information, see [Quotas and pay-as-you-go usage](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-pay-as-you-go-usage).   
**Pay-as-you-go usage above quota** |  A setting that lets usage continue after the pooled quota runs out. This usage is charged at pay-as-you-go rates.   
**Project monthly spend limit** |  A Cloud Billing budget cap that stops paid usage when your project reaches the amount that you set.   
**Billing account type** |  Determines how you pay for usage: 

  * A _self-serve (online)_ account pays with prepaid credits. 
  * An _invoiced_ account pays on its monthly invoice. 

To check your account type, see [Find out your Cloud Billing account type and charging cycle](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle#view-your-charging-cycle).   
**Prepaid credits** |  Credits that a self-serve billing account buys in advance. Paid usage is deducted from the credit balance. When you turn on pay-as-you-go usage above quota for the first time, you can continue with a zero balance. If your balance is zero, usage above quota stops until you add credits. If prepaid credits are already set up and your balance is zero, you must add credits before turning it on again. To use the Pay-as-you-go edition, you must buy credits when setting up prepaid credits on your billing account. For more information, see [Manage prepaid credits](https://docs.cloud.google.com/gemini/enterprise/docs/manage-prepaid-credits).   
  
## Before you begin

You can configure pay-as-you-go usage above quota and set spend limits if you meet the following requirements:

  * You have the [Gemini Enterprise Admin](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) (`roles/discoveryengine.agentspaceAdmin`) role on the project.

  * You have at least one active, non-free-trial [Gemini Enterprise subscription](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#about-subscriptions) for a license-based edition (such as Gemini Enterprise Standard, Plus, Frontline, EDU, or Emerging Market editions).

  * Your project is linked to a Cloud Billing account that's in good standing. To check your billing account type, see [Find out your Cloud Billing account type and charging cycle](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle#view-your-charging-cycle).

  * To turn on pay-as-you-go usage above quota for the first time with a self-serve billing account, you need the [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`) role on the billing account. This step sets up the prepaid credit balance. Without this role, the Google Cloud console shows **You do not have billing admin access**.




## Turn on pay-as-you-go usage above quota

To turn on pay-as-you-go usage above quota for a subscription tier, follow these steps:

  1. In the Google Cloud console, go to the **Gemini Enterprise > Usage & spend** page.

[Go to Usage & spend](https://console.cloud.google.com/gemini-enterprise/usage-and-spending)

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

  6. In the **PayGo Option** column, select your pay-as-you-go option:

     * **Standard** : Default pay-as-you-go throughput.
     * **Priority** : Priority pay-as-you-go provides more consistent performance than Standard PayGo without the upfront commitment of Provisioned Throughput. Priority PayGo is available only when your application location is set to **global**.
  7. Click **Save changes**.

  8. Complete the dialog that appears:

     * **Self-serve billing account (with billing permissions):** In the **Your current credit balance** dialog, click **Add credits** to [buy credits](https://docs.cloud.google.com/gemini/enterprise/docs/manage-prepaid-credits#buy-credits), or click **Continue** to use your current balance.
     * **Invoiced billing account (or self-serve without billing permissions):** In the **Overage enabled** dialog, click **Got it**.

**Note:** If your project's billing account isn't eligible or you lack billing permissions, a notice is displayed, such as _Unable to verify billing status. Please contact your Billing Account Administrator to confirm your permissions and account eligibility._ If prepaid credits are already set up on a self-serve billing account with a zero balance, a notice states: _Pay-as-you-go usage above quota can't be turned on because your prepaid credit balance is USD 0.00. Add credits to turn it on._

## Set a monthly spend limit

You can set a monthly spend limit on pay-as-you-go usage above quota and Pay-as-you-go edition usage for your project. When your project reaches this limit, Gemini Enterprise automatically stops usage beyond quota to prevent unexpected charges. Usage resumes at the start of the next month, or earlier if you [lift the spend cap](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps#lift-spend-cap).

**Note:** Because stopping usage can take some time to take effect, you might incur charges that exceed your limit.

If you pay with prepaid credits, the spend limit still applies. Usage stops when your project reaches the spend limit or your credit balance reaches zero, whichever happens first.

The budget you set applies to the following product areas:

  * Gemini Enterprise app
  * Gemini Enterprise Agent Platform
  * AI developer tools such as Google Antigravity



To configure a monthly spend limit, do the following:

  1. In the Google Cloud console, go to the **Gemini Enterprise > Usage & spend** page.

[Go to Usage & spend](https://console.cloud.google.com/gemini-enterprise/usage-and-spending)

  2. Select the **Usage** tab.

  3. In the **Project monthly spend limit** section, click **Set limit**.

  4. In Cloud Billing, configure your budget and spend cap actions. When defining the scope of your budget, select **Vertex AI (aiplatform.googleapis.com)** from the **Services** list. Cloud Billing bills pay-as-you-go charges for Gemini Enterprise and AI developer tools under Vertex AI API.

For more information about creating budgets and configuring spend limits, see [Set budget spend caps](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps).




## Turn off pay-as-you-go usage above quota

When you turn off pay-as-you-go usage above quota, feature usage stops after your project reaches its pooled quota limits for that tier.

If you pay with prepaid credits, your remaining credits stay in your balance until they expire, and you can use them if you turn pay-as-you-go usage above quota on again. Because billing data can take some time to process, you might be charged for some usage after you turn it off.

To turn off pay-as-you-go usage above quota for a subscription tier, follow these steps:

  1. In the Google Cloud console, go to the **Gemini Enterprise > Usage & spend** page.

[Go to Usage & spend](https://console.cloud.google.com/gemini-enterprise/usage-and-spending)

  2. Select the **Usage** tab.

  3. In the tier selector banner at the top of the page, select the subscription tier where you want to turn off pay-as-you-go usage.

  4. In the **Feature usage** section, locate the **Pay-as-you-go usage above quota** card.

  5. In the **Status** column, turn off the toggle (**Disabled**).

  6. Click **Save changes**.

  7. In the **Disable overage?** dialog, click **Disable overage**.


**Note:** If third-party models (such as Anthropic Claude models) are enabled in any of your applications and the selected tier is the only tier with pay-as-you-go usage enabled, you can't turn off pay-as-you-go usage above quota. You must first disable all third-party models in **Feature management** for each application before turning off pay-as-you-go usage on the remaining tier.

## Configure a single-user quota limit

To prevent any individual user from exhausting an edition's included subscription quota pool before other users can access it, you can configure a single-user quota limit in the **Feature usage** > **Limit any single-user's quota** section on the **Usage & spend > Usage** tab.

Single-user quota limits apply only while your edition's subscription quota pool has remaining capacity; they don't limit pay-as-you-go usage above quota after the subscription pool is depleted. For more information, see the following:

  * [How single-user quota limits interact with pay-as-you-go usage above quota](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-pay-as-you-go-usage#single-user-limits-and-pay-as-you-go)
  * [Configure a single-user quota limit](https://docs.cloud.google.com/gemini/enterprise/docs/feature-usage#configure-single-user-quota-limit)



## What's next

  * Learn how to [view feature usage and configure single-user quota limits](https://docs.cloud.google.com/gemini/enterprise/docs/feature-usage).
  * Learn how to [view costs](https://docs.cloud.google.com/gemini/enterprise/docs/view-costs).
  * Learn how to [manage prepaid credits](https://docs.cloud.google.com/gemini/enterprise/docs/manage-prepaid-credits).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 

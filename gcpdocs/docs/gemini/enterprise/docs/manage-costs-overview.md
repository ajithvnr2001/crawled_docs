---
url: https://docs.cloud.google.com/gemini/enterprise/docs/manage-costs-overview/
title: How billing works in Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:27.549129+00:00
---

# How billing works in Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/manage-costs-overview/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  How billing works in Gemini Enterprise Stay organized with collections  Save and categorize content based on your preferences. 

Understanding how Gemini Enterprise bills for licenses and usage helps you choose the right model for your team. This page explains how charges flow and where you can keep an eye on your costs.

## Billing concepts

Term | Definition  
---|---  
**License** |  Gives a user access to a license-based edition, such as Gemini Enterprise Standard or Plus. Licenses are billed to your Cloud Billing account. For more information, see [Get subscriptions and assign licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses).   
**Pooled quota** |  The usage included with your licenses. Each license adds to a quota for each feature that all users in the edition share. For more information, see [Quotas and pay-as-you-go usage](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-pay-as-you-go-usage).   
**Pay-as-you-go usage above quota** |  A setting that lets usage continue after the pooled quota runs out. This usage is charged at pay-as-you-go rates. For more information, see [Configure pay-as-you-go usage above quota](https://docs.cloud.google.com/gemini/enterprise/docs/configure-pay-as-you-go-usage-above-quota).   
**Pay-as-you-go edition** |  An edition with no license fee and no pooled quota. All usage is charged at [pay-as-you-go rates](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-pay-as-you-go-usage#quotas-pay-as-you-go).   
**Project monthly spend limit** |  A Cloud Billing budget cap that stops paid usage when your project reaches the amount that you set. For more information, see Cap costs with a project spend limit.   
**Billing account type** |  Determines how you pay for usage: 

  * A _self-serve (online)_ account pays with prepaid credits. 
  * An _invoiced_ account pays on its monthly invoice. 

To check your account type, see [Find out your Cloud Billing account type and charging cycle](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle#view-your-charging-cycle).   
**Prepaid credits** |  Credits that a self-serve billing account buys in advance. Paid usage is deducted from the credit balance. When you turn on pay-as-you-go usage above quota for the first time, you can continue with a zero balance. If your balance is zero, usage above quota stops until you add credits. If prepaid credits are already set up and your balance is zero, you must add credits before turning it on again. To use the Pay-as-you-go edition, you must buy credits when setting up prepaid credits on your billing account. For more information, see [Manage prepaid credits](https://docs.cloud.google.com/gemini/enterprise/docs/manage-prepaid-credits).   
  
## How charges flow

The following diagram shows how license fees and usage are billed:

![Flowchart of how license fees, pooled quota, and pay-as-you-go usage are billed across editions and billing account types.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/billing-flow.svg)

## Billing models

How you're billed depends on your edition and on whether you turn on pay-as-you-go usage above quota:

Billing model | Editions | Subscription fees | Usage charges  
---|---|---|---  
**Subscription only** | 

  * Gemini Enterprise Standard
  * Gemini Enterprise Plus
  * Gemini Enterprise Frontline Starter and Frontline Worker
  * Gemini Enterprise EDU and EDU Pro
  * Gemini Enterprise Emerging Market editions

| Billed to your Cloud Billing account per license. |  None. Usage is limited to your edition's [pooled quotas](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-pay-as-you-go-usage). When a feature reaches its quota, usage of that feature stops until the quota resets.   
**Subscription with pay-as-you-go usage above quota** | 

  * Gemini Enterprise Standard
  * Gemini Enterprise Plus
  * Gemini Enterprise Frontline Starter and Frontline Worker
  * Gemini Enterprise EDU and EDU Pro
  * Gemini Enterprise Emerging Market editions

| Billed to your Cloud Billing account per license. |  Usage above your pooled quotas is charged at [pay-as-you-go rates](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-pay-as-you-go-usage#pay-as-you-go-usage-above-quota). You turn on pay-as-you-go usage above quota separately for each edition. For more information, see [Configure pay-as-you-go usage above quota](https://docs.cloud.google.com/gemini/enterprise/docs/configure-pay-as-you-go-usage-above-quota).   
**Pay-as-you-go** | 

  * Gemini Enterprise Pay-as-you-go

| None. |  All usage is charged at [pay-as-you-go rates](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-pay-as-you-go-usage#quotas-pay-as-you-go), with no pooled quota limits.   
**Note:** Gemini Enterprise Emerging Market editions are available only to eligible customers. Contact your Google account team to assess the requirements and determine your eligibility.

## Where to manage billing

Task | Location  
---|---  
Manage subscriptions and view your credit balance |  **Gemini Enterprise > Plans & billing** page in the Google Cloud console   
View feature usage, turn on pay-as-you-go usage above quota, and set a spend limit  |  **Gemini Enterprise > Usage & spend > Usage** tab in the Google Cloud console   
View costs |  **Gemini Enterprise > Usage & spend > Spend** tab in the Google Cloud console   
Manage auto-reload, payment methods, and invoices | **Billing** page in the Google Cloud console  
  
## Cap costs with a project spend limit

To prevent unexpected charges when you turn on pay-as-you-go usage above quota, you can configure a monthly spend limit on your total spend in Cloud Billing. When defining a budget for your project, you select **Vertex AI (aiplatform.googleapis.com)** as the service scope. This sets a project-level spend cap that applies across all of the following areas:

  * Gemini Enterprise app
  * Gemini Enterprise Agent Platform
  * AI coding and developer tools (such as Google Antigravity)



When your project reaches this spend limit, paid usage is automatically stopped. Usage resumes at the start of the next month, or earlier if you [lift the spend cap](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps#lift-spend-cap). To configure a monthly spend limit for your project, see [Set a monthly spend limit](https://docs.cloud.google.com/gemini/enterprise/docs/configure-pay-as-you-go-usage-above-quota#set-spend-limit).

If you pay with prepaid credits, the spend limit still applies. Usage stops when your project reaches the spend limit or your credit balance reaches zero, whichever happens first. To limit how much auto-reload can charge, you can also set a [monthly auto-charge limit](https://docs.cloud.google.com/gemini/enterprise/docs/manage-prepaid-credits#monthly-limit).

**Note:** Because stopping usage can take some time to take effect, you might incur charges that exceed your limit.

## Switch billing models

Your prepaid credit balance stays with your Cloud Billing account when you change how you use Gemini Enterprise:

  * **Add a license-based subscription alongside Pay-as-you-go:** For users assigned a seat-based license, your remaining credits pay for usage above quota if you turn on pay-as-you-go usage above quota for that edition. If you keep your Pay-as-you-go subscription active, users assigned to it continue using your credits.
  * **Move from a license-based subscription to Pay-as-you-go:** If you cancel your license-based subscription, it remains active until the end of its current term. When you subscribe to the Pay-as-you-go edition, buy credits if prepaid credits aren't set up on your billing account yet. After you assign users to the subscription, your credits pay for their Pay-as-you-go usage.
  * **Turn off pay-as-you-go usage above quota:** Your credits stay in your balance until they expire, and you can use them if you turn it on again.



If you move to an invoiced billing account, your credits stay on the self-serve billing account where you bought them.

## End-user experience when limits are reached

When your project reaches a usage or spending limit, Gemini Enterprise restricts further usage. Feature access resumes automatically when the quota resets or at the start of the next billing cycle.

Gemini Enterprise app displays the **Usage limit reached** error message when you chat with the assistant or use Gemini Enterprise features in either of the following scenarios: 

  * Your project reached its monthly spend cap.
  * Your project exceeds its pooled quota limit for a specific feature and your Gemini Enterprise administrator hasn't enabled overages. 



This error affects only the feature that reached its limit. You can continue using other features that have remaining quota. 

If you pay with prepaid credits and your credit balance is empty or inactive, users see a message that your organization's prepaid balance is used up or inactive. To restore access, a billing account administrator must [buy credits](https://docs.cloud.google.com/gemini/enterprise/docs/manage-prepaid-credits#buy-credits).

## Budget and billing notifications

The Gemini Enterprise app doesn't send automated email alerts or push notifications when your project reaches its pooled feature quotas or starts incurring pay-as-you-go charges. When your project reaches a pooled quota and you haven't turned on pay-as-you-go usage above quota, end users see the **Usage limit reached** error message in the app.

If you pay with prepaid credits, Cloud Billing sends email notifications and shows alerts in the Google Cloud console when any of the following happens:

  * Your credit balance is low or empty.
  * A payment is declined.
  * Auto-reload pauses because it reached your monthly auto-charge limit.



When you configure a monthly spend limit in Cloud Billing, you can set alert threshold rules to monitor your costs. Cloud Billing automatically sends email notifications when your spend reaches specified percentages of your budget, such as 50%, 80%, and 100% of the budget amount.

The following principals receive budget alert notifications:

  * **Default recipients:** Cloud Billing sends email alerts to users who have the **Billing Account Administrator** or **Billing Account User** IAM roles on the target billing account.
  * **Custom recipients:** You can configure custom email recipients, such as specific project administrators, team distribution lists, or Pub/Sub channels, in your budget alert rules.



## What's next

  * Learn how to [manage prepaid credits](https://docs.cloud.google.com/gemini/enterprise/docs/manage-prepaid-credits).
  * Learn how to [configure pay-as-you-go usage above quota](https://docs.cloud.google.com/gemini/enterprise/docs/configure-pay-as-you-go-usage-above-quota).
  * Learn how to [view costs](https://docs.cloud.google.com/gemini/enterprise/docs/view-costs).
  * Learn how to [create budgets and budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets).
  * Learn how to [manage budget alert recipients](https://docs.cloud.google.com/billing/docs/how-to/budgets-notification-recipients).
  * Learn how to [troubleshoot billing and payments](https://docs.cloud.google.com/gemini/enterprise/docs/billing-questions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 

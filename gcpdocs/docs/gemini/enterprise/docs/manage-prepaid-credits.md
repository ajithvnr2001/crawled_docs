---
url: https://docs.cloud.google.com/gemini/enterprise/docs/manage-prepaid-credits/
title: Manage prepaid credits \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:07.926060+00:00
---

# Manage prepaid credits  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/manage-prepaid-credits/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Manage prepaid credits Stay organized with collections  Save and categorize content based on your preferences. 

To help keep your Gemini Enterprise features running without interruption, you can buy prepaid credits to cover usage that goes beyond your included subscription quota.

**Note:** Prepaid credits for self-serve (online) billing accounts are rolling out gradually. If you don't see the **Credit balance** tab on **Plans & billing** or the **AI developer tools** tab on **Settings** yet, your account hasn't been included.

## Key concepts

This section introduces key billing concepts for prepaid credits in Gemini Enterprise. Term | Definition  
---|---  
**Pay-as-you-go usage above quota** |  A setting that lets usage continue after the pooled quota runs out. This usage is charged at pay-as-you-go rates. For more information, see [Configure pay-as-you-go usage above quota](https://docs.cloud.google.com/gemini/enterprise/docs/configure-pay-as-you-go-usage-above-quota).   
**Pay-as-you-go edition** |  An edition with no license fee and no pooled quota. All usage is charged at [pay-as-you-go rates](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-pay-as-you-go-usage#quotas-pay-as-you-go).   
**Billing account type** |  Determines how you pay for usage: 

  * A _self-serve (online)_ account pays with prepaid credits. 
  * An _invoiced_ account pays on its monthly invoice. 

To check your account type, see [Find out your Cloud Billing account type and charging cycle](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle#view-your-charging-cycle).   
**Prepaid credits** |  Credits that a self-serve billing account buys in advance. Paid usage is deducted from the credit balance. When you turn on pay-as-you-go usage above quota for the first time, you can continue with a zero balance. If your balance is zero, usage above quota stops until you add credits. If prepaid credits are already set up and your balance is zero, you must add credits before turning it on again. To use the Pay-as-you-go edition, you must buy credits when setting up prepaid credits on your billing account.   
  
## About prepaid credits

Prepaid credits pay for the following usage:

  * All usage in the [Gemini Enterprise Pay-as-you-go edition](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-pay-as-you-go-usage#quotas-pay-as-you-go).
  * [Usage above quota](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-pay-as-you-go-usage#pay-as-you-go-usage-above-quota) in license-based editions, such as Gemini Enterprise Standard and Plus, when pay-as-you-go usage above quota is turned on.



Credits apply to usage in the Gemini Enterprise app, Gemini Enterprise Agent Platform, and AI developer tools such as Google Antigravity. Subscription fees for license-based editions are billed to your Cloud Billing account, not paid with credits.

Your credit balance belongs to your Cloud Billing account. All projects linked to the same billing account draw from the same balance.

**Note:** Credits for Gemini Enterprise are separate from prepaid credits for the Gemini API in Google AI Studio. You can't use one to pay for the other. If your billing account has both, you see two separate balances.

### Expiration and refunds

Credits expire one year after purchase. Credits are non-refundable, except as allowed by the [Supplemental Paid Credit Terms](https://cloud.google.com/terms/supplemental-paid-credit). If you close your Cloud Billing account, any remaining credit balance is lost and can't be recovered.

### Purchase and balance limits

The following limits apply to credit purchases. Amounts in other currencies are converted to the local equivalent.

Limit | Amount  
---|---  
Minimum purchase |  USD 5. Some accounts require a higher minimum purchase, which is shown when you buy credits.   
Maximum credit balance |  USD 10,000. You can't buy credits that would take your balance above this amount.   
Minimum auto-reload threshold | USD 1  
Maximum auto-reload amount and threshold | USD 5,000 each  
  
The following regional limits also apply:

  * **Australia:** The maximum credit balance is AUD 5,000 (or USD 3,000 if billed in USD). The maximum auto-reload amount and threshold are AUD 2,500 each.
  * **India:** The maximum auto-reload amount and threshold are INR 15,000 each per transaction. One-time purchases aren't subject to this INR 15,000 limit (only the overall maximum credit balance limit applies).



### Supported payment methods

Available payment methods depend on your country and currency. You can buy credits with the following payment methods:

  * Credit and debit cards, for one-time purchases and auto-reload.
  * UPI (India), for one-time purchases and auto-reload.
  * RuPay (India), for one-time purchases only.
  * PIX (Brazil), for one-time purchases only.



PayPal and SEPA bank accounts aren't supported. For more information about available payment methods by location, see [Add, remove, or update a payment method](https://docs.cloud.google.com/billing/docs/how-to/payment-methods#supported_payment_methods).

## Before you begin

  * Make sure that your project is linked to an open, upgraded paid self-serve Cloud Billing account in good standing. Direct accounts with a Payments profile and an active automatic payment method are supported; free-trial accounts and reseller-managed subaccounts aren't supported.

  * Prepaid credits are set up on your billing account the first time you [subscribe to the Gemini Enterprise Pay-as-you-go edition](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#about-subscriptions) or [turn on pay-as-you-go usage above quota](https://docs.cloud.google.com/gemini/enterprise/docs/configure-pay-as-you-go-usage-above-quota#turn-on-pay-as-you-go-usage-above-quota) for the first time. Before setup, the **Credit balance** tab indicates that your billing account isn't set up for prepay.

  * To view and manage prepaid credits on the **Plans & billing** page, ask your administrator to grant you the following Identity and Access Management (IAM) roles:

    * **Project role:** [Gemini Enterprise Admin](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) (`roles/discoveryengine.agentspaceAdmin`) on the project, to open **Plans & billing**.
    * **Billing account role:** [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`) on the billing account to set up prepaid credits, buy credits, set up auto-reload, and manage payment methods, or [Billing Account Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.viewer) (`roles/billing.viewer`) to view the credit balance only.

The Billing Account User role (`roles/billing.user`) doesn't include permission to view or buy credits.




## Buy credits

After prepaid credits are set up on your billing account, you can buy credits at any time. You're also asked to buy credits in the following cases:

  * When you [subscribe to the Gemini Enterprise Pay-as-you-go edition](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#about-subscriptions) with a self-serve billing account. Invoiced accounts don't use prepaid credits. If prepaid credits aren't set up on the self-serve billing account yet, buying credits is required to complete the subscription—if you cancel the purchase, the subscription isn't created and you aren't charged. If prepaid credits are already set up, you can add credits or close the window to complete the subscription.
  * When you [turn on pay-as-you-go usage above quota](https://docs.cloud.google.com/gemini/enterprise/docs/configure-pay-as-you-go-usage-above-quota#turn-on-pay-as-you-go-usage-above-quota) for the first time with a self-serve billing account.



To buy credits, follow these steps:

  1. In the Google Cloud console, go to the **Gemini Enterprise > Plans & billing** page.

[Go to Plans & billing](https://console.cloud.google.com/gemini-enterprise/manage-subscription)

  2. On the **Credit balance** tab, click **Make a payment** to open the **Buy credits** window.

  3. Select an amount and a payment method, and then follow the prompts to complete the purchase.




Credits are added to your balance after the payment is confirmed. For more information, see Payment processing times.

## Set up or manage auto-reload

Auto-reload buys credits automatically when your credit balance reaches a threshold that you set. You can set up or manage auto-reload from the **Gemini Enterprise > Plans & billing** page or from the **Billing** page.

### Set up or manage auto-reload from Gemini Enterprise

  1. In the Google Cloud console, go to the **Gemini Enterprise > Plans & billing** page.

[Go to Plans & billing](https://console.cloud.google.com/gemini-enterprise/manage-subscription)

  2. Select the **Credit balance** tab.

  3. On the **Credit balance** card, if the status is **Auto-reload: Off** , click **Set up auto-reload**. If the status is **Auto-reload: On** , click **Manage auto-reload**.

  4. Configure the following auto-reload options:

     * **Reload amount:** The amount to buy each time auto-reload runs.
     * **When credit balance falls below:** The balance that triggers auto-reload.
     * **Monthly limit** (optional): The maximum total amount that auto-reload can charge in a billing month. For more information, see Set a monthly auto-charge limit.
  5. Click **Save**.




### Set up or manage auto-reload from Cloud Billing

  1. In the Google Cloud console, go to the **Billing** page.

[Go to Billing](https://console.cloud.google.com/billing)

  2. Select your billing account.

  3. Click **How you pay**. If your billing account has multiple payment tabs, then select **Prepay - Gemini Enterprise**.

  4. Click **Manage auto-reload**.

  5. Configure the reload options, and then click **Save**.




### Set a monthly auto-charge limit

The monthly auto-charge limit caps how much auto-reload can charge in one billing month. The limit must be at least as large as the reload amount. If you leave it empty, there's no limit.

When auto-reload reaches the limit, it pauses until the start of the next billing month. To turn it back on in the current month, increase the limit. Credits that you buy manually don't count toward the limit.

## View your credit balance and transactions

To view your credit balance, payment settings, and transaction history, follow these steps:

  1. In the Google Cloud console, go to the **Gemini Enterprise > Plans & billing** page.

[Go to Plans & billing](https://console.cloud.google.com/gemini-enterprise/manage-subscription)

  2. Select the **Credit balance** tab.




## Payment processing times

  * **Credit usage:** Usage costs can take some time to be deducted from your balance. Usage can produce a negative balance after exceeding the prepaid credit, and this negative balance will be charged to your account.
  * **Payment confirmation:** Credits are added to your balance only after the payment is confirmed. Some payment methods take several days to clear.



For more information, see [Transaction latencies](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle).

## Fix a declined payment

If a purchase or an auto-reload payment is declined, credits aren't added to your balance. If your balance reaches zero, usage that's paid with credits stops.

To fix a declined payment, update your payment method:

  1. In the Google Cloud console, go to the **Billing** page.

[Go to Billing](https://console.cloud.google.com/billing)

  2. Select your billing account.

  3. Click **How you pay**. If your billing account has multiple payment tabs, then select **Prepay - Gemini Enterprise** , and then update your payment method.

  4. To restore your balance, buy credits.




## What's next

  * Learn [how billing works in Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/manage-costs-overview).
  * Learn how to [configure pay-as-you-go usage above quota](https://docs.cloud.google.com/gemini/enterprise/docs/configure-pay-as-you-go-usage-above-quota).
  * Learn how to [troubleshoot billing and payments](https://docs.cloud.google.com/gemini/enterprise/docs/billing-questions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 

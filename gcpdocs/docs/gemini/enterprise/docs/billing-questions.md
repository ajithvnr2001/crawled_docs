---
url: https://docs.cloud.google.com/gemini/enterprise/docs/billing-questions/
title: Troubleshoot billing and payments \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:27.274026+00:00
---

# Troubleshoot billing and payments  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/billing-questions/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Resources ](https://docs.cloud.google.com/gemini/enterprise/docs/resources)



Send feedback 

#  Troubleshoot billing and payments Stay organized with collections  Save and categorize content based on your preferences. 

Billing and payments can be complicated. This page helps you identify common issues and find the quickest way to get your account back in good standing. To learn how billing works, see [How billing works in Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/manage-costs-overview).

## Usage is blocked

This section describes common issues that block feature usage or prevent you from turning on pay-as-you-go usage above quota.

Issue | Cause | Resolution  
---|---|---  
Users see the **Usage limit reached** message |  Your project reached its monthly spend limit, or a feature reached its pooled quota and pay-as-you-go usage above quota isn't turned on for the user's edition.  |  [Raise the spend limit](https://docs.cloud.google.com/gemini/enterprise/docs/configure-pay-as-you-go-usage-above-quota#set-spend-limit) or [turn on pay-as-you-go usage above quota](https://docs.cloud.google.com/gemini/enterprise/docs/configure-pay-as-you-go-usage-above-quota#turn-on-pay-as-you-go-usage-above-quota). If you reached the spend limit, usage resumes at the start of the next month, or earlier if you [lift the spend cap](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps#lift-spend-cap). Otherwise, usage resumes when the quota resets.   
Users see that the prepaid balance is used up or inactive |  Your project pays with prepaid credits, and the credit balance is empty or can't be charged.  |  A billing account administrator must [buy credits](https://docs.cloud.google.com/gemini/enterprise/docs/manage-prepaid-credits#buy-credits) or [set up auto-reload](https://docs.cloud.google.com/gemini/enterprise/docs/manage-prepaid-credits#auto-reload).   
You see the message **You do not have billing admin access** when turning on pay-as-you-go usage above quota  |  Turning on **Pay-as-you-go usage above quota** for the first time sets up the prepaid credit balance, which requires the Billing Account Administrator role.  |  Ask a user with the [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`) role to turn on pay-as-you-go usage above quota for the first time, or ask for that role.   
You see the message **This billing account cannot be used** when subscribing to Pay-as-you-go  |  Pay-as-you-go requires an open [self-serve (online) or invoiced Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) in good standing. Self-serve accounts pay with prepaid credits, while invoiced accounts are billed on their monthly invoice. You see this message if the selected billing account has one of the following issues:

  * **The account isn't open:** It's closed or suspended.
  * **The account isn't in good standing:** It has overdue payments or a billing hold.
  * **The account type isn't supported:** For example, it's an unupgraded free-trial account, a reseller-managed subaccount, has no payments profile, or is a self-serve account without an automatic payment method, such as a credit or debit card.

|  Check the specific reason shown under the error message, and then take one of the following actions: 

  * Reopen the billing account, pay any overdue balance, upgrade your free-trial account, or add an automatic payment method in Cloud Billing.
  * [Link your project to a different billing account](https://docs.cloud.google.com/billing/docs/how-to/modify-project) that's an open self-serve or invoiced account in good standing.

  
  
## Credits and payments

This section describes common issues with purchasing prepaid credits, configuring auto-reload, and processing payments.

Issue | Cause | Resolution  
---|---|---  
Credits don't appear after you buy them |  Credits are added only after the payment is confirmed. Some payment methods take several days to clear.  |  Wait for the payment to be confirmed. For more information, see [Payment processing times](https://docs.cloud.google.com/gemini/enterprise/docs/manage-prepaid-credits#processing-times).   
Auto-reload didn't add credits |  Auto-reload reached your monthly auto-charge limit, or the payment was declined.  |  Increase your [monthly auto-charge limit](https://docs.cloud.google.com/gemini/enterprise/docs/manage-prepaid-credits#monthly-limit), or [update your payment method](https://docs.cloud.google.com/gemini/enterprise/docs/manage-prepaid-credits#fix-declined-payment).   
A payment was declined |  The payment method expired, has insufficient funds, or isn't supported.  |  [Update your payment method](https://docs.cloud.google.com/gemini/enterprise/docs/manage-prepaid-credits#fix-declined-payment), and then buy credits again. For more information, see [Supported payment methods](https://docs.cloud.google.com/gemini/enterprise/docs/manage-prepaid-credits#payment-methods).   
The amount you entered isn't accepted |  The amount is outside the purchase or balance limits.  |  Enter an amount within the [purchase and balance limits](https://docs.cloud.google.com/gemini/enterprise/docs/manage-prepaid-credits#limits).   
  
## Charges and invoices

This section describes common questions and issues related to pay-as-you-go charges, prepaid credit balances, and invoice taxes.

Issue | Cause | Resolution  
---|---|---  
Charges after you turn off pay-as-you-go usage above quota or reach a limit  |  Billing data can take some time to process. Usage can produce a negative balance after exceeding the prepaid credit, and this negative balance will be charged to your account.  |  No action is needed. For more information, see [Payment processing times](https://docs.cloud.google.com/gemini/enterprise/docs/manage-prepaid-credits#processing-times).   
More than one prepaid balance on your billing account |  Prepaid credits for Gemini Enterprise and for the Gemini API in Google AI Studio are kept in separate balances.  |  No action is needed. Credits for Gemini Enterprise pay only for Gemini Enterprise usage. For more information, see [About prepaid credits](https://docs.cloud.google.com/gemini/enterprise/docs/manage-prepaid-credits#about-prepaid-credits).   
Tax on your invoice |  Prices don't include taxes. Applicable taxes are based on the address of your Cloud Billing account. With prepaid credits, tax might be charged when you buy credits, depending on your country.  |  For more information, see [Taxes](https://docs.cloud.google.com/gemini/enterprise/docs/view-costs#taxes).   
  
## Get billing support

If your issue isn't listed on this page, then use the following resources:

  * To view billing reports, see [View your billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports).
  * To learn more about billing, read the [Cloud Billing documentation](https://docs.cloud.google.com/billing/docs).
  * To resolve billing concerns, use the [Google Cloud Billing Troubleshooter](https://support.google.com/cloud/troubleshooter/7279311).
  * To request help with billing questions, contact [Cloud Billing Support](https://docs.cloud.google.com/support/billing).
  * To change or disable billing on a project, go to the **Billing** page in the Google Cloud console. For more information, see [Modify a project's billing settings](https://docs.cloud.google.com/billing/docs/how-to/modify-project).

**Caution:** When you disable billing for a project, you also disable all product resources in that project.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 

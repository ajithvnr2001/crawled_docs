---
url: https://docs.cloud.google.com/billing/docs/how-to/resolve-invalid-billing-account/
title: Resolve an invalid Cloud Billing account \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:19:40.847528+00:00
---

# Resolve an invalid Cloud Billing account  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/resolve-invalid-billing-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Resolve an invalid Cloud Billing account Stay organized with collections  Save and categorize content based on your preferences. 

Every Cloud Billing account requires an active linked Google payments profile to process charges and fund subscriptions. If the linked payments profile is missing, closed, or permanently deleted, the Cloud Billing account becomes invalid. You might encounter this issue during purchase flows in the Google Cloud console, such as Cloud Customer Care purchase setup, or when reviewing your account status on the **Account management** or **How you pay** page.

## Identify why the account is invalid

Use the following table to identify the cause of the invalid account and choose a resolution:

Condition | Resolution  
---|---  
Your selected Cloud Billing account is invalid, but you have another active account | Option 1: Select a different active Cloud Billing account  
The payments profile was deleted | Option 2: Create a new Cloud Billing account and move projects  
The payments profile was closed | Option 3: Verify or recover a payments profile  
  
## Permissions required

The permissions required to resolve an invalid Cloud Billing account depend on which resolution option you choose and whether your resources are managed under an [Organization node](https://docs.cloud.google.com/billing/docs/concepts#organization). For specific role and permission requirements, see the permissions section in the linked documentation for your chosen option.

## Resolve the invalid Cloud Billing account

To resolve the invalid account issue, choose one of the following options:

### Option 1: Select a different active Cloud Billing account

If your organization has another active self-serve or invoiced Cloud Billing account, select that account in the Google Cloud console to complete your purchase or fund your projects:

  * **During a purchase flow** : Select a different active Cloud Billing account from the billing account selector, such as during [Standard Support purchase setup](https://docs.cloud.google.com/support/docs/purchasing-setting-up-standard#purchase).
  * **For existing projects** : Move your projects to the active Cloud Billing account by following [Change the Cloud Billing account for a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#change_the_billing_account_for_a_project).



### Option 2: Create a new Cloud Billing account and move projects

  1. Create a new Cloud Billing account and link it to an active payments profile using [Create a new self-serve Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account#create-new-billing-account).
  2. Move affected projects to the new Cloud Billing account using [Change the Cloud Billing account for a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#change_the_billing_account_for_a_project).
  3. If you were completing a purchase in the Google Cloud console, such as Customer Care, return to the purchase flow and select the new Cloud Billing account.



### Option 3: Verify or recover a Google payments profile

To verify whether your profile was suspended or closed, visit the [Google payments center](https://payments.google.com).

If a payments profile was closed within 30 days, you can [contact Google payments center support](https://support.google.com/googlepay/gethelp) to reopen it. Review the closing and reopening instructions in [Close a payments profile](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account#close-payments-profile).

Self-serve Cloud Billing accounts that are associated with a permanently deleted payments profile are permanently invalid. You can't edit an existing self-serve Cloud Billing account to attach a different payments profile to it. Use Option 2 to create a new Cloud Billing account.

For invoiced accounts, contact your account team or Cloud Billing Support to request a payments profile update.

## Contact Cloud Billing Support

Resolving billing issues doesn't require a paid support subscription.

You can contact [Cloud Billing Support](https://docs.cloud.google.com/support/docs/get-billing-support) at no additional charge.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

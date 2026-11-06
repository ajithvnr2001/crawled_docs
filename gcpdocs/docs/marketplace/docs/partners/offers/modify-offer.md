---
url: https://docs.cloud.google.com/marketplace/docs/partners/offers/modify-offer/
title: Modify a published offer \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T10:22:05.750122+00:00
---

# Modify a published offer  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/offers/modify-offer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Go to market ](https://docs.cloud.google.com/marketplace/docs/partners/gtm)



Send feedback 

#  Modify a published offer Stay organized with collections  Save and categorize content based on your preferences. 

When you use Private Offers to create offers with custom pricing, you can modify published private offers from installment to installment. For more information, see the [Private Offers documentation](https://docs.cloud.google.com/marketplace/docs/partners/offers).

**Note:** If the offer expires in 24 or less hours, you can't modify or replace the offer.

## Modify an offer

To modify or amend an **Active** private offer, complete the following steps:

  1. On the **Private Offers** page, for the offer that you want to amend, click **Manage your offers** more_vert, and then click **Amend**.

  2. In the **Amend active order** dialog, click **Amend**.




Producer Portal copies the order into a new draft replacement offer. The existing order stays active until your customer accepts the amended offer. You can also start an amendment by creating a new offer with the same customer Cloud Billing account and product, which retrieves the existing offer's details.

**Note:** To change a published offer that your customer hasn't accepted yet, use **Edit** instead. For details, see [Publish your offer](https://docs.cloud.google.com/marketplace/docs/partners/offers/review-offer#publish-offer).

When you amend an offer, you can change the following:

  * The end date of the contract.
  * The number of remaining installments.
  * The details of any installments which haven't started yet.



If your current pricing model is **committed use discount (CUD)** , you can add partner-sponsored one-time credits to specific installments. To add one-time credits, use the **Free credit** toggle and then add the amounts of the one-time credits that you want to sponsor to the installments that you want them to apply to. One-time credits expire or roll over according to the rules that you specified for the installments that they apply to when you created the original offer.

You can't change the following:

  * Details of installments which have already been paid for.
  * [Billing frequency](https://docs.cloud.google.com/marketplace/docs/partners/offers/select-payment-schedule), except to **Custom**.



When you amend a contract, the following rules apply:

  * The _installment value_ of each of the contract's installments must be equal to or greater than 50% of the value of the previous installment's installment value. Cloud Marketplace calculates installment value as the amount paid for an installment, divided by the number of days in the installment.
  * The amended contract's _total contract value_ must be equal to or greater than 50% of the current contract's total contract value.



The replacement offer starts immediately when it's purchased and approved.

### Modify pricing details

For replacement offers, you can modify certain pricing details based on the pricing model your current offer uses:

  * If your current pricing model is **CUD** , you can modify the commitment and discount percentage. If the offer has a monthly, quarterly, or annual billing frequency, the new commitment must be equal to or higher than the current offer's commitment. You can't change the type of CUD model (_Commitment discount with additional usage at list price_ or _Commitment with all usage discounted_) or the plan.

  * If your current pricing model is **Usage only** , you can modify the discount percentage, or replace the model with a **CUD** model.

  * If your current pricing model is **Flat fee** (SaaS), you can modify the payment amount and features list. You can't switch to a usage-based pricing model.




## Extend the offer deadline

To give your customer extra time to accept a published offer, or to reactivate an unaccepted **Offer expired** offer, extend the acceptance deadline. The URL stays the same, so you don't need to send a new URL to your customer. If the offer has a scheduled start date that has already passed, you can't extend the deadline. Create a new offer instead.

  1. On the **Private Offers** page, for the offer that you want to extend, click **Manage your offers** more_vert, and then click **Extend acceptance deadline**.

  2. In the **Extend acceptance deadline** dialog, select the new date. The deadline must be within three months of when you extend the offer, and before any scheduled start date or fixed future installment date.

  3. Click **Save**.




The **Private Offers** page shows the new deadline in the **Acceptance due date** column.

## What's next

The following articles describe additional ways that you can manage your customers' private offers:

  * [View the current status](https://docs.cloud.google.com/marketplace/docs/partners/offers/view-offer-status) of your offers.

  * [Approve an accepted offer](https://docs.cloud.google.com/marketplace/docs/partners/offers/approve-offer).

  * [Download an offer](https://docs.cloud.google.com/marketplace/docs/partners/offers/download-offer) as a PDF.

  * [Cancel a published offer](https://docs.cloud.google.com/marketplace/docs/partners/offers/cancel-offer).

  * [Archive an inactive offer](https://docs.cloud.google.com/marketplace/docs/partners/offers/archive-offer).

  * [Cancel an active order](https://docs.cloud.google.com/marketplace/docs/partners/offers/cancel-active-order).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-05 UTC."],[],[]] 

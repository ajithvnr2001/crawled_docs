---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult/
title: ClientExecutionResult \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-05T00:17:46.458134+00:00
---

# ClientExecutionResult  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  ClientExecutionResult Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * FinalizeOrderResponse
    * JSON representation
  * DonationInfo
    * JSON representation
  * DonationOffer
    * JSON representation
  * DonationOption
    * JSON representation
  * DonationType
  * SuppressionReason
  * AppliedDonation
    * JSON representation
  * DonationRequestStatus
  * SubmitOrderResponse
    * JSON representation
  * LoyaltyResponse
    * JSON representation
  * LoyaltyMetadata
    * JSON representation
  * CustomerInformation
    * JSON representation
  * AccrualForecast
    * JSON representation
  * OrderPricesResponse
    * JSON representation
  * ValidateDeliveryAddressResponse
    * JSON representation
  * ValidDeliveryStore
    * JSON representation
  * OrderStatusResponse
    * JSON representation
  * ClientExecutionStatus
    * JSON representation
  * RejectionReason



The result of a client execution request.

JSON representation  
---  
      
    
    {
      "executionId": string,
      "clientExecutionStatus": {
        object ([ClientExecutionStatus](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#ClientExecutionStatus))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "finalizeOrderResponse": {
        object ([FinalizeOrderResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#FinalizeOrderResponse))
      },
      "submitOrderResponse": {
        object ([SubmitOrderResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#SubmitOrderResponse))
      },
      "loyaltyResponse": {
        object ([LoyaltyResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#LoyaltyResponse))
      },
      "orderPricesResponse": {
        object ([OrderPricesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#OrderPricesResponse))
      },
      "validateDeliveryAddressResponse": {
        object ([ValidateDeliveryAddressResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#ValidateDeliveryAddressResponse))
      },
      "orderStatusResponse": {
        object ([OrderStatusResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#OrderStatusResponse))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`executionId` |  `string` Required. The ID of the execution request this is a result for.  
`clientExecutionStatus` |  `object (`[ClientExecutionStatus](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#ClientExecutionStatus)`)` Optional. Client execution status.  
The specific result of the execution. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`finalizeOrderResponse` |  `object (`[FinalizeOrderResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#FinalizeOrderResponse)`)` The result of finalizing the order.  
`submitOrderResponse` |  `object (`[SubmitOrderResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#SubmitOrderResponse)`)` The result of submitting the order.  
`loyaltyResponse` |  `object (`[LoyaltyResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#LoyaltyResponse)`)` Optional. Unified loyalty response.  
`orderPricesResponse` |  `object (`[OrderPricesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#OrderPricesResponse)`)` The result of getting the order prices.  
`validateDeliveryAddressResponse` |  `object (`[ValidateDeliveryAddressResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#ValidateDeliveryAddressResponse)`)` The result of validating the delivery address.  
`orderStatusResponse` |  `object (`[OrderStatusResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#OrderStatusResponse)`)` The result of getting the order status.  
End of mutually exclusive fields.  
  
## FinalizeOrderResponse

The result of finalizing the order.

JSON representation  
---  
      
    
    {
      "paymentFlowEnabled": boolean,
      "paymentInfo": {
        object ([PaymentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#PaymentInfo))
      },
      "totalAmountDue": {
        object ([Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money))
      },
      "orderPriceInfo": {
        object ([OrderPriceInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#OrderPriceInfo))
      },
      "donationInfo": {
        object ([DonationInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#DonationInfo))
      }
    }  
  
Fields  
---  
`paymentFlowEnabled` |  `boolean` Optional. Whether to enable the payment handling flow in the agent.  
`paymentInfo` |  `object (`[PaymentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#PaymentInfo)`)` Optional. The payment information of the customer. No-op if paymentFlowEnabled is false. Only `creditCardLastFourDigits` and `paymentMethod` should be populated here; raw cardholder or sensitive authentication data must never be included.  
`totalAmountDue` |  `object (`[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money)`)` Optional. The total amount due for the order.  
`orderPriceInfo` |  `object (`[OrderPriceInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#OrderPriceInfo)`)` Optional. The detailed price information of the order.  
`donationInfo` |  `object (`[DonationInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#DonationInfo)`)` Optional. Charity donation information for the order, including any offer to present, currently applied donations, and the outcome of a donation change.  
  
## DonationInfo

Charity donation offer, applied donations, and request status for the order.

JSON representation  
---  
      
    
    {
      "offer": {
        object ([DonationOffer](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#DonationOffer))
      },
      "appliedDonations": [
        {
          object ([AppliedDonation](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#AppliedDonation))
        }
      ],
      "requestStatus": enum ([DonationRequestStatus](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#DonationRequestStatus))
    }  
  
Fields  
---  
`offer` |  `object (`[DonationOffer](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#DonationOffer)`)` Optional. The donation the agent may offer, evaluated by the client from store settings and session rules. If omitted, the agent does not offer a donation.  
`appliedDonations[]` |  `object (`[AppliedDonation](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#AppliedDonation)`)` Optional. The donations currently applied to the client order. Empty if no donations are applied.  
`requestStatus` |  `enum (`[DonationRequestStatus](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#DonationRequestStatus)`)` Optional. The outcome of the donation change derived by the client from the order state since the previous finalization, such as when a donation item is added or removed. Unspecified if no donation changed.  
  
## DonationOffer

Donation offer directives evaluated by the client from store settings and session rules.

JSON representation  
---  
      
    
    {
      "eligible": boolean,
      "options": [
        {
          object ([DonationOption](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#DonationOption))
        }
      ],
      "suppressionReason": enum ([SuppressionReason](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#SuppressionReason))
    }  
  
Fields  
---  
`eligible` |  `boolean` Optional. Whether the agent should proactively offer a donation.  
`options[]` |  `object (`[DonationOption](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#DonationOption)`)` Optional. The donation options the agent may offer, such as a round-up or fixed-amount tiers. The first option is the default offer.  
`suppressionReason` |  `enum (`[SuppressionReason](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#SuppressionReason)`)` Optional. The reason a donation should not be offered. Set only when `eligible` is `false`.  
  
## DonationOption

One donation option that the agent may offer.

JSON representation  
---  
      
    
    {
      "type": enum ([DonationType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#DonationType)),
      "amount": {
        object ([Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money))
      },
      "projectedTotal": {
        object ([Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money))
      },
      "charityDisplayName": string
    }  
  
Fields  
---  
`type` |  `enum (`[DonationType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#DonationType)`)` Optional. The kind of donation.  
`amount` |  `object (`[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money)`)` Optional. The donation amount, such as $0.25 for a round-up or $5.00 for a fixed tier.  
`projectedTotal` |  `object (`[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money)`)` Optional. The total amount due if this option is applied.  
`charityDisplayName` |  `string` Optional. The display name of the charity presented to the customer.  
  
## DonationType

The kind of donation.

Enums  
---  
`DONATION_TYPE_UNSPECIFIED` | Indicates that the donation type is not specified.  
`DONATION_TYPE_ROUND_UP` | Rounds the total amount due up to the next whole currency unit.  
`DONATION_TYPE_FIXED_AMOUNT` | A fixed donation tier offered by the brand, such as $5.00.  
`DONATION_TYPE_CUSTOM_AMOUNT` | An arbitrary donation amount chosen by the customer.  
  
## SuppressionReason

Reasons a donation should not be offered.

Enums  
---  
`SUPPRESSION_REASON_UNSPECIFIED` | Indicates that the suppression reason is not specified.  
`SUPPRESSION_REASON_STORE_DISABLED` | Indicates that donations are disabled for the store.  
`SUPPRESSION_REASON_ZERO_TOTAL` | Indicates that the total amount due is zero.  
`SUPPRESSION_REASON_WHOLE_AMOUNT` | Indicates that the total amount due is already a whole currency amount, so there is nothing to round up.  
`SUPPRESSION_REASON_BELOW_MIN_THRESHOLD` | Indicates that the round-up amount is below the minimum threshold for an offer.  
`SUPPRESSION_REASON_ALREADY_APPLIED` | Indicates that a donation is already applied to the order.  
  
## AppliedDonation

A donation currently applied to the client order.

JSON representation  
---  
      
    
    {
      "type": enum ([DonationType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#DonationType)),
      "amount": {
        object ([Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money))
      }
    }  
  
Fields  
---  
`type` |  `enum (`[DonationType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#DonationType)`)` Optional. The kind of donation.  
`amount` |  `object (`[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money)`)` Optional. The donation amount.  
  
## DonationRequestStatus

The outcome of a donation change derived by the client from the order state.

Enums  
---  
`DONATION_REQUEST_STATUS_UNSPECIFIED` | Indicates that no donation changed or the status is not specified.  
`DONATION_REQUEST_STATUS_APPLIED` | Indicates that the donation is applied to the order.  
`DONATION_REQUEST_STATUS_REMOVED` | Indicates that the donation is removed from the order.  
`DONATION_REQUEST_STATUS_NOT_ELIGIBLE` | Indicates that the donation is not applied because the order is not eligible, for example when the total amount due is already a whole currency amount.  
`DONATION_REQUEST_STATUS_FAILED` | Fails to apply or remove the donation.  
  
## SubmitOrderResponse

The result of submitting the order.

JSON representation  
---  
      
    
    {
      "success": boolean,
      "estimatedReadyDuration": string,
      "externalOrderId": string
    }  
  
Fields  
---  
`success` |  `boolean` Required. Whether the order was successfully submitted.  
`estimatedReadyDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The estimated duration until the order is ready.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`externalOrderId` |  `string` Optional. The external identifier for this order. Usually from the client's point of sale system for analysis purposes.  
  
## LoyaltyResponse

Response for loyalty operations.

JSON representation  
---  
      
    
    {
      "category": enum ([LoyaltyActionCategory](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/LoyaltyActionCategory)),
      "loyaltyMetadata": {
        object ([LoyaltyMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#LoyaltyMetadata))
      },
      "customIntegrationAttributes": {
        object
      }
    }  
  
Fields  
---  
`category` |  `enum (`[LoyaltyActionCategory](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/LoyaltyActionCategory)`)` Optional. Type of loyalty response.  
`loyaltyMetadata` |  `object (`[LoyaltyMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#LoyaltyMetadata)`)` Optional. Loyalty metadata.  
`customIntegrationAttributes` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Contains partner-specific loyalty metadata that does not map to typed fields in LoyaltyMetadata. Must not contain personally identifiable information, authentication or payment tokens, or secret redemption codes.  
  
## LoyaltyMetadata

Metadata for the loyalty session.

JSON representation  
---  
      
    
    {
      "customer": {
        object ([CustomerInformation](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#CustomerInformation))
      },
      "accrual": {
        object ([AccrualForecast](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#AccrualForecast))
      },
      "availableRewards": [
        {
          object ([LoyaltyReward](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.sessionRecords#LoyaltyReward))
        }
      ],
      "appliedCodes": [
        string
      ],
      "appliedRewardIds": [
        string
      ]
    }  
  
Fields  
---  
`customer` |  `object (`[CustomerInformation](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#CustomerInformation)`)` Optional. Customer information associated with the session.  
`accrual` |  `object (`[AccrualForecast](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#AccrualForecast)`)` Optional. Forecast of points accrual.  
`availableRewards[]` |  `object (`[LoyaltyReward](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands.sessionRecords#LoyaltyReward)`)` Optional. Available rewards for the customer.  
`appliedCodes[]` |  `string` Optional. Codes that are currently applied to the order/session.  
`appliedRewardIds[]` |  `string` Optional. Reward IDs that are currently applied to the order/session.  
  
## CustomerInformation

Information about the customer.

JSON representation  
---  
      
    
    {
      "name": string,
      "pointsBalance": integer,
      "loyaltyAmount": {
        object ([LoyaltyAmount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/LoyaltyAmount))
      },
      "tier": string
    }  
  
Fields  
---  
`name` |  `string` Optional. The name of the customer.  
`pointsBalance  
**(deprecated)**` |  `integer` This item is deprecated!Optional. The customer's loyalty amount - points or balance.  
`loyaltyAmount` |  `object (`[LoyaltyAmount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/LoyaltyAmount)`)` Optional. The customer's loyalty amount - points or balance.  
`tier` |  `string` Optional. The customer's tier.  
  
## AccrualForecast

Forecast of loyalty points to be accrued.

JSON representation  
---  
      
    
    {
      "potentialAccrual": {
        object ([LoyaltyAmount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/LoyaltyAmount))
      },
      "upsellNudge": string
    }  
  
Fields  
---  
`potentialAccrual` |  `object (`[LoyaltyAmount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/LoyaltyAmount)`)` Optional. Potential points / balance to be earned.  
`upsellNudge` |  `string` Optional. Nudge text suggesting upsell opportunities.  
  
## OrderPricesResponse

The result of getting the order prices.

JSON representation  
---  
      
    
    {
      "success": boolean,
      "orderPriceInfo": {
        object ([OrderPriceInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#OrderPriceInfo))
      }
    }  
  
Fields  
---  
`success` |  `boolean` Required. Whether the order prices were successfully retrieved.  
`orderPriceInfo` |  `object (`[OrderPriceInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#OrderPriceInfo)`)` Optional. Total order price after all discounts, fees, taxes, etc  
  
## ValidateDeliveryAddressResponse

The result of validating a delivery address.

JSON representation  
---  
      
    
    {
      "success": boolean,
      "validationStatus": enum ([ValidationStatus](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#ValidationStatus)),
      "validDeliveryStores": [
        {
          object ([ValidDeliveryStore](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#ValidDeliveryStore))
        }
      ]
    }  
  
Fields  
---  
`success` |  `boolean` Required. Whether or not the validation completed without error.  
`validationStatus` |  `enum (`[ValidationStatus](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#ValidationStatus)`)` Required. The validation status of the delivery address.  
`validDeliveryStores[]` |  `object (`[ValidDeliveryStore](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#ValidDeliveryStore)`)` Optional. The list of valid stores that can deliver to the original delivery address. This should only be populated when the validation status is VALIDATION_STATUS_OUT_OF_RANGE. And will be ignored otherwise.  
  
## ValidDeliveryStore

A store that can deliver to the specified delivery address.

JSON representation  
---  
      
    
    {
      "store": string
    }  
  
Fields  
---  
`store` |  `string` Required. The store that can deliver to the address. Format: `projects/{project}/locations/{location}/brands/{brand}/stores/{store}`  
  
## OrderStatusResponse

The result of getting the order status.

JSON representation  
---  
      
    
    {
      "success": boolean
    }  
  
Fields  
---  
`success` |  `boolean` Required. Whether the order status was successfully retrieved.  
  
## ClientExecutionStatus

Status details for the response.

JSON representation  
---  
      
    
    {
      "httpStatusCode": integer,
      "rawProviderMessage": string,
      "rejectionReason": enum ([RejectionReason](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#RejectionReason))
    }  
  
Fields  
---  
`httpStatusCode` |  `integer` Optional. The HTTP status code from the provider.  
`rawProviderMessage` |  `string` Optional. The raw response message from the provider.  
`rejectionReason` |  `enum (`[RejectionReason](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult#RejectionReason)`)` Optional. Structured rejection reason if applicable.  
  
## RejectionReason

Reasons for rejecting a loyalty request.

Enums  
---  
`REJECTION_REASON_UNSPECIFIED` | The rejection reason is not specified.  
`REJECTION_REASON_INVALID_ID` | The ID provided was invalid.  
`REJECTION_REASON_COOLDOWN_PERIOD` | The loyalty account is subject to a cooldown period.  
`REJECTION_REASON_INSUFFICIENT_FUNDS` | The loyalty account has insufficient funds.  
`REJECTION_REASON_INSUFFICIENT_POINTS` | The loyalty account has insufficient points.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 

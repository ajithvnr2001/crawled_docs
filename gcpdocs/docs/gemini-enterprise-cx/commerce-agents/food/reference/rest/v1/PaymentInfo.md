---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/PaymentInfo/
title: PaymentInfo \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:38:57.757272+00:00
---

# PaymentInfo  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/PaymentInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  PaymentInfo Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * PaymentMethod



Payment information of the user.

Direction of flow and PCI scope:

  * `creditCardLastFourDigits` and `paymentMethod` may flow in both directions (e.g., returned in `FinalizeOrderResponse.payment_info` or passed in `Config.user_info.payment_info` to indicate a saved card on file).
  * `creditCardCvv`, `creditCardNumber`, `creditCardExpirationMonth`, `creditCardExpirationYear`, and `creditCardPostalCode` are outbound-only from the Food Ordering Service to the client POS integration in `SubmitOrderRequest.payment_info` (populated deterministically from DTMF keypad callbacks without routing through the LLM). Clients must never populate these fields in `FinalizeOrderResponse.payment_info`, `Config.user_info.payment_info`, or `OrderPayment.payment_info`.

JSON representation  
---  
      
    
    {
      "creditCardLastFourDigits": string,
      "creditCardCvv": string,
      "paymentMethod": enum ([PaymentMethod](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/PaymentInfo#PaymentMethod)),
      "creditCardNumber": string,
      "creditCardExpirationMonth": integer,
      "creditCardExpirationYear": integer,
      "creditCardPostalCode": string
    }  
  
Fields  
---  
`creditCardLastFourDigits` |  `string` Optional. The last four digits of the credit card. This is used to verify the credit card number at the payment stage.  
`creditCardCvv` |  `string` Optional. CVV of the credit card. Outbound-only in `SubmitOrderRequest.payment_info`; must never be populated in `FinalizeOrderResponse`, `UserInfo`, or `OrderPayment`.  
`paymentMethod` |  `enum (`[PaymentMethod](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/PaymentInfo#PaymentMethod)`)` Optional. The type of payment method used.  
`creditCardNumber` |  `string` Optional. The credit card number (digits only, no spaces or separators; 12 to 19 digits per ISO/IEC 7812) when paying with a new credit card. Outbound-only in `SubmitOrderRequest.payment_info`; must never be populated in `FinalizeOrderResponse`, `UserInfo`, or `OrderPayment`.  
`creditCardExpirationMonth` |  `integer` Optional. The expiration month of the credit card (1 through 12) when paying with a new credit card. Outbound-only in `SubmitOrderRequest.payment_info`; must never be populated in `FinalizeOrderResponse`, `UserInfo`, or `OrderPayment`.  
`creditCardExpirationYear` |  `integer` Optional. The four-digit expiration year of the credit card (e.g. 2028) when paying with a new credit card. Outbound-only in `SubmitOrderRequest.payment_info`; must never be populated in `FinalizeOrderResponse`, `UserInfo`, or `OrderPayment`.  
`creditCardPostalCode` |  `string` Optional. The billing postal/ZIP code of the credit card (e.g. "40299" or "M5V 3L9") when paying with a new credit card. Outbound-only in `SubmitOrderRequest.payment_info`; must never be populated in `FinalizeOrderResponse`, `UserInfo`, or `OrderPayment`.  
  
## PaymentMethod

The type of payment method.

Enums  
---  
`PAYMENT_METHOD_UNSPECIFIED` | Unspecified payment method.  
`PAYMENT_METHOD_CREDIT_CARD` | Credit card.  
`PAYMENT_METHOD_CASH` | Cash.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 

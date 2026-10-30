---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/ClientExecutionResult/
title: ClientExecutionResult \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:39:33.007035+00:00
---

# ClientExecutionResult  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/ClientExecutionResult/

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
  * OrderPricesResponse
    * JSON representation
  * ValidateDeliveryAddressResponse
    * JSON representation
  * ValidDeliveryStore
    * JSON representation
  * OrderStatusResponse
    * JSON representation



The result of a client execution request.

JSON representation  
---  
      
    
    {
      "executionId": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "finalizeOrderResponse": {
        object ([FinalizeOrderResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/ClientExecutionResult#FinalizeOrderResponse))
      },
      "orderPricesResponse": {
        object ([OrderPricesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/ClientExecutionResult#OrderPricesResponse))
      },
      "validateDeliveryAddressResponse": {
        object ([ValidateDeliveryAddressResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/ClientExecutionResult#ValidateDeliveryAddressResponse))
      },
      "orderStatusResponse": {
        object ([OrderStatusResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/ClientExecutionResult#OrderStatusResponse))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`executionId` |  `string` Required. The ID of the execution request this is a result for.  
The specific result of the execution. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`finalizeOrderResponse` |  `object (`[FinalizeOrderResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/ClientExecutionResult#FinalizeOrderResponse)`)` The result of finalizing the order.  
`orderPricesResponse` |  `object (`[OrderPricesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/ClientExecutionResult#OrderPricesResponse)`)` The result of getting the order prices.  
`validateDeliveryAddressResponse` |  `object (`[ValidateDeliveryAddressResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/ClientExecutionResult#ValidateDeliveryAddressResponse)`)` The result of validating the delivery address.  
`orderStatusResponse` |  `object (`[OrderStatusResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/ClientExecutionResult#OrderStatusResponse)`)` The result of getting the order status.  
End of mutually exclusive fields.  
  
## FinalizeOrderResponse

The result of finalizing the order.

JSON representation  
---  
      
    
    {
      "paymentFlowEnabled": boolean,
      "paymentInfo": {
        object ([PaymentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/PaymentInfo))
      },
      "totalAmountDue": {
        object ([Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money))
      },
      "orderPriceInfo": {
        object ([OrderPriceInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Order#OrderPriceInfo))
      }
    }  
  
Fields  
---  
`paymentFlowEnabled` |  `boolean` Optional. Whether to enable the payment handling flow in the agent.  
`paymentInfo` |  `object (`[PaymentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/PaymentInfo)`)` Optional. The payment information of the customer. No-op if paymentFlowEnabled is false. Only `creditCardLastFourDigits` and `paymentMethod` should be populated here; raw cardholder or sensitive authentication data must never be included.  
`totalAmountDue` |  `object (`[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money)`)` Optional. The total amount due for the order.  
`orderPriceInfo` |  `object (`[OrderPriceInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Order#OrderPriceInfo)`)` Optional. The detailed price information of the order.  
  
## OrderPricesResponse

The result of getting the order prices.

JSON representation  
---  
      
    
    {
      "success": boolean,
      "orderPriceInfo": {
        object ([OrderPriceInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Order#OrderPriceInfo))
      }
    }  
  
Fields  
---  
`success` |  `boolean` Required. Whether the order prices were successfully retrieved.  
`orderPriceInfo` |  `object (`[OrderPriceInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Order#OrderPriceInfo)`)` Optional. Total order price after all discounts, fees, taxes, etc  
  
## ValidateDeliveryAddressResponse

The result of validating a delivery address.

JSON representation  
---  
      
    
    {
      "success": boolean,
      "validationStatus": enum ([ValidationStatus](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Order#ValidationStatus)),
      "validDeliveryStores": [
        {
          object ([ValidDeliveryStore](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/ClientExecutionResult#ValidDeliveryStore))
        }
      ]
    }  
  
Fields  
---  
`success` |  `boolean` Required. Whether or not the validation completed without error.  
`validationStatus` |  `enum (`[ValidationStatus](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Order#ValidationStatus)`)` Required. The validation status of the delivery address.  
`validDeliveryStores[]` |  `object (`[ValidDeliveryStore](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/ClientExecutionResult#ValidDeliveryStore)`)` Optional. The list of valid stores that can deliver to the original delivery address. This should only be populated when the validation status is VALIDATION_STATUS_OUT_OF_RANGE. And will be ignored otherwise.  
  
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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 

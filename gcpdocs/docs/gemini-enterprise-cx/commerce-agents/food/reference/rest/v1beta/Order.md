---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order/
title: Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T06:00:14.942293+00:00
---

# Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  Order Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * OrderItem
    * JSON representation
  * OrderModifierGroup
    * JSON representation
  * OrderModifier
    * JSON representation
  * OrderModifierAction
    * JSON representation
  * OrderMetadata
    * JSON representation
  * DeliveryAddress
    * JSON representation
  * ValidationStatus
  * OrderFulfillment
    * JSON representation
  * OrderPriceInfo
    * JSON representation
  * OrderPayment
    * JSON representation
  * TippingInfo
    * JSON representation
  * LoyaltyAmount
    * JSON representation
  * PaymentInfo
    * JSON representation
  * PaymentMethod



Order represents the content of a user's in-progress or completed order.

JSON representation  
---  
      
    
    {
      "items": [
        {
          object ([OrderItem](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#OrderItem))
        }
      ],
      "metadata": {
        object ([OrderMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#OrderMetadata))
      },
      "fulfillment": {
        object ([OrderFulfillment](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#OrderFulfillment))
      },
      "priceInfo": {
        object ([OrderPriceInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#OrderPriceInfo))
      },
      "externalOrderId": string,
      "orderPayment": {
        object ([OrderPayment](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#OrderPayment))
      },
      "customIntegrationAttributes": {
        object
      }
    }  
  
Fields  
---  
`items[]` |  `object (`[OrderItem](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#OrderItem)`)` Optional. The items in the order.  
`metadata` |  `object (`[OrderMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#OrderMetadata)`)` Optional. Other metadata collected or inferred during the order.  
`fulfillment` |  `object (`[OrderFulfillment](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#OrderFulfillment)`)` Optional. The fulfillment information for the order.  
`priceInfo` |  `object (`[OrderPriceInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#OrderPriceInfo)`)` Optional. Price information for the order.  
`externalOrderId` |  `string` Output only. The external identifier for this order. Populated only if a point-of-sale integration is enabled.  
`orderPayment` |  `object (`[OrderPayment](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#OrderPayment)`)` Optional. The payment state associated with this order.  
`customIntegrationAttributes` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Output only. Arbitrary metadata associated with the order, used for downstream custom integrations. For example, it can be converted into the payload expected by a point-of-sale (POS) system or a web/mobile client to sync the cart or submit the order. Populated by brand-specific hooks.  
  
## OrderItem

OrderItem specifies the state of an Item which is part of an Order.

JSON representation  
---  
      
    
    {
      "uid": string,
      "itemId": string,
      "displayName": string,
      "image": {
        object ([Image](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Image))
      },
      "basePrice": {
        object ([Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money))
      },
      "integrationAttributes": {
        object ([ItemIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ItemIntegrationAttributes))
      },
      "modifierGroups": [
        {
          object ([OrderModifierGroup](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#OrderModifierGroup))
        }
      ],
      "quantity": integer,
      "totalPrice": {
        object ([Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money))
      },
      "categoryIds": [
        string
      ],
      "isPending": boolean
    }  
  
Fields  
---  
`uid` |  `string` Optional. A system-assigned unique identifier for this item.  
`itemId` |  `string` Required. Identifier for an Item in the Menu, unique within its Menu.  
`displayName` |  `string` Output only. Human-readable name for this line item to be shown on user interfaces.  
`image` |  `object (`[Image](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Image)`)` Output only. Image to display for this item in the UI.  
`basePrice` |  `object (`[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money)`)` Output only. The base price of the item. This may be affected by the selected modifiers. This is the price per unit of the item.  
`integrationAttributes` |  `object (`[ItemIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ItemIntegrationAttributes)`)` Output only. Metadata associated with this entity used for downstream integrations.  
`modifierGroups[]` |  `object (`[OrderModifierGroup](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#OrderModifierGroup)`)` Optional. ModifierGroups applied to this item.  
`quantity` |  `integer` Optional. The quantity of this item in the order.  
`totalPrice` |  `object (`[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money)`)` Output only. The total price for this line item, inclusive of selected modifiers and reflecting the item quantity, before tax. Used for per-item bag display.  
`categoryIds[]` |  `string` Output only. Category IDs the underlying menu item belongs to. Mirrors the menu's Item.category_ids so clients can group ordered items by menu category.  
`isPending` |  `boolean` Output only. Indicates if the item is in a pending state.  
  
## OrderModifierGroup

OrderModifierGroup specifies the state of a ModifierGroup which is part of an OrderItem.

JSON representation  
---  
      
    
    {
      "modifierGroupId": string,
      "displayName": string,
      "integrationAttributes": {
        object ([ModifierGroupIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ModifierGroupIntegrationAttributes))
      },
      "modifiers": [
        {
          object ([OrderModifier](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#OrderModifier))
        }
      ]
    }  
  
Fields  
---  
`modifierGroupId` |  `string` Required. Identifier for this modifier group, unique within its menu.  
`displayName` |  `string` Output only. The modifier group name -- e.g. "Toppings (Sandwich)" or "Side for Medium Combo".  
`integrationAttributes` |  `object (`[ModifierGroupIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ModifierGroupIntegrationAttributes)`)` Output only. Metadata associated with this entity used for downstream integrations.  
`modifiers[]` |  `object (`[OrderModifier](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#OrderModifier)`)` Optional. The modifiers applied to this modifier group.  
  
## OrderModifier

OrderModifier specifies the state of a Modifier which is part of an OrderModifierGroup.

JSON representation  
---  
      
    
    {
      "uid": string,
      "modifierId": string,
      "displayName": string,
      "priceAdjustment": {
        object ([Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money))
      },
      "quantity": integer,
      "modifierAction": {
        object ([OrderModifierAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#OrderModifierAction))
      },
      "image": {
        object ([Image](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Image))
      },
      "integrationAttributes": {
        object ([ModifierIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ModifierIntegrationAttributes))
      },
      "modifierGroups": [
        {
          object ([OrderModifierGroup](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#OrderModifierGroup))
        }
      ],
      "isDefault": boolean
    }  
  
Fields  
---  
`uid` |  `string` Optional. A system-assigned unique identifier for this modifier.  
`modifierId` |  `string` Required. Identifier for this modifier, unique within the menu.  
`displayName` |  `string` Output only. The modifier display name to be shown on user interfaces.  
`priceAdjustment` |  `object (`[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money)`)` Output only. The price adjustment associated with this modifier, if any. This is the price per unit of the modifier.  
`quantity` |  `integer` Optional. The quantity of this modifier action applied.  
`modifierAction` |  `object (`[OrderModifierAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#OrderModifierAction)`)` Optional. The modifier action applied to this modifier.  
`image` |  `object (`[Image](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Image)`)` Output only. Image to display for this modifier in the UI.  
`integrationAttributes` |  `object (`[ModifierIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ModifierIntegrationAttributes)`)` Output only. Metadata associated with this entity used for downstream integrations.  
`modifierGroups[]` |  `object (`[OrderModifierGroup](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#OrderModifierGroup)`)` Optional. Nested modifier groups applied to this modifier.  
`isDefault` |  `boolean` Output only. Whether this modifier is a default selection for its modifier group. Needed so clients can compute an accurate selections diff.  
  
## OrderModifierAction

OrderModifierAction specifies the ModifierAction associated with an applied OrderModifier.

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Optional. The modifier action name -- e.g. "NO", "SIDE", "ADD", "EXTRA".  
  
## OrderMetadata

OrderMetadata contains other metadata collected or inferred during the order.

JSON representation  
---  
      
    
    {
      "collectedCustomerName": string,
      "callerPhoneNumber": string,
      "deliveryAddress": {
        object ([DeliveryAddress](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#DeliveryAddress))
      }
    }  
  
Fields  
---  
`collectedCustomerName` |  `string` Optional. Name of the customer, collected while taking the order. Only populated when the agent is configured to collect the customer's name. This may be collected verbally and could contain spelling mistakes or mistranscriptions, so care should be taken when displaying it to users, and it shouldn't be trusted as e.g. payment information.  
`callerPhoneNumber` |  `string` Optional. The phone number of the customer placing the order.  
`deliveryAddress` |  `object (`[DeliveryAddress](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#DeliveryAddress)`)` Optional. The delivery address, if the order is a delivery order.  
  
## DeliveryAddress

The delivery address of an order. It could be an existing saved or collected address.

JSON representation  
---  
      
    
    {
      "address": {
        object ([PostalAddress](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/PostalAddress))
      },
      "validationStatus": enum ([ValidationStatus](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#ValidationStatus)),
      "coordinates": {
        object ([LatLng](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/LatLng))
      }
    }  
  
Fields  
---  
`address` |  `object (`[PostalAddress](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/PostalAddress)`)` Optional. The delivery address.  
`validationStatus` |  `enum (`[ValidationStatus](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#ValidationStatus)`)` Optional. The validation status of the address.  
`coordinates` |  `object (`[LatLng](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/LatLng)`)` Optional. The geographic coordinates of the address. Used to validate if the address is within the delivery range of the store.  
  
## ValidationStatus

The validation status of the delivery address. It is determined by client-specific validation logic.

Enums  
---  
`VALIDATION_STATUS_UNSPECIFIED` | The address has not yet been validated.  
`VALIDATION_STATUS_VALID` | The address is valid.  
`VALIDATION_STATUS_INVALID` | The address is invalid (does not exist, cannot be parsed, etc.)  
`VALIDATION_STATUS_OUT_OF_RANGE` | The address exists and is resolved, but out of range for the store.  
`VALIDATION_STATUS_INCOMPLETE_ADDRESS` | The address is missing required fields (missing street number/name, city, state, zip, etc)  
  
## OrderFulfillment

OrderFulfillment contains information about order fulfillment.

JSON representation  
---  
      
    
    {
      "fulfillmentMethod": enum ([FulfillmentMethod](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/FulfillmentMethod)),
      "createTime": string,
      "targetFulfillmentTime": string
    }  
  
Fields  
---  
`fulfillmentMethod` |  `enum (`[FulfillmentMethod](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/FulfillmentMethod)`)` Optional. The fulfillment method of the order.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the order was created at.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`targetFulfillmentTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The time the order is scheduled for fulfillment, used for 'order ahead'. If not provided, the order is assumed to be for 'as soon as possible'.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## OrderPriceInfo

OrderPriceInfo encapsulates the various price components of an order.

JSON representation  
---  
      
    
    {
      "totalPrice": {
        object ([Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money))
      },
      "subtotalPrice": {
        object ([Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money))
      },
      "taxPrice": {
        object ([Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money))
      },
      "discount": {
        object ([Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money))
      },
      "saving": {
        object ([Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money))
      },
      "fees": {
        object ([Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money))
      },
      "tip": {
        object ([Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money))
      }
    }  
  
Fields  
---  
`totalPrice` |  `object (`[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money)`)` Optional. The final total price after all taxes, fees, and discounts are applied.  
`subtotalPrice` |  `object (`[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money)`)` Optional. The subtotal price of all items and modifiers, before taxes, discounts.  
`taxPrice` |  `object (`[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money)`)` Optional. The amount of tax applied to the order.  
`discount` |  `object (`[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money)`)` Optional. Total discount applied to the order  
`saving` |  `object (`[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money)`)` Optional. Deal savings applied to the order  
`fees` |  `object (`[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money)`)` Optional. Total fees applied to the order  
`tip` |  `object (`[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money)`)` Optional. The resolved tip amount applied to the order.  
  
## OrderPayment

The payment related information for an order.

JSON representation  
---  
      
    
    {
      "tippingInfo": {
        object ([TippingInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#TippingInfo))
      },
      "loyaltyConsumed": {
        object ([LoyaltyAmount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#LoyaltyAmount))
      },
      "paymentInfo": {
        object ([PaymentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#PaymentInfo))
      }
    }  
  
Fields  
---  
`tippingInfo` |  `object (`[TippingInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#TippingInfo)`)` Optional. Tipping information.  
`loyaltyConsumed` |  `object (`[LoyaltyAmount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#LoyaltyAmount)`)` Optional. Loyalty amount consumed for the payment.  
`paymentInfo` |  `object (`[PaymentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#PaymentInfo)`)` Optional. Information about the payment method used.  
  
## TippingInfo

Information about tipping.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "amount": {
        object ([Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money))
      },
      "percentageBps": integer
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The tip amount or percentage. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`amount` |  `object (`[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money)`)` Optional. A specific money amount for the tip.  
`percentageBps` |  `integer` Optional. Percentage in basis points, e.g., 450 = 4.5%.  
End of mutually exclusive fields.  
  
## LoyaltyAmount

Represents a customer's loyalty amount.

JSON representation  
---  
      
    
    {
      "units": string
    }  
  
Fields  
---  
`units` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The loyalty points.  
  
## PaymentInfo

Payment information of the user.

Direction of flow and PCI scope:

  * `creditCardLastFourDigits` and `paymentMethod` may flow in both directions (e.g., returned in `FinalizeOrderResponse.payment_info` or passed in `Config.user_info.payment_info` to indicate a saved card on file).
  * `creditCardCvv`, `creditCardNumber`, `creditCardExpirationMonth`, `creditCardExpirationYear`, and `creditCardPostalCode` are outbound-only from the Food Ordering Service to the client POS integration in `SubmitOrderRequest.payment_info` (populated deterministically from DTMF keypad callbacks without routing through the LLM). Clients must never populate these fields in `FinalizeOrderResponse.payment_info`, `Config.user_info.payment_info`, or `OrderPayment.payment_info`.

JSON representation  
---  
      
    
    {
      "creditCardLastFourDigits": string,
      "creditCardCvv": string,
      "paymentMethod": enum ([PaymentMethod](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#PaymentMethod)),
      "creditCardNumber": string,
      "creditCardExpirationMonth": integer,
      "creditCardExpirationYear": integer,
      "creditCardPostalCode": string
    }  
  
Fields  
---  
`creditCardLastFourDigits` |  `string` Optional. The last four digits of the credit card. This is used to verify the credit card number at the payment stage.  
`creditCardCvv` |  `string` Optional. CVV of the credit card. Outbound-only in `SubmitOrderRequest.payment_info`; must never be populated in `FinalizeOrderResponse`, `UserInfo`, or `OrderPayment`.  
`paymentMethod` |  `enum (`[PaymentMethod](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#PaymentMethod)`)` Optional. The type of payment method used.  
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

---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Config/
title: Config \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:39:15.521326+00:00
---

# Config  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  Config Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * UserInfo
    * JSON representation
  * PastOrder
    * JSON representation
  * OrderType
  * FeatureGate
    * JSON representation
  * ClientAppInfo
    * JSON representation
  * SessionMode



The configuration for a session and food ordering properties. At the start of each connection, the client must first send a config message. This must happen before any other requests to initiate the session. If the client disconnects, they should repeat the same config message when they reconnect.

JSON representation  
---  
      
    
    {
      "session": string,
      "store": string,
      "laneId": string,
      "enableEchoCancellation": boolean,
      "daypartId": string,
      "userInfo": {
        object ([UserInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Config#UserInfo))
      },
      "orderType": enum ([OrderType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Config#OrderType)),
      "initialOrder": {
        object ([Order](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order))
      },
      "featureGate": {
        object ([FeatureGate](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Config#FeatureGate))
      },
      "initialUtterance": string,
      "clientAppInfo": {
        object ([ClientAppInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Config#ClientAppInfo))
      },
      "mode": enum ([SessionMode](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Config#SessionMode)),
      "channelType": enum ([ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ChannelType)),
      "enableListenOnlyDualChannel": boolean,
      "testSessionStartTime": string,
      "fulfillmentMethod": enum ([FulfillmentMethod](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/FulfillmentMethod)),
      "clientEnv": string
    }  
  
Fields  
---  
`session` |  `string` Required. The session for the order. Format: `projects/{project}/locations/{location}/sessions/{session}`  
`store` |  `string` Required. The store the order is being placed for. Format: `projects/{project}/locations/{location}/brands/{brand}/stores/{store}`  
`laneId` |  `string` Optional. The id of a specifc drive through lane.  
`enableEchoCancellation` |  `boolean` Optional. Whether to enable echo cancellation for the session. If enabled, the client should provide the customerAudio and crewAudio in the AudioInput.  
`daypartId` |  `string` Optional. Daypart of the food menu, including breakfast, lunch, dinner, etc. This is used to determine the menu to use for the order.  
`userInfo` |  `object (`[UserInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Config#UserInfo)`)` Optional. The personal information of the end user shared with the agent.  
`orderType  
**(deprecated)**` |  `enum (`[OrderType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Config#OrderType)`)` This item is deprecated!Optional. Deprecated: Use initialOrder.fulfillment.fulfillment_type instead. The type of order to be placed.  
`initialOrder` |  `object (`[Order](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order)`)` Optional. The initial order before starting the agent session. If provided, the agent will use it as the initial order state.  
`featureGate` |  `object (`[FeatureGate](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Config#FeatureGate)`)` Optional. The feature gates for the session. This is used to enable or disable features for the session.  
`initialUtterance` |  `string` Optional. The initial utterance from the client to kick off the conversation. If provided, the agent will use this as the first user utterance, and will not start with a greeting message.  
`clientAppInfo` |  `object (`[ClientAppInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Config#ClientAppInfo)`)` Optional. The information about the client application and device environment.  
`mode` |  `enum (`[SessionMode](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Config#SessionMode)`)` Optional. The mode of the session.  
`channelType` |  `enum (`[ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ChannelType)`)` Optional. The type of channel used for agent communication.  
`enableListenOnlyDualChannel` |  `boolean` Optional. Whether to enable listen-only dual channel for the session. If enabled, the client should provide the customerAudio and crewAudio in the AudioInput.  
`testSessionStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The start time of the session, used for testing or evaluation purposes.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`fulfillmentMethod` |  `enum (`[FulfillmentMethod](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/FulfillmentMethod)`)` Optional. The fulfillment method for the session.  
`clientEnv` |  `string` Optional. The environment on the client side (e.g., "qa", "uat", "preprod").  
  
## UserInfo

Personal information of the end user shared with the Food AI agent.

JSON representation  
---  
      
    
    {
      "preferredName": string,
      "paymentInfo": {
        object ([PaymentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#PaymentInfo))
      },
      "deliveryAddress": string,
      "pastOrders": [
        {
          object ([PastOrder](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Config#PastOrder))
        }
      ],
      "loyaltyInfo": {
        object ([LoyaltyInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/LoyaltyInfo))
      },
      "phoneNumber": string,
      "userId": string,
      "savedDeliveryAddress": {
        object ([DeliveryAddress](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#DeliveryAddress))
      },
      "additionalSavedAddresses": [
        {
          object ([DeliveryAddress](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#DeliveryAddress))
        }
      ],
      "additionalSavedCustomerNames": [
        string
      ]
    }  
  
Fields  
---  
`preferredName` |  `string` Optional. The name of the user that the agent should use to address the user. Food AI client is responsible for selecting the preferred name based on the user's profile, and make sure it aligns with the brand's convention, e.g. use first name, or full name.  
`paymentInfo` |  `object (`[PaymentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#PaymentInfo)`)` Optional. The payment information of the user. Only `creditCardLastFourDigits` and `paymentMethod` should be populated here; raw cardholder or sensitive authentication data must never be included.  
`deliveryAddress  
**(deprecated)**` |  `string` This item is deprecated!Optional. Deprecated: Use savedDeliveryAddress instead. The saved delivery address of the user.  
`pastOrders[]` |  `object (`[PastOrder](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Config#PastOrder)`)` Optional. The order history of the user.  
`loyaltyInfo` |  `object (`[LoyaltyInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/LoyaltyInfo)`)` Optional. The loyalty info of the user.  
`phoneNumber` |  `string` Optional. The phone number of the user.  
`userId` |  `string` Optional. The unique identifier of the user in the client's system.  
`savedDeliveryAddress` |  `object (`[DeliveryAddress](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#DeliveryAddress)`)` Optional. The saved delivery address of the user. Will be replacing the existing string deliveryAddress field.  
`additionalSavedAddresses[]` |  `object (`[DeliveryAddress](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order#DeliveryAddress)`)` Optional. All past delivery addresses previously used with the user's phone number, deduplicated by the client. Unlike savedDeliveryAddress, these are not confirmed to belong to the current user: e.g. if the session is for a phone call, the phone number might be associated with multiple users. Addresses need not be validated. May include savedDeliveryAddress.  
`additionalSavedCustomerNames[]` |  `string` Optional. All customer names previously used with the user's phone number, deduplicated by the client. Unlike preferredName, these are not confirmed to belong to the current user: e.g. if the session is for a phone call, the phone number might be associated with multiple users. May include preferredName.  
  
## PastOrder

The past order of the user.

JSON representation  
---  
      
    
    {
      "order": {
        object ([Order](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order))
      }
    }  
  
Fields  
---  
`order` |  `object (`[Order](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order)`)` Required. The original Food AI order.  
  
## OrderType

The type of order to be placed.

Enums  
---  
`ORDER_TYPE_UNSPECIFIED` | The order type is not specified.  
`ORDER_TYPE_DRIVE_THROUGH` | The order is for drive through.  
`ORDER_TYPE_CARRY_OUT` | The order is for carry out.  
`ORDER_TYPE_DELIVERY` | The order is for delivery.  
  
## FeatureGate

The feature gates for the session. This is used to enable or disable features for the session.

JSON representation  
---  
      
    
    {
      "triggerOfferEngineOnDemand": boolean,
      "triggerLoyaltyOnDemand": boolean,
      "triggerOrderMediaAssistantOnDemand": boolean,
      "menuResponseEnabled": boolean,
      "revampedPaymentFlowEnabled": boolean,
      "updatedOrderStateEnabled": boolean,
      "enableOrderStatusRetrieval": boolean,
      "enableClientEscalationAudio": boolean
    }  
  
Fields  
---  
`triggerOfferEngineOnDemand` |  `boolean` Optional. For limited audience only, if set, offer engine will be optional in the payment flow and will only be triggered when users request for it.  
`triggerLoyaltyOnDemand` |  `boolean` Optional. For limited audience only, if set, loyalty will be optional in the payment flow and will only be triggered when users request for it.  
`triggerOrderMediaAssistantOnDemand` |  `boolean` Optional. For limited audience only, if set, order media assistant will be optional and will only be triggered when users request for it.  
`menuResponseEnabled` |  `boolean` Optional. Returns the menu data to the client in BidiProcessOrderResponse if set.  
`revampedPaymentFlowEnabled` |  `boolean` Optional. For limited audience only, if set, a revamped version of the payment flow will be used.  
`updatedOrderStateEnabled` |  `boolean` Optional. If set, updatedOrderState is returned instead of legacyOrderStateResponse.  
`enableOrderStatusRetrieval` |  `boolean` Optional. If set, the agent will support order status retrieval.  
`enableClientEscalationAudio` |  `boolean` Optional. If set, client escalation audio is synthesized and streamed on ClientEscalationEvent.  
  
## ClientAppInfo

Information about the client application and device environment. This is primarily used for logging, analytics, and debugging.

JSON representation  
---  
      
    
    {
      "deviceModel": string,
      "osVersion": string,
      "sdkVersion": string
    }  
  
Fields  
---  
`deviceModel` |  `string` Optional. The device model of the client (e.g., "iPhone 13", "Pixel 7", "Kiosk v2").  
`osVersion` |  `string` Optional. The operating system version of the client (e.g., "iOS 16.1", "Android 13").  
`sdkVersion` |  `string` Optional. The version of the client SDK or application software.  
  
## SessionMode

The mode of the session.

Enums  
---  
`SESSION_MODE_UNSPECIFIED` | The session mode is not specified.  
`HYBRID` | The session supports both audio and text. This is the default.  
`TEXT` | The session is text-only.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 

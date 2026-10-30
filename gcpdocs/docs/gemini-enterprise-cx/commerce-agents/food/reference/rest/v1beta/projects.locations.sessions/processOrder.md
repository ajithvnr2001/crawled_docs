---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.sessions/processOrder/
title: Method: projects.locations.sessions.processOrder \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T06:00:09.969842+00:00
---

# Method: projects.locations.sessions.processOrder  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.sessions/processOrder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  Method: projects.locations.sessions.processOrder Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes



Performs a single turn logic to process user input and return the result.

### HTTP request

`POST https://foodorderingaiagent.googleapis.com/v1beta/{config.session=projects/*/locations/*/sessions/*}:processOrder`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`config.session` |  `string` Required. The session for the order. Format: `projects/{project}/locations/{location}/sessions/{session}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "config": {
        "session": string,
        "store": string,
        "laneId": string,
        "enableEchoCancellation": boolean,
        "daypartId": string,
        "userInfo": {
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
        },
        "orderType": enum ([OrderType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Config#OrderType)),
        "initialOrder": {
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
        },
        "featureGate": {
          "triggerOfferEngineOnDemand": boolean,
          "triggerLoyaltyOnDemand": boolean,
          "triggerOrderMediaAssistantOnDemand": boolean,
          "menuResponseEnabled": boolean,
          "revampedPaymentFlowEnabled": boolean,
          "updatedOrderStateEnabled": boolean,
          "enableOrderStatusRetrieval": boolean,
          "enableClientEscalationAudio": boolean
        },
        "initialUtterance": string,
        "clientAppInfo": {
          "deviceModel": string,
          "osVersion": string,
          "sdkVersion": string
        },
        "mode": enum ([SessionMode](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Config#SessionMode)),
        "channelType": enum ([ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ChannelType)),
        "enableListenOnlyDualChannel": boolean,
        "testSessionStartTime": string,
        "fulfillmentMethod": enum ([FulfillmentMethod](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/FulfillmentMethod)),
        "clientEnv": string
      },
      "turnType": enum ([TurnType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/TurnType)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "textInput": {
        object ([TextInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/TextInput))
      },
      "audioInput": {
        object ([AudioInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/AudioInput))
      },
      "eventInput": {
        object ([EventInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/EventInput))
      },
      "clientExecutionResult": {
        object ([ClientExecutionResult](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult))
      },
      "blobInput": {
        object ([Blob](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Blob))
      },
      "dtmfInput": {
        object ([DtmfInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/DtmfInput))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`config.store` |  `string` Required. The store the order is being placed for. Format: `projects/{project}/locations/{location}/brands/{brand}/stores/{store}`  
`config.laneId` |  `string` Optional. The id of a specifc drive through lane.  
`config.enableEchoCancellation` |  `boolean` Optional. Whether to enable echo cancellation for the session. If enabled, the client should provide the customerAudio and crewAudio in the AudioInput.  
`config.daypartId` |  `string` Optional. Daypart of the food menu, including breakfast, lunch, dinner, etc. This is used to determine the menu to use for the order.  
`config.userInfo` |  `object (`[UserInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Config#UserInfo)`)` Optional. The personal information of the end user shared with the agent.  
`config.orderType  
**(deprecated)**` |  `enum (`[OrderType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Config#OrderType)`)` Optional. Deprecated: Use initialOrder.fulfillment.fulfillment_type instead. The type of order to be placed.  
`config.initialOrder` |  `object (`[Order](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order)`)` Optional. The initial order before starting the agent session. If provided, the agent will use it as the initial order state.  
`config.featureGate` |  `object (`[FeatureGate](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Config#FeatureGate)`)` Optional. The feature gates for the session. This is used to enable or disable features for the session.  
`config.initialUtterance` |  `string` Optional. The initial utterance from the client to kick off the conversation. If provided, the agent will use this as the first user utterance, and will not start with a greeting message.  
`config.clientAppInfo` |  `object (`[ClientAppInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Config#ClientAppInfo)`)` Optional. The information about the client application and device environment.  
`config.mode` |  `enum (`[SessionMode](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Config#SessionMode)`)` Optional. The mode of the session.  
`config.channelType` |  `enum (`[ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ChannelType)`)` Optional. The type of channel used for agent communication.  
`config.enableListenOnlyDualChannel` |  `boolean` Optional. Whether to enable listen-only dual channel for the session. If enabled, the client should provide the customerAudio and crewAudio in the AudioInput.  
`config.testSessionStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The start time of the session, used for testing or evaluation purposes.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`config.fulfillmentMethod` |  `enum (`[FulfillmentMethod](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/FulfillmentMethod)`)` Optional. The fulfillment method for the session.  
`config.clientEnv` |  `string` Optional. The environment on the client side (e.g., "qa", "uat", "preprod").  
`turnType` |  `enum (`[TurnType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/TurnType)`)` Optional. Explicit indicator of the request's position in the session lifecycle. Allows clients to deterministically control when initial session setup variables are injected.  
The input from the client. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`textInput` |  `object (`[TextInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/TextInput)`)` The text input from the client.  
`audioInput` |  `object (`[AudioInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/AudioInput)`)` The audio input from the client.  
`eventInput` |  `object (`[EventInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/EventInput)`)` The event input from the client.  
`clientExecutionResult` |  `object (`[ClientExecutionResult](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ClientExecutionResult)`)` The result of a client execution request.  
`blobInput` |  `object (`[Blob](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Blob)`)` Generic binary data input.  
`dtmfInput` |  `object (`[DtmfInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/DtmfInput)`)` The DTMF input from the client.  
End of mutually exclusive fields.  
  
### Response body

Response message for `[FoodOrderingService.ProcessOrder](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.sessions/processOrder#google.cloud.foodorderingaiagent.v1beta.FoodOrderingService.ProcessOrder)`. Functionally contains fields from BidiProcessOrderResponse minus streaming-specific ones.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "responses": [
        {
          object ([BidiProcessOrderResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/BidiProcessOrderResponse))
        }
      ]
    }  
  
Fields  
---  
`responses[]` |  `object (`[BidiProcessOrderResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/BidiProcessOrderResponse)`)` Output only. List of agent responses to the request, returned in-order.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 

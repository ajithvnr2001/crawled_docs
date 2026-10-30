---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse/
title: BidiProcessOrderResponse \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:38:29.286023+00:00
---

# BidiProcessOrderResponse  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  BidiProcessOrderResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * AgentAudio
    * JSON representation
  * SpeechRecognition
    * JSON representation
  * InterruptionSignal
  * AgentEvent
    * JSON representation
  * RestartOrder
    * JSON representation
  * ClientExecutionRequest
    * JSON representation
  * FinalizeOrderRequest
  * SubmitOrderRequest
    * JSON representation
  * LoyaltyInfo
    * JSON representation
  * LoyaltyAmount
    * JSON representation
  * OrderPricesRequest
    * JSON representation
  * ValidateDeliveryAddressRequest
    * JSON representation
  * OrderStatusRequest
  * UpdatedOrderState
    * JSON representation
  * OrderStateUpdateStatus
  * AgentText
    * JSON representation
  * SentimentMeasurement
    * JSON representation
  * TurnCompleted
  * EndSession
    * JSON representation
  * EndType
  * DiagnosticInfo
    * JSON representation



The top-level message returned from `FoodOrderingService.BidiProcessOrder` method.

JSON representation  
---  
      
    
    {
      "diagnosticInfo": {
        object ([DiagnosticInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#DiagnosticInfo))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "agentAudio": {
        object ([AgentAudio](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#AgentAudio))
      },
      "speechRecognition": {
        object ([SpeechRecognition](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#SpeechRecognition))
      },
      "legacyOrderStateResponse": {
        object
      },
      "interruptionSignal": {
        object ([InterruptionSignal](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#InterruptionSignal))
      },
      "agentEvent": {
        object ([AgentEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#AgentEvent))
      },
      "clientExecutionRequest": {
        object ([ClientExecutionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#ClientExecutionRequest))
      },
      "updatedOrderState": {
        object ([UpdatedOrderState](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#UpdatedOrderState))
      },
      "agentText": {
        object ([AgentText](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#AgentText))
      },
      "suggestedOptions": {
        object ([SuggestedOptions](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedOptions))
      },
      "sentimentMeasurement": {
        object ([SentimentMeasurement](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#SentimentMeasurement))
      },
      "turnCompleted": {
        object ([TurnCompleted](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#TurnCompleted))
      },
      "endSession": {
        object ([EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#EndSession))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`diagnosticInfo` |  `object (`[DiagnosticInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#DiagnosticInfo)`)` Diagnostic information containing execution timing, VAD speech boundaries, and latency metrics for the completed turn. Populated upon turn completion.  
The response from the agent. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`agentAudio` |  `object (`[AgentAudio](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#AgentAudio)`)` The audio response from the agent.  
`speechRecognition` |  `object (`[SpeechRecognition](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#SpeechRecognition)`)` The speech recognition result from the agent.  
`legacyOrderStateResponse` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The legacy order state response for a session.  
`interruptionSignal` |  `object (`[InterruptionSignal](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#InterruptionSignal)`)` Interruption signal detected from the audio input.  
`agentEvent` |  `object (`[AgentEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#AgentEvent)`)` Event from the agent.  
`clientExecutionRequest` |  `object (`[ClientExecutionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#ClientExecutionRequest)`)` The request forward to the client to execute. This is used for client side execution, such as adding a code to the order.  
`updatedOrderState` |  `object (`[UpdatedOrderState](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#UpdatedOrderState)`)` Indicates an update to the order state. Includes the complete state of the order.  
`agentText` |  `object (`[AgentText](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#AgentText)`)` The text response from the agent.  
`suggestedOptions` |  `object (`[SuggestedOptions](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedOptions)`)` Options to suggest to the customer.  
`sentimentMeasurement` |  `object (`[SentimentMeasurement](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#SentimentMeasurement)`)` The realtime sentiment score measured for this turn.  
`turnCompleted` |  `object (`[TurnCompleted](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#TurnCompleted)`)` Turn Completed message.  
`endSession` |  `object (`[EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#EndSession)`)` Indicates that the session is ending, and that this will be the last turn.The agent will finish sending any pending responses for the current turn, and then send a final turnCompleted message. The agent will not start any new turns. For example, a 2 turn session will look like:

  * Turn 1
  * customer input 1
  * ... agent response and order state messages
  * turnCompleted
  * Turn 2
  * customer input 2
  * ... agent response and order state messages
  * endSession
  * ... pending agent response and order state messages
  * turnCompleted

  
End of mutually exclusive fields.  
  
## AgentAudio

The audio response from the agent.

JSON representation  
---  
      
    
    {
      "agentAudio": string
    }  
  
Fields  
---  
`agentAudio` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The audio data from the agent.A base64-encoded string.  
  
## SpeechRecognition

The speech recognition result from the agent.

JSON representation  
---  
      
    
    {
      "transcript": string,
      "languageCode": string,
      "isFinal": boolean
    }  
  
Fields  
---  
`transcript` |  `string` Transcribed text from the audio input in the detected language.  
`languageCode` |  `string` The language code of the transcript. The language code should be in BCP-47 format, such as "en-US".  
`isFinal` |  `boolean` Indicates whether this is the final transcript for the turn.  
  
## InterruptionSignal

This type has no fields.

Indicates the agent's audio response has been interrupted (e.g. by end user barge-in). Client should stop playback immediately.

## AgentEvent

Special event from the agent that needs client to take action.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "restartOrder": {
        object ([RestartOrder](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#RestartOrder))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The event from the agent. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`restartOrder` |  `object (`[RestartOrder](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#RestartOrder)`)` Customer requests to restart the order.  
End of mutually exclusive fields.  
  
## RestartOrder

Customer requests to start over the order.

JSON representation  
---  
      
    
    {
      "confirmationStep": boolean
    }  
  
Fields  
---  
`confirmationStep` |  `boolean` The agent is asking the customer to confirm the restarting request.  
  
## ClientExecutionRequest

A request to the for client side to execute a command.

JSON representation  
---  
      
    
    {
      "executionId": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "finalizeOrderRequest": {
        object ([FinalizeOrderRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#FinalizeOrderRequest))
      },
      "submitOrderRequest": {
        object ([SubmitOrderRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#SubmitOrderRequest))
      },
      "orderPricesRequest": {
        object ([OrderPricesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#OrderPricesRequest))
      },
      "validateDeliveryAddressRequest": {
        object ([ValidateDeliveryAddressRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#ValidateDeliveryAddressRequest))
      },
      "orderStatusRequest": {
        object ([OrderStatusRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#OrderStatusRequest))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`executionId` |  `string` Required. A unique ID for this execution request.  
The specific request to be executed. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`finalizeOrderRequest` |  `object (`[FinalizeOrderRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#FinalizeOrderRequest)`)` A request to finalize the order.  
`submitOrderRequest` |  `object (`[SubmitOrderRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#SubmitOrderRequest)`)` A request to submit the order.  
`orderPricesRequest` |  `object (`[OrderPricesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#OrderPricesRequest)`)` A request to get the order prices.  
`validateDeliveryAddressRequest` |  `object (`[ValidateDeliveryAddressRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#ValidateDeliveryAddressRequest)`)` A request to validate the delivery address.  
`orderStatusRequest` |  `object (`[OrderStatusRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#OrderStatusRequest)`)` A request to get the order status.  
End of mutually exclusive fields.  
  
## FinalizeOrderRequest

This type has no fields.

A request to finalize the order. This is typically sent by the agent when the customer indicates they are done ordering and want to pay.

## SubmitOrderRequest

A request to submit the order, with all the required payment information collected from the customer.

JSON representation  
---  
      
    
    {
      "paymentInfo": {
        object ([PaymentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/PaymentInfo))
      },
      "loyaltyInfo": {
        object ([LoyaltyInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#LoyaltyInfo))
      },
      "tipAmount": {
        object ([Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money))
      }
    }  
  
Fields  
---  
`paymentInfo` |  `object (`[PaymentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/PaymentInfo)`)` Required. The payment information for the order.  
`loyaltyInfo` |  `object (`[LoyaltyInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#LoyaltyInfo)`)` Optional. The loyalty consumed for the order.  
`tipAmount` |  `object (`[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money)`)` Optional. The tip amount for the order.  
  
## LoyaltyInfo

Represents a customer's loyalty information.

JSON representation  
---  
      
    
    {
      "loyaltyAmount": {
        object ([LoyaltyAmount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#LoyaltyAmount))
      }
    }  
  
Fields  
---  
`loyaltyAmount` |  `object (`[LoyaltyAmount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#LoyaltyAmount)`)` Required. The loyalty amount. This can be a loyalty balance or loyalty consumed.  
  
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
  
## OrderPricesRequest

A request to get the order prices.

JSON representation  
---  
      
    
    {
      "order": {
        object ([Order](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Order))
      }
    }  
  
Fields  
---  
`order` |  `object (`[Order](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Order)`)` Optional. The order to get the prices for. If not specified, we can assume the request is for the existing order/cart in the session.  
  
## ValidateDeliveryAddressRequest

A request to validate a delivery address collected during the session.

JSON representation  
---  
      
    
    {
      "deliveryAddress": {
        object ([DeliveryAddress](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Order#DeliveryAddress))
      }
    }  
  
Fields  
---  
`deliveryAddress` |  `object (`[DeliveryAddress](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Order#DeliveryAddress)`)` Required. The delivery address to validate.  
  
## OrderStatusRequest

This type has no fields.

A request to get the order status.

## UpdatedOrderState

Event returned by the agent representing an update to the order state.

JSON representation  
---  
      
    
    {
      "order": {
        object ([Order](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Order))
      },
      "changed": boolean,
      "status": enum ([OrderStateUpdateStatus](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#OrderStateUpdateStatus)),
      "detailedMessage": string
    }  
  
Fields  
---  
`order` |  `object (`[Order](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Order)`)` The updated state of the Order associated with this session.  
`changed` |  `boolean` Output only. Whether the order state has updates.  
`status` |  `enum (`[OrderStateUpdateStatus](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#OrderStateUpdateStatus)`)` Output only. Status of the order state update.  
`detailedMessage` |  `string` Output only. Detailed message if the update failed.  
  
## OrderStateUpdateStatus

Status of the order state update.

Enums  
---  
`ORDER_STATE_UPDATE_STATUS_UNSPECIFIED` | Unspecified status.  
`SUCCEEDED` | The update succeeded.  
`FAILED` | The update failed.  
  
## AgentText

The text response from the agent.

JSON representation  
---  
      
    
    {
      "text": string
    }  
  
Fields  
---  
`text` |  `string` The text response from the agent.  
  
## SentimentMeasurement

The realtime sentiment score measured for this turn.

JSON representation  
---  
      
    
    {
      "score": number,
      "magnitude": number
    }  
  
Fields  
---  
`score` |  `number` Optional. Sentiment score between -1.0 (negative sentiment) and 1.0 (positive sentiment).  
`magnitude` |  `number` Optional. Magnitude of sentiment, regardless of score.  
  
## TurnCompleted

This type has no fields.

Indicates that the Food AI agent has detected the end of the current conversation turn and will provide no further output for this turn.

## EndSession

Indicates the agent has terminated the session, due to either successful completion (e.g. user says "Good bye!" ) or an agent escalation.

JSON representation  
---  
      
    
    {
      "type": enum ([EndType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#EndType)),
      "reason": string,
      "posResponse": string,
      "agentResponse": string,
      "storeSchedule": {
        object ([Schedule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Schedule))
      }
    }  
  
Fields  
---  
`type` |  `enum (`[EndType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/BidiProcessOrderResponse#EndType)`)` The type of end session event.  
`reason` |  `string` The reason for ending the session.  
`posResponse` |  `string` Optional. The POS response from checking in the order (optional). This is an opaque string payload representing the POS transaction status.  
`agentResponse` |  `string` Optional. The final agent response message to be spoken/displayed to the user (optional).  
`storeSchedule` |  `object (`[Schedule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Schedule)`)` Optional. The store schedule. This is only set when the end type is STORE_CLOSED.  
  
## EndType

Type of end session event.

Enums  
---  
`END_TYPE_UNSPECIFIED` | The end type is not specified.  
`DRIVE_OFF` | The customer drove off.  
`AGENT_ESCALATION` | The agent escalated the session to a human agent.  
`CREW_INTERJECTION` | A crew member interjected in the session.  
`ORDER_COMPLETED` | Order was successfully completed and no further action is needed.  
`PAYMENT_FLOW_SUCCESS` | The payment flow was successful and no further action is needed.  
`PAYMENT_FLOW_FAILURE` | The payment flow failed.  
`CLIENT_ESCALATION` | The client escalated the session to a human agent.  
`CALLER_HANGUP` | The customer hung up the call prematurely.  
`REQUESTED_CHECKOUT` | The customer requested to check out.  
`REQUESTED_ORDER_STATUS` | The customer asked about their order status.  
`STORE_CLOSED` | The store is closed.  
  
## DiagnosticInfo

DiagnosticInfo provides strongly typed execution timing and latency metrics for a conversational turn.

JSON representation  
---  
      
    
    {
      "speechStartOffset": string,
      "speechEndOffset": string,
      "perceivedLatency": string
    }  
  
Fields  
---  
`speechStartOffset` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The duration relative to the start of the audio stream when user speech began.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`speechEndOffset` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The duration relative to the start of the audio stream when user speech ended.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`perceivedLatency` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Perceived latency for the completed turn, measured from acoustic end of speech to the first synthesized audio packet dispatched to the client. Includes the 200ms VAD silence confirmation window.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 

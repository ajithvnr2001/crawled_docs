---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/EventInput/
title: EventInput \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:39:42.810464+00:00
---

# EventInput  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/EventInput/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  EventInput Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * DriveOffEvent
    * JSON representation
  * CrewInterjectionEvent
    * JSON representation
  * OrderStateUpdateEvent
    * JSON representation
  * ClientEscalationEvent
    * JSON representation
  * CustomizedInputEvent
    * JSON representation
  * CallerHangupEvent
  * PosErrorEvent
    * JSON representation
  * EndSessionEvent
    * JSON representation
  * Reason
  * StoreChangeEvent



The event input from the client. This is used to trigger specific events within the agent.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "driveOffEvent": {
        object ([DriveOffEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/EventInput#DriveOffEvent))
      },
      "crewInterjectionEvent": {
        object ([CrewInterjectionEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/EventInput#CrewInterjectionEvent))
      },
      "updateOrderStateEvent": {
        object ([OrderStateUpdateEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/EventInput#OrderStateUpdateEvent))
      },
      "clientEscalationEvent": {
        object ([ClientEscalationEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/EventInput#ClientEscalationEvent))
      },
      "customizedInputEvent": {
        object ([CustomizedInputEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/EventInput#CustomizedInputEvent))
      },
      "callerHangupEvent": {
        object ([CallerHangupEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/EventInput#CallerHangupEvent))
      },
      "posErrorInput": {
        object ([PosErrorEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/EventInput#PosErrorEvent))
      },
      "endSessionEvent": {
        object ([EndSessionEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/EventInput#EndSessionEvent))
      },
      "storeChangeEvent": {
        object ([StoreChangeEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/EventInput#StoreChangeEvent))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Next ID: 12 The event to trigger. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`driveOffEvent` |  `object (`[DriveOffEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/EventInput#DriveOffEvent)`)` The drive off event.  
`crewInterjectionEvent` |  `object (`[CrewInterjectionEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/EventInput#CrewInterjectionEvent)`)` The crew interjection event.  
`updateOrderStateEvent` |  `object (`[OrderStateUpdateEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/EventInput#OrderStateUpdateEvent)`)` A client-side update to the order state.  
`clientEscalationEvent` |  `object (`[ClientEscalationEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/EventInput#ClientEscalationEvent)`)` A client-side escalation event.  
`customizedInputEvent` |  `object (`[CustomizedInputEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/EventInput#CustomizedInputEvent)`)` A customized input event.  
`callerHangupEvent` |  `object (`[CallerHangupEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/EventInput#CallerHangupEvent)`)` Optional. A caller hangup event.  
`posErrorInput` |  `object (`[PosErrorEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/EventInput#PosErrorEvent)`)` Optional. A POS error event.  
`endSessionEvent` |  `object (`[EndSessionEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/EventInput#EndSessionEvent)`)` Optional. A client-initiated end session event.  
`storeChangeEvent` |  `object (`[StoreChangeEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/EventInput#StoreChangeEvent)`)` Optional. The store change event.  
End of mutually exclusive fields.  
  
## DriveOffEvent

The drive off event. This indicates the customer drove off. Session will be closed after this event.

JSON representation  
---  
      
    
    {
      "reason": string
    }  
  
Fields  
---  
`reason` |  `string` Optional. The reason for drive off e.g. "order completed", "unexpected driveoff".  
  
## CrewInterjectionEvent

The crew interjection event. This indicates a crew member interjected in the session. Session will be closed after this event.

JSON representation  
---  
      
    
    {
      "mode": string
    }  
  
Fields  
---  
`mode` |  `string` Optional. The mode in which the crew member interjected, e.g. "headset", "pos".  
  
## OrderStateUpdateEvent

The update order state request. This event should be sent when the order is updated on the client side, e.g. when an item is added or removed via a traditional touch interface.

JSON representation  
---  
      
    
    {
      "order": {
        object ([Order](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order))
      }
    }  
  
Fields  
---  
`order` |  `object (`[Order](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Order)`)` Required. The updated state of the Order associated with this session.  
  
## ClientEscalationEvent

Indicates the client is escalating the session to a human agent.

JSON representation  
---  
      
    
    {
      "reason": string
    }  
  
Fields  
---  
`reason` |  `string` Optional. The reason for client escalation e.g. "payment-declined", "pos-error", "integration-error" etc.  
  
## CustomizedInputEvent

This filed enables a Food AI client to send a customized event to the agent. By default, it is a no-op. Please contact the customer support to enable this feature.

JSON representation  
---  
      
    
    {
      "input": {
        object
      }
    }  
  
Fields  
---  
`input` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Required. Input from the client to the agent.  
  
## CallerHangupEvent

This type has no fields.

Indicates the customer hung up the call prematurely (e.g., AI aversion).

## PosErrorEvent

Point-of-Sale (POS) specific failures.

JSON representation  
---  
      
    
    {
      "errorMessages": [
        string
      ],
      "affectedItemUids": [
        string
      ],
      "affectedExternalIds": [
        string
      ],
      "metadata": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`errorMessages[]` |  `string` Optional. A list of human-readable descriptions of the errors. Multiple error messages can be provided if multiple issues occur simultaneously (e.g., multiple items are out of stock) or to provide a more detailed breakdown of a single complex failure. These messages may be used by the agent to inform the customer or for logging purposes.  
`affectedItemUids[]` |  `string` Optional. Unique item UIDs generated by the Food Ordering AI Agent that caused the error. Corresponds to `UpdatedOrderState.OrderItem.uid`.  
`affectedExternalIds[]` |  `string` Optional. List of external IDs (from the Menu) that caused the error. Should be equal to the actual representatives in the POS, which are usually under integration attributes in menu.proto (e.g., in `ItemIntegrationAttributes` or `ModifierIntegrationAttributes`).  
`metadata` |  `map (key: string, value: string)` Optional. Free-form metadata for debugging or brand-specific signaling. Can be used to pass brand-specific error codes or categories (e.g., {"BRAND_ERROR_CODE": "OUT_OF_STOCK"}).An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## EndSessionEvent

Indicates the client is explicitly requesting to end the session (for example, the customer tapped a "Checkout" or "Done" button on a touch interface, rather than the agent detecting the end of the conversation). The session will be closed after this event.

JSON representation  
---  
      
    
    {
      "reason": enum ([Reason](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/EventInput#Reason))
    }  
  
Fields  
---  
`reason` |  `enum (`[Reason](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/EventInput#Reason)`)` Optional. The reason the client is ending the session.  
  
## Reason

The reason the client is ending the session.

Enums  
---  
`REASON_UNSPECIFIED` | The reason is unspecified. The session is ended as a generic client-initiated request.  
`CHECKOUT` | The customer proceeded to checkout / payment.  
`CHECKOUT_COMPLETED` | The checkout is completed.  
  
## StoreChangeEvent

This type has no fields.

The store change event. This indicates the client selected or switched to a different store.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 

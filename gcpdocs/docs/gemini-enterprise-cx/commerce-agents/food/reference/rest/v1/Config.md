---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Config/
title: Config \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:39:23.795660+00:00
---

# Config  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  Config Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
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
      "featureGate": {
        object ([FeatureGate](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Config#FeatureGate))
      },
      "clientAppInfo": {
        object ([ClientAppInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Config#ClientAppInfo))
      },
      "mode": enum ([SessionMode](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Config#SessionMode)),
      "channelType": enum ([ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/ChannelType)),
      "enableListenOnlyDualChannel": boolean,
      "testSessionStartTime": string,
      "fulfillmentMethod": enum ([FulfillmentMethod](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/FulfillmentMethod)),
      "clientEnv": string
    }  
  
Fields  
---  
`session` |  `string` Required. The session for the order. Format: `projects/{project}/locations/{location}/sessions/{session}`  
`store` |  `string` Required. The store the order is being placed for. Format: `projects/{project}/locations/{location}/brands/{brand}/stores/{store}`  
`laneId` |  `string` Optional. The id of a specifc drive through lane.  
`enableEchoCancellation` |  `boolean` Optional. Whether to enable echo cancellation for the session. If enabled, the client should provide the customerAudio and crewAudio in the AudioInput.  
`daypartId` |  `string` Optional. Daypart of the food menu, including breakfast, lunch, dinner, etc. This is used to determine the menu to use for the order.  
`featureGate` |  `object (`[FeatureGate](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Config#FeatureGate)`)` Optional. The feature gates for the session. This is used to enable or disable features for the session.  
`clientAppInfo` |  `object (`[ClientAppInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Config#ClientAppInfo)`)` Optional. The information about the client application and device environment.  
`mode` |  `enum (`[SessionMode](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Config#SessionMode)`)` Optional. The mode of the session.  
`channelType` |  `enum (`[ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/ChannelType)`)` Optional. The type of channel used for agent communication.  
`enableListenOnlyDualChannel` |  `boolean` Optional. Whether to enable listen-only dual channel for the session. If enabled, the client should provide the customerAudio and crewAudio in the AudioInput.  
`testSessionStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The start time of the session, used for testing or evaluation purposes.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`fulfillmentMethod` |  `enum (`[FulfillmentMethod](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/FulfillmentMethod)`)` Optional. The fulfillment method for the session.  
`clientEnv` |  `string` Optional. The environment on the client side (e.g., "qa", "uat", "preprod").  
  
## FeatureGate

The feature gates for the session. This is used to enable or disable features for the session.

JSON representation  
---  
      
    
    {
      "menuResponseEnabled": boolean,
      "updatedOrderStateEnabled": boolean,
      "enableOrderStatusRetrieval": boolean,
      "enableClientEscalationAudio": boolean
    }  
  
Fields  
---  
`menuResponseEnabled` |  `boolean` Optional. Returns the menu data to the client in BidiProcessOrderResponse if set.  
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

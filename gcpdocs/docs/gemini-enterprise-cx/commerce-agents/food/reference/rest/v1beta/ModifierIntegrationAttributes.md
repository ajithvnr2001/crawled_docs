---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ModifierIntegrationAttributes/
title: ModifierIntegrationAttributes \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T06:00:15.787069+00:00
---

# ModifierIntegrationAttributes  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ModifierIntegrationAttributes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  ModifierIntegrationAttributes Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ToastModifierIntegrationAttributes
    * JSON representation



Metadata associated with a modifier used for downstream integrations.

JSON representation  
---  
      
    
    {
      "customIntegrationAttributes": {
        object
      },
      "toastAttributes": {
        object ([ToastModifierIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ModifierIntegrationAttributes#ToastModifierIntegrationAttributes))
      },
      "externalModifierId": string
    }  
  
Fields  
---  
`customIntegrationAttributes` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Arbitrary metadata to be associated with an entity, used to build downstream integrations, i.e. identifiers or schema information for constructing an order for submission to a third-party point of sale API.  
`toastAttributes` |  `object (`[ToastModifierIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ModifierIntegrationAttributes#ToastModifierIntegrationAttributes)`)` Optional. Represents metadata associated with this modifier used for Toast integration. If Toast integration isn't enabled for the store, this field is ignored.  
`externalModifierId` |  `string` Optional. The external modifier ID.  
  
## ToastModifierIntegrationAttributes

Represents attributes for a Modifier from a Toast menu.

JSON representation  
---  
      
    
    {
      "guid": string,
      "isPreModifier": boolean
    }  
  
Fields  
---  
`guid` |  `string` Optional. Represents the modifier option guid of the item in Toast's menu.  
`isPreModifier` |  `boolean` Optional. If true, this modifier represents a Toast PreModifier.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 

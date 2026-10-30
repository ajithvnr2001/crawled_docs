---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/RemediationAction/
title: RemediationAction \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:38:35.148487+00:00
---

# RemediationAction  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/RemediationAction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  RemediationAction Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * RenamePayload
    * JSON representation
  * UpdateCategoryPayload
    * JSON representation
  * ActionType



A structured action for remediation.

JSON representation  
---  
      
    
    {
      "actionType": enum ([ActionType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/RemediationAction#ActionType)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "renamePayload": {
        object ([RenamePayload](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/RemediationAction#RenamePayload))
      },
      "updateCategoryPayload": {
        object ([UpdateCategoryPayload](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/RemediationAction#UpdateCategoryPayload))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`actionType` |  `enum (`[ActionType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/RemediationAction#ActionType)`)` Required. The specific operation to execute.  
Payload containing the specific data required to execute the chosen action. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`renamePayload` |  `object (`[RenamePayload](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/RemediationAction#RenamePayload)`)` The replacement display name to use when the action type is RENAME_ENTITY.  
`updateCategoryPayload` |  `object (`[UpdateCategoryPayload](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/RemediationAction#UpdateCategoryPayload)`)` The target hierarchical category to use when the action type is UPDATE_CATEGORY.  
End of mutually exclusive fields.  
  
## RenamePayload

Payload containing parameters for renaming a menu entity.

JSON representation  
---  
      
    
    {
      "displayName": string
    }  
  
Fields  
---  
`displayName` |  `string` Optional. The replacement display name to use for the target entity.  
  
## UpdateCategoryPayload

Payload containing parameters for updating the hierarchical category of a menu entity.

JSON representation  
---  
      
    
    {
      "hierarchicalCategory": string
    }  
  
Fields  
---  
`hierarchicalCategory` |  `string` Optional. The new hierarchical category path to assign to the target entity.  
  
## ActionType

Defines the specific operation to execute against the menu ingestion pipeline.

Enums  
---  
`ACTION_TYPE_UNSPECIFIED` | Unspecified action type.  
`DISABLE_ITEM` | Disables the item entirely so customers cannot order it.  
`SET_NON_A_LA_CARTE` | Restricts the item from being sold individually while preserving modifier behavior.  
`RENAME_ENTITY` | Renames the entity to resolve ambiguous naming.  
`UPDATE_CATEGORY` | Moves the item into a new, correct category.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 

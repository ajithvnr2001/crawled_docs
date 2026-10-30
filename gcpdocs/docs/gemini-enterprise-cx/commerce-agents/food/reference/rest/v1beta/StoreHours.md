---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/StoreHours/
title: StoreHours \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:38:58.170136+00:00
---

# StoreHours  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/StoreHours/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  StoreHours Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The operating hours of the store.

JSON representation  
---  
      
    
    {
      "fulfillmentMethod": enum ([FulfillmentMethod](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/FulfillmentMethod)),
      "schedules": [
        {
          object ([Schedule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Schedule))
        }
      ]
    }  
  
Fields  
---  
`fulfillmentMethod` |  `enum (`[FulfillmentMethod](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/FulfillmentMethod)`)` Optional. The fulfillment method of the store hours, for instance "PICKUP", "DELIVERY", etc. If unspecified, the store hours are assumed to be applicable to all fulfillment methods.  
`schedules[]` |  `object (`[Schedule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Schedule)`)` Optional. The operating hours for the store for the specified fulfillmentMethod. The store is open when any schedule with `timeRanges` is active. A schedule without `timeRanges` lists days on which the store does not open; it never makes the store open and does not override other schedules.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 

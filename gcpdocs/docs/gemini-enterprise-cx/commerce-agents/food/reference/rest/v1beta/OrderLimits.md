---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/OrderLimits/
title: OrderLimits \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:38:22.840425+00:00
---

# OrderLimits  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/OrderLimits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  OrderLimits Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Limits applied to orders, e.g. max items and max order total.

JSON representation  
---  
      
    
    {
      "orderItemLimit": integer,
      "orderValueLimit": {
        object ([Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money))
      }
    }  
  
Fields  
---  
`orderItemLimit` |  `integer` Optional. Max number of items allowed in an order.  
`orderValueLimit` |  `object (`[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money)`)` Optional. Max order total allowed. Currency is hardcoded to USD for now.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 

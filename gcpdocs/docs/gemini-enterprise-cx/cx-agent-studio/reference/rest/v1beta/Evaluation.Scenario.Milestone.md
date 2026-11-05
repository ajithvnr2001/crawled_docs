---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Evaluation.Scenario.Milestone
title: Evaluation.Scenario.Milestone \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T22:27:29.933690+00:00
---

# Evaluation.Scenario.Milestone  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Evaluation.Scenario.Milestone

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Evaluation.Scenario.Milestone Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Represents a single milestone in the scenario. Used to guide the behaviour of the user simulator to follow a protocol. The user simulator executes the milestone sequentially and only proceeds to the next one if the successCriteria of that milestone is achieved.

JSON representation  
---  
      
    
    {
      "goal": string,
      "maxTurnCount": integer,
      "successCriteria": string,
      "protocol": string,
      "staticUtterance": string,
      "event": {
        object ([Event](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Event))
      }
    }  
  
Fields  
---  
`goal` |  `string` Required. The goal of the milestone.  
`maxTurnCount` |  `integer` Optional. The maximum number of turns for this milestone.  
`successCriteria` |  `string` Optional. The success criteria of the milestone.  
`protocol` |  `string` Optional. The guidelines the agent should follow during the conversation.  
`staticUtterance` |  `string` Optional. A static utterance that the simulator will send exactly, instead of dynamically generating user input.  
`event` |  `object (`[Event](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Event)`)` Optional. An event input to send instead of dynamic generation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/AudioInput/
title: AudioInput \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:40:44.340916+00:00
---

# AudioInput  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/AudioInput/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  AudioInput Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The audio input from the client. The input audio may have multiple channels for the customer, crew, etc. These should all be synchronized and in the format specified by the configuration . Audio headers should not be included. By default, the audio should be using 16-bit linear PCM audio encoding and 16000 Hz sample rate. Total bytes from all channels should be less than 25600 bytes.

JSON representation  
---  
      
    
    {
      "customerAudio": string,
      "crewAudio": string
    }  
  
Fields  
---  
`customerAudio` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. Customer audio data.A base64-encoded string.  
`crewAudio` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. Crew audio data. This is an optional audio channel for the crew member in the same lane as the customer, and served as the reference audio for echo cancellation.A base64-encoded string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 

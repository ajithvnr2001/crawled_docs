---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/DtmfInput/
title: DtmfInput \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:38:49.645700+00:00
---

# DtmfInput  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/DtmfInput/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  DtmfInput Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The DTMF (Dual-Tone Multi-Frequency) input from the client.

Represents touch-tone keypad input from telephony or client applications.

  1. Collection & Buffering: Clients may stream single digits in real time as the user presses them, or send multiple digits at once. Food AI Agent buffers incoming digits and resets caller inactivity timers.
  2. Endpointing & Termination: The sequence is finalized when an agent-configured finish digit (default is '#') is encountered, or when an endpointing silence timeout (default is 3 seconds) elapses without new digits. If a finish digit terminates a sequence, it is stripped from the digits passed to the agent unless it was the sole digit entered.
  3. Agent Response: Once finalized, Food AI Agent processes the digits and responds with standard conversational turn output (such as synthesized agent audio, POS tool calls, or text).
  4. Dynamic Control: The agent can dynamically enable or disable DTMF listening, configure the finish digit, or adjust the endpointing timeout per turn based on conversational context (for example, when prompting for a zip code or card number).

JSON representation  
---  
      
    
    {
      "digits": string,
      "finishDigit": string
    }  
  
Fields  
---  
`digits` |  `string` Required. The DTMF digits entered by the user.Supported DTMF characters: '0'-'9', '*', '#', and 'A'-'D'.  
`finishDigit` |  `string` Optional. The finish digit (e.g., '#') that was used to complete the DTMF input, if any. When streaming digits in real time, clients can either send the finish digit as the last character in `digits` or specify it explicitly here.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 

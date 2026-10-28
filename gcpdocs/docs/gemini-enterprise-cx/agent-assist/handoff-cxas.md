---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/handoff-cxas/
title: CX Agent Studio handoff \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T15:19:10.779218+00:00
---

# CX Agent Studio handoff  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/handoff-cxas/

[ Skip to main content ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/handoff-cxas/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/handoff-cxas/)
  * [Deutsch](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/handoff-cxas/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/handoff-cxas/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/handoff-cxas/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/handoff-cxas/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/handoff-cxas/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/handoff-cxas/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/handoff-cxas/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/handoff-cxas/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/handoff-cxas/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/handoff-cxas/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/handoff-cxas/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/ai-and-machine-learning-color.svg) ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [End session](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/handoff-cxas/#end-session)
    * [Supported parameters](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/handoff-cxas/#parameters)
  * [How to handoff](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/handoff-cxas/#how_to_handoff)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)


Send feedback 
#  CX Agent Studio handoff Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [End session](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/handoff-cxas/#end-session)
    * [Supported parameters](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/handoff-cxas/#parameters)
  * [How to handoff](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/handoff-cxas/#how_to_handoff)


Handoff is the process of transferring an end user conversation from a [Customer Experience Agent Studio (CX Agent Studio) agent](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/agent) to a human agent. When you create a conversation profile that uses both Agent Assist features and a CX Agent Studio agent, CX Agent Studio answers incoming voice calls and chat messages. When the end user escalates to a human agent, the CX Agent Studio agent becomes silent and Agent Assist creates a human agent participant so the conversation can continue. This process only works with the [bidirectional API](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/bidi-stream-api).
## End session
The `end_session` [tool](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool/system) contains the information that Gemini Enterprise for Customer Experience needs to successfully transfer an end user conversation from a CX Agent Studio agent to a human agent. The `end_session` tool consists of the following objects that customize your end users' transfer experience.
  * `escalationMessage`: The text of the message that CX Agent Studio delivers to the end user in a voice call or chat.
  * `telephonyTransferCall`: The phone number to transfer a call to and how Gemini Enterprise for CX sends the [SIP signal](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/overview).
  * `liveAgentHandoff`: Whether or not the conversation is transferred to a human agent.


You can use the `endSession` parameter inside the `liveAgentHandoff` object to tell your CX Agent Studio agent to end a voice or chat conversation. The bidirectional API relies on the `endSession` parameter to determine whether or not to terminate a conversation and the default value is `False`. If you're using Agent Assist, don't change the value of `endSession`. With the default value, Gemini Enterprise for CX transfers the conversation from your CX Agent Studio agent to Agent Assist to help the human agent. For example, if an end user says they want to speak to the billing agent, use the `end_session` tool as follows:

```
end_session( reason="Billing issue", session_escalated=True, params={
"escalationMessage": "Transferring your call to a billing agent",
"telephonyTransferCall": { "phoneNumber": "+15552420836", "useOriginatingTrunk": True },
"liveAgentHandoff": { "endSession": False, "key": "value" } } )

```

If you're not using Agent Assist, change the value of `endSession` to `True` to end the conversation in CX Agent Studio.
### Supported parameters
You can use the following parameters within each object of the `end_session` tool.
  * `liveAgentHandoff`: Each parameter is optional.
    * `endSession`: A boolean parameter that initiates session end and call hangup.
    * `sipRefer`: A boolean that specifies if a SIP REFER should be used.
    * `uuiHeaders`: A list of strings with user-to-user information headers.
    * `xHeaders`: A map or object with custom SIP X-headers.
  * `telephonyTransferCall`
    * `phoneNumber`: A string that contains the destination number for the transfer.
    * `sipUri`: A string that contains the SIP URI for the transfer.
    * `useOriginatingTrunk`: A boolean that specifies whether to use the same trunk for the transfer.


## How to handoff
Initiate handoff from a CX Agent Studio agent with a [SIP INVITE](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/deploy/google-telephony-platform#send_a_sip_invite).
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

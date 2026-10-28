---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agent-reason-codes/
title: Virtual agent reason codes \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T01:38:13.873024+00:00
---

# Virtual agent reason codes  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agent-reason-codes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Virtual agent reason codes Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the coded values associated with virtual agent activity: failure, finish, escalation, deflection, error, participant, and status values. Use it to interpret the values that you see in virtual agent reports, in call and chat session metadata, and in Apps API and Manager API responses.

Some of these values belong to code sets that Contact Center AI Platform (CCAI Platform) also uses for human agent activity. Where that is the case, each section indicates which values virtual agent handling produces, and for which channels.

## Call finish reasons

These finish reasons appear on calls that ended during, or because of, virtual agent handling:

Code | Value | Description  
---|---|---  
`virtual_agent_escalation_failed` | 20001 | Escalation from a virtual agent to a human agent failed.  
`va_callback_machine_detected` | 60001 | A virtual agent callback detected an answering machine.  
  
## Transfer fail reasons

This fail reason appears on a transfer that failed during a virtual agent escalation on a call:

Code | Value | Description  
---|---|---  
`va_failure` | 20 | The transfer failed because of a virtual agent failure.  
  
## Chat fail reasons

This fail reason appears on chats that ended because an escalation out of a virtual agent couldn't be completed:

Code | Value | Description  
---|---|---  
`escalation_failed` | 5 | The chat failed because its virtual agent escalation couldn't be routed to a human agent queue.  
  
## Escalation status

An escalation record tracks the hand-off of a call or chat out of virtual agent handling. Its status shows how far that hand-off has progressed. This value appears as `status` on the escalation records returned by the Apps API and the Manager API. It is distinct from the escalation reason, which records why the hand-off happened:

Code | Value | Description  
---|---|---  
`escalating` | 0 | The interaction is being handed to a queue.  
`escalated` | 1 | An agent or another virtual agent has taken the interaction.  
`canceled` | 2 | The escalation ended before anyone took the interaction.  
`deflecting` | 3 | The interaction couldn't be handed to the queue as requested, and no outcome has been recorded yet. Where CCAI Platform offers the end user alternatives, this is the state while that choice is outstanding.  
`deflected` | 4 | A deflection outcome is recorded on the escalation. The escalation deflection value names which one.  
  
## Escalation reasons

These values record why an escalation out of a virtual agent occurred. They appear as `reason` on escalation records, and as the **Escalation Reason** column of the virtual agent deflected escalation reports for calls and chats:

Code | Value | Description  
---|---|---  
`unknown` | 0 | Escalation for an unexpected reason, for example an expired credential.  
`by_end_user_ask` | 1 | The end user selected the escalation option.  
`by_end_user_message` | 2 | Escalation in response to the end user's message.  
`by_virtual_agent` | 3 | Planned transfer by virtual agent design.  
`payload_failure` | 4 | Escalation because of a payload failure.  
`could_not_resume` | 5 | The virtual agent session wasn't resumable after the chat was dismissed.  
`by_human_agent` | 6 | A human agent ended the virtual agent forcefully (task virtual agent).  
`invalid_queue` | 7 | The virtual agent escalated to an invalid queue selection.  
`dismissed` | 8 | Dismissed and escalated (task virtual agent).  
  
## Escalation deflection

An escalation record carries a deflection value identifying whether—and how—the interaction was offered an alternative outcome or redirected elsewhere. The following tables group those values by the condition or workflow that produced them.

The escalation record always stores this value as `deflection`. It reaches the other two surfaces only when CCAI Platform records a deflected escalation for the interaction: it then appears in the `virtual_agent_deflected_escalations` block of the call or chat session metadata, and as the **Deflection Reason** column of the virtual agent deflected escalation report. An escalation that was never deflected, or that is still waiting on the end user's choice, has nothing on either surface. Two recorded outcomes never reach them either: `over_cap_wait`, where the caller stays in the queue, and `ivr_presession_deflection`.

Within the over-capacity, after-hours, and temporary-redirection families, the bare value (`over_cap`, `after_hours`, `temp_redirection`) identifies the condition that CCAI Platform detected when the escalation was created, before any outcome-specific value is recorded. The remaining values in each family name the recorded outcome.

**Warning:** These values apply to escalation records only. Calls and transfers carry their own `deflection` field using a different set of numeric values, so don't read a call or transfer deflection value against these tables.

### No deflection

One value records that no deflection occurred:

Code | Value | Applies to | Description  
---|---|---|---  
`no_deflection` | 0 | Calls, chats | No deflection outcome was recorded for the escalation.  
  
### Over-capacity deflections

These values apply when the target queue was over its capacity threshold:

Code | Value | Applies to | Description  
---|---|---|---  
`over_cap` | 1 | Calls, chats | The queue was over capacity when the escalation was created, and no outcome has been recorded yet.  
`over_cap_email` | 2 | Chats | The end user chose to send an email instead of waiting.  
`over_cap_virtual_agent` | 3 | Chats | The end user chose to keep talking to the virtual agent.  
`over_cap_human_agent` | 4 | Chats | The end user chose to keep waiting for a human agent.  
`over_cap_sip` | 5 | Calls | The call was redirected to a SIP destination.  
`over_cap_extension` | 6 | Calls | The call was redirected to an extension.  
`over_cap_voicemail` | 20 | Calls | The caller was sent to voicemail.  
`over_cap_phone` | 21 | Calls | The call was redirected to another phone number.  
`over_cap_callback` | 22 | Calls | The caller requested a callback.  
`over_cap_wait` | 23 | Calls | The caller chose to keep waiting in the queue.  
`over_cap_message` | 24 | Calls | CCAI Platform played the over-capacity message to the caller.  
`over_cap_queue` | 25 | Calls | The call was redirected to another queue.  
`over_cap_phone_with_extension` | 26 | Calls | The call was redirected to another phone number and extension.  
  
### After-hours deflections

These values apply when the escalation arrived outside the queue's configured operating hours:

Code | Value | Applies to | Description  
---|---|---|---  
`after_hours` | 10 | Calls, chats | The queue was outside its operating hours when the escalation was created, and no outcome has been recorded yet.  
`after_hours_email` | 11 | Chats | The end user chose to send an email.  
`after_hours_virtual_agent` | 12 | Chats | The end user chose to keep talking to the virtual agent.  
`after_hours_voicemail` | 30 | Calls | The caller was sent to voicemail.  
`after_hours_phone` | 31 | Calls | The call was redirected to another phone number.  
`after_hours_message_only` | 32 | Calls | CCAI Platform played the after-hours message and offered no other alternative.  
`after_hours_message` | 33 | Calls | CCAI Platform played the after-hours message.  
`after_hours_queue` | 34 | Calls | The call was redirected to another queue.  
`after_hours_sip` | 35 | Calls | The call was redirected to a SIP destination.  
`after_hours_extension` | 36 | Calls | The call was redirected to an extension.  
`after_hours_phone_with_extension` | 37 | Calls | The call was redirected to another phone number and extension.  
  
### Temporary redirection deflections

These values apply when an administrator had a temporary redirection configured on the queue:

Code | Value | Applies to | Description  
---|---|---|---  
`temp_redirection` | 39 | Calls | A temporary redirection was in effect when the escalation was created, and no outcome-specific value has been recorded yet.  
`temp_redirection_phone` | 40 | Calls | The temporary redirection sent the call to another phone number.  
`temp_redirection_message` | 41 | Calls | The temporary redirection played a message to the caller.  
`temp_redirection_voicemail` | 42 | Calls | The temporary redirection sent the caller to voicemail.  
`temp_redirection_queue` | 43 | Calls | The temporary redirection sent the call to another queue.  
`temp_redirection_sip` | 44 | Calls | The temporary redirection sent the call to a SIP destination.  
`temp_redirection_extension` | 45 | Calls | The temporary redirection sent the call to an extension.  
`temp_redirection_phone_with_extension` | 46 | Calls | The temporary redirection sent the call to another phone number and extension.  
  
### Other deflections

These values record deflections that the virtual agent or the pre-session flow initiated, rather than a queue condition:

Code | Value | Applies to | Description  
---|---|---|---  
`ivr_presession_deflection` | 50 | Calls | The caller was moved to an SMS conversation by pre-session deflection.  
`va_redirection_phone` | 60 | Calls | The virtual agent redirected the call to an external phone number.  
`va_redirection_sip` | 61 | Calls | The virtual agent redirected the call to an external SIP address.  
`va_third_party_phone` | 62 | Calls | The virtual agent invited a third party by phone.  
`va_third_party_sip` | 63 | Calls | The virtual agent invited a third party over SIP.  
  
Third-party invite deflections require the virtual agent third-party invite capability. For more information about implementation, contact your account team or support.

For the deflection and escalation reason fields in the raw deflected escalation datasets, see [Raw data export dictionary](https://docs.cloud.google.com/contact-center/ccai-platform/docs/raw-data-export-dictionary).

For how to escalate a virtual agent chat, record a deflection outcome, and close the chat through the Apps API, see [Escalate from a virtual agent to a human agent](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-platform-api-guide#escalate-to-human).

## Chatbot finish reasons

These values record how a virtual agent session ended. They appear as the **Interaction Outcome** column of the virtual agent detail report:

Code | Value | Description  
---|---|---  
`undefined` | 0 | Undefined finish reason.  
`resolved` | 1 | The virtual agent session resolved successfully.  
`unexpectedly_ended` | 2 | The virtual agent session ended unexpectedly.  
`escalated` | 3 | The virtual agent escalated to a human agent.  
`failed` | 4 | The virtual agent session failed.  
`consumer_ended` | 5 | The end user ended the virtual agent session.  
`timeout` | 6 | The virtual agent session timed out.  
  
**Mapping logic:** CCAI Platform derives the finish reason in this order and stops at the first rule that matches:

  1. A finish reason already set on the session is used as it is.

  2. An unknown end reason becomes `unexpectedly_ended`.

  3. Any deflection becomes `escalated`.

  4. An escalation reason of `unknown` becomes `unexpectedly_ended`.

  5. `by_end_user_ask`, `by_end_user_message`, or `by_virtual_agent` becomes `escalated`.

  6. `payload_failure` or `invalid_queue` becomes `failed`.

  7. All others, including `could_not_resume`, `by_human_agent`, and `dismissed`, become `undefined`.




Because rule 3 precedes rule 6, a deflected escalation is reported as `escalated` regardless of its escalation reason.

## Task virtual agent status

These values track a task virtual agent from the moment it is started to the moment it ends:

Code | Value | Description  
---|---|---  
`initiated` | 0 | The task virtual agent was initiated.  
`in_progress` | 1 | The task virtual agent is in progress.  
`finished` | 2 | The task virtual agent finished successfully.  
`failed` | 3 | The task virtual agent failed.  
`dismissed` | 4 | The task virtual agent was dismissed.  
`cancelled` | 5 | The task virtual agent was cancelled.  
  
**Finish type mapping:**

  * `unknown` or `payload_failure` becomes `failed`.

  * `dismissed` becomes `dismissed`.

  * `by_human_agent` or `cancelled` becomes `cancelled`.

  * All others become `finished`.




## Chatbot server error codes

CCAI Platform returns these codes when a request to the chatbot service fails:

Code | Value | Description  
---|---|---  
`INTERNAL_CODE_NOT_SPECIFIED` | 0 | Internal error code not specified.  
`INTERNAL_SERVER_ERROR` | 1 | Internal server error.  
`REQUEST_INVALID_PARAMS` | 1000 | Invalid request parameters.  
`CHATBOT_CREDENTIAL_INVALID` | 2000 | Chatbot credential invalid.  
`CHATBOT_CREDENTIAL_NOT_FOUND` | 2001 | Chatbot credential not found.  
`CHATBOT_PROJECT_NOT_FOUND` | 3000 | Chatbot project not found.  
`CHATBOT_PROVIDER_UNAVAILABLE` | 4000 | Chatbot provider unavailable.  
`CHATBOT_PROVIDER_EXHAUSTED` | 4001 | Chatbot provider exhausted.  
`CHATBOT_RESOURCE_NOT_FOUND` | 5000 | Chatbot resource not found.  
`CHATBOT_INVALID_CLIENT_REQUEST` | 6000 | Invalid client request.  
  
## VASS (virtual agent speech service) error codes

CCAI Platform returns these codes when a request to the virtual agent speech service fails:

Code | Value | Description  
---|---|---  
`INTERNAL_CODE_NOT_SPECIFIED` | 0 | Internal error code not specified.  
`INTERNAL_SERVER_ERROR` | 1 | Internal server error.  
`REQUEST_INVALID_PARAMS` | 1000 | Invalid request parameters.  
`VASS_CREDENTIAL_INVALID` | 2000 | VASS credential invalid.  
`VASS_CREDENTIAL_NOT_FOUND` | 2001 | VASS credential not found.  
`VASS_PROJECT_NOT_FOUND` | 3000 | VASS project not found.  
`VASS_PROVIDER_UNAVAILABLE` | 4000 | VASS provider unavailable.  
`VASS_PROVIDER_EXHAUSTED` | 4001 | VASS provider exhausted.  
`VASS_RESOURCE_NOT_FOUND` | 5000 | VASS resource not found.  
`VASS_INVALID_CLIENT_REQUEST` | 6000 | Invalid client request.  
  
## Participant types (virtual agent-related)

Two participant type values identify virtual agents, on calls and on chats alike:

Code | Value | Description  
---|---|---  
`virtual_agent` | 3 | Virtual agent participant.  
`task_virtual_agent` | 5 | Task virtual agent participant.  
  
## Chat status (VA-related)

These chat statuses indicate that a virtual agent holds the chat:

Code | Value | Description  
---|---|---  
`va_assigned` | 20 | The chat is assigned to a virtual agent.  
`va_dismissed` | 21 | The chat was dismissed while with a virtual agent.  
  
## Call or chat answered by

This value indicates that a virtual agent, rather than a human agent, answered the call or chat:

Code | Value | Description  
---|---|---  
`answered_by_virtual_agent` | 2 | A virtual agent answered the call or chat.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 

---
url: https://docs.fish.audio/agents/build/system-tools/
title: System Tools for Voice Agents - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-11-24T19:00:07.951852+00:00
---

# System Tools for Voice Agents - Fish Audio

> Source: https://docs.fish.audio/agents/build/system-tools/

## On this page

Back to top

  * Toggle a system tool
  * Hang up call
    * Farewell
    * Questions before hanging up
  * Press keys
    * Turn it on
    * Tell the agent where to go
    * Limitations
  * Transfer call
  * Going further



Tools

# System Tools for Voice Agents

Copy pageCopy page

Built-in agent capabilities like hanging up the call and pressing phone keys, enabled per agent

Copy pageCopy page

System tools are capabilities built into the platform. There is nothing to create or host. Each agent simply enables the ones it needs.

Tool| Key| What it does  
---|---|---  
Hang up call| `hang_up_call`| Lets the agent end the call itself.  
Press keys (Beta)| `press_keys`| On outbound calls, lets the agent press phone keys to get through an automated phone menu.  
  
## Toggle a system tool

  * Console

  * API




Open your agent’s **Tools** page in the Builder. The **System tools** card holds a switch for each tool.

Set the switches under `tools.system_tools` in the agent’s config. A switch is `true` or `false`, except `press_keys`, which is an object with `enabled`. Switches you leave out keep their current value. The change goes to the draft, so [publish](https://docs.fish.audio/agents/deploy/versions-publishing) afterwards.

Request
    
    
    curl --request PATCH "https://api.fish.audio/v1/agent/agents/$AGENT_ID/config" \
      --header "Authorization: Bearer $FISH_API_KEY" \
      --header "Content-Type: application/json" \
      --data '{
        "tools": {
          "system_tools": {
            "hang_up_call": true,
            "press_keys": { "enabled": true }
          }
        }
      }'
    

`GET /v1/agent/agents/$AGENT_ID/config` returns every switch in the same place.

Response
    
    
    {
      "tools": {
        "system_tools": {
          "hang_up_call": true,
          "hang_up_call_farewell_mode": "generated",
          "hang_up_call_farewell_message": "",
          "hang_up_call_refuse_questions": true,
          "press_keys": { "enabled": true }
        }
      }
    }
    

The response has more fields than shown here. See [Configuration](https://docs.fish.audio/agents/build/configuration) for the rest of the config.

## Hang up call

With **Hang up call** on, the agent can end the call itself by calling the built-in `_end_call` tool. The call ends once the agent finishes speaking.

### Farewell

Choose what callers hear before the call ends.

Mode| Behavior  
---|---  
**Generated** (default)| The agent writes a short goodbye into the tool call’s `message`, and the caller hears it.  
**Fixed message**|  The agent ends with the exact text you provide.  
**Off**|  The call ends as soon as the agent finishes its current reply, with no extra goodbye.  
  
In every mode, anything the agent says in the same reply as the `_end_call` call is spoken first. In **Generated** mode, `message` is said only when that reply says nothing, so callers never hear two goodbyes.

  * Console

  * API




On the agent’s **Tools** page, turn on **Hang up call** in the **System tools** card. Pick a mode under **Farewell** below it. For **Fixed message** , type the line in the box that appears.

Set `tools.system_tools.hang_up_call_farewell_mode` to `generated`, `fixed`, or `off`, and put the fixed text in `tools.system_tools.hang_up_call_farewell_message`.

Request
    
    
    curl --request PATCH "https://api.fish.audio/v1/agent/agents/$AGENT_ID/config" \
      --header "Authorization: Bearer $FISH_API_KEY" \
      --header "Content-Type: application/json" \
      --data '{
        "tools": {
          "system_tools": {
            "hang_up_call": true,
            "hang_up_call_farewell_mode": "fixed",
            "hang_up_call_farewell_message": "Thanks for calling Acme. Goodbye!"
          }
        }
      }'
    

The fixed message is up to 1,000 characters and accepts the same `{{placeholders}}` as the system prompt (see [Dynamic variables](https://docs.fish.audio/agents/build/dynamic-variables)). A fixed mode with an empty message falls back to **Generated**.

### Questions before hanging up

Turn on **Don’t hang up on a question** to stop the agent from hanging up on a question. With it on, if the `message` the caller would hear contains a question mark, for example “Is there anything else I can help you with?”, the `_end_call` call fails and the call stays open. The agent asks the question in its reply, waits for the answer, and calls `_end_call` again after that.

  * Console

  * API




On the agent’s **Tools** page, under **Hang up call** , set **Farewell** to **Generated** , then turn on **Don’t hang up on a question**. The switch shows only in **Generated** mode.

Set `tools.system_tools.hang_up_call_refuse_questions` to `true`.

Request
    
    
    curl --request PATCH "https://api.fish.audio/v1/agent/agents/$AGENT_ID/config" \
      --header "Authorization: Bearer $FISH_API_KEY" \
      --header "Content-Type: application/json" \
      --data '{ "tools": { "system_tools": { "hang_up_call_refuse_questions": true } } }'
    

The switch has no effect with a **Fixed message** or **Off**. Agent tests and simulations follow the same setting.

## Press keys

Press keys is in Beta. The instructions the agent gets for it, and when exactly a key goes out, may still be tuned.

Many business numbers are answered by an automated phone menu before a person picks up. With **Press keys** on, the agent can get through that menu on the calls it places. On [outbound calls](https://docs.fish.audio/agents/telephony/outbound-calls) it gets two more tools.

Tool| What the agent does with it  
---|---  
`_press_keys`| Presses keys on the phone keypad, such as a menu option, an extension or an account number.  
`_skip_turn`| Stays silent for a turn and keeps listening, while a menu is still reading its options or a hold message plays.  
  
The agent decides from what it hears. A call to a company’s main line can go like this.

1

A menu answers

“For sales, press 1. For support, press 2.” The agent presses 2 and says nothing.

2

The call is on hold

“Please hold for the next available representative.” The agent stays silent and keeps listening.

3

A person answers

“Support, this is Amy.” The agent talks to Amy as on any other call.

The setting applies to outbound phone calls only. Inbound calls, web and SDK sessions ignore it. To press keys on the call to a transfer destination, see [Pressing keys on a transfer](https://docs.fish.audio/agents/telephony/transfers#pressing-keys-on-a-transfer).

### Turn it on

  * Console

  * API




On the agent’s **Tools** page, turn on **Press keys** in the **System tools** card, then [publish](https://docs.fish.audio/agents/deploy/versions-publishing). Outbound calls run the published version.

Set `tools.system_tools.press_keys.enabled`, then [publish](https://docs.fish.audio/agents/deploy/versions-publishing).
    
    
    curl --request PATCH "https://api.fish.audio/v1/agent/agents/$AGENT_ID/config" \
      --header "Authorization: Bearer $FISH_API_KEY" \
      --header "Content-Type: application/json" \
      --data '{ "tools": { "system_tools": { "press_keys": { "enabled": true } } } }'
    

### Tell the agent where to go

The agent picks keys from the menu it hears and from its system prompt. Say in the prompt who it should reach, and give it every number it may be asked for. The agent only enters numbers that are in its instructions or that the phone system itself reads out. Pass values that change per call as [dynamic variables](https://docs.fish.audio/agents/build/dynamic-variables).
    
    
    You are calling {{clinic_name}} to confirm an appointment for {{patient_name}}.
    If an automated system answers, choose the option for appointments or the
    front desk. If it asks for an extension, enter {{extension}}.
    When a person answers, introduce yourself and say why you are calling.
    If you reach voicemail, leave a short message with the callback number.
    

### Limitations

  * **Imported SIP numbers.** Keys are sent as telephone events (RFC 4733). On an [imported SIP number](https://docs.fish.audio/agents/telephony/byo-sip) they reach the other side only when your SIP provider carries them. Place a test call to a menu to confirm.
  * **Tests.** [Agent tests](https://docs.fish.audio/agents/test/agent-tests), simulations and [preview calls](https://docs.fish.audio/agents/test/preview-calls) do not include the two tools. Test with a real outbound call.



## Transfer call

`_transfer_call` has no switch of its own: it is enabled automatically once the agent has a transfer destination configured, and only on phone sessions (web sessions have no call to transfer). See [Transfers](https://docs.fish.audio/agents/telephony/transfers) for configuring destinations and everything else about transfers.

## Going further

## Tools overview

How webhook, client, and system tools fit together.

## Webhook tools

Call your own HTTP endpoints from a conversation.

## Client tools

Run tool calls inside your own app via the SDK.

## Voice & language

Configure the agent’s voice and speaking language.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/fishaudio/docs/edit/main/agents/build/system-tools.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/agents/build/system-tools)

[Client Tools](https://docs.fish.audio/agents/build/client-tools)[Dynamic Variables](https://docs.fish.audio/agents/build/dynamic-variables)

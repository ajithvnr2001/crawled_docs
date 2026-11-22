---
url: https://docs.fish.audio/agents/build/background-sound-voice-effect/
title: Agent Background Sound & Voice Effect - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-11-22T15:30:42.616380+00:00
---

# Agent Background Sound & Voice Effect - Fish Audio

> Source: https://docs.fish.audio/agents/build/background-sound-voice-effect/

## On this page

Back to top

  * Background sound
    * Pick a sound
    * Volume
    * Use your own clip
    * Recordings
  * Voice effect
  * Going further



Build

# Agent Background Sound & Voice Effect

Copy pageCopy page

Make calls feel more real with an ambience under your agent’s voice and a phone line or intercom sound on web calls

Copy pageCopy page

Two voice settings can make a call with your agent feel much more real to the caller. A real call is never a studio-clean voice over pure silence. Background sound puts a place behind the agent’s voice, and voice effect makes the voice sound like it comes over a real line. Neither changes what your agent says. Both are off by default, and you can use them together.

Setting| What it does| Calls it applies to| Config field  
---|---|---|---  
Background sound| Plays a looping ambience under the agent’s voice, such as an office or a café| Every voice call (web, phone, and WhatsApp)| `voice.background_sound`  
Voice effect| Makes the agent’s voice sound like a phone line or an intercom speaker| Web calls| `voice.effect`  
  
Like every voice setting, a change is saved to the agent’s draft. [Preview calls](https://docs.fish.audio/agents/test/preview-calls) play it right away, and live sessions get it once you [publish](https://docs.fish.audio/agents/deploy/versions-publishing).

## Background sound

The ambience plays for as long as the agent is on the call. It keeps playing while the agent listens or waits for a tool, so a pause in the conversation is not dead silence.

### Pick a sound

  * Console

  * API




On your agent’s **Configuration** page, open **Background sound** in the voice section and pick a sound. Hover over a sound in the list and select its play button to hear it first. Once a sound is picked, a **Volume** slider appears below it.

Set `voice.background_sound` in the agent’s configuration.

API (curl)
    
    
    curl --request PATCH "https://api.fish.audio/v1/agent/agents/$AGENT_ID/config" \
      --header "Authorization: Bearer $FISH_API_KEY" \
      --header "Content-Type: application/json" \
      --data '{
        "voice": {
          "background_sound": {
            "preset": "office",
            "volume": 0.2
          }
        }
      }'
    

`background_sound` is replaced as a whole, so send `preset` and `volume` together. A field you leave out goes back to its default. Send `null` to turn the sound off.

`preset`| Label in the Builder| What you hear  
---|---|---  
`off`| Off| No background sound. This is the default.  
`office`| Office| The room tone of a quiet office, with no voices  
`call_center`| Call center| Overlapping voices on a call center floor  
`restaurant`| Restaurant| A fast-food kitchen heard from a drive-thru, with timer beeps and traffic outside  
`cafe`| Café| The chatter of a busy café  
`city_street`| City street| Traffic passing on a city street  
`phone_line`| Analog phone line| Line hiss with a low mains hum  
`phone_line_digital`| Digital phone line| Line hiss without the hum  
`custom`| Custom upload| Your own clip  
  
### Volume

`volume` runs from `0` (silent) to `1` (the sound at its full level), and the Builder shows it as a percentage. The default is `0.15`, which keeps the ambience soft under the voice.

### Use your own clip

Upload a recording of your own to play instead of a preset.

  * Console

  * API




Pick **Custom upload** in the **Background sound** list, then select **Upload new clip** and choose a file. The clip is selected as soon as the upload finishes.Clips uploaded earlier appear in the clip picker, where you can preview, select, or delete each one.

Upload the file as `multipart/form-data`, in the `file` field.

Upload a clip
    
    
    curl --request POST https://api.fish.audio/v1/agent/background-sounds \
      --header "Authorization: Bearer $FISH_API_KEY" \
      --form "file=@lobby.mp3"
    

Response
    
    
    {
      "_id": "bgs_7ff7207884084c088c290ee7e7a8781e",
      "name": "lobby.mp3",
      "duration_seconds": 20.0,
      "size_bytes": 321068,
      "created_at": "2026-11-19T11:34:41.317602Z"
    }
    

Then select the clip by its `_id`.

Select the clip
    
    
    curl --request PATCH "https://api.fish.audio/v1/agent/agents/$AGENT_ID/config" \
      --header "Authorization: Bearer $FISH_API_KEY" \
      --header "Content-Type: application/json" \
      --data '{
        "voice": {
          "background_sound": {
            "preset": "custom",
            "volume": 0.2,
            "custom_asset_id": "bgs_7ff7207884084c088c290ee7e7a8781e"
          }
        }
      }'
    

`custom_asset_id` is required with the `custom` preset and rejected with any other preset. An id that is not one of your clips is rejected with `422`.

Endpoint| Description  
---|---  
[`GET /v1/agent/background-sounds`](https://docs.fish.audio/api-reference/endpoint/agent/list-background-sounds)| List your clips, newest first  
[`POST /v1/agent/background-sounds`](https://docs.fish.audio/api-reference/endpoint/agent/create-background-sound)| Upload a clip  
[`DELETE /v1/agent/background-sounds/{asset_id}`](https://docs.fish.audio/api-reference/endpoint/agent/delete-background-sound)| Delete a clip  
  
Limit| Value  
---|---  
File formats| MP3, WAV, OGG, M4A  
File size| 10 MB  
Length| 5 minutes  
Clips| 50 per team  
  
  * **The clip loops.** When it reaches its end it starts again from the beginning, so pick a recording whose end runs smoothly into its start.
  * **The clip is converted to mono.**
  * **Some uploads are rejected.** A file over a limit, in another format, or whose content does not match its extension gets a `400`. An upload past the 50 clips gets a `422`.
  * **Deleting does not check which agents use the clip.** An agent that still has it selected plays no background sound from its next session on, and the Builder shows **Unavailable clip** in its picker.



### Recordings

When a session [records audio](https://docs.fish.audio/agents/monitor/conversation-history#what-gets-stored), the background sound is recorded as a track of its own, apart from the agent’s voice. The [recording response](https://docs.fish.audio/agents/monitor/conversation-history#download-recordings) then has two tracks with the role `agent`.

## Voice effect

On a web call the agent’s voice is clean and full-band, cleaner than any phone line. A voice effect shapes it to sound like the line or speaker your agent will really be heard on, which helps when you demo or preview a phone or drive-thru agent in the browser.

`effect`| Label in the Builder| What you hear  
---|---|---  
`none`| Off (clean voice)| The voice as it is. This is the default.  
`phone`| Phone line| A handset on a phone line. The voice is narrowed to the telephone band (300 to 3400 Hz) and carries the slight grain of a phone codec.  
`intercom`| Intercom speaker| A small, overdriven speaker, like a drive-thru order post or a door intercom  
  
  * Console

  * API




On your agent’s **Configuration** page, open **Voice effect** in the voice section and pick an effect.

Set `voice.effect` in the agent’s configuration. Send `none` to turn the effect off.

API (curl)
    
    
    curl --request PATCH "https://api.fish.audio/v1/agent/agents/$AGENT_ID/config" \
      --header "Authorization: Bearer $FISH_API_KEY" \
      --header "Content-Type: application/json" \
      --data '{
        "voice": {
          "effect": "phone"
        }
      }'
    

  * **It applies to web calls only.** Web calls are the ones made from a browser or an app, which covers Preview calls, the widget, and the Web, React, and React Native SDKs. Phone and WhatsApp calls already sound like a call on a line, so they ignore the setting.
  * **It covers everything the agent says** , with any [speech model](https://docs.fish.audio/agents/build/voice-language#text-to-speech-model).
  * **It changes the voice only.** The effect adds no line noise and leaves the background sound as it is. For the hiss of a real line, add the **Analog phone line** or **Digital phone line** background sound.
  * **Recordings carry it.** The agent’s track in a [recording](https://docs.fish.audio/agents/monitor/conversation-history#download-recordings) sounds as the caller heard it.



## Going further

## Voice & language

The voice, speaking language, and speech model.

## Preview calls

Hear the sound and the effect on your draft.

## Versions & publishing

How drafts become the live agent.

## Conversation history

Download the recorded tracks of a session.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/fishaudio/docs/edit/main/agents/build/background-sound-voice-effect.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/agents/build/background-sound-voice-effect)

[Voice & Language](https://docs.fish.audio/agents/build/voice-language)[Time & Timezone](https://docs.fish.audio/agents/build/time-timezone)

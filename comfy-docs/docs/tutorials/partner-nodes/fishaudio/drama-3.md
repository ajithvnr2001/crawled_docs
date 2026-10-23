---
url: https://docs.comfy.org/tutorials/partner-nodes/fishaudio/drama-3/
title: Fish Audio Drama 3: directions, word tags, and templates - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:06.651208+00:00
---

# Fish Audio Drama 3: directions, word tags, and templates - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/fishaudio/drama-3/

## On this page

  * Use Drama 3 in ComfyUI
    * Selecting the model
    * Connecting voices
  * Directing a performance
    * Describe the delivery
    * Add sounds and pauses
    * Direct in any language
    * Change only specific words
    * Switch language mid-line
    * Combine them
  * Available workflows
    * Fish Audio Drama 3: Directed Performance
    * Fish Audio Drama 3: Two-Speaker Dialogue
  * Account and pricing
  * Get started



Fish Audio

# Fish Audio Drama 3: directions, word tags, and templates

Copy pageCopy page

Run Fish Audio Drama 3 in ComfyUI: direct a performance with plain-language directions and paired word tags, then use the ready-made Drama 3 templates.

Copy pageCopy page

Drama 3 is Fish Audio’s newest text-to-speech model, built for voice direction. A whole scene is written as one script, the delivery is described in plain language inside the text, and paired word tags change only the words they wrap. In ComfyUI it runs in the Fish Audio Text to Speech node with `model` set to `drama-3`. For the other Fish Audio models, see [Fish Audio: Text to Speech, Voice Cloning, and Speech to Text](https://docs.comfy.org/tutorials/partner-nodes/fishaudio/fish-audio).

To use the Partner Nodes, you need to ensure that you are logged in properly and using a permitted network environment. Please refer to the [Partner Nodes Overview](https://docs.comfy.org/tutorials/partner-nodes/overview) section of the documentation to understand the specific requirements for using the Partner Nodes.

  * Local users

  * Cloud users




Make sure your ComfyUI is updated.

  * [Download ComfyUI](https://www.comfy.org/download)
  * [Update Guide](https://docs.comfy.org/installation/update_comfyui)

Workflows in this guide can be found in the [Workflow Templates](https://docs.comfy.org/interface/features/template). If you can’t find them in the template, your ComfyUI may be outdated.If nodes are missing when loading a workflow, possible reasons:

  1. You are not using the latest ComfyUI version (Nightly version)
  2. Some nodes failed to import at startup



  * [Cloud](https://cloud.comfy.org) will update after ComfyUI stable release.

So, if you find any core node missing in this document, it might be because the new core nodes have not yet been released in the latest stable version. Please wait for the next stable release.

## 

​

Use Drama 3 in ComfyUI

The Fish Audio partner nodes are available in the node menu under `partner/audio/Fish Audio`, and Drama 3 uses the same ones as the other models: Text to Speech, Speech to Text, Voice Selector, and Instant Voice Clone.

### 

​

Selecting the model

Set `model` to `drama-3` on the Text to Speech node.

### 

​

Connecting voices

The `voice` output of the Voice Selector or the Instant Voice Clone connects to the Text to Speech node. `drama-3` exposes the growable `voices` input with up to 5 slots. With one connected voice, the node passes it internally as `reference_id`. With two or more, the text must mark speakers with `@Voice1`, `@Voice2`, and so on, and every connected voice must appear in the text at least once or the node raises an error.

## 

​

Directing a performance

`drama-3` takes direction from the script itself. A plain-language direction in square brackets shifts the delivery from that point on, and a paired word tag changes only the words it wraps:
    
    
    [calm and inviting] Welcome back to the studio.
    [leans in, conspiratorial] There is one trick nobody tells you about.
    [light, playful] Ready? <whisper>It is all in the timing.</whisper> [bright, back to full voice] And that is the whole secret.
    

### 

​

Describe the delivery

Put a direction in square brackets before the words it applies to, and write it the way you would brief a voice actor: emotion, intent, pacing, or who the character is talking to.
    
    
    [barely holding it together, forcing a smile] I'm fine. Really. Go on without me.
    [professional broadcast tone] And now, the headlines.
    

A direction applies until the next one. `[calm]` at the start of a line holds for the whole line unless another direction replaces it, and several directions in one line shift the delivery within that line.

### 

​

Add sounds and pauses

Write a sound or a pause in brackets at the point where it should happen, such as a sigh, a laugh, or a breath:
    
    
    I'm fine. [shaky breath] Really. [small laugh] Go on without me.
    

### 

​

Direct in any language

Directions do not have to match the language of the script. An English script can be directed in Chinese, and the other way around:
    
    
    [像是在强忍着眼泪，却努力笑着] I'm fine. Really. Go on without me.
    

### 

​

Change only specific words

Wrap words in a paired tag to change the delivery of those words only. The supported tags are `<whisper>`, `<emphasis>`, `<soft>`, `<fast>`, `<slow>`, `<stress>`, and `<forceful>`:
    
    
    It is going to <emphasis>blow</emphasis>.
    I'm fine. Really. <whisper>Go on without me.</whisper>
    

### 

​

Switch language mid-line

Fish Audio lists language tags as experimental.

Wrap a phrase in a language tag to switch language for those words only. This helps in a line that mixes two languages, or when a phrase should be read in another language:
    
    
    She looked at the menu and said <french>Je voudrais une table pour deux, s'il vous plaît.</french> The waiter smiled.
    

### 

​

Combine them

Directions, word tags, and the [phoneme tags](https://docs.comfy.org/tutorials/partner-nodes/fishaudio/prompt-guide#phoneme-control) all work in the same script, including inside a multi-speaker turn:
    
    
    @Voice1 [calm and inviting] Welcome back to the studio.
    @Voice2 [leans in, conspiratorial] There is one trick nobody tells you about.
    @Voice1 [light, playful] Ready? <whisper>It is all in the timing.</whisper> [bright, back to full voice] And that is the whole secret.
    

The emotion, tone, and effect tags in the [prompt guide](https://docs.comfy.org/tutorials/partner-nodes/fishaudio/prompt-guide) belong to the other models. On `drama-3`, use the directions and word tags on this page instead.

## 

​

Available workflows

Two ready-made templates cover Drama 3: a single directed performance and a two-speaker dialogue. Open them from the Template Library in ComfyUI, or run them directly on Comfy Cloud. Both require ComfyUI 0.39.3 or newer.

### 

​

Fish Audio Drama 3: Directed Performance

Act out one script with a single voice. Directions in the `text` field shift the delivery line by line, and `<whisper>...</whisper>` changes a few words without changing the rest of the line. The template starts from the Delia preset voice, and you can swap it in the Voice Selector. ![Fish Audio Drama 3: Directed Performance workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_fishaudio_drama3_directed-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Fish Audio Drama 3: Directed Performance” in Template Library

**Input materials** Upload this file to the matching `LoadAudio` node:

## fish_audio_example.mp3

`LoadAudio` node 11 · `fish_audio_example.mp3`

### 

​

Fish Audio Drama 3: Two-Speaker Dialogue

Generate a whole scene in one pass, with one Voice Selector per speaker and the dialogue tags in the script. The template ships with the Delia and Sheila preset voices:
    
    
    [deep, cinematic narrator] @Voice1 Every night, the city tells a story.
    [soft, close, like a secret] @Voice2 But only one voice ever finishes it.
    [drops to a whisper, then brightens] @Voice1 Fish Audio Drama 3, <whisper>now in ComfyUI</whisper>.
    

![Fish Audio Drama 3: Two-Speaker Dialogue workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_fishaudio_drama3_dialogue-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Fish Audio Drama 3: Two-Speaker Dialogue” in Template Library

**Input materials** Upload this file to the matching `LoadAudio` node:

## fish_audio_example.mp3

`LoadAudio` node 11 · `fish_audio_example.mp3`

## 

​

Account and pricing

The nodes require signing in to a ComfyUI account and are billed per use. Drama 3 costs about 14.30per1Mbytesoftextduringthelaunchoffer,then14.30 per 1M bytes of text during the launch offer, then 14.30per1Mbytesoftextduringthelaunchoffer,then35.75 from November 13, 2026. See [Partner Node pricing](https://docs.comfy.org/tutorials/partner-nodes/pricing) for the credit rates and the offer window.

## 

​

Get started

  1. Update ComfyUI to 0.39.3 or newer
  2. Open one of the Drama 3 templates above, or add the Fish Audio nodes from `partner/audio/Fish Audio`
  3. Select `drama-3` in the Text to Speech node and connect a voice through the Voice Selector or the Instant Voice Clone
  4. Write the script with directions and word tags, then run it



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/fishaudio/drama-3.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/fishaudio/drama-3)

[Fish Audio: Text to Speech, Voice Cloning, and Speech to Text in ComfyUIPrevious](https://docs.comfy.org/tutorials/partner-nodes/fishaudio/fish-audio)[Fish Audio Prompt Guide: writing prompts for Fish Audio TTS in ComfyUINext](https://docs.comfy.org/tutorials/partner-nodes/fishaudio/prompt-guide)

⌘I

[ComfyUI home page![light logo](https://mintcdn.com/dripart/WCFdTagRdhtvk9-o/logo/light.svg?fit=max&auto=format&n=WCFdTagRdhtvk9-o&q=85&s=ec112de87239058f5a931a7e4b594965)![dark logo](https://mintcdn.com/dripart/QzWbjSCBG7w61rR3/logo/dark.svg?fit=max&auto=format&n=QzWbjSCBG7w61rR3&q=85&s=62b4d879fb3aadbd7a468d1539032d6f)](https://docs.comfy.org/)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

Resources

[installation](https://docs.comfy.org/installation/system_requirements)[Tutorials](https://docs.comfy.org/tutorials/basic/text-to-image)[Development](https://docs.comfy.org/development/overview)

Products

[Features](https://www.comfy.org/?utm_source=docs)[Gallery](https://www.comfy.org/gallery?utm_source=docs)[Download](https://www.comfy.org/download?utm_source=docs)

Company

[About](https://www.comfy.org/about?utm_source=docs)[Careers](https://www.comfy.org/careers?utm_source=docs)[Terms of Service](https://www.comfy.org/terms-of-service?utm_source=docs)[Privacy Policy](https://www.comfy.org/privacy-policy?utm_source=docs)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=dripart)

---
url: https://docs.sarvam.ai/creative-cloning-use/
title: Using a Cloned Voice | Sarvam API Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-29T06:33:50.125102+00:00
---

# Using a Cloned Voice | Sarvam API Docs

> Source: https://docs.sarvam.ai/creative-cloning-use/

Skip to navigation

On this page

  * Where to Select It
  * Use the same voice in the API



Scroll to top

[Content Studio](https://docs.sarvam.ai/creative-dubbing)[Instant Voice Cloning](https://docs.sarvam.ai/creative-voice-cloning)

# Using a Cloned Voice

Beta

Ask a question|Copy page|[View as Markdown](https://docs.sarvam.ai/creative-cloning-use.md "View this page as plain text")|More actions

This page is for Content Studio.

Once processing completes, your cloned voice appears under the **My voices** tab in the Voice Library, and as a selectable persona in:

  * Text to Speech’s Cloned voices tab.
  * Dubbing’s **Clone speaker voice** strategy.



Everyone in your workspace sees your cloned voice under **My voices** and on the **Instant Voice Cloning** page. The Text to Speech **Cloned voices** tab lists only voices you created yourself.

Voice cloning works from a single ~10-second recording - one take is enough to generate a usable persona, though a cleaner, clearer reading generally produces more accurate results.

## Where to Select It

[1](https://docs.sarvam.ai/creative-cloning-use#in-text-to-speech)

### In Text to Speech

Open the **Cloned voices** tab and select your voice.

[2](https://docs.sarvam.ai/creative-cloning-use#in-dubbing)

### In Dubbing

Choose **Clone speaker voice** as the speaker strategy, then select the cloned voice from the list.

See [Managing Your Voice Library](https://docs.sarvam.ai/creative-voice-library-manage) for removing clones you no longer need. Only the person who created a clone, an organization owner or admin, or a workspace admin can remove it.

## Use the same voice in the API

Studio and the Instant Voice Cloning API share one voice library per workspace. Everyone in the workspace sees the same cloned voices, and a clone created in either place is available in both. Prefer the [Python and TypeScript SDKs](https://docs.sarvam.ai/api/getting-started/sdks) (`voice_cloning.convert` / `voiceCloning.convert`) for application code.

To call the API with a Studio-created voice:

  1. Open **Voice Library → My voices** (or the Instant Voice Cloning home).
  2. On the clone card, find **Voice ID** (format `svc-…`) and use the copy control.
  3. Pass that value as `voice_id` on `POST /voices/clone`.



Voices you create with `POST /voices/create` also appear under **My voices** for everyone in the same workspace — the person who created one can select it in Text to Speech without recreating it in Studio.

See the [Instant Voice Cloning API overview](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/overview) and [Manage saved voices](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/overview#manage-saved-voices).

Was this page helpful?

YesNo

[Previous](https://docs.sarvam.ai/creative-cloning-create)[Cloning Best PracticesNext](https://docs.sarvam.ai/creative-cloning-best-practices)[Built with](https://buildwithfern.com/?utm_source=others&utm_medium=organic&utm_campaign=fern_indocs_url&utm_content=book_demo&utm_term=docs.sarvam.ai)

  * Getting Started

    * [Overview](https://docs.sarvam.ai/creative/studio-overview)
  * Content Studio

    * [Dubbing (Beta)](https://docs.sarvam.ai/creative-dubbing)

    * [Text to Speech](https://docs.sarvam.ai/creative-text-to-speech)

    * [Voice Library](https://docs.sarvam.ai/creative-voice-library)

    * [Instant Voice CloningBeta](https://docs.sarvam.ai/creative-voice-cloning)
      * [Creating a CloneBeta](https://docs.sarvam.ai/creative-cloning-create)
      * [Using a Cloned VoiceBeta](https://docs.sarvam.ai/creative-cloning-use)
      * [Cloning Best PracticesBeta](https://docs.sarvam.ai/creative-cloning-best-practices)

    * [Speech to Text](https://docs.sarvam.ai/creative-speech-to-text)

  * Resources

    * [Frequently Asked Questions](https://docs.sarvam.ai/creative/resources/faq)
    * [Data retention](https://docs.sarvam.ai/api/platform/data-retention "Data retention")



  * [Overview](https://docs.sarvam.ai/creative/studio-overview)
  * [Dubbing (Beta)](https://docs.sarvam.ai/creative-dubbing)
  * [Creating a Dub](https://docs.sarvam.ai/creative-dubbing-create)
  * [Editing a Dub](https://docs.sarvam.ai/creative-dubbing-edit)
  * [Dubbing Best Practices](https://docs.sarvam.ai/creative-dubbing-best-practices)
  * [Text to Speech](https://docs.sarvam.ai/creative-text-to-speech)
  * [Generating Speech](https://docs.sarvam.ai/creative-tts-generate)
  * [Text to Speech Best Practices](https://docs.sarvam.ai/creative-tts-best-practices)
  * [Voice Library](https://docs.sarvam.ai/creative-voice-library)
  * [Browsing and Selecting Voices](https://docs.sarvam.ai/creative-voice-library-browse)
  * [Managing Your Voice Library](https://docs.sarvam.ai/creative-voice-library-manage)
  * [Instant Voice Cloning](https://docs.sarvam.ai/creative-voice-cloning)
  * [Creating a Clone](https://docs.sarvam.ai/creative-cloning-create)
  * [Using a Cloned Voice](https://docs.sarvam.ai/creative-cloning-use)
  * [Cloning Best Practices](https://docs.sarvam.ai/creative-cloning-best-practices)
  * [Speech to Text](https://docs.sarvam.ai/creative-speech-to-text)
  * [Transcribing a File](https://docs.sarvam.ai/creative-stt-transcribe)
  * [Speech to Text Best Practices](https://docs.sarvam.ai/creative-stt-best-practices)
  * [Frequently Asked Questions](https://docs.sarvam.ai/creative/resources/faq)



  * [Model APIs](https://docs.sarvam.ai/api)
  * [Voice Agents](https://docs.sarvam.ai/voice-agents)
  * [Doc Agents](https://docs.sarvam.ai/docai)
  * [Content Studio](https://docs.sarvam.ai/creative)
  * [Cowork](https://docs.sarvam.ai/cowork)
  * [API Reference](https://docs.sarvam.ai/api-reference)
  * [Changelog](https://docs.sarvam.ai/changelog)



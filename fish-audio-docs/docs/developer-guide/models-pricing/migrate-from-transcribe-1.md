---
url: https://docs.fish.audio/developer-guide/models-pricing/migrate-from-transcribe-1/
title: Migrate from transcribe-1 - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-10-29T14:32:54.411358+00:00
---

# Migrate from transcribe-1 - Fish Audio

> Source: https://docs.fish.audio/developer-guide/models-pricing/migrate-from-transcribe-1/

## On this page

Back to top

  * What is changing
  * What happens if you do nothing
  * Migrate to transcribe-1-pro
    * Send the model header
    * Keep plain transcripts, if you need them
    * If you use a compatible endpoint
    * Check your error handling
  * Support



Models & Pricing

# Migrate from transcribe-1

Copy pageCopy page

transcribe-1 will be retired on December 31, 2026. Move your speech-to-text requests from transcribe-1 to transcribe-1-pro.

Copy pageCopy page

This guide is for you if your speech-to-text requests are served by `transcribe-1`. That includes requests you did not explicitly send to `transcribe-1`:

  * `POST /v1/asr` requests with no `model` header, or with a value that is not an exact, lowercase match, such as `Transcribe-1-Pro`.
  * The Python and JavaScript SDKs, when you don’t set the `model` header.
  * The OpenAI-, Groq-, and OpenRouter-compatible transcription endpoints, with `fish-audio/transcribe-1` or an alias such as `whisper-1`, `gpt-4o-transcribe`, or `whisper-large-v3`.
  * The ElevenLabs-compatible speech-to-text endpoint, which ignores `model_id`.
  * OpenAI Realtime-compatible transcription sessions opened with `?intent=transcription` and no `model`, or with `fish-audio/transcribe-1`.



## 

​

What is changing

`transcribe-1` is deprecated and will be retired on December 31, 2026. After that date, every request that `transcribe-1` serves today is served by `transcribe-1-pro`. Requests keep working, and no error is returned. We recommend that you switch to `transcribe-1-pro` before then, so you can test your transcripts on your own schedule.

## 

​

What happens if you do nothing

After December 31, 2026, your requests are served by `transcribe-1-pro` and billed as `transcribe-1-pro`. Both models cost $0.36 / audio hour, so your cost does not change. See [Pricing & Rate Limits](https://docs.fish.audio/developer-guide/models-pricing/pricing-and-rate-limits). Your transcripts can still change, because `transcribe-1-pro` returns more than `transcribe-1` by default:

  * `text` can include speaker markers such as `<|speaker:0|>` when more than one person speaks.
  * `text` can include emotion and vocal-event cues such as `[laughter]`.
  * With timestamps requested, the response also includes `speaker_turns`.
  * Error bodies add `code` and `request_id` to `status` and `message`.

The steps below cover each of these changes.

## 

​

Migrate to transcribe-1-pro

### 

​

Send the `model` header

Select the model with the `model` HTTP header, and send `model: transcribe-1-pro`, in lowercase, with every request. `model` is not a form or body field.

curl

Python

JavaScript
    
    
    curl --request POST https://api.fish.audio/v1/asr \
      --header "Authorization: Bearer $FISH_API_KEY" \
      --header "model: transcribe-1-pro" \
      --form audio=@speech.wav
    
    
    
    from fishaudio import FishAudio
    from fishaudio.core import RequestOptions
    
    client = FishAudio()  # reads FISH_API_KEY
    
    with open("speech.wav", "rb") as f:
        result = client.asr.transcribe(
            audio=f.read(),
            request_options=RequestOptions(
                additional_headers={"model": "transcribe-1-pro"}
            ),
        )
    
    print(result.text)
    
    
    
    import { FishAudioClient } from "fish-audio";
    import { readFile } from "fs/promises";
    
    const client = new FishAudioClient({ apiKey: process.env.FISH_API_KEY });
    
    const result = await client.speechToText.convert(
      { audio: new File([await readFile("speech.wav")], "speech.wav") },
      { headers: { model: "transcribe-1-pro" } }
    );
    console.log(result.text);
    

### 

​

Keep plain transcripts, if you need them

If your code expects `text` without speaker markers or event cues, send `diarize=false` and `tag_audio_events=false`:
    
    
    curl --request POST https://api.fish.audio/v1/asr \
      --header "Authorization: Bearer $FISH_API_KEY" \
      --header "model: transcribe-1-pro" \
      --form audio=@speech.wav \
      --form diarize=false \
      --form tag_audio_events=false
    

The Python and JavaScript SDKs can’t send `diarize` or `tag_audio_events`. If you need plain transcripts, call `POST /v1/asr` directly, as above, or remove the markers and cues from `text` in your code. To use the speaker markers instead, see [Multi-speaker conversations](https://docs.fish.audio/features/speech-to-text#multi-speaker-conversations) and [Emotion and vocal-event cues](https://docs.fish.audio/features/speech-to-text#emotion-and-vocal-event-cues).

### 

​

If you use a compatible endpoint

The OpenAI-, Groq-, OpenRouter-, and ElevenLabs-compatible endpoints, and OpenAI Realtime-compatible transcription sessions, keep working after December 31, 2026, and their requests are served by `transcribe-1-pro`. You don’t need to change the model name you send. These endpoints don’t accept `diarize` or `tag_audio_events`. If your application needs plain transcripts, or you want to control speaker markers and event cues, move to the native [Speech to Text API](https://docs.fish.audio/features/speech-to-text) with `model: transcribe-1-pro`, and test before December 31, 2026.

### 

​

Check your error handling

`transcribe-1-pro` errors are JSON with `status`, `message`, `code`, and `request_id`. Code that reads only `status` and `message` keeps working; to branch on the cause, use `code`. See [Errors](https://docs.fish.audio/features/speech-to-text#errors).

## 

​

Support

Need help? Check out these resources:

  * [API Reference](https://docs.fish.audio/api-reference/introduction) \- Complete API documentation
  * [Create a Voice Clone](https://docs.fish.audio/api-reference/endpoint/model/create-model) \- Create a voice clone model
  * [Generate Speech](https://docs.fish.audio/api-reference/endpoint/openapi-v1/text-to-speech) \- Generate realistic speech
  * [Real-time Streaming](https://docs.fish.audio/features/realtime-streaming) \- WebSocket for real-time streaming
  * [Discord Community](https://discord.com/invite/dF9Db2Tt3Y) \- Get help from the community
  * [Support Email](mailto:support@fish.audio) \- Contact our support team



Was this page helpful?

YesNo

[Suggest edits](https://github.com/fishaudio/docs/edit/main/developer-guide/models-pricing/migrate-from-transcribe-1.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/developer-guide/models-pricing/migrate-from-transcribe-1)

[Migrate from S1](https://docs.fish.audio/developer-guide/models-pricing/migrate-from-s1)[Pricing & Rate Limits](https://docs.fish.audio/developer-guide/models-pricing/pricing-and-rate-limits)

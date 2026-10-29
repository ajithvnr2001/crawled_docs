---
url: https://docs.fish.audio/developer-guide/sdk-guide/quickstart/
title: SDK Quickstart - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-10-29T14:32:55.635083+00:00
---

# SDK Quickstart - Fish Audio

> Source: https://docs.fish.audio/developer-guide/sdk-guide/quickstart/

## On this page

Back to top

  * 1\. Install
  * 2\. Authenticate
  * 3\. Generate your first audio
  * Next steps



Set Up the SDK

# SDK Quickstart

Copy pageCopy page

Install a Fish Audio SDK, authenticate, and generate your first audio in under a minute

Copy pageCopy page

The fastest path from zero to playable audio with the official Fish Audio SDKs. By the end you’ll have a script that turns text into an MP3.

The Python SDK is the recommended starting point and is fully covered below. The JavaScript SDK is in early release. See the [JavaScript SDK guide](https://docs.fish.audio/api-reference/sdk/javascript/api-reference) for its current surface.

## 

​

1\. Install

Python

JavaScript
    
    
    pip install fish-audio-sdk
    
    # optional: local audio playback (needs ffmpeg)
    pip install "fish-audio-sdk[utils]"
    
    
    
    npm install fish-audio
    

## 

​

2\. Authenticate

Create a Fish Audio account

Sign up for a free Fish Audio account to get started with our API.

  1. [Sign up on fish.audio](https://fish.audio/app/developers/get-started/?utm_source=docs&utm_medium=prerequisites&utm_content=sign-up)
  2. Fill in your details to create an account, complete steps to verify your account.
  3. Log in to your account and open [Get Started](https://fish.audio/app/developers/get-started/?utm_source=docs&utm_medium=prerequisites&utm_content=developer-dashboard)



Get your API key

Once you have an account, you’ll need an API key to authenticate your requests.

  1. Log in and open [Get Started](https://fish.audio/app/developers/get-started/?utm_source=docs&utm_medium=prerequisites&utm_content=get-api-key)
  2. Click “Get your API key”: the key is created in one click and shown only once
  3. Copy your key and store it securely



Keep your API key secret! Never commit it to version control or share it publicly.

Both SDKs read your key from the `FISH_API_KEY` environment variable:
    
    
    export FISH_API_KEY=your_api_key_here
    

## 

​

3\. Generate your first audio

Python

JavaScript
    
    
    from fishaudio import FishAudio
    from fishaudio.utils import save
    
    client = FishAudio()  # reads FISH_API_KEY
    
    audio = client.tts.convert(text="Hello from Fish Audio!", model="s2.1-pro-free")  # free model
    save(audio, "output.mp3")
    
    
    
    import { FishAudioClient, play } from "fish-audio";
    
    const client = new FishAudioClient(); // reads FISH_API_KEY
    const audio = await client.textToSpeech.convert({ text: "Hello from Fish Audio!" }, "s2.1-pro-free"); // free model
    await play(audio);
    

Run it, and you’ll have `output.mp3` (Python) or local playback (JavaScript).

Want async in Python? Every method mirrors onto `AsyncFishAudio`: `async with AsyncFishAudio() as client: audio = await client.tts.convert(text="...", model="s2.1-pro-free")`.

## 

​

Next steps

## Text-to-Speech

Voices, formats, prosody, and model selection

## Voice Cloning

Instant cloning and persistent voice models

## Realtime WebSocket

Stream LLM tokens to speech as they arrive

## Errors & Retries

Exception types, retries, and timeouts

## Cookbook

Task-focused recipes

## API Reference

Full Python SDK reference

Was this page helpful?

YesNo

[Suggest edits](https://github.com/fishaudio/docs/edit/main/developer-guide/sdk-guide/quickstart.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/developer-guide/sdk-guide/quickstart)

[Authentication](https://docs.fish.audio/developer-guide/sdk-guide/python/authentication)

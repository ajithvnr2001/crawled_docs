---
url: https://docs.fish.audio/developer-guide/getting-started/api-key/
title: Get Your API Key - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-10-29T14:32:55.188174+00:00
---

# Get Your API Key - Fish Audio

> Source: https://docs.fish.audio/developer-guide/getting-started/api-key/

## On this page

Back to top

  * 1\. Create an account and key
  * 2\. Store it as an environment variable
  * 3\. Make your first request



Get Started

# Get Your API Key

Copy pageCopy page

Create a Fish Audio account, generate an API key, and make your first request

Copy pageCopy page

Everything you build with Fish Audio (the API, the Python library, JavaScript) authenticates with a single **API key**. Here’s how to get one and make your first call in a couple of minutes.

## 

​

1\. Create an account and key

1

Sign up

[Sign up on fish.audio](https://fish.audio/app/developers/get-started/?utm_source=docs&utm_medium=api-key-page&utm_content=sign-up), create an account, and verify your email.

2

Open Get Started

Sign in and open [Get Started](https://fish.audio/app/developers/get-started/?utm_source=docs&utm_medium=api-key-page&utm_content=get-api-key).

3

Create a key

Click **Get your API key**. The key is created in one click and shown only once, so **copy it and store it securely**.

Never commit your API key to version control or share it publicly.

## 

​

2\. Store it as an environment variable

The SDKs and the examples throughout these docs read your key from `FISH_API_KEY`:
    
    
    export FISH_API_KEY="your_api_key_here"
    

This keeps the key out of your code and lets you use different keys for development and production.

## 

​

3\. Make your first request

Install the Python SDK first: `pip install fish-audio-sdk`.

Python

API (curl)
    
    
    from fishaudio import FishAudio
    from fishaudio.utils import save
    
    client = FishAudio()  # reads FISH_API_KEY
    audio = client.tts.convert(text="Hello from Fish Audio!", model="s2.1-pro-free")  # free model
    save(audio, "hello.mp3")
    
    
    
    curl --request POST https://api.fish.audio/v1/tts \
      --header "Authorization: Bearer $FISH_API_KEY" \
      --header "Content-Type: application/json" \
      --header "model: s2.1-pro-free" \
      --data '{ "text": "Hello from Fish Audio!", "format": "mp3" }' \
      --output hello.mp3
    

You just generated your first audio. Where to next:

## Text to Speech

Voices, formats, speed, and streaming.

## Quick Start

A fuller first-request walkthrough.

## Voice Cloning

Build a custom voice from your own audio.

## Speech to Text

Transcribe audio with timestamps.

**Building with an AI coding agent?** Install the Fish Audio skill so it writes correct SDK/API code: `npx skills add docs.fish.audio`. See [AI Coding Agents](https://docs.fish.audio/developer-guide/resources/coding-agents).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/fishaudio/docs/edit/main/developer-guide/getting-started/api-key.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/developer-guide/getting-started/api-key)

[Overview](https://docs.fish.audio/overview/capabilities)[Quick Start](https://docs.fish.audio/developer-guide/getting-started/quickstart)

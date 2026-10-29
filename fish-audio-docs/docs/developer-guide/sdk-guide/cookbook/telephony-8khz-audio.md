---
url: https://docs.fish.audio/developer-guide/sdk-guide/cookbook/telephony-8khz-audio/
title: Telephony-grade audio (8 kHz) for IVR and phone - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-10-29T14:32:56.523402+00:00
---

# Telephony-grade audio (8 kHz) for IVR and phone - Fish Audio

> Source: https://docs.fish.audio/developer-guide/sdk-guide/cookbook/telephony-8khz-audio/

## On this page

Back to top

  * Prerequisites
  * Recipe
  * Related



Text to Speech

# Telephony-grade audio (8 kHz) for IVR and phone

Copy pageCopy page

Generate 8 kHz mono WAV/PCM that matches the narrowband sample rate phone networks expect for IVR and call-center playback

Copy pageCopy page

## 

​

Prerequisites

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

## 

​

Recipe

Phone networks carry narrowband audio at 8 kHz. Generating at a higher rate just forces the carrier to downsample on the way through, wasting bandwidth and often softening the result. Synthesize at 8 kHz directly and the bytes are ready to hand to your IVR or SIP stack. Set the sample rate on [`TTSConfig`](https://docs.fish.audio/api-reference/sdk/python/types#ttsconfig-objects) (it is not a top-level argument) and write the WAV to disk. Install the Python SDK first: `pip install fish-audio-sdk`.

Synchronous

Asynchronous

JavaScript
    
    
    from fishaudio import FishAudio
    from fishaudio.types import TTSConfig
    from fishaudio.utils import save
    
    client = FishAudio()
    
    audio = client.tts.convert(
        text="Thank you for calling. Press one to speak with an agent.",
        config=TTSConfig(format="wav", sample_rate=8000),
        model="s2.1-pro-free",
    )
    
    save(audio, "out.wav")
    
    
    
    import asyncio
    from fishaudio import AsyncFishAudio
    from fishaudio.types import TTSConfig
    from fishaudio.utils import save
    
    async def main():
        async with AsyncFishAudio() as client:
            audio = await client.tts.convert(
                text="Thank you for calling. Press one to speak with an agent.",
                config=TTSConfig(format="wav", sample_rate=8000),
                model="s2.1-pro-free",
            )
        save(audio, "out.wav")
    
    asyncio.run(main())
    
    
    
    import { FishAudioClient } from "fish-audio";
    import { writeFile } from "fs/promises";
    
    const client = new FishAudioClient({ apiKey: process.env.FISH_API_KEY });
    
    const stream = await client.textToSpeech.convert(
      {
        text: "Thank you for calling. Press one to speak with an agent.",
        format: "wav",
        sample_rate: 8000,
      },
      "s2.1-pro-free"
    );
    
    const chunks = [];
    for await (const chunk of stream) chunks.push(Buffer.from(chunk));
    
    await writeFile("out.wav", Buffer.concat(chunks));
    

The output is a mono 8 kHz WAV, the standard for G.711 PCM telephony. For a headerless stream to feed straight into a SIP or RTP pipeline, switch to raw PCM with `format="pcm"`; the sample rate stays on `TTSConfig`.
    
    
    audio = client.tts.convert(
        text="Thank you for calling. Press one to speak with an agent.",
        config=TTSConfig(format="pcm", sample_rate=8000),
        model="s2.1-pro-free",
    )
    

API (curl)
    
    
    curl --request POST https://api.fish.audio/v1/tts \
      --header "Authorization: Bearer $FISH_API_KEY" \
      --header "Content-Type: application/json" \
      --header "model: s2.1-pro-free" \
      --data '{ "text": "Thank you for calling. Press one to speak with an agent.", "format": "wav", "sample_rate": 8000 }' \
      --output out.wav
    

8 kHz discards everything above ~4 kHz, so plosives and sibilance lose detail. Keep prompts short and articulate, and reserve higher sample rates (16/24 kHz) for VoIP or recordings that never touch the legacy phone network.

## 

​

Related

  * [Text-to-Speech guide](https://docs.fish.audio/features/text-to-speech)
  * [Stream TTS to a file](https://docs.fish.audio/developer-guide/sdk-guide/cookbook/streaming-to-file)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/fishaudio/docs/edit/main/developer-guide/sdk-guide/cookbook/telephony-8khz-audio.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/developer-guide/sdk-guide/cookbook/telephony-8khz-audio)

[Stream TTS to a file](https://docs.fish.audio/developer-guide/sdk-guide/cookbook/streaming-to-file)[Transcribe audio to SRT/VTT captions](https://docs.fish.audio/developer-guide/sdk-guide/cookbook/transcribe-to-captions)

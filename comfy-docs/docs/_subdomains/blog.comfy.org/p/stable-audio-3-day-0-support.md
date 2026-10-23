---
url: https://blog.comfy.org/p/stable-audio-3-day-0-support/
title: Stable Audio 3.0 Day-0 Support in ComfyUI\uff1aFrom Sound Effects to Longer, More Musical Tracks
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:55.035728+00:00
---

# Stable Audio 3.0 Day-0 Support in ComfyUI：From Sound Effects to Longer, More Musical Tracks

> Source: https://blog.comfy.org/p/stable-audio-3-day-0-support/

# Stable Audio 3.0 Day-0 Support in ComfyUI：From Sound Effects to Longer, More Musical Tracks

### From sound effects to longer, more musical audio

[![Daxiong \(Lin\)'s avatar](https://substackcdn.com/image/fetch/$s_!7zTL!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F08d1a924-8801-4c3b-8e0a-e42ce365f1c0_1077x1077.jpeg)](https://substack.com/@comfyuiwiki)[![JMS's avatar](https://substackcdn.com/image/fetch/$s_!wsK7!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa72bbe5c-9683-452e-9f22-27fb7ffcad1d_500x500.png)](https://substack.com/@jmsvid)

[Daxiong (Lin)](https://substack.com/@comfyuiwiki) and [JMS](https://substack.com/@jmsvid)

May 21, 2026

17

6

1

Share

We’re excited to share that **[Stable Audio 3.0](https://huggingface.co/collections/stabilityai/stable-audio-3)** —Stability AI’s new family of music models built for **artistic experimentation** —is coming to **ComfyUI**. Trained on **fully licensed data** , these models bring **variable-length** generation, **on-device-friendly** small checkpoints, and **stronger musicality** for longer structure—so you can go from quick SFX to extended tracks inside the workflows you already use.

[Download Workflow](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/audio_stable_audio_3_medium_base.json)

## **Model highlights**

  * **Licensed for commercial use** — trained on fully licensed music data.

  * **Flexible clip length** — from quick SFX and short loops to longer tracks (up to about **two minutes** on Small, **six minutes** on Medium).

  * **Lightweight, small models** — run [Small SFX](https://huggingface.co/stabilityai/stable-audio-3-small-sfx) and [Small music](https://huggingface.co/stabilityai/stable-audio-3-small-music) on a **CPU** , no big GPU required.

  * **Medium for longer music** — fuller tracks with stronger structure when you have a **GPU**.




## **Available Models**

  * **Small-SFX** : Sound effects and short ambiance, up to **2:00** ,

  * **Small-Music** : Short music and on-device-friendly loops, up to **2:00**

  * **Medium** : Longer tracks with stronger structure and musicality, up to **~6:20**




**Small** reaches **two minutes** (vs. **11s** / **47s** on Stable Audio Open). **Medium** goes beyond **six minutes** when you need length.

  * [🤗 Stabilityai/stable-audio-3](https://huggingface.co/collections/stabilityai/stable-audio-3)

  * [🤗 Comfy-Org/stable-audio-3](https://huggingface.co/Comfy-Org/stable-audio-3) (for ComfyUI)




## **Examples**

#### **Music**

A short idea for a complete piece (genre, instruments, mood, length).

0:00

-2:30

Audio playback is not supported on your browser. Please upgrade.
    
    
    Lo-fi hip-hop chill track with mellow electric piano, soft vinyl crackle, subtle synth pads, low-pass filtered drums, percussion loops, and soft plucked bass for a relaxed, dreamy vibe. BPM: 75. Length: 150 seconds

0:00

-3:00

Audio playback is not supported on your browser. Please upgrade.
    
    
    Synthwave 80s retro track with arpeggiated synth leads, analog pads, electric bass, punchy electronic drums, gated reverb snares, and atmospheric FX for nostalgic and vibrant energy. BPM: 110. Length: 180 seconds

#### **Instrument**

Single-instrument or small-group clips for production and scoring.

0:00

-0:08

Audio playback is not supported on your browser. Please upgrade.
    
    
    Guitar muted strum loop with tight rhythmic feel. BPM: 100. Length: 8 seconds

0:00

-0:10

Audio playback is not supported on your browser. Please upgrade.
    
    
    Pluck sequence loop with bright resonant tone. BPM: 128. Length: 10 seconds

#### **Sound effects and ambience**

Impacts, textures, environments, and motion sounds for pictures and games.

0:00

-0:08

Audio playback is not supported on your browser. Please upgrade.
    
    
    Footsteps on gravel, steady walking pace, close perspective. Length: 8 seconds

0:00

-0:03

Audio playback is not supported on your browser. Please upgrade.
    
    
    Car speeding past at high velocity, doppler effect, realistic whoosh. Length: 3 seconds

#### **One-shot**

Brief isolated sounds for drums, UI, transitions, and sample libraries.

0:00

-0:03

Audio playback is not supported on your browser. Please upgrade.
    
    
    Bass pluck with jazzy tone and resonant wooden body. Length: 3 seconds

0:00

-0:03

Audio playback is not supported on your browser. Please upgrade.
    
    
    Latin drums, dynamic Latin drums and percussion ensemble featuring authentic rhythmic patterns. Length: 3 seconds

## **  
Get started**

  1. **Update ComfyUI** to v0.22.0 or go to [Comfy Cloud](https://links.comfy.org/4dloFeq)

  2. Go to the left sidebar → Template → Audio category → Choose Stable Audio 3.0 Template

  3. For local users, please follow the note in the workflow to download the models and place them in the correct directory

  4. **Write a prompt** , set the **duration** in seconds, then hit run.




[Stable Audio 3.0 Medium Base Workflow](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/audio_stable_audio_3_medium_base.json)

[Stable Audio 3.0 Medium Workflow](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/audio_stable_audio_3_medium.json)

As always, enjoy creating!

​

17

6

1

Share

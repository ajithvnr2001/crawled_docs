---
url: https://blog.comfy.org/p/ace-step-15-is-now-available-in-comfyui/
title: ACE-Step 1.5 is Now Available in ComfyUI - by Purz
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:45.951547+00:00
---

# ACE-Step 1.5 is Now Available in ComfyUI - by Purz

> Source: https://blog.comfy.org/p/ace-step-15-is-now-available-in-comfyui/

Playback speed

×

Share post

Share post at current time

Share from 0:00

0:00

/

32

17

1

## ACE-Step 1.5 is Now Available in ComfyUI

Commercial-grade music generation on consumer hardware

[![Purz's avatar](https://substackcdn.com/image/fetch/$s_!FaQt!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8b68a786-01d0-4123-bba7-3936c8854e57_400x400.jpeg)](https://substack.com/@purz)

[Purz](https://substack.com/@purz)

Feb 03, 2026

32

17

1

Share

Transcript

We’re excited to share that **ACE-Step 1.5** is now available in ComfyUI! This major update to the open-source music generation model brings commercial-grade quality to your local machine—generating full songs in under 10 seconds on consumer hardware.

[Try on Comfy Cloud](https://links.comfy.org/4kcEhCE)

## What’s New in ACE-Step 1.5

ACE-Step 1.5 introduces a novel hybrid architecture that fundamentally changes how AI generates music. At its core, a Language Model acts as an omni-capable planner, transforming simple user queries into comprehensive song blueprints—scaling from short loops to 10-minute compositions.

  * **Commercial-Grade Quality**  
On standard evaluation metrics, ACE-Step 1.5 achieves quality beyond most commercial music models, scoring 4.72 on musical coherence.

  * **Blazing Fast Generation**  
Generate a full 4-minute song in ~1 second on a RTX 5090, or under 10 seconds on an RTX 3090.

  * **Runs on Consumer Hardware**

  * **50+ Language Support**  
Strict adherence to prompts across 50+ languages, with particularly strong support for English, Chinese, Japanese, Korean, Spanish, German, French, Portuguese, Italian, and Russian.




* * *

## Chain-of-Thought Planning

The model synthesizes metadata, lyrics, and captions via Chain-of-Thought reasoning to guide the diffusion process, resulting in more coherent long-form compositions.

* * *

## LoRA Fine-Tuning

ACE-Step 1.5 supports lightweight personalization through LoRA training. With just a few songs—or a few dozen—you can train a LoRA that captures a specific style.

LoRAs let creators fine-tune toward a specific style using their own music. It learns from your songs and captures your sound. And because you run it locally, you own the LoRA and don’t have to worry about data leakage.

* * *

## How It Works

ACE-Step 1.5 combines several architectural innovations:

  1. **Hybrid LM + DiT Architecture** : A Language Model plans the song structure while a Diffusion Transformer (DiT) handles audio synthesis.

  2. Distribution Matching Distillation: Leverage Z-Image's DMD2 to realise both fast generation (2 secs on an A100) and better quality.

  3. **Intrinsic Reinforcement Learning** : Alignment is achieved through the model’s internal mechanisms, eliminating biases from external reward models.

  4. Self-Learning Tokenizer: The audio tokenizer is learned during DiT training, to close the gap between generation and tokenizing




[Try it on Comfy Cloud!](https://links.comfy.org/4kcEhCE)

* * *

## Coming Soon

ACE-Step 1.5 has a few more tricks up its sleeve. These aren’t yet supported in ComfyUI, but we have no doubt the community will figure it out.

### **Cover**

Give the model any song as input along with a new prompt and lyrics, and it will reimagine the track in a completely different style.

### **Repaint**

Sometimes a generated track is 90% perfect and 10% not quite right. Repaint fixes that. Select a segment, regenerate just that section, and the model stitches it back in while keeping everything else untouched.

* * *

## Vocal Examples

0:00

-0:36

Audio playback is not supported on your browser. Please upgrade.
    
    
    _Neo-Soul: A warm, organic neo-soul track dripping with live instrumentation and effortless groove. A live drummer plays a loose, hip-hop influenced pocket—soft kick drum with lazy swing, snare hits that sit just behind the beat, and brushed hi-hats that breathe and shuffle with human imperfection._

0:00

-0:41

Audio playback is not supported on your browser. Please upgrade.
    
    
    UK Garage: A skippy, energetic UK garage track built on a classic two-step drum pattern with shuffling hi-hats and a punchy, syncopated kick and snare. A warm, wobbling Reese bass line provides the low-end foundation and chopped, pitched-up female vocal samples create the melodic hooks.

0:00

-1:10

Audio playback is not supported on your browser. Please upgrade.
    
    
    K-Pop: A slick, maximalist K-pop track that genre-hops with precision and style. The production shifts seamlessly between sections—a hard-hitting trap-influenced verse with rapid-fire rapping, a softer R&B pre-chorus with breathy vocals and lush harmonies, then an explosive, synth-driven pop chorus with an ear worm hook.

* * *

## Instrumental Examples

0:00

-1:20

Audio playback is not supported on your browser. Please upgrade.
    
    
    Synth-wave: A nostalgic, cinematic ride through neon and chrome. Punchy gated drums with big reverb snare, arpeggiated synth lines running through chorus and delay, warm analog bass, and soaring lead melodies that feel heroic and bittersweet. Driving but emotional, like the credits rolling on a film that never existed.

0:00

-0:43

Audio playback is not supported on your browser. Please upgrade.
    
    
    Meditative Roller: A deep, meditative roller locked into a hypnotic 140 BPM groove, all smooth forward motion and late-night introspection. The bass line is the soul of it—warm, undulating, endlessly cycling through subtle variations like waves lapping at a shore, never jarring, never stopping.

0:00

-1:01

Audio playback is not supported on your browser. Please upgrade.
    
    
    Progressive House: A warm, rolling journey that builds patiently. Soft four-on-the-floor kick with airy hats, a plucky melodic synth hook that repeats and evolves, pads that swell across long phrases, and subtle acid bass bubbling underneath. Emotional but restrained, always moving forward toward a sunrise.

* * *

## Getting Started

### For ComfyUI Desktop & Local Users

  1. Update ComfyUI to the latest version

  2. Go to **Template Library → Audio** and select the ACE-Step 1.5 workflow

  3. Download the model when prompted (or manually from [Hugging Face](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files))

  4. Add your style tags and lyrics, then run!




[Download ACE-Step 1.5 Workflow](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/audio_ace_step_1_5_checkpoint.json)

[Download ACE-Step 1.5 Models](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/tree/main/split_files)

* * *

### Workflow Tips

  * **Style Tags** : Be descriptive! Include genre, instruments, mood, tempo, and vocal style. Example: `rock, hard rock, alternative rock, clear male vocalist, powerful voice, energetic, electric guitar, bass, drums, anthem, 120 bpm`

  * **Lyrics Structure** : Use tags like `[verse]`, `[chorus]`, `[bridge]` to guide song structure.

  * **Duration** : Start with 90–120 seconds for more consistent results. Longer durations (180+ seconds) may require generating multiple batches.

  * **Batch Generation** : Set `batch_size` to 8 or 16 and pick the best result—the model can be inconsistent, so generating multiple samples helps.




* * *

As always, enjoy creating!

#### Discussion about this video

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

[![ComfyUI Newsletter](https://substackcdn.com/image/fetch/$s_!uyu8!,w_96,h_96,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9545d140-0202-4a03-b9a2-58724fc1be59_500x500.png)](https://blog.comfy.org)

ComfyUI Newsletter

Subscribe

Authors

[![Purz's avatar](https://substackcdn.com/image/fetch/$s_!FaQt!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8b68a786-01d0-4123-bba7-3936c8854e57_400x400.jpeg)](https://substack.com/@purz?utm_source=author-byline-face-podcast)

[Purz](https://substack.com/@purz)

Recent Posts

![](https://substackcdn.com/image/fetch/$s_!-181!,w_150,h_150,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-video.s3.amazonaws.com%2Fvideo_upload%2Fpost%2F184356389%2Fd0458b5a-f42b-410c-8f88-ab75b5157212%2Ftranscoded-00001.png)

[Preprocessor and Frame Interpolation Workflows in ComfyUI](https://blog.comfy.org/p/preprocessor-and-frame-interpolation)

Jan 14 • [Purz](https://substack.com/@purz)

![](https://substackcdn.com/image/fetch/$s_!HVba!,w_150,h_150,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-video.s3.amazonaws.com%2Fvideo_upload%2Fpost%2F176280742%2Fa5c56de7-212b-46a7-b304-1617d9994c5d%2Ftranscoded-00001.png)

[Veo 3.1 is now available in ComfyUI!](https://blog.comfy.org/p/veo-31-is-now-available-in-comfyui)

Oct 16, 2025 • [Purz](https://substack.com/@purz)

![](https://substackcdn.com/image/fetch/$s_!3A7b!,w_150,h_150,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-video.s3.amazonaws.com%2Fvideo_upload%2Fpost%2F173554494%2F30b9758b-9ba5-49b2-8003-2d2688855c93%2Ftranscoded-1757948438.png)

[Comfy Cloud](https://blog.comfy.org/p/comfy-cloud)

Sep 15, 2025 • [Robin](https://substack.com/@robinjhuang)

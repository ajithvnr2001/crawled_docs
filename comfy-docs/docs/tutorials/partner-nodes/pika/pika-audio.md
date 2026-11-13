---
url: https://docs.comfy.org/tutorials/partner-nodes/pika/pika-audio/
title: Pika Music and Pika SFX in ComfyUI: AI songs and sound effects - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-13T15:12:13.009745+00:00
---

# Pika Music and Pika SFX in ComfyUI: AI songs and sound effects - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/pika/pika-audio/

## On this page

Back to top

  * Get started
  * Pika Music: text to music
  * Pika Music: cover a song
  * Pika SFX: text to sound effects
  * Writing a music prompt
  * Lyrics and section tags
  * Writing a sound effect prompt
  * Duration, limits and credits
  * Output and saving
  * Which Pika audio node to use
  * Related pages



Pika

# Pika Music and Pika SFX in ComfyUI: AI songs and sound effects

Copy pageCopy page

Generate a full song from a style prompt and lyrics, cover an existing track, or build 1 to 20 second sound effects with the Pika Music and Pika SFX nodes in ComfyUI.

Copy pageCopy page

Pika’s audio nodes turn a written description into finished audio without a local GPU. **Pika Music** writes a song from a style prompt plus optional lyrics, at a length you choose from 10 to 360 seconds, and it can cover an uploaded track at that track’s own length. **Pika SFX** returns one sound effect from 1 to 20 seconds, for foley, UI blips, risers and trailer hits. Neither node downloads weights. Both hand back a single `AUDIO` output, run on your Comfy account, and are billed in credits by the second of generated audio. **What these nodes are for**

  * A cue, jingle or instrumental bed cut to the exact length of a video edit
  * A song from lyrics you already wrote, in a style you can change without touching the words
  * A restyled version of a track you own: new genre, new tempo, the same song underneath
  * Foley, impacts, whooshes, room tone and game event sounds for a finished picture



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

## Get started

  1. Update ComfyUI to 0.45.0 or later
  2. Go to Template Library, search for `Pika Music` or `Pika SFX`
  3. Write the prompt, set `duration`, then run the workflow



## Pika Music: text to music

Write the arrangement, the mood and the instrumentation into the prompt, then add lyrics if you want a vocal. The node returns one finished track, mixed by the model. ![Pika Music text to music workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pika_music-1.webp)

## Download Workflow

Download JSON or search “Pika Music” in Template Library

  1. Choose `text to music` in the `Pika Music` node.
  2. Write the brief into `prompt`: genre and era, BPM and key, the instruments that carry the hook, the vocal character, and how the song moves from section to section. Up to 4,000 characters reach the model.
  3. Add `lyrics` with section tags such as `[Verse]` and `[Chorus]`, or leave the field empty for an instrumental. Up to 8,000 characters.
  4. Set `duration` between 10 and 360 seconds, 30 by default. Turn on `rewrite_prompt` only when your prompt is a few words and you want a model to expand it first.
  5. Run the workflow. `Save Audio (Advanced)` writes an MP3 to `ComfyUI/output/audio/`.



## Pika Music: cover a song

Switch the same node’s mode to `cover` to restyle a song you already have instead of writing a new one. Connect an audio file to `source_audio`, then write the brief as the arrangement you want instead: a different genre, a different tempo, a different band. Cover ignores `duration`. The result keeps the length of the source, clamped to 5 to 360 seconds, so a three-minute upload comes back three minutes long. The `lyrics` input still applies, which means you can keep the original words or hand the model a new set for the same arrangement. A cover works from a mix, so separation is the model’s job. A centered lead vocal and a simple arrangement survive a restyle more reliably than a dense master.

## Pika SFX: text to sound effects

Name the sound in one line and the node returns a single effect. Pika follows the brief without adding speech, music or background noise you did not ask for, so an effect drops into a timeline without a bed you have to strip out. ![Pika SFX text to sound effect workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pika_sfx-1.webp)

## Download Workflow

Download JSON or search “Pika SFX” in Template Library

  1. Write the sound in the `Pika SFX` prompt, for example an old timber door creaking open on rusty hinges, then a heavy latch clicking shut.
  2. Set `duration` between 1 and 20 seconds, 5 by default, then run the workflow. The MP3 lands in `ComfyUI/output/audio/`.

Each run produces one effect at 44.1 kHz stereo. For a sequence of sounds, run the node once per sound and place them on the timeline yourself. Pika SFX does not write music or sung vocals; use Pika Music for that.

## Writing a music prompt

Build the brief in this order: **genre and era, BPM and key, the instruments that carry the hook, vocal character, arrangement arc, mix notes**. The model reads all 4,000 characters, so detail earns its place; a stack of adjectives does not. The default prompt in the template shows the shape:
    
    
    Slow-burning indie soul ballad at 72 BPM: warm Rhodes electric piano, brushed drums, upright bass and a soft horn section that swells in the chorus. Intimate late-night lounge mood, analog tape saturation, wide stereo reverb.
    

More starting points:

  * `Mainstream dance pop, four-on-the-floor beat at 124 BPM in A minor, bright female lead in an upper-mid register, sidechained warm pads, plucked synth hook, filtered verse lifting into a festival-sized chorus, glossy radio mix.`
  * `Sparse solo grand piano at 68 BPM, felt hammers and close mic, rubato intro resolving into a steady left-hand arpeggio, no drums, no vocals.`
  * `Cinematic orchestral build at 90 BPM, taiko and low-string ostinato, brass swell around twenty seconds, choir pad underneath, wide trailer mix, instrumental.`
  * `Lofi hip hop at 82 BPM, dusty boom-bap drums, vinyl crackle, warm electric piano loop, upright bass, no vocals, loopable.`

What changes the result:

  * **Ask for the arc, not just the palette.** “Filtered verse lifting into a full chorus” gives the track somewhere to go; a long instrument list on its own tends to come back as a static texture.
  * **Say what you do not want.** `no vocals`, `no ad-libs`, `dry close-mic lead` are all read as direction.
  * **Name the delivery.** Register, gender and how forward the vocal sits in the mix move the track more than one more instrument does.
  * **Match the length to the job.** A 10-second sting and a 180-second cue want different briefs, so generate the length you need instead of cutting a long song down.
  * **Iterate one dimension at a time.** Keep the seed while you edit the prompt, so the difference you hear comes from the change you made.



## Lyrics and section tags

`lyrics` is a separate input from the prompt, so the same words can come back as a ballad, a dance single or a rock performance when only the brief changes.

  * An empty `lyrics` field returns an instrumental on the same brief, with no vocal.
  * Tags set the structure. They are read as phrasing and section boundaries rather than text to sing. `[Verse]`, `[Pre-Chorus]` and `[Chorus]` cover most songs; add `[Verse 2]`, `[Bridge]` or `[Final Chorus]` to name repeats and the ending.
  * Keep one lyric line per line. Line breaks are what the model phrases against.


    
    
    [Verse]
    Streetlights hum on the empty avenue
    I keep the radio low and the windows down
    [Pre-Chorus]
    Every red light is a chance to turn around
    [Chorus]
    I'm not lost, I'm just taking the long way home
    

## Writing a sound effect prompt

One line, and four things in it: **what the material is, what happens to it, the space it happens in, and how close the mic is**. Intensity goes last. A close, dry description reads better than a list of adjectives.

Goal| Prompt  
---|---  
Door, foley| `Old timber door creaks open slowly on rusty hinges, then a heavy latch clicks shut, close perspective, dry, no music, no voices`  
UI blip| `Short bright digital blip, one hundred milliseconds, clean tone, no reverb`  
Trailer impact| `Deep sub-bass impact with a metal debris tail, close and heavy, wide stereo, cinematic`  
Crowd ambience| `Reverberant stadium crowd cheering, chants and claps, steady bed with no music`  
Riser| `Rising noise sweep with a pitch climb across eight seconds, tension building to a hard stop`  
Mechanical detail| `Close-up foley inside an antique mechanical clock, steady pendulum tick-tock, tiny brass gears turning, escapement clicking`  
  
  * **One event per run.** A door opening and a latch closing share one prompt only when they land in that order inside the duration you set.
  * **Say`no music, no voices`** when the effect has to sit under dialogue. It keeps the render clean.
  * **Match duration to the event.** A click is one second; a riser has to fill the gap in front of the cut.
  * **Audition variants.** Re-run with a new seed, then change one dimension: material first, then space, then intensity.



## Duration, limits and credits

Limit| Pika Music| Pika SFX  
---|---|---  
Prompt| 1 to 4,000 characters| 1 to 4,000 characters  
Lyrics| up to 8,000 characters, optional| not supported  
Duration| 10 to 360 seconds, default 30| 1 to 20 seconds, default 5  
Cover length| follows `source_audio`, clamped to 5 to 360 seconds| not supported  
Output| one track, stereo| one effect, 44.1 kHz stereo  
  
Both nodes bill in credits by the second of generated audio, so a 10-second sting costs a fraction of a 3-minute song. See [Partner node pricing](https://docs.comfy.org/tutorials/partner-nodes/pricing) for the current rate. The same prompt, lyrics, duration and seed with `rewrite_prompt` off reproduce the same result. With `rewrite_prompt` on, a model rewrites the brief before generation, so the seed alone no longer pins the output. Leave it off when you want a reproducible workflow. Both nodes start at `seed` 42, so hold it while you edit the prompt and change it only to audition another take.

## Output and saving

Both nodes output `AUDIO`, and the templates save it with `Save Audio (Advanced)`: prefix `audio/Pika_Music` or `audio/Pika_SFX`, format `mp3` at `V0`, which lands in `ComfyUI/output/audio/`. Switch the format to `flac` when you want a lossless file to master or re-cut. The output is an ordinary audio stream, so it composes with the rest of the graph:

  * Connect it to `Create Video` to attach the track to a set of frames
  * Run `Pika SFX` once per hit and layer the results in an editor, since one run gives one effect
  * Set the track duration to the length of the cut instead of trimming a longer song in the timeline



## Which Pika audio node to use

Node| Input| Output| Use it when  
---|---|---|---  
**Pika Music**|  prompt, lyrics, optional source song| A full song, 10 to 360 seconds| You need music: a bed, a jingle, a song, or a cover  
**Pika SFX**|  prompt| One effect, 1 to 20 seconds| You need one specific sound from a description  
**Pika Soundtrack**|  a video, optional instruction| The clip’s audio replaced with a synchronized soundtrack| The sound has to follow the picture, up to 10 minutes  
  
For an effect timed to action on screen, the video path is [Pika Soundtrack on the Pika H3 Flex page](https://docs.comfy.org/tutorials/partner-nodes/pika/pika-h3-flex), which reads the clip instead of a description.

## Related pages

  * [Pika H3 Flex](https://docs.comfy.org/tutorials/partner-nodes/pika/pika-h3-flex): video generation with synchronized audio
  * [Mirelo SFX 2.0](https://docs.comfy.org/tutorials/partner-nodes/mirelo/mirelo-sfx): foley timed to a clip, and text to SFX
  * [ACE-Step 1.5](https://docs.comfy.org/tutorials/audio/ace-step/ace-step-v1-5): an open-weights music model that runs locally on your own GPU
  * [Partner node pricing](https://docs.comfy.org/tutorials/partner-nodes/pricing) and [concurrency limits](https://docs.comfy.org/tutorials/partner-nodes/concurrency-limits)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/pika/pika-audio.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/pika/pika-audio)

[Pika H3 Flex](https://docs.comfy.org/tutorials/partner-nodes/pika/pika-h3-flex)[PixVerse AI](https://docs.comfy.org/tutorials/partner-nodes/pixverse/overview)

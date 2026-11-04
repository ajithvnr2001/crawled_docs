---
url: https://docs.comfy.org/tutorials/partner-nodes/sonilo/music-1-5/
title: Sonilo Music 1.5 in ComfyUI: Lyrics to Song - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-04T15:15:41.451195+00:00
---

# Sonilo Music 1.5 in ComfyUI: Lyrics to Song - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/sonilo/music-1-5/

## On this page

Back to top

  * Get started
  * Sonilo: Music 1.5 (Lyrics to Song)



Sonilo

# Sonilo Music 1.5 in ComfyUI: Lyrics to Song

Copy pageCopy page

Generate a full song with sung vocals in ComfyUI using the Sonilo Music 1.5 partner node, with the prompt format, lyrics tags, and duration control.

Copy pageCopy page

Sonilo Music 1.5 turns a written prompt into a finished song with sung vocals. Describe the style first, add a `Lyrics:` block with your own words, and the node sings them. Without a lyrics block the model writes its own. For Sonilo video soundtracks and the older text to music node, see [Sonilo: Video to Music and Text to Audio](https://docs.comfy.org/tutorials/partner-nodes/sonilo/video-to-music).

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

Get started

1

Update ComfyUI

Update ComfyUI to a version that includes the `Sonilo Music 1.5` node.

2

Find the Sonilo Music 1.5 workflow

Open the **Workflow Library** , browse **Templates** , and search for “Sonilo Music 1.5”.

3

Write the direction and the lyrics

Fill in the prompt, then click the **Run** button or use `Ctrl(Cmd) + Enter`.

## 

​

Sonilo: Music 1.5 (Lyrics to Song)

Generate a song from a text prompt. The prompt sets the musical direction, and the lyrics block sets the words that are sung. ![Sonilo Music 1.5 lyrics to song workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_sonilo_music1_5-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Sonilo Music 1.5” in Template Library

**Prompt format** : describe the musical direction first, then put `Lyrics:` on its own line and write the song underneath. Bracket tags such as `[Verse]`, `[Chorus]` and `[Bridge]` go on their own line above each section, and you repeat the tag every time that section comes back.

  * **Length** : `auto` fits the song to the lyrics. Switch `duration` to `custom` to fix a length between 10 and 360 seconds; a custom length cuts lyrics that do not fit and repeats short ones
  * **Prompt limit** : 2000 characters for the direction and the lyrics together
  * **Instrumental** : with no `Lyrics:` block, say `instrumental`, `no vocals` or `lyric-free` in the direction to get a music bed instead of a song
  * **Output** : the template writes an MP3 through Save Audio (Advanced)

**Example prompt:**
    
    
    Warm indie folk at 104 BPM, fingerpicked guitar, brushed drums, upright bass,
    male vocal with light harmonies, written for a cooking video intro.
    
    Lyrics:
    [Verse]
    Flour on the wooden board
    Make a well right in the core
    
    [Chorus]
    Roll it out, roll it thin
    Let the kitchen groove begin
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/sonilo/music-1-5.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/sonilo/music-1-5)

[Video To Music](https://docs.comfy.org/tutorials/partner-nodes/sonilo/video-to-music)[HeyGen Voice 1.0](https://docs.comfy.org/tutorials/partner-nodes/heygen/heygen-voice-1)

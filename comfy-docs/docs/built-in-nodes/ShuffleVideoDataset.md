---
url: https://docs.comfy.org/built-in-nodes/ShuffleVideoDataset/
title: ShuffleVideoDataset - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:54.001967+00:00
---

# ShuffleVideoDataset - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ShuffleVideoDataset/

Batch

# ShuffleVideoDataset - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node takes a list of videos and randomly reorders them.

Copy pageCopy page

This node takes a list of videos and randomly reorders them. It uses a random seed to make the shuffle reproducible, so the same seed always produces the same output order.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`videos`| List of videos to shuffle.| VIDEO| Yes| List of video inputs  
`seed`| Random seed for shuffling (default: 0).| INT| No| 0 to 18446744073709551615  
  
Note: The seed value is reduced modulo 4294967295 (2^32 - 1) before being used. As a result, seeds that differ by a multiple of 4294967295 produce the same output order.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`videos`| Shuffled list of videos in random order.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleVideoDataset/en.md)

* * *

**Source fingerprint (SHA-256):** `0bd32b664197d3bbd4c53f65e29ef38fba836579f07f05cb7fb85f3b8a1024ac`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ShuffleVideoDataset.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ShuffleVideoDataset)

[wanBlockSwap](https://docs.comfy.org/built-in-nodes/wanBlockSwap)[ShuffleVideoTextDataset](https://docs.comfy.org/built-in-nodes/ShuffleVideoTextDataset)

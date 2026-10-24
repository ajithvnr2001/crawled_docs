---
url: https://docs.comfy.org/built-in-nodes/MergeImageLists/
title: MergeImageLists - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-24T11:54:52.011728+00:00
---

# MergeImageLists - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MergeImageLists/

Batch

# MergeImageLists - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Merge Image Lists node combines multiple separate lists of images into a single, continuous list.

Copy pageCopy page

The Merge Image Lists node combines multiple separate lists of images into a single, continuous list. It works by taking all the images from each connected input and appending them together in the order they are received. This is useful for organizing or batching images from different sources for further processing. **Note:** This node is deprecated and superseded by the Create List node.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| A list of images to be merged. This input can accept multiple connections, and each connected list will be concatenated into the final output.| IMAGE| Yes| -  
  
**Note:** This node is designed to receive multiple inputs. You can connect several image lists to the single `images` input socket. The node will automatically concatenate all images from all connected lists into one output list.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`images`| The single, merged list containing all images from every connected input list.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeImageLists/en.md)

* * *

**Source fingerprint (SHA-256):** `0c9e302b02694a6a23fc7776c872856b1a629df3efe914a3e591a89d5a28914a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MergeImageLists.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MergeImageLists)

[ImageMergeTileList](https://docs.comfy.org/built-in-nodes/ImageMergeTileList)[RebatchImages](https://docs.comfy.org/built-in-nodes/RebatchImages)

---
url: https://docs.comfy.org/built-in-nodes/GeminiDecisionScore/
title: Google Gemini Decision (Score) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-22T15:07:50.595715+00:00
---

# Google Gemini Decision (Score) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/GeminiDecisionScore/

Text

# Google Gemini Decision (Score) - ComfyUI Built-in Node Documentation

Copy pageCopy page

Rate the text, images, audio or video you connect from 1 to 10, and get the score plus a boolean that flips at a threshold you set.

Copy pageCopy page

Rate the text, images, audio or video you connect from 1 to 10, and get the score plus a boolean that flips at a threshold you set. Use it to filter or sort outputs, for example to keep only images that score at least 7, and connect `result` to an If/Else Switch node to act on it. One run scores what you connect as a whole, so filtering individual images means scoring them one at a time.

## Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model to use (default: `"gemini-decision-1"`).| COMBO| Yes| `"gemini-decision-1"`  
`question`| What to rate, saying what 1 and 10 mean (default: “Rate the technical quality of the image from 1 (worst) to 10 (best).”).| STRING| Yes| 1 to 5000 characters  
`threshold`| `result` is true when the score is at least this value. Clean, sharp images score about 7 to 8, badly damaged ones about 3 to 5 (default: 6.0).| FLOAT| Yes| 1.0 to 10.0 (step 0.1)  
`images`| Images to rate, up to 16 across the growable slots (`image_1` … `image_16`). A batched image counts once per image.| IMAGE| No| Up to 16 images  
`audio`| Audio clip to rate.| AUDIO| No| -  
`video`| Video clip to rate.| VIDEO| No| -  
`text`| Text the question is about, such as a prompt or an LLM response, up to 20000 characters.| STRING| No| Up to 20000 characters  
  
Connect at least one of `text`, `images`, `audio` or `video`; the node raises an error when there is nothing to rate. With several images, name them `image_1`, `image_2` and so on inside the question.

## Outputs

Output Name| Description| Data Type  
---|---|---  
`result`| True when the score is at least `threshold`, otherwise false.| BOOLEAN  
`score`| The rating from 1 to 10.| FLOAT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionScore/en.md)

* * *

**Source fingerprint (SHA-256):** `9b0a68cc7f29b1d4d23e23e051a008f34932aac6d1fe1a16e45a0e70b4df412f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/GeminiDecisionScore.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/GeminiDecisionScore)

[Google Gemini Decision (Pick Image)](https://docs.comfy.org/built-in-nodes/GeminiDecisionPickImage)[Google Gemini Decision (Yes/No)](https://docs.comfy.org/built-in-nodes/GeminiDecisionYesNo)

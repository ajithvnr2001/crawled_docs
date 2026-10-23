---
url: https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image
title: Gemini 3.1 Flash Lite image
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:44:38.780226+00:00
---

# Gemini 3.1 Flash Lite image

> Source: https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image

**Nano Banana 2 Lite** is designed as the efficiency specialist of the image generation family, offering ultra-low latency and cost-effective image generation and editing. By targeting a sub-2 second latency and significantly reduced TPU compute costs, this model enables high-volume interactive developer use cases and real-time consumer applications.

**Key capabilities:**

  * **Sub-2 second end-to-end latency**
  * **Interleaved generation and editing** with native support for Text -> Text + Image(s) and Image + Text -> Text + Image(s).
  * **Optimized for lower resolutions** of 1K (1024x1024px).
  * Supports a discrete set of **14 aspect ratios** including standard formats.
  * **Fast multi-turn local edits** (swapping colors, sticker creation, background adjustments).
  * Maintains high character alignment matching original Nano Banana standards.
  * New `1:1`, `3:2`, `2:3`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9` aspect ratios.
  * Supported `image_size` values: `1024px` (1K). _(Note: 2K and 4K are unsupported)._
  * **SynthID watermarking (Always On) + C2PA**.



[Try in Google AI Studio](https://aistudio.google.com?model=gemini-3.1-flash-lite-image)

## Documentation

Visit the [Image generation](https://ai.google.dev/gemini-api/docs/image-generation) page for full coverage of features and capabilities.

## gemini-3.1-flash-lite-image

Property | Description  
---|---  
id_cardModel code | `gemini-3.1-flash-lite-image`  
saveSupported data types |  **Inputs** Text, Image, Video, and PDF **Output** Image and Text  
token_autoToken limits[[*]](https://ai.google.dev/gemini-api/docs/tokens) |  **Input token limit** 65,536 **Output token limit** 4,096  
handymanCapabilities |  **[Audio generation](https://ai.google.dev/gemini-api/docs/speech-generation)** Not supported **[Caching](https://ai.google.dev/gemini-api/docs/caching)** Not supported **[Code execution](https://ai.google.dev/gemini-api/docs/code-execution)** Not supported **[File search](https://ai.google.dev/gemini-api/docs/file-search)** Not supported **[Function calling](https://ai.google.dev/gemini-api/docs/function-calling)** Not supported **[Grounding with Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding)** Not supported **[Image generation](https://ai.google.dev/gemini-api/docs/image-generation)** Supported **[Live API](https://ai.google.dev/gemini-api/docs/live-api)** Not supported **[Search grounding](https://ai.google.dev/gemini-api/docs/google-search)** Not supported **[Structured outputs](https://ai.google.dev/gemini-api/docs/structured-output)** Not supported **[Thinking](https://ai.google.dev/gemini-api/docs/thinking)** Supported (minimal and high) **[URL context](https://ai.google.dev/gemini-api/docs/url-context)** Not supported  
speedConsumption options |  **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api)** Supported **[Flex inference](https://ai.google.dev/gemini-api/docs/flex-inference)** Not supported **[Priority inference](https://ai.google.dev/gemini-api/docs/priority-inference)** Not supported  
123Versions |  Read the [model version patterns](https://ai.google.dev/gemini-api/docs/models/gemini#model-versions) for more details.

  * Stable: `gemini-3.1-flash-lite-image`

  
calendar_monthLatest update | June 2026  
id_cardModel card | [Model card](https://deepmind.google/models/model-cards/gemini-3-1-flash-lite-image/)

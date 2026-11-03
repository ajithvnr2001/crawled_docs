---
url: https://www.canva.dev/blog/developers/image-gen-with-craft/
title: Build AI image generation into your app with Canva Craft - Canva Developers Blog
method: scrapling+scrapegraph
fetched_at: 2026-11-03T17:24:20.568891+00:00
---

# Build AI image generation into your app with Canva Craft - Canva Developers Blog

> Source: https://www.canva.dev/blog/developers/image-gen-with-craft/

Developers Blog

[Overview](https://www.canva.dev/blog/developers/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Generative AI

# Build AI image generation into your app with Canva Craft

Generate visual assets with Canva Craft (`craft_v1_2k`) using Canva’s preview Image generation API, then download the result or save it to a user’s Canva account.

![](https://www.canva.dev/_next/static/media/thumbnail.3524a884.jpg)

* * *

  * 


[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Oct 28, 2026

* * *

Canva Craft is Canva’s first-party image-generation model, available to developers through the preview Image generation API. The current Craft model is **CRAFT-1 2K** (`craft_v1_2k`). Send a text prompt, select Craft, and generate an image to use in your app or save to a user’s Canva account.

The Image generation API is currently in preview and can change without notice. Apps that use the preview API can't pass public-app review or be made available to all Canva users.

Craft is well suited to infographics, posters, slides, people and portraits, abstract art and patterns, landscapes and nature, product imagery, and marketing materials.

What sets Craft apart is its two-stage architecture: it plans the composition before rendering the image. As described in the [Canva Craft announcement⁠(opens in a new tab or window)](https://www.canva.com/newsroom/news/canva-craft/), that approach improves precision, consistency, and control for complex layouts, object placement, visual relationships, and text in an image.

Whether you’re prototyping a new creative experience or adding image generation to an existing product, you can get started with a single asynchronous API workflow.

## Craft image generation capabilities

Prompt used with `craft_v1_2k`
    
    
    A clean editorial infographic poster titled "Ocean Plastics 2026". Three large stat callouts: "11 million tons" enter the ocean each year, "1 in 3" fish contain microplastics, and "2040" is the target to cut inflow in half. A simple wave illustration, deep teal and sand, generous margins, readable sans-serif type, no watermark.

Copy

Example output

![Craft-generated portrait infographic titled Ocean Plastics 2026, with three large statistic callouts, fish illustrations, and layered teal waves.](https://www.canva.dev/_next/static/media/craftoutput.78eb0328.png)

A Craft output from the preceding prompt, demonstrating a structured infographic-style composition. The statistics are illustrative prompt content.

## Craft at a glance

  * **Model ID:** `craft_v1_2k`
  * **API:** Canva Image generation API (preview)
  * **Authentication:** OAuth on behalf of the user
  * **Required app configuration:** `asset:write` scope
  * **Required user capabilities:** `image_generation`
  * **Workflow:** Create a job, poll for completion, then download the result or save it to Canva
  * **Credit usage:** Each generation uses the user’s [AI credit allowance⁠(opens in a new tab or window)](https://www.canva.com/help/ai-access/)



You can check user capabilities with the [Get user capabilities](https://www.canva.dev/docs/apps/rest-apis/reference/users/get-user-capabilities/) endpoint.

## Generate an image with Craft

To generate an image with Craft, create an app in the Developer Portal and configure it to use the Canva REST APIs.

  1. **Create and configure a REST API app.**

In the Developer Portal, select **Outside Canva** , then click **Start integrating** to enable the REST APIs. On the Configuration page, select the `asset:write` scope.

  2. **Authorize the user and confirm their capability.**

The Image generation API acts on behalf of a user, so your app must use OAuth and obtain user authorization. You can find Canva's [Authorization guide](https://www.canva.dev/docs/apps/rest-apis/authentication/) to learn how to authorize users.

The user must also have the `image_generation` capability. You can check this with the [Get user capabilities](https://www.canva.dev/docs/apps/rest-apis/reference/users/get-user-capabilities/) endpoint.

  3. **Create a generation job.**

Send a `POST` request to the [Create image generation job](https://www.canva.dev/docs/apps/rest-apis/reference/generations/create-image-generation-job/). Add `asset_upload` when you want the generated image saved to the user's Canva account:
         
         {
         
           "prompt": "A bold, colorful poster for a neighborhood summer music festival",
         
           "model": "craft_v1_2k",
         
           "aspect_ratio": "portrait",
         
           "asset_upload": {
         
             "type": "upload"
         
           },
         
           "idempotency_key": "<unique UUID for this generation attempt>"
         
         }

JSON

Copy

The `prompt` and `idempotency_key` fields are required. Generate a new UUID for each new generation attempt; don't ship a copied example UUID. Reusing the same key for 24 hours returns the original job, including if that job failed. To make another attempt, use a new key.

Without `asset_upload`, the completed job returns only a download URL. With `asset_upload` set to `{ "type": "upload" }`, the completed job returns both the download URL and an image asset in the user's Canva account.

  4. **Poll the job until it completes.**

Image generation is asynchronous. Use the [Get image generation job](https://www.canva.dev/docs/apps/rest-apis/reference/generations/get-image-generation-job/) to poll the job until it completes. The completed job and its download URL are available for 24 hours.

  5. **Optionally import the saved image asset as a Canva design.**

The [Create image-to-design import job](https://www.canva.dev/docs/apps/rest-apis/reference/design-imports/create-image-to-design-import-job/) endpoint accepts an image asset already in the user's Canva account. It doesn't accept the generation URL or a raw image file.

To use it, first generate the image with `asset_upload` enabled, then import the resulting Canva image asset. Your app also needs the `design:content:write` scope, and the user needs the `image_to_design_imports` capability, which requires Canva AI and Magic Layers enabled by their admin in their Canva account. Image-to-design is a preview API and uses additional AI credits.




## Build with Craft

Craft is a useful fit for experiences that turn a short brief into a visual starting point:

  * Campaign and social-content tools: Generate posters, campaign concepts, and marketing visuals.
  * Product experiences: Create product imagery or visual concepts from product context.
  * Presentation workflows: Generate a visual asset, save it to Canva, then use it in a presentation or optionally import it into an editable design.
  * Creative-assistance tools: Help users turn a written idea into an image they can refine or use in another workflow.



Results vary by prompt, so test Craft with the visual styles, layouts, and subject matter your product needs to support.

## Try Craft

Ready to experiment? Create an app in the Developer Portal, and make your first request with `craft_v1_2k`.

For model options and the latest API details, see the [Image generation API guide](https://www.canva.dev/docs/apps/rest-apis/reference/generations/).

## More from the Developers Blog

[![](https://www.canva.dev/_next/static/media/thumbnail.6c865963.jpg)](https://www.canva.dev/blog/developers/apps-to-win-big/)

[Apps SDKSimple apps to win big in the Canva Apps MarketplaceWhat kind of apps are we looking for for the Apps Marketplace?](https://www.canva.dev/blog/developers/apps-to-win-big/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Sep 19, 2023

[![](https://www.canva.dev/_next/static/media/thumbnail.02a1ad94.jpg)](https://www.canva.dev/blog/developers/building-with-content-publisher-part3/)

[Content Publisher intentMeet the Content Publisher Intent - Part 3Complete implementation, Preview UIs, and publishing](https://www.canva.dev/blog/developers/building-with-content-publisher-part3/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)May 8, 2026

[![](https://www.canva.dev/_next/static/media/thumbnail.5ca88239.jpg)](https://www.canva.dev/blog/developers/importance-of-the-apps-marketplace/)

[Magic StudioThe importance of the Apps Marketplace to Magic StudioHow our view of AI apps are shaping our future.](https://www.canva.dev/blog/developers/importance-of-the-apps-marketplace/)

Anwar HaneefNov 3, 2023

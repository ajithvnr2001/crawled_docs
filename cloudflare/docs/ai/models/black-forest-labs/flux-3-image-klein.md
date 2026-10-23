---
url: https://developers.cloudflare.com/ai/models/black-forest-labs/flux-3-image-klein/
title: FLUX 3 Image Klein (Black Forest Labs) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:11:05.778326+00:00
---

# FLUX 3 Image Klein (Black Forest Labs) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/black-forest-labs/flux-3-image-klein/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Black Forest Labs logo](https://developers.cloudflare.com/_astro/blackforestlabs.Ccs-Y4-D.svg)

# FLUX 3 Image Klein

Text-to-Image • Black Forest Labs

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`black-forest-labs/flux-3-image-klein`

  * Third-party



FLUX 3 Image Klein is Black Forest Labs' 5.6B-parameter image model for text-to-image, image editing, and multi-reference generation with up to 10 reference images. It supports native 4K output and bounding-box layout control.

Model Info|   
---|---  
Terms and License| [link ↗](https://blackforestlabs.ai/terms-of-service/)  
More information| [link ↗](https://docs.bfl.ai/api-reference/utility/generate-an-image-with-flux-3-klein)  
Pricing| 

  * First output megapixel$0.009
  * Per additional output megapixel$0.001667
  * Per input megapixel$0.00

  
  
## Usage
    
    
    const response = await env.AI.run(
      'black-forest-labs/flux-3-image-klein',
      { prompt: 'A golden retriever puppy playing in autumn leaves', resolution: '1k' },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "black-forest-labs/flux-3-image-klein",
      "input": {
        "prompt": "A golden retriever puppy playing in autumn leaves",
        "resolution": "1k"
      }
    }'

![Simple Prompt](https://examples.aig.cloudflare.com/black-forest-labs/flux-3-image-klein/simple-prompt.jpg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/black-forest-labs/flux-3-image-klein/simple-prompt.jpg"
      }
    }

## Examples

**Recolor One Element** — Edit a single element of a reference image and leave the rest unchanged
    
    
    const response = await env.AI.run(
      'black-forest-labs/flux-3-image-klein',
      {
        prompt: 'change the color of only one bird in the middle to #e01075',
        images: [
          'https://cdn.sanity.io/images/2gpum2i6/production/4792198dfeba9223bf3ecf020fed2942de7f0bd7-1800x1200.webp',
        ],
        resolution: '1k',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "black-forest-labs/flux-3-image-klein",
      "input": {
        "prompt": "change the color of only one bird in the middle to #e01075",
        "images": [
          "https://cdn.sanity.io/images/2gpum2i6/production/4792198dfeba9223bf3ecf020fed2942de7f0bd7-1800x1200.webp"
        ],
        "resolution": "1k"
      }
    }'

![Recolor One Element](https://examples.aig.cloudflare.com/black-forest-labs/flux-3-image-klein/recolor-one-element.jpg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/black-forest-labs/flux-3-image-klein/recolor-one-element.jpg"
      }
    }

**Style Transfer** — Apply the style of a second reference image to the first, using two references
    
    
    const response = await env.AI.run(
      'black-forest-labs/flux-3-image-klein',
      {
        prompt: 'Turn Image 1 in the Style of Image 2',
        images: [
          'https://cdn.sanity.io/images/2gpum2i6/production/ababcf5c9cf86074d71c92d6362ff63545d90661-1800x1201.webp',
          'https://cdn.sanity.io/images/2gpum2i6/production/dc642f5b01040c4afc46c1b4f8c4945152932683-1350x1800.webp',
        ],
        resolution: '1k',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "black-forest-labs/flux-3-image-klein",
      "input": {
        "prompt": "Turn Image 1 in the Style of Image 2",
        "images": [
          "https://cdn.sanity.io/images/2gpum2i6/production/ababcf5c9cf86074d71c92d6362ff63545d90661-1800x1201.webp",
          "https://cdn.sanity.io/images/2gpum2i6/production/dc642f5b01040c4afc46c1b4f8c4945152932683-1350x1800.webp"
        ],
        "resolution": "1k"
      }
    }'

![Style Transfer](https://examples.aig.cloudflare.com/black-forest-labs/flux-3-image-klein/style-transfer.jpg)
    
    
    {
      "id": "1867eff0-e11e-4609-ac66-73dc4c558632",
      "status": "Ready",
      "result": {
        "sample": "https://examples.aig.cloudflare.com/black-forest-labs/flux-3-image-klein/style-transfer.jpg",
        "duration": 6.776479244232178,
        "prompt": "Create a whimsical storybook illustration of the ancient stone temple from the first image, preserving its exact frontal composition: the tall central weathered tower with its paired rounded peaks, three dark rectangular doorways, layered terraces, broad steps, and the two narrower towers rising at frame-left and frame-right. Render the entire scene in the style of the second image, using simplified hand-painted shapes, softly irregular ink contours, muted earthy browns, charcoal blacks, dusty blue-gray, and visible watercolor-and-gouache paper texture. Translate the temple’s carved masonry into gently uneven blocks and sparse linear details while retaining its recognizable proportions, openings, and aged surface. Replace the pale sky with a mottled blue-gray paper field scattered with tiny cream, rust, and brown speckles like drifting snow or stars. Add slender, crooked dark tree trunks and sparse bare branches around the outer edges, echoing the second image’s quiet woodland framing without obscuring the architecture. Include the second image’s small round dark-brown creature with a pale face, pointed hat, and tiny feet, standing near the lower steps and reaching upward toward a softly glowing crescent moon suspended beside the central tower. Keep the moon’s warm cream glow subtle against the cool background, with no text or modern objects.",
        "seed": 1125826703
      },
      "progress": null,
      "details": null,
      "preview": null
    }

**Layout With Boxes** — Place elements in a composition using bounding boxes on a 0 to 1000 grid
    
    
    const response = await env.AI.run(
      'black-forest-labs/flux-3-image-klein',
      {
        prompt:
          'Minimalist graphic illustration featuring a black silhouette of a person <silhouette_1> centered against a solid, vibrant chartreuse background <background_1>. The figure is captured in a dynamic, mid-stride running pose, facing toward the left side of the frame. The image relies entirely on the high-contrast relationship between the two colors, mimicking a digital recreation of a screen-printed or risograph aesthetic, with no discernible light source or shadow. [{"id":"background_1","bbox":[0,0,1000,1000],"desc":"A flat field of neon yellow-green possessing a subtle, tactile paper texture with fine, organic grain and slight variations in color saturation, giving the flat surface a sense of physical depth."},{"id":"silhouette_1","bbox":[150,150,850,850],"desc":"A black silhouette of a person in motion, composed of a dense, stippled texture that resembles physical ink on paper or a low-resolution digital dither. The leading edges, including the front of the head, chest, and forward leg, are relatively solid and opaque. The trailing edges, such as the back, outstretched rear arm, and lifted back leg, dissolve into a spray of coarse, square-shaped pixels and scattered dots. The black ink shows a slight textural irregularity, as if pressed onto a porous surface."}]',
        resolution: '1k',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "black-forest-labs/flux-3-image-klein",
      "input": {
        "prompt": "Minimalist graphic illustration featuring a black silhouette of a person <silhouette_1> centered against a solid, vibrant chartreuse background <background_1>. The figure is captured in a dynamic, mid-stride running pose, facing toward the left side of the frame. The image relies entirely on the high-contrast relationship between the two colors, mimicking a digital recreation of a screen-printed or risograph aesthetic, with no discernible light source or shadow. [{\"id\":\"background_1\",\"bbox\":[0,0,1000,1000],\"desc\":\"A flat field of neon yellow-green possessing a subtle, tactile paper texture with fine, organic grain and slight variations in color saturation, giving the flat surface a sense of physical depth.\"},{\"id\":\"silhouette_1\",\"bbox\":[150,150,850,850],\"desc\":\"A black silhouette of a person in motion, composed of a dense, stippled texture that resembles physical ink on paper or a low-resolution digital dither. The leading edges, including the front of the head, chest, and forward leg, are relatively solid and opaque. The trailing edges, such as the back, outstretched rear arm, and lifted back leg, dissolve into a spray of coarse, square-shaped pixels and scattered dots. The black ink shows a slight textural irregularity, as if pressed onto a porous surface.\"}]",
        "resolution": "1k"
      }
    }'

![Layout With Boxes](https://examples.aig.cloudflare.com/black-forest-labs/flux-3-image-klein/layout-with-boxes.jpg)
    
    
    {
      "id": "cbcaa104-fb37-4ec4-80ec-038f7a951f83",
      "status": "Ready",
      "result": {
        "sample": "https://examples.aig.cloudflare.com/black-forest-labs/flux-3-image-klein/layout-with-boxes.jpg",
        "duration": 1.596290111541748,
        "prompt": "Minimalist graphic illustration featuring a black silhouette of a person <silhouette_1> centered against a solid, vibrant chartreuse background <background_1>. The figure is captured in a dynamic, mid-stride running pose, facing toward the left side of the frame. The image relies entirely on the high-contrast relationship between the two colors, mimicking a digital recreation of a screen-printed or risograph aesthetic, with no discernible light source or shadow. [{\"id\":\"background_1\",\"bbox\":[0,0,1000,1000],\"desc\":\"A flat field of neon yellow-green possessing a subtle, tactile paper texture with fine, organic grain and slight variations in color saturation, giving the flat surface a sense of physical depth.\"},{\"id\":\"silhouette_1\",\"bbox\":[150,150,850,850],\"desc\":\"A black silhouette of a person in motion, composed of a dense, stippled texture that resembles physical ink on paper or a low-resolution digital dither. The leading edges, including the front of the head, chest, and forward leg, are relatively solid and opaque. The trailing edges, such as the back, outstretched rear arm, and lifted back leg, dissolve into a spray of coarse, square-shaped pixels and scattered dots. The black ink shows a slight textural irregularity, as if pressed onto a porous surface.\"}]",
        "seed": 1025881393
      },
      "progress": null,
      "details": null,
      "preview": null
    }

## Parameters

prompt

`string`required

▶images[]

`array`maxItems: 10format: uri

▶aspect_ratio

`one of`

resolution

`string`enum: 768sq, 1k, 1.5k, 2k, 4k

seed

`integer`minimum: 0maximum: 4294967295

image

`string`format: uri

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-3-image-klein/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-3-image-klein/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-3-image-klein/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-3-image-klein/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

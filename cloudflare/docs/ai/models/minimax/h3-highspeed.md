---
url: https://developers.cloudflare.com/ai/models/minimax/h3-highspeed/
title: MiniMax H3 Highspeed (MiniMax) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-31T08:10:16.887974+00:00
---

# MiniMax H3 Highspeed (MiniMax) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/minimax/h3-highspeed/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![MiniMax logo](https://developers.cloudflare.com/_astro/minimax.B0Y99aoe.svg)

# MiniMax H3 Highspeed

Text-to-Video • MiniMax

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`minimax/h3-highspeed`

  * Third-party



A multimodal video generation model that balances quality and speed, supporting text-to-video, first and last frame image-to-video, and reference-to-video generation at 768P.

Model Info|   
---|---  
Terms and License| [link ↗](https://platform.minimax.io/docs/guides/terms-of-service.md)  
More information| [link ↗](https://platform.minimax.io/docs/guides/video-generation.md)  
Pricing| 

  * @768p (per second)$0.06
  * Default (per second)$0.06

  
  
## Usage
    
    
    const response = await env.AI.run(
      'minimax/h3-highspeed',
      {
        content: [
          {
            type: 'text',
            text: 'Premium product commercial: a matte black wireless earbud case sits on a wet reflective surface, the lid opens on its own and soft rim light traces the edges [orbit]. Water droplets catch the light, then the camera settles on a clean centered hero shot [static].',
          },
        ],
        duration: 5,
        ratio: '16:9',
        resolution: '768P',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/h3-highspeed",
      "input": {
        "content": [
          {
            "type": "text",
            "text": "Premium product commercial: a matte black wireless earbud case sits on a wet reflective surface, the lid opens on its own and soft rim light traces the edges [orbit]. Water droplets catch the light, then the camera settles on a clean centered hero shot [static]."
          }
        ],
        "duration": 5,
        "ratio": "16:9",
        "resolution": "768P"
      }
    }'
    
    
    {
      "task": {
        "id": "457313369043439",
        "model": "MiniMax-H3-Highspeed",
        "status": "succeeded",
        "created_at": 1793202285,
        "updated_at": 1793202389,
        "content": {
          "url": "https://examples.aig.cloudflare.com/minimax/h3-highspeed/product-commercial.mp4"
        },
        "resolution": "768P",
        "duration": 5,
        "usage": {
          "total_seconds": 5,
          "input_seconds": 0,
          "output_seconds": 5,
          "input_image_count": 0,
          "total_tokens": 130195,
          "prompt_tokens": 0,
          "completion_tokens": 130195
        },
        "ratio": "16:9",
        "task_type": "generation"
      }
    }

## Examples

**Sketch to Product Reveal** — Turn a design sketch into a photoreal product shot from a first frame.
    
    
    const response = await env.AI.run(
      'minimax/h3-highspeed',
      {
        content: [
          {
            type: 'text',
            text: 'The pencil sneaker sketch comes to life: graphite lines fill in with white leather, an orange suede heel panel and a translucent sole, and the sneaker lifts off the page onto a slowly rotating white studio turntable. Softbox lighting, crisp reflections, smooth camera orbit.',
          },
          {
            type: 'image_url',
            image_url: {
              url: 'https://examples.aig.cloudflare.com/klingai/kling-v4/inputs/sneaker-sketch.jpg',
            },
            role: 'first_frame',
          },
        ],
        duration: 5,
        ratio: 'adaptive',
        resolution: '768P',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/h3-highspeed",
      "input": {
        "content": [
          {
            "type": "text",
            "text": "The pencil sneaker sketch comes to life: graphite lines fill in with white leather, an orange suede heel panel and a translucent sole, and the sneaker lifts off the page onto a slowly rotating white studio turntable. Softbox lighting, crisp reflections, smooth camera orbit."
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "https://examples.aig.cloudflare.com/klingai/kling-v4/inputs/sneaker-sketch.jpg"
            },
            "role": "first_frame"
          }
        ],
        "duration": 5,
        "ratio": "adaptive",
        "resolution": "768P"
      }
    }'
    
    
    {
      "task": {
        "id": "457315643584847",
        "model": "MiniMax-H3-Highspeed",
        "status": "succeeded",
        "created_at": 1793202399,
        "updated_at": 1793202411,
        "content": {
          "url": "https://examples.aig.cloudflare.com/minimax/h3-highspeed/sketch-to-product-reveal.mp4"
        },
        "resolution": "768P",
        "duration": 5,
        "usage": {
          "total_seconds": 5,
          "input_seconds": 0,
          "output_seconds": 5,
          "input_image_count": 1,
          "total_tokens": 143215,
          "prompt_tokens": 13020,
          "completion_tokens": 130195
        },
        "ratio": "adaptive",
        "task_type": "generation"
      }
    }

**Dusk to Milky Way** — End on a supplied last frame: a night-sky time-lapse.
    
    
    const response = await env.AI.run(
      'minimax/h3-highspeed',
      {
        content: [
          {
            type: 'text',
            text: 'Time-lapse over a quiet mountain landscape: the blue dusk sky darkens, the first stars appear and the Milky Way slowly rises into the final frame. Locked-off camera, gentle cloud movement.',
          },
          {
            type: 'image_url',
            image_url: { url: 'https://docs.x.ai/assets/api-examples/video/milkyway-still.png' },
            role: 'last_frame',
          },
        ],
        duration: 5,
        ratio: 'adaptive',
        resolution: '768P',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/h3-highspeed",
      "input": {
        "content": [
          {
            "type": "text",
            "text": "Time-lapse over a quiet mountain landscape: the blue dusk sky darkens, the first stars appear and the Milky Way slowly rises into the final frame. Locked-off camera, gentle cloud movement."
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "https://docs.x.ai/assets/api-examples/video/milkyway-still.png"
            },
            "role": "last_frame"
          }
        ],
        "duration": 5,
        "ratio": "adaptive",
        "resolution": "768P"
      }
    }'
    
    
    {
      "task": {
        "id": "457315350925788",
        "model": "MiniMax-H3-Highspeed",
        "status": "succeeded",
        "created_at": 1793202420,
        "updated_at": 1793202435,
        "content": {
          "url": "https://examples.aig.cloudflare.com/minimax/h3-highspeed/dusk-to-milky-way.mp4"
        },
        "resolution": "768P",
        "duration": 5,
        "usage": {
          "total_seconds": 5,
          "input_seconds": 0,
          "output_seconds": 5,
          "input_image_count": 1,
          "total_tokens": 143215,
          "prompt_tokens": 13020,
          "completion_tokens": 130195
        },
        "ratio": "adaptive",
        "task_type": "generation"
      }
    }

**Mascot Comes to Life** — Controlled transition between a supplied first and last frame.
    
    
    const response = await env.AI.run(
      'minimax/h3-highspeed',
      {
        content: [
          {
            type: 'text',
            text: 'A flat illustrated robot mascot printed on a notebook page wakes up, blinks, peels itself off the paper into a glossy 3D toy, hops onto the wooden desk next to the coffee mug and waves at the camera. Warm morning light, playful stop-motion feel, one continuous shot.',
          },
          {
            type: 'image_url',
            image_url: {
              url: 'https://examples.aig.cloudflare.com/klingai/kling-v4/inputs/mascot-page.jpg',
            },
            role: 'first_frame',
          },
          {
            type: 'image_url',
            image_url: {
              url: 'https://examples.aig.cloudflare.com/klingai/kling-v4/inputs/mascot-desk.jpg',
            },
            role: 'last_frame',
          },
        ],
        duration: 5,
        ratio: 'adaptive',
        resolution: '768P',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/h3-highspeed",
      "input": {
        "content": [
          {
            "type": "text",
            "text": "A flat illustrated robot mascot printed on a notebook page wakes up, blinks, peels itself off the paper into a glossy 3D toy, hops onto the wooden desk next to the coffee mug and waves at the camera. Warm morning light, playful stop-motion feel, one continuous shot."
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "https://examples.aig.cloudflare.com/klingai/kling-v4/inputs/mascot-page.jpg"
            },
            "role": "first_frame"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "https://examples.aig.cloudflare.com/klingai/kling-v4/inputs/mascot-desk.jpg"
            },
            "role": "last_frame"
          }
        ],
        "duration": 5,
        "ratio": "adaptive",
        "resolution": "768P"
      }
    }'
    
    
    {
      "task": {
        "id": "457316282126857",
        "model": "MiniMax-H3-Highspeed",
        "status": "succeeded",
        "created_at": 1793202441,
        "updated_at": 1793202454,
        "content": {
          "url": "https://examples.aig.cloudflare.com/minimax/h3-highspeed/mascot-comes-to-life.mp4"
        },
        "resolution": "768P",
        "duration": 5,
        "usage": {
          "total_seconds": 5,
          "input_seconds": 0,
          "output_seconds": 5,
          "input_image_count": 2,
          "total_tokens": 156235,
          "prompt_tokens": 26040,
          "completion_tokens": 130195
        },
        "ratio": "adaptive",
        "task_type": "generation"
      }
    }

**Mascot Reference Shot** — Keep a character consistent from a reference image in a new scene.
    
    
    const response = await env.AI.run(
      'minimax/h3-highspeed',
      {
        content: [
          {
            type: 'text',
            text: "The robot mascot from the reference image rolls a pencil across the wooden desk, looks up at the camera and gives a thumbs-up. Keep the mascot's shape, colors and antenna exactly as in the reference. Warm morning light, shallow depth of field.",
          },
          {
            type: 'image_url',
            image_url: {
              url: 'https://examples.aig.cloudflare.com/klingai/kling-v4/inputs/mascot-desk.jpg',
            },
            role: 'reference_image',
          },
        ],
        duration: 5,
        ratio: 'adaptive',
        resolution: '768P',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/h3-highspeed",
      "input": {
        "content": [
          {
            "type": "text",
            "text": "The robot mascot from the reference image rolls a pencil across the wooden desk, looks up at the camera and gives a thumbs-up. Keep the mascot'\''s shape, colors and antenna exactly as in the reference. Warm morning light, shallow depth of field."
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "https://examples.aig.cloudflare.com/klingai/kling-v4/inputs/mascot-desk.jpg"
            },
            "role": "reference_image"
          }
        ],
        "duration": 5,
        "ratio": "adaptive",
        "resolution": "768P"
      }
    }'
    
    
    {
      "task": {
        "id": "457315037172263",
        "model": "MiniMax-H3-Highspeed",
        "status": "succeeded",
        "created_at": 1793202462,
        "updated_at": 1793202477,
        "content": {
          "url": "https://examples.aig.cloudflare.com/minimax/h3-highspeed/mascot-reference-shot.mp4"
        },
        "resolution": "768P",
        "duration": 5,
        "usage": {
          "total_seconds": 5,
          "input_seconds": 0,
          "output_seconds": 5,
          "input_image_count": 1,
          "total_tokens": 143215,
          "prompt_tokens": 13020,
          "completion_tokens": 130195
        },
        "ratio": "adaptive",
        "task_type": "generation"
      }
    }

## Parameters

▶content[]

`array`requiredminItems: 1

duration

`integer`requiredminimum: 4maximum: 15

ratio

`string`enum: adaptive, 21:9, 16:9, 4:3, 1:1, 3:4, 9:16

callback_url

`string`format: uri

resolution

`string`requiredenum: 768P

▶task{}

`object`

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/minimax/h3-highspeed/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/minimax/h3-highspeed/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/minimax/h3-highspeed/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/minimax/h3-highspeed/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

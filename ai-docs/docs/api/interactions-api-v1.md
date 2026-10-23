---
url: https://ai.google.dev/api/interactions-api-v1/
title: Gemini Interactions API
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:00:19.939464+00:00
---

# Gemini Interactions API

> Source: https://ai.google.dev/api/interactions-api-v1/

The Gemini Interactions API allows developers to build generative AI applications using Gemini models. Gemini is our most capable model, built from the ground up to be multimodal. It can generalize and seamlessly understand, operate across, and combine different types of information including language, images, audio, video, and code. You can use the Gemini API for use cases like reasoning across text and images, content generation, dialogue agents, summarization and classification systems, and more.

[View as markdown](https://ai.google.dev/static/api/interactions-v1.md.txt) [View the OpenAPI Spec](https://ai.google.dev/static/api/interactions-v1.openapi.json)

API version: [v1beta](https://ai.google.dev/api/interactions-api) v1

## Creating an interaction

post  https://generativelanguage.googleapis.com/v1/interactions 

Creates a new interaction.

  * Request body
  * Response



### Request body

The request body contains data with the following structure:

model ModelOption (optional)

The name of the `Model` used for generating the interaction.   
**Required if `agent` is not provided.**

The model that will complete your prompt.\n\nSee [models](https://ai.google.dev/gemini-api/docs/models) for additional details.

#### Possible values

  * `models/gemini-2.5-flash-lite`

Our smallest and most cost effective model, built for at scale usage.

  * `models/gemini-2.5-flash-image`

Our native image generation model, optimized for speed, flexibility, and contextual understanding. Text input and output is priced the same as 2.5 Flash.

  * `models/gemini-3.1-flash-lite`

Our most cost-efficient model, optimized for high-volume agentic tasks, translation, and simple data processing.

  * `models/gemini-3.1-flash-image`

Pro-level visual intelligence with Flash-speed efficiency and reality-grounded generation capabilities.

  * `models/gemini-3.5-flash`

Our most intelligent model for sustained frontier performance in agentic and coding tasks.

  * `models/gemini-3.6-flash`

Our most intelligent model for sustained frontier performance in agentic and coding tasks.

  * `models/gemini-3.7-flash`

Our most intelligent model for sustained frontier performance in agentic and coding tasks.




agent AgentOption (optional)

The name of the `Agent` used for generating the interaction.   
**Required if `model` is not provided.**

The agent to interact with.

#### Possible values

  * `deep-research-pro-preview-12-2025`

Gemini Deep Research Agent

  * `deep-research-preview-04-2026`

Gemini Deep Research Agent

  * `deep-research-max-preview-04-2026`

Gemini Deep Research Max Agent

  * `antigravity-preview-05-2026`

Use the Antigravity managed agent to perform multi-step tasks that require reasoning, file operations, and tool use.




input Content or array (Content) or array (Step) or string (required)

The inputs for the interaction (common to both Model and Agent).

generation_config GenerationConfig (optional)

**Model Configuration**  
Configuration parameters for the model interaction.   
_Alternative to `agent_config`. Only applicable when `model` is set._

Configuration parameters for model interactions.

#### Fields

tool_choice ToolChoiceConfig or enum (string) (optional)

The tool choice configuration.

Possible values:

  * `auto`

Auto tool choice.

  * `any`

Any tool choice.

  * `none`

No tool choice.

  * `validated`

Validated tool choice.




seed integer (optional)

Seed used in decoding for reproducibility.

stop_sequences array (string) (optional)

A list of character sequences that will stop output interaction.

thinking_level ThinkingLevel (optional)

The level of thought tokens that the model should generate.

#### Possible values

  * `minimal`

Little to no thinking.

  * `low`

Low thinking level.

  * `medium`

Medium thinking level.

  * `high`

High thinking level.




thinking_summaries ThinkingSummaries (optional)

Whether to include thought summaries in the response.

#### Possible values

  * `auto`

Auto thinking summaries.

  * `none`

No thinking summaries.




max_output_tokens integer (optional)

The maximum number of tokens to include in the response.

video_config VideoConfig (optional)

Configuration for video generation.

Configuration options for video generation.

#### Fields

task enum (string) (optional)

Optional task mode for video generation. If not specified, the model automatically determines the appropriate mode based on the provided text prompt and input media.

Possible values:

  * `text_to_video`

Generates video solely from a text prompt.

  * `image_to_video`

Generates video from one or two source images. The first image defines the starting frame, and the optional second image defines the ending frame.

  * `reference_to_video`

Generates video using reference media (such as images, audio, or video).

  * `edit`

Modifies an existing input video.

  * `extend`

Extends an existing input video.




agent_config DynamicAgentConfig (optional)

**Agent Configuration**  
Configuration for the agent.   
_Alternative to `generation_config`. Only applicable when `agent` is set._

Configuration for dynamic agents.

#### Fields

type object (required)

No description provided.

Always set to `"dynamic"`.

response_format ResponseFormat or array (ResponseFormat) (optional)

Enforces that the generated response is a JSON object that complies with the JSON schema specified in this field.

system_instruction string (optional)

System instruction for the interaction.

tools array (Tool) (optional)

A list of tool declarations the model may call during interaction.

previous_interaction_id string (optional)

The ID of the previous interaction, if any.

service_tier ServiceTier (optional)

The service tier for the interaction.

#### Possible values

  * `flex`

Flex service tier.

  * `standard`

Standard service tier.

  * `priority`

Priority service tier.




safety_settings array (SafetySetting) (optional)

Safety settings for the interaction.

A safety setting that affects the safety-blocking behavior. A SafetySetting consists of a harm category and a threshold for that category.

#### Fields

type HarmCategory (required)

Required. The type of harm category to be blocked.

#### Possible values

  * `hate_speech`

Content that promotes violence or incites hatred against individuals or groups based on certain attributes.

  * `dangerous_content`

Content that promotes, facilitates, or enables dangerous activities.

  * `harassment`

Abusive, threatening, or content intended to bully, torment, or ridicule.

  * `sexually_explicit`

Content that contains sexually explicit material.

  * `jailbreak`

Prompts designed to bypass safety filters.




threshold enum (string) (required)

Required. The threshold for blocking content. If the harm probability exceeds this threshold, the content will be blocked.

Possible values:

  * `block_low_and_above`

Block content with a low harm probability or higher.

  * `block_medium_and_above`

Block content with a medium harm probability or higher.

  * `block_only_high`

Block content with a high harm probability.

  * `off`

Turn off the safety filter entirely.




method enum (string) (optional)

Optional. The method for blocking content. If not specified, the default behavior is to use the probability score.

Possible values:

  * `severity`

The harm block method uses both probability and severity scores.

  * `probability`

The harm block method uses the probability score.




stream boolean (optional)

Input only. Whether the interaction will be streamed.

store boolean (optional)

Input only. Whether to store the response and request for later retrieval.

background boolean (optional)

Input only. Whether to run the model interaction in the background.

### Response

Returns an Interaction resource.

### Simple Request

####  Example Response
    
    
    {
      "created": "2025-11-26T12:25:15Z",
      "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
      "model": "gemini-3.6-flash",
      "object": "interaction",
      "status": "completed",
      "steps": [
        {
          "type": "model_output",
          "content": [
            {
              "type": "text",
              "text": "Hello! I'm functioning perfectly and ready to assist you.\n\nHow are you doing today?"
            }
          ]
        }
      ],
      "updated": "2025-11-26T12:25:15Z",
      "usage": {
        "input_tokens_by_modality": [
          {
            "modality": "text",
            "tokens": 7
          }
        ],
        "total_cached_tokens": 0,
        "total_input_tokens": 7,
        "total_output_tokens": 20,
        "total_thought_tokens": 22,
        "total_tokens": 49,
        "total_tool_use_tokens": 0
      }
    }

### Multi-turn

####  Example Response
    
    
    {
      "created": "2025-11-26T12:22:47Z",
      "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
      "model": "gemini-3.6-flash",
      "object": "interaction",
      "status": "completed",
      "steps": [
        {
          "type": "model_output",
          "content": [
            {
              "type": "text",
              "text": "The capital of France is Paris."
            }
          ]
        }
      ],
      "updated": "2025-11-26T12:22:47Z",
      "usage": {
        "input_tokens_by_modality": [
          {
            "modality": "text",
            "tokens": 50
          }
        ],
        "total_cached_tokens": 0,
        "total_input_tokens": 50,
        "total_output_tokens": 10,
        "total_thought_tokens": 0,
        "total_tokens": 60,
        "total_tool_use_tokens": 0
      }
    }

### Image Input

####  Example Response
    
    
    {
      "created": "2025-11-26T12:22:47Z",
      "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
      "model": "gemini-3.6-flash",
      "object": "interaction",
      "status": "completed",
      "steps": [
        {
          "type": "model_output",
          "content": [
            {
              "type": "text",
              "text": "A white humanoid robot with glowing blue eyes stands holding a red skateboard."
            }
          ]
        }
      ],
      "updated": "2025-11-26T12:22:47Z",
      "usage": {
        "input_tokens_by_modality": [
          {
            "modality": "text",
            "tokens": 10
          },
          {
            "modality": "image",
            "tokens": 258
          }
        ],
        "total_cached_tokens": 0,
        "total_input_tokens": 268,
        "total_output_tokens": 20,
        "total_thought_tokens": 0,
        "total_tokens": 288,
        "total_tool_use_tokens": 0
      }
    }

### Function Calling

####  Example Response
    
    
    {
      "created": "2025-11-26T12:22:47Z",
      "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
      "model": "gemini-3.6-flash",
      "object": "interaction",
      "status": "requires_action",
      "steps": [
        {
          "name": "get_weather",
          "type": "function_call",
          "arguments": {
            "location": "Boston, MA"
          },
          "id": "gth23981"
        }
      ],
      "updated": "2025-11-26T12:22:47Z",
      "usage": {
        "input_tokens_by_modality": [
          {
            "modality": "text",
            "tokens": 100
          }
        ],
        "total_cached_tokens": 0,
        "total_input_tokens": 100,
        "total_output_tokens": 25,
        "total_thought_tokens": 0,
        "total_tokens": 125,
        "total_tool_use_tokens": 50
      }
    }

### Deep Research

### Antigravity

### Reuse Env

### With Sources

### Custom Agent

## Canceling an interaction

post  https://generativelanguage.googleapis.com/v1/interactions/{id}/cancel 

Cancels an interaction by id. This only applies to background interactions that are still running.

  * Path / Query parameters
  * Response



### Path / Query Parameters

api_version string (required)

API version for request routing.

id string (required)

The unique identifier of the interaction to cancel.

### Response

Returns an Interaction resource.

### Cancel Interaction

####  Example Response
    
    
    {
      "created": "2025-11-26T12:25:15Z",
      "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
      "model": "gemini-3.6-flash",
      "object": "interaction",
      "status": "cancelled",
      "updated": "2025-11-26T12:25:15Z"
    }

## Retrieving an interaction

get  https://generativelanguage.googleapis.com/v1/interactions/{id} 

Retrieves the full details of a single interaction based on its `Interaction.id`.

  * Path / Query parameters
  * Response



### Path / Query Parameters

api_version string (required)

API version for request routing.

id string (required)

The unique identifier of the interaction to retrieve.

last_event_id string (optional)

Optional. If set, resumes the interaction stream from the next chunk after the event marked by the event id. Can only be used if `stream` is true.

stream boolean (optional)

If set to true, the generated content will be streamed incrementally.

_Defaults to:`False`_

### Response

Returns an Interaction resource.

### Get Interaction

####  Example Response
    
    
    {
      "created": "2025-11-26T12:25:15Z",
      "id": "v1_ChdPU0F4YWFtNkFwS2kxZThQZ05lbXdROBIXT1NBeGFhbTZBcEtpMWU4UGdOZW13UTg",
      "model": "gemini-3.6-flash",
      "object": "interaction",
      "status": "completed",
      "steps": [
        {
          "type": "model_output",
          "content": [
            {
              "type": "text",
              "text": "I'm doing great, thank you for asking! How can I help you today?"
            }
          ]
        }
      ],
      "updated": "2025-11-26T12:25:15Z"
    }

## Deleting an interaction

delete  https://generativelanguage.googleapis.com/v1/interactions/{id} 

Deletes the interaction by id.

  * Path / Query parameters
  * Response



### Path / Query Parameters

api_version string (required)

API version for request routing.

id string (required)

The unique identifier of the interaction to delete.

interactionsId string (required)

Required. The name of the interaction to delete.

### Response

If successful, the response is empty.

### Delete

## Resources

### Interaction

The Interaction resource.

#### Fields

id string (required)

Required. Output only. A unique identifier for the interaction completion.

status enum (string) (required)

Required. Output only. The status of the interaction.

Possible values:

  * `in_progress`

The interaction is in progress.

  * `requires_action`

The interaction requires action/input from the user.

  * `completed`

The interaction is completed.

  * `failed`

The interaction failed.

  * `cancelled`

The interaction was cancelled.

  * `incomplete`

The interaction is completed, but contains incomplete results (e.g. hitting max_tokens).




created string (required)

Required. Output only. The time at which the response was created in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).

updated string (required)

Required. Output only. The time at which the response was last updated in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).

steps array (Step) (required)

Required. Output only. The steps that make up the interaction, when included in the response.

model ModelOption (optional)

The name of the `Model` used for generating the interaction.

The model that will complete your prompt.\n\nSee [models](https://ai.google.dev/gemini-api/docs/models) for additional details.

#### Possible values

  * `models/gemini-2.5-flash-lite`

Our smallest and most cost effective model, built for at scale usage.

  * `models/gemini-2.5-flash-image`

Our native image generation model, optimized for speed, flexibility, and contextual understanding. Text input and output is priced the same as 2.5 Flash.

  * `models/gemini-3.1-flash-lite`

Our most cost-efficient model, optimized for high-volume agentic tasks, translation, and simple data processing.

  * `models/gemini-3.1-flash-image`

Pro-level visual intelligence with Flash-speed efficiency and reality-grounded generation capabilities.

  * `models/gemini-3.5-flash`

Our most intelligent model for sustained frontier performance in agentic and coding tasks.

  * `models/gemini-3.6-flash`

Our most intelligent model for sustained frontier performance in agentic and coding tasks.

  * `models/gemini-3.7-flash`

Our most intelligent model for sustained frontier performance in agentic and coding tasks.




input Content or array (Content) or array (Step) or string (optional)

The input for the interaction.

response_format ResponseFormat or array (ResponseFormat) (optional)

Enforces that the generated response is a JSON object that complies with the JSON schema specified in this field.

system_instruction string (optional)

System instruction for the interaction.

tools array (Tool) (optional)

A list of tool declarations the model may call during interaction.

usage Usage (optional)

Output only. Statistics on the interaction request's token usage.

Statistics on the interaction request's token usage.

#### Fields

total_input_tokens integer (optional)

Number of tokens in the prompt (context).

input_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of input token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_cached_tokens integer (optional)

Number of tokens in the cached part of the prompt (the cached content).

cached_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of cached token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_output_tokens integer (optional)

Total number of tokens across all the generated responses.

output_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of output token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_tool_use_tokens integer (optional)

Number of tokens present in tool-use prompt(s).

tool_use_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of tool-use token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_thought_tokens integer (optional)

Number of tokens of thoughts for thinking models.

total_tokens integer (optional)

Total token count for the interaction request (prompt + responses + other internal tokens).

grounding_tool_count array (GroundingToolCount) (optional)

Grounding tool count.

The number of grounding tool counts.

#### Fields

type enum (string) (optional)

The grounding tool type associated with the count.

Possible values:

  * `google_search`

Grounding with Google Web Search and Image Search, & Web Grounding for Enterprise.

  * `google_maps`

Grounding with Google Maps.




count integer (optional)

The number of grounding tool counts.

previous_interaction_id string (optional)

The ID of the previous interaction, if any.

service_tier ServiceTier (optional)

The service tier for the interaction.

#### Possible values

  * `flex`

Flex service tier.

  * `standard`

Standard service tier.

  * `priority`

Priority service tier.




safety_settings array (SafetySetting) (optional)

Safety settings for the interaction.

A safety setting that affects the safety-blocking behavior. A SafetySetting consists of a harm category and a threshold for that category.

#### Fields

type HarmCategory (required)

Required. The type of harm category to be blocked.

#### Possible values

  * `hate_speech`

Content that promotes violence or incites hatred against individuals or groups based on certain attributes.

  * `dangerous_content`

Content that promotes, facilitates, or enables dangerous activities.

  * `harassment`

Abusive, threatening, or content intended to bully, torment, or ridicule.

  * `sexually_explicit`

Content that contains sexually explicit material.

  * `jailbreak`

Prompts designed to bypass safety filters.




threshold enum (string) (required)

Required. The threshold for blocking content. If the harm probability exceeds this threshold, the content will be blocked.

Possible values:

  * `block_low_and_above`

Block content with a low harm probability or higher.

  * `block_medium_and_above`

Block content with a medium harm probability or higher.

  * `block_only_high`

Block content with a high harm probability.

  * `off`

Turn off the safety filter entirely.




method enum (string) (optional)

Optional. The method for blocking content. If not specified, the default behavior is to use the probability score.

Possible values:

  * `severity`

The harm block method uses both probability and severity scores.

  * `probability`

The harm block method uses the probability score.




errors array (Error) (optional)

Output only. Diagnostic faults / platform errors recorded on the interaction.

Error message from an interaction.

#### Fields

code string (optional)

A URI that identifies the error type.

message string (optional)

A human-readable error message.

agent AgentOption (optional)

The name of the `Agent` used for generating the interaction.

The agent to interact with.

#### Possible values

  * `deep-research-pro-preview-12-2025`

Gemini Deep Research Agent

  * `deep-research-preview-04-2026`

Gemini Deep Research Agent

  * `deep-research-max-preview-04-2026`

Gemini Deep Research Max Agent

  * `antigravity-preview-05-2026`

Use the Antigravity managed agent to perform multi-step tasks that require reasoning, file operations, and tool use.




agent_config DynamicAgentConfig (optional)

Configuration parameters for the agent interaction.

Configuration for dynamic agents.

#### Fields

type object (required)

No description provided.

Always set to `"dynamic"`.

max_total_tokens string (optional)

Max total tokens for the agent run.

### Examples

### Example
    
    
    {
      "created": "2025-12-04T15:01:45Z",
      "id": "v1_ChdXS0l4YWZXTk9xbk0xZThQczhEcmlROBIXV0tJeGFmV05PcW5NMWU4UHM4RHJpUTg",
      "model": "gemini-3.6-flash",
      "object": "interaction",
      "status": "completed",
      "steps": [
        {
          "type": "model_output",
          "content": [
            {
              "type": "text",
              "text": "Hello! I'm doing well, functioning as expected. Thank you for asking! How are you doing today?"
            }
          ]
        }
      ],
      "updated": "2025-12-04T15:01:45Z",
      "usage": {
        "input_tokens_by_modality": [
          {
            "modality": "text",
            "tokens": 7
          }
        ],
        "total_cached_tokens": 0,
        "total_input_tokens": 7,
        "total_output_tokens": 23,
        "total_thought_tokens": 49,
        "total_tokens": 79,
        "total_tool_use_tokens": 0
      }
    }

## Data Models

### Content

The content of the response.

### Possible Types

AudioContent

An audio content block.

type object (required)

No description provided.

Always set to `"audio"`.

data string (optional)

The audio content.

uri string (optional)

The URI of the audio.

channels integer (optional)

The number of audio channels.

sample_rate integer (optional)

The sample rate of the audio.

mime_type enum (string) (optional)

The mime type of the audio.

Possible values:

  * `audio/wav`

WAV audio format

  * `audio/mp3`

MP3 audio format

  * `audio/aiff`

AIFF audio format

  * `audio/aac`

AAC audio format

  * `audio/ogg`

OGG audio format

  * `audio/flac`

FLAC audio format

  * `audio/mpeg`

MPEG audio format

  * `audio/m4a`

M4A audio format

  * `audio/l16`

L16 audio format

  * `audio/opus`

OPUS audio format

  * `audio/alaw`

ALAW audio format

  * `audio/mulaw`

MULAW audio format

  * `audio/webm`

WEBM audio format




DocumentContent

A document content block.

type object (required)

No description provided.

Always set to `"document"`.

data string (optional)

The document content.

uri string (optional)

The URI of the document.

mime_type enum (string) (optional)

The mime type of the document.

Possible values:

  * `application/pdf`

PDF document format

  * `text/csv`

CSV document format




ImageContent

An image content block.

type object (required)

No description provided.

Always set to `"image"`.

data string (optional)

The image content.

uri string (optional)

The URI of the image.

resolution MediaResolution (optional)

The resolution of the media.

#### Possible values

  * `low`

Low resolution.

  * `medium`

Medium resolution.

  * `high`

High resolution.

  * `ultra_high`

Ultra high resolution.




mime_type enum (string) (optional)

The mime type of the image.

Possible values:

  * `image/png`

PNG image format

  * `image/jpeg`

JPEG image format

  * `image/webp`

WebP image format

  * `image/heic`

HEIC image format

  * `image/heif`

HEIF image format

  * `image/gif`

GIF image format

  * `image/bmp`

BMP image format

  * `image/tiff`

TIFF image format




TextContent

A text content block.

text string (required)

Required. The text content.

type object (required)

No description provided.

Always set to `"text"`.

annotations array (Annotation) (optional)

Citation information for model-generated content.

Citation information for model-generated content.

#### Possible Types

FileCitation

A file citation annotation.

type object (required)

No description provided.

Always set to `"file_citation"`.

document_uri string (optional)

The URI of the file.

file_name string (optional)

The name of the file.

source string (optional)

Source attributed for a portion of the text.

custom_metadata object (optional)

User provided metadata about the retrieved context.

page_number integer (optional)

Page number of the cited document, if applicable.

media_id string (optional)

Media ID in-case of image citations, if applicable.

start_index integer (optional)

Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

end_index integer (optional)

End of the attributed segment, exclusive.

PlaceCitation

A place citation annotation.

type object (required)

No description provided.

Always set to `"place_citation"`.

place_id string (optional)

The ID of the place, in `places/{place_id}` format.

name string (optional)

Title of the place.

url string (optional)

URI reference of the place.

review_snippets array (ReviewSnippet) (optional)

Snippets of reviews that are used to generate answers about the features of a given place in Google Maps.

Encapsulates a snippet of a user review that answers a question about the features of a specific place in Google Maps.

#### Fields

title string (optional)

Title of the review.

url string (optional)

A link that corresponds to the user review on Google Maps.

review_id string (optional)

The ID of the review snippet.

start_index integer (optional)

Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

end_index integer (optional)

End of the attributed segment, exclusive.

UrlCitation

A URL citation annotation.

type object (required)

No description provided.

Always set to `"url_citation"`.

url string (optional)

The URL.

title string (optional)

The title of the URL.

start_index integer (optional)

Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

end_index integer (optional)

End of the attributed segment, exclusive.

VideoContent

A video content block.

type object (required)

No description provided.

Always set to `"video"`.

data string (optional)

The video content.

uri string (optional)

The URI of the video.

processing MediaProcessing or enum (string) (optional)

How the model processes this video for understanding.

Can be a string (`"static"` | `"agentic"`) or a `StaticMediaProcessing` object:

  * `agentic`: Model-driven dynamic navigation. 
  * `static`: Fixed-rate frame extraction. All frames placed in context. Can be passed as the string `"static"`, or as an object with the following fields: 

type string (required)

No description provided.

Always set to `"static"`.

start_offset string (optional)

Optional. Segment start time. Specified as a decimal number of seconds followed by an 's' suffix, e.g., "10.5s". Must be non-negative.

end_offset string (optional)

Optional. Segment end time. Specified as a decimal number of seconds followed by an 's' suffix, e.g., "30s". Must be non-negative and greater than `start_offset` if `start_offset` is set.

fps number (optional)

Optional. Video frame-rate sampling density.




resolution MediaResolution (optional)

The resolution of the media.

#### Possible values

  * `low`

Low resolution.

  * `medium`

Medium resolution.

  * `high`

High resolution.

  * `ultra_high`

Ultra high resolution.




name string (optional)

A user-defined name for this content block. Can be referenced by the model in the final response.

mime_type enum (string) (optional)

The mime type of the video.

Possible values:

  * `video/mp4`

MP4 video format

  * `video/mpeg`

MPEG video format

  * `video/mpg`

MPG video format

  * `video/mov`

MOV video format

  * `video/avi`

AVI video format

  * `video/x-flv`

FLV video format

  * `video/webm`

WebM video format

  * `video/wmv`

WMV video format

  * `video/3gpp`

3GPP video format

  * `video/jpeg2000`

JPEG 2000 video format




### Examples

### Audio
    
    
    {
      "type": "audio",
      "data": "BASE64_ENCODED_AUDIO",
      "mime_type": "audio/wav"
    }

### Document
    
    
    {
      "type": "document",
      "data": "BASE64_ENCODED_DOCUMENT",
      "mime_type": "application/pdf"
    }

### Image
    
    
    {
      "type": "image",
      "data": "BASE64_ENCODED_IMAGE",
      "mime_type": "image/png"
    }

### Text
    
    
    {
      "type": "text",
      "text": "Hello, how are you?"
    }

### VideoContent

No examples available for this type.

### Tool

A tool that can be used by the model.

### Possible Types

CodeExecution

A tool that can be used by the model to execute code.

type object (required)

No description provided.

Always set to `"code_execution"`.

FileSearch

A tool that can be used by the model to search files.

type object (required)

No description provided.

Always set to `"file_search"`.

file_search_store_names array (string) (optional)

The file search store names to search.

top_k integer (optional)

The number of semantic retrieval chunks to retrieve.

metadata_filter string (optional)

Metadata filter to apply to the semantic retrieval documents and chunks.

Function

A tool that can be used by the model.

type object (required)

No description provided.

Always set to `"function"`.

name string (optional)

The name of the function.

description string (optional)

A description of the function.

parameters object (optional)

The JSON Schema for the function's parameters. Supports a subset of JSON Schema. `minLength`, `maxLength`, `minProperties`, `maxProperties`, `uniqueItems`, `contains`, `minContains`, and `maxContains` are ignored and not enforced.

GoogleMaps

A tool that can be used by the model to call Google Maps.

type object (required)

No description provided.

Always set to `"google_maps"`.

enable_widget boolean (optional)

Whether to return a widget context token in the tool call result of the response.

latitude number (optional)

The latitude of the user's location.

longitude number (optional)

The longitude of the user's location.

GoogleSearch

A tool that can be used by the model to search Google.

type object (required)

No description provided.

Always set to `"google_search"`.

search_types array (enum (string)) (optional)

The types of search grounding to enable.

Possible values:

  * `web_search`

Setting this field enables web search. Only text results are returned.

  * `image_search`

Setting this field enables image search. Image bytes are returned.




McpServer

A MCPServer is a server that can be called by the model to perform actions.

type object (required)

No description provided.

Always set to `"mcp_server"`.

url string (optional)

The full URL for the MCPServer endpoint. Example: "https://api.example.com/mcp"

name string (optional)

The name of the MCPServer.

headers object (optional)

Optional: Fields for authentication headers, timeouts, etc., if needed.

allowed_tools array (AllowedTools) (optional)

The allowed tools.

The configuration for allowed tools.

#### Fields

mode enum (string) (optional)

The mode of the tool choice.

Possible values:

  * `auto`

Auto tool choice.

  * `any`

Any tool choice.

  * `none`

No tool choice.

  * `validated`

Validated tool choice.




tools array (string) (optional)

The names of the allowed tools.

UrlContext

A tool that can be used by the model to fetch URL context.

type object (required)

No description provided.

Always set to `"url_context"`.

### Examples

### CodeExecution

### FileSearch

### Function

### GoogleMaps

### GoogleSearch

### McpServer

### UrlContext

### InteractionSseEvent

### Possible Types

ErrorEvent

event_type object (required)

No description provided.

Always set to `"error"`.

error Error (optional)

No description provided.

Error message from an interaction.

#### Fields

code string (optional)

A URI that identifies the error type.

message string (optional)

A human-readable error message.

event_id string (optional)

The event_id token to be used to resume the interaction stream, from this event.

InteractionCompletedEvent

Signals that the Interaction completed. Sent when the Interaction receives Complete/Cancel or naturally terminates. No more input can be sent to the Interaction after this.

interaction InteractionSseEventInteraction (required)

Required. Partial completed interaction resource emitted at the end of the stream.

Partial interaction resource emitted by interaction lifecycle SSE events. Streaming lifecycle payloads may omit fields that are only available on full non-streaming Interaction responses. 

#### Fields

id string (required)

Required. Output only. A unique identifier for the interaction completion.

status enum (string) (required)

Required. Output only. The status of the interaction.

Possible values:

  * `in_progress`

The interaction is in progress.

  * `requires_action`

The interaction requires action/input from the user.

  * `completed`

The interaction is completed.

  * `failed`

The interaction failed.

  * `cancelled`

The interaction was cancelled.

  * `incomplete`

The interaction is completed, but contains incomplete results (e.g. hitting max_tokens).




model string (optional)

The model that will complete your prompt.

created string (optional)

Output only. The time at which the response was created in ISO 8601 format.

updated string (optional)

Output only. The time at which the response was last updated in ISO 8601 format.

usage Usage (optional)

Output only. Statistics on the interaction request's token usage.

Statistics on the interaction request's token usage.

#### Fields

total_input_tokens integer (optional)

Number of tokens in the prompt (context).

input_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of input token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_cached_tokens integer (optional)

Number of tokens in the cached part of the prompt (the cached content).

cached_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of cached token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_output_tokens integer (optional)

Total number of tokens across all the generated responses.

output_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of output token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_tool_use_tokens integer (optional)

Number of tokens present in tool-use prompt(s).

tool_use_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of tool-use token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_thought_tokens integer (optional)

Number of tokens of thoughts for thinking models.

total_tokens integer (optional)

Total token count for the interaction request (prompt + responses + other internal tokens).

grounding_tool_count array (GroundingToolCount) (optional)

Grounding tool count.

The number of grounding tool counts.

#### Fields

type enum (string) (optional)

The grounding tool type associated with the count.

Possible values:

  * `google_search`

Grounding with Google Web Search and Image Search, & Web Grounding for Enterprise.

  * `google_maps`

Grounding with Google Maps.




count integer (optional)

The number of grounding tool counts.

service_tier ServiceTier (optional)

The service tier for the interaction.

#### Possible values

  * `flex`

Flex service tier.

  * `standard`

Standard service tier.

  * `priority`

Priority service tier.




steps array (Step) (optional)

Output only. The steps that make up the interaction, if included in this event.

agent string (optional)

The agent to interact with.

object string (optional)

Output only. The resource type.

event_type object (required)

No description provided.

Always set to `"interaction.completed"`.

event_id string (optional)

The event_id token to be used to resume the interaction stream, from this event.

InteractionCreatedEvent

Server response confirming that a new interaction was created.

interaction InteractionSseEventInteraction (required)

Required. Partial interaction resource emitted when the stream is created.

Partial interaction resource emitted by interaction lifecycle SSE events. Streaming lifecycle payloads may omit fields that are only available on full non-streaming Interaction responses. 

#### Fields

id string (required)

Required. Output only. A unique identifier for the interaction completion.

status enum (string) (required)

Required. Output only. The status of the interaction.

Possible values:

  * `in_progress`

The interaction is in progress.

  * `requires_action`

The interaction requires action/input from the user.

  * `completed`

The interaction is completed.

  * `failed`

The interaction failed.

  * `cancelled`

The interaction was cancelled.

  * `incomplete`

The interaction is completed, but contains incomplete results (e.g. hitting max_tokens).




model string (optional)

The model that will complete your prompt.

created string (optional)

Output only. The time at which the response was created in ISO 8601 format.

updated string (optional)

Output only. The time at which the response was last updated in ISO 8601 format.

usage Usage (optional)

Output only. Statistics on the interaction request's token usage.

Statistics on the interaction request's token usage.

#### Fields

total_input_tokens integer (optional)

Number of tokens in the prompt (context).

input_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of input token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_cached_tokens integer (optional)

Number of tokens in the cached part of the prompt (the cached content).

cached_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of cached token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_output_tokens integer (optional)

Total number of tokens across all the generated responses.

output_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of output token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_tool_use_tokens integer (optional)

Number of tokens present in tool-use prompt(s).

tool_use_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of tool-use token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_thought_tokens integer (optional)

Number of tokens of thoughts for thinking models.

total_tokens integer (optional)

Total token count for the interaction request (prompt + responses + other internal tokens).

grounding_tool_count array (GroundingToolCount) (optional)

Grounding tool count.

The number of grounding tool counts.

#### Fields

type enum (string) (optional)

The grounding tool type associated with the count.

Possible values:

  * `google_search`

Grounding with Google Web Search and Image Search, & Web Grounding for Enterprise.

  * `google_maps`

Grounding with Google Maps.




count integer (optional)

The number of grounding tool counts.

service_tier ServiceTier (optional)

The service tier for the interaction.

#### Possible values

  * `flex`

Flex service tier.

  * `standard`

Standard service tier.

  * `priority`

Priority service tier.




steps array (Step) (optional)

Output only. The steps that make up the interaction, if included in this event.

agent string (optional)

The agent to interact with.

object string (optional)

Output only. The resource type.

event_type object (required)

No description provided.

Always set to `"interaction.created"`.

event_id string (optional)

The event_id token to be used to resume the interaction stream, from this event.

InteractionStatusUpdate

interaction_id string (required)

No description provided.

status enum (string) (required)

No description provided.

Possible values:

  * `in_progress`

The interaction is in progress.

  * `requires_action`

The interaction requires action/input from the user.

  * `completed`

The interaction is completed.

  * `failed`

The interaction failed.

  * `cancelled`

The interaction was cancelled.

  * `incomplete`

The interaction is completed, but contains incomplete results (e.g. hitting max_tokens).




event_type object (required)

No description provided.

Always set to `"interaction.status_update"`.

continuation_token string (optional)

An optional opaque continuation token used to resume decoding from the latest checkpoint after a disconnected stream.

usage Usage (optional)

Model usage statistics up to this checkpoint.

Statistics on the interaction request's token usage.

#### Fields

total_input_tokens integer (optional)

Number of tokens in the prompt (context).

input_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of input token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_cached_tokens integer (optional)

Number of tokens in the cached part of the prompt (the cached content).

cached_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of cached token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_output_tokens integer (optional)

Total number of tokens across all the generated responses.

output_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of output token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_tool_use_tokens integer (optional)

Number of tokens present in tool-use prompt(s).

tool_use_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of tool-use token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_thought_tokens integer (optional)

Number of tokens of thoughts for thinking models.

total_tokens integer (optional)

Total token count for the interaction request (prompt + responses + other internal tokens).

grounding_tool_count array (GroundingToolCount) (optional)

Grounding tool count.

The number of grounding tool counts.

#### Fields

type enum (string) (optional)

The grounding tool type associated with the count.

Possible values:

  * `google_search`

Grounding with Google Web Search and Image Search, & Web Grounding for Enterprise.

  * `google_maps`

Grounding with Google Maps.




count integer (optional)

The number of grounding tool counts.

event_id string (optional)

The event_id token to be used to resume the interaction stream, from this event.

StepDelta

index integer (required)

No description provided.

delta StepDeltaData (required)

No description provided.

#### Possible Types

ArgumentsDelta

type object (required)

No description provided.

Always set to `"arguments_delta"`.

arguments string (optional)

No description provided.

AudioDelta

type object (required)

No description provided.

Always set to `"audio"`.

data string (optional)

No description provided.

uri string (optional)

No description provided.

mime_type enum (string) (optional)

No description provided.

Possible values:

  * `audio/wav`

WAV audio format

  * `audio/mp3`

MP3 audio format

  * `audio/aiff`

AIFF audio format

  * `audio/aac`

AAC audio format

  * `audio/ogg`

OGG audio format

  * `audio/flac`

FLAC audio format

  * `audio/mpeg`

MPEG audio format

  * `audio/m4a`

M4A audio format

  * `audio/l16`

L16 audio format

  * `audio/opus`

OPUS audio format

  * `audio/alaw`

ALAW audio format

  * `audio/mulaw`

MULAW audio format

  * `audio/webm`

WEBM audio format




sample_rate integer (optional)

The sample rate of the audio.

channels integer (optional)

The number of audio channels.

CodeExecutionCallDelta

arguments CodeExecutionCallArguments (required)

No description provided.

The arguments to pass to the code execution.

#### Fields

language enum (string) (optional)

Programming language of the `code`.

Possible values:

  * `python`

Python >= 3.10, with numpy and simpy available.

  * `bash`

Bash. Only available for Gemini 3.0 model or above.




code string (optional)

The code to be executed.

type object (required)

No description provided.

Always set to `"code_execution_call"`.

signature string (optional)

A signature hash for backend validation.

CodeExecutionResultDelta

result string (required)

No description provided.

type object (required)

No description provided.

Always set to `"code_execution_result"`.

is_error boolean (optional)

No description provided.

signature string (optional)

A signature hash for backend validation.

DocumentDelta

type object (required)

No description provided.

Always set to `"document"`.

data string (optional)

No description provided.

uri string (optional)

No description provided.

mime_type enum (string) (optional)

No description provided.

Possible values:

  * `application/pdf`

PDF document format

  * `text/csv`

CSV document format




FileSearchCallDelta

type object (required)

No description provided.

Always set to `"file_search_call"`.

signature string (optional)

A signature hash for backend validation.

FileSearchResultDelta

result array (FileSearchResult) (required)

No description provided.

The result of the File Search.

type object (required)

No description provided.

Always set to `"file_search_result"`.

signature string (optional)

A signature hash for backend validation.

FunctionResultDelta

result array (ImageContent or TextContent) or object or string (required)

No description provided.

type object (required)

No description provided.

Always set to `"function_result"`.

name string (optional)

No description provided.

is_error boolean (optional)

No description provided.

GoogleMapsCallDelta

type object (required)

No description provided.

Always set to `"google_maps_call"`.

arguments GoogleMapsCallArguments (optional)

The arguments to pass to the Google Maps tool.

The arguments to pass to the Google Maps tool.

#### Fields

queries array (string) (optional)

The queries to be executed.

signature string (optional)

A signature hash for backend validation.

GoogleMapsResultDelta

type object (required)

No description provided.

Always set to `"google_maps_result"`.

result array (GoogleMapsResult) (optional)

The results of the Google Maps.

The result of the Google Maps.

#### Fields

places array (Places) (optional)

The places that were found.

#### Fields

place_id string (optional)

The ID of the place, in `places/{place_id}` format.

name string (optional)

Title of the place.

url string (optional)

URI reference of the place.

review_snippets array (ReviewSnippet) (optional)

Snippets of reviews that are used to generate answers about the features of a given place in Google Maps.

Encapsulates a snippet of a user review that answers a question about the features of a specific place in Google Maps.

#### Fields

title string (optional)

Title of the review.

url string (optional)

A link that corresponds to the user review on Google Maps.

review_id string (optional)

The ID of the review snippet.

widget_context_token string (optional)

Resource name of the Google Maps widget context token.

signature string (optional)

A signature hash for backend validation.

GoogleSearchCallDelta

arguments GoogleSearchCallArguments (required)

No description provided.

The arguments to pass to Google Search.

#### Fields

queries array (string) (optional)

Web search queries for the following-up web search.

type object (required)

No description provided.

Always set to `"google_search_call"`.

signature string (optional)

A signature hash for backend validation.

GoogleSearchResultDelta

result array (GoogleSearchResult) (required)

No description provided.

The result of the Google Search.

#### Fields

search_suggestions string (optional)

Web content snippet that can be embedded in a web page or an app webview.

type object (required)

No description provided.

Always set to `"google_search_result"`.

is_error boolean (optional)

No description provided.

signature string (optional)

A signature hash for backend validation.

ImageDelta

type object (required)

No description provided.

Always set to `"image"`.

data string (optional)

No description provided.

uri string (optional)

No description provided.

mime_type enum (string) (optional)

No description provided.

Possible values:

  * `image/png`

PNG image format

  * `image/jpeg`

JPEG image format

  * `image/webp`

WebP image format

  * `image/heic`

HEIC image format

  * `image/heif`

HEIF image format

  * `image/gif`

GIF image format

  * `image/bmp`

BMP image format

  * `image/tiff`

TIFF image format




resolution MediaResolution (optional)

The resolution of the media.

#### Possible values

  * `low`

Low resolution.

  * `medium`

Medium resolution.

  * `high`

High resolution.

  * `ultra_high`

Ultra high resolution.




McpServerToolCallDelta

name string (required)

No description provided.

server_name string (required)

No description provided.

arguments object (required)

No description provided.

type object (required)

No description provided.

Always set to `"mcp_server_tool_call"`.

McpServerToolResultDelta

result array (ImageContent or TextContent) or object or string (required)

No description provided.

type object (required)

No description provided.

Always set to `"mcp_server_tool_result"`.

name string (optional)

No description provided.

server_name string (optional)

No description provided.

TextAnnotationDelta

type object (required)

No description provided.

Always set to `"text_annotation_delta"`.

annotations array (Annotation) (optional)

Citation information for model-generated content.

Citation information for model-generated content.

#### Possible Types

FileCitation

A file citation annotation.

type object (required)

No description provided.

Always set to `"file_citation"`.

document_uri string (optional)

The URI of the file.

file_name string (optional)

The name of the file.

source string (optional)

Source attributed for a portion of the text.

custom_metadata object (optional)

User provided metadata about the retrieved context.

page_number integer (optional)

Page number of the cited document, if applicable.

media_id string (optional)

Media ID in-case of image citations, if applicable.

start_index integer (optional)

Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

end_index integer (optional)

End of the attributed segment, exclusive.

PlaceCitation

A place citation annotation.

type object (required)

No description provided.

Always set to `"place_citation"`.

place_id string (optional)

The ID of the place, in `places/{place_id}` format.

name string (optional)

Title of the place.

url string (optional)

URI reference of the place.

review_snippets array (ReviewSnippet) (optional)

Snippets of reviews that are used to generate answers about the features of a given place in Google Maps.

Encapsulates a snippet of a user review that answers a question about the features of a specific place in Google Maps.

#### Fields

title string (optional)

Title of the review.

url string (optional)

A link that corresponds to the user review on Google Maps.

review_id string (optional)

The ID of the review snippet.

start_index integer (optional)

Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

end_index integer (optional)

End of the attributed segment, exclusive.

UrlCitation

A URL citation annotation.

type object (required)

No description provided.

Always set to `"url_citation"`.

url string (optional)

The URL.

title string (optional)

The title of the URL.

start_index integer (optional)

Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

end_index integer (optional)

End of the attributed segment, exclusive.

TextDelta

text string (required)

No description provided.

type object (required)

No description provided.

Always set to `"text"`.

ThoughtSignatureDelta

type object (required)

No description provided.

Always set to `"thought_signature"`.

signature string (optional)

Signature to match the backend source to be part of the generation.

ThoughtSummaryDelta

type object (required)

No description provided.

Always set to `"thought_summary"`.

content Content (optional)

A new summary item to be added to the thought.

UrlContextCallDelta

arguments UrlContextCallArguments (required)

No description provided.

The arguments to pass to the URL context.

#### Fields

urls array (string) (optional)

The URLs to fetch.

type object (required)

No description provided.

Always set to `"url_context_call"`.

signature string (optional)

A signature hash for backend validation.

UrlContextResultDelta

result array (UrlContextResult) (required)

No description provided.

The result of the URL context.

#### Fields

url string (optional)

The URL that was fetched.

status enum (string) (optional)

The status of the URL retrieval.

Possible values:

  * `success`

Url retrieval is successful.

  * `error`

Url retrieval is failed due to error.

  * `paywall`

Url retrieval is failed because the content is behind paywall.

  * `unsafe`

Url retrieval is failed because the content is unsafe.




type object (required)

No description provided.

Always set to `"url_context_result"`.

is_error boolean (optional)

No description provided.

signature string (optional)

A signature hash for backend validation.

VideoDelta

type object (required)

No description provided.

Always set to `"video"`.

data string (optional)

No description provided.

uri string (optional)

No description provided.

mime_type enum (string) (optional)

No description provided.

Possible values:

  * `video/mp4`

MP4 video format

  * `video/mpeg`

MPEG video format

  * `video/mpg`

MPG video format

  * `video/mov`

MOV video format

  * `video/avi`

AVI video format

  * `video/x-flv`

FLV video format

  * `video/webm`

WebM video format

  * `video/wmv`

WMV video format

  * `video/3gpp`

3GPP video format

  * `video/jpeg2000`

JPEG 2000 video format




resolution MediaResolution (optional)

The resolution of the media.

#### Possible values

  * `low`

Low resolution.

  * `medium`

Medium resolution.

  * `high`

High resolution.

  * `ultra_high`

Ultra high resolution.




event_type object (required)

No description provided.

Always set to `"step.delta"`.

event_id string (optional)

The event_id token to be used to resume the interaction stream, from this event.

metadata StepDeltaMetadata (optional)

No description provided.

Optional metadata accompanying ANY streamed event.

#### Fields

total_usage Usage (optional)

Statistics on the interaction request's token usage.

Statistics on the interaction request's token usage.

#### Fields

total_input_tokens integer (optional)

Number of tokens in the prompt (context).

input_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of input token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_cached_tokens integer (optional)

Number of tokens in the cached part of the prompt (the cached content).

cached_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of cached token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_output_tokens integer (optional)

Total number of tokens across all the generated responses.

output_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of output token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_tool_use_tokens integer (optional)

Number of tokens present in tool-use prompt(s).

tool_use_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of tool-use token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_thought_tokens integer (optional)

Number of tokens of thoughts for thinking models.

total_tokens integer (optional)

Total token count for the interaction request (prompt + responses + other internal tokens).

grounding_tool_count array (GroundingToolCount) (optional)

Grounding tool count.

The number of grounding tool counts.

#### Fields

type enum (string) (optional)

The grounding tool type associated with the count.

Possible values:

  * `google_search`

Grounding with Google Web Search and Image Search, & Web Grounding for Enterprise.

  * `google_maps`

Grounding with Google Maps.




count integer (optional)

The number of grounding tool counts.

StepStart

index integer (required)

No description provided.

step Step (required)

No description provided.

event_type object (required)

No description provided.

Always set to `"step.start"`.

event_id string (optional)

The event_id token to be used to resume the interaction stream, from this event.

StepStop

index integer (required)

No description provided.

event_type object (required)

No description provided.

Always set to `"step.stop"`.

usage Usage (optional)

Cumulative model usage stats from the start of the session.

Statistics on the interaction request's token usage.

#### Fields

total_input_tokens integer (optional)

Number of tokens in the prompt (context).

input_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of input token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_cached_tokens integer (optional)

Number of tokens in the cached part of the prompt (the cached content).

cached_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of cached token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_output_tokens integer (optional)

Total number of tokens across all the generated responses.

output_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of output token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_tool_use_tokens integer (optional)

Number of tokens present in tool-use prompt(s).

tool_use_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of tool-use token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_thought_tokens integer (optional)

Number of tokens of thoughts for thinking models.

total_tokens integer (optional)

Total token count for the interaction request (prompt + responses + other internal tokens).

grounding_tool_count array (GroundingToolCount) (optional)

Grounding tool count.

The number of grounding tool counts.

#### Fields

type enum (string) (optional)

The grounding tool type associated with the count.

Possible values:

  * `google_search`

Grounding with Google Web Search and Image Search, & Web Grounding for Enterprise.

  * `google_maps`

Grounding with Google Maps.




count integer (optional)

The number of grounding tool counts.

step_usage Usage (optional)

Model usage stats for this specific step.

Statistics on the interaction request's token usage.

#### Fields

total_input_tokens integer (optional)

Number of tokens in the prompt (context).

input_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of input token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_cached_tokens integer (optional)

Number of tokens in the cached part of the prompt (the cached content).

cached_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of cached token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_output_tokens integer (optional)

Total number of tokens across all the generated responses.

output_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of output token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_tool_use_tokens integer (optional)

Number of tokens present in tool-use prompt(s).

tool_use_tokens_by_modality array (ModalityTokens) (optional)

A breakdown of tool-use token usage by modality.

The token count for a single response modality.

#### Fields

modality ResponseModality (optional)

The modality associated with the token count.

#### Possible values

  * `text`

Indicates the model should return text.

  * `image`

Indicates the model should return images.

  * `audio`

Indicates the model should return audio.

  * `video`

Indicates the model should return video.

  * `document`

Indicates the model should return documents.




tokens integer (optional)

Number of tokens for the modality.

total_thought_tokens integer (optional)

Number of tokens of thoughts for thinking models.

total_tokens integer (optional)

Total token count for the interaction request (prompt + responses + other internal tokens).

grounding_tool_count array (GroundingToolCount) (optional)

Grounding tool count.

The number of grounding tool counts.

#### Fields

type enum (string) (optional)

The grounding tool type associated with the count.

Possible values:

  * `google_search`

Grounding with Google Web Search and Image Search, & Web Grounding for Enterprise.

  * `google_maps`

Grounding with Google Maps.




count integer (optional)

The number of grounding tool counts.

event_id string (optional)

The event_id token to be used to resume the interaction stream, from this event.

### Examples

### Error Event
    
    
    {
      "error": {
        "code": "not_found",
        "message": "Failed to get completed interaction: Result not found."
      },
      "event_type": "error"
    }

### Interaction Completed
    
    
    {
      "event_id": "evt_123",
      "event_type": "interaction.completed",
      "interaction": {
        "created": "2025-12-04T15:01:45Z",
        "id": "v1_ChdXS0l4YWZXTk9xbk0xZThQczhEcmlROBIXV0tJeGFmV05PcW5NMWU4UHM4RHJpUTg",
        "model": "gemini-3.6-flash",
        "status": "completed",
        "updated": "2025-12-04T15:01:45Z"
      }
    }

### Interaction Completed
    
    
    {
      "event_id": "evt_123",
      "event_type": "interaction.completed",
      "interaction": {
        "created": "2025-12-04T15:01:45Z",
        "id": "v1_ChdXS0l4YWZXTk9xbk0xZThQczhEcmlROBIXV0tJeGFmV05PcW5NMWU4UHM4RHJpUTg",
        "model": "gemini-3-flash-preview",
        "object": "interaction",
        "status": "completed",
        "updated": "2025-12-04T15:01:45Z"
      }
    }

### Interaction Created
    
    
    {
      "event_id": "evt_123",
      "event_type": "interaction.created",
      "interaction": {
        "created": "2025-12-04T15:01:45Z",
        "id": "v1_ChdXS0l4YWZXTk9xbk0xZThQczhEcmlROBIXV0tJeGFmV05PcW5NMWU4UHM4RHJpUTg",
        "model": "gemini-3.6-flash",
        "status": "in_progress",
        "updated": "2025-12-04T15:01:45Z"
      }
    }

### Interaction Created
    
    
    {
      "event_id": "evt_123",
      "event_type": "interaction.created",
      "interaction": {
        "id": "v1_ChdXS0l4YWZXTk9xbk0xZThQczhEcmlROBIXV0tJeGFmV05PcW5NMWU4UHM4RHJpUTg",
        "model": "gemini-3-flash-preview",
        "object": "interaction",
        "status": "in_progress"
      }
    }

### Interaction Status Update
    
    
    {
      "event_type": "interaction.status_update",
      "interaction_id": "v1_ChdTMjQ0YWJ5TUF1TzcxZThQdjRpcnFRcxIXUzI0NGFieU1BdU83MWU4UHY0aXJxUXM",
      "status": "in_progress"
    }

### Step Delta
    
    
    {
      "delta": {
        "type": "text",
        "text": "Hello"
      },
      "event_type": "step.delta",
      "index": 0
    }

### Step Start
    
    
    {
      "event_type": "step.start",
      "index": 0,
      "step": {
        "type": "model_output"
      }
    }

### Step Stop
    
    
    {
      "event_type": "step.stop",
      "index": 0
    }

### ResponseFormat

### Possible Types

AudioResponseFormat

Configuration for audio output format.

type object (required)

No description provided.

Always set to `"audio"`.

mime_type enum (string) (optional)

The MIME type of the audio output.

Possible values:

  * `audio/mp3`

MP3 audio format.

  * `audio/ogg_opus`

OGG Opus audio format.

  * `audio/l16`

Raw PCM (L16) audio format.

  * `audio/wav`

WAV audio format.

  * `audio/alaw`

A-law audio format.

  * `audio/mulaw`

Mu-law audio format.




delivery enum (string) (optional)

The delivery mode for the audio output.

Possible values:

  * `inline`

Audio data is returned inline in the response.

  * `uri`

Audio data is returned as a URI.




sample_rate integer (optional)

Sample rate in Hz.

bit_rate integer (optional)

Bit rate in bits per second (bps). Only applicable for compressed formats (MP3, Opus).

ImageResponseFormat

Configuration for image output format.

type object (required)

No description provided.

Always set to `"image"`.

mime_type enum (string) (optional)

The MIME type of the image output.

Possible values:

  * `image/jpeg`

JPEG image format.




delivery enum (string) (optional)

The delivery mode for the image output.

Possible values:

  * `inline`

Image data is returned inline in the response.

  * `uri`

Image data is returned as a URI.




aspect_ratio enum (string) (optional)

The aspect ratio for the image output.

Possible values:

  * `1:1`

1:1 aspect ratio.

  * `2:3`

2:3 aspect ratio.

  * `3:2`

3:2 aspect ratio.

  * `3:4`

3:4 aspect ratio.

  * `4:3`

4:3 aspect ratio.

  * `4:5`

4:5 aspect ratio.

  * `5:4`

5:4 aspect ratio.

  * `9:16`

9:16 aspect ratio.

  * `16:9`

16:9 aspect ratio.

  * `21:9`

21:9 aspect ratio.

  * `1:8`

1:8 aspect ratio.

  * `8:1`

8:1 aspect ratio.

  * `1:4`

1:4 aspect ratio.

  * `4:1`

4:1 aspect ratio.




image_size enum (string) (optional)

The size of the image output.

Possible values:

  * `512`

512px image size.

  * `1K`

1K image size.

  * `2K`

2K image size.

  * `4K`

4K image size.




TextResponseFormat

Configuration for text output format.

type object (required)

No description provided.

Always set to `"text"`.

mime_type enum (string) (optional)

The MIME type of the text output.

Possible values:

  * `application/json`

JSON output format.

  * `text/plain`

Plain text output format.




schema object (optional)

The JSON schema that the output should conform to. Only applicable when mime_type is application/json. Supports a subset of JSON Schema. `minLength`, `maxLength`, `minProperties`, `maxProperties`, `uniqueItems`, `contains`, `minContains`, and `maxContains` are ignored and not enforced; validate these in your application. `minItems` and `maxItems` are enforced. Schemas that are too complex to enforce (for example, large `maxItems` on nested arrays) return a 400 INVALID_ARGUMENT error.

VideoResponseFormat

Configuration for video output format.

type object (required)

No description provided.

Always set to `"video"`.

delivery enum (string) (optional)

The delivery mode for the video output.

Possible values:

  * `inline`

Video data is returned inline in the response.

  * `uri`

Video data is returned as a URI.




aspect_ratio enum (string) (optional)

The aspect ratio for the video output.

Possible values:

  * `16:9`

16:9 aspect ratio.

  * `9:16`

9:16 aspect ratio.




duration string (optional)

The duration for the video output.

resolution enum (string) (optional)

The video output resolution. Defaults to 720p.

Possible values:

  * `360p`

360p resolution.

  * `720p`

720p resolution.

  * `1080p`

1080p resolution.

  * `4k`

4K resolution.




### Examples

### Audio Output
    
    
    {
      "type": "audio",
      "sample_rate": 24000
    }

### Image Output
    
    
    {
      "type": "image",
      "aspect_ratio": "16:9",
      "image_size": "1K",
      "mime_type": "image/jpeg"
    }

### Text Output (JSON Schema)
    
    
    {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "ingredients": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "recipe_name": {
            "type": "string"
          }
        },
        "required": [
          "ingredients",
          "recipe_name"
        ]
      }
    }

### VideoResponseFormat

No examples available for this type.

### Step

A step in the interaction.

### Possible Types

CodeExecutionCallStep

Code execution call step.

arguments CodeExecutionCallStepArguments (required)

Required. The arguments to pass to the code execution.

The arguments to pass to the code execution.

#### Fields

language enum (string) (optional)

Programming language of the `code`.

Possible values:

  * `python`

Python >= 3.10, with numpy and simpy available.

  * `bash`

Bash. Only available for Gemini 3.0 model or above.




code string (optional)

The code to be executed.

id string (required)

Required. A unique ID for this specific tool call.

type object (required)

No description provided.

Always set to `"code_execution_call"`.

signature string (optional)

A signature hash for backend validation.

CodeExecutionResultStep

Code execution result step.

result string (required)

Required. The output of the code execution.

call_id string (required)

Required. ID to match the ID from the function call block.

type object (required)

No description provided.

Always set to `"code_execution_result"`.

is_error boolean (optional)

Whether the code execution resulted in an error.

signature string (optional)

A signature hash for backend validation.

FileSearchCallStep

File Search call step.

id string (required)

Required. A unique ID for this specific tool call.

type object (required)

No description provided.

Always set to `"file_search_call"`.

signature string (optional)

A signature hash for backend validation.

FileSearchResultStep

File Search result step.

call_id string (required)

Required. ID to match the ID from the function call block.

type object (required)

No description provided.

Always set to `"file_search_result"`.

signature string (optional)

A signature hash for backend validation.

FunctionCallStep

A function tool call step.

name string (required)

Required. The name of the tool to call.

arguments object (required)

Required. The arguments to pass to the function.

id string (required)

Required. A unique ID for this specific tool call.

type object (required)

No description provided.

Always set to `"function_call"`.

FunctionResultStep

Result of a function tool call.

result array (ImageContent or TextContent) or object or string (required)

Required. The result of the tool call.

call_id string (required)

Required. ID to match the ID from the function call block.

type object (required)

No description provided.

Always set to `"function_result"`.

name string (optional)

The name of the tool that was called.

is_error boolean (optional)

Whether the tool call resulted in an error.

GoogleMapsCallStep

Google Maps call step.

id string (required)

Required. A unique ID for this specific tool call.

type object (required)

No description provided.

Always set to `"google_maps_call"`.

arguments GoogleMapsCallStepArguments (optional)

The arguments to pass to the Google Maps tool.

The arguments to pass to the Google Maps tool.

#### Fields

queries array (string) (optional)

The queries to be executed.

signature string (optional)

A signature hash for backend validation.

GoogleMapsResultStep

Google Maps result step.

result array (GoogleMapsResultItem) (required)

No description provided.

The result of the Google Maps.

#### Fields

places array (GoogleMapsResultPlaces) (optional)

No description provided.

#### Fields

place_id string (optional)

No description provided.

name string (optional)

No description provided.

url string (optional)

No description provided.

review_snippets array (ReviewSnippet) (optional)

No description provided.

Encapsulates a snippet of a user review that answers a question about the features of a specific place in Google Maps.

#### Fields

title string (optional)

Title of the review.

url string (optional)

A link that corresponds to the user review on Google Maps.

review_id string (optional)

The ID of the review snippet.

widget_context_token string (optional)

No description provided.

call_id string (required)

Required. ID to match the ID from the function call block.

type object (required)

No description provided.

Always set to `"google_maps_result"`.

signature string (optional)

A signature hash for backend validation.

GoogleSearchCallStep

Google Search call step.

arguments GoogleSearchCallStepArguments (required)

Required. The arguments to pass to Google Search.

The arguments to pass to Google Search.

#### Fields

queries array (string) (optional)

Web search queries for the following-up web search.

id string (required)

Required. A unique ID for this specific tool call.

type object (required)

No description provided.

Always set to `"google_search_call"`.

search_type enum (string) (optional)

The type of search grounding enabled.

Possible values:

  * `web_search`

Setting this field enables web search. Only text results are returned.

  * `image_search`

Setting this field enables image search. Image bytes are returned.




signature string (optional)

A signature hash for backend validation.

GoogleSearchResultStep

Google Search result step.

result array (GoogleSearchResultItem) (required)

Required. The results of the Google Search.

The result of the Google Search.

#### Fields

search_suggestions string (optional)

Web content snippet that can be embedded in a web page or an app webview.

call_id string (required)

Required. ID to match the ID from the function call block.

type object (required)

No description provided.

Always set to `"google_search_result"`.

is_error boolean (optional)

Whether the Google Search resulted in an error.

signature string (optional)

A signature hash for backend validation.

McpServerToolCallStep

MCPServer tool call step.

name string (required)

Required. The name of the tool which was called.

server_name string (required)

Required. The name of the used MCP server.

arguments object (required)

Required. The JSON object of arguments for the function.

id string (required)

Required. A unique ID for this specific tool call.

type object (required)

No description provided.

Always set to `"mcp_server_tool_call"`.

McpServerToolResultStep

MCPServer tool result step.

result array (ImageContent or TextContent) or object or string (required)

Required. The output from the MCP server call. Can be simple text or rich content.

call_id string (required)

Required. ID to match the ID from the function call block.

type object (required)

No description provided.

Always set to `"mcp_server_tool_result"`.

name string (optional)

Name of the tool which is called for this specific tool call.

server_name string (optional)

The name of the used MCP server.

ModelOutputStep

Output generated by the model.

type object (required)

No description provided.

Always set to `"model_output"`.

content array (Content) (optional)

No description provided.

ProcessingCallStep

A server-initiated processing step for media analysis (e.g. video understanding).

id string (required)

Required. A unique ID for this specific tool call.

type object (required)

No description provided.

Always set to `"processing_call"`.

ProcessingResultStep

The result of a server-initiated media processing step.

call_id string (required)

Required. ID to match the ID from the function call block.

type object (required)

No description provided.

Always set to `"processing_result"`.

ThoughtStep

A thought step.

type object (required)

No description provided.

Always set to `"thought"`.

signature string (optional)

A signature hash for backend validation.

summary array (Content) (optional)

A summary of the thought.

UrlContextCallStep

URL context call step.

arguments UrlContextCallArguments (required)

Required. The arguments to pass to the URL context.

The arguments to pass to the URL context.

#### Fields

urls array (string) (optional)

The URLs to fetch.

id string (required)

Required. A unique ID for this specific tool call.

type object (required)

No description provided.

Always set to `"url_context_call"`.

signature string (optional)

A signature hash for backend validation.

UrlContextResultStep

URL context result step.

result array (UrlContextResult) (required)

Required. The results of the URL context.

The result of the URL context.

#### Fields

url string (optional)

The URL that was fetched.

status enum (string) (optional)

The status of the URL retrieval.

Possible values:

  * `success`

Url retrieval is successful.

  * `error`

Url retrieval is failed due to error.

  * `paywall`

Url retrieval is failed because the content is behind paywall.

  * `unsafe`

Url retrieval is failed because the content is unsafe.




call_id string (required)

Required. ID to match the ID from the function call block.

type object (required)

No description provided.

Always set to `"url_context_result"`.

is_error boolean (optional)

Whether the URL context resulted in an error.

signature string (optional)

A signature hash for backend validation.

UserInputStep

Input provided by the user.

type object (required)

No description provided.

Always set to `"user_input"`.

content array (Content) (optional)

No description provided.

### Examples

### CodeExecutionCallStep
    
    
    {
      "type": "code_execution_call",
      "arguments": {
        "code": "print(sum(range(1, 11)))"
      },
      "id": "code_call_71021"
    }

### CodeExecutionResultStep
    
    
    {
      "type": "code_execution_result",
      "call_id": "code_call_71021",
      "result": "55\n"
    }

### FileSearchCallStep
    
    
    {
      "type": "file_search_call",
      "id": "file_call_88192"
    }

### FileSearchResultStep
    
    
    {
      "type": "file_search_result",
      "call_id": "file_call_88192"
    }

### FunctionCallStep
    
    
    {
      "name": "get_weather",
      "type": "function_call",
      "arguments": {
        "location": "Boston, MA"
      },
      "id": "call_98231"
    }

### FunctionResultStep
    
    
    {
      "name": "get_weather",
      "type": "function_result",
      "call_id": "call_98231",
      "result": [
        {
          "type": "text",
          "text": "{\"weather\":\"sunny\"}"
        }
      ]
    }

### GoogleMapsCallStep
    
    
    {
      "type": "google_maps_call",
      "arguments": {
        "latitude": 37.7749,
        "longitude": -122.4194
      },
      "id": "maps_call_39201"
    }

### GoogleMapsResultStep
    
    
    {
      "type": "google_maps_result",
      "call_id": "maps_call_39201",
      "result": [
        {
          "name": "Golden Gate Park",
          "place_id": "ChIJIQBpAG2ahYAR9R7bNdTLg8M",
          "rating": 4.8
        }
      ]
    }

### GoogleSearchCallStep
    
    
    {
      "type": "google_search_call",
      "arguments": {
        "query": "Who won the men's 100m in Paris 2024?"
      },
      "id": "search_call_19201"
    }

### GoogleSearchResultStep
    
    
    {
      "type": "google_search_result",
      "call_id": "search_call_19201",
      "result": [
        {
          "title": "Paris 2024 Olympics: Noah Lyles wins men's 100m gold",
          "url": "https://olympics.com/en/news/paris-2024-noah-lyles-wins-mens-100m-gold",
          "snippet": "American Noah Lyles won the Olympic men's 100m gold medal in a photo finish."
        }
      ]
    }

### McpServerToolCallStep

No examples available for this type.

### McpServerToolResultStep

No examples available for this type.

### ModelOutputStep
    
    
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The capital of France is Paris."
        }
      ]
    }

### ProcessingCallStep

No examples available for this type.

### ProcessingResultStep

No examples available for this type.

### ThoughtStep
    
    
    {
      "type": "thought",
      "signature": "thought_sig_abcd1234",
      "summary": [
        {
          "type": "text",
          "text": "The model is searching Google for the capital of France."
        }
      ]
    }

### UrlContextCallStep
    
    
    {
      "type": "url_context_call",
      "arguments": {
        "urls": [
          "https://www.example.com"
        ]
      },
      "id": "url_call_10219"
    }

### UrlContextResultStep
    
    
    {
      "type": "url_context_result",
      "call_id": "url_call_10219",
      "result": [
        {
          "title": "Example Domain",
          "url": "https://www.example.com",
          "snippet": "This domain is for use in illustrative examples in documents."
        }
      ]
    }

### UserInputStep
    
    
    {
      "type": "user_input",
      "content": [
        {
          "type": "text",
          "text": "What is the capital of France?"
        }
      ]
    }

### ToolChoiceConfig

The tool choice configuration containing allowed tools.

#### Fields

allowed_tools AllowedTools (optional)

The allowed tools.

The configuration for allowed tools.

#### Fields

mode enum (string) (optional)

The mode of the tool choice.

Possible values:

  * `auto`

Auto tool choice.

  * `any`

Any tool choice.

  * `none`

No tool choice.

  * `validated`

Validated tool choice.




tools array (string) (optional)

The names of the allowed tools.

### Examples

### Example
    
    
    {
      "allowed_tools": {
        "mode": "any",
        "tools": [
          "my_tool"
        ]
      }
    }

### ImageContent

An image content block.

#### Fields

type object (required)

No description provided.

Always set to `"image"`.

data string (optional)

The image content.

uri string (optional)

The URI of the image.

resolution MediaResolution (optional)

The resolution of the media.

#### Possible values

  * `low`

Low resolution.

  * `medium`

Medium resolution.

  * `high`

High resolution.

  * `ultra_high`

Ultra high resolution.




mime_type enum (string) (optional)

The mime type of the image.

Possible values:

  * `image/png`

PNG image format

  * `image/jpeg`

JPEG image format

  * `image/webp`

WebP image format

  * `image/heic`

HEIC image format

  * `image/heif`

HEIF image format

  * `image/gif`

GIF image format

  * `image/bmp`

BMP image format

  * `image/tiff`

TIFF image format




### Examples

### Image
    
    
    {
      "type": "image",
      "data": "BASE64_ENCODED_IMAGE",
      "mime_type": "image/png"
    }

### TextContent

A text content block.

#### Fields

text string (required)

Required. The text content.

type object (required)

No description provided.

Always set to `"text"`.

annotations array (Annotation) (optional)

Citation information for model-generated content.

Citation information for model-generated content.

#### Possible Types

FileCitation

A file citation annotation.

type object (required)

No description provided.

Always set to `"file_citation"`.

document_uri string (optional)

The URI of the file.

file_name string (optional)

The name of the file.

source string (optional)

Source attributed for a portion of the text.

custom_metadata object (optional)

User provided metadata about the retrieved context.

page_number integer (optional)

Page number of the cited document, if applicable.

media_id string (optional)

Media ID in-case of image citations, if applicable.

start_index integer (optional)

Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

end_index integer (optional)

End of the attributed segment, exclusive.

PlaceCitation

A place citation annotation.

type object (required)

No description provided.

Always set to `"place_citation"`.

place_id string (optional)

The ID of the place, in `places/{place_id}` format.

name string (optional)

Title of the place.

url string (optional)

URI reference of the place.

review_snippets array (ReviewSnippet) (optional)

Snippets of reviews that are used to generate answers about the features of a given place in Google Maps.

Encapsulates a snippet of a user review that answers a question about the features of a specific place in Google Maps.

#### Fields

title string (optional)

Title of the review.

url string (optional)

A link that corresponds to the user review on Google Maps.

review_id string (optional)

The ID of the review snippet.

start_index integer (optional)

Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

end_index integer (optional)

End of the attributed segment, exclusive.

UrlCitation

A URL citation annotation.

type object (required)

No description provided.

Always set to `"url_citation"`.

url string (optional)

The URL.

title string (optional)

The title of the URL.

start_index integer (optional)

Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

end_index integer (optional)

End of the attributed segment, exclusive.

### Examples

### Text
    
    
    {
      "type": "text",
      "text": "Hello, how are you?"
    }

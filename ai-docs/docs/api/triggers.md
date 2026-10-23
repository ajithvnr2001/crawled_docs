---
url: https://ai.google.dev/api/triggers/
title: Gemini Triggers API
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:00:14.136181+00:00
---

# Gemini Triggers API

> Source: https://ai.google.dev/api/triggers/

Triggers allow you to schedule agent executions on a cron schedule, enabling automated and recurring tasks.

[View as markdown](https://ai.google.dev/static/api/triggers.md.txt) [View the OpenAPI Spec](https://ai.google.dev/static/api/interactions.openapi.json)

## CreateTrigger

post  https://generativelanguage.googleapis.com/v1beta/triggers 

Creates a new trigger that will invoke the specified agent on the given cron schedule.

  * Request body
  * Response



### Request body

The request body contains data with the following structure:

schedule string (required)

Required. The cron schedule on which the trigger should run. Standard cron format.

time_zone string (required)

Required. Time zone in which the schedule should be interpreted.

interaction CreateAgentInteractionParams (required)

Required. The interaction request template to be executed.

Parameters for creating agent interactions

#### Fields

agent AgentOption (required)

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




input Content or array (Content) or array (Step) or string (required)

The input for the interaction.

agent_config AntigravityAgentConfig or DeepResearchAgentConfig or DynamicAgentConfig (optional)

Configuration parameters for the agent interaction.

response_format ResponseFormat or array (ResponseFormat) (optional)

Enforces that the generated response is a JSON object that complies with the JSON schema specified in this field.

#### Possible Types

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




environment EnvironmentConfig or string (optional)

The environment configuration for the interaction. Can be an object specifying remote environment sources or a string referencing an existing environment ID.

Configuration for a custom environment.

#### Fields

type object (required)

No description provided.

Always set to `"remote"`.

network EnvironmentNetworkEgressAllowlist or enum (string) (optional)

Network configuration for the environment.

Network egress configuration for the environment.

#### Fields

allowlist array (EgressRule) or enum (string) (optional)

List of allowed domains and their configurations. Set to `"disabled"` to block all network egress.

Possible values:

  * `disabled`

All network egress is blocked.




sources array (Source) (optional)

No description provided.

A source to be mounted into the environment.

#### Fields

type enum (string) (optional)

No description provided.

Possible values:

  * `gcs`

A Cloud Storage bucket.

  * `inline`

Inline content.

  * `repository`

A generic repository. The protocol prefix in the source URL identifies the provider (e.g., github://, gcs://).




source string (optional)

The source of the environment. For Cloud Storage, this is the Cloud Storage path. For GitHub, this is the GitHub path.

target string (optional)

Where the source should appear in the environment.

content string (optional)

The inline content if `type` is `INLINE`.

encoding string (optional)

Optional encoding for inline content (e.g. `base64`).

environment_id string (optional)

Optional. The environment ID for the interaction. If specified, the request will update the existing environment instead of creating a new one.

env object or string (optional)

Environment variables to set in the sandbox environment.

#### Possible Types

object

string

A direct string value.

id string (optional)

Required. Output only. A unique identifier for the interaction completion.

status enum (string) (optional)

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




created string (optional)

Required. Output only. The time at which the response was created in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).

updated string (optional)

Required. Output only. The time at which the response was last updated in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).

system_instruction string (optional)

System instruction for the interaction.

tools array (Tool) (optional)

A list of tool declarations the model may call during interaction.

A tool that can be used by the model.

#### Possible Types

CodeExecution

A tool that can be used by the model to execute code.

type object (required)

No description provided.

Always set to `"code_execution"`.

ComputerUse

A tool that can be used by the model to interact with the computer.

type object (required)

No description provided.

Always set to `"computer_use"`.

environment enum (string) (optional)

The environment being operated.

Possible values:

  * `browser`

Operates in a web browser.

  * `mobile`

Operates in a mobile environment.

  * `desktop`

Operates in a desktop environment.




excluded_predefined_functions array (string) (optional)

The list of predefined functions that are excluded from the model call.

enable_prompt_injection_detection boolean (optional)

Whether enable the prompt injection detection check on computer-use request.

disabled_safety_policies array (enum (string)) (optional)

Optional. Disabled safety policies for computer use.

Possible values:

  * `financial_transactions`

Safety policy for financial transactions.

  * `sensitive_data_modification`

Safety policy for sensitive data modification.

  * `communication_tool`

Safety policy for communication tools (e.g. Gmail, Chat, Meet).

  * `account_creation`

Safety policy for account creation.

  * `data_modification`

Safety policy for data modification.

  * `user_consent_management`

Safety policy for user consent management.

  * `legal_terms_and_agreements`

Safety policy for legal terms and agreements.




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

previous_interaction_id string (optional)

The ID of the previous interaction, if any.

environment_id string (optional)

Output only. The environment ID for the interaction. Only populated if environment config is set in the request.

service_tier ServiceTier (optional)

The service tier for the interaction.

#### Possible values

  * `flex`

Flex service tier.

  * `standard`

Standard service tier.

  * `priority`

Priority service tier.




webhook_config WebhookConfig (optional)

Optional. Webhook configuration for receiving notifications when the interaction completes.

Message for configuring webhook events for a request.

#### Fields

uris array (string) (optional)

Optional. If set, these webhook URIs will be used for webhook events instead of the registered webhooks.

user_metadata object (optional)

Optional. The user metadata that will be returned on each event emission to the webhooks.

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




labels object (optional)

The labels with user-defined metadata for the request. Label keys and values can be no longer than 63 characters (Unicode codepoints) and can only contain lowercase letters, numeric characters, underscores, and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter.

display_name string (optional)

Optional. The display name of the trigger.

environment_id string (optional)

Optional. The environment ID for the trigger execution.

max_consecutive_failures integer (optional)

Optional. The maximum number of consecutive failures allowed before the trigger is automatically paused (status becomes ERROR).

execution_timeout_seconds integer (optional)

Optional. The execution timeout for the triggered interaction.

### Response

If successful, the response body contains data with the following structure:

schedule string (required)

Required. The cron schedule on which the trigger should run. Standard cron format.

time_zone string (required)

Required. Time zone in which the schedule should be interpreted.

interaction CreateAgentInteractionParams (required)

Required. The interaction request template to be executed.

Parameters for creating agent interactions

#### Fields

agent AgentOption (required)

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




input Content or array (Content) or array (Step) or string (required)

The input for the interaction.

agent_config AntigravityAgentConfig or DeepResearchAgentConfig or DynamicAgentConfig (optional)

Configuration parameters for the agent interaction.

response_format ResponseFormat or array (ResponseFormat) (optional)

Enforces that the generated response is a JSON object that complies with the JSON schema specified in this field.

#### Possible Types

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




environment EnvironmentConfig or string (optional)

The environment configuration for the interaction. Can be an object specifying remote environment sources or a string referencing an existing environment ID.

Configuration for a custom environment.

#### Fields

type object (required)

No description provided.

Always set to `"remote"`.

network EnvironmentNetworkEgressAllowlist or enum (string) (optional)

Network configuration for the environment.

Network egress configuration for the environment.

#### Fields

allowlist array (EgressRule) or enum (string) (optional)

List of allowed domains and their configurations. Set to `"disabled"` to block all network egress.

Possible values:

  * `disabled`

All network egress is blocked.




sources array (Source) (optional)

No description provided.

A source to be mounted into the environment.

#### Fields

type enum (string) (optional)

No description provided.

Possible values:

  * `gcs`

A Cloud Storage bucket.

  * `inline`

Inline content.

  * `repository`

A generic repository. The protocol prefix in the source URL identifies the provider (e.g., github://, gcs://).




source string (optional)

The source of the environment. For Cloud Storage, this is the Cloud Storage path. For GitHub, this is the GitHub path.

target string (optional)

Where the source should appear in the environment.

content string (optional)

The inline content if `type` is `INLINE`.

encoding string (optional)

Optional encoding for inline content (e.g. `base64`).

environment_id string (optional)

Optional. The environment ID for the interaction. If specified, the request will update the existing environment instead of creating a new one.

env object or string (optional)

Environment variables to set in the sandbox environment.

#### Possible Types

object

string

A direct string value.

id string (optional)

Required. Output only. A unique identifier for the interaction completion.

status enum (string) (optional)

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




created string (optional)

Required. Output only. The time at which the response was created in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).

updated string (optional)

Required. Output only. The time at which the response was last updated in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).

system_instruction string (optional)

System instruction for the interaction.

tools array (Tool) (optional)

A list of tool declarations the model may call during interaction.

A tool that can be used by the model.

#### Possible Types

CodeExecution

A tool that can be used by the model to execute code.

type object (required)

No description provided.

Always set to `"code_execution"`.

ComputerUse

A tool that can be used by the model to interact with the computer.

type object (required)

No description provided.

Always set to `"computer_use"`.

environment enum (string) (optional)

The environment being operated.

Possible values:

  * `browser`

Operates in a web browser.

  * `mobile`

Operates in a mobile environment.

  * `desktop`

Operates in a desktop environment.




excluded_predefined_functions array (string) (optional)

The list of predefined functions that are excluded from the model call.

enable_prompt_injection_detection boolean (optional)

Whether enable the prompt injection detection check on computer-use request.

disabled_safety_policies array (enum (string)) (optional)

Optional. Disabled safety policies for computer use.

Possible values:

  * `financial_transactions`

Safety policy for financial transactions.

  * `sensitive_data_modification`

Safety policy for sensitive data modification.

  * `communication_tool`

Safety policy for communication tools (e.g. Gmail, Chat, Meet).

  * `account_creation`

Safety policy for account creation.

  * `data_modification`

Safety policy for data modification.

  * `user_consent_management`

Safety policy for user consent management.

  * `legal_terms_and_agreements`

Safety policy for legal terms and agreements.




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

previous_interaction_id string (optional)

The ID of the previous interaction, if any.

environment_id string (optional)

Output only. The environment ID for the interaction. Only populated if environment config is set in the request.

service_tier ServiceTier (optional)

The service tier for the interaction.

#### Possible values

  * `flex`

Flex service tier.

  * `standard`

Standard service tier.

  * `priority`

Priority service tier.




webhook_config WebhookConfig (optional)

Optional. Webhook configuration for receiving notifications when the interaction completes.

Message for configuring webhook events for a request.

#### Fields

uris array (string) (optional)

Optional. If set, these webhook URIs will be used for webhook events instead of the registered webhooks.

user_metadata object (optional)

Optional. The user metadata that will be returned on each event emission to the webhooks.

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




labels object (optional)

The labels with user-defined metadata for the request. Label keys and values can be no longer than 63 characters (Unicode codepoints) and can only contain lowercase letters, numeric characters, underscores, and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter.

id string (required)

Required. Output only. Identifier. The ID of the trigger.

display_name string (optional)

Optional. The display name of the trigger.

environment_id string (optional)

Optional. The environment ID for the trigger execution.

max_consecutive_failures integer (optional)

Optional. The maximum number of consecutive failures allowed before the trigger is automatically paused (status becomes ERROR).

execution_timeout_seconds integer (optional)

Optional. The execution timeout for the triggered interaction.

consecutive_failure_count integer (optional)

Output only. The number of consecutive failures that have occurred since the last successful execution.

create_time string (optional)

Output only. The time when the trigger was created.

update_time string (optional)

Output only. The time when the trigger was last updated.

last_run_time string (optional)

Output only. The time when the trigger was last run.

next_run_time string (optional)

Output only. The time when the trigger is scheduled to run next.

last_pause_time string (optional)

Output only. The time when the trigger was last paused.

last_resume_time string (optional)

Output only. The time when the trigger was last resumed.

previous_interaction_id string (optional)

Output only. The ID of the last interaction created by this trigger.

status enum (string) (optional)

Output only. The current status of the trigger.

Possible values:

  * `active`

The trigger is active and will fire on schedule.

  * `paused`

The trigger is paused and will not fire.

  * `error`

The trigger has entered an error state due to consecutive failures.




### Create

## RunTrigger

post  https://generativelanguage.googleapis.com/v1beta/triggers/{triggerId}/executions 

Runs a trigger immediately.

  * Path / Query parameters
  * Response



### Path / Query Parameters

triggerId string (required)

Required. Resource name of the trigger.

### Response

If successful, the response body contains data with the following structure:

id string (required)

Required. Output only. Identifier. The ID of the trigger execution.

trigger_id string (required)

Required. Output only. Identifier. The ID of the trigger that created this execution.

scheduled_time string (optional)

Output only. The time when the execution was scheduled to run.

start_time string (optional)

Output only. The time when the execution started.

end_time string (optional)

Output only. The time when the execution finished.

status enum (string) (optional)

Output only. The status of the execution.

Possible values:

  * `in_progress`

The execution is currently in progress.

  * `completed`

The execution completed successfully.

  * `failed`

The execution failed.

  * `skipped`

The execution was skipped (e.g., previous execution still running).

  * `timed_out`

The execution timed out.




interaction_id string (optional)

Output only. The ID of the interaction created by this execution, if any.

environment_id string (optional)

Output only. The environment ID used for the execution.

error string (optional)

Output only. The error message if the execution failed.

### Example

####  Example Response
    
    
    {
      "id": "string",
      "trigger_id": "string",
      "scheduled_time": "string",
      "start_time": "string",
      "end_time": "string",
      "status": "in_progress",
      "interaction_id": "string",
      "environment_id": "string",
      "error": "string"
    }

## ListTriggers

get  https://generativelanguage.googleapis.com/v1beta/triggers 

Lists triggers for a project.

  * Path / Query parameters
  * Response



### Path / Query Parameters

filter string (optional)

Optional. Filter expression (e.g., by state).

page_size integer (optional)

Optional. The maximum number of triggers to return per page.

page_token string (optional)

Optional. A page token from a previous ListTriggers call.

### Response

If successful, the response body contains data with the following structure:

triggers array (Trigger) (optional)

The list of triggers.

next_page_token string (optional)

A page token, received from a previous `ListTriggers` call. Provide this to retrieve the subsequent page.

### Example

####  Example Response
    
    
    {
      "triggers": [
        {
          "schedule": "string",
          "time_zone": "string",
          "interaction": {
            "agent": "deep-research-pro-preview-12-2025",
            "input": {
              "type": "...",
              "data": "...",
              "uri": "...",
              "channels": "...",
              "sample_rate": "...",
              "mime_type": "..."
            },
            "agent_config": {
              "type": {},
              "model": "string",
              "max_total_tokens": "string"
            },
            "response_format": {
              "type": {},
              "mime_type": "audio/mp3",
              "delivery": "inline",
              "sample_rate": 0,
              "bit_rate": 0
            },
            "environment": {
              "type": {},
              "network": {
                "allowlist": "..."
              },
              "sources": [
                "..."
              ],
              "environment_id": "string",
              "env": {}
            },
            "id": "string",
            "status": "in_progress",
            "created": "string",
            "updated": "string",
            "system_instruction": "string",
            "tools": [
              {
                "type": "..."
              }
            ],
            "previous_interaction_id": "string",
            "environment_id": "string",
            "service_tier": "flex",
            "webhook_config": {
              "uris": [
                "string"
              ],
              "user_metadata": {}
            },
            "safety_settings": [
              {
                "type": "...",
                "threshold": "block_low_and_above",
                "method": "severity"
              }
            ],
            "labels": {},
            "stream": true,
            "store": true,
            "background": true
          },
          "id": "string",
          "display_name": "string",
          "environment_id": "string",
          "max_consecutive_failures": 0,
          "execution_timeout_seconds": 0,
          "consecutive_failure_count": 0,
          "create_time": "string",
          "update_time": "string",
          "last_run_time": "string",
          "next_run_time": "string",
          "last_pause_time": "string",
          "last_resume_time": "string",
          "previous_interaction_id": "string",
          "status": "active"
        }
      ],
      "next_page_token": "string"
    }

## GetTrigger

get  https://generativelanguage.googleapis.com/v1beta/triggers/{id} 

Gets details of a single trigger.

  * Path / Query parameters
  * Response



### Path / Query Parameters

id string (required)

Required. Resource name of the trigger.

### Response

If successful, the response body contains data with the following structure:

schedule string (required)

Required. The cron schedule on which the trigger should run. Standard cron format.

time_zone string (required)

Required. Time zone in which the schedule should be interpreted.

interaction CreateAgentInteractionParams (required)

Required. The interaction request template to be executed.

Parameters for creating agent interactions

#### Fields

agent AgentOption (required)

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




input Content or array (Content) or array (Step) or string (required)

The input for the interaction.

agent_config AntigravityAgentConfig or DeepResearchAgentConfig or DynamicAgentConfig (optional)

Configuration parameters for the agent interaction.

response_format ResponseFormat or array (ResponseFormat) (optional)

Enforces that the generated response is a JSON object that complies with the JSON schema specified in this field.

#### Possible Types

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




environment EnvironmentConfig or string (optional)

The environment configuration for the interaction. Can be an object specifying remote environment sources or a string referencing an existing environment ID.

Configuration for a custom environment.

#### Fields

type object (required)

No description provided.

Always set to `"remote"`.

network EnvironmentNetworkEgressAllowlist or enum (string) (optional)

Network configuration for the environment.

Network egress configuration for the environment.

#### Fields

allowlist array (EgressRule) or enum (string) (optional)

List of allowed domains and their configurations. Set to `"disabled"` to block all network egress.

Possible values:

  * `disabled`

All network egress is blocked.




sources array (Source) (optional)

No description provided.

A source to be mounted into the environment.

#### Fields

type enum (string) (optional)

No description provided.

Possible values:

  * `gcs`

A Cloud Storage bucket.

  * `inline`

Inline content.

  * `repository`

A generic repository. The protocol prefix in the source URL identifies the provider (e.g., github://, gcs://).




source string (optional)

The source of the environment. For Cloud Storage, this is the Cloud Storage path. For GitHub, this is the GitHub path.

target string (optional)

Where the source should appear in the environment.

content string (optional)

The inline content if `type` is `INLINE`.

encoding string (optional)

Optional encoding for inline content (e.g. `base64`).

environment_id string (optional)

Optional. The environment ID for the interaction. If specified, the request will update the existing environment instead of creating a new one.

env object or string (optional)

Environment variables to set in the sandbox environment.

#### Possible Types

object

string

A direct string value.

id string (optional)

Required. Output only. A unique identifier for the interaction completion.

status enum (string) (optional)

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




created string (optional)

Required. Output only. The time at which the response was created in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).

updated string (optional)

Required. Output only. The time at which the response was last updated in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).

system_instruction string (optional)

System instruction for the interaction.

tools array (Tool) (optional)

A list of tool declarations the model may call during interaction.

A tool that can be used by the model.

#### Possible Types

CodeExecution

A tool that can be used by the model to execute code.

type object (required)

No description provided.

Always set to `"code_execution"`.

ComputerUse

A tool that can be used by the model to interact with the computer.

type object (required)

No description provided.

Always set to `"computer_use"`.

environment enum (string) (optional)

The environment being operated.

Possible values:

  * `browser`

Operates in a web browser.

  * `mobile`

Operates in a mobile environment.

  * `desktop`

Operates in a desktop environment.




excluded_predefined_functions array (string) (optional)

The list of predefined functions that are excluded from the model call.

enable_prompt_injection_detection boolean (optional)

Whether enable the prompt injection detection check on computer-use request.

disabled_safety_policies array (enum (string)) (optional)

Optional. Disabled safety policies for computer use.

Possible values:

  * `financial_transactions`

Safety policy for financial transactions.

  * `sensitive_data_modification`

Safety policy for sensitive data modification.

  * `communication_tool`

Safety policy for communication tools (e.g. Gmail, Chat, Meet).

  * `account_creation`

Safety policy for account creation.

  * `data_modification`

Safety policy for data modification.

  * `user_consent_management`

Safety policy for user consent management.

  * `legal_terms_and_agreements`

Safety policy for legal terms and agreements.




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

previous_interaction_id string (optional)

The ID of the previous interaction, if any.

environment_id string (optional)

Output only. The environment ID for the interaction. Only populated if environment config is set in the request.

service_tier ServiceTier (optional)

The service tier for the interaction.

#### Possible values

  * `flex`

Flex service tier.

  * `standard`

Standard service tier.

  * `priority`

Priority service tier.




webhook_config WebhookConfig (optional)

Optional. Webhook configuration for receiving notifications when the interaction completes.

Message for configuring webhook events for a request.

#### Fields

uris array (string) (optional)

Optional. If set, these webhook URIs will be used for webhook events instead of the registered webhooks.

user_metadata object (optional)

Optional. The user metadata that will be returned on each event emission to the webhooks.

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




labels object (optional)

The labels with user-defined metadata for the request. Label keys and values can be no longer than 63 characters (Unicode codepoints) and can only contain lowercase letters, numeric characters, underscores, and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter.

id string (required)

Required. Output only. Identifier. The ID of the trigger.

display_name string (optional)

Optional. The display name of the trigger.

environment_id string (optional)

Optional. The environment ID for the trigger execution.

max_consecutive_failures integer (optional)

Optional. The maximum number of consecutive failures allowed before the trigger is automatically paused (status becomes ERROR).

execution_timeout_seconds integer (optional)

Optional. The execution timeout for the triggered interaction.

consecutive_failure_count integer (optional)

Output only. The number of consecutive failures that have occurred since the last successful execution.

create_time string (optional)

Output only. The time when the trigger was created.

update_time string (optional)

Output only. The time when the trigger was last updated.

last_run_time string (optional)

Output only. The time when the trigger was last run.

next_run_time string (optional)

Output only. The time when the trigger is scheduled to run next.

last_pause_time string (optional)

Output only. The time when the trigger was last paused.

last_resume_time string (optional)

Output only. The time when the trigger was last resumed.

previous_interaction_id string (optional)

Output only. The ID of the last interaction created by this trigger.

status enum (string) (optional)

Output only. The current status of the trigger.

Possible values:

  * `active`

The trigger is active and will fire on schedule.

  * `paused`

The trigger is paused and will not fire.

  * `error`

The trigger has entered an error state due to consecutive failures.




### Example

####  Example Response
    
    
    {
      "schedule": "string",
      "time_zone": "string",
      "interaction": {
        "agent": "deep-research-pro-preview-12-2025",
        "input": {
          "type": {},
          "data": "string",
          "uri": "string",
          "channels": 0,
          "sample_rate": 0,
          "mime_type": "audio/wav"
        },
        "agent_config": {
          "type": {},
          "model": "string",
          "max_total_tokens": "string"
        },
        "response_format": {
          "type": {},
          "mime_type": "audio/mp3",
          "delivery": "inline",
          "sample_rate": 0,
          "bit_rate": 0
        },
        "environment": {
          "type": {},
          "network": {
            "allowlist": [
              {
                "domain": "...",
                "transform": "...",
                "credential": "..."
              }
            ]
          },
          "sources": [
            {
              "type": "gcs",
              "source": "string",
              "target": "string",
              "content": "string",
              "encoding": "string"
            }
          ],
          "environment_id": "string",
          "env": {}
        },
        "id": "string",
        "status": "in_progress",
        "created": "string",
        "updated": "string",
        "system_instruction": "string",
        "tools": [
          {
            "type": {}
          }
        ],
        "previous_interaction_id": "string",
        "environment_id": "string",
        "service_tier": "flex",
        "webhook_config": {
          "uris": [
            "string"
          ],
          "user_metadata": {}
        },
        "safety_settings": [
          {
            "type": "hate_speech",
            "threshold": "block_low_and_above",
            "method": "severity"
          }
        ],
        "labels": {},
        "stream": true,
        "store": true,
        "background": true
      },
      "id": "string",
      "display_name": "string",
      "environment_id": "string",
      "max_consecutive_failures": 0,
      "execution_timeout_seconds": 0,
      "consecutive_failure_count": 0,
      "create_time": "string",
      "update_time": "string",
      "last_run_time": "string",
      "next_run_time": "string",
      "last_pause_time": "string",
      "last_resume_time": "string",
      "previous_interaction_id": "string",
      "status": "active"
    }

## ListTriggerExecutions

get  https://generativelanguage.googleapis.com/v1beta/triggers/{triggerId}/executions 

Lists executions for a trigger.

  * Path / Query parameters
  * Response



### Path / Query Parameters

triggerId string (required)

Required. The trigger ID to list executions from.

filter string (optional)

Optional. Filter expression.

page_size integer (optional)

The maximum number of executions to return per page.

page_token string (optional)

A page token from a previous ListTriggerExecutions call.

### Response

If successful, the response body contains data with the following structure:

trigger_executions array (TriggerExecution) (optional)

The list of trigger executions.

An execution instance of a trigger.

#### Fields

id string (required)

Required. Output only. Identifier. The ID of the trigger execution.

trigger_id string (required)

Required. Output only. Identifier. The ID of the trigger that created this execution.

scheduled_time string (optional)

Output only. The time when the execution was scheduled to run.

start_time string (optional)

Output only. The time when the execution started.

end_time string (optional)

Output only. The time when the execution finished.

status enum (string) (optional)

Output only. The status of the execution.

Possible values:

  * `in_progress`

The execution is currently in progress.

  * `completed`

The execution completed successfully.

  * `failed`

The execution failed.

  * `skipped`

The execution was skipped (e.g., previous execution still running).

  * `timed_out`

The execution timed out.




interaction_id string (optional)

Output only. The ID of the interaction created by this execution, if any.

environment_id string (optional)

Output only. The environment ID used for the execution.

error string (optional)

Output only. The error message if the execution failed.

next_page_token string (optional)

A page token, received from a previous `ListTriggerExecutions` call. Provide this to retrieve the subsequent page.

### Example

####  Example Response
    
    
    {
      "trigger_executions": [
        {
          "id": "string",
          "trigger_id": "string",
          "scheduled_time": "string",
          "start_time": "string",
          "end_time": "string",
          "status": "in_progress",
          "interaction_id": "string",
          "environment_id": "string",
          "error": "string"
        }
      ],
      "next_page_token": "string"
    }

## UpdateTrigger

patch  https://generativelanguage.googleapis.com/v1beta/triggers/{id} 

Updates a trigger.

  * Path / Query parameters
  * Request body
  * Response



### Path / Query Parameters

id string (required)

Required. Resource name of the trigger.

### Request body

The request body contains data with the following structure:

trigger TriggerUpdate (required)

Required. The trigger to update.

Represents the fields of a Trigger that can be updated.

#### Fields

status enum (string) (optional)

Optional. The status of the trigger.

Possible values:

  * `active`

The trigger is active and will fire on schedule.

  * `paused`

The trigger is paused and will not fire.

  * `error`

The trigger has entered an error state due to consecutive failures.




display_name string (optional)

Optional. The display name of the trigger.

id string (required)

Required. The ID of the trigger to update.

update_mask string (optional)

Optional. The update mask applies to the resource.

### Response

If successful, the response body contains data with the following structure:

schedule string (required)

Required. The cron schedule on which the trigger should run. Standard cron format.

time_zone string (required)

Required. Time zone in which the schedule should be interpreted.

interaction CreateAgentInteractionParams (required)

Required. The interaction request template to be executed.

Parameters for creating agent interactions

#### Fields

agent AgentOption (required)

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




input Content or array (Content) or array (Step) or string (required)

The input for the interaction.

agent_config AntigravityAgentConfig or DeepResearchAgentConfig or DynamicAgentConfig (optional)

Configuration parameters for the agent interaction.

response_format ResponseFormat or array (ResponseFormat) (optional)

Enforces that the generated response is a JSON object that complies with the JSON schema specified in this field.

#### Possible Types

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




environment EnvironmentConfig or string (optional)

The environment configuration for the interaction. Can be an object specifying remote environment sources or a string referencing an existing environment ID.

Configuration for a custom environment.

#### Fields

type object (required)

No description provided.

Always set to `"remote"`.

network EnvironmentNetworkEgressAllowlist or enum (string) (optional)

Network configuration for the environment.

Network egress configuration for the environment.

#### Fields

allowlist array (EgressRule) or enum (string) (optional)

List of allowed domains and their configurations. Set to `"disabled"` to block all network egress.

Possible values:

  * `disabled`

All network egress is blocked.




sources array (Source) (optional)

No description provided.

A source to be mounted into the environment.

#### Fields

type enum (string) (optional)

No description provided.

Possible values:

  * `gcs`

A Cloud Storage bucket.

  * `inline`

Inline content.

  * `repository`

A generic repository. The protocol prefix in the source URL identifies the provider (e.g., github://, gcs://).




source string (optional)

The source of the environment. For Cloud Storage, this is the Cloud Storage path. For GitHub, this is the GitHub path.

target string (optional)

Where the source should appear in the environment.

content string (optional)

The inline content if `type` is `INLINE`.

encoding string (optional)

Optional encoding for inline content (e.g. `base64`).

environment_id string (optional)

Optional. The environment ID for the interaction. If specified, the request will update the existing environment instead of creating a new one.

env object or string (optional)

Environment variables to set in the sandbox environment.

#### Possible Types

object

string

A direct string value.

id string (optional)

Required. Output only. A unique identifier for the interaction completion.

status enum (string) (optional)

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




created string (optional)

Required. Output only. The time at which the response was created in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).

updated string (optional)

Required. Output only. The time at which the response was last updated in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).

system_instruction string (optional)

System instruction for the interaction.

tools array (Tool) (optional)

A list of tool declarations the model may call during interaction.

A tool that can be used by the model.

#### Possible Types

CodeExecution

A tool that can be used by the model to execute code.

type object (required)

No description provided.

Always set to `"code_execution"`.

ComputerUse

A tool that can be used by the model to interact with the computer.

type object (required)

No description provided.

Always set to `"computer_use"`.

environment enum (string) (optional)

The environment being operated.

Possible values:

  * `browser`

Operates in a web browser.

  * `mobile`

Operates in a mobile environment.

  * `desktop`

Operates in a desktop environment.




excluded_predefined_functions array (string) (optional)

The list of predefined functions that are excluded from the model call.

enable_prompt_injection_detection boolean (optional)

Whether enable the prompt injection detection check on computer-use request.

disabled_safety_policies array (enum (string)) (optional)

Optional. Disabled safety policies for computer use.

Possible values:

  * `financial_transactions`

Safety policy for financial transactions.

  * `sensitive_data_modification`

Safety policy for sensitive data modification.

  * `communication_tool`

Safety policy for communication tools (e.g. Gmail, Chat, Meet).

  * `account_creation`

Safety policy for account creation.

  * `data_modification`

Safety policy for data modification.

  * `user_consent_management`

Safety policy for user consent management.

  * `legal_terms_and_agreements`

Safety policy for legal terms and agreements.




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

previous_interaction_id string (optional)

The ID of the previous interaction, if any.

environment_id string (optional)

Output only. The environment ID for the interaction. Only populated if environment config is set in the request.

service_tier ServiceTier (optional)

The service tier for the interaction.

#### Possible values

  * `flex`

Flex service tier.

  * `standard`

Standard service tier.

  * `priority`

Priority service tier.




webhook_config WebhookConfig (optional)

Optional. Webhook configuration for receiving notifications when the interaction completes.

Message for configuring webhook events for a request.

#### Fields

uris array (string) (optional)

Optional. If set, these webhook URIs will be used for webhook events instead of the registered webhooks.

user_metadata object (optional)

Optional. The user metadata that will be returned on each event emission to the webhooks.

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




labels object (optional)

The labels with user-defined metadata for the request. Label keys and values can be no longer than 63 characters (Unicode codepoints) and can only contain lowercase letters, numeric characters, underscores, and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter.

id string (required)

Required. Output only. Identifier. The ID of the trigger.

display_name string (optional)

Optional. The display name of the trigger.

environment_id string (optional)

Optional. The environment ID for the trigger execution.

max_consecutive_failures integer (optional)

Optional. The maximum number of consecutive failures allowed before the trigger is automatically paused (status becomes ERROR).

execution_timeout_seconds integer (optional)

Optional. The execution timeout for the triggered interaction.

consecutive_failure_count integer (optional)

Output only. The number of consecutive failures that have occurred since the last successful execution.

create_time string (optional)

Output only. The time when the trigger was created.

update_time string (optional)

Output only. The time when the trigger was last updated.

last_run_time string (optional)

Output only. The time when the trigger was last run.

next_run_time string (optional)

Output only. The time when the trigger is scheduled to run next.

last_pause_time string (optional)

Output only. The time when the trigger was last paused.

last_resume_time string (optional)

Output only. The time when the trigger was last resumed.

previous_interaction_id string (optional)

Output only. The ID of the last interaction created by this trigger.

status enum (string) (optional)

Output only. The current status of the trigger.

Possible values:

  * `active`

The trigger is active and will fire on schedule.

  * `paused`

The trigger is paused and will not fire.

  * `error`

The trigger has entered an error state due to consecutive failures.




### Example

####  Example Response
    
    
    {
      "schedule": "string",
      "time_zone": "string",
      "interaction": {
        "agent": "deep-research-pro-preview-12-2025",
        "input": {
          "type": {},
          "data": "string",
          "uri": "string",
          "channels": 0,
          "sample_rate": 0,
          "mime_type": "audio/wav"
        },
        "agent_config": {
          "type": {},
          "model": "string",
          "max_total_tokens": "string"
        },
        "response_format": {
          "type": {},
          "mime_type": "audio/mp3",
          "delivery": "inline",
          "sample_rate": 0,
          "bit_rate": 0
        },
        "environment": {
          "type": {},
          "network": {
            "allowlist": [
              {
                "domain": "...",
                "transform": "...",
                "credential": "..."
              }
            ]
          },
          "sources": [
            {
              "type": "gcs",
              "source": "string",
              "target": "string",
              "content": "string",
              "encoding": "string"
            }
          ],
          "environment_id": "string",
          "env": {}
        },
        "id": "string",
        "status": "in_progress",
        "created": "string",
        "updated": "string",
        "system_instruction": "string",
        "tools": [
          {
            "type": {}
          }
        ],
        "previous_interaction_id": "string",
        "environment_id": "string",
        "service_tier": "flex",
        "webhook_config": {
          "uris": [
            "string"
          ],
          "user_metadata": {}
        },
        "safety_settings": [
          {
            "type": "hate_speech",
            "threshold": "block_low_and_above",
            "method": "severity"
          }
        ],
        "labels": {},
        "stream": true,
        "store": true,
        "background": true
      },
      "id": "string",
      "display_name": "string",
      "environment_id": "string",
      "max_consecutive_failures": 0,
      "execution_timeout_seconds": 0,
      "consecutive_failure_count": 0,
      "create_time": "string",
      "update_time": "string",
      "last_run_time": "string",
      "next_run_time": "string",
      "last_pause_time": "string",
      "last_resume_time": "string",
      "previous_interaction_id": "string",
      "status": "active"
    }

## DeleteTrigger

delete  https://generativelanguage.googleapis.com/v1beta/triggers/{id} 

Deletes a trigger.

  * Path / Query parameters
  * Response



### Path / Query Parameters

id string (required)

Required. Resource name of the trigger.

### Response

If successful, the response is empty.

### Example

## Resources

### Trigger

A trigger configuration that is scheduled to run an agent.

#### Fields

schedule string (required)

Required. The cron schedule on which the trigger should run. Standard cron format.

time_zone string (required)

Required. Time zone in which the schedule should be interpreted.

interaction CreateAgentInteractionParams (required)

Required. The interaction request template to be executed.

Parameters for creating agent interactions

#### Fields

agent AgentOption (required)

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




input Content or array (Content) or array (Step) or string (required)

The input for the interaction.

agent_config AntigravityAgentConfig or DeepResearchAgentConfig or DynamicAgentConfig (optional)

Configuration parameters for the agent interaction.

response_format ResponseFormat or array (ResponseFormat) (optional)

Enforces that the generated response is a JSON object that complies with the JSON schema specified in this field.

#### Possible Types

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




environment EnvironmentConfig or string (optional)

The environment configuration for the interaction. Can be an object specifying remote environment sources or a string referencing an existing environment ID.

Configuration for a custom environment.

#### Fields

type object (required)

No description provided.

Always set to `"remote"`.

network EnvironmentNetworkEgressAllowlist or enum (string) (optional)

Network configuration for the environment.

Network egress configuration for the environment.

#### Fields

allowlist array (EgressRule) or enum (string) (optional)

List of allowed domains and their configurations. Set to `"disabled"` to block all network egress.

Possible values:

  * `disabled`

All network egress is blocked.




sources array (Source) (optional)

No description provided.

A source to be mounted into the environment.

#### Fields

type enum (string) (optional)

No description provided.

Possible values:

  * `gcs`

A Cloud Storage bucket.

  * `inline`

Inline content.

  * `repository`

A generic repository. The protocol prefix in the source URL identifies the provider (e.g., github://, gcs://).




source string (optional)

The source of the environment. For Cloud Storage, this is the Cloud Storage path. For GitHub, this is the GitHub path.

target string (optional)

Where the source should appear in the environment.

content string (optional)

The inline content if `type` is `INLINE`.

encoding string (optional)

Optional encoding for inline content (e.g. `base64`).

environment_id string (optional)

Optional. The environment ID for the interaction. If specified, the request will update the existing environment instead of creating a new one.

env object or string (optional)

Environment variables to set in the sandbox environment.

#### Possible Types

object

string

A direct string value.

id string (optional)

Required. Output only. A unique identifier for the interaction completion.

status enum (string) (optional)

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




created string (optional)

Required. Output only. The time at which the response was created in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).

updated string (optional)

Required. Output only. The time at which the response was last updated in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).

system_instruction string (optional)

System instruction for the interaction.

tools array (Tool) (optional)

A list of tool declarations the model may call during interaction.

A tool that can be used by the model.

#### Possible Types

CodeExecution

A tool that can be used by the model to execute code.

type object (required)

No description provided.

Always set to `"code_execution"`.

ComputerUse

A tool that can be used by the model to interact with the computer.

type object (required)

No description provided.

Always set to `"computer_use"`.

environment enum (string) (optional)

The environment being operated.

Possible values:

  * `browser`

Operates in a web browser.

  * `mobile`

Operates in a mobile environment.

  * `desktop`

Operates in a desktop environment.




excluded_predefined_functions array (string) (optional)

The list of predefined functions that are excluded from the model call.

enable_prompt_injection_detection boolean (optional)

Whether enable the prompt injection detection check on computer-use request.

disabled_safety_policies array (enum (string)) (optional)

Optional. Disabled safety policies for computer use.

Possible values:

  * `financial_transactions`

Safety policy for financial transactions.

  * `sensitive_data_modification`

Safety policy for sensitive data modification.

  * `communication_tool`

Safety policy for communication tools (e.g. Gmail, Chat, Meet).

  * `account_creation`

Safety policy for account creation.

  * `data_modification`

Safety policy for data modification.

  * `user_consent_management`

Safety policy for user consent management.

  * `legal_terms_and_agreements`

Safety policy for legal terms and agreements.




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

previous_interaction_id string (optional)

The ID of the previous interaction, if any.

environment_id string (optional)

Output only. The environment ID for the interaction. Only populated if environment config is set in the request.

service_tier ServiceTier (optional)

The service tier for the interaction.

#### Possible values

  * `flex`

Flex service tier.

  * `standard`

Standard service tier.

  * `priority`

Priority service tier.




webhook_config WebhookConfig (optional)

Optional. Webhook configuration for receiving notifications when the interaction completes.

Message for configuring webhook events for a request.

#### Fields

uris array (string) (optional)

Optional. If set, these webhook URIs will be used for webhook events instead of the registered webhooks.

user_metadata object (optional)

Optional. The user metadata that will be returned on each event emission to the webhooks.

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




labels object (optional)

The labels with user-defined metadata for the request. Label keys and values can be no longer than 63 characters (Unicode codepoints) and can only contain lowercase letters, numeric characters, underscores, and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter.

id string (required)

Required. Output only. Identifier. The ID of the trigger.

display_name string (optional)

Optional. The display name of the trigger.

environment_id string (optional)

Optional. The environment ID for the trigger execution.

max_consecutive_failures integer (optional)

Optional. The maximum number of consecutive failures allowed before the trigger is automatically paused (status becomes ERROR).

execution_timeout_seconds integer (optional)

Optional. The execution timeout for the triggered interaction.

consecutive_failure_count integer (optional)

Output only. The number of consecutive failures that have occurred since the last successful execution.

create_time string (optional)

Output only. The time when the trigger was created.

update_time string (optional)

Output only. The time when the trigger was last updated.

last_run_time string (optional)

Output only. The time when the trigger was last run.

next_run_time string (optional)

Output only. The time when the trigger is scheduled to run next.

last_pause_time string (optional)

Output only. The time when the trigger was last paused.

last_resume_time string (optional)

Output only. The time when the trigger was last resumed.

previous_interaction_id string (optional)

Output only. The ID of the last interaction created by this trigger.

status enum (string) (optional)

Output only. The current status of the trigger.

Possible values:

  * `active`

The trigger is active and will fire on schedule.

  * `paused`

The trigger is paused and will not fire.

  * `error`

The trigger has entered an error state due to consecutive failures.




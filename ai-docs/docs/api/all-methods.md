---
url: https://ai.google.dev/api/all-methods/
title: All methods \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:15:51.861991+00:00
---

# All methods  |  Gemini API  |  Google AI for Developers

> Source: https://ai.google.dev/api/all-methods/

Gemini 4 Argon is now available. [Try it out](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon). 

  * [ Home ](https://ai.google.dev/)
  * [ Gemini API ](https://ai.google.dev/gemini-api)
  * [ API reference ](https://ai.google.dev/api)



Send feedback 

#  All methods

## Gemini API

The Gemini API allows developers to build generative AI applications using Gemini models. Gemini is our most capable model, built from the ground up to be multimodal. It can generalize and seamlessly understand, operate across, and combine different types of information including language, images, audio, video, and code. You can use the Gemini API for use cases like reasoning across text and images, content generation, dialogue agents, summarization and classification systems, and more.

  * REST Resource: v1beta.auth_tokens
  * REST Resource: v1beta.batches
  * REST Resource: v1beta.cachedContents
  * REST Resource: v1beta.corpora
  * REST Resource: v1beta.corpora.operations
  * REST Resource: v1beta.corpora.permissions
  * REST Resource: v1beta.dynamic
  * REST Resource: v1beta.environments
  * REST Resource: v1beta.environments.files.media
  * REST Resource: v1beta.fileSearchStores
  * REST Resource: v1beta.fileSearchStores.documents
  * REST Resource: v1beta.fileSearchStores.operations
  * REST Resource: v1beta.fileSearchStores.upload.operations
  * REST Resource: v1beta.files
  * REST Resource: v1beta.generatedFiles
  * REST Resource: v1beta.generatedFiles.operations
  * REST Resource: v1beta.media
  * REST Resource: v1beta.models
  * REST Resource: v1beta.models.operations
  * REST Resource: v1beta.tunedModels
  * REST Resource: v1beta.tunedModels.operations
  * REST Resource: v1beta.tunedModels.permissions



## Service: generativelanguage.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://generativelanguage.googleapis.com`



## REST Resource: [v1beta.auth_tokens](https://ai.google.dev/api/generate-content#v1beta.auth_tokens)

Methods  
---  
`[create](https://ai.google.dev/api/generate-content#v1beta.auth_tokens.create)` |  `POST /v1beta/auth_tokens`   
Creates a token that can be used to constrain the behavior of a BidiGenerateContent session.  
  
## REST Resource: [v1beta.batches](https://ai.google.dev/api/batch-api#v1beta.batches)

Methods  
---  
`[cancel](https://ai.google.dev/api/batch-api#v1beta.batches.cancel)` |  `POST /v1beta/{name=batches/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://ai.google.dev/api/batch-api#v1beta.batches.delete)` |  `DELETE /v1beta/{name=batches/*}`   
Deletes a long-running operation.  
`[get](https://ai.google.dev/api/batch-api#v1beta.batches.get)` |  `GET /v1beta/{name=batches/*}`   
Gets the latest state of a long-running operation.  
`[list](https://ai.google.dev/api/batch-api#v1beta.batches.list)` |  `GET /v1beta/{name=batches}`   
Lists operations that match the specified filter in the request.  
`[updateEmbedContentBatch](https://ai.google.dev/api/batch-api#v1beta.batches.updateEmbedContentBatch)` |  `PATCH /v1beta/{embedContentBatch.name=batches/*}:updateEmbedContentBatch`   
Updates a batch of EmbedContent requests for batch processing.  
`[updateGenerateContentBatch](https://ai.google.dev/api/batch-api#v1beta.batches.updateGenerateContentBatch)` |  `PATCH /v1beta/{generateContentBatch.name=batches/*}:updateGenerateContentBatch`   
Updates a batch of GenerateContent requests for batch processing.  
  
## REST Resource: [v1beta.cachedContents](https://ai.google.dev/api/caching#v1beta.cachedContents)

Methods  
---  
`[create](https://ai.google.dev/api/caching#v1beta.cachedContents.create)` |  `POST /v1beta/cachedContents`   
Creates CachedContent resource.  
`[delete](https://ai.google.dev/api/caching#v1beta.cachedContents.delete)` |  `DELETE /v1beta/{name=cachedContents/*}`   
Deletes CachedContent resource.  
`[get](https://ai.google.dev/api/caching#v1beta.cachedContents.get)` |  `GET /v1beta/{name=cachedContents/*}`   
Reads CachedContent resource.  
`[list](https://ai.google.dev/api/caching#v1beta.cachedContents.list)` |  `GET /v1beta/cachedContents`   
Lists CachedContents.  
`[patch](https://ai.google.dev/api/caching#v1beta.cachedContents.patch)` |  `PATCH /v1beta/{cachedContent.name=cachedContents/*}`   
Updates CachedContent resource (only expiration is updatable).  
  
## REST Resource: [v1beta.fileSearchStores](https://ai.google.dev/api/file-search/file-search-stores#v1beta.fileSearchStores)

Methods  
---  
`[create](https://ai.google.dev/api/file-search/file-search-stores#v1beta.fileSearchStores.create)` |  `POST /v1beta/fileSearchStores`   
Creates an empty `FileSearchStore`.  
`[delete](https://ai.google.dev/api/file-search/file-search-stores#v1beta.fileSearchStores.delete)` |  `DELETE /v1beta/{name=fileSearchStores/*}`   
Deletes a `FileSearchStore`.  
`[get](https://ai.google.dev/api/file-search/file-search-stores#v1beta.fileSearchStores.get)` |  `GET /v1beta/{name=fileSearchStores/*}`   
Gets information about a specific `FileSearchStore`.  
`[importFile](https://ai.google.dev/api/file-search/file-search-stores#v1beta.fileSearchStores.importFile)` |  `POST /v1beta/{fileSearchStoreName=fileSearchStores/*}:importFile`   
Imports a `File` from File Service to a `FileSearchStore`.  
`[list](https://ai.google.dev/api/file-search/file-search-stores#v1beta.fileSearchStores.list)` |  `GET /v1beta/fileSearchStores`   
Lists all `FileSearchStores` owned by the user.  
  
## REST Resource: [v1beta.fileSearchStores.documents](https://ai.google.dev/api/file-search/documents#v1beta.fileSearchStores.documents)

Methods  
---  
`[delete](https://ai.google.dev/api/file-search/documents#v1beta.fileSearchStores.documents.delete)` |  `DELETE /v1beta/{name=fileSearchStores/*/documents/*}`   
Deletes a `Document`.  
`[get](https://ai.google.dev/api/file-search/documents#v1beta.fileSearchStores.documents.get)` |  `GET /v1beta/{name=fileSearchStores/*/documents/*}`   
Gets information about a specific `Document`.  
`[list](https://ai.google.dev/api/file-search/documents#v1beta.fileSearchStores.documents.list)` |  `GET /v1beta/{parent=fileSearchStores/*}/documents`   
Lists all `Document`s in a `Corpus`.  
  
## REST Resource: [v1beta.fileSearchStores.operations](https://ai.google.dev/api/file-search/file-search-stores#v1beta.fileSearchStores.operations)

Methods  
---  
`[get](https://ai.google.dev/api/file-search/file-search-stores#v1beta.fileSearchStores.operations.get)` |  `GET /v1beta/{name=fileSearchStores/*/operations/*}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v1beta.fileSearchStores.upload.operations](https://ai.google.dev/api/file-search/file-search-stores#v1beta.fileSearchStores.upload.operations)

Methods  
---  
`[get](https://ai.google.dev/api/file-search/file-search-stores#v1beta.fileSearchStores.upload.operations.get)` |  `GET /v1beta/{name=fileSearchStores/*/upload/operations/*}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v1beta.files](https://ai.google.dev/api/files#v1beta.files)

Methods  
---  
`[delete](https://ai.google.dev/api/files#v1beta.files.delete)` |  `DELETE /v1beta/{name=files/*}`   
Deletes the `File`.  
`[get](https://ai.google.dev/api/files#v1beta.files.get)` |  `GET /v1beta/{name=files/*}`   
Gets the metadata for the given `File`.  
`[list](https://ai.google.dev/api/files#v1beta.files.list)` |  `GET /v1beta/files`   
Lists the metadata for `File`s owned by the requesting project.  
`[register](https://ai.google.dev/api/files#v1beta.files.register)` |  `POST /v1beta/files:register`   
Registers a Google Cloud Storage files with FileService.  
  
## REST Resource: v1beta.media

Methods  
---  
`[upload](https://ai.google.dev/api/files#v1beta.media.upload)` |  `POST /v1beta/files`   
`POST /upload/v1beta/files`   
Creates a `File`.  
`[uploadToFileSearchStore](https://ai.google.dev/api/file-search/file-search-stores#v1beta.media.uploadToFileSearchStore)` |  `POST /v1beta/{fileSearchStoreName=fileSearchStores/*}:uploadToFileSearchStore`   
`POST /upload/v1beta/{fileSearchStoreName=fileSearchStores/*}:uploadToFileSearchStore`   
Uploads data to a FileSearchStore, preprocesses and chunks before storing it in a FileSearchStore Document.  
  
## REST Resource: [v1beta.models](https://ai.google.dev/api/models#v1beta.models)

Methods  
---  
`[asyncBatchEmbedContent](https://ai.google.dev/api/embeddings#v1beta.models.asyncBatchEmbedContent)` |  `POST /v1beta/{batch.model=models/*}:asyncBatchEmbedContent`   
Enqueues a batch of `EmbedContent` requests for batch processing.  
`[batchEmbedContents](https://ai.google.dev/api/embeddings#v1beta.models.batchEmbedContents)` |  `POST /v1beta/{model=models/*}:batchEmbedContents`   
Generates multiple embedding vectors from the input `Content` which consists of a batch of strings represented as `EmbedContentRequest` objects.  
`[batchGenerateContent](https://ai.google.dev/api/batch-api#v1beta.models.batchGenerateContent)` |  `POST /v1beta/{batch.model=models/*}:batchGenerateContent`   
Enqueues a batch of `GenerateContent` requests for batch processing.  
`[countTokens](https://ai.google.dev/api/tokens#v1beta.models.countTokens)` |  `POST /v1beta/{model=models/*}:countTokens`   
Runs a model's tokenizer on input `Content` and returns the token count.  
`[embedContent](https://ai.google.dev/api/embeddings#v1beta.models.embedContent)` |  `POST /v1beta/{model=models/*}:embedContent`   
Generates a text embedding vector from the input `Content` using the specified [Gemini Embedding model](https://ai.google.dev/gemini-api/docs/models/gemini#text-embedding).  
`[generateContent](https://ai.google.dev/api/generate-content#v1beta.models.generateContent)` |  `POST /v1beta/{model=models/*}:generateContent`   
Generates a model response given an input `GenerateContentRequest`.  
`[get](https://ai.google.dev/api/models#v1beta.models.get)` |  `GET /v1beta/{name=models/*}`   
Gets information about a specific `Model` such as its version number, token limits, [parameters](https://ai.google.dev/gemini-api/docs/models/generative-models#model-parameters) and other metadata.  
`[list](https://ai.google.dev/api/models#v1beta.models.list)` |  `GET /v1beta/models`   
Lists the [`Model`s](https://ai.google.dev/gemini-api/docs/models/gemini) available through the Gemini API.  
`[predict](https://ai.google.dev/api/models#v1beta.models.predict)` |  `POST /v1beta/{model=models/*}:predict`   
Performs a prediction request.  
`[predictLongRunning](https://ai.google.dev/api/models#v1beta.models.predictLongRunning)` |  `POST /v1beta/{model=models/*}:predictLongRunning`   
Same as Predict but returns an LRO.  
`[streamGenerateContent](https://ai.google.dev/api/generate-content#v1beta.models.streamGenerateContent)` |  `POST /v1beta/{model=models/*}:streamGenerateContent`   
Generates a [streamed response](https://ai.google.dev/gemini-api/docs/text-generation?lang=python#generate-a-text-stream) from the model given an input `GenerateContentRequest`.  
  
## REST Resource: [v1beta.interactions](https://ai.google.dev/api/interactions-api)

Methods  
---  
`[CreateInteraction](https://ai.google.dev/api/interactions-api#CreateInteraction)` |  `POST /v1beta/interactions`   
Creates a new interaction.  
`[cancelInteractionById](https://ai.google.dev/api/interactions-api#cancelInteractionById)` |  `POST /v1beta/interactions/{interactionsId}/cancel`   
Cancels an interaction by id.  
`[getInteractionById](https://ai.google.dev/api/interactions-api#getInteractionById)` |  `GET /v1beta/interactions/{interactionsId}`   
Retrieves the full details of a single interaction based on its `Interaction.id`.  
`[deleteInteraction](https://ai.google.dev/api/interactions-api#deleteInteraction)` |  `DELETE /v1beta/interactions/{interactionsId}`   
Deletes the interaction by id.  
  
## REST Resource: [v1beta.agents](https://ai.google.dev/api/agents)

Methods  
---  
`[CreateAgent](https://ai.google.dev/api/agents#CreateAgent)` |  `POST /v1beta/agents`   
Creates a new Agent (Typed version for SDK).  
`[ListAgents](https://ai.google.dev/api/agents#ListAgents)` |  `GET /v1beta/agents`   
Lists all Agents.  
`[GetAgent](https://ai.google.dev/api/agents#GetAgent)` |  `GET /v1beta/agents/{agentsId}`   
Gets a specific Agent.  
`[DeleteAgent](https://ai.google.dev/api/agents#DeleteAgent)` |  `DELETE /v1beta/agents/{agentsId}`   
Deletes an Agent.  
  
## REST Resource: [v1beta.webhooks](https://ai.google.dev/api/webhooks)

Methods  
---  
`[CreateWebhook](https://ai.google.dev/api/webhooks#CreateWebhook)` |  `POST /v1beta/webhooks`   
Creates a new Webhook.  
`[PingWebhook](https://ai.google.dev/api/webhooks#PingWebhook)` |  `POST /v1beta/webhooks/{id}:ping`   
Sends a ping event to a Webhook.  
`[RotateSigningSecret](https://ai.google.dev/api/webhooks#RotateSigningSecret)` |  `POST /v1beta/webhooks/{id}:rotateSigningSecret`   
Generates a new signing secret for a Webhook.  
`[ListWebhooks](https://ai.google.dev/api/webhooks#ListWebhooks)` |  `GET /v1beta/webhooks`   
Lists all Webhooks.  
`[GetWebhook](https://ai.google.dev/api/webhooks#GetWebhook)` |  `GET /v1beta/webhooks/{id}`   
Gets a specific Webhook.  
`[UpdateWebhook](https://ai.google.dev/api/webhooks#UpdateWebhook)` |  `PATCH /v1beta/webhooks/{id}`   
Updates an existing Webhook.  
`[DeleteWebhook](https://ai.google.dev/api/webhooks#DeleteWebhook)` |  `DELETE /v1beta/webhooks/{id}`   
Deletes a Webhook.  
  
## REST Resource: [v1beta.triggers](https://ai.google.dev/api/triggers)

Methods  
---  
`[CreateTrigger](https://ai.google.dev/api/triggers#CreateTrigger)` |  `POST /v1beta/triggers`   
Creates a new trigger that will invoke the specified agent on the given cron schedule.  
`[RunTrigger](https://ai.google.dev/api/triggers#RunTrigger)` |  `POST /v1beta/triggers/{triggerId}/executions`   
Runs a trigger immediately.  
`[ListTriggers](https://ai.google.dev/api/triggers#ListTriggers)` |  `GET /v1beta/triggers`   
Lists triggers for a project.  
`[GetTrigger](https://ai.google.dev/api/triggers#GetTrigger)` |  `GET /v1beta/triggers/{id}`   
Gets details of a single trigger.  
`[ListTriggerExecutions](https://ai.google.dev/api/triggers#ListTriggerExecutions)` |  `GET /v1beta/triggers/{triggerId}/executions`   
Lists executions for a trigger.  
`[UpdateTrigger](https://ai.google.dev/api/triggers#UpdateTrigger)` |  `PATCH /v1beta/triggers/{id}`   
Updates a trigger.  
`[DeleteTrigger](https://ai.google.dev/api/triggers#DeleteTrigger)` |  `DELETE /v1beta/triggers/{id}`   
Deletes a trigger.  
  
## REST Resource: [v1beta.environments](https://ai.google.dev/api/environments)

Methods  
---  
`[CreateEnvironment](https://ai.google.dev/api/environments#CreateEnvironment)` |  `POST /v1beta/environments`   
Creates an environment.  
`[ListEnvironments](https://ai.google.dev/api/environments#ListEnvironments)` |  `GET /v1beta/environments`   
Lists environments.  
`[GetEnvironmentFiles](https://ai.google.dev/api/environments#GetEnvironmentFiles)` |  `GET /v1beta/environments/{environment}/files/{path}`   
Retrieves file metadata or directory contents from an environment's snapshot.  
`[GetEnvironment](https://ai.google.dev/api/environments#GetEnvironment)` |  `GET /v1beta/environments/{id}`   
Gets an environment.  
`[StartEnvironmentFileUpload](https://ai.google.dev/api/environments#StartEnvironmentFileUpload)` |  `PUT /upload/v1beta/environments/{environment}/files/{path}`   
Starts a resumable upload session for a file in an environment workspace.  
`[DeleteEnvironment](https://ai.google.dev/api/environments#DeleteEnvironment)` |  `DELETE /v1beta/environments/{id}`   
Deletes an environment.  
  
## REST Resource: [v1beta.voices](https://ai.google.dev/api/voices)

Methods  
---  
`[CreateVoice](https://ai.google.dev/api/voices#CreateVoice)` |  `POST /v1beta/voices`   
Creates a custom voice from a natural-language prompt (`VOICE_TYPE_PROMPTED`) or from reference and consent audio recordings (`VOICE_TYPE_REPLICATED`).  
`[ListVoices](https://ai.google.dev/api/voices#ListVoices)` |  `GET /v1beta/voices`   
Lists custom stored voices owned by the caller (ordered newest first) followed by prebuilt system voices from Google's voice catalog.  
`[GetVoice](https://ai.google.dev/api/voices#GetVoice)` |  `GET /v1beta/voices/{voicesId}`   
Gets a custom stored voice (`store = true`) by resource name.  
`[DeleteVoice](https://ai.google.dev/api/voices#DeleteVoice)` |  `DELETE /v1beta/voices/{voicesId}`   
Deletes a custom stored voice (`store = true`) by resource name.  
  
## REST Resource: [v1beta.credentials](https://ai.google.dev/api/credentials)

Methods  
---  
`[CreateCredential](https://ai.google.dev/api/credentials#CreateCredential)` |  `POST /v1beta/credentials`   
Creates a new credential.  
`[ListCredentials](https://ai.google.dev/api/credentials#ListCredentials)` |  `GET /v1beta/credentials`   
Lists credentials.  
`[GetCredential](https://ai.google.dev/api/credentials#GetCredential)` |  `GET /v1beta/credentials/{id}`   
Gets a credential by ID.  
`[UpdateCredential](https://ai.google.dev/api/credentials#UpdateCredential)` |  `PATCH /v1beta/credentials/{id}`   
Updates a credential.  
`[DeleteCredential](https://ai.google.dev/api/credentials#DeleteCredential)` |  `DELETE /v1beta/credentials/{id}`   
Deletes a credential.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/
title: Register and call remote AI models in AlloyDB Omni overview \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.5.2 \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:44:19.270100+00:00
---

# Register and call remote AI models in AlloyDB Omni overview  |  AlloyDB Omni for Kubernetes: 15.5.2  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/

[ Skip to main content ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/)
  * [Deutsch](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/?hl=de)
  * [Español](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/?hl=es-419)
  * [Français](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/?hl=id)
  * [Italiano](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/?hl=it)
  * [Português](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/?hl=ja)
  * [한국어](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/alloydb-color.svg) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/overview)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/overview)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Overview](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/#overview_3)
  * [How it works](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/#how_it_works_3)
  * [Key concepts](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/#key-concepts)
    * [Model provider {: #model-provider}̦](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/#model_provider_model-provider%CC%A6)
    * [Model type](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/#model-type)
    * [Authentication](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/#authentication_3)
    * [Prediction functions](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/#prediction_functions_3)
    * [Transform functions](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/#transform_functions_3)
    * [HTTP header generation function](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/#http_header_generation_function_3)
  * [What's next](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/#whats_next_3)


This page documents AlloyDB Omni version **15.5.2** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/overview)


Send feedback 
#  Register and call remote AI models in AlloyDB Omni overview Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Overview](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/#overview_3)
  * [How it works](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/#how_it_works_3)
  * [Key concepts](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/#key-concepts)
    * [Model provider {: #model-provider}̦](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/#model_provider_model-provider%CC%A6)
    * [Model type](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/#model-type)
    * [Authentication](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/#authentication_3)
    * [Prediction functions](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/#prediction_functions_3)
    * [Transform functions](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/#transform_functions_3)
    * [HTTP header generation function](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/#http_header_generation_function_3)
  * [What's next](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview/#whats_next_3)


Select a documentation version:  15.5.2keyboard_arrow_down
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/model-endpoint-overview)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/model-endpoint-overview)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-overview)


This page describes a preview that lets you experiment with registering an AI model endpoint and invoking predictions with Model endpoint management in AlloyDB Omni. To use AI models in production environments, see [Build generative AI applications using AlloyDB AI](https://docs.cloud.google.com/alloydb/omni/docs/ai/overview-ai) and [Work with vector embeddings](https://docs.cloud.google.com/alloydb/docs/ai/work-with-embeddings).
To register remote model endpoints with AlloyDB, see [Register and call remote AI models in AlloyDB](https://docs.cloud.google.com/alloydb/docs/ai/model-endpoint-overview).
## Overview
The _Model endpoint management_ preview lets you register a model endpoint, manage model endpoint metadata in your database cluster, and then interact with the models using SQL queries. It provides the [`google_ml_integration`](https://docs.cloud.google.com/alloydb/omni/docs/reference/model-endpoint) extension that includes functions to add and register the model endpoint metadata related to the models, and then use the models to generate vector embeddings or invoke predictions.
Some of the example model types that you can register using model endpoint management are as follows:
  * [Vertex AI](https://docs.cloud.google.com/vertex-ai/docs) text embedding models
  * Embedding models provided by third-party providers, such as Anthropic, Hugging Face, or OpenAI.
  * Custom-hosted text embedding models
  * Generic models with a JSON-based API—for example, `facebook/bart-large-mnli` model hosted on Hugging Face or `gemini-pro` model from the Vertex AI Model Garden


## How it works
You can use model endpoint management to register a model endpoint that complies to the following:
  * Model input and output supports JSON format.
  * Model can be called using the REST protocol.


When you [register a model endpoint with the model endpoint management](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-register-model), it registers each endpoint with a unique model ID that you provided as a reference to the model. You can use this model ID to query models:
  * Generate embeddings to translate text prompts to numerical vectors. You can store generated embeddings as vector data when the `pgvector` extension is enabled in the database.
  * Invoke predictions to call a model using SQL within a transaction.


Your applications can access the model endpoint management using the `google_ml_integration` extension. This extension provides the following functions:
  * The `google_ml.create_model()` SQL function, which is used to register the model endpoint that is used in the prediction or embedding function.
  * The `google_ml.create_sm_secret()` SQL function, which uses secrets in the Google Cloud Secret Manager, where the API keys are stored.
  * The `google_ml.embedding()` SQL function, which is a prediction function that generates text embeddings.
  * The `google_ml.predict_row()` SQL function that generates predictions when you call generic models that support JSON input and output format.
  * Other helper functions that handle generating custom URL, generating HTTP headers, or passing transform functions for your generic models.
  * Functions to manage the registered model endpoints and secrets.


## Key concepts
Before you start using the model endpoint management, understand the concepts required to connect to and use the models.
### Model provider {: #model-provider}̦
_Model provider_ indicates the supported model hosting providers. The following table shows the model provider value you must set based on the model provider you use:  
| Model provider  | Set in function as…  |  
| --- | --- |  
| Vertex AI  | `google`  |  
| Hugging Face models  | `custom`  |  
| Anthropic models  | `custom`  |  
| Other models  | `custom`  |  
| OpenAI  | `open_ai`  |  
The default model provider is `custom`.
Based on the provider type, the supported authentication method differs. The Vertex AI models use the AlloyDB service account to authenticate, while other providers can use the Secret Manager to authenticate. 
### Model type
_Model type_ indicates the type of the AI model. The extension supports text embedding as well as any generic model type. The supported model type you can set when registering a model endpoint are `text-embedding` and `generic`. Setting model type is optional when registering generic model endpoints as `generic` is the default model type. 

Text embedding models with built-in support
    The model endpoint management provides built-in support for all versions of the `textembedding-gecko` model by Vertex AI and the `text-embedding-ada-002` model by OpenAI. To register these model endpoints, use the `google_ml.create_model()` function. AlloyDB automatically sets up default transform functions for these models.     The model type for these models is `text-embedding`. 

Other text embedding models
    For other text embedding models, you need to create transform functions to handle the input and output formats that the model supports. Optionally, you can use the HTTP header generation function that generates custom headers required by your model.     The model type for these models is `text-embedding`. 

Generic models
    The model endpoint management also supports registering of all other model types apart from text embedding models. To invoke predictions for generic models, use the `google_ml.predict_row()` function. You can set model endpoint metadata, such as a request endpoint and HTTP headers that are specific to your model.      You cannot pass transform functions when you are registering a generic model endpoint. Ensure that when you invoke predictions the input to the function is in the JSON format, and that you parse the JSON output to derive the final output.     The model type for these models is `generic`.
### Authentication
_Auth types_ indicate the authentication type that you can use to connect to the model endpoint management using the `google_ml_integration` extension. Setting authentication is optional and is required only if you need to authenticate to access your model.
For Vertex AI models, the AlloyDB service account is used for authentication. For other models, API key or bearer token that is stored as a secret in the Secret Manager can be used with the `google_ml.create_sm_secret()` SQL function.
The following table shows the auth types that you can set:  
| Authentication method  | Set in function as…  | Model provider  |  
| --- | --- | --- |  
| AlloyDB service agent  | `alloydb_service_agent_iam`  | Vertex AI provider  |  
| Secret Manager  | `secret_manager`  | third-party providers, such as Anthropic, Hugging Face, or OpenAI  |  
### Prediction functions
The `google_ml_integration` extension includes the following prediction functions: 

`google_ml.embedding()`
    Used to call a registered text embedding model endpoint to generate embeddings. It includes built-in support for the `textembedding-gecko` model by Vertex AI and the `text-embedding-ada-002` model by OpenAI.     For text embedding models without built-in support, the input and output parameters are unique to a model and need to be transformed for the function to call the model. Create a transform input function to transform input of the prediction function to the model specific input, and a transform output function to transform model specific output to the prediction function output.  

`google_ml.predict_row()`
    Used to call a registered generic model endpoint, as long as they support JSON-based API, to invoke predictions.
### Transform functions
Transform functions modify the input to a format that the model understands, and convert the model response to the format that the prediction function expects. The transform functions are used when registering the `text-embedding` model endpoint without built-in support. The signature of the transform functions depends on the prediction function for the model type.
You cannot use transform functions when registering a `generic` model endpoint.
The following shows the signatures for the prediction function for text embedding models:

```
// define custom model specific input/output transform functions.
CREATE OR REPLACE FUNCTION input_transform_function(model_id VARCHAR(100), input_text TEXT) RETURNS JSON;

CREATE OR REPLACE FUNCTION output_transform_function(model_id VARCHAR(100), response_json JSON) RETURNS real[];

```

For more information about how to create transform functions, see [Transform functions example](https://docs.cloud.google.com/alloydb/docs/reference/model-endpoint#transform-function).
### HTTP header generation function
The HTTP header generation function generates the output in JSON key value pairs that are used as HTTP headers. The signature of the prediction function defines the signatures of the header generation function.
The following example shows the signature for the `google_ml.embedding()` prediction function.

```
CREATE OR REPLACE FUNCTION generate_headers(model_id VARCHAR(100), input TEXT) RETURNS JSON;

```

For the `google_ml.predict_row()` prediction function, the signature is as follows:

```
CREATE OR REPLACE FUNCTION generate_headers(model_id VARCHAR(100), input JSON) RETURNS JSON;

```

For more information about how to create a header generation function, see [HTTP header generation function](https://docs.cloud.google.com/alloydb/docs/reference/model-endpoint#header-gen-function).
## What's next
  * [Register a model endpoint with model endpoint management](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-register-model).
  * Learn about the [model endpoint management reference](https://docs.cloud.google.com/alloydb/docs/reference/model-endpoint-reference).


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

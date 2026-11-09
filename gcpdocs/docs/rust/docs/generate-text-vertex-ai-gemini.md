---
url: https://docs.cloud.google.com/rust/docs/generate-text-vertex-ai-gemini/
title: Generate text using Gemini \u00a0|\u00a0 Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-09T07:07:04.695642+00:00
---

# Generate text using Gemini  |  Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/generate-text-vertex-ai-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Generate text using Gemini Stay organized with collections  Save and categorize content based on your preferences. 

In this guide, you send a text prompt request and a multimodal prompt and image request to the Vertex AI Gemini API and view the responses.

## Prerequisites

To complete this guide, you must have a Google Cloud project with the Vertex AI API enabled. Follow the [Vertex AI setup guide](https://docs.cloud.google.com/vertex-ai/docs/start/cloud-environment) to complete these steps.

## Add the Vertex AI client library as a dependency

The Vertex AI client library includes many features. To speed up compilation, enable only the features that you need:
    
    
    cargo add google-cloud-aiplatform-v1 --no-default-features --features prediction-service
    

## Send a prompt to the Vertex AI Gemini API

  1. Initialize the client using the default settings: 
         
         let client = PredictionService::builder().build().await?;

  2. Build the model name. This example receives the project ID as an argument, uses a fixed location (`global`), and sets the model to a specific version of Gemini. If you run this function in your own code, pass the project ID (without any `projects/` prefix) of the project that you selected in the prerequisites: 
         
         const MODEL: &str = "gemini-3.8-flash";
         let model = format!("projects/{project_id}/locations/global/publishers/google/models/{MODEL}");

  3. Send the request: 
         
         let response = client
             .generate_content()
             .set_model(&model)
             .set_contents([Content::new()
                 .set_role("user")
                 .set_parts([Part::new().set_text(
                     "What's a good name for a flower shop that specializes in selling bouquets of dried flowers?",
                 )])])
             .send()
             .await;

  4. Print the response. You can use the `:#?` format specifier to format the nested response objects: 
         
         println!("RESPONSE = {response:#?}");




### Text prompt: complete code
    
    
    use google_cloud_aiplatform_v1::client::PredictionService;
    use google_cloud_aiplatform_v1::model::{Content, Part};
    
    pub async fn sample(project_id: &str) -> anyhow::Result<()> {
        let client = PredictionService::builder().build().await?;
    
        const MODEL: &str = "gemini-3.8-flash";
        let model = format!("projects/{project_id}/locations/global/publishers/google/models/{MODEL}");
    
        let response = client
            .generate_content()
            .set_model(&model)
            .set_contents([Content::new()
                .set_role("user")
                .set_parts([Part::new().set_text(
                    "What's a good name for a flower shop that specializes in selling bouquets of dried flowers?",
                )])])
            .send()
            .await;
        println!("RESPONSE = {response:#?}");
    
        Ok(())
    }

## Send a prompt and an image to the Vertex AI Gemini API

  1. Initialize the client using the default settings: 
         
         let client = PredictionService::builder().build().await?;

  2. Build the model name: 
         
         const MODEL: &str = "gemini-3.8-flash";
         let model = format!("projects/{project_id}/locations/global/publishers/google/models/{MODEL}");

  3. Create the image part of the request: 
         
         Part::new().set_file_data(
             FileData::new()
                 .set_mime_type("image/jpeg")
                 .set_file_uri("gs://generativeai-downloads/images/scones.jpg"),
         ),

  4. Create the text prompt part of the request: 
         
         Part::new().set_text("Describe this picture."),

  5. Send the full request: 
         
         let response = client
             .generate_content()
             .set_model(&model)
             .set_contents([Content::new().set_role("user").set_parts([
                 Part::new().set_file_data(
                     FileData::new()
                         .set_mime_type("image/jpeg")
                         .set_file_uri("gs://generativeai-downloads/images/scones.jpg"),
                 ),
                 Part::new().set_text("Describe this picture."),
             ])])
             .send()
             .await;

  6. Print the full response: 
         
         println!("RESPONSE = {response:#?}");




### Prompt and image: complete code
    
    
    use google_cloud_aiplatform_v1::client::PredictionService;
    use google_cloud_aiplatform_v1::model::{Content, FileData, Part};
    
    pub async fn sample(project_id: &str) -> anyhow::Result<()> {
        let client = PredictionService::builder().build().await?;
    
        const MODEL: &str = "gemini-3.8-flash";
        let model = format!("projects/{project_id}/locations/global/publishers/google/models/{MODEL}");
    
        let response = client
            .generate_content()
            .set_model(&model)
            .set_contents([Content::new().set_role("user").set_parts([
                Part::new().set_file_data(
                    FileData::new()
                        .set_mime_type("image/jpeg")
                        .set_file_uri("gs://generativeai-downloads/images/scones.jpg"),
                ),
                Part::new().set_text("Describe this picture."),
            ])])
            .send()
            .await;
        println!("RESPONSE = {response:#?}");
    
        Ok(())
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 

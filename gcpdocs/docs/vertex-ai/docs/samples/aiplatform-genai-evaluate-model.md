---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-genai-evaluate-model/
title: Evaluate a model \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T09:37:43.442300+00:00
---

# Evaluate a model  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-genai-evaluate-model/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Evaluate a model Stay organized with collections  Save and categorize content based on your preferences. 

Evaluate the performance of a generative AI model.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Run a computation-based evaluation pipeline](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/computation-based-eval-pipeline)



## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import os
    
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/vertexai/latest)
    from vertexai.evaluation import EvalResult, EvalTask
    
    # TODO (Developer) Set environment variables
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
    LOCATION_ID = os.getenv("LOCATION_ID", "us-central1")
    MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.5-flash")
    
    
    def evaluate_model() -> EvalResult:
        """Evaluate the performance of a generative AI model."""
    
        [vertexai](https://docs.cloud.google.com/python/docs/reference/vertexai/latest).init(project=PROJECT_ID, location=LOCATION_ID)
    
        # Dataset URI containing input prompts and ground truth labels
        dataset_uri = "gs://cloud-samples-data/ai-platform/generative_ai/llm_classification_bp_input_prompts_with_ground_truth.jsonl"
    
        metric_column_mapping = {"reference": "ground_truth"}
    
        # Define evaluation task
        eval_task = EvalTask(
            dataset=dataset_uri,
            metrics=["exact_match"],
            experiment="gemini-classification-eval",
            metric_column_mapping=metric_column_mapping,
        )
    
        # Define a prompt template so the generative Gemini model produces formatted labels
        prompt_template = (
            "Classify the following text into exactly one category from "
            "[nature, news, sports, health, startups]. Return only the category name:\n\n{prompt}"
        )
    
        # Evaluate using a modern Gemini model
        eval_result = eval_task.[evaluate](https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai._genai.evals.Evals.html#vertexai__genai_evals_Evals_evaluate)(
            model=MODEL_NAME,
            prompt_template=prompt_template,
        )
    
        print("=== SUMMARY METRICS ===")
        print(eval_result.summary_metrics)
    
        print("\n=== METRICS TABLE SAMPLE ===")
        print(eval_result.metrics_table.head())
    
        return eval_result
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=vertexai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

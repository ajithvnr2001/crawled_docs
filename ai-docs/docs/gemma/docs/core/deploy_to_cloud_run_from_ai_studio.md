---
url: https://ai.google.dev/gemma/docs/core/deploy_to_cloud_run_from_ai_studio/
title: Deploy Gemma 3 to Cloud Run with Google AI Studio
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:45:38.365902+00:00
---

# Deploy Gemma 3 to Cloud Run with Google AI Studio

> Source: https://ai.google.dev/gemma/docs/core/deploy_to_cloud_run_from_ai_studio/

This guide shows how to deploy Gemma 3 open models on a [Cloud Run](https://cloud.google.com/run/docs/overview/what-is-cloud-run) with a single click in [Google AI Studio](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart).

Google AI Studio is a browser-based platform that lets you quickly try out models and experiment with different prompts. After you've entered a chat prompt to design a prototype web app that uses the selected Gemma 3 model, you can select **Deploy to Cloud Run** to run the Gemma model on a [GPU-enabled Cloud Run service](https://cloud.google.com/run/docs/overview/what-is-cloud-run).

By using Google AI Studio to deploy a generated front-end service to Cloud Run, you skip most of the setup steps of preparing a container since Cloud Run provides a [prebuilt container](https://github.com/google-gemma/cookbook/tree/main/apps/Gemma-on-Cloudrun) for serving Gemma open models on Cloud Run that supports the Google Gen AI SDK.

## Get started with Google AI Studio

This section guides you through deploying Gemma 3 to Cloud Run using Google AI Studio.

  1. Select a Gemma model in Google AI Studio.

[Go to Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemma-3-1b-it)

In the **Run settings** panel on the **Chat** page, use the default Gemma model, or select one of the Gemma models.

  2. In the top bar, select **View more actions** and click **Deploy to Cloud Run**.

  3. In the **Deploy Gemma 3 on Google Cloud Run** dialog, follow the prompts to create a new Google Cloud project, or select an existing project. You might be prompted to enable billing if there is no associated billing account.

  4. After Google AI Studio verifies your project, click **Deploy to Google Cloud**.

  5. After the Gemma 3 model has successfully deployed to Google Cloud, the dialog displays the following:

     * A Cloud Run endpoint URL of your Cloud Run service running Gemma 3 and Ollama.
     * A generated API Key that is used for authentication with the [Gemini API libraries](https://ai.google.dev/gemini-api/docs/libraries). This key is configured as an [environment variable](https://cloud.google.com/run/docs/configuring/services/environment-variables) of the deployed Cloud Run service to authorize incoming requests. We recommend that you modify the API key to use IAM authentication. For more details, see [Securely interact with the Google Gen AI SDK](https://cloud.google.com/run/docs/run-gemma-on-cloud-run#securely-interact-with-gen-ai-sdk).
     * A link to the Cloud Run service in the Google Cloud console. To learn about the default configuration settings for your Cloud Run service, go to the link, then select **Edit & deploy new revision** to view or modify the configuration settings.
  6. To view the Gemini API sample code that was used to create the Cloud Run service, select **Get Code**.

  7. Optional: Copy the code and make modifications as needed.




With your code, you can use the deployed Cloud Run endpoint and API key with the [Google Gen AI SDK](https://ai.google.dev/gemini-api/docs/libraries).

For example, if you are using the [Google Gen AI SDK for Python](https://ai.google.dev/gemini-api/docs/libraries), the Python code might look as follows:
    
    
    from google import genai
    from google.genai.types import HttpOptions
    
    # Configure the client to use your Cloud Run endpoint and API key
    client = genai.Client(api_key="<YOUR_API_KEY>", http_options=HttpOptions(base_url="<cloud_run_url>"))
    
    
    # Example: Generate content (non-streaming)
    response = client.models.generate_content(
       model="<model>", # Replace model with the Gemma 3 model you selected in Google AI Studio, such as "gemma-3-1b-it".
       contents=["How does AI work?"]
    )
    print(response.text)
    
    
    # Example: Stream generate content
    response = client.models.generate_content_stream(
       model="<model>", # Replace model with the Gemma 3 model you selected in Google AI Studio, such as "gemma-3-1b-it".
       contents=["Write a story about a magic backpack. You are the narrator of an interactive text adventure game."]
    )
    for chunk in response:
       print(chunk.text, end="")
    

## Considerations

When you deploy a Cloud Run service from Google AI Studio, consider the following:

  * **Pricing** : [Cloud Run](https://cloud.google.com/run/pricing) is a billable component. To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator).
  * **Quota** : Cloud Run automatically makes the request for `Request Total Nvidia L4 GPU allocation, per project per region` quota under the Cloud Run Admin API.
  * **App Proxy Server** : The deployed service uses the [Google AI Studio Gemini App Proxy Server](https://github.com/google-gemini/aistudio-showcase/tree/main/src/server_proxy) to wrap Ollama and make your service compatible with the Gemini API.
  * **Permissions** : If you need to modify your Cloud Run service, you must have the [required IAM roles](https://cloud.google.com/run/docs/run-gemma-on-cloud-run#before-you-begin) granted to your account on your project.
  * **Authentication** : By default, when you deploy a Cloud Run service from Google AI Studio, the service is deployed with [public (unauthenticated) access](https://cloud.google.com/run/docs/authenticating/public) (`--allow-unauthenticated` flag). To use a stronger security mechanism, we recommend that you [authenticate with IAM](https://cloud.google.com/run/docs/run-gemma-on-cloud-run#securely-interact-with-gen-ai-sdk).



## What's next

Learn about best practices for securing and optimizing performance when you [deploy to Cloud Run from Google AI Studio](https://cloud.google.com/run/docs/run-gemma-on-cloud-run).

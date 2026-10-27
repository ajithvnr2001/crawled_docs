---
url: https://ai.google.dev/gemini-api/docs/logs-datasets/
title: Logs and datasets
method: scrapling+scrapegraph
fetched_at: 2026-10-27T09:34:57.080022+00:00
---

# Logs and datasets

> Source: https://ai.google.dev/gemini-api/docs/logs-datasets/

In this guide you'll learn how to view logs from Gemini API usage in the Google AI Studio dashboard to better understand model behavior and how users may be interacting with your applications. Use logging to observe, debug, and _optionally share usage feedback with Google to help improve Gemini across developer use cases_.[*](https://ai.google.dev/gemini-api/docs/logs-policy)

All `GenerateContent`, `BatchGenerateContent`, `StreamGenerateContent` API calls, and [Interactions](https://ai.google.dev/gemini-api/docs/interactions) API calls excluding Managed Agents are supported. This includes calls made through [OpenAI compatibility](https://ai.google.dev/gemini-api/docs/openai) endpoints.

## Configure project logging

By default, both the [Interactions](https://ai.google.dev/gemini-api/docs/interactions) API and the Generate Content API store requests (`store=true`). For the Interactions API, this also enables server-side state management features.

In Google [AI Studio](https://aistudio.google.com/logs) you can enable or disable storage for individual projects and change these preferences at any time through the **Settings** panel in your [Gemini API Logs Dashboard](https://aistudio.google.com/logs). You can toggle logging on or off independently for the `generateContent` API and the [Interactions](https://ai.google.dev/gemini-api/docs/interactions) API to change the default storage behavior for a project.

### Request-level logging

Both APIs store requests by default (`store=true`):

  * **[Interactions API](https://ai.google.dev/gemini-api/docs/interactions):** Stores requests by default to simplify server-side state management.
  * **Generate Content API (`generateContent`, `streamGenerateContent`, and `batchGenerateContent`):** Stores requests by default for projects created on or after October 26, 2026. Projects created before that date don't store requests by default (`store=false`) unless logging is enabled in AI Studio.



The request-level `store` property takes precedence over the project-level setting. Setting `store` on Generate Content API requests requires `google-genai` 2.33.0 or later for Python, `@google/genai` 2.31.0 or later for JavaScript, `google-genai` 1.79.0 or later for Java, and `google.golang.org/genai` 1.76.0 or later for Go. Here is how you can set the `store` property:

**GenerateContent API**

### Python
    
    
    from google import genai
    
    client = genai.Client()
    
    response = client.models.generate_content(
        model='gemini-3.8-flash',
        contents='Explain quantum entanglement in simple terms.',
        config={'store': True} # Set to False to disable logging of this request
    )
    
    print(response.text)
    

### JavaScript
    
    
    import { GoogleGenAI } from '@google/genai';
    
    const client = new GoogleGenAI({});
    
    const response = await client.models.generateContent({
        model: 'gemini-3.8-flash',
        contents: 'Explain quantum entanglement in simple terms.',
        config: {
            store: true // Set to false to disable logging of this request
        }
    });
    
    console.log(response.text);
    

### Java
    
    
    import com.google.genai.Client;
    import com.google.genai.types.GenerateContentConfig;
    import com.google.genai.types.GenerateContentResponse;
    
    Client client = new Client();
    
    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3.8-flash",
            "Explain quantum entanglement in simple terms.",
            GenerateContentConfig.builder()
                .store(true) // Set to false to disable logging of this request
                .build());
    
    System.out.println(response.text());
    

### Go
    
    
    package main
    
    import (
        "context"
        "fmt"
        "log"
    
        "google.golang.org/genai"
    )
    
    func main() {
        ctx := context.Background()
        client, err := genai.NewClient(ctx, nil)
        if err != nil {
            log.Fatal(err)
        }
    
        response, err := client.Models.GenerateContent(
            ctx,
            "gemini-3.8-flash",
            genai.Text("Explain quantum entanglement in simple terms."),
            &genai.GenerateContentConfig{
                Store: genai.Ptr(true), // Set to false to disable logging of this request
            },
        )
        if err != nil {
            log.Fatal(err)
        }
        fmt.Println(response.Text())
    }
    

**Interactions API**

### Python
    
    
    from google import genai
    
    client = genai.Client()
    
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input="Explain quantum entanglement in simple terms.",
        store=True # Set to False to disable logging of this request
    )
    
    print(interaction.outputs[-1].text)
    

### JavaScript
    
    
    import { GoogleGenAI } from '@google/genai';
    
    const client = new GoogleGenAI({});
    
    const interaction = await client.interactions.create({
        model: 'gemini-3.8-flash',
        input: 'Explain quantum entanglement in simple terms.',
        store: true // Set to false to disable logging of this request
    });
    
    console.log(interaction.outputs[interaction.outputs.length - 1].text);
    

### Java
    
    
    import com.google.genai.Client;
    import com.google.genai.gaos.models.interactions.CreateModelInteraction;
    import com.google.genai.gaos.models.interactions.Interaction;
    import com.google.genai.gaos.models.interactions.InteractionsInput;
    import com.google.genai.gaos.models.interactions.Model;
    import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
    
    Client client = new Client();
    
    CreateModelInteraction params =
        CreateModelInteraction.builder()
            .model(Model.of("gemini-3.8-flash"))
            .input(InteractionsInput.of("Explain quantum entanglement in simple terms."))
            .store(true) // Set to false to disable logging of this request
            .build();
    
    Interaction interaction =
        client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
    
    System.out.println(interaction.outputText().orElse(""));
    

### Go
    
    
    package main
    
    import (
        "context"
        "fmt"
        "log"
    
        "google.golang.org/genai"
        "google.golang.org/genai/interactions/models/interactions"
        "google.golang.org/genai/interactions/models/operations"
    )
    
    func main() {
        ctx := context.Background()
        client, err := genai.NewClient(ctx, nil)
        if err != nil {
            log.Fatal(err)
        }
    
        res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
            Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Explain quantum entanglement in simple terms."),
                Store: genai.Ptr(true), // Set to false to disable logging of this request
            }),
        })
        if err != nil {
            log.Fatal(err)
        }
        if res.Interaction.OutputText != nil {
            fmt.Println(*res.Interaction.OutputText)
        }
    }
    

## View project logs in AI Studio

  1. Go to the Logs page in [AI Studio](https://aistudio.google.com/logs).
  2. Select a project from the drop-down.
  3. Logs will appear in the table in reverse chronological order, if they exist.
  4. For projects created before October 26, 2026, first enable Generate Content API logging in the settings panel to observe project logs for the Generate Content API.



Click an entry for a preview of the payload. You can inspect the full prompt and response from Gemini, and the context from the previous turns. For **Interactions API** requests, logs also include a direct link to the `previous_interaction_id`.

## Configure project storage retention

Logs will expire and be marked for deletion after a default retention window of 55 days (unless saved to a dataset, which don't expire). You can configure the retention window of a project's logs to 7, 14, 28, or 55 days max.

## Create and share datasets

You can save logs to datasets to organize and export them more effectively.

  * From the [Logs page](https://aistudio.google.com/logs), locate the filter bar at the top to select a property to filter by.
  * From your filtered view, use the checkboxes to select all or individual logs.
  * Click the **Create dataset** button that appears at the top of the list.
  * Give your new dataset a name and optional description.
  * You will see the dataset you just created with the curated set of logs.
  * Export your dataset for further analysis as CSV, JSONL files or to Google Sheets.



Datasets can be helpful for a number of different use cases.

  * **Curate challenge sets:** Drive future improvements that target areas where you want your AI to improve.
  * **Curate sample sets:** For example, a sample from real usage to generate responses from another model, or a collection of edge cases for routine checks before deployment.
  * **Evaluation sets:** Sets that are representative of real usage across important capabilities, for comparison across other models or system instruction iterations.



You can contribute to Gemini research and development by choosing to share your datasets with Google as demonstration examples.

## Limitations

Logging is not currently supported for the following:

  * Imagen and Veo models
  * Gemini embedding models
  * Gemini Robotics model
  * Inputs containing videos, GIFs or PDFs
  * Public Preview Agents in the Gemini API



## What's next

  * **Prototype with session history:** Use [AI Studio Build](https://aistudio.google.com/apps) to vibe code apps and add your API key to enable a history of Gemini API logs for AI features.
  * **Re-run logs with the Gemini Batch API:** Use datasets for response sampling and evaluation of models or application logic by re-running logs with the [Gemini Batch API](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb).



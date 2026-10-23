---
url: https://ai.google.dev/gemini-api/docs/api-versions/
title: API versions explained
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:42:49.221149+00:00
---

# API versions explained

> Source: https://ai.google.dev/gemini-api/docs/api-versions/

This document provides a high-level overview of the differences between the `v1` and `v1beta` versions of the Gemini API.

  * **v1** : Stable version of the API. Features in the stable version are fully supported over the lifetime of the major version. If there are any breaking changes, a new major version of the API will be created and the existing version will be deprecated after a reasonable period of time. Non-breaking changes may be introduced to the API without changing the major version. The **Interactions API** and its core features are generally available in `v1`.
  * **v1beta** : This version includes early features and capabilities that are actively being developed. While features in `v1beta` may be subject to changes as we refine them based on feedback, it lets you try new capabilities before they are promoted to stable.



## Capability and feature support

The following table details the availability of capabilities across `v1` (GA) and `v1beta` (Beta). Core API capabilities and tools apply to both the Interactions API and `generateContent` unless specified otherwise:

Feature | v1 | v1beta  
---|---|---  
**Core API capabilities** |  |   
[Interactions API](https://ai.google.dev/gemini-api/docs/get-started) |  |   
[Function Calling](https://ai.google.dev/gemini-api/docs/function-calling) |  |   
[Structured Output](https://ai.google.dev/gemini-api/docs/structured-output) |  |   
[Thinking / Reasoning](https://ai.google.dev/gemini-api/docs/thinking) |  |   
[System Instructions](https://ai.google.dev/gemini-api/docs/system-instructions) |  |   
[Audio Output (Speech Config)](https://ai.google.dev/gemini-api/docs/audio) |  |   
[Service Tier (Priority / Flex)](https://ai.google.dev/gemini-api/docs/priority-inference) |  |   
**Tools** |  |   
[Code Execution Tool](https://ai.google.dev/gemini-api/docs/code-execution) |  |   
[Google Search Grounding](https://ai.google.dev/gemini-api/docs/google-search) |  |   
[Google Maps Grounding](https://ai.google.dev/gemini-api/docs/maps-grounding) |  |   
[URL Context Tool](https://ai.google.dev/gemini-api/docs/url-context) |  |   
[File Search Tool](https://ai.google.dev/gemini-api/docs/file-search) |  |   
[Computer Use Tool](https://ai.google.dev/gemini-api/docs/computer-use) |  |   
[MCP Servers Tool](https://ai.google.dev/gemini-api/docs/function-calling#mcp) |  |   
**Realtime APIs** |  |   
[Live API (WebSockets)](https://ai.google.dev/gemini-api/docs/live-api) |  |   
[Live Music API](https://ai.google.dev/gemini-api/docs/realtime-music-generation) |  |   
[Ephemeral Tokens (Live API)](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens) |  |   
**Platform APIs** |  |   
[Models API](https://ai.google.dev/gemini-api/docs/models) |  |   
[Files Service Route](https://ai.google.dev/gemini-api/docs/files) |  |   
[File Search Stores Route](https://ai.google.dev/gemini-api/docs/file-search) |  |   
[Agents API](https://ai.google.dev/gemini-api/docs/agents) |  |   
[Webhooks API](https://ai.google.dev/gemini-api/docs/webhooks) |  |   
[Context Caching](https://ai.google.dev/gemini-api/docs/caching) |  |   
  
  * \- Supported



## Configure API version in an SDK

The Gemini API SDKs default to `v1beta`, but you can explicitly specify versions by setting the API version as shown in the following code sample:

### Python
    
    
    from google import genai
    
    client = genai.Client(http_options={'api_version': 'v1'})
    
    interaction = client.interactions.create(
        model='gemini-3.8-flash',
        input="Explain how AI works",
    )
    
    print(interaction.output_text)
    

### JavaScript
    
    
    import { GoogleGenAI } from "@google/genai";
    
    const ai = new GoogleGenAI({
      httpOptions: { apiVersion: "v1" },
    });
    
    async function main() {
      const interaction = await ai.interactions.create({
        model: "gemini-3.8-flash",
        input: "Explain how AI works",
      });
      console.log(interaction.output_text);
    }
    
    await main();
    

### Java
    
    
    import com.google.genai.Client;
    import com.google.genai.gaos.models.interactions.CreateModelInteraction;
    import com.google.genai.gaos.models.interactions.InteractionsInput;
    import com.google.genai.gaos.models.interactions.Model;
    import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
    import com.google.genai.types.HttpOptions;
    
    Client client = Client.builder()
        .httpOptions(HttpOptions.builder().apiVersion("v1").build())
        .build();
    
    CreateModelInteraction req = CreateModelInteraction.builder()
        .model(Model.of("gemini-3.6-flash"))
        .input(InteractionsInput.of("Explain how AI works"))
        .build();
    var interaction = client.interactions.create(CreateInteractionRequestBody.of(req)).interaction().get();
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
        client, err := genai.NewClient(ctx, &genai.ClientConfig{
            HTTPOptions: genai.HTTPOptions{
                APIVersion: "v1",
            },
        })
        if err != nil {
            log.Fatal(err)
        }
    
        res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
            Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.6-flash"),
                Input: interactions.NewInteractionsInput("Explain how AI works"),
            }),
        })
        if err != nil {
            log.Fatal(err)
        }
        if res.Interaction.OutputText != nil {
            fmt.Println(*res.Interaction.OutputText)
        }
    }
    

### REST
    
    
    curl -X POST "https://generativelanguage.googleapis.com/v1/interactions" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H 'Content-Type: application/json' \
      -d '{
        "model": "gemini-3.8-flash",
        "input": "Explain how AI works",
      }'
    

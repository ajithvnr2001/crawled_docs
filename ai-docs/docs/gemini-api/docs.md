---
url: https://ai.google.dev/gemini-api/docs/
title: Gemini API
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:42:36.694075+00:00
---

# Gemini API

> Source: https://ai.google.dev/gemini-api/docs/

The Gemini API is the fastest path from prompt to production with Gemini, Veo, Nano Banana, and more. It lets you integrate these generative models into your applications to generate text and images, analyze multimodal inputs, and build conversational agents.

### Python
    
    
    from google import genai
    
    client = genai.Client()
    
    interaction = client.interactions.create(
        model="gemini-4-argon",
        input="Explain how AI works in a few words"
    )
    
    print(interaction.output_text)
    

### JavaScript
    
    
    import { GoogleGenAI } from "@google/genai";
    
    const ai = new GoogleGenAI({});
    
    const interaction = await ai.interactions.create({
      model: "gemini-4-argon",
      input: "Explain how AI works in a few words",
    });
    
    console.log(interaction.output_text);
    

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
            .model(Model.of("gemini-4-argon"))
            .input(InteractionsInput.of("Explain how AI works in a few words"))
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
                Model: interactions.Model("gemini-4-argon"),
                Input: interactions.NewInteractionsInput("Explain how AI works in a few words"),
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
    
    
    curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H 'Content-Type: application/json' \
      -d '{
        "model": "gemini-4-argon",
        "input": "Explain how AI works in a few words"
      }'
    

[Get Started](https://ai.google.dev/gemini-api/docs/get-started) [Create API Key](https://aistudio.google.com/apikey)

* * *

## Meet the models

[View all](https://ai.google.dev/gemini-api/docs/models)

[ auto_awesome Gemini 4 Argon New Our flagship reasoning model with a shared 1M context window and long decodes up to 1M tokens.  ](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon) [ spark Gemini 3.8 Flash New Our most intelligent Flash model, engineered for long-horizon software engineering, autonomous agents, and complex enterprise workflows.  ](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash) [ graphic_eq Gemini 3.8 Flash TTS New Studio-grade text-to-speech model with expressive acting, custom Voice design, and Voice replication.  ](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts) [ spark Gemini 3.5 Flash-Lite  High-volume, cost-sensitive model optimized for low-latency high throughput subagent tasks.  ](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite) [ 🍌 Nano Banana  State-of-the-art image generation and editing models.  ](https://ai.google.dev/gemini-api/docs/image-generation) [ video_library Gemini Omni Flash  Our state-of-the-art video generation and editing model.  ](https://ai.google.dev/gemini-api/docs/omni) [ speech_to_text Gemini 3.5 Transcribe New Low-latency speech-to-text model with utterance-based language detection, speaker diarization, and word timestamps.  ](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe) [ spark Gemini Robotics  A vision-language model (VLM) that brings Gemini's agentic capabilities to robotics and enables advanced reasoning in the physical world.  ](https://ai.google.dev/gemini-api/docs/robotics-overview)

## Explore Capabilities

[ imagesmode Image Generation  Generate and edit highly contextual images natively with Nano Banana.  ](https://ai.google.dev/gemini-api/docs/image-generation) [ article Long Context  Input millions of tokens to Gemini models and derive understanding from unstructured images, videos, and documents.  ](https://ai.google.dev/gemini-api/docs/long-context) [ code Structured Outputs  Constrain Gemini to respond with JSON, a structured data format suitable for automated processing.  ](https://ai.google.dev/gemini-api/docs/structured-output) [ functions Function Calling  Build agentic workflows by connecting Gemini to external APIs and tools.  ](https://ai.google.dev/gemini-api/docs/function-calling) [ videocam Video Generation with Gemini Omni Flash  Create high-quality video content from text or image prompts with our state-of-the-art model.  ](https://ai.google.dev/gemini-api/docs/video) [ android_recorder Voice Agents with Live API  Build real-time voice applications and agents with the Live API.  ](https://ai.google.dev/gemini-api/docs/live) [ build Tools  Connect Gemini to the world through built-in tools like Google Search, URL Context, Google Maps, Code Execution and Computer Use.  ](https://ai.google.dev/gemini-api/docs/tools) [ stacks Document Understanding  Process up to 1000 pages of PDF files with full multimodal understanding or other text-based file types.  ](https://ai.google.dev/gemini-api/docs/document-processing) [ cognition_2 Thinking  Explore how thinking capabilities improve reasoning for complex tasks and agents.  ](https://ai.google.dev/gemini-api/docs/thinking)

## Create agents

Managed Agents give Gemini a workspace to plan and complete tasks on its own. In a single request, Gemini can write and run code, search the web, and create files in a hosted sandbox environment. Start with our prebuilt Antigravity agent, or customize it with your own instructions and tools.

### Python
    
    
    from google import genai
    
    client = genai.Client()
    
    interaction = client.interactions.create(
        agent="antigravity-preview-09-2026",
        input=(
            "Research the top 5 sustainable fashion brands, "
            "compare their materials and pricing tiers, and "
            "build an interactive dashboard in analysis.html."
        ),
        environment="remote"
    )
    
    print(interaction.output_text)
    

### JavaScript
    
    
    import { GoogleGenAI } from "@google/genai";
    
    const ai = new GoogleGenAI({});
    
    const interaction = await ai.interactions.create({
      agent: "antigravity-preview-09-2026",
      input:
        "Research the top 5 sustainable fashion brands, " +
        "compare their materials and pricing tiers, and " +
        "build an interactive dashboard in analysis.html.",
      environment: "remote",
    });
    
    console.log(interaction.output_text);
    

### Java
    
    
    import com.google.genai.Client;
    import com.google.genai.gaos.models.interactions.AgentOption;
    import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
    import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
    import com.google.genai.gaos.models.interactions.Interaction;
    import com.google.genai.gaos.models.interactions.InteractionsInput;
    import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
    
    Client client = new Client();
    
    CreateAgentInteraction params =
        CreateAgentInteraction.builder()
            .agent(AgentOption.of("antigravity-preview-09-2026"))
            .input(
                InteractionsInput.of(
                    "Research the top 5 sustainable fashion brands, "
                        + "compare their materials and pricing tiers, and "
                        + "build an interactive dashboard in analysis.html."))
            .environment(CreateAgentInteractionEnvironment.of("remote"))
            .build();
    
    Interaction interaction =
        client.interactions.create(CreateInteractionRequestBody.of(params))
            .interaction()
            .get();
    
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
            Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
                Agent: interactions.AgentOption("antigravity-preview-09-2026"),
                Input: interactions.NewInteractionsInput(
                    "Research the top 5 sustainable fashion brands, " +
                        "compare their materials and pricing tiers, and " +
                        "build an interactive dashboard in analysis.html.",
                ),
                Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
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
    
    
    curl -X POST \
      "https://generativelanguage.googleapis.com/v1beta/interactions" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H 'Content-Type: application/json' \
      -d '{
        "agent": "antigravity-preview-09-2026",
        "input": "Research the top 5 sustainable fashion brands, compare their materials and pricing tiers, and build an interactive dashboard in analysis.html.",
        "environment": "remote"
      }'
    

[Agents quickstart](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart) [Try in AI Studio](https://aistudio.google.com/prompts/new_chat?model=antigravity-preview-09-2026)

## Interactions API

The **Interactions API** has become our default interface as of June 2026 and is the best way to build with Gemini models and agents going forward. If you're starting a new project, you should use the Interactions API. While it remains supported, the `generateContent` API is now considered legacy.

[ hub Interactions Overview  Learn how the Interactions API manages conversation state, messages, and output formats.  ](https://ai.google.dev/gemini-api/docs/interactions-overview) [ swap_horiz Migration Guide  Step-by-step guide to transition your code from generateContent to the Interactions API.  ](https://ai.google.dev/gemini-api/docs/migrate-to-interactions) [ stream Streaming  Stream real-time tokens, incremental thoughts, and tool call events.  ](https://ai.google.dev/gemini-api/docs/streaming)

[ Google AI Studio  Test prompts, manage your API keys, monitor usage, and build prototypes.  ](https://aistudio.google.com) [ group Developer Community  Ask questions and find solutions from other developers and Google engineers.  ](https://discuss.ai.google.dev/c/gemini-api/4) [ menu_book API Reference  Find detailed information about the Gemini API in the official reference documentation.  ](https://ai.google.dev/api) [ sensors Status  Check the status of Gemini API, Google AI Studio, and our model services.  ](https://aistudio.google.com/status)

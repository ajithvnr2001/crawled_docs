---
url: https://ai.google.dev/gemini-api/docs/migrate-to-cloud/
title: Gemini Developer API vs. Gemini platform
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:44:25.540175+00:00
---

# Gemini Developer API vs. Gemini platform

> Source: https://ai.google.dev/gemini-api/docs/migrate-to-cloud/

When developing generative AI solutions with Gemini, Google offers two API products: the [Gemini Developer API](https://ai.google.dev/gemini-api/docs) and the [Gemini platform API](https://cloud.google.com/gemini-enterprise-agent-platform/overview).

The Gemini Developer API provides the fastest path to build, productionize, and scale Gemini powered applications. Most developers should use the Gemini Developer API unless there is a need for specific enterprise controls.

Gemini platform offers a comprehensive ecosystem of enterprise ready features and services for building and deploying generative AI applications backed by Google Cloud.

We've recently simplified migrating between these services. Both the Gemini Developer API and the Gemini platform API are now accessible through the unified [Google GenAI SDK](https://ai.google.dev/gemini-api/docs/libraries) and the [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview).

## Code comparison: Interactions API (recommended)

The [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview) is the recommended way to build with Gemini models and agents. The following examples compare text generation between the Gemini Developer API and Gemini platform.

### Python

You can access both the Gemini Developer API and Gemini platform services through the `google-genai` library (`>= 2.3.0`). See the [libraries](https://ai.google.dev/gemini-api/docs/libraries) page for instructions on how to install `google-genai`.

### Gemini Developer API
    
    
    from google import genai
    
    client = genai.Client()
    
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input="Explain how AI works in a few words",
    )
    print(interaction.output_text)
    

### Gemini platform API
    
    
    from google import genai
    
    client = genai.Client(
        enterprise=True, project="your-project-id", location="global"
    )
    
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input="Explain how AI works in a few words",
    )
    print(interaction.output_text)
    

### JavaScript and TypeScript

You can access both Gemini Developer API and Gemini platform services through the `@google/genai` library (`>= 2.3.0`). See the [libraries](https://ai.google.dev/gemini-api/docs/libraries) page for instructions on how to install `@google/genai`.

### Gemini Developer API
    
    
    import { GoogleGenAI } from "@google/genai";
    
    const ai = new GoogleGenAI({});
    
    const interaction = await ai.interactions.create({
      model: "gemini-3.8-flash",
      input: "Explain how AI works in a few words",
    });
    console.log(interaction.output_text);
    

### Gemini platform API
    
    
    import { GoogleGenAI } from "@google/genai";
    
    const ai = new GoogleGenAI({
      enterprise: true,
      project: "your_project",
      location: "global",
    });
    
    const interaction = await ai.interactions.create({
      model: "gemini-3.8-flash",
      input: "Explain how AI works in a few words",
    });
    console.log(interaction.output_text);
    

## Code comparison: generateContent API

While the Interactions API is recommended for new projects, the `generateContent` API remains supported.

### Python

You can access both the Gemini Developer API and Gemini platform services through the `google-genai` library. See the [libraries](https://ai.google.dev/gemini-api/docs/libraries) page for instructions on how to install `google-genai`.

### Gemini Developer API
    
    
    from google import genai
    
    client = genai.Client()
    
    response = client.models.generate_content(
        model="gemini-3.8-flash", contents="Explain how AI works in a few words"
    )
    print(response.text)
    

### Gemini platform API
    
    
    from google import genai
    
    client = genai.Client(
        vertexai=True, project='your-project-id', location='us-central1'
    )
    
    response = client.models.generate_content(
        model="gemini-3.8-flash", contents="Explain how AI works in a few words"
    )
    print(response.text)
    

### JavaScript and TypeScript

You can access both Gemini Developer API and Gemini platform services through `@google/genai` library. See [libraries](https://ai.google.dev/gemini-api/docs/libraries) page for instructions on how to install `@google/genai`.

### Gemini Developer API
    
    
    import { GoogleGenAI } from "@google/genai";
    
    const ai = new GoogleGenAI({});
    
    async function main() {
      const response = await ai.models.generateContent({
        model: "gemini-3.8-flash",
        contents: "Explain how AI works in a few words",
      });
      console.log(response.text);
    }
    
    main();
    

### Gemini platform API
    
    
    import { GoogleGenAI } from '@google/genai';
    const ai = new GoogleGenAI({
      vertexai: true,
      project: 'your_project',
      location: 'your_location',
    });
    
    async function main() {
      const response = await ai.models.generateContent({
        model: "gemini-3.8-flash",
        contents: "Explain how AI works in a few words",
      });
      console.log(response.text);
    }
    
    main();
    

### Go

You can access both Gemini Developer API and Gemini platform services through `google.golang.org/genai` library. See [libraries](https://ai.google.dev/gemini-api/docs/libraries) page for instructions on how to install `google.golang.org/genai`.

### Gemini Developer API
    
    
    import (
      "context"
      "encoding/json"
      "fmt"
      "log"
      "google.golang.org/genai"
    )
    
    // Your Google API key
    const apiKey = "your-api-key"
    
    func main() {
      ctx := context.Background()
      client, err := genai.NewClient(ctx, nil)
      if err != nil {
          log.Fatal(err)
      }
    
      // Call the GenerateContent method.
      result, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", genai.Text("Tell me about New York?"), nil)
    
    }
    

### Gemini platform API
    
    
    import (
      "context"
      "encoding/json"
      "fmt"
      "log"
      "google.golang.org/genai"
    )
    
    // Your Google Cloud project
    const project = "your-project"
    
    // A Google Cloud location like "us-central1"
    const location = "some-gcp-location"
    
    func main() {
      ctx := context.Background()
      client, err := genai.NewClient(ctx, &genai.ClientConfig
      {
            Project:  project,
          Location: location,
          Backend:  genai.BackendVertexAI,
      })
    
      // Call the GenerateContent method.
      result, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", genai.Text("Tell me about New York?"), nil)
    
    }
    

### Other use cases and platforms

Refer to use case specific guides on [Gemini Developer API Documentation](https://ai.google.dev/gemini-api/docs) and [Gemini platform documentation](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview) for other platforms and use cases.

## Migration considerations

When you migrate:

  * You'll need to use Google Cloud service accounts to authenticate. See the [Gemini platform documentation](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview) for more information.

  * You can use your existing Google Cloud project (the same one you used to generate your API key) or you can [create a new Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

  * Supported regions may differ between the Gemini Developer API and the Gemini platform API. During Preview, the [Interactions API on Gemini platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/interactions/) only supports the `global` endpoint (`location="global"`). See the list of [supported regions for generative AI on Google Cloud](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/learn/locations-genai).

  * Any models you created in Google AI Studio need to be retrained in Gemini platform.




If you no longer need to use your Gemini API key for the Gemini Developer API, then follow security best practices and delete it.

To delete an API key:

  1. Open the [Google Cloud API Credentials](https://console.cloud.google.com/apis/credentials) page.

  2. Find the API key you want to delete and click the **Actions** icon.

  3. Select **Delete API key**.

  4. In the **Delete credential** modal, select **Delete**.

Deleting an API key takes a few minutes to propagate. After propagation completes, any traffic using the deleted API key is rejected.




## Next steps

  * Explore the [Interactions API on Gemini platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/interactions/) developer guide.
  * See the [Generative AI on Gemini platform overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview) to learn more about generative AI solutions on Gemini platform.



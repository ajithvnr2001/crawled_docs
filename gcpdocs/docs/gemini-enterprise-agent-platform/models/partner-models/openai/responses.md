---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/openai/responses/
title: Responses API \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T05:51:13.707113+00:00
---

# Responses API  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/openai/responses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Responses API Stay organized with collections  Save and categorize content based on your preferences. 

**Private Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

OpenAI partner models on Gemini Enterprise Agent Platform support the OpenAI Responses API (`publishers/openai/v1/responses`) for text generation from text and image inputs, tool calling, reasoning effort control, and conversation compaction.

## Before you begin

To use OpenAI partner models with Gemini Enterprise Agent Platform, you must complete the following steps. The Gemini Enterprise Agent Platform API (`aiplatform.googleapis.com`) must be enabled on your Google Cloud project.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Gemini Enterprise Agent Platform API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Gemini Enterprise Agent Platform API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com)

  8. Complete the onboarding steps in [OpenAI GPT Models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/openai#preview-access), including purchasing the product through Google Cloud Marketplace and enabling the model in Model Garden.

  9. If your organization's policy restricts model access, [allow the model in that policy](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/control-model-access).




### Required roles

To get the permissions that you need to call OpenAI partner models, ask your administrator to grant you the [Agent Platform User ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.user) (`roles/aiplatform.user`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Endpoints

OpenAI partner models are served from the following Agent Platform base URLs:

  * **Global endpoint (`global`):** `https://aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/global/publishers/openai/v1`
  * **US multi-region endpoint (`us`):** `https://aiplatform.us.rep.googleapis.com/v1/projects/PROJECT_ID/locations/us/publishers/openai/v1`



Replace `<var>PROJECT_ID</var>` with your Google Cloud project ID.

## Call the Responses API using the OpenAI Python SDK

You can use the official `openai` Python library by setting `base_url` to your Agent Platform endpoint and passing a refreshed Google Cloud OAuth 2.0 access token as `api_key`. Set `store=False` for stateless requests and ZDR workloads.
    
    
    import google.auth
    from google.auth.transport.requests import Request
    from openai import OpenAI
    
    credentials, _ = google.auth.default(
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    credentials.refresh(Request())
    
    project_id = "PROJECT_ID"
    base_url = (
        f"https://aiplatform.googleapis.com/v1/projects/{project_id}"
        "/locations/global/publishers/openai/v1"
    )
    
    client = OpenAI(
        base_url=base_url,
        api_key=credentials.token,
    )
    
    response = client.responses.create(
        model="gpt-6.1-sol",
        input="Explain how Zero Data Retention works on Agent Platform.",
        reasoning={"effort": "medium"},
        store=False,
    )
    print(response.output_text)

### Stream responses

To stream incremental text deltas over server-sent events (SSE), set `stream=True`:
    
    
    import google.auth
    from google.auth.transport.requests import Request
    from openai import OpenAI
    
    credentials, _ = google.auth.default(
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    credentials.refresh(Request())
    
    project_id = "PROJECT_ID"
    base_url = (
        f"https://aiplatform.googleapis.com/v1/projects/{project_id}"
        "/locations/global/publishers/openai/v1"
    )
    
    client = OpenAI(
        base_url=base_url,
        api_key=credentials.token,
    )
    
    stream = client.responses.create(
        model="gpt-6-luna",
        input="Write a short Python function to validate a JSON schema.",
        stream=True,
        store=False,
    )
    
    for event in stream:
        if event.type == "response.output_text.delta":
            print(event.delta, end="")

### Compact conversation history

For long-horizon agentic sessions, call the standalone compaction endpoint (`POST .../responses/compact`) to compress prior messages into an encrypted compaction item that can be passed into subsequent stateless `/responses` calls:
    
    
    import google.auth
    from google.auth.transport.requests import Request
    from openai import OpenAI
    
    credentials, _ = google.auth.default(
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    credentials.refresh(Request())
    
    project_id = "PROJECT_ID"
    base_url = (
        f"https://aiplatform.googleapis.com/v1/projects/{project_id}"
        "/locations/global/publishers/openai/v1"
    )
    
    client = OpenAI(
        base_url=base_url,
        api_key=credentials.token,
    )
    
    compacted = client.responses.compact(
        model="gpt-6-astra",
        input=[
            {"role": "user", "content": "Audit our multi-region VPC firewall rules."},
            {"role": "assistant", "content": "I checked the ingress rules for us-east1 and us-central1."},
        ],
    )
    print(compacted.output)

## Call the Responses API using the OpenAI Node.js SDK

You can use the official `openai` Node.js library with Google Cloud OAuth credentials:
    
    
    import OpenAI from "openai";
    
    const projectId = "PROJECT_ID";
    const client = new OpenAI({
      apiKey: process.env.GOOGLE_CLOUD_ACCESS_TOKEN,
      baseURL: `https://aiplatform.googleapis.com/v1/projects/${projectId}/locations/global/publishers/openai/v1`,
    });
    
    const response = await client.responses.create({
      model: "gpt-6-luna",
      input: "Write a short summary of how authentication works on Agent Platform.",
      store: false,
    });
    console.log(response.output_text);

## Call the Responses API using the OpenAI Go SDK

You can use the official `openai-go` library with Google Cloud OAuth credentials:
    
    
    package main
    
    import (
        "context"
        "fmt"
        "os"
    
        "github.com/openai/openai-go/v3"
        "github.com/openai/openai-go/v3/option"
        "github.com/openai/openai-go/v3/responses"
    )
    
    func main() {
        ctx := context.Background()
        projectID := "PROJECT_ID"
        client := openai.NewClient(
            option.WithAPIKey(os.Getenv("GOOGLE_CLOUD_ACCESS_TOKEN")),
            option.WithBaseURL("https://aiplatform.googleapis.com/v1/projects/"+projectID+"/locations/global/publishers/openai/v1"),
        )
    
        response, err := client.Responses.New(ctx, responses.ResponseNewParams{
            Model: "gpt-6-luna",
            Input: responses.ResponseNewParamsInputUnion{
                OfString: openai.String("Write a one-sentence bedtime story about a unicorn."),
            },
            Store: openai.Bool(false),
        })
        if err != nil {
            panic(err)
        }
        fmt.Println(response.OutputText())
    }

## Call the Responses API using curl

You can send a REST request directly to the Responses API using curl.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID.



HTTP method and URL: 
    
    
    POST https://aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/global/publishers/openai/v1/responses

Request JSON body: 
    
    
    {
      "model": "gpt-6.1-sol",
      "input": "Summarize the key differences between Google Cloud and OpenAI terms.",
      "reasoning": {"effort": "medium"},
      "store": false
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command uses Application Default Credentials. If you haven't set them up, run [`gcloud auth application-default login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login). For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/global/publishers/openai/v1/responses"

#### PowerShell (Windows)

**Note:** The following command uses Application Default Credentials. If you haven't set them up, run [`gcloud auth application-default login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login). For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth application-default print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/global/publishers/openai/v1/responses" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

**Note:** Setting `store: false` configures requests to be stateless, but doesn't enable Zero Data Retention (ZDR). ZDR requires project-level approval from OpenAI.

## Error handling

Build exponential backoff with jitter on 429 and 5xx responses into production workloads.

Status code | Probable cause | Recommended action  
---|---|---  
`401` | Access token expired or invalid. | Refresh your Google Cloud access token and retry the request.  
`403` | Caller identity lacks required permissions, or the API, project, or model isn't enabled. | Verify IAM roles, API enablement, project allowlisting, and Model Garden enablement.  
`404` | Endpoint path, location, or model identifier is incorrect. | Verify the base URL, location segment, and model name.  
`429` | Rate, quota, or available capacity limit reached. | Back off exponentially and retry. Contact your account team if sustained.  
`5xx` | Transient server condition. | Retry with exponential backoff.  
  
## Connect Codex to Google Cloud

You can configure OpenAI Codex (CLI or Desktop App) to route model requests through your Google Cloud project using Google Cloud authentication. For complete setup instructions, interactive sign-in steps, and manual `config.toml` options, see [Connect OpenAI Codex to Google Cloud](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/openai/codex).

## What's next

  * Configure developer tools in [Connect OpenAI Codex to Google Cloud](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/openai/codex).
  * Review model specifications, ZDR procedures, and governing terms in [OpenAI GPT Models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/openai).
  * Learn about [Abuse monitoring](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/abuse-monitoring) and [Zero data retention](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 

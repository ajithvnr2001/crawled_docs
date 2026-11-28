---
url: https://docs.copilotkit.ai/strands/deploy-agentcore/
title: AWS AgentCore
method: scrapling+scrapegraph
fetched_at: 2026-11-28T11:35:20.071742+00:00
---

# AWS AgentCore

> Source: https://docs.copilotkit.ai/strands/deploy-agentcore/

Strands Agents (Python)

# AWS AgentCore

Add a production-ready frontend to your AWS AgentCore agents with CopilotKit.

Copy MarkdownOpen

[AWS Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) gives you a secure, serverless runtime for deploying AG-UI agents at scale. It handles auth, session isolation, and infrastructure. CopilotKit gives those agents a frontend.

## How it worksCopy Anchor Link

The two connect through **CopilotKit Runtime** , a lightweight server-side layer that sits between your browser and AgentCore. This is the same runtime as for any CopilotKit agent. With AgentCore, the runtime must run on the server. Browsers cannot sign SigV4 or OAuth2 requests to AgentCore.

Copy Text
    
    
    Browser → CopilotKit Runtime → AgentCore Runtime → your agent

## What you getCopy Anchor Link

  * **Chat UI** : prebuilt chat interface, or headless APIs to build your own
  * **Shared state** : bidirectional sync between agent state and your frontend UI
  * **Generative UI** : render custom components from tool calls in real time
  * **Human-in-the-loop** : let users review, approve, or redirect agent actions
  * **AgentCore memory** : conversation history persists across sessions via AgentCore's memory layer



## QuickstartCopy Anchor Link

AWS CLI required

Both paths below require AWS credentials configured locally. If you haven't done this yet, follow the [AWS CLI getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) before continuing.

Choose your starting point

Start fresh with our CLI, or connect CopilotKit to an agent you've already deployed on AgentCore.

Start from scratch

Scaffold a complete AgentCore + CopilotKit application with one command.

I already have an agent

I've followed the AWS guide and have an AG-UI agent deployed on AgentCore Runtime.

### Run the CLICopy Anchor Link

Strands

Copy Text
    
    
    npx copilotkit@latest create -f agentcore-strands

The CLI downloads the full AgentCore template and sets up `config.yaml` for you.

### ConfigureCopy Anchor Link

Open `config.yaml` and set your details:

config.yaml

Copy Text
    
    
    stack_name_base: my-agentcore-app   # prefix for all AWS resources (max 35 chars)
    admin_user_email: you@example.com   # where your Cognito invite will be sent

### DeployCopy Anchor Link

One command deploys everything (CDK infrastructure, AgentCore Runtime, and the frontend):

Strands

Copy Text
    
    
    ./deploy-strands.sh

### Open your appCopy Anchor Link

The deploy script prints an Amplify URL when it finishes. Open it and sign in with your `admin_user_email`.

### Run locallyCopy Anchor Link

To run the full stack locally (agent, CopilotKit runtime, and frontend) without deploying:

Copy Text
    
    
    cp .env.example .env
    cp docker/.env.example docker/.env
    cd docker
    # Fill in AWS credentials in docker/.env
    ./up.sh --build

Service| Port| Description  
---|---|---  
`agent`| 8080| Your agent, hot-reloads on `.py` changes  
`bridge`| 3001| CopilotKit Runtime  
`frontend`| 3000| Vite dev server  
  
### Tear downCopy Anchor Link

When done, delete all AWS resources to stop charges:

Copy Text
    
    
    cd infra-cdk && npx cdk destroy --all

To render components from tool calls, see [Generative UI](https://docs.copilotkit.ai/strands/generative-ui/tool-rendering).

## TroubleshootingCopy Anchor Link

### HTTP 401: `Missing Authentication Token`Copy Anchor Link

Copy Text
    
    
    Agent execution failed: Error: HTTP 401:
    {"jsonrpc":"2.0","error":{"code":-32001,"message":"Missing Authentication Token"},"id":"null"}

`Missing Authentication Token` is AWS's own error, not a CopilotKit or agent error. AWS returns it when a request reaches an AgentCore or API Gateway endpoint with no credentials, or when the request path matches no deployed route. Check the following, in order:

  * **The runtime is actually sending a token.** Set `AGENTCORE_ACCESS_TOKEN` in the environment of the Copilot Runtime **server** , not the frontend. If the variable is unset, the `Authorization` header interpolates to `Bearer undefined`, which AWS rejects exactly like a missing header.
  * **The token has not expired.** Cognito access tokens are short-lived. Mint a fresh one and retry before you debug anything else.
  * **`AGENTCORE_ENDPOINT_URL` is the full invocation URL**, ending in `/invocations`, with the agent ARN URL-encoded: `https://bedrock-agentcore.{region}.amazonaws.com/runtimes/{encoded-arn}/invocations`. A URL that stops short of `/invocations` matches no route, and AWS reports that as `Missing Authentication Token` rather than as a 404.
  * **The browser is not calling AgentCore directly.** AgentCore requires SigV4 or OAuth2 signing, which a browser cannot perform. Point the frontend at your Copilot Runtime endpoint and let the runtime make the AgentCore call server-side.



This error does not apply to the local quickstart

The framework quickstarts run the agent locally on `http://localhost:8000`, and a local agent server never returns `Missing Authentication Token`. If you see this error, the runtime is pointed at a deployed AWS endpoint.

How is this guide?

GoodBad

[Previous PageWebMCP](https://docs.copilotkit.ai/strands/webmcp)[Next PageAdd to Existing Threads](https://docs.copilotkit.ai/strands/threads-import)

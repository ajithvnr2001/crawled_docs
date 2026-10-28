---
url: https://docs.cloud.google.com/python/docs/observability/
title: Instrumenting Google Cloud Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T01:38:25.529502+00:00
---

# Instrumenting Google Cloud Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/observability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Guides ](https://docs.cloud.google.com/python/docs/setup)



Send feedback 

#  Instrumenting Google Cloud Python client libraries Stay organized with collections  Save and categorize content based on your preferences. 

This guide demonstrates how to configure and use [OpenTelemetry](https://opentelemetry.io/) distributed tracing in Google Cloud Python client libraries.

## Overview

Google Cloud Python client libraries provide built-in OpenTelemetry distributed tracing. This instrumentation offers deep visibility into client operations, RPC invocations, retry behavior, network latency, and service responses without requiring manual monkey-patching.

Key characteristics:

  * **Backend Agnostic** : Emits standard OpenTelemetry spans. You can export traces directly to [Cloud Trace](https://cloud.google.com/trace), an on-premises OpenTelemetry Collector, or third-party observability platforms.
  * **Opt-In** : Distributed tracing is disabled by default to avoid runtime overhead for applications that don't require telemetry.
  * **Context Propagation** : Spans automatically bind to the active OpenTelemetry trace context using Python's built-in `contextvars`, correlating client calls with incoming HTTP/gRPC requests.



## How Tracing Works (Span Hierarchy)

When enabled, Google Cloud Python client libraries emit a hierarchical, two-level span architecture that clearly separates user-facing method execution from underlying wire attempts:
    
    
    [Logical Client Method Span] (Parent: covers full method duration, retries, and backoff)
     │
     ├── [Network Attempt Span #1] (Child: First wire call; e.g. transient 503 UNAVAILABLE)
     └── [Network Attempt Span #2] (Child: Retry wire call; succeeds 200 OK)
    

### 1\. Logical Client Method Spans (Parent)

  * **Scope** : Encapsulates the entire client library method call lifecycle from invocation to completion.
  * **Duration** : Covers all retry attempts, exponential backoff pauses, and timeout policies.
  * **Identity** : Named after the fully-qualified RPC method (for example, `google.cloud.secretmanager.v1.SecretManagerService/GetSecretVersion`).
  * **Attributes** : Captures logical RPC metadata, destination service, and the final high-level outcome.



### 2\. Network Attempt Spans (Child)

  * **Scope** : Created as child spans of the logical method span, representing individual HTTP/REST or gRPC physical network attempts.
  * **Lifecycle** : A new span is generated for each network attempt. If an operation succeeds on the first try, exactly one child span is recorded. If an operation encounters transient errors and retries, each attempt is recorded as an independent child span with its own timing and status.
  * **Attributes** : Captures low-level wire status codes, destination server address, and transport details.



## Prerequisites & Installation

Google Cloud Python client library tracing relies on standard OpenTelemetry Python packages.

### 1\. Install Packages

  * **Client library & gRPC transport instrumentation**:

    * `opentelemetry-api` is installed automatically with `google-api-core` to support logical method spans and `HTTP/REST` (`rest`) transport spans.
    * To also record low-level `gRPC` transport spans, install your client library along with `google-api-core[tracing]` (which installs `opentelemetry-instrumentation-grpc`):
    
    pip install google-cloud-secret-manager "google-api-core[tracing]"
    

  * **OpenTelemetry SDK (for standalone apps and code samples)** :

    * Client libraries don't require `opentelemetry-sdk` if your environment already provides a `TracerProvider`.
    * However, to configure a `TracerProvider` and export spans in your own code (including the samples on this page), install `opentelemetry-sdk`:
    
    pip install opentelemetry-sdk
    


**Note:** The `opentelemetry-instrumentation-grpc` package is required only for low-level gRPC transport spans. Logical client method spans and HTTP/REST (`rest`) transport spans work without it.

For instructions on configuring OpenTelemetry exporters to send spans to Cloud Trace or an OpenTelemetry Collector in production, see [Set up Python with OpenTelemetry](https://docs.cloud.google.com/trace/docs/setup/python-ot) and [Choose an instrumentation approach](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach).

## Enabling Tracing

Distributed tracing can be enabled either globally using an environment variable or programmatically on a per-client basis. Per-client configuration passed using `ClientOptions` takes precedence over environment variable settings.

### Option 1: Global configuration (Environment variables)

To enable tracing across all supported Google Cloud Python client libraries in your environment, set the following environment variable before starting your application:
    
    
    export GOOGLE_SDK_PYTHON_TRACING_ENABLED=true
    

When set to `true`, client libraries automatically detect the globally registered OpenTelemetry `TracerProvider` and emit spans for all client invocations.

### Option 2: Per-client configuration (Code)

For fine-grained control or multi-tenant applications, configure a specific client instance by passing a `tracer_provider` using `ClientOptions`:
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import secretmanager
    
    options = ClientOptions(tracer_provider=my_tracer_provider)
    client = secretmanager.[SecretManagerServiceClient](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html)(client_options=options)
    

## Code Examples

Client libraries can use [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials) to easily authenticate with Google APIs and send requests to those APIs. With Application Default Credentials, you can test your application locally and deploy it without changing the underlying code. For more information, see [ Authenticate for using client libraries](https://docs.cloud.google.com/docs/authentication/client-libraries).

### 1\. Quickstart Example (`SecretManagerServiceClient`)

The following self-contained example demonstrates configuring standard OpenTelemetry, enabling client library tracing using an environment variable, and printing emitted spans directly to the terminal as JSON using `ConsoleSpanExporter`.
    
    
    import os
    
    from google.cloud import secretmanager
    from opentelemetry import trace
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor
    
    
    def get_secret_version_with_tracing(
        project_id: str,
        secret_id: str,
        version_id: str = "latest",
    ) -> secretmanager.SecretVersion:
        """Get a secret version in Secret Manager with OpenTelemetry tracing enabled.
    
        Args:
            project_id: Google Cloud project ID.
            secret_id: ID of the secret.
            version_id: ID of the secret version (defaults to "latest").
    
        Returns:
            The SecretVersion metadata object.
        """
        # NOTE: In standalone scripts or CLI tools, initialize and shut down the
        # TracerProvider within the script workflow. In long-running production
        # applications (e.g., web servers), configure the TracerProvider once at
        # application startup.
        #
        # Initialize the OpenTelemetry TracerProvider with a Console exporter
        provider = TracerProvider()
        provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
        trace.set_tracer_provider(provider)
    
        # Enable Google Cloud client library tracing
        os.environ["GOOGLE_SDK_PYTHON_TRACING_ENABLED"] = "true"
    
        # Instantiate the client (automatically discovers the active TracerProvider)
        client = secretmanager.[SecretManagerServiceClient](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html)()
    
        # Construct the resource name and invoke the RPC
        name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
    
        try:
            print("--- OpenTelemetry Trace Spans (JSON) ---")
            response = client.[get_secret_version](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_get_secret_version)(request={"name": name})
            state_name = response.state.name
            print(
                f"\nAPI Result: Retrieved secret version {response.name} (state: {state_name})"
            )
            return response
        finally:
            # Flush buffered spans before program completion
            provider.shutdown()
    
    
    
    [get_secret_version_trace.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/d831f8ba63b5c16cdfa97783b059547f00555eb8/secretmanager/snippets/get_secret_version_trace.py#L19-L73)

### 2\. Programmatic Configuration (`ClientOptions`)

If you prefer not to use environment variables or need to pass different `TracerProvider` instances to different clients, configure a client programmatically by passing `tracer_provider` using `ClientOptions`:
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import secretmanager
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor
    
    
    def get_secret_version_with_client_options(
        project_id: str,
        secret_id: str,
        version_id: str = "latest",
    ) -> secretmanager.SecretVersion:
        """Get a secret version configuring tracing programmatically via ClientOptions.
    
        Args:
            project_id: Google Cloud project ID.
            secret_id: ID of the secret.
            version_id: ID of the secret version (defaults to "latest").
    
        Returns:
            The SecretVersion metadata object.
        """
        # Initialize an independent TracerProvider (no global registration required)
        provider = TracerProvider()
        provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
    
        # Pass the TracerProvider directly via ClientOptions
        # Tracing is activated specifically for this client instance, even without
        # setting the GOOGLE_SDK_PYTHON_TRACING_ENABLED environment variable.
        options = ClientOptions(tracer_provider=provider)
        client = secretmanager.[SecretManagerServiceClient](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html)(client_options=options)
    
        # Construct resource name and invoke RPC
        name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
    
        try:
            print("--- OpenTelemetry Trace Spans (JSON) ---")
            response = client.[get_secret_version](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_get_secret_version)(request={"name": name})
            state_name = response.state.name
            print(
                f"\nAPI Result: Retrieved secret version {response.name} (state: {state_name})"
            )
            return response
        finally:
            # Flush buffered spans before program completion
            provider.shutdown()
    
    
    
    [get_secret_version_trace_client_options.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/d831f8ba63b5c16cdfa97783b059547f00555eb8/secretmanager/snippets/get_secret_version_trace_client_options.py#L19-L65)

### 3\. Asynchronous Client Example (`SecretManagerServiceAsyncClient`)

The following sample defines an asynchronous coroutine (`async def get_secret_version_with_tracing_async`) using `SecretManagerServiceAsyncClient`. Because this client is asynchronous, ensure you execute it within an active `asyncio` event loop.
    
    
    import asyncio
    import os
    
    from google.cloud import secretmanager
    from opentelemetry import trace
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor
    
    
    async def get_secret_version_with_tracing_async(
        project_id: str,
        secret_id: str,
        version_id: str = "latest",
    ) -> secretmanager.SecretVersion:
        """Get a secret version using SecretManagerServiceAsyncClient with OpenTelemetry tracing.
    
        Args:
            project_id: Google Cloud project ID.
            secret_id: ID of the secret.
            version_id: ID of the secret version (defaults to "latest").
    
        Returns:
            The SecretVersion metadata object.
        """
        # NOTE: In standalone scripts or CLI tools, initialize and shut down the
        # TracerProvider within the script workflow. In long-running production
        # applications (e.g., web servers), configure the TracerProvider once at
        # application startup.
        #
        # Initialize the OpenTelemetry TracerProvider with a Console exporter
        provider = TracerProvider()
        provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
        trace.set_tracer_provider(provider)
    
        # Enable Google Cloud client library tracing
        os.environ["GOOGLE_SDK_PYTHON_TRACING_ENABLED"] = "true"
    
        # Instantiate the async client
        client = secretmanager.[SecretManagerServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceAsyncClient.html)()
    
        # Construct resource name and invoke the async RPC
        name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
    
        try:
            print("--- OpenTelemetry Trace Spans (JSON) ---")
            response = await client.[get_secret_version](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceAsyncClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceAsyncClient_get_secret_version)(request={"name": name})
            state_name = response.state.name
            print(
                f"\nAPI Result: Retrieved secret version {response.name} (state: {state_name})"
            )
            return response
        finally:
            # Flush buffered spans before program completion
            provider.shutdown()
    
    
    
    [get_secret_version_trace_async.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/d831f8ba63b5c16cdfa97783b059547f00555eb8/secretmanager/snippets/get_secret_version_trace_async.py#L19-L74)

**Context Propagation in Asynchronous Code:** OpenTelemetry Python automatically propagates trace context across `await` points and concurrent tasks using Python's built-in `contextvars`. Even when multiple coroutines yield and resume execution concurrently, each client call correctly preserves its active parent span and trace context.

## Semantic Attributes Reference

Spans emitted by Google Cloud Python client libraries adhere to the standard [OpenTelemetry Semantic Conventions for RPC Spans](https://opentelemetry.io/docs/specs/semconv/rpc/rpc-spans/), recording standard metadata for the transport protocol, RPC method identity, destination server address, response status codes, and error details. You can use these attributes to filter, aggregate, and create alert policies in your observability or Cloud Trace dashboard.

## Security & Sensitive Data

Google Cloud Python client library instrumentation is designed following strict security and privacy standards:

  * **Payload Protection** : Client libraries **never** record request or response payload data (such as file contents, secret values, or database query results) on trace spans.
  * **Identifier Visibility** : Resource names (such as project IDs, dataset IDs, and secret names) appear in method parameters and URL endpoint attributes. If resource identifiers contain sensitive business information, ensure your trace storage complies with your internal compliance policies.
  * **Third-Party Exporters** : When exporting traces to third-party observability services or SaaS vendors, review your organization's data protection agreements and configure exporter attribute filtering if necessary.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

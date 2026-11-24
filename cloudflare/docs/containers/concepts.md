---
url: https://developers.cloudflare.com/containers/concepts/
title: Container Fundamentals \u00b7 Cloudflare Containers docs
method: scrapling+scrapegraph
fetched_at: 2026-11-24T12:11:03.720993+00:00
---

# Container Fundamentals · Cloudflare Containers docs

> Source: https://developers.cloudflare.com/containers/concepts/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Containers](https://developers.cloudflare.com/containers/)
  3. /Concepts



# Container Fundamentals

Last updated Nov 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewThe Container runtimeHow requests reach a ContainerContainer lifecycleSizingPlacementStorage and connectivityStart buildingRelated resources

A Cloudflare Container runs your container image in a full Linux environment on Cloudflare's network, alongside a Worker. The Worker handles incoming HTTP requests and can handle raw TCP connections in public beta. The Container provides the runtime, binaries, and languages your application needs. Together, they let you run Linux workloads without managing the underlying infrastructure.

## The Container runtime

_Run Linux workloads alongside your Worker._

A Worker runs code in an isolated JavaScript environment. A Container runs your image in a full Linux environment, so you can bring custom runtimes and binaries when your application needs them. Each Container instance runs inside its own virtual machine, which isolates it from other workloads. The Worker receives inbound HTTP requests and routes them to the Container, so the Container is not exposed directly to end users.

PlayReset

A request reaches the Worker, which routes it to a Container running inside its own virtual machine. The Worker remains in front of the Container while the Container serves the request.

For more information, refer to [Lifecycle of a Container](https://developers.cloudflare.com/containers/concepts/architecture/).

For TCP applications, Spectrum can invoke a Worker's [`connect()` handler](https://developers.cloudflare.com/workers/runtime-apis/handlers/connect/). The Worker can then forward the raw socket to a process in the Container. This supports protocols such as bidirectional gRPC. Refer to [Bidirectional gRPC with Workers and Containers](https://developers.cloudflare.com/containers/examples/bidirectional-grpc/).

## How requests reach a Container

_Route every request through your Worker._

The request begins at your Worker, which uses the [Durable Object](https://developers.cloudflare.com/durable-objects/) layer to identify and reach a Container. This layer coordinates routing and lifecycle behavior, allowing the Container to continue serving requests while it runs. A Container can start when it receives its first request, so the first request may take longer to complete.

Choose an instance identity to send a request

ABReset

A request flows from the client to the Worker and then to a Container. The Worker and Durable Object layer coordinate routing and lifecycle behavior before the Container serves the request. If the Container is not already running, it starts as part of that process.

For more information, refer to [Lifecycle of a Container](https://developers.cloudflare.com/containers/concepts/architecture/).

## Container lifecycle

_Start on demand, then stop when idle._

A Container starts when your application needs it, so the first request can take longer while its environment starts. Once running, it serves requests until it becomes inactive; after an inactivity period, it can stop and release its running resources. When another request arrives, the Container can start again.

PlayReset

The lifecycle begins with a stopped Container and a request that starts it. The Container then serves requests, becomes inactive, and stops again until another request arrives.

For more information, refer to [Lifecycle of a Container](https://developers.cloudflare.com/containers/concepts/architecture/) and [Pricing](https://developers.cloudflare.com/containers/platform/pricing/).

## Sizing

_Choose resources for your workload._

Container instance sizes let you match resources to your workload. You can choose a predefined size or configure a custom one, with larger sizes providing more CPU, memory, and disk. When choosing a size, consider the resources your application needs and refer to [Limits and instance types](https://developers.cloudflare.com/containers/platform/limits/) for the available options and constraints.

For more information, refer to [Pricing](https://developers.cloudflare.com/containers/platform/pricing/).

## Placement

_Start instances in eligible locations._

When a Durable Object starts a Container, Cloudflare selects a suitable location based on request routing, available capacity, and image availability. The Container and its Durable Object may run in different locations.

With the `durable_object` scheduling policy, the Durable Object's jurisdiction determines eligible Container locations. Your application can start multiple Container instances when it needs more capacity.

For more information, refer to [Placement](https://developers.cloudflare.com/containers/concepts/placement/).

## Storage and connectivity

_Keep durable data outside the local disk._

Treat a Container's local disk as temporary working space, because data on it can be lost when the Container stops or restarts. For data that must persist, use Durable Object storage or Cloudflare storage bindings such as KV, R2, and D1. Configured outbound handlers let the Container access these bindings and external services without requiring an SDK inside the Container.

ResetPlay

Idle — click Next to step through the request

A Container can reach Cloudflare storage and external services through configured connections. Its local disk is temporary, while data in durable storage persists beyond the Container's lifecycle.

For more information, refer to [Connect to Workers and bindings](https://developers.cloudflare.com/containers/configuration/workers-connections/) and [Outbound traffic](https://developers.cloudflare.com/containers/configuration/outbound-traffic/).

## Start building

When you are ready to build, start with a deployed Container or explore the available guides.

### [Get started](https://developers.cloudflare.com/containers/get-started/)

Deploy your first container.

### [Guides](https://developers.cloudflare.com/containers/guides/)

Task-focused walkthroughs for common container workloads.

### [Bidirectional gRPC](https://developers.cloudflare.com/containers/examples/bidirectional-grpc/)

Route a gRPC stream through Spectrum and Workers to a Container.

## Related resources

  * [Lifecycle of a Container](https://developers.cloudflare.com/containers/concepts/architecture/): the deep dive on deployment, routing, and shutdown.
  * [Placement](https://developers.cloudflare.com/containers/concepts/placement/): where instances run and how Durable Object jurisdiction affects placement.
  * [Connect to Workers and bindings](https://developers.cloudflare.com/containers/configuration/workers-connections/): reaching Cloudflare resources from a container.
  * [Bidirectional gRPC with Workers and Containers](https://developers.cloudflare.com/containers/examples/bidirectional-grpc/): routing raw TCP streams to a containerized gRPC server.
  * [Limits and instance types](https://developers.cloudflare.com/containers/platform/limits/) and [Pricing](https://developers.cloudflare.com/containers/platform/pricing/): sizes, account limits, and billing.
  * [Rollouts](https://developers.cloudflare.com/containers/configuration/rollouts/): how new versions roll out across instances.



[PreviousGet started](https://developers.cloudflare.com/containers/get-started/)[NextLifecycle of a Container](https://developers.cloudflare.com/containers/concepts/architecture/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/containers/concepts/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://docs.fish.audio/developer-guide/self-hosting/introduction/
title: Introduction - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-10-30T14:25:07.714462+00:00
---

# Introduction - Fish Audio

> Source: https://docs.fish.audio/developer-guide/self-hosting/introduction/

## On this page

Back to top

  * Why self-host
  * Platforms
  * Billing
  * Supported APIs
  * Getting access
  * Next steps



Self-Hosting

# Introduction

Copy pageCopy page

Run the Fish Audio Enterprise speech stack inside your own infrastructure

Copy pageCopy page

Fish Audio Enterprise can be deployed into infrastructure you control: your own cloud account, an on-premise data center, or a network with no internet access at all. Fish Audio delivers each model’s container images and Helm chart through a private registry; you own the cluster, the network boundary, and the data. The self-hosted stack runs the same speech engine as the hosted API, so requests, audio formats, and voice behavior match what you already build against.

## 

​

Why self-host

Reason| What it gives you  
---|---  
Colocation| Run inference in the same region, VPC, or rack as your application and remove public-internet round trips from time-to-first-audio.  
Single-tenant isolation| Dedicated GPUs and queues. Capacity is not shared with other tenants, and you decide when the deployment is upgraded.  
Security posture| Voice traffic never leaves your network. The offline modes need no outbound access at runtime and run on disconnected networks.  
Data sovereignty| Input text, generated audio, and reference voices stay inside your boundary and under your own retention policy.  
  
## 

​

Platforms

Each model ships on two platforms. Your agreement decides which ones your team gets, and in which modes; **Developer → Self Host** shows them.

| Helm (Kubernetes)| All-in-One (Docker)  
---|---|---  
What it is| The model’s chart, installed on your cluster| One container on a single machine  
Best for| Production clusters and elastic capacity| Evaluation, fixed-size appliances, strict air gaps  
Scaling| Replicas across GPUs and nodes, with optional autoscaling| None: one worker and one vocoder  
Metrics| Prometheus metrics from the speech services| API metrics only, at `/metrics`  
Timestamps| Optional, where available| Not included  
Guide| [Kubernetes deployment](https://docs.fish.audio/developer-guide/self-hosting/kubernetes)| [All-in-One container](https://docs.fish.audio/developer-guide/self-hosting/all-in-one)  
  
The GPUs each model needs are on [Models](https://docs.fish.audio/developer-guide/self-hosting/models). On either platform, ingress, DNS, TLS, external load balancing, and network allowlists are yours to choose and configure.

## 

​

Billing

Both platforms come in either billing mode:

| Online| Offline  
---|---|---  
Usage| Authorized and billed per request against Fish Audio| Recorded in a signed ledger on your side and reconciled with Fish Audio  
Network needed at runtime| Outbound HTTPS to Fish Audio| None, so it can run air-gapped — see [Air-gapped deployments](https://docs.fish.audio/developer-guide/self-hosting/air-gapped)  
Request token| A [Fish Audio API key](https://docs.fish.audio/developer-guide/getting-started/api-key) with credit| Any stable, non-empty token, one per tenant, recorded as the billing identity and not checked: control access in front of the deployment  
  
## 

​

Supported APIs

A self-hosted deployment serves:

  * **Text to speech** over [HTTP](https://docs.fish.audio/api-reference/endpoint/openapi-v1/text-to-speech) and [WebSocket streaming](https://docs.fish.audio/api-reference/endpoint/websocket/tts-live).
  * **Reference voices.** A request that names a voice by `reference_id` uses that voice’s archive on the deployment. Your team’s fish.audio voices and Fish Audio’s official voices get there by hand, or over HTTPS through the optional voice sync; the hosted voice library is never read at request time.
  * **[Word and segment timestamps](https://docs.fish.audio/api-reference/endpoint/openapi-v1/text-to-speech-stream-with-timestamps)** , optional. They need one more GPU; contact Fish Audio to enable them.

Other Fish Audio products are hosted-only unless your agreement says otherwise.

## 

​

Getting access

1

Agree the deployment scope

Self-hosting is enabled per team under an enterprise agreement. Reach out through [fish.audio/enterprise](https://fish.audio/enterprise) with your GPU target, expected concurrency, and whether you need air-gapped operation.

2

Get your team enabled

Once your agreement is in place, Fish Audio grants your team the models and modes it is entitled to, and the charts and images that go with them.

3

Create a deploy token

Sign in to fish.audio and open **Developer → Self Host** to see the models, platforms, and modes your team is granted and to create the token that authenticates against the registry. See [Registry & license](https://docs.fish.audio/developer-guide/self-hosting/registry-access).

## 

​

Next steps

## Models

The models you can self-host, and where their requirements differ.

## Requirements

GPU, CPU, memory, storage, and platform baselines.

## Registry & license

Create a deploy token, sign in, and download the license bundle.

## Kubernetes deployment

What the Helm install involves and what to arrange first.

## All-in-One container

Run the whole stack from a single `docker run`.

## Air-gapped deployments

Mirror artifacts, account for usage offline, and prove zero egress.

## Operations

Monitoring signals, scaling, backups, and upgrades.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/fishaudio/docs/edit/main/developer-guide/self-hosting/introduction.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/developer-guide/self-hosting/introduction)

[Realtime protocol](https://docs.fish.audio/developer-guide/compat/realtime-protocol)[Models](https://docs.fish.audio/developer-guide/self-hosting/models)

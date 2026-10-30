---
url: https://docs.fish.audio/developer-guide/self-hosting/all-in-one/
title: All-in-One container - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-10-30T14:25:07.932735+00:00
---

# All-in-One container - Fish Audio

> Source: https://docs.fish.audio/developer-guide/self-hosting/all-in-one/

## On this page

Back to top

  * What it cannot do
  * What running it involves
  * Tokens and tenancy
  * Capacity
  * Next steps



Self-Hosting

# All-in-One container

Copy pageCopy page

Run a model’s whole speech stack in one Docker container on a single machine

Copy pageCopy page

The All-in-One image packages the whole speech stack into one container and runs as a turnkey single-node appliance, no Kubernetes. The model weights are baked into the image, except in the external-weights modes, which mount them from your own storage at run time. Each image is built for one [billing mode](https://docs.fish.audio/developer-guide/self-hosting/introduction#billing), online or offline; the container logs which at startup.

This page covers what the appliance is and what to plan for. The commands, tuning options, and troubleshooting are in the **All-in-One guide** , which you download from **Developer → Self Host** with the image version you run.

## 

​

What it cannot do

The appliance runs one inference worker and one vocoder, on the cards its model takes — see [Models](https://docs.fish.audio/developer-guide/self-hosting/models). It does not autoscale or add workers on more GPUs or nodes, and it does not include timestamp alignment, so it returns no word or segment timings. For elastic or higher-throughput deployments, use the [Kubernetes chart](https://docs.fish.audio/developer-guide/self-hosting/kubernetes), which scales replicas across all GPUs and nodes.

## 

​

What running it involves

One `docker run` on a host that meets the [requirements](https://docs.fish.audio/developer-guide/self-hosting/requirements). It needs:

  * **The GPUs its model takes** — usually two; a Single-GPU mode, where the model offers one, shares one card at lower throughput.
  * **One exposed port** for the API.
  * **One persistent volume.** Caches, reference voice archives, and — in the offline mode — the [usage ledger](https://docs.fish.audio/developer-guide/self-hosting/air-gapped#offline-usage-accounting) all live there; the model weights do not.
  * **The license bundle** from **Developer → Self Host** , mounted read-only. See [The license](https://docs.fish.audio/developer-guide/self-hosting/registry-access#the-license).

Everything inside the container runs as a non-root user, so a reused volume or a host bind mount has to be writable by it. **Plan for a slow first start.** The worker and the vocoder prepare for your GPU type before either serves, and the health endpoint verifies the speech backend end to end rather than reporting immediate liveness. Every start takes minutes; the first can take much longer. To upgrade, pull or load the new version’s image and recreate the container against the same volume.

## 

​

Tokens and tenancy

Offline, any non-empty bearer token is accepted and recorded as the billing identity: give each tenant a stable token of its own, and control access in front of the appliance. Online, each request must carry a [Fish Audio API key](https://docs.fish.audio/developer-guide/getting-started/api-key) with credit, not the deploy token. It is authorized against Fish Audio with no local fallback, so treat outbound reachability as a production dependency.

## 

​

Capacity

The worker admits a bounded number of requests at once; beyond that, requests queue and time-to-first-audio climbs. Your deployment guide gives the cap for your model; validate latency and error rate before changing it.

## 

​

Next steps

  * [Requirements](https://docs.fish.audio/developer-guide/self-hosting/requirements): host baseline
  * [Registry & license](https://docs.fish.audio/developer-guide/self-hosting/registry-access): how your team gets the image
  * [Air-gapped deployments](https://docs.fish.audio/developer-guide/self-hosting/air-gapped): moving the image to a disconnected host



Was this page helpful?

YesNo

[Suggest edits](https://github.com/fishaudio/docs/edit/main/developer-guide/self-hosting/all-in-one.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/developer-guide/self-hosting/all-in-one)

[Kubernetes deployment](https://docs.fish.audio/developer-guide/self-hosting/kubernetes)[Air-gapped deployments](https://docs.fish.audio/developer-guide/self-hosting/air-gapped)

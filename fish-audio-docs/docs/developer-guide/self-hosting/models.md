---
url: https://docs.fish.audio/developer-guide/self-hosting/models/
title: Models - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-10-30T14:25:07.195846+00:00
---

# Models - Fish Audio

> Source: https://docs.fish.audio/developer-guide/self-hosting/models/

## On this page

Back to top

  * At a glance
  * S2.1 Pro
  * Drama 3



Self-Hosting

# Models

Copy pageCopy page

The models you can self-host, and where their requirements differ

Copy pageCopy page

Each model is delivered on its own: its own Helm chart, All-in-One images, versions, and deployment guide. Your agreement grants each model separately, and **Developer → Self Host** lists the ones your team can install. The rest of this section applies to every model; this page covers where they differ.

## 

​

At a glance

Model| Request header| GPU types| GPUs per deployment  
---|---|---|---  
S2.1 Pro| `model: s2.1-pro`| H100, H200, or B300| Two; one in the All-in-One’s Single-GPU mode, at lower throughput  
Drama 3| `model: drama-3`| H200 or B300 recommended| At least two or three, depending on the GPU  
  
## 

​

S2.1 Pro

  * **The first start compiles for your GPU.** The result is cached on shared storage on Helm, and on the volume on the All-in-One, so later starts are quicker. Moving to a different GPU type compiles once more.
  * **Timestamps offline.** A Helm install without internet access copies the timestamp model onto shared storage before turning timestamps on; the deployment runbook has the step.



## 

​

Drama 3

[Drama 3](https://docs.fish.audio/features/text-to-speech/drama-3) is a much larger model than S2.1 Pro and needs more resources, GPUs above all; your deployment guide has the sizing. For a GPU other than H200 or B300, check with Fish Audio before you plan around it.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/fishaudio/docs/edit/main/developer-guide/self-hosting/models.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/developer-guide/self-hosting/models)

[Introduction](https://docs.fish.audio/developer-guide/self-hosting/introduction)[Requirements](https://docs.fish.audio/developer-guide/self-hosting/requirements)

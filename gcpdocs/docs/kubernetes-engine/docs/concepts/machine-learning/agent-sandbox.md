---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox/
title: About Agent Sandbox on GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T23:12:22.950508+00:00
---

# About Agent Sandbox on GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  About Agent Sandbox on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Agent Sandbox on Google Kubernetes Engine (GKE) helps you run isolated agent workloads in dedicated Kubernetes Pods. Isolation is important when AI agents run untrusted, LLM-generated code. For most agent workloads, you should use [Agent Substrate on GKE](https://docs.cloud.google.com/kubernetes-engine/ai-ml/about-agent-substrate) instead, because it can run more agents on the same nodes. Use Agent Sandbox on GKE when each agent needs a dedicated Pod, GPUs or TPUs, a full Kubernetes PodSpec, or a GKE Autopilot cluster. To compare Agent Sandbox on GKE with Agent Substrate on GKE and choose an architecture for your AI agent workloads, see [Plan an architecture for AI agent workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-workloads).

[Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox/) is an open source project under Kubernetes SIG Apps. To use Agent Sandbox on GKE, you install the Agent Sandbox controller on your cluster. You're responsible for upgrading the controller. For instructions, see [Install Agent Sandbox on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox).

This document provides a conceptual overview of Agent Sandbox on GKE.

## Why use Agent Sandbox on GKE

Agent Sandbox on GKE gives each agent a dedicated, kernel-isolated Pod that you manage with standard Kubernetes APIs. Key benefits include the following:

  * **Kernel-level isolation** : Isolates untrusted, LLM-generated code from the node's kernel by using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) with gVisor or microVMs. Agent Sandbox on GKE also works with self-managed open source [Kata Containers](https://katacontainers.io/) that you install on your nodes instead of GKE Sandbox. For a tutorial about using open source Kata Containers with Agent Sandbox on GKE, see [Enabling Kata Containers on GKE](https://github.com/kubernetes-sigs/agent-sandbox/tree/v1.0.6/examples/kata-gke-sandbox).

**Note:** Kata Containers isn't a Google Cloud product. If you install and use this software, then you're responsible for management and troubleshooting. Google's support and SLAs don't apply to Kata Containers.
  * **Sub-second provisioning** : Provides pre-warmed Pods for your agents, typically in less than one second, instead of waiting for standard Kubernetes Pod scheduling and startup.

  * **Cloud-native extensibility** : Leverages the power of the Kubernetes paradigm and the managed infrastructure of GKE.




By providing a declarative, standardized API, Agent Sandbox on GKE offers a single-container experience that provides isolation and persistence characteristics similar to a virtual machine (VM), built entirely on Kubernetes primitives.

## Common use cases for Agent Sandbox on GKE

Use Agent Sandbox on GKE for workloads that require isolation, persistence, and a stable identity. Example use cases include the following:

  * **AI agent runtimes** : Run untrusted code in a Pod that uses [gVisor](https://gvisor.dev/) or [microVMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#sandbox-technologies) to isolate the code from the node's kernel.
  * **Development environments** : Provide developers with persistent, isolated cloud-based coding environments.
  * **Notebooks and research tools** : Host single-container sessions for interactive tools like Jupyter Notebooks.
  * **Stateful single-Pod services** : Run applications that need a stable identity and storage without the complexity of a StatefulSet.
  * **Programmatic environment management** : Use provided client library SDKs, such as the [Agent Sandbox Python SDK](https://github.com/kubernetes-sigs/agent-sandbox/tree/v1.0.6/clients/python/agentic-sandbox-client), to request and manage Sandbox resources directly from your application logic without managing Kubernetes YAML.



## How Agent Sandbox on GKE works

Agent Sandbox on GKE uses a custom controller and several Kubernetes Custom Resource Definitions (CRDs) to manage the lifecycle of Sandbox resources.

### Core architecture

  * **[Sandbox custom resource](https://github.com/kubernetes-sigs/agent-sandbox/blob/v1.0.6/docs/api.md#sandbox)** : the primary resource that represents a single, stateful Pod. The resource manages stable hostnames, network identity, and persistent storage. To suspend an idle agent, set the `spec.operatingMode` field of its Sandbox resource to `Suspended`. The controller deletes the Pod but keeps the Sandbox resource and its persistent volumes. In-memory data and container file system changes are lost unless you take a [Pod snapshot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox-pod-snapshots) first. To resume the agent, set the field back to `Running`. Agent Sandbox on GKE doesn't detect idle agents; your application decides when to suspend them.
  * **Sandbox Router** : a component that provides a stable endpoint and tunnels traffic to the Pods that run your agents, abstracting the underlying networking complexity.
  * **Integration with Pod snapshots** : Agent Sandbox on GKE integrates with the [GKE Pod snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox-pod-snapshots) feature to suspend and resume workloads by saving and restoring the full state of a container.



### Claim model

The **claim model** is a key feature that separates the user's request for an environment from the specific implementation details, such as where and how the workload is provisioned. Unlike a standard Kubernetes StatefulSet, the claim model lets you request a Sandbox resource without needing to manage the underlying Pod or storage configurations directly.

The claim model uses the [SandboxClaim](https://github.com/kubernetes-sigs/agent-sandbox/blob/v1.0.6/docs/api.md#sandboxclaim), [SandboxWarmPool](https://github.com/kubernetes-sigs/agent-sandbox/blob/v1.0.6/docs/api.md#sandboxwarmpool), and [SandboxTemplate](https://github.com/kubernetes-sigs/agent-sandbox/blob/v1.0.6/docs/api.md#sandboxtemplate) custom resources and works as follows:

  1. Users or applications request a Sandbox resource by creating a SandboxClaim resource that references a SandboxWarmPool resource. The warm pool references the SandboxTemplate resource that defines the Pod configuration.
  2. The controller assigns a ready Sandbox resource (and its running Pod) from the warm pool to the claim. If no Sandbox resource in the pool is ready, the controller creates a new Sandbox resource for the claim from the template.



### Warm pools

The **warm pool** feature is designed to minimize startup latency for interactive AI agent scenarios. By using a warm pool, Agent Sandbox on GKE can provide execution environments in less than one second. The feature uses the [SandboxWarmPool](https://github.com/kubernetes-sigs/agent-sandbox/blob/v1.0.6/docs/api.md#sandboxwarmpool) custom resource and works as follows:

  1. A SandboxWarmPool resource maintains a pool of pre-warmed Sandbox resources with Pods in a ready state.
  2. When a SandboxClaim resource is created, the controller assigns a ready Sandbox resource and its running Pod from the pool instead of waiting for a new Pod to pull images and start.
  3. When combined with Pod snapshots, warm pools can restore Pods from a pre-configured state instead of starting them from scratch.



### Network isolation

Agent Sandbox on GKE implements a default deny network policy for the Pods that the controller creates from a SandboxTemplate resource. For each SandboxTemplate resource, the controller creates a NetworkPolicy resource that helps prevent untrusted code inside the Pod from accessing unauthorized internal networks or the GKE control plane. You can define specific network restrictions and allowed egress or ingress rules within your SandboxTemplate resource to control network access for agent workloads.

The controller doesn't create a NetworkPolicy resource for a Sandbox resource that you create directly. To restrict network access for the Pods of these Sandbox resources, create your own NetworkPolicy resource.

### Programmatic access with SDKs

AI engineers can consume Agent Sandbox on GKE resources programmatically by using the provided client libraries. For example, the [Python SDK](https://github.com/kubernetes-sigs/agent-sandbox/tree/v1.0.6/clients/python/agentic-sandbox-client) provides a high-level interface that creates the underlying SandboxClaim resource for you. The claim references a SandboxWarmPool resource that you create. This interface lets you create and interact with isolated environments directly from your Python-based agent frameworks like LangChain or the Vertex AI Agentic SDK.

## Limitations and requirements

Agent Sandbox on GKE has the following limitations and requirements:

  * **Cluster version** : Agent Sandbox on GKE runs on any supported GKE version. To use [Pod snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox-pod-snapshots), your cluster must run GKE version 1.35.3-gke.1234000 or later.
  * **Infrastructure requirements** : Requires the Agent Sandbox controller to be [installed and configured](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox) on the cluster. Agent Sandbox on GKE doesn't require a specific machine type. For example, the installation guide uses `e2-standard-2` nodes. However, [Pod snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox-pod-snapshots) don't support E2 machine types, so if you plan to use Pod snapshots, use another machine series, such as N2.
  * **Isolation runtimes** : Agent Sandbox on GKE supports [gVisor](https://gvisor.dev/) and [microVMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#sandbox-technologies) as isolation runtimes. [Pod snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox-pod-snapshots) require gVisor and don't work with microVMs. If you don't specify a GKE Sandbox runtime (gVisor or microVMs), your Pods run without kernel isolation, so don't use them to run untrusted code.
  * **Hardware accelerators** : GPUs and TPUs work only with the gVisor runtime on supported [GPU](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#gpus) models and [TPU](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#tpus) versions, and aren't supported with microVMs. In addition, [Pod snapshots don't support TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/pod-snapshots#limitations).
  * **Underlying features availability** : Some underlying features, such as [GKE Pod snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/pod-snapshots), might be in Preview or have specific regional availability.



## What's next

  * [Learn how to install Agent Sandbox on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox).
  * Learn more about [isolating AI code execution with Agent Sandbox on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox).
  * To learn how to use Pod snapshots with Agent Sandbox on GKE, see [Save and restore Agent Sandbox on GKE environments with Pod snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox-pod-snapshots).
  * Learn about actor-based agent orchestration in [About Agent Substrate on GKE](https://docs.cloud.google.com/kubernetes-engine/ai-ml/about-agent-substrate).
  * Learn how to use open source [Kata Containers with Agent Sandbox on GKE](https://github.com/kubernetes-sigs/agent-sandbox/tree/v1.0.6/examples/kata-gke-sandbox). Kata Containers isn't a Google Cloud product. If you install and use this software, then you're responsible for management and troubleshooting. Google's support and SLAs don't apply to Kata Containers.
  * For the underlying open-source implementation, see the [Agent Sandbox GitHub project](https://github.com/kubernetes-sigs/agent-sandbox/).
  * For example runtimes and YAML configurations for scenarios such as code execution or computer use, see the [Agent Sandbox examples](https://github.com/kubernetes-sigs/agent-sandbox/tree/v1.0.6/examples).
  * To interact with Sandbox resources programmatically, see the [Agent Sandbox Python SDK README](https://github.com/kubernetes-sigs/agent-sandbox/blob/v1.0.6/clients/python/agentic-sandbox-client/README.md) on GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 

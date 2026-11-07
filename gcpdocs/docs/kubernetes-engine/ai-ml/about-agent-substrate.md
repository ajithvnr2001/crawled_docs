---
url: https://docs.cloud.google.com/kubernetes-engine/ai-ml/about-agent-substrate/
title: About Agent Substrate on GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-07T05:45:32.714507+00:00
---

# About Agent Substrate on GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/ai-ml/about-agent-substrate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  About Agent Substrate on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Agent Substrate on GKE runs agentic workloads at scale on Kubernetes clusters. It addresses a common resource inefficiency: interactive agents (such as personal assistants and coding agents) often spend most of their time waiting for user input or external triggers. Keeping these inactive agents continuously running uses CPU and memory that could otherwise be allocated to active workloads.

Agent Substrate on GKE solves this problem by letting your application suspend idle agents. When your application suspends an agent, the system takes a snapshot of the agent's active memory (RAM) and local files. When the suspended agent needs to act again, the system restores the agent's state onto an available sandbox in under a second.

Agent Substrate on GKE builds on the capabilities of [Agent Sandbox on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox), and improves on Agent Sandbox on GKE by bypassing the bottlenecks of the standard Kubernetes control plane. As a result, Agent Substrate on GKE runs more concurrent agents per machine and starts agents faster than Agent Sandbox on GKE does. To compare Agent Substrate on GKE with Agent Sandbox on GKE and choose an architecture for your AI agent workloads, see [Plan an architecture for AI agent workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-workloads).

Standard Kubernetes deployments (including Agent Sandbox on GKE) associate each agent workload with a dedicated Pod. Although Kubernetes is highly scalable, it's constrained by the scheduling throughput and startup latency of Pods. In addition, Kubernetes doesn't support hibernating Pods, and keeping millions of idle agents in a cluster would exhaust Pod limits and control plane memory. To avoid paying for idle compute, you have to shut down the Pods and manage agent state in external storage. Agent Substrate on GKE solves these scaling constraints by decoupling agent state from underlying Pods: it stores millions of suspended agent snapshots in storage and restores them on demand onto a shared pool of warm Workers.

Agent Substrate on GKE is an open source system that you deploy directly onto your own GKE Standard clusters. Although the core project is developed in the open source [Agent Substrate repository](https://github.com/agent-substrate/substrate), Google provides GKE-optimized deployment tooling and scripts in the [substrate-gke repository](https://github.com/ai-on-gke/substrate-gke), for eligible Google Cloud customers.

## Benefits of Agent Substrate on GKE

You can use Agent Substrate on GKE to achieve the following goals:

  * **Run untrusted code safely** : Agent Substrate on GKE enforces kernel and network isolation so that you can execute AI-generated code without risking your broader infrastructure.
  * **Build long-running, stateful agents** : an agent's working memory and files are preserved across sessions. The agent resumes from the exact point it paused.
  * **Respond to requests in real time** : when a new request triggers a suspended agent, the system restores the agent's state in a fraction of a second.
  * **Reduce compute costs** : you can run more agents on fewer machines by sharing a pool of Worker sandboxes across all your agents. Because idle agents are suspended and not using CPU and memory, you pay for compute only when agents are actively processing tasks.



## Use cases

Agent Substrate on GKE is designed to run agents at any scale, from tens to millions of concurrent agents. Here are three example workloads:

  * **Productivity agents** : long-term background assistants that maintain context over weeks. Because these assistants spend the majority of time waiting for triggers, suspending the workloads when not in use reduces compute costs.
  * **Ephemeral sandboxes** : on-demand, isolated environments for executing untrusted LLM-generated code, running tool calls, or analyzing data. Because sandboxes restore in under a second, the system can provide disposable environments for short-lived tasks and release resources when execution finishes.
  * **Coding agents** : AI assistants that hold real-time conversations with developers to write, build, and test code. The agent runs terminal commands and modifies files inside a sandbox. When the agent is idle, your application suspends it until the developer sends another prompt.



## How Agent Substrate on GKE works

Agent Substrate on GKE is built on Kubernetes, but you don't need to understand Kubernetes to use it. The core concepts of Agent Substrate on GKE are the following:

  * **Actor** : a single running instance of an agent.
  * **ActorTemplate** : a configuration blueprint (defining container images, environment variables, and compute resources) that's used to instantiate Actors.
  * **Worker** : a sandbox where an active Actor runs.
  * **WorkerPool** : a group of pre-started, idle Workers that are kept ready to receive an Actor.



Because an Actor isn't tied to a specific Worker, the system can reuse the compute that an Actor frees when your application suspends it. This architecture lets the system run millions of agents on a limited number of machines.

A typical agent lifecycle follows these steps:

  1. **Routing** : each incoming API request from your application specifies its target Actor. For example, when a user types a new prompt into a chat interface, your application sends a request directed at the specific Actor managing the user's session.
  2. **Resuming** : if the request is for a suspended Actor, the system claims a warm Worker from the WorkerPool and restores the Actor's snapshot onto that Worker.
  3. **Executing** : the system routes the request to this newly active Worker, and the Actor processes the task.
  4. **Suspending** : when your application suspends an idle Actor, the system takes a fresh snapshot of the Actor's memory and files, saves the snapshot to storage, and releases the empty Worker back to the pool.



## Workload isolation and GKE Sandbox

Agent Substrate on GKE uses [gVisor](https://gvisor.dev/) or [Cloud Hypervisor](https://www.cloudhypervisor.org/) to run each workload in a sandbox that isolates the application code from the host kernel. The Agent Substrate on GKE installation includes its own gVisor runtime for Workers. Don't enable [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) on the node pools where Agent Substrate on GKE runs, because Agent Substrate on GKE can't run on those nodes. You can still use GKE Sandbox for other workloads, including Agent Sandbox on GKE.

## Limitations and requirements

Agent Substrate on GKE has the following limitations and requirements:

  * **Cluster mode, version, and release channel** : Agent Substrate on GKE supports GKE Standard clusters whose control plane and node pools run version 1.37 or later. Autopilot clusters and versions earlier than 1.37 aren't supported. On version 1.37 and later, GKE serves the `podcertificaterequests` and `clustertrustbundles` Kubernetes APIs and lets nodes mount Pod certificates and trust bundles into Pods, so you don't need to turn on the beta versions of these APIs yourself. However, the installer turns on the beta versions in every cluster that it creates or configures. Because the Extended release channel [doesn't support explicitly enabled beta APIs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#limitations-for-extended), you can't use the installer with clusters that are enrolled in the Extended release channel.
  * **Workload Identity Federation for GKE** : GKE clusters must have [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) enabled. Agent Substrate on GKE uses Workload Identity Federation for GKE to authenticate to Google Cloud APIs, such as Cloud Storage for saving agent snapshots. To save and restore snapshots, the system uses a dedicated service account named `ate-snapshot-transfer`. The credentials for each save or restore operation can access only the snapshots of one Actor. As a result, you don't need to grant your GKE nodes access to the snapshot bucket. The installer creates the `ate-snapshot-transfer` service account and grants it access to the snapshot bucket. If you set up permissions yourself instead, grant the following IAM roles:

    * On the snapshot bucket, grant the `ate-snapshot-transfer` service account and the `ate-api-server` Kubernetes service account the Storage Object Admin (`roles/storage.objectAdmin`) and Storage Bucket Viewer (`roles/storage.bucketViewer`) roles.
    * On the `ate-snapshot-transfer` service account, grant the `ate-api-server` Kubernetes service account the Service Account Token Creator role (`roles/iam.serviceAccountTokenCreator`). The `ate-api-server` service account impersonates the `ate-snapshot-transfer` service account to issue the credentials for each Actor.
    * If you use the microVM runtime, grant the `atelet` Kubernetes service account the Storage Object Viewer role (`roles/storage.objectViewer`) on the asset bucket.

For the full list of bindings and the equivalent `gcloud` commands, see [What `create iam` actually grants](https://github.com/ai-on-gke/substrate-gke/blob/main/tools/setup-gcp/README.md#what-create-iam-actually-grants) in the `setup-gcp` README.

  * **VM families** :

    * **Mixed CPU architectures** : Agent Substrate on GKE doesn't support general-purpose machine series that run on mixed CPU architectures (such as E2 machine types) because of a known issue in gVisor.
    * **Uniform VM types per Actor template** : all the Actors that you create from one `ActorTemplate` must run on the same VM type. An `ActorTemplate` isn't a Kubernetes resource and doesn't have a node selector. Instead, the `workerSelector` field of the `ActorTemplate` selects `WorkerPool` resources by their labels. Each `WorkerPool` can select the nodes for its Workers by using its `spec.template.nodeSelector` field. For example, if your cluster has node pools that use C4 VMs and N2 VMs, configure each `WorkerPool` to select nodes of only one VM type. Then, set the `workerSelector` field of the `ActorTemplate` to match only the `WorkerPool` resources that use C4 VMs.
    * **Nested virtualization or bare metal for microVM runtimes** : the microVM runtime runs each sandbox in its own virtual machine, so Workers that use this runtime need nodes that can run virtual machines. These nodes must use the x86 CPU architecture, not Arm. When the installer creates a cluster, the node pool that it creates has [nested virtualization](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nested-virtualization) enabled. If you install Agent Substrate on GKE in an existing cluster or add your own node pools for microVM Workers, use a node pool that has nested virtualization enabled or that uses an x86 bare-metal machine type. You can enable nested virtualization only when you create a node pool. To check which machine series support nested virtualization, such as C3, C4, N2, and N4, see [Machine series comparison](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison).
  * **GPU support** : GPU device passthrough into Actor containers isn't supported. Specifying `nvidia.com/gpu` only places Pods on GPU-enabled nodes, but doesn't pass the GPU device into the Actor container. In addition, gVisor can't snapshot live CUDA contexts.

  * **Open network connections** : open network connections (such as database sessions or connections to MCP servers) aren't preserved when an agent suspends. Your agent code must handle reconnecting to external services when the agent resumes.

  * **Observability and Managed OpenTelemetry** : [Managed OpenTelemetry for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managed-otel-gke) has the following limitations:

    * Collector connectors aren't supported, which requires using an external proxy meter for telemetry benchmarking.
    * Collector deployments incur memory cache overhead that scales linearly with the number of Pods in large clusters.
    * TLS isn't supported in Managed OpenTelemetry for GKE.
  * **Storage** : Agent Substrate on GKE uses the following [Cloud Storage](https://docs.cloud.google.com/storage) buckets, which the installer creates if they don't exist:

    * **Snapshot bucket** : stores the snapshots of all the agents in your cluster. This bucket is required.
    * **Asset bucket** : stores the files that the microVM runtime needs, such as a Linux kernel and a root file system. The microVM runtime uses these files to run each sandbox in its own virtual machine. The name of this bucket is the name of the snapshot bucket followed by `-assets`. For example, if your snapshot bucket is named `example-snapshots`, then the asset bucket is named `example-snapshots-assets`. If you don't use the microVM runtime, this bucket stays empty.
  * **Kernel settings for high sandbox density** : running more than approximately 800 concurrent sandboxes on a node exceeds the default limits in the Linux kernel for file system monitoring (inotify) and for the neighbor table of the Address Resolution Protocol (ARP). Without higher limits, sandboxes can fail to start and networking can stall. The installer applies the required kernel settings to clusters that it creates. If you install Agent Substrate on GKE in an existing cluster or add your own node pools, you must apply these settings yourself. For the required values, see [Cluster requirements](https://docs.cloud.google.com/kubernetes-engine/ai-ml/install-overview-substrate#cluster-requirements) and [Design your infrastructure for Agent Substrate on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/design-substrate-infrastructure#rules).

  * **Installation environment** : you can't install Agent Substrate on GKE in [Cloud Shell](https://docs.cloud.google.com/shell). Cloud Shell has a 5 GB persistent disk storage limit which doesn't provide enough disk space for the installation. You must install Agent Substrate on GKE from a local workstation or a virtual machine (VM) that has sufficient disk space.




## What's next

  * Learn how to [install Agent Substrate on GKE](https://docs.cloud.google.com/kubernetes-engine/ai-ml/install-overview-substrate).
  * Learn how to right-size your cluster, isolate system node pools, and configure custom ComputeClasses and capacity buffers in [Design your infrastructure for Agent Substrate on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/design-substrate-infrastructure).
  * Explore the code that installs Agent Substrate on GKE in the [substrate-gke GitHub repository](https://github.com/ai-on-gke/substrate-gke).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 

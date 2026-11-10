---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-workloads/
title: Plan an architecture for AI agent workloads on GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T16:58:40.316336+00:00
---

# Plan an architecture for AI agent workloads on GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Plan an architecture for AI agent workloads on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Google Kubernetes Engine (GKE) provides two orchestration models for running AI agents inside kernel-isolated sandboxes (using Cloud Hypervisor microVMs or gVisor):

  * **[Agent Substrate on GKE](https://docs.cloud.google.com/kubernetes-engine/ai-ml/about-agent-substrate) (actor-based, recommended)**: use this model for most AI agent workloads, especially stateful, CPU-based agents that frequently suspend and resume. Active agent sessions (actors) share a pool of warm worker Pods and can be restored from Cloud Storage in less than one second.
  * **[Agent Sandbox on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox) (Pod-based)**: use this model when each agent requires a dedicated Kubernetes Pod. Choose this option for continuously active agents or workloads that need a full Kubernetes PodSpec (such as sidecars), GPUs or TPUs, Arm nodes, or GKE Autopilot clusters.



For a side-by-side summary of the two orchestration models, see Compare Agent Substrate and Agent Sandbox.

Read this document to choose an orchestration model, sandbox runtime, isolation controls, and storage options before you provision your GKE cluster. This document is for solution architects, AI developers, and platform admins and operators who design execution environments for AI agents on GKE.

## Architectural requirements for AI agent workloads on GKE

Running AI agent workloads on GKE lets you place isolated agent execution environments in the same cluster and network perimeter as your supporting Kubernetes services, and use GKE for node auto-provisioning, burst scaling, and lifecycle management.

Unlike continuously active microservices, AI agent workloads have the following architectural requirements:

  * **Untrusted code execution** : agents that generate and run code or shell commands need kernel, credential, and network isolation between sessions. Both orchestration models isolate agent sessions from the host kernel by using microVMs or gVisor, and let you restrict credentials and network egress in Agent Substrate or credentials and network policies in Agent Sandbox.
  * **High idle ratios** : interactive coding assistants and background productivity agents spend most of their lifecycle waiting for human input, model inference, or tool responses. In both Agent Substrate and Agent Sandbox, an active agent holds compute resources until your application suspends it.
  * **Rapid environment churn** : agent platforms frequently create, suspend, resume, or stop large numbers of environments in bursts. To keep node capacity ready for bursts of WorkerPool Pods in Agent Substrate or SandboxWarmPool Pods in Agent Sandbox, use GKE [custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes) to auto-provision nodes and [capacity buffers](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/capacity-buffer) to reserve standby capacity.
  * **Fast state suspend and resume** : stateful agents need to checkpoint and restore working memory (RAM) and workspace files without rebuilding environments from scratch. GKE integrates with [Cloud Storage](https://docs.cloud.google.com/storage/docs), [Filestore](https://docs.cloud.google.com/filestore/docs), and [Google Cloud Hyperdisk](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hyperdisk) to support session checkpoints and workspace storage in Agent Substrate and Pod snapshots and persistent storage in Agent Sandbox.



## Actor-based model: Agent Substrate on GKE (recommended)

[Agent Substrate on GKE](https://docs.cloud.google.com/kubernetes-engine/ai-ml/about-agent-substrate) is an execution runtime that decouples agent sessions (actors) from underlying Kubernetes Pods. Active actors share a pool of pre-warmed worker Pods (WorkerPool resources) across actor templates (ActorTemplate resources). When your application suspends an idle actor, Agent Substrate checkpoints the actor's state to Cloud Storage and releases its worker capacity so that other actors can use the node. When a new request arrives, Agent Substrate restores the actor onto an available worker in less than one second.

Use Agent Substrate as your default architecture for CPU-based agent workloads, including the following use cases:

  * **Interactive coding agents** : AI assistants that run terminal commands, build code, and edit files during developer conversations, and suspend between prompts.
  * **Long-running productivity agents** : background assistants that keep context over days or weeks while spending most of their time waiting for user input or external triggers.
  * **Ephemeral code and browser sandboxes** : on-demand environments for running LLM-generated code, headless browsers, or tool calls that restore in under a second and release compute after execution.



Agent Substrate requires GKE Standard clusters (version 1.37 or later on both the control plane and node pools) with x86 CPU worker nodes. GKE Autopilot isn't supported because the Agent Substrate node agent (`atelet`) runs as a privileged DaemonSet, and microVM worker pools require nested virtualization or bare-metal nodes. GPUs and TPUs aren't supported.

### Identity, credentials, and network egress

Agent Substrate provisions a unique SPIFFE X.509 certificate and JSON Web Token (JWT) for each actor to authenticate and audit requests from individual sessions. Because multiple actors share worker Pods over time, use Pod-level [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) only for worker infrastructure tasks.

To keep API keys and tokens outside the sandbox, the built-in egress gateway injects credentials into outbound requests in transit. You store secrets in Kubernetes Secret objects or in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview). When an outbound HTTP or HTTPS request matches an egress rule, the gateway authenticates the actor's mTLS tunnel and replaces placeholder headers with a fetched secret or an actor JWT. For more information, see the [open source Agent Substrate egress credential injection documentation](https://github.com/agent-substrate/substrate/blob/main/docs/guides/egress-credential-injection.md).

By default, Agent Substrate blocks all outbound traffic to other actors, the Kubernetes control plane, the Compute Engine metadata server, and the internet. Non-DNS UDP, arbitrary raw TCP connections, and HTTP WebSocket upgrades are blocked, and DNS resolves only hostnames that are allowed by the actor's EgressPolicy resource. To allow outbound connections, define HTTP, HTTPS, or TLS passthrough rules in the EgressPolicy resource by using fully qualified domain names (FQDNs) or wildcard hostnames. IP addresses and CIDR ranges aren't supported. For more information, see the open source Agent Substrate [egress traffic](https://github.com/agent-substrate/substrate/blob/main/docs/guides/egress-traffic.md) and [security](https://github.com/agent-substrate/substrate/blob/main/docs/security/security.md) documentation.

### Session checkpoints and workspace storage

When your application suspends an actor (on either gVisor or microVMs), Agent Substrate saves a snapshot to Cloud Storage across three layers: active memory, root file system changes, and durable directories (the volumes layer). Any attached external CSI volumes persist on their backing storage outside the snapshot and are re-attached on resume.

When a suspended actor resumes, Agent Substrate restores the highest snapshot layer that matches the target environment:

  * **Memory, root file system, and volumes** : restored in less than one second when the actor resumes with the same hardware, sandbox runtime, and container image.
  * **Root file system and volumes** : restored when the node hardware or sandbox runtime changes. The actor restarts its processes while keeping root file system changes and durable directories.
  * **Volumes only** : restored when you update the container image in the ActorTemplate resource while the actor is suspended. The next resume starts the containers from the updated image and restores durable directories and external volumes. Write data that must survive image updates to durable directories or external storage.



Suspend and resume latency scales with snapshot size. For large workspaces that need fast cross-node re-attachment when an actor resumes on a different node, use external [Filestore agent volumes](https://docs.cloud.google.com/filestore/docs/agent-substrate) rather than storing the data inside the snapshot. Each external CSI volume ([Preview](https://cloud.google.com/products#product-launch-stages)) in an ActorTemplate resource is provisioned exclusively for a single actor (not shared across actors) and is deleted with that actor. Production support for Filestore agent volumes is offered through a limited GA program that requires an access request.

Block storage (such as Hyperdisk) is used for node boot disks and local snapshot caching rather than per-actor CSI volumes because cross-node block detach and attach latency slows actor resume. For more information, see the [open source Agent Substrate CSI volumes documentation](https://github.com/agent-substrate/substrate/blob/main/docs/guides/csi-volumes.md).

## Pod-based model: Agent Sandbox on GKE

[Agent Sandbox on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox) runs each agent in a dedicated, stateful Kubernetes Pod managed through Kubernetes custom resources (Sandbox, SandboxClaim, SandboxTemplate, and SandboxWarmPool). A SandboxWarmPool resource maintains pre-warmed Sandbox resources with running Pods for a specific SandboxTemplate resource so that the controller can assign a ready Sandbox resource and its running Pod to a claim in less than one second.

Choose Agent Sandbox when each agent needs a dedicated Pod or when your workloads have any of the following requirements:

  * **Continuously active agents and single-Pod services** : workloads without frequent idle periods, or persistent sessions (such as cloud development environments or Jupyter Notebooks) that need a stable hostname and storage without StatefulSet complexity.
  * **Hardware accelerators (GPUs or TPUs)** : agents that need direct access to GPUs or TPUs inside the sandbox. Accelerators work only with the gVisor runtime on supported [GPU models](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#gpus) and [TPU versions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#tpus). MicroVMs don't support GPUs or TPUs.
  * **Full Kubernetes PodSpec, Arm nodes, or GKE Autopilot** : workloads that require custom sidecar or init containers, standard Kubernetes APIs and tooling (for example, `kubectl` commands, role-based access control, and existing controllers), Arm CPUs, or GKE Autopilot clusters.



### Identity, credentials, and network policies

Because each agent runs in a dedicated Pod, you can grant Google Cloud Identity and Access Management (IAM) permissions to the Pod by using [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) or [Agent Identity](https://docs.cloud.google.com/kubernetes-engine/security/about-agent-identity) ([Preview](https://cloud.google.com/products#product-launch-stages)). Both options bind identity to the Pod's Kubernetes ServiceAccount at Pod creation, so all pre-warmed Pods in a SandboxWarmPool resource share the same identity. To isolate identities per agent or tenant, maintain a separate SandboxWarmPool resource per identity or create Sandbox resources on demand without a warm pool.

You mount secrets into Pods by using standard Kubernetes Secret objects or CSI volumes. Agent Sandbox doesn't include a gateway for out-of-sandbox credential injection. To inject credentials in transit, deploy your own external proxy.

The controller creates a default-deny NetworkPolicy object for each SandboxTemplate resource. For Sandbox resources that you create directly without a template, create your own NetworkPolicy object. You restrict traffic by using standard GKE network controls:

  * **Layer 4** : restrict Pod-to-Pod and IP traffic with [GKE network policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy) (NetworkPolicy objects).
  * **Layer 7** : restrict outbound connections to approved domains with [FQDN network policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/fqdn-network-policies) (FQDNNetworkPolicy objects).



### Idle suspension, Pod snapshots, and storage

An idle agent's Pod keeps its reserved CPU and memory until your application suspends the Sandbox resource by setting its `spec.operatingMode` field to `Suspended`. Suspending the Sandbox resource deletes the Pod while keeping its persistent volumes. Deleting the Pod clears in-memory data and container file system changes. To save and restore that state from Cloud Storage, take a [GKE Pod snapshot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox-pod-snapshots) before suspending the agent. Pod snapshots require the gVisor runtime and don't support microVMs or TPUs. Restoring a Pod from a snapshot takes approximately three to five seconds.

For persistent storage beyond Pod snapshots, choose from the following options:

  * **Filestore** : mount a shared `ReadWriteMany` (`RWX`) PersistentVolumeClaim (PVC) across multiple Sandbox Pods for collaborative workspaces. For more information, see [Choose storage for AI agentic workloads](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox-storage).
  * **Hyperdisk** : use Google Cloud Hyperdisk Balanced (`ReadWriteOnce` access mode) for isolated Pod disks, or Google Cloud Hyperdisk ML (`ReadOnlyMany` access mode) to share read-only datasets or model weights across nodes. For more information, see [Choose storage for AI agentic workloads](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox-storage) and [About Hyperdisk for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hyperdisk).



## Compare Agent Substrate and Agent Sandbox

The following table summarizes the architectural differences between Agent Substrate on GKE and Agent Sandbox on GKE:

Dimension |  Agent Substrate on GKE (actor-based)  |  Agent Sandbox on GKE (Pod-based)   
---|---|---  
Recommended AI agent workloads |  Most stateful, CPU-based agents that frequently suspend and resume  |  Continuously active agents, GPU or TPU workloads, custom PodSpecs, Arm nodes, or GKE Autopilot   
Scheduling unit | Multiple actors share a pool of warm Pods (WorkerPool) | One dedicated Pod per agent (Sandbox)  
Sandbox runtimes |  gVisor and Cloud Hypervisor microVMs (managed inside WorkerPool Pods)  |  gVisor and microVMs on GKE Standard (with GKE Sandbox enabled on the node pool or ComputeClass), or gVisor on GKE Autopilot (enabled by default)   
Warm pooling |  Shared WorkerPool resources across actor templates and container images  | One SandboxWarmPool resource per template and container image  
Control plane path |  Dedicated control plane and database outside the `kube-apiserver` component  |  Standard Kubernetes controllers, `kube-apiserver`, and `etcd`  
Idle resource handling | Suspending an idle actor releases its worker CPU and memory |  Suspending an idle Sandbox resource deletes its Pod and keeps persistent volumes   
State checkpoints |  Built-in Cloud Storage snapshots on gVisor and microVMs, restoring in less than one second  |  [GKE Pod snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox-pod-snapshots) (supported on gVisor only), restoring in 3-5 seconds   
Supported cluster modes |  GKE Standard (version 1.37 or later, x86 nodes)  |  GKE Standard and GKE Autopilot   
Hardware accelerators | Not supported (CPU-only worker nodes) | GPUs and TPUs supported with the gVisor runtime only  
Kubernetes PodSpec support | Subset split across ActorTemplate and WorkerPool resources | Full PodSpec, including sidecars and init containers  
Networking |  Built-in Envoy ingress and egress gateways with per-actor mTLS tunnels  | Kubernetes Services, NetworkPolicy, and FQDNNetworkPolicy  
Identity model | Per-actor SPIFFE X.509 certificate and JWT |  Pod ServiceAccount using Workload Identity Federation for GKE or Agent Identity ([Preview](https://cloud.google.com/products#product-launch-stages)), shared across a warm pool   
Secret management | Injected into outbound requests at the egress gateway |  Mounted in the Pod by using Kubernetes Secret objects or CSI volumes   
  
## Select a sandbox runtime

Both Agent Substrate and Agent Sandbox isolate untrusted code from the host node by using Cloud Hypervisor microVMs or gVisor, but you configure the runtime differently in each model:

  * **Agent Substrate** : select the runtime on the WorkerPool resource. Agent Substrate manages its own microVM and gVisor runtimes inside its WorkerPool Pods rather than using the node-level [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) feature. Don't enable GKE Sandbox on Agent Substrate worker node pools, because the `sandbox.gke.io/runtime` node taint prevents WorkerPool Pods from scheduling.
  * **Agent Sandbox** : set the `runtimeClassName` field to `gvisor` or `microvm` in the Pod template of your SandboxTemplate resource. On GKE Standard, also enable GKE Sandbox on the node pool or in a custom ComputeClass. On GKE Autopilot, gVisor is available by default and microVMs aren't supported.



Both runtimes run untrusted code and headless browsers:

  * **MicroVMs** : each sandbox runs in a lightweight virtual machine with a dedicated guest Linux kernel. Choose microVMs when you need VM-level isolation, full Linux syscall compatibility, or per-container CPU and memory limits inside a multi-container actor.
  * **gVisor** : each sandbox runs in a user-space kernel that intercepts and filters Linux syscalls. Choose gVisor for faster cold starts, lower memory overhead, or broader Compute Engine machine support (including GPUs, TPUs, Arm nodes, and GKE Autopilot in Agent Sandbox).

The following table compares microVMs and gVisor on GKE: Feature | MicroVMs | gVisor  
---|---|---  
Kernel access | Full Linux kernel | Subset of Linux kernel syscalls  
Isolation level |  Hardware virtualization with a dedicated guest kernel  |  Syscall interception in a user-space kernel   
CPU and memory overhead |  Per-actor VMM memory in Agent Substrate. Fixed 250 mCPU and 130 MiB per Pod in GKE Sandbox.  |  Dynamic overhead with low base memory   
Start time |  1 to 2 seconds  | Less than 100 ms  
GKE node configuration |  GKE Standard nodes with [nested virtualization](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nested-virtualization) (both models), or x86 bare-metal nodes (Agent Substrate only)  |  GKE Standard node pools (both models), or GKE Autopilot nodes (Agent Sandbox only)   
Node image support |  Container-Optimized OS (`cos_containerd`) in Agent Substrate. Container-Optimized OS (`cos_containerd`) or Ubuntu in GKE Sandbox.  |  Container-Optimized OS (`cos_containerd`) only   
Machine type compatibility |  x86 [machine series that support nested virtualization](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview) and x86 bare metal (not supported on E2 or Arm)  |  Non-mixed-CPU x86 series in Agent Substrate. Most x86, Arm, and accelerator series in Agent Sandbox.   
Accelerator support |  Not supported  |  Supported [GPU models](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#gpus) and [TPU versions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#tpus) (Agent Sandbox only)   
Example use cases | 

  * Autonomous coding and browser agents
  * Workloads that require full Linux kernel compatibility
  * High-I/O workloads with frequent system calls

| 

  * Untrusted applications in Python, Node.js, Go, Java, or Rust 
  * CPU, GPU, or TPU inference and code-execution sandboxes
  * Web frontends, caches, and proxies

  
  
For more information about these isolation technologies, see [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods).

## What's next

  * Learn more about actor lifecycles in [About Agent Substrate on GKE](https://docs.cloud.google.com/kubernetes-engine/ai-ml/about-agent-substrate).
  * [Install Agent Substrate on GKE](https://docs.cloud.google.com/kubernetes-engine/ai-ml/install-overview-substrate).
  * Learn how to [Design your infrastructure for Agent Substrate on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/design-substrate-infrastructure).
  * Learn more about Pod-based sandboxes in [About Agent Sandbox on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox).
  * [Install Agent Sandbox on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox/
title: Install Agent Sandbox on GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:51:45.936117+00:00
---

# Install Agent Sandbox on GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Install Agent Sandbox on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document explains how to install the open source [Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox) controller on a Google Kubernetes Engine (GKE) cluster to run sandboxed workloads in dedicated Kubernetes Pods. You also learn how to create a sandboxed environment on the cluster to safely execute untrusted code.

For an overview of how Agent Sandbox on GKE isolates untrusted AI-generated code, see [About Agent Sandbox on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox).

## Choose between Pod-based and actor-based architectures

Before you install Agent Sandbox on GKE, confirm which GKE architecture fits your AI agent workloads:

  * **Agent Substrate on GKE (actor-based)** : use this architecture for most agentic workloads, especially stateful agents that frequently suspend and resume. Active agents share a pool of warm Pods instead of keeping a dedicated Pod per agent, so you can run more agents on fewer nodes. Agent Substrate on GKE provides automatic suspension and resumption for idle workloads, and restores agents from storage in less than one second. In contrast, Agent Sandbox on GKE requires manual [Pod snapshotting](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox-pod-snapshots), and you need to build application code to detect inactivity and save the agent's progress. Agent Substrate on GKE requires a GKE Standard cluster. For more information, see [About Agent Substrate on GKE](https://docs.cloud.google.com/kubernetes-engine/ai-ml/about-agent-substrate). To install this option instead, see [Install Agent Substrate on GKE](https://docs.cloud.google.com/kubernetes-engine/ai-ml/install-overview-substrate).
  * **Agent Sandbox on GKE (Pod-based)** : use this architecture, which you install in this document, when each agent needs a dedicated Kubernetes Pod on a GKE Autopilot or Standard cluster. Choose this option for continuously active agents or workloads that require any of the following: 
    * Declarative Kubernetes APIs, such as the `Sandbox` and `SandboxClaim` custom resources
    * The full Kubernetes `PodSpec` schema, including custom sidecar and init containers
    * Direct access to hardware accelerators, such as GPUs or TPUs
    * GKE Autopilot clusters



## Costs

Agent Sandbox on GKE is open source software that you can use at no extra charge. [GKE pricing](https://cloud.google.com/kubernetes-engine/pricing) applies to the resources that you create, including the compute resources that the Agent Sandbox controller uses.

To avoid unnecessary charges, ensure that you disable GKE or delete the project after you have completed this document.

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Enable the Google Kubernetes Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)

  4. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)




## Define environment variables

To simplify the commands that you run in this document, you can set environment variables in Cloud Shell. In Cloud Shell, define the following useful environment variables by running the following commands:
    
    
    export CLUSTER_NAME="agent-sandbox-cluster"
    export LOCATION="us-central1"
    export AGENT_SANDBOX_VERSION="v1.0.6"
    export NODE_POOL_NAME="agent-sandbox-pool"
    export MACHINE_TYPE="e2-standard-2"
    

Here's an explanation of these environment variables:

  * `CLUSTER_NAME`: the name of your GKE cluster—for example, `agent-sandbox-cluster`.
  * `LOCATION`: the Google Cloud region or zone where your GKE cluster is created. If you create an Autopilot cluster, set this to the region (for example, `us-central1`). Autopilot clusters are always regional. If you create a Standard cluster, set this to the zone (for example, `us-central1-a`). To reduce costs, this document creates a zonal cluster, which uses fewer nodes than a regional cluster.
  * `AGENT_SANDBOX_VERSION`: the version of the open source Agent Sandbox controller to install. This document uses version 1.0.6. To see other versions, go to the [Agent Sandbox releases page](https://github.com/kubernetes-sigs/agent-sandbox/releases).
  * `NODE_POOL_NAME`: the name of the node pool that will run sandboxed workloads—for example, `agent-sandbox-pool`. This variable is only required if you are creating a GKE Standard cluster.
  * `MACHINE_TYPE`: the machine type of the nodes in your cluster's default node pool and in the gVisor node pool—for example, `e2-standard-2`. For details about different machine series and choosing between different options, see the [Machine families resource and comparison guide](https://docs.cloud.google.com/compute/docs/machine-resource). This variable is only required if you are creating a GKE Standard cluster.



## Create a GKE cluster

Agent Sandbox on GKE isolates sandboxed workloads by using [gVisor](https://gvisor.dev/docs/) or [microVMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#sandbox-technologies). If you don't specify a sandbox runtime, sandboxes run without kernel isolation, which we don't recommend for untrusted code. This document uses gVisor. Autopilot clusters enable gVisor automatically. In Standard clusters, you create a node pool that has gVisor enabled. To use microVMs instead, see [Enable the microVM sandbox type](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods#enable-microvm). The recommended security policy allows only gVisor, so it rejects sandboxes that use microVMs.

**Best practice** : 

Use an Autopilot cluster for a fully managed Kubernetes experience. To choose the GKE mode of operation that's the best fit for your workloads, see [Choose a GKE mode of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

###  Autopilot 

To create an Autopilot cluster, make sure that the `LOCATION` environment variable is set to a region, such as `us-central1`, and then run the following command:
    
    
    gcloud container clusters create-auto ${CLUSTER_NAME} \
        --location=${LOCATION}
    

###  Standard 

To create a Standard cluster, you create the cluster and then add a node pool with gVisor enabled. To reduce costs, this document creates a zonal cluster with a single node per pool.

**Best practice** : 

Use a [regional cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters) for production workloads. Regional clusters replicate the control plane and nodes across multiple zones, which provides higher availability than zonal clusters.

  1. Set the `LOCATION` environment variable to a zone, such as `us-central1-a`:
         
         export LOCATION="us-central1-a"
         

  2. Create the cluster:
         
         gcloud container clusters create ${CLUSTER_NAME} \
             --location=${LOCATION} \
             --machine-type=${MACHINE_TYPE} \
             --num-nodes=1
         

  3. Create a separate node pool with gVisor enabled:
         
         gcloud container node-pools create ${NODE_POOL_NAME} \
             --cluster=${CLUSTER_NAME} \
             --machine-type=${MACHINE_TYPE} \
             --location=${LOCATION} \
             --num-nodes=1 \
             --image-type=cos_containerd \
             --sandbox=type=gvisor
         

To use microVMs instead of gVisor, create the node pool as described in [Enable the microVM sandbox type](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods#enable-microvm). The rest of this document uses gVisor.




To use an existing Standard cluster instead, make sure that the cluster includes a node pool that has gVisor enabled. If the cluster doesn't have such a node pool, create one by running the preceding `gcloud container node-pools create` command.

To enable the `kubectl` command-line tool to connect to the cluster, get the cluster credentials:
    
    
    gcloud container clusters get-credentials ${CLUSTER_NAME} \
        --location=${LOCATION}
    

## Install Agent Sandbox

To install Agent Sandbox, apply a release manifest from the Agent Sandbox GitHub repository. The `sandbox-with-extensions.yaml` manifest installs the Agent Sandbox controller and the CustomResourceDefinitions for the `Sandbox` resource and for the `SandboxTemplate`, `SandboxClaim`, and `SandboxWarmPool` extension resources.

  1. Apply the release manifest:
         
         kubectl apply -f https://github.com/kubernetes-sigs/agent-sandbox/releases/download/${AGENT_SANDBOX_VERSION}/sandbox-with-extensions.yaml
         

The manifest creates the `agent-sandbox-system` namespace and deploys the controller in that namespace.

  2. Wait until the controller is ready:
         
         kubectl rollout status deployment/agent-sandbox-controller \
             --namespace=agent-sandbox-system \
             --timeout=120s
         

**Note:** In an Autopilot cluster, the controller can take several minutes to become ready because GKE might need to create a node for it. If the command times out before the controller is ready, run the command again.



You can also install Agent Sandbox by using Helm. For instructions, see the [Agent Sandbox Helm chart README](https://github.com/kubernetes-sigs/agent-sandbox/blob/v1.0.6/helm/README.md).

## Verify the installation

  1. Verify that the Agent Sandbox CustomResourceDefinitions are installed:
         
         kubectl get crd \
             sandboxes.agents.x-k8s.io \
             sandboxtemplates.extensions.agents.x-k8s.io \
             sandboxclaims.extensions.agents.x-k8s.io \
             sandboxwarmpools.extensions.agents.x-k8s.io
         

The output lists the four CustomResourceDefinitions.

  2. Verify that the controller is running:
         
         kubectl get deployment agent-sandbox-controller \
             --namespace=agent-sandbox-system
         

When the controller is running, the `READY` column shows `1/1`.




## Apply the recommended security policy

By default, Agent Sandbox on GKE doesn't restrict the configuration of the Pods that run your sandboxes. To help enforce isolation settings for your sandboxes, apply the recommended `secure-sandbox-policy` [ValidatingAdmissionPolicy](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/) from the Agent Sandbox GitHub repository. This policy rejects any `Sandbox` resource that doesn't meet the Agent Sandbox on GKE deployment requirements.

  1. Apply the policy:
         
         kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/agent-sandbox/${AGENT_SANDBOX_VERSION}/examples/policy/vap/secure-sandbox-policy.yaml
         

  2. Apply the policy binding. The binding enforces the policy in all namespaces except system namespaces, such as `kube-system`:
         
         kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/agent-sandbox/${AGENT_SANDBOX_VERSION}/examples/policy/vap/secure-sandbox-binding.yaml
         




The policy validates `Sandbox` resources. When you create a `SandboxWarmPool` resource or a `SandboxClaim` resource, the controller creates `Sandbox` resources from a `SandboxTemplate` resource. If the template doesn't meet the requirements, the policy rejects the `Sandbox` resource, and the error appears in the controller logs. To view the logs, run the following command:
    
    
    kubectl logs deployment/agent-sandbox-controller \
        --namespace=agent-sandbox-system
    

You own this policy, and you can modify it to fit your workloads. For more information, see [Sandbox security policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox#sandbox-security-policies).

## Agent Sandbox on GKE deployment requirements

If you apply the recommended security policy, your workload manifests, such as a `Sandbox` or `SandboxTemplate` resource, must include specific security and configuration settings. If a `Sandbox` resource doesn't meet these requirements, the admission controller rejects it. The container requirements apply to all containers in the Pod, including init containers and ephemeral containers.

### Required configuration

Your deployment manifest must include the following settings:

  * `runtimeClassName: gvisor`: ensures the Pod runs in a gVisor sandbox. The policy rejects sandboxes that use any other runtime, including microVMs.
  * `automountServiceAccountToken: false`: prevents the Pod from automatically mounting the default service account token.
  * `securityContext.runAsNonRoot: true`: ensures the container does not run as the root user.
  * `securityContext.capabilities.drop: ["ALL"]`: drops all Linux capabilities from the container.
  * `resources.limits`: you must specify CPU and memory limits to prevent potential denial-of-service (DoS) scenarios.
  * `nodeSelector`: must target `sandbox.gke.io/runtime: gvisor`.
  * `tolerations`: must include a toleration for the `sandbox.gke.io/runtime=gvisor:NoSchedule` taint.



### Prohibited configuration

Your deployment manifest must **not** include any of the following:

  * `hostNetwork: true`, `hostPID: true`, or `hostIPC: true`.
  * `privileged: true` in container security contexts.
  * `procMount: Unmasked` in container security contexts.
  * `HostPath` volumes.
  * Added capabilities (`capabilities.add`).
  * `hostPort` settings.
  * Custom sysctls.
  * Projected volumes for service account tokens or certificates.



## Deploy the Sandbox Router (optional)

The Sandbox Router is an HTTP proxy that routes requests from clients, such as the [Agent Sandbox Python client](https://pypi.org/project/k8s-agent-sandbox/), to the Pods that run your sandboxes. If you plan to use the Python client, for example as described in [Isolate AI code execution with Agent Sandbox on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox), deploy the router.

You deploy the router in the `agent-sandbox-system` namespace. By default, the network policy that Agent Sandbox on GKE creates for each `SandboxTemplate` resource allows incoming traffic to sandboxes only from the router Pods in this namespace.

  1. Create the router's service account and the RBAC permissions that let the router look up sandbox Pods:
         
         kubectl apply \
             -f https://raw.githubusercontent.com/kubernetes-sigs/agent-sandbox/${AGENT_SANDBOX_VERSION}/sandbox-router/deploy/serviceaccount.yaml \
             -f https://raw.githubusercontent.com/kubernetes-sigs/agent-sandbox/${AGENT_SANDBOX_VERSION}/sandbox-router/deploy/rbac.yaml
         

  2. Deploy the router. The following command sets the router image to the same version as the controller:
         
         curl -sSL https://raw.githubusercontent.com/kubernetes-sigs/agent-sandbox/${AGENT_SANDBOX_VERSION}/sandbox-router/deploy/deployment.yaml \
             | sed "s|sandbox-router-go:latest|sandbox-router-go:${AGENT_SANDBOX_VERSION}|" \
             | kubectl apply -f -
         

  3. Create the router's Service:
         
         kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/agent-sandbox/${AGENT_SANDBOX_VERSION}/sandbox-router/deploy/service.yaml
         

  4. Wait until the router is ready:
         
         kubectl rollout status deployment/sandbox-router \
             --namespace=agent-sandbox-system \
             --timeout=120s
         




This router configuration is for development and testing. For production settings, such as TLS, replica counts, and network policies for the router, see the [Sandbox Router deployment README](https://github.com/kubernetes-sigs/agent-sandbox/blob/v1.0.6/sandbox-router/deploy/README.md).

## Deploy a sandboxed environment

We recommend deploying a sandboxed environment by defining a `SandboxTemplate` resource and keeping pre-warmed instances ready by using a `SandboxWarmPool` resource. You can then request an instance from this warm pool by using a `SandboxClaim` resource. Alternatively, you can create a `Sandbox` resource directly, but this approach doesn't support warm pools.

`SandboxTemplate`, `SandboxWarmPool`, `SandboxClaim`, and `Sandbox` are [Kubernetes custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/).

### Recommended: Create `SandboxTemplate` and `SandboxWarmPool` resources

The `SandboxTemplate` resource acts as a reusable blueprint. The `SandboxWarmPool` resource helps ensure that a specified number of pre-warmed sandboxes are always running and ready to be claimed. Use of this custom resource minimizes startup latency.

To deploy a sandboxed environment by creating the `SandboxTemplate` and `SandboxWarmPool` resources, complete the following steps:

  1. In Cloud Shell, create a file named `sandbox-template.yaml` with the following content:
         
         apiVersion: extensions.agents.x-k8s.io/v1beta1
         kind: SandboxTemplate
         metadata:
           name: python-runtime-template
           namespace: default
         spec:
           podTemplate:
             metadata:
               labels:
                 sandbox-type: python-runtime
             spec:
               runtimeClassName: gvisor # Required
               automountServiceAccountToken: false # Required
               securityContext:
                 runAsNonRoot: true # Required
               nodeSelector:
                 sandbox.gke.io/runtime: gvisor # Required
               tolerations:
               - key: "sandbox.gke.io/runtime"
                 value: "gvisor"
                 effect: "NoSchedule" # Required
               containers:
               - name: runtime
                 image: registry.k8s.io/agent-sandbox/python-runtime-sandbox:v0.1.0
                 ports:
                 - containerPort: 8888
                 resources:
                   requests:
                     cpu: "250m"
                     memory: "512Mi"
                   limits:
                     cpu: "500m"
                     memory: "1Gi" # Required
                 securityContext:
                   capabilities:
                     drop: ["ALL"] # Required
               restartPolicy: OnFailure
         

  2. Apply the `SandboxTemplate` manifest:
         
         kubectl apply -f sandbox-template.yaml
         

  3. Create a file named `sandbox-warmpool.yaml` with the following content:
         
         apiVersion: extensions.agents.x-k8s.io/v1beta1
         kind: SandboxWarmPool
         metadata:
           name: python-runtime-warmpool
           namespace: default
           labels:
             app: python-runtime-warmpool
         spec:
           replicas: 2
           sandboxTemplateRef:
             # This must match the name of the SandboxTemplate.
             name: python-runtime-template
         

  4. Apply the `SandboxWarmPool` manifest:
         
         kubectl apply -f sandbox-warmpool.yaml
         

  5. Wait until the warm pool's sandboxes are ready:
         
         kubectl wait sandboxwarmpool python-runtime-warmpool \
             --for=jsonpath='{.status.readyReplicas}'=2 \
             --timeout=600s
         

If you create a `SandboxClaim` resource before the pool's sandboxes are ready, the controller might create a new sandbox for the claim instead of assigning one from the pool. In an Autopilot cluster, the sandboxes can take several minutes to become ready because GKE might need to create nodes for them.




### Create a `SandboxClaim` resource

The `SandboxClaim` resource requests a sandbox from the warm pool. Because you created a warm pool, the controller assigns a running sandbox from the pool to the claim instead of creating a new one.

To request a sandbox from the warm pool by creating a `SandboxClaim` resource, complete the following steps:

  1. Create a file named `sandbox-claim.yaml` with the following content:
         
         apiVersion: extensions.agents.x-k8s.io/v1beta1
         kind: SandboxClaim
         metadata:
           name: sandbox-claim
           namespace: default
         spec:
           warmPoolRef:
             # This must match the name of the SandboxWarmPool.
             name: python-runtime-warmpool
         

  2. Apply the `SandboxClaim` manifest:
         
         kubectl apply -f sandbox-claim.yaml
         

  3. Verify that the sandbox, claim, and warm pool are ready:
         
         kubectl get sandboxwarmpool,sandboxclaim,sandbox,pod
         




### Alternative: Create a `Sandbox` resource directly

If you don't need the fast startup times provided by warm pools, you can deploy a `Sandbox` resource directly without using templates.

To deploy a sandboxed environment by creating a `Sandbox` resource directly, complete the following steps:

  1. Create a file named `sandbox.yaml` with the following content:
         
         apiVersion: agents.x-k8s.io/v1beta1
         kind: Sandbox
         metadata:
           name: sandbox-example-2
         spec:
           podTemplate:
             metadata:
               labels:
                 sandbox: sandbox-example
             spec:
               runtimeClassName: gvisor
               restartPolicy: OnFailure
               automountServiceAccountToken: false # Required
               securityContext:
                 runAsNonRoot: true # Required
                 runAsUser: 1000 # Required if image defaults to root (for example, busybox)
               nodeSelector:
                 sandbox.gke.io/runtime: gvisor
               tolerations:
               - key: "sandbox.gke.io/runtime"
                 value: "gvisor"
                 effect: "NoSchedule" # Required
               containers:
               - name: my-container
                 image: busybox
                 command: ["/bin/sh", "-c"]
                 args: ["sleep 3600000; echo 'Container finished successfully'; exit 0"]
                 securityContext:
                   capabilities:
                     drop: ["ALL"] # Required
                   allowPrivilegeEscalation: false
                 resources:
                   limits:
                     cpu: "100m"
                     memory: "128Mi" # Required
         

  2. Apply the `Sandbox` manifest:
         
         kubectl apply -f sandbox.yaml
         

  3. Verify that the sandbox is running:
         
         kubectl get sandbox
         




## Upgrade Agent Sandbox

To upgrade Agent Sandbox, apply the release manifest for the new version:
    
    
    export AGENT_SANDBOX_VERSION="NEW_VERSION"
    kubectl apply -f https://github.com/kubernetes-sigs/agent-sandbox/releases/download/${AGENT_SANDBOX_VERSION}/sandbox-with-extensions.yaml
    

Replace `NEW_VERSION` with the version that you want to install, such as a version listed on the [Agent Sandbox releases page](https://github.com/kubernetes-sigs/agent-sandbox/releases).

Before you upgrade, review the release notes for the new version. If your cluster runs a version of Agent Sandbox earlier than 1.0.0, you must migrate your resources to the `v1beta1` API before you upgrade, because version 1.0.0 removed the `v1alpha1` API. For instructions, see the [API migration guide](https://github.com/kubernetes-sigs/agent-sandbox/blob/v1.0.6/docs/api-migration-guide.md).

If you deployed the Sandbox Router or applied the recommended security policy, repeat those steps for the new version.

## Uninstall Agent Sandbox

**Caution:** Uninstalling Agent Sandbox deletes the Agent Sandbox CustomResourceDefinitions, which also deletes all `Sandbox`, `SandboxTemplate`, `SandboxClaim`, and `SandboxWarmPool` resources in all namespaces.

  1. Check for Agent Sandbox resources that are still in use:
         
         kubectl get sandboxes,sandboxclaims,sandboxwarmpools,sandboxtemplates \
             --all-namespaces
         

  2. If you applied the recommended security policy, delete the policy binding and the policy:
         
         kubectl delete validatingadmissionpolicybinding secure-sandbox-binding
         kubectl delete validatingadmissionpolicy secure-sandbox-policy
         

  3. If you deployed the Sandbox Router, delete its cluster-wide RBAC resources:
         
         kubectl delete -f https://raw.githubusercontent.com/kubernetes-sigs/agent-sandbox/${AGENT_SANDBOX_VERSION}/sandbox-router/deploy/rbac.yaml
         

The router's other resources are in the `agent-sandbox-system` namespace, which the next step deletes.

  4. To delete the Agent Sandbox controller, its namespace, and its CustomResourceDefinitions, delete the release manifest for the version that you installed:
         
         kubectl delete -f https://github.com/kubernetes-sigs/agent-sandbox/releases/download/${AGENT_SANDBOX_VERSION}/sandbox-with-extensions.yaml
         




## Clean up resources

To avoid incurring charges to your Google Cloud account, delete the GKE cluster that you created.
    
    
    gcloud container clusters delete ${CLUSTER_NAME} \
        --location=${LOCATION} \
        --quiet
    

If you created an Autopilot cluster, the location is the region (for example, `us-central1`). If you created a Standard cluster, the location is the zone (for example, `us-central1-a`).

## What's next

  * Learn how to [save and restore Agent Sandbox on GKE environments with Pod snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox-pod-snapshots).
  * Learn about the underlying technology used by [Agent Sandbox on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods).
  * Learn more about [GKE security](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview).
  * Explore the [Agent Sandbox open-source project](https://github.com/kubernetes-sigs/agent-sandbox) on GitHub.
  * Learn how to use open source [Kata Containers with Agent Sandbox on GKE](https://github.com/kubernetes-sigs/agent-sandbox/tree/v1.0.6/examples/kata-gke-sandbox). Kata Containers isn't a Google Cloud product. If you install and use this software, then you're responsible for management and troubleshooting. Google's support and SLAs don't apply to Kata Containers.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 

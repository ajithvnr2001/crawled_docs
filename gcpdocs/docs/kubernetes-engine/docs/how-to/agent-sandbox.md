---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox/
title: Isolate AI code execution with Agent Sandbox on GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:51:44.805219+00:00
---

# Isolate AI code execution with Agent Sandbox on GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Isolate AI code execution with Agent Sandbox on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows you how to run AI-generated code in an isolated sandbox on a Google Kubernetes Engine (GKE) cluster. You create a sandbox template and a pool of ready sandboxes on the cluster. Then, you run a Python script that requests a sandbox from the pool and runs a command in the sandbox. The script uses the Agent Sandbox Python client, a library for creating and managing sandboxes.

Running untrusted code in a sandbox helps protect your system from potential vulnerabilities in AI-generated code, increase development velocity, and improve the security of your deployments. For an overview of how Agent Sandbox on GKE isolates untrusted AI-generated code, see [About Agent Sandbox on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox).

## Costs

Agent Sandbox on GKE is open source software that you can use at no extra charge. [GKE pricing](https://cloud.google.com/kubernetes-engine/pricing) applies to the resources that you create, including the compute resources that the Agent Sandbox controller uses.

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Enable the Kubernetes Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)

  4. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  5. Verify that you have the permissions required to complete this document.
  6. Make sure that you have a GKE cluster that has the Agent Sandbox controller installed and the Sandbox Router deployed. If you don't, complete only the following sections of [Install Agent Sandbox on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox), and then return to this document: 
     1. [Define environment variables](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox#define-environment-variables)
     2. [Create a GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox#create-cluster)
     3. [Install Agent Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox#install-agent-sandbox)
     4. [Deploy the Sandbox Router](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox#deploy-sandbox-router)
You don't need to complete the other sections of that document, such as [Deploy a sandboxed environment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox#deploy-a-sandboxed-environment). Later in this document, you create your own `SandboxTemplate` and `SandboxWarmPool` resources.



### Required roles

To get the permissions that you need to create and manage sandboxes, ask your administrator to grant you the [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Define environment variables

To simplify the commands that you run in this document, you can set environment variables in Cloud Shell. In Cloud Shell, define the following useful environment variables by running the following commands:
    
    
    export CLUSTER_NAME="agent-sandbox-cluster"
    export LOCATION="us-central1"
    

Here's an explanation of these environment variables:

  * `CLUSTER_NAME`: the name of your GKE cluster—for example, `agent-sandbox-cluster`.
  * `LOCATION`: the Google Cloud region or zone where your GKE cluster is located. If you use an Autopilot cluster, set this to the region (for example, `us-central1`). If you use a Standard cluster, set this to the zone (for example, `us-central1-a`).



## Deploy a sandboxed environment

This section shows you how to create the sandbox blueprint (a `SandboxTemplate` resource), verify the networking router, and install the Python client you will use to interact with the sandbox.

The recommended way to create and interact with your sandbox is by using the [Agentic Sandbox Python client](https://github.com/kubernetes-sigs/agent-sandbox/tree/v1.0.6/clients/python/agentic-sandbox-client). This client provides an interface that simplifies the entire lifecycle of a sandbox, from creation to cleanup. It's a Python library you can use to programmatically create, use, and delete sandboxes.

The client uses a Sandbox Router as a central entry point for all traffic. In the example described in this document, the client creates a tunnel to this router using the command `kubectl port-forward`, so that you don't need to expose any public IP addresses. Be aware that making use of `kubectl port-forward` isn't a secure solution and its use should be limited to development environments.

### Create `SandboxTemplate` and `SandboxWarmPool` resources

You now define the configuration for your sandbox by creating a `SandboxTemplate` resource and a `SandboxWarmPool` resource. The `SandboxTemplate` resource acts as a reusable blueprint that the Agent Sandbox controller uses to create consistent, pre-configured sandbox environments. The `SandboxWarmPool` resource helps ensure that a specified number of _pre-warmed_ Pods are always running and ready to be claimed. A pre-warmed sandbox is a running Pod that's already initialized. This pre-initialization enables new sandboxes to be created in under a second, and avoids the startup latency of launching a regular sandbox:

  1. In Cloud Shell, create a file named `sandbox-template-and-pool.yaml` with the following content:
         
         apiVersion: extensions.agents.x-k8s.io/v1beta1
         kind: SandboxTemplate
         metadata:
           name: python-sandbox-template
           namespace: default
         spec:
           podTemplate:
             metadata:
               labels:
                 sandbox: python-sandbox-example
             spec:
               runtimeClassName: gvisor
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
               - name: python-runtime
                 image: registry.k8s.io/agent-sandbox/python-runtime-sandbox:v0.1.0
                 ports:
                 - containerPort: 8888
                 readinessProbe:
                   httpGet:
                     path: "/"
                     port: 8888
                   initialDelaySeconds: 0
                   periodSeconds: 1
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
               restartPolicy: "OnFailure"
         ---
         apiVersion: extensions.agents.x-k8s.io/v1beta1
         kind: SandboxWarmPool
         metadata:
           name: python-sandbox-warmpool
           namespace: default
         spec:
           replicas: 2
           sandboxTemplateRef:
             name: python-sandbox-template
         

  2. Apply the `SandboxTemplate` and `SandboxWarmPool` manifest:
         
         kubectl apply -f sandbox-template-and-pool.yaml
         

  3. Wait until the warm pool's sandboxes are ready:
         
         kubectl wait sandboxwarmpool python-sandbox-warmpool \
             --for=jsonpath='{.status.readyReplicas}'=2 \
             --timeout=600s
         

Later in this document, the Python client creates a `SandboxClaim` resource. If the client creates the claim before the pool's sandboxes are ready, the controller might create a new sandbox for the claim instead of assigning one from the pool. In an Autopilot cluster, the sandboxes can take several minutes to become ready because GKE might need to create nodes for them.




### Verify the Sandbox Router

The Python client that you will use to create and interact with sandboxed environments uses a component called the Sandbox Router to communicate with the sandboxes.

For this example, you use the client's _developer mode_ for testing. This mode is intended for local development, and uses the command `kubectl port-forward` to establish a direct tunnel from your local machine to the Sandbox Router service running in the cluster. This tunneling approach avoids the need for a public IP address or complex ingress setup, and simplifies interacting with sandboxes from your local environment.

Verify that the Sandbox Router is running in the `agent-sandbox-system` namespace:
    
    
    kubectl get deployment sandbox-router --namespace=agent-sandbox-system
    

When the router is running, the `READY` column shows that all replicas are ready, for example `2/2`. If the command returns a `NotFound` error, deploy the router by following the steps in [Deploy the Sandbox Router](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox#deploy-sandbox-router).

### Install the Python client

Now that the in-cluster components like the Sandbox Router are deployed, the final preparatory step is to install the [Agentic Sandbox Python client](https://pypi.org/project/k8s-agent-sandbox/) on your local machine. Recall that this client is a Python library that lets you programmatically create, use, and delete sandboxes. You use it in the next section to test the environment:

  1. Create and activate a Python virtual environment:
         
         python3 -m venv .venv
         source .venv/bin/activate
         

  2. Install the client package. Use the same version as the Agent Sandbox controller:
         
         pip install k8s-agent-sandbox==1.0.6
         




## Test the sandbox

With all the setup components in place, you can now create and interact with a sandbox using the Agentic Sandbox Python client.

  1. Create a Python script named `test_sandbox.py` with the following content:
         
         from k8s_agent_sandbox import SandboxClient
         from k8s_agent_sandbox.models import SandboxLocalTunnelConnectionConfig
         
         # Tunnels to svc/sandbox-router-svc in the agent-sandbox-system namespace.
         # cleanup=True deletes the sandbox when the script exits.
         client = SandboxClient(
             connection_config=SandboxLocalTunnelConnectionConfig(),
             cleanup=True,
         )
         
         sandbox = client.create_sandbox(warmpool="python-sandbox-warmpool", namespace="default")
         try:
             print(sandbox.commands.run("echo 'Hello from the sandboxed environment!'").stdout)
         except Exception as e:
             print(f"An error occurred: {e}")
         

  2. From your terminal (with the virtual environment still active), run the test script:
         
         python3 test_sandbox.py
         




You should see the message "Hello from the sandboxed environment!" which is output from the sandbox.

Congratulations! You have successfully run a shell command inside a secure sandbox. Using the `sandbox.commands.run()` method, you can execute any shell command, and Agent Sandbox on GKE runs the command within a secure barrier that protects your cluster's nodes and other workloads from untrusted code. This provides a safe and reliable way for an AI agent or any automated workflow to execute tasks.

When you run the script, the `SandboxClient` handles all the steps for you. It creates the `SandboxClaim` resource to start the sandbox, waits for the sandbox to be ready, and then uses the `sandbox.commands.run()` method to execute bash shell commands inside the secure container. The client then captures and prints the `stdout` from that command. Because the script sets the `cleanup` parameter to `True`, the client deletes the sandbox when the program exits.

When a `SandboxClaim` resource is created, an available sandbox from the warm pool is assigned to the claim and the claim is marked ready. The `SandboxWarmPool` resource then automatically replenishes itself to maintain the configured number of replicas.

To verify if a specific sandbox is claimed or available, check the `ownerReferences` in the `Sandbox` resource's metadata. If the value of the `kind` field is `SandboxClaim`, the sandbox is in use. If the value of the `kind` field is `SandboxWarmPool`, the sandbox is idle and waiting to be claimed.

## Run sandboxes in production

In this document, you interact with sandboxes from outside of the cluster by using Cloud Shell. The Python client uses your user credentials to authenticate to the cluster and manage sandbox resources, and uses the `kubectl port-forward` command to establish a connection with sandboxes. These steps work well for development scenarios.

In a production scenario, a controller application (like an AI orchestrator) is responsible for creating and managing sandbox resources. To use Agent Sandbox on GKE in production, consider the following:

  * **Authentication** : your controller application must authenticate to the cluster API server to run sandboxes. How you configure authentication depends on where the controller application runs, as follows:

    * If the controller application runs as a Pod in the same cluster, use [Kubernetes RBAC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control) or [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) with IAM policies to grant the Pod's Kubernetes ServiceAccount the necessary permissions to watch sandboxes or discover network endpoints.
    * If the controller application runs outside of the cluster, use [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation), or IAM service accounts to give the application an identity that you can reference in allow policies.
  * **Routing** : requests from the Python client in your controller application must reach the Sandbox Router in your cluster. In production, use one of the following methods to establish a network connection:

    * If the controller application runs in the same cluster, use the `SandboxDirectConnectionConfig` function to target the URL and port that the Sandbox Router service uses.
    * If the controller application runs outside of the cluster, use the [GKE Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api) to create an internal or external load balancer. In your client code, use the `SandboxGatewayConnectionConfig` function to reference your Gateway.

For more information about these routing methods, see the [usage examples on GitHub](https://github.com/kubernetes-sigs/agent-sandbox/blob/v1.0.6/clients/python/agentic-sandbox-client/README.md#usage-examples) and the [Gateway deployment steps for the router](https://github.com/kubernetes-sigs/agent-sandbox/blob/v1.0.6/sandbox-router/deploy/README.md).

  * **Sandbox access to Google Cloud resources** : if your sandbox code needs to send requests to Google Cloud APIs, such as Cloud Storage, use an IAM policy with [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to give the Kubernetes ServiceAccount that the sandbox Pod uses the permissions that are required for that access. Because the default network policy blocks access to the Google Cloud metadata server (`169.254.169.254`), you must customize the network policy to allow this traffic.

  * **Network Policy restrictions** : by default, Agent Sandbox on GKE enforces a strict _Secure-by-Default_ network posture (`networkPolicyManagement: Managed`). The following restrictions apply under this posture:

    * **Ingress** is blocked from all sources except the designated Sandbox Router (Pods that have the `app: sandbox-router` label in the `agent-sandbox-system` namespace).
    * **Egress** is allowed to the public internet, but egress to private LAN ranges (RFC 1918), internal cluster DNS (CoreDNS), and the Cloud Provider Metadata Server (`169.254.0.0/16`) is explicitly blocked.

To use Workload Identity Federation for GKE or access other private resources, you must define custom network policies in the `SandboxTemplate` resource. For detailed configuration details and customizable templates (such as air-gapped sandboxes or Workload Identity Federation for GKE integration), see [Agent Sandbox Network Policy Management](https://github.com/kubernetes-sigs/agent-sandbox/blob/v1.0.6/examples/policy/network-policy-management/README.md).




## Sandbox security policies

By default, Agent Sandbox on GKE doesn't apply security policies to sandboxes. To help enforce isolation settings for your sandboxes, apply the recommended `secure-sandbox-policy` Kubernetes Validating Admission Policy (VAP) from the Agent Sandbox GitHub repository. For instructions, see [Apply the recommended security policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox#apply-security-policy).

The policy enforces isolation requirements, such as requiring gVisor, disabling `hostNetwork`, and blocking `hostPath` volumes. The policy also enforces hardening requirements, such as dropping all capabilities, preventing the addition of new capabilities, and requiring containers to run as non-root and to set resource limits. For the full list of requirements, see [Agent Sandbox on GKE deployment requirements](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox#deployment-requirements).

### Modify or remove policy constraints

Because you apply the policy yourself, you can change it to fit your workloads. If your workloads require exemptions from some of the rules, you can modify the policy to remove specific constraints or delete the policy binding entirely. Removing a constraint reduces the isolation that the policy provides, so remove only the constraints that your workloads require.

To modify the policy and remove a specific constraint (for example, to allow containers to run as root or omit resource limits), edit the `ValidatingAdmissionPolicy` resource:
    
    
    kubectl edit validatingadmissionpolicy secure-sandbox-policy
    

In the text editor that opens, locate the `validations` section and remove or modify the constraint expression that blocks your workload.

Alternatively, if you want to stop enforcing the policy in your cluster, delete the policy binding:
    
    
    kubectl delete validatingadmissionpolicybinding secure-sandbox-binding
    

## Known issues

This section describes known issues when using Agent Sandbox on GKE, and how to resolve or work around them.

### Security policy blocks capabilities when using a service mesh

If you applied the [recommended security policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox#apply-security-policy) and you attempt to deploy a sandbox that integrates with a service mesh sidecar (for example, Envoy or Istio), the creation of the sandbox might be blocked by the policy with an error like the following:
    
    
    sandbox create error: sandboxes.agents.x-k8s.io "claude-cli-claim-managed" is forbidden:
    ValidatingAdmissionPolicy 'secure-sandbox-policy' with binding 'secure-sandbox-binding'
    denied request: Security Violation: Capabilities.add must be empty. You cannot add capabilities.
    

  * **Cause** : Service mesh sidecars often use an init container, such as `istio-init` or `proxy-init`. These init containers require capabilities like `NET_ADMIN` or `NET_RAW` to configure `iptables` rules for transparent egress routing. The `secure-sandbox-policy` ValidatingAdmissionPolicy blocks all capability additions in all container types.
  * **Workaround** : because you manage this policy in your cluster, you can modify the `ValidatingAdmissionPolicy` to allow specific trusted init containers to request `NET_ADMIN` and `NET_RAW` capabilities. For instructions about how to modify or remove policy constraints, see Modify or remove policy constraints. For example, you can update the policy's validation expressions or variables to exempt trusted container names from the capabilities rule.



### Egress latency or timeout when connecting to Google APIs over IPv6

Workloads inside the sandbox might experience connection timeouts or high latency, as high as two minutes, when attempting to connect to external resources or Google APIs (such as Vertex AI or Cloud Storage).

  * **Cause** : if your GKE cluster has dual-stack IPv6 enabled, DNS resolution for Google APIs returns both IPv4 (A) and IPv6 (AAAA) addresses. Some algorithms in runtime engines, such as Node.js, attempt to connect over IPv6 first. If your GKE VPC doesn't have a valid IPv6 egress route, such as a Cloud NAT or an internet gateway for IPv6, the TCP connection stops responding until the TCP SYN timeout expires. Then, the TCP connection falls back to IPv4.
  * **Resolution** : to resolve this issue, do one of the following:

    * **Configure IPv6 egress** : to allow outbound IPv6 traffic to return to the cluster, configure a valid IPv6 Cloud NAT or internet gateway in your VPC network.
    * **Prefer IPv4 in the workload** : to prefer IPv4 DNS resolution, configure your workload's runtime. For example, in a Node.js application, you can set the following environment variables in your `SandboxTemplate` definition:
          
          env:
          - name: NODE_OPTIONS
            value: "--dns-result-order=ipv4first --no-network-family-autoselection"
          




## Clean up resources

To avoid incurring charges to your Google Cloud account, you should delete the GKE cluster that you created:
    
    
    gcloud container clusters delete ${CLUSTER_NAME} \
        --location=${LOCATION} \
        --quiet
    

## What's next

  * Learn how to [Save and restore Agent Sandbox on GKE environments with Pod snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox-pod-snapshots).
  * Learn more about the Agent Sandbox open-source project on [GitHub](https://github.com/kubernetes-sigs/agent-sandbox).
  * Learn how to use open source [Kata Containers with Agent Sandbox on GKE](https://github.com/kubernetes-sigs/agent-sandbox/tree/v1.0.6/examples/kata-gke-sandbox). Kata Containers isn't a Google Cloud product. If you install and use this software, then you're responsible for management and troubleshooting. Google's support and SLAs don't apply to Kata Containers.
  * To understand the underlying technology that provides security isolation for your workloads, see [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods).
  * For more information about enhancing security for your clusters and workloads, see [GKE security overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/kubernetes-engine/ai-ml/install-overview-substrate/
title: Install Agent Substrate on GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T23:41:21.908515+00:00
---

# Install Agent Substrate on GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/ai-ml/install-overview-substrate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Install Agent Substrate on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

[Agent Substrate on GKE](https://docs.cloud.google.com/kubernetes-engine/ai-ml/about-agent-substrate) runs agentic workloads efficiently on GKE clusters: your application suspends idle agents, and the system restores them when they need to act again. Agent Substrate on GKE is open source software that you can install onto a GKE Standard cluster. To compare Agent Substrate on GKE with Agent Sandbox on GKE and choose an architecture for your AI agent workloads, see [Plan an architecture for AI agent workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-workloads).

This document helps you prepare your Google Cloud project and GKE cluster for Agent Substrate on GKE, explains how to run the installer, and describes the resources that the installation creates.

## Pricing

Agent Substrate on GKE is offered at no extra charge. [GKE pricing](https://cloud.google.com/kubernetes-engine/pricing) applies to the resources that you create.

## Limitations

Agent Substrate on GKE has the following installation limitations:

  * **Cloud Shell** : you can't install Agent Substrate on GKE in Cloud Shell because Cloud Shell provides 5 GB of persistent disk storage, which is insufficient for the installation. You must run the installer on your local machine.
  * **Cluster mode** : you can install Agent Substrate on GKE only in GKE Standard clusters. Autopilot clusters aren't supported.
  * **Cluster version** : both the control plane and the node pools in your cluster must run GKE version 1.37 or later. Versions earlier than 1.37 aren't supported.
  * **Release channel** : you can't install Agent Substrate on GKE in clusters that are enrolled in the Extended release channel. The installer enables Kubernetes beta APIs in your cluster, and the Extended channel [doesn't support explicitly enabled beta APIs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#limitations-for-extended).
  * **Machine types** : you can't use machine series that run on mixed CPU architectures (such as E2 machine types).



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * [Install the following components in the gcloud CLI](https://docs.cloud.google.com/sdk/docs/components#installing_components): 
    * `kubectl`
    * `gke-gcloud-auth-plugin`
  * Ensure that the following tools are installed on your local machine: 
    * [Git](https://git-scm.com/downloads) to clone the Agent Substrate repository.
    * [Go](https://go.dev/doc/install) to run the installer's programs, which are distributed as source code.
    * `make` to start the installer.
    * [Docker](https://docs.docker.com/engine/install/) and its [Buildx plugin](https://docs.docker.com/build/concepts/overview/#buildx) to build the Agent Substrate on GKE container images.
    * `sha256sum`, `zstd`, `unzip`, and `jq` to set up the microVM runtime, if you plan to use it. The installer doesn't offer the microVM runtime if any of these tools is missing.
  * To let the installer push the images that it builds, configure Docker to authenticate to Artifact Registry in the region of your cluster:
        
        gcloud auth configure-docker REGION-docker.pkg.dev
        

Replace `REGION` with the region of your cluster, such as `us-west1`. For more information, see [Configure authentication to Artifact Registry for Docker](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication#gcloud-helper).

  * Because the installer acts on your behalf to enable APIs and provision resources, set up Application Default Credentials (ADC) by running the following command:
        
        gcloud auth application-default login
        

For more information about authenticating with ADC, see [Set up Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc).




### Required roles

To get the permissions that you need to install Agent Substrate on GKE, ask your administrator to grant you the following IAM roles on your project: 

  * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)
  * [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`)
  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)
  * [Artifact Registry Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`)
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
  * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
  * [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Cluster requirements

If you let the installer create a cluster for you, it automatically configures a cluster that meets all requirements for Agent Substrate on GKE.

If you choose instead to install Agent Substrate on GKE in an existing cluster, that cluster must meet the following requirements:

  * Runs on GKE Standard (Agent Substrate on GKE is supported on Standard clusters only).
  * Runs GKE version 1.37 or later on both the control plane and the node pools. If the control plane runs an earlier version, [upgrade the control plane](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrading_the_cluster) first. Then [upgrade any node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrading-nodes) that run an earlier version so that the nodes can mount Pod certificates into Pods.
  * Isn't enrolled in the Extended release channel. For more information, see Limitations.
  * Uses [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2).
  * Uses `c3-standard-4` or larger machine types for nodes.
  * If you plan to run more than approximately 800 concurrent sandboxes per node, the cluster uses nodes that have higher limits in the Linux kernel for file system monitoring (inotify) and for the neighbor table of the Address Resolution Protocol (ARP). Without these higher limits, sandboxes can fail to start and networking can stall. The nodes need the following kernel settings:

    * `net.ipv4.neigh.default.gc_thresh1`: `4096`
    * `net.ipv4.neigh.default.gc_thresh2`: `16384`
    * `net.ipv4.neigh.default.gc_thresh3`: `32768`
    * `fs.inotify.max_user_instances`: `65536`
    * `fs.inotify.max_user_watches`: `1048576`

The installer applies these settings automatically only to clusters that it creates. To apply these settings to node pools in an existing cluster, use a node system configuration. For more information, see [Sysctl configuration options](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#sysctl-options).




## Install Agent Substrate on GKE

To install Agent Substrate on GKE, run one of the following commands in your local terminal:

  * To install for your own workloads, run the following command:
        
        curl -sSL https://raw.githubusercontent.com/ai-on-gke/substrate-gke/main/install.sh | bash
        

  * To install and then try the Counter demo, run the following command:
        
        curl -sSL https://raw.githubusercontent.com/ai-on-gke/substrate-gke/main/install.sh | bash -s -- --demo
        




The interactive installer prompts you for your container images and for your project, cluster, storage, and ingress settings. The installer suggests recommended defaults where possible, which you can accept or customize:

  * **Container images (required)** : when the installer asks you to choose your images, select **Build from source**. The installer builds the images from the upstream [Agent Substrate repository](https://github.com/agent-substrate/substrate) and pushes them to an Artifact Registry repository in your project. By default, the installer builds the latest version of Agent Substrate. To build a different version, enter a branch, a tag, or a full commit SHA from the upstream repository.
  * **Project ID (required)** : specify the Google Cloud project where resources will be provisioned. If you configured a default project for the gcloud CLI, then the installer uses that project ID.
  * **Cluster (required)** : choose whether to let the installer create a new GKE cluster with recommended defaults or to install Agent Substrate on GKE in an existing cluster. If you choose to install on an existing cluster, verify that it meets the requirements in the Cluster requirements section.
  * **Snapshot bucket (optional)** : specify a custom Cloud Storage bucket name, or leave it blank to let the installer create a default bucket named `ate-snapshots-<project>-<cluster>-<zone>`. Because the default name includes the cluster name, clusters in the same project and zone don't share a bucket. A custom name can have at most 56 characters, because the installer also creates an asset bucket by adding the `-assets` suffix to the name, and bucket names can have at most 63 characters. If the default name is longer than 56 characters, the installer shortens it and appends a hash.
  * **Ingress clients (required)** : enter the SPIFFE IDs of the workloads that send requests to your Actors, such as the frontend or backend service of your application. A SPIFFE ID identifies a workload by the namespace and the Kubernetes service account that its Pods run as. For example, Pods that run in the `shop` namespace as the `frontend` service account have the SPIFFE ID `spiffe://cluster.local/ns/shop/sa/frontend`. Because the ID depends only on the namespace and the service account, you can enter IDs for clients that you haven't deployed yet. Separate multiple IDs with commas. Requests reach your Actors through an ingress router, which admits only clients that present a Pod certificate whose SPIFFE ID is on this list. Any client on the list can reach any Actor. If you include the `--demo` flag, the installer allows only the Pods of the Counter demo instead of asking for IDs. To add clients after the installation, see [Reaching actors through the ingress router](https://github.com/ai-on-gke/substrate-gke#reaching-actors-through-the-ingress-router) in the `substrate-gke` README.



### What the installer does

The installer executes the following programs on your behalf:

  * `setup-gcp`: creates or verifies the required Google Cloud resources, enables APIs, creates the GKE cluster (if you chose not to use an existing cluster) and Cloud Storage bucket, and configures IAM policies.
  * `ate-setup`: deploys the Agent Substrate on GKE container images and controllers onto your GKE cluster.



First, the installer makes the following changes to your Google Cloud project:

  1. Enables the Google Cloud APIs that Agent Substrate on GKE needs.
  2. Creates a GKE Standard cluster (if not using an existing cluster) that runs version 1.37 or later and has the following settings: 
     * **Workload Identity Federation for GKE** : allows Agent Substrate on GKE to access Cloud Storage without storing keys on the nodes.
     * **GKE Dataplane V2** : handles the networking required to route incoming requests to your agents.
     * **Managed OpenTelemetry** : collects metrics and traces from your cluster.
  3. Creates the Cloud Storage buckets that Agent Substrate on GKE uses: one for your snapshots, and one for the files that the microVM runtime needs. The name of the second bucket is the name of the snapshot bucket followed by the `-assets` suffix.
  4. Creates an Artifact Registry repository named `ate-images` for the container images that the installer builds.
  5. Creates a service account named `ate-snapshot-transfer` that Agent Substrate on GKE uses to transfer snapshots.
  6. Grants the GKE nodes, the Agent Substrate on GKE components, and the `ate-snapshot-transfer` service account the IAM permissions that they need to access the buckets and the container images.
  7. Creates Cloud Monitoring dashboards that chart Agent Substrate on GKE routing latency, snapshot size, and gRPC traffic.



Next, the installer makes the following changes to your cluster:

  1. Adds the Agent Substrate on GKE Kubernetes custom resources to your cluster, such as `WorkerPool` (which defines how many idle sandboxes stay ready) and `SandboxConfig` (which defines a sandbox runtime). Other Agent Substrate on GKE resources, such as `ActorTemplate` (which defines the container images and resources your agents use) and Actors, aren't Kubernetes resources. You manage them through the Agent Substrate on GKE API by using the `kubectl ate` plugin, a `kubectl` plugin for managing Actors and Workers. To install the plugin, see Install the `kubectl ate` plugin.
  2. Sets up the certificate authorities that issue the certificates identifying Agent Substrate on GKE components and your Actors. Components present these certificates to authenticate to each other using mTLS.
  3. Deploys Agent Substrate on GKE components to your cluster, along with a PostgreSQL database that tracks the state of your Actors and Workers. The database stores its data on a 500 GiB persistent disk. The installer waits for the database and all control plane Pods to become ready. For production clusters, you can isolate the PostgreSQL database and system infrastructure components onto dedicated node pools before running the installer. For instructions, see [Isolate system infrastructure and worker node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/design-substrate-infrastructure#isolate-node-pools).



Agent Substrate on GKE deploys its components as ordinary workloads within the `ate-system` and `podcertificate-controller-system` namespaces. If you install in an existing cluster, the installer also updates the cluster to turn on the following features if they're off: Workload Identity Federation for GKE, Managed OpenTelemetry, and the beta versions of the `podcertificaterequests` and `clustertrustbundles` Kubernetes APIs. Turning on the beta APIs updates the GKE control plane, which takes about 10 minutes.

The components that get deployed include the gVisor-based runtime that Agent Substrate on GKE uses by default to isolate each of your agents from the node it runs on. If you choose the microVM runtime during the optional steps, the installer also uploads the files that the microVM runtime needs to Cloud Storage and applies a cluster-wide `SandboxConfig` resource named `microvm` that points to those files.

Workers that use the microVM runtime need nodes that can run virtual machines. When the installer creates a cluster, the node pool that it creates has [nested virtualization](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nested-virtualization) enabled. If you choose the **Advanced** setup and change the machine type, choose a [machine series that supports nested virtualization](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison), such as C3, C4, N2, or N4.

If you install Agent Substrate on GKE in an existing cluster, the installer doesn't add node pools to the cluster. To use the microVM runtime, the cluster needs a node pool that has nested virtualization enabled or that uses an x86 bare-metal machine type. You can enable nested virtualization only when you create a node pool. If the cluster has no such node pool, the installer warns you when you choose the microVM runtime. If you continue, microVM Workers stay in the `Pending` state. For more information about how to configure these node pools, including taints, see [Sandbox runtimes](https://github.com/ai-on-gke/substrate-gke#sandbox-runtimes) in the `substrate-gke` README.

If the installation fails at any point (for example, due to a transient network error or token expiration), rerun the command. The installer preserves existing resources and resumes from where it left off.

To upgrade an existing installation of Agent Substrate on GKE, run the installer and select **Upgrade an installed cluster**. This option doesn't change your cluster. Instead, the installer downloads the source code of the installed version and of the version that you upgrade to, and prepares the `~/ate-upgrade` directory that the upgrade runbook uses. To perform the upgrade, run the command that the installer prints, and then follow the [upgrade runbook](https://github.com/agent-substrate/substrate/blob/main/docs/guides/upgrade.md) in the upstream Agent Substrate repository from the first step. The runbook supports upgrades to a later patch release of the same minor version and, for version 1.0 and later, to the next minor version. For versions earlier than 1.0, moving to a later minor version requires a reinstall. For details, see [Upgrading an installed cluster](https://github.com/ai-on-gke/substrate-gke#upgrading-an-installed-cluster) in the `substrate-gke` README.

### Optional steps

After deploying the core components, the installer offers the following optional steps:

  * **Filestore CSI driver** : installs the [Filestore CSI driver](https://docs.cloud.google.com/filestore/docs/filestore-for-gke) configured for Agent Substrate on GKE. Choose this option if your agents need persistent storage that stays available when an agent resumes on a different node. Each agent gets its own storage, which isn't shared with other agents. Production support for Filestore agent volumes is limited GA, so you need to request access. For details, see [Use Filestore agent volumes with Agent Substrate on GKE](https://docs.cloud.google.com/filestore/docs/agent-substrate). If your cluster has the managed GKE Filestore add-on enabled, the installer disables it before deploying the driver. The installer deploys the driver in the `gcp-filestore-csi-driver` namespace and creates a service account named `substrate-filestore-csi`, which has the IAM permissions that the driver needs.
  * **Node pool autoscaling** : enables GKE [cluster autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) on your node pool. You specify the minimum and maximum number of nodes for the pool. Choose this option if you want GKE to automatically add nodes during demand surges and remove nodes when agents are suspended. Skip this option if you prefer a fixed node count with predictable compute costs. To configure automated hardware fallback with custom ComputeClasses, standby capacity buffers, and scale-down protections for active Actors, see [Design your infrastructure for Agent Substrate on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/design-substrate-infrastructure).
  * **Sandbox runtime** : lets you choose the runtime that isolates your agents. The installer installs the gVisor runtime as part of the core components, so the gVisor runtime needs no extra configuration. If you want isolation that uses hardware virtualization, choose the microVM runtime. Before you choose this option for an existing cluster, make sure that the cluster has a node pool that has nested virtualization enabled or that uses an x86 bare-metal machine type. For details, see What the installer does.
  * **Counter demo** : deploys an example workload that demonstrates agent suspension and restoration. This step appears only if you include the `--demo` flag when you start the installer. Choose this option if you want to test the cluster after installation. For details, see Try the Counter demo.



## Verify the installation

To verify that the installation succeeded and the core components are running, run the following commands and ensure that all Pods have a status of `Running`:
    
    
    kubectl get pods -n ate-system
    kubectl get pods -n podcertificate-controller-system
    

## Install the `kubectl ate` plugin

To manage Actors and `ActorTemplate` resources, install the `kubectl ate` plugin from the source code of the Agent Substrate version that you installed:
    
    
    git clone --depth 1 --branch VERSION https://github.com/agent-substrate/substrate.git
    cd substrate
    go install ./cmd/kubectl-ate
    

Replace `VERSION` with the Agent Substrate version that you installed, such as `v1.0.0`, the installer's default version.

The `go install` command places the plugin in the `bin` directory of your Go workspace. The `kubectl` tool finds the plugin only if that directory is in your `PATH` environment variable. If your `PATH` environment variable doesn't include that directory, add it before you run any `kubectl ate` commands:
    
    
    export PATH="$PATH:$(go env GOPATH)/bin"
    

## Try the Counter demo

If you included the `--demo` flag when you ran the installer and chose to deploy the Counter demo, the installer deploys a `WorkerPool` and an `ActorTemplate` for a web server that counts requests in memory and in a file. Agent Substrate on GKE preserves both counts when you suspend and restore the Actor that runs the server.

After the installation, the installer prints the next steps of the demo: a command that installs the `kubectl ate` plugin, and a command that creates an Actor from the `ActorTemplate`. Before you run `kubectl ate` commands, make sure that the plugin is in your `PATH` environment variable, as described in Install the `kubectl ate` plugin.

The installer doesn't print a command that sends requests to the Actor. The ingress router admits only clients that present a Pod certificate whose SPIFFE ID is on its allowlist, so it refuses requests that you send directly from your local machine. For more information about the demo, see the [Counter demo README](https://github.com/agent-substrate/substrate/blob/release-1.0/demos/counter/README.md) for version 1.0.0 of Agent Substrate, which the installer deploys by default. In a cluster that the installer set up, the README's steps that send requests through a port forward don't work, for the same reason.

## Uninstall Agent Substrate on GKE

When the installation completes and exits, the installer prints customized cleanup commands for your environment.

To remove resources created during installation, choose one of the following options:

  * **Remove Agent Substrate on GKE from an existing cluster** : if you installed on an existing cluster and want to retain the cluster and its other workloads, delete only the Agent Substrate on GKE components by running the `ate-setup delete ate-system` command that the installer prints. The installer pre-populates this command with the project, cluster, and location values configured during installation.

  * **Delete all resources (including the cluster)** : to delete the GKE cluster, the snapshot and asset buckets, the `ate-snapshot-transfer` service account, IAM bindings, dashboards, and the `ate-images` Artifact Registry repository, run the `cleanup-gcp` command that the installer prints. The installer pre-populates this command with the project, cluster, location, and bucket values configured during installation. Because the command runs the `tools/cleanup-gcp` script by using a relative path, run the command from the directory where the installer cloned the `substrate-gke` repository. By default, the installer clones the repository into the `~/.substrate-gke` directory.

If other clusters in the project run Agent Substrate on GKE, add the `--cluster-scoped` flag to the command. This flag keeps the dashboards, the `ate-snapshot-transfer` service account, and the project-level IAM bindings, which those clusters share. The `--cluster-scoped` flag doesn't keep the `ate-images` repository. If other clusters in the same region use the `ate-images` repository, also add the `--keep-repository` flag to the end of the command. For details, see the "Tearing down" section of the [substrate-gke README](https://github.com/ai-on-gke/substrate-gke#tearing-down).




The `cleanup-gcp` command doesn't delete the following resources:

  * **The persistent disk of the PostgreSQL database** : GKE [keeps persistent disks when it deletes a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#persistent-storage-cluster-deletion), so you continue to pay for the 500 GiB disk. To delete the disk, run the `ate-setup delete ate-system` command that the installer prints. Then, wait until the `kubectl get pv` command no longer lists a volume for the `ate-system/data-postgres-0` claim before you run `cleanup-gcp`. If you already deleted the cluster, find the disk by running the following command, and then delete the disk by running the `gcloud compute disks delete` command:
        
        gcloud compute disks list --filter="description~data-postgres-0"
        

  * **The`substrate-filestore-csi` service account**: all the clusters in the project that run the Filestore CSI driver share this service account. If you installed the driver and no other clusters in the project run the driver, delete the service account by running the following command:
        
        gcloud iam service-accounts delete substrate-filestore-csi@PROJECT_ID.iam.gserviceaccount.com
        

Replace `PROJECT_ID` with your project ID.




## What's next

  * To learn more about Agent Substrate on GKE, see [About Agent Substrate on GKE](https://docs.cloud.google.com/kubernetes-engine/ai-ml/about-agent-substrate).
  * To right-size your cluster for production scale, isolate system node pools, and configure custom ComputeClasses and capacity buffers, see [Design your infrastructure for Agent Substrate on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/design-substrate-infrastructure).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 

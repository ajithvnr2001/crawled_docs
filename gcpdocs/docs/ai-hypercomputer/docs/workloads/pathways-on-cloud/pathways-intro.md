---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-intro/
title: Introduction to Pathways on Cloud \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T10:16:13.400284+00:00
---

# Introduction to Pathways on Cloud  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-intro/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Introduction to Pathways on Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Pathways is a system designed to enable the creation of large-scale, multi-task, and sparsely activated machine learning (ML) systems. It lets you use thousands or tens of thousands of accelerators, with the ability to dynamically allocate varying amounts of compute for different tasks based on their processing requirements.

Pathways simplifies large-scale ML computations by enabling a single JAX client to orchestrate workloads across large TPU slices, potentially spanning thousands of TPU chips.

Google uses Pathways internally to train large models such as Gemini. Pathways on Cloud brings the same benefits to Google Cloud customers.

## Before you begin

  * Select the tab for how you plan to use the samples on this page:

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Before you begin

You can run Pathways on Google Kubernetes Engine (GKE) or on a [Cluster Director](https://cloud.google.com/products/cluster-director) cluster with Slurm. Select the tab for your platform.

###  GKE 

Complete the following prerequisites:

  * [Install Kubernetes tools](https://kubernetes.io/docs/tasks/tools/).
  * [Install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  * [Enable the Kubernetes Engine API](https://console.cloud.google.com/flows/enableapi?apiid=container.googleapis.com).



This document provides an overview of how to use Pathways-managed TPUs on GKE for batch, real-time, and interactive workloads. It assumes that you're already familiar with using [TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#type-node-pool), including both single-slice and [multislice TPUs on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpu-multislice), and have general experience with [multislice TPUs](https://docs.cloud.google.com/tpu/docs/multislice-introduction).

###  Cluster Director 

Complete the following prerequisites:

  * [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  * [Enable the Hypercompute Cluster API](https://console.cloud.google.com/flows/enableapi?apiid=hypercomputecluster.googleapis.com).



This document provides an overview of how to use Pathways with TPUs on a Cluster Director cluster for batch and interactive workloads. It assumes that you're already familiar with [Cluster Director](https://docs.cloud.google.com/cluster-director/docs/overview), [TPU machines in Cluster Director](https://docs.cloud.google.com/cluster-director/docs/tpu-machines), and running jobs with [Slurm](https://docs.cloud.google.com/cluster-director/docs/orchestration), and have general experience with [multislice TPUs](https://docs.cloud.google.com/tpu/docs/multislice-introduction).

To create a cluster, see [Create a Cluster Director cluster with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-cluster-director-cluster).

## Single controller and multi-controller

There are two primary ways to manage and orchestrate computations across multiple devices:

Feature | Single-controller (Pathways) | Multi-controller (JAX default)  
---|---|---  
**Control** | Single point of control: A single client program acts as the central controller. | Distributed control: Multiple processes participate, each with its own Python interpreter instance.  
**View** | Unified view: The client sees all devices as a single, unified system. | Localized view: Each Python process sees only the devices connected to it.  
**Programming** | Simplified programming: You interact with a single client, making the system appear as a single large machine with many local accelerators. | Single program, multiple data (SPMD): Primarily uses the SPMD paradigm, requiring all devices to run the same program.  
**Flexibility** | Supports complex computation patterns beyond SPMD, including asymmetrical pipeline parallelism and computational sparsity. | Can be less flexible in resource management, especially across different TPU slices.  
  
## Pathways components

The following sections outline the main components of the Pathways architecture.

### Pathways resource manager

This component is the central control plane of the Pathways system. It manages all accelerator resources and coordinates the allocation of accelerators for your jobs. It monitors the health of workers and handles job scheduling, pausing, and resuming. It serves as a single point of contact for errors and system status. This component requires only CPU resources.

### Pathways client

This component is an implementation of the [Interim Framework Runtime (IFRT)](https://github.com/openxla/xla/blob/main/xla/python/ifrt/README.md) that serves as the entry point into the Pathways system. It receives High-Level Operations (HLOs) from your program. The Pathways client coordinates with the Pathways resource manager to determine where to place compiled programs for execution based on your code. It presents a unified view of the system to a given JAX client. This component requires only CPU resources.

### Pathways worker

Pathways worker processes run on the accelerator machines (TPU VMs). They receive compiled executables of your program from the IFRT proxy server and perform the computations on the TPUs. Pathways workers send data back to your program over the IFRT proxy server. This component requires accelerator resources.

### IFRT proxy client

The IFRT proxy client is an open-source implementation of the [Interim Framework Runtime (IFRT)](https://github.com/openxla/xla/blob/main/xla/python/ifrt/README.md) API that decouples user code from the underlying runtime and enhances code portability and transparency. JAX uses this implementation as an alternative to its default multi-controller runtime. The IFRT proxy client acts as a communication bridge between your program and the Pathways components. It sends requests to the IFRT proxy server and receives results from it. This component requires only CPU resources.

### IFRT proxy server

The IFRT proxy server is a [gRPC](https://grpc.io/) server receives requests from the IFRT proxy client and forwards them to the Pathways client, which handles the distribution of work. This component requires only CPU resources.

### Sidecar server

The sidecar server is a [gRPC](https://grpc.io/) server that is co-located with the Pathways worker on the accelerator VM. It runs user-specified Python code directly on the accelerator VM to reduce data-transfer latency between the controller and accelerators. The sidecar server interacts with the Pathways worker over a custom versioned protocol on the gRPC transport.

[ ![Architecture diagram showing how the JAX client, IFRT proxy,
      Pathways resource manager, and Pathways workers interact.](https://docs.cloud.google.com/ai-hypercomputer/images/pathways-components.png)](https://docs.cloud.google.com/ai-hypercomputer/images/pathways-components.png) Pathways components

## Pathways components on GKE

This section maps Pathways components to GKE components such as containers and Pods.

You can find Pathways container images at the following locations:

Container type | Location  
---|---  
IFRT proxy server | `us-docker.pkg.dev/cloud-tpu-v2-images/cloud-pathways/proxy_server:jax-JAX_VERSION`  
Pathways resource manager/worker | `us-docker.pkg.dev/cloud-tpu-v2-images/cloud-pathways/server:jax-JAX_VERSION`  
  
### Pathways resource manager

After you [create a GKE cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-gke-cluster), you can use the following `containerSpec` to deploy the Pathways resource manager:
    
    
      - name: pathways-rm
        image: us-docker.pkg.dev/cloud-tpu-v2-images/cloud-pathways/server:latest
        imagePullPolicy: Always
        env:
        - name: HOST_ADDRESS
          valueFrom:
            fieldRef:
              fieldPath: "metadata.labels['jobset.sigs.k8s.io/coordinator']"
        - name: TPU_SKIP_MDS_QUERY
          value: "true"
        args:
        - --server_port=29001
        - --node_type=resource_manager
        - --instance_count=WORKLOAD_NODEPOOL_COUNT
        - --instance_type=SLICE_TOPOLOGY
        - --gcs_scratch_location=gs://BUCKET_NAME

The container uses the following arguments:

  * `--server_port`: the port that the Pathways resource manager uses to communicate with other Pathways components.
  * `--node_type`: the node type. Set this argument to `resource_manager` for the Pathways resource manager; it isn't needed for the other containers.
  * `--instance_count`: the number of TPU slices.
  * `--instance_type`: the TPU type and topology of the slice, in the format `tpuTPU_TYPE:TOPOLOGY`—for example, `tpuv5e:4x4`.
  * `--gcs_scratch_location`: a Cloud Storage bucket used for temporary files.



### IFRT proxy server

You can use the following `containerSpec` to deploy an IFRT proxy server:
    
    
      - name: pathways-proxy
        image: us-docker.pkg.dev/cloud-tpu-v2-images/cloud-pathways/proxy_server:latest
        imagePullPolicy: Always
        env:
        - name: PATHWAYS_HEAD
          valueFrom:
            fieldRef:
              fieldPath: "metadata.labels['jobset.sigs.k8s.io/coordinator']"
        args:
        - --resource_manager_address=$(PATHWAYS_HEAD):29001
        - --server_port=29000
        - --gcs_scratch_location=gs://BUCKET_NAME
        ports:
        - containerPort: 29000

The container uses the following arguments:

  * `--resource_manager_address`: the hostname and port that the proxy server uses to communicate with the Pathways resource manager. The port must match the `--server_port` value used for the Pathways resource manager container.
  * `--server_port`: the port that the IFRT proxy server uses to communicate with the IFRT proxy client.
  * `--gcs_scratch_location`: a Cloud Storage bucket used for temporary files.



### Pathways worker

You can use the following `containerSpec` to deploy Pathways workers:
    
    
    - name: worker
      image: us-docker.pkg.dev/cloud-tpu-v2-images/cloud-pathways/server:latest
      imagePullPolicy: Always
      env:
      - name: PATHWAYS_HEAD
        valueFrom:
          fieldRef:
            fieldPath: "metadata.labels['jobset.sigs.k8s.io/coordinator']"
      - name: MEGASCALE_NUM_SLICES
        valueFrom:
          fieldRef:
            fieldPath: "metadata.labels['jobset.sigs.k8s.io/replicatedjob-replicas']"
      - name: MEGASCALE_SLICE_ID
        valueFrom:
          fieldRef:
            fieldPath: "metadata.labels['jobset.sigs.k8s.io/job-index']"
      - name: MEGASCALE_COORDINATOR_ADDRESS
        value: "$(PATHWAYS_HEAD)"
      args:
      - --server_port=29001
      - --resource_manager_address=$(PATHWAYS_HEAD):29001
      - --gcs_scratch_location=gs://BUCKET_NAME
      ports:
      - containerPort: 29001
      resources:
        limits:
          google.com/tpu: "4"

The container uses the following arguments:

  * `--resource_manager_address`: the hostname and port that the TPU workers use to communicate with the Pathways resource manager. The port must match the `--server_port` value used for the Pathways resource manager container.
  * `--server_port`: the port that the workers use to communicate with the proxy server and Pathways resource manager.
  * `--gcs_scratch_location`: a Cloud Storage bucket used for temporary files.



The Pathways resource manager, IFRT proxy server, and Pathways workers can all have different ports, but in this example, the Pathways resource manager and the Pathways worker share the same port.

## Pathways components on Cluster Director

This section maps Pathways components to Slurm jobs on a Cluster Director cluster.

The Pathways scripts run the Pathways components with Enroot. The `setup_env.sh` script uses the following container images, which match the JAX version (`0.11.1`) of the Python environment that it builds:

Container type | Location  
---|---  
IFRT proxy server | `us-docker.pkg.dev/cloud-tpu-v2-images/pathways/proxy_server:20261103-jax_0.11.1`  
Pathways resource manager/worker | `us-docker.pkg.dev/cloud-tpu-v2-images/pathways/server:20261103-jax_0.11.1`  
  
You start the Pathways components by submitting the `start_pathways.sh` script as the Pathways service job. You don't write the following commands yourself: the scripts derive the arguments from the environment variables that you set when you submit `start_pathways.sh`, such as `SLICE_SHAPE`, `MIN_SLICES`, `MAX_SLICES`, and `GCS_BUCKET`.

### Pathways resource manager

The Pathways service job runs the Pathways resource manager on one CPU node. It runs the following command in the Pathways server container:
    
    
    /pathways/server \
        --server_port=29001 \
        --node_type=resource_manager \
        --instance_type=tpuTPU_TYPE:TOPOLOGY \
        --instance_count=MAX_SLICES \
        --gcs_scratch_location=gs://BUCKET_NAME/pathways-scratch/shared \
        --enable_gcs_olm=false

The command uses the following arguments:

  * `--server_port`: the port that the Pathways resource manager listens on. The IFRT proxy server and the Pathways workers connect to this port.
  * `--node_type`: the node type, `resource_manager`. Only the Pathways resource manager sets this argument.
  * `--instance_type`: the TPU type and topology of each slice, from `SLICE_SHAPE`. For example, `SLICE_SHAPE=2x4` sets `tpuv6e:2x4`.
  * `--instance_count`: the number of TPU slices, from `MAX_SLICES`.
  * `--gcs_scratch_location`: a path in your Cloud Storage bucket, from `GCS_BUCKET`, used for temporary files such as the compilation cache.
  * `--enable_gcs_olm`: whether Pathways creates Cloud Storage object lifecycle rules to clean up old compilation cache entries. The script turns this off because it requires additional permissions on the bucket.



### IFRT proxy server

The Pathways service job runs the IFRT proxy server on the same CPU node as the Pathways resource manager. It runs the following command in the IFRT proxy server container:
    
    
    /pathways/proxy_server \
        --server_port=29000 \
        --resource_manager_address=RM_IP:29001 \
        --gcs_scratch_location=gs://BUCKET_NAME/pathways-scratch/shared \
        --num_elastic_instances=MAX_SLICES

The command uses the following arguments:

  * `--server_port`: the port that the IFRT proxy server listens on. Your JAX program connects to this port.
  * `--resource_manager_address`: the address of the Pathways resource manager. `RM_IP` is the internal IP address of the CPU node.
  * `--gcs_scratch_location`: the same Cloud Storage path as the Pathways resource manager.
  * `--num_elastic_instances`: the number of slices that can be unavailable without stopping the IFRT proxy session, from `MAX_SLICES`. Your workload enforces `MIN_SLICES`.



When at least `MIN_SLICES` slices are running, the service job writes the IFRT proxy server address to `~/pathways/cluster.env`. Your JAX program, the IFRT proxy client, reads this file to connect to Pathways. The JAX program runs as your workload—for example, `run_maxtext.sh`—or in a Jupyter notebook.

### Pathways worker

The Pathways service job submits a Slurm job array (`run_worker_slice.sh`) with one array task for each TPU slice. Each array task runs the following command in the Pathways server container on every TPU VM in its slice:
    
    
    /pathways/server \
        --server_port=29001 \
        --resource_manager_address=RM_IP:29001 \
        --gcs_scratch_location=gs://BUCKET_NAME/pathways-scratch/shared \
        --enable_gcs_olm=false

The command uses the following arguments:

  * `--server_port`: the port that the Pathways worker listens on. The Pathways resource manager and the IFRT proxy server connect to this port.
  * `--resource_manager_address`: the address of the Pathways resource manager, the same as for the IFRT proxy server.
  * `--gcs_scratch_location`, `--enable_gcs_olm`: the same as for the Pathways resource manager.



The script also sets the TPU topology and `MEGASCALE_*` environment variables for each worker from the slice's nodes and the array task index.

If a TPU slice is preempted or fails, Slurm requeues its array task. If you have [passwordless `sudo`](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-cluster-director-cluster#before-you-begin) on the cluster nodes, the service job also powers down the slice's nodes so that Slurm can recreate them. The Pathways resource manager and IFRT proxy server keep running, so your JAX program doesn't need to connect to a new address.

## What's next

  * [Create a GKE cluster with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-gke-cluster)
  * [Create a Cluster Director cluster with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-cluster-director-cluster)
  * [Run a batch workload with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/batch-workload)
  * [Run an interactive workload with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-interactive-mode)
  * [Resilient training with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/resilient-training)
  * [Port JAX workloads to Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/porting-jax-workloads)
  * [Troubleshoot Pathways on Cloud](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/troubleshooting-pathways)
  * [Run workloads with Pathways in Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/run-workloads-pathways)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

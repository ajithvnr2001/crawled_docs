---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/serve-llama-3-1-405b-a4-gke-sglang/
title: Serve Llama 3.1 405B on GKE with PD disaggregation using Dynamo and SGLang on A4 VMs \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:40:07.023792+00:00
---

# Serve Llama 3.1 405B on GKE with PD disaggregation using Dynamo and SGLang on A4 VMs  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/serve-llama-3-1-405b-a4-gke-sglang/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Serve Llama 3.1 405B on GKE with PD disaggregation using Dynamo and SGLang on A4 VMs Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This tutorial shows you how to deploy and serve [Llama 3.1 405B (`nvidia/Llama-3.1-405B-Instruct-FP8`)](https://huggingface.co/nvidia/Llama-3.1-405B-Instruct-FP8), a 405 billion-parameter instruction-tuned model quantized to FP8, on Google Kubernetes Engine (GKE) on Google Cloud. The deployment uses Cluster Toolkit, two [A4 (`a4-highgpu-8g`)](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms) virtual machine (VM) instances with a total of 16 NVIDIA B200 GPUs, [NVIDIA Dynamo](https://github.com/ai-dynamo/dynamo), and the [SGLang serving framework](https://github.com/sgl-project/sglang) with single-host prefill-decode (PD) disaggregation.

In the deployment configuration that's described in this tutorial, you use Cluster Toolkit to provision a GKE cluster in Standard mode. The cluster contains two `a4-highgpu-8g` nodes connected over GPUDirect Remote Direct Memory Access (RDMA) networking. You then install the KAI Scheduler and NVIDIA Dynamo platform with Grove gang scheduling. Finally, you deploy a DynamoGraphDeployment custom resource that separates prefill and decode across two single-host eight-GPU workers with tensor parallelism and an FP8 KV cache.

## Objectives

  * Install Cluster Toolkit and provision a two-node A4 GKE cluster in Standard mode.
  * Install the KAI Scheduler and NVIDIA Dynamo platform with Grove gang scheduling on your cluster.
  * Deploy a PD-disaggregated SGLang inference server with one single-host A4 prefill worker and one single-host A4 decode worker.
  * Send a chat completion request to the Dynamo frontend router.
  * Run a serving benchmark workload.
  * Clean up the deployed resources.



## Costs

In this document, you use the following billable components of Google Cloud:

  * [GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * [Compute Engine](https://docs.cloud.google.com/compute/all-pricing)
  * [Cloud Storage](https://docs.cloud.google.com/storage/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator).

## Before you begin

Set up your environment for the tutorial:

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) and [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the Google Cloud CLI, and install [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl) and [Helm](https://helm.sh/docs/intro/install/) (version 3.10 or later). If you use Cloud Shell, these tools are preinstalled.
  2. If you're running this tutorial from a Linux or macOS workstation rather than Cloud Shell, install the required [Cluster Toolkit dependencies](https://docs.cloud.google.com/cluster-toolkit/docs/setup/install-dependencies), such as Terraform and Git.
  3. Enable the Kubernetes Engine API, Compute Engine API, Cloud Storage API, Identity and Access Management API, Cloud Resource Manager API, and Service Usage API in your Google Cloud project:

[Enable APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,compute.googleapis.com,storage.googleapis.com,iam.googleapis.com,cloudresourcemanager.googleapis.com,serviceusage.googleapis.com)


**Important:** To complete this tutorial, you must have capacity for two A4 (`a4-highgpu-8g`) VMs, which have a total of 16 NVIDIA B200 GPUs, in your Google Cloud project. This tutorial uses a specific reservation, but you can also use Spot VMs or Flex-start VMs if available. To learn more about your options for reserving capacity in AI Hypercomputer, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).

### Get a Hugging Face access token

You need a Hugging Face access token to use this tutorial. You can sign up for a free account at [Hugging Face](http://huggingface.co/login). After you have an account, generate an access token:

  1. On the [Welcome to Hugging Face](https://huggingface.co/welcome) page, click your account avatar and select **Access tokens**.
  2. On the **Access tokens** page, click **Create new token**.
  3. Select the **Read** token type and enter a name for your token.
  4. Your access token is displayed. Save the token in a safe place.



### Required roles

To get the permissions that you need to complete this tutorial, ask your administrator to grant you the following IAM roles on your project: 

  * [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`)
  * [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)
  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
  * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Set up your environment variables

Export the environment variables that you use throughout this tutorial:
    
    
    export PROJECT_ID="YOUR_PROJECT_ID"
    export REGION="YOUR_REGION"
    export ZONE="YOUR_ZONE"
    export CLUSTER_NAME="YOUR_CLUSTER_NAME"
    export RESERVATION_NAME="YOUR_RESERVATION_NAME"
    export GCS_BUCKET="YOUR_BUCKET_NAME"
    export HF_TOKEN="YOUR_HF_TOKEN"
    export CLUSTER_TOOLKIT_VERSION="v1.104.0"
    export DYNAMO_RELEASE_VERSION="1.5.0"
    
    gcloud config set project "${PROJECT_ID}"
    gcloud config set billing/quota_project "${PROJECT_ID}"

Replace the following:

  * `YOUR_PROJECT_ID`: the ID of your Google Cloud project.
  * `YOUR_REGION`: the region where your A4 capacity is located and where you want to deploy your cluster, such as `us-central1`.
  * `YOUR_ZONE`: the zone where your A4 capacity is located, such as `us-central1-b`.
  * `YOUR_CLUSTER_NAME`: the name for your GKE cluster and Cluster Toolkit deployment. Use a name of 20 characters or fewer so that the generated node pool service account ID (`YOUR_CLUSTER_NAME-gke-np-sa`) stays within the 30-character Identity and Access Management (IAM) limit.
  * `YOUR_RESERVATION_NAME`: the name of your A4 reservation.
  * `YOUR_BUCKET_NAME`: a globally unique name for the Cloud Storage bucket that stores the Terraform state for Cluster Toolkit.
  * `YOUR_HF_TOKEN`: your Hugging Face access token.

**Note:** If you use Cloud Shell and your home directory runs low on disk space, you can switch to an ephemeral Cloud Shell session. From the Cloud Shell toolbar, click the **More** menu and select **Ephemeral mode**.

## Create the GKE cluster

Download Cluster Toolkit and provision a GKE cluster in Standard mode with two `a4-highgpu-8g` nodes, GPUDirect RDMA networking, and DRA support:

  1. Sign in to the Google Cloud CLI and generate [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) for Terraform:
         
         gcloud auth login
         gcloud auth application-default login

  2. Download and extract the prebuilt Cluster Toolkit bundle for the version specified in `CLUSTER_TOOLKIT_VERSION` (`v1.104.0`):
         
         TAG="${CLUSTER_TOOLKIT_VERSION:-v1.104.0}"
         OS="linux"
         ARCH="amd64"
         mkdir -p cluster-toolkit && curl -L "https://github.com/GoogleCloudPlatform/cluster-toolkit/releases/download/${TAG}/gcluster_bundle_${OS}_${ARCH}.tgz" | tar -xz -C cluster-toolkit

If you run this command on macOS or on an `arm64` workstation, set `OS="mac"` or `ARCH="arm64"` to match your platform.

  3. To store the Terraform state for your Cluster Toolkit deployment, create a Cloud Storage bucket with object versioning enabled:
         
         gcloud storage buckets create "gs://${GCS_BUCKET}" \
             --default-storage-class=STANDARD \
             --project="${PROJECT_ID}" \
             --location="${REGION}" \
             --uniform-bucket-level-access
         gcloud storage buckets update "gs://${GCS_BUCKET}" --versioning

  4. Create the `cluster-toolkit/examples/gke-a4/gke-a4-deployment.yaml` deployment configuration file for two `a4-highgpu-8g` nodes:
         
         cat <<EOF > cluster-toolkit/examples/gke-a4/gke-a4-deployment.yaml
         terraform_backend_defaults:
           type: gcs
           configuration:
             bucket: ${GCS_BUCKET}
         
         vars:
           project_id: ${PROJECT_ID}
           deployment_name: ${CLUSTER_NAME}
           region: ${REGION}
           zone: ${ZONE}
           static_node_count: 2
           authorized_cidr: 0.0.0.0/0
           reservation_affinity:
             consume_reservation_type: SPECIFIC_RESERVATION
             specific_reservations:
             - name: ${RESERVATION_NAME}
         EOF

By default, the deployment file is configured to consume a [specific reservation](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-consumption-options#reservations). If you don't have a specific reservation, then before you deploy the cluster, you can update `cluster-toolkit/examples/gke-a4/gke-a4-deployment.yaml` to use an alternative consumption option, such as [Spot VMs](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-consumption-options#spot-vms) or [Flex-start VMs](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-consumption-options#dws-flex-start). For configuration instructions, see [GKE consumption options](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-consumption-options).

  5. Change to the `cluster-toolkit` directory, deploy the GKE cluster by using the [`gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy), and then return to your working directory:
         
         cd cluster-toolkit
         ./gcluster deploy \
             -d examples/gke-a4/gke-a4-deployment.yaml \
             examples/gke-a4/gke-a4.yaml \
             --auto-approve -w
         cd ..

Cluster creation takes approximately 20 to 30 minutes. If you run `./gcluster deploy` without the `--auto-approve` flag, then to apply the proposed changes, enter `a` when you're prompted to.

  6. Configure `kubectl` credentials to communicate with your cluster:
         
         gcloud container clusters get-credentials "${CLUSTER_NAME}" \
             --location="${REGION}" \
             --project="${PROJECT_ID}"




## Install KAI Scheduler and NVIDIA Dynamo

Prepare your cluster by creating a Hugging Face Secret and installing the KAI Scheduler and NVIDIA Dynamo platform with Grove gang scheduling:

  1. Create a Kubernetes Secret named `hf-secret` to store your Hugging Face access token:
         
         kubectl create secret generic hf-secret \
             --from-literal=hf_api_token="${HF_TOKEN}" \
             --dry-run=client -o yaml | kubectl apply -f -

  2. Download the NVIDIA Dynamo platform Helm chart (`v1.5.0`), install the KAI Scheduler, and install the Dynamo platform with Grove enabled:
         
         RELEASE_VERSION="${DYNAMO_RELEASE_VERSION:-1.5.0}"
         helm fetch "https://helm.ngc.nvidia.com/nvidia/ai-dynamo/charts/dynamo-platform-${RELEASE_VERSION}.tgz"
         tar -zxf "dynamo-platform-${RELEASE_VERSION}.tgz"
         
         helm upgrade --install kai-scheduler ./dynamo-platform/charts/kai-scheduler \
             --set scheduler.args.default-staleness-grace-period="-1s" \
             --set topologyMigration.enabled=false
         
         kubectl wait --for=condition=Available deployment/kai-operator --timeout=120s
         until kubectl get deployment/queue-controller >/dev/null 2>&1; do sleep 2; done
         kubectl wait --for=condition=Available deployment/queue-controller --timeout=120s
         
         helm upgrade --install dynamo-platform ./dynamo-platform \
             --set global.grove.install=true \
             --set global.grove.enabled=true \
             --set global.kai-scheduler.enabled=true




## Deploy the single-host disaggregated SGLang server

The workload manifest (`llama3.1-405b-singlehost-a4.yaml`) defines a Kubernetes ResourceClaimTemplate (`all-mrdma`), which allocates the node's multi-NIC RDMA devices (`mrdma.google.com`) through DRA, and an NVIDIA Dynamo DynamoGraphDeployment (`llama3-405b-a4-disagg`) with Grove gang scheduling enabled. The deployment consists of the following:

  * **Frontend (`Frontend`)**: runs one router replica that accepts client requests, discovers registered prefill and decode workers, and coordinates disaggregated request routing.
  * **Prefill worker (`Prefill`)**: runs a single-host worker on one `a4-highgpu-8g` node with eight NVIDIA B200 GPUs. On startup, the Pod sources the NCCL/gIB environment, downloads the `nvidia/Llama-3.1-405B-Instruct-FP8` checkpoint from Hugging Face Hub to the node's Local NVMe SSD, and launches `python3 -m dynamo.sglang` in `--disaggregation-mode prefill` with the following flags: 
    * `--tensor-parallel-size 8`
    * `--kv-cache-dtype fp8_e4m3`
    * `--context-length 16384`
    * `--mem-fraction-static 0.85`
  * **Decode worker (`Decode`)**: runs a single-host worker on the second `a4-highgpu-8g` node with eight NVIDIA B200 GPUs. On startup, the Pod caches the model weights on the node's Local NVMe SSD and launches `python3 -m dynamo.sglang` in `--disaggregation-mode decode` with the following flags: 
    * `--tensor-parallel-size 8`
    * `--kv-cache-dtype fp8_e4m3`
    * `--context-length 16384`
    * `--mem-fraction-static 0.85`



Deploy and monitor the disaggregated inference server:

  1. Download the `llama3.1-405b-singlehost-a4.yaml` workload manifest:
         
         curl -O https://raw.githubusercontent.com/GoogleCloudSamples/AIHypercomputerSamples/refs/heads/main/gpu/inference/llama3-405b/llama3.1-405b-singlehost-a4.yaml

Alternatively, create a file named `llama3.1-405b-singlehost-a4.yaml` with the following content:
         
         # ==============================================================================
         # Single-Host Disaggregated Serving of Llama 3.1 405B FP8 on GKE
         # using NVIDIA Dynamo Platform (v1.5.0) and SGLang on GPU A4 (2 x a4-highgpu-8g)
         # Topology: 1-node Prefill (8 x B200, TP=8) + 1-node Decode (8 x B200, TP=8)
         # ==============================================================================
         apiVersion: resource.k8s.io/v1
         kind: ResourceClaimTemplate
         metadata:
           name: all-mrdma
         spec:
           spec:
             devices:
               requests:
                 - name: req-mrdma
                   exactly:
                     deviceClassName: mrdma.google.com
                     allocationMode: All
         ---
         apiVersion: nvidia.com/v1alpha1
         kind: DynamoGraphDeployment
         metadata:
           name: llama3-405b-a4-disagg
           annotations:
             nvidia.com/enable-grove: "true"
         spec:
           backendFramework: sglang
           services:
             # --------------------------------------------------------------------------
             # FRONTEND: Dynamo OpenAI-Compatible Router (`python3 -m dynamo.frontend`)
             # --------------------------------------------------------------------------
             Frontend:
               componentType: frontend
               replicas: 1
               resources:
                 requests:
                   cpu: "8"
                   memory: "32Gi"
                 limits:
                   cpu: "8"
                   memory: "32Gi"
               extraPodSpec:
                 tolerations:
                   - key: "nvidia.com/gpu"
                     operator: "Exists"
                     effect: "NoSchedule"
                 mainContainer:
                   image: nvcr.io/nvidia/ai-dynamo/sglang-runtime:1.5.0
                   command: ["/bin/bash", "-c"]
                   args:
                     - |
                       set -ex
                       exec python3 -m dynamo.frontend --http-port 8000
         
             # --------------------------------------------------------------------------
             # PREFILL WORKER: 1 x GPU A4 (`a4-highgpu-8g`, 8 x B200 GPUs, TP=8)
             # --------------------------------------------------------------------------
             Prefill:
               componentType: worker
               subComponentType: prefill
               replicas: 1
               livenessProbe:
                 httpGet:
                   path: /live
                   port: system
                 initialDelaySeconds: 600
                 periodSeconds: 60
                 timeoutSeconds: 30
                 failureThreshold: 60
               readinessProbe:
                 httpGet:
                   path: /health
                   port: system
                 initialDelaySeconds: 120
                 periodSeconds: 30
                 timeoutSeconds: 30
                 failureThreshold: 60
               sharedMemory:
                 size: 128Gi
               resources:
                 requests:
                   gpu: "8"
                   cpu: "128"
                   memory: "1500Gi"
                 limits:
                   gpu: "8"
                   cpu: "128"
                   memory: "2000Gi"
               envs:
                 - name: MODEL_PATH
                   value: "nvidia/Llama-3.1-405B-Instruct-FP8"
                 - name: HF_HOME
                   value: "/data"
                 - name: HF_TOKEN
                   valueFrom:
                     secretKeyRef:
                       name: hf-secret
                       key: hf_api_token
                       optional: true
                 - name: DYN_SYSTEM_ENABLED
                   value: "true"
                 - name: DYN_SYSTEM_USE_ENDPOINT_HEALTH_STATUS
                   value: "[\"generate\"]"
                 - name: DYN_SYSTEM_PORT
                   value: "9090"
                 - name: LD_LIBRARY_PATH
                   value: "/usr/local/gib/lib64:/usr/local/nvidia/lib64"
                 - name: GLOO_SOCKET_IFNAME
                   value: "eth0"
                 - name: WITH_NVIDIA_PEERMEM
                   value: "0"
                 # Xet CAS downloads returned unretried 429s; plain HTTP downloads back off on 429.
                 - name: HF_HUB_DISABLE_XET
                   value: "1"
               extraPodSpec:
                 resourceClaims:
                   - name: rdma
                     resourceClaimTemplateName: all-mrdma
                 nodeSelector:
                   cloud.google.com/gke-accelerator: nvidia-b200
                   cloud.google.com/gke-gpu: "true"
                   kubernetes.io/arch: amd64
                 tolerations:
                   - key: "nvidia.com/gpu"
                     operator: "Exists"
                     effect: "NoSchedule"
                   - key: "kubernetes.io/arch"
                     operator: "Equal"
                     value: "amd64"
                     effect: "NoSchedule"
                 mainContainer:
                   image: nvcr.io/nvidia/ai-dynamo/sglang-runtime:1.5.0
                   resources:
                     claims:
                       - name: rdma
                   startupProbe:
                     httpGet:
                       path: /live
                       port: system
                     initialDelaySeconds: 120
                     periodSeconds: 30
                     timeoutSeconds: 10
                     failureThreshold: 120
                   command: ["/bin/bash", "-c"]
                   args:
                     - |
                       set -ex
                       if [ -f /usr/local/gib/scripts/set_nccl_env.sh ]; then
                         . /usr/local/gib/scripts/set_nccl_env.sh
                       fi
         
                       # Pre-download with huggingface_hub, which backs off on HTTP 429s. Dynamo's built-in
                       # downloader (ModelExpress) aborts on the first 429 and skips fetching if weights are cached.
                       echo "=== [Dynamo Prefill Worker] Ensuring weights are cached in ${HF_HOME:-/data} ==="
                       python3 -c "import os; from huggingface_hub import snapshot_download; snapshot_download(os.environ['MODEL_PATH'], max_workers=16)"
                       # --host 0.0.0.0 is required so MooncakeKVBootstrapServer binds to 0.0.0.0:30001 instead of 127.0.0.1:30001.
                       echo "=== [Dynamo Prefill Worker] Launching dynamo.sglang ==="
                       exec python3 -m dynamo.sglang \
                         --model-path "${MODEL_PATH}" \
                         --host 0.0.0.0 \
                         --disaggregation-mode prefill \
                         --disaggregation-bootstrap-port 30001 \
                         --tensor-parallel-size 8 \
                         --kv-cache-dtype fp8_e4m3 \
                         --context-length 16384 \
                         --mem-fraction-static 0.85 \
                         --enable-metrics
                   volumeMounts:
                     - name: library-dir-host
                       mountPath: /usr/local/nvidia
                     - name: gib
                       mountPath: /usr/local/gib
                     - name: data-volume
                       mountPath: /data
                 volumes:
                   - name: library-dir-host
                     hostPath:
                       path: /home/kubernetes/bin/nvidia
                   - name: gib
                     hostPath:
                       path: /home/kubernetes/bin/gib
                   - name: data-volume
                     emptyDir: {}
         
             # --------------------------------------------------------------------------
             # DECODE WORKER: 1 x GPU A4 (`a4-highgpu-8g`, 8 x B200 GPUs, TP=8)
             # --------------------------------------------------------------------------
             Decode:
               componentType: worker
               subComponentType: decode
               replicas: 1
               livenessProbe:
                 httpGet:
                   path: /live
                   port: system
                 initialDelaySeconds: 600
                 periodSeconds: 60
                 timeoutSeconds: 30
                 failureThreshold: 60
               readinessProbe:
                 httpGet:
                   path: /health
                   port: system
                 initialDelaySeconds: 120
                 periodSeconds: 30
                 timeoutSeconds: 30
                 failureThreshold: 60
               sharedMemory:
                 size: 128Gi
               resources:
                 requests:
                   gpu: "8"
                   cpu: "128"
                   memory: "1500Gi"
                 limits:
                   gpu: "8"
                   cpu: "128"
                   memory: "2000Gi"
               envs:
                 - name: MODEL_PATH
                   value: "nvidia/Llama-3.1-405B-Instruct-FP8"
                 - name: HF_HOME
                   value: "/data"
                 - name: HF_TOKEN
                   valueFrom:
                     secretKeyRef:
                       name: hf-secret
                       key: hf_api_token
                       optional: true
                 - name: DYN_SYSTEM_ENABLED
                   value: "true"
                 - name: DYN_SYSTEM_USE_ENDPOINT_HEALTH_STATUS
                   value: "[\"generate\"]"
                 - name: DYN_SYSTEM_PORT
                   value: "9090"
                 - name: LD_LIBRARY_PATH
                   value: "/usr/local/gib/lib64:/usr/local/nvidia/lib64"
                 - name: GLOO_SOCKET_IFNAME
                   value: "eth0"
                 - name: WITH_NVIDIA_PEERMEM
                   value: "0"
                 # Xet CAS downloads returned unretried 429s; plain HTTP downloads back off on 429.
                 - name: HF_HUB_DISABLE_XET
                   value: "1"
               extraPodSpec:
                 resourceClaims:
                   - name: rdma
                     resourceClaimTemplateName: all-mrdma
                 nodeSelector:
                   cloud.google.com/gke-accelerator: nvidia-b200
                   cloud.google.com/gke-gpu: "true"
                   kubernetes.io/arch: amd64
                 tolerations:
                   - key: "nvidia.com/gpu"
                     operator: "Exists"
                     effect: "NoSchedule"
                   - key: "kubernetes.io/arch"
                     operator: "Equal"
                     value: "amd64"
                     effect: "NoSchedule"
                 mainContainer:
                   image: nvcr.io/nvidia/ai-dynamo/sglang-runtime:1.5.0
                   resources:
                     claims:
                       - name: rdma
                   startupProbe:
                     httpGet:
                       path: /live
                       port: system
                     initialDelaySeconds: 120
                     periodSeconds: 30
                     timeoutSeconds: 10
                     failureThreshold: 120
                   command: ["/bin/bash", "-c"]
                   args:
                     - |
                       set -ex
                       if [ -f /usr/local/gib/scripts/set_nccl_env.sh ]; then
                         . /usr/local/gib/scripts/set_nccl_env.sh
                       fi
         
                       # Pre-download with huggingface_hub, which backs off on HTTP 429s. Dynamo's built-in
                       # downloader (ModelExpress) aborts on the first 429 and skips fetching if weights are cached.
                       echo "=== [Dynamo Decode Worker] Ensuring weights are cached in ${HF_HOME:-/data} ==="
                       python3 -c "import os; from huggingface_hub import snapshot_download; snapshot_download(os.environ['MODEL_PATH'], max_workers=16)"
                       echo "=== [Dynamo Decode Worker] Launching dynamo.sglang ==="
                       exec python3 -m dynamo.sglang \
                         --model-path "${MODEL_PATH}" \
                         --host 0.0.0.0 \
                         --disaggregation-mode decode \
                         --disaggregation-bootstrap-port 30001 \
                         --tensor-parallel-size 8 \
                         --kv-cache-dtype fp8_e4m3 \
                         --context-length 16384 \
                         --mem-fraction-static 0.85 \
                         --enable-metrics
                   volumeMounts:
                     - name: library-dir-host
                       mountPath: /usr/local/nvidia
                     - name: gib
                       mountPath: /usr/local/gib
                     - name: data-volume
                       mountPath: /data
                 volumes:
                   - name: library-dir-host
                     hostPath:
                       path: /home/kubernetes/bin/nvidia
                   - name: gib
                     hostPath:
                       path: /home/kubernetes/bin/gib
                   - name: data-volume
                     emptyDir: {}

  2. Apply the workload manifest to your cluster:
         
         kubectl apply -f llama3.1-405b-singlehost-a4.yaml

  3. To monitor weight download and server initialization, list the Pods in your cluster, and stream the logs of the prefill and decode Pods:
         
         kubectl get pods
         POD_NAME="YOUR_POD_NAME"
         kubectl logs -f "${POD_NAME}"

Replace `YOUR_POD_NAME` with the name of the prefill Pod or decode Pod from the `kubectl get pods` output.

On the first run, it takes approximately 10 to 20 minutes to download the 405B FP8 model weights and initialize the SGLang servers. Before you send any requests, wait until the frontend, prefill, and decode Pods show `1/1` in the `READY` column of `kubectl get pods`:
         
         NAME                                        READY   STATUS    RESTARTS   AGE
         llama3-405b-a4-disagg-0-decode-tgl7q        1/1     Running   0          15m
         llama3-405b-a4-disagg-0-frontend-wrxq5      1/1     Running   0          15m
         llama3-405b-a4-disagg-0-prefill-67h5s       1/1     Running   0          15m
         




## Send inference requests

Send a chat completion request to the deployed Llama 3.1 405B service:

  1. Forward local port `8000` to the `llama3-405b-a4-disagg-frontend` service:
         
         kubectl port-forward svc/llama3-405b-a4-disagg-frontend 8000:8000

Leave port forwarding running in this terminal session, or run the command in the background.

  2. In a second terminal session, send a chat completion request to the `/v1/chat/completions` endpoint:
         
         curl http://127.0.0.1:8000/v1/chat/completions \
           -H "Content-Type: application/json" \
           -d '{
             "model": "nvidia/Llama-3.1-405B-Instruct-FP8",
             "messages": [{"role": "user", "content": "Explain KV-cache disaggregation in one sentence."}],
             "max_tokens": 64
           }' | jq .




## Run a benchmark workload

Benchmark the deployed Llama 3.1 405B server from the Dynamo frontend Pod by using `sglang.bench_serving`. Configure the benchmark for 1,024 input tokens, 1,024 output tokens (`1k/1k`), 2,048 prompts, and a maximum concurrency of 512:
    
    
    ROUTER_POD=$(kubectl get pod -l 'nvidia.com/dynamo-component-type=frontend' -o jsonpath='{.items[0].metadata.name}')
    
    kubectl exec "${ROUTER_POD}" -- python3 -m sglang.bench_serving \
      --backend sglang-oai-chat \
      --base-url http://localhost:8000 \
      --model nvidia/Llama-3.1-405B-Instruct-FP8 \
      --dataset-name random \
      --random-input-len 1024 \
      --random-output-len 1024 \
      --random-range-ratio 1.0 \
      --num-prompts 2048 \
      --max-concurrency 512 \
      --warmup-requests 10 | tee benchmark.log

After the benchmark completes, look for output that contains metrics such as the following:

  * `Output token throughput`
  * `Total token throughput`
  * `TTFT`
  * `TPOT`



## Clean up

To avoid incurring additional ongoing charges to your Google Cloud account for the resources used in this tutorial, delete the Kubernetes workloads, the GKE cluster, and your Cloud Storage bucket:

  1. Delete the DynamoGraphDeployment and ResourceClaimTemplate resources:
         
         kubectl delete -f llama3.1-405b-singlehost-a4.yaml --ignore-not-found || true

  2. Uninstall the NVIDIA Dynamo platform and KAI Scheduler Helm releases:
         
         helm uninstall dynamo-platform kai-scheduler || true

  3. Delete the Hugging Face Kubernetes Secret:
         
         kubectl delete secret hf-secret --ignore-not-found || true

  4. From the `cluster-toolkit` directory, destroy the GKE cluster and its associated infrastructure by using the [`gcluster destroy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-destroy):
         
         cd cluster-toolkit
         ./gcluster destroy "${CLUSTER_NAME}" --auto-approve || true
         cd ..

  5. To delete the Cloud Storage bucket that stores the Terraform state, use the [`gcloud storage rm` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rm):
         
         gcloud storage rm --recursive "gs://${GCS_BUCKET}"




## What's next

  * Learn more about [NVIDIA Dynamo](https://github.com/ai-dynamo/dynamo).
  * Learn more about [SGLang](https://github.com/sgl-project/sglang).
  * Learn more about [A4 VMs with NVIDIA B200 GPUs](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms).
  * Learn more about [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview).
  * Learn more about [managing AI-optimized GKE clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/manage-gke-clusters).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 

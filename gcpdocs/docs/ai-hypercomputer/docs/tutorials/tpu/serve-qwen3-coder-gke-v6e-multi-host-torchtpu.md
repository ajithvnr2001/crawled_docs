---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/serve-qwen3-coder-gke-v6e-multi-host-torchtpu/
title: Serve Qwen3-Coder-30B-A3B on GKE with multi-host SGLang TorchTPU and PD disaggregation on TPU v6e accelerators \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-08T05:43:45.344078+00:00
---

# Serve Qwen3-Coder-30B-A3B on GKE with multi-host SGLang TorchTPU and PD disaggregation on TPU v6e accelerators  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/serve-qwen3-coder-gke-v6e-multi-host-torchtpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Serve Qwen3-Coder-30B-A3B on GKE with multi-host SGLang TorchTPU and PD disaggregation on TPU v6e accelerators Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to deploy and serve [Qwen3-Coder-30B-A3B (`Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8`)](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8), a mixture of experts coding model, on Google Kubernetes Engine (GKE). The deployment uses multi-host [TPU v6e (Trillium)](https://docs.cloud.google.com/tpu/docs/v6e) accelerators and the [SGLang serving framework](https://github.com/sgl-project/sglang-torchtpu) with TorchTPU (`torchtpu`) and prefill-decode (PD) disaggregation.

In the deployment configuration that's described in this tutorial, you provision two multi-host `ct6e-standard-4t` node pools, each arranged in a `2x4` topology (eight TPU v6e chips across two nodes per node pool, for a total of 16 TPU v6e chips). You use the Kubernetes LeaderWorkerSet API to do the following:

  * Run disaggregated multi-host prefill and decode servers on separate TPU v6e slices with tensor parallelism and expert parallelism enabled.
  * Route requests through an SGLang disaggregation router.



To run a similar multi-host SGLang TorchTPU serving workflow on [TPU7x (Ironwood)](https://docs.cloud.google.com/tpu/docs/tpu7x) accelerators with the larger Qwen3-Coder-480B model, see [Serve Qwen3-Coder-480B on GKE with multi-host SGLang TorchTPU and PD disaggregation on TPU7x accelerators](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/serve-qwen3-coder-gke-ironwood-multi-host-torchtpu).

## Objectives

  * Set up your GKE cluster and multi-host TPU v6e node pools.
  * Configure credentials and install the LeaderWorkerSet controller.
  * Deploy the multi-host SGLang prefill, decode, and router workloads.
  * Send an inference request to the SGLang router service.
  * Run a serving benchmark workload.
  * Clean up.



## Costs

In this document, you use the following billable components of Google Cloud:

  * [GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * [Cloud TPU](https://docs.cloud.google.com/tpu/pricing)
  * [Compute Engine](https://docs.cloud.google.com/compute/all-pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator).

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

Set up your environment for the tutorial:

  * [Install](https://docs.cloud.google.com/sdk/docs/install) and [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the Google Cloud CLI, and install [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl). If you use Cloud Shell, both tools are preinstalled.

  * Enable the Kubernetes Engine API, Compute Engine API, Cloud TPU API, and Artifact Registry API in your Google Cloud project:

[Enable APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,compute.googleapis.com,tpu.googleapis.com,artifactregistry.googleapis.com)

  * Ensure that your project has sufficient [disk quota and external IP address quota](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#additional-quotas) in the region where your TPU capacity is located:

    1. In the Google Cloud console, go to the **Quotas & System Limits** page.

[Go to Quotas & System Limits](https://console.cloud.google.com/iam-admin/quotas)

    2. Verify that you have at least 400 GiB of available Google Cloud Hyperdisk Balanced quota across the four 100 GiB ephemeral volumes that are used for model caching by the prefill and decode Pods.

    3. Filter by **In-use regional external IPv4 addresses** and verify that you have sufficient IP address quota in your target region.


**Important:** To complete this tutorial, you must have quota for TPU v6e chips in your Google Cloud project. TPU quota is [region- and zone-specific](https://docs.cloud.google.com/tpu/docs/regions-zones), so create your resources in a region and zone where TPU v6e capacity is available. This tutorial uses a TPU v6e reservation, but you can also use Spot capacity or Flex-start VMs if available. To learn more about reserving Cloud TPU capacity, see [About Cloud TPU reservations](https://docs.cloud.google.com/tpu/docs/about-tpu-reservations).

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
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Ensure that your [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) has the following Identity and Access Management (IAM) roles on your project:

  * [Kubernetes Engine Default Node Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.defaultNodeServiceAccount) (`roles/container.defaultNodeServiceAccount`)
  * [Artifact Registry Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`)



## Set up your environment variables

Export the environment variables that you use throughout this tutorial:
    
    
    export CLUSTER_NAME="YOUR_CLUSTER_NAME" # <= 40 chars; start with a-z; only a-z, 0-9, -
    export PROJECT_ID="YOUR_PROJECT_ID" # Your Google Cloud project ID
    export REGION="YOUR_REGION" # for example, us-central1
    export ZONE="YOUR_ZONE" # for example, us-central1-c
    export RESERVATION="YOUR_RESERVATION_NAME" # TPU7x reservation name (if using a reservation)
    export HF_TOKEN="YOUR_HF_TOKEN" # Hugging Face access token
    export SGLANG_IMAGE="lmsysorg/sglang:v0.1.0-tpu"

Replace the following:

  * `YOUR_CLUSTER_NAME`: the name of your GKE cluster.
  * `YOUR_PROJECT_ID`: the ID of your Google Cloud project.
  * `YOUR_REGION`: the region where you want to deploy your cluster, such as `us-central1`.
  * `YOUR_ZONE`: the zone where you want to deploy your TPU v6e node pools, such as `us-central1-b`.
  * `YOUR_RESERVATION_NAME`: if you're using a reservation, the name of your TPU v6e reservation.
  * `YOUR_HF_TOKEN`: your Hugging Face access token.



If you're using a custom SGLang TorchTPU container image, replace `lmsysorg/sglang:v0.1.0-tpu` in the `SGLANG_IMAGE` variable with the URI of your image.

## Create the GKE cluster

To create a GKE cluster in Standard mode and attach two multi-host TPU v6e node pools for prefill and decode disaggregation, complete the following steps:

  1. Create a regional GKE cluster that uses `e2-standard-4` nodes for the default node pool, which provides sufficient CPU and memory resources for the LeaderWorkerSet controller and the SGLang disaggregation router:
         
         gcloud container clusters create "${CLUSTER_NAME}" \
           --project="${PROJECT_ID}" \
           --location="${REGION}" \
           --machine-type=e2-standard-4

  2. Create two multi-host TPU v6e node pools, each containing two `ct6e-standard-4t` nodes (eight TPU v6e chips in a `2x4` topology per node pool, for a total of 16 TPU v6e chips):
         
         gcloud container node-pools create tpu-v6e-pool-0 \
             --cluster="${CLUSTER_NAME}" \
             --location="${REGION}" \
             --node-locations="${ZONE}" \
             --machine-type=ct6e-standard-4t \
             --tpu-topology=2x4 \
             --num-nodes=2 \
             --reservation-affinity=specific \
             --reservation="${RESERVATION}" \
             --project="${PROJECT_ID}"
         
         gcloud container node-pools create tpu-v6e-pool-1 \
             --cluster="${CLUSTER_NAME}" \
             --location="${REGION}" \
             --node-locations="${ZONE}" \
             --machine-type=ct6e-standard-4t \
             --tpu-topology=2x4 \
             --num-nodes=2 \
             --reservation-affinity=specific \
             --reservation="${RESERVATION}" \
             --project="${PROJECT_ID}"

Instead of using a specific reservation, you can also create the node pools using Spot capacity or Flex-start VMs:

### Spot VMs

Provision the node pools using Spot capacity by replacing the `--reservation-affinity=specific` and `--reservation="${RESERVATION}"` flags with the `--spot` flag:
         
         gcloud container node-pools create tpu-v6e-pool-0 \
             --cluster="${CLUSTER_NAME}" \
             --location="${REGION}" \
             --node-locations="${ZONE}" \
             --machine-type=ct6e-standard-4t \
             --tpu-topology=2x4 \
             --num-nodes=2 \
             --project="${PROJECT_ID}" \
             --spot
         
         gcloud container node-pools create tpu-v6e-pool-1 \
             --cluster="${CLUSTER_NAME}" \
             --location="${REGION}" \
             --node-locations="${ZONE}" \
             --machine-type=ct6e-standard-4t \
             --tpu-topology=2x4 \
             --num-nodes=2 \
             --project="${PROJECT_ID}" \
             --spot

Instances using Spot capacity might take time to be created after the node pool is created, and they might be preempted during workload runs.

### Flex-start VMs

Provision the node pools using the [Flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws) consumption option:
         
         gcloud container node-pools create tpu-v6e-pool-0 \
             --cluster="${CLUSTER_NAME}" \
             --location="${REGION}" \
             --node-locations="${ZONE}" \
             --machine-type=ct6e-standard-4t \
             --tpu-topology=2x4 \
             --project="${PROJECT_ID}" \
             --reservation-affinity=none \
             --enable-autoscaling \
             --num-nodes=0 \
             --min-nodes=0 \
             --max-nodes=2 \
             --flex-start
         
         gcloud container node-pools create tpu-v6e-pool-1 \
             --cluster="${CLUSTER_NAME}" \
             --location="${REGION}" \
             --node-locations="${ZONE}" \
             --machine-type=ct6e-standard-4t \
             --tpu-topology=2x4 \
             --project="${PROJECT_ID}" \
             --reservation-affinity=none \
             --enable-autoscaling \
             --num-nodes=0 \
             --min-nodes=0 \
             --max-nodes=2 \
             --flex-start

For more information, see [Run a small batch workload with TPUs and Flex-start VMs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dws-flex-start-training-tpu).

  3. Configure `kubectl` credentials to communicate with your cluster:
         
         gcloud container clusters get-credentials "${CLUSTER_NAME}" --location="${REGION}" --project="${PROJECT_ID}"




## Configure credentials and install LeaderWorkerSet

To prepare your cluster for the multi-host SGLang deployment, complete the following steps:

  1. Create a Kubernetes Secret named `hf-secret` to store your Hugging Face access token:
         
         kubectl create secret generic hf-secret \
             --from-literal=hf_api_token="${HF_TOKEN}"

  2. Install the LeaderWorkerSet CustomResourceDefinition and controller on your cluster:
         
         kubectl apply --server-side -k github.com/kubernetes-sigs/lws/config/default?ref=main
         echo "Waiting for LWS controller to be ready..."
         kubectl wait --for=condition=Available --timeout=300s deployment/lws-controller-manager -n lws-system




## Deploy the multi-host SGLang server

The workload manifest (`qwen3-coder-30b-multihost-disagg-v6e-2x4.yaml`) defines the following resources to coordinate disaggregated prefill and decode serving across the two `2x4` TPU v6e node pools:

  * **StorageClass (`hyperdisk-balanced-tpu`)**: provisions ephemeral 100 GiB ReadWriteOnce volumes backed by Google Cloud Hyperdisk Balanced storage. Each of the four prefill and decode Pods mounts its own volume at `/data` to store the downloaded `Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8` checkpoints locally.

  * **Prefill pool (`sglang-prefill-service` and `sglang-tpu-prefill`)**: runs a LeaderWorkerSet, which contains one leader Pod and one worker Pod, pinned exclusively to one `2x4` TPU v6e node pool. This node pool has eight TPU chips, which provide eight TensorCores. The LeaderWorkerSet uses the `leaderworkerset.sigs.k8s.io/exclusive-topology` annotation set to `"cloud.google.com/gke-nodepool"`. The Pods launch `sglang.launch_server` with the following flags, exposing port `8000` and bootstrap port `8998`:

    * `--disaggregation-mode=prefill`
    * `--tensor-parallel-size=8`
    * `--ep-size=8`
  * **Decode pool (`sglang-decode-service` and `sglang-tpu-decode`)**: runs a LeaderWorkerSet of `size: 2` pinned to the second `2x4` TPU v6e node pool (eight TPU chips, which provide eight TensorCores). The LeaderWorkerSet launches `sglang.launch_server` with the following flags:

    * `--disaggregation-mode=decode`
    * `--tensor-parallel-size=8`
    * `--ep-size=8`
  * **Disaggregation router (`sglang-router` and `sglang-service`)**: runs a CPU deployment that executes the `sglang_router.launch_router` module with the `--pd-disaggregation` flag and exposes a ClusterIP Service on port `8000`. The router directs prompts and coordinates KV cache transfer between the `sglang-prefill-service` and `sglang-decode-service` services.




To deploy and monitor the multi-host SGLang servers, complete the following steps:

  1. Download the workload manifest:
         
         curl -LO https://raw.githubusercontent.com/GoogleCloudSamples/AIHypercomputerSamples/main/tpu/inference/qwen3-coder/qwen3-coder-30b-multihost-disagg-v6e-2x4.yaml

Alternatively, create a file named `qwen3-coder-30b-multihost-disagg-v6e-2x4.yaml` with the following content:
         
         # ==============================================================================
         # Serve Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 on GKE / Trillium (TPU v6e)
         # using SGLang TorchTPU with Prefill/Decode Disaggregation, multi-host (2x4)
         # ==============================================================================
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
           name: hyperdisk-balanced-tpu
         provisioner: pd.csi.storage.gke.io
         volumeBindingMode: WaitForFirstConsumer
         allowVolumeExpansion: true
         parameters:
           type: hyperdisk-balanced
         ---
         # ==============================================================================
         # PREFILL POOL: Internal ClusterIP Service exposing SGLang Prefill Endpoint
         # ==============================================================================
         apiVersion: v1
         kind: Service
         metadata:
           name: sglang-prefill-service
           labels:
             app: sglang-prefill
         spec:
           type: ClusterIP
           selector:
             app: sglang-prefill
             role: leader
           ports:
             - name: http
               protocol: TCP
               port: 8000
               targetPort: 8000
             - name: bootstrap
               protocol: TCP
               port: 8998
               targetPort: 8998
         ---
         # ==============================================================================
         # PREFILL POOL: LeaderWorkerSet (TPU v6e, 1 slice = 2 nodes, 8 chips / 8 TensorCores, 2x4)
         # ==============================================================================
         apiVersion: leaderworkerset.x-k8s.io/v1
         kind: LeaderWorkerSet
         metadata:
           name: sglang-tpu-prefill
           annotations:
             leaderworkerset.sigs.k8s.io/exclusive-topology: "cloud.google.com/gke-nodepool"
           labels:
             app: sglang-prefill
         spec:
           replicas: 1
           rolloutStrategy:
             type: RollingUpdate
           leaderWorkerTemplate:
             size: 2
             restartPolicy: RecreateGroupOnPodRestart
             leaderTemplate:
               metadata:
                 labels:
                   app: sglang-prefill
                   role: leader
               spec: &prefill-pod-spec
                 securityContext:
                   fsGroup: 65534
                 nodeSelector:
                   cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
                   cloud.google.com/gke-tpu-topology: 2x4
                 tolerations:
                   - key: "google.com/tpu"
                     operator: "Exists"
                     effect: "NoSchedule"
                 containers:
                   - name: sglang
                     image: $SGLANG_IMAGE
                     command:
                       - /bin/bash
                       - -c
                       - |
                         set -ex
                         ulimit -c 0
                         LEADER_POD="${LWS_LEADER_ADDRESS%%.*}"
                         DNS_SUFFIX="${LWS_LEADER_ADDRESS#*.}"
                         HOSTS="${LWS_LEADER_ADDRESS}"
                         for ((i = 1; i < LWS_GROUP_SIZE; i++)); do
                           HOSTS="${HOSTS},${LEADER_POD}-${i}.${DNS_SUFFIX}"
                         done
                         export TPU_WORKER_HOSTNAMES="${HOSTS}"
                         export TPU_WORKER_ID="${LWS_WORKER_INDEX}"
                         export TORCH_TPU_DEVICES_PER_HOST=4
                         export TPU_TOPOLOGY="2x4x1"
                         echo "=== [prefill rank ${LWS_WORKER_INDEX}/${LWS_GROUP_SIZE}] hosts=${TPU_WORKER_HOSTNAMES} ==="
                         exec python3 -m sglang.launch_server \
                           --device=tpu \
                           --host=0.0.0.0 \
                           --port=8000 \
                           --model-path=Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 \
                           --tensor-parallel-size=8 \
                           --ep-size=8 \
                           --nnodes="${LWS_GROUP_SIZE}" \
                           --node-rank="${LWS_WORKER_INDEX}" \
                           --dist-init-addr="${LWS_LEADER_ADDRESS}:20000" \
                           --attention-backend=pallas_tpu_rpa_batched \
                           --mem-fraction-static=0.8 \
                           --max-running-requests=256 \
                           --chunked-prefill-size=8192 \
                           --max-total-tokens=524288 \
                           --context-length=9216 \
                           --enable-torch-compile \
                           --torch-compile-max-bs=256 \
                           --tpu-compile-tracer=direct \
                           --sampling-defaults=openai \
                           --enable-fused-qk-norm-rope \
                           --disaggregation-mode=prefill \
                           --disaggregation-transfer-backend=tpu \
                           --download-dir=/data \
                           --tpu-compile-tokens=8192 \
                           --disable-radix-cache
                     env:
                       - name: HF_TOKEN
                         valueFrom:
                           secretKeyRef:
                             name: hf-secret
                             key: hf_api_token
                             optional: true
                     resources:
                       requests:
                         cpu: "16"
                         memory: 128Gi
                         google.com/tpu: "4"
                       limits:
                         memory: 280Gi
                         google.com/tpu: "4"
                     ports:
                       - containerPort: 8000
                         name: http
                       - containerPort: 8998
                         name: bootstrap
                     startupProbe:
                       httpGet:
                         path: /health
                         port: 8000
                       initialDelaySeconds: 60
                       periodSeconds: 15
                       timeoutSeconds: 10
                       failureThreshold: 236
                     readinessProbe:
                       httpGet:
                         path: /health
                         port: 8000
                       periodSeconds: 10
                       timeoutSeconds: 10
                       failureThreshold: 6
                     volumeMounts:
                       - name: model-cache
                         mountPath: /data
                       - name: dshm
                         mountPath: /dev/shm
                 volumes:
                   - name: dshm
                     emptyDir:
                       medium: Memory
                       sizeLimit: 32Gi
                   - name: model-cache
                     ephemeral:
                       volumeClaimTemplate:
                         spec:
                           accessModes: ["ReadWriteOnce"]
                           storageClassName: hyperdisk-balanced-tpu
                           resources:
                             requests:
                               storage: 100Gi
             workerTemplate:
               metadata:
                 labels:
                   app: sglang-prefill
                   role: worker
               spec: *prefill-pod-spec
         ---
         # ==============================================================================
         # DECODE POOL: Internal ClusterIP Service exposing SGLang Decode Endpoint
         # ==============================================================================
         apiVersion: v1
         kind: Service
         metadata:
           name: sglang-decode-service
           labels:
             app: sglang-decode
         spec:
           type: ClusterIP
           selector:
             app: sglang-decode
             role: leader
           ports:
             - name: http
               protocol: TCP
               port: 8000
               targetPort: 8000
             - name: bootstrap
               protocol: TCP
               port: 8998
               targetPort: 8998
         ---
         # ==============================================================================
         # DECODE POOL: LeaderWorkerSet (TPU v6e, 1 slice = 2 nodes, 8 chips / 8 TensorCores, 2x4)
         # ==============================================================================
         apiVersion: leaderworkerset.x-k8s.io/v1
         kind: LeaderWorkerSet
         metadata:
           name: sglang-tpu-decode
           annotations:
             leaderworkerset.sigs.k8s.io/exclusive-topology: "cloud.google.com/gke-nodepool"
           labels:
             app: sglang-decode
         spec:
           replicas: 1
           rolloutStrategy:
             type: RollingUpdate
           leaderWorkerTemplate:
             size: 2
             restartPolicy: RecreateGroupOnPodRestart
             leaderTemplate:
               metadata:
                 labels:
                   app: sglang-decode
                   role: leader
               spec: &decode-pod-spec
                 securityContext:
                   fsGroup: 65534
                 nodeSelector:
                   cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
                   cloud.google.com/gke-tpu-topology: 2x4
                 tolerations:
                   - key: "google.com/tpu"
                     operator: "Exists"
                     effect: "NoSchedule"
                 containers:
                   - name: sglang
                     image: $SGLANG_IMAGE
                     command:
                       - /bin/bash
                       - -c
                       - |
                         set -ex
                         ulimit -c 0
                         LEADER_POD="${LWS_LEADER_ADDRESS%%.*}"
                         DNS_SUFFIX="${LWS_LEADER_ADDRESS#*.}"
                         HOSTS="${LWS_LEADER_ADDRESS}"
                         for ((i = 1; i < LWS_GROUP_SIZE; i++)); do
                           HOSTS="${HOSTS},${LEADER_POD}-${i}.${DNS_SUFFIX}"
                         done
                         export TPU_WORKER_HOSTNAMES="${HOSTS}"
                         export TPU_WORKER_ID="${LWS_WORKER_INDEX}"
                         export TORCH_TPU_DEVICES_PER_HOST=4
                         export TPU_TOPOLOGY="2x4x1"
                         echo "=== [decode rank ${LWS_WORKER_INDEX}/${LWS_GROUP_SIZE}] hosts=${TPU_WORKER_HOSTNAMES} ==="
                         exec python3 -m sglang.launch_server \
                           --device=tpu \
                           --host=0.0.0.0 \
                           --port=8000 \
                           --model-path=Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 \
                           --tensor-parallel-size=8 \
                           --ep-size=8 \
                           --nnodes="${LWS_GROUP_SIZE}" \
                           --node-rank="${LWS_WORKER_INDEX}" \
                           --dist-init-addr="${LWS_LEADER_ADDRESS}:20000" \
                           --attention-backend=pallas_tpu_rpa_batched \
                           --mem-fraction-static=0.8 \
                           --max-running-requests=256 \
                           --chunked-prefill-size=8192 \
                           --max-total-tokens=524288 \
                           --context-length=9216 \
                           --enable-torch-compile \
                           --torch-compile-max-bs=256 \
                           --tpu-compile-tracer=direct \
                           --sampling-defaults=openai \
                           --enable-fused-qk-norm-rope \
                           --disaggregation-mode=decode \
                           --disaggregation-transfer-backend=tpu \
                           --download-dir=/data
                     env:
                       - name: HF_TOKEN
                         valueFrom:
                           secretKeyRef:
                             name: hf-secret
                             key: hf_api_token
                             optional: true
                     resources:
                       requests:
                         cpu: "16"
                         memory: 128Gi
                         google.com/tpu: "4"
                       limits:
                         memory: 280Gi
                         google.com/tpu: "4"
                     ports:
                       - containerPort: 8000
                         name: http
                       - containerPort: 8998
                         name: bootstrap
                     startupProbe:
                       httpGet:
                         path: /health
                         port: 8000
                       initialDelaySeconds: 60
                       periodSeconds: 15
                       timeoutSeconds: 10
                       failureThreshold: 236
                     readinessProbe:
                       httpGet:
                         path: /health
                         port: 8000
                       periodSeconds: 10
                       timeoutSeconds: 10
                       failureThreshold: 6
                     volumeMounts:
                       - name: model-cache
                         mountPath: /data
                       - name: dshm
                         mountPath: /dev/shm
                 volumes:
                   - name: dshm
                     emptyDir:
                       medium: Memory
                       sizeLimit: 32Gi
                   - name: model-cache
                     ephemeral:
                       volumeClaimTemplate:
                         spec:
                           accessModes: ["ReadWriteOnce"]
                           storageClassName: hyperdisk-balanced-tpu
                           resources:
                             requests:
                               storage: 100Gi
             workerTemplate:
               metadata:
                 labels:
                   app: sglang-decode
                   role: worker
               spec: *decode-pod-spec
         ---
         # ==============================================================================
         # SGLANG DISAGGREGATION ROUTER / PROXY DEPLOYMENT
         # ==============================================================================
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: sglang-router
           labels:
             app: sglang-router
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: sglang-router
           template:
             metadata:
               labels:
                 app: sglang-router
             spec:
               containers:
                 - name: router
                   image: $SGLANG_IMAGE
                   command:
                     - python3
                     - -m
                     - sglang_router.launch_router
                   args:
                     - --pd-disaggregation
                     - --prefill
                     - http://sglang-prefill-service:8000
                     - "8998"
                     - --decode
                     - http://sglang-decode-service:8000
                     - --host
                     - 0.0.0.0
                     - --port
                     - "8000"
                     - --model-path
                     - Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8
                     - --request-timeout-secs
                     - "3600"
                     - --worker-startup-timeout-secs
                     - "5400"
                   env:
                     - name: HF_TOKEN
                       valueFrom:
                         secretKeyRef:
                           name: hf-secret
                           key: hf_api_token
                           optional: true
                   ports:
                     - containerPort: 8000
                       name: http
                   readinessProbe:
                     httpGet:
                       path: /health_generate
                       port: 8000
                     initialDelaySeconds: 15
                     periodSeconds: 30
                     timeoutSeconds: 10
                     failureThreshold: 3
                   resources:
                     requests:
                       cpu: "1"
                       memory: 4Gi
                     limits:
                       cpu: "4"
                       memory: 12Gi
         ---
         # ==============================================================================
         # SGLANG EXTERNAL SERVICE: Public / Client Endpoint for OpenAI-compatible Serving
         # ==============================================================================
         apiVersion: v1
         kind: Service
         metadata:
           name: sglang-service
           labels:
             app: sglang-router
         spec:
           type: ClusterIP
           selector:
             app: sglang-router
           ports:
             - name: http
               protocol: TCP
               port: 8000
               targetPort: 8000
         

  2. Apply the workload manifest to your cluster:
         
         envsubst '$SGLANG_IMAGE' < qwen3-coder-30b-multihost-disagg-v6e-2x4.yaml | kubectl apply -f -

  3. Verify that the router, prefill, and decode Pods are created:
         
         kubectl get pods

When all Pods are ready, the output is similar to the following:
         
         NAME                             READY   STATUS    RESTARTS   AGE
         sglang-router-6d87cb8c7d-gv4wr   1/1     Running   0          39m
         sglang-tpu-decode-0              1/1     Running   0          40m
         sglang-tpu-decode-0-1            1/1     Running   0          40m
         sglang-tpu-prefill-0             1/1     Running   0          40m
         sglang-tpu-prefill-0-1           1/1     Running   0          40m
         

  4. Wait for the prefill, decode, and router workloads to become ready:
         
         kubectl wait --for=condition=Available --timeout=5400s \
           lws/sglang-tpu-prefill lws/sglang-tpu-decode deployment/sglang-router

This command blocks in your terminal until all Pods pass their readiness checks. Initial model download, weight loading, and compilation take approximately seven to ten minutes on the first run. To monitor the Pod startup logs in real time while you wait, open another terminal session and run the following command:
         
         kubectl logs -f -l 'role in (leader,worker)' --prefix=true
         

If you're using preemptible capacity such as Spot capacity or Flex-start VMs, it might take longer after node pool creation for your TPU slice nodes to be created, and they might be preempted during workload runs. For more information, see [Preemptible VM instances](https://docs.cloud.google.com/compute/docs/instances/preemptible#preemption). To check whether your TPU slice nodes have been created, see [Check the node's status and conditions](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/node-notready#check-node-status-conditions).

When the server is ready to accept inference requests, the `kubectl wait` command in your first terminal exits with the following output:
         
         leaderworkerset.leaderworkerset.x-k8s.io/sglang-tpu-prefill condition met
         leaderworkerset.leaderworkerset.x-k8s.io/sglang-tpu-decode condition met
         deployment.apps/sglang-router condition met
         

  5. Open a second terminal session and forward local port `8000` to `sglang-service`:
         
         kubectl port-forward service/sglang-service 8000:8000

Leave port forwarding running in this terminal session.




## Send inference requests

Return to your first terminal session and send a chat completion request to the `/v1/chat/completions` endpoint exposed by the SGLang router:
    
    
    curl -s -X POST http://localhost:8000/v1/chat/completions \
      -H "Content-Type: application/json" \
      -d '{
        "model": "Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8",
        "messages": [
          {"role": "user", "content": "Explain quicksort in two sentences."}
        ],
        "max_tokens": 60,
        "temperature": 0.0
      }'

## Run a benchmark workload

To benchmark the deployed Qwen3-Coder-30B-A3B model using a 1,024-token input and 1,024-token output (`1k/1k`) workload from the `sglang-router` Pod, run the following command:
    
    
    kubectl exec deployment/sglang-router -- python3 -m sglang.bench_serving \
      --backend sglang \
      --base-url http://localhost:8000 \
      --model Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 \
      --dataset-name random \
      --random-input-len 1024 \
      --random-output-len 1024 \
      --random-range-ratio 1.0 \
      --num-prompts 256 \
      --max-concurrency 256

After the benchmark has completed, look for output that contains metrics such as the following:

  * `Output token throughput`
  * `Total token throughput`
  * `TTFT`
  * `TPOT`



## Clean up

To avoid incurring additional ongoing charges to your Google Cloud account for the resources used in this tutorial, delete the following resources:

  1. To stop the `kubectl port-forward` process, in your second terminal session, press `Control+C` (or `Command+C` on macOS).

  2. Return to your first terminal session and delete the SGLang prefill, decode, and router workloads and the `hf-secret` Secret:
         
         kubectl delete -f qwen3-coder-30b-multihost-disagg-v6e-2x4.yaml --ignore-not-found
         kubectl delete secret hf-secret --ignore-not-found

  3. Delete the TPU v6e node pools and the GKE cluster:
         
         gcloud container node-pools delete tpu-v6e-pool-0 \
             --cluster="${CLUSTER_NAME}" \
             --location="${REGION}" \
             --project="${PROJECT_ID}" \
             --quiet
         
         gcloud container node-pools delete tpu-v6e-pool-1 \
             --cluster="${CLUSTER_NAME}" \
             --location="${REGION}" \
             --project="${PROJECT_ID}" \
             --quiet
         
         gcloud container clusters delete "${CLUSTER_NAME}" \
             --location="${REGION}" \
             --project="${PROJECT_ID}" \
             --quiet




## What's next

  * Learn more about [SGLang](https://github.com/sgl-project/sglang-torchtpu).
  * Learn more about [TPU v6e (Trillium)](https://docs.cloud.google.com/tpu/docs/v6e).
  * Learn more about [Cloud TPU](https://docs.cloud.google.com/tpu/docs/intro-to-tpu).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 

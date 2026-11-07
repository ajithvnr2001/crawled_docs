---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/serve-llama-3-1-405b-a4-gke-sglang/
title: Serve Llama 3.1 405B on GKE with PD disaggregation using Dynamo and SGLang on A4 VMs \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-07T05:46:09.435658+00:00
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

In the deployment configuration that's described in this tutorial, you use Cluster Toolkit to provision a GKE cluster in Standard mode. The cluster contains two `a4-highgpu-8g` nodes connected over GPUDirect Remote Direct Memory Access (RDMA) networking. You then install the KAI Scheduler and NVIDIA Dynamo platform with Grove gang scheduling, and stage the model weights in Cloud Storage. Next, you deploy a DynamoGraphDeployment custom resource that mounts the bucket with Cloud Storage FUSE and separates prefill and decode across two single-host eight-GPU workers with tensor parallelism and an FP8 KV cache.

## Objectives

  * Install Cluster Toolkit and provision a two-node A4 GKE cluster in Standard mode.
  * Install the KAI Scheduler and NVIDIA Dynamo platform with Grove gang scheduling on your cluster.
  * Stage the Llama 3.1 405B model weights in a Cloud Storage bucket.
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

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) and [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the Google Cloud CLI. If you're using Cloud Shell, the Google Cloud CLI is preinstalled.
  2. Install [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl), `gke-gcloud-auth-plugin`, `jq`, and [Helm](https://helm.sh/docs/intro/install/) (version 3.10 or later). If you're using Cloud Shell, these tools are preinstalled.
  3. If you're running this tutorial from a Linux or macOS workstation rather than Cloud Shell, install the required [Cluster Toolkit dependencies](https://docs.cloud.google.com/cluster-toolkit/docs/setup/install-dependencies), such as Terraform and Git.
  4. Enable the Kubernetes Engine API, Compute Engine API, Cloud Storage API, Identity and Access Management API, Cloud Resource Manager API, and Service Usage API in your Google Cloud project:

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
  * `YOUR_CLUSTER_NAME`: the name for your GKE cluster and Cluster Toolkit deployment. Use a name of 20 characters or fewer so that the generated node pool service account ID (`YOUR_CLUSTER_NAME-gke-np-sa`) stays within the 30-character Identity and Access Management (IAM) limit. Additionally, the name must start with a lowercase letter, and contain only lowercase letters, numbers, and hyphens.
  * `YOUR_RESERVATION_NAME`: the name of your A4 reservation.
  * `YOUR_BUCKET_NAME`: a globally unique name for the Cloud Storage bucket that stores the Terraform state for Cluster Toolkit and the staged Llama 3.1 405B model weights.
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

  3. To store the Terraform state for your Cluster Toolkit deployment and the staged model weights, create a Cloud Storage bucket in the same region as your A4 reservation with uniform bucket-level access and object versioning enabled:
         
         gcloud storage buckets create "gs://${GCS_BUCKET}" \
             --default-storage-class=STANDARD \
             --project="${PROJECT_ID}" \
             --location="${REGION}" \
             --uniform-bucket-level-access
         gcloud storage buckets update "gs://${GCS_BUCKET}" --versioning

  4. Create the `cluster-toolkit/gke-a4-deployment.yaml` deployment configuration file for two `a4-highgpu-8g` nodes:
         
         cat <<EOF > cluster-toolkit/gke-a4-deployment.yaml
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

By default, the deployment file is configured to consume a [specific reservation](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-consumption-options#reservations). If you don't have a specific reservation, then before you deploy the cluster, you can follow the example in `cluster-toolkit/examples/gke-a4/gke-a4-deployment.yaml` to use an alternative consumption option, such as [Spot VMs](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-consumption-options#spot-vms) or [Flex-start VMs](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-consumption-options#dws-flex-start). For configuration instructions, see [GKE consumption options](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-consumption-options).

  5. Change to the `cluster-toolkit` directory, deploy the GKE cluster by using the [`gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy), and then return to your working directory:
         
         cd cluster-toolkit
         ./gcluster deploy \
             -d gke-a4-deployment.yaml \
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
         
         echo "Waiting for Dynamo operator and Grove operator deployments to become Available..."
         kubectl wait --for=condition=Available deployment/dynamo-platform-dynamo-operator-controller-manager --timeout=300s || true
         kubectl wait --for=condition=Available deployment/grove-operator --timeout=300s || true




## Stage the model weights in Cloud Storage

Stage the `nvidia/Llama-3.1-405B-Instruct-FP8` checkpoint in your in-region Cloud Storage bucket (`gs://${GCS_BUCKET}`). This lets the inference worker Pods mount the weights with Cloud Storage FUSE instead of downloading them from Hugging Face on every cold start:

  1. Grant the Storage Object User role (`roles/storage.objectUser`) on the `gs://${GCS_BUCKET}` bucket that you created in Create the GKE cluster to the Google service account bound to the `workload-identity-k8s-sa` Kubernetes service account:
         
         GSA=$(kubectl get sa workload-identity-k8s-sa -o jsonpath='{.metadata.annotations.iam\.gke\.io/gcp-service-account}')
         gcloud storage buckets add-iam-policy-binding "gs://${GCS_BUCKET}" \
             --member="serviceAccount:${GSA}" \
             --role="roles/storage.objectUser"

  2. Download the `llama3.1-405b-stage-weights-job.yaml` and `llama3.1-405b-singlehost-a4-gcsfuse.yaml` manifests:
         
         curl -O https://raw.githubusercontent.com/GoogleCloudSamples/AIHypercomputerSamples/refs/heads/main/gpu/inference/llama3-405b/llama3.1-405b-stage-weights-job.yaml
         curl -O https://raw.githubusercontent.com/GoogleCloudSamples/AIHypercomputerSamples/refs/heads/main/gpu/inference/llama3-405b/llama3.1-405b-singlehost-a4-gcsfuse.yaml

Alternatively, create a file named `llama3.1-405b-stage-weights-job.yaml` with the following content. This Indexed Job runs two parallel Pods across your two A4 nodes. Each Pod downloads a size-balanced slice of the `nvidia/Llama-3.1-405B-Instruct-FP8` checkpoint to the node's Local NVMe SSD and uploads it to `gs://${GCS_BUCKET}/hf_models/models--nvidia--llama-3_1-405b-instruct-fp8` by using `gcloud storage rsync`:
         
         # ==============================================================================
         # Stage nvidia/Llama-3.1-405B-Instruct-FP8 (~430 GB, 86 safetensors shards) from
         # Hugging Face Hub into an in-region Cloud Storage bucket for
         # llama3.1-405b-singlehost-a4-gcsfuse.yaml
         #
         # Each Indexed Job pod downloads a size-balanced slice of the repo onto the node's
         # local NVMe SSD, then uploads that slice with `gcloud storage rsync`.
         # ==============================================================================
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: llama3-405b-stage-weights
         spec:
           completionMode: Indexed
           completions: 2
           parallelism: 2
           backoffLimitPerIndex: 2
           template:
             metadata:
               labels:
                 app: llama3-405b-stage-weights
             spec:
               restartPolicy: Never
               serviceAccountName: workload-identity-k8s-sa
               nodeSelector:
                 cloud.google.com/gke-accelerator: nvidia-b200
               tolerations:
                 - key: "nvidia.com/gpu"
                   operator: "Exists"
                   effect: "NoSchedule"
               topologySpreadConstraints:
                 - maxSkew: 1
                   topologyKey: kubernetes.io/hostname
                   whenUnsatisfiable: DoNotSchedule
                   labelSelector:
                     matchLabels:
                       app: llama3-405b-stage-weights
               initContainers:
                 - name: download
                   image: nvcr.io/nvidia/ai-dynamo/sglang-runtime:1.5.0
                   command: ["python3", "-c"]
                   args:
                     - |
                       import os, time
                       from huggingface_hub import HfApi, snapshot_download
                       repo = os.environ["REPO_ID"]
                       n = int(os.environ["NUM_SHARDS"])
                       i = int(os.environ["JOB_COMPLETION_INDEX"])
                       info = HfApi().model_info(repo, files_metadata=True)
                       files = sorted(((s.size or 0, s.rfilename) for s in info.siblings), reverse=True)
                       bins = [[0, []] for _ in range(n)]
                       for size, name in files:
                           b = min(bins, key=lambda x: x[0])
                           b[0] += size
                           b[1].append(name)
                       size, mine = bins[i]
                       print(f"shard {i}/{n}: {len(mine)} files, {size / 1e9:.1f} GB", flush=True)
                       for attempt in range(1, 7):
                           try:
                               snapshot_download(repo, local_dir="/ssd/model", allow_patterns=mine, max_workers=16)
                               break
                           except Exception as e:
                               print(f"shard {i}/{n}: attempt {attempt} failed: {e!r}", flush=True)
                               if attempt == 6:
                                   raise
                               time.sleep(30)
                       print(f"shard {i}/{n}: download complete", flush=True)
                   env:
                     - name: REPO_ID
                       value: "nvidia/Llama-3.1-405B-Instruct-FP8"
                     - name: NUM_SHARDS
                       value: "2"
                     - name: HF_HOME
                       value: "/ssd/hf"
                     - name: HF_HUB_DISABLE_XET
                       value: "1"
                     - name: HF_TOKEN
                       valueFrom:
                         secretKeyRef:
                           name: hf-secret
                           key: hf_api_token
                           optional: true
                   resources:
                     requests:
                       cpu: "16"
                       memory: "64Gi"
                       ephemeral-storage: "300Gi"
                     limits:
                       cpu: "16"
                       memory: "64Gi"
                       ephemeral-storage: "500Gi"
                   volumeMounts:
                     - name: ssd
                       mountPath: /ssd
               containers:
                 - name: upload
                   image: gcr.io/google.com/cloudsdktool/google-cloud-cli:slim
                   command: ["/bin/bash", "-c"]
                   args:
                     - |
                       set -euo pipefail
                       gcloud storage rsync --recursive --exclude='^\.cache/.*' /ssd/model "${DEST}"
                       echo "shard ${JOB_COMPLETION_INDEX}: upload complete"
                   env:
                     - name: DEST
                       value: "gs://${GCS_BUCKET}/hf_models/models--nvidia--llama-3_1-405b-instruct-fp8"
                   resources:
                     requests:
                       cpu: "16"
                       memory: "32Gi"
                     limits:
                       cpu: "16"
                       memory: "32Gi"
                   volumeMounts:
                     - name: ssd
                       mountPath: /ssd
               volumes:
                 - name: ssd
                   emptyDir: {}

  3. Substitute your Cloud Storage bucket name into `llama3.1-405b-stage-weights-job.yaml`, start the staging Job, and wait for both Pods to finish uploading the weights:
         
         envsubst '${GCS_BUCKET}' < llama3.1-405b-stage-weights-job.yaml | kubectl apply -f -
         
         kubectl wait --for=condition=complete job/llama3-405b-stage-weights --timeout=2h

It takes approximately 10 to 15 minutes to download the model weights to Local NVMe SSD and upload them to Cloud Storage.

  4. Optional: While the staging Job is running, stream the logs of the Job in a second terminal session to monitor the download and upload progress:
         
         until kubectl logs -l job-name=llama3-405b-stage-weights -c download >/dev/null 2>&1; do sleep 2; done
         kubectl logs -f -l job-name=llama3-405b-stage-weights -c download --prefix
         
         until kubectl logs -l job-name=llama3-405b-stage-weights -c upload >/dev/null 2>&1; do sleep 2; done
         kubectl logs -f -l job-name=llama3-405b-stage-weights -c upload --prefix

  5. After the Job has completed, verify that all 86 `.safetensors` shards are present in your Cloud Storage bucket:
         
         gcloud storage ls "gs://${GCS_BUCKET}/hf_models/models--nvidia--llama-3_1-405b-instruct-fp8/*.safetensors" | wc -l

  6. Delete the completed staging Job:
         
         kubectl delete job llama3-405b-stage-weights




## Deploy the single-host disaggregated SGLang server

The workload manifest (`llama3.1-405b-singlehost-a4-gcsfuse.yaml`) defines a Kubernetes ResourceClaimTemplate (`all-mrdma`). This template allocates the node's multi-NIC RDMA devices (`mrdma.google.com`) through DRA, Role and RoleBinding resources for the `workload-identity-k8s-sa` service account, and an NVIDIA Dynamo DynamoGraphDeployment (`llama3-405b-a4-disagg`) with Grove gang scheduling. The deployment consists of the following:

  * **Frontend (`Frontend`)**: runs one router replica that accepts client requests, discovers registered prefill and decode workers, and coordinates disaggregated request routing.
  * **Prefill worker (`Prefill`)**: runs a single-host worker on one `a4-highgpu-8g` node with eight NVIDIA B200 GPUs. The Pod mounts the staged `nvidia/Llama-3.1-405B-Instruct-FP8` weights from your Cloud Storage bucket at `/model-weights` by using the Cloud Storage FUSE CSI driver (`gcsfuse.csi.storage.gke.io`) with Local NVMe SSD file caching, sources the NCCL/gIB environment, and launches `python3 -m dynamo.sglang` in `--disaggregation-mode prefill` with the following flags: 
    * `--served-model-name "nvidia/Llama-3.1-405B-Instruct-FP8"`
    * `--tensor-parallel-size 8`
    * `--kv-cache-dtype fp8_e4m3`
    * `--context-length 16384`
    * `--mem-fraction-static 0.85`
  * **Decode worker (`Decode`)**: runs a single-host worker on the second `a4-highgpu-8g` node with eight NVIDIA B200 GPUs. The Pod mounts the staged model weights from Cloud Storage at `/model-weights` through the Cloud Storage FUSE CSI driver and launches `python3 -m dynamo.sglang` in `--disaggregation-mode decode` with the following flags: 
    * `--served-model-name "nvidia/Llama-3.1-405B-Instruct-FP8"`
    * `--tensor-parallel-size 8`
    * `--kv-cache-dtype fp8_e4m3`
    * `--context-length 16384`
    * `--mem-fraction-static 0.85`



Deploy and monitor the disaggregated inference server:

  1. Review the `llama3.1-405b-singlehost-a4-gcsfuse.yaml` workload manifest that you downloaded earlier. Alternatively, create a file named `llama3.1-405b-singlehost-a4-gcsfuse.yaml` with the following content:
         
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
         apiVersion: rbac.authorization.k8s.io/v1
         kind: Role
         metadata:
           name: dynamo-workload-identity-discovery-role
           namespace: default
         rules:
           - apiGroups: [""]
             resources: ["endpoints", "pods"]
             verbs: ["get", "list", "watch"]
           - apiGroups: ["discovery.k8s.io"]
             resources: ["endpointslices"]
             verbs: ["get", "list", "watch"]
           - apiGroups: ["nvidia.com"]
             resources: ["dynamoworkermetadatas"]
             verbs: ["create", "get", "list", "watch", "update", "patch", "delete"]
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: RoleBinding
         metadata:
           name: dynamo-workload-identity-discovery-binding
           namespace: default
         roleRef:
           apiGroup: rbac.authorization.k8s.io
           kind: Role
           name: dynamo-workload-identity-discovery-role
         subjects:
           - kind: ServiceAccount
             name: workload-identity-k8s-sa
             namespace: default
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
               extraPodMetadata:
                 annotations:
                   gke-gcsfuse/volumes: "true"
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
                   value: "/model-weights/hf_models/models--nvidia--llama-3_1-405b-instruct-fp8"
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
               extraPodSpec:
                 serviceAccountName: workload-identity-k8s-sa
                 automountServiceAccountToken: true
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
         
                       # --host 0.0.0.0 is required so MooncakeKVBootstrapServer binds to 0.0.0.0:30001 instead of 127.0.0.1:30001.
                       echo "=== [Dynamo Prefill Worker] Launching dynamo.sglang ==="
                       exec python3 -m dynamo.sglang \
                         --model-path "${MODEL_PATH}" \
                         --served-model-name "nvidia/Llama-3.1-405B-Instruct-FP8" \
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
                     - name: gcs-model-dir
                       mountPath: /model-weights
                       readOnly: true
                 volumes:
                   - name: library-dir-host
                     hostPath:
                       path: /home/kubernetes/bin/nvidia
                   - name: gib
                     hostPath:
                       path: /home/kubernetes/bin/gib
                   - name: gcs-model-dir
                     csi:
                       driver: gcsfuse.csi.storage.gke.io
                       readOnly: true
                       volumeAttributes:
                         bucketName: ${GCS_BUCKET}
                         mountOptions: "implicit-dirs,file-cache:max-size-mb:-1"
         
             # --------------------------------------------------------------------------
             # DECODE WORKER: 1 x GPU A4 (`a4-highgpu-8g`, 8 x B200 GPUs, TP=8)
             # --------------------------------------------------------------------------
             Decode:
               componentType: worker
               subComponentType: decode
               replicas: 1
               extraPodMetadata:
                 annotations:
                   gke-gcsfuse/volumes: "true"
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
                   value: "/model-weights/hf_models/models--nvidia--llama-3_1-405b-instruct-fp8"
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
               extraPodSpec:
                 serviceAccountName: workload-identity-k8s-sa
                 automountServiceAccountToken: true
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
         
                       echo "=== [Dynamo Decode Worker] Launching dynamo.sglang ==="
                       exec python3 -m dynamo.sglang \
                         --model-path "${MODEL_PATH}" \
                         --served-model-name "nvidia/Llama-3.1-405B-Instruct-FP8" \
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
                     - name: gcs-model-dir
                       mountPath: /model-weights
                       readOnly: true
                 volumes:
                   - name: library-dir-host
                     hostPath:
                       path: /home/kubernetes/bin/nvidia
                   - name: gib
                     hostPath:
                       path: /home/kubernetes/bin/gib
                   - name: gcs-model-dir
                     csi:
                       driver: gcsfuse.csi.storage.gke.io
                       readOnly: true
                       volumeAttributes:
                         bucketName: ${GCS_BUCKET}
                         mountOptions: "implicit-dirs,file-cache:max-size-mb:-1"

  2. Substitute your Cloud Storage bucket name into `llama3.1-405b-singlehost-a4-gcsfuse.yaml` and apply the workload manifest to your cluster:
         
         envsubst '${GCS_BUCKET}' < llama3.1-405b-singlehost-a4-gcsfuse.yaml | kubectl apply -f -

  3. Before you send any inference requests, poll the frontend, prefill, and decode Pods to determine when the server is ready:
         
         until [[ $(kubectl get pods -l nvidia.com/dynamo-component-type --no-headers 2>/dev/null | wc -l) -eq 3 ]]; do sleep 2; done
         frontend_pod=$(kubectl get pods -l "nvidia.com/dynamo-component-type=frontend" -o jsonpath='{.items[*].metadata.name}')
         prefill_pod=$(kubectl get pods -l "nvidia.com/dynamo-sub-component-type=prefill" -o jsonpath='{.items[*].metadata.name}')
         decode_pod=$(kubectl get pods -l "nvidia.com/dynamo-sub-component-type=decode" -o jsonpath='{.items[*].metadata.name}')
         echo "Created frontend/prefill/decode pods:"
         echo "  Frontend: ${frontend_pod}"
         echo "  Prefill:  ${prefill_pod}"
         echo "  Decode:   ${decode_pod}"
         echo ""
         echo "Waiting for pods to be ready..."
         kubectl wait --for=condition=Ready pod "${frontend_pod}" "${prefill_pod}" "${decode_pod}" --timeout=3600s

On a cold start, it takes approximately 5 to 10 minutes to stream the 405B FP8 model weights (~430 GB across 86 shards) from Cloud Storage through Cloud Storage FUSE and initialize the SGLang servers. Before you send any requests, wait until the frontend Pod shows `1/1` and the prefill and decode Pods show `2/2` in the `READY` column of `kubectl get pods`:
         
         NAME                                        READY   STATUS    RESTARTS   AGE
         llama3-405b-a4-disagg-0-decode-tgl7q        2/2     Running   0          6m
         llama3-405b-a4-disagg-0-frontend-wrxq5      1/1     Running   0          6m
         llama3-405b-a4-disagg-0-prefill-67h5s       2/2     Running   0          6m
         

  4. Optional: To monitor weight loading and server initialization, in a second terminal session, stream the logs of the prefill and decode Pods:
         
         # monitor prefill pod
         kubectl logs -f -c main --tail=-1 \
         $(kubectl get pods -l "nvidia.com/dynamo-sub-component-type=prefill" -o jsonpath='{.items[*].metadata.name}')
         
         # monitor decode pod
         kubectl logs -f -c main --tail=-1 \
         $(kubectl get pods -l "nvidia.com/dynamo-sub-component-type=decode" -o jsonpath='{.items[*].metadata.name}')

**Note:** The prefill and decode Pods might not output logs while they load the model weights. To stop streaming logs at any time, press `Control+C`.



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
         
         kubectl delete -f llama3.1-405b-singlehost-a4-gcsfuse.yaml --ignore-not-found || true

  2. Uninstall the NVIDIA Dynamo platform and KAI Scheduler Helm releases:
         
         helm uninstall dynamo-platform kai-scheduler || true

  3. Delete the Hugging Face Kubernetes Secret:
         
         kubectl delete secret hf-secret --ignore-not-found || true

  4. From the `cluster-toolkit` directory, destroy the GKE cluster and its associated infrastructure by using the [`gcluster destroy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-destroy):
         
         cd cluster-toolkit
         ./gcluster destroy "${CLUSTER_NAME}" --auto-approve || true
         cd ..

  5. To delete the Cloud Storage bucket that stores the staged model weights and the Terraform state, use the [`gcloud storage rm` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rm):
         
         gcloud storage rm --recursive "gs://${GCS_BUCKET}"




## What's next

  * Learn more about [NVIDIA Dynamo](https://github.com/ai-dynamo/dynamo).
  * Learn more about [SGLang](https://github.com/sgl-project/sglang).
  * Learn more about [A4 VMs with NVIDIA B200 GPUs](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms).
  * Learn more about [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview).
  * Learn more about [managing AI-optimized GKE clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/manage-gke-clusters).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 

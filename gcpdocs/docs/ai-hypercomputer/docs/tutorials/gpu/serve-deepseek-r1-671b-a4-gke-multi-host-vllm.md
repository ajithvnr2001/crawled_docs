---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/serve-deepseek-r1-671b-a4-gke-multi-host-vllm/
title: Serve DeepSeek-R1 671B on GKE with multi-host vLLM on A4 VMs \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:40:54.438107+00:00
---

# Serve DeepSeek-R1 671B on GKE with multi-host vLLM on A4 VMs  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/serve-deepseek-r1-671b-a4-gke-multi-host-vllm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Serve DeepSeek-R1 671B on GKE with multi-host vLLM on A4 VMs Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This tutorial shows you how to deploy and serve [DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) (`deepseek-ai/DeepSeek-R1`), a 671 billion-parameter Mixture-of-Experts model with 37 billion active parameters, on Google Kubernetes Engine (GKE) on Google Cloud. The deployment uses Cluster Toolkit, two multi-host [A4 (`a4-highgpu-8g`)](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms) virtual machine (VM) instances with a total of 16 NVIDIA B200 GPUs, and the [vLLM serving framework](https://github.com/vllm-project/vllm).

In the deployment configuration that's described in this tutorial, you use Cluster Toolkit to provision a GKE cluster in Standard mode. The cluster has two `a4-highgpu-8g` nodes connected over GPUDirect Remote Direct Memory Access (RDMA) networking. You then stage the model weights in Cloud Storage and use the Kubernetes JobSet API and Ray to serve the model across all 16 NVIDIA B200 GPUs with tensor parallelism, expert parallelism, and an FP8 KV cache.

## Objectives

  * Install Cluster Toolkit and provision a multi-host A4 GKE cluster in Standard mode.
  * Stage the DeepSeek-R1 model weights in a Cloud Storage bucket.
  * Deploy a multi-host vLLM inference server with JobSet and Ray across two A4 nodes, with a total of 16 NVIDIA B200 GPUs.
  * Send a chat completion request to the vLLM server.
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

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) and [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the Google Cloud CLI, and install [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl). If you use Cloud Shell, both tools are preinstalled.
  2. If you're running this tutorial from a Linux or macOS workstation rather than Cloud Shell, install the required [Cluster Toolkit dependencies](https://docs.cloud.google.com/cluster-toolkit/docs/setup/install-dependencies) (such as Terraform and Git).
  3. Enable the Kubernetes Engine API, Compute Engine API, Cloud Storage API, Artifact Registry API, and Service Usage API in your Google Cloud project:

[Enable APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,compute.googleapis.com,storage.googleapis.com,artifactregistry.googleapis.com,serviceusage.googleapis.com)


**Important:** To complete this tutorial, you must have capacity for two A4 (`a4-highgpu-8g`) VMs (16 NVIDIA B200 GPUs) in your Google Cloud project. This tutorial uses a specific reservation, but you can also use Spot capacity or Flex-start VMs if available. To learn more about your options for reserving capacity in AI Hypercomputer, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).

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

Set up your authentication and environment variables for the tutorial:

  1. Set up your authentication:
         
         gcloud auth login
         gcloud auth application-default login

  2. Export the environment variables that you use throughout this tutorial:
         
         export PROJECT_ID="YOUR_PROJECT_ID"
         export REGION="YOUR_REGION"
         export ZONE="YOUR_ZONE"
         export CLUSTER_NAME="YOUR_CLUSTER_NAME"
         export RESERVATION_NAME="YOUR_RESERVATION_NAME"
         export HF_TOKEN="YOUR_HF_TOKEN"
         export MODEL_BUCKET="YOUR_GCS_BUCKET"
         export TERRAFORM_BUCKET="${MODEL_BUCKET}-tf-state"
         export CLUSTER_TOOLKIT_VERSION="v1.104.0"
         
         gcloud config set project "${PROJECT_ID}"
         gcloud config set billing/quota_project "${PROJECT_ID}"

Replace the following:

     * `YOUR_PROJECT_ID`: the ID of your Google Cloud project.
     * `YOUR_REGION`: the compute region where your A4 capacity is located and where you want to deploy your cluster, such as `us-central1`.
     * `YOUR_ZONE`: the compute zone where your A4 capacity is located, such as `us-central1-b`.
     * `YOUR_CLUSTER_NAME`: the name for your GKE cluster and Cluster Toolkit deployment. Use a name of 20 characters or fewer so that the generated node pool service account ID (`YOUR_CLUSTER_NAME-gke-np-sa`) stays within the 30-character Identity and Access Management (IAM) limit.
     * `YOUR_RESERVATION_NAME`: the name of your A4 reservation, or the extended reservation block path in the format `RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME`.
     * `YOUR_HF_TOKEN`: your Hugging Face access token.
     * `YOUR_GCS_BUCKET`: a globally unique name for the Cloud Storage bucket where you stage the model weights. The script also sets `TERRAFORM_BUCKET` to `YOUR_GCS_BUCKET-tf-state` to store the Terraform state for Cluster Toolkit.

The script also sets `CLUSTER_TOOLKIT_VERSION` to `v1.104.0`, which specifies the Cluster Toolkit version to install. Cluster Toolkit version `v1.104.0` and later include built-in capacity consumption options for `examples/gke-a4/gke-a4-deployment.yaml`. In versions earlier than `v1.104.0`, you must add these capacity options manually.


**Note:** If you use Cloud Shell and your home directory runs low on disk space, you can switch to an ephemeral Cloud Shell session from the Cloud Shell toolbar by clicking the **More** menu and selecting **Ephemeral mode**.

## Create the GKE cluster

Download Cluster Toolkit and provision a GKE cluster in Standard mode with two `a4-highgpu-8g` nodes, GPUDirect RDMA networking, and the JobSet controller:

  1. Download and extract the prebuilt Cluster Toolkit bundle for the version specified in `CLUSTER_TOOLKIT_VERSION` (`v1.104.0`), change your working directory to the `cluster-toolkit` directory, and verify the binary version:
         
         case "$(uname -s)-$(uname -m)" in
           Linux-x86_64)              BUNDLE="gcluster_bundle_linux_amd64.tgz" ;;
           Linux-aarch64|Linux-arm64) BUNDLE="gcluster_bundle_linux_arm64.tgz" ;;
           Darwin-x86_64)             BUNDLE="gcluster_bundle_mac_amd64.tgz" ;;
           Darwin-arm64)              BUNDLE="gcluster_bundle_mac_arm64.tgz" ;;
           *) BUNDLE=""; echo "Unsupported platform: $(uname -s)-$(uname -m)" >&2 ;;
         esac
         mkdir -p cluster-toolkit
         curl -fsSL "https://github.com/GoogleCloudPlatform/cluster-toolkit/releases/download/${CLUSTER_TOOLKIT_VERSION}/${BUNDLE:?}" \
           | tar -xz -C cluster-toolkit
         cd cluster-toolkit
         ./gcluster --version

  2. Optionally, view the available commands and flags in Cluster Toolkit:
         
         ./gcluster --help

  3. Create the Cloud Storage bucket that stores the Terraform state for your Cluster Toolkit deployment:
         
         gcloud storage buckets create "gs://${TERRAFORM_BUCKET}" \
             --default-storage-class=STANDARD \
             --project="${PROJECT_ID}" \
             --location="${REGION}" \
             --uniform-bucket-level-access

  4. Create the `examples/gke-a4/gke-a4-deployment.yaml` deployment configuration file for two `a4-highgpu-8g` nodes:
         
         cat <<EOF > examples/gke-a4/gke-a4-deployment.yaml
         terraform_backend_defaults:
           type: gcs
           configuration:
             bucket: ${TERRAFORM_BUCKET}
         
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

**Note:** Cluster Toolkit version `v1.104.0` and later include built-in capacity consumption options for `examples/gke-a4/gke-a4-deployment.yaml` (see [GKE consumption options](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-consumption-options)). In versions earlier than `v1.104.0`, you must add these capacity options manually.

By default, the `examples/gke-a4/gke-a4.yaml` blueprint is configured to use a specific reservation. If you don't have a specific reservation, you can edit `examples/gke-a4/gke-a4.yaml` before you deploy the cluster to use one of the following consumption options:

     * **Spot capacity** : ensure that your project has sufficient [preemptible quota](https://docs.cloud.google.com/compute/docs/instances/spot#quotas) for your GPUs, disks, and CPUs. At the bottom of `examples/gke-a4/gke-a4.yaml`, comment out the `--- Option 1: Specific Reservation ---` section and uncomment the `--- Option 4: Spot ---` section.
     * **Flex-start VMs** : ensure that your project has sufficient [preemptible quota](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms#quota) for your GPUs, disks, and CPUs. At the bottom of `examples/gke-a4/gke-a4.yaml`, comment out the `--- Option 1: Specific Reservation ---` section and uncomment the `--- Option 2: DWS Flex Start ---` section.
  5. Deploy the GKE cluster by using the [`gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy):
         
         ./gcluster deploy -d examples/gke-a4/gke-a4-deployment.yaml examples/gke-a4/gke-a4.yaml \
             --download-dependencies \
             --auto-approve -w

Cluster creation takes approximately 30 to 45 minutes. If you run `./gcluster deploy` without the `--auto-approve` flag, then to apply the proposed changes, enter `a` when you're prompted to. When deployment finishes, the output ends with a message similar to the following:
         
         Apply complete! Resources: 80 added, 0 changed, 0 destroyed.
         

  6. Configure `kubectl` credentials to communicate with your cluster:
         
         gcloud container clusters get-credentials "${CLUSTER_NAME}" \
             --project="${PROJECT_ID}" \
             --location="${REGION}"




## Stage the model weights in Cloud Storage

Download the DeepSeek-R1 weights onto the Local SSD of one of your A4 nodes and transfer them to a Cloud Storage bucket for fast streaming across nodes:

  1. Download the Kubernetes manifest files for the model download Job, the vLLM inference server, and the benchmark Pods:
         
         curl -LO https://raw.githubusercontent.com/GoogleCloudSamples/AIHypercomputerSamples/main/gpu/inference/deepseek-r1-gcluster/download_model.yaml
         curl -LO https://raw.githubusercontent.com/GoogleCloudSamples/AIHypercomputerSamples/main/gpu/inference/deepseek-r1-gcluster/deepseek_r1_server.yaml
         curl -LO https://raw.githubusercontent.com/GoogleCloudSamples/AIHypercomputerSamples/main/gpu/inference/deepseek-r1-gcluster/deepseek_r1_8k_1k.yaml

  2. Create the Cloud Storage bucket with uniform bucket-level access to store the model weights:
         
         gcloud storage buckets create "gs://${MODEL_BUCKET}" \
             --project="${PROJECT_ID}" \
             --location="${REGION}" \
             --uniform-bucket-level-access

  3. Grant IAM permissions on the bucket to the default Kubernetes service account, the default Compute Engine service account, and the cluster node pool service account (`${CLUSTER_NAME}-gke-np-sa`):
         
         PROJECT_NUMBER=$(gcloud projects describe "${PROJECT_ID}" --format="value(projectNumber)")
         
         gcloud storage buckets add-iam-policy-binding "gs://${MODEL_BUCKET}" \
             --member="principal://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${PROJECT_ID}.svc.id.goog/subject/ns/default/sa/default" \
             --role="roles/storage.objectAdmin"
         
         gcloud storage buckets add-iam-policy-binding "gs://${MODEL_BUCKET}" \
             --member="serviceAccount:${PROJECT_NUMBER}-compute@developer.gserviceaccount.com" \
             --role="roles/storage.objectAdmin"
         
         gcloud storage buckets add-iam-policy-binding "gs://${MODEL_BUCKET}" \
             --member="serviceAccount:${CLUSTER_NAME}-gke-np-sa@${PROJECT_ID}.iam.gserviceaccount.com" \
             --role="roles/storage.objectAdmin"
         
         # legacyBucketReader is required to load the model with --load-format runai_streamer
         gcloud storage buckets add-iam-policy-binding "gs://${MODEL_BUCKET}" \
             --member="serviceAccount:${CLUSTER_NAME}-gke-np-sa@${PROJECT_ID}.iam.gserviceaccount.com" \
             --role="roles/storage.legacyBucketReader"

The IAM permissions granted by the preceding script include the Storage Legacy Bucket Reader role (`roles/storage.legacyBucketReader`), which is required for `--load-format runai_streamer`.

  4. Create a Kubernetes Secret named `hf-secret` to store your Hugging Face access token:
         
         kubectl create secret generic hf-secret \
             --from-literal=hf_api_token="${HF_TOKEN}" \
             --dry-run=client -o yaml | kubectl apply -f -

  5. Review the `download_model.yaml` manifest, or create the file locally if you didn't download it earlier:
         
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: download-deepseek-r1
           namespace: default
         spec:
           backoffLimit: 1
           template:
             spec:
               restartPolicy: OnFailure
               # Schedule onto an A4 node with Local SSD
               nodeSelector:
                 cloud.google.com/gke-accelerator: nvidia-b200
               tolerations:
               - operator: Exists
               containers:
               - name: model-downloader
                 image: gcr.io/google.com/cloudsdktool/google-cloud-cli:slim
                 env:
                 - name: HF_TOKEN
                   valueFrom:
                     secretKeyRef:
                       name: hf-secret
                       key: hf_api_token
                 # Enable high-performance concurrent chunked downloads in huggingface_hub
                 - name: HF_XET_HIGH_PERFORMANCE
                   value: "1"
                 # Place Hugging Face cache on Local SSD so the boot disk never fills up
                 - name: HF_HOME
                   value: "/local-ssd/hf-cache"
                 command: ["/bin/bash", "-c"]
                 args:
                 - |
                   set -euo pipefail
         
                   echo "=== 1. Installing huggingface_hub ==="
                   pip3 install --break-system-packages -q -U "huggingface_hub"
         
                   echo "=== 2. Downloading deepseek-ai/DeepSeek-R1 to Local NVMe SSD ==="
                   hf download deepseek-ai/DeepSeek-R1 --local-dir /local-ssd/DeepSeek-R1
                   rm -rf /local-ssd/DeepSeek-R1/.cache
         
                   echo "=== 3. Uploading from Local SSD to GCS ==="
                   gcloud config set storage/parallel_composite_upload_compatibility_check False
                   gcloud storage cp -r /local-ssd/DeepSeek-R1 gs://$MODEL_BUCKET/
         
                   echo "=== 4. Cleaning up Local SSD ==="
                   rm -rf /local-ssd/DeepSeek-R1 /local-ssd/hf-cache
                 resources:
                   requests:
                     cpu: "64"
                     memory: "128Gi"
                 volumeMounts:
                 - name: local-ssd
                   mountPath: /local-ssd
               volumes:
               - name: local-ssd
                 emptyDir: {}

  6. Substitute your Cloud Storage bucket name into the `download_model.yaml` manifest and start the model download Job:
         
         envsubst '$MODEL_BUCKET' < download_model.yaml | kubectl apply -f -

  7. Wait for the download Pod to start, and then stream the Job logs:
         
         kubectl wait --for=condition=Ready pod -l job-name=download-deepseek-r1 --timeout=120s
         kubectl logs -f job/download-deepseek-r1

It takes approximately 30 to 40 minutes to download the model to the node's Local NVMe SSD and upload the weights to your Cloud Storage bucket.

  8. After the Job has completed, verify that all 163 `.safetensors` shards are present in your Cloud Storage bucket:
         
         gcloud storage ls "gs://${MODEL_BUCKET}/DeepSeek-R1/*.safetensors" | wc -l

  9. Delete the completed staging Job:
         
         kubectl delete job download-deepseek-r1




## Deploy the multi-host vLLM server

The workload manifest (`deepseek_r1_server.yaml`) defines a ClusterIP Service (`vllm-r1-leader`) and a Kubernetes JobSet (`vllm-r1`) that coordinate multi-host serving across the two `a4-highgpu-8g` nodes:

  * **Leader (`leader`)**: runs one replica on an A4 node with eight NVIDIA B200 GPUs, sources the NCCL/gIB environment (`/usr/local/gib/scripts/set_nccl_env.sh`), starts the Ray head node on port `6379` for a two-node cluster, and launches `vllm serve` on HTTP port `8080`. The server streams weights directly from `gs://$MODEL_BUCKET/DeepSeek-R1` by using `--load-format runai_streamer` and loads the tokenizer from the mounted Cloud Storage FUSE volume at `/models/DeepSeek-R1`. It runs with `--tensor-parallel-size 16`, `--pipeline-parallel-size 1`, `--distributed-executor-backend ray`, `--enable-expert-parallel`, `--kv-cache-dtype fp8_e4m3`, `--async-scheduling`, and CUDA graphs (`FULL_AND_PIECEWISE`).
  * **Worker (`worker`)**: runs one headless replica on the second A4 node with eight NVIDIA B200 GPUs, configures NCCL/gIB, and joins the leader's Ray cluster at `vllm-r1-leader:6379`.



Deploy and monitor the multi-host vLLM server:

  1. Review the `deepseek_r1_server.yaml` manifest, or create the file locally if you didn't download it earlier:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: vllm-r1-leader
           namespace: default
           labels:
             app: vllm-r1
         spec:
           ports:
           - name: http
             port: 8080
             targetPort: 8080
           - name: ray-head
             port: 6379
             targetPort: 6379
           selector:
             app: vllm-r1
             role: leader
           type: ClusterIP
         ---
         apiVersion: jobset.x-k8s.io/v1alpha2
         kind: JobSet
         metadata:
           name: vllm-r1
           namespace: default
           labels:
             app: vllm-r1
         spec:
           failurePolicy:
             maxRestarts: 3
             restartStrategy: Recreate
           network:
             enableDNSHostnames: true
             publishNotReadyAddresses: true
           replicatedJobs:
           # -------------------- LEADER --------------------
           - name: leader
             replicas: 1
             template:
               spec:
                 parallelism: 1
                 completions: 1
                 backoffLimit: 1
                 template:
                   metadata:
                     labels:
                       app: vllm-r1
                       role: leader
                     annotations:
                       gke-gcsfuse/volumes: "true"
                   spec:
                     hostNetwork: true
                     dnsPolicy: ClusterFirstWithHostNet
                     hostIPC: true
                     nodeSelector:
                       cloud.google.com/gke-accelerator: nvidia-b200
                     tolerations:
                     - key: nvidia.com/gpu
                       operator: Exists
                     - key: cloud.google.com/impending-node-termination
                       operator: Exists
                     - effect: NoSchedule
                       key: cloud.google.com/gke-queued
                       value: "true"
                     containers:
                     - name: vllm-leader
                       image: docker.io/vllm/vllm-openai@sha256:61fc8a896b0a4fbbbdc063bc4b0dbc25ce98e02b5050c24aeb7830ac02039b14
                       imagePullPolicy: IfNotPresent
                       securityContext:
                         privileged: true
                       env:
                       - name: PYTHONUNBUFFERED
                         value: "1"
                       - name: NCCL_DEBUG
                         value: "INFO"
                       - name: VLLM_ENGINE_READY_TIMEOUT_S
                         value: "1800"
                       - name: VLLM_RPC_TIMEOUT
                         value: "1800000"
                       - name: HF_TOKEN
                         valueFrom:
                           secretKeyRef:
                             name: hf-secret
                             key: hf_api_token
                       command: ["/bin/bash", "-c"]
                       args:
                       - |
                         set -e
                         echo "precedence ::ffff:0:0/96  100" >> /etc/gai.conf 2>/dev/null || true
                         ulimit -l unlimited || true
                         export LD_LIBRARY_PATH=/usr/local/gib/lib64:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH:-}
                         source /usr/local/gib/scripts/set_nccl_env.sh
                         export GLOO_SOCKET_IFNAME=eth0
                         export NCCL_SOCKET_IFNAME=eth0
                         export VLLM_HOST_IP=$(hostname -I | awk '{print $1}')
                         echo "=== Starting Optimized vLLM Server with Ray (Leader, rank 0) ==="
                         echo "Host IP: ${VLLM_HOST_IP}"
                         # 0. Install Ray with Compiled Graph support (not pre-installed in vLLM 0.28.0 image)
                         uv pip install --system "ray[cgraph]"
                         # 1. Start Ray head on port 6379 and wait until all 2 nodes (16 GPUs) join
                         bash /vllm-workspace/examples/ray_serving/multi-node-serving.sh leader \
                           --ray_cluster_size=2 \
                           --ray_port=6379 \
                           --node-ip-address="${VLLM_HOST_IP}"
                         # 2. Launch vLLM on the Leader using the Ray cluster
                         exec vllm serve \
                           --host 0.0.0.0 \
                           --port 8080 \
                           --model gs://$MODEL_BUCKET/DeepSeek-R1 \
                           --tokenizer /models/DeepSeek-R1 \
                           --load-format runai_streamer \
                           --model-loader-extra-config '{"distributed": true, "concurrency": 16, "memory_limit": 34359738368}' \
                           --served-model-name deepseek-ai/DeepSeek-R1 \
                           --tensor-parallel-size 16 \
                           --pipeline-parallel-size 1 \
                           --distributed-executor-backend ray \
                           --async-scheduling \
                           --disable-custom-all-reduce \
                           --kv-cache-dtype fp8_e4m3 \
                           --block-size 128 \
                           --enable-expert-parallel \
                           --max-num-batched-tokens 8192 \
                           --max-num-seqs 160 \
                           --compilation-config '{"mode": 3, "cudagraph_mode":"FULL_AND_PIECEWISE", "custom_ops":["none"], "pass_config":{"fuse_allreduce_rms":false}}' \
                           --trust-remote-code \
                           --max-model-len 16384 \
                           --gpu-memory-utilization 0.90
                       resources:
                         requests:
                           nvidia.com/gpu: "8"
                         limits:
                           nvidia.com/gpu: "8"
                       ports:
                       - containerPort: 8080
                         name: http
                       - containerPort: 6379
                         name: ray-head
                       volumeMounts:
                       - mountPath: /dev/shm
                         name: dshm
                       - mountPath: /models
                         name: model-volume
                         readOnly: true
                       - mountPath: /usr/local/gib
                         name: gib
                       - mountPath: /usr/local/nvidia/lib64
                         name: nvidia-lib64
                     volumes:
                     - name: dshm
                       emptyDir:
                         medium: Memory
                         sizeLimit: 64Gi
                     - name: model-volume
                       csi:
                         driver: gcsfuse.csi.storage.gke.io
                         volumeAttributes:
                           bucketName: $MODEL_BUCKET
                           mountOptions: implicit-dirs
                     - name: gib
                       hostPath:
                         path: /home/kubernetes/bin/gib
                     - name: nvidia-lib64
                       hostPath:
                         path: /home/kubernetes/bin/nvidia/lib64
           # -------------------- WORKER --------------------
           - name: worker
             replicas: 1
             template:
               spec:
                 parallelism: 1
                 completions: 1
                 backoffLimit: 1
                 template:
                   metadata:
                     labels:
                       app: vllm-r1
                       role: worker
                     annotations:
                       gke-gcsfuse/volumes: "true"
                   spec:
                     hostNetwork: true
                     dnsPolicy: ClusterFirstWithHostNet
                     hostIPC: true
                     nodeSelector:
                       cloud.google.com/gke-accelerator: nvidia-b200
                     tolerations:
                     - key: nvidia.com/gpu
                       operator: Exists
                     - key: cloud.google.com/impending-node-termination
                       operator: Exists
                     - effect: NoSchedule
                       key: cloud.google.com/gke-queued
                       value: "true"
                     containers:
                     - name: vllm-worker
                       image: docker.io/vllm/vllm-openai@sha256:61fc8a896b0a4fbbbdc063bc4b0dbc25ce98e02b5050c24aeb7830ac02039b14
                       imagePullPolicy: IfNotPresent
                       securityContext:
                         privileged: true
                       env:
                       - name: PYTHONUNBUFFERED
                         value: "1"
                       - name: NCCL_DEBUG
                         value: "INFO"
                       - name: VLLM_ENGINE_READY_TIMEOUT_S
                         value: "1800"
                       - name: VLLM_RPC_TIMEOUT
                         value: "1800000"
                       - name: HF_TOKEN
                         valueFrom:
                           secretKeyRef:
                             name: hf-secret
                             key: hf_api_token
                       command: ["/bin/bash", "-c"]
                       args:
                       - |
                         set -e
                         echo "precedence ::ffff:0:0/96  100" >> /etc/gai.conf 2>/dev/null || true
                         ulimit -l unlimited || true
                         export LD_LIBRARY_PATH=/usr/local/gib/lib64:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH:-}
                         source /usr/local/gib/scripts/set_nccl_env.sh
                         export GLOO_SOCKET_IFNAME=eth0
                         export NCCL_SOCKET_IFNAME=eth0
                         export VLLM_HOST_IP=$(hostname -I | awk '{print $1}')
                         echo "=== Starting Optimized vLLM Ray Worker (rank 1) ==="
                         echo "Host IP: ${VLLM_HOST_IP}"
                         # 0. Install Ray with Compiled Graph support (not pre-installed in vLLM 0.28.0 image)
                         uv pip install --system "ray[cgraph]"
                         # Join the Leader's Ray cluster and block so the container stays alive
                         exec bash /vllm-workspace/examples/ray_serving/multi-node-serving.sh worker \
                           --ray_address=vllm-r1-leader \
                           --ray_port=6379 \
                           --node-ip-address="${VLLM_HOST_IP}"
                       resources:
                         requests:
                           nvidia.com/gpu: "8"
                         limits:
                           nvidia.com/gpu: "8"
                       ports:
                       - containerPort: 8080
                         name: http
                       volumeMounts:
                       - mountPath: /dev/shm
                         name: dshm
                       - mountPath: /models
                         name: model-volume
                         readOnly: true
                       - mountPath: /usr/local/gib
                         name: gib
                       - mountPath: /usr/local/nvidia/lib64
                         name: nvidia-lib64
                     volumes:
                     - name: dshm
                       emptyDir:
                         medium: Memory
                         sizeLimit: 64Gi
                     - name: model-volume
                       csi:
                         driver: gcsfuse.csi.storage.gke.io
                         volumeAttributes:
                           bucketName: $MODEL_BUCKET
                           mountOptions: implicit-dirs
                     - name: gib
                       hostPath:
                         path: /home/kubernetes/bin/gib
                     - name: nvidia-lib64
                       hostPath:
                         path: /home/kubernetes/bin/nvidia/lib64

To scale this deployment to more hosts, update the parameters in `deepseek_r1_server.yaml`. For example, to scale to four A4 nodes, with a total of 32 NVIDIA B200 GPUs, set `replicas: 3` under the `worker` replicated Job, and update the leader arguments as follows:

     * `--ray_cluster_size=4`
     * `--tensor-parallel-size=16`
     * `--pipeline-parallel-size=2`
  2. Substitute your Cloud Storage bucket name into `deepseek_r1_server.yaml` and apply the manifest to your cluster:
         
         envsubst '$MODEL_BUCKET' < deepseek_r1_server.yaml | kubectl apply -f -

  3. Monitor the leader and worker Pod logs until server startup has completed:
         
         # monitor leader
         kubectl logs -l jobset.sigs.k8s.io/replicatedjob-name=leader -c vllm-leader -f --tail=-1
         # monitor worker
         kubectl logs -l jobset.sigs.k8s.io/replicatedjob-name=worker -c vllm-worker -f --tail=-1

Because `kubectl logs -f` streams logs in the foreground, run the worker logs command in a separate terminal session if you want to monitor both Pods simultaneously. To stop streaming logs at any time, press `Control+C`.

Initial weight streaming, model loading, and CUDA graph capture take approximately 15 to 20 minutes. Before you send requests, wait until the leader Pod logs output the following messages:
         
         (APIServer pid=1) INFO:     Started server process [1]
         (APIServer pid=1) INFO:     Waiting for application startup.
         (APIServer pid=1) INFO:     Application startup complete.
         




## Send inference requests

Send a chat completion request to the deployed vLLM server:

  1. Forward local port `8080` to the `vllm-r1-leader` Service in the background:
         
         kubectl port-forward service/vllm-r1-leader 8080:8080 &

  2. Send a chat completion request to the `/v1/chat/completions` endpoint:
         
         curl http://localhost:8080/v1/chat/completions \
             -H "Content-Type: application/json" \
             -d '{
                 "model": "deepseek-ai/DeepSeek-R1",
                 "messages": [
                     {"role": "user", "content": "Explain tensor parallelism in one sentence."}
                 ],
                 "max_tokens": 100,
                 "temperature": 0.6
             }'




## Run benchmark workloads

Benchmark the deployed DeepSeek-R1 server by using `vllm bench serve` with a configuration of 8,192 input tokens and 1,024 output tokens (`8k/1k`):

  1. Review the `deepseek_r1_8k_1k.yaml` manifest, or create the file locally if you didn't download it earlier:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: vllm-bench-8k-1k
           namespace: default
           labels:
             app: vllm-bench
           annotations:
             gke-gcsfuse/volumes: "true"
         spec:
           restartPolicy: Never
           tolerations:
           - operator: Exists
           containers:
           - name: benchmark
             image: docker.io/vllm/vllm-openai@sha256:61fc8a896b0a4fbbbdc063bc4b0dbc25ce98e02b5050c24aeb7830ac02039b14
             imagePullPolicy: IfNotPresent
             env:
             - name: PYTHONUNBUFFERED
               value: "1"
             - name: HF_TOKEN
               valueFrom:
                 secretKeyRef:
                   name: hf-secret
                   key: hf_api_token
             - name: HUGGING_FACE_HUB_TOKEN
               valueFrom:
                 secretKeyRef:
                   name: hf-secret
                   key: hf_api_token
             command: ["/bin/bash", "-c"]
             args:
             - |
               set -e
               echo "=== Benchmark: Input 8k (8192) / Output 1k (1024) [1280 Prompts, Concurrency 112] ==="
               vllm bench serve \
                 --backend openai \
                 --base-url http://vllm-r1-leader:8080 \
                 --model deepseek-ai/DeepSeek-R1 \
                 --tokenizer /models/DeepSeek-R1 \
                 --dataset-name random \
                 --random-input-len 8192 \
                 --random-output-len 1024 \
                 --random-range-ratio 0.0 \
                 --num-prompts 1280 \
                 --max-concurrency 112 \
                 --request-rate inf \
                 --ready-check-timeout-sec 0 \
                 --trust-remote-code
             resources:
               requests:
                 cpu: "8"
                 memory: 16Gi
             volumeMounts:
             - mountPath: /models
               name: model-volume
               readOnly: true
           volumes:
           - name: model-volume
             csi:
               driver: gcsfuse.csi.storage.gke.io
               volumeAttributes:
                 bucketName: $MODEL_BUCKET
                 mountOptions: implicit-dirs

The manifest specifies 8,192 input tokens, 1,024 output tokens, 1,280 prompts, and a maximum concurrency of 112.

  2. Apply the `deepseek_r1_8k_1k.yaml` manifest:
         
         envsubst '$MODEL_BUCKET' < deepseek_r1_8k_1k.yaml | kubectl apply -f -

  3. Wait for the `vllm-bench-8k-1k` Pod to start, and then stream the benchmark logs:
         
         kubectl wait --for=condition=Ready pod/vllm-bench-8k-1k --timeout=120s
         kubectl logs -f vllm-bench-8k-1k -c benchmark

The benchmark takes approximately 15 minutes to complete. After the benchmark has completed, look for output that contains metrics such as the following:

     * `Output token throughput`
     * `Total token throughput`
     * `TTFT`
     * `TPOT`



## Clean up

To avoid incurring additional ongoing charges to your Google Cloud account for the resources used in this tutorial, delete the Kubernetes workloads, the GKE cluster, and your Cloud Storage buckets:

  1. Delete the benchmark Pods, the vLLM server JobSet and Service, the model download Job, and the Hugging Face Secret:
         
         envsubst '$MODEL_BUCKET' < deepseek_r1_8k_1k.yaml | kubectl delete -f - --ignore-not-found || true
         envsubst '$MODEL_BUCKET' < deepseek_r1_server.yaml | kubectl delete -f - --ignore-not-found || true
         kubectl delete job download-deepseek-r1 --ignore-not-found || true
         kubectl wait --for=delete pod -l app=vllm-r1 --timeout=120s || true
         kubectl delete secret hf-secret --ignore-not-found || true

  2. Delete the Cloud Storage bucket that stores the staged model weights:
         
         gcloud storage rm --recursive "gs://${MODEL_BUCKET}"

  3. From the `cluster-toolkit` directory, destroy the GKE cluster and its associated infrastructure by using the [`gcluster destroy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-destroy):
         
         ./gcluster destroy "${CLUSTER_NAME}" --robust --auto-approve

  4. Delete the Cloud Storage bucket that stores the Terraform state:
         
         gcloud storage rm --recursive "gs://${TERRAFORM_BUCKET}"




## What's next

  * Learn more about [vLLM](https://github.com/vllm-project/vllm).
  * Learn more about [A4 VMs with NVIDIA B200 GPUs](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms).
  * Learn more about [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview).
  * Learn more about [managing AI-optimized GKE clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/manage-gke-clusters).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 

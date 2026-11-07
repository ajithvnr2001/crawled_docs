---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/batch-workload/
title: Run a batch workload with Pathways \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-07T08:30:02.820682+00:00
---

# Run a batch workload with Pathways  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/batch-workload/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Run a batch workload with Pathways Stay organized with collections  Save and categorize content based on your preferences. 

This guide uses a JAX training workload that runs to completion in the same cluster as the Pathways controller components to demonstrate how to run a batch workload.

You can run batch workloads on a Google Kubernetes Engine (GKE) cluster or on a Cluster Director cluster with Slurm:

  * On GKE, completion of the JAX workload terminates the Pathways cluster components.
  * On Cluster Director, the Pathways controller components run as a separate Slurm job, so they keep running after the JAX workload completes, until you stop them.



This page has instructions for both platforms. In each section, select the **GKE** or **Cluster Director** tab.

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

###  GKE 

Complete the following prerequisites:

  * [Create a GKE cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-gke-cluster).
  * [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * [Install Kubernetes tools](https://kubernetes.io/docs/tasks/tools/).
  * [Enable the Kubernetes Engine API](https://console.cloud.google.com/flows/enableapi?apiid=container.googleapis.com).
  * Create a Cloud Storage bucket for Pathways artifacts and outputs.



###  Cluster Director 

Complete the following prerequisites:

  * [Create a Cluster Director cluster and set up the Pathways environment](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-cluster-director-cluster).
  * Create a Cloud Storage bucket that you can write to for Pathways scratch data and checkpoints.



## Build a training image by using MaxText

[MaxText](https://github.com/AI-Hypercomputer/maxtext) is an open-source large language model (LLM) project developed by Google. It's written in JAX and designed to run efficiently on Google Cloud TPUs and GPUs.

###  GKE 

To build a MaxText Docker image by using the latest version of stable JAX from the open-source GitHub repository, run the following command:
    
    
    git clone https://github.com/AI-Hypercomputer/maxtext
    cd maxtext
    gcloud config set project PROJECT_ID
    bash src/dependencies/scripts/docker_build_dependency_image.sh MODE=stable
    gcloud auth configure-docker
    # This script needs bash version >= 4.2 to execute.
    bash src/dependencies/scripts/docker_upload_runner.sh \
        CLOUD_IMAGE_NAME=USER_runner

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `USER`: your Google Cloud user ID.



This command pushes the MaxText Kubernetes image to `gcr.io/PROJECT_ID/USER_runner`. You can use this Docker image to run training on TPUs by using the Pathways backend.

###  Cluster Director 

You don't need to build a training image: `setup_env.sh` installed MaxText in the Pathways environment in `/home/pathways`, and `run_maxtext.sh` runs it.

## Run a batch workload

###  GKE 

  1. If the [`gcluster` binary](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster) isn't in your `PATH` environment variable, add the directory containing `gcluster` to your `PATH`:
         
         export PATH="$PATH:CLUSTER_TOOLKIT_PATH"

Replace `CLUSTER_TOOLKIT_PATH` with the absolute path to the directory containing the `gcluster` binary, such as `$HOME/cluster-toolkit`.

  2. Submit the prebuilt MaxText Docker image by using the `gcluster job submit` command:
         
         gcluster job submit \
             --pathways \
             --pathways-gcs-location="gs://BUCKET_NAME/pathways-artifacts" \
             --name=WORKLOAD \
             --cluster=CLUSTER \
             --project=PROJECT_ID \
             --location=LOCATION \
             --num-slices=WORKLOAD_NODEPOOL_COUNT \
             --compute-type=COMPUTE_TYPE \
             --topology=TOPOLOGY \
             --image="gcr.io/PROJECT_ID/USER_runner" \
             --command="python3 -m maxtext.trainers.pre_train.train /deps/src/maxtext/configs/base.yml base_output_directory=gs://BUCKET_NAME per_device_batch_size=1 enable_checkpointing=false remat_policy=full global_parameter_scale=1 steps=20 max_target_length=2048 use_iota_embed=true reuse_example_batch=1 dataset_type=synthetic attention=flash gcs_metrics=True enable_single_controller=True run_name=RUN_NAME-pathways-job"

Replace the following:

     * `BUCKET_NAME`: the Cloud Storage bucket for outputs.
     * `WORKLOAD`: a unique name to identify your workload (22 characters or fewer due to DNS label limits).
     * `CLUSTER`: the name of your GKE cluster.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `LOCATION`: the region or zone of your GKE cluster.
     * `WORKLOAD_NODEPOOL_COUNT`: the number of TPU slice node pools.
     * `COMPUTE_TYPE`: the TPU machine type—for example, `ct6e-standard-4t`. For more information about supported TPU types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
     * `TOPOLOGY`: the TPU placement topology—for example, `2x4`.
     * `USER`: your Google Cloud user ID.
     * `RUN_NAME`: a user-assigned name to identify the workflow run.

For more information about job submission options, see the [Cluster Toolkit Job Submission Guide](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/docs/gcluster_job_guide.md).

  3. Follow the progress of your workload by using the `gcluster job logs` command:
         
         gcluster job logs WORKLOAD \
             --cluster=CLUSTER \
             --project=PROJECT_ID \
             --location=LOCATION \
             --main-only \
             --follow

The output is similar to the following:
         
         completed step: 0, seconds: 1.259, TFLOP/s/device: 10.792, Tokens/s/device: 1626.636, total_weights: 65536, loss: 10.876, lm_loss: 10.876, perplexity: 52906.090
         completed step: 1, seconds: 3.366, TFLOP/s/device: 4.036, Tokens/s/device: 608.366, total_weights: 65536, loss: 10.876, lm_loss: 10.876, perplexity: 52906.090
         completed step: 2, seconds: 0.264, TFLOP/s/device: 51.415, Tokens/s/device: 7749.885, total_weights: 65536, loss: 10.563, lm_loss: 10.563, perplexity: 38665.316
         completed step: 3, seconds: 1.025, TFLOP/s/device: 13.257, Tokens/s/device: 1998.187, total_weights: 65536, loss: 9.983, lm_loss: 9.983, perplexity: 21646.125
         completed step: 4, seconds: 1.194, TFLOP/s/device: 11.376, Tokens/s/device: 1714.750, total_weights: 65536, loss: 9.462, lm_loss: 9.462, perplexity: 12864.218
         completed step: 5, seconds: 1.185, TFLOP/s/device: 11.465, Tokens/s/device: 1728.203, total_weights: 65536, loss: 8.961, lm_loss: 8.961, perplexity: 7791.373
         

  4. Optional: To cancel the workload before it completes, use the `gcluster job cancel` command:
         
         gcluster job cancel WORKLOAD \
             --cluster=CLUSTER \
             --project=PROJECT_ID \
             --location=LOCATION




###  Cluster Director 

Run the following commands on the cluster's login node from `~/pathways`. The scripts look for each other and write their logs in that directory.

  1. Start the Pathways service:
         
         cd ~/pathways
         SLICE_SHAPE=TOPOLOGY \
             MIN_SLICES=MIN_SLICES \
             MAX_SLICES=MAX_SLICES \
             GCS_BUCKET=gs://BUCKET_NAME \
             sbatch start_pathways.sh

Replace the following:

     * `TOPOLOGY`: the TPU topology of each slice. It must match the `acceleratorTopology` of your TPU nodeset—for example, `2x4`.
     * `MIN_SLICES`: the minimum number of running slices required to start and continue training.
     * `MAX_SLICES`: the maximum number of slices to use, normally the number of slices in the nodeset.
     * `BUCKET_NAME`: the Cloud Storage bucket for Pathways scratch data and checkpoints.

If your TPU partition isn't the cluster's default partition, also set `PARTITION` to its name.

The service is ready when its log, `pathways-service-JOB_ID.out` (where `JOB_ID` is the Slurm job ID), shows output similar to the following:
    
    Pathways Runtime Service is READY!
     Discovery file    : /home/USER/pathways/cluster.env
     IFRT Proxy Target : grpc://RM_IP:29000
     Running TPU Slices : 2 / 2 (min=2)
    

  2. Submit the MaxText training workload. You can submit it right after the service job: it waits up to an hour for the service to be ready.
         
         sbatch run_maxtext.sh
         

The MaxText job waits until the Pathways service has at least `MIN_SLICES` running slices before it starts training. The workload trains Llama 3.1 8B on synthetic data. The slice settings and the bucket come from the service, so don't set them on this job. You can set the following optional variables:

     * `STEPS`: the number of training steps. The default is `30`.
     * `CHECKPOINT_PERIOD`: the number of steps between checkpoints. The default is `5`.
     * `BASE_OUTPUT_DIR`: the Cloud Storage path where MaxText writes checkpoints. The default is `gs://BUCKET_NAME/maxtext-runs`.
     * `REDUCED_LAYERS=1`: trains an 8-layer variant instead of the full 32 layers, for `2x2` slices.

Follow the progress of your workload (replace `JOB_ID` with the Slurm job ID of the MaxText job). MaxText writes its log to standard error:
    
    tail -f maxtext-llama31-JOB_ID.err

Each training step prints a line similar to the following:
    
    completed step: 24, seconds: 0.326, live slice count: 2, TFLOP/s/device: 88.199, Tokens/s/device: 6289.27, total_weights: 32768, loss: 6.238
    

You can submit `run_maxtext.sh` again later without restarting the service.

  3. When you're done, stop the workload and then the Pathways service:
         
         scancel -u ${USER} -n maxtext-llama31
         scancel -u ${USER} -n pathways-service
         

Canceling the service also cancels the Pathways worker jobs. The TPU VMs are static nodes, so they keep running and become available to other Slurm jobs.




If you run into problems, see [Troubleshoot Pathways on Cloud](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/troubleshooting-pathways#debugging-common).

## What's next

  * [Create a GKE cluster with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-gke-cluster)
  * [Create a Cluster Director cluster with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-cluster-director-cluster)
  * [Run an interactive workload with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-interactive-mode)
  * [Port JAX workloads to Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/porting-jax-workloads)
  * [Resilient training with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/resilient-training)
  * [Troubleshoot Pathways on Cloud](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/troubleshooting-pathways)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-06 UTC."],[],[]] 

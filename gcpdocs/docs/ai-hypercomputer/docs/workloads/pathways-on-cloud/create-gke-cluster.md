---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-gke-cluster/
title: Create a GKE cluster with Pathways \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-05T11:08:53.609867+00:00
---

# Create a GKE cluster with Pathways  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-gke-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Create a GKE cluster with Pathways Stay organized with collections  Save and categorize content based on your preferences. 

This page shows platform administrators and machine learning (ML) engineers how to create a Google Kubernetes Engine (GKE) cluster configured for Pathways-based workloads. You can provision pre-configured clusters automatically by using [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview), or create clusters manually by using the Google Cloud CLI.

## Before you begin

Complete the following prerequisites before you proceed:

  * [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  * [Install `kubectl` and the `gke-gcloud-auth-plugin`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl).
  * If you use Cluster Toolkit, [set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment) and [update it to the latest version](https://docs.cloud.google.com/cluster-toolkit/docs/setup/update-cluster-toolkit).
  * [Enable the Kubernetes Engine API](https://console.cloud.google.com/flows/enableapi?apiid=container.googleapis.com).
  * Verify that you have enough [TPU quota](https://docs.cloud.google.com/tpu/docs/quota) or a [TPU reservation](https://docs.cloud.google.com/tpu/docs/about-tpu-reservations) for the TPU slices that you want to create.

**Note:** Following the steps on this page creates billable resources, including a GKE cluster, TPU v6e slice node pools, and CPU node pools.

## Set up your local environment

Sign in to the gcloud CLI with your Google Cloud credentials:
    
    
    gcloud auth login
    

If you use Cluster Toolkit, also generate Application Default Credentials (ADC), which Terraform uses:
    
    
    gcloud auth application-default login
    

## Create a GKE cluster

In the following example, you create a cluster with TPU v6e 2x4 node pools. You can create a cluster by using Cluster Toolkit or the gcloud CLI.

### Cluster Toolkit

  1. Deploy a GKE TPU cluster by following the instructions in [Deploy a GKE TPU v6e cluster](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-v6e). For an overview of all TPU deployment options, see [Cloud TPU deployments overview](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-overview).

When configuring your deployment blueprint, do the following:

     * Set `enable_pathways_for_tpus` to `true` (enabled by default in Cluster Toolkit TPU blueprints). This setting automatically provisions the required `cpu-np` CPU node pool (`n4-standard-64`) and Kueue configurations for the Pathways controller. Cluster Toolkit applies the default Pathways Kueue configuration only if you don't specify a custom Kueue configuration file in the `kueue_configuration_path` variable.
     * Set `num_slices` to the number of TPU slice node pools required for your workload.
     * Set `tpu_topology` to your selected TPU slice topology (for example, `2x4` or `4x4`).
     * Choose a consumption option. By default, the TPU v6e deployment file consumes a specific [TPU reservation](https://docs.cloud.google.com/tpu/docs/about-tpu-reservations), so specify the reservation name in the `reservation_affinity` variable. To use a different consumption option, see [GKE consumption options](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-consumption-options).
  2. Verify that the cluster nodes have a `STATUS` of `Ready`:
         
         kubectl get nodes
         

After you create the cluster, you can submit Pathways workloads by using the `gcluster job submit` command with the `--pathways` and `--pathways-gcs-location` flags. For more information, see [Run workloads with Pathways](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/run-workloads-pathways).




### gcloud

To create a GKE cluster and set it up for running Pathways workloads, follow these steps:

  1. Set the following environment variables:
         
         CLUSTER=GKE_CLUSTER_NAME
         PROJECT=PROJECT_ID
         ZONE=ZONE
         REGION=REGION
         CLUSTER_VERSION=GKE_CLUSTER_VERSION
         PW_CPU_MACHINE_TYPE="n2-standard-64"
         NETWORK=NETWORK
         SUBNETWORK=SUB_NETWORK
         CLUSTER_NODEPOOL_COUNT=3
         TPU_MACHINE_TYPE="ct6e-standard-4t"
         WORKERS_PER_SLICE=2
         TOPOLOGY="2x4"
         NUM_CPU_NODES=1

Replace the following:

     * `GKE_CLUSTER_NAME`: the name of your GKE cluster.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `ZONE`: the zone where you create the cluster. Choose a zone where TPU v6e is available. For more information, see [Cloud TPU regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones).
     * `REGION`: Optional: the region where you create resources if you use a regional cluster.
     * `GKE_CLUSTER_VERSION`: Optional: the GKE cluster version. Use `1.32.2-gke.1475000` or later, and choose a version that's in standard support. For more information, see the [GKE release schedule](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule). If you don't specify a version, remove the `--cluster-version` flag from the following `gcloud container clusters create` command.
     * `NETWORK`: Optional: the name of a Virtual Private Cloud (VPC) network. The network must exist before you create the cluster. If you don't specify a network, remove the `--network` flag from the following `gcloud container clusters create` command.
     * `SUB_NETWORK`: Optional: the name of a subnetwork. The subnetwork must exist before you create the cluster. If you don't specify a subnetwork, remove the `--subnetwork` flag from the following `gcloud container clusters create` command.

This example sets default values for the remaining variables, which you can modify for your workload:

     * `PW_CPU_MACHINE_TYPE`: the machine type for the default node pool of the cluster and for the CPU node pool that runs the Pathways head (the Pathways resource manager and proxy).
     * `NUM_CPU_NODES`: the number of nodes in the CPU node pool.
     * `CLUSTER_NODEPOOL_COUNT`: the number of TPU slices. Each slice is a separate node pool.
     * `TPU_MACHINE_TYPE` and `TOPOLOGY`: the TPU machine type and the TPU topology of each slice.
     * `WORKERS_PER_SLICE`: the number of nodes in each slice, which is the number of TPU chips in the topology divided by the number of chips per node. For example, a `2x4` topology has 8 chips and a `ct6e-standard-4t` node has 4 chips, so each slice has 2 nodes.
  2. Create a GKE cluster by using the [`gcloud container clusters create` command](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create):
         
         gcloud container clusters create ${CLUSTER} \
             --project=${PROJECT} \
             --zone=${ZONE} \
             --cluster-version=${CLUSTER_VERSION} \
             --scopes=storage-full,gke-default,cloud-platform \
             --machine-type=${PW_CPU_MACHINE_TYPE} \
             --network=${NETWORK} \
             --subnetwork=${SUBNETWORK}
         

  3. Create the TPU slice node pools by using the [`gcloud container node-pools create` command](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create):
         
         for i in $(seq 1 ${CLUSTER_NODEPOOL_COUNT}); do
             gcloud container node-pools create "tpu-np-${i}" \
                 --project=${PROJECT} \
                 --zone=${ZONE} \
                 --cluster=${CLUSTER} \
                 --machine-type=${TPU_MACHINE_TYPE} \
                 --num-nodes=${WORKERS_PER_SLICE} \
                 --placement-type=COMPACT \
                 --tpu-topology=${TOPOLOGY} \
                 --scopes=storage-full,gke-default,cloud-platform \
                 --workload-metadata=GCE_METADATA
         done
         

These commands don't target a specific reservation. To consume a [TPU reservation](https://docs.cloud.google.com/tpu/docs/about-tpu-reservations), add the `--reservation-affinity=specific` and `--reservation=RESERVATION_NAME` flags, where `RESERVATION_NAME` is the name of your TPU reservation. To use Spot VMs, add the `--spot` flag.

  4. Create a CPU node pool for the Pathways head, which runs the Pathways resource manager and proxy. Name the node pool `cpu-np` so that the `gcluster job submit --pathways` command can detect it:
         
         gcloud container node-pools create cpu-np \
             --project=${PROJECT} \
             --zone=${ZONE} \
             --cluster=${CLUSTER} \
             --machine-type=${PW_CPU_MACHINE_TYPE} \
             --num-nodes=${NUM_CPU_NODES} \
             --scopes=storage-full,gke-default,cloud-platform \
             --workload-metadata=GCE_METADATA
         

**Note:** Pathways workloads store temporary files and cached compiled code in a Cloud Storage bucket. Because the node pools in this example use `--workload-metadata=GCE_METADATA`, Pathways containers access Cloud Storage by using the node service account. By default, this account is the Compute Engine default service account. Grant this service account the Storage Object Admin role (`roles/storage.objectAdmin`) on the bucket.
  5. Get credentials for the cluster and set the default namespace for `kubectl`:

**Note:** If you use a zonal cluster, such as the cluster in this example, specify `--zone`. If you use a regional cluster, replace `--zone=${ZONE}` with `--region=${REGION}`.
         
         gcloud container clusters get-credentials ${CLUSTER} \
             --zone=${ZONE} \
             --project=${PROJECT} \
             && kubectl config set-context --current --namespace=default
         

  6. To use the Pathways architecture on your GKE cluster, install the `JobSet` API:
         
         kubectl apply --server-side -f https://github.com/kubernetes-sigs/jobset/releases/download/v0.12.0/manifests.yaml
         

  7. Verify that the nodes have a `STATUS` of `Ready` and that the `jobset-controller-manager` pod has a `STATUS` of `Running`:
         
         kubectl get nodes
         kubectl get pods --namespace=jobset-system
         

The output is similar to the following:
         
         NAME                                      STATUS   ROLES    AGE   VERSION
         gke-cluster-cpu-np-12345678-abcd          Ready    <none>   5m    v1.32.2-gke.1475000
         gke-cluster-tpu-np-1-12345678-efgh        Ready    <none>   5m    v1.32.2-gke.1475000
         ...
         NAME                                         READY   STATUS    RESTARTS   AGE
         jobset-controller-manager-6f7b8c9d4-xyz12    1/1     Running   0          2m
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the cluster when you are finished:

  * **Cluster Toolkit** : Destroy the deployment by running the following command:
        
        ./gcluster destroy DEPLOYMENT_FOLDER_NAME

Replace `DEPLOYMENT_FOLDER_NAME` with the name of your deployment folder.

  * **gcloud CLI** : Delete the GKE cluster and its node pools by running the following command:
        
        gcloud container clusters delete ${CLUSTER} \
            --project=${PROJECT} \
            --zone=${ZONE}
        




## What's next

  * [Run a batch workload with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/batch-workload)
  * [Pathways interactive mode](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-interactive-mode)
  * [Resilient training with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/resilient-training)
  * [Porting JAX workloads to Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/porting-jax-workloads)
  * [Troubleshoot Pathways on cloud](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/troubleshooting-pathways)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 

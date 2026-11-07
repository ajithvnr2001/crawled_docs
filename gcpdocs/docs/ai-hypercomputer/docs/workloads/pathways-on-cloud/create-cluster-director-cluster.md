---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-cluster-director-cluster/
title: Create a Cluster Director cluster with Pathways \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-07T05:38:49.084156+00:00
---

# Create a Cluster Director cluster with Pathways  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-cluster-director-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Create a Cluster Director cluster with Pathways Stay organized with collections  Save and categorize content based on your preferences. 

This page shows platform administrators and machine learning (ML) engineers how to create a Slurm-orchestrated [Cluster Director](https://cloud.google.com/products/cluster-director) cluster and configure it for Pathways workloads. By completing these steps, you provision a cluster with TPU v6e slices, a CPU controller node, a shared Google Cloud Managed Lustre file system, and the `/home/pathways` runtime environment. Pathways isn't preinstalled on a Cluster Director cluster: after you create the cluster, you download the Pathways scripts to the login node and run a setup script once.

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

Before you begin, complete the following prerequisites:

  * [Install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  * [Enable the Hypercompute Cluster API](https://console.cloud.google.com/flows/enableapi?apiid=hypercomputecluster.googleapis.com).
  * Make sure that your user account and the Compute Engine default service account have the Identity and Access Management (IAM) roles required to create and connect to a Cluster Director cluster. For the list of roles, see [Before you begin](https://docs.cloud.google.com/cluster-director/docs/create/quickstart#before-you-begin) in the Cluster Director quickstart.
  * Create a [TPU v6e reservation](https://docs.cloud.google.com/tpu/docs/about-tpu-reservations) in the zone where you plan to create the cluster (for example, at least four `ct6e-standard-4t` VMs for two `2x4` slices).
  * Configure passwordless `sudo` on the cluster nodes for automatic slice recovery. Ask your administrator to grant you the Compute OS Admin Login (`roles/compute.osAdminLogin`) role on the project.
  * Create a Cloud Storage bucket for Pathways scratch data and workload outputs, and grant the Storage Object User (`roles/storage.objectUser`) role on the project to your user account and the Compute Engine default service account.



## Set up your local environment

Sign in with your Google Cloud credentials:
    
    
    gcloud auth login
    

Define the following environment variables with values appropriate to your workload:
    
    
    export PROJECT=PROJECT_ID
    export REGION=REGION
    export ZONE=ZONE
    export CLUSTER_ID=CLUSTER_ID
    export RESERVATION_NAME=RESERVATION_NAME

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `REGION`: the region where you create resources.
  * `ZONE`: the zone where you create resources.
  * `CLUSTER_ID`: the cluster name. The name can contain up to 10 characters and can use only numbers and lowercase letters.
  * `RESERVATION_NAME`: the name of your TPU v6e reservation in `ZONE`.



## Create a Cluster Director cluster

In the following example, you create a cluster with two TPU v6e `2x4` slices (four `ct6e-standard-4t` VMs) from your reservation, and one CPU node for the Pathways controller. All nodes mount a shared Managed Lustre file system at `/home`. For more information about the fields in the cluster definition, see [Create a custom cluster](https://docs.cloud.google.com/cluster-director/docs/create/custom-cluster).

  1. Create the cluster by using the REST API:

Create the request body:
         
         cat <<EOF > "${CLUSTER_ID}_create.json"
         {
           "networkResources": {
             "net": {
               "config": {
                 "newNetwork": {
                   "network": "projects/${PROJECT}/global/networks/${CLUSTER_ID}-net"
                 }
               }
             }
           },
           "storageResources": {
             "home": {
               "config": {
                 "newLustre": {
                   "lustre": "projects/${PROJECT}/locations/${ZONE}/instances/${CLUSTER_ID}-lustre",
                   "filesystem": "lustre",
                   "capacityGb": "18000",
                   "perUnitStorageThroughput": "500"
                 }
               }
             }
           },
           "computeResources": {
             "crtpu": {
               "config": {
                 "newReservedInstances": {
                   "reservation": "projects/${PROJECT}/zones/${ZONE}/reservations/${RESERVATION_NAME}"
                 }
               }
             },
             "crcpu": {
               "config": {
                 "newOnDemandInstances": {
                   "zone": "${ZONE}",
                   "machineType": "n2-highmem-32"
                 }
               }
             }
           },
           "orchestrator": {
             "slurm": {
               "loginNodes": {
                 "count": "1",
                 "zone": "${ZONE}",
                 "machineType": "n2-standard-16",
                 "enableOsLogin": true,
                 "enablePublicIps": true,
                 "bootDisk": {
                   "type": "pd-balanced",
                   "sizeGb": "100"
                 },
                 "storageConfigs": [
                   {
                     "id": "home",
                     "localMount": "/home"
                   }
                 ]
               },
               "nodeSets": [
                 {
                   "id": "nstpu",
                   "computeId": "crtpu",
                   "staticNodeCount": "4",
                   "maxDynamicNodeCount": "0",
                   "enablePublicIps": true,
                   "resourcePolicyConfig": {
                     "acceleratorTopology": "2x4"
                   },
                   "computeInstance": {
                     "bootDisk": {
                       "type": "hyperdisk-balanced",
                       "sizeGb": "100"
                     }
                   },
                   "storageConfigs": [
                     {
                       "id": "home",
                       "localMount": "/home"
                     }
                   ]
                 },
                 {
                   "id": "nscpu",
                   "computeId": "crcpu",
                   "staticNodeCount": "1",
                   "maxDynamicNodeCount": "0",
                   "enablePublicIps": true,
                   "computeInstance": {
                     "bootDisk": {
                       "type": "pd-balanced",
                       "sizeGb": "100",
                       "image": "projects/clusterdirector-public-images/global/images/family/tpu-v6e-v5p-ubuntu2204-slurm2605-v20260902"
                     }
                   },
                   "storageConfigs": [
                     {
                       "id": "home",
                       "localMount": "/home"
                     }
                   ]
                 }
               ],
               "partitions": [
                 {
                   "id": "tpu",
                   "nodeSetIds": ["nstpu"]
                 },
                 {
                   "id": "cpu",
                   "nodeSetIds": ["nscpu"]
                 }
               ],
               "defaultPartition": "tpu",
               "config": {
                 "requeueExitCodes": [1, 2, 134, 137, 139, 143]
               }
             }
           }
         }
         EOF
         

Then send the request:
         
         curl -s -X POST \
             -H "Content-Type: application/json" \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -d @"${CLUSTER_ID}_create.json" \
             "https://hypercomputecluster.googleapis.com/v1alpha/projects/${PROJECT}/locations/${REGION}/clusters?clusterId=${CLUSTER_ID}"
         

The cluster includes the following:

     * **`tpu` partition**: a static nodeset of reserved TPU v6e VMs. `staticNodeCount` is the number of VMs, and `acceleratorTopology` is the topology of each slice. Each `ct6e-standard-4t` VM has four chips, so a `2x4` slice has two VMs. For more slices, multiply: two `2x4` slices need a `staticNodeCount` of `4`.
     * **`cpu` partition**: one on-demand VM that runs the Pathways resource manager, the IFRT proxy server, and the MaxText client. The Pathways scripts submit jobs to a partition named `cpu`. The VM uses the `n2-highmem-32` machine type because the Pathways service and MaxText together need up to 240 GB of memory while they save checkpoints. It also uses an image with Slurm 26.05, which supports TPU slices, because the Pathways service submits the TPU worker jobs from this VM.
     * **`requeueExitCodes`** : Slurm requeues a job that exits with one of these codes. This setting lets Slurm restart a TPU worker job when any VM in the slice is preempted, not only the first one.
  2. Wait until the cluster is ready. You can follow the progress on the [Cluster Director page](https://console.cloud.google.com/cluster-director/clusters) in the Google Cloud console, or check that `reconciling` is `false` in the output of the following command:
         
         curl -s \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             "https://hypercomputecluster.googleapis.com/v1alpha/projects/${PROJECT}/locations/${REGION}/clusters/${CLUSTER_ID}"
         




## Set up the Pathways environment

The Pathways environment lives in `/home/pathways` on the shared file system, so you set it up once per cluster. It contains the Pathways container images, a Python environment with JAX and `pathwaysutils`, and the Pathways scripts.

  1. Connect to the login node. For other ways to connect, see [Connect to a cluster](https://docs.cloud.google.com/cluster-director/docs/manage/connect-to-cluster).
         
         gcloud compute ssh ${CLUSTER_ID}-login-001 \
             --project=${PROJECT} \
             --zone=${ZONE} \
             --tunnel-through-iap
         

  2. Verify that the `cpu` and `tpu` partitions exist and are in the `idle` state:
         
         sinfo -o "%P %a %D %T %N %f"
         

The output is similar to the following:
         
         PARTITION AVAIL NODES STATE NODELIST FEATURES
         tpu* up 4 idle ${CLUSTER_ID}-nstpu-[0-3]
         cpu up 1 idle ${CLUSTER_ID}-nscpu-0
         

  3. Download the Pathways scripts to the login node:
         
         mkdir -p ~/pathways-scripts && cd ~/pathways-scripts
         for f in setup_env.sh start_pathways.sh run_worker_slice.sh run_maxtext.sh; do
           curl -fsSLO "https://raw.githubusercontent.com/GoogleCloudPlatform/slurm-gcp/tpu-2605/pathways/scripts/${f}"
         done
         

This command downloads the following scripts:

     * `setup_env.sh`: performs a one-time setup of the Pathways environment.
     * `start_pathways.sh`: starts the Pathways service.
     * `run_worker_slice.sh`: starts the Pathways worker for one TPU slice (submitted by `start_pathways.sh`).
     * `run_maxtext.sh`: runs an example MaxText training workload.
  4. Run the setup script. It takes about 5 minutes:
         
         chmod +x *.sh
         ./setup_env.sh
         

The script pulls the Pathways server and proxy images, builds a Python environment with JAX, `pathwaysutils`, and MaxText, copies the scripts to `/home/pathways`, and links `~/pathways` to `/home/pathways`. It ends with output similar to the following:
         
         Environment ready: JAX 0.11.1
         

  5. Optional: To give other cluster users access to the Pathways environment, have them link `/home/pathways` to their home directory:
         
         ln -sfn /home/pathways ~/pathways
         




At this point, the cluster is ready for Pathways. You start the Pathways service as part of running a workload, because batch and interactive workloads start it with different settings. For more information, see [Run a batch workload with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/batch-workload) and [Run an interactive workload with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-interactive-mode).

If you run into problems, see [Troubleshoot Pathways on Cloud](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/troubleshooting-pathways#debugging-common).

## Cleaning up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Cluster Director cluster when you're finished:
    
    
    curl -s -X DELETE \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://hypercomputecluster.googleapis.com/v1alpha/projects/${PROJECT}/locations/${REGION}/clusters/${CLUSTER_ID}"
    

## What's next

  * [Run a batch workload with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/batch-workload)
  * [Run an interactive workload with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-interactive-mode)
  * [Resilient training with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/resilient-training)
  * [Port JAX workloads to Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/porting-jax-workloads)
  * [Troubleshoot Pathways on Cloud](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/troubleshooting-pathways)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-06 UTC."],[],[]] 

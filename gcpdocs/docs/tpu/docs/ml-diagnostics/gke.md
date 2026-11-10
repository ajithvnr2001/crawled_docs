---
url: https://docs.cloud.google.com/tpu/docs/ml-diagnostics/gke/
title: Configure GKE or self-managed Kubernetes \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T16:58:45.328933+00:00
---

# Configure GKE or self-managed Kubernetes  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/ml-diagnostics/gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure GKE or self-managed Kubernetes

You can configure the ML Diagnostics platform for ML workloads running on Google Kubernetes Engine (GKE) or self-managed Kubernetes.

ML Diagnostics includes the following generally available features:

  * **Automatic workload monitoring and system metrics collection** : For automatic workload monitoring and system metrics collection on GKE, you don't need to instrument your code or perform any extra configuration. Workload monitoring and system metrics collection are enabled by default, and you aren't required to perform the steps in this guide. Workload monitoring supports the `JobSet` and `Job` GKE job types, and is compatible with GKE versions `1.36.4-gke.1247000` and later.
  * **ML Diagnostics SDK metrics and programmatic profiling** : If you want to use the ML Diagnostics SDK to collect metrics and run programmatic profiling, install the `injection-webhook` Helm chart, label the workload, and use the [ML Diagnostics SDK](https://docs.cloud.google.com/tpu/docs/ml-diagnostics/sdk). On GKE, you can use a single Google Cloud CLI command if you use a supported GKE version, or perform a manual installation. On self-managed Kubernetes, you must install the webhook manually.
  * **On-demand profiling** : If you want to use on-demand profiling, install the `connection-operator` Helm chart. On GKE, you can use a single gcloud CLI command if you use a supported GKE version, or perform a manual installation. On self-managed Kubernetes, you must install the operator manually.



ML Diagnostics also includes the following Preview feature:

  * **Diagon DaemonSet profiling** : If you want to use on-demand profiling, continuous profiling, and automatic profile capture from workload monitoring on your GKE workload, deploy the Diagon DaemonSet on your GKE TPU clusters. This DaemonSet also works on self-managed Kubernetes clusters, where only on-demand and continuous profiling are supported. Workload monitoring is not supported on self-managed Kubernetes.



## Deploy the Diagon DaemonSet

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If you run containerized workloads on GKE or self-managed Kubernetes clusters, you can deploy the Diagon daemon as a DaemonSet. This ensures that a copy of the daemon runs on all, or selected, GPU and TPU nodes within the cluster.

### Container image repository

The Diagon daemon is published as a Docker image and is available from the following Artifact Registry path:

`us-central1-docker.pkg.dev/hypercomputediagon-release/daemon-docker/mldiagnostics-daemon:latest`

### Deployment steps

To deploy the Diagon DaemonSet to your cluster, complete the following steps:

  1. **Create the DaemonSet configuration** : Save the following YAML configuration as `diagon-daemonset.yaml`. This configuration runs the Diagon daemon in privileged mode so that it can collect diagnostic and profiling metrics from the underlying host GPU and TPU devices.
         
         # diagon-daemonset.yaml
         apiVersion: apps/v1
         kind: DaemonSet
         metadata:
           name: diagon-daemon
           namespace: diagon
           labels:
             app.kubernetes.io/name: diagon-daemon
             app.kubernetes.io/part-of: diagon
         spec:
           selector:
             matchLabels:
               name: diagon-daemon
           template:
             metadata:
               labels:
                 name: diagon-daemon
             spec:
               hostNetwork: true
               dnsPolicy: ClusterFirstWithHostNet
               serviceAccountName: SERVICE_ACCOUNT_NAME
               terminationGracePeriodSeconds: 30
               tolerations:
               - operator: Exists
                 effect: NoSchedule
               - operator: Exists
                 effect: NoExecute
               containers:
               - name: diagon-daemon
                 image: us-central1-docker.pkg.dev/hypercomputediagon-release/daemon-docker/mldiagnostics-daemon:latest
                 imagePullPolicy: Always
                 command:
                 - /mldiagnostics_extension_files/bin/mldiagnostics_extension
                 - -standalone=true
                 - -channel=hypercomputecluster.googleapis.com/diagnostics
                 - -alsologtostderr=true
                 securityContext:
                   privileged: true
                 resources:
                   requests:
                     cpu: 10m
                     memory: 32Mi
                   limits:
                     memory: 256Mi  # No CPU limit.
         

  2. **Deploy the DaemonSet to the cluster** : Run the following command to deploy the daemon to your active Kubernetes context.
         
         kubectl apply -f diagon-daemonset.yaml
         

  3. **Verify deployment and daemon health** : On your administrative workstation or in Cloud Shell, check that all daemon pods are scheduled across worker nodes and have reached the `Running` state:
         
         kubectl get pods -n diagon -l name=diagon-daemon -o wide
         

Inspect the streaming logs to confirm connectivity to the Google Cloud ML Diagnostics control plane and active heartbeats:
         
         kubectl logs -n diagon -l name=diagon-daemon --tail=50
         

The output includes the following expected log signatures:
         
         Stream established.
         Received successful DaemonRegistrationResponse from backend
         Sending DaemonHeartbeatRequest
         

  4. **Update the DaemonSet image** : To update to a newer version of the daemon or roll back, update the image tag in your YAML file, or run the following command directly.
         
         kubectl set image daemonset/diagon-daemon diagon-daemon=us-docker.pkg.dev/hypercomputediagon-release/daemon/diagon-daemon:v2.1.0 --namespace=kube-system
         

To check the progress of the deployment or update, verify the rollout status:
         
         kubectl rollout status daemonset/diagon-daemon --namespace=kube-system
         




## Set up operator and webhook

For the operator and webhook setup, you have the following options:

  * If you use a version of GKE that is later than `1.35.0-gke.3065000`, you can set up your GKE cluster for ML Diagnostics with a single gcloud CLI command, through the Google Cloud console, or by using Terraform.

  * For GKE versions earlier than `1.35.0-gke.3065000` and self-managed Kubernetes, you must manually configure the cluster to install the `cert-manager`, `injection-webhook`, and `connection-operator` artifacts. For more information, see Manual installation.




Deploy the operator and webhook on your GKE cluster, along with the Diagon DaemonSet. If you already deployed the operator and webhook, you don't need to delete them. Instead, the operator serves as the fallback path for on-demand profile capture, and the webhook is still required to use the SDK.

If you use a self-managed Kubernetes environment instead of GKE, install the webhook for the SDK and deploy the Diagon DaemonSet. In a self-managed Kubernetes environment, workload monitoring doesn't work; only SDK metrics, programmatic profiling, on-demand profiling, and continuous profiling are supported.

For GKE versions later than `1.35.0-gke.3065000`, use one of the following methods to deploy the required ML Diagnostics components (both `connection-operator` and `injection-webhook`) into your GKE cluster.

###  gcloud 

For new GKE clusters:
    
    
    gcloud beta container clusters create CLUSTER_NAME --enable-managed-mldiagnostics
    

For existing GKE clusters:
    
    
    gcloud beta container clusters update CLUSTER_NAME --enable-managed-mldiagnostics
    

To disable ML Diagnostics, use the following:
    
    
    gcloud beta container clusters update CLUSTER_NAME --no-enable-managed-mldiagnostics
    

For more information on gcloud CLI commands to set up a GKE cluster for ML Diagnostics, refer to the `enable-managed-mldiagnostics` flag in the following API reference pages:

  * [`container clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/clusters/update)
  * [`container clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/clusters/create)



###  Console 

  * For new GKE clusters, go to **Feature Manager > Managed Machine Learning Diagnostics**.

[Go to GKE Managed Machine Learning Diagnostics](https://console.cloud.google.com/kubernetes/features)

  * For existing GKE clusters, go to **Clusters** , select the name of your cluster, go to **Edit** , and edit **Managed Machine Learning Diagnostics** under **Features**.




###  Terraform 

If you use Terraform to provision your GKE infrastructure, you can use the `terraform-provider-google-beta` provider (version `v7.28.0` or later), or the `terraform-google-modules/kubernetes-engine/google` module (version `v45.0.0` or later).

### Using the Google Cloud Terraform provider

To enable Managed ML Diagnostics on a new cluster using the `google_container_cluster` resource, add the `managed_machine_learning_diagnostics_config` block with `enabled = true` using the `google-beta` provider (version `v7.28.0` or later):
    
    
    terraform {
      required_providers {
        google-beta = {
          source  = "hashicorp/google-beta"
          version = ">= 7.28.0"
        }
      }
    }
    
    resource "google_container_cluster" "primary" {
      provider = google-beta
      name     = "CLUSTER_NAME"
      location = "LOCATION"
    
      # ... other cluster configuration ...
    
      managed_machine_learning_diagnostics_config {
        enabled = true
      }
    }
    

To disable Managed ML Diagnostics on a cluster using the Terraform resource, set `enabled = false` in the `managed_machine_learning_diagnostics_config` block:
    
    
    resource "google_container_cluster" "primary" {
      provider = google-beta
      name     = "CLUSTER_NAME"
      location = "LOCATION"
    
      # ... other cluster configuration ...
    
      managed_machine_learning_diagnostics_config {
        enabled = false
      }
    }
    

### Using the GKE Terraform module

To enable Managed ML Diagnostics on a cluster using the [`terraform-google-modules/kubernetes-engine/google`](https://github.com/terraform-google-modules/terraform-google-kubernetes-engine) module (such as the `beta-public-cluster` submodule), set `enable_managed_machine_learning_diagnostics = true`:
    
    
    module "gke" {
      source  = "terraform-google-modules/kubernetes-engine/google//modules/beta-public-cluster"
      version = ">= 45.0"
    
      project_id = "PROJECT_ID"
      name       = "CLUSTER_NAME"
      region     = "LOCATION"
    
      # ... other cluster configuration ...
    
      enable_managed_machine_learning_diagnostics = true
    }
    

To disable Managed ML Diagnostics on a cluster using the Terraform module, set `enable_managed_machine_learning_diagnostics = false`:
    
    
    module "gke" {
      source  = "terraform-google-modules/kubernetes-engine/google//modules/beta-public-cluster"
      version = ">= 45.0"
    
      # ... other cluster configuration ...
    
      enable_managed_machine_learning_diagnostics = false
    }
    

After updating your configuration, apply the changes:
    
    
    terraform apply
    

To learn more about using Terraform with GKE, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

## Manual installation

For GKE versions prior to `1.35.0-gke.3065000`, you need to manually configure the GKE cluster to install the following:

  * `cert-manager`: A prerequisite for the `injection-webhook`.
  * `injection-webhook`: Provides the SDK with the required metadata. It supports common ML Kubernetes workloads, like `JobSet`, `RayJob`, and `LeaderWorkerSet`.
  * `connection-operator`: For on-demand profiling on GKE. Deploying `connection-operator` along with `injection-webhook` into the GKE cluster initializes profiling requests to target pods with profiling servers running when you trigger on-demand capture.



For more information about setting up a GKE cluster, see [Configure GKE cluster](https://github.com/AI-Hypercomputer/google-cloud-mldiagnostics#configure-gke-cluster).

### Cert-manager

The `cert-manager` add-on acts as the certificate controller for your cluster, ensuring that your applications are secure and that your certificates never unintentionally expire.

Use Helm to install the following:
    
    
    helm repo add jetstack https://charts.jetstack.io
    helm repo update
    
    helm install \
      cert-manager jetstack/cert-manager \
      --namespace cert-manager \
      --create-namespace \
      --version v1.13.0 \
      --set installCRDs=true \
      --set global.leaderElection.namespace=cert-manager \
      --timeout 10m
    

### Injection-webhook

The `injection-webhook` Helm chart passes metadata into the SDK. Use `helm upgrade --install` to install for the first time or upgrade an existing installation.
    
    
    helm upgrade --install mldiagnostics-injection-webhook \
      --namespace=gke-mldiagnostics \
      --create-namespace \
      --version 0.25.0 \
      oci://us-docker.pkg.dev/ai-on-gke/mldiagnostics-webhook-and-operator-helm/mldiagnostics-injection-webhook
    

### Connection-operator

The `connection-operator` Helm chart enables on-demand profiling on GKE. Use the following table to find the correct `mldiagnostics-connection-operator` version:

JAX version | Helm chart version  
---|---  
0.8.x | 0.24.0  
0.9.x+ | 0.24.0+  
  
Use Helm to install the required version.

For JAX 0.8.x:
    
    
    helm upgrade --install mldiagnostics-connection-operator \
      --namespace=gke-mldiagnostics \
      --create-namespace \
      --version 0.24.0 \
      oci://us-docker.pkg.dev/ai-on-gke/mldiagnostics-webhook-and-operator-helm/mldiagnostics-connection-operator \
      --set 'mldiagnosticsConnectionOperator.controller.args={--metrics-bind-address=:8443,--health-probe-bind-address=:8081,--sidecar-timeout=65m,--disable-hostname-override}'
    

For JAX 0.9.x+:
    
    
    helm upgrade --install mldiagnostics-connection-operator \
      --namespace=gke-mldiagnostics \
      --create-namespace \
      --version 0.24.0 \
      oci://us-docker.pkg.dev/ai-on-gke/mldiagnostics-webhook-and-operator-helm/mldiagnostics-connection-operator
    

## Label workload

For **programmatic profiling** , you need to trigger the `injection-webhook` to inject metadata into pods. Label either the workload or its namespace with `managed-mldiagnostics-gke=true` before deploying the workload:

  * **Label a workload** : Label a `JobSet`, `LeaderWorkerSet`, or `RayJob` workload, which enables the webhook for that specific workload. The following is an example for a `JobSet` workload:
        
        apiVersion: jobset.x-k8s.io/v1alpha2
        kind: JobSet
        metadata:
          name: single-host-tpu-v3-jobset2
          namespace: default
          labels:
            managed-mldiagnostics-gke: "true"
        

  * **Label a namespace** : This enables the webhook for all `JobSet`, `LeaderWorkerSet`, and `RayJob` workloads within that namespace.
        
        kubectl create namespace ai-workloads
        kubectl label namespace ai-workloads managed-mldiagnostics-gke=true
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 

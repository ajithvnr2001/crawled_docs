---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/configure-terraform/
title: Configure Terraform \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T05:59:24.462402+00:00
---

# Configure Terraform  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/configure-terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Configure Terraform Stay organized with collections  Save and categorize content based on your preferences. 

To use Terraform in your Google Distributed Cloud (GDC) air-gapped environment, you must download it and configure it to handle Kubernetes resources.

## Before you begin

  * Download Terraform 1.6.3 or later to your workstation following the documentation provided by HashiCorp: <https://developer.hashicorp.com/terraform/install>. The backend configuration in this document uses settings that older Terraform versions don't support.

  * [Verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-storage-buckets#verify_bucket_and_related_resource_creation) you have an existing GDC storage bucket. If you don't have a storage bucket, [create one](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-storage-buckets#create_a_bucket).

  * Make sure your system can recognize the Certificate Authority (CA) certificate used by object storage.




## Manage the state file

The state file in Terraform is used to record the current state of the deployment and map it to the Terraform configuration. Since GDC object storage is implemented using S3, you can use the Terraform S3 API to sync with a shared state file. To do this, you must configure Terraform to sync with the remote state:

  1. Add the following configuration to a Terraform file that is stored locally, such as the `main.tf` file:
         
         terraform {
           backend "s3" {
             bucket = "BUCKET_FQN"
             key = "TF_STATE_PATH"
             region = "ZONE"
             endpoints = {
               s3 = "BUCKET_ENDPOINT"
             }
             use_path_style = true
             access_key = "ACCESS_KEY"
             secret_key = "SECRET_KEY"
             skip_credentials_validation = true
             skip_requesting_account_id = true
             skip_metadata_api_check = true
             skip_region_validation = true
             skip_s3_checksum = true
           }
         }
         

Replace the following:

     * `BUCKET_FQN`: the `status.fullyQualifiedName` value from the `Bucket` custom resource. For example, `aabc2z8-platform-terraform-state`.

     * `TF_STATE_PATH`: the path of the Terraform state file to store in the storage bucket. For example, `main.tfstate`.

     * `ZONE`: the zone of the `Bucket` custom resource (`status.region`). For example, `zone1`. Terraform requires a region value, but GDC object storage doesn't check it.

     * `BUCKET_ENDPOINT`: the `status.endpoint` value from the `Bucket` custom resource. For example, `https://objectstorage.org-1.zone1.google.gdch.test`.

     * `ACCESS_KEY`: the access key acquired from the secret containing your access credentials. Follow [Obtain bucket access credentials](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/grant-obtain-storage-access#getting_bucket_access_credentials) to acquire the access key. The value in the secret is base64-encoded. Decode it before you use it.

     * `SECRET_KEY`: the secret key acquired from the secret containing your access credentials. Follow [Obtain bucket access credentials](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/grant-obtain-storage-access#getting_bucket_access_credentials) to acquire the secret key. The value in the secret is base64-encoded. Decode it before you use it.

GDC object storage is S3-compatible, but it isn't AWS. The remaining settings configure the backend for non-AWS S3 storage:

     * `use_path_style`: uses path-style bucket addressing for GDC object storage.

     * `skip_credentials_validation` and `skip_requesting_account_id`: stops Terraform from calling AWS STS and AWS IAM. GDC doesn't provide those services.

     * `skip_metadata_api_check`: stops Terraform from querying the AWS EC2 metadata service.

     * `skip_region_validation`: lets you use the zone name as the region.

     * `skip_s3_checksum`: stops Terraform from asking for a SHA-256 checksum when it uploads the state file.

**Note:** We recommend using environment variables to store the credentials. If credentials are hardcoded, they are stored within the `.terraform` directory and in plan files. To use environment variables, remove the `access_key` and `secret_key` settings and set the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables instead.
  2. Initialize the new state file edits in the storage bucket you specified in the previous step:
         
         terraform init
         




## Set permissions

Besides the permissions required to perform a specific task using Terraform, such as creating a GDC project, you must also have permissions to view custom resource definitions at that scope. Apply the required permissions to use Terraform:

  1. Create the `crd-viewer` cluster role resource:
         
         kubectl apply --kubeconfig KUBECONFIG -f - <<EOF
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRole
         metadata:
           name: crd-viewer
         rules:
         - apiGroups: ["apiextensions.k8s.io"]
           resources: ["customresourcedefinitions"]
           verbs: ["get", "list", "watch"]
         EOF
         

Replace `KUBECONFIG` with the kubeconfig file of the API server or cluster that hosts the resource you're managing with Terraform. For example, most resources run on the Management API server. For container workloads, set your Kubernetes cluster kubeconfig file. Be sure to set the global API server if you're managing a global resource.

  2. Bind the cluster role defined in the previous step to the user:
         
         kubectl apply --kubeconfig KUBECONFIG -f - <<EOF
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRoleBinding
         metadata:
           name: crd-viewer-binding
         subjects:
         - kind: User
           name: USER_EMAIL
         roleRef:
           kind: ClusterRole
           name: crd-viewer
           apiGroup: rbac.authorization.k8s.io
         EOF
         




Repeat these steps for each API server or cluster you want to set Terraform permissions for.

## Install and configure Terraform provider

You must install the [Kubernetes Provider](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs) to provision and manage Kubernetes resources.

  1. In a Terraform file within your module, such as the `main.tf` file, insert the following `required_providers` block:
         
         terraform {
           required_providers {
             kubernetes = {
               source = "hashicorp/kubernetes"
               version = ">=2.24.0"
             }
           }
         }
         

  2. Initialize your Terraform working directory to install the provider:
         
         terraform init
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 

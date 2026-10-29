---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/terraform/
title: Use Terraform \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T05:59:41.295965+00:00
---

# Use Terraform  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Use Terraform Stay organized with collections  Save and categorize content based on your preferences. 

To configure Terraform in your Google Distributed Cloud (GDC) air-gapped environment, you must download it and configure it to handle Kubernetes resources.

This document is for all audience groups that need to set up Terraform to manage their air-gapped hardware and software workflows. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

  * Download Terraform 1.6.3 or later to your workstation following the documentation provided by HashiCorp: <https://developer.hashicorp.com/terraform/install>. The backend configuration in this document uses settings that older Terraform versions don't support.

  * Verify that you have an existing GDC storage bucket. If you don't have a storage bucket, create one. For more information, see [Create storage buckets](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-storage-buckets).

  * Make sure your system can recognize the Certificate Authority (CA) certificate used by object storage.

  * Install the gdcloud CLI. For more information, see [Use the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/gdcloud).

  * Generate the kubeconfig file for the API server or cluster that's hosting the resources you want to manage with Terraform. For more information, see [Get a kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth#get-kubeconfig).




## Set up Terraform

To set up Terraform in your GDC environment, complete the following:

  1. Within your Terraform module, or collection of Terraform files on your workstation, create the `main.tf` file and add the following configuration:
         
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

     * `ACCESS_KEY`: the access key acquired from the secret containing your access credentials. For more information about acquiring the access key, see [Obtain bucket access credentials](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/grant-obtain-storage-access#getting_bucket_access_credentials). The value in the secret is base64-encoded. Decode it before you use it.

     * `SECRET_KEY`: the secret key acquired from the secret containing your access credentials. For more information about acquiring the secret key, see [Obtain bucket access credentials](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/grant-obtain-storage-access#getting_bucket_access_credentials). The value in the secret is base64-encoded. Decode it before you use it.

GDC object storage is S3-compatible, but it isn't AWS. The remaining settings configure the backend for non-AWS S3 storage:

     * `use_path_style`: uses path-style bucket addressing for GDC object storage.

     * `skip_credentials_validation` and `skip_requesting_account_id`: stops Terraform from calling AWS STS and AWS IAM. GDC doesn't provide those services.

     * `skip_metadata_api_check`: stops Terraform from querying the AWS EC2 metadata service.

     * `skip_region_validation`: lets you use the zone name as the region.

     * `skip_s3_checksum`: stops Terraform from asking for a SHA-256 checksum when it uploads the state file.

**Note:** We recommend using environment variables to store the credentials. If credentials are hardcoded, they are stored within the `.terraform` directory and in plan files. To use environment variables, remove the `access_key` and `secret_key` settings and set the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables instead.
  2. Initialize your Terraform state file in the storage bucket you specified in the previous step:
         
         terraform init
         

  3. Deploy the `crd-viewer` cluster role resource and bind it to your user account:
         
         kubectl apply --kubeconfig KUBECONFIG -f - <<EOF
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRole
         metadata:
           name: crd-viewer
         rules:
         - apiGroups: ["apiextensions.k8s.io"]
           resources: ["customresourcedefinitions"]
           verbs: ["get", "list", "watch"]
         ---
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
         

Replace the following:

     * `KUBECONFIG`: the kubeconfig file of the API server or cluster that hosts the resources you're managing with Terraform.

     * `USER_EMAIL`: the email of the user to bind the role to.

Deploy the `crd-viewer` role to each API server or cluster you want to use Terraform for.

  4. In the `main.tf` file, insert the following `required_providers` block:
         
         terraform {
           required_providers {
             kubernetes = {
               source = "hashicorp/kubernetes"
               version = ">=2.24.0"
             }
           }
         }
         

This configuration installs the [Kubernetes provider](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs) to provision and manage Kubernetes resources in your GDC environment.

  5. Initialize your Terraform working directory to install the provider:
         
         terraform init
         




## What's next

  * [Access zones with your tools](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/access-zones)
  * [Resource hierarchy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/resource-hierarchy)
  * [Connect to an identity provider](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/connect-identity)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog/
title: Cluster blueprint catalog \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:53:55.711450+00:00
---

# Cluster blueprint catalog  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Cluster blueprint catalog Stay organized with collections  Save and categorize content based on your preferences. 

This page provides a catalog of cluster blueprints, which are reusable YAML configuration files that define pre configured environments that you can deploy by using Cluster Toolkit. Each blueprint specifies the scheduler, storage, machine types, and base operating system for a specific workload. By default, cluster blueprints use a Rocky Linux 9 OS image. For more information about cluster blueprints, see [Cluster blueprints](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).

To search the catalog, filter by your required scheduler, storage type, machine type, base operating system, or featured software and Google Cloud resources. For machine types that automatically attach NVIDIA GPUs, the GPU model appears in parentheses in the **Select machine type** filter.

BatchGKESlurmHTCondorNoneCloud StorageFilestoreGoogle Cloud Managed LustreGoogle Cloud NetApp VolumesLocal SSDgke-persistent-volumegke-storagepre-existing-network-storageNoneA4X Max (NVIDIA GB300)A4 (NVIDIA B200)A4X (NVIDIA GB200 Superchips)A3 Ultra (NVIDIA H200)A3 Mega (NVIDIA H100)A3 High (NVIDIA H100)A2 (NVIDIA A100)C2 C2DC3C3DG4 (NVIDIA RTX PRO 6000)G2 (NVIDIA L4)H4DH3N2N2DN1TPU v4TPU v5eTPU v5pTPU v6eTPU7xContainer-Optimized OSdebian-12hpc-centos-7hpc-rocky-linux-8hpc-rocky-linux-9rocky-linux-9-optimized-gcpslurm-gcp-6-4-tf-2.14.0ubuntu-2204-ltsubuntu-2404-ltsubuntu-accelerator-2204-amd64-with-nvidia-580ubuntu-accelerator-2404-amd64-with-nvidia-580ubuntu-accelerator-2404-arm64-with-nvidia-580Advanced Compute ImagesAlphaFold 3Ansys FluentBare metalCloud RDMAConfidential VMGKE Inference GatewayGPUsTPUsGROMACSJAXKueueJobSetMaxTextNCCLNVIDIA IMEXOpenFOAMPackerPyTorchSpackStar CCM+TensorFlowVDI with VMDWRF

Clear all

**Cluster blueprint** | **Guide** | **Scheduler** | **Storage** | **Machine types** | **Base operating system** | **Featured software and compute resources** | **Collection**  
---|---|---|---|---|---|---|---  
[a4x-maxgpu-4g-metal](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/machine-learning/a4x-maxgpu-4g-metal) | [A4X Max for Slurm](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/slurm/create-a4x-max-cluster) | Slurm | Cloud Storage, Google Cloud Managed Lustre | A4X Max | `ubuntu-accelerator-2404-arm64-with-nvidia-580` | 

  * NVIDIA ConnectX-8
  * Bare metal
  * NVIDIA IMEX
  * GPUs
  * Cloud RDMA

| Core  
[gke-a4x-max-bm](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/gke-a4x-max-bm) | [A4X Max for GKE](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/create-a4x-max-cluster) | GKE | Cloud Storage, gke-persistent-volume | A4X Max | Container-Optimized OS | 

  * NVIDIA ConnectX-8
  * Bare metal
  * GPUs
  * JobSet
  * Kueue

| Core  
[gke-tpu-7x](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/gke-tpu-7x) | [TPU 7x for GKE](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-7x) | GKE | None | TPU7x | Container-Optimized OS | 

  * TPUs
  * JobSet
  * Kueue
  * JAX
  * Multi-VPC Networking

| Core  
[gke-tpu-v6e](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/gke-tpu-v6e) | [TPU v6e for GKE](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-v6e) | GKE | None | TPU v6e | Container-Optimized OS | 

  * TPUs
  * JobSet
  * Kueue
  * JAX
  * Multi-VPC Networking

| Core  
[gke-tpu-v5p](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/gke-tpu-v5p) |  | GKE | None | TPU v5p | Container-Optimized OS | 

  * TPUs
  * JobSet
  * Kueue
  * JAX

| Core  
[gke-tpu-v5e](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/gke-tpu-v5e) |  | GKE | None | TPU v5e | Container-Optimized OS | 

  * TPUs
  * JobSet
  * Kueue
  * JAX

| Core  
[gke-tpu-v4](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/gke-tpu-v4) |  | GKE | None | TPU v4 | Container-Optimized OS | 

  * TPUs
  * JobSet
  * Kueue
  * JAX

| Core  
[a4-highgpu-8g](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/machine-learning/a4-highgpu-8g) | [A4 for Slurm](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/slurm/create-a4-cluster) | Slurm | Cloud Storage, Google Cloud Managed Lustre | A4  | `ubuntu-2404-lts` | 

  * Advanced Compute Images
  * NVIDIA ConnectX-7
  * Google Virtual NIC (gVNIC)
  * GPUs
  * Virtual Private Cloud

| Core  
[a4x-highgpu-4g](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/machine-learning/a4x-highgpu-4g) | [A4X for Slurm](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/slurm/create-a4x-cluster) | Slurm | Cloud Storage, Google Cloud Managed Lustre | A4X | `ubuntu-2404-lts` | 

  * Advanced Compute Images
  * NVIDIA ConnectX-7
  * Google Virtual NIC (gVNIC)
  * NVIDIA IMEX
  * GPUs

| Core  
[gke-a4x](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/gke-a4x) | [A4X for GKE](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/create-a4x-cluster) | GKE | Cloud Storage, gke-persistent-volume | A4X | Container-Optimized OS | 

  * GPUs
  * JobSet
  * Kueue

| Core  
[gke-a3-ultragpu](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/gke-a3-ultragpu) | [A3 Ultra for GKE](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/create-a3-ultra-cluster) | GKE | Cloud Storage, gke-persistent-volume | A3 Ultra | Container-Optimized OS | 

  * NVIDIA ConnectX-7
  * Google Virtual NIC (gVNIC)
  * GPUs

| Core  
[gke-a3-highgpu](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/gke-a3-highgpu) | [A3 High for GKE](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/create-a3-high-cluster) | GKE | None | A3 High | Container-Optimized OS | 

  * GPUs
  * JobSet
  * Kueue

| Core  
[gke-a3-highgpu-inference-gateway](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#gke-a3-highgpu-inference-gatewayyaml-) |  | GKE | None | A3 High | Container-Optimized OS | 

  * GPUs
  * GKE Inference Gateway

| Core  
[gke-a3-megagpu](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/gke-a3-megagpu) | [A3 Mega for GKE](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/deploy-a3-mega-gke-cluster) | GKE | None | A3 Mega | Container-Optimized OS | 

  * GPUs
  * JobSet
  * Kueue

| Core  
[gke-managed-hyperdisk](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#gke-managed-hyperdiskyaml--) |  | GKE | gke-storage | C3 | Container-Optimized OS |  | Core, Experimental  
[gke-managed-lustre](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#gke-managed-lustreyaml-) |  | GKE | Google Cloud Managed Lustre, gke-persistent-volume | N2D | Container-Optimized OS |  | Core  
[gke-a4](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/gke-a4) | [A4 for GKE](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/create-a4-cluster) | GKE | Cloud Storage, gke-persistent-volume | A4  | Container-Optimized OS | 

  * GPUs
  * JobSet
  * Kueue

| Core  
[gke-g4](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/gke-g4) |  | GKE | None | G4 | Container-Optimized OS | 

  * GPUs
  * JobSet
  * Kueue

| Core  
[gke-g4-confidential](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/gke-g4-confidential) |  | GKE | gke-storage | G4 | Container-Optimized OS | 

  * Confidential VM
  * GPUs
  * JobSet
  * Kueue

| Core  
[ml-slurm-g4](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#ml-slurm-g4yaml-) |  | Slurm | Filestore | G4, N2 | `ubuntu-accelerator-2204-amd64-with-nvidia-580` | 

  * GPUs
  * Packer

| Core  
[gke-h4d](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/gke-h4d) |  | GKE | Filestore, gke-persistent-volume | H4D | Container-Optimized OS | 

  * Cloud RDMA
  * Google Virtual NIC (gVNIC)
  * JobSet
  * Kueue
  * Service account

| Core  
[a3-ultragpu-8g](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/machine-learning/a3-ultragpu-8g) | [A3 Ultra for Slurm](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/slurm/create-a3-ultra-cluster) | Slurm | Cloud Storage, Google Cloud Managed Lustre | A3 Ultra | `ubuntu-2404-lts` | 

  * Advanced Compute Images
  * NVIDIA ConnectX-7
  * Google Virtual NIC (gVNIC)
  * GPUs

| Core  
[a3-highgpu-8g](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/machine-learning/a3-highgpu-8g) | [A3 High for Slurm](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/slurm/create-a3-high-cluster) | Slurm | Google Cloud Managed Lustre | A3 High | `ubuntu-2204-lts*` | 

  * Google Virtual NIC (gVNIC)
  * GPUs

| Core  
[a3-megagpu-8g](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/machine-learning/a3-megagpu-8g) | [A3 Mega for Slurm](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/slurm/deploy-a3-mega-cluster) | Slurm | Cloud Storage, Google Cloud Managed Lustre | A3 Mega | `ubuntu-accelerator-2404-amd64-with-nvidia-580` | 

  * Google Virtual NIC (gVNIC)
  * GPUs

| Core  
[h4d-vm](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/h4d-vm.yaml) |  | None | Filestore, Local SSD | H4D | `hpc-rocky-linux-9` | 

  * Google Virtual NIC (gVNIC)
  * Cloud RDMA

| Core, Experimental  
[hpc-slurm-h4d](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/hpc-slurm-h4d) | [RDMA cluster with H4D](https://docs.cloud.google.com/cluster-toolkit/docs/quickstarts/create-a-slurm-cluster-h4d) | Slurm | Filestore, Local SSD | N2, H4D | `hpc-rocky-linux-9` | 

  * Google Virtual NIC (gVNIC)
  * Cloud RDMA

| Core  
[hpc-slurm](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#hpc-slurmyaml-) | [Slurm cluster](https://docs.cloud.google.com/cluster-toolkit/docs/quickstarts/slurm-cluster) | Slurm | Filestore | N2, C2 , H3 | `hpc-rocky-linux-9*` |  | Core  
[hpc-enterprise-slurm](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#hpc-enterprise-slurmyaml-) |  | Slurm | Filestore, Google Cloud Managed Lustre | N2, C2 , C2D, C3, A2, H3 | `hpc-rocky-linux-9*` | 

  * GPUs

| Core  
[hpc-slurm6-tpu-maxtext](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#hpc-slurm6-tpu-maxtextyaml--) |  | Slurm | None | TPU v4, N2, C2  | `slurm-gcp-6-4-tf-2.14.0*` | 

  * TPUs
  * MaxText

| Community, Experimental  
[ml-slurm](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#ml-slurmyaml-) |  | Slurm | Filestore | C2 , A2, G2 | `debian-12*` | 

  * GPUs
  * NCCL
  * PyTorch
  * TensorFlow

| Core  
[batch](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#batchyaml-) |  | Batch | Filestore | N2 | `rocky-linux-9-optimized-gcp` |  | Core  
[batch-mpi](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#batch-mpiyaml-) |  | Batch | Filestore | C2  | `hpc-rocky-linux-9` | 

  * Spack
  * Weather Research and Forecasting (WRF)

| Core  
[pfs-managed-lustre-slurm](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#pfs-managed-lustre-slurmyaml-) |  | Slurm | Google Cloud Managed Lustre | C2 , N2 | `hpc-rocky-linux-9*` |  | Core  
[pfs-managed-lustre-vm](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#pfs-managed-lustre-vmyaml-) |  | None | Google Cloud Managed Lustre | N2 | `hpc-rocky-linux-9` |  | Core  
[storage-slurm](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#storage-slurmyaml-) |  | Slurm | Cloud Storage | C3D | `hpc-rocky-linux-9*` |  | Core  
[storage-vm](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#storage-vmyaml-) |  | None | None | C3D | `hpc-rocky-linux-9` |  | Core  
[netapp-volumes](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#netapp-volumesyaml-) |  | None | Google Cloud NetApp Volumes | N2 | `hpc-rocky-linux-9` |  | Core  
[netapp-volumes-slurm](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#netapp-volumes-slurmyaml-) |  | Slurm | Google Cloud NetApp Volumes | N2 | `hpc-rocky-linux-9*` |  | Core  
[cae-slurm](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#cae-slurmyaml-) |  | Slurm | Filestore | H3, C3, N2 | `hpc-rocky-linux-9*` |  | Core  
[af3-slurm](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#af3-slurmyaml--) |  | Slurm | pre-existing-network-storage | C3D, G2, A2, N2, C2  | `hpc-rocky-linux-9*` | 

  * AlphaFold 3
  * GPUs
  * Packer

| Core, Experimental  
[tutorial-starccm](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/community/examples/tutorial-starccm.yaml) | [Simcenter STAR CCM+](https://docs.cloud.google.com/cluster-toolkit/docs/simcenter-star-ccm/run-workload) | None | Filestore | C2  | `hpc-centos-7` | 

  * Star CCM+

| Community, Experimental  
[tutorial-fluent](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/community/examples/tutorial-fluent.yaml) | [Ansys Fluent](https://docs.cloud.google.com/cluster-toolkit/docs/tutorials/ansys-fluent) | None | Filestore | C2  | `hpc-rocky-linux-9` | 

  * Ansys Fluent

| Community, Experimental  
[image-builder](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#image-builderyaml-) |  | Slurm | None | C2 , N2 | `hpc-rocky-linux-9*` | 

  * Packer

| Core  
[hpc-build-slurm-image](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#hpc-build-slurm-imageyaml--) |  | Slurm | None | N2D | `hpc-rocky-linux-9*` | 

  * Packer
  * Building Slurm

| Community, Experimental  
[hpc-amd-slurm](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/community/examples/AMD/README.md) |  | Slurm | Filestore | C2D | `hpc-rocky-linux-9*` | 

  * AMD
  * AMD Optimizing C/C++ and Fortran Compilers (AOCC)
  * OpenFOAM
  * Spack

| Community  
[hpc-slurm-local-ssd](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#hpc-slurm-local-ssdyaml--) |  | Slurm | Filestore, Local SSD | C2 , N1 | `hpc-rocky-linux-9*` |  | Community, Experimental  
[hpc-slurm-ubuntu2204](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/community/examples/hpc-slurm-ubuntu2204.yaml) |  | Slurm | Filestore | N2, C2  | `ubuntu-2204-lts` | 

  * Advanced Compute Images

| Community  
[hpc-slurm-gromacs](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#hpc-slurm-gromacsyaml--) |  | Slurm | Filestore | C2  | `hpc-rocky-linux-9*` | 

  * GROMACS
  * Spack

| Community, Experimental  
[hcls-blueprint](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#hcls-blueprintyaml-) |  | Slurm | Cloud Storage, Filestore | G2, C2  | `hpc-rocky-linux-9*` | 

  * GPUs
  * GROMACS on GPUs
  * Spack
  * VDI with VMD

| Core  
[htc-htcondor](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#htc-htcondoryaml--) |  | HTCondor | None | C2  | `hpc-rocky-linux-8` |  | Community, Experimental  
[ml-gke](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#ml-gkeyaml-) |  | GKE | None | G2 | Container-Optimized OS | 

  * GPUs

| Core  
[hpc-gke](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#hpc-gkeyaml-) |  | GKE | None | N2, C2  | Container-Optimized OS |  | Core  
[storage-gke](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#storage-gkeyaml-) |  | GKE | Filestore, Local SSD, Cloud Storage, gke-persistent-volume, gke-storage | N2D, C3D | Container-Optimized OS | 

  * CSI Drivers
  * Persistent Volumes

| Core  
[client-google-cloud-storage](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#client-google-cloud-storageyaml--) |  | None | Cloud Storage, pre-existing-network-storage | N2D | `hpc-rocky-linux-9` |  | Community, Experimental  
[hpc-slurm-sharedvpc](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#hpc-slurm-sharedvpcyaml--) |  | Slurm | Filestore | N2, C2  | `hpc-rocky-linux-9*` | 

  * Shared VPC configuration

| Community, Experimental  
  
*This OS image is an optimized SchedMD Slurm image that is based on the specified operating system.

## What's next

  * To set up your environment, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * To learn about the deployment process, see [Cluster deployment overview](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/deploy-cluster-overview).
  * To customize your blueprints by using modules, see [Modules](https://docs.cloud.google.com/cluster-toolkit/docs/modules/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

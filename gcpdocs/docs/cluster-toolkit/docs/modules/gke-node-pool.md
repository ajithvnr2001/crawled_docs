---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-node-pool/
title: Create a Google Kubernetes node pool \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:54:04.597446+00:00
---

# Create a Google Kubernetes node pool  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-node-pool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create a Google Kubernetes node pool Stay organized with collections  Save and categorize content based on your preferences. 

You use the `gke-node-pool` module to define and configure node pools for your Google Kubernetes Engine (GKE) clusters within Cluster Toolkit blueprints. This module simplifies setting up worker nodes, so you can tailor configurations like machine types, autoscaling, hardware accelerators (GPUs/TPUs), and storage. By customizing these settings, you optimize performance and resource utilization for your high performance computing (HPC) or artificial intelligence (AI) workloads on Google Cloud. 

To use this module, your Cluster Toolkit blueprint must reference an existing [GKE cluster](https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-cluster). For a complete list of inputs and outputs, see the [`gke-node-pool` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/compute/gke-node-pool/README.md#inputs) in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for the `gke-node-pool` module, see the [`examples/hpc-gke.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/hpc-gke.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints that support the `gke-node-pool` module, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page, click the **Select scheduler** menu and then select **GKE**.
  * In your blueprint, you must have added a [GKE cluster](https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-cluster).



### Required roles

To get the permissions that you need to create and manage GKE node pools, ask your administrator to grant you the following IAM roles on your project: 

  * [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`)
  * [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a GKE node pool

To create a node pool, add the `gke-node-pool` module to your blueprint and connect it to your GKE cluster.

The following example creates a node pool:
    
    
      - id: compute_pool
        source: modules/compute/gke-node-pool
        use: [gke_cluster]
    

## Configure node taints and tolerations

By default, the `gke-node-pool` module applies the taint `user-workload=true:NoSchedule` to prevent system pods from being scheduled on your worker nodes. Your jobs targeting this node pool must include the corresponding toleration.

You can override this behavior by using the `--node-taints` flag. For more information, see [Configure workload separation in GKE](https://cloud.google.com/kubernetes-engine/docs/how-to/node-taints).

## Configure Local SSD storage

GKE offers the following two options for managing locally attached SSDs (Local SSDs):

  * **Ephemeral storage:** To let GKE manage the storage, set the `local_ssd_count_ephemeral_storage` field to a value of `1`. We recommend this method because it automatically attaches the storage to pods that request an `emptyDir` volume. For example:
        
        - id: local-ssd-pool
          source: modules/compute/gke-node-pool
          use: [gke_cluster, node_pool_service_account]
          settings:
            name: local-ssd
            machine_type: n2d-standard-2
            local_ssd_count_ephemeral_storage: 1
        

  * **Raw block storage:** To attach nodes as raw block storage, use the field `local_ssd_count_nvme_block`. This option requires you to handle Redundant Array of Independent Disks (RAID) settings, partitioning, and formatting manually, but it is useful for use cases that `emptyDir` volumes don't support, such as `ReadOnlyMany` or `ReadWriteMany` persistent volumes. For example:
        
        cli_deployment_vars:
          region: "us-central1"
          zone: "us-central1-a"
          network_name: "default"
          reservation_affinity: "ANY_RESERVATION"
          local_ssd_count_nvme_block: 2
        

**Note:** The number of SSDs that you can attach depends on the machine type. For more information, see the [Machine families resource and comparison guide](https://docs.cloud.google.com/compute/docs/machine-resource).



## Configure GPU support

When you attach a GPU to a node, the module automatically adds the taint `nvidia.com/gpu=present:NoSchedule`. To place jobs on these nodes, you must provide the equivalent toleration. If you use the `gke-job-template` module, the module applies this toleration automatically.

### Install drivers

We recommend that you install Nvidia GPU drivers by applying a DaemonSet to the cluster. For installation instructions, see [Manually install NVIDIA GPU drivers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#cos).

If you need to compile a custom driver (for example, to install a specific version), you must disable the `enable_secure_boot` option to let unsigned kernel modules load.

### GPU configuration examples

This section describes how you can add GPUs to a node pool. Use one of the following approaches, based upon your requirements:

  * **Pre-defined GPU machine families:** For A2, A3, and G2 machine types, the GPU configuration is inferred automatically.
        
        - id: simple-a2-pool
          source: modules/compute/gke-node-pool
          use: [gke_cluster]
          settings:
            machine_type: a2-highgpu-1g
        

  * **Partitioned GPUs (A100):** To partition an A100 GPU, specify the `guest_accelerator` block.
        
        - id: multi-instance-gpu-pool
          source: modules/compute/gke-node-pool
          use: [gke_cluster]
          settings:
            machine_type: a2-highgpu-1g
            guest_accelerator:
            - gpu_partition_size: 1g.5gb
        

  * **Time-sharing GPUs:** To enable time-sharing, configure the `gpu_sharing_config` setting.
        
        - id: time-sharing-gpu-pool
          source: modules/compute/gke-node-pool
          use: [gke_cluster]
          settings:
            machine_type: a2-highgpu-1g
            guest_accelerator:
            - gpu_partition_size: 1g.5gb
              gpu_sharing_config:
                gpu_sharing_strategy: TIME_SHARING
                max_shared_clients_per_gpu: 3
        

  * **Attached GPUs (N1 family):** To attach GPUs to N1 machines, specify the type and count.
        
        - id: t4-pool
          source: modules/compute/gke-node-pool
          use: [gke_cluster]
          settings:
            machine_type: n1-standard-16
            guest_accelerator:
            - type: nvidia-tesla-t4
              count: 2
        

  * **Attached GPUs with time-sharing (N1 family):** To use a GPU with sharing configuration attached to an N1 machine, specify the `gpu_sharing_config` block within `guest_accelerator`.
        
        - id: n1-t4-pool
            source: modules/compute/gke-node-pool
            use: [gke_cluster]
            settings:
              name: n1-t4-pool
              machine_type: n1-standard-1
              guest_accelerator:
              - type: nvidia-tesla-t4
                count: 2
                gpu_driver_installation_config:
                  gpu_driver_version: "LATEST"
                gpu_sharing_config:
                  max_shared_clients_per_gpu: 2
                  gpu_sharing_strategy: "TIME_SHARING"
        

  * **Multi-networking:** To add multi-networking support to a node pool (for example, when using A3 Mega GPUs), configure the `vpc` and `multivpc` modules, and reference them in your `gke-cluster` and `gke-node-pool` definitions.
        
        - id: network
          source: modules/network/vpc
          settings:
            subnetwork_name: gke-subnet
            secondary_ranges:
              gke-subnet:
              - range_name: pods
                ip_cidr_range: 10.4.0.0/14
              - range_name: services
                ip_cidr_range: 10.0.32.0/20
        
        - id: multinetwork
          source: modules/network/multivpc
          settings:
            network_name_prefix: multivpc-net
            network_count: 8
            global_ip_address_range: 172.16.0.0/12
            subnetwork_cidr_suffix: 16
        
        - id: gke-cluster
          source: modules/scheduler/gke-cluster
          use: [network, multinetwork]
          settings:
            cluster_name: $(vars.deployment_name)
        
        - id: a3-megagpu_pool
          source: modules/compute/gke-node-pool
          use: [gke-cluster, multinetwork]
          settings:
            machine_type: a3-megagpu-8g
        ...
        




## Configure capacity reservations

Use Compute Engine reservations to ensure that resources are available for your workloads when needed. For more information about managing reservations, see [Choose a reservation type](https://docs.cloud.google.com/compute/docs/instances/reserving-zonal-resources).

After you create a reservation, you can consume the reserved Compute Engine instances in your cluster by using the `reservation_affinity` field. Clusters that are deployed by using Cluster Toolkit support the following consumption modes:

  * **`NO_RESERVATION` (default):** The node pool does not consume any reservation and uses on-demand capacity. This mode is the default setting.
  * **`ANY_RESERVATION`:** The node pool automatically consumes any available matching reservation that creates compute instances with properties (such as machine type and region) matching the node pool. If no matching reservation is found, the node pool generally falls back to on-demand capacity depending on your project's configuration.
        
        reservation_affinity:
          consume_reservation_type: ANY_RESERVATION
        

  * **`SPECIFIC_RESERVATION`:** The node pool targets a specific reservation by name. This mode sets the node pool to consume capacity only from the specified reservation.
        
        # Target a specific reservation
        reservation_affinity:
          consume_reservation_type: SPECIFIC_RESERVATION
          specific_reservations:
          - name: specific-reservation-1
        




To use a specific reservation, ensure that your configuration meets the following requirements:

  * A reservation with the specified name exists in the project (`var.project_id`) and zone (`var.zones`) that you specified.
  * The reservation consumption type is specific. For more information, see [How reservations work](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#how-reservations-work).
  * The compute instance properties of the reservation, such as the machine type, accelerators, and Local SSD count, must match the properties of the node pool.



To use a shared reservation, you must explicitly specify the owner project of the shared reservation. A shared reservation lets a consumer project use capacity reserved by an owner project.

**Note:** A shared reservation must use a `consume_reservation_type` type value of `SPECIFIC_RESERVATION`. For more information, see [Create a shared reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-shared).
    
    
    reservation_affinity:
      consume_reservation_type: SPECIFIC_RESERVATION
      specific_reservations:
      - name: specific-reservation-shared
        project: shared_reservation_owner_project_id
    

### Pin node pools to reservation sub-blocks

Reservations that use a dense allocation model, such as future reservations for capacity blocks and future reservations in calendar mode, are divided into [blocks and sub-blocks](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology). A sub-block is a group of hosts that share a high-bandwidth interconnect, such as one NVLink domain. To keep each node pool within one sub-block, you can create multiple node pools from a single `gke-node-pool` module and pin each node pool to its own sub-block.

Before you pin node pools to sub-blocks, verify that your `gke-node-pool` module's `settings` block meets the following requirements:

  * **Reservation type is set to`SPECIFIC_RESERVATION`:** Set the `consume_reservation_type` field to `SPECIFIC_RESERVATION` and include only one entry in the `specific_reservations` field. Set the `name` field to only the reservation name, not the path of a block or sub-block.
  * **Matching node pool count:** If you manually specify the `reservation_subblocks` field, then the value in the `num_node_pools` field must equal the number of entries in the `reservation_subblocks` field.
  * **Set IAM permissions:** To let the `gcluster` CLI propose sub-blocks, you must have the `compute.reservationBlocks.list` and `compute.reservationSubBlocks.list` permissions on the project that owns the reservation, such as the Compute Viewer (`roles/compute.viewer`) role. For a shared reservation, set the `project` field in the `specific_reservations` field to the owner project ID. If the `reservation_subblocks` field already contains all entries, then you don't need these permissions.



To pin node pools to sub-blocks, set the following fields in the `settings` block of the module:

  * `num_node_pools`: the number of node pools to create, with one node pool for each sub-block.
  * `pin_to_subblocks`: a boolean value that specifies whether the `gcluster` CLI chooses the sub-blocks. To let the `gcluster` CLI choose the sub-blocks, set this field to `true`.
  * `reservation_subblocks`: a map of keys to paths of reservation sub-blocks. We recommend that you reference a variable in your deployment file so that the `gcluster` CLI can save the map to your deployment file.



The following example creates three node pools of 18 nodes each, with one node pool in each of the three sub-blocks:
    
    
    vars:
      reservation_subblocks: {}   # gcluster automatically populates this map on the first deployment
    deployment_groups:
    - group: primary
      modules:
      - id: gpu-sb
        source: modules/compute/gke-node-pool
        use: [gke_cluster]
        settings:
          name: gpu-sb
          machine_type: a4x-highgpu-4g
          zones: [us-central1-a]
          num_node_pools: 3
          static_node_count: 18
          reservation_affinity:
            consume_reservation_type: SPECIFIC_RESERVATION
            specific_reservations:
            - name: my-reservation
              pin_to_subblocks: true
              reservation_subblocks: $(vars.reservation_subblocks)
    

**Important:** Keep the `name` field in the `settings` block short (8 characters or fewer). Each node pool is named `NAME-KEY`, where `NAME` is the value of the `name` field (such as `gpu-sb`) and `KEY` is the key in the `reservation_subblocks` map (such as `02-0001`). If `NAME-KEY` exceeds 16 characters, then GKE truncates the node pool prefix in the names of the compute instances and instance templates, which can make node pools difficult to distinguish.

When you run the [`gcluster deploy`](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy) or [`gcluster create`](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-create) command, the `gcluster` CLI checks the `reservation_subblocks` map and, depending on the number of entries, does one of the following:

  * **Fewer entries than specified in the`num_node_pools` field:** If the map is empty or has fewer entries than the value of the `num_node_pools` field, then the `gcluster` CLI lists the sub-blocks of the reservation and proposes available sub-blocks. The `gcluster` CLI proposes `HEALTHY` sub-blocks first, and proposes `DEGRADED` sub-blocks with a warning only if there are not enough `HEALTHY` sub-blocks available. After you confirm the proposed sub-blocks, the `gcluster` CLI saves the updated map to your deployment file and keeps a backup of the previous file.
  * **More entries than specified in the`num_node_pools` field:** If the map has more entries than the value of the `num_node_pools` field, then the `gcluster` CLI proposes to remove the extra entries, and the next deployment deletes the node pools for the removed entries.
  * **Equal entries to the value specified in the`num_node_pools` field:** If the map already has the number of entries that is specified in the `num_node_pools` field, then the `gcluster` CLI uses the map without prompting you for confirmation to proceed.



Each node pool is named `NAME-BLOCK_NAME-SUBBLOCK_NAME`, such as `gpu-sb-02-0001`, where `NAME` is the value of the `name` field, `BLOCK_NAME` is the block number, and `SUBBLOCK_NAME` is the sub-block number. Because each node pool is identified by its key in the `reservation_subblocks` map, if you add or remove an entry, then the `gcluster` CLI creates or deletes only that node pool. If you change the sub-block for an entry, then the `gcluster` CLI recreates only that node pool.

To choose the sub-blocks yourself, omit the `pin_to_subblocks` field or set the field to `false`, and set the `reservation_subblocks` field to a map of your choice:
    
    
    reservation_subblocks:
      "01-0001": my-reservation/reservationBlocks/my-reservation-block-0001/reservationSubBlocks/my-reservation-block-0001-subblock-0001
      "01-0002": my-reservation/reservationBlocks/my-reservation-block-0001/reservationSubBlocks/my-reservation-block-0001-subblock-0002
    

## What's next

  * To learn how to submit jobs to this node pool, see [Create a Google Kubernetes job template](https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-job-template).
  * For a complete list of all available input fields and output values, see the [`gke-node-pool` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/compute/gke-node-pool/README.md#inputs) on GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

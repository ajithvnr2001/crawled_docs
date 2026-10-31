---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/mixed-local-ssd/
title: Provision and use mixed Local SSDs for raw block and ephemeral storage \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:02.772931+00:00
---

# Provision and use mixed Local SSDs for raw block and ephemeral storage  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/mixed-local-ssd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Provision and use mixed Local SSDs for raw block and ephemeral storage Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows you how to provision and partition [Local SSDs](https://docs.cloud.google.com/compute/docs/disks/local-ssd) in Google Kubernetes Engine (GKE) to support workloads that require both a standard ephemeral storage file system and unformatted raw block storage on the same node.

Use this configuration for stateful applications and highly optimized databases. These workloads often require direct disk access for increased performance, but also need standard ephemeral file storage for sidecars, logs, or container caches. By using mixed Local SSD capacity, you can reduce cluster management overhead and maximize hardware utilization, because you don't need to dedicate separate nodes or full disks exclusively to raw block infrastructure.

When you create a cluster or node pool with mixed Local SSD capacity, GKE partitions every physically attached Local SSD as follows:

  * **Ephemeral storage:** the requested ephemeral capacity is divided equally across the Local SSDs and combined to provide the node's standard ephemeral file storage. When ephemeral capacity is partitioned across multiple Local SSDs, the storage is combined into a [RAID-0](https://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_0) array. You can access the ephemeral storage using standard [`emptyDir` volumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd#use).
  * **Raw block storage:** the remainder of the physical capacity on each disk is presented to the node as distinct, unformatted raw block devices.



This document is for Platform admins and operators and DevOps who want to optimize hardware utilization and storage performance in GKE for specialized workloads.

## Considerations

In addition to the [Compute Engine Local SSD limitations](https://docs.cloud.google.com/compute/docs/disks/local-ssd#limitations), review the following GKE-specific considerations before configuring mixed Local SSD modes:

  * **Autopilot compatibility:** GKE Autopilot clusters do not support mixed raw block and ephemeral storage. To learn how to use Local SSDs for standard ephemeral storage in Autopilot, see [Local SSDs in Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd#local-ssd-autopilot).
  * **Custom ComputeClasses:** custom ComputeClasses don't support mixed Local SSD configuration.
  * **Operating system:** mixed Local SSD mode is supported only on Linux node images (Container-Optimized OS and Ubuntu). Windows Server node pools aren't supported.
  * **Maintenance events:** we don't recommend using Local SSD as raw block storage for storage-optimized Z3 or Z4D VMs. Data on these VMs might not survive maintenance events. For more information, see [Provision and use Local SSD-backed raw block storage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd-raw).
  * **Shared I/O:** because both the ephemeral RAID-0 array and your targeted raw block partitions rely on the same underlying physical SSDs, intensive operations on one logical partition might impact the throughput of the other. For information about maximum throughput limits, see [Local SSD performance](https://docs.cloud.google.com/compute/docs/disks/local-ssd#performance).
  * **Pricing:** when you use mixed modes to partition Local SSD capacity, you pay for the total underlying physical Local SSD capacity attached to the node, regardless of how much capacity is allocated for ephemeral storage compared to raw block storage. For more information, see [Local SSD pricing](https://cloud.google.com/products/compute/pricing/storage-optimized).
  * **Manual configuration:** to use Local SSD-backed raw block storage, you must manually configure the devices because GKE doesn't format or mount the raw block partitions. You are also responsible for managing node capacity and handling potential disruptions from colocated workloads. Using a [local PersistentVolume object](https://kubernetes.io/docs/concepts/storage/volumes/#local) provides integrated Pod scheduling. If your workloads don't require data to persist across the Pod lifecycle, or if they lack specialized performance needs, use the [fully ephemeral Local SSD configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd) instead. The fully ephemeral configuration is suitable for most use cases.
  * **Node memory swap:** you can combine mixed Local SSD capacity with node memory swap by using the boot disk profile or the ephemeral Local SSD profile. The dedicated Local SSD profile isn't supported with mixed Local SSD capacity. For more information, see [Node memory swap with mixed Local SSD capacity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-memory-swap#mixed-local-ssd).



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



To use this feature, GKE nodes must run version 1.37.0-gke.3570000 or later.

### Required roles

To get the permissions that you need to create clusters and node pools with mixed Local SSD capacity, ask your administrator to grant you the [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a cluster or node pool with mixed Local SSD storage

You can allocate ephemeral capacity and reserve raw block partitions by using the `capacity` property of the `--ephemeral-storage-local-ssd` flag.

Create your cluster or node pool by specifying the `capacity` subfield with the `--ephemeral-storage-local-ssd` flag.

If your machine type allows a configurable number of Local SSDs, you must also specify the `count` subfield. If your machine type has a fixed number of Local SSDs, for example, `-lssd` types, you can omit the `count` subfield because GKE automatically calculates the disk count based on the VM shape.

### Create a cluster with mixed Local SSD storage

To create a new cluster, use the `gcloud container clusters create` command. These settings apply to the default node pool only. If subsequent node pools need mixed Local SSD storage, specify the `--ephemeral-storage-local-ssd` flag when you create the node pool. The maximum number of disks you can attach [varies by machine type and region](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_number_local_ssds).

If the version for your cluster is earlier than `1.37.0-gke.3570000`, add one of the following flags to the following cluster creation commands:

  * The `--cluster-version=VERSION` flag with `VERSION` set to `1.37.0-gke.3570000` or later, or
  * The `--release-channel=rapid` flag.



**For machine types with a configurable Local SSD count, run the following:**
    
    
    gcloud container clusters create CLUSTER_NAME \
        --machine-type=MACHINE_TYPE \
        --ephemeral-storage-local-ssd count=NUMBER_OF_DISKS,capacity=CAPACITY
    

**For machine types with a fixed Local SSD count, run the following:**
    
    
    gcloud container clusters create CLUSTER_NAME \
        --machine-type=MACHINE_TYPE \
        --ephemeral-storage-local-ssd capacity=CAPACITY
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster you want to create.
  * `MACHINE_TYPE`: the machine type to use. For a list of supported machine types, see [Machine series support](https://docs.cloud.google.com/compute/docs/disks/local-ssd#machine-series-lssd). You cannot use Local SSDs with the default `e2-medium` machine type, because [shared-core machine types](https://docs.cloud.google.com/compute/docs/disks/local-ssd#limitations) don't support them.
  * `NUMBER_OF_DISKS`: for machine types with a configurable Local SSD count, the number of Local SSD disks to provision on each node.
  * `CAPACITY`: the total Local SSD capacity to format for ephemeral storage. This value must be greater than 0 and strictly less than the total physical Local SSD capacity (disk count × per-disk size), for example, `200GB`. Note the following:

    * The value can't be changed after the cluster is created.
    * GKE reserves part of this capacity for system use, so allocatable ephemeral storage is less than `CAPACITY`. For more information, see [Local ephemeral storage reservation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes#local_ephemeral_storage_reservation).



### Create a node pool with mixed Local SSD storage

To add a node pool to an existing cluster, use the `gcloud container node-pools create` command.

If the version for your node pool is earlier than `1.37.0-gke.3570000`, you must do the following:

  * Add the `--node-version=VERSION` flag to the following node pool creation commands, with `VERSION` set to `1.37.0-gke.3570000` or later.
  * Ensure that the cluster control plane is on version `1.37.0-gke.3570000` or later.



**For machine types with a configurable Local SSD count, run the following:**
    
    
    gcloud container node-pools create POOL_NAME \
        --cluster=CLUSTER_NAME \
        --machine-type=MACHINE_TYPE \
        --ephemeral-storage-local-ssd count=NUMBER_OF_DISKS,capacity=CAPACITY
    

**For machine types with a fixed Local SSD count, run the following:**
    
    
    gcloud container node-pools create POOL_NAME \
        --cluster=CLUSTER_NAME \
        --machine-type=MACHINE_TYPE \
        --ephemeral-storage-local-ssd capacity=CAPACITY
    

Replace the following:

  * `POOL_NAME`: the name of the new node pool you want to create.
  * `CLUSTER_NAME`: the name of the cluster.
  * `MACHINE_TYPE`: the machine type to use. For a list of supported machine types, see [Machine series support](https://docs.cloud.google.com/compute/docs/disks/local-ssd#machine-series-lssd). You cannot use Local SSDs with the default `e2-medium` machine type, because [shared-core machine types](https://docs.cloud.google.com/compute/docs/disks/local-ssd#limitations) don't support them.
  * `NUMBER_OF_DISKS`: for machine types with a configurable Local SSD count, the number of Local SSD disks to provision on each node.
  * `CAPACITY`: the total Local SSD capacity to format for ephemeral storage. This value must be greater than 0 and strictly less than the total physical Local SSD capacity (disk count × per-disk size), for example, `200GB`. Note the following:

    * The value can't be changed after the node pool is created.
    * GKE reserves part of this capacity for system use, so allocatable ephemeral storage is less than `CAPACITY`. For more information, see [Local ephemeral storage reservation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes#local_ephemeral_storage_reservation).



### Verify the node labels

After provisioning, to verify that the nodes have the correct labels for both ephemeral and raw block storage, run the following command:
    
    
    kubectl describe node NODE_NAME
    

The output should contain both of the following node labels:

  * `cloud.google.com/gke-ephemeral-storage-local-ssd: "true"`
  * `cloud.google.com/gke-local-nvme-ssd-partition: "true"`

**Note:** The `cloud.google.com/gke-local-nvme-ssd-partition: "true"` label is distinct from the `cloud.google.com/gke-local-nvme-ssd=true` label that is used for fully raw block configuration. For more information about using fully raw block configuration, see [Local SSD-backed raw block storage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd-raw#create).

## Access the ephemeral capacity

Access your reserved ephemeral storage through [`emptyDir` volumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd#use) exactly as you would for any other GKE ephemeral volume.

## Access the raw block capacity

To access your raw block capacity, you create a StorageClass object, provision a local PersistentVolume object, and claim it using a PersistentVolumeClaim object.

**Warning:** The standard raw block workflow uses a community RAID DaemonSet (`gke-daemonset-raid-disks.yaml`) together with the [local volume static provisioner](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd-raw#run-local-volume-static-provisioner). If you adapt the RAID `DaemonSet` for your mixed configuration nodes (for example, by modifying its `nodeSelector`), you must _not_ run this RAID configuration. GKE already manages the ephemeral portion of each disk, and running the RAID DaemonSet breaks your node's ephemeral capacity.

### Create a StorageClass

Because you are provisioning your PersistentVolume objects without the community static provisioner, we recommend creating a StorageClass object with the `volumeBindingMode: WaitForFirstConsumer` field. This delays binding until Pod scheduling, ensuring that Kubernetes chooses a Local SSD from an appropriate node that can run the Pod.
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: "local-storage"
    provisioner: "kubernetes.io/no-provisioner"
    volumeBindingMode: "WaitForFirstConsumer"
    

### Create the PersistentVolume

Local PersistentVolume objects have important limitations regarding node upgrades, scaling, and cluster autoscaling. Before creating your volumes, review the [Limitations of local PersistentVolumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd-raw#limitations_of_local_persistentvolumes) to understand how lifecycle events affect your data.

To create the PersistentVolume object, complete the following steps to find the symbolic link path to the Local SSD partition, determine its exact remaining capacity, and configure the manifest.

#### Find the partition capacity

Run the following command on the target node to find the exact raw block capacity left over for the partition.
    
    
    kubectl debug node/NODE_NAME -it --image=ubuntu -- \
        sh -c 'ls -l /host/dev/disk/by-id/ | grep partition; lsblk -o NAME,SIZE,TYPE'
    

Replace `NODE_NAME` with the name of the node where the Local SSD is attached.

The output shows the mapping between device names and partition symlinks so that you can verify which partition corresponds to which device. It also lists the block devices attached to the node and their sizes.

For example, if you attach two Local SSDs to the node and allocate 200 GB to ephemeral storage (`capacity=200GB`), the output is similar to the following:
    
    
    google-local-ssd-partition0 -> /dev/nvme0n1p2
    google-local-ssd-partition1 -> /dev/nvme0n2p2
    NAME          SIZE TYPE
    ...
    nvme0n1       375G disk
    |-nvme0n1p1   100G part
    | `-md0     199.9G raid0
    `-nvme0n1p2   275G part
    nvme0n2       375G disk
    |-nvme0n2p1   100G part
    | `-md0     199.9G raid0
    `-nvme0n2p2   275G part
    

Note the mapping between the `google-local-ssd-partition` symlink and the underlying device name, as well as the size of that partition. You use the size as the `PARTITION_SIZE` and the symlink path as the `LOCAL_SSD_SYMLINK_PATH` in the PersistentVolume manifest.

For example, in the preceding output, the `/dev/disk/by-id/google-local-ssd-partition0` symlink points to the `nvme0n1p2` partition, which has a size of `275G`.

The `kubectl debug` command leaves a temporary Pod running in the default namespace. To prevent it from consuming resources, delete this Pod by running the following command:
    
    
    kubectl delete pod DEBUG_POD_NAME
    

Replace `DEBUG_POD_NAME` with the name of the Pod created by the `kubectl debug` command, which is printed when you run the command.

#### Configure the PersistentVolume manifest

Configure the volume manifest with the partition size you found. The `nodeAffinity` field is required for local volumes. It helps ensure that Kubernetes schedules Pods claiming this volume to the specific node where the Local SSD is physically attached. The following example shows a manifest for a raw block Local SSD partition:
    
    
    apiVersion: v1
    kind: PersistentVolume
    metadata:
      name: "example-local-pv"
    spec:
      capacity:
        storage: PARTITION_SIZE
      accessModes:
      - "ReadWriteOnce"
      volumeMode: "Block"
      persistentVolumeReclaimPolicy: "Retain"
      storageClassName: "local-storage"
      local:
        path: "LOCAL_SSD_SYMLINK_PATH"
      nodeAffinity:
        required:
          nodeSelectorTerms:
          - matchExpressions:
            - key: "kubernetes.io/hostname"
              operator: "In"
              values:
              - "NODE_NAME"
    

Replace the following:

  * `PARTITION_SIZE`: the actual raw block capacity left over that you found in the first step. Use the `Gi` suffix (for example, `275Gi`) so that the value matches the capacity of the partition exactly.
  * `NODE_NAME`: the name of the node where the Local SSD is attached.
  * `LOCAL_SSD_SYMLINK_PATH`: the symbolic link path to the unformatted Local SSD partition that you found in the first step. For each Local SSD attached to the node pool, the host OS creates a symbolic link to access the remaining raw block capacity. The paths follow a zero-indexed pattern. For example, if you attach three Local SSDs, the raw block paths for the partitions are the following: 
    * `/dev/disk/by-id/google-local-ssd-partition0`
    * `/dev/disk/by-id/google-local-ssd-partition1`
    * `/dev/disk/by-id/google-local-ssd-partition2`



### Create the PersistentVolumeClaim

Create a PersistentVolumeClaim object to claim the volume. The corresponding specification looks like the following:
    
    
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: "example-local-pvc"
    spec:
      accessModes:
      - "ReadWriteOnce"
      volumeMode: "Block"
      storageClassName: "local-storage"
      resources:
        requests:
          storage: PARTITION_SIZE
    

## Use the volume in a Pod

You can use the PersistentVolume object in a Pod by referencing the PersistentVolumeClaim object in a `volumeDevices` specification. The following is a sample Pod manifest that uses the `example-local-pvc` claim:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: "example-pod"
    spec:
      containers:
      - name: "app"
        image: "ubuntu:22.04"
        command: ["/bin/sh", "-c"]
        args: ["tail -f /dev/null"]
        volumeDevices:
        - name: "raw"
          devicePath: "/dev/xvda"
      volumes:
      - name: "raw"
        persistentVolumeClaim:
          claimName: "example-local-pvc"
    

Because you are using the `kubernetes.io/no-provisioner` provisioner, GKE does not automatically clean up local volumes. If you delete the PersistentVolume object, you must manually erase data from the underlying disk before the disk can be safely reused.

## Troubleshooting

For troubleshooting instructions, see [Troubleshooting storage in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshooting-gke-storage#local-ssds).

## What's next

  * Learn how to use [fully ephemeral Local SSD storage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd) for workload caching.
  * Learn how to provision [fully raw block Local SSD volumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd-raw) for dedicated high-performance database storage.
  * Learn how to [deploy a stateful application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-apps).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 

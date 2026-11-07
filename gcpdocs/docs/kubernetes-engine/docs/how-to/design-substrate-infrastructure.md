---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/design-substrate-infrastructure/
title: Design your infrastructure for Agent Substrate on GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-07T05:42:53.288691+00:00
---

# Design your infrastructure for Agent Substrate on GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/design-substrate-infrastructure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Design your infrastructure for Agent Substrate on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Google Kubernetes Engine (GKE) lets you scale [Agent Substrate on GKE](https://docs.cloud.google.com/kubernetes-engine/ai-ml/about-agent-substrate) clusters to support high-concurrency AI agentic workloads while minimizing idle compute costs. By combining dedicated system infrastructure node pools with custom ComputeClasses and capacity buffers, you can isolate critical system components, automate hardware fallback across Compute Engine machine series, and keep standby Worker capacity warm.

Read this document to right-size your GKE cluster components, isolate system infrastructure and database node pools, configure automated node provisioning for WorkerPool resources, and plan for cluster maintenance and upgrades. This document is for platform administrators who provision and manage Agent Substrate on GKE infrastructure.

## Before you begin

Before you configure your cluster infrastructure for scale, ensure that your environment meets the following requirements:

  * **GKE cluster mode and version** : you must use a GKE Standard cluster in which both the control plane and the node pools run version 1.37 or later. GKE Autopilot clusters aren't supported for Agent Substrate on GKE.
  * **Agent Substrate on GKE installation** : you must have an existing Agent Substrate on GKE installation or plan to install Agent Substrate on GKE with system infrastructure node isolation enabled. For installation steps, see [Install Agent Substrate on GKE](https://docs.cloud.google.com/kubernetes-engine/ai-ml/install-overview-substrate).



## Right-size your Agent Substrate cluster

Size your cluster for peak concurrency and peak resume rates rather than averages. Worker nodes must hold the maximum number of Actors running at the same time, and the system infrastructure components and storage paths must keep up with the fastest rate of Actor resumes and suspends.

### Estimate your workload peaks

If you don't have production measurements, then estimate your peak concurrency and resume rate from your total registered Actor count (`total_actors`), the average fraction of Actors running concurrently (`average_active_fraction`), your traffic burst multiplier (`burst_factor`), and the average duration that an Actor stays active per turn (`average_seconds_active_per_resume`):
    
    
    peak_running_actors = total_actors × average_active_fraction × burst_factor
    peak_resume_rate    = peak_running_actors / average_seconds_active_per_resume

For example, if you have 100,000 total Actors with 10% active on average (10,000 Actors) and a burst factor of two, then your cluster must support 20,000 peak running Actors. If each Actor runs for an average of 100 seconds before suspending, then sustaining that peak requires 200 resumes per second and 200 suspends per second.

Agent Substrate on GKE doesn't suspend idle Actors automatically; your application or orchestrator must trigger suspension.

### Size the data plane

This section covers best practices for sizing the data plane, including Worker Pods, GKE nodes, snapshot bandwidth, and the `atelet` node agent.

#### Calculate Worker Pods and GKE nodes

Each Worker Pod in a WorkerPool hosts multiple Actors. A Worker can accept a new Actor while it hosts fewer Actors than the limit set by the `--max-actors` flag on the `ateworker` container (default `1000`) and has enough remaining CPU and memory capacity to fit the ActorTemplate limits. For more information about how Worker limits interact with Actor limits, see the open source [Right-sizing resources in the Agent Substrate API guide](https://github.com/agent-substrate/substrate/blob/main/docs/reference/api-guide.md#sandbox-right-sizing-resources).

Calculate the required number of Worker Pods with 20% available scheduling capacity (the `0.8` factor):
    
    
    slots_per_worker = min(max_actors, worker_memory / actor_memory, worker_cpu / actor_cpu)
    total_workers    = peak_running_actors / (slots_per_worker × 0.8)

In this formula, the `max_actors` variable defaults to `1000` (configured by the `--max-actors` flag). Subtract the memory that the Worker reserves for its own process from the `worker_memory` value. For microVM WorkerPool resources, add the per-Actor virtual machine monitor (VMM) memory overhead reported by the Worker to the `actor_memory` value, because placement counts that overhead against Worker capacity.

With one Worker Pod per node, the number of Workers equals the number of GKE worker nodes. Don't allocate 100% of a node's allocatable CPU and memory to the Worker Pod; leave capacity on each node for the `atelet` DaemonSet (in the `ate-system` namespace) and GKE system daemons. GKE Standard supports up to [65,000 nodes per cluster and up to 512 Pods per node](https://docs.cloud.google.com/kubernetes-engine/quotas#limits_per_cluster). The default maximum is 110 Pods per node (configurable with the `--max-pods-per-node` flag), and [large clusters have additional requirements](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-clusters#clusters-5k-nodes).

#### Size snapshot bandwidth and node disks

Each Actor suspend writes a snapshot to the local node disk under the `/var/lib/ate` directory path. In `SYNCHRONOUS` mode, the `atelet` agent uploads the snapshot to Cloud Storage before the suspend operation returns. In `ASYNCHRONOUS` mode, the `atelet` agent schedules the upload to Cloud Storage after a delay of approximately the `--snapshot-upload-delay` flag value (default `5m`) from when the snapshot is taken. Agent Substrate caches the latest snapshot on the node for the period configured in the `--snapshot-detach-delay` flag, which defaults to a value of `30m`. An Actor that resumes within that window schedules onto the same node and restores from the local disk instead of downloading the snapshot from Cloud Storage.

Estimate your uncompressed snapshot size (`snapshot_size`) as the ActorTemplate memory limit plus any data written to the writable root file system or durable directories. Sparse file handling and `zstd` compression reduce the compressed snapshot size (`compressed_snapshot_size`) transferred to and from Cloud Storage, where Agent Substrate stores up to two snapshots per Actor (the previous snapshot and the in-progress snapshot):

  * **Peak Cloud Storage bandwidth (each direction):** `peak_resume_rate × compressed_snapshot_size`
  * **Peak node disk write throughput per node:** `2 × peak_resume_rate × snapshot_size / total_nodes` (both resume downloads and suspend checkpoints write to the node disk).



The default 100 GiB `hyperdisk-balanced` boot disk in GKE provides [3,600 IOPS and 290 MiB/s of throughput](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#default-perf) (default performance scales with disk size), which can limit snapshot operations under heavy guest I/O. When you create worker node pools, either mount a dedicated disk at the `/var/lib/ate/snapshots` directory path or increase boot disk performance by using the `--boot-disk-provisioned-iops` and `--boot-disk-provisioned-throughput` flags with the `gcloud container node-pools create` command.

#### Check Security Token Service quota

Each snapshot transfer to or from Cloud Storage requires a token scoped to the Actor, which the `ate-api-server` component requests from the [Security Token Service (STS) API](https://docs.cloud.google.com/iam/docs/reference/sts/rest). The `ate-api-server` component makes up to one STS request per Actor every 20 to 40 minutes (typically on the first resume in that window) and reuses the token until 20 minutes before expiration.

The STS `Exchange token global requests` quota defaults to _6,000 requests per project per minute_ and is shared with Workload Identity Federation for GKE:

  * **Required STS quota (requests per minute):** estimate as up to 60 times the peak rate of resumes for Actors whose last snapshot transfer was more than 20 minutes ago, plus capacity for Workload Identity Federation for GKE. If you don't know that rate, use the `60 × peak_resume_rate` formula as a fallback. For example, 200 resumes per second requires up to 12,000 requests per minute.
  * **How to increase quota:** request a quota increase on the **Quotas & System Limits** page in Google Cloud console. Snapshot transfers work without the Security Token Service API enabled in your project, but you must enable the API for the quota to appear on the **Quotas & System Limits** page. For more information, see [Quota for the Exchange Token API in Security Token Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity#sts-quota) in the Workload Identity Federation for GKE documentation.



#### Tune the `atelet` node agent

The `atelet` DaemonSet runs one Pod per worker node to restore and checkpoint Actors. In each `atelet` Pod, the `objectstore-plugin` container compresses and transfers snapshots to and from Cloud Storage.

The following table describes key sizing settings for the `atelet` and `objectstore-plugin` containers:

Setting | Default | Sizing guidance  
---|---|---  
`atelet` and `objectstore-plugin` container CPU and memory  | Requests: 50 mCPU, 128 MiB memory; no limits |  Configure Burstable QoS without memory limits by omitting memory limits on both containers, because hitting a memory limit stops the node agent and halts all resumes on the node. Raise CPU and memory requests to match measured peak usage on a full node at your peak resume rate so Worker Pods don't consume resources needed by the `atelet` agent.   
`--upload-memory-budget` flag (`objectstore-plugin` container) and `--snapshot-upload-workers` flag (`atelet` container)  | 512 MiB budget; 2 upload workers |  To prevent concurrent snapshot uploads from queuing on multi-Actor nodes with high suspend rates, do the following: 

  * Increase the value of the `--upload-memory-budget` flag (and set the `objectstore-plugin` container memory request higher than this budget). 
  * Increase the value of the `--snapshot-upload-workers` flag. 

  
`--drain-timeout` flag and `terminationGracePeriodSeconds` field  |  5 minutes (`--drain-timeout` flag); 330 seconds (`terminationGracePeriodSeconds` field)  |  Controls how long the `atelet` agent finishes in-flight restores and snapshot uploads when its Pod stops during a node drain or upgrade. If you increase the value of the `--drain-timeout` flag for large snapshots, then also increase the value of the `terminationGracePeriodSeconds` field on the `atelet` DaemonSet so the `kubelet` agent doesn't stop the `atelet` agent before uploads finish.   
  
### Size system infrastructure components and the database

For stateless system component Deployments in the `ate-system` namespace that scale horizontally, estimate the required replica count with 35% available capacity (the `0.65` factor) plus one spare replica (`+ 1`) to tolerate node disruptions:
    
    
    replicas = ceil(peak_load / (capacity_per_replica × 0.65)) + 1

Horizontal scaling stops improving throughput after a shared dependency (such as PostgreSQL CPU or connection limits) reaches capacity. Size your system infrastructure components and database together. For more information about component flags, see the open source [operator install guide](https://github.com/agent-substrate/substrate/blob/main/docs/guides/operator-install.md#settings).

The following table describes resource and scaling rules for each system infrastructure component:

Component | QoS and resource rules | Scaling and connection tuning  
---|---|---  
Ingress router (`atenet-router`) |  **Configure Guaranteed QoS** : set matching CPU and memory requests and limits so the Go runtime aligns its thread count with the container CPU budget.  |  Scale replicas horizontally based on peak ingress requests per second, mTLS overhead, and request payload sizes.   
API server (`ate-api-server`) |  **Configure Guaranteed QoS** : set matching CPU and memory requests and limits so the Go runtime aligns its thread count with the container CPU budget.  |  Scale replicas based on peak resume and suspend cycles per second (approximately 4 ms of CPU per resume and suspend cycle) and ingress request lookup load. Explicitly set the `ateapi.postgres.poolMaxConns` setting. Each replica opens up to `poolMaxConns + 6` database connections, and the sum across all replicas must stay less than the PostgreSQL `max_connections` setting.   
Database (PostgreSQL) |  **Configure Burstable QoS with guaranteed memory** : set memory requests equal to limits to lock the `shared_buffers` cache in memory and help prevent out-of-memory (OOM) eviction. Omit CPU limits when running on a dedicated `ate-postgres` node so kernel CPU throttling doesn't slow down checkpoint and autovacuum bursts.  |  Scale this single-instance StatefulSet vertically. Provision enough CPU to stay at less than 80% utilization at peak load, enough RAM to cache the Actor table (with the `shared_buffers` parameter set to approximately 25% of memory), and an SSD-backed StorageClass set at installation time with the `ateapi.postgres.storageClass` setting (for example, the `dynamic-rwo` StorageClass on C4 or N4, or the `premium-rwo` StorageClass on C3 or N2). Increase the `max_connections` parameter in the `postgres-config` ConfigMap (the `postgresql.conf` file) to fit all `ate-api-server` replicas.   
Egress proxy (`atenet-egress`) |  **Resource rules** : set a CPU request of 512 mCPU (limit 8 vCPUs) and a memory request of 512 MiB (limit 1 GiB). Increase requests and limits if outbound Actor traffic experiences increased latency.  |  Scale replicas horizontally based on Actor outbound request traffic.   
Worker controller (`ate-controller`) |  **Resource rules** : keep at one replica (no leader election). Set CPU and memory requests based on peak usage during large WorkerPool scale-out events.  |  If new Worker Pods take too long to register in large fleets, then increase the value of the `--worker-sync-concurrency` flag (default `2`).   
Certificate controller (`podcertificate-controller`)  |  **Resource rules** : runs in the `podcertificate-controller-system` namespace to sign mTLS certificates for new Worker Pods before they can accept Actors.  |  For fleets of thousands of Workers, increase the values of the `podcert.workersPerSigner` setting (default `0`, which keeps the manifest default of `1` worker per signer), the `--kube-api-qps` flag (default `5`), and the `--kube-api-burst` flag (default `10`).   
Identity provider (`ate-idp-server`) |  **Resource rules** : serves the OpenID Connect (OIDC) discovery document and JSON Web Key Set (JWKS) in the `ate-system` namespace for verifying Actor JSON Web Tokens (JWTs). Set CPU and memory requests based on peak JWKS query volume.  |  Scale replicas horizontally if relying parties query the JWKS endpoint at high request rates without caching keys.   
Credential provider (`k8s-credential-provider`)  |  **Resource rules** : runs in the `ate-system` namespace when Kubernetes Secret credential injection is enabled. Set CPU and memory requests based on outbound credential-injection volume.  |  Scale replicas horizontally based on the rate of outbound Actor requests that require Kubernetes Secret credential injection at the `atenet-egress` proxy.   
  
## Isolate system infrastructure and worker node pools

In production clusters, high-churn Actor scheduling and snapshot traffic on worker nodes can compete with system infrastructure components for CPU, memory, and disk I/O. Separate your GKE cluster into three distinct node pool tiers:

  * **Database node pool (`ate-postgres` label)**: a dedicated node pool for the PostgreSQL StatefulSet, which stores all Actor and Worker metadata.
  * **System infrastructure node pool (`ate-system-infra` label)**: a dedicated node pool for the remaining system infrastructure services (the `atenet-router`, `ate-api-server`, `atenet-egress`, `ate-controller`, `ate-idp-server`, and `k8s-credential-provider` components).
  * **Worker node pools (WorkerPool)** : dynamically scaled node pools managed by GKE custom ComputeClasses and GKE capacity buffers to host active Actor sandboxes.



You can isolate the database and system infrastructure components onto dedicated nodes when you install Agent Substrate on GKE by using the `cordonSystemInfraComponents` setting (or the `--cordon-system-infra-components` flag). Before you install, you must create both node pools with the required labels and `NoSchedule` taints:
    
    
    # 1. Create the dedicated PostgreSQL node pool
    gcloud container node-pools create ate-postgres-pool \
        --cluster=CLUSTER_NAME \
        --location=LOCATION \
        --node-locations=POSTGRES_ZONE \
        --machine-type=POSTGRES_MACHINE_TYPE \
        --num-nodes=1 \
        --node-labels=ate.dev/workloadType=ate-postgres \
        --node-taints=ate.dev/workloadType=ate-postgres:NoSchedule
    
    # 2. Create the dedicated system infrastructure node pool
    gcloud container node-pools create ate-system-infra-pool \
        --cluster=CLUSTER_NAME \
        --location=LOCATION \
        --machine-type=SYSTEM_INFRA_MACHINE_TYPE \
        --num-nodes=2 \
        --node-labels=ate.dev/workloadType=ate-system-infra \
        --node-taints=ate.dev/workloadType=ate-system-infra:NoSchedule
    

Replace the following:

  * `CLUSTER_NAME`: the name of your GKE Standard cluster.
  * `LOCATION`: the Compute Engine zone or region of your cluster's control plane.
  * `POSTGRES_ZONE`: a single Compute Engine zone for the single-replica PostgreSQL StatefulSet. For a regional cluster, specify one zone within the cluster's region so that the node pool provisions a single node in the zone where the StatefulSet's persistent disk will be created. For a zonal cluster, specify the cluster's zone.
  * `POSTGRES_MACHINE_TYPE`: the Compute Engine machine type sized for your PostgreSQL instance.
  * `SYSTEM_INFRA_MACHINE_TYPE`: the Compute Engine machine type sized for your system infrastructure components (for example, the `c3-standard-8` machine type).



In a regional cluster, the `--num-nodes` flag applies per zone (for example, setting the `--num-nodes=2` flag across three zones creates six nodes total). To place the `ate-system-infra-pool` node pool in specific zones, add the `--node-locations` flag.

If you enable the `cordonSystemInfraComponents` setting during installation and either node pool is missing, the corresponding system Pods remain in the `Pending` state.

## Automate hardware targeting using custom ComputeClasses

GKE [custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes) let you define prioritized lists of Compute Engine machine series for your WorkerPool nodes and automatically fall back to secondary machine series if a zone experiences resource unavailability.

### Select Compute Engine machine series by runtime

Configure a separate ComputeClass for each sandbox runtime:

  * **MicroVM runtime (Cloud Hypervisor)** : set the `enableNestedVirtualization: true` field in your ComputeClass priorities and target x86 Compute Engine machine series that support [nested virtualization](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview) (such as N4, C3, C4, or N2), or use x86 bare-metal machine types, which run KVM natively and don't require the `enableNestedVirtualization` field. Arm-based VMs and machine series listed in [Nested virtualization restrictions](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview#restrictions) aren't supported.
  * **gVisor runtime** : target general-purpose or compute-optimized x86 Compute Engine machine series (such as N4, C3, C4, or N2) without nested virtualization enabled. Machine series that run on mixed CPU microarchitectures (such as E2) and Arm-based VMs aren't supported for Agent Substrate on GKE. All WorkerPool resources that an ActorTemplate selects must share the same CPU architecture.



For a detailed comparison, see [Select a sandbox runtime](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-workloads#select-sandbox-runtime).

### Required ComputeClass rules for Agent Substrate

When you create a ComputeClass for Agent Substrate on GKE worker nodes, follow these rules:

  * **Use node-based ComputeClasses** : don't use Pod-based billing (the `podFamily` field), which doesn't support nested virtualization.
  * **Don't set the`nodePoolConfig.sandbox.type: microvm` field**: that setting enables the Kata runtime for GKE Sandbox on Pod-based workloads and applies a `sandbox.gke.io/runtime=microvm` taint that prevents Agent Substrate on GKE Workers from scheduling. Agent Substrate on GKE manages its own microVM runtime and requires only Compute Engine nested virtualization on standard Container-Optimized OS (`cos_containerd` image type) nodes.
  * **Configure Linux kernel`sysctl` settings for high sandbox density**: if a worker node runs more than approximately 800 concurrent sandboxes, you must increase the Linux kernel limits for file system monitoring (`fs.inotify.*` parameters) and for the Address Resolution Protocol (ARP) neighbor table (`net.ipv4.neigh.default.gc_thresh*` parameters). The installer applies these settings only to clusters that it creates. When you configure custom ComputeClasses (by using the `priorityDefaults.nodeSystemConfig.linuxNodeConfig.sysctls` field) or pre-create worker node pools (by using the `--system-config-from-file` flag), apply the following `sysctl` values yourself:

    * `fs.inotify.max_user_instances`: `65536`
    * `fs.inotify.max_user_watches`: `1048576`
    * `net.ipv4.neigh.default.gc_thresh1`: `4096`
    * `net.ipv4.neigh.default.gc_thresh2`: `16384`
    * `net.ipv4.neigh.default.gc_thresh3`: `32768`

For more information about configuring node `sysctl` parameters, see [Sysctl configuration options](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#sysctl-options).




### Choose a scale-up pattern for microVM WorkerPool resources

MicroVM Worker Pods request the `ate.dev/kvm: 1` extended resource, which is advertised by the `atelet` device plugin only after a node boots and the `atelet` agent starts. Because GKE node auto-provisioning doesn't see the `ate.dev/kvm` extended resource on unprovisioned node templates, a pending microVM Worker Pod can't trigger GKE to auto-create a new node pool from zero replicas on its own. However, if a node pool already has at least one running node, GKE can scale that node pool up.

The following table compares the supported patterns for scaling microVM WorkerPool resources on GKE:

Pattern | How it works | Scales to 0 nodes? | Multi-priority fallback for resource unavailability? | Best used when  
---|---|---|---|---  
Auto-created pools with the `minimumCapacity` field  |  Sets the `nodePoolAutoCreation.enabled: true` and `minimumCapacity.targetNodeCount: 1` fields with explicit `machineType` priorities.  | No (keeps 1 warm node running) |  Only at initial provisioning for the class-level `minimumCapacity` field; mid-burst fallback requires setting the `minimumCapacity.targetNodeCount: 1` field on each fallback entry in the `spec.priorities[]` field (keeping 1 warm node per priority)  |  You want automated node pool creation and always keep at least 1 worker node running.   
Auto-created pools with capacity buffers |  Combines the `nodePoolAutoCreation.enabled: true` field with an active or standby CapacityBuffer whose PodTemplate omits the `ate.dev/kvm` extended resource.  |  Suspends to standby (for example, approximately 8% of running compute cost on a `c3-standard-4` node with a default 100 GiB boot disk)  |  Yes (buffer placeholders trigger node auto-provisioning fallback across priorities)  |  You want fast burst scaling (1 to 4 seconds active, or 20 to 35 seconds to resume standby nodes and 50 to 85 seconds until new Workers are ready) with low idle cost.   
Pre-created 0-node pools with node-template labels  |  Pre-creates autoscaled 0-node pools with the `clusterautoscaler-nodetemplate-resources.ate.dev/kvm=4096` label and references them in the `spec.priorities[].nodepools` field of the ComputeClass.  | Yes (true 0 nodes, no idle compute cost) | Yes, across the pre-created node pools |  You want true scale-to-zero without maintaining standby capacity buffers.   
  
#### Example: ComputeClass with the `minimumCapacity` field

When you use the `minimumCapacity` field, every entry in the `spec.priorities` field must specify an explicit `machineType` field instead of only specifying the `machineFamily` field:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: substrate-microvm
    spec:
      priorityDefaults:
        enableNestedVirtualization: true
        nodeSystemConfig:
          linuxNodeConfig:
            sysctls:
              fs.inotify.max_user_instances: 65536
              fs.inotify.max_user_watches: 1048576
              net.ipv4.neigh.default.gc_thresh1: 4096
              net.ipv4.neigh.default.gc_thresh2: 16384
              net.ipv4.neigh.default.gc_thresh3: 32768
      priorities:
      - machineType: n4-standard-4
      - machineType: c3-standard-4
      - machineType: n2-standard-4
      nodePoolAutoCreation:
        enabled: true
      minimumCapacity:
        targetNodeCount: 1
      nodePoolConfig:
        imageType: cos_containerd
      whenUnsatisfiable: DoNotScaleUp
    

To target a WorkerPool to this ComputeClass, add the `nodeSelector: {cloud.google.com/compute-class: substrate-microvm}` field to the WorkerPool Pod template.

When a ComputeClass falls back across different x86 machine series (such as from N4 to C3 or N2), restoring a durable snapshot at memory fidelity (the `SNAPSHOT_FIDELITY_MEMORY` mode) requires a Worker whose CPU features are a superset of the snapshot's CPU features. If no compatible Worker has capacity, Agent Substrate downgrades the restore to root-file-system fidelity (the `SNAPSHOT_FIDELITY_ROOTFS` mode), which preserves root file system and durable volume data while restarting the Actor's processes.

**Note:** Setting the `spec.minimumCapacity.targetNodeCount: 1` field at the ComputeClass level falls back to secondary priorities (the `c3-standard-4` or `n2-standard-4` machine types) only if the primary priority (the `n4-standard-4` machine type) is unavailable when provisioning that first node. After the primary priority provisions one node, the fallback priorities remain at zero nodes and can't scale from zero during mid-burst resource unavailability because pending microVM Worker Pods request the `ate.dev/kvm: 1` extended resource. To allow mid-burst fallback across priorities with the `minimumCapacity` field, set the `minimumCapacity.targetNodeCount: 1` field on each fallback entry under the `spec.priorities[]` field, which keeps one warm node running per priority. Alternatively, use capacity buffers or pre-created 0-node pools.

#### Example: Scale from zero with pre-created 0-node pools

  1. Save the high-density Linux kernel `sysctl` settings as a `system-config.yaml` file:
         
         linuxConfig:
           sysctl:
             fs.inotify.max_user_instances: '65536'
             fs.inotify.max_user_watches: '1048576'
             net.ipv4.neigh.default.gc_thresh1: '4096'
             net.ipv4.neigh.default.gc_thresh2: '16384'
             net.ipv4.neigh.default.gc_thresh3: '32768'
         

  2. Pre-create your primary and fallback nested-virtualization node pools at 0 nodes with the `--system-config-from-file=system-config.yaml` flag and the `clusterautoscaler-nodetemplate-resources.ate.dev/kvm=4096` label so the GKE cluster autoscaler knows that the empty pool provides the `ate.dev/kvm` extended resource:
         
         # Primary N4 pool (0 nodes)
         gcloud container node-pools create microvm-n4-pool \
             --cluster=CLUSTER_NAME \
             --location=LOCATION \
             --machine-type=n4-standard-4 \
             --enable-nested-virtualization \
             --system-config-from-file=system-config.yaml \
             --num-nodes=0 \
             --enable-autoscaling --total-min-nodes=0 --total-max-nodes=10 \
             --node-labels=cloud.google.com/compute-class=substrate-microvm-zero,clusterautoscaler-nodetemplate-resources.ate.dev/kvm=4096 \
             --node-taints=cloud.google.com/compute-class=substrate-microvm-zero:NoSchedule
         
         # Fallback C3 pool (0 nodes)
         gcloud container node-pools create microvm-c3-pool \
             --cluster=CLUSTER_NAME \
             --location=LOCATION \
             --machine-type=c3-standard-4 \
             --enable-nested-virtualization \
             --system-config-from-file=system-config.yaml \
             --num-nodes=0 \
             --enable-autoscaling --total-min-nodes=0 --total-max-nodes=10 \
             --node-labels=cloud.google.com/compute-class=substrate-microvm-zero,clusterautoscaler-nodetemplate-resources.ate.dev/kvm=4096 \
             --node-taints=cloud.google.com/compute-class=substrate-microvm-zero:NoSchedule
         

Replace the following:

     * `CLUSTER_NAME`: the name of your GKE Standard cluster.
     * `LOCATION`: the Compute Engine zone or region of your cluster. Using the `--total-min-nodes` and `--total-max-nodes` flags sets the autoscaling bounds across the entire node pool rather than per zone.
  3. Reference the pre-created pools in priority order in your ComputeClass:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: substrate-microvm-zero
         spec:
           nodePoolAutoCreation:
             enabled: false
           priorities:
           - nodepools:
             - microvm-n4-pool
           - nodepools:
             - microvm-c3-pool
           whenUnsatisfiable: DoNotScaleUp
         

The `priorityDefaults` field doesn't apply to priorities that use the `nodepools` field, because node settings come from the pre-created node pools. As with auto-created fallback priorities, resuming an Actor on a fallback machine series whose CPU features aren't a superset of the snapshot's CPU features downgrades the restore to the `SNAPSHOT_FIDELITY_ROOTFS` mode and restarts the Actor's processes.




For more information about ComputeClass configuration, see [Control autoscaled node attributes with custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-attributes-compute-classes).

## Configure capacity buffers for WorkerPool burst scaling

When an Actor traffic spike exceeds the capacity of your running WorkerPool Pods, new Worker Pods must wait for Compute Engine node provisioning, `atelet` agent initialization, and sandbox asset prewarming before they can serve Actors. [GKE capacity buffers](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/capacity-buffer) move node provisioning and `atelet` asset prewarming off the critical path:

  * **Active capacity buffers (`buffer.x-k8s.io/active-capacity` strategy)**: keep pre-provisioned nodes running and ready so new Worker Pods schedule in one to four seconds, at the full running cost of the Compute Engine VM.
  * **Standby capacity buffers (`buffer.gke.io/standby-capacity` strategy)**: provision nodes and let the `atelet` agent initialize and prewarm sandbox assets (the `runsc` binary or Cloud Hypervisor and Kata images) on disk during the [standby initialization window](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-capacity-buffer#customize-standby-behavior) before GKE suspends the Compute Engine VMs. This window defaults to five minutes (`5m`) and is configured by the `buffer.gke.io/standby-capacity-init-time` annotation on the CapacityBuffer. Increase the value of this annotation if asset prewarming takes longer than five minutes. When a burst occurs, GKE resumes the suspended nodes in approximately 20 to 35 seconds, and end-to-end WorkerPool readiness (scheduling Worker Pods, issuing Pod certificates, and registering capacity with the `ate-api-server` component) completes in approximately 50 to 85 seconds. While suspended, you pay only for suspended VM memory and boot disk storage. For example, suspended storage costs approximately 8% of the running compute cost on a `c3-standard-4` node with a default 100 GiB `hyperdisk-balanced` boot disk; the exact percentage varies with machine shape, boot disk size, and provisioned IOPS or throughput.



For more information about buffer strategies, see [Strategies to reduce startup latency](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/startup-latency-reduction-strategies).

### Limitations and rules for capacity buffers

When you configure capacity buffers for Agent Substrate on GKE, apply the following rules:

  * **Compute Engine machine-shape restrictions for standby buffers** : Compute Engine instance suspension isn't supported on VMs with attached Local SSDs or on machine shapes with more than 208 GB of memory (such as the `c3-highmem-88` machine type or bare metal shapes). For large worker node shapes or nodes with Local SSDs, use active capacity buffers instead of standby buffers.
  * **Avoid pointing the`scalableRef` field at a 0-replica WorkerPool or microVM Deployment**: 
    * The GKE CapacityBuffer controller can't resolve a custom resource (`kind: WorkerPool`) when the pool is scaled to 0 replicas.
    * For microVM WorkerPool resources, also don't point the `scalableRef` field at the underlying Deployment, because the Deployment Pod template includes the `ate.dev/kvm: 1` extended resource (which prevents node auto-provisioning from scaling out an empty pool). Instead, configure buffers by referencing a PodTemplate (in the `podTemplateRef` field) that selects the ComputeClass without requesting the `ate.dev/kvm` extended resource.
    * For gVisor WorkerPool resources (which don't request the `ate.dev/kvm` extended resource), you can point the `scalableRef` field directly to the WorkerPool underlying Deployment or use a PodTemplate.



#### Example: Standby CapacityBuffer using a PodTemplate

The following manifest defines a PodTemplate and a standby CapacityBuffer that work for either microVM or gVisor WorkerPool resources:
    
    
    apiVersion: v1
    kind: PodTemplate
    metadata:
      name: substrate-worker-buffer-template
      namespace: WORKERPOOL_NAMESPACE
    template:
      spec:
        nodeSelector:
          cloud.google.com/compute-class: COMPUTE_CLASS_NAME
        containers:
        - name: buffer-placeholder
          image: registry.k8s.io/pause:3.9
          resources:
            requests:
              cpu: "WORKER_CPU_REQUEST"
              memory: "WORKER_MEMORY_REQUEST"
    ---
    apiVersion: autoscaling.x-k8s.io/v1beta1
    kind: CapacityBuffer
    metadata:
      name: substrate-standby-buffer
      namespace: WORKERPOOL_NAMESPACE
    spec:
      podTemplateRef:
        name: substrate-worker-buffer-template
      replicas: BUFFER_REPLICAS
      provisioningStrategy: buffer.gke.io/standby-capacity
    

Replace the following:

  * `WORKERPOOL_NAMESPACE`: the Kubernetes namespace of your WorkerPool (for example, `my-workerpool`).
  * `COMPUTE_CLASS_NAME`: the name of the custom ComputeClass targeted by your WorkerPool (for example, `substrate-microvm`).
  * `WORKER_CPU_REQUEST` and `WORKER_MEMORY_REQUEST`: the CPU and memory requests of a single Worker Pod in your WorkerPool (for example, `2` CPUs and `4Gi` of memory on a 4-vCPU node), leaving node capacity for the `atelet` agent and GKE system daemons. Matching these values to one Worker Pod's requests helps ensure that each buffer replica provisions one standby worker node rather than packing multiple buffer placeholders onto a single node.
  * `BUFFER_REPLICAS`: the number of standby worker nodes to keep prewarmed (for example, `4` nodes).



When you use standby capacity buffers, add a toleration for the `buffer.gke.io/standby-capacity-node-suspended` taint (with the `operator: "Exists"` field) to the `atelet` DaemonSet so that replacement `atelet` Pods can remain scheduled on suspended standby nodes (for example, during a DaemonSet rolling update). For an example DaemonSet configuration, see [Preload images on standby buffers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-capacity-buffer#preload-images).

If multiple workloads share the same ComputeClass, add matching workload-separation tolerations and `nodeSelector` labels to both your WorkerPool Pod template and the buffer PodTemplate so that GKE provisions dedicated tainted nodes that other workloads don't claim. Also add a matching toleration to the `atelet` DaemonSet so that the `atelet` agent can schedule on those dedicated nodes. For step-by-step instructions, see [Configure capacity buffers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-capacity-buffer).

## Manage upgrades and autoscaler interactions

This section describes how to manage `atelet` DaemonSet updates, cluster autoscaler scale-down events, and node upgrades without disrupting active Actors.

### Update the `atelet` DaemonSet with standby buffers

Suspended standby buffer nodes carry the `buffer.gke.io/standby-capacity-node-suspended` taint and an unreachable taint while suspended, so the `kubelet` agent on a suspended node can't acknowledge Pod deletions. Ensure that the `atelet` DaemonSet tolerates the `buffer.gke.io/standby-capacity-node-suspended` taint (with the `operator: "Exists"` field). Even with that toleration, during a standard rolling update of the `atelet` DaemonSet (with the `maxUnavailable: 1` field), Pods on suspended nodes enter the `Terminating` state and can block the update from progressing on running nodes.

Before you update the `atelet` DaemonSet on a cluster with suspended standby nodes, do one of the following:

  * So unreachable standby nodes don't exhaust the update budget, set the `spec.updateStrategy.rollingUpdate.maxUnavailable` field on the `atelet` DaemonSet to a value greater than the maximum number of suspended standby nodes.
  * Before you update the `atelet` DaemonSet, temporarily scale your standby CapacityBuffer replicas to `0` and wait until the cluster autoscaler removes all [suspended standby buffer nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-capacity-buffer#identify-suspended-standby-buffer-nodes) (typically 10 to 15 minutes). To check whether any nodes still report a `Suspended` condition status of `True`, run the following command:
        
        kubectl get nodes -o custom-columns='NAME:.metadata.name,SUSPENDED:.status.conditions[?(@.type=="Suspended")].status'
        




### Protect active Actors during scale-down and upgrades

Because active Actors execute inside sandboxes managed by the `atelet` agent rather than as individual Kubernetes Pods, a node's CPU and memory requests might appear low to the GKE cluster autoscaler even while a Worker Pod on that node is hosting active Actors. When a node is drained, the `kubelet` agent sends a `SIGTERM` signal to the Worker Pod, and the Worker forwards the `SIGTERM` signal to the main process of each container of every Actor that it hosts. Each active Actor then has up to 30 minutes to be suspended before the Worker stops. Give every stateful Actor a `SIGTERM` handler that doesn't exit on the signal and that calls the `SuspendActor` method with the `DURABILITY_MODE_SYNCHRONOUS` mode. An Actor whose main process exits on the `SIGTERM` signal loses unsaved state immediately. If the Worker Pod stops while still hosting an active Actor, then the Actor enters the `ACTOR_STATE_CRASHED` state.

To minimize disruptions during scale-down events and GKE cluster upgrades, apply the following practices:

  * Avoid using Spot VMs for stateful WorkerPool nodes, because Spot VM preemption provides only 15 seconds to 2 minutes of termination notice before stopping the node.
  * Coordinate draining in your orchestrator so active Actors are checkpointed and suspended before Worker Pods stop, or prevent the cluster autoscaler from evicting active Worker Pods (for example, by using the `cluster-autoscaler.kubernetes.io/safe-to-evict: "false"` Pod annotation). If you set the `safe-to-evict: "false"` annotation statically in the WorkerPool Pod template, then the cluster autoscaler won't scale down a node while a Worker Pod is scheduled on it—even when that Worker hosts zero active Actors. To release idle nodes, you must scale down WorkerPool replicas or manage the annotation dynamically. For more information about the Worker eviction lifecycle and recovering crashed Actors with the `RevertActor` method, see [Eviction in the Agent Substrate API guide](https://github.com/agent-substrate/substrate/blob/main/docs/reference/api-guide.md#eviction).
  * Configure [GKE surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#max-surge) and review [Upgrade in a resource-constrained environment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota#upgrade-resource-constrained) so new worker nodes are provisioned before existing worker nodes are cordoned and drained.



## What's next

  * Learn how to choose the right orchestration model, sandbox runtime, isolation controls, and storage options in [Plan an architecture for AI agent workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-workloads).
  * Learn more about [GKE custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes) and [GKE capacity buffers](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/capacity-buffer).
  * Explore more resources in the [Agent Substrate GitHub repository](https://github.com/agent-substrate/substrate/blob/main/docs/reference/api-guide.md).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 

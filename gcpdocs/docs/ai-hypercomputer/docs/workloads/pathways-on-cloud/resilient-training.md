---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/resilient-training/
title: Resilient training with Pathways \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-05T00:17:55.198666+00:00
---

# Resilient training with Pathways  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/resilient-training/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Resilient training with Pathways Stay organized with collections  Save and categorize content based on your preferences. 

Pathways provides resiliency benefits in the following ways:

  * **Suspend-Resume** : lets your workload tolerate planned interruptions such as preemption notices without requiring custom preemption-handling code.
  * **Elastic training** : lets your workload tolerate unplanned hardware failures without crashing the client by using recovery logic in your training code.



## Before you begin

Before you begin, complete the following tasks:

  * [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment)
  * [Install Kubernetes tools](https://kubernetes.io/docs/tasks/tools/)
  * [Install the Google Cloud CLI CLI](https://docs.cloud.google.com/sdk/docs/install)
  * [Enable the Google Kubernetes Engine API](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api)



## Suspend-resume

Google Kubernetes Engine (GKE) typically sends a preemption notice to an accelerator Pod before the Pod is preempted. Pathways preemption tolerance is enabled by default on all cloud deployments and Pathways accelerator jobs listen for these notices.

When a preemption notice arrives, Pathways first determines whether Pathways can transparently save and restore the workload. If so, then it attempts to transparently suspend your ML workload by writing out its current state to persistent storage such as Cloud Storage before GKE evicts your accelerator jobs. When GKE reschedules your jobs later, Pathways resumes your ML workload by reading back its persisted state.

If the workload isn't restorable, Pathways shuts down the accelerator job and forwards the failure to your job if elastic training is configured. If elastic training isn't configured, GKE restarts the entire workload based on the JobSet restart policy.

Typical ML workloads defined using JAX rely on stateless Pathways XLA components which are restorable using a high bandwidth memory (HBM) snapshot. Certain ML workloads such as those defined using the [JAX colocated python API](https://github.com/jax-ml/jax/blob/main/jax/experimental/colocated_python/api.py) rely on stateful Pathways components; these workloads aren't restorable.

## Elastic training

Elastic training lets your training job continue when hardware failures or slice preemptions occur, without restarting the entire workload. In a multi-slice training job, Pathways keeps the single-controller client process and the healthy TPU slices alive when an individual slice becomes unavailable.

Elastic training combines Pathways system capabilities with recovery logic in your training code:

  * **Failure detection** : When a hardware failure or preemption occurs on a TPU slice, Pathways unassigns the affected slice and raises a `jax.errors.JaxRuntimeError` the next time your workload accesses data on that slice. Because the client process remains active, your code can catch this error, reconfigure your resources, and continue training.
  * **Recovery modes** : The `pathwaysutils.elastic.manager.Manager` class and its `elastic_retry` decorator support two recovery strategies: 
    * **Pause and resume** : When `minimum_slice_count` is `None` or equal to the total number of slices in the job, training pauses when a slice is lost and waits until all slices are healthy again before resuming. Because the slice count doesn't change across attempts, your workload can reuse its existing device mesh and compiled executables.
    * **Replica resize** : When `minimum_slice_count` is less than the total number of slices, training continues immediately on the remaining active slices by rebuilding the device mesh and recompiling for the smaller topology. A background monitor thread periodically checks inactive slices and records newly healthy slices in `elastic_manager.available_inactive_slices`. Your training loop can then rebuild the device mesh with the replacement slices, reinitialize for the expanded topology, and place the current state onto the new mesh.
  * **State recovery** : To resume training after an elastic event, your workload restores model parameters, optimizer state, and data iterator state using in-memory snapshots. The `Snapshotter` class in `orbax.checkpoint` asynchronously copies replicated state from TPU HBM to `pinned_host` CPU memory on each slice. During recovery, `Snapshotter` reconstructs the state from surviving host replicas and reshards it directly onto the active TPU mesh without reading from remote storage.



### Enable elasticity on the Pathways proxy server

To enable elastic device sets on Pathways in GKE, add the `--num_elastic_instances` flag to the `args` field of the `pathways-proxy` container in your JobSet manifest and specify the number of elastic TPU slices in your workload:
    
    
    - name: pathways-proxy
      image: us-docker.pkg.dev/cloud-tpu-v2-images/pathways/proxy_server:latest
      args:
      - --resource_manager_address=$(PATHWAYS_HEAD):29001
      - --server_port=29000
      - --gcs_scratch_location=gs://BUCKET_NAME
      - --num_elastic_instances=NUM_SLICES
    

Replace the following:

  * `BUCKET_NAME`: the Cloud Storage bucket used for Pathways temporary files.
  * `NUM_SLICES`: the number of TPU slices in your workload.



### Filter active devices and build the device mesh

In a Pathways workload, `jax.devices()` returns all devices in the initial allocation for the lifetime of the client process. When you use elastic training, use `elastic_manager.active_devices` so that your device mesh and batch size only use healthy, active slices:
    
    
    import jax
    import numpy as np
    from pathwaysutils.elastic import manager
    
    elastic_manager = manager.Manager()
    
    
    def create_mesh(
        elastic_manager: manager.Manager, devices_per_slice: int
    ) -> jax.sharding.Mesh:
      device_array = np.asarray(elastic_manager.active_devices).reshape(
          (elastic_manager.active_slice_count, devices_per_slice)
      )
      return jax.sharding.Mesh(device_array, axis_names=("replica", "model"))
    

When the number of active slices changes in replica resize mode, use an elastic data loader such as `grain.experimental.ElasticIterator`. Standard per-host data iterators save state per host and can't restore onto a different number of hosts, whereas `ElasticIterator` tracks a single global dataset position that can be restored across any number of active slices.

### Elastic training loop

An elastic training loop coordinates slice monitoring, failure recovery, and in-memory snapshotting, as shown in the following code example:

  * Your `train` function creates a single `manager.Manager()` instance and an Orbax `Snapshotter` outside the retry wrapper so slice tracking and host-memory snapshots persist across attempts.
  * Decorating the inner `run_training_loop` function with `@elastic_manager.elastic_retry` waits for healthy slices, sets `jax.default_device` to an active slice, keeps the background monitor thread active across steps, and retries the loop when a `jax.errors.JaxRuntimeError` occurs.
  * When recovering from a slice failure at the start of an attempt, your code must rebuild the device mesh from `elastic_manager.active_devices` and call `snapshotter.load` to restore the latest snapshot onto the updated mesh shardings, while letting device buffers from the failed attempt go out of scope.
  * During each step of the loop, your code periodically calls `snapshotter.save` to back up the training state, and checks `elastic_manager.available_inactive_slices` to detect healthy replacement slices. When replacement slices are available, your code adds them to `elastic_manager.active_slice_indices`, rebuilds the mesh, reinitializes the training loop, and places the state onto the expanded mesh.



The following example shows how to implement an elastic training loop by combining `manager.Manager`, `elastic_retry`, and Orbax's in-memory `Snapshotter`:
    
    
    import jax
    import orbax.checkpoint as ocp
    import pathwaysutils
    from pathwaysutils.elastic import manager
    
    pathwaysutils.initialize()
    
    
    def train(
        final_step: int,
        snapshot_interval: int,  # in steps
        devices_per_slice: int,
    ):
      elastic_manager = manager.Manager()
      snapshotter = ocp.v1.training.pathways.Snapshotter(replica_axis_index=0)
    
      @elastic_manager.elastic_retry(
          minimum_slice_count=1,
          poll_interval=10,  # in seconds
          timeout=300,  # in seconds
          retry_policy=manager.ElasticRetryLimit(max_attempts=10),
      )
      def run_training_loop():
        mesh = create_mesh(elastic_manager, devices_per_slice)
        state, abstract_state, jitted_train_step, data_iterator = (
            initialize_training_loop(mesh)
        )
        step = 0
    
        # Restore from the latest in-memory snapshot after a slice failure.
        if snapshotter.latest is not None:
          snapshotter.join()
          restored = snapshotter.load({
              "state": abstract_state,
              "step": step,
              "iterator_state": data_iterator.get_state(),
          })
          state = restored["state"]
          step = int(restored["step"]) + 1
          data_iterator.set_state(restored["iterator_state"])
    
        while step < final_step:
          batch = next(data_iterator)
          state = jitted_train_step(state, batch)
    
          if step % snapshot_interval == 0:
            snapshotter.save(
                step,
                {
                    "state": state,
                    "step": step,
                    "iterator_state": data_iterator.get_state(),
                },
            )
    
          # If replacement slices are healthy, reinitialize and place state onto the new mesh.
          if elastic_manager.available_inactive_slices:
            elastic_manager.active_slice_indices |= (
                elastic_manager.available_inactive_slices
            )
            mesh = create_mesh(elastic_manager, devices_per_slice)
            iterator_state = data_iterator.get_state()
            _, abstract_state, jitted_train_step, data_iterator = (
                initialize_training_loop(mesh)
            )
            data_iterator.set_state(iterator_state)
            state_shardings = jax.tree.map(lambda x: x.sharding, abstract_state)
            state = jax.device_put(state, state_shardings)
    
          step += 1
    
        return state
    
      state = run_training_loop()
      snapshotter.join()
      return state
    

### Configure the elastic manager and retry behavior

You instantiate `manager.Manager(devices=None)` once per process. If you omit `devices`, the manager uses `jax.devices()` and groups devices by their `slice_index` attribute.

The `Manager` instance exposes the following properties to inspect cluster topology during training:

  * `slice_to_devices`: A mapping from each `slice_index` to the sequence of `jax.Device` objects belonging to that slice.
  * `all_slice_indices`: A `frozenset` of all slice indices in the allocation.
  * `active_slice_indices`: A `frozenset` of slice indices participating in the active computation mesh.
  * `active_devices`: A list of `jax.Device` objects belonging to the active slices, ordered by `slice_index`.
  * `inactive_slice_indices`: A `frozenset` of slice indices in the allocation that aren't participating in the computation mesh.
  * `available_inactive_slices`: A `frozenset` of inactive slice indices that the background monitor thread has detected as healthy and ready to rejoin.
  * `total_slice_count` and `active_slice_count`: The total number of allocated slices and the number of active slices.
  * `default_device`: Device `0` from an active slice, which `elastic_retry` automatically sets as the default JAX device for each attempt.



You can customize retry and scaling behavior by passing the following arguments to `@elastic_manager.elastic_retry`:

  * `minimum_slice_count`: The minimum number of healthy slices required before starting the initial execution or a retry attempt. If set to `None` (the default), `elastic_retry` waits for all slices in the allocation (`total_slice_count`), operating in pause and resume mode. If set to a smaller integer (such as `1`), `elastic_retry` operates in replica resize mode.
  * `poll_interval`: The interval in seconds between slice health checks performed by the elastic training manager (`Manager`) during training. Defaults to `10`.
  * `timeout`: The maximum number of seconds to wait for `minimum_slice_count` slices to become active before raising a `TimeoutError`. Defaults to `None` (no timeout).
  * `pre_callback`: An optional callback that is run at the beginning of each attempt after `active_slice_indices` is updated and before the wrapped training loop function runs.
  * `on_elastic_event_callback`: An optional callback that is run after a slice-down `jax.errors.JaxRuntimeError` is caught, before the next retry attempt begins. You can use this callback to clean up incomplete checkpoints or reset data iterators.
  * `retry_policy`: A callable `(attempt: int, error: Exception) -> bool` that determines whether to continue retrying after an elastic event. Use `manager.ElasticRetryLimit(max_attempts)` to cap the total number of attempts. If omitted, `elastic_retry` retries indefinitely.



On an elastic event, JAX frees device buffers from the failed attempt once the stack frame unwinds and no variables reference those arrays. Avoid keeping references to device arrays from a failed attempt inside global variables or long-lived callbacks so that memory is released before the next attempt starts.

### In-memory snapshots with Orbax

The `ocp.v1.training.pathways.Snapshotter` class (available in `orbax-checkpoint` version 0.12.6 and later) maintains an in-memory backup of your training state in `pinned_host` memory across slices:

  * `Snapshotter(replica_axis_index=0)`: Initializes the snapshotter and specifies which mesh axis represents data-parallel slice replicas. All JAX arrays in the saved state must be replicated along this mesh axis so that surviving slices retain a complete copy of the model and optimizer state when a slice fails. If your state contains single-device arrays, replicate them across the mesh before calling `save`.
  * `save(step, state)`: Asynchronously transfers `state` to `pinned_host` memory and splits it into per-replica trees along `replica_axis_index`. If a previous snapshot transfer is still in progress, `save` skips the new request to avoid stalling the training loop.
  * `load(abstract_state, reset_snapshot_state=True)`: Probes the saved host replicas to identify surviving slices, concatenates the healthy replicas, and reshards the state onto the target shardings specified by `abstract_state`.
  * `join()`: Blocks until any queued snapshot operation completes.
  * `latest`: Returns metadata (including `step`) for the most recently completed snapshot, or `None` if no snapshot has completed.



### Reduce sharding on slice failure

When a TPU slice fails or is preempted during execution, Pathways raises a `jax.errors.JaxRuntimeError` (such as `DATA_LOSS`, `DEADLINE_EXCEEDED`, `NOT_FOUND`, or `INTERNAL`). The `elastic_retry` decorator catches this exception and checks `elastic.is_error_due_to_slice_down(error)`:

  * If the error isn't caused by a slice-down event, `elastic_retry` re-raises the exception immediately.
  * If the error is caused by a slice-down event, `elastic_retry` stops any active JAX profiler trace, runs `on_elastic_event_callback`, and evaluates `retry_policy(attempt, error)`.
  * Before starting the next attempt, `elastic_retry` calls `elastic.wait_for_slices` once, which polls slice health until at least `minimum_slice_count` slices are active, updates `elastic_manager.active_slice_indices`, and runs your training loop function on the surviving slices.



### Increase sharding when slices rejoin

When your workload runs on a reduced number of slices in replica resize mode, the background monitor thread periodically runs health checks on `elastic_manager.inactive_slice_indices`. When repaired or rescheduled slices pass the health check, the monitor thread adds their slice indices to `elastic_manager.available_inactive_slices`.

When `elastic_manager.available_inactive_slices` is non-empty at the end of a training step, the workload scales back up in place without losing training progress:

  * Adding the slice indices in `elastic_manager.available_inactive_slices` to `elastic_manager.active_slice_indices` incorporates the rejoined slices into `elastic_manager.active_devices` and clears them from `available_inactive_slices`.
  * Rebuilding the device mesh from `elastic_manager.active_devices` and reinitializing the training step and data iterator adapts the computation to the expanded topology.
  * Calling `jax.device_put` places the current training state onto the new mesh shardings without restoring from a snapshot.



## Hot-swap

Hot-swap refers to a feature of the GKE JobSet API where a higher-priority job can quickly take over resources from a lower-priority job, minimizing downtime and ensuring faster recovery.

When a JobSet is created, GKE schedules the workload across multiple slices, as specified in the JobSet configuration. If a hardware failure occurs on one or more slices, the affected Pods are marked as failed. If your GKE cluster has a spare slice running a lower-priority job, the JobSet system remaps the failed slice's workload from the higher-priority job onto that spare slice. This remapping typically takes less than a minute.

When a JobSet restarts, hot-swap can occur in the following situations:

  * **Default mode** : If spare, idle TPU slices are available within the same cluster, the Kubernetes scheduler prioritizes scheduling the restarted jobs onto these slices rather than waiting for the failed slices to be repaired. This scheduling behavior provides faster recovery.
  * **Heterogeneous workloads** : In clusters running multiple workloads with a configured Kubernetes `PriorityClass` resource, a restarted JobSet can trigger a hot-swap. If the restarted job's affinity matches a lower-priority job's resources, Kubernetes preempts the lower-priority job so that the higher-priority job can start without waiting for slice repair. For example, you can configure your Pathways worker Pods with different priorities by using a `PriorityClass` resource.



To use priorities in your cluster, define a `PriorityClass` manifest:
    
    
    kind: PriorityClass
    metadata:
      name: high-prior-job
    value: 2000
    globalDefault: false
    description: "This priority class should be used for high priority job."
    

Apply this YAML to your GKE cluster:
    
    
    kubectl apply -f high-prior-job.yaml
    

Next, attach the new priority class to your Pathways worker job by adding the following text to the podspec of your `pathways-worker` Pod.
    
    
    priorityClassName: high-prior-job
    

## What's next

  * [Create a GKE cluster with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-gke-cluster)
  * [Run a batch workload with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/batch-workload)
  * [Pathways interactive mode](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-interactive-mode)
  * [Porting JAX workloads to Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/porting-jax-workloads)
  * [Troubleshoot Pathways on cloud](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/troubleshooting-pathways)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 

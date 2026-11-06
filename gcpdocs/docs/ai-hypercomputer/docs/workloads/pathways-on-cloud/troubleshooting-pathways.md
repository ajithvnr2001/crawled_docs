---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/troubleshooting-pathways/
title: Troubleshoot Pathways on Cloud \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T05:53:22.707611+00:00
---

# Troubleshoot Pathways on Cloud  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/troubleshooting-pathways/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Troubleshoot Pathways on Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This page helps machine learning (ML) engineers and platform administrators diagnose and resolve issues with Pathways workloads on Google Cloud. Use this guide to inspect component logs, verify cluster and slice readiness, monitor Megascale XLA (MXLA) transfer metrics, and fix common runtime errors. In each section, select the **GKE** or **Cluster Director** tab for your environment. 

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

###  GKE 

Complete the following prerequisites before you proceed:

  * [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * [Install Kubernetes tools](https://kubernetes.io/docs/tasks/tools/).
  * [Install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  * [Enable the Kubernetes Engine API](https://console.cloud.google.com/flows/enableapi?apiid=container.googleapis.com).
  * [Create a Google Kubernetes Engine (GKE) cluster with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-gke-cluster).
  * To view logs and metrics in the Google Cloud console, make sure that you have the [Logs Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) and [Monitoring Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`) Identity and Access Management (IAM) roles on your project.



###  Cluster Director 

Complete the following prerequisites before you proceed:

  * [Create a Cluster Director cluster and set up the Pathways environment](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-cluster-director-cluster).
  * Verify that you have SSH access to the cluster's login node.



## View logs

###  GKE 

You can view logs for your Pathways workloads directly by using the `gcluster job logs` command (pass `--main-only=false` to include worker pod logs):
    
    
    gcluster job logs WORKLOAD_NAME \
        --cluster=CLUSTER \
        --project=PROJECT_ID \
        --location=LOCATION \
        --main-only=false

Replace the following:

  * `WORKLOAD_NAME`: the name of your workload when you use Cluster Toolkit, or the JobSet name when you use `kubectl`.
  * `CLUSTER`: the name of your GKE cluster.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the region or zone where you created your GKE cluster.



To list all pods for your workload by using `kubectl`, filter by the JobSet name label:
    
    
    kubectl get pods \
        -l jobset.sigs.k8s.io/jobset-name=WORKLOAD_NAME

To check workload status or list failed jobs, use the `gcluster job list` command:
    
    
    gcluster job list --status Failed \
        --cluster=CLUSTER \
        --project=PROJECT_ID \
        --location=LOCATION

**Note:** Status values for the `gcluster job list` command are case-sensitive (`Pending`, `Running`, `Succeeded`, `Failed`, `Suspended`).

Alternatively, in the Cloud Logging [Logs Explorer](https://console.cloud.google.com/logs/query), run the following query adjusted for your project, location, cluster, and workload:
    
    
    resource.type="k8s_container"
    resource.labels.project_id="PROJECT_ID"
    resource.labels.location="LOCATION"
    resource.labels.cluster_name="CLUSTER"
    resource.labels.namespace_name="default"
    resource.labels.pod_name:"WORKLOAD_NAME"

This query matches multiple Pathways Kubernetes containers with names such as `pathways-rm`, `pathways-proxy`, `pathways-worker`, and `workload-container`. To determine which container is causing a problem, add a container name filter such as `resource.labels.container_name:"CONTAINER_NAME"`, where `CONTAINER_NAME` is the name of the container.

###  Cluster Director 

The Pathways scripts write logs to the shared file system:

  * The Pathways service job writes `pathways-service-SERVICE_JOB_ID.out` and `pathways-service-SERVICE_JOB_ID.err` in the directory where you ran `sbatch`, for example, `~/pathways`.
  * The Pathways resource manager, IFRT proxy server, and TPU workers write to `~/pathways/service_SERVICE_JOB_ID/logs`, including `rm.log`, `proxy.log`, and one `slice-*.out` and `slice-*.err` file per worker task.
  * The example MaxText workload writes its log to `maxtext-llama31-JOB_ID.err`.



On the login node, check the state of the Pathways jobs and find their job IDs:
    
    
    squeue -u ${USER}
    

## Monitor Pathways components and metrics

The following sections apply to Pathways on GKE.

### Health monitoring

You can monitor the health of various Pathways components by looking for entries in the container logs.

The `pathways-proxy` container is ready to serve new connection requests when it writes the following log entry. To view the logs, run the following command:
    
    
    kubectl logs HEAD_POD_NAME --container pathways-proxy

Replace `HEAD_POD_NAME` with the name of the Pathways head pod.

The output includes a line similar to the following:
    
    
    I1101 04:51:41.967764       1 proxy_server.cc:125] IFRT proxy server started with status OK
    

The `pathways-rm` container is ready to serve new connection requests when it writes the following log entry:
    
    
    kubectl logs HEAD_POD_NAME --container pathways-rm

The output includes a line similar to the following:
    
    
    I1101 04:50:41.967764       1 server_lib.cc:1473] Pathways Server serving on POD_IP:29001
    

`POD_IP` is the IP address of the pod, which can change when the pod restarts or is rescheduled.

To verify that all TPU slices are ready, check the `pathways-rm` container logs for `Pathways Slices Now Ready`:
    
    
    kubectl logs HEAD_POD_NAME --container pathways-rm

For example, the following log entry shows that 2 of 2 slices are ready:
    
    
    I1101 04:52:41.967764       1 multi_job_allocator.cc:1063] *** 2/2 Pathways Slices Now Ready ***
    

The Pathways client can connect to the IFRT proxy server as soon as the proxy server is ready, even if not all slices are ready. Your job works with virtual slices until the TPU slices become ready. Virtual slices let your code run when TPUs are unavailable.

To verify that a `pathways-worker` container is ready, check its logs:
    
    
    kubectl logs WORKER_POD_NAME --container pathways-worker

Replace `WORKER_POD_NAME` with the name of a Pathways worker pod.

When the worker is ready, the output includes a line similar to the following:
    
    
    I1101 04:50:41.967764       1 server_lib.cc:1473] Pathways Server serving on POD_IP:29005
    

`POD_IP` is the IP address of the pod, which can change when the pod restarts or is rescheduled.

### Metrics collection

Pathways can write low-level system metrics to Cloud Monitoring for debugging. The metrics include the following:

  * Data center network (DCN) transfer latency
  * Collective latency
  * Host-to-device transfer latency
  * Device-to-host transfer latency

**Note:** These metrics are available only for multislice workloads, which are workloads that run on two or more TPU slices.

You can find the metrics on the Monitoring dashboard of the Google Cloud project where the GKE cluster is running.

To monitor these metrics in Metrics Explorer, follow these steps:

  1. In the Google Cloud console, go to the [Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer) page.
  2. In the **Select a metric** field, filter by the name of the metric.
  3. To filter by your workload name and time range, click **Add filter** , and then filter by `pod_name`.
  4. For **Aggregation** , choose an aggregation type based on the metric and the workloads that you're monitoring.



#### DCN transfer latency

This Megascale XLA (MXLA) metric measures the cumulative distribution of network-transfer latencies for multislice traffic. Latency measurement starts when the system issues a request to transfer data over the DCN and ends when it receives an acknowledgment that the data transfer is complete. To monitor this metric, filter by the `dcn_transfer_latencies` metric name.

#### Collective latency

This MXLA metric measures the cumulative distribution of end-to-end collective latency for multislice traffic. Latency measurement starts when the system issues a request for a collective operation and ends when it receives an acknowledgment that the data transfer is complete. To monitor this metric, filter by the `collective_end_to_end_latencies` metric name.

#### Host-to-device transfer latency

This MXLA metric measures the cumulative distribution of host-to-device transfer latencies for multislice traffic. Latency measurement starts when the system issues a request to transfer data from the host to a TPU device and ends when it receives an acknowledgment that the data transfer is complete. To monitor this metric, filter by the `host_to_device_transfer_latencies` metric name.

#### Device-to-host transfer latency

This MXLA metric measures the cumulative distribution of device-to-host transfer latencies for multislice traffic. Latency measurement starts when the system issues a request to transfer data from a TPU device to the host and ends when it receives an acknowledgment that the data transfer is complete. To monitor this metric, filter by the `device_to_host_transfer_latencies` metric name.

## Debug common errors

###  GKE 

**Unable to hash accelerator config warnings**

The following messages are only warnings and don't affect the performance of your JAX code:
    
    
    INFO:jax._src.cache_key:get (_hash_accelerator_config): unable to hash accelerator config, falling back to hashing devices + platform: UNIMPLEMENTED: GetTopologyForDevices is not supported for the IFRT proxy client. (type <class 'jaxlib.xla_extension.XlaRuntimeError'>)
    

**Permission`logging.logEntries.create` denied on resource**

If you see the following error, make sure that the Compute Engine service account used by Vertex AI Workbench has permission to write log entries to Logging:
    
    
    INFO:absl:Created 'ArrayHandler' with primary_host=0, replica-id=0
    WARNING:absl:pathwaysutils: Detected Pathways-on-Cloud backend. Applying changes.
    Failed to submit 1 logs.
    Traceback (most recent call last):
      File "/opt/conda/lib/python3.10/site-packages/google/api_core/grpc_helpers.py", line 65, in error_remapped_callable
        return callable_(**args, **kwargs)
      File "/opt/conda/lib/python3.10/site-packages/grpc/_channel.py", line 1181, in __call__
        return _end_unary_response_blocking(state, call, False, None)
      File "/opt/conda/lib/python3.10/site-packages/google/api_core/grpc_helpers.py", line 1006, in _end_unary_response_blocking
        raise _InactiveRpcError(state) # pytype: disable-not-instantiable
    grpc._channel._InactiveRpcError: <_InactiveRpcError of RPC that terminated with:
      status = StatusCode.PERMISSION_DENIED
      details = "Permission 'logging.logEntries.create' denied on resource (or it may not exist)."
      debug_error_string = "UNKNOWN:Error received from peer ipv4:216.239.34.174:443 {created_time:"2024-10-03T20:30:44.820425276+00.00", grpc_status:7, grpc_message:"Permission \'logging.logEntries.create\' denied on resource (or it may not exist)."}"
    >
    

To fix this issue, grant the [Logs Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`) role to the Compute Engine service account.

**Not able to connect to the IFRT proxy server**

When your first JAX command that sends an IFRT command to the Pathways cluster tries to run, it might stop responding for about a minute and then display a `RuntimeError` similar to the following:
    
    
    RuntimeError: Unable to initialize backend 'proxy': UNAVAILABLE: Unable to establish connection to ifrt_proxy server, please check provided address example-workload-proxy-0-0.example-workload.default.svc.example-cluster-domain.:38676'; detailed error: DNS resolution failed (set JAX_PLATFORMS='' to automatically choose an available backend)
    

If you see this error, your IFRT proxy client can't connect to the IFRT proxy server. Check the following:

  * Verify that you configured your Virtual Private Cloud (VPC) network correctly.
  * Verify that your firewall rules allow the connection.
  * Verify that your Pathways cluster is provisioned.
  * Check for startup error messages in the container logs.



**ALTS handshake failed or socket closed when connecting to the IFRT proxy server**

You might see `Alts handshake failed (TSI_INTERNAL_ERROR)` or `UNAVAILABLE: Unable to establish connection to ifrt_proxy server ... Socket closed` when you run a custom manifest without the `hostNetwork: true` field on a Workload Identity Federation for GKE node pool. To resolve this issue, set the `IFRT_PROXY_USE_INSECURE_GRPC_CREDENTIALS: "true"` environment variable on both the `pathways-proxy` container and the JAX client container (both sides must match). Adding this environment variable disables ALTS and uses insecure gRPC instead, so use it only within a trusted cluster network.

**There is an existing connection to the Pathways cluster**

A Pathways cluster can maintain a session with only one client at a time. If two separate notebooks attempt to connect to the same Pathways cluster, one connects and the other displays the following errors:
    
    
    INFO:absl:Created ArrayHandler with primary_host=0, replica_id=0
    WARNING:absl:pathwaysutils: Detected Pathways-on-Cloud backend. Applying changes.
    E0927 21:19:52.919607   37624 rpc_helper.cc:56] Connection to IFRT proxy server was terminated: CANCELLED: Cancelled
    E0927 21:20:03.467547   37719 rpc_helper.cc:56] Connection to IFRT proxy server was terminated: CANCELLED: Cancelled
    E0927 21:20:14.011645   37807 rpc_helper.cc:56] Connection to IFRT proxy server was terminated: CANCELLED: Cancelled
    E0927 21:20:24.557955   37924 rpc_helper.cc:56] Connection to IFRT proxy server was terminated: CANCELLED: Cancelled
    ---------------------------------------------------------------------------
    XlaRuntimeError                           Traceback (most recent call last)
    File /opt/conda/lib/python3.10/site-packages/jax/_src/xla_bridge.py:887, in backends()
        885   continue
    --> 887 backend = _init_backend(platform)
        888 _backends[platform] = backend
    
    File /opt/conda/lib/python3.10/site-packages/jax/_src/xla_bridge.py:973, in _init_backend(platform)
        972 logger.debug("Initializing backend '%s'", platform)
    --> 973 backend = registration.factory()
        974 # TODO: consider raising more descriptive errors directly from backend
        975 # factories instead of returning None.
    
    File /opt/conda/lib/python3.10/site-packages/pathwaysutils/proxy_backend.py:24, in register_backend_factory.<locals>.<lambda>()
         21 def register_backend_factory():
         22   xla_bridge.register_backend_factory(
         23       "proxy",
    ---> 24       lambda: ifrt_proxy.get_client(
         25           jax.config.read("jax_backend_target"),
         26           ifrt_proxy.ClientConnectionOptions(),
         27       ),
         28       priority=-1,
         29   )
    
    XlaRuntimeError: UNAVAILABLE: Unable to establish connection to ifrt_proxy server, please check provided address example-workload-proxy-0-0.example-workload.default.svc.example-cluster-domain.:38676'; detailed error: Connection to IFRT proxy server was terminated: CANCELLED: Cancelled
    
    During handling of the above exception, another exception occurred:
    
    RuntimeError                              Traceback (most recent call last)
    Cell In[2], line 4
          1 import pathwaysutils
          3 import jax
    ----> 4 print(jax.devices())
    
    File /opt/conda/lib/python3.10/site-packages/jax/_src/xla_bridge.py:1085, in devices(backend)
       1060 def devices(
       1061     backend: str | xla_client.Client | None = None
       1062 ) -> list[xla_client.Device]:
       1063   """Returns a list of all devices for a given backend.
       1064
       1065   .. currentmodule:: jaxlib.xla_extension
       (...)
       1083     List of Device subclasses.
       1084   """
    -> 1085   return get_backend(backend).devices()
    
    File /opt/conda/lib/python3.10/site-packages/jax/_src/xla_bridge.py:1019, in get_backend(platform)
       1015 @lru_cache(maxsize=None)  # don't use util.memoize because there is no X64 dependence.
       1016 def get_backend(
       1017     platform: None | str | xla_client.Client = None
       1018 ) -> xla_client.Client:
    -> 1019   return _get_backend_uncached(platform)
    
    File /opt/conda/lib/python3.10/site-packages/jax/_src/xla_bridge.py:998, in _get_backend_uncached(platform)
        994   return platform
        996 platform = (platform or _XLA_BACKEND.value or _PLATFORM_NAME.value or None)
    --> 998 bs = backends()
        999 if platform is not None:
       1000   platform = canonicalize_platform(platform)
    
    File /opt/conda/lib/python3.10/site-packages/jax/_src/xla_bridge.py:903, in backends()
        901       else:
        902         err_msg += " (you may need to uninstall the failing plugin package, or set JAX_PLATFORMS=cpu to skip this backend.)"
    --> 903       raise RuntimeError(err_msg)
        905 assert _default_backend is not None
        906 if not config.jax_platforms.value:
    
    RuntimeError: Unable to initialize backend 'proxy': UNAVAILABLE: Unable to establish connection to ifrt_proxy server, please check provided address 'example-workload-proxy-0-0.example-workload.default.svc.example-cluster-domain.:38676'; detailed error: Connection to IFRT proxy server was terminated: CANCELLED: Cancelled (set JAX_PLATFORMS='' to automatically choose an available backend)
    

After the original client disconnects, the second client can connect. After an unexpected disconnection, you might need to restart the Pathways cluster so that other clients can connect.

**`LocalProxy.__init__()` got an unexpected keyword argument `'unbound_message'`**

If you see the following error after importing `pathwaysutils`, check whether outdated versions of Flask or Werkzeug are installed in your environment (replace `pip3` with `pip` if needed):
    
    
    pip3 list --outdated
    

If Flask or Werkzeug is listed, upgrade the packages (note that upgrading might affect other packages or dependencies in your project):
    
    
    pip3 install --upgrade flask Werkzeug
    

**Internal error from proxy server**
    
    
    "Internal error from proxy server during Array::IsDeleted(): UNAVAILABLE:Connection to IFRT proxy server was terminated: FAILED_PRECONDITION:
    GrpcClientSession: writes no longer allowed."
    

This error indicates that the IFRT proxy server disconnected from the client. To fix this issue, restart your client. For notebooks, restart the notebook kernel and rerun your notebook.

**`SIGTERM` and HBM OOM**

A `SIGTERM` entry in the logs associated with a `RESOURCE_EXHAUSTED` error might indicate a high-bandwidth memory (HBM) out-of-memory (OOM) error. In this case, reduce the amount of HBM that your JAX code uses.

**`INVALID_ARGUMENT`**
    
    
    "INVALID_ARGUMENT : Permanent error, with a last message of Lifecycle
    matches_prefix cannot specify more than 50 prefixes per config.; Error while
    initializing persistent cache storage Cloud Storage"
    

This error occurs if the Cloud Storage bucket passed to the `--pathways-gcs-location` flag has reached the maximum lifecycle policy limit (50 prefixes). To resolve this issue, delete Cloud Storage lifecycle policies that you no longer use.

**Permanent error**
    
    
    Permanent error, with a last message of The specified bucket does not exist.; Error while initializing persistent cache storage gcs
    

The Pathways resource manager or Pathways workers print this error when you provide an invalid Cloud Storage location to Pathways containers.

**Error response from daemon**
    
    
    Error response from daemon: dockerfile parse error line 16: Unknown flag: exclude
    

This error occurs when you use an older version of Docker. Upgrade your Docker version.

**IFRT proxy client and server failed to agree**
    
    
    IFRT Proxy client and server failed to agree on the protocol version; supported versions: client = [1, 1], server = [3, 14]
    

This error indicates that you're using an older version of MaxText. Rebuild the latest MaxText image.

###  Cluster Director 

**`setup_env.sh` fails with an Enroot `mktemp` error**

If `setup_env.sh` fails with the following error, Enroot's temporary directory doesn't exist:
    
    
    mktemp: failed to create directory via template '/tmp/UID/tmp/enroot...'
    

To fix this issue, run `mkdir -p /tmp/$(id -u)/tmp`, and then run the script again.

**`setup_env.sh` can't pull the Pathways images**

If `setup_env.sh` fails with `Couldn't pull ...`, no Pathways image is tagged for the requested `JAX_VERSION`. Use a supported JAX version.

**The cluster has no`cpu` partition**

If `sinfo` doesn't show a `cpu` partition, the cluster definition is missing the CPU nodeset or names its partition differently. The Pathways scripts submit jobs to a partition named `cpu`. To fix this issue, update your cluster blueprint to define a CPU partition named `cpu` and redeploy the cluster, or update the partition name in your Pathways job scripts to match the CPU partition shown by `sinfo`.

**TPU nodes don't come up**

Check that the reservation is in the cluster's zone and has enough `ct6e-standard-4t` VMs, and that `staticNodeCount` and `acceleratorTopology` match.

**The Pathways service exits with`Invalid partition name specified`**

The `PARTITION` variable is wrong. Choose a TPU partition from the output of `sinfo`.

**The Pathways service doesn't become ready**

If the service log stays at `Waiting for at least MIN_SLICES=...`, not enough slices are running. The `NODELIST(REASON)` column of the following command shows the reason, for example, no available capacity or a `SLICE_SHAPE` value that doesn't match the TPU nodeset:
    
    
    squeue -u ${USER} -n pw-slice
    

**The Pathways resource manager or IFRT proxy server doesn't start**

If the service fails with `Timed out waiting for Pathways Resource Manager` or `Timed out waiting for Pathways IFRT Proxy Server`, a Pathways container didn't start. Check `rm.log` and `proxy.log` in the log directory.

**The Pathways service stops unexpectedly**

If the service stops with `The Pathways Resource Manager or IFRT proxy exited`, one of them crashed, and the service stopped its workers. Check `rm.log` and `proxy.log` in the log directory, and then start the service again.

**A TPU node is stuck in a bad state**

To recover the node, run the following command on the login node:
    
    
    sudo scontrol update nodename=NODE \
        state=power_down_force

Replace `NODE` with the name of the node, as shown by `sinfo`.

**MaxText can't find a running Pathways service**

If MaxText fails with `No running Pathways service after 60 minutes`, the service isn't running or isn't ready yet. Check the service log. To wait longer, set `SERVICE_WAIT_MINUTES` when you submit `run_maxtext.sh`.

**MaxText fails with`RESOURCE_EXHAUSTED`**

The model doesn't fit in TPU memory. Use `2x4` or `4x4` slices, or set `REDUCED_LAYERS=1`.

**The MaxText job stays pending**

The CPU node doesn't have the 8 CPUs and 96 GB of memory that `run_maxtext.sh` requests, in addition to what the Pathways service uses. To fix this issue, increase the CPU and memory capacity (or the number of nodes) in your `cpu` partition, or reduce the resource request in `run_maxtext.sh`.

**Not able to connect to the IFRT proxy server**

If the client stops responding or fails with `UNAVAILABLE`, it can't reach the proxy server:

  * Check that the service log shows `READY`.
  * Check that `JAX_BACKEND_TARGET` matches the address in `~/pathways/cluster.env`.
  * If you use port forwarding, check that the SSH tunnel is still running.
  * If the client runs on a VM, check that the VM is in the cluster's subnet. The following command should succeed:
        
        nc -zv PROXY_IP 29000

Replace `PROXY_IP` with the IFRT proxy IP address from the service log.




**`jax.devices()` lists CPU devices instead of TPU devices**

You set the `JAX_PLATFORMS` and `JAX_BACKEND_TARGET` environment variables after you imported `jax`. Restart the notebook kernel, and set the variables before you import `jax`.

**Errors right after connecting to the IFRT proxy server**

The client's `jax` or `pathwaysutils` version doesn't match the Pathways server. Install the versions in `~/pathways/venv`.

**A computation fails with`DATA_LOSS` and `PlacementDataLoss`**

The computation used a device on a slice that isn't running. Check that `MIN_SLICES` equals `MAX_SLICES`, and that every worker task is running:
    
    
    squeue -u ${USER} -n pw-slice
    

**A computation fails after a Spot preemption**

Computations that use the preempted slice's devices fail. To recover from Spot preemptions automatically, configure checkpointing and elastic slice rescaling as described in [Resilient training with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/resilient-training).

## What's next

  * [Create a GKE cluster with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-gke-cluster)
  * [Create a Cluster Director cluster with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-cluster-director-cluster)
  * [Run a batch workload with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/batch-workload)
  * [Run an interactive workload with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-interactive-mode)
  * [Port JAX workloads to Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/porting-jax-workloads)
  * [Resilient training with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/resilient-training)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-06 UTC."],[],[]] 

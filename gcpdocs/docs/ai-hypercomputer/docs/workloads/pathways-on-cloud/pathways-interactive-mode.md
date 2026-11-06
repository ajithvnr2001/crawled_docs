---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-interactive-mode/
title: Run an interactive workload with Pathways \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T08:36:19.156327+00:00
---

# Run an interactive workload with Pathways  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-interactive-mode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Run an interactive workload with Pathways Stay organized with collections  Save and categorize content based on your preferences. 

Pathways interactive workloads are remote JAX workloads that run outside of the Google Kubernetes Engine (GKE) cluster's Pathways controller components, for example, on a VM. Unlike batch workloads, when an interactive workload finishes, it doesn't shut down the Pathways cluster components, which remain available for connections from other JAX clients. This document uses a Jupyter notebook as an example to demonstrate interactive workloads.

Using the [IFRT](https://github.com/openxla/xla/blob/main/xla/python/ifrt/README.md) interface, JAX users send commands to a Pathways cluster. JAX code, whether executed from a terminal, notebook, or any Python-compatible environment, can interact with Pathways resources.

## Before you begin

Complete the following prerequisites:

  * [Create a GKE cluster with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-gke-cluster).
  * [Install Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * [Install Kubernetes tools](https://kubernetes.io/docs/tasks/tools/).
  * [Install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  * [Enable the Kubernetes Engine API](https://console.cloud.google.com/flows/enableapi?apiid=container.googleapis.com).
  * Make sure that Pathways is enabled for your Google Cloud project.



## Run Pathways in interactive mode

  1. Set the following environment variables:
         
         export WORKLOAD=WORKLOAD
         export WORKLOAD_NODEPOOL_COUNT=WORKLOAD_NODEPOOL_COUNT
         export COMPUTE_TYPE="COMPUTE_TYPE"
         export TOPOLOGY="TOPOLOGY"
         export PROJECT_ID=PROJECT_ID
         export REGION=REGION
         export ZONE=ZONE
         export CLUSTER=CLUSTER
         export BUCKET_NAME=BUCKET_NAME

Replace the following:

     * `WORKLOAD`: a unique name to identify your workload (22 characters or fewer due to DNS label limits).
     * `WORKLOAD_NODEPOOL_COUNT`: the number of node pools used by a Pathways workload.
     * `COMPUTE_TYPE`: the TPU machine type—for example, `ct6e-standard-4t`. For more information about supported TPU types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
     * `TOPOLOGY`: the TPU placement topology—for example, `2x4`.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `REGION`: the region where your bucket and cluster are located.
     * `ZONE`: the zone where you plan to run your workload.
     * `CLUSTER`: the name of your GKE cluster.
     * `BUCKET_NAME`: the Cloud Storage bucket for Pathways artifacts.
  2. If you haven't already created a Cloud Storage bucket for Pathways artifacts, create one:
         
         gcloud storage buckets create gs://${BUCKET_NAME} \
             --project=${PROJECT_ID} \
             --location=${REGION}
         

  3. Create the Pathways containers on the cluster. To run a headless workload, use the `gcluster job submit` command (for more information, see the [Cluster Toolkit Job Submission Guide](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/docs/gcluster_job_guide.md)):
         
         gcluster job submit \
             --pathways \
             --pathways-gcs-location="gs://${BUCKET_NAME}/pathways-artifacts" \
             --name=${WORKLOAD} \
             --cluster=${CLUSTER} \
             --project=${PROJECT_ID} \
             --location=${ZONE} \
             --num-slices=${WORKLOAD_NODEPOOL_COUNT} \
             --compute-type=${COMPUTE_TYPE} \
             --topology=${TOPOLOGY} \
             --pathways-headless
         

The `gcluster job submit` command looks for a CPU node pool named `cpu-np` or `pathways-np` to run the Pathways head Pod. If your CPU node pool has a different name (such as `cpu-pathways-np` from the [cluster creation guide](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-gke-cluster)), add the `--pathways-head-np=NODE_POOL_NAME` flag to the `gcluster job submit` commands on this page. Otherwise, the command fails with the error `failed to auto-detect a suitable CPU node pool`.




At this point, your JAX workload can connect to the IFRT proxy server.

## Connect to the Pathways cluster in interactive mode

You can connect to the Pathways cluster with or without port forwarding. Use one of the following sections to connect to the Pathways cluster.

### Connect by using port forwarding

From any host with access to your cluster's control plane, forward local port `29000` to the Pathways head Pod to access the proxy server:
    
    
    PROXY_POD=$(kubectl get pods | grep ${WORKLOAD}-pathways-head | awk '{print $1}')
    PROXY_PORT=29000
    kubectl port-forward ${PROXY_POD} ${PROXY_PORT}:${PROXY_PORT}
    

The output is similar to the following:
    
    
    Forwarding from 127.0.0.1:29000 -> 29000
    Forwarding from [::1]:29000 -> 29000
    

On the same host, open a new terminal window. Using Python 3.11 or later, create a virtual environment, install the `pathwaysutils` and `jax` packages, set the `JAX_PLATFORMS` and `JAX_BACKEND_TARGET` environment variables, and run a Python script that imports `pathwaysutils` and `jax`:
    
    
    python3 -m venv .venv
    source .venv/bin/activate
    pip install pathwaysutils jax
    
    JAX_PLATFORMS=proxy JAX_BACKEND_TARGET=grpc://127.0.0.1:29000 python -c 'import pathwaysutils; import jax; import pprint; pathwaysutils.initialize(); pprint.pprint(jax.devices())'
    

The output is similar to the following:
    
    
    [device(144,TPU_DEVICE,coords=[0,0,0,0],vtask=0,slice=0,default_mem=device,mem_spaces=3),
    device(145,TPU_DEVICE,coords=[1,0,0,0],vtask=0,slice=0,default_mem=device,mem_spaces=3),
    device(146,TPU_DEVICE,coords=[0,1,0,0],vtask=0,slice=0,default_mem=device,mem_spaces=3),
    device(147,TPU_DEVICE,coords=[1,1,0,0],vtask=0,slice=0,default_mem=device,mem_spaces=3),
    device(148,TPU_DEVICE,coords=[0,0,1,0],vtask=1,slice=0,default_mem=device,mem_spaces=3),
    device(149,TPU_DEVICE,coords=[1,0,1,0],vtask=1,slice=0,default_mem=device,mem_spaces=3),
    device(150,TPU_DEVICE,coords=[0,1,1,0],vtask=1,slice=0,default_mem=device,mem_spaces=3),
    device(151,TPU_DEVICE,coords=[1,1,1,0],vtask=1,slice=0,default_mem=device,mem_spaces=3),
    device(162,TPU_DEVICE,coords=[0,0,0,0],vtask=0,slice=1,default_mem=device,mem_spaces=3),
    device(163,TPU_DEVICE,coords=[1,0,0,0],vtask=0,slice=1,default_mem=device,mem_spaces=3),
    device(164,TPU_DEVICE,coords=[0,1,0,0],vtask=0,slice=1,default_mem=device,mem_spaces=3),
    device(165,TPU_DEVICE,coords=[1,1,0,0],vtask=0,slice=1,default_mem=device,mem_spaces=3),
    device(166,TPU_DEVICE,coords=[0,0,1,0],vtask=1,slice=1,default_mem=device,mem_spaces=3),
    device(167,TPU_DEVICE,coords=[1,0,1,0],vtask=1,slice=1,default_mem=device,mem_spaces=3),
    device(168,TPU_DEVICE,coords=[0,1,1,0],vtask=1,slice=1,default_mem=device,mem_spaces=3),
    device(169,TPU_DEVICE,coords=[1,1,1,0],vtask=1,slice=1,default_mem=device,mem_spaces=3)]
    Waiting up to 5 seconds.
    Sent all pending logs.
    2024-11-13 21:38:51.267523: W external/xla/xla/python/ifrt_proxy/client/grpc_client.cc:63] IFRT proxy server disconnected: CANCELLED: Cancelled
    

### Connect from hosts in the VPC without using port forwarding

If you don't want to use port forwarding, you can connect to the Pathways cluster by using Cloud DNS or an internal load balancer.

#### Connect by using Cloud DNS

Enabling Cloud DNS in your cluster switches the DNS provider from `kube-dns` to Cloud DNS. When enabled, GKE creates a private Cloud DNS zone in your Virtual Private Cloud (VPC) network for the DNS names. For more information, see [Using Cloud DNS for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns).

If you enable Cloud DNS with VPC scope or additive VPC scope, the Kubernetes DNS names are resolvable from non-GKE VMs inside your VPC network. With cluster scope, only nodes in the cluster can resolve these names. The names have the format `SERVICE_NAME.NAMESPACE.svc.CUSTOM_DNS_DOMAIN`. The Pathways head Pod has a service named `WORKLOAD-pathways-head-0-0.WORKLOAD.NAMESPACE.svc.CUSTOM_DNS_DOMAIN`.

The following commands show how to connect to your Pathways cluster by using Cloud DNS:

  1. Confirm that the leader DNS entry is resolvable from a non-GKE host:
         
         host WORKLOAD-pathways-head-0-0.WORKLOAD.default.svc.CUSTOM_DNS_DOMAIN

Replace the following:

     * `WORKLOAD`: the name of your Pathways workload.
     * `CUSTOM_DNS_DOMAIN`: the custom DNS domain configured for your cluster.

The output is similar to the following:
    
    WORKLOAD-pathways-head-0-0.WORKLOAD.default.svc.CUSTOM_DNS_DOMAIN has address 10.0.2.75

  2. Connect to the Pathways cluster by using the DNS name:
         
         JAX_PLATFORMS=proxy JAX_BACKEND_TARGET=grpc://WORKLOAD-pathways-head-0-0.WORKLOAD.default.svc.CUSTOM_DNS_DOMAIN:29000 python -c 'import pathwaysutils; import jax; import pprint; pathwaysutils.initialize(); pprint.pprint(jax.devices())'

The output is similar to the following:
         
         [device(216,TPU_DEVICE,coords=[0,0,0,0],vtask=0,slice=0,default_mem=device,mem_spaces=3),
         device(217,TPU_DEVICE,coords=[1,0,0,0],vtask=0,slice=0,default_mem=device,mem_spaces=3),
         device(218,TPU_DEVICE,coords=[0,1,0,0],vtask=0,slice=0,default_mem=device,mem_spaces=3),
         device(219,TPU_DEVICE,coords=[1,1,0,0],vtask=0,slice=0,default_mem=device,mem_spaces=3),
         device(220,TPU_DEVICE,coords=[0,0,1,0],vtask=1,slice=0,default_mem=device,mem_spaces=3),
         device(221,TPU_DEVICE,coords=[1,0,1,0],vtask=1,slice=0,default_mem=device,mem_spaces=3),
         device(222,TPU_DEVICE,coords=[0,1,1,0],vtask=1,slice=0,default_mem=device,mem_spaces=3),
         device(223,TPU_DEVICE,coords=[1,1,1,0],vtask=1,slice=0,default_mem=device,mem_spaces=3),
         device(234,TPU_DEVICE,coords=[0,0,0,0],vtask=0,slice=1,default_mem=device,mem_spaces=3),
         device(235,TPU_DEVICE,coords=[1,0,0,0],vtask=0,slice=1,default_mem=device,mem_spaces=3),
         device(236,TPU_DEVICE,coords=[0,1,0,0],vtask=0,slice=1,default_mem=device,mem_spaces=3),
         device(237,TPU_DEVICE,coords=[1,1,0,0],vtask=0,slice=1,default_mem=device,mem_spaces=3),
         device(238,TPU_DEVICE,coords=[0,0,1,0],vtask=1,slice=1,default_mem=device,mem_spaces=3),
         device(239,TPU_DEVICE,coords=[1,0,1,0],vtask=1,slice=1,default_mem=device,mem_spaces=3),
         device(240,TPU_DEVICE,coords=[0,1,1,0],vtask=1,slice=1,default_mem=device,mem_spaces=3),
         device(241,TPU_DEVICE,coords=[1,1,1,0],vtask=1,slice=1,default_mem=device,mem_spaces=3)]
         Waiting up to 5 seconds.
         Sent all pending logs.
         2024-11-14 00:02:49.882044: W external/xla/xla/python/ifrt_proxy/client/grpc_client.cc:63] IFRT proxy server disconnected: CANCELLED: Cancelled
         




#### Connect by using an internal load balancer

For a private IP address in your VPC network that points to your Pathways deployment, create a Service backed by an internal load balancer (ILB). This doesn't require your cluster to have Cloud DNS enabled.

For clusters with many VMs, enable ILB subsetting if you create internal load balancers. For more information, see [Enable GKE subsetting in an existing cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing#enable_ilb_subsetting_existing_cluster). When ILB subsetting isn't enabled, all nodes in the cluster are part of the backend instance group for all internal load balancers, which doesn't scale beyond 250 nodes. With ILB subsetting enabled, GKE creates network endpoint groups instead of instance groups, and includes only nodes that run one of the Service's serving Pods. Enabling ILB subsetting has a one-time setup latency of about 15 minutes. The following command enables ILB subsetting:
    
    
    gcloud container clusters update ${CLUSTER} \
        --project=${PROJECT_ID} \
        --location=CLUSTER_LOCATION \
        --enable-l4-ilb-subsetting

Replace `CLUSTER_LOCATION` with the region or zone where your cluster is located.

After you enable ILB subsetting, create a Kubernetes Service of type `LoadBalancer` by using the following YAML manifest. This causes GKE to create an internal load balancer inside your cluster's VPC network:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: WORKLOAD-ilb
      annotations:
        networking.gke.io/load-balancer-type: "Internal"
        networking.gke.io/internal-load-balancer-allow-global-access: "true"
    spec:
      type: LoadBalancer
      externalTrafficPolicy: Local
      selector:
        jobset.sigs.k8s.io/jobset-name: WORKLOAD
        jobset.sigs.k8s.io/replicatedjob-name: pathways-head
      ports:
      - name: tcp-port
        protocol: TCP
        port: 29000
        targetPort: 29000

Replace `WORKLOAD` with the name of your Pathways workload, and save the file as `pathways-headless-ilb.yaml`.

Apply the manifest:
    
    
    kubectl apply -f pathways-headless-ilb.yaml
    

After GKE creates the load balancer (about a minute later), verify that the `EXTERNAL-IP` column shows an IP address:
    
    
    kubectl get services
    

The output is similar to the following:
    
    
    NAME             TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)           AGE
    WORKLOAD       ClusterIP      None            <none>        <none>            30m
    WORKLOAD-ilb   LoadBalancer   34.118.232.46   10.0.0.22     29000:31246/TCP   2m41s

You can access the Pathways deployment without port forwarding from hosts in the same VPC network as your cluster:
    
    
    JAX_PLATFORMS=proxy JAX_BACKEND_TARGET=grpc://EXTERNAL_IP:29000 python -c 'import pathwaysutils; import jax; import pprint; pathwaysutils.initialize(); pprint.pprint(jax.devices())'

Replace `EXTERNAL_IP` with the `EXTERNAL-IP` value displayed by `kubectl get services`—for example, `10.0.0.22`.

The output is similar to the following:
    
    
    [device(288,TPU_DEVICE,coords=[0,0,0,0],vtask=0,slice=0,default_mem=device,mem_spaces=3),
     device(289,TPU_DEVICE,coords=[1,0,0,0],vtask=0,slice=0,default_mem=device,mem_spaces=3),
     device(290,TPU_DEVICE,coords=[0,1,0,0],vtask=0,slice=0,default_mem=device,mem_spaces=3),
     device(291,TPU_DEVICE,coords=[1,1,0,0],vtask=0,slice=0,default_mem=device,mem_spaces=3),
     device(292,TPU_DEVICE,coords=[0,0,1,0],vtask=1,slice=0,default_mem=device,mem_spaces=3),
     device(293,TPU_DEVICE,coords=[1,0,1,0],vtask=1,slice=0,default_mem=device,mem_spaces=3),
     device(294,TPU_DEVICE,coords=[0,1,1,0],vtask=1,slice=0,default_mem=device,mem_spaces=3),
     device(295,TPU_DEVICE,coords=[1,1,1,0],vtask=1,slice=0,default_mem=device,mem_spaces=3),
     device(306,TPU_DEVICE,coords=[0,0,0,0],vtask=0,slice=1,default_mem=device,mem_spaces=3),
     device(307,TPU_DEVICE,coords=[1,0,0,0],vtask=0,slice=1,default_mem=device,mem_spaces=3),
     device(308,TPU_DEVICE,coords=[0,1,0,0],vtask=0,slice=1,default_mem=device,mem_spaces=3),
     device(309,TPU_DEVICE,coords=[1,1,0,0],vtask=0,slice=1,default_mem=device,mem_spaces=3),
     device(310,TPU_DEVICE,coords=[0,0,1,0],vtask=1,slice=1,default_mem=device,mem_spaces=3),
     device(311,TPU_DEVICE,coords=[1,0,1,0],vtask=1,slice=1,default_mem=device,mem_spaces=3),
     device(312,TPU_DEVICE,coords=[0,1,1,0],vtask=1,slice=1,default_mem=device,mem_spaces=3),
     device(313,TPU_DEVICE,coords=[1,1,1,0],vtask=1,slice=1,default_mem=device,mem_spaces=3)]
    Waiting up to 5 seconds.
    Sent all pending logs.
    2024-11-14 00:30:07.296917: W external/xla/xla/python/ifrt_proxy/client/grpc_client.cc:63] IFRT proxy server disconnected: CANCELLED: Cancelled
    

**Note:** Your IP addresses differ from the addresses shown in the preceding command and output examples.

## Jupyter notebooks

You can create a Jupyter notebook by using Vertex AI, or you can create a self-hosted Jupyter notebook.

### Create a Vertex AI Workbench instance

After setting up and verifying your Pathways cluster, you can access the GKE TPU VMs from a Vertex AI Workbench Jupyter notebook. The following setup instructions assume that your GKE Pathways cluster resides in the same VPC network (which is the default network unless you've configured otherwise).

  1. Go to the [Vertex AI Workbench](https://console.cloud.google.com/vertex-ai/workbench) page in the Google Cloud console.
  2. On the **Instances** tab, click **Create new** , and make sure that the network matches your GKE cluster's network.

Alternatively, use the command line to create a new Vertex AI Workbench instance:
         
         gcloud workbench instances create INSTANCE_NAME \
             --project=PROJECT_ID \
             --machine-type=e2-standard-4 \
             --data-disk-size=100 \
             --location=ZONE \
             --network=NETWORK

Replace the following:

     * `INSTANCE_NAME`: the name of your Vertex AI Workbench instance.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `ZONE`: the zone where you want to create the instance.
     * `NETWORK`: the name of your GKE cluster's VPC network. The `--network` flag is optional; if you omit it, the command uses the `default` network.
  3. After Vertex AI creates the instance, go to the instance and click **Open JupyterLab**.




### Create a self-hosted Jupyter notebook instance

The following command shows how to create a self-hosted Jupyter notebook instance by using the `gcluster job submit` command:
    
    
    gcluster job submit \
        --pathways \
        --name=${WORKLOAD} \
        --cluster=${CLUSTER} \
        --project=${PROJECT_ID} \
        --location=${ZONE} \
        --num-slices=${WORKLOAD_NODEPOOL_COUNT} \
        --compute-type=${COMPUTE_TYPE} \
        --topology=${TOPOLOGY} \
        --pathways-gcs-location="gs://${BUCKET_NAME}/pathways-artifacts" \
        --image=jupyter/base-notebook \
        --command="start-notebook.sh"
    

The following YAML manifest shows how to create a self-hosted Jupyter notebook instance by using `kubectl`. Apply the following YAML manifest after you create a headless Pathways cluster. For more information, see Run Pathways in interactive mode:
    
    
    apiVersion: batch/v1
    kind: Job
    metadata:
      name: WORKLOAD
    spec:
      template:
        spec:
          hostNetwork: true
          dnsPolicy: ClusterFirstWithHostNet
          restartPolicy: OnFailure
          containers:
          - name: jupyter-notebook
            image: jupyter/base-notebook  # Use the appropriate Jupyter image
            ports:
            - containerPort: 8888

The `hostNetwork: true` field lets the JAX client in the notebook complete the Application Layer Transport Security (ALTS) handshake with the Pathways proxy server. Without this field, the connection fails on node pools that use Workload Identity Federation for GKE. The `dnsPolicy: ClusterFirstWithHostNet` field lets the notebook resolve in-cluster DNS names, such as the name of the Pathways head Pod. For more information, see [Troubleshoot Pathways on Cloud](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/troubleshooting-pathways).

### Connect to the notebook instance

Connect to the notebook from your local machine by using port forwarding:

### Cluster Toolkit
    
    
    MAIN_POD=$(kubectl get pods | grep ${WORKLOAD}-pathways-head | awk '{print $1}')
    kubectl port-forward pod/${MAIN_POD} 8888:8888
    

### kubectl
    
    
    MAIN_POD=$(kubectl get pods \
      --selector=batch.kubernetes.io/job-name=WORKLOAD \
      --output=jsonpath='{.items[0].metadata.name}')
    kubectl port-forward pod/${MAIN_POD} 8888:8888

In your local browser, go to `http://localhost:8888?token=TOKEN`. Replace `TOKEN` with the token from the Jupyter notebook container's logs:
    
    
    kubectl logs ${MAIN_POD}

The output is similar to the following:
    
    
    ...
    Or copy and paste one of these URLs:
      http://NODE_NAME:8888/lab?token=TOKEN
      http://127.0.0.1:8888/lab?token=TOKEN

`NODE_NAME` is the hostname of the GKE node that runs the notebook Pod (for example, `gke-my-cluster-cpu-np-1a2b3c4d-ef56`).

### Notebook connectivity to the Pathways cluster

  1. From within JupyterLab, create a new Python 3 notebook.
  2. Connect to the Pathways proxy server.



In the notebook, add a cell to install `pathwaysutils`, set `JAX_PLATFORMS` to `proxy`, and set `JAX_BACKEND_TARGET` to `grpc://PROXY_ADDRESS:29000`:

**Note:** The value for `PROXY_ADDRESS` depends on the connection option that you chose in Connect to the Pathways cluster in interactive mode.
    
    
    !pip install pathwaysutils
    # Set JAX_PLATFORMS and JAX_BACKEND_TARGET if you're not using `gcluster job submit` to deploy the notebook
    %env JAX_PLATFORMS=proxy
      # Replace your proxy address in the following line:
    %env JAX_BACKEND_TARGET=grpc://PROXY_ADDRESS:29000

Replace `PROXY_ADDRESS` with the host or IP address of your Pathways proxy server from Connect to the Pathways cluster in interactive mode (for example, `127.0.0.1`, the Cloud DNS hostname, or the internal load balancer IP address). If you deployed a self-hosted notebook by using `kubectl`, replace `PROXY_ADDRESS` with the in-cluster DNS name of the Pathways head Pod, so that the `JAX_BACKEND_TARGET` value is `grpc://WORKLOAD-pathways-head-0-0.WORKLOAD:29000`.

Add a second cell to verify connectivity and print the devices in the Pathways cluster:
    
    
    import pathwaysutils
    import jax
    
    pathwaysutils.initialize()
    print(jax.devices())
    

If the connection succeeds, the output includes a message indicating that JAX detected the `Pathways-on-Cloud` backend.

The number of JAX devices listed matches the number of TPU chips and the number of slices that you specified when you created the Pathways cluster.

### Add your code to a notebook

Add your own JAX code and execute it interactively on the TPUs in the Pathways cluster. The following code shows how to perform computations across two slices from a single notebook. To run the complete example, create your Pathways workload with at least two slices by setting `WORKLOAD_NODEPOOL_COUNT` to `2` or more. With one slice, `slice1_devices` is empty, and the last part of the example fails with a `ValueError`:
    
    
    import jax
    import jax.numpy as jnp
    from jax import lax
    import numpy as np
    
    # You can use JAX APIs as usual across any of the devices.
    x = jax.device_put(np.pi / 2., jax.devices()[-1])
    jax.jit(jnp.sin)(x)
    
    # pmap can run across all devices on all slices
    num_tpus = jax.device_count()
    f = jax.pmap(lambda x: lax.psum(1, 'i'), 'i')
    x = jnp.arange(num_tpus)
    y = f(x)
    print(y)
    
    # You can also target devices from a specific slice
    slice0_devices = [d for d in jax.devices() if d.slice_index == 0]
    f = jax.pmap(lambda x: lax.psum(1, 'i'), 'i', devices=slice0_devices)
    x = jnp.arange(len(slice0_devices))
    y = f(x)
    print(y)
    print(y.global_shards)
    
    # You can send data produced on one slice to another slice
    slice1_devices = [d for d in jax.devices() if d.slice_index == 1]
    g = jax.pmap(lambda x: x + lax.axis_index('i'), 'i', devices=slice1_devices)
    z = g(y)
    print(z)
    print(z.global_shards)
    

## Delete your Pathways interactive workload

### Cluster Toolkit
    
    
    gcluster job cancel WORKLOAD \
      --cluster=CLUSTER \
      --project=PROJECT_ID \
      --location=ZONE

### kubectl
    
    
    kubectl delete job WORKLOAD

## What's next

  * [Create a GKE cluster with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-gke-cluster)
  * [Run a batch workload with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/batch-workload)
  * [Port JAX workloads to Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/porting-jax-workloads)
  * [Resilient training with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/resilient-training)
  * [Troubleshoot Pathways on Cloud](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/troubleshooting-pathways)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-06 UTC."],[],[]] 

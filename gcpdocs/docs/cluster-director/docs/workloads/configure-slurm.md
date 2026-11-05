---
url: https://docs.cloud.google.com/cluster-director/docs/workloads/configure-slurm/
title: Submit and monitor jobs with Slurm \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-05T11:12:31.411688+00:00
---

# Submit and monitor jobs with Slurm  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/workloads/configure-slurm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Submit and monitor jobs with Slurm Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to submit and monitor jobs by using Slurm in Cluster Director. By using flags that optimize job scheduling for your hardware and checking node states, you can achieve the following:

  * Align job scheduling with the underlying physical hardware for A4X virtual machine (VM) instances to minimize network latency.

  * Specify 2D or 3D slice topologies for TPU VMs across static or dynamic nodesets in your cluster.

  * Verify job allocations across cluster partitions and stop unneeded nodes.




For a high-level overview of how Slurm orchestrates jobs in Cluster Director, see [Slurm orchestration in Cluster Director](https://docs.cloud.google.com/cluster-director/docs/orchestration).

## Before you begin

If you haven't already, then connect to a login node in your cluster. For instructions, see [Connect to a cluster's login node](https://docs.cloud.google.com/cluster-director/docs/manage/connect-to-cluster#login).

## Submit jobs on A4X VMs

For cluster partitions that use [A4X VMs](https://docs.cloud.google.com/cluster-director/docs/gpu-machines#a4x-series), Slurm uses [block topology](https://slurm.schedmd.com/topology.html#block) to align job scheduling with the physical layout of A4X machines. This configuration minimizes network latency by ensuring that tasks run on VMs that are physically close to each other.

When you run the [`salloc`](https://slurm.schedmd.com/salloc.html), [`sbatch`](https://slurm.schedmd.com/sbatch.html), or [`srun` commands](https://slurm.schedmd.com/srun.html) in Slurm, you can control how the job interacts with blocks of A4X VMs by using the following flags:

  * To group nodes into blocks of a specific size, use the [`--segment` flag](https://slurm.schedmd.com/sbatch.html#OPT_segment):
        
        --segment=SEGMENT_SIZE
        

Replace `SEGMENT_SIZE` with a value between `1` and `18`. If your job can't start because there aren't enough adjacent nodes to match your segment size, then specify `1`.

  * To reserve an entire sub-block for a job, use the [`--exclusive=topo` flag](https://slurm.schedmd.com/sbatch.html#OPT_exclusive):
        
        --exclusive=topo
        

This flag prevents other jobs from sharing the NVLink domain, which helps ensure that no other jobs interfere with your job.




## Submit jobs on TPU VMs

**Preview — Submit jobs on TPU VMs**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For cluster partitions that use [TPU VMs](https://docs.cloud.google.com/cluster-director/docs/tpu-machines) with Slurm controller version `26.05`, you must specify the TPU generation and slice topology with the `--layout` flag. Include this flag when you run the [`salloc`](https://slurm.schedmd.com/salloc.html), [`sbatch`](https://slurm.schedmd.com/sbatch.html), or [`srun` commands](https://slurm.schedmd.com/srun.html) in Slurm.

For example, to run a workload or allocate resources on a TPU slice, use one of the following commands:

  * To run a single command across a TPU slice, use the `srun` command:
        
        srun --layout=TPU_GENERATION=TOPOLOGY hostname
        

  * To allocate an interactive TPU slice across multiple commands, use the `salloc` command:
        
        salloc --layout=TPU_GENERATION=TOPOLOGY
        

When you finish your interactive session, run `exit` to release the TPU slice.




Replace the following:

  * `TPU_GENERATION`: the TPU generation for the partition's machine type. Specify one of the following values:

    * For TPU7x: `tpu7x`

    * For TPU v6e: `v6e`

    * For TPU v5p: `v5p`

  * `TOPOLOGY`: the 2D (`AxB` for TPU v6e) or 3D (`AxBxC` for TPU7x and TPU v5p) chip topology for the slice. Specify multi-host dimensions from smallest to largest, such as `2x4` instead of `4x2`, or `2x2x4` instead of `4x2x2`. For a single-host 3D slice, specify `2x2x1`. Cluster Director supports slices of up to 1,000 TPU VMs for TPU7x and TPU v5p, and up to 64 TPU VMs for TPU v6e. How Slurm handles this value depends on the nodeset type:

    * **Static TPU nodesets** : this topology must match the fixed slice topology of the nodeset and fill an entire slice. To check which `--layout` value a static nodeset uses, see View TPU node features and slices.

    * **Dynamic TPU nodesets** : Slurm provisions a slice that matches this topology for a single job and deletes the slice when the job finishes. To reuse a dynamic slice across multiple commands, allocate the slice with the `salloc` command, and then run `exit` when you finish.


**Caution:** When you use the `--layout` flag, omit the [`-N` and `--nodes` flags](https://slurm.schedmd.com/srun.html#OPT_nodes). Slurm calculates the required VM count from the slice topology at 4 TPU chips per VM. If you specify a node count that doesn't match the slice topology, then your job fails.

The following table shows an example `--layout` value for each supported TPU generation. For the complete list of supported slice topologies, VM counts, and chip counts, see [Slice topologies and boot disk requirements](https://docs.cloud.google.com/cluster-director/docs/tpu-machines#topologies-and-boot-disks).

TPU generation | Machine type | Example `--layout` value | VMs per slice | TPU chips per slice  
---|---|---|---|---  
TPU7x (Ironwood) | `tpu7x-standard-4t` | `tpu7x=2x2x2` | 2 | 8  
TPU v6e (Trillium) | `ct6e-standard-4t` | `v6e=2x4` | 2 | 8  
TPU v5p | `ct5p-hightpu-4t` | `v5p=2x2x2` | 2 | 8  
  
### View TPU node features and slices

Cluster Director assigns [node features](https://slurm.schedmd.com/slurm.conf.html#OPT_Features) to TPU nodesets in Slurm so that you don't need to check the Google Cloud console or the Cluster Director API. Cluster Director sets the following features based on the nodeset type:

  * **Static TPU nodesets** : Cluster Director groups static nodes into slices based on the fixed slice topology (`acceleratorTopology`) set on the nodeset and assigns the `TPU_GENERATION_TOPOLOGY` feature—for example, `v6e_2x4`.

  * **Dynamic TPU nodesets** : Cluster Director assigns the `tpu_dynamic` feature to dynamic TPU nodes.




From a login node, you can inspect TPU node features and static slices with the following Slurm commands:

  * To view node features and find which `--layout` value a static TPU nodeset uses, run [`sinfo`](https://slurm.schedmd.com/sinfo.html):
        
        sinfo -a -o "%30N %10D %20F %f"
        

The output is similar to the following:
        
        NODELIST                       NODES      NODES(A/I/O/T)       AVAIL_FEATURES
        cluster000-cpu-0               1          1/0/0/1              (null)
        cluster000-tpu-dyn-[0-29]      30         4/26/0/30            tpu_dynamic
        cluster000-tpu-static-[0-7]    8          2/0/6/8              v6e_2x4
        

  * To view which VM nodes belong to each static slice, run [`scontrol`](https://slurm.schedmd.com/scontrol.html):
        
        scontrol show topology tpu
        

For static TPU nodesets, Cluster Director tracks each slice as a block in a Slurm topology named `tpu`. The command output lists the VMs in each TPU slice block, not the chip topology for the `--layout` flag. The output is similar to the following:
        
        BlockName=tpu-static-1a2b3c4 BlockIndex=0 Nodes=cluster000-tpu-static-[0-1]
        BlockName=tpu-static-5d6e7f8 BlockIndex=1 Nodes=cluster000-tpu-static-[2-3]
        BlockName=tpu-static-9a0b1c2 BlockIndex=2 Nodes=cluster000-tpu-static-[4-5]
        BlockName=tpu-static-3d4e5f6 BlockIndex=3 Nodes=cluster000-tpu-static-[6-7]
        




### Submit a single-slice TPU job

This batch script requires a shared `/home` directory and outbound internet access on compute nodes, such as [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview). To submit a batch job that initializes JAX across a single TPU slice, complete the following steps:

  1. Create a batch script named `single_slice.sh`:
         
         #!/bin/bash
         #SBATCH --job-name=tpu_single_slice
         #SBATCH --output=single_slice_%j.log
         #SBATCH --layout=TPU_GENERATION=TOPOLOGY
         
         VENV="${HOME}/jax_env"
         if [ ! -f "${VENV}/bin/activate" ]; then
           python3 -m venv "${VENV}"
           source "${VENV}/bin/activate"
           pip install --upgrade pip
           pip install "jax[tpu]" \
             -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
         else
           source "${VENV}/bin/activate"
         fi
         
         srun python3 -c \
           "import jax; jax.distributed.initialize(); print(jax.devices())"
         

Replace the following:

     * `TPU_GENERATION`: the TPU generation that your VMs use. Specify one of the following values:

       * For TPU7x: `tpu7x`

       * For TPU v6e: `v6e`

       * For TPU v5p: `v5p`

     * `TOPOLOGY`: your slice topology, such as `2x2x2` or `2x4`

  2. Submit the batch script with the `sbatch` command:
         
         sbatch single_slice.sh
         

  3. Check the job status with `squeue`, and after the job finishes, inspect the output log:
         
         squeue
         cat single_slice_JOB_ID.log
         

Replace `JOB_ID` with the job ID returned by `sbatch`. Confirm that the log lists the TPU machines in your slice.




### Submit a multi-slice TPU job

To run a workload across multiple TPU slices, submit a Slurm [heterogeneous job](https://slurm.schedmd.com/heterogeneous_jobs.html). Each `#SBATCH hetjob` directive separates a slice in the job allocation. For distributed frameworks such as JAX to coordinate communication across separate slices over the data center network (DCN), you must set the following MegaScale environment variables on the worker nodes in each slice:

  * **`MEGASCALE_COORDINATOR_ADDRESS`** : the IP address and port of the primary coordinator host (the first node in heterogeneous group `0`).

  * **`MEGASCALE_NUM_SLICES`** : the total number of TPU slices in the job.

  * **`MEGASCALE_SLICE_ID`** : the zero-based index of each slice (for example, `0` or `1`).




This batch script requires a shared `/home` directory and outbound internet access on compute nodes, such as [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview). To submit a multi-slice batch job across two TPU slices, complete the following steps:

  1. Create a batch script named `multislice.sh`:
         
         #!/bin/bash
         #SBATCH --job-name=tpu_multislice
         #SBATCH --output=multislice_%j.log
         #SBATCH --layout=TPU_GENERATION=TOPOLOGY
         #SBATCH hetjob
         #SBATCH --layout=TPU_GENERATION=TOPOLOGY
         set -ex
         
         # 1. Create and activate a shared Python virtual environment with JAX
         VENV="${HOME}/jax_env"
         if [ ! -f "${VENV}/bin/activate" ]; then
           python3 -m venv "${VENV}"
           source "${VENV}/bin/activate"
           pip install --upgrade pip
           pip install "jax[tpu]" \
             -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
         else
           source "${VENV}/bin/activate"
         fi
         
         # 2. Configure the MegaScale and JAX coordinators on the first node
         export COORDINATOR_HOST_IP=$(hostname -I | awk '{print $1}')
         export MEGASCALE_COORDINATOR_ADDRESS="${COORDINATOR_HOST_IP}:8080"
         export MEGASCALE_NUM_SLICES=2
         export JAX_COORDINATOR_PORT=8476
         
         # 3. Write the slice ID to /tmp/tpu_env on each slice
         srun --het-group=0 \
           bash -c 'echo "export MEGASCALE_SLICE_ID=0" > /tmp/tpu_env'
         srun --het-group=1 \
           bash -c 'echo "export MEGASCALE_SLICE_ID=1" > /tmp/tpu_env'
         
         # 4. Run the workload across both slices
         srun --het-group=0,1 bash -c '
           source /tmp/tpu_env &&
           source "${HOME}/jax_env/bin/activate" &&
           python3 - << "EOF"
         import os
         import jax
         
         num_slices = int(os.environ["MEGASCALE_NUM_SLICES"])
         slice_id = int(os.environ["MEGASCALE_SLICE_ID"])
         vms_per_slice = int(os.environ["SLURM_NNODES"])
         node_id = int(os.environ["SLURM_NODEID"])
         coordinator = (
             os.environ["COORDINATOR_HOST_IP"]
             + ":"
             + os.environ["JAX_COORDINATOR_PORT"]
         )
         
         jax.distributed.initialize(
             coordinator_address=coordinator,
             num_processes=num_slices * vms_per_slice,
             process_id=slice_id * vms_per_slice + node_id,
         )
         print(f"Total devices: {jax.device_count()}")
         EOF
         '
         

Replace the following:

     * `TPU_GENERATION`: the TPU generation that your VMs use. Specify one of the following values:

       * For TPU7x: `tpu7x`

       * For TPU v6e: `v6e`

       * For TPU v5p: `v5p`

     * `TOPOLOGY`: your slice topology, such as `2x2x2` or `2x4`

  2. Submit the batch script with the `sbatch` command:
         
         sbatch multislice.sh
         

  3. Check the job status with `squeue`, and after the job finishes, inspect the output log:
         
         squeue
         cat multislice_JOB_ID.log
         

Replace `JOB_ID` with the job ID returned by `sbatch`. Confirm that the log reports `Total devices:` for the combined TPU devices across both slices.




## Verify job allocations in your cluster

To verify whether your nodes have jobs that are scheduled on them, use the [`sinfo` command](https://slurm.schedmd.com/sinfo.html):
    
    
    sinfo
    

In the output, you can view the state for each node:

  * **`alloc`** : Slurm has assigned all vCPUs on the node to one or more jobs.

  * **`alloc#`** : Slurm has allocated the node to a job, and Cluster Director is starting the underlying compute instance.

  * **`alloc!`** : the node is active and running a job, and Slurm deletes the dynamic node when the job completes.

  * **`completing`** : the node has finished running a job. Slurm must wait for all associated processes to complete and for the node to return to the `idle` state before scheduling new jobs on this node.

  * **`down`** : Slurm can't schedule jobs on the node. A node enters this state if it encounters a host error, or if Cluster Director fails to obtain capacity for it.

  * **`drained`** : Slurm has removed the node from scheduling after the prolog health check identified an issue with the GPUs that are attached to the node. If workloads are already running on the node, then they might keep running until they complete. To return the node to service, see [Troubleshoot GPU health check failures](https://docs.cloud.google.com/cluster-director/docs/troubleshoot/health-checks).

  * **`idle`** : the node has obtained capacity and is preparing to run jobs.

  * **`idle#`** : Cluster Director is provisioning capacity to run your job on the node. If the node is a Flex-start VM, then this state also indicates that Cluster Director is attempting to obtain capacity. For more information, see [Characteristics of Flex-start](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option#key-characteristics-2).

  * **`idle~`** : the node isn't running or has stopped running.

  * **`idle%`** : Cluster Director is deleting the node.

  * **`mix`** : Slurm has allocated jobs to some, but not all, vCPUs on the node.

  * **`mix#`** : Slurm has allocated jobs to some vCPUs on the node; however, Cluster Director is still looking for capacity to run the jobs.




## Delete nodes

You can delete nodes in your cluster when, for example, you want to free up resources, scale down your cluster, or recreate nodes with a different OS image. For TPU nodes, all VMs in a slice share the same lifecycle; if you delete a TPU node in a slice, then Cluster Director tears down all other VMs in that slice. After deletion, Slurm recreates the nodes based on their type:

  * **Static nodes** : Slurm recreates the node. As soon as the compute instance boots, the node returns to service and you can run jobs on it.

  * **Dynamic nodes** : the node state changes to `idle~`. Slurm recreates the node when you submit a job that requires the additional compute capacity.




To delete nodes in your cluster, use the [`scontrol` command](https://slurm.schedmd.com/scontrol.html):
    
    
    sudo scontrol update nodename=NODE_NAMES state=NODE_STATE
    

Replace the following:

  * `NODE_NAMES`: a comma-separated list of nodes that you want to delete—for example, `node-1,node-2`. To delete a node in a TPU slice, then you must specify all nodes in that slice.

  * `NODE_STATE`: the power-down state for the nodes. Specify one of the following values:

    * To delete nodes after running jobs finish, specify `power_down_asap`.

    * To delete unresponsive nodes and stop running jobs without delay, specify `power_down_force`.




## What's next

  * [Monitor cluster performance with prebuilt dashboards](https://docs.cloud.google.com/cluster-director/docs/monitor/dashboards)

  * [Monitor clusters with custom dashboards or alerts](https://docs.cloud.google.com/cluster-director/docs/monitor/custom-dashboards)

  * [Manage cluster health](https://docs.cloud.google.com/cluster-director/docs/monitor/cluster-health)

  * [Troubleshoot cluster errors](https://docs.cloud.google.com/cluster-director/docs/troubleshoot/cluster-errors)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 

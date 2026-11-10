---
url: https://docs.cloud.google.com/filestore/docs/agent-sandbox-latebind/
title: Use Filestore agent volumes with GKE Agent Sandbox dynamic storage late-binding \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T16:20:34.325173+00:00
---

# Use Filestore agent volumes with GKE Agent Sandbox dynamic storage late-binding  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/agent-sandbox-latebind/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Use Filestore agent volumes with GKE Agent Sandbox dynamic storage late-binding Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Filestore agent volumes are available under an Allowlisted GA (AGA) program. To request access for your Google Cloud project, submit the Filestore agent volumes [access request form](https://forms.gle/vYPkcFiZVoTjf7Ah7). 

Dynamic storage late-binding lets you inject Filestore agent volumes directly into running, pre-warmed Google Kubernetes Engine (GKE) Agent Sandbox pods upon claim. By bypassing the standard Kubernetes volume attachment lifecycle, dynamic late-binding achieves under 100 ms storage attachment latency without requiring pod restarts.

This architecture lets high-density, low-latency agent platforms perform the following tasks:

  * Eliminate pod cold-start and container initialization delays.
  * Dynamically attach and detach persistent workspaces on demand.
  * Pause or hibernate idle agent sessions and resume them on any available pre-warmed sandbox pod while preserving file system state.



## Before you begin

  1. Complete the initial setup in [Set up GKE environment for Filestore agent volumes](https://docs.cloud.google.com/filestore/docs/use-filestore-agent-volumes-gke).
  2. Verify that your GKE cluster runs version `1.36.0-gke.3302001` or later. 
  3. Verify that your `volume-pool-sc` `StorageClass` specifies `volumeBindingMode: Immediate` and `reclaimPolicy: Delete`.



## Architecture overview

The late-binding architecture consists of four components:

  * **Platform orchestrator or custom controller:** A control-plane service or Kubernetes controller that manages session lifecycles. It watches for `SandboxClaim` events, resolves tenant volume metadata, calls the storage node daemon API to bind or unbind storage, and manages deletion finalizers.
  * **Storage node daemon:** A privileged `DaemonSet` running on each gVisor node that exposes a mount API to bind Filestore NFS exports into host pod directories.
  * **`SandboxTemplate` with `force-shared`:** A [gVisor sandbox pod](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) template that lets host mounts propagate dynamically into the gVisor sandbox container.
  * **`SandboxWarmPool`:** A pool of pre-warmed running sandbox pods ready to receive mount requests instantly upon claim.



### How dynamic late-binding works

Instead of attaching a `PersistentVolumeClaim` (PVC) at pod creation time, dynamic late-binding uses the following lifecycle:

  1. **Pre-warm sandboxes:** A `SandboxWarmPool` maintains running gVisor pods configured with an `emptyDir` volume, `HostToContainer` mount propagation, and the `dev.gvisor.empty-dir.VOLUME_NAME.force-shared: "true"` annotation, where `<var>VOLUME_NAME</var>` is the name of the `emptyDir` volume.
  2. **Claim and provision:** When an agent session starts, your orchestrator creates a `SandboxClaim` (with a deletion finalizer) to claim a warm pod and provisions or selects a backing Filestore PVC.
  3. **Bind storage on the host:** Your orchestrator resolves the claimed pod's UID, node, and Filestore NFS export details, adds a deletion finalizer to the pod, and instructs the storage node daemon on that node to mount the NFS volume into the pod's backing `emptyDir` path on the host. With mount propagation enabled, the mounted workspace immediately appears inside the running gVisor container.
  4. **Unbind before teardown:** When the session pauses or ends, your orchestrator instructs the node daemon to unmount the NFS volume from the host directory before removing the finalizers from the `Pod` and `SandboxClaim`.

**Caution:** Because host-level mounts bypass standard Kubelet volume tracking, deleting a pod before unmounting its storage causes Kubelet cleanup of the `emptyDir` directory to fail with a `Device or resource busy` error, leaving the pod stuck in a `Terminating` state. Using finalizers on both the `SandboxClaim` and the `Pod` ensures that your orchestrator can cleanly unmount the Filestore volume before Kubernetes deletes the pod.



For a production reference implementation that automates these steps with a custom controller and authenticated node daemon, see the [GKE Sandbox late-binding storage example](https://github.com/kubernetes-sigs/agent-sandbox/tree/main/examples/latebind-storage-gke-sandbox) on GitHub.

## Deploy the storage node daemon

To test the late-binding workflow, deploy a privileged `DaemonSet` on your gVisor nodes that installs the NFS client utilities on the host and provides an execution environment for host mount commands.

  1. Create a manifest named `storage-node-daemon.yaml`:
         
         apiVersion: apps/v1
         kind: DaemonSet
         metadata:
           name: storage-node-daemon
           namespace: default
         spec:
           selector:
             matchLabels:
               app: storage-node-daemon
           template:
             metadata:
               labels:
                 app: storage-node-daemon
             spec:
               hostPID: true
               nodeSelector:
                 sandbox.gke.io/runtime: gvisor
               tolerations:
                 - key: "sandbox.gke.io/runtime"
                   operator: "Equal"
                   value: "gvisor"
                   effect: "NoSchedule"
               containers:
                 - name: daemon
                   image: debian:stable-slim
                   securityContext:
                     privileged: true
                   command: ["/bin/sh", "-c"]
                   args:
                     - |
                       nsenter -t 1 -m -u -i -n -- apt-get update && \
                       nsenter -t 1 -m -u -i -n -- apt-get install -y nfs-common || true
                       sleep infinity
         

  2. Apply the manifest:
         
         kubectl apply -f storage-node-daemon.yaml
         




## Configure the `SandboxTemplate` and `SandboxWarmPool`

To enable dynamic host mounts to propagate into a running gVisor sandbox, your `SandboxTemplate` must include the `dev.gvisor.empty-dir.workspace-volume.force-shared: "true"` annotation and set `mountPropagation: HostToContainer` on the `emptyDir` volume mount.

  1. Create a manifest named `sandbox-latebind.yaml` containing the template and warm pool:
         
         apiVersion: extensions.agents.x-k8s.io/v1alpha1
         kind: SandboxTemplate
         metadata:
           name: late-bind-template
           namespace: default
         spec:
           networkPolicyManagement: Unmanaged
           podTemplate:
             metadata:
               annotations:
                 dev.gvisor.empty-dir.workspace-volume.force-shared: "true"
             spec:
               runtimeClassName: gvisor
               automountServiceAccountToken: false
               nodeSelector:
                 sandbox.gke.io/runtime: gvisor
               tolerations:
                 - key: "sandbox.gke.io/runtime"
                   value: "gvisor"
                   effect: "NoSchedule"
               securityContext:
                 runAsNonRoot: true
                 runAsUser: 1000
                 runAsGroup: 1000
                 fsGroup: 1000
               containers:
                 - name: agent
                   image: busybox:latest
                   securityContext:
                     capabilities:
                       drop: ["ALL"]
                     allowPrivilegeEscalation: false
                   volumeMounts:
                     - name: workspace-volume
                       mountPath: /workspace
                       mountPropagation: HostToContainer
                   env:
                     - name: MOUNT_PATH
                       value: "/workspace"
                     - name: SUB_DIR
                       value: "user_data"
                   command: ["/bin/sh", "-c"]
                   args:
                     - |
                       echo "Waiting for late-bind signal..."
                       while [ ! -f $MOUNT_PATH/.ready ]; do sleep 0.05; done
                       echo "Filestore volume mounted successfully!"
                       ls -la $MOUNT_PATH/$SUB_DIR
                       date >> $MOUNT_PATH/$SUB_DIR/session.txt
                       sleep infinity
               volumes:
                 - name: workspace-volume
                   emptyDir: {}
         ---
         apiVersion: extensions.agents.x-k8s.io/v1alpha1
         kind: SandboxWarmPool
         metadata:
           name: late-bind-warmpool
           namespace: default
         spec:
           replicas: 2
           sandboxTemplateRef:
             name: late-bind-template
         

  2. Apply the manifest:
         
         kubectl apply -f sandbox-latebind.yaml
         




## Claim a sandbox and dynamically bind storage

  1. Create a manifest named `late-bind-claim.yaml` that claims a warm sandbox with a deletion finalizer (`agent.sandbox/storage-cleanup`) and provisions a Filestore agent volume PVC:
         
         apiVersion: extensions.agents.x-k8s.io/v1alpha1
         kind: SandboxClaim
         metadata:
           name: late-bind-session-1
           namespace: default
           finalizers:
             - agent.sandbox/storage-cleanup
         spec:
           sandboxTemplateRef:
             name: late-bind-template
         ---
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: session-1-pvc
           namespace: default
         spec:
           accessModes: [ReadWriteMany]
           storageClassName: volume-pool-sc
           resources:
             requests:
               storage: 1Gi
         

  2. Apply the manifest:
         
         kubectl apply -f late-bind-claim.yaml
         

  3. Retrieve the assigned pod details and backing Filestore NFS export attributes:
         
         POD_NAME=$(kubectl get pods \
           -l extensions.agents.x-k8s.io/claimed-by=late-bind-session-1 \
           -o jsonpath='{.items[0].metadata.name}')
         POD_UID=$(kubectl get pod "${POD_NAME}" -o jsonpath='{.metadata.uid}')
         NODE_NAME=$(kubectl get pod "${POD_NAME}" -o jsonpath='{.spec.nodeName}')
         PV_NAME=$(kubectl get pvc session-1-pvc -o jsonpath='{.spec.volumeName}')
         NFS_IP=$(kubectl get pv "${PV_NAME}" \
           -o jsonpath='{.spec.csi.volumeAttributes.ip}')
         NFS_PATH="/$(kubectl get pv "${PV_NAME}" \
           -o jsonpath='{.spec.csi.volumeAttributes.volume}')"
         

  4. Add a deletion finalizer to the claimed pod to prevent Kubelet from deleting the pod while the host mount is active:
         
         kubectl patch pod "${POD_NAME}" --type=merge \
           -p '{"metadata":{"finalizers":["agent.sandbox/storage-cleanup"]}}'
         

  5. Mount the Filestore NFS volume into the pod's host `emptyDir` directory and signal readiness:
         
         DAEMON_POD=$(kubectl get pods -l app=storage-node-daemon \
           --field-selector spec.nodeName="${NODE_NAME}" \
           -o jsonpath='{.items[0].metadata.name}')
         HOST_DIR="/var/lib/kubelet/pods/${POD_UID}/volumes/kubernetes.io~empty-dir/workspace-volume"
         kubectl exec "${DAEMON_POD}" -- nsenter -t 1 -m -- sh -c "
           mkdir -p ${HOST_DIR}/user_data &&
           mount -t nfs ${NFS_IP}:${NFS_PATH} ${HOST_DIR}/user_data &&
           chown -R 1000:1000 ${HOST_DIR}/user_data &&
           echo ready > ${HOST_DIR}/.ready
         "
         

  6. Verify that the volume is mounted inside the running sandbox pod:
         
         kubectl logs "${POD_NAME}" -c agent
         

The output confirms that the volume was mounted:
         
         Waiting for late-bind signal...
         Filestore volume mounted successfully!
         drwxr-xr-x    2 1000     1000          4096 ... user_data
         




## Unbind storage and release the sandbox

When an agent session pauses or ends, unmount the host storage before allowing Kubernetes to delete the pod.

  1. Initiate deletion of the `SandboxClaim` in the background. Because of the finalizer, Kubernetes marks the claim for deletion but pauses pod termination:
         
         kubectl delete sandboxclaim late-bind-session-1 --wait=false
         

  2. Unmount the Filestore NFS volume on the host node:
         
         kubectl exec "${DAEMON_POD}" -- nsenter -t 1 -m -- \
           umount -l "${HOST_DIR}/user_data"
         

  3. Remove the finalizers from both the `SandboxClaim` and the pod to complete termination:
         
         kubectl patch sandboxclaim late-bind-session-1 --type=merge \
           -p '{"metadata":{"finalizers":[]}}'
         kubectl patch pod "${POD_NAME}" --type=merge \
           -p '{"metadata":{"finalizers":[]}}'
         




To resume the session later, create a new `SandboxClaim` and mount the existing PVC (`session-1-pvc`) into the newly claimed warm pod.

## What's next

  * Explore static [Agent Sandbox integration](https://docs.cloud.google.com/filestore/docs/agent-sandbox).
  * Deploy self-managed [GKE workloads](https://docs.cloud.google.com/filestore/docs/self-managed-gke).
  * Learn how to create and manage [volume pools](https://docs.cloud.google.com/filestore/docs/create-volume-pools).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

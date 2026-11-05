---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/
title: Create Harbor registry instances \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-05T00:20:37.082099+00:00
---

# Create Harbor registry instances  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create Harbor registry instances Stay organized with collections  Save and categorize content based on your preferences. 

Use the Google Distributed Cloud (GDC) air-gapped Managed Harbor Service (MHS) to create a Harbor registry instance in each project. A Harbor registry instance serves as a central repository for storing and managing container images in a cloud-native environment. It extends the capabilities of the open-source Docker distribution. The following restrictions apply:

  * You can create a maximum of one instance per project.
  * Instances are isolated and don't share any data or compute resources.



## Before you begin

If you are responsible for creating Harbor registry instances, contact your IAM Project Admin to request the **Harbor Instance Admin** (`harbor-instance-admin`) role, which lets you get, list, watch, create, update, patch, and delete Harbor instances, backup repositories, backup plans, backups, and restores within a project namespace. This role includes the required permissions to provision new Harbor instances.

## Create a Harbor registry instance

Create a Harbor registry instance in the GDC console or the gdcloud CLI.

###  Console 

In the GDC console, follow these steps:

  1. In the navigation menu, in the **CI/CD** section, click **Harbor Container Registry**.
  2. Click **Create Instance**.
  3. In the **Instance name** field, enter a name for the instance.
  4. Optional: In the **Projects** section, to create a default project for this Harbor instance, click the **Create a default project when creating this instance** toggle to the on position, and then do the following: 
     1. In the **Project Name** field, enter a project name.
  5. Read the **Harbor managed Terms of Service** , and then select the checkbox if you accept the terms.
  6. Click **Create**. The **Status** shows **In progress** , and the **Name** shows an external link containing the name of your newly created Harbor instance.
  7. After the instance is created and the **Status** shows **Ready** , click the external link on the page to visit the web UI of the Harbor instance.



###  gdcloud 

Create the Harbor registry instance:
    
    
    gdcloud harbor instances create INSTANCE \
      --project=PROJECT
    

Replace the following:

  * `INSTANCE`: the name of the instance
  * `PROJECT`: the name of the GDC project in which to create the instance



## Cluster node trust for Harbor registry instances

When a Harbor registry instance is ready, GDC automatically configures the nodes of shared and standard Kubernetes clusters in your organization to trust the instance's TLS certificate, which is issued by your organization's trusted root certificate authority (CA). To pull images from the instance, you don't need to install the root CA or change the container runtime configuration on cluster nodes.

The automatic configuration has the following behavior:

  * **Node update timing:** GDC adds the instance to the private registry configuration of each cluster, and then updates every node in the cluster. A node can pull images from the instance only after the update finishes on that node, which can take up to 60 minutes across all nodes.
  * **New and cross-zone clusters:** GDC also configures clusters that you create after the instance is ready and clusters in other zones of your organization.
  * **Trusted hostname:** Nodes trust only the instance hostname, which is the instance URL without the `https://` prefix, such as `harbor-1-my-project.org-1.zone1.google.gdc.test`. You can find the instance URL in the GDC console instance link or in the `status.url` field of the `gdcloud harbor instances describe` command output. Use the instance hostname in your image references, such as `INSTANCE_HOSTNAME/HARBOR_PROJECT/IMAGE:TAG`, where `HARBOR_PROJECT` is the Harbor project that stores the image.
  * **Workstation Docker client:** Automatic trust applies only to cluster nodes. To push or pull images with Docker from your workstation, you must configure your local Docker client to trust the root CA. For more information, see [Configure Docker to trust the Harbor root CA](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/configure-docker-trust).



If cluster nodes don't trust your instance, see Troubleshoot certificate errors when pulling images.

## Troubleshoot certificate errors when pulling images

If the cluster nodes don't trust the certificate for the hostname in an image reference, pods can't pull the image. The pods show the `ErrImagePull` or `ImagePullBackOff` status, and the pod events show an error similar to the following:
    
    
    failed to pull and unpack image "INSTANCE_HOSTNAME/HARBOR_PROJECT/IMAGE:TAG": ... x509: certificate signed by unknown authority
    

**Caution:** GDC manages cluster node trust automatically. Don't use manual workarounds to bypass `x509` errors, because unsupported changes weaken TLS verification and node updates overwrite them. For example, if a pod fails to pull an image, don't modify the node container runtime, install CA certificates with `DaemonSet` workloads or privileged pods, configure an insecure registry, or pull images by IP address or over HTTP.

To troubleshoot certificate errors, you need the following:

  * The **Harbor Instance Viewer** (`harbor-instance-viewer`) or **Harbor Instance Admin** (`harbor-instance-admin`) role in the GDC project that contains the instance.
  * A role that lets you view pod events and delete pods on the affected cluster: 
    * For a shared cluster, the **Namespace Admin** (`namespace-admin`) role in the project namespace of the workload.
    * For a standard cluster, the **Cluster Developer** (`cluster-developer`) role in the project that contains the cluster.
  * A kubeconfig file for the affected Kubernetes cluster: 
    * For a shared cluster, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-cluster-kubeconfig).
    * For a standard cluster, see [Manage access to standard clusters](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/standard-clusters#manage-access-within-cluster).



To resolve this issue, complete the following steps:

  1. View the pod events and the node that runs the pod:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG \
           -n NAMESPACE describe pod POD_NAME
         

Replace the following:

     * `CLUSTER_KUBECONFIG`: the path to the kubeconfig file of the affected Kubernetes cluster.
     * `NAMESPACE`: the namespace of the pod. For a shared cluster, this is a project namespace.
     * `POD_NAME`: the name of the pod.

In the output, the `Node` field shows the node that runs the pod, and the `Events` section shows the error message and the image reference.

  2. Verify that the instance is ready and has no error codes:

     * In the GDC console, verify that the **Status** of the instance shows **Ready**. Even if the **Status** shows **Ready** , use the gdcloud CLI to check for error codes.
     * Use the gdcloud CLI to check the instance status and any error codes:
           
           gdcloud harbor instances describe INSTANCE \
             --project=PROJECT
           

Replace the following:

       * `INSTANCE`: the name of the Harbor registry instance.
       * `PROJECT`: the name of the GDC project that contains the instance.

In the output, verify that the condition with `type: Ready` in the `status.conditions` list has `status: "True"`. The output is similar to the following:
    
    # Several lines of code are omitted here.
    status:
      conditions:
      - message: HarborInstance reconciled
        reason: Reconciled
        status: "True"
        type: Ready
      # Several lines of code are omitted here.
      url: https://harbor-1-my-project.org-1.zone1.google.gdc.test
    

If the **Status** stays **In progress** or shows **Unknown** or **Error** , or the `Ready` condition doesn't have `status: "True"`, contact your infrastructure operator (IO). If the `status` section of the `gdcloud harbor instances describe` output contains an `errorStatus` field with error codes, such as `HAAS0008`, contact your IO even if the `Ready` condition is `True`. Include the error codes and messages.

  3. Verify that the image reference in your workload uses the instance hostname exactly as it appears in the instance URL, without the `https://` prefix. Nodes don't trust other names for the instance, such as an IP address. If the image reference uses a different name, update the reference to use the instance hostname, and then redeploy the workload.

  4. If less than 60 minutes have passed since the instance showed the **Ready** status or since you created the cluster, whichever is later, wait for GDC to finish updating the cluster nodes:

     * **Partial node updates:** If image pulls succeed on some nodes and fail on others, the update is still in progress.
     * **Backups and restores:** Node updates wait while a backup or restore of the instance is in progress. Start the 60-minute period after the backup or restore finishes.
     * **New or cross-zone clusters:** For clusters that you create after the instance is ready, and for clusters in a different zone from the instance, the **Ready** status of the instance doesn't show whether the cluster nodes are updated.
  5. After the node update finishes, verify that your workload can pull the image. Kubernetes retries failed image pulls automatically. To retry immediately, delete the failing pod so that its controller, such as a `Deployment`, recreates it:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG \
           -n NAMESPACE delete pod POD_NAME
         

If no controller manages the pod, recreate the pod. To confirm that the issue is resolved, verify that the new pod shows the `Running` status instead of `ErrImagePull` or `ImagePullBackOff`:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG \
           -n NAMESPACE get pods
         

  6. If the error continues for more than 60 minutes after the instance showed the **Ready** status or after you created the cluster, whichever is later, contact your IO. Provide the following information:

     * The organization and the zone of the instance and of the affected cluster
     * The instance name and the GDC project that contains the instance
     * The name of the affected Kubernetes cluster, whether it's a shared or standard cluster, and, for a standard cluster, the project that contains the cluster
     * The full image reference and the full error message from the pod events
     * The names of the nodes where image pulls fail, and whether image pulls succeed on other nodes
     * When the instance showed the **Ready** status, when you created the cluster, and whether a backup or restore of the instance was in progress
     * The `status` section of the `gdcloud harbor instances describe` output, including any `errorStatus` error codes



## What's next

After your Harbor registry instance is ready, you can create projects to host your image collections or manage your existing instances:

  * [Create Harbor projects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-projects)
  * [Manage Harbor registry instances](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/manage-harbor-instances)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 

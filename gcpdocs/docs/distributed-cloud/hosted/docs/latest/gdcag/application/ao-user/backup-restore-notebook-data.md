---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data/
title: Create a backup and restore notebook data \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:07:24.807143+00:00
---

# Create a backup and restore notebook data  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data/

[ Skip to main content ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data/)
  * [Deutsch](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data/?hl=de)
  * [Español](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data/?hl=es-419)
  * [Français](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data/?hl=id)
  * [Italiano](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data/?hl=it)
  * [Português](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data/?hl=ja)
  * [한국어](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fdistributed-cloud%2Fhosted%2Fdocs%2Flatest%2Fgdcag%2Fapplication%2Fao-user%2Fbackup-restore-notebook-data%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/distributed-cloud-color.svg) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data/#before-you-begin)
  * [Create a backup and restore JupyterLab instance data](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data/#backup-and-restore-data)
  * [Copy restored data to a new JupyterLab instance](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data/#copy-restored-data)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)


Was this helpful?
Send feedback 
#  Create a backup and restore notebook data Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data/#before-you-begin)
  * [Create a backup and restore JupyterLab instance data](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data/#backup-and-restore-data)
  * [Copy restored data to a new JupyterLab instance](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data/#copy-restored-data)


Google Distributed Cloud (GDC) air-gapped lets you create backups and restore data from the home directory of your JupyterLab instances.
This page describes creating and restoring backups of Vertex AI Workbench notebook data. If you are new to Vertex AI, [learn more about Vertex AI Workbench](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-workbench-intro).
## Before you begin
To get the permissions that you need to copy restored data, ask your IAM Org Admin to grant you the User Cluster Developer (`user-cluster-developer`) role.
## Create a backup and restore JupyterLab instance data
Define protected applications to create a backup of the home directory of an individual JupyterLab instance or the home directories of all JupyterLab instances in a project at once.
Create a `ProtectedApplication` custom resource in the cluster where you want to schedule backups. Backup and restore plans use protected applications to select resources. For information about creating protected applications, see [Protected application strategies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/protected-application-strategies).
The `ProtectedApplication` custom resource contains the following fields:  
| **Field**  | **Description**  |  
| --- | --- |  
| `resourceSelection`  | The way in which the `ProtectedApplication` object selects resources for backups or restorations.  |  
|   | `type`  | The method to select resources. A `Selector` type indicates that resources with matching labels must be selected.  |  
|   | `selector`  | The selection rules. This field contains the following sub-fields:  |  
|   |   | `matchLabels`  | The labels that the `ProtectedApplication` object uses to match resources. This field contains the following sub-fields:  |  
|   |   |   | `app.kubernetes.io/part-of`  | The name of a higher level application this one is part of. Select Vertex AI Workbench as the high-level application for JupyterLab instances.  |  
|   |   |   | `app.kubernetes.io/component`  | The component within the architecture. Select resources from Vertex AI Workbench that provide storage for JupyterLab instances.  |  
|   |   |   | `app.kubernetes.io/instance`  | A unique name identifying the instance of an application. Narrow the scope to select a JupyterLab instance. The value is the same as the name of the JupyterLab instance on the GDC console.  |  
Use the `ProtectedApplication` custom resource to select the storage of a single JupyterLab instance or all JupyterLab instances in a project, as in the following examples:
  * **Select the storage of a single JupyterLab instance** :
The following example shows a `ProtectedApplication` custom resource that selects the storage for a JupyterLab instance named `my-instance-name` in the `my-project` namespace:

```
apiVersion: gkebackup.gke.io/v1
kind: ProtectedApplication
metadata:
  name: my-protected-application
  namespace: my-project
spec:
  resourceSelection:
    type: Selector
    selector:
      matchLabels:
        app.kubernetes.io/part-of: vtxwb
        app.kubernetes.io/component: storage
        app.kubernetes.io/instance: my-instance-name

```

  * **Select the storage of all JupyterLab instances** :
The following example shows a `ProtectedApplication` custom resource that selects the storage for all JupyterLab instances in the `my-project` namespace:

```
apiVersion: gkebackup.gke.io/v1
kind: ProtectedApplication
metadata:
  name: my-protected-application
  namespace: my-project
spec:
  resourceSelection:
    type: Selector
    selector:
      matchLabels:
        app.kubernetes.io/part-of: vtxwb
        app.kubernetes.io/component: storage

```

This example doesn't contain the `app.kubernetes.io/instance` label because it selects all JupyterLab instances.


To create a backup and restore data from a JupyterLab instance, [plan a set of backups](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/plan-backups) and [plan a set of restores](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/plan-restores) using the `ProtectedApplication` custom resource you defined.
## Copy restored data to a new JupyterLab instance
Follow these steps to copy restored data from the `PersistentVolumeClaim` resource of a JupyterLab instance to a new JupyterLab instance:
  1. [Meet the prerequisites](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data/#before-you-begin).
  2. [Create a JupyterLab notebook](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-workbench#create-notebook) associated with a JupyterLab instance to copy restored data.
  3. Get the pod name of the JupyterLab instance where you created the notebook:

```
kubectl get pods -l notebook-name=INSTANCE_NAME -n PROJECT_NAMESPACE

```

Replace the following:
     * `INSTANCE_NAME`: the name of the JupyterLab instance you configured.
     * `PROJECT_NAMESPACE`: the project namespace where you created the JupyterLab instance.
  4. Get the name of the image that the JupyterLab instance is running:

```
kubectl get pods POD_NAME -n PROJECT_NAMESPACE -o jsonpath="{.spec.containers[0].image}"

```

Replace the following:
     * `POD_NAME`: the pod name of the JupyterLab instance.
     * `PROJECT_NAMESPACE`: the project namespace where you created the JupyterLab instance.
  5. Find the name of the `PersistentVolumeClaim` resource that was restored:

```
kubectl get pvc -l app.kubernetes.io/part-of=vtxwb,app.kubernetes.io/component=storage,app.kubernetes.io/instance=RESTORED_INSTANCE_NAME -n PROJECT_NAMESPACE

```

Replace the following:
     * `RESTORED_INSTANCE_NAME`: the name of the JupyterLab instance that you restored.
     * `PROJECT_NAMESPACE`: the project namespace where you created the JupyterLab instance.
  6. Create a YAML file named `vtxwb-data.yaml` with the following content:

```
apiVersion: v1
kind: Pod
metadata:
  name: vtxwb-data
  namespace: PROJECT_NAMESPACE
  labels:
    aiplatform.gdc.goog/service-type: workbench
spec:
  containers:
  - args:
    - sleep infinity
    command:
    - bash
    - -c
    image: IMAGE_NAME
    imagePullPolicy: IfNotPresent
    name: vtxwb-data
    resources:
      limits:
        cpu: "1"
        memory: 1Gi
      requests:
        cpu: "1"
        memory: 1Gi
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: File
    volumeMounts:
    - mountPath: /home/jovyan
      name: restore-data
    workingDir: /home/jovyan
  volumes:
  - name: restore-data
    persistentVolumeClaim:
      claimName: RESTORED_PVC_NAME

```

Replace the following:
     * `PROJECT_NAMESPACE`: the project namespace where you created the JupyterLab instance.
     * `IMAGE_NAME`: the name of the container image that the JupyterLab instance is running.
     * `RESTORED_PVC_NAME`: the name of the restored `PersistentVolumeClaim` resource.
  7. Create a new pod for your restored `PersistentVolumeClaim` resource:

```
kubectl apply -f ./vtxwb-data --kubeconfig KUBECONFIG_PATH

```

Replace `KUBECONFIG_PATH` with the path of the kubeconfig file in the cluster.
  8. Wait for the `vtxwb-data` pod to reach the `RUNNING` state.
  9. Copy your restored data to a new JupyterLab instance:

```
kubectl cp PROJECT_NAMESPACE/vtxwb-data:/home/jovyan ./restore --kubeconfig KUBECONFIG_PATH

kubectl cp ./restore PROJECT_NAMESPACE/POD_NAME:/home/jovyan/restore --kubeconfig KUBECONFIG_PATH

rm ./restore

```

Replace the following:
     * `PROJECT_NAMESPACE`: the project namespace where you created the JupyterLab instance.
     * `KUBECONFIG_PATH`: the path of the kubeconfig file in the cluster.
     * `POD_NAME`: the pod name of the JupyterLab instance.
After copying the data, your restored data is available in the `/home/jovyan/restore` directory.
  10. Delete the pod that you created to access your restored data:

```
kubectl delete pod vtxwb-data -n my-namespace` --kubeconfig KUBECONFIG_PATH

```

Replace `KUBECONFIG_PATH` with the path of the kubeconfig file in the cluster.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

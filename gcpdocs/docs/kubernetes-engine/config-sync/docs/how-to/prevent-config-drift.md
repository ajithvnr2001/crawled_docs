---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/prevent-config-drift/
title: Prevent config drift \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T02:29:31.659940+00:00
---

# Prevent config drift  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/prevent-config-drift/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Prevent config drift Stay organized with collections  Save and categorize content based on your preferences. 

Config Sync lets you prevent configuration drift so that cluster resources stay aligned with your central source of truth. By default, built-in self-healing in Config Sync automatically detects and reverts drift with minimal impact on cluster performance.

When your environment requires blocking conflicting changes before the cluster applies them, you can enable the Config Sync admission webhook for drift prevention. Because this webhook increases memory overhead and can cause out-of-memory (OOM) errors, rely on built-in self-healing for most use cases.

## Why drift prevention isn't recommended

The admission webhook requires Config Sync to load the Kubernetes OpenAPI schema to validate requests. In clusters with many resources or CustomResourceDefinitions, this schema processing can exceed memory limits, leading to component failures. For most use cases, built-in self-healing in Config Sync provides drift protection without the stability risks of the webhook. You can't disable built-in self-healing.

When enabled, drift prevention protects `RootSync` objects by default. You can configure the feature to protect `RepoSync` objects. To use drift prevention, you must enable the `RootSync` and `RepoSync` APIs. For more information, see [RootSync and RepoSync fields](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields).

**Note:** Both self-healing and drift prevention use [server-side apply](https://kubernetes.io/docs/reference/using-api/server-side-apply/), which means they only prevent or revert changes to fields explicitly specified in the source of truth. Config Sync allows unspecified fields to drift because many Kubernetes controllers update metadata and spec fields at runtime, not just status fields.

## Before you begin

If you previously installed the Google Cloud CLI, get the latest version by running the `gcloud components update` command.

## Enable drift prevention

You can enable drift prevention by using the gcloud CLI. You can't enable drift prevention in the Google Cloud console.

To enable drift prevention, complete the following steps:

  1. Update your [apply spec manifest](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/gcloud-apply-fields) to set the `spec.configSync.preventDrift` field to `true`:
         
         applySpecVersion: 1
         spec:
           configSync:
             enabled: true
             ... existing content ...
             **preventDrift : true**
         

  2. Apply the updated manifest:
         
         gcloud beta container fleet config-management apply \
             --membership=MEMBERSHIP_NAME \
             --config=MANIFEST_NAME  \
             --project=PROJECT_ID
         

Replace the following:

     * `MEMBERSHIP_NAME`: the fleet membership name that you chose when you registered your cluster. Get the name with the `gcloud container fleet memberships list` command.
     * `MANIFEST_NAME`: the name of your apply spec manifest, usually `apply-spec.yaml`.
     * `PROJECT_ID`: your project ID.
  3. Wait until the Config Sync `ValidateWebhookConfiguration` object is created by the ConfigManagement Operator:
         
         kubectl get validatingwebhookconfiguration admission-webhook.configsync.gke.io
         

You should see output similar to the following example:
         
         NAME                                  WEBHOOKS   AGE
         admission-webhook.configsync.gke.io   0          2m15s
         

  4. Commit a new change to the source of truth to be synced so that the `root-reconciler` Deployment can add webhooks into the Config Sync ValidatingWebhookConfiguration object. An alternative is to delete the `root-reconcilier` Deployment to trigger a reconciliation. The new `root-reconciler` Deployment would update the Config Sync ValidatingWebhookConfiguration object.

  5. Wait until the webhook server is ready. The Config Sync admission webhook Deployment log should include `serving webhook server`. This can take several minutes.
         
         kubectl logs -n config-management-system -l app=admission-webhook --tail=-1 | grep "serving webhook server"
         

You should see output similar to the following example:
         
         I1201 18:05:41.805531       1 deleg.go:130] controller-runtime/webhook "level"=0 "msg"="serving webhook server"  "host"="" "port"=10250
         I1201 18:07:04.626199       1 deleg.go:130] controller-runtime/webhook "level"=0 "msg"="serving webhook server"  "host"="" "port"=10250
         




## Disable drift prevention

When you disable drift prevention, Config Sync deletes all the Config Sync admission webhook resources. Since the Config Sync `ValidatingWebhookConfiguration` object no longer exists, the Config Sync reconcilers no longer generate the webhook configs for managed resources.

To disable drift prevention, complete the following steps:

  1. Update your [apply spec manifest](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/gcloud-apply-fields) to set the `spec.configSync.preventDrift` field to `false`:
         
         applySpecVersion: 1
         spec:
           configSync:
             enabled: false
             ... existing content ...
             **preventDrift : false**
         

  2. Apply the updated manifest:
         
         gcloud beta container fleet config-management apply \
             --membership=MEMBERSHIP_NAME \
             --config=MANIFEST_NAME  \
             --project=PROJECT_ID
         

Replace the following:

     * `MEMBERSHIP_NAME`: the fleet membership name that you chose when you registered your cluster. Get the name with the `gcloud container fleet memberships list` command.
     * `MANIFEST_NAME`: the name of your apply spec manifest, usually `apply-spec.yaml`.
     * `PROJECT_ID`: your project ID.



## Enable the admission webhook in namespace-scoped sources

Namespace-scoped sources of truth are not fully protected by the webhook. The Config Sync reconciler for each namespace source does not have permission to read or update the `ValidatingWebhookConfiguration` objects at the cluster level.

This lack of permission results in an error for the namespace reconcilers logs similar to the following example:
    
    
    Failed to update admission webhook: KNV2013: applying changes to
    admission webhook: Insufficient permission. To fix, make sure the reconciler has
    sufficient permissions.:
    validatingwebhookconfigurations.admissionregistration.k8s.io "admission-
    webhook.configsync.gke.io" is forbidden: User "system:serviceaccount:config-
    management-system:ns-reconciler-NAMESPACE" cannot update resource
    "validatingwebhookconfigurations" in API group "admissionregistration.k8s.io" at
    the cluster scope
    

You can ignore this error if you don't want to use the webhook protection for your namespace-scoped source of truth. However, if you want to use the webhook, grant permission to the reconciler for each namespace-scoped source of truth after you have [configured syncing from more than one source of truth](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories). You might not need to perform these steps if a RoleBinding for the `ns-reconciler-NAMESPACE` already exists with ClusterRole `cluster-admin` permissions.

**Caution:** Giving permission to read or update the ValidatingWebhookConfiguration objects to a namespace-scoped source of truth means that the namespace-scoped source owners can make changes to the Config Sync admission webhook configs in the cluster.

  1. In the root source of truth, declare a new ClusterRole configuration that grants permission to the Config Sync admission webhook. This ClusterRole only needs to be defined once per cluster:
         
         # ROOT_SOURCE/cluster-roles/webhook-role.yaml
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRole
         metadata:
           name: admission-webhook-role
         rules:
         - apiGroups: ["admissionregistration.k8s.io"]
           resources: ["validatingwebhookconfigurations"]
           resourceNames: ["admission-webhook.configsync.gke.io"]
           verbs: ["get", "update"]
         

  2. For each namespace-scoped source where the admission webhook permission needs to be granted, declare a ClusterRoleBinding configuration to grant access to the admission webhook:
         
         # ROOT_SOURCE/NAMESPACE/sync-webhook-rolebinding.yaml
         kind: ClusterRoleBinding
         apiVersion: rbac.authorization.k8s.io/v1
         metadata:
           name: syncs-webhook
         subjects:
         - kind: ServiceAccount
           name: ns-reconciler-NAMESPACE
           namespace: config-management-system
         roleRef:
           kind: ClusterRole
           name: admission-webhook-role
           apiGroup: rbac.authorization.k8s.io
         

Replace `NAMESPACE` with the namespace that you created your namespace-scoped source in.

  3. Commit the changes to the root source of truth, for example, if syncing from a Git repository:
         
         git add .
         git commit -m 'Providing namespace repository the permission to update the admission webhook.'
         git push
         
         

  4. To verify, use `kubectl get` to make sure the ClusterRole and ClusterRoleBinding have been created:
         
         kubectl get clusterrole admission-webhook-role
         kubectl get clusterrolebindings syncs-webhook
         




## What's next

  * Learn how to [troubleshoot the webhook](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/troubleshooting/webhook).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/migrate-hierarchy-controller/
title: Disable Hierarchy Controller \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T02:29:31.858321+00:00
---

# Disable Hierarchy Controller  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/migrate-hierarchy-controller/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Disable Hierarchy Controller Stay organized with collections  Save and categorize content based on your preferences. 

Disabling Hierarchy Controller on your clusters lets you upgrade Config Sync to newer supported versions. Because Hierarchy Controller is no longer available, Config Sync blocks upgrades if the component remains installed on a cluster.

## Before you begin

To determine how to disable Hierarchy Controller, inspect the [`kubectl` `ConfigManagement` object](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/configmanagement-fields) or [`gcloud` `apply spec` file](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/gcloud-apply-fields) and take an action that corresponds to the value in the following fields:

  * `hierarchyController.enablePodTreeLabels`: if `true`, and you previously enabled hierarchical observability, don't proceed with the steps in this document. Instead, contact [Cloud Customer Care](https://docs.cloud.google.com/support/docs) for help removing Hierarchy Controller.
  * `hierarchyController.enabled`: if `true`, follow the instructions in Disable Hierarchy Controller.



## Disable Hierarchy Controller

When you disable Hierarchy Controller, Config Sync deletes the Hierarchy Controller components in your cluster but doesn't delete the Hierarchy Controller CustomResourceDefinitions. You must manually remove those CustomResourceDefinitions by using the `kubectl` command-line tool:

  * `HierarchyConfiguration`
  * `HNCConfiguration`
  * `SubnamespaceAnchor`
  * `HierarchicalResourceQuota`



To remove the Hierarchy Controller fields, review the instructions for the method that you used to install Hierarchy Controller:

###  gcloud 

Remove the `hierarchyController` block from your [Google Cloud CLI `apply spec` file](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/gcloud-apply-fields).

### Terraform

Remove the `hierarchyController` block from your [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_feature_membership#argument-reference).

###  Config Connector 

Set Hierarchy Controller fields to `false` in the [`GKEHubFeatureMembership`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/gkehub/gkehubfeaturemembership) resource.

**Important:** Don't remove the Hierarchy Controller fields from the `GKEHubFeatureMembership` resource. Removing the fields doesn't disable Hierarchy Controller and causes the fields to become [externally-managed](https://docs.cloud.google.com/config-connector/docs/concepts/managing-fields-externally) instead of managed by Config Connector.

### kubectl

Remove the `hierarchyController` block from the [`ConfigManagement` object](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/configmanagement-fields).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

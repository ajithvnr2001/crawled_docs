---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-overview/
title: Upgrade overview \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T17:00:04.887780+00:00
---

# Upgrade overview  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Upgrade overview Stay organized with collections  Save and categorize content based on your preferences. 

Planning a cluster upgrade for Google Distributed Cloud software only for VMware helps you determine the required upgrade order, choose compatible management tools, and minimize workload disruption in a multi-cluster environment. For a pre-upgrade readiness checklist, see [Upgrade best practices](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-best-practices).

## How versions, order, and tools impact upgrades

The order in which you upgrade clusters, the tools you use, and the checks you must perform vary significantly depending on the following:

  * The version you start from
  * The version you upgrade to
  * Whether you upgrade _from_ an advanced or non-advanced cluster
  * Whether you upgrade _to_ an advanced or non-advanced cluster
  * Whether Controlplane V2 is enabled on the user cluster



Depending on the version you start from, the order in which you upgrade clusters, the tools you use to update, the versions of clusters, and what you can and can't do varies significantly.

## Check if a cluster is advanced or non-advanced

To check if your clusters are advanced or non-advanced, identify the version you are using:

  * If your clusters use version 1.30 or earlier, they are non-advanced clusters.
  * If your clusters use version 1.33 and you did not explicitly opt-out of advanced clusters, they are advanced clusters.
  * If your clusters use version 1.34 and later, they are advanced clusters.



If your clusters use versions 1.31 and 1.32, check whether a cluster is advanced or not by checking cluster custom resources with `kubectl`:

  1. In your admin cluster kubeconfig, check the `enableAdvancedCluster` spec field for the admin cluster:
         
         kubectl get onpremadminclusters -A \
             -o custom-columns=NAME:.metadata.name,VERSION:.spec.gkeOnPremVersion,ADVANCED:.spec.enableAdvancedCluster \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

Replace `ADMIN_CLUSTER_KUBECONFIG` with the path to your admin cluster kubeconfig file.

  2. In your admin cluster kubeconfig, check the `enableAdvancedCluster` spec field for the user clusters:
         
         kubectl get onpremuserclusters -A \
             -o custom-columns=NAME:.metadata.name,VERSION:.spec.gkeOnPremVersion,ADVANCED:.spec.enableAdvancedCluster \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         




When advanced clusters are enabled, the output is similar to the following:
    
    
    NAME              VERSION           ADVANCED
    gke-admin-abc12   1.32.0-gke.1085   true
    

If `ADVANCED` is `true`, it is an advanced cluster. For version 1.32 or earlier, `ADVANCED` might display as `<none>`.

## High-level upgrade process

The following sections describe the overall upgrade process when upgrading clusters, depending on the type of cluster you are upgrading from and to.

Before you begin an upgrade, review detailed information about how versions impact upgrades. See [Upgrade version rules](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-version-rules) for a detailed list of dependencies by version and information about skipping versions and version skew rules.

### Advanced versus non-advanced clusters

There are two types of clusters: advanced and non-advanced. All clusters created in versions 1.33 or later are advanced clusters. Advanced clusters use improved architectures that provide greater flexibility and scalability.

After you upgrade your clusters to advanced clusters, you always use advanced clusters and use the advanced cluster upgrade process. Whether a cluster is advanced or non-advanced only matters when you upgrade from a version before 1.33.

Advanced clusters use a consolidated Google Distributed Cloud architecture by using Google Distributed Cloud software only for bare metal as the underlying framework for Google Distributed Cloud software only for VMware. You might see references to "bare metal" in node labels, API resources, and system tags.

The advanced clusters feature implements a cluster architecture that better aligns Google Distributed Cloud software only for VMware with the rest of the Google Distributed Cloud products. A cluster that has advanced clusters enabled has a shared platform with other Google Distributed Cloud clusters. This shared platform uses the same controllers and agents, which increases reliability and can help Google provide better support. There's also improved performance for cluster operations when advanced clusters is enabled.

The new architecture brings a consistent experience and implementation with all other Google Distributed Cloud offerings. For details on the features available for advanced clusters versus non-advanced clusters, see [Advanced cluster feature support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster#adv-clusters-feature-support).

### Upgrade from advanced clusters to advanced clusters (current versions, starting from 1.31)

In version 1.32 and later, when upgrading from one advanced cluster to another, you can perform both patch version upgrades and sequential minor version upgrades. In version 1.31 Preview, you can perform only patch version upgrades within version 1.31.

To perform this upgrade, you can use the `gkectl` CLI, the Google Cloud CLI, the Google Cloud console, or Terraform (depending on the version).

To upgrade from an advanced cluster to an advanced cluster, you must follow this order:

  1. Upgrade the admin workstation, if applicable.
  2. Use `gkectl diagnose cluster` to verify that your admin cluster is healthy. Resolve any issues.
  3. Upgrade the admin cluster.
  4. Use `gkectl diagnose cluster` to verify that the upgrade was successful and that your user clusters are healthy. Resolve any issues.
  5. Upgrade the user clusters, one at a time. You can upgrade the user cluster control plane and node pools together or separately. For more information, see [Upgrade node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-node-pools).
  6. Verify that the upgrade was successful by using `gkectl diagnose cluster`.



When all node pools in a user cluster are at the same version as the user cluster's control plane, the user cluster is upgraded and the upgrade is complete.

The control plane for the user cluster runs on the user cluster itself and is upgraded during the user cluster upgrade. The admin cluster control plane nodes are upgraded during the admin cluster upgrade.

For more information on how to diagnose clusters using `gkectl diagnose cluster`, see [Diagnose clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose).

For information on how to perform upgrades from advanced clusters to advanced clusters, see [Upgrade a cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading).

### Upgrade from non-advanced clusters to advanced clusters

Upgrades from a non-advanced cluster to an advanced cluster only occur for versions 1.31, 1.32, 1.33, and 1.34. For more information about upgrading from non-advanced clusters to advanced clusters in these versions, see [Upgrade version rules](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-version-rules).

To upgrade from a non-advanced cluster to an advanced cluster, you must use `gkectl` with the same version as the target version (for example, if you are upgrading to version 1.32.0, you must use `gkectl` version 1.32.0) and follow this order:

  1. Upgrade the admin workstation and artifacts.
  2. Use `gkectl diagnose cluster` to verify that your admin cluster is healthy. Resolve any issues.
  3. Upgrade the admin cluster.
  4. Use `gkectl diagnose cluster` to verify that the upgrade was successful and that your user clusters are healthy. Resolve any issues.
  5. Upgrade the user cluster.
  6. Verify that the upgrade was successful by using `gkectl diagnose cluster`.



For more information on how to diagnose clusters using `gkectl diagnose cluster`, see [Diagnose clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose).

For more information on how to perform an upgrade from a non-advanced cluster to an advanced cluster see [Update or upgrade from a non-advanced cluster to an advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster).

### Upgrade from non-advanced cluster to non-advanced cluster

You can upgrade from non-advanced clusters to another non-advanced cluster for version 1.33 and earlier. For details about versions that allow upgrades from a non-advanced cluster to another non-advanced cluster, see [Upgrade version rules](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-version-rules).

The order in which you upgrade non-advanced clusters depends on the target version:

  * For target versions 1.31, 1.32, and 1.33, you must upgrade the admin cluster before you upgrade the user clusters.
  * For target versions 1.30 and earlier, you must upgrade all user clusters before you upgrade the admin cluster.



#### Upgrade to version 1.31, 1.32, or 1.33

To upgrade to version 1.31, 1.32, or 1.33 while keeping your clusters non-advanced, you must follow this order:

  1. Upgrade the admin workstation and prepare the bundle artifacts.
  2. Use `gkectl diagnose cluster` to verify that your admin cluster is healthy. Resolve any issues.
  3. Upgrade the admin cluster.
  4. Use `gkectl diagnose cluster` to verify that the upgrade was successful and that your user clusters are healthy. Resolve any issues.
  5. Upgrade the user clusters, one at a time.
  6. Verify that the upgrade was successful by using `gkectl diagnose cluster`.



#### Upgrade to version 1.30 or earlier

To upgrade to version 1.30 or earlier, you must follow this order:

  1. Upgrade the admin workstation and prepare the bundle artifacts.
  2. Use `gkectl diagnose cluster` to verify that your user clusters are healthy. Resolve any issues.
  3. Upgrade all user clusters, one at a time.
  4. Use `gkectl diagnose cluster` to verify that the upgrade was successful and that your admin cluster is healthy. Resolve any issues.
  5. Upgrade the admin cluster.
  6. Verify that the upgrade was successful by using `gkectl diagnose cluster`.



For more information on how to diagnose clusters using `gkectl diagnose cluster`, see [Diagnose clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose).

For more information on how to perform an upgrade from a non-advanced cluster to a non-advanced cluster, see [Upgrade and maintain non-advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-maintain-non-advanced-cluster).

## Cluster upgrades

You always upgrade admin clusters one at a time.

When you upgrade user clusters, you can upgrade the whole user cluster (the control plane and all node pools in the cluster at the same time), or you can upgrade the user cluster's control plane and leave the node pools at the current version. Which approach you take depends on several factors, such as:

  * The environment (production or non-production) that the cluster is in.
  * The length of your maintenance window.
  * The version of the user cluster.



For example, in a development environment, you might want to keep the process straightforward and upgrade both the user cluster's control plane and all node pools. But in a production environment with a short maintenance window, you might want to upgrade only the control plane because that takes less time and with high availability (HA) control planes, the control plane upgrade shouldn't disrupt user workloads.

### Choose a tool to upgrade clusters

The tool that you use depends on how and what you plan to upgrade.

For admin clusters, you must use `gkectl` to upgrade.

For user clusters, you can use one of the following tools to upgrade clusters:

  * The `gkectl` command-line tool (required for upgrades from non-advanced clusters to advanced clusters)
  * Terraform, if you created the user cluster using Terraform
  * Google Cloud console
  * Google Cloud CLI



The following table lists which tools support which use cases.

Upgrade use case | `gkectl` | gcloud CLI | console | Terraform | Notes & restrictions  
---|---|---|---|---|---  
Upgrade admin clusters _(any path)_ | _Yes_ | No | No | No | Admin clusters always require `gkectl`.  
Upgrade non-advanced to advanced clusters _(conversion)_ | _Yes_ | No | No | No | `gkectl` version must match target version; zero version skew permitted between control plane (CP) and node pools.  
Upgrade non-advanced to non-advanced clusters _(legacy)_ | _Yes_ | No | No | No | Only available in 1.33 and earlier (opt-out path); API clients not supported.  
Upgrade user clusters: Advanced to advanced | _Yes_ | _Yes_ | _Yes_ | _Yes_ 1 | Standard version skew rules apply.  
Upgrade whole user cluster _(CP and node pools together)_ | _Yes_ | _Yes_ | _Yes_ | _Yes_ 1 | Supported across all tools for advanced user clusters.  
Upgrade user cluster control plane separately _(CP only)_ | _Yes_ | _Yes_ | No | _Yes_ 1 | console does not support upgrading only the control plane.  
Selectively upgrade node pools after CP upgrade | _Yes_ | _Yes_ | No | _Yes_ 1 | console does not support individual node pool upgrades.  
Upgrade CP and one or more node pools at the same time | _Yes_ | No | No | No | Only `gkectl` supports partial concurrent CP + node pool version upgrades.  
  
1 Terraform Requirement: You can use Terraform for user cluster upgrades only if the user cluster was originally created and managed using Terraform.

To get information about clusters you created with `gkectl` using the console or the gcloud CLI, [enroll the cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster#get_cluster_information) in the GKE On-Prem API.

## What's next

Review [Upgrade version rules](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-version-rules) to understand how versions impact upgrades and to find the version rules for the version you have and the version you are upgrading to.

Review [Upgrade best practices](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-best-practices) and create a plan for upgrading your clusters.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 

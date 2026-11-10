---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-version-rules/
title: Upgrade version rules \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T05:49:34.952746+00:00
---

# Upgrade version rules  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-version-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Upgrade version rules Stay organized with collections  Save and categorize content based on your preferences. 

Understanding how your current version and target version affect your [cluster upgrade](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-overview) helps you verify version skew, upgrade order, and OS requirements before you begin.

## Version-specific upgrade information

The following table describes version-specific upgrade information. Following the table, you can find details about specific releases. Versions are ordered from newest to oldest. Find the version you are upgrading _to_ for the specific details and rules that apply to your cluster.

Version | Upgrade first | Control plane (CP) versions | Worker node pool versions | Advanced cluster status | Legacy features supported? | Default & required OS images | Kubeception node upgrade behavior | Bundled `cert-manager`  
---|---|---|---|---|---|---|---|---  
1.36 | Admin cluster | 1.36, 1.35, 1.34 | 1.36, 1.35, 1.34 | Mandatory | None | `ubuntu_cgv2`, `cos_cgv2` | Unsupported | Bundled  
1.35 | Admin cluster | 1.35, 1.34, 1.33 | 1.35, 1.34, 1.33 | Mandatory | None | `ubuntu_cgv2`, `cos_cgv2` mandatory (cgroup v1 dropped) | Unsupported | Bundled  
1.34 | Admin cluster | 1.34, 1.33, 1.32 | 1.34, 1.33, 1.32 | Mandatory (no opt-out; non-advanced auto-converted) | None | `ubuntu_cgv2` (default), `cos_cgv2`, `ubuntu_containerd`, `cos` | Unsupported | Bundled  
1.33 | Admin cluster | 1.33, 1.32, 1.31 | 1.33, 1.32, 1.31 | Default (auto-conversion) (opt-out only for 1.32 to 1.33) | None | `ubuntu_cgv2` (default), `cos_cgv2`, `ubuntu_containerd`, `cos` | Unsupported | Bundled for advanced clusters  
1.32 | Admin cluster | 1.32, 1.31, 1.30 | 1.32, 1.31, 1.30 | GA (Upgrades supported; separate & skip node upgrades supported) | None | `ubuntu_cgv2` (default), `cos_cgv2`, `ubuntu_containerd`, `cos` | Unsupported (must migrate to Controlplane V2) | Bundled for advanced clusters  
1.31 | Admin cluster | 1.31, 1.30, 1.29 | 1.31, 1.30, 1.29 | Preview (no upgrade to 1.32; no separate or skip node upgrades) | Yes (Seesaw, F5, Kubeception, non-HA); migration to recommended features strongly advised; Dataplane V2 mandatory | `ubuntu_cgv2` (default), `cos_cgv2`, `ubuntu_containerd`, `cos` | Admin nodes upgraded with admin; user CP nodes upgraded with user cluster | Not bundled  
1.30 | User cluster | 1.30 | 1.30, 1.29, 1.28 | Not available | Yes (Seesaw, F5, Kubeception, non-HA); migration to recommended features strongly advised | `ubuntu_cgv2` (default), `cos_cgv2`, `ubuntu_containerd`, `cos` | CP & admin nodes upgraded during admin cluster upgrade | Not bundled  
1.29 | User cluster | 1.29, 1.30 | 1.29, 1.28, 1.16 | Not available | Yes (Seesaw, F5, Kubeception, non-HA) | `ubuntu_cgv2` (default), `cos_cgv2`, `ubuntu_containerd`, `cos` | CP & admin nodes upgraded during admin cluster upgrade | Not bundled  
1.28 | User cluster | 1.28, 1.29, 1.30 | 1.28, 1.16, 1.15 | Not available | Yes (Seesaw, F5, Kubeception, non-HA) | `ubuntu_containerd` (default), `cos`, `ubuntu_cgv2`, `cos_cgv2` | CP & admin nodes upgraded during admin cluster upgrade | Not bundled  
  
For all versions, you must upgrade load balancer node pool versions (node pools with `enableLoadBalancer: true`) at the same time and to the same version as the user cluster control plane.

## Upgrade information by release version

Find the section for the version you're upgrading _to_ for specific information you need to upgrade to that version.

### Release 1.36

**Upgrade first:** Admin cluster

**Version skew rules:**

  * Admin cluster at 1.36 can manage user clusters at 1.36, 1.35, and 1.34.
  * User cluster control plane versions: 1.36, 1.35, or 1.34.
  * Worker node pool versions: 1.36, 1.35, or 1.34.



**Advanced cluster status:** Advanced clusters are mandatory.

**Skip node upgrades:** Supported.

**Legacy features supported:** No. Blocks upgrade.

**Default and required OS images:** `ubuntu_cgv2`, `cos_cgv2`. Default `osImageType` for new configurations is `ubuntu_cgv2`.

**Kubeception node upgrade behavior:** Unsupported. Blocks upgrade.

**Upgrade tools:**

  * `gkectl`: Required for admin clusters. Supported versions are 1.36, 1.37, and 1.38.
  * Terraform: Supported if you created the user cluster using Terraform.
  * Google Cloud console: Supported for user cluster upgrades.
  * Google Cloud CLI: Supported for user cluster upgrades.



**Additional requirements:**

  * You can run admin cluster upgrades asynchronously with `gkectl upgrade admin --async`.



### Release 1.35

**Upgrade first:** Admin cluster

**Version skew rules:**

  * Admin cluster at 1.35 can manage user clusters at 1.35, 1.34, and 1.33.
  * User cluster control plane versions: 1.35, 1.34, or 1.33.
  * Worker node pool versions: 1.35, 1.34, or 1.33.



**Advanced cluster status:** Advanced clusters are mandatory.

**Skip node upgrades:** Supported.

**Legacy features supported:** No. Blocks upgrade.

**Default and required OS images:** `ubuntu_cgv2`, `cos_cgv2` mandatory (cgroup v1 dropped). Default `osImageType` for new configurations is `ubuntu_cgv2`. You must migrate clusters to cgroup v2 before you upgrade.

**Kubeception node upgrade behavior:** Unsupported. Blocks upgrade.

**Upgrade tools:**

  * `gkectl`: Required for admin clusters. Supported versions are 1.35, 1.36, and 1.37.
  * Terraform: Supported if you created the user cluster using Terraform.
  * console: Supported for user cluster upgrades.
  * gcloud CLI: Supported for user cluster upgrades.



**Additional requirements:**

  * You can run admin cluster upgrades asynchronously with `gkectl upgrade admin --async`.



### Release 1.34

**Upgrade first:** Admin cluster

**Version skew rules:**

  * Admin cluster at 1.34 can manage user clusters at 1.34, 1.33, and 1.32.
  * User cluster control plane versions: 1.34, 1.33, or 1.32.
  * Worker node pool versions: 1.34, 1.33, or 1.32.

**Note:** When you convert a non-advanced cluster to an advanced cluster, no version skew is allowed. You must upgrade the control plane and all node pools at the same time.



**Advanced cluster status:** Advanced clusters are mandatory.

**Skip node upgrades:** Supported.

**Legacy features supported:** No. Blocks upgrade.

**Default and required OS images:** `ubuntu_cgv2`, `cos_cgv2`, `ubuntu_containerd`, `cos`. Default `osImageType` is `ubuntu_cgv2`.

**Kubeception node upgrade behavior:** Unsupported. Blocks upgrade.

**Upgrade tools:**

  * `gkectl`: Required for admin clusters. Required to convert non-advanced clusters to advanced clusters (mandatory in 1.34; the `gkectl` binary version must exactly match the target release version). Supported versions are 1.34, 1.35, and 1.36.
  * Terraform: Supported if you created the user cluster using Terraform.
  * console: Supported for advanced user cluster upgrades.
  * gcloud CLI: Supported for advanced user cluster upgrades.



**Additional requirements:**

The following additional requirements apply to upgrades to version 1.34:

  * Non-advanced clusters automatically convert to advanced clusters when you upgrade to 1.34. For information about the specific rules for upgrades from non-advanced to advanced clusters, see [Update or upgrade a cluster to an advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster).

  * Bundled `cert-manager` is mandatory and updated to version 1.19, overriding pre-existing custom `cert-manager` installations. For more information about upgrades to bundled `cert-manager`, see Use bundled `cert-manager`.

  * Node container runtime upgraded to containerd 2.0. This can have the following impacts:

    * containerd 2.0 doesn't support legacy Docker Image Manifest v2 or Schema 1 images. Make sure workloads pull container images using Docker Schema 2 or an OCI-compliant format before you upgrade to 1.34.
    * Registry mirror configuration is migrated to the hosts.toml format in containerd 2.0. If you manage custom mirror configurations or air-gapped registry endpoints directly on your nodes, verify that your configuration aligns with hosts.toml.
    * If you use custom DaemonSets or scripts that patch /etc/containerd/config.toml, make sure they don't use deprecated containerd v1 configuration options, which can cause containerd startup failures with containerd 2.0.
  * The default value of the [`nodePoolUpdatePolicy.maximumConcurrentNodePoolUpdate`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepoolupdatepolicy-maximumconcurrentnodepoolupdate-field) field changed in version 1.34.300. If you want sequential node pool upgrades in versions 1.34.300+, set `nodePoolUpdatePolicy.maximumConcurrentNodePoolUpdate: 1` in your user cluster configuration file:

    * For versions 1.34.0-1.34.200, `nodePoolUpdatePolicy.maximumConcurrentNodePoolUpdate` defaults to `1`, which updates one node pool at a time sequentially.
    * For versions 1.34.300+, `nodePoolUpdatePolicy.maximumConcurrentNodePoolUpdate` defaults to `0`, which updates all node pools concurrently.

For more information, see [Configure node pool update policy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-pool-update-policy).

  * Upgrade preflight checks actively validate all `PodDisruptionBudget` (PDB) configurations across the cluster. Before you upgrade, verify that your workloads don't have overly restrictive PDBs (for example, `maxUnavailable: 0` or `minAvailable` matching total replicas) that block node draining or preflight checks can fail.

  * If an upgrade is interrupted, upgrade directly to version 1.34.300-gke.59 or higher. This version prevents the bootstrap cluster from being deleted if you need to rerun `gkectl upgrade admin` after a failure. For more information, see [Rerunning `gkectl upgrade admin` deletes the bootstrap cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/known-issues#rerunning-gkectl-upgrade-admin-deletes-the-bootstrap-cluster-upgrade-to-the-advanced-clusters).

  * You can run admin cluster upgrades asynchronously with `gkectl upgrade admin --async` for advanced clusters except when you convert from non-advanced to an advanced cluster.




### Release 1.33

**Upgrade first:** Admin cluster

**Version skew rules:**

  * Admin cluster at 1.33 can manage user clusters at 1.33, 1.32, and 1.31.
  * User cluster control plane versions: 1.33, 1.32, or 1.31.
  * Worker node pool versions: 1.33, 1.32, or 1.31.

**Note:** When you convert a non-advanced cluster to an advanced cluster, no version skew is allowed. You must upgrade the control plane and all node pools at the same time.



**Advanced cluster status:** Advanced clusters are the default cluster type and are converted automatically. Opt-out allowed. For more information, see [Upgrade and maintain non-advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-maintain-non-advanced-cluster). If you set `enableAdvancedCluster` to `false`, new cluster creation fails.

**Skip node upgrades:** Supported.

**Legacy features supported:** No. Blocks upgrade.

**Default and required OS images:** `ubuntu_cgv2`, `cos_cgv2`, `ubuntu_containerd`, `cos`. Default `osImageType` is `ubuntu_cgv2`.

**Kubeception node upgrade behavior:** Unsupported. Blocks upgrade.

**Upgrade tools:**

  * `gkectl`: Required to convert non-advanced clusters to advanced clusters (the `gkectl` binary version must exactly match the target release version). Required for admin clusters. Supported versions are 1.33, 1.34, and 1.35.
  * Terraform: Supported if you created the user cluster using Terraform.
  * console: Supported for advanced user cluster upgrades.
  * gcloud CLI: Supported for advanced user cluster upgrades.



**Additional requirements:**

The following additional requirements apply to upgrades to version 1.33:

  * Upgrades from 1.32 to 1.33 automatically convert non-advanced clusters to advanced clusters by default. You can keep clusters non-advanced. For more information on how to keep clusters non-advanced, see [Upgrade and maintain non-advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-maintain-non-advanced-cluster).

  * Advanced clusters automatically install and bundle `cert-manager` v1.18, overriding pre-existing custom `cert-manager` installations. For more information about upgrades to bundled `cert-manager`, see Use bundled `cert-manager`.

  * If you upgrade to advanced clusters in this release, the `gkectl` binary version must exactly match the target release version when you convert from non-advanced to advanced clusters. This requirement only applies during the upgrade to an advanced cluster. For all other upgrades on your advanced cluster, the standard version skew rules are in effect.

  * If an upgrade is interrupted, upgrade directly to version 1.33.700-gke.71 or higher. This version prevents the bootstrap cluster from being deleted if you need to rerun `gkectl upgrade admin` after a failure.

  * You can run admin cluster upgrades asynchronously with `gkectl upgrade admin --async` for advanced clusters and non-advanced HA clusters if all user clusters run Controlplane V2. You can't use the `--async` flag when you convert from non-advanced to an advanced cluster.




### Release 1.32

**Upgrade first:** Admin cluster

**Version skew rules:**

  * Admin cluster at 1.32 can manage user clusters at 1.32, 1.31, and 1.30.
  * User cluster control plane versions: 1.32, 1.31, or 1.30.
  * Worker node pool versions: 1.32, 1.31, or 1.30.

**Note:** When you convert a non-advanced cluster to an advanced cluster, no version skew is allowed. You must upgrade the control plane and all node pools at the same time.



**Advanced cluster status:** Supported.

**Skip node upgrades:** Supported.

**Legacy features supported:** No. Blocks upgrade.

**Default and required OS images:** `ubuntu_cgv2`, `cos_cgv2`, `ubuntu_containerd`, `cos`. Default `osImageType` is `ubuntu_cgv2`.

**Kubeception node upgrade behavior:** Unsupported. Blocks upgrade. Must migrate to [Controlplane V2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features#migrate_user_clusters_to_controlplane_v2).

**Upgrade tools:**

  * `gkectl`: Required to convert non-advanced clusters to advanced clusters (the `gkectl` binary version must exactly match the target release version). Required for admin clusters. Supported versions are 1.32, 1.33, and 1.34.
  * Terraform: Supported if you created the user cluster using Terraform.
  * console: Supported for advanced user cluster upgrades.
  * gcloud CLI: Supported for advanced user cluster upgrades.



**Additional requirements:**

The following additional requirements apply to upgrades to version 1.32:

  * This is the first version that allows an optional upgrade to a fully-supported [GA](https://cloud.google.com/products#product-launch-stages) advanced cluster. You can choose to:

    * Upgrade to a non-advanced cluster and [maintain the non-advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-maintain-non-advanced-cluster). If you choose this option, you can do the following, starting in this release:

      * Upgrade the user cluster's control plane and the worker node pools separately. The worker node pools can be up to 2 minor versions behind the control plane.
      * Run the upgrade asynchronously for admin and user clusters.
    * Upgrade to a non-advanced cluster and then [convert the non-advanced cluster to an advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster). If you choose this option, you can do the following, starting in this release:

      * Upgrade the user cluster's control plane and the worker node pools separately when you upgrade the non-advanced cluster, but not when you convert to an advanced cluster. The worker node pools can be up to 2 minor versions behind the control plane.
      * Run the upgrade asynchronously for admin and user clusters when you upgrade the non-advanced cluster.
      * When you convert to the advanced cluster, upgrade to release version 1.32.1000-gke.57 or higher because it incorporates a fix to a known issue that prevents the bootstrap cluster from being deleted.
    * Upgrade to an advanced cluster directly. If you choose this option, the following applies, starting in this release:

      * You must upgrade the control plane and all node pools together.
      * You can run the upgrade asynchronously for user clusters, but not admin clusters.
      * Upgrade to release version 1.32.1000-gke.57 or higher because it incorporates a fix to a known issue that prevents the bootstrap cluster from being deleted.
  * The following legacy features aren't supported starting with this version. For more information, see Legacy features:

    * Dataplane V1 (Calico). Upgrade to Dataplane V2 before upgrading to 1.32.
    * Seesaw. Upgrade to an alternative load balancer before upgrading to 1.32.
    * Integrated F5 BIG-IP. Upgrade to an alternative load balancer before upgrading to 1.32.
    * Kubeception. Upgrade to a non-Kubeception cluster before upgrading to 1.32.
    * Non-HA admin clusters. Upgrade to an HA admin cluster before upgrading to 1.32.
  * The `gkectl` binary version must exactly match the target release version when you convert from non-advanced to advanced clusters. This requirement only applies during the upgrade to an advanced cluster. For all other upgrades on your advanced cluster, the standard version skew rules are in effect.

  * If an upgrade is interrupted, upgrade directly to version 1.32.1000-gke.57 or higher. This version prevents the bootstrap cluster from being deleted if you need to rerun `gkectl upgrade admin` after a failure.

  * In version 1.32 and later, you can run admin cluster upgrades asynchronously with `gkectl upgrade admin --async` for advanced clusters and non-advanced HA clusters if all user clusters run Controlplane V2. You can't use the `--async` flag when you convert from non-advanced to an advanced cluster.




### Release 1.31

**Upgrade first:** Admin cluster

**Version skew rules:**

  * Admin cluster at 1.31 can manage user clusters at 1.31, 1.30, and 1.29.
  * User cluster control plane versions: 1.31, 1.30, or 1.29.
  * Worker node pool versions: 1.31, 1.30, or 1.29. (Not supported on 1.31 advanced clusters).
  * To upgrade from 1.29/1.30 to 1.31, you must upgrade all clusters to version 1.30 before you upgrade the admin cluster to 1.31.



**Advanced cluster status:** Preview only. Can't upgrade to higher versions.

**Skip node upgrades:** Supported.

**Legacy features supported:** Dataplane V2 mandatory; Kubeception, Seesaw, and F5 still supported.

**Default and required OS images:** `ubuntu_cgv2`, `cos_cgv2`, `ubuntu_containerd`, `cos`. Default `osImageType` is `ubuntu_cgv2`.

**Kubeception node upgrade behavior:** Admin nodes upgraded with admin cluster; user CP nodes upgraded with user cluster.

**Upgrade tools:**

  * `gkectl`: Required for admin clusters, non-advanced clusters, and advanced clusters (preview, for this release). Supported versions are 1.31, 1.32, and 1.33.
  * Terraform: Supported for enrolled user clusters if you created the user cluster using Terraform.
  * console: Supported for enrolled user cluster upgrades.
  * gcloud CLI: Supported for enrolled user cluster upgrades.



**Additional requirements:**

The following additional requirements apply to upgrades to version 1.31:

  * This release introduced advanced clusters in preview mode. You can't migrate non-advanced clusters to advanced clusters in this release. You can create new clusters as advanced clusters, but you can't upgrade these preview-version advanced clusters to a higher version. We don't recommend creating advanced clusters in this release. For more information on product launch stages, like preview, see [Product launch stages](https://cloud.google.com/products#product-launch-stages).

  * In 1.31 and later, the architecture of upgrades changed to a model where the admin cluster must now be higher than or equal to its user clusters. Previously, user clusters could be up to two minor versions ahead of the admin cluster.

  * You must upgrade the admin cluster before you upgrade the user clusters managed by the admin cluster. Admin clusters can manage user clusters with the same minor version or up to 2 minor versions lower. For example, an admin cluster at version 1.31 can manage user clusters at versions 1.31, 1.30, and 1.29.

  * To upgrade from 1.29 to 1.31, you must stage the 1.30 bundle as an intermediate step. You must download both the 1.30 and 1.31 bundles on the admin workstation to upgrade to 1.31. To perform a skip-version upgrade from 1.29 to 1.31, do the following:

    1. Upgrade only the user cluster control plane from 1.29 to 1.30 (leaving worker node pools at 1.29).
    2. Upgrade the admin cluster from 1.29 to 1.30.
    3. Upgrade the admin cluster from 1.30 to the target 1.31.
    4. Upgrade the user cluster control plane and worker node pools together to 1.31.
  * If you use Kubeception, the admin cluster nodes are upgraded during the admin cluster upgrade and the user cluster control plane nodes are upgraded during the user cluster upgrade.

  * To upgrade to 1.31, you must enable Dataplane V2. To prevent network policy conflicts and traffic drops during CNI migration, you must manually save and then delete all `NetworkPolicy` objects and restore them after the upgrade. To transition to Dataplane V2, do the following:

    1. Export and save all your custom network policies:
           
           kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
               get networkpolicy -A -o wide \
               --field-selector metadata.namespace!=kube-system
           kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
               get networkpolicy POLICY_NAME \
               -n NAMESPACE -o yaml > policy.yaml
           

Replace the following:

       * `USER_CLUSTER_KUBECONFIG`: the path of the kubeconfig file for the user cluster
       * `POLICY_NAME`: the name of the `NetworkPolicy` object
       * `NAMESPACE`: the namespace of the `NetworkPolicy` object
    2. Delete the network policies from the cluster:
           
           kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
               delete networkpolicy POLICY_NAME \
               -n NAMESPACE
           

    3. Set `enableDataplaneV2: true` in the user cluster configuration file and perform the upgrade to 1.31.

    4. Apply the saved policies after the 1.31 upgrade completes so Cilium compiles them cleanly into extended Berkeley Packet Filter (eBPF):
           
           kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
               apply -f policy.yaml
           

  * If you have HA admin clusters, and all user clusters run Controlplane V2, you can run the upgrade asynchronously with the `gkectl upgrade admin --async` command.

  * Dataplane V2 is required for all user clusters. Before you upgrade a user cluster to version 1.31, follow the steps in [Enable Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#enable-dataplane-v2).

  * Legacy features aren't supported in 1.32 and you can replace them in 1.30 and 1.31 to prevent issues when you upgrade to 1.32.




### Release 1.30

**Upgrade first:** User cluster

**Version skew rules:**

  * User cluster at 1.30 can be managed by an admin cluster at 1.30, 1.29, or 1.28.
  * Admin cluster at 1.30 can only manage user clusters at 1.30. All user clusters and the admin cluster must reach 1.30 before you can upgrade the admin cluster to 1.31, and you must upgrade the admin cluster to 1.31 before any user cluster can upgrade to 1.31.
  * User cluster control plane versions: 1.30.
  * Worker node pool versions: 1.30, 1.29, or 1.28.



**Advanced cluster status:** Not available.

**Skip node upgrades:** Supported.

**Legacy features supported:** Supported. Migration to recommended features strongly advised.

**Default and required OS images:** `ubuntu_cgv2`, `cos_cgv2`, `ubuntu_containerd`, `cos`. Default `osImageType` is `ubuntu_cgv2`.

  * Kubeception node upgrade behavior:** Control plane & admin nodes upgrade during admin cluster upgrade



**Upgrade tools:**

  * `gkectl`: Required for admin clusters. Supported versions are 1.30, 1.31, and 1.32.
  * Terraform: Supported for enrolled user clusters if you created the user cluster using Terraform.
  * console: Supported for enrolled user cluster upgrades.
  * gcloud CLI: Supported for enrolled user cluster upgrades.



**Additional requirements:**

The following additional requirements apply to upgrades to version 1.30:

  * For this version and all previous versions, you must migrate all user clusters before you upgrade the managing admin cluster. The admin cluster must be at the same or a lower minor version than any managed user cluster.

  * If you use Kubeception the following is what happens during an upgrade:

    1. Upgrade the user cluster. Because the user control plane lives inside the admin cluster, running `gkectl upgrade cluster` only upgrades the worker node pools.
    2. Upgrade the admin cluster. The admin cluster upgrade upgrades the admin nodes and automatically upgrades all the user cluster control planes at the same time.
  * If you have Controlplane V2, the following is what happens during the upgrade:

    1. Upgrade the user cluster. This upgrades the control plane and worker node pools.
    2. Upgrade the admin cluster. This upgrades the admin nodes.
  * When you create a new user cluster, you must set the `enableControlplaneV2` field to `true`, which is the default, starting in this release. If you set the `enableControlplaneV2` field to `false`, `gkectl` rejects the file and won't create the cluster.

  * If you have HA admin clusters, and all user clusters run Controlplane V2, you can run the upgrade asynchronously with the `gkectl upgrade admin --async` command.

  * Legacy features aren't supported in 1.32 and you can replace them in 1.30 and 1.31 to prevent issues when you upgrade to 1.32.




### Release 1.29

**Upgrade first:** User cluster

**Version skew rules:**

  * User cluster at 1.29 can be managed by an admin cluster at 1.29, 1.28, or 1.16.
  * Admin cluster at 1.29 can manage user clusters at 1.29 and 1.30. An admin cluster at 1.29 can't manage user clusters at 1.31 because all clusters must first reach 1.30 and the admin cluster must be upgraded to 1.31 before any user cluster can upgrade to 1.31.
  * User cluster control plane versions: 1.29 or 1.30, which is up to 1 minor version higher.
  * Worker node pool versions: 1.29, 1.28, or 1.16.



**Advanced cluster status:** Not available.

**Skip node upgrades:** Supported.

**Legacy features supported:** Supported.

**Default and required OS images:** `ubuntu_cgv2`, `cos_cgv2`, `ubuntu_containerd`, `cos`. Default `osImageType` is `ubuntu_cgv2`.

**Kubeception node upgrade behavior:** Control plane & admin nodes upgrade during admin cluster upgrade

**Upgrade tools:**

  * `gkectl`: Required for admin clusters. Supported versions are 1.29, 1.30, and 1.31.
  * Terraform: Supported for enrolled user clusters if you created the user cluster using Terraform.
  * console: Supported for enrolled user cluster upgrades.
  * gcloud CLI: Supported for enrolled user cluster upgrades.



**Additional requirements:**

The following additional requirements apply to upgrades to version 1.29:

  * Worker nodes can be up to 2 minor versions behind the control plane (n+2).
  * You can skip a minor version when you upgrade worker node pools. For example, you can upgrade a worker node pool from 1.28 to 1.30.
  * Preflight checks run as pods inside the admin cluster or a temporary bootstrap kind cluster, instead of on the admin workstation.
  * Starting with this version, you can run a preflight check without upgrading the cluster using `gkectl upgrade cluster --dry-run`.
  * If you have HA admin clusters, and all user clusters run Controlplane V2, you can run the upgrade asynchronously with the `gkectl upgrade admin --async` command.



### Release 1.28

**Upgrade first:** User cluster

**Version skew rules:**

  * User cluster at 1.28 can be managed by an admin cluster at 1.28, 1.16, or 1.15.
  * Admin cluster at 1.28 can manage user clusters at 1.28, 1.29, and 1.30.
  * User cluster control plane versions: 1.28, 1.29, or 1.30, which is up to 2 minor versions higher.
  * Worker node pool versions: 1.28, 1.16, or 1.15, which is up to 2 minor versions lower.



**Advanced cluster status:** Not available.

**Skip node upgrades:** Supported.

**Legacy features supported:** Supported.

**Default and required OS images:** `ubuntu_containerd`, `cos`, `ubuntu_cgv2`, `cos_cgv2`. Default `osImageType` is `ubuntu_containerd`.

**Kubeception node upgrade behavior:** Control plane & admin nodes upgrade during admin cluster upgrade

**Upgrade tools:**

  * `gkectl`: Required for admin clusters. Supported versions are 1.28, 1.29, and 1.30.
  * Terraform: Supported for enrolled user clusters if you created the user cluster using Terraform.
  * console: Supported for enrolled user cluster upgrades.
  * gcloud CLI: Supported for enrolled user cluster upgrades.



**Additional requirements:**

The following additional requirements apply to upgrades to version 1.28:

  * You must enable `kubernetesmetadata.googleapis.com` and grant `roles/kubernetesmetadata.publisher` to the logging-monitoring service account. If you don't, preflight checks can fail or you might see `403 PERMISSION_DENIED` errors. Enable the API and grant the role to the existing logging-monitoring service account:
        
        gcloud services enable kubernetesmetadata.googleapis.com
        gcloud projects add-iam-policy-binding PROJECT_ID \
            --member="serviceAccount:LOGGING_SA" \
            --role="roles/kubernetesmetadata.publisher"
        

Replace the following:

    * `PROJECT_ID`: the ID of the fleet host project in which the user cluster is a member.
    * `LOGGING_SA`: the email address of your logging-monitoring service account.
  * Even though it is technically possible to skip versions during a node pool upgrade, this feature was introduced as a preview feature and it is not recommended for this version. For more information on product launch stages, like preview, see [Product launch stages](https://cloud.google.com/products#product-launch-stages).

  * Node pools with a bundled load balancer must exactly match the cluster version.

  * You can upgrade multiple nodes at the same time by setting the `nodePools[i].updateStrategy.rollingUpdate.maxSurge` field. Your vSphere cluster must have enough CPU, RAM, and available IP addresses to accommodate the extra surge VMs during the upgrade:

    * Set `maxSurge: 1` (default) to upgrade one node at a time (drain, replace, verify, then repeat).
    * Set `maxSurge: N` (where `N > 1`) to provision and drain up to `N` worker nodes at the same time (for example, `maxSurge: 3` upgrades 3 worker nodes concurrently).
  * You must have at least 100 GB of free disk space on your admin workstation to upgrade the admin workstation.

  * The `gkectl` version you use to upgrade can be up to two minor versions higher than the current cluster. You can't use a lower minor version.




### Releases before 1.28

The following additional requirements apply to upgrades to releases earlier than version 1.28. There were no release versions between 1.16 and 1.28:

Release 1.16:

  * Version skew between admin and user clusters and between control plane and node pools can only be 1 minor version apart. For example, an admin cluster at 1.15 can only manage user clusters with versions 1.15 or 1.16. A user cluster control plane upgraded to 1.16 can manage worker node pools running version 1.15 or 1.16. A pool at version 1.14 must be upgraded to 1.15 before the control plane can move to version 1.16. For more information about version skews, see Version skew rules.
  * Clusters are automatically enrolled in the GKE On-Prem API when created or upgraded to 1.16. With this change, you can view, monitor, and upgrade user clusters using console, gcloud CLI CLI, and Terraform instead of only the admin workstation shell.



Release 1.14:

  * You can upgrade only the user cluster control plane first, so that you don't have to drain and upgrade every worker node pool at the same time.
  * During upgrade, the system automatically inspects and updates the existing admin and user cluster kubeconfig files on the workstation, renewing credentials automatically.



Release 1.13:

  * Before this version, you could have an offline admin cluster. This release requires you to register your admin cluster to Google Cloud. For information on how to register a cluster, see [Register an existing cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster).
  * To upgrade a cluster to Google Distributed Cloud software only for VMware version 1.13 or later, you must first update any user cluster node pools that still use Docker Engine to containerd.



### Use bundled `cert-manager`

You must use the bundled `cert-manager`, which is automatically installed on advanced clusters. When you migrate from a non-advanced cluster to an advanced cluster, the integrated `cert-manager` automatically overrides any customer-installed versions of `cert-manager`. Make sure you don't have critical custom configurations or features applied to your existing `cert-manager` before you update or upgrade to advanced clusters.

To see if you applied critical custom configurations or features to your `cert-manager`, do the following:

  * Suspend continuous deployment tools. If you manage `cert-manager` using GitOps tools (such as Config Sync, ArgoCD, or Flux), suspend synchronization or remove `cert-manager` manifests from your repository before you upgrade. If a GitOps controller attempts to reconcile `cert-manager` back to an older version or custom manifest while the cluster upgrade runs, it creates a reconciliation loop that can stall the cluster upgrade.
  * Don't manually uninstall or delete `cert-manager` pods, namespaces, or CRDs before you upgrade. `gkectl` manages these upgrades in-place.
  * If you modified `cert-manager` deployment flags, node selectors, or pod resource limits, revert them. Advanced clusters don't support custom binary arguments or deployment-level overrides on `cert-manager`.
  * If you use specialized external issuers, private ACME DNS-01 webhook plugins, or custom webhooks, verify that your third-party plugins are compatible with the bundled `cert-manager` version for the release you are upgrading to.



For more information, see [Upgrade to `cert-manager` bundled with advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster#upgrade-cert-manager).

The following table lists which release versions require bundled `cert-manager`:

Version | Status for new clusters | Status for existing cluster upgrades | Bundled `cert-manager` required?  
---|---|---|---  
1.34+ | Mandatory | Mandatory conversion (v1.19 bundled) | Universally required for all customers. Non-advanced clusters can no longer exist.  
1.33 | Standard / Default for all new clusters | Auto-converts to advanced clusters by default (v1.18 bundled) | Required for almost all clusters, unless explicitly opting out with `enableAdvancedCluster: false` (1.32 → 1.33 only).  
1.32 (GA) | Enabled by default | Optional conversion to advanced clusters | Required if advanced clusters is enabled.  
1.31 (Preview) | Optional (`enableAdvancedCluster: true`) | Not supported | Required if advanced clusters is enabled.  
  
To see which `cert-manager` version is bundled with each supported release, see [Bundled `cert-manager` versions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/version-history#bundled-cert-manager-versions).

### Controlplane V2

When Controlplane V2 is enabled, the control plane for the user cluster runs on the user cluster itself. For Controlplane V2, the user cluster control plane nodes are upgraded during the user cluster upgrade, and the admin cluster control plane nodes are upgraded during the admin cluster upgrade.

### Legacy features

The following table lists legacy features that are blocked in version 1.32 and later. If you use these features, you must migrate to the recommended alternatives before you can upgrade to version 1.32 or later.

| Legacy feature (blocked in 1.32) | Replace with (recommended) | Link to migration instructions | | --- | --- | --- | | Dataplane V1 (Calico) | Dataplane V2 (Cilium / eBPF) | [Migrate to Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-user-cluster-recommended-features#migrate_to_dataplane_v2)| | Kubeception | Controlplane V2 | [Migrate to Controlplane V2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features#migrate_user_clusters_to_controlplane_v2) | | Non-HA admin cluster (1 replica) | HA admin cluster (3 replicas) | [Migrate to HA admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features#migrate_to_an_ha_admin_cluster) | | Seesaw load balancer | MetalLB or ManualLB | [Migrate to MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features#migrate_from_seesaw_to_metallb) or [Migrate load balancer type](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features#migrate_load_balancer_type)| | Integrated F5 BIG-IP (loadBalancer.kind: "F5BigIP") | ManualLB (paired with F5 Big-IP Controller or CCGI) | [Migrate to ManualLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features#migrate_configuration_settings_for_your_f5_big-ip_load_balancer) |

For details about how to migrate from legacy features to recommended features, see [Plan cluster migration to recommended features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features).

#### Kubeception migration and version behavior

Kubeception is a legacy feature that must be migrated to Controlplane V2 before you can upgrade to version 1.32 or later.

Upgrades behave differently for clusters with Kubeception depending on your version:

  * For 1.28: Control plane & admin nodes upgrade during admin cluster upgrade
  * For 1.29: Control plane & admin nodes upgrade during admin cluster upgrade
  * For 1.30: Control plane & admin nodes upgrade during admin cluster upgrade. If you use Kubeception the following is what happens during an upgrade:

    1. Upgrade the user cluster. Because the user control plane lives inside the admin cluster, running `gkectl upgrade cluster` only upgrades the worker node pools.
    2. Upgrade the admin cluster. The admin cluster upgrade upgrades the admin nodes and automatically upgrades all the user cluster control planes at the same time.
  * For 1.31: Admin nodes upgraded with admin cluster; user control plane nodes upgraded with user cluster.

  * For 1.32 and later: Kubeception is not supported. You must migrate to Controlplane V2 before you can upgrade to 1.32 or later.

For details about migrating Kubeception to Controlplane V2, see [Plan cluster migration to recommended features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features).




## Version skew versus skipping a version during upgrade

Version skew is the allowed difference in minor versions between an admin cluster and its managed user clusters or the difference in minor versions between a user cluster's control plane and the node pools on the user cluster.

Version skew is different from skipping a minor version when you upgrade.

You can only skip a minor version when you upgrade worker node pools, after you upgrade the control plane. This applies to advanced and non-advanced clusters, except advanced clusters running version 1.31 and versions prior to 1.28. For example, if a worker node pool is at version 1.29, update the user cluster control plane to 1.30 and then 1.31. After the control plane is at 1.31, upgrade the worker node pool from 1.29 to 1.31 directly, without upgrading to 1.30. For more information, see [Skip a version when upgrading node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/skip-version-upgrade).

To upgrade to a higher minor release than the next sequential minor release, upgrade to the next minor release first, then upgrade to the higher minor release. You can't skip a minor version when you upgrade admin and user cluster control planes. For example, if you want to upgrade from version 1.34.x to version 1.36.x, you can't upgrade directly. You must first upgrade from 1.34.x to 1.35.x, and then upgrade to 1.36.x.

A user cluster's control plane can be up to 2 minor versions higher than the worker node pools in the cluster. For example, if a user cluster's control plane is at 1.36, the worker node pools in the cluster can be 1.34, 1.35, or 1.36.

### What version skews are allowed?

An admin cluster can manage user clusters up to 2 minor versions _lower_. For example, if an admin cluster is at 1.31, the user clusters managed by that admin cluster can be at 1.29, 1.30, or 1.31.

Before version 1.31, the following version skew rules apply:

  * For versions 1.28 to 1.30, user clusters can be up to 2 minor versions _higher_ than their admin cluster. For example, if an admin cluster is at 1.15, the user clusters managed by that admin cluster can be at 1.15, 1.16, or 1.28. You can't upgrade a 1.28 user cluster to 1.29 until the admin cluster is upgraded to at least 1.16. Because version 1.31 changes the upgrade order to require upgrading the admin cluster first, an admin cluster at 1.29 or 1.30 can't manage user clusters at 1.31 or 1.32. All user clusters and the admin cluster must reach 1.30 before you can upgrade the admin cluster to 1.31.
  * For versions 1.16 and lower, user clusters can only be 1 minor version _higher_ than their admin cluster. For example, if an admin cluster is at 1.15, the user clusters managed by that admin cluster can be at 1.15 or 1.16.



## Do I have to upgrade user clusters all at once?

When you upgrade user clusters, you can choose one of the following:

  * Upgrade the whole user cluster with the control plane and all node pools in the cluster at the same time.
  * Upgrade the user cluster's control plane and leave the node pools at the current version.
  * Upgrade the user cluster's control plane and selectively upgrade node pools.



Which approach you take depends on several factors, such as:

  * The environment (production or non-production) that the cluster is in.
  * The length of your maintenance window.
  * The version of the user cluster.



For example, you might want to upgrade both the user cluster's control plane and all node pools in a development environment. But in a production environment with a short maintenance window, you might want to upgrade only the control plane because it takes less time and the control plane upgrade shouldn't disrupt user workloads.

Load balancer node pools (node pools with `enableLoadBalancer: true`) must be the same version as the cluster for every version.

### Version rules for `gkectl`

The version of `gkectl` that you can use for the upgrade depends on the target cluster version (that is, the version of the cluster you are upgrading to). Typically, you use the same version of `gkectl` as the cluster target version. The following rules are enforced during the upgrade:

  * The `gkectl` version must be the same or higher than the target minor cluster version. For example, if you are upgrading a 1.29 cluster to 1.30, you must use `gkectl` 1.30 or higher. Patch versions don't matter.

  * The `gkectl` version can be up to two minor versions higher than the current cluster version. For example, to upgrade a 1.28 cluster to 1.29, use `gkectl` version 1.29 or 1.30, but not version 1.31 because that is three minor versions higher than the cluster version.




The `gkectl` binary version must exactly match the target release version when you convert from non-advanced to advanced clusters. This strict version requirement only applies during the upgrade to an advanced cluster. For all other advanced cluster upgrades, the standard version skew rules apply.

## Patch version upgrade rules

Upgrade to the [latest patch version](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/version-and-upgrade-support#google_cloud_distributed) whenever possible to ensure your clusters have the latest security fixes. Patch versions don't affect the version skew and upgrade rules. For a given minor version, you can upgrade to any higher patch version. For example, you can upgrade from `1.35.0` to `1.35.1` and you can upgrade from `1.35.1` to `1.35.3`.

## What's next

  * Review [Upgrade best practices](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-best-practices) and create a plan for upgrading your clusters.

  * Create clusters with advanced clusters enabled:

    * [Create an admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster)
    * [Create a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster)
    * [Update or upgrade a cluster to an advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster/
title: Update or upgrade a cluster to an advanced cluster \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T16:59:22.532298+00:00
---

# Update or upgrade a cluster to an advanced cluster  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Update or upgrade a cluster to an advanced cluster Stay organized with collections  Save and categorize content based on your preferences. 

You can convert a version 1.32 cluster to an [advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-overview) by updating it in place at version 1.32 or by upgrading it to version 1.33. Converting to an advanced cluster prepares your environment for version 1.33 and later, where advanced clusters are the default or required architecture.

## Key differences after moving to advanced clusters

Upgrading or updating your cluster to an advanced cluster introduces several key differences compared to standard clusters. Here are the major changes in advanced clusters:

  * **Resource location** : Cluster and machine resources are no longer located in user clusters. These resources are located exclusively within the admin cluster.

  * **`NodeExternalIP`** : The `NodeExternalIP` isn't set on the nodes.

  * **`cert-manager` installation**: `cert-manager` is automatically installed on advanced clusters. If you installed `cert-manager` in your cluster, updating or upgrading to advanced cluster overwrites it with the advanced cluster version.




### Feature differences between advanced and non-advanced clusters

When you enable advanced clusters, some features or capabilities won't work the same way as they do in non-advanced clusters. Some of these changes apply only to the Preview version of advanced clusters in version 1.31. The differences are noted throughout the documentation.

The following table lists the features supported for Google Distributed Cloud software only for VMware, their availability status when advanced clusters is enabled, and any differences in behavior or use:

Make a selectionNo differencesChanges applyNot supportedNot recommendedDeprecatedFeature/capability | **1.31 Adv. clusters (Preview)** | **1.32 Not enabled** | **1.32 Advanced clusters (GA)** | **1.33 Advanced clusters (GA)** | **Differences**  
---|---|---|---|---|---  
Advanced clusters | **Preview** | GA | GA | GA | Not supported  
[Topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up) | **Preview** |  | **Preview** | **Preview** | Changes apply. For more information see [Set up topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up) and related cluster configuration references.  
[Regional fleet membership](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#gkeconnect-location-field) | GA | GA | GA | GA | No differences.  
[Version skew n+2 admin cluster - user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-version-rules#version-skew) |  | GA | GA | GA | Not recommended: Because managing a lower-version preview user cluster isn't supported, don't use this feature.   
[Version skew n+2 node pool - user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-version-rules#version-skew) |  | GA | GA | GA | Not recommended: Because managing a lower-version preview user cluster isn't supported, don't use this feature.  
[Max surge setting for node pool updates](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-updatestrategy-rollingupdate-maxsurge-field) | **Preview** | **Preview** | **Preview** | **Preview** | No differences.  
[cgroup v2 for nodes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-osimagetype-field) | GA | GA | GA | GA | No differences.  
[DSR mode for Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#dataplanev2-forwardmode-field) | GA | GA | GA | GA | No differences.  
[Binary Authorization for Controlplane V2 user clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/binary-authorization-policy) | GA | GA | GA | GA | No differences.  
[User-managed admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-workstation) | GA | GA | GA | GA | No differences.  
[StatefulSet CSI migration tool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/using-statefulset-csi-migration-tool) | GA | GA | GA | GA | No differences.  
[Seesaw to MetalLB migration](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-seesaw-metallb) | GA | GA | GA | GA | No differences.  
[Disable bundled ingress](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/disable-bundled-ingress) | GA | GA | GA | GA | No differences.  
[Admin cluster prepared credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials-admin) |  | GA | GA | GA | No differences.  
[Storage policy for a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-storage-policy) | GA | GA | GA | GA | No differences.  
[Storage policy for an admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-storage-policy) | GA | GA | GA | GA | No differences.  
[Node auto repair](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-repair) | GA | GA | GA | GA | Changes apply: If advanced cluster is enabled, the periodic health checks aren't run as part of auto repair. For information and other differences, see [Automatic node repair and health checking](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-repair).  
[High availability admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster) | GA | GA | GA | GA | No differences.  
[VM host affinity](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-vm-host-affinity) |  | GA | GA | GA | Supported on advanced clusters in version 1.32.200 and 1.33 and later. When you use [topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up), configure host groups in [`topologyDomains[i].compute.hostGroups`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file#topology-domains-compute-host-groups) in the vSphere infrastructure configuration file instead of `nodePools[i].vsphere.hostgroups` in the user cluster configuration file.  
[Generate configuration files from an existing cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/get-configuration-file-from-cluster) | GA | GA | GA | GA | Changes apply. Clusters that use [topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up#limitations) aren't supported.  
[Google Cloud Managed Service for Prometheus system metrics collection](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/logging-and-monitoring#using-managed-service-for-prometheus) | GA | GA | GA | GA | No differences.  
[Upgrade and rollback of node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-node-pools) |  | GA | GA | GA | No differences.  
[Update private registry credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-cluster-credentials#update_private_registry_credentials) | GA | GA | GA | GA | No differences.  
[Admin cluster backup and restore with gkectl](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-and-restore-an-admin-cluster-with-gkectl) |  | **Preview** | **Preview** | GA | Changes apply. Updated the `gkectl` command for improved restoring of admin clusters and to support backing up and restoring user clusters. For more information, see [Back up and restore advanced clusters with gkectl.](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-and-restore-advanced-cluster-with-gkectl)  
[User cluster node pool autoscaling](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-autoscaling-section) | GA | GA | GA | GA | No differences.  
[Cluster automatic node resizing](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-resize) |  | GA |  | GA | No differences.  
[Multiple vSphere cluster support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/install-overview#2_set_up_your_vsphere_environment) | GA | GA | GA | GA | No differences.  
[Multiple vSphere data centers support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/install-overview#2_set_up_your_vsphere_environment) | GA | GA | GA | GA | No differences.  
[OpenID Connect (OIDC) support for authentication to clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/authentication) | GA | GA | GA | GA | No differences.  
[CA certificate rotation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ca-rotation) |  | GA | GA | GA | No differences.  
[Workload Identity Federation support](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity) | GA | GA | GA | GA | No differences.  
[GKE Identity Service with LDAP authentication support](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/ldap) | GA | GA | GA | GA | No differences.  
[Always-on secrets encryption without hardware security module (HSM)](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/always-on-secrets-encryption) |  | GA | GA | GA | No differences.  
[Update vCenter CA certificates with gkectl](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-vcenter-certificate) | GA | GA | GA | GA | No differences.  
[Egress NAT gateway](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/egress-nat-gateway) | GA | GA | GA | GA | No differences.  
[Admin cluster fleet registration](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#gkeconnect-section) | GA | GA | GA | GA | No differences.  
[Windows node pool support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-guide-for-windows-server-os-node-pools) |  | GA |  |  | Not supported.  
[`containerd` runtime for Windows node pool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-guide-for-windows-server-os-node-pools) |  | GA |  |  | Not supported.  
[Container-Optimized OS node pool support](https://docs.cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits) |  | GA | GA | GA | No differences.  
[CoreDNS as the cluster DNS provider](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-dns) | GA | GA | GA | GA | No differences.  
[User cluster lifecycle in the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster) |  | GA | **Partial support** | GA | Changes apply. For more information, see [Advanced cluster limitations](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools#advanced_cluster_limitations).  
[Admin cluster node creation with Container-Optimized OS](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#os-image-type-field) |  | GA | GA | GA | No differences.  
[Multi-NIC capability for Pods](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multi-nic) | GA | GA | GA | GA | No differences.  
[MetalLB load balancer option](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb) | GA | GA | GA | GA | Changes apply. For details, see [Bundled load balancing with MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb).  
[`gkectl update admin` support for enabling and disabling Cloud Logging and Cloud Monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/logging-and-monitoring) | GA | GA | GA | GA | No differences.  
Windows Dataplane V2 support |  | GA |  |  | Not supported.  
Summary API metrics | GA | GA | GA | GA | No differences.  
[`gkectl update credentials` support for updating component access service account key](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/rotating-service-account-keys) | **Partial support** | GA | **Partial support** | **Partial support** | Changes apply. For details about what is or isn't supported for updating credentials for advanced clusters, see [Advanced cluster differences for rotating service account keys](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/rotating-service-account-keys#adv-cluster-diffs).  
[Prepared credentials for user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials) |  | GA | GA | GA | No differences.  
[Dry run upgrade of user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#upgrade_user_cluster) | GA | GA | GA | GA | No differences.  
[Asynchronous upgrade of user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#upgrade_user_cluster) | GA | GA | GA | GA | No differences.  
Dry run upgrade of admin cluster |  |  | GA | GA | No differences.  
[Asynchronous upgrade of admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#upgrade_admin_cluster) | GA | GA | GA | GA | No differences.  
[Sequential update of node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepoolupdatepolicy-maximumconcurrentnodepoolupdate-field) |  | GA | GA | GA | No differences.  
[Create volume snapshot with vSphere CSI driver](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vsphere-csi-restore-volume-snapshot) | **Preview** | **Preview** | **Preview** | **Preview** | No differences.  
[Create user cluster with Controlplane V2 enabled](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster) | GA | GA | GA | GA | No differences.  
[Storage migration with SPBM](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/storage-migration-spbm) | GA | GA | GA | GA | No differences.  
[Migrate a datastore to an SPBM](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-datastore-spbm) | GA | GA | GA | GA | No differences.  
[Migrate a user cluster to Controlplane V2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-kubeception-controlplane-v2) | GA | GA | GA | GA | No differences.  
[Migrate to an HA admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-admin-cluster-ha) | GA | GA | GA | GA | No differences.  
[Migrate configuration settings for F5 BIG-IP](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-f5-manual) | GA | GA | GA | GA | No differences.  
[Load balancer](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/setup-load-balance) | **Partial support** | GA | GA | GA | Changes apply. For more information, refer to the relevant load balancer and cluster configuration reference documentation.  
[Preflight checks](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/preflight-checks) | **Partial support** | GA | GA | GA | No differences.  
[Hardware requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cpu-ram-storage) | GA | GA | GA | GA | Changes apply. For details, see [CPU, RAM, and storage requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cpu-ram-storage).  
[Snapshot](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/snapshots-advanced-cluster) | GA | GA | GA | GA | No differences.  
[Private registry](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/private-registry) | GA | GA | GA | GA | Changes apply. For details about using a private registry on an advanced cluster, see [Limitations with advanced clusters and the full bundle](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/private-registry#advanced-cluster-limitation).  
IPAM, [DNS](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-dns), NTP and [multi-NIC](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multi-nic) | GA | GA | GA | GA | No differences.  
Cluster creation/upgrade/deletion | GA | GA | GA | GA | Changes apply. For more information, refer to the relevant cluster operation documentation and [ Advanced cluster limitations](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools#advanced_cluster_limitations).   
[Proxy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/firewall-rules) | GA | GA | GA | GA | No differences.  
[NodePool update policy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-pool-update-policy) |  | GA | GA | GA | No differences.  
[Diagnose](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose) |  | GA | GA | GA | Changes apply. vCenter-related checks aren't available for advanced clusters. Since there's no longer an `onprem-user-cluster-controller` controller, the [Diagnose cluster issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose) guide is obsolete for advanced clusters. For version 1.32 advanced clusters, the `gkectl diagnose cluster` command runs [health checks](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/healthchecks) for the specified cluster.  
[vSphere tags and VM tracking](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vm-track-tags) |  | GA |  | GA | No differences.  
vSphere host group |  | GA |  | GA | No differences.  
[Logging and monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/logging-and-monitoring) | GA | GA | GA | GA | No differences.  
[Anti-affinity groups](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#antiaffinitygroups-enabled-field) |  | GA | GA | GA | No differences.  
Non-HA user cluster control plane |  | GA |  |  | Not supported.  
`gkectl check-config` |  | GA | GA | GA | Changes apply. Support for the command on advanced user clusters was added in the following versions: 1.32.700+, 1.33.300+, and 1.34.0 and higher.  
  
## Prerequisites

  * The `gkectl` version must be the same as the target cluster version.

    * If needed, see [Download `gkectl`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads#download_gkectl) to get a supported version of `gkectl`.
  * Always [diagnose](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose) your cluster before updating or upgrading to an advanced cluster:

    * Run `gkectl diagnose cluster` on your admin and user clusters to ensure that they are healthy.
    * If the command reports any errors or warnings, resolve them before you start the update or upgrade to an advanced cluster.
  * Make sure your clusters use only [recommended features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features).

  * Verify your clusters don't use any features not supported by advanced clusters before starting the update or upgrade. If any unsupported features are active, disable them using [update](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-general) first.

    * Although highly-available (HA) user clusters are required on advanced clusters, you can still update or upgrade a non-HA user cluster to an HA advanced cluster following this guide.
  * You must update or upgrade the admin cluster to an advanced cluster before you update or upgrade any user clusters.

  * About `cert-manager` installation: `cert-manager` is automatically installed on advanced clusters. When you migrate from a non-advanced cluster to an advanced cluster, the integrated `cert-manager` automatically overrides any customer-installed versions of `cert-manager`. Make sure you don't have critical custom configurations or features applied to your existing `cert-manager` before you update or upgrade to advanced clusters.




## Update or upgrade the admin cluster to advanced cluster

**Caution:** If an update or upgrade to admin clusters fails, make sure you don't delete the external bootstrap cluster from the workstation. The bootstrap cluster contains all states required to resume the update or upgrade. If you need to rerun `gkectl update admin` or `gkectl upgrade admin` after a failure, you must add the `--reuse-bootstrap-cluster` (or `-r`) flag. Failure to use this flag can cause a severe issue where critical data is lost.

### Update

**Important:** Make sure your cluster version is at least 1.32.0.

  1. Diagnose your cluster to make sure it is healthy:
         
         gkectl diagnose cluster \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

     * If the command reports any errors or warnings, refer to [Diagnose cluster issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose#diagnose_admin_cluster) and resolve them before proceeding.
  2. Prepare for the advanced cluster:
         
         gkectl prepare \
             --bundle-path BUNDLE_PATH \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --advanced-cluster
         

Replace the following:

     * `BUNDLE_PATH`: the path of the bundle file. This file is on your admin workstation in `/var/lib/gke/bundles/`. For example:
           
           /var/lib/gke/bundles/gke-onprem-vsphere-1.32.0-gke.1085-full.tgz
           

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.

  3. Set `enableAdvancedCluster` in your [admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#enable-advanced-cluster-field) to `true`.

  4. Update the admin cluster to the advanced cluster:
         
         gkectl update admin \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --config ADMIN_CLUSTER_CONFIG
         

Replace the following:

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.
     * `ADMIN_CLUSTER_CONFIG`: the path of the admin cluster configuration file.

The command will recreate all the nodes in the admin cluster.




### Upgrade

**Caution:** If your cluster is using `cos` or `cos_cgv2` as the [control plane OS image type](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#os-image-type-field) or [node pool OS image type](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-osimagetype-field), make sure your cluster version is at least `1.32.0` before upgrading. Otherwise, make sure your cluster version is at least `1.31.100`.

  1. [Upgrade your admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#upgrade_awstation) if needed.

  2. Diagnose your cluster to make sure it is healthy:
         
         gkectl diagnose cluster \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

     * If the command reports any errors or warnings, refer to [Diagnose cluster issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose#diagnose_admin_cluster) and resolve them before proceeding.
  3. Prepare for the advanced cluster:
         
         gkectl prepare \
             --bundle-path BUNDLE_PATH \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --advanced-cluster
         

Replace the following:

     * `BUNDLE_PATH`: the path of the bundle file. This file is on your admin workstation in `/var/lib/gke/bundles/`. For example:
           
           /var/lib/gke/bundles/gke-onprem-vsphere-1.32.0-gke.1085-full.tgz
           

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.

  4. Set `enableAdvancedCluster` in your [admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#enable-advanced-cluster-field) to `true`.

  5. Make sure the `bundlepath` field in the [admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#bundlepath-field) matches the path of the bundle to which you want to upgrade.

  6. Upgrade the admin cluster to the advanced cluster:
         
         gkectl upgrade admin \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --config ADMIN_CLUSTER_CONFIG
         

Replace the following:

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.
     * `ADMIN_CLUSTER_CONFIG`: the path of the admin cluster configuration file.

The command will rollout recreate all the nodes in the admin cluster. With the rollout recreate deployment strategy, the nodes are upgraded one at a time. During the node upgrade, the VM is deleted and then recreated with the new version.




After the admin cluster has been updated or upgraded to an advanced cluster:

  * Your existing non-advanced user clusters continue to function normally.

  * You can create only advanced user clusters that are managed by the advanced admin cluster.




Upgrade all user clusters to advanced clusters soon afterward to maintain a consistent and fully-featured environment.

## Update or upgrade the user cluster to advanced cluster

**Important:** Make sure the admin cluster has already been updated or upgraded to the advanced cluster.

### Update

**Important:** Make sure your cluster version is at least 1.32.0.

  1. Diagnose your cluster to make sure it is healthy:
         
         gkectl diagnose cluster \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --cluster-name USER_CLUSTER_NAME
         

     * If the command reports any errors or warnings, refer to [Diagnose cluster issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose#diagnose_user_cluster) and resolve them before proceeding.
  2. If your user cluster control plane is not highly available (HA):

**Caution:** Due to a [known issue with the `masterNode.replicas` field](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/known-issues#nonha-to-ha-adv-update-fail), to update a version 1.32 or version 1.33 non-HA user cluster to an HA advanced cluster, your cluster must be at a version higher than 1.32.600 or higher than 1.33.100 respectively.
     1. Change [`masterNode.replicas`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#masternode-replicas-field) from 1 to 3.

     2. Add the static IP addresses for the user cluster control-plane nodes to the [`network.controlPlaneIPBlock.ips`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-controlplaneipblock-ips-section) section.

  3. Prepare for the advanced cluster:
         
         gkectl prepare \
             --bundle-path BUNDLE_PATH \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --advanced-cluster
         

Replace the following:

     * `BUNDLE_PATH`: the path of the bundle file. This file is on your admin workstation in `/var/lib/gke/bundles/`. For example:
           
           /var/lib/gke/bundles/gke-onprem-vsphere-1.32.0-gke.1085-full.tgz
           

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.

  4. Set `enableAdvancedCluster` in your [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field) to `true`.

  5. Update the user cluster to the advanced cluster:
         
         gkectl update cluster \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --config USER_CLUSTER_CONFIG
         

Replace the following:

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.
     * `USER_CLUSTER_CONFIG`: the path of the user cluster configuration file.

The command will rollout recreate all the nodes in the user cluster. With the rollout recreate deployment strategy, the nodes are updated one at a time. During the node update, the VM is deleted and then recreated with the new configuration.




### Upgrade

**Caution:** If your cluster is using `cos` or `cos_cgv2` as the [control plane OS image type](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#os-image-type-field) or [node pool OS image type](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-osimagetype-field), make sure your cluster version is at least `1.32.0` before upgrading. Otherwise, make sure your cluster version is at least `1.31.100`.

  1. Diagnose your cluster to make sure it is healthy:
         
         gkectl diagnose cluster \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --cluster-name USER_CLUSTER_NAME
         

     * If the command reports any errors or warnings, refer to [Diagnose cluster issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose#diagnose_user_cluster) and resolve them before proceeding.
  2. If your user cluster control plane is not highly available (HA):

     1. Change [`masterNode.replicas`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#masternode-replicas-field) from 1 to 3.

     2. Add the static IP addresses for the user cluster control-plane nodes to the [`network.controlPlaneIPBlock.ips`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-controlplaneipblock-ips-section) section.

  3. Prepare for the advanced cluster:
         
         gkectl prepare \
             --bundle-path BUNDLE_PATH \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --advanced-cluster
         

Replace the following:

     * `BUNDLE_PATH`: the path of the bundle file. This file is on your admin workstation in `/var/lib/gke/bundles/`. For example:
           
           /var/lib/gke/bundles/gke-onprem-vsphere-1.32.0-gke.1085-full.tgz
           

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.

  4. Set `enableAdvancedCluster` in your [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field) to `true`.

  5. Make sure the `gkeOnPremVersion` field in the [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#gkeonpremversion-field) matches the target version of your upgrade.

  6. Upgrade the user cluster to the advanced cluster:
         
         gkectl upgrade cluster \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --config USER_CLUSTER_CONFIG
         

Replace the following:

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.
     * `USER_CLUSTER_CONFIG`: the path of the user cluster configuration file.

The command will recreate all the nodes in the user cluster.




## `cert-manager` bundled with advanced clusters

`cert-manager` is a mandatory, system-managed component in [advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-overview).

If you use `cert-manager` without advanced clusters, check the following before you upgrade to advanced clusters:

  * There are no custom configurations or feature flags in your `cert-manager`.
  * Your `cert-manager` version is the same version or one version behind the bundled version.



### Apigee Hybrid compatibility

The bundled `cert-manager` is fully compatible with **Apigee Hybrid** workloads. When you upgrade to an advanced cluster, the installer might warn you that the existing `cert-manager` installation will be replaced. This is expected behavior that the system handles automatically.

To ensure a smooth transition for your Apigee workloads:

  * **Do not uninstall** your existing `cert-manager` manually before the upgrade.
  * **Revert customizations** : If you manage `cert-manager` using GitOps or have applied custom configurations to the `cert-manager` deployment, you must revert these customizations or suspend sync before the upgrade to avoid configuration drift and potential upgrade pauses.



### Capabilities and limitations

You can do the following with the bundled `cert-manager`:

  * Create and edit `Issuer` and `ClusterIssuer` resources.
  * Create and edit certificate resources that reference issuers and standard issuer types.
  * Create and edit standard Kubernetes resources that `cert-manager` uses.
  * Create Kubernetes Secrets containing API keys and reference them in your issuers.
  * Configure your issuers to use specific HTTP-01 or DNS-01 solvers.



You cannot customize the following in the bundled `cert-manager`:

  * Set the `deployment` or `helm` values.
  * Add command line arguments or flags to the `cert-manager` binary.
  * Change resource limits or node selectors for `cert-manager` pods.
  * Modify the installation logic of the `cert-manager` software.
  * Turn on experimental features.
  * Force `cert-manager` control plane pods to run on specific infrastructure nodes.



If you have specific constraints that prevent you from using the bundled `cert-manager`, contact [Google Cloud support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support) for assistance with advanced configuration options.

### Bundled versions

The following table lists the bundled `cert-manager` versions for each version of Google Distributed Cloud (software only) for VMware.

Google Distributed Cloud (software only) for VMware | Bundled `cert-manager` version  
---|---  
1.32 | 1.17  
1.33 | 1.18  
1.34 | 1.19  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 

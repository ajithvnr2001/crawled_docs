---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/single-stack-ipv6/
title: Create and manage single-stack IPv6 clusters \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T22:53:48.777841+00:00
---

# Create and manage single-stack IPv6 clusters  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/single-stack-ipv6/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Create and manage single-stack IPv6 clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains how to create, configure, and manage single-stack IPv6 clusters in Google Kubernetes Engine (GKE).

You can run containerized workloads in an IPv6-only networking environment to avoid exhausting private IPv4 address space (RFC 1918). When you deploy a single-stack IPv6 cluster, you assign only IPv6 addresses to your Pods, nodes, and Services while maintaining ingress and egress connectivity to internal and external resources.

## Overview

As your workloads scale and cluster density increases, private IPv4 address space can quickly become exhausted. In IPv4-only and dual-stack clusters, every Pod requires an IPv4 address, which can make allocating CIDR blocks across your VPC network a major scaling bottleneck.

In GKE single-stack IPv6 clusters, you assign IPv6 addresses exclusively across the cluster data plane, removing IPv4 address constraints entirely. Worker nodes run on single-stack IPv6 Compute Engine VM instances, and Pods and Services communicate over IPv6 connections.

### IP address allocation (IPAM)

Single-stack IPv6 clusters allocate IPv6 addresses across your subnetwork, nodes, Pods, and Services by using the following prefix sizes:

Resource | CIDR block prefix | Description  
---|---|---  
Subnetwork | `/64` | Specified as an IPv6-only subnetwork CIDR block.  
Node | `/96` | Assigned automatically by GKE from the subnetwork CIDR block, providing approximately 4.29 billion unique IPv6 addresses per node.  
Pod | `/112` | Assigned from a subset of the node's `/96` subrange.  
Service | `/64` | Assigned automatically by GKE for ClusterIP Services from the `2600:2D00:0:4::0:0/64` IPv6 address range.  
  
### External and internal IPv6 access types

When setting up your cluster subnetwork, you can choose between two IPv6 access types to control internet routability:

  * **Internal (ULA):** subnetworks with the `INTERNAL` access type use Unique Local Unicast Addresses (ULA) within the `fd20::/20` range. Communication is scoped to your VPC network, peering networks, and hybrid connections. Nodes and Pods can't directly reach public IPv6 internet resources or receive direct internet ingress.
  * **External (GUA):** subnetworks with the `EXTERNAL` access type use Global Unicast Addresses (GUA). Nodes and Pods are assigned globally unique IPv6 addresses and can communicate with public IPv6 internet resources across both ingress and egress, subject to VPC firewall rules and routing tables.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Requirements and limitations

To use single-stack IPv6 clusters, ensure you meet the following requirements and limitations:

  * Your cluster must run GKE version 1.37.1-gke.3020000 or later.
  * Your cluster must be a VPC-native cluster that uses GKE Dataplane V2. Single-stack IPv6 clusters don't support route-based clusters.
  * Single-stack IPv6 clusters support only single-stack IPv6 VM instances as worker nodes, and don't support mixed or dual-stack node pools.
  * You must use Cloud DNS as the cluster DNS provider (`--cluster-dns=clouddns`). Single-stack IPv6 clusters don't support `kube-dns`.
  * Control plane access in single-stack IPv6 clusters uses two distinct paths: 
    * **External clients** : clients outside the cluster (for example, using `kubectl`) access the control plane through a domain-based endpoint over GKE Frontend (GKFE).
    * **Internal workloads** : nodes and Pods connect securely to the control plane over Private Service Connect. To support this communication, you must provide or create a subnetwork with an `INTERNAL` IPv6 access type (`--private-endpoint-subnetwork`).
  * On internal (`INTERNAL`) IPv6 subnetworks, nodes and Pods can reach Google APIs and Artifact Registry over IPv6 without a Cloud NAT gateway. However, consider the following: 
    * To reach external IPv4-only endpoints (such as external IPv4-only container registries), you must configure DNS64 and Cloud NAT (NAT64).
    * Nodes and Pods on `INTERNAL` subnetworks can't reach external public IPv6 endpoints outside Google because Unique Local Addresses (ULA) aren't routable on the public IPv6 internet and Cloud NAT doesn't support IPv6-to-IPv6 (`NAT66`) translation.
  * Single-stack IPv6 clusters don't support the `--private-ipv6-google-access-type` and `--enable-private-nodes` cluster flags. Instead, configure [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access) and IPv6 access types (`INTERNAL` or `EXTERNAL`) directly on your VPC subnetwork.
  * Single-stack IPv6 clusters don't support [multi-subnet configurations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-subnet-cluster).
  * Single-stack IPv6 clusters don't support [GKE Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress). To configure Layer 7 Application Load Balancers, use [Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api).
  * The GKE multi-networking API doesn't support IPv6 Pod networks; secondary Pod networks must be IPv4-only. For more information, see Multi-network support for Pods.
  * IPv6-only clusters don't support [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview).
  * You can use [bring your own IPv6 addresses (BYOIPv6)](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip) with single-stack IPv6 clusters. To learn about the requirements that apply to BYOIPv6 prefixes, see [Create and use IPv6 sub-prefixes](https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes).



### Workload metadata server configuration

Because workloads running in IPv6-only Pods can't reach the standard IPv4 metadata server address (`169.254.169.254`), apply the following adjustments:

  * Configure your applications and client libraries to access the metadata server by using the domain name `metadata.google.internal` (recommended) or the literal ULA IPv6 address `[fd20:ce::254]`.
  * If you use client libraries or applications with hardcoded IPv4 metadata server endpoints (for example, earlier versions of Google API client libraries), set the `GCE_METADATA_HOST` environment variable in your container images or Pod specs:
        
        env:
        - name: GCE_METADATA_HOST
          value: "metadata.google.internal"
        




## Create a single-stack IPv6 cluster

You can create a single-stack IPv6 cluster by using the Google Cloud CLI.

### Create a cluster and subnetwork simultaneously

If you don't have pre-existing custom subnetworks, you can create a Standard single-stack IPv6 cluster and have GKE automatically provision the required node subnetwork and `--private-endpoint-subnetwork` in a single command.

Run the following command:
    
    
    gcloud beta container clusters create CLUSTER_NAME \
        --cluster-version=VERSION \
        --enable-dataplane-v2 \
        --cluster-dns=clouddns \
        --stack-type=ipv6 \
        --network=NETWORK_NAME \
        --create-subnetwork name=SUBNET_NAME \
        --ipv6-access-type=ACCESS_TYPE \
        --location=COMPUTE_LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: the name for your new cluster.
  * `VERSION`: GKE version 1.37.1-gke.3020000 or later.
  * `NETWORK_NAME`: the name of an existing custom-mode VPC network.
  * `SUBNET_NAME`: the name of the new node subnetwork to create.
  * `ACCESS_TYPE`: the internet routability of the subnetwork. Specify `INTERNAL` for private ULA addressing or `EXTERNAL` for public GUA addressing. Defaults to `EXTERNAL` if omitted.
  * `COMPUTE_LOCATION`: the compute region or zone for your cluster.

**Note:** When using `--create-subnetwork`, GKE automatically provisions both the node subnetwork and the required internal PSC control plane subnetwork. When you delete the cluster, GKE makes a best-effort attempt to delete these subnetworks, provided no other resources use them.

### Create a Standard cluster on custom subnetworks

To use pre-existing or custom subnetworks, create the VPC network, the PSC control plane subnetwork, and the node subnetwork before you create your cluster.

  1. Create a custom-mode VPC network with ULA internal IPv6 addresses enabled:
         
         gcloud compute networks create NETWORK_NAME \
             --subnet-mode=CUSTOM \
             --enable-ula-internal-ipv6
         

  2. Create the dedicated internal PSC control plane subnetwork:
         
         gcloud compute networks subnets create PSC_SUBNET_NAME \
             --stack-type=ipv6_only \
             --ipv6-access-type=INTERNAL \
             --network=NETWORK_NAME \
             --region=COMPUTE_REGION
         

Replace `COMPUTE_REGION` with the region where you deploy your cluster (for example, `us-central1`). You can also specify `--stack-type=ipv4_ipv6` for the PSC control plane subnetwork.

  3. Create the node subnetwork. Choose either internal access (`INTERNAL`) or external access (`EXTERNAL`):
         
         gcloud compute networks subnets create NODE_SUBNET_NAME \
             --stack-type=ipv6_only \
             --ipv6-access-type=ACCESS_TYPE \
             --network=NETWORK_NAME \
             --region=COMPUTE_REGION
         

  4. Create the single-stack IPv6 Standard cluster referencing both subnetworks:
         
         gcloud container clusters create CLUSTER_NAME \
             --cluster-version=VERSION \
             --enable-dataplane-v2 \
             --cluster-dns=clouddns \
             --stack-type=ipv6 \
             --network=NETWORK_NAME \
             --subnetwork=NODE_SUBNET_NAME \
             --private-endpoint-subnetwork=PSC_SUBNET_NAME \
             --location=COMPUTE_LOCATION
         




### Create an Autopilot cluster on custom subnetworks

Autopilot clusters automatically inherit their stack type from the node subnetwork that you specify. When you select an IPv6-only subnetwork, GKE creates a single-stack IPv6 Autopilot cluster.

  1. Ensure you have created a custom VPC network, an internal PSC subnetwork, and an IPv6-only node subnetwork as described in the previous section.

  2. Create the Autopilot cluster:
         
         gcloud container clusters create-auto CLUSTER_NAME \
             --cluster-version=VERSION \
             --network=NETWORK_NAME \
             --subnetwork=NODE_SUBNET_NAME \
             --private-endpoint-subnetwork=PSC_SUBNET_NAME \
             --location=COMPUTE_LOCATION
         




### Create a Standard cluster with managed nodes

You can also create a single-stack IPv6 Standard cluster that uses managed nodes configured at the workload level. To learn more about configuring managed ComputeClasses in Standard clusters, see [Autopilot classes in Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-classes-standard-clusters).

### Use bring your own IPv6 addresses for nodes and Pods

You can create a single-stack IPv6 cluster whose nodes and Pods use [bring your own IPv6 addresses (BYOIPv6)](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip) instead of Google-provided addresses. To do so, create the node subnetwork with an external IPv6 address range that comes from a regional IPv6 sub-prefix of your public delegated prefix (PDP). Nodes and Pods then receive IPv6 addresses from that prefix and communicate with the internet and with each other by using those addresses.

  1. Create a regional IPv6 sub-prefix of your public delegated prefix in `EXTERNAL_IPV6_SUBNETWORK_CREATION` mode. For more information, see [Create IPv6 sub-prefixes](https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes#create-subprefix).

  2. Create the node subnetwork with an `EXTERNAL` IPv6 access type and reference the sub-prefix by using the `--ip-collection` flag. Compute Engine allocates the subnetwork's `/64` IPv6 address range from the sub-prefix:
         
         gcloud compute networks subnets create NODE_SUBNET_NAME \
             --stack-type=ipv6_only \
             --ipv6-access-type=EXTERNAL \
             --ip-collection=SUB_PREFIX_NAME \
             --network=NETWORK_NAME \
             --region=COMPUTE_REGION
         

Replace `SUB_PREFIX_NAME` with the name of the sub-prefix that you created in the previous step. The sub-prefix must be in the same region as the subnetwork. To choose a specific `/64` range from the sub-prefix instead of letting Compute Engine allocate one, add the `--external-ipv6-prefix` flag.

  3. Create the cluster on this node subnetwork by following the steps in Create a Standard cluster on custom subnetworks or Create an Autopilot cluster on custom subnetworks. The PSC control plane subnetwork doesn't need a BYOIPv6 address range.

  4. After GKE creates the cluster, verify that the nodes and Pods have IPv6 addresses from your prefix:
         
         kubectl get nodes -o wide
         kubectl get pods --all-namespaces -o wide
         




Keep the following in mind:

  * This procedure uses a node subnetwork with the `EXTERNAL` IPv6 access type, so nodes and Pods get globally routable addresses from your prefix. You can also use a node subnetwork with the `INTERNAL` IPv6 access type by referencing a sub-prefix in `INTERNAL_IPV6_SUBNETWORK_CREATION` mode; in that case, nodes and Pods get internal BYOIPv6 addresses and the connectivity limitations of the internal IPv6 access type apply. For more information, see Connect to external and private resources.
  * To expose workloads on BYOIPv6 addresses with LoadBalancer Services, see [Bring your own IPv6 addresses (BYOIPv6)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters#byoipv6), which doesn't require a BYOIPv6 node subnetwork.
  * For the requirements that apply to BYOIPv6 prefixes, see [Create and use IPv6 sub-prefixes](https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes).



### Verify the cluster stack type

After cluster creation finishes, list your clusters to verify that your cluster runs in single-stack IPv6 mode:
    
    
    gcloud beta container clusters list
    

The output confirms the `STACK_TYPE` column is set to `IPV6`:
    
    
    NAME               LOCATION       MASTER_VERSION      MASTER_IP                                 MACHINE_TYPE  NODE_VERSION        NUM_NODES  STACK_TYPE  STATUS
    v6-only-cluster-1  us-central1-c  1.37.0-gke.1000000  gke-3a3234-123456.us-central1-c.gke.goog  e2-medium     1.37.0-gke.1000000  1          IPV6        RUNNING
    

## Load balancing in single-stack IPv6 clusters

You can expose applications running inside single-stack IPv6 clusters using both Layer 7 and Layer 4 load balancers:

  * **Layer 7 Application Load Balancing (Gateway API)** : use the Kubernetes Gateway API to deploy Layer 7 Application Load Balancers (`gke-l7-rilb`, `gke-l7-regional-external-managed`, or `gke-l7-global-external-managed`). These Gateways can serve both internal and external IPv4 and IPv6 clients while routing traffic transparently to internal IPv6-only Pod endpoints. Note that [GKE Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress) is not supported on single-stack IPv6 clusters. When you deploy regional Gateways (`gke-l7-rilb` and `gke-l7-regional-external-managed`) on single-stack IPv6 clusters, keep the following subnetwork requirements in mind:

    * **Proxy-only subnetwork** : on single-stack IPv6 clusters, the regional proxy-only subnetwork (`--purpose=REGIONAL_MANAGED_PROXY`) must be dual-stack (`--stack-type=IPV4_IPV6`). On IPv4-only and dual-stack clusters, the subnetwork can be either IPv4-only or dual-stack.
    * **Gateway VIP subnetwork** : unlike IPv4 regional external Gateways (which don't allocate VIPs from a subnetwork), IPv6 regional external Gateways (`gke-l7-regional-external-managed`) require a subnetwork with `EXTERNAL` IPv6 access, and regional internal Gateways (`gke-l7-rilb`) require a subnetwork with `INTERNAL` IPv6 access (or an IPv4 range for an internal IPv4 VIP). To allocate an ephemeral regional Gateway VIP from a custom subnetwork instead of the cluster's node subnetwork, specify the subnetwork name in the `spec.default.subnetwork` field of a `GCPGatewayPolicy` attached to the Gateway.

For configuration instructions, see [Deploy Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways).

  * **Layer 4 Passthrough Load Balancing (Service API)** : You can expose workloads to IPv6 clients using Kubernetes Services configured with `type: LoadBalancer`. Depending on whether your cluster nodes run on an `INTERNAL` (ULA) or `EXTERNAL` (GUA) subnetwork, you might need to provision a dedicated load balancer subnetwork and reference it using the `networking.gke.io/load-balancer-subnet` annotation:

    * For internal load balancers, see [Create an internal LoadBalancer Service on a single-stack IPv6 cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing#single-stack-ipv6).
    * For external load balancers, see [Create an external LoadBalancer Service on a single-stack IPv6 cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/backend-service-based-external-load-balancer#single-stack-ipv6).
    * To assign BYOIPv6 addresses to load balancers, see [Bring your own IPv6 addresses (BYOIPv6)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters#byoipv6). External LoadBalancer Services can allocate their addresses directly from a BYOIPv6 public delegated prefix regardless of the access type of the node subnetwork.



## Connect to external and private resources

Workloads in your single-stack IPv6 cluster often need to communicate with external services across the internet or private services in Google Cloud.

### Connect to public IPv6 internet resources

If your cluster nodes run on a subnetwork configured with the `EXTERNAL` IPv6 access type (`--ipv6-access-type=EXTERNAL`), outbound egress and ingress connectivity to public internet IPv6 endpoints is enabled by default. Verify that your VPC firewall rules permit the required IPv6 traffic. To learn more, see [Use VPC firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls).

### Connect to public IPv4 internet resources (DNS64 and NAT64)

Because Pods in a single-stack IPv6 cluster have only IPv6 addresses, connecting to public IPv4-only internet endpoints requires network translation. You can configure Cloud DNS and Cloud NAT across your VPC network to provide automatic DNS64 and NAT64 translation:

  1. Create a DNS64 server policy:
         
         gcloud dns policies create POLICY_NAME \
             --description="DNS64 policy for single-stack IPv6 cluster" \
             --networks=NETWORK_NAME \
             --enable-dns64-all-queries
         

  2. Create a Cloud Router in the region where your cluster is deployed:
         
         gcloud compute routers create ROUTER_NAME \
             --network=NETWORK_NAME \
             --region=COMPUTE_REGION
         

  3. Create a Cloud NAT gateway configured for NAT64 translation:
         
         gcloud compute routers nats create NAT_NAME \
             --router=ROUTER_NAME \
             --region=COMPUTE_REGION \
             --auto-allocate-nat-external-ips \
             --nat64-all-v6-subnet-ip-ranges
         

To configure NAT64 with specific subnetworks or manual external IP addresses, use `--nat64-custom-v6-subnet-ip-ranges` and `--nat-external-ip-pool`.




To learn more about address translation, see [Configure DNS64 and NAT64](https://docs.cloud.google.com/vpc/docs/connect-ipv6-to-ipv4#configure-dns64-and-nat64) and [DNS64 and NAT64 for 6to4 connectivity](https://docs.cloud.google.com/vpc/docs/ipv6-to-ipv4-overview).

### Connect to private services using Private Service Connect

Private Service Connect (PSC) supports IPv6-to-IPv4 address translation across endpoints and forwarding rules. You can connect workloads in your single-stack IPv6 cluster to Google Cloud managed services (such as Cloud SQL instances) or third-party producer services:

  1. Reserve a static internal IPv6 address from your cluster's PSC subnetwork:
         
         gcloud compute addresses create ADDRESS_NAME \
             --ip-version=IPV6 \
             --subnet=PSC_SUBNET_NAME \
             --region=COMPUTE_REGION
         

  2. Create a PSC endpoint forwarding rule targeting the service attachment:
         
         gcloud compute forwarding-rules create FORWARDING_RULE_NAME \
             --address=ADDRESS_NAME \
             --region=COMPUTE_REGION \
             --network=NETWORK_NAME \
             --target-service-attachment=SERVICE_ATTACHMENT_URL \
             --allow-psc-global-access
         

  3. Retrieve the assigned IPv6 address:
         
         gcloud compute forwarding-rules describe FORWARDING_RULE_NAME \
             --region=COMPUTE_REGION \
             --format='value(IPAddress)'
         

  4. Use the retrieved IPv6 address inside your application connection strings. PSC translates the traffic so that your IPv6 Pods can securely reach IPv4 or dual-stack producer services.




To learn more about consuming published services, see [Create a Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#create-endpoint) and [Connect to Cloud SQL with Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect). To publish an internal LoadBalancer Service running in your cluster to consumers in other VPC networks using a `ServiceAttachment` resource, see [Create an internal load balancer with Private Service Connect](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing-across-vpc-net#ilb_psc).

## Advanced networking and accelerators

You can configure single-stack IPv6 clusters with secondary network interfaces for accelerator node pools and multi-network Pods.

### Multi-NIC accelerator networking

In Standard single-stack IPv6 clusters, you can attach secondary data networks (`RDMA` or `DIORITE`) to accelerator node pools (GPUs and TPUs) using automated networking (`--accelerator-network-profile=auto`) or manual multi-network configuration (`--additional-node-network`). Secondary interfaces can run on IPv4 subnetworks, dual-stack subnetworks, or IPv6-only subnetworks.

For step-by-step instructions, see [Configure multi-NIC node networks on single-stack IPv6 clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/config-auto-net-for-accelerators#ipv6-multi-nic).

### Multi-network support for Pods

Single-stack IPv6 clusters support multi-networking for Pods with the following characteristics:

  * The primary Pod network interface (`eth0`) uses single-stack IPv6 networking.
  * Additional Pod network interfaces must be IPv4-only (Layer 3 VPC networks). Single-stack IPv6 clusters don't support IPv6 Pod networks on additional network interfaces.
  * The `networking.gke.io/default-interface` Pod annotation configures the default interface for IPv4 traffic only; no default interface is configured for IPv6 traffic.



To learn how to configure secondary IPv4 Pod networks backed by VPC subnetworks, see [Set up multi-network support for Pods on single-stack IPv6 clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods#single-stack-ipv6).

## Migrate to single-stack IPv6 clusters

You can't directly convert or in-place update existing IPv4 clusters or dual-stack clusters to single-stack IPv6 clusters. To transition workloads, use a blue-green migration:

  1. **Audit dependencies** : verify that application configurations, client libraries, and agents use DNS names (such as `metadata.google.internal`) rather than hardcoded IPv4 addresses. Configure `GCE_METADATA_HOST` if required.
  2. **Provision green cluster** : deploy a new single-stack IPv6 cluster side-by-side with your existing cluster within the same or peered VPC network. Verify that Cloud DNS, DNS64, Cloud NAT (NAT64), and PSC forwarding rules are configured.
  3. **Deploy workloads** : apply your Kubernetes manifests to the green cluster and verify that Pods start and communicate successfully.
  4. **Shift traffic** : Using your load balancers (Gateway API or Cloud DNS routing policies), gradually shift traffic from the legacy cluster to the new IPv6 cluster while monitoring metrics and error rates.
  5. **Decommission legacy cluster** : after all traffic has shifted and the green cluster is verified stable, drain and delete the old cluster.



## What's next

  * To learn more about GKE networking, see [GKE network overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview).
  * To learn how GKE assigns IP addresses, see [Understand IP addressing in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-ip-addressing).
  * To configure Layer 7 load balancing, see [Deploying Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways).
  * To configure secondary Pod networks, see [Set up multi-network support for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 

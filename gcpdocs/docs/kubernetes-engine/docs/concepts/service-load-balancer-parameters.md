---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters/
title: LoadBalancer Service parameters \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-07T05:43:57.713967+00:00
---

# LoadBalancer Service parameters  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  LoadBalancer Service parameters Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes parameters for the Service manifests which control LoadBalancer Service behavior and configuration. Before reading this page, ensure that you're familiar with [Google Kubernetes Engine (GKE) LoadBalancer Service concepts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer).

**Important:** LoadBalancer Services rely on specific finalizers (prefixed with `networking.gke.io`) and debug annotations (prefixed with `service.kubernetes.io`). Don't manually edit or remove these finalizers or annotations. Modifying or removing these objects can cause unexpected behavior or disruptions.

## Service parameters

GKE supports the following parameters for LoadBalancer Services.

Parameter | Service field and description | Internal | External | Version Support  
---|---|---|---|---  
Internal passthrough Network Load Balancer | 

  * `spec.loadBalancerClass: networking.gke.io/l4-regional-internal`
  * `networking.gke.io/load-balancer-type: "Internal"`

Instructs GKE to create an internal passthrough Network Load Balancer. The load balancer uses `GCE_VM_IP` NEG backends if either of the following is true:

  * The Service manifest is applied to a cluster that has [ GKE subsetting](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#subsetting) enabled.
  * The Service manifest is applied to a cluster that runs GKE version 1.36 or later. GKE subsetting is automatically enabled in GKE version 1.36 and later.

In all other situations, the load balancer uses instance group backends. For more information, see [ Node grouping](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#endpoint-grouping). |  |  | 

  * `spec.loadBalancerClass: networking.gke.io/l4-regional-internal`: requires GKE version 1.33.1-gke.1779000 and later _and_ GKE subsetting enabled.
  * `networking.gke.io/load-balancer-type: "Internal"`: all supported versions.

We recommend `spec.loadBalancerClass` if your cluster uses GKE version 1.33.1-gke.1779000 or later, and has GKE subsetting enabled. This attribute is immutable and can't be changed after the Service manifest has been applied to a cluster.  
Backend service-based regional external passthrough Network Load Balancer | 

  * Default behavior in GKE 1.37 and later
  * `spec.loadBalancerClass: networking.gke.io/l4-regional-external`
  * `cloud.google.com/l4-rbs: "enabled"`

Instructs GKE to create a regional external passthrough Network Load Balancer. The load balancer uses `GCE_VM_IP` NEG backends if any of the following is true:

  * The Service is created in a cluster that runs GKE version 1.37 or later. No annotations or classes are required.
  * The Service manifest includes `spec.loadBalancerClass: networking.gke.io/l4-regional-external` and is applied to a cluster that runs GKE version 1.33.1-gke.1779000 to 1.36.
  * The Service manifest includes the `cloud.google.com/l4-rbs: "enabled"` annotation and is applied to a cluster that runs GKE version 1.32.2-gke.1652000 to 1.36.

In all other situations, the load balancer uses instance group backends. For more information, see [ Node grouping](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#endpoint-grouping). |  |  | 

  * `spec.loadBalancerClass: networking.gke.io/l4-regional-external`: requires GKE version 1.33.1-gke.1779000 and later.
  * `cloud.google.com/l4-rbs: "enabled"`: all supported versions.

We recommend `spec.loadBalancerClass` if your cluster uses GKE version 1.33.1-gke.1779000 to 1.36. This attribute is immutable and can't be changed after the Service manifest has been applied to a cluster. In GKE 1.37 and later, no fields are needed for this load balancer type.  
Weighted Load Balancing | `networking.gke.io/weighted-load-balancing: "pods-per-node"` Allows nodes that have more serving Pods to receive a larger proportion of new connections compared to nodes that have fewer serving Pods. |  |  | GKE 1.31.0+  
Internal Traffic Policy | `spec.internalTrafficPolicy` When set to the `Local` value, GKE only routes packets from client Pods on a node to serving Pods on the same node. When set to the `Cluster` value, GKE routes packets from client Pods on a node to serving Pods on any node. For more details, see [ Service Internal Traffic Policy](https://kubernetes.io/docs/concepts/services-networking/service-traffic-policy/). This parameter is not supported in clusters running GKE Dataplane V2. |  |  | GKE 1.22+  
External Traffic Policy | `spec.externalTrafficPolicy` Controls which node VMs pass load balancer health checks and how packets are routed to ready and serving Pods in the cluster. Also controls how nodes are grouped into `GCE_VM_IP` NEGs when _GKE subsetting_ is enabled. For details, see [ LoadBalancer Service concepts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer). |  |  | GKE 1.14+ (1.23.4-gke.400+ for Windows node pool).  
Zonal affinity | `spec.trafficDistribution: PreferSameZone` Enables zonal affinity for internal LoadBalancer Services. Zonal affinity controls the zone to which the internal passthrough Network Load Balancer routes incoming traffic for compatible clients when a zonal match is possible. To use zonal affinity, you must enable GKE subsetting (enabled by default from GKE version 1.36 and later). For more information, see [ Zonal affinity and traffic distribution](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#zonal-affinity). |  |  | Preview in GKE 1.33.3-gke.1392000 and later. Generally available in GKE version 1.36 and later.   
Health check port | `spec.healthCheckNodePort` Deploys a load balancer health check for LoadBalancer Services. This parameter is only valid if `spec.externalTrafficPolicy` is set to `Local`. |  |  | All supported versions.  
Firewall rules and source IP address allowlist | `spec.loadBalancerSourceRanges` Configures optional firewall rules in GKE and in the VPC network to only allow certain source ranges. `kube-proxy` also configures `iptables` rules to match the specified source ranges. |  |  | All supported versions.  
Static IP addresses | 

  * `spec.loadBalancerIP` (IPv4 only)
  * `networking.gke.io/load-balancer-ip-addresses`

Specifies a static IPv4 address, static IPv6 address range, or both, that are assigned to the forwarding rules of the load balancer. See Considerations for sharing a common IP address for important configuration requirements and implementation details. |  |  | 

  * `spec.loadBalancerIP`: All supported versions.
  * `networking.gke.io/load-balancer-ip-addresses`: GKE 1.29 and later. See Static IP address parameters for additional cluster configuration or annotation requirements.

  
Network Service Tiers | `cloud.google.com/network-tier` Specifies which [Network Service Tiers](https://docs.cloud.google.com/network-tiers/docs/overview) GKE uses for the external forwarding rule and IP address. The annotation valid values are `Standard` and `Premium` (default). |  |  | GKE 1.19 and later.  
Custom subnet | `networking.gke.io/load-balancer-subnet` |  |   
(only applies to IPv6) | GKE 1.29 and later. For additional requirements, see Custom subnet annotation.  
Bring your own IPv6 addresses (BYOIPv6) | `networking.gke.io/ip-collection-v6: "projects/PROJECT_ID/regions/REGION/publicDelegatedPrefixes/SUB_PREFIX_NAME"` Specifies a regional IPv6 sub-prefix of a public delegated prefix (PDP) in `EXTERNAL_IPV6_FORWARDING_RULE_CREATION` mode. From this sub-prefix, GKE allocates an ephemeral external `/96` IPv6 address range for a single-stack IPv6 external LoadBalancer Service. You can specify the sub-prefix as a full resource URL or as the partial resource path that's shown in the example. If you change this annotation, GKE re-creates the IPv6 forwarding rule with a new address from the new prefix. If you remove the annotation, the Service reverts to a Google-provided address from a subnet with an external IPv6 address range; if the cluster's subnet has an internal IPv6 address range, add the `networking.gke.io/load-balancer-subnet` annotation at the same time. For internal LoadBalancer Services, configure BYOIPv6 by specifying a BYOIPv6 internal subnet with the `networking.gke.io/load-balancer-subnet` annotation. |  |   
(only applies to single-stack IPv6) | GKE version 1.37.1-gke.2097000 and later  
Global access | `networking.gke.io/internal-load-balancer-allow-global-access: "true"` Enables the IP address of the forwarding rule to be accessible by clients in any region of the VPC network or a connected network. |  |  | Preview in GKE 1.16+. Generally available in GKE 1.17.9-gke.600+.  
All ports | GKE automatically configures the forwarding rule to use all ports if more than five (up to 100) unique ports are specified in `spec.ports[].port`. |  |  | GKE version 1.18.19-gke.1400 or later  
ipFamilyPolicy | `spec.ipFamilyPolicy` Defines how GKE allocates IP addresses to a Service. You can define the `spec.ipFamilyPolicy` as `SingleStack`, `PreferDualStack`, or `RequireDualStack`. To create a single-stack IPv6 LoadBalancer Service in a dual-stack cluster, set the value of this field to `SingleStack` and set the value of the `spec.ipFamilies` field to `IPv6`. In an IPv6-only cluster, these are the default values and you can omit them. For more information, see IPv6 LoadBalancer Services. |  |  | GKE clusters in version 1.29 or later support dual-stack network for LoadBalancer Services.   
  
Single-stack IPv6 LoadBalancer Services are available in Preview in GKE version 1.36.0-gke.2646000 and later.  
ipFamilies (Optional) | `spec.ipFamilies` Defines the IP address family to allocate either single-stack or dual-stack Services. Use any of the following values:

  * `IPv4` for single-stack IPv4 Service only.
  * `IPv6` for IPv6 Service only.
  * `IPv4,IPv6` for dual-stack Service where the primary IP address of the Service is IPv4.
  * `IPv6,IPv4` for dual-stack Service where the primary IP address of the Service is IPv6.

For a single-stack IPv6 LoadBalancer Service in a dual-stack cluster, set the value of this field to `IPv6` and set the value of the `spec.ipFamilyPolicy` field to `SingleStack`. In an IPv6-only cluster, these are the default values and you can omit them. For more information, see IPv6 LoadBalancer Services. |  |  | GKE clusters in version 1.29 or later support dual-stack network for LoadBalancer Services.   
  
Preview in GKE version 1.36.0-gke.2646000 and later for single-stack IPv6 LoadBalancer Services.  
  
### Health check port

As described in [Load balancer health checks](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#health_check), GKE always deploys a load balancer health check when it creates a regional external passthrough Network Load Balancer or internal passthrough Network Load Balancer.

Whether you can set up `healthCheckNodePort` parameter or not depends on the following `externalTrafficPolicy` configuration:

`externalTrafficPolicy` | Health check port  
---|---  
`Cluster` |  You cannot use `spec.healthCheckNodePort`.   
`Local` |  You can select a custom port by using the `spec.healthCheckNodePort`. If unspecified, the Kubernetes control plane assigns a health check port from the node port range.  **Note: Either the**`kube-proxy` software (on clusters that don't use GKE Dataplane V2) or `cilium-agent` (GKE Dataplane V2) responds to packets sent to the health check node port. Health checks for LoadBalancer Services cannot be answered by serving Pods.  
**Warning:** Don't customize the regional external passthrough Network Load Balancer or internal passthrough Network Load Balancer by modifying its health check resource outside of GKE. GKE does not offer any other customization parameters for load balancer health checks created for LoadBalancer Services.

### Firewall rules and source IP address allowlist

Unless you've configured a cluster to [skip creating VPC firewall rules for LoadBalancer Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/user-managed-firewall-rules), GKE creates an ingress allow [VPC firewall rule for each Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules#service-fws).

Each automatically created firewall rule has the following characteristics:

  * The firewall rule's direction is ingress, and its action is allow. The [implied deny ingress firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) in Google Cloud mean that GKE uses an allowlist model when creating ingress firewall rules.
  * GKE sets the firewall rule's protocol and destination port to those specified in the Service's `spec.ports[]` list.
  * GKE configures firewall rules for LoadBalancer Services by explicitly setting the [destination parameter](https://docs.cloud.google.com/firewall/docs/firewalls#destination_parameter_ingress_rule) to the virtual IP address of the LoadBalancer (the load balancer's forwarding rule).
  * GKE sets the [target parameter](https://docs.cloud.google.com/firewall/docs/firewalls#rule_assignment) of the firewall rule to include all nodes of the cluster.
  * If the Service includes `spec.loadBalancerSourceRanges[]`, GKE sets the firewall rule's [source parameter](https://docs.cloud.google.com/firewall/docs/firewalls#source_parameter_ingress_rule) to the IP addresses in that list. Additionally, GKE configures routes and rules within the node operating system to limit the source IP addresses for load-balanced traffic, using `kube-proxy` and `iptables` (on clusters that don't use GKE Dataplane V2) or `cilium-agent` and eBPF rules (on clusters with GKE Dataplane V2). If the Service does not include `loadBalancerSourceRanges[]`, GKE sets the firewall rule's source parameter to all IP addresses `(0.0.0.0/0)`.
  * For an IPv6 LoadBalancer Service, specify IPv6 CIDR ranges in the `spec.loadBalancerSourceRanges[]` field (for example, the `2001:db8::/32` range). GKE creates a separate firewall rule for the Service's IPv6 forwarding rule. If the Service doesn't include the `loadBalancerSourceRanges[]` field, GKE sets that firewall rule's source parameter to all IPv6 addresses `(::/0)`.



### Static IP addresses

You can [create a static IP address](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) and configure GKE to assign that static address to the load balancer's forwarding rule. Using a static IP address helps ensure that the load balancer's IP address remains the same even if you make changes to the LoadBalancer Service. Without a static IP address, GKE might assign a different IP address to the load balancer forwarding rule when you update a LoadBalancer Service. The forwarding rule IP address is _not_ the same as the Service's `spec.clusterIP` address. The ClusterIP address for a Service never changes when you update a LoadBalancer Service.

#### Static IP address parameters

To instruct a LoadBalancer Service to use a static IP address, use either the `spec.loadBalancerIP` parameter or the `networking.gke.io/load-balancer-ip-addresses` annotation. In GKE version 1.29 and later, the annotation takes precedence over `spec.loadBalancerIP` if the Service manifest contains both the parameter and the annotation.

Parameter or annotation and value | Requirements and capabilities  
---|---  
`spec.loadBalancerIP:`  
`IPv4_ADDRESS` | You can specify a static internal IPv4 address for an IPv4-only Internal LoadBalancer Service. You can specify a static external IPv4 address for an IPv4-only External LoadBalancer Service. The parameter works with all supported GKE versions.  
`networking.gke.io/load-balancer-ip-addresses:`  
`IP_ADDRESS_RESOURCE_NAME`

  * For single-stack LoadBalancer Services, set the value of the annotation to the IPv4 or IPv6 address resource _name_ , not the IP address itself.
  * For dual-stack LoadBalancer Services, set the value of the annotation to the static IPv4 address resource name and the static IPv6 address range resource name separated by a comma.

| You can specify static IPv4 address, static IPv6 address range, or both for IPv4-only, IPv6-only, and dual-stack Internal and External LoadBalancer Services. The annotation requires GKE 1.29 or later and the following additional requirements:

  * To use this annotation with an Internal LoadBalancer Service, your cluster must have [ GKE subsetting](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#subsetting) enabled. GKE subsetting is enabled by default in GKE version 1.36 and later.
  * To use this annotation with an External LoadBalancer Service, you must set the `spec.loadBalancerClass` field to the `networking.gke.io/l4-regional-external` value in the Service manifest when you create the External LoadBalancer Service.
  * For a single-stack IPv6 external LoadBalancer Service in GKE version 1.37.1-gke.2097000 and later, you can also reserve the static IPv6 address range from a regional BYOIPv6 public delegated prefix in `EXTERNAL_IPV6_FORWARDING_RULE_CREATION` mode.
  * For an internal LoadBalancer Service, you can reserve the static IPv6 address range from an internal subnet provisioned from a BYOIPv6 public delegated prefix in `INTERNAL_IPV6_SUBNETWORK_CREATION` mode.

  
  
#### Considerations for sharing a common IP address

Two or more LoadBalancer Services can reference the same static IP address if the forwarding rule for each load balancer uses a unique combination of IP address, protocol, port specification, and Network Service Tiers specification, as indicated in the table in this section. Additionally:

  * Static IPv6 addresses are actually `/96` IPv6 address ranges, but GKE only configures nodes to accept packets on the first IPv6 address (`/128`) in the `/96` range.

  * For two or more Internal LoadBalancer Services to use the same internal IPv4 address, the static IP address must be created with the `SHARED_LOADBALANCER_VIP` purpose.


| Internal LoadBalancer Service | External LoadBalancer Service  
---|---|---  
Port specification | Forwarding rules for internal passthrough Network Load Balancers support up to five individual port numbers, or they can be configured to use all ports. When an Internal LoadBalancer Service has more than five `spec.ports[]` specified, GKE configures the forwarding rule for the internal passthrough Network Load Balancer to use all ports. Forwarding rules with the same IP address and protocol cannot have overlapping ports. This means you cannot create multiple Internal LoadBalancer Services that share the same IP address, protocol, and port(s). For example:

  * If you create an Internal LoadBalancer Service using TCP port 80, you cannot create another Service using TCP ports 80, 81, and 90 because port 80 overlaps.
  * If an Internal LoadBalancer Service uses TCP ports 80, 8080, and 90, you cannot create another Service using TCP on all ports, as this would also result in overlapping ports

For more information, see: [ internal passthrough Network Load Balancer forwarding rules that use a common IP address](https://docs.cloud.google.com/load-balancing/docs/internal/multiple-forwarding-rules-same-ip#two-int-passthrough-network-lbs). | For clusters running GKE versions earlier than 1.37, GKE creates a target pool based regional external passthrough Network Load Balancer if the LoadBalancer Service manifest _doesn't_ have the `spec.loadBalancerClass` field set to the `networking.gke.io/l4-regional-external` value, or doesn't include the `cloud.google.com/l4-rbs: "enabled"` annotation. For clusters running GKE 1.37 or later, you must explicitly set `spec.loadBalancerClass: "networking.gke.io/l4-regional-external-legacy"` to create a target pool based regional external passthrough Network Load Balancer. Forwarding rules for target pool based regional external passthrough Network Load Balancers must use _contiguous_ port ranges. The contiguous port range includes all ports the Service needs, but the range might also include additional ports not used by the Service. For example, an External LoadBalancer Service powered by a target pool based regional external passthrough Network Load Balancer which specifies ports 80 and 443 in its Service manifest uses a load balancer forwarding rule with a _port range_ of 80-443. This port range prevents other External LoadBalancer Services from using any of the ports 80, 443, and any of the numbers between 80 and 443. GKE creates a backend service-based regional external passthrough Network Load Balancer by default in versions 1.37 or later. In earlier versions, GKE creates the load balancer if the LoadBalancer Service manifest _includes_ the `spec.loadBalancerClass` field set to the `networking.gke.io/l4-regional-external` value. Forwarding rules for backend service-based regional external passthrough Network Load Balancers support up to five discrete port numbers or a _contiguous_ port range.  
Network Service Tiers | Not configurable—internal addresses are always Premium tier. | Configurable for static regional external IPv4 addresses. Static regional external IPv6 address ranges can only be created in the Premium tier. The Network Service Tiers specification of the static external IP address must match either:

  * The tier specified in the LoadBalancer Service manifest's `cloud.google.com/network-tier` annotation, if that annotation is present in the manifest, or
  * The project's default tier, if the `cloud.google.com/network-tier` annotation is absent from the LoadBalancer Service manifest.

The project's default tier is Premium, unless you have configured it differently.  
  
#### IP address reservation

GKE doesn't reserve the static IP addresses configured using `spec.loadBalancerIP` or `networking.gke.io/load-balancer-ip-addresses` annotation. This means that the IP address you assign to your Service can be released when the Service is deleted.

To keep the IP address reserved, you must manually create an address resource in your project. The static IP address must have the following attributes:

  * Be regional only.
  * Be in the same region as the cluster.
  * Be in the same Network Service Tiers as the LoadBalancer Service.
  * Have a name which does doesn't use the LoadBalancer name, prefixes like `k8s-`, or the service's UUID.



If you don't reserve the address yourself, the project logs can contain entries about address resources created and shortly removed. This is a part of normal service provisioning and should be expected.

### LoadBalancer subnet

You can configure an Internal LoadBalancer Service to use an ephemeral or static IPv4 address, IPv6 address range, or both, in a custom subnet located in the same region and VPC network as the cluster. Use a custom subnet for an Internal LoadBalancer Service to:

  * Group internal passthrough Network Load Balancers created by Internal LoadBalancer Services from two or more GKE clusters in the same VPC network and region.
  * Create Internal LoadBalancer Services whose internal passthrough Network Load Balancers have IPv4 addresses separate from the cluster's node IPv4 addresses.
  * Create Internal LoadBalancer Services whose internal passthrough Network Load Balancers have IPv6 address ranges separate from the cluster's node and Pod IPv6 addresses. A custom LoadBalancer subnet is mandatory to support Internal LoadBalancer Services if the cluster's subnet has an _external_ IPv6 address range.



You can configure an External LoadBalancer Service to use an ephemeral or static IPv6 address range in a custom subnet located in the same region and VPC network as the cluster. Use a custom subnet to create External LoadBalancer Services whose regional external passthrough Network Load Balancers have IPv6 address ranges separate from the cluster's node and Pod IPv6 addresses. A custom LoadBalancer subnet is mandatory to support External LoadBalancer Services if the cluster's subnet has an _internal_ IPv6 address range.

IPv6 addresses for internal passthrough Network Load Balancers and regional external passthrough Network Load Balancers typically come from a subnet range in your VPC network. For single-stack IPv6 external LoadBalancer Services in GKE version 1.37.1-gke.2097000 and later, the IPv6 addresses can instead come from a BYOIPv6 public delegated prefix. When the address comes from a subnet, the IPv6 access type of that subnet must match the type of load balancer you create: internal LoadBalancer Services require a subnet with an _internal_ IPv6 address range (including subnets provisioned from a BYOIPv6 prefix), and external LoadBalancer Services require a subnet with an _external_ IPv6 address range. For a summary of when a custom LoadBalancer subnet is required, see IPv6 LoadBalancer Services.

**Note:** The custom subnet annotation has no effect on the selection of the external IPv4 address for an External LoadBalancer Service because IPv4 addresses for regional external passthrough Network Load Balancers are not sourced from subnet ranges of a VPC network.

#### Custom subnet annotation

Use the `networking.gke.io/load-balancer-subnet: SUBNET_RESOURCE_NAME` annotation to instruct a LoadBalancer Service to use an ephemeral or static IP address in a custom subnet, where `SUBNET_RESOURCE_NAME` is the name of the custom subnet. You can use this annotation to specify a custom subnet for an IPv4-only, IPv6-only, or dual-stack Internal LoadBalancer Service, or for an IPv6-only or dual-stack External LoadBalancer Service.

To use the `networking.gke.io/load-balancer-subnet` annotation, you must meet the following requirements:

  * Your cluster must run GKE version 1.29 or later.
  * To specify a custom subnet for an Internal LoadBalancer Service, your cluster must have [GKE subsetting](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#subsetting) enabled. GKE subsetting is enabled by default in versions 1.36 and later.
  * To specify a custom subnet for an External LoadBalancer Service, you must configure a backend-service based load balancer. In GKE version 1.37 and later, this configuration is the default behavior. In earlier versions, you must include the `spec.loadBalancerClass` field set to the `networking.gke.io/l4-regional-external` value in the Service manifest when you create the External LoadBalancer Service.
  * For [single-stack IPv6 clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/single-stack-ipv6) (created with the `--stack-type=ipv6` flag), you must use this annotation when the load balancer access type differs from your node subnetwork access type. For example, use this annotation when you deploy an External LoadBalancer Service on a cluster whose node subnetwork uses the `INTERNAL` IPv6 access type (ULA), or when you deploy an Internal LoadBalancer Service on a cluster whose node subnetwork uses the `EXTERNAL` IPv6 access type (GUA). The subnetwork specified by this annotation must have an IPv6 access type (`EXTERNAL` or `INTERNAL`) that matches the corresponding load balancer type. Alternatively, an external LoadBalancer Service can take its IPv6 address range from a BYOIPv6 public delegated prefix instead of a subnet; in that case, don't use this annotation.



#### Subnet and IPv4 address for an Internal LoadBalancer Service

The following table describes valid subnet specification and IPv4 address combinations for an IPv4-only or dual-stack Internal LoadBalancer Service.

| Static IPv4 address 

  * For IPv4-only, can be specified using either Static IP address parameter. 
  * For dual-stack, must be specified using the  `networking.gke.io/load-balancer-ip-addresses` annotation. 

| Ephemeral IPv4 address  
---|---|---  
Custom subnet  


  * Must be in the same VPC network and region as the cluster.
  * For IPv4-only, can be specified using either of the Custom subnet annotations.
  * For dual-stack, must be specified using the  `networking.gke.io/load-balancer-subnet` annotation.

| **Custom subnet and static IPv4 address** : The static internal IPv4 address must have been created in the custom subnet's primary IPv4 address range.  | **Custom subnet and ephemeral IPv4 address** : GKE uses an unallocated internal IPv4 address in the custom subnet primary IPv4 address range.   
Cluster subnet | **Cluster subnet and static IPv4 address** : The static internal IPv4 address must have been created in the cluster subnet's primary IPv4 address range.  | **Cluster subnet and ephemeral IPv4 address** : GKE uses an unallocated internal IPv4 address in the cluster subnet primary IPv4 address range.   
  
#### Subnet and IPv6 address range for an Internal LoadBalancer Service

The following table describes valid subnet specification and IPv6 address range combinations for an IPv6-only or dual-stack Internal LoadBalancer Service. Even though the internal passthrough Network Load Balancer IPv6 forwarding rule uses an internal `/96` IPv6 address range, GKE only configures nodes to accept packets whose destinations match the first IPv6 address (`/128`) of the forwarding rule's `/96` range.

| Static IPv6 address range 

  * Must be specified using the `networking.gke.io/load-balancer-ip-addresses` annotation

| Ephemeral IPv6 address range  
---|---|---  
Custom dual-stack or IPv6-only subnet  


  * Must be in the same VPC network and region as the cluster.
  * Must have an internal IPv6 address range (access type `INTERNAL`), which can be either a Google-provided internal IPv6 address range or a BYOIPv6 internal address range provisioned from a public delegated prefix that's in `INTERNAL_IPV6_SUBNETWORK_CREATION` mode.
  * Must be specified using the  `networking.gke.io/load-balancer-subnet` annotation.

| **Custom subnet and static IPv6 address range** : The static internal `/96` IPv6 address range must have been created in the custom subnet's internal `/64` IPv6 address range.  | **Custom subnet and ephemeral IPv6 address range** : GKE uses an unallocated internal `/96` IPv6 address range from the custom subnet's internal `/64` IPv6 address range.   
Cluster dual-stack or IPv6-only subnet 

  * Must have an internal IPv6 address range (access type `INTERNAL`), which can be either a Google-provided internal IPv6 address range or a BYOIPv6 internal address range.

| **Cluster subnet and static IPv6 address range** : The static internal `/96` IPv6 address range must have been created in the cluster subnet's internal `/64` IPv6 address range.  | **Cluster subnet and ephemeral IPv6 address range** : GKE uses an unallocated internal `/96` IPv6 address range from the cluster subnet's internal `/64` IPv6 address range.   
  
#### Subnet and IPv4 address for an External LoadBalancer Service

For IPv4-only and dual-stack External LoadBalancer Services, the external IPv4 address—whether a static external IPv4 address or an ephemeral external IPv4 address—doesn't come from a subnet.

#### Subnet and IPv6 address range for an External LoadBalancer Service

The following table describes the valid combinations of subnet or sub-prefix and IPv6 address range for a single-stack IPv6 or dual-stack external LoadBalancer Service. Even though the regional external passthrough Network Load Balancer IPv6 forwarding rule uses an external `/96` IPv6 address range, GKE only configures nodes to accept packets whose destinations match the first IPv6 address (`/128`) of the forwarding rule's `/96` range.

| Static IPv6 address range 

  * Must be specified using the `networking.gke.io/load-balancer-ip-addresses` annotation

| Ephemeral IPv6 address range  
---|---|---  
Custom dual-stack or IPv6-only subnet  


  * Must be in the same VPC network and region as the cluster.
  * Must have an external IPv6 address range (access type `EXTERNAL`).
  * Must be specified using the  `networking.gke.io/load-balancer-subnet` annotation.

| **Custom subnet and static IPv6 address range** : The static external `/96` IPv6 address range must have been created in the custom subnet's external `/64` IPv6 address range. Static external IPv6 address ranges can be created only in Premium tier.  | **Custom subnet and ephemeral IPv6 address range** : GKE uses an unallocated external `/96` IPv6 address range from the custom subnet's external `/64` IPv6 address range.   
Cluster dual-stack or IPv6-only subnet 

  * Must have an external IPv6 address range (access type `EXTERNAL`).

| **Cluster subnet and static IPv6 address range** : The static external `/96` IPv6 address range must have been created in the cluster subnet's external `/64` IPv6 address range. Static external IPv6 address ranges can be created only in Premium tier.  | **Cluster subnet and ephemeral IPv6 address range** : GKE uses an unallocated external `/96` IPv6 address range from the cluster subnet's external `/64` IPv6 address range.   
BYOIPv6 public delegated prefix  


  * Applies only to single-stack IPv6 external LoadBalancer Services in GKE version 1.37.1-gke.2097000 and later.
  * The regional sub-prefix must be in the same region as the cluster, must use the `EXTERNAL_IPV6_FORWARDING_RULE_CREATION` mode, and must have an allocatable prefix length of `/96`.
  * The sub-prefix must have the `ANNOUNCED` status.
  * Works on single-stack IPv6 clusters and on dual-stack clusters (the Service itself must be single-stack IPv6). The cluster's subnet can have either an internal or an external IPv6 address range (access type `INTERNAL` or `EXTERNAL`); no external IPv6 subnet is required because the address range comes from the sub-prefix.
  * Requires a backend-service based regional external passthrough Network Load Balancer (`spec.loadBalancerClass: networking.gke.io/l4-regional-external`) in Premium Tier.

| **BYOIPv6 prefix and static IPv6 address range** : You must reserve the static external `/96` IPv6 address range from the regional sub-prefix by using the `--endpoint-type=NETLB` and `--ip-collection` flags, and reference the static address by using the `networking.gke.io/load-balancer-ip-addresses` annotation. Optionally, you can also include the `networking.gke.io/ip-collection-v6` annotation; if you do, this annotation must reference the same sub-prefix that you reserved the static address from.  | **BYOIPv6 prefix and ephemeral IPv6 address range** : Specify the regional sub-prefix by using the `networking.gke.io/ip-collection-v6` annotation. GKE allocates an available external `/96` IPv6 address range from the sub-prefix.   
  
### Global access

When the `networking.gke.io/internal-load-balancer-allow-global-access` annotation is `false` or unspecified for an Internal LoadBalancer Service, GKE creates an internal passthrough Network Load Balancer whose forwarding rule has global access disabled. When global access is disabled, clients that need to access the load balancer must be located in the same region and VPC network, or a network connected to the cluster's VPC network.

When the `networking.gke.io/internal-load-balancer-allow-global-access` annotation is `true` for an Internal LoadBalancer Service, GKE enables the global access option on the internal passthrough Network Load Balancer's forwarding rule. Clients located in any region of the VPC network or a network connected to the cluster's VPC network can access the load balancer.

**Note:** If you use an [internal load balancer with Private Service Connect](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing-across-vpc-net#ilb_psc), you might face an error when you enable global access on the Service. To mitigate this issue, follow the steps outlined in [Error enabling global access](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing-across-vpc-net#global-access).

For more information about how global access applies to clients in a connected network, see:

  * [Client access](https://docs.cloud.google.com/load-balancing/docs/internal#client-access) in the internal passthrough Network Load Balancer documentation
  * [Internal passthrough Network Load Balancers and connected networks](https://docs.cloud.google.com/load-balancing/docs/internal/internal-tcp-udp-lb-and-other-networks)



### All ports forwarding rules

Forwarding rules for internal passthrough Network Load Balancers support five unique port numbers or all ports.

In GKE, an Internal LoadBalancer Service can only support up to 100 ports in the Service's `spec.ports[].port`. If an Internal LoadBalancer Service defines up to five ports, the forwarding rule will include those specific ports. However, if the Service specifies more than five ports, the forwarding rule will automatically be configured to match all ports. When configuring a forwarding rule to use all ports, GKE only creates ingress allow firewall rules for the specific ports configured in `spec.ports[].port` on the Service.

For more information about internal passthrough Network Load Balancer forwarding rules and valid port specifications, see [Forwarding rules and port specifications](https://docs.cloud.google.com/load-balancing/docs/internal#all_ports).

### IPv4/IPv6 dual-stack LoadBalancer Service

You can create an Internal or External LoadBalancer Service that can be single-stack (IPv4 only or IPv6 only) or dual-stack. Single-stack LoadBalancer Services create a single forwarding rule with either an IPv4 address or an IPv6 address. Dual-stack LoadBalancer Services create two forwarding rules: one with an IPv4 address, and another with an IPv6 address. To create a IPv4/IPv6 dual-stack LoadBalancer Service, deploy it on a [IPv4/IPv6 dual-stack cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#dual-stack) and complete any of the following depending on the type of load balancer you use:

  * For Internal LoadBalancer Services, you must have GKE subsetting enabled. GKE subsetting is enabled by default for single-stack IPv6 and dual-stack clusters. For more information, see enabling [Internal load balancer subsetting](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing#enable_ilb_subsetting_existing_cluster).
  * For External LoadBalancer Services, you must use a backend service-based regional external passthrough Network Load Balancer. For more information, see [backend service-based external Network Load Balancer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/backend-service-based-external-load-balancer).



For each Service, you can define `ipFamilyPolicy` and `ipFamilies` specs. To learn more, see [IPv4/IPv6 dual-stack](https://kubernetes.io/docs/concepts/services-networking/dual-stack/#services).

#### Restrictions of dual-stack LoadBalancer Services

  * LoadBalancer Services with IPv6 addresses aren't supported on clusters with the `ipv4` stack type. For more information, see [Use a dual-stack IP address for a VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#dual-stack) or [Configure a single-stack IPv6 cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/single-stack-ipv6).
  * LoadBalancer Services created with a single-stack address cannot be upgraded to dual-stack Services.

  * LoadBalancer Services created with a dual-stack addresses can be changed to single stack according to the following conditions:

    * A Service with ipFamilies `["IPv4","IPv6"]` can be changed to a Service with ipFamilies `IPv4` but not `IPv6`.
    * A Service with ipFamilies `["IPv6","IPv4"]` can be changed to a Service with ipFamilies `IPv6` but not `IPv4`.



### IPv6 LoadBalancer Services

An IPv6 LoadBalancer Service is a LoadBalancer Service whose forwarding rule has an IPv6 address. A Service can be single-stack IPv6, or dual-stack with both an IPv4 and an IPv6 forwarding rule. To create a single-stack IPv6 LoadBalancer Service in a dual-stack cluster, set the value of the `spec.ipFamilyPolicy` field to `SingleStack` and set the value of the `spec.ipFamilies` field to `IPv6`. In an IPv6-only cluster, these are the default values and you can omit them.

IPv6 LoadBalancer Services always use `GCE_VM_IP` NEG backends, and their IPv6 addresses come from a subnet range in your VPC network or from a bring your own IPv6 (BYOIPv6) public delegated prefix.

Single-stack IPv6 LoadBalancer Services are available in Preview in GKE version 1.36.0-gke.2646000 and later.

#### Restrictions of IPv6 LoadBalancer Services

  * You can't use the `spec.loadBalancerIP` field to specify an IPv6 address. Use the `networking.gke.io/load-balancer-ip-addresses` annotation instead.
  * External IPv6 LoadBalancer Services, including static external IPv6 address ranges, are supported only in [Premium Tier](https://docs.cloud.google.com/network-tiers/docs/overview). GKE rejects external IPv6 LoadBalancer Services that set the `cloud.google.com/network-tier: Standard` annotation.
  * You can't change a single-stack IPv6 LoadBalancer Service to use an IPv4 address. Setting the value of the `spec.ipFamilies` field to `IPv4` or setting the value of the `spec.ipFamilyPolicy` field to `RequireDualStack` is rejected.
  * You can use the `networking.gke.io/ip-collection-v6` annotation only on single-stack IPv6 external LoadBalancer Services in GKE version 1.37.1-gke.2097000 and later. GKE doesn't support the `networking.gke.io/ip-collection-v6` annotation for dual-stack Services, IPv4 Services, or internal LoadBalancer Services, and you can't combine this annotation with the `networking.gke.io/load-balancer-subnet` annotation.



#### Choose a subnet for the load balancer

The IPv6 access type of the subnet that provides the load balancer's IP address must match the type of load balancer. If the cluster's subnet already has the required access type, GKE uses the cluster's subnet. Otherwise, you must create a custom LoadBalancer subnet with the required access type and specify this subnet with the `networking.gke.io/load-balancer-subnet` annotation. The only exception is an external LoadBalancer Service that uses a BYOIPv6 public delegated prefix because that prefix provides the IPv6 address range regardless of the cluster subnet's access type.

The following table summarizes which subnet or prefix provides the IPv6 address range of the load balancer:

LoadBalancer Service type | IPv6 access type of the cluster's subnet | Source of the load balancer's IPv6 address range  
---|---|---  
Internal | `INTERNAL` | The cluster's subnet. No annotation is required.  
Internal | `EXTERNAL` | A custom LoadBalancer subnet with an `INTERNAL` IPv6 access type, specified with the `networking.gke.io/load-balancer-subnet` annotation.  
Internal with BYOIPv6 | `INTERNAL` or `EXTERNAL` | A subnet whose internal IPv6 address range comes from a BYOIPv6 public delegated prefix in `INTERNAL_IPV6_SUBNETWORK_CREATION` mode, specified with the `networking.gke.io/load-balancer-subnet` annotation (no annotation is required if that subnet is the cluster's subnet).  
External | `EXTERNAL` | The cluster's subnet. No annotation is required.  
External | `INTERNAL` | A custom LoadBalancer subnet with an `EXTERNAL` IPv6 access type, specified with the `networking.gke.io/load-balancer-subnet` annotation.  
External with BYOIPv6  
(GKE 1.37.1-gke.2097000 and later) | `INTERNAL` or `EXTERNAL` | A BYOIPv6 public delegated prefix in `EXTERNAL_IPV6_FORWARDING_RULE_CREATION` mode, specified with the `networking.gke.io/ip-collection-v6` annotation or by a static IPv6 address reserved from the prefix. Don't specify the `networking.gke.io/load-balancer-subnet` annotation.  
  
For the valid combinations of subnet and IPv6 address range, see Subnet and IPv6 address range for an Internal LoadBalancer Service and Subnet and IPv6 address range for an External LoadBalancer Service.

#### Bring your own IPv6 addresses (BYOIPv6)

You can use [bring your own IPv6 addresses (BYOIPv6)](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip) with both internal and external IPv6 LoadBalancer Services.

For external LoadBalancer Services, which allocate addresses directly from a public delegated prefix, the [GKE service agent](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts#gke-service-agents) (`service-PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com`) requires specific Identity and Access Management (IAM) permissions. Grant the Compute Public IP Admin role (`roles/compute.publicIpAdmin`) to this agent on the project that owns the public delegated prefix. This role includes the `compute.publicDelegatedPrefixes.use` permission.

GKE requires this permission both during initial Service creation and each time it syncs the Service.

**External LoadBalancer Services (GKE version 1.37.1-gke.2097000 and later)** : single-stack IPv6 external LoadBalancer Services (`spec.ipFamilyPolicy: SingleStack` and `spec.ipFamilies: ["IPv6"]`) allocate external `/96` BYOIPv6 address ranges directly from a regional IPv6 sub-prefix of a public delegated prefix (PDP). GKE supports this feature on both single-stack IPv6 clusters and dual-stack clusters, provided that the Service is single-stack IPv6. The cluster's subnet can have either an internal or an external IPv6 access type, because the address range originates from the sub-prefix rather than a subnet.

The regional IPv6 sub-prefix must meet the following requirements:

  * Configured with the `EXTERNAL_IPV6_FORWARDING_RULE_CREATION` mode
  * Configured with an allocatable prefix length of `/96`
  * In the `ANNOUNCED` status



To allocate an ephemeral external BYOIPv6 address range, specify the sub-prefix in the `networking.gke.io/ip-collection-v6` annotation (provided as a full resource URL or the partial resource path `projects/PROJECT_ID/regions/REGION/publicDelegatedPrefixes/SUB_PREFIX_NAME`). Alternatively, to use a static external BYOIPv6 address range that you reserved from the sub-prefix, use the `networking.gke.io/load-balancer-ip-addresses` annotation.

If you change the `networking.gke.io/ip-collection-v6` annotation, GKE re-creates the IPv6 forwarding rule with a new address from the new prefix, which briefly disrupts traffic. If you remove the annotation, the Service reverts to a Google-provided address from a subnet with an external IPv6 address range. If your cluster subnet uses an internal IPv6 address range, to avoid errors, you must simultaneously add the `networking.gke.io/load-balancer-subnet` annotation. For more information, see [Use bring your own IPv6 addresses (BYOIPv6) for an external LoadBalancer Service](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/backend-service-based-external-load-balancer#create-ipv6-byoip).

**Internal LoadBalancer Services** : IPv6 internal LoadBalancer Services use BYOIPv6 addresses from an internal IPv6 subnet. You create this subnet from a regional IPv6 sub-prefix of a public delegated prefix (PDP) configured in `INTERNAL_IPV6_SUBNETWORK_CREATION` mode. For more information, see [Create and use IPv6 sub-prefixes](https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes).

To configure the Service, specify the BYOIPv6 subnet by using the `networking.gke.io/load-balancer-subnet` annotation, or use that subnet as the cluster's default subnet. Optionally, specify a reserved static internal BYOIPv6 address by using the `networking.gke.io/load-balancer-ip-addresses` annotation.

Internal LoadBalancer Services don't support the `networking.gke.io/ip-collection-v6` annotation. If you apply this annotation, GKE ignores it and emits an `IPCollectionV6Error` warning event. For more information, see [Use bring your own IPv6 addresses (BYOIPv6) for an internal LoadBalancer Service](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing#create-ipv6-byoip).

## What's next

  * Learn about [LoadBalancer Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer).
  * Learn how to set up an [internal load balancer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing).
  * Read an overview of [Ingress for Application Load Balancers](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress).
  * Learn how to use [standalone NEGs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg).
  * Learn more about [VPC firewall rules](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 

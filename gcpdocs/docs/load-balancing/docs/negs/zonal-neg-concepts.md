---
url: https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts/
title: Zonal network endpoint groups overview \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T10:05:31.708746+00:00
---

# Zonal network endpoint groups overview  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Zonal network endpoint groups overview Stay organized with collections  Save and categorize content based on your preferences. 

A network endpoint group (NEG) is a collection of network endpoints. Every endpoint in a NEG must point to a unique IP address of a VM's network interface. A network endpoint belongs to exactly one network endpoint group. A single IP address _cannot_ be referenced by more than one endpoint in a NEG. However, a single IP address can be referenced by endpoints in different NEGs. The following diagram presents a stylized representation of this concept. In the diagram, "IP address - 2" and "IP address - 3" are referenced by network endpoints that are located in different network endpoint groups.

[ ![A network endpoint group is a collection of network endpoints.](https://docs.cloud.google.com/static/load-balancing/images/zonal-negs.svg)](https://docs.cloud.google.com/static/load-balancing/images/zonal-negs.svg) Network endpoint group (click to enlarge).

Zonal NEGs are [zonal](https://docs.cloud.google.com/compute/docs/regions-zones) resources that represent collections of either IP addresses or IP address and port combinations for Google Cloud resources within a single VPC subnet. Zonal NEGs let you do the following:

  * Route packets to any network interface of a VM instance, including interfaces other than `nic0`. This lets you create logical groupings of IP addresses and ports representing software services instead of entire VMs.

  * Create a flexible set of unique endpoint IP addresses or IP addresses and ports.




There are two types of zonal NEGs, depending on the type of network endpoints that make up the NEG. The two types of zonal NEGs support different use cases and load balancer types.

  * Zonal NEGs with `GCE_VM_IP` endpoints are supported as backends for the following load balancers:

    * [Global external passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture)
    * [Regional external passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service)
    * [Internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal)
  * Zonal NEGs with `GCE_VM_IP_PORT` endpoints are supported as backends for the following proxy-based load balancers:

    * [External Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https)
    * [Internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal)
    * [External proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp)
    * [Internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy)



## NEGs with `GCE_VM_IP` endpoints

These zonal NEGs contain one or more `GCE_VM_IP` endpoints with each endpoint having one of the following IP addresses:

  * The primary internal IPv4 address of a Compute Engine VM's network interface.
  * The first IPv6 address (`/128`) from a `/96` range assigned to a Compute Engine VM's network interface.



With a `GCE_VM_IP` endpoint, you select the primary internal IPv4 address or the first IPv6 address of a network interface, which provides a level of granularity similar to selecting a network interface directly.

A `GCE_VM_IP` endpoint can't point to an IP address from an [alias IPv4 range](https://docs.cloud.google.com/vpc/docs/alias-ip). The network interface referenced by the `GCE_VM_IP` endpoint must be in the same subnet as the NEG.

As depicted in the following table, `GCE_VM_IP` endpoints can reference a [VM's network interface whose stack type can be IPv4-only, IPv6-only, or dual-stack](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#stack-types). You _cannot_ add an endpoint that is simultaneously IPv4 and IPv6 (a dual-stack endpoint) to a `GCE_VM_IP` zonal NEG. In other words, you can only use a single IP address when creating a `GCE_VM_IP` endpoint.

Network endpoint | Compatible VM network interface  
---|---  
IPv4 endpoint (primary) | IPv4-only interface  
IPv4 endpoint (primary) | Dual-stack interface  
IPv6 endpoint (first in range) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) | IPv6-only interface  
IPv6 endpoint (first in range) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) | Dual-stack interface  
  
Because a `GCE_VM_IP` endpoint identifies a network interface, you _cannot_ specify a port with a `GCE_VM_IP` endpoint.

These types of endpoints can only be used as backends in [backend services](https://docs.cloud.google.com/load-balancing/docs/backend-service) for internal passthrough Network Load Balancers and regional external passthrough Network Load Balancers.

## NEGs with `GCE_VM_IP_PORT` endpoints

These zonal NEGs contain one or more `GCE_VM_IP_PORT` endpoints with each endpoint having one of the following IP address combinations along with the destination port:

  * **Primary IPv4 address + port** : the primary internal IPv4 address of a VM network interface plus a destination port number

  * **Alias IPv4 address + port** : an internal IPv4 address from the alias IP address range assigned to a VM network interface plus a destination port number

  * **Primary IPv4 address + any IPv6 address + port** : the primary internal IPv4 address of a VM network interface and any IPv6 address (`/128`) from a `/96` range assigned to a VM network interface plus a destination port number

  * **Alias IPv4 address + any IPv6 address + port** : an internal IPv4 address from the alias IP address range assigned to a VM network interface and any IPv6 address (`/128`) from a `/96` range assigned to a VM network interface plus a destination port number

  * **IPv6 address + port** : any IPv6 address (`/128`) from a `/96` range assigned to a VM network interface plus a destination port number




Compared to a `GCE_VM_IP` endpoint, with a `GCE_VM_IP_PORT` endpoint you can select not only the primary IP address of a network interface but any IP address, so the level of granularity that a `GCE_VM_IP_PORT` endpoint provides is greater than just selecting a network interface.

The network interface referenced by the `GCE_VM_IP_PORT` endpoint must be in the same subnet as the NEG. When you omit a port number from a `GCE_VM_IP_PORT` endpoint, Google Cloud uses the NEG's default port number for the endpoint.

As depicted in the following table, `GCE_VM_IP_PORT` endpoints can reference a [VM's network interface whose stack type can be IPv4-only, IPv6-only, or dual-stack](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#stack-types).

Network endpoint | Compatible VM network interface  
---|---  
IPv4 endpoint (primary or alias) | IPv4-only interface  
IPv4 endpoint (primary or alias) | Dual-stack interface  
IPv6 endpoint (any from a `/96` range) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) | IPv6-only interface  
IPv6 endpoint (any from a `/96` range) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) | Dual-stack interface  
IPv4 (primary or alias) and IPv6 (any from a `/96` range) endpoint Also referred to as a dual-stack endpoint | Dual-stack interface  
  
Because these zonal NEG backends let you specify IP addresses and ports, you can distribute traffic in a granular fashion among applications or containers running _within_ VM instances—container-native load balancing. GKE uses `GCE_VM_IP_PORT` endpoints for:

  * [GKE Ingress for Application Load Balancers](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress)
  * [Kubernetes Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api)



You can create self-managed load balancers that use zonal NEGs whose `GCE_VM_IP_PORT` endpoints are managed by GKE. For more information, see [Container-native load balancing through standalone zonal NEGs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg).

Application Load Balancers and proxy Network Load Balancers support zonal NEGs with `GCE_VM_IP_PORT` endpoints.

## Endpoint specifications

Each endpoint that you add to a zonal NEG must be a unique [load balancer target interface](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#load-balancers). Each zonal NEG supports up to the [maximum number of endpoints per NEG](https://docs.cloud.google.com/load-balancing/docs/quotas#endpoints_per_neg).

### `GCE_VM_IP` zonal NEG backends and network interfaces

When you create a new zonal NEG with `GCE_VM_IP` endpoints, you specify a zone, a VPC network, and a subnet in that network. None of these attributes can be changed after the zonal NEG has been created.

The NEG's subnet must be in the same region as the NEG's zone. If the NEG's network is an auto mode VPC network, you can omit specifying the NEG's subnet. When you don't specify a subnet, Google Cloud sets the NEG's subnet to the automatically created subnet in the region that contains the NEG's zone.

Zonal NEGs with `GCE_VM_IP` endpoints enforce the following rules for adding endpoints:

  * If you specify only an instance name for the endpoint, the instance must be in the same zone as the NEG and have a load balancer target interface in the NEG's subnet. If the endpoint references an IPv4-only or a dual-stack network interface, the primary internal IPv4 address of the instance's network interface is selected as the endpoint IP address. If the endpoint references an IPv6-only network interface, the first IPv6 address (`/128`) of the instance's network interface is selected as the endpoint IP address.

  * If you specify both an instance name and an IP address for adding an endpoint, the instance must be in the same zone as the NEG. The IP address must be set to the primary internal IPv4 address or the first IPv6 address (`/128`) of the instance's network interface.




Since an instance can have only one NIC in the NEG's subnet, it can have only one `GCE_VM_IP` endpoint per zonal NEG. For `GCE_VM_IP` endpoints, the endpoint IP address is a redundant label whose value must be a primary internal IPv4 address or the first IPv6 address (`/128`) of a load balancer target interface. The actual destination IP addresses of load-balanced packets match a passthrough Network Load Balancer forwarding rule.

### `GCE_VM_IP_PORT` zonal NEG backends and network interfaces

When you create a new zonal NEG with `GCE_VM_IP_PORT` endpoints, you specify a zone, a default port, a VPC network, and a subnet in that network. None of these attributes can be changed after the zonal NEG has been created.

The NEG's subnet must be in the same region as the NEG's zone. If the NEG's network is an auto mode VPC network, you can omit specifying the NEG's subnet. When you don't specify a subnet, Google Cloud sets the NEG's subnet to the automatically created subnet in the region that contains the NEG's zone.

Zonal NEGs with `GCE_VM_IP_PORT` endpoints enforce the following rules for adding endpoints:

  * If you specify only an instance name for the endpoint, the instance must be in the same zone as the NEG and have a load balancer target interface in the NEG's subnet. The endpoint's IP address is set to the primary internal IPv4 address of the load balancer target interface, and the endpoint's port is set to the NEG's default port.

  * If you specify an instance name and an IP address, or an instance name, an IP address, and port information for the endpoint, the instance must be in the same zone as the NEG, and:

    * If you specify an IPv4 address, the IPv4 address must be a primary internal IPv4 address or an IPv4 address from an alias IP range that's associated with a load balancer target interface in the NEG's subnet.

    * If you specify an IPv6 address, the IPv6 address must be a single IPv6 address (`/128`) from the `/96` IPv6 address range of the load balancer target interface in the NEG's subnet.

    * The endpoint's port is the port you specify. If you don't specify a port, the endpoint's port is set to the NEG's default port.




## Load balancing with zonal NEGs

Zonal NEGs can be used as backend groups connected to a [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service) in a load balancer. When you use a zonal NEG as a backend group, the backend service's other backend groups must be zonal NEGs with the same type of endpoints (either all `GCE_VM_IP` or `GCE_VM_IP_PORT`). You cannot use both instance groups and zonal NEGs as backend groups on the same backend service.

You can add the same network endpoint to more than one zonal NEG. You can also use the same zonal NEG as a backend for more than one backend service.

Zonal NEGs with `GCE_VM_IP_PORT` endpoints are supported by proxy-based load balancers with the balancing modes as defined in [Balancing modes for Application Load Balancers and Cloud Service Mesh](https://docs.cloud.google.com/load-balancing/docs/backend-service#applb-csm) and [Balancing modes for Proxy Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/backend-service#proxy-net-lb).

Zonal NEGs with `GCE_VM_IP` endpoints are are supported by passthrough Network Load Balancers, with the balancing modes as defined in [Balancing modes for passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/backend-service#pass-net-lb).

### Flexible endpoint grouping

Like instance groups, you can use the same NEG as a backend for multiple passthrough Network Load Balancers. Unlike instance groups, a NEG endpoint can be a member of multiple NEGs, and each of those NEGs can be used as a backend for one or more passthrough Network Load Balancers. Compared to instance groups, you aren't constrained by the fact that a VM instance can only be a part of a single instance group.

The following figure shows a sample internal passthrough Network Load Balancer architecture with a shared VM.

[ ![Internal passthrough Network Load Balancers with overlapping `GCE_VM_IP` zonal NEGs.](https://docs.cloud.google.com/static/load-balancing/images/l4ilb-zonal-neg-overlap.svg)](https://docs.cloud.google.com/static/load-balancing/images/l4ilb-zonal-neg-overlap.svg) Internal passthrough Network Load Balancers with overlapping zonal NEGs (click to enlarge).

### Load balanced network interfaces and endpoints

Zonal NEGs support distributing load-balanced traffic to `nic0` vNICs, non-`nic0` vNICs, and Dynamic NICs. For more information, see [load balancer target interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#load-balancers).

For information about using zonal NEGs with passthrough Network Load Balancers, see the following documents:

  * [Zonal NEG backends and network interfaces for global external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture#neg-nic-net)

  * [Zonal NEG backends and network interfaces for regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#neg-nic-net)

  * [Zonal NEG backends and network interfaces for internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal#neg-nic-net)




### GKE and zonal NEGs

GKE uses zonal NEGs with `GCE_VM_IP` and `GCE_VM_IP_PORT` endpoints:

  * GKE creates a unique `GCE_VM_IP` NEG in each zone for each LoadBalancer Service. These NEGs contain cluster node VMs as endpoints, which GKE selects based on the `externalTrafficPolicy` of the service and the number of nodes in the cluster. For more information, see [Node grouping](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#endpoint-grouping) in _About LoadBalancer Services_ document.

  * GKE Gateway and Ingress controllers use `GCE_VM_IP_PORT` NEGs to route traffic directly to Pods ([container-native load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-load-balancing#what_is_container-native_load_balancing)). Each endpoint in a `GCE_VM_IP_PORT` NEG contains a Pod's IP address and container port (`targetPort`). The way GKE creates these NEGs depends on the Gateway or Ingress resource that you use:

    * **Internal and external Gateway** : GKE creates `GCE_VM_IP_PORT` NEGs automatically for each referenced Service. See [About Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api).

    * **Internal Ingress** : GKE creates `GCE_VM_IP_PORT` NEGs automatically for each referenced Service. See [Configure Ingress for internal Application Load Balancer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balance-ingress).

    * **External Ingress** : GKE creates `GCE_VM_IP_PORT` NEGs for each referenced Service that includes the `cloud.google.com/neg: '{"ingress": true}'` annotation. See [Configure Ingress for external Application Load Balancer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/load-balance-ingress).

  * You can instruct GKE to create standalone `GCE_VM_IP_PORT` NEGs and maintain their Pod endpoints so that you can attach those NEGs as backends to Application Load Balancers and proxy Network Load Balancers that you manage yourself. For more information, see [Container-native load balancing through standalone zonal NEGs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg).




## Limitations

  * You cannot use zonal NEGs with legacy networks.
  * The [`default-port` property](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/create) is not supported for `GCE_VM_IP` zonal NEGs.



## Quotas

  * For information about NEG quotas—such as NEGs per project, NEGs per backend service, and endpoints per NEG—see the [load balancing quotas page](https://docs.cloud.google.com/load-balancing/docs/quotas).



## What's next

  * For information about configuring zonal NEGs, see [Set up zonal network endpoint groups](https://docs.cloud.google.com/load-balancing/docs/negs/setting-up-zonal-negs).
  * For information about using zonal NEGs in Google Kubernetes Engine, see [Container-native load balancing through Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/container-native-load-balancing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-06 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/service-mesh/docs/security/configuring-mtls/
title: Configure transport security \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T06:14:15.444292+00:00
---

# Configure transport security  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/security/configuring-mtls/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure transport security

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

You can secure inter-service traffic in Cloud Service Mesh with Istio APIs by enforcing strict mutual TLS (mTLS). In Kubernetes workloads, auto mTLS is enabled by default: client sidecar proxies automatically send mTLS traffic to sidecars, but destination services still accept both plaintext and encrypted requests.

`PeerAuthentication` policies let you restrict services to only accept mTLS. You can apply a policy mesh-wide, to a specific namespace, or to an individual workload. For supported fields across platforms, see [Supported features (managed control plane)](https://docs.cloud.google.com/service-mesh/docs/supported-features-managed#peer_authentication), [API support in managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/onboarding/api-support#peerauthentication), and [Supported features (in-cluster control plane)](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster).

## Enable mutual TLS per namespace

To enable mTLS for all workloads within a particular namespace, use a namespace-wide authentication policy. You specify the namespace it applies to under `metadata`.
    
    
    kubectl apply -f - <<EOF
    apiVersion: "security.istio.io/v1beta1"
    kind: "PeerAuthentication"
    metadata:
      name: "AUTH_POLICY_NAME"
      namespace: "NAMESPACE"
    spec:
      mtls:
        mode: STRICT
    EOF
    

Expected output: 
    
    
    peerauthentication.security.istio.io/AUTH_POLICY_NAME created

## Enable mutual TLS per workload

To set a `PeerAuthentication` policy for a specific workload, you must configure the `selector` section and specify the labels that match the targeted workload. However, Cloud Service Mesh can't aggregate workload-level policies for outbound mTLS traffic to a service. You need to configure a destination rule to manage that behavior.

  1. Apply an authentication policy to a specific workload in your namespace:
         
         cat <<EOF | kubectl apply -n NAMESPACE -f -
         apiVersion: "security.istio.io/v1beta1"
         kind: "PeerAuthentication"
         metadata:
           name: "AUTH_POLICY_NAME"
           namespace: "NAMESPACE"
         spec:
           selector:
             matchLabels:
               app: WORKLOAD
           mtls:
             mode: STRICT
         EOF
         

Expected output:
         
         peerauthentication.security.istio.io/AUTH_POLICY_NAME created

  2. Configure a matching destination rule:
         
         cat <<EOF | kubectl apply -n NAMESPACE -f -
         apiVersion: "networking.istio.io/v1beta1"
         kind: "DestinationRule"
         metadata:
           name: "DEST_RULE_NAME"
         spec:
           host: "WORKLOAD.NAMESPACE.svc.cluster.local"
           trafficPolicy:
             tls:
               mode: ISTIO_MUTUAL
         EOF
         

Expected output:
         
         destinationrule.networking.istio.io/DEST_RULE_NAME created




## Enforce mesh-wide mTLS

To prevent all your services in the mesh from accepting plain-text traffic, set a mesh-wide `PeerAuthentication` policy with the mTLS mode set to `STRICT` (the default is `PERMISSIVE`). The mesh-wide `PeerAuthentication` policy shouldn't have a selector and must be applied in the root namespace, `istio-system`. When you deploy the policy, the control plane automatically provisions TLS certificates so that workloads can authenticate with each other.

To enforce mesh-wide mTLS:
    
    
    kubectl apply -f - <<EOF
    apiVersion: "security.istio.io/v1beta1"
    kind: "PeerAuthentication"
    metadata:
      name: "AUTH_POLICY_NAME"
      namespace: "istio-system"
    spec:
      mtls:
        mode: STRICT
    EOF
    

Expected output: 
    
    
    peerauthentication.security.istio.io/AUTH_POLICY_NAME created

### Disable mTLS

Managed Cloud Service Mesh with the `TRAFFIC_DIRECTOR` control plane doesn't support `DISABLE` mode in `PeerAuthentication` resources (`mtls.mode: DISABLE` or `portLevelMtls.mode: DISABLE`).

To send plaintext traffic to a specific service or port in managed Cloud Service Mesh, configure both the server-side and client-side proxies:

  1. **Server-side (`PeerAuthentication`)**: Ensure the destination workload accepts plaintext traffic by using `PERMISSIVE` mode. If your mesh or namespace uses the default `PERMISSIVE` policy, you don't need to create a `PeerAuthentication` resource. If you enforced mesh-wide or namespace-wide `STRICT` mTLS, apply a workload-specific or port-specific `PeerAuthentication` policy set to `PERMISSIVE`.
  2. **Client-side (`DestinationRule`)**: Configure a `DestinationRule` resource with `tls.mode: DISABLE` so client sidecar proxies send plaintext traffic when calling that service or port.



NOTE: Because the server-side proxy uses `PERMISSIVE` mode instead of `DISABLE`, the destination workload still accepts mTLS traffic from any client not covered by the `DestinationRule`. To ensure all mesh clients send plaintext, create the `DestinationRule` in the destination service's namespace (or `istio-system`) without restricting `exportTo`.

#### Example: Disable mTLS for a service

  1. If your mesh or namespace enforces `STRICT` mTLS, allow the target workload (or specific port) to accept plaintext traffic by setting its `PeerAuthentication` mode to `PERMISSIVE`:
         
         cat <<EOF | kubectl apply -n NAMESPACE -f -
         apiVersion: "security.istio.io/v1beta1"
         kind: "PeerAuthentication"
         metadata:
           name: "AUTH_POLICY_NAME"
           namespace: "NAMESPACE"
         spec:
           selector:
             matchLabels:
               app: WORKLOAD
           mtls:
             mode: PERMISSIVE
         EOF
         

To allow plaintext only on a specific workload port (for example, when migrating from `portLevelMtls`), set `portLevelMtls` instead:
         
         spec:
           selector:
             matchLabels:
               app: WORKLOAD
           mtls:
             mode: STRICT
           portLevelMtls:
             WORKLOAD_PORT:
               mode: PERMISSIVE
         

  2. Configure a `DestinationRule` to instruct client proxies to send plaintext traffic to the target service:
         
         cat <<EOF | kubectl apply -n NAMESPACE -f -
         apiVersion: "networking.istio.io/v1beta1"
         kind: "DestinationRule"
         metadata:
           name: "DEST_RULE_NAME"
           namespace: "NAMESPACE"
         spec:
           host: "SERVICE_NAME.NAMESPACE.svc.cluster.local"
           trafficPolicy:
             tls:
               mode: DISABLE
         EOF
         

To disable mTLS only for a specific service port, use `portLevelSettings` in the `DestinationRule`:
         
         spec:
           host: "SERVICE_NAME.NAMESPACE.svc.cluster.local"
           trafficPolicy:
             portLevelSettings:
             - port:
                 number: SERVICE_PORT
               tls:
                 mode: DISABLE
         




## Find and delete `PeerAuthentication` policies

For a list of all the `PeerAuthentication` policies in the service mesh:
    
    
    kubectl get peerauthentication --all-namespaces
    

If there is a `PeerAuthentication` policy in force, you can delete it with `kubectl delete`:
    
    
    kubectl delete peerauthentication -n NAMESPACE AUTH_POLICY_NAME
    

## What's next

  * [Cloud Service Mesh by example: mTLS](https://docs.cloud.google.com/service-mesh/docs/tutorials/mtls)
  * [Learn about security in Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/security/security-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 

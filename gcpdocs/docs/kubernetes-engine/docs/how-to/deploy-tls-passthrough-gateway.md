---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-tls-passthrough-gateway/
title: Deploy a TLS passthrough Gateway \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T05:52:41.539773+00:00
---

# Deploy a TLS passthrough Gateway  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-tls-passthrough-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Deploy a TLS passthrough Gateway Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows you how to deploy a Kubernetes Gateway resource configured for TLS passthrough to enable Server Name Indication (SNI)-based routing in Google Kubernetes Engine (GKE). This approach preserves end-to-end encryption and mutual TLS (mTLS) between clients and backend Pods, supports non-HTTP TLS-based protocols, and conserves IP addresses.

This document is for Cloud architects, Networking specialists, and Developers who design, deploy, and manage encrypted networking for containerized workloads. To learn more about common roles and example tasks, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Overview

In addition to Layer 7 HTTP and HTTPS Application Load Balancers, the [GKE Gateway controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api) supports Layer 4 proxy Network Load Balancers (TCP proxy load balancers) configured with TLS passthrough.

With TLS passthrough, the load balancer does not terminate or decrypt the TLS session. Instead, when a client initiates a TLS handshake, the load balancer inspects the unencrypted `ClientHello` message to read the Server Name Indication (SNI) hostname. Based on this SNI hostname, the load balancer routes the raw, encrypted TCP stream to the appropriate backend Kubernetes Service, where your application Pods terminate TLS directly.

When you use TLS passthrough with the Gateway API, you can do the following:

  * **Maintain end-to-end encryption and support zero-trust compliance:** keep traffic fully encrypted from the client to the backend Pod without giving the load balancer access to private keys or plaintext data.
  * **Use mutual TLS (mTLS) authentication:** authenticate clients directly at the backend application layer.
  * **Conserve IPv4 addresses:** multiplex multiple independent TLS services across distinct domains or subdomains by using a single Gateway IP address and port (such as `443`).
  * **Support non-HTTP TLS-based protocols:** route encrypted traffic for stateful workloads, databases, custom gRPC services, or proprietary protocols running over TLS.



### Supported GatewayClasses

The following GKE GatewayClasses support TLS passthrough listeners and TLSRoute resources:

  * `gke-l7-regional-external-managed`
  * `gke-l7-regional-external-managed-mc`
  * `gke-l7-rilb`
  * `gke-l7-rilb-mc`
  * `gke-l7-cross-regional-internal-managed-mc`

**Note:** The `gke-l7-global-external-managed` GatewayClass, `gke-l7-global-external-managed-mc` GatewayClass, and classic GatewayClasses (`gke-l7-gxlb` and `gke-l7-gxlb-mc`) don't support TLS passthrough or TLSRoute resources.

For a full comparison of GatewayClass capabilities, see [GatewayClass capabilities](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Verify that you have an existing Autopilot or Standard cluster running GKE version 1.35 or later with Gateway API enabled. To create a cluster, see [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster). To enable Gateway API on an existing cluster, see [Enable Gateway API in your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#enable-gateway).
  * Verify that you have the [OpenSSL](https://www.openssl.org/docs/) command-line tool installed. You use this tool to generate self-signed TLS certificates for the sample applications.



### GKE Gateway controller requirements

  * Gateway API is supported on [VPC-native](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips) clusters only.
  * If you are using the regional or cross-region GatewayClasses, you must enable a [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets).
  * Your cluster must have the `HttpLoadBalancing` add-on enabled.
  * If you are using Istio, you must upgrade Istio to one of the following versions: 
    * 1.15.2 or later
    * 1.14.5 or later
    * 1.13.9 or later.
  * If you are using Shared VPC, then in the host project, you need to assign the `Compute Network User` role to the GKE Service account for the service project. 



### Restrictions and limitations

When deploying TLS passthrough Gateways and TLSRoute resources, observe the following limitations:

  * When you configure the `protocol: TLS` setting on a listener, you must explicitly set the `tls.mode` field to the `Passthrough` value. GKE doesn't support the default `Terminate` mode for `TLS` listeners.
  * On a `TLS` listener, don't set the `certificateRefs` field. Gateway-level client certificate validation (the `spec.tls.frontendValidation` field) doesn't apply to `TLS` listeners. To use mTLS, validate client certificates in your backend.
  * A `TLS` listener can share a port only with other `TLS` listeners. You can't configure `HTTP` or `HTTPS` listeners on the same port as a `TLS` listener.
  * In the `TLSRoute.spec.hostnames` field, you must specify a list of 1 to 1,024 SNI hostnames (exact hostname or wildcard prefix, such as `*.example.com`). Each entry can't exceed 253 characters and can't be an IP address.
  * In the `TLSRoute.spec.rules` field, you can configure at most one rule.
  * Each rule supports exactly one `backendRef` entry. Layer 4 proxy backends don't support weighted traffic splitting across multiple backends.
  * Single-cluster GatewayClasses support only Service backends, and multi-cluster GatewayClasses support only ServiceImport backends.
  * In the `TLSRoute.spec.rules.backendRefs` field, set the `port` field to a port declared by the target Service or ServiceImport resource, not to the container port.
  * The backend Kubernetes Service (including Services exported as a ServiceImport) referenced by a TLSRoute resource must use the `TCP` value for its port protocol.
  * You can't attach a BackendTLSPolicy resource, Identity-Aware Proxy, or Google Cloud Armor security policy to a TLSRoute backend because the controller rejects configurations of this type.
  * When you attach a GCPBackendPolicy resource to a Service or ServiceImport that is referenced by a TLSRoute resource, you must set the `spec.protocol` field to the `TCP` value (omitting the `spec.protocol` field defaults to the `HTTP` value, which applies only to HTTPRoute backends). A Service or ServiceImport can have one `HTTP` policy and one `TCP` policy attached at the same time; if multiple policies with the same `spec.protocol` value target the same Service or ServiceImport, the oldest policy takes precedence and newer ones aren't attached.
  * A GCPBackendPolicy resource with the `spec.protocol` field set to `TCP` supports only the following fields in the `spec.default` field (when targeting a ServiceImport resource, you can set the last three fields per cluster, zone, or region in the `spec.default.scopes` field instead):

    * `timeoutSec`
    * `connectionDraining`
    * `logging.enabled` and `logging.sampleRate`
    * `sessionAffinity.type` (valid values are `CLIENT_IP` or `NONE`)
    * `capacityScalerPercent`
    * `balancingMode: CONNECTION`
    * `maxConnectionsPerEndpoint`

You can't create a `TCP` policy that includes any other fields, or an `HTTP` policy that includes `TCP`-only fields (`balancingMode: CONNECTION` and `maxConnectionsPerEndpoint`); the Kubernetes API server rejects the policy on creation. For more information, see [Configure Gateway resources using Policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources).

  * If both an HTTPRoute and a TLSRoute resource reference the same Service or ServiceImport, attaching a HealthCheckPolicy resource to that target replaces the separate default health checks and applies the same health check configuration to both routes' backends. To configure health checks independently (such as `HTTP` health checks for HTTPRoute backends and `SSL` or `TCP` health checks for TLSRoute backends), create a separate Service for each route and attach a HealthCheckPolicy resource to each Service. Both Services can select the same Pods.

  * Layer 7 features (such as URL rewrites, path-based routing, and HTTP header transformations) don't apply to Layer 4 TCP proxy load balancers.




## Configure a proxy-only subnet

A regional Gateway requires a proxy-only subnet (`purpose=REGIONAL_MANAGED_PROXY`) in each region where you deploy it. One proxy-only subnet serves all regional Envoy-based load balancers in that region. If your region doesn't already have one, see [Configure a proxy-only subnet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#configure_a_proxy-only_subnet).

## Reserve a static IP address

Before you deploy the Gateway, reserve a regional static IP address so that the Gateway address doesn't change and you can resolve your sample hostnames to it. For instructions on creating a static IP address, see [Create a regional external HTTP(S) Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#create_a_regional_external_https_gateway).

## Deploy a Gateway with TLS passthrough listeners

The Gateway in this section configures two `TLS` listeners that share port `443`. Each listener matches a different SNI hostname and forwards connections in passthrough mode to attached TLSRoute resources.

  1. Save the following manifest as `store-gateway.yaml`:
         
         kind: Gateway
         apiVersion: gateway.networking.k8s.io/v1
         metadata:
           name: store-tls
         spec:
           gatewayClassName: gke-l7-regional-external-managed
           listeners:
           # Accept TLS connections for store.example.com without decrypting them.
           - name: store
             protocol: TLS
             port: 443
             hostname: "store.example.com"
             tls:
               mode: Passthrough
             allowedRoutes:
               kinds:
               - kind: TLSRoute
           # A second listener on the same port, selected by a different SNI name.
           - name: store-german
             protocol: TLS
             port: 443
             hostname: "store-de.example.com"
             tls:
               mode: Passthrough
             allowedRoutes:
               kinds:
               - kind: TLSRoute
           addresses:
           - type: NamedAddress
             value: IP_ADDRESS_NAME
         

Replace IP_ADDRESS_NAME with the name of the static IP address that you reserved.

Note that the `tls` block has no `certificateRefs` field. In `Passthrough` mode, the TLS certificate resides in your backend Pods rather than on the load balancer.

  2. Apply the Gateway manifest:
         
         kubectl apply -f store-gateway.yaml
         

  3. Verify that the Gateway is programmed:
         
         kubectl get gateway store-tls
         

Provisioning the load balancer takes a few minutes. The output is similar to the following:
         
         NAME        CLASS                              ADDRESS         PROGRAMMED   AGE
         store-tls   gke-l7-regional-external-managed   35.118.32.224   True         53s
         




### Use an internal Gateway

To keep traffic inside your VPC network, change the value of the `gatewayClassName` field to `gke-l7-rilb` and remove the `addresses` field from the Gateway manifest. GKE then creates a regional internal proxy Network Load Balancer and assigns an internal IP address from your cluster subnet. The remaining steps on this page are unchanged. Send your test requests from a Compute Engine instance in the same VPC network, because the internal IP address isn't reachable from the internet.

## Deploy sample TLS applications

In this section, you deploy two NGINX Deployments (`store-v1` and `store-german`) that terminate TLS on port `8443`. Each Deployment serves a different TLS certificate and reports the SNI hostname that it received, which lets you verify that routing occurred based on SNI.

  1. Generate a self-signed TLS certificate and private key for each hostname:
         
         openssl req -x509 -newkey rsa:2048 -nodes -sha256 -days 365 \
             -keyout store.key -out store.crt \
             -subj '/CN=store.example.com' \
             -addext 'subjectAltName=DNS:store.example.com'
         openssl req -x509 -newkey rsa:2048 -nodes -sha256 -days 365 \
             -keyout store-de.key -out store-de.crt \
             -subj '/CN=store-de.example.com' \
             -addext 'subjectAltName=DNS:store-de.example.com'
         

Use certificates from your certificate authority in production. Self-signed certificates keep this example self-contained.

  2. Store each certificate and key in a Kubernetes Secret by running the following commands:
         
         kubectl create secret tls store-cert \
             --cert=store.crt --key=store.key
         kubectl create secret tls store-de-cert \
             --cert=store-de.crt --key=store-de.key
         

  3. Save the following manifest as `store-tls-app.yaml`:
         
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: store-nginx
         data:
           default.conf: |
             server {
               listen 8443 ssl;
               ssl_certificate     /etc/nginx/ssl/tls.crt;
               ssl_certificate_key /etc/nginx/ssl/tls.key;
               default_type text/plain;
               # Report which Pod answered and which SNI name it received.
               return 200 "backend: $hostname\nsni: $ssl_server_name\n";
             }
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: store-v1
         spec:
           replicas: 2
           selector:
             matchLabels:
               app: store-v1
           template:
             metadata:
               labels:
                 app: store-v1
             spec:
               containers:
               - name: nginx
                 image: nginx:1.27
                 ports:
                 - containerPort: 8443
                 volumeMounts:
                 - name: config
                   mountPath: /etc/nginx/conf.d
                 - name: cert
                   mountPath: /etc/nginx/ssl
                   readOnly: true
               volumes:
               - name: config
                 configMap:
                   name: store-nginx
               - name: cert
                 secret:
                   secretName: store-cert
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: store-v1
         spec:
           selector:
             app: store-v1
           ports:
           - port: 443
             targetPort: 8443
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: store-german
         spec:
           replicas: 2
           selector:
             matchLabels:
               app: store-german
           template:
             metadata:
               labels:
                 app: store-german
             spec:
               containers:
               - name: nginx
                 image: nginx:1.27
                 ports:
                 - containerPort: 8443
                 volumeMounts:
                 - name: config
                   mountPath: /etc/nginx/conf.d
                 - name: cert
                   mountPath: /etc/nginx/ssl
                   readOnly: true
               volumes:
               - name: config
                 configMap:
                   name: store-nginx
               - name: cert
                 secret:
                   secretName: store-de-cert
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: store-german
         spec:
           selector:
             app: store-german
           ports:
           - port: 443
             targetPort: 8443
         

The Services don't need an `appProtocol` field. GKE forwards TLSRoute traffic to the backend as TCP, so the field has no effect.

  4. Apply the manifest to your cluster:
         
         kubectl apply -f store-tls-app.yaml
         

  5. Verify that the Pods are running:
         
         kubectl get pods -l 'app in (store-v1,store-german)'
         

The output is similar to the following:
         
         NAME                            READY   STATUS    RESTARTS   AGE
         store-german-7d9f8c5b47-2xqkd   1/1     Running   0          41s
         store-german-7d9f8c5b47-h6tzn   1/1     Running   0          41s
         store-v1-6c4b9d8f65-kp8vr       1/1     Running   0          41s
         store-v1-6c4b9d8f65-wm2ls       1/1     Running   0          41s
         




## Deploy TLSRoute resources for SNI-based routing

A TLSRoute resource attaches to a Gateway listener and routes connections that match its hostnames to a single backend Service.

  1. Save the following manifest as `store-tls-routes.yaml`:
         
         kind: TLSRoute
         apiVersion: gateway.networking.k8s.io/v1
         metadata:
           name: store
         spec:
           parentRefs:
           - kind: Gateway
             name: store-tls
             sectionName: store
           hostnames:
           - "store.example.com"
           rules:
           - backendRefs:
             - name: store-v1
               port: 443
         ---
         kind: TLSRoute
         apiVersion: gateway.networking.k8s.io/v1
         metadata:
           name: store-german
         spec:
           parentRefs:
           - kind: Gateway
             name: store-tls
             sectionName: store-german
           hostnames:
           - "store-de.example.com"
           rules:
           - backendRefs:
             - name: store-german
               port: 443
         

The `sectionName` field selects the target listener on the Gateway. The `port` field specifies the Service port (`443`), not the container port.

  2. Apply the TLSRoute manifest:
         
         kubectl apply -f store-tls-routes.yaml
         

  3. Verify that the Gateway controller accepted the route:
         
         kubectl get tlsroute store -o yaml
         

The `status` field is similar to the following:
         
         status:
           parents:
           - controllerName: networking.gke.io/gateway
             parentRef:
               name: store-tls
               sectionName: store
             conditions:
             - type: ResolvedRefs
               status: "True"
               reason: ResolvedRefs
             - type: Accepted
               status: "True"
               reason: Accepted
             - type: Reconciled
               status: "True"
               reason: ReconciliationSucceeded
         

The `Reconciled` condition is a GKE-specific status condition that reports whether the Gateway controller created the underlying Google Cloud resources.

  4. Verify that the Gateway listener accepted the route:
         
         kubectl get gateway store-tls -o yaml
         

Each entry in the `status.listeners` field is similar to the following:
         
         - name: store
           supportedKinds:
           - group: gateway.networking.k8s.io
             kind: TLSRoute
           attachedRoutes: 1
           conditions:
           - type: ResolvedRefs
             status: "True"
             reason: ResolvedRefs
           - type: Accepted
             status: "True"
             reason: Accepted
           - type: Programmed
             status: "True"
             reason: Programmed
         




## Verify traffic routing

GKE health checks a TLS passthrough backend by completing a TLS handshake with it. Your Pods might take a few minutes to pass the initial health check.

  1. Retrieve the Gateway IP address:
         
         kubectl get gateway store-tls -o jsonpath='{.status.addresses[0].value}'
         

  2. Send a request to each hostname, replacing GATEWAY_IP with the IP address from the previous step:
         
         curl --resolve store.example.com:443:GATEWAY_IP \
             --cacert store.crt https://store.example.com
         curl --resolve store-de.example.com:443:GATEWAY_IP \
             --cacert store-de.crt https://store-de.example.com
         

Each response names the Pod that answered and echoes the SNI hostname that reached it:
         
         backend: store-v1-6c4b9d8f65-kp8vr
         sni: store.example.com
         backend: store-german-7d9f8c5b47-2xqkd
         sni: store-de.example.com
         

Because each request used a different certificate authority file and both succeeded, each backend served its own certificate. The load balancer forwarded the encrypted connection without terminating it.

  3. Confirm that routing happens during the TLS handshake, before the client sends any HTTP request:
         
         openssl s_client -connect GATEWAY_IP:443 \
             -servername store-de.example.com </dev/null 2>/dev/null \
             | openssl x509 -noout -subject
         

The output shows the certificate of the `store-german` backend:
         
         subject=CN=store-de.example.com
         

Changing only the value of the `-servername` flag changes the certificate returned, confirming that the load balancer selected the backend based on SNI alone.

  4. Send a request with an SNI hostname that no listener matches:
         
         curl --resolve other.example.com:443:GATEWAY_IP \
             https://other.example.com
         

The connection closes because no listener on port `443` matches the SNI hostname `other.example.com`.




## Configure backend connection capacity

For GKE Services referenced by TLSRoute resources, the GKE Gateway controller configures a TCP [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service) by using the `CONNECTION` balancing mode, and sets the default value of the `maxConnectionsPerEndpoint` field to `100,000,000` (`1e8`).

Because the Gateway controller can't automatically determine a container's concurrent connection limit, you can use a GCPBackendPolicy resource to override the default value of the `maxConnectionsPerEndpoint` field (from `1` to `1,000,000,000`). To determine the optimal connection limit for your backend Pods, evaluate the following:

  * **Software limits:** check your server or application configuration, such as the Apache `MaxRequestWorkers` directive, the NGINX `worker_processes * worker_connections` settings, the Tomcat `maxConnections` attribute, or database connection pool limits.
  * **Load testing:** gradually increase concurrent connections against an isolated Pod while monitoring CPU, memory, latency, and socket or file descriptor limits.



### Apply a custom GCPBackendPolicy

To override the default value of the `maxConnectionsPerEndpoint` field on a TLSRoute backend Service, attach a GCPBackendPolicy resource with the `spec.protocol` field set to `TCP` and the `balancingMode` field set to `CONNECTION`:

  1. Save the following manifest as `backend-policy.yaml`:
         
         apiVersion: networking.gke.io/v1
         kind: GCPBackendPolicy
         metadata:
           name: store-v1-backend-policy
         spec:
           protocol: TCP
           default:
             balancingMode: CONNECTION
             maxConnectionsPerEndpoint: 1000
           targetRef:
             group: ""
             kind: Service
             name: store-v1
         

  2. Apply the policy:
         
         kubectl apply -f backend-policy.yaml
         




For more information about configuring backend policies, see [Configure Gateway resources using Policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources).

## Configure health checks for TLS passthrough

By default, for backend Services associated with TLS passthrough TLSRoute resources, the GKE Gateway controller automatically provisions a health check of type `SSL`.

### Handle the absence of SNI extensions from probers

When configuring health checks for TLS passthrough backends, you must account for how Google Cloud health check probers interact with TLS endpoints.

**Caution:** Google Cloud SSL health check probers don't send an SNI extension in their `ClientHello` handshake when checking backend health. This behavior applies specifically to SSL health checks. In contrast, TCP health checks verify basic socket connectivity and avoid the TLS handshake entirely.

If your backend applications require a valid SNI hostname to complete a TLS handshake, default SSL health checks will fail. To resolve this, use one of the following approaches:

  * **Configure fallback certificates:** configure your backend server or Pod to serve a default fallback TLS certificate when a TLS connection arrives without an SNI extension.
  * **Use TCP health checks with HealthCheckPolicy:** attach a HealthCheckPolicy resource (with the `config.type` field set to `TCP`) to your Service to check raw TCP port connectivity and avoid the TLS handshake.



### Apply a custom HealthCheckPolicy

To configure custom health check parameters or switch to TCP health checking, use a HealthCheckPolicy resource:

  1. Save the following manifest as `health-check-policy.yaml`:
         
         apiVersion: networking.gke.io/v1
         kind: HealthCheckPolicy
         metadata:
           name: store-health-check
         spec:
           default:
             checkIntervalSec: 10
             timeoutSec: 5
             healthyThreshold: 2
             unhealthyThreshold: 3
             config:
               type: TCP
               tcpHealthCheck:
                 port: 8443
           targetRef:
             group: ""
             kind: Service
             name: store-service
         

  2. Apply the policy:
         
         kubectl apply -f health-check-policy.yaml
         




For more information about configuring health checks, see [Configure Gateway resources using Policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure_health_check).

## Advanced configurations

This section describes advanced routing patterns, multi-tenant configurations, and multi-cluster deployments supported with TLS passthrough Gateways and TLSRoute resources.

### Wildcard hostname matching

TLSRoute resources support wildcard prefix matching for hostnames and follow deterministic precedence rules when multiple routes match the same incoming traffic.

Save the following manifest to define a wildcard TLSRoute:
    
    
    apiVersion: gateway.networking.k8s.io/v1
    kind: TLSRoute
    metadata:
      name: wildcard-tls-route
    spec:
      parentRefs:
      - name: store-tls
        sectionName: store
      hostnames:
      - "*.example.com"
      rules:
      - backendRefs:
        - name: store-v1
          port: 443
    

#### Precedence and conflict resolution rules

When multiple TLSRoute resources attach to the same Gateway listener and claim overlapping or identical hostnames, the GKE Gateway controller resolves conflicts by using the same hostname specificity and creation timestamp rules as other Gateway routes:

  * Exact hostname matches (such as `store.example.com`) take precedence over wildcard matches (such as `*.example.com`), and longer wildcard matches take precedence over broader wildcard matches (such as `*.com`).
  * If two or more TLSRoute resources declare the exact same hostname, the route with the oldest creation timestamp (`metadata.creationTimestamp`) takes precedence. If creation timestamps match, the lexicographically smaller `<namespace>/<name>` identifier breaks the tie. The Gateway controller doesn't accept conflicting routes, which report an `Accepted: False` condition with the `Conflicted` reason.



For more information about route precedence, see [Route merging, precedence, and validation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#route-merging).

### Cross-namespace routing with ReferenceGrant

In multi-tenant environments, a centralized platform team can manage the Gateway in an infrastructure namespace (such as `gateway-infra`), while application teams manage TLSRoute and Service resources in developer namespaces (such as `store-ns`).

  1. In the Gateway listener, allow routes from all namespaces (or selected namespaces):
         
         apiVersion: gateway.networking.k8s.io/v1
         kind: Gateway
         metadata:
           name: shared-tls-gateway
           namespace: gateway-infra
         spec:
           gatewayClassName: gke-l7-regional-external-managed
           listeners:
           - name: tls-passthrough
             protocol: TLS
             port: 443
             tls:
               mode: Passthrough
             allowedRoutes:
               namespaces:
                 from: All
               kinds:
               - kind: TLSRoute
         

  2. In the application namespace (`store-ns`), create a ReferenceGrant resource that permits the Gateway in the `gateway-infra` namespace to reference the TLSRoute or Service resource:
         
         apiVersion: gateway.networking.k8s.io/v1beta1
         kind: ReferenceGrant
         metadata:
           name: allow-gateway-infra
           namespace: store-ns
         spec:
           from:
           - group: gateway.networking.k8s.io
             kind: Gateway
             namespace: gateway-infra
           to:
           - group: ""
             kind: Service
         

  3. In the application namespace (`store-ns`), create the TLSRoute resource referencing the shared Gateway:
         
         apiVersion: gateway.networking.k8s.io/v1
         kind: TLSRoute
         metadata:
           name: store-tls-route
           namespace: store-ns
         spec:
           parentRefs:
           - name: shared-tls-gateway
             namespace: gateway-infra
             sectionName: tls-passthrough
           hostnames:
           - "store.example.com"
           rules:
           - backendRefs:
             - name: store-service
               port: 443
         




### Multi-cluster TLS passthrough Gateway

You can deploy multi-cluster Gateways with TLS passthrough across multiple GKE clusters in a fleet:

  1. Use a supported multi-cluster GatewayClass (`gke-l7-regional-external-managed-mc`, `gke-l7-rilb-mc`, or `gke-l7-cross-regional-internal-managed-mc`).
  2. Export your backend Service across the fleet by using a ServiceExport resource.
  3. In your TLSRoute resource, reference the multi-cluster backend by using a ServiceImport resource:
         
         apiVersion: gateway.networking.k8s.io/v1
         kind: TLSRoute
         metadata:
           name: mc-store-tls-route
         spec:
           parentRefs:
           - name: mc-tls-gateway
             sectionName: tls-passthrough
           hostnames:
           - "store.example.com"
           rules:
           - backendRefs:
             - group: net.gke.io
               kind: ServiceImport
               name: store-service
               port: 443
         




#### Multiple IP addresses in multi-cluster Gateways

When deploying cross-regional multi-cluster Gateways (such as when using the `gke-l7-cross-regional-internal-managed-mc` GatewayClass), you can define multiple IP addresses in the `spec.addresses` field to expose an internal VIP across different regions.

When you configure multiple IP addresses in a single Gateway, the GKE Gateway controller translates each IP address into a separate forwarding rule. At the same time, the controller references a shared target proxy and reuses the same underlying routing configuration. The controller does not multiply the underlying TLSRoute resources by the number of IP addresses, which helps prevent route duplication and quota exhaustion.

The following example shows a multi-cluster Gateway configured with ephemeral IP addresses across two regions:
    
    
    kind: Gateway
    apiVersion: gateway.networking.k8s.io/v1
    metadata:
      name: internal-cross-region-tls-gateway
    spec:
      gatewayClassName: gke-l7-cross-regional-internal-managed-mc
      addresses:
      - type: networking.gke.io/ephemeral-ipv4-address/us-west1
        value: "us-west1"
      - type: networking.gke.io/ephemeral-ipv4-address/us-east1
        value: "us-east1"
      listeners:
      - name: tls-passthrough
        protocol: TLS
        port: 443
        tls:
          mode: Passthrough
        allowedRoutes:
          kinds:
          - kind: TLSRoute
    

For more information about deploying internal multi-cluster Gateways, see [Deploy an internal multi-cluster Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-internal-multi-cluster-gateway).

## HTTP connection coalescing

**Warning:** When deploying HTTPS applications behind a TCP proxy load balancer that uses SNI-based routing, HTTP/2 connection coalescing can lead to misdirected requests if backend certificates share overlapping domain names.

According to [RFC 7540 (Section 9.1.1)](https://datatracker.ietf.org/doc/html/rfc7540#section-9.1.1), web browsers and HTTP/2 clients can reuse an established TLS connection for multiple requests if both of the following conditions are met:

  * The target hostnames resolve to the same IP address.
  * The server's presented TLS certificate is authoritative for both hostnames. For example, a certificate can cover multiple hostnames when you use wildcard certificates such as `*.example.com` or multi-domain Subject Alternative Names (SANs).



Because a Layer 4 TCP proxy load balancer does not inspect HTTP request headers after the initial TLS handshake, the load balancer forwards coalesced requests over the existing connection to the initially matched backend Pod.

To prevent connection coalescing issues:

  * **Use distinct, non-overlapping TLS certificates:** don't share wildcard certificates or common SAN identities across different backend services multiplexed behind the same Gateway IP address.
  * **Return HTTP 421 Misdirected Request:** configure your backend HTTPS servers to check the HTTP `:authority` (or `Host`) header. If the requested host does not match the server's expected domain, return an `HTTP 421 Misdirected Request` status code, prompting the client to open a new connection.
  * **Enable HTTP/2 ORIGIN Frame:** adopt [RFC 8336 ORIGIN Frame support](https://datatracker.ietf.org/doc/html/rfc8336) on your origin servers and explicitly declare which hostnames are valid for connection reuse.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the resources:

  1. Delete the TLSRoute resources:
         
         kubectl delete tlsroute store store-german
         

  2. Delete the Gateway resource:
         
         kubectl delete gateway store-tls
         

  3. Delete the sample Deployment, Service, and Secret resources:
         
         kubectl delete -f store-tls-app.yaml
         kubectl delete secret store-cert store-de-cert
         




## What's next

  * Learn about [GatewayClass capabilities](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities).
  * Learn about [Gateway security](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-security).
  * Learn how to [Configure Gateway resources using Policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 

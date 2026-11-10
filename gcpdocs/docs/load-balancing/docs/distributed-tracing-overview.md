---
url: https://docs.cloud.google.com/load-balancing/docs/distributed-tracing-overview/
title: Distributed tracing overview \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T06:06:07.185814+00:00
---

# Distributed tracing overview  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/distributed-tracing-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Distributed tracing overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Distributed tracing for Application Load Balancers provides end-to-end visibility into requests as they travel from your clients, through the load balancer, and to your backend services.

Cloud Load Balancing integrates with [Cloud Trace](https://docs.cloud.google.com/trace/docs/overview) to generate trace spans for requests that the load balancer processes. Because the load balancer is the entry point for your application traffic, starting and propagating trace context at the load balancer ensures diagnostic visibility across the entire request path. You can use these traces to identify latency bottlenecks, isolate failing hops, and troubleshoot errors across multi-tier architectures.

The load balancer generates traces that conform to open standards ([W3C Trace Context](https://www.w3.org/TR/trace-context/) and [OpenTelemetry](https://opentelemetry.io/)). Backend services that are instrumented with OpenTelemetry can continue the trace that the load balancer starts.

**Note:** During [Preview](https://cloud.google.com/products#product-launch-stages), distributed tracing is subject to specific limitations. For more information, in this document, see Limitations.

## Key benefits

Distributed tracing with Cloud Trace provides the following benefits:

  * **End-to-end request visibility** : trace a request's path across external and internal Application Load Balancers and the backend services that they route traffic to.
  * **Edge observability** : capture trace spans at the forwarding rule, before the load balancer selects a backend, so that you can see edge errors and latency that backend instrumentation can't detect.
  * **Decoupled telemetry configuration** : define tracing settings in standalone `TelemetryPolicy` resources without changing your load balancer's routing configuration.
  * **Cross-telemetry correlation** : correlate trace spans with Cloud Load Balancing request logs and Cloud Monitoring metrics to pinpoint where latency or errors originate.



## Supported load balancers

The following table lists the load balancers that support distributed tracing and the sampling modes that each load balancer supports:

Load balancer | Load balancing scheme | Probabilistic sampling | Parent-based sampling  
---|---|---|---  
Global external Application Load Balancer | `EXTERNAL_MANAGED` |  |   
Regional external Application Load Balancer | `EXTERNAL_MANAGED` |  |   
Regional internal Application Load Balancer | `INTERNAL_MANAGED` |  |   
Cross-region internal Application Load Balancer | `INTERNAL_MANAGED` |  |   
  
Classic Application Load Balancers don't support distributed tracing.

## How distributed tracing works

To configure distributed tracing, create a `TelemetryPolicy` resource in the Network Services API. A telemetry policy specifies the following:

  * **Targets** : the forwarding rules of the load balancers that you want to trace.
  * **Tracing configuration** : the sampling settings that determine which requests the load balancer traces.



When a request arrives at a forwarding rule that a telemetry policy targets, the load balancer decides whether to sample the request. If the request is sampled, the load balancer generates a trace span, sends the span to Cloud Trace, and propagates the trace context to the backend in the W3C `traceparent` request header.

### Forwarding rule attachment

Telemetry policies target the load balancer's [forwarding rule](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts), which represents the frontend of the load balancer. By attaching tracing at the forwarding rule, the load balancer can trace all traffic that enters a virtual IP address (VIP) and port, including requests that fail before the load balancer selects a backend.

Telemetry policies have the following characteristics:

  * **Independent lifecycle** : telemetry policies are separate from backend services, URL maps, and target proxies. You can create, modify, or delete a telemetry policy without changing how the load balancer routes traffic.
  * **Reusable across frontends** : a single telemetry policy can target multiple forwarding rules, so you can apply consistent tracing settings across several load balancer frontends.
  * **Location-scoped** : create a telemetry policy in the `global` location to target global forwarding rules, such as those used by global external Application Load Balancers and cross-region internal Application Load Balancers. Create a telemetry policy in a region to target regional forwarding rules in that region, such as those used by regional external Application Load Balancers and regional internal Application Load Balancers.



### Sampling modes

Distributed tracing supports the following sampling modes. For more information about which sampling modes each load balancer supports, in this document, see Supported load balancers.

  * **Probabilistic sampling** : the load balancer samples a fixed proportion of requests, which you set in the `samplingRate` field. For example, a value of `0.01` samples 1% of requests. Probabilistic sampling is supported on all supported load balancers.
  * **Parent-based sampling** : the load balancer honors the [sampling decision](https://www.w3.org/TR/trace-context/#sampling-decision) in the incoming `traceparent` header from an upstream client or service. You configure parent-based sampling in the `parentBasedSampling` field. Parent-based sampling is supported only on internal Application Load Balancers.

When you enable parent-based sampling, the load balancer handles requests as follows:

    * If the incoming `traceparent` header has the sampled flag set, the load balancer samples the request at the rate specified in the `parentBasedSampling.samplingRate` field. For example, set this field to `1.0` to trace all requests that an upstream service has already sampled.
    * If the incoming `traceparent` header doesn't have the sampled flag set, the load balancer doesn't sample the request. This behavior respects the upstream decision and follows the OpenTelemetry specification, which prevents disconnected traces from appearing in Cloud Trace.
    * If the request doesn't include a `traceparent` header, the load balancer applies the baseline `samplingRate`.



### Trace context header handling

The load balancer handles the W3C `traceparent` header as follows:

  * **Tracing isn't enabled, or the request isn't sampled** : the load balancer forwards the incoming `traceparent` header to the backend without changes.
  * **The request is sampled and doesn't include a`traceparent` header**: the load balancer generates a new trace ID and span ID, and sets the trace flags to `03` (random and sampled).
  * **The request is sampled and includes a`traceparent` header**: the load balancer preserves the incoming trace ID and random flag, generates a new span ID, and sets the sampled flag.



Backend services that use an OpenTelemetry SDK with the W3C Trace Context propagator automatically read the `traceparent` header and continue the trace. For more information, see [Trace context](https://docs.cloud.google.com/trace/docs/trace-context#http-requests).

## Common use cases

This section describes common scenarios for distributed tracing.

### Monitor the storefront edge

An ecommerce storefront uses a global external Application Load Balancer to receive customer traffic. To monitor edge latency and errors such as `404` responses and TLS failures, you attach a telemetry policy with probabilistic sampling to the storefront's forwarding rule. A low sampling rate, such as `0.01` (1%), keeps Cloud Trace ingestion costs predictable during peak traffic events.

### Maintain trace continuity across checkout services

Checkout requests travel from the storefront through an internal Application Load Balancer to internal cart, inventory, and payment services. To make sure that checkout requests sampled at the storefront are traced across every internal hop, you enable parent-based sampling on the internal load balancer with a `parentBasedSampling.samplingRate` of `1.0`. Routine internal traffic that doesn't carry an upstream sampling decision is sampled at the baseline `samplingRate`.

### Isolate latency bottlenecks

When checkout latency increases or `5xx` errors spike, you compare load balancer spans in Cloud Trace with load balancer request logs and latency metrics. This comparison helps you determine whether the issue originates at the load balancer edge, at an internal load balancer hop, or in a backend service.

## Pricing

The load balancer doesn't charge for generating trace spans. However, Cloud Trace charges for trace span ingestion according to [Cloud Trace pricing](https://cloud.google.com/products/observability/pricing#trace-pricing-summary).

To manage ingestion costs for high-traffic production workloads, we recommend a `samplingRate` of `0.01` (1%) or `0.001` (0.1%).

## Limitations

During Preview, distributed tracing for Application Load Balancers has the following limitations:

  * Parent-based sampling isn't supported on external Application Load Balancers.
  * Custom span attributes aren't supported.
  * You can't configure distributed tracing by using the Google Kubernetes Engine Gateway API or Terraform.
  * A single telemetry policy can target up to 50 resources.



## Distributed tracing for Agent Gateway

If you use Agent Gateway to manage traffic for AI agents, see [Monitor traffic through Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/monitor-agent-gateway) for information about monitoring agent traffic.

## What's next

  * [Trace inbound traffic with Cloud Trace](https://docs.cloud.google.com/load-balancing/docs/trace-inbound-traffic)
  * [Cloud Trace overview](https://docs.cloud.google.com/trace/docs/overview)
  * [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 

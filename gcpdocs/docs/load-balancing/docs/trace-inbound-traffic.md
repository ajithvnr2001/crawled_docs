---
url: https://docs.cloud.google.com/load-balancing/docs/trace-inbound-traffic/
title: Trace inbound traffic with Cloud Trace \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T05:45:55.102254+00:00
---

# Trace inbound traffic with Cloud Trace  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/trace-inbound-traffic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Trace inbound traffic with Cloud Trace Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains how to configure distributed tracing for Application Load Balancers by using [Cloud Trace](https://docs.cloud.google.com/trace/docs/overview). You create a telemetry policy that targets the forwarding rule of your load balancer, and then view the resulting traces in Cloud Trace.

The examples in this document use an ecommerce application that has the following architecture:

  * A global external Application Load Balancer that receives customer traffic for a web storefront.
  * A regional internal Application Load Balancer that routes checkout requests from the storefront to internal cart, inventory, and payment services.



For information about how distributed tracing works, including sampling modes and trace context header handling, see [Distributed tracing overview](https://docs.cloud.google.com/load-balancing/docs/distributed-tracing-overview).

## Before you begin

  1. Enable the Cloud Trace API and the Network Services API in your project:
         
         gcloud services enable \
             cloudtrace.googleapis.com \
             networkservices.googleapis.com
         

  2. Make sure that you have a [supported load balancer](https://docs.cloud.google.com/load-balancing/docs/distributed-tracing-overview#supported-load-balancers) deployed. For more information, see the following:

     * [Set up a global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-compute)
     * [Set up a regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb)
     * [Set up a regional internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal)
     * [Set up a cross-region internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-cross-reg-internal)
**Note:** Classic Application Load Balancers don't support distributed tracing.
  3. Note the name and scope of the forwarding rule of your load balancer. The scope of the forwarding rule depends on the load balancer type:

     * **Global forwarding rule** : used by global external Application Load Balancers and cross-region internal Application Load Balancers.
     * **Regional forwarding rule** : used by regional external Application Load Balancers and regional internal Application Load Balancers.

To list the forwarding rules in your project, use the [`gcloud compute forwarding-rules list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/list):
    
    gcloud compute forwarding-rules list
    




### Required roles

To get the permissions that you need to configure telemetry policies and view traces, ask your administrator to grant you the following Identity and Access Management (IAM) roles on your project:

  * To create, update, or delete telemetry policies: [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) or [Compute Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)
  * To view traces in the Google Cloud console: [Cloud Trace User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.user) (`roles/cloudtrace.user`)



To let the load balancer write trace spans to Cloud Trace, grant the [Cloud Trace Agent role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.agent) (`roles/cloudtrace.agent`) on your project to the following service accounts:

  * Compute Engine service agent: `service-PROJECT_NUMBER@compute-system.iam.gserviceaccount.com`
  * Network Security service agent: `service-PROJECT_NUMBER@gcp-sa-networksecurity.iam.gserviceaccount.com`
  * The service accounts of your backend workloads, if your backends export their own spans to Cloud Trace. Without this role, Cloud Trace shows only the load balancer span, and the trace doesn't contain backend spans.



Replace `PROJECT_NUMBER` with your Google Cloud project number.

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Telemetry policy configuration

You define a telemetry policy in a YAML file that uses the following format:
    
    
    name: "projects/PROJECT_ID/locations/LOCATION/telemetryPolicies/POLICY_NAME"
    displayName: "DISPLAY_NAME"
    telemetryTarget:
      resources:
      - "FORWARDING_RULE_URI"
    tracingConfiguration:
      samplingRate: SAMPLING_RATE
      parentBasedSampling:
        enabled: ENABLE_PARENT_BASED_SAMPLING
        samplingRate: PARENT_BASED_SAMPLING_RATE
    

The following table describes the fields in a telemetry policy:

Field | Description  
---|---  
`name` |  The resource name of the telemetry policy. Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the location of the telemetry policy, which must match the scope of the forwarding rules that the policy targets. For global forwarding rules, use `global`. For regional forwarding rules, use the region of the forwarding rule, such as `us-central1`.
  * `POLICY_NAME`: the name of the telemetry policy. The name must be 4 to 63 characters long, start with a lowercase letter, contain only lowercase letters, numbers, and hyphens, and end with a lowercase letter or number.

  
`displayName` | Optional. A human-readable name (`DISPLAY_NAME`) for the telemetry policy.  
`telemetryTarget.resources` |  A list of the full resource names (`FORWARDING_RULE_URI`) of the forwarding rules that the policy applies to. You can specify up to 50 resources. Use one of the following formats:

  * Global forwarding rule: `//compute.googleapis.com/projects/PROJECT_ID/global/forwardingRules/FORWARDING_RULE_NAME`
  * Regional forwarding rule: `//compute.googleapis.com/projects/PROJECT_ID/regions/REGION/forwardingRules/FORWARDING_RULE_NAME`

Replace the following: 
  * `FORWARDING_RULE_NAME`: the name of the forwarding rule
  * `REGION`: the region of the forwarding rule, such as `us-central1`

  
`tracingConfiguration.samplingRate` | The proportion of requests to trace (`SAMPLING_RATE`), specified as a value from `0.0` (0%) to `1.0` (100%). For example, `0.01` samples 1% of requests. The default value is `0.0`.  
`tracingConfiguration.parentBasedSampling.enabled` | Optional. Whether the load balancer honors the sampled flag in the incoming W3C `traceparent` header (`ENABLE_PARENT_BASED_SAMPLING`) is `true` or `false`. The default value is `false`. Supported only on internal Application Load Balancers.  
`tracingConfiguration.parentBasedSampling.samplingRate` | Optional. The proportion of upstream-sampled requests to trace (`PARENT_BASED_SAMPLING_RATE`), specified as a value from `0.0` to `1.0`. For example, `1.0` traces all requests that an upstream client or service has already sampled.  
  
## Configure tracing for an external load balancer

This example configures probabilistic sampling on the forwarding rule of a global external Application Load Balancer for an ecommerce storefront. A sampling rate of `0.01` traces 1% of requests, which captures edge latency and errors while keeping Cloud Trace ingestion costs predictable during high traffic.

  1. Create a YAML file named `storefront-tracing-policy.yaml`:
         
         cat <<EOF > storefront-tracing-policy.yaml
         name: "projects/PROJECT_ID/locations/global/telemetryPolicies/storefront-tracing-policy"
         displayName: "Tracing policy for the storefront load balancer"
         telemetryTarget:
           resources:
             - "//compute.googleapis.com/projects/PROJECT_ID/global/forwardingRules/FORWARDING_RULE_NAME"
         tracingConfiguration:
           samplingRate: 0.01
         EOF
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project
     * `FORWARDING_RULE_NAME`: the name of the global forwarding rule of your load balancer

For a regional external Application Load Balancer, replace `global` in the policy name with the region of the forwarding rule, and use the regional forwarding rule format.

  2. Import the telemetry policy by using the [`gcloud beta network-services telemetry-policies import` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-services/telemetry-policies/import):
         
         gcloud beta network-services telemetry-policies import storefront-tracing-policy \
             --source=storefront-tracing-policy.yaml \
             --location=global
         




## Configure tracing for an internal load balancer

This example configures a regional internal Application Load Balancer for internal checkout and payment services. The policy uses the following sampling settings:

  * A baseline `samplingRate` of `0.01` (1%) for requests that don't carry an upstream sampling decision.
  * Parent-based sampling with a `samplingRate` of `1.0` (100%), so that every checkout request that's already sampled at the storefront, or by any upstream service, is traced across the internal load balancer.



To configure the policy, do the following:

  1. Create a YAML file named `checkout-tracing-policy.yaml`:
         
         cat <<EOF > checkout-tracing-policy.yaml
         name: "projects/PROJECT_ID/locations/REGION/telemetryPolicies/checkout-tracing-policy"
         displayName: "Tracing policy for the internal checkout load balancer"
         telemetryTarget:
           resources:
             - "//compute.googleapis.com/projects/PROJECT_ID/regions/REGION/forwardingRules/FORWARDING_RULE_NAME"
         tracingConfiguration:
           samplingRate: 0.01
           parentBasedSampling:
             enabled: true
             samplingRate: 1.0
         EOF
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project
     * `REGION`: the region of the forwarding rule, such as `us-central1`
     * `FORWARDING_RULE_NAME`: the name of the regional forwarding rule of your load balancer

For a cross-region internal Application Load Balancer, use `global` as the location in the policy name, and use the global forwarding rule format.

  2. Import the telemetry policy:
         
         gcloud beta network-services telemetry-policies import checkout-tracing-policy \
             --source=checkout-tracing-policy.yaml \
             --location=REGION
         




## Verify the telemetry policy

To verify that the telemetry policy exists and targets the correct forwarding rules, use the [`gcloud beta network-services telemetry-policies describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-services/telemetry-policies/describe):
    
    
    gcloud beta network-services telemetry-policies describe POLICY_NAME \
        --location=LOCATION
    

Replace the following:

  * `POLICY_NAME`: the name of the telemetry policy
  * `LOCATION`: `global` or the region of the telemetry policy



To list all telemetry policies in a location, use the [`gcloud beta network-services telemetry-policies list` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-services/telemetry-policies/list):
    
    
    gcloud beta network-services telemetry-policies list \
        --location=LOCATION
    

## Update a telemetry policy

To change the sampling settings, or to apply the same policy to additional forwarding rules, do the following:

  1. Edit the policy YAML file. For example, to apply the storefront policy to multiple global forwarding rules, add each forwarding rule to the `telemetryTarget.resources` list:
         
         telemetryTarget:
           resources:
             - "//compute.googleapis.com/projects/PROJECT_ID/global/forwardingRules/storefront-https-fr"
             - "//compute.googleapis.com/projects/PROJECT_ID/global/forwardingRules/cart-https-fr"
         

  2. Import the updated policy:
         
         gcloud beta network-services telemetry-policies import POLICY_NAME \
             --source=POLICY_FILE \
             --location=LOCATION
         

Replace `POLICY_FILE` with the path to your policy YAML file.




## View traces

After you configure tracing and send traffic through your load balancer, view the traces in the Google Cloud console:

  1. In the Google Cloud console, go to the **Trace Explorer** page.

[Go to Trace Explorer](https://console.cloud.google.com/traces/explorer)

  2. Select your Google Cloud project.

  3. In the **Filter** field, enter a filter to find the traces that you want to inspect. For example, attribute ID or latency threshold.

  4. Optionally, to explore a specific trace, go to the toolbar, click **Trace ID** , and enter the trace ID.

  5. Click a trace to view its spans in the timeline and graph views.

  6. Inspect the load balancer span to see details such as the total duration and the backend that served the request.




For more information about using Trace Explorer, see [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces).

## Correlate traces with logs and metrics

You can correlate load balancer trace spans with request logs and metrics to isolate the source of latency or errors.

### Correlate traces with logs

If you [enable logging](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring) on your backend service, the load balancer adds a `trace` field to each request log entry for a sampled request. The field uses the following format:
    
    
    projects/PROJECT_ID/traces/TRACE_ID
    

#### View a trace from a load balancer log entry

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Expand a load balancer log entry.

  3. In the log entry summary, click the trace icon.

![The trace icon next to a log entry summary in Logs Explorer.](https://docs.cloud.google.com/static/logging/docs/images/trace-latency-chip.png)

  4. Select **View trace details**.




The trace opens on the **Trace Explorer** page.

#### View load balancer logs from a trace

  1. In the Google Cloud console, go to the **Trace Explorer** page.

[Go to Trace Explorer](https://console.cloud.google.com/traces/explorer)

  2. Click a trace to open the **Details** pane.

  3. Click **View Logs**.




The load balancer log entries for the request appear.

### Correlate traces with metrics

Compare latency spikes in load balancer metrics with trace span breakdowns to determine whether latency originates in the load balancer or in the backend. You can view and query these metrics in [**Metrics Explorer**](https://console.cloud.google.com/monitoring/metrics-explorer) in Cloud Monitoring. Use the following metrics:

  * Global external Application Load Balancer: `loadbalancing.googleapis.com/https/total_latencies` and `loadbalancing.googleapis.com/https/backend_latencies`
  * Regional external Application Load Balancer: `loadbalancing.googleapis.com/https/external/regional/total_latencies`
  * Internal Application Load Balancer: `loadbalancing.googleapis.com/https/internal/total_latencies`



## Disable tracing

To stop tracing requests for a load balancer, do one of the following:

  * Remove the forwarding rule from the `telemetryTarget.resources` list of the policy, and then import the updated policy.
  * Delete the telemetry policy by using the [`gcloud beta network-services telemetry-policies delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-services/telemetry-policies/delete):
        
        gcloud beta network-services telemetry-policies delete POLICY_NAME \
            --location=LOCATION
        




## Best practices

Consider the following best practices when you configure distributed tracing:

  * **Size sampling rates for your traffic volume** : for high-traffic production workloads, use a `samplingRate` of `0.01` (1%) or `0.001` (0.1%) to balance observability with Cloud Trace ingestion costs.
  * **Use parent-based sampling for multi-tier architectures** : on internal Application Load Balancers, enable parent-based sampling so that requests sampled upstream are traced across every internal hop.
  * **Instrument your backends** : use an OpenTelemetry SDK with the W3C Trace Context propagator in your backend services so that backend spans join the trace that the load balancer starts.



## Troubleshoot

This section describes common issues and their resolutions.

### Traces don't appear in Cloud Trace

If traces don't appear in Cloud Trace, do the following:

  1. Make sure that the Cloud Trace API is enabled in your project:
         
         gcloud services enable cloudtrace.googleapis.com \
             --project=PROJECT_ID
         

  2. Verify that the Cloud Trace Agent role (`roles/cloudtrace.agent`) is granted to the service accounts listed in Required roles.

  3. Verify that the telemetry policy exists in the correct location and that it targets the correct forwarding rule. For more information, see Verify the telemetry policy.

  4. Check the configured `samplingRate`. If the traffic volume or the sampling rate is low, the load balancer might not capture traces immediately. To confirm that tracing works, temporarily set `samplingRate` to `1.0`, and then restore your production rate when you finish testing.




### Trace spans are disconnected or incomplete

If load balancer spans appear as separate root traces instead of as part of your application's traces, do the following:

  1. For internal Application Load Balancers, verify that parent-based sampling is enabled (`parentBasedSampling.enabled: true`) in the telemetry policy.

  2. Verify that the service accounts of your client and backend workloads have the Cloud Trace Agent role (`roles/cloudtrace.agent`), so that their spans can be exported to Cloud Trace.

  3. Verify that your applications use an OpenTelemetry SDK with W3C Trace Context propagation enabled, so that the `traceparent` header is propagated across service boundaries. For more information, see the [OpenTelemetry context propagation documentation](https://opentelemetry.io/docs/concepts/context-propagation/).




## What's next

  * [Distributed tracing overview](https://docs.cloud.google.com/load-balancing/docs/distributed-tracing-overview)
  * [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces)
  * [Global external Application Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring)
  * [Regional external Application Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/https/https-reg-logging-monitoring)
  * [Internal Application Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/l7-internal/monitoring)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-02 UTC."],[],[]] 

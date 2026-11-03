---
url: https://docs.cloud.google.com/app-hub/docs/regional-endpoints/
title: Configure regional endpoints \u00a0|\u00a0 App Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T05:44:07.087307+00:00
---

# Configure regional endpoints  |  App Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-hub/docs/regional-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ App Hub ](https://docs.cloud.google.com/app-hub/docs)
  * [ Guides ](https://docs.cloud.google.com/app-hub/docs/overview)



Send feedback 

#  Configure regional endpoints Stay organized with collections  Save and categorize content based on your preferences. 

Regional endpoints let you run your App Hub workloads in a manner that complies with [data residency](https://docs.cloud.google.com/assured-workloads/docs/data-residency) and data sovereignty requirements, where your request traffic is routed directly to the region specified in the endpoint.

## What are regional endpoints?

Regional endpoints are request endpoints that only allow requests to proceed if the affected resource exists in the location specified by the endpoint. For example, when you use the endpoint `https://apphub.us-central1.rep.googleapis.com` in a request to manage resources, the request only proceeds if the application or registered component is located in `us-central1`.

Unlike global endpoints, where requests might be processed in a different location from where the resource resides, regional endpoints only process requests within the location specified by the endpoint. Regional endpoints terminate TLS sessions in the location specified by the endpoint for requests received from the internet, other Google Cloud resources, such as Compute Engine virtual machines, on-premises services using VPN or Interconnect, and Virtual Private Clouds (VPCs).

Regional endpoints support data residency by ensuring that your application's metadata stays within the specified region both at rest and in transit.

## Limitations

You can't use regional endpoints to manage global resources in App Hub, such as global applications, perimeters, Service Project Attachments (SPAs), and boundaries.

API requests related to these global resources that use a regional endpoint will fail because these requests include the `/global/` location in the API path. For example, the request `GET .../locations/global/applications/globalApp` will be rejected.

To manage global resources, use the standard global endpoint, `https://apphub.googleapis.com`.

## Supported locations

You can use regional endpoints for all regional locations where App Hub is available. For a list of supported regions, see [Locations](https://docs.cloud.google.com/app-hub/docs/locations).

## Tools for using regional endpoints

You can configure Google Cloud CLI or make direct REST or RPC API requests using regional endpoints.

### Google Cloud CLI

To configure the Google Cloud CLI for use with regional endpoints, follow these steps:

  1. Ensure that you use the Google Cloud CLI version `402.0.0` or later.

  2. Set the `api_endpoint_overrides/apphub` property to the regional endpoint you want to use:
         
         gcloud config set api_endpoint_overrides/apphub https://apphub.LOCATION.rep.googleapis.com/
         

Replace `LOCATION` with a supported region, such as `us-central1`.




Alternatively, set the `CLOUDSDK_API_ENDPOINT_OVERRIDES_APPHUB` environment variable to the endpoint:
    
    
    CLOUDSDK_API_ENDPOINT_OVERRIDES_APPHUB=https://apphub.LOCATION.rep.googleapis.com/
    gcloud apphub applications list
    

### REST APIs

To make requests to regional endpoints, use the following URI, replacing `LOCATION` with a supported region:
    
    
    https://apphub.LOCATION.rep.googleapis.com
    

For example, you can use the following endpoint to access App Hub in the `us-central1` region:

`https://apphub.us-central1.rep.googleapis.com`

### Terraform

To use regional endpoints with Terraform, you must override the App Hub endpoint in the Google provider block.

When you set a regional endpoint as the custom endpoint, you can't use Terraform to manage global resources such as `google_apphub_service_project_attachment`.
    
    
    provider "google" {
      project = "project-id"
      region = "us-central1"
      # Override the App Hub API endpoint to use a regional endpoint
      apphub_custom_endpoint = "https://apphub.us-central1.rep.googleapis.com/"
    }
    

### Client libraries

To use regional endpoints with client libraries, you must override the `api_endpoint` property in the client options.

The following example uses the Python client library.
    
    
    from google.cloud import [apphub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apphub/latest)
    from google.api_core import client_options
    
    rep_endpoint = "apphub.us-central1.rep.googleapis.com"
    options = client_options.ClientOptions(api_endpoint=rep_endpoint)
    
    # Instantiate the client
    client = [apphub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apphub/latest).[AppHubClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apphub/latest/google.cloud.apphub_v1.services.app_hub.AppHubClient.html)(client_options=options)
    

## Restricting global API endpoint usage

To help enforce the use of regional endpoints, you can use the `constraints/gcp.restrictEndpointUsage` organization policy constraint to block requests to the global API endpoint. For more information about restricting endpoint usage, see [Restrict endpoint usage](https://docs.cloud.google.com/docs/security/compliance/restrict-endpoint-usage).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-02 UTC."],[],[]] 

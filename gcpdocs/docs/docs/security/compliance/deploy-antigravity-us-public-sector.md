---
url: https://docs.cloud.google.com/docs/security/compliance/deploy-antigravity-us-public-sector/
title: Deploy the Antigravity App and Antigravity CLI for US public sector \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T05:37:22.619437+00:00
---

# Deploy the Antigravity App and Antigravity CLI for US public sector  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/compliance/deploy-antigravity-us-public-sector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Deploy the Antigravity App and Antigravity CLI for US public sector Stay organized with collections  Save and categorize content based on your preferences. 

You can deploy Antigravity App and Antigravity CLI in FedRAMP High, IL4, IL5, ITAR, and CJIS data boundary environments when used with the Gemini platform.

Use these instructions to configure the [Antigravity App](https://antigravity.google/docs/overview) and the [Antigravity CLI](https://antigravity.google/product/antigravity-cli/) to support the regulatory standards and similar guidelines required for US public sector organizations and enterprise customers. Deviation from the steps on this page can lead to a non-compliant configuration. 

A Third-Party Assessment Organization (3PAO) validated that these deployment instructions allow the Antigravity App and Antigravity CLI to only communicate with one US-based cloud service API regional endpoint. The `aiplatform.us.rep.googleapis.com` API endpoint is [already supported](https://docs.cloud.google.com/assured-workloads/docs/supported-products) by the Assured Workloads data boundaries for FedRAMP High, IL4, IL5, ITAR, and CJIS. For more information, see [Coalfire's Evaluation of Antigravity App and CLI](https://services.google.com/fh/files/misc/antigravity_attestation_10-26-2026.pdf).

**Note:** You can't use the enterprise integration of [Antigravity in Gemini Enterprise](https://antigravity.google/docs/enterprise/) to support US public sector compliance.

## Prerequisites

  * [Create an Assured Workloads folder](https://docs.cloud.google.com/assured-workloads/docs/create-folder) for your compliance framework.



## Deploy Antigravity App and Antigravity CLI

Complete the following steps to deploy Antigravity App and Antigravity CLI and configure your local environment and client to meet your organization's security expectations:

  1. [Download Antigravity App and Antigravity CLI](https://antigravity.google/download) locally.
  2. Create a project in your Assured Workloads folder and enable API access. For instructions, see the [Google Cloud project and API setup](https://antigravity.google/docs/enterprise#google-cloud-project-and-api-setup) section.
  3. Configure authentication to Antigravity as appropriate for your users and clients. You can use Cloud Identity (for federation with your external identity provider or system) and Google Cloud service accounts to authenticate to Antigravity.
  4. Sign in to Antigravity using [Application Default Credentials](https://antigravity.google/docs/enterprise#application-default-credentials-adc-in-antigravity-cli), as follows:

     * When using the Antigravity desktop client:

       1. Select a project within the Assured Workloads folder.
       2. Choose the US location.
     * When using the Antigravity CLI:

       1. Use the Google Cloud CLI to configure your quota project:
              
              gcloud auth application-default set-quota-project QUOTA_PROJECT_ID
              

Replace `QUOTA_PROJECT_ID` with the ID of the project in your Assured Workloads folder.

       2. Set the following environment variables:
              
              export AGY_ADC_AUTH=true
              export GOOGLE_CLOUD_LOCATION=us
              export AGY_CLI_DISABLE_AUTO_UPDATE=true
              




## Connect to supported models

The following models are supported for FedRAMP High, IL4, IL5, ITAR, and CJIS: 

  * Gemini 3.6 Flash
  * Gemini 3.7 Flash
  * Gemini 3.8 Flash



To connect to a version of the model that supports US Public Sector compliance requirements, select **US** as your base endpoint URI. You must select **US** to ensure that prompts and responses conform to the specific requirements of US Public Sector customers. For instructions, see [Regional endpoints and network allowlists](https://antigravity.google/docs/enterprise#regional-endpoints-and-network-allowlists).

## Disable optional APIs

Antigravity App and Antigravity CLI call other backend APIs, not all of which support compliance with US Public Sector requirements. These APIs aren't necessary for the core functionality of the product. To maintain the compliance of your deployment, disable the ability to invoke the following APIs from your local environment:

  * All non-US multi-region endpoints in `aiplatform.*.rep.googleapis.com` (except for `aiplatform.us.rep.googleapis.com`)
  * `antigravity.google`
  * `*.antigravity.google`
  * `antigravity.google.com`
  * `*.antigravity.google.com`
  * `antigravity-cli-auto-updater-974169037036.us-central1.run.app`
  * `antigravity-hub-auto-updater-974169037036.us-central1.run.app`
  * `antigravity-unleash.goog`
  * `businessaicode.googleapis.com`
  * `chromewebstore.google.com`
  * `cloudcode-pa.googleapis.com`
  * `aicode.googleapis.com`
  * `daily-cloudcode-pa.googleapis.com`
  * `play.googleapis.com`



To disable these endpoints in your local environment, apply the following controls:

  * **Network and proxy rules** : in your corporate web proxy, firewall, or DNS policy, block outbound requests to the listed domains while still permitting traffic to the `aiplatform.us.rep.googleapis.com` endpoint.
  * **Endpoint usage organization policy** : configure the `constraints/gcp.restrictEndpointUsage` organization policy constraint at the folder or project level to deny the `in:non-us-aiplatform-endpoints` value group (which blocks global and non-US Gemini Enterprise Agent Platform endpoints) and the `businessaicode.googleapis.com`, `businessaicode.us.rep.googleapis.com`, and `businessaicode.eu.rep.googleapis.com` endpoints. To find the supported multi-region endpoints for Agent Platform, see [Multi-region endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations#multi-region-endpoints). For instructions on configuring this constraint and its curated value groups, see [Restrict endpoint usage](https://docs.cloud.google.com/docs/security/compliance/restrict-endpoint-usage).
  * **Project API management** : disable the `businessaicode.googleapis.com` and `cloudaicompanion.googleapis.com` APIs in your Assured Workloads project if they are enabled. The `cloudcode-pa.googleapis.com` endpoint is an internal Google client endpoint that you can't enable or disable through Service Usage and must block by using your network or proxy rules. For more information, see [Disable services](https://docs.cloud.google.com/service-usage/docs/enable-disable#disabling).
  * **Automatic CLI updates** : set the `AGY_CLI_DISABLE_AUTO_UPDATE=true` environment variable to help prevent the Antigravity CLI from querying the `antigravity-cli-auto-updater-974169037036.us-central1.run.app` endpoint on startup.



## Support SSL/TLS inspection and certificates

Antigravity App and CLI automatically query and use the host operating system's trusted root store, such as `/etc/ssl/certs` on Linux, the Windows Certificate Store on Windows, and the Keychain on macOS. 

If you deploy the enterprise's corporate CA certificate bundle to the client OS, Antigravity automatically trusts and operates within the inspected SSL/TLS environment. You don't require a custom CA override.

If you use corporate proxies, the HTTP transport from the Go language supports the system's standard proxy environment variables. Configure these variables on the machines that run Antigravity: 

  * `HTTP_PROXY`
  * `HTTPS_PROXY`
  * `NO_PROXY`



For more information, see [Settings](https://antigravity.google/docs/settings/). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

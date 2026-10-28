---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security/
title: Secure Data Cloud connectors \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:54:39.011576+00:00
---

# Secure Data Cloud connectors  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security/

[ Skip to main content ](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security/)
  * [Deutsch](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security/?hl=ko)


[ ![](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/gemini-spark-blue-192px.svg) ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Supported security and compliance controls](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security/#supported-security-controls)
  * [Allow Data Cloud connectors in organization policies](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security/#allow-connectors-org-policies)


**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)


Send feedback 
#  Secure Data Cloud connectors Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Supported security and compliance controls](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security/#supported-security-controls)
  * [Allow Data Cloud connectors in organization policies](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security/#allow-connectors-org-policies)


This page describes the security and compliance controls supported by [Data Cloud connectors](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-data-cloud) in Gemini Enterprise and explains how to configure organization policies when your project is protected by a VPC Service Controls perimeter.
## Supported security and compliance controls
Data Cloud connectors support the following enterprise security and compliance controls in Gemini Enterprise:
  * **Data residency (DRZ)** : When you use federated query mode, your customer data remains where it's already stored and isn't moved. The connector queries your data in place and returns the results to the agent in the location of your Gemini Enterprise app. If write actions are enabled, the agent can also modify data in place within the underlying data source, subject to the user's Identity and Access Management permissions. Gemini Enterprise supports data residency in the `us` and `eu` multi-regions. For more information, see [Gemini Enterprise locations](https://docs.cloud.google.com/gemini/enterprise/docs/locations).
  * **Customer-managed encryption keys (CMEK)** : When you use federated query mode, your underlying data remains in the connected data source, where you can configure CMEK directly in that service. In Gemini Enterprise, you can use encryption keys managed in Cloud Key Management Service to protect data at rest, including query results returned to the agent and stored in conversations, connector configurations, and end-user credentials. For more information, see [Customer-managed encryption keys](https://docs.cloud.google.com/gemini/enterprise/docs/cmek).
  * **VPC Service Controls** : You can protect your Gemini Enterprise apps and Data Cloud connectors within a VPC Service Controls service perimeter to help mitigate data exfiltration risks. When VPC Service Controls is enabled, you must also allow the Data Cloud connector IDs in your organization policies as described in [Allow Data Cloud connectors in organization policies](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security/#allow-connectors-org-policies). For general perimeter setup instructions, see [Use VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).


## Allow Data Cloud connectors in organization policies
If your project is protected by a VPC Service Controls perimeter, or is explicitly included in the `enforcedProjects` parameter of an organization policy, Gemini Enterprise enforces the Google-managed `constraints/discoveryengine.managed.allowedDataSources` organization policy constraint. This constraint blocks data store creation unless the connector's internal identifier is explicitly listed in the policy's `allowedDataSources` parameter.
To allow Data Cloud connectors, add the corresponding connector identifier to the `allowedDataSources` parameter:
  * `bigquery_mcp`: Allows the BigQuery federated data connector.
  * `spanner`: Allows the Spanner federated data connector.
  * `cloudsql`: Allows the Cloud SQL federated data connector.
  * `alloydb`: Allows the AlloyDB for PostgreSQL federated data connector.


For more information about managed constraints and step-by-step instructions for configuring organization policies in the Google Cloud console, see the following resources:
  * [Overview of managed policy constraints](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/managed-policy-constraints-overview)
  * [Configure allowed data sources](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-allowed-data-sources)
  * [Configure allowed egress FQDNs](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-allowed-egress-fqdns)


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

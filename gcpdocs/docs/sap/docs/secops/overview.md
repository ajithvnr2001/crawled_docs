---
url: https://docs.cloud.google.com/sap/docs/secops/overview/
title: Secure SAP applications with Google SecOps \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-01T05:45:17.808092+00:00
---

# Secure SAP applications with Google SecOps  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/secops/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Secure SAP applications with Google SecOps Stay organized with collections  Save and categorize content based on your preferences. 

Integrate business-critical SAP telemetry into [Google Security Operations](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview) (SecOps) to help secure your enterprise applications. Google SecOps for SAP closes the visibility gap between SAP environments and security operations, letting your analysts detect, investigate, and respond to SAP-specific threats alongside the broader IT landscape. 

Integrating SAP infrastructure and application logs into your security operations helps you defend business-critical data against unauthorized access, data exfiltration, and fraud without needing specialized SAP expertise or custom log pipelines.

To deploy and manage this integration, make sure that you're familiar with the following concepts:

  * **Security operations:** Basic understanding of [security information and event management (SIEM)](https://cloud.google.com/discover/what-is-siem) concepts, [security orchestration, automation, and response (SOAR)](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/soar-overview) concepts, [log parsing](https://docs.cloud.google.com/chronicle/docs/event-processing/parsing-overview), [alert management](https://docs.cloud.google.com/chronicle/docs/investigation/investigate-alert), and [automated response playbooks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/whats-on-the-playbooks-screen).
  * **Google SecOps concepts:** Understanding of [Unified Data Model (UDM)](https://docs.cloud.google.com/chronicle/docs/event-processing/udm-overview) and [YARA-L](https://docs.cloud.google.com/chronicle/docs/yara-l/getting-started) syntax is helpful but isn't required for initial setup.



## Target audience

Google SecOps for SAP is designed for the following personas:

  * **SAP Basis administrators:** Configure SAP log extraction and manage the health of the connection to Google SecOps.
  * **SecOps teams and analysts:** Use Google SecOps to monitor SAP-specific threats alongside the rest of the IT landscape.
  * **Chief Information Security Officer (CISO) and compliance teams:** Monitor enterprise security posture and ensure regulatory compliance through unified visibility.



## Key benefits

Integrating your SAP logs into Google SecOps provides the following benefits:

  * **Unified enterprise-wide visibility:** Gain a centralized view for monitoring threats across your entire IT infrastructure, including on-premises, cloud, and SAP RISE environments.
  * **Business-critical protection:** Defend sensitive data, such as financial records, customer information, and intellectual property, by using Google's threat intelligence and curated SAP-specific security detections.
  * **Actionable intelligence** : Use SAP-specific YARA-L detection rules and automated response (SOAR) playbooks to identify threats and contain incidents across your SAP systems.
  * **Operational efficiency:** Stop building and maintaining complex, custom log pipelines. Use SAP-specific standard parsers to normalize raw SAP data into the UDM without requiring deep SAP technical expertise.
  * **AI-powered insights:** Use [Gemini in Google SecOps](https://docs.cloud.google.com/chronicle/docs/secops/gemini-chronicle) to accelerate threat hunting, summarize complex cases, and automate response workflows with natural language prompts.
  * **Expertise without the overhead:** Help your existing SecOps team [detect and respond to SAP threats](https://docs.cloud.google.com/sap/docs/secops/detect-sap-threats) in near real-time using standard security terminology and playbooks.



## Supported log sources

You can use Google SecOps for SAP to help secure your entire SAP landscape, regardless of where your SAP system is hosted or how your landscape is managed.

### Supported environments

You can monitor SAP systems running in the following environments:

  * **SAP RISE:** Managed SAP landscapes on Google Cloud or other cloud platforms.
  * **Self-managed cloud:** SAP systems that you manage on Google Cloud or other cloud platforms.
  * **On-premises:** SAP systems that run in your local data centers.



### Supported log types

Google SecOps for SAP provides ingestion and parsing capabilities for critical logs across both infrastructure and application layers:

Log category | SAP log sources  
---|---  
**Infrastructure** | SAP HANA Audit, SAP ICM, SAP Gateway, and SAP Web Dispatcher  
**Application** | SAP Security Audit Logs and SAP Change Documents  
  
For information about how these logs are ingested and the extraction mechanisms used for each environment, see [Plan for log ingestion](https://docs.cloud.google.com/sap/docs/secops/plan-log-ingestion).

## Integration workflows

The Google SecOps for SAP solution operates across two workflows: an [inbound pipeline for log ingestion and threat detection](https://docs.cloud.google.com/sap/docs/secops/overview#log-ingestion-workflow), and an outbound pipeline for automated response.

### Log ingestion and detection workflow

The following diagram shows how the integration workflow routes your SAP logs from the source environment to Google SecOps for analysis.

![Google SecOps for SAP integration workflow](https://docs.cloud.google.com/sap/docs/images/secops-sap-workflow.svg)

The integration lifecycle includes the following stages:

  1. **Log extraction** : Capture logs from your SAP source and route the data to Google SecOps:

     * **Data capture** : Infrastructure and application logs are gathered from your environment using SAP LogServ, the Application Telemetry Collector, or the Bindplane agent.
     * **Data movement** : Captured logs are then securely transferred to Google SecOps through the Bindplane server or feeds.
  2. **Log ingestion and parsing** : Receive and normalize raw SAP logs within Google SecOps using standard SAP parsers to prepare the logs for analysis:

     * **Data ingestion** : Google SecOps receives logs directly or pulls them from storage buckets.
     * **Automated parsing** : Google SecOps uses SAP-specific standard parsers to convert complex logs into the structured UDM format.
  3. **Detect, investigate, and respond to threats** : Transition from data collection to active SIEM and SOAR operations:

     * **Threat detection (SIEM)** : Monitor your SAP landscape using curated YARA-L rules designed by Google security experts.
     * **Automated response (SOAR)** : Respond to alerts by triggering automated SOAR playbooks.



### Automated response workflow

**Preview — Automated response workflow**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The following diagram shows how the automated response workflow transitions your SAP logs from the source environment into actionable security insights.

![Google SecOps for SAP automated response workflow](https://docs.cloud.google.com/sap/docs/images/secops-sap-workflow-soar.svg)

While the ingestion workflow pulls data into Google SecOps, the automated response workflow connects Google SecOps back to your SAP environment to execute mitigation actions as follows:

  1. **Threat detection and case creation:** A predefined YARA-L rule detects a threat and generates an alert. Google SecOps then groups the alert into a case.
  2. **Playbook execution:** In response to this alert or case, Google SecOps triggers a SOAR playbook that generates a mitigation command.
  3. **Command routing:** Google SecOps formats the mitigation command as an HTTP request and routes it to your Google SecOps remote agent.
  4. **Gateway translation:** The remote agent forwards this HTTP request to the SAP RFC Gateway that runs on Cloud Run.
  5. **SAP mitigation:** The SAP RFC Gateway translates the HTTP request into a Remote Function Call (RFC) and executes the action (for example, locking a user) directly in your SAP system.



## Solution components and pricing

To use Google SecOps for SAP, you combine the core security platform, specialized ingestion components, and curated security content.

  * **Google SecOps** : The central SaaS platform that provides SIEM and SOAR capabilities. Google SecOps serves as the destination for your SAP logs, featuring built-in log types and parsers that transform raw, complex SAP data into actionable security insights. Google SecOps is available in packages and pricing is based on ingestion. For more information, see the [Google SecOps pricing guide](https://cloud.google.com/security/products/security-operations#pricing) and [Understand your Google SecOps billing components](https://docs.cloud.google.com/chronicle/docs/onboard/understand-billing).

  * **Bindplane (Google Edition)** : Acts as the high-performance ingestion pipeline for transporting logs from self-managed SAP systems and from the Application Telemetry Collector. While [Bindplane (Google Edition)](https://bindplane.com/google) is [included at no additional cost](https://docs.bindplane.com/plans-and-pricing) for Google SecOps customers, you're responsible for the infrastructure costs of the host machines.

  * **Application Telemetry Collector** : A specialized, Docker-based log collector used to extract high-value application security logs, such as Security Audit Logs and Change Documents. Google provides the collector image at no cost. You're responsible for the infrastructure costs where the collector is hosted, as well as any associated Google Cloud service costs.

  * **SAP RFC Gateway** : A containerized HTTP-to-RFC bridge that you deploy on Cloud Run. It lets Google SecOps SOAR execute automated mitigation actions in your SAP systems. Google provides the gateway image at no cost. You're responsible for the infrastructure costs of the hosting environment, such as Cloud Run, and any associated Google Cloud services.

  * **Google Cloud services** : Depending on your ingestion path, you incur charges for using the following Google Cloud services:

    * **Cloud Storage** : Stores logs from SAP LogServ and hosts dependencies for the Application Telemetry Collector. For information about pricing, see [Cloud Storage pricing](https://docs.cloud.google.com/storage/pricing).
    * **Pub/Sub** : Required for SAP RISE environments to provide the notification mechanism for near real-time ingestion. For information about pricing, see [Pub/Sub pricing](https://docs.cloud.google.com/pubsub/pricing).
    * **Secret Manager** : Securely stores SAP service user credentials for the Application Telemetry Collector. For information about pricing, see [Secret Manager pricing](https://docs.cloud.google.com/secret-manager/pricing).
    * **Cloud Run** : Hosts the containerized SAP RFC Gateway required for automated response capabilities. For information about pricing, see [Cloud Run pricing](https://docs.cloud.google.com/run/pricing).
  * **SAP RISE (LogServ)** : Provides streamlined access to infrastructure logs for customers in SAP RISE environments. SAP manages this service, which delivers logs to a storage bucket and uses an event-driven notification mechanism, such as Pub/Sub, to achieve near real-time ingestion with minimal latency. To use LogServ and understand its pricing, contact your SAP account representative.




## Solution versioning and maintenance

Google SecOps for SAP consists of the following components, and each component follows its own versioning and maintenance lifecycle:

  * **Application Telemetry Collector** : Google distributes the collector as a container image in Artifact Registry. To support all log sources, distributed locking, and performance optimizations, you must update to the latest General Availability (GA) image of the collector. You update the collector by pulling the latest image tag (such as `1.1` or `latest`) from Artifact Registry. To update the collector, see the update instructions for your environment: [Self-managed systems](https://docs.cloud.google.com/sap/docs/secops/ingest-self-managed-sap-logs#update-the-application-telemetry-collector) or [SAP RISE](https://docs.cloud.google.com/sap/docs/secops/ingest-sap-rise-logs#update-the-application-telemetry-collector).
  * **SAP RFC Gateway** : Google distributes the gateway as a container image that you deploy to Cloud Run. When Google releases response actions or security updates, you update the gateway by deploying the latest container image tag. For deployment instructions, see [Deploy the SAP RFC Gateway](https://docs.cloud.google.com/sap/docs/secops/configure-sap-response-integration#deploy-sap-rfc-gateway-cloud-run).
  * **SAP transport** : Google provides the transport as an SAP transport request containing custom function modules (`/GOOG/READ_CHANGE_DOCUMENTS` and `/GOOG/ACTIVATE_SEC_AUDIT_LOG`). When Google releases function modules updates or patches, you re-import the transport as described in [Import the SAP transport](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#import-the-sap-transport).
  * **Google SecOps parsers and detection content** : Google manages and automatically updates standard SAP parsers and UDM mappings in the cloud without requiring manual intervention. When Google updates the SAP YARA-L detection rules on GitHub, you can download and import the updated files into your environment.



## Licensing

Google SecOps for SAP downloadable components (for example, the Application Telemetry Collector and the SAP RFC Gateway) are made available as "Software" under the agreement governing your use of Google Cloud Platform, including the Service Specific Terms available at <https://cloud.google.com/terms/service-terms>. Without limiting the generality of the Service Specific Terms, you may not modify or distribute these components without express written permission from Google.

These components are offered at no cost. For clarity, your use of other "Software" and "Services" under the agreement governing your use of Google Cloud Platform, such as Google SecOps, Cloud Storage, Pub/Sub, and Secret Manager, incurs a cost.

Google SecOps for SAP components do not include any license to SAP software (such as the SAP Java Connector) or third-party solutions (such as Bindplane); you must separately procure appropriate licenses for those products.

## Get support

For issues related to Google SecOps for SAP, [contact Google SecOps support](https://docs.cloud.google.com/chronicle/docs/getting-support). Our team provides assistance or guides you to the right resource to help ensure a timely resolution.

For issues involving SAP systems or the LogServ service, contact SAP support. For issues related to other third-party products, such as Bindplane, contact the appropriate third-party vendor for assistance.

Get technical answers and peer support in the [Google SecOps Community](https://security.googlecloudcommunity.com/google-security-operations-2).

## What's next

  * [Plan for log ingestion](https://docs.cloud.google.com/sap/docs/secops/plan-log-ingestion)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 

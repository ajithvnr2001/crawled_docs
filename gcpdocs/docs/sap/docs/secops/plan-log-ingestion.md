---
url: https://docs.cloud.google.com/sap/docs/secops/plan-log-ingestion/
title: Plan for log ingestion \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T12:39:36.848133+00:00
---

# Plan for log ingestion  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/secops/plan-log-ingestion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Plan for log ingestion Stay organized with collections  Save and categorize content based on your preferences. 

Before you deploy Google Security Operations for SAP, develop a deployment strategy. 

This guide helps you:

  * Choose the ingestion path for logs from your SAP RISE or self-managed environments.
  * Review how SAP logs map to Google SecOps log types.
  * Verify infrastructure, network, and SAP software version requirements for log extraction.
  * Evaluate the architectural requirements for the automated response (SOAR) integration ([Preview](https://cloud.google.com/products#product-launch-stages)).
  * Evaluate factors that impact log delivery and latency.



## Select your log ingestion path

The ingestion path varies depending on whether SAP manages your environment (SAP RISE) or you manage the landscape yourself (on-premises or any cloud).

The following table summarizes the ingestion path for each SAP environment and log category:

SAP environment | Log category | Ingestion path  
---|---|---  
**Managed by SAP (SAP RISE)** | Infrastructure logs | SAP LogServ and Google SecOps feeds  
Application logs | Application Telemetry Collector, Bindplane agent, and Bindplane server  
**Self-managed** | Infrastructure logs | Bindplane agent and Bindplane server  
Application logs | Application Telemetry Collector, Bindplane agent, and Bindplane server  
**Note:** To extract security and audit logs from the SAP Business Technology Platform (BTP), you deploy a separate Cloud Run collection script. For architecture and setup instructions, see [Collect SAP BTP logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-btp).

### For SAP RISE environments

In an SAP RISE environment, the ingestion path depends on the type of logs that you are ingesting.

#### Infrastructure logs

The ingestion path for RISE infrastructure logs involves the following stages:

  1. **Log extraction** : SAP LogServ writes infrastructure logs to cloud-based storage, such as Cloud Storage, Amazon S3, or Azure Blob Storage.
  2. **Transfer** : SAP LogServ triggers an event-driven notification to alert Google SecOps that new data is available.
  3. **Parsing** : Google SecOps feeds pull the logs from the storage bucket and normalize them into the UDM format by using the standard SAP parsers.



#### Application logs

The ingestion path for RISE application logs involves the following stages:

  1. **Log extraction** : The Application Telemetry Collector connects to the SAP RISE environment by using the RFC protocol to extract application logs.
  2. **Transfer** : The collector forwards the logs to the Bindplane server, which batches and sends them to Google SecOps.
  3. **Parsing** : Google SecOps processes the incoming logs and normalizes the data into the UDM format by using the standard SAP parsers.



### For self-managed environments

For environments where you manage the infrastructure, the ingestion path depends on the type of logs that you are ingesting.

#### Infrastructure logs

The ingestion path for self-managed infrastructure logs involves the following stages:

  1. **Log extraction** : The Bindplane agent, which is installed on each SAP host, tails local infrastructure logs.
  2. **Transfer** : The agent forwards the logs to the central Bindplane server, which sends them to Google SecOps.
  3. **Parsing** : Google SecOps processes the incoming logs and normalizes the data into the UDM format by using the standard SAP parsers.



#### Application logs

The ingestion path for self-managed application logs involves the following stages:

  1. **Log extraction** : The Application Telemetry Collector connects to your self-managed SAP instances through the RFC protocol to extract application logs.
  2. **Transfer** : The collector forwards the logs to the Bindplane server, which batches and sends them to Google SecOps.
  3. **Parsing** : Google SecOps processes the incoming logs and normalizes the data into the UDM format by using the standard SAP parsers.



## Review supported log sources

The following table provides the mapping between your SAP log sources, their typical locations, and the corresponding Google SecOps log types.

**Note:** The **Log location** column specifies paths on self-managed hosts. In an SAP RISE environment, SAP ECS manages the extraction and delivery of logs to your storage bucket.Log category | SAP log source | Log location (Self-managed) | SecOps log type  
---|---|---|---  
**Infrastructure** | **SAP ICM Logs** | `/usr/sap/SID/DINSTANCE_NUMBER/work/dev_icm` | `SAP_ICM`  
**SAP Gateway Logs** | `/usr/sap/SID/DINSTANCE_NUMBER/work/dev_rd` | `SAP_GATEWAY`  
**SAP Web Dispatcher Logs** | `/usr/sap/SID/WINSTANCE_NUMBER/work/dev_webdisp` | `SAP_WEBDISP`  
**SAP HANA Audit Logs** | `/usr/sap/SID/HDBINSTANCE_NUMBER/HOSTNAME/trace/audit_log_backup.csv` | `SAP_HANA_AUDIT`  
**Application** | **Change Document Logs** | Database tables `CDHDR` and `CDPOS` | `SAP_CHANGE_DOCUMENT`  
**Security Audit Logs** | File system | `SAP_SECURITY_AUDIT`  
  
## Verify technical requirements

Before you configure log ingestion or automated response, verify that your SAP instances and hosting infrastructure meet the following technical specifications.

### System and version requirements

Verify that your SAP systems meet the following minimum SAP NetWeaver version requirements for infrastructure and application logs:

Component | Minimum version | Notes  
---|---|---  
SAP NetWeaver | SAP_BASIS 7.00 | Required to ingest infrastructure logs.  
SAP NetWeaver | SAP_BASIS 7.50 | Required to ingest application logs.  
  
### Infrastructure requirements

Review the following infrastructure requirements based on the components you plan to deploy.

#### Log ingestion infrastructure

The following requirements apply to the host machine that runs the Application Telemetry Collector and Bindplane components.

You can deploy the collector on the infrastructure that best matches your organizational standards, including Google Compute Engine, AWS EC2, Azure VM, on-premises Linux servers, or persistent pods on Google Kubernetes Engine.

Because the Application Telemetry Collector requires a persistent, "always-on" runtime to prevent data gaps, avoid using serverless platforms with request-based timeouts (such as Cloud Run) to host the collector.

Requirement | Specification | Notes  
---|---|---  
Operating system | Debian 11 or later, Ubuntu 22.04 or later | Supported OS for the log collector and agents.  
Container runtime | Docker Engine 20.10 or later | Required for the containerized log collector.  
  
#### Automated response infrastructure

**Preview — Automated response workflow**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To enable Security Orchestration, Automation, and Response (SOAR) capabilities for threat mitigation, you must deploy the SAP RFC Gateway. Ensure your architecture accounts for the following requirements:

  * **Infrastructure** : The gateway is a containerized Java application that you deploy as a [Cloud Run](https://docs.cloud.google.com/run/docs) service.
  * **Remote agent** : The integration relies on a [Google SecOps Remote Agent](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/what-is-a-remote-agent) to route commands securely. The agent must reside in the same Google Cloud project and use the same VPC network as the Cloud Run service.
  * **State and secrets management** : You must provision a [Cloud Storage](https://docs.cloud.google.com/storage/docs) bucket to host your gateway configuration file and the SAP Java Connector (JCo) libraries. To securely store SAP credentials or X.509 certificates without using plaintext passwords, use [Secret Manager](https://docs.cloud.google.com/secret-manager/docs).



### Network and connectivity

Ensure your network architecture allows for the following connections:

#### SAP application server connectivity

The Application Telemetry Collector and the SAP RFC Gateway (Preview) act as RFC clients and require direct network access to your SAP environment:

  * **Network connection:** A direct connection, such as a VPC network, Cloud Interconnect, or VPN (for the collector) or [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) (for the Cloud Run gateway service).
  * **Ports:** Outbound access from the collector and gateway hosts to the following ports on your SAP application servers: Port | Description  
---|---  
`32INSTANCE_NUMBER` | Standard SAP Gateway, where `INSTANCE_NUMBER` is the SAP instance number.  
`33INSTANCE_NUMBER` | SAP Gateway for secured communication, required when using Secure Network Communication.  



#### Bindplane agent and collector connectivity

Ensure your network architecture allows for the following traffic flows for management functions and log data transfer:

  * **Agent management** : All Bindplane agents, whether installed on SAP hosts or collector hosts, must have outbound connectivity to the Bindplane server host on port `3001` (OpAMP). This connection is required to manage configurations, apply updates, and monitor agent health.
  * **Log data transfer** : The Application Telemetry Collector must have outbound connectivity to the host where the Bindplane agent runs on the following ports: 
    * **Port 4317** (gRPC): OTLP data ingestion port. Required for the collector to forward logs to the agent.
    * **Port 4318** (HTTP): OTLP data ingestion port, as an alternative to gRPC.



If you are running the Bindplane agent on the same host as the Application Telemetry Collector, you must enable both the IPv4 loopback (`127.0.0.1`) and IPv6 loopback (`::1`) interfaces on the host.

#### Ingress from Google SecOps

To support automated response, the SAP RFC Gateway requires ingress HTTP traffic on port `8080` carrying execution payloads from Google SecOps webhooks.

#### Egress to Google Cloud

The log ingestion components and the SAP RFC Gateway require outbound access to the following Google Cloud API endpoints on port `443` (HTTPS). You can establish this connectivity through the public internet or through Private Google Access for hosts without an external IP address.

Service | Purpose | Destination / Endpoint  
---|---|---  
**Cloud Storage API** | Reading configuration and SAP Java Connector (JCo) libraries, and writing ingestion state. | `storage.googleapis.com` (Port 443)  
**Google SecOps API** | Sending logs to the Google SecOps API. | `malachiteingestion-pa.googleapis.com` (Port 443)  
**Secret Manager API** | Retrieving SAP or API credentials. | `secretmanager.googleapis.com` (Port 443)  
**Cloud Monitoring API** | Sending health and performance metrics for the collector. | `monitoring.googleapis.com` (Port 443)  
  
### SAP authorizations

Create a dedicated SAP service user to interact with your SAP systems. The authorizations required depend on your deployment scope.

#### Authorizations for log ingestion

To extract application logs, the service user requires the following authorizations and configurations:

  * **SAP transport** (Recommended): Import the Google-provided SAP transport into your SAP system. This transport contains the `/GOOG/READ_CHANGE_DOCUMENTS` module, which extracts change documents. If you don't install this transport, the collector falls back to the standard `RFC_READ_TABLE` module, which is not optimized for continuous data extraction and can cause significant log fetch latency.
  * **Service user** : Create a dedicated service user that the Application Telemetry Collector uses to call Remote Function Modules in SAP. Make a note of the user ID and password.
  * **Custom role** : Assign a custom role with `S_RFC` authorizations limited to the required function modules: `RSAU_API_GET_LOG_DATA` and either `/GOOG/READ_CHANGE_DOCUMENTS` (if you're using the recommended transport) or `RFC_READ_TABLE` (if using the fallback method).
  * **Secure Network Communication (SNC)** (Recommended): Use X.509 certificates for mutual authentication to eliminate the need for static passwords.



#### Authorizations for automated response

The SAP RFC Gateway uses the dedicated service user to execute mitigation actions. You must assign a custom role with `S_RFC` authorizations limited to the required mitigation function modules: `BAPI_USER_LOCK`, `TH_DELETE_USER`, and `/GOOG/ACTIVATE_SEC_AUDIT_LOG` (included in the Google-provided SAP transport).

## Log delivery expectations

When planning your SIEM operations, consider the end-to-end latency for log delivery. Log delivery times vary based on several factors:

  * **SAP RISE delivery** : The time required for SAP LogServ to write logs to the storage bucket.
  * **Notification processing and polling** : The time required for the notification mechanism, such as Pub/Sub, to alert Google SecOps, or the frequency at which Google SecOps feeds or agents poll for new data.
  * **Feed processing** : The time required for the Google SecOps ingestion pipeline to parse and normalize the logs by using the standard SAP parsers.



In most cases, logs appear for search and detection in near real time, often within minutes of the event occurring in the SAP system.

## Get support

For issues related to Google SecOps for SAP, [contact Google SecOps support](https://docs.cloud.google.com/chronicle/docs/getting-support). Our team provides assistance or guides you to the right resource to help ensure a timely resolution.

For issues involving SAP systems or the LogServ service, contact SAP support. For issues related to other third-party products, such as Bindplane, contact the appropriate third-party vendor for assistance.

Get technical answers and peer support in the [Google SecOps Community](https://security.googlecloudcommunity.com/google-security-operations-2).

## Further reading

For more information about using Bindplane and Google SecOps, see the following documentation:

  * [Google SecOps: Use Bindplane for ingestion](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent)
  * [Google SecOps: Data processing pipeline](https://docs.cloud.google.com/chronicle/docs/ingestion/data-processing-pipeline)
  * [Bindplane documentation](https://docs.bindplane.com/)



## What's next

  * [Prepare your environment for log ingestion](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion)
  * [Set up log ingestion for SAP RISE](https://docs.cloud.google.com/sap/docs/secops/ingest-sap-rise-logs)
  * [Set up log ingestion for self-managed SAP systems](https://docs.cloud.google.com/sap/docs/secops/ingest-self-managed-sap-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

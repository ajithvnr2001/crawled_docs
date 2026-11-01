---
url: https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion/
title: Prepare your environment for log ingestion \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-01T05:45:18.038486+00:00
---

# Prepare your environment for log ingestion  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Prepare your environment for log ingestion Stay organized with collections  Save and categorize content based on your preferences. 

This guide explains how to:

  * **Onboard to Google SecOps** : Provision and configure your Google SecOps instance.
  * **Set up the Bindplane server** : Install and configure the centralized ingestion point required for all application logs and self-managed infrastructure logs.
  * **Prepare for infrastructure logs ingestion** : Coordinate for [SAP RISE (LogServ)](https://blog.sap-press.com/cybersecurity-for-rise-with-sap) and confirm your infrastructure is ready for self-managed log collection.
  * **Prepare for application logs ingestion** : Set up the required Google Cloud resources, SAP service user, authorizations, and secure communication.
  * **Prepare for automated response ([Preview](https://cloud.google.com/products#product-launch-stages)):** Set up the required SAP transport, authorizations, and Google Cloud resources to allow Google SecOps to execute mitigation actions in your SAP system.



After completing these preparation steps, you configure the ingestion-specific resources as part of the log ingestion setup for your specific environment.

## Onboard to Google SecOps

Before ingesting SAP logs into Google SecOps, provision and configure a Google SecOps instance. A Google Cloud project serves as the control layer for this instance, where your security logs, audit logs, and sensitive instance-level data are stored. The onboarding process involves preparing your Google Cloud environment, setting up an identity provider, and deploying the instance through an activation link.

### Google SecOps resources

For detailed configuration guides, see the following Google SecOps documentation:

Resource | Description  
---|---  
[Onboarding Overview](https://docs.cloud.google.com/chronicle/docs/onboard) | Primary guide for deploying Standard, Enterprise, and Enterprise Plus packages.  
[Configure Google Cloud project](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project) | Detailed steps for enabling the Google SecOps API and setting up the project control layer.  
[Link a Google SecOps instance to Google Cloud](https://docs.cloud.google.com/chronicle/docs/onboard/link-chronicle-cloud) | Instructions for using the one-time activation link and connecting to Google SecOps services.  
[Configure third-party identity](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication) | Setup guide for Workforce Identity Federation with providers like Okta or Azure AD.  
[Configure Google Cloud identity](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-authentication) | Configuration steps for organizations using Cloud Identity or Google Workspace.  
[Access a Google SecOps instance](https://docs.cloud.google.com/chronicle/docs/onboard/log-in-to-new-instance) | Post-deployment requirements to ensure administrators and users can sign in.  
  
For permissions required to deploy a Google SecOps instance, see [Required roles and permissions](https://docs.cloud.google.com/chronicle/docs/onboard#required-roles).

## Set up the Bindplane server

The Bindplane server acts as the centralized ingestion point for your SAP logs. Before configuring log ingestion, you must have a Bindplane server instance installed and accessible.

### Bindplane resources

To install and configure the Bindplane server, see the following Bindplane documentation:

Resource | Description  
---|---  
[Install PostgreSQL](https://docs.bindplane.com/deployment/virtual-machine/bindplane/postgresql/postgres-installation) | Instructions for installing the required PostgreSQL database.  
[Install Bindplane server](https://bindplane.com/download) | Instructions for installing the Bindplane server.  
[Access Bindplane UI](https://docs.bindplane.com/readme/access-bindplane-ui) | Instructions for accessing the centralized management interface.  
  
After you install the Bindplane server, ensure that you can sign in to the BindPlane UI. This access is required for subsequent configuration steps.

## Prepare for infrastructure logs ingestion

The method for extracting infrastructure logs depends on whether your environment is managed by SAP (SAP RISE) or self-managed.

### For SAP RISE (LogServ)

In an SAP RISE environment, SAP Enterprise Cloud Services (ECS) manages infrastructure log extraction through the LogServ service.

To provision and configure the LogServ service for your landscape, do the following:

  1. **Enable LogServ** : Contact your SAP account team to enable LogServ for your landscape.
  2. **Provide the Google SecOps identity** : Provide the service account that the Google SecOps feed uses to your SAP ECS representative. SAP ECS provisions the destination storage and notification resources for your landscape and grants the necessary roles to this identity, including Storage Object Viewer for Cloud Storage or S3 Bucket Policy updates for AWS.

**Note:** To find your Google SecOps feed identity, go to **SIEM Settings** > **Feeds** in the Google SecOps console and select your feed. The identity is listed as **Service Account**.
  3. **Obtain resource details** : Obtain the bucket and notification details from your SAP ECS representative. Depending on your hosting provider, these might include:

     * **Google Cloud** : Storage bucket URI and Pub/Sub subscription name.
     * **AWS** : S3 bucket URI and SQS queue ARN.
     * **Azure** : Storage account name, container name, and storage queue URI.



### For self-managed systems

For self-managed environments, infrastructure logs are collected by the Bindplane agents installed on your SAP hosts.

To prepare for this collection, ensure you have completed the Set up the Bindplane server step. You install and configure the individual agents during the [log ingestion setup for self-managed SAP](https://docs.cloud.google.com/sap/docs/secops/ingest-self-managed-sap-logs).

## Prepare for application logs ingestion

Connect to your SAP application servers through the Application Telemetry Collector to extract application logs. These steps apply to both SAP RISE and self-managed environments.

### Configure Google Cloud resources for log ingestion

Set up the required Google Cloud resources and identity for the Application Telemetry Collector.

#### Enable APIs

Enable the following APIs in your project:

  * **Secret Manager API** (`secretmanager.googleapis.com`): Required to securely store and retrieve SAP service user credentials and SNC artifacts.
  * **Cloud Storage API** (`storage.googleapis.com`): Required to manage the storage buckets used for SAP Java Connector (JCo) libraries and configuration state.
  * **Cloud Monitoring API** (`monitoring.googleapis.com`): Required to send health and performance metrics for the collector.



For information about how to enable Google Cloud APIs, see [Enabling APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis).

#### Set up Cloud Storage buckets and IAM roles

Set up the Cloud Storage buckets and IAM roles required for the collector to store its configuration and libraries.

  * **Service Account and IAM** : In your Google Cloud project, create a Service Account for the collector and grant the following roles:

    * **Storage Object Admin (`roles/storage.objectAdmin`)**: To read configuration and libraries, and maintain application state.
    * **Secret Manager Secret Accessor (`roles/secretmanager.secretAccessor`)**: Required to retrieve SAP credentials, PSE files, and certificates from Secret Manager.
    * **Monitoring Metric Writer (`roles/monitoring.metricWriter`)**: Required if you set `heartbeat_enabled` to `true` in your configuration.

For more information, see [Create service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-create) and [Grant or revoke a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#single-role).

  * **Service Account Key** (External hosts only): If your collector host is outside Google Cloud, then create and download a **Service Account key (JSON)**. This key is used for authentication between the collector and Google Cloud APIs.

For more information about managing service account keys, see [Create and delete service account keys](https://docs.cloud.google.com/iam/docs/keys-create-delete).

  * **Cloud Storage** : Create a bucket in your project to store the JCo libraries and configuration.

    * Create a folder named `jco/`. Download the SAP Java Connector files (`sapjco3.jar` and `libsapjco3.so`) from the [SAP Support Portal](https://support.sap.com/en/product/connectors/jco.html) and upload them to this folder. Ensure that you download the Linux 64-bit version (ARM or x86) that matches your host machine's architecture.
    * If you use SNC, download the `libslcryptokernel.so` and `libsapcrypto.so` files from SAP, extract them using the `sapcar` utility, and upload them to the `jco/` folder. For instructions on how to download the `.SAR` file and extract the files by using the `sapcar` utility, see the [SAP documentation](https://help.sap.com/docs/SAP_HANA_CLIENT/8e208b44c0784f028b948958ef1d05e7/463d3ceeb7404eca8762dfe74e9cff62.html).
    * Create a folder named `config/`. This folder stores the configuration files for your telemetry collector and RFC gateway that you create during the setup phases.

For instructions on creating and managing buckets, see [Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets).




### Prepare the SAP application layer for log ingestion

Configure your SAP system to allow the Application Telemetry Collector to connect and extract the required logs.

#### Import the SAP transport

To ensure optimal log extraction performance and enable automated response capabilities, import the provided SAP transport request into your SAP system.

The transport contains the following custom function modules:

  * **`/GOOG/READ_CHANGE_DOCUMENTS`** : Efficiently extracts SAP change document logs (`CDHDR` and `CDPOS`) for ingestion. If you don't install this transport, the collector falls back to the standard `RFC_READ_TABLE` module, which isn't optimized for continuous data extraction and can cause log fetch latency.
  * **`/GOOG/ACTIVATE_SEC_AUDIT_LOG`** ([Preview](https://cloud.google.com/products#product-launch-stages)): Lets SOAR playbooks dynamically reactivate the SAP Security Audit Log during an incident.



Download the [SAP transport package (`google-secops-for-sap-1.0.zip`)](https://storage.googleapis.com/cloudsapdeploy/secops/google-secops-for-sap-1.0.zip) and extract the transport files. Import the transport request into your target SAP system following your organization's standard transport procedure, such as by using transaction `STMS` or `STMS_IMPORT`.

#### Create an SAP service user

Google Security Operations for SAP uses a dedicated SAP service user to connect to your SAP system and extract application logs through the Application Telemetry Collector.

To create the SAP service user, do the following:

  1. In your SAP system, run transaction `SU01`.
  2. In the **User** field, enter a name for the service user and click **Create**.
  3. On the **Address** tab, provide any required information, such as the last name.
  4. On the **Logon Data** tab, configure the following settings: 
     * Set the **User Type** to **System** or **Communication**. These types ensure that the user can only be used for background tasks or API calls and can't be used for interactive logons.
     * Assign and confirm a secure **Password**.
  5. Make a note of the **user ID** and **password**. You need these credentials when you configure the Application Telemetry Collector.
  6. Recommended: If you use Secure Network Communication (SNC), configure X.509 certificates for mutual authentication on the **SNC** tab to avoid using static passwords. Set the Quality of Protection (QoP) to **Privacy** (Level 3) to ensure end-to-end payload encryption.



For information about how to maintain user accounts, see [SAP Community: How to create a new user in SAP](https://community.sap.com/t5/technology-blog-posts-by-members/su01-how-to-create-a-new-user-in-sap/ba-p/13562053).

#### Configure SAP authorizations

To extract logs from the SAP application layer, the service user requires specific SAP authorizations. We recommend creating a custom role, for example, `Z_GOOGLE_SECOPS_COLLECTOR`, and assigning the role to the service user.

##### Set up remote function call (RFC) authorizations

The collector acts as an RFC client. Authorize the service user to execute the following function modules:

Authorization object | Field | Value  
---|---|---  
`S_RFC` | `RFC_TYPE` | `FUNC` (Function module)  
`S_RFC` | `RFC_NAME` | `RSAU_API_GET_LOG_DATA` and either `/GOOG/READ_CHANGE_DOCUMENTS` (recommended) or `RFC_READ_TABLE` (fallback method)  
`S_RFC` | `ACTVT` | `16` (Execute)  
**Note:** If the function module `RSAU_API_GET_LOG_DATA` is missing in your system, contact your SAP Basis team to apply [SAP Note 2926298](https://launchpad.support.sap.com/#/notes/2926298).

##### Set up security audit log authorizations

To extract Security Audit Logs, the service user requires access to one of the following objects, depending on the SAP release:

  * **Primary** : Object `S_SAL`
  * **Fallback (Older SAP releases)** : Object `S_ADMI_FCD`

Authorization object | Field | Value  
---|---|---  
`S_SAL` | `SAL_ACTVT` | `SHOW_LOG`  
`S_ADMI_FCD` | `S_ADMI_FCD` | `AUDD`  
  
##### Set up table access authorizations

To read SAP Change Documents, the service user requires read access to the following tables:

Authorization object | Field | Value  
---|---|---  
`S_TABU_DIS` | `DICBERCLS` | `&NC&` (or the specific group for `CDHDR`/`CDPOS`)  
`S_TABU_NAM` | `TABLE` | `CDHDR`, `CDPOS`  
`S_TABU_DIS` | `ACTVT` | `03` (Display)  
  
#### Enable security audit logging

The Application Telemetry Collector extracts logs from the SAP Security Audit Log. To ensure logs are available for extraction:

  1. Use transaction `SM19`, or `RSAU_CONFIG` in newer versions, to confirm that Security Audit Logging is status **Active**.
  2. Ensure that the logging filters are configured to capture the events you want to monitor in Google SecOps.



### Configure authentication and encryption

Specify how the Application Telemetry Collector or the SAP RFC Gateway authenticates with your SAP system. You can use either basic authentication (username and password) or Secure Network Communication (SNC) with X.509 certificates.

#### Basic authentication

Use basic authentication if you want to connect to SAP using a username and password.

  1. **SAP Credentials** : Ensure you have the user ID and password for the SAP service user that you created in the Create an SAP service user step.
  2. **Store credentials in Secret Manager** : Create two secrets in Secret Manager to securely store the username and password.



For information about creating secrets, see [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart).

When you create the secrets, make a note of the fully qualified name for the secret version: `projects/PROJECT_ID/secrets/SECRET_NAME/versions/VERSION`.

#### Secure Network Communication (SNC)

We recommend that you use SNC to protect your SAP credentials and encrypt log data in transit. SNC supports X.509 certificates for mutual authentication, which eliminates the need to maintain static passwords.

##### Configure SNC for X.509 certificate-based authentication

If you use X.509 certificates for authentication, then configure SNC for the service user. For detailed instructions, see the [SAP documentation](https://help.sap.com/docs/SAP_SINGLE_SIGN-ON/df185fd53bb645b1bd99284ee4e4a750/631b1669678d41d79d94601c238e218b.html) or [Section 4.10: X.509 and Kerberos Authentication](https://help.sap.com/doc/7d3f26c449524c54b5d8232e11f0a771/3.0/en-US/SecureLoginForSAPSSO3.0_UACP.pdf) in the SAP Single Sign-On guide.

To generate the required SNC artifacts, run the following `sapgenpse` commands on a secure Linux machine where you have downloaded the SAP Crypto library:

  1. Create the PSE file:
         
         sapgenpse get_pse -p PSE_NAME SNC_NAME
         

  2. Create the credentials file (`cred_v2`):
         
         sapgenpse seclogin -p PSE_NAME -O OS_USER
         

  3. Export the public certificate:
         
         sapgenpse export_own_cert -p PSE_NAME -o collector_cert.crt
         




Replace the following:

  * PSE_NAME: The name of your PSE file, for example `sapcrypto.pse`.
  * SNC_NAME: The SNC name of the Application Telemetry Collector or the SAP RFC Gateway as configured in SAP.
  * OS_USER: The operating system user that runs the Application Telemetry Collector container or the SAP RFC Gateway container.



##### Store SNC artifacts in Secret Manager

After you generate the required artifacts, create a secret in Secret Manager for each of the following files:

  * **PSE file** : The generated `.pse` file.
  * **Credentials file** : The generated `cred_v2` file.
  * **Public certificate** : The generated `collector_cert.crt` file.



For information about creating secrets, see [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart).

When you create the secrets, make a note of the fully qualified name for the secret version: `projects/PROJECT_ID/secrets/SECRET_NAME/versions/VERSION`.

## Prepare for automated response

**Preview — Automated response workflow**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If you plan to use Google SecOps SOAR to trigger automated mitigations, complete the following preparation steps for your Google Cloud and SAP environments.

The SAP RFC Gateway shares several foundational resources with the Application Telemetry Collector. Before proceeding, ensure that you have completed the following shared preparation steps from the log ingestion section:

  * Created a Cloud Storage bucket and uploaded the SAP Java Connector (JCo) and Crypto libraries, as described in Set up Cloud Storage buckets and IAM roles.
  * Stored your SAP credentials securely in Secret Manager. Depending on your chosen authentication method, ensure that you've completed the following: 
    * **For basic authentication:** Created secrets for your SAP username and password as described in Basic authentication.
    * **For X.509 authentication:** Generated the gateway's SNC artifacts and created secrets for the PSE, `cred_v2`, and public certificate files, as described in Configure SNC for X.509 certificate-based authentication.
  * Imported the Google-provided SAP transport as described in Import the SAP transport. This transport includes the `/GOOG/ACTIVATE_SEC_AUDIT_LOG` module required for specific SOAR playbooks.



Once this shared foundation is in place, complete the following SOAR-specific configurations.

### Configure Google Cloud resources for automated response

  1. Enable the Cloud Run API in your Google Cloud project. This API is required to deploy the SAP RFC Gateway container.
  2. Create a service account for the Cloud Run service. Grant the service account the `roles/storage.objectAdmin` role to access your Cloud Storage bucket and the `roles/secretmanager.secretAccessor` role to access your SAP secrets.



### Configure SAP authorizations

To execute mitigation functions, the dedicated SAP service user requires a custom role with `S_RFC` authorizations limited to the following function modules:

Authorization object | Field | Value  
---|---|---  
`S_RFC` | `RFC_TYPE` | `FUNC` (Function module)  
`S_RFC` | `RFC_NAME` |  `BAPI_USER_LOCK`, `TH_DELETE_USER`, and `/GOOG/ACTIVATE_SEC_AUDIT_LOG` (included in the Google-provided SAP transport)   
`S_RFC` | `ACTVT` | `16` (Execute)  
  
## Get support

For issues related to Google SecOps for SAP, [contact Google SecOps support](https://docs.cloud.google.com/chronicle/docs/getting-support). Our team provides assistance or guides you to the right resource to help ensure a timely resolution.

For issues involving SAP systems or the LogServ service, contact SAP support. For issues related to other third-party products, such as Bindplane, contact the appropriate third-party vendor for assistance.

Get technical answers and peer support in the [Google SecOps Community](https://security.googlecloudcommunity.com/google-security-operations-2).

## What's next

After your SAP system is prepared, choose the ingestion path for your environment:

  * [Set up log ingestion for SAP RISE](https://docs.cloud.google.com/sap/docs/secops/ingest-sap-rise-logs)
  * [Set up log ingestion for self-managed SAP systems](https://docs.cloud.google.com/sap/docs/secops/ingest-self-managed-sap-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/sap/docs/secops/configure-sap-response-integration/
title: Configure the SAP response integration \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:04.314419+00:00
---

# Configure the SAP response integration  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/secops/configure-sap-response-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Configure the SAP response integration Stay organized with collections  Save and categorize content based on your preferences. 

****

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The SAP response integration in [Google SecOps](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview) SOAR enables security operations teams to automate incident response and threat containment directly within SAP systems.

While Google SecOps drives automation through response playbooks, executing mitigation tasks inside an SAP system requires a secure bridge. The integration uses the SAP RFC Gateway, a containerized HTTP-to-RFC bridge that exposes SAP Remote Function Call (RFC) capabilities as REST endpoints that Google SecOps can securely trigger.

This document explains how to deploy the SAP RFC Gateway and connect it to Google SecOps to enable Security Orchestration, Automation, and Response (SOAR) capabilities.

## Before you begin

Before deploying the SAP RFC Gateway, complete the following prerequisites:

  * Review the architectural requirements described in [Plan for log ingestion](https://docs.cloud.google.com/sap/docs/secops/plan-log-ingestion).
  * Complete the prerequisite steps described in [Prepare for automated response](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#prepare-for-automated-response). Make sure that you have the following resources available: 
    * An active Google SecOps instance with Security Orchestration, Automation, and Response ([SOAR](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/whats-on-the-playbooks-screen)) capabilities configured.
    * A [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) with [billing enabled](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled), attached to a [Virtual Private Cloud (VPC)](https://docs.cloud.google.com/vpc/docs/overview) network that has a direct connection to your SAP application servers.
    * An existing Google SecOps remote agent that operates within the same project and VPC network as your SAP instance and Cloud Run service. If you haven't set up a remote agent, set it up by following the instructions described in [Working with remote agents](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/what-is-a-remote-agent).
    * A dedicated SAP service user authorized to execute the required mitigation functions. For authorization requirements, see [Configure SAP authorizations](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#configure-sap-authorizations-automated-response).
    * A [Cloud Storage](https://docs.cloud.google.com/storage/docs/creating-buckets) bucket containing your SAP Java Connector (JCo) libraries and SAP Crypto library.
    * Your SAP credentials stored securely in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart).
    * A provisioned [service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) for the Cloud Run service.



## Create the gateway configuration file

The SAP RFC Gateway uses a `gateway_config.json` file to define your SAP connections and route mitigation commands to the correct SAP instance during an incident.

To create and upload the gateway configuration file, do the following:

  1. In your local working directory, create a `gateway_config.json` file by using the configuration example and field descriptions.
  2. To route commands successfully during an incident, ensure that the `instance_name` for each SAP system matches the server name populated in the Unified Data Model (UDM) fields of your exported SAP security logs.
  3. Optional: To manage multiple SAP instances through a single gateway deployment, add multiple entries to the `systems` array in the configuration file. Each instance must reside in the same Google Cloud project as the SAP RFC Gateway and have a unique `instance_name`.
  4. Upload the `gateway_config.json` file to the `config/` folder in the Cloud Storage bucket that you created in [Prepare for automated response](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#prepare-for-automated-response).



### Configuration example and field descriptions

Use the following JSON example to create your gateway configuration file, and refer to the field descriptions for detailed parameter information:
    
    
    {
      "systems": [
        {
          "instance_name": "sap-prd_PRD_00",
          "connection": {
            "host": "sap-prd.example.com",
            "client": "100",
            "system_number": "00"
          },
          "auth": {
            "basic": {
              "username_secret": "projects/SAP_PROJECT_ID/secrets/SAP_RFC_USER/versions/latest",
              "password_secret": "projects/SAP_PROJECT_ID/secrets/SAP_RFC_PASS/versions/latest"
            }
          }
        },
        {
          "instance_name": "sap-dev_DEV_01",
          "connection": {
            "host": "10.128.0.50",
            "client": "200",
            "system_number": "01"
          },
          "auth": {
            "x509": {
              "snc_name": "p:CN=SAP-Gateway, O=MyCompany, C=US",
              "snc_partner_name": "p:CN=SAP-Server-DEV, O=MyCompany, C=US",
              "snc_qop": "3",
              "x509_cert_secret": "projects/SAP_PROJECT_ID/secrets/SAP_X509_CERT/versions/latest"
            }
          }
        }
      ],
      "jco_pse_secret": "projects/SAP_PROJECT_ID/secrets/SAP_GATEWAY_PSE/versions/latest",
      "jco_cred_secret": "projects/SAP_PROJECT_ID/secrets/SAP_GATEWAY_CRED/versions/latest"
    }
    

The following table describes the fields in the `gateway_config.json` file.

Section | Field | Description  
---|---|---  
**System connection (`systems`)**  
List of SAP systems to route commands to.  | `instance_name` |  The actual server name of your SAP system, for example, `sap-prd_PRD_00`. In the example, replace `sap-prd_PRD_00` with your SAP application server instance name.  To find this value in the SAP GUI, go to **System** > **Status** , and in the **Host data** section, copy the **Server name** value.  This value must match the instance name populated in logs exported from SAP so that when SOAR playbooks run, they can automatically populate this parameter when calling the response API.   
`connection` |  Contains the following RFC connection parameters: 

  * `host`: The fully qualified domain name (FQDN) or IP address of your SAP server. Replace `sap-prd.example.com` in the example. 
  * `client`: The 3-digit SAP client number, for example, `100`. 
  * `system_number`: The 2-digit SAP system instance number, for example, `00`. 

  
**Authentication (`auth`)**  
Choose one of the authentication methods.  | `basic` |  Username and password authentication. Provide the full Secret Manager paths for `username_secret` and `password_secret`. These secrets must contain the credentials of the [SAP service user](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#create-an-sap-service-user) created in the preparation guide. For more information, see [Basic authentication](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#auth-option-basic).   
`x509` (SNC) |  Secure Network Communication authentication. For setup instructions, see [Secure Network Communication (SNC)](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#configure-snc-x509). Provide the following: 

  * `snc_name`: The gateway's SNC identity, for example, `p:CN=SAP-Gateway,O=MyCompany,C=US`. 
  * `snc_partner_name`: The SNC identity of the SAP application server. 
  * `snc_qop`: (Optional) The Quality of Protection level required by the SAP server, for example, `3` for end-to-end data privacy and payload encryption. 
  * `x509_cert_secret`: (Optional) The full Secret Manager path to the secret containing the gateway's public X.509 certificate. For more information, see [Store SNC artifacts in Secret Manager](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#store-snc-artifacts). 

  
**Global gateway settings**  
Applied to the entire instance.  | `jco_pse_secret` |  The full Secret Manager path to the secret containing your binary `.pse` file (for example, `sapcrypto.pse`). For more information, see [Store SNC artifacts in Secret Manager](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#store-snc-artifacts).   
`jco_cred_secret` |  The full Secret Manager path to the secret containing your binary credentials file (`cred_v2`). For more information, see [Store SNC artifacts in Secret Manager](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#store-snc-artifacts).   
  
## Deploy the SAP RFC Gateway to Cloud Run

To deploy the SAP RFC Gateway, do the following:

  1. Deploy the SAP RFC Gateway container image as a Cloud Run service. Ensure that the service connects to the VPC network containing your SAP systems using direct VPC egress or a Serverless VPC Access connector:
         
         gcloud run deploy sap-rfc-gateway \
             --image=IMAGE_PATH \
             --region=REGION \
             --service-account=SERVICE_ACCOUNT_EMAIL \
             --set-env-vars=GATEWAY_GCS_BUCKET=gs://BUCKET_NAME \
             --vpc-egress=all-traffic \
             --network=VPC_NETWORK_NAME \
             --subnet=VPC_SUBNET_NAME \
             --port=8080
         

Replace the following:

     * `IMAGE_PATH`: The URI of the SAP RFC Gateway image in Artifact Registry. Use one of the following regional paths:

       * `us-docker.pkg.dev/sap-core-eng-products/sap-rfc-gateway/google-cloud-sap-rfc-gateway:TAG`
       * `europe-docker.pkg.dev/sap-core-eng-products/sap-rfc-gateway/google-cloud-sap-rfc-gateway:TAG`
       * `asia-docker.pkg.dev/sap-core-eng-products/sap-rfc-gateway/google-cloud-sap-rfc-gateway:TAG`

Replace `TAG` with the version of the gateway image that you want to download, for example, `latest`. For more information about how tags work, see [Artifact Registry container concepts](https://docs.cloud.google.com/artifact-registry/docs/container-concepts#tags).

     * `REGION`: The Google Cloud region where you want to deploy the service.

     * `SERVICE_ACCOUNT_EMAIL`: The email address of the dedicated Google Cloud service account that you created for the gateway.

     * `BUCKET_NAME`: The name of the Cloud Storage bucket where you uploaded the SAP JCo libraries, SAP Crypto library, and `gateway_config.json` file, for example, `sap-gateway-config`.

     * `VPC_NETWORK_NAME`: The name of the VPC network that provides connectivity to your SAP environment.

     * `VPC_SUBNET_NAME`: The name of the subnet within your VPC network that handles outbound traffic to your SAP instances.

  2. After the deployment, note the generated Cloud Run service URL. You use this URL in a later section of this procedure.




### Grant invocation permissions

By default, Cloud Run services require authentication. To allow your Google SecOps remote agent to trigger the gateway, you must grant the Cloud Run Invoker (`roles/run.invoker`) role to the service account attached to the remote agent's host VM.

For more information about Cloud Run authentication, see [Manage access with IAM](https://docs.cloud.google.com/run/docs/securing/managing-access).

To grant the Cloud Run Invoker role to the remote agent's service account, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **Cloud Run** page: 

[Go to Cloud Run](https://console.cloud.google.com/run/)

  2. Select the checkbox for the `sap-rfc-gateway` service. Don't click the service name. 
  3. Click **Permissions**. If the information pane isn't visible, click **Show info panel** , and then click **Permissions**. 
  4. Click **Add principal**.
  5. In the **New principals** field, enter the email address of the service account attached to the VM hosting your Google SecOps remote agent. 
  6. In the **Select a role** list, select **Cloud Run Invoker**. 
  7. Click **Save**.



### gcloud

Grant the Cloud Run Invoker role to the remote agent service account: 
    
    
    gcloud run services add-iam-policy-binding sap-rfc-gateway \
        --member="serviceAccount:REMOTE_AGENT_SERVICE_ACCOUNT" \
        --role="roles/run.invoker" \
        --region=REGION

Replace the following:

  * `REMOTE_AGENT_SERVICE_ACCOUNT`: the email address of the service account attached to the VM hosting your Google SecOps remote agent. 
  * `REGION`: the Google Cloud region where you deployed the gateway. 



## Configure the integration in Google SecOps

To add and configure an **SAP ERP** integration instance in Google SecOps, do the following:

  1. In the Google SecOps menu, go to **Response** > **Integrations Setup**.
  2. In the **Environments** list, select the environment where you want to configure the integration, such as **Shared Instances** or **Default Environment**.
  3. Click add **Create a new instance**.
  4. In the **Add Instance** dialog, in the **Integrations** list, search for and select **SAP ERP** , and then click **Save**.
  5. In the **SAP ERP - Configure Instance** dialog, configure the following settings: 
     * **Instance Name** : Enter a name for the integration instance, for example, `SapErp_1`.
     * **Cloud Run Service URL** : Enter the Cloud Run service URL generated when you deployed the SAP RFC Gateway.
     * **Run Remotely** : Select the **Run Remotely** checkbox, and then select the Google SecOps remote agent deployed in the same Google Cloud project and VPC network as your SAP RFC Gateway.
  6. Optional: Click **Test** to verify connectivity to your SAP RFC Gateway.
  7. Click **Save** to apply the instance configuration.



For information about how to manage integration instances, see [Add and configure an integration instance](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances#configure-integration).

## Prebuilt SAP mitigation actions

The SAP SOAR integration supports the following built-in mitigation actions:

  * **Lock compromised users** : Locks an SAP user account to prevent further unauthorized access. This action uses the `BAPI_USER_LOCK` function module.
  * **Terminate sessions** : Terminates active interactive SAP sessions to halt in-progress attacks. This action uses the `TH_DELETE_USER` function module.
  * **Activate audit logging** : Activates the SAP Security Audit Log during an incident. This action uses the `/GOOG/ACTIVATE_SEC_AUDIT_LOG` function module included in the Google-provided SAP transport.



When used in SOAR playbooks, these actions map parameters extracted from the security logs. For example, the playbook automatically reads the SAP username and the SAP System ID or instance name from the alert's Unified Data Model ([UDM](https://docs.cloud.google.com/chronicle/docs/event-processing/udm-overview)) fields, so that you don't need to manually input parameters for every response action.

**Note:** If you write custom [YARA-L rules](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) for SAP, then ensure your rule logic maps the SAP instance details and the target username to the alert's UDM fields. If these fields are missing, then the playbook cannot route the mitigation command to the correct SAP instance.

## Get support

For issues related to Google SecOps for SAP, [contact Google SecOps support](https://docs.cloud.google.com/chronicle/docs/getting-support). Our team provides assistance or guides you to the right resource to help ensure a timely resolution.

For issues involving SAP systems or the LogServ service, contact SAP support. For issues related to other third-party products, such as Bindplane, contact the appropriate third-party vendor for assistance.

Get technical answers and peer support in the [Google SecOps Community](https://security.googlecloudcommunity.com/google-security-operations-2).

## What's next

  * [Detect and investigate threats in SAP logs](https://docs.cloud.google.com/sap/docs/secops/detect-sap-threats): Review alerts and configure detection rules.
  * [Troubleshoot SAP log ingestion and response](https://docs.cloud.google.com/sap/docs/secops/troubleshooting): Resolve integration and gateway connectivity issues.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 

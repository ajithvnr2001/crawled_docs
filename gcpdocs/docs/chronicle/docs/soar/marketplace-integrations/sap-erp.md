---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/sap-erp/
title: Integrate SAP ERP with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T08:27:37.344265+00:00
---

# Integrate SAP ERP with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/sap-erp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate SAP ERP with Google SecOps 

This document explains how to integrate SAP ERP with Google Security Operations.

The SAP ERP integration connects Google SecOps to your SAP ERP environment through a Cloud Run gateway service. For more information about monitoring and securing SAP environments in Google SecOps, see [Secure SAP applications with Google SecOps](https://docs.cloud.google.com/sap/docs/secops/overview).

## Use cases

The SAP ERP integration uses Google SecOps capabilities to support the following use cases:

  * **Contain compromised SAP user accounts** : Immediately lock SAP user accounts during automated incident response playbooks when suspicious activity, credential abuse, or unauthorized privilege escalation is detected.

  * **Terminate active user sessions** : End active SAP sessions for a targeted username and client to revoke in-progress access after an account compromise or policy violation.

  * **Enforce security audit logging** : Remotely activate the SAP Security Audit Log on target SAP instances and clients to make sure critical application security events are recorded.

  * **Validate gateway connectivity** : Verify Google Cloud authentication and network connectivity between Google SecOps and the Cloud Run gateway service.




## Before you begin

Before you configure the SAP ERP integration in Google SecOps, complete the following prerequisite steps:

  1. Deploy and configure the Cloud Run SAP RFC Gateway to forward actions to your SAP ERP instances.

  2. Configure Google Cloud authentication and IAM permissions using Workload Identity or a service account JSON key.

  3. Configure SAP permissions for the gateway communication user in your target SAP clients.

  4. Verify network connectivity between Google SecOps, your Cloud Run service, and your SAP ERP instances.




### Deploy and configure the Cloud Run SAP RFC Gateway

The SAP ERP integration communicates with your SAP systems through a Cloud Run SAP RFC Gateway service. This service securely forwards actions from Google SecOps to your target SAP instances.

Make sure that your Cloud Run gateway service is deployed and configured with the connection details for each target SAP instance (`SAP Instance Name`) and three-digit SAP client (`SAP Client Number`). Record the HTTPS URL of the Cloud Run service for the `Cloud Run Service URL` integration parameter.

### Configure Google Cloud authentication and IAM permissions

To authenticate requests to your Cloud Run gateway service, configure a Google Cloud service account using one of the following methods:

  * **Workload Identity (recommended)** : Uses service account impersonation so that you don't need to download or manage static JSON keys.
  * **Service account JSON key** : Uses a downloaded JSON key file. Use this method only if you can't configure Workload Identity. If you provide both `Service Account JSON` and `Workload Identity Email`, the integration uses `Service Account JSON`.



Follow the principle of least privilege when assigning Google Cloud IAM roles. Avoid granting broad administrative roles such as `roles/owner` or `roles/editor`. Grant only the minimal roles listed in the following table:

Principal | Target resource | Required IAM role | Purpose  
---|---|---|---  
Service account (configured in `Workload Identity Email` or `Service Account JSON`) | Cloud Run SAP RFC Gateway service | **Cloud Run Invoker** (`roles/run.invoker`) | Allows the service account to call the Cloud Run gateway service.  
Google SecOps instance identity (only when using `Workload Identity Email`) | Service account specified in `Workload Identity Email` | **Service Account Token Creator** (`roles/iam.serviceAccountTokenCreator`) | Allows your Google SecOps instance to impersonate the service account when calling the gateway.  
  
#### Authenticate with Workload Identity (recommended)

To authenticate using Workload Identity, create a service account, grant it access to invoke your Cloud Run service, and authorize your Google SecOps instance to impersonate that service account.

##### Create a service account and grant Cloud Run access

  1. In the Google Cloud console, go to **IAM & Admin > [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)**.

  2. Click **Create service account** , enter a name for the service account, and click **Create and continue**.

  3. Click **Done** to finish creating the service account, and copy its email address.

  4. In the Google Cloud console, go to [**Cloud Run**](https://console.cloud.google.com/run) and select your SAP RFC Gateway service.

  5. Go to the **Security** or **Permissions** tab and click **Add principal**.

  6. In the **New principals** field, paste your service account email address.

  7. In the **Select a role** menu, select **Cloud Run Invoker** (`roles/run.invoker`), and click **Save**.




##### Grant impersonation permissions to your Google SecOps instance

  1. In Google SecOps, go to **Content Hub > Response Integrations**.

  2. Select the **SAP ERP** integration, enter your `Cloud Run Service URL`, and enter your service account email in `Workload Identity Email`.

  3. Click **Save > Test**. The test is expected to fail before you grant impersonation permissions.

  4. Click close_small next to **Test** and locate the Google SecOps instance service account email in the error message (formatted as `gke-init-python@`PROJECT`.iam.gserviceaccount.com` or `soar-python@`TENANT_PROJECT`.iam.gserviceaccount.com`). Copy this email address.

  5. In the Google Cloud console, go to **IAM & Admin > [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)** and select your service account.

  6. Go to **Permissions > Grant access**.

  7. Under **New principals** , paste the Google SecOps instance email address that you copied.

  8. Under **Assign roles** , select **Service Account Token Creator** (`roles/iam.serviceAccountTokenCreator`) and click **Save**.

**Note:** IAM changes can take a few minutes to propagate before the integration test succeeds.



#### Authenticate with a service account JSON key

If you can't use Workload Identity, create a service account and extract its JSON key file:

  1. In the Google Cloud console, go to **IAM & Admin > [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)**.

  2. Select an existing service account or click **Create service account** to create a dedicated one.

  3. Make sure the service account has the **Cloud Run Invoker** (`roles/run.invoker`) role on your Cloud Run SAP RFC Gateway service.

  4. Select your service account and go to **Keys > Add key > Create new key**.

  5. Select **JSON** as the key type and click **Create**. A JSON key file downloads to your computer.

  6. Open the downloaded file in a text editor, copy the entire JSON content, and paste it into the `Service Account JSON` parameter in Google SecOps.




### Configure SAP permissions

In each target SAP client, grant the SAP communication user configured in your Cloud Run gateway only the minimal permissions required for the actions you plan to run:

Action | Required SAP permission  
---|---  
**Activate Audit Log** | Permission to remotely activate the SAP Security Audit Log in the target SAP client.  
**Delete User Session** | Permission to run the `TH_DELETE_USER` function module to terminate active user sessions in the target SAP client.  
**Lock SAP User** | Permission to lock user accounts in the target SAP client.  
  
### Verify network connectivity

Make sure that your environment meets the following network requirements:

  * Google SecOps (or your remote agent) can reach your Cloud Run SAP RFC Gateway URL over HTTPS (port 443).
  * Your Cloud Run SAP RFC Gateway service has network connectivity to your target SAP ERP instances.



## Integration parameters

The SAP ERP integration requires the following parameters:

Parameter | Description  
---|---  
`Cloud Run Service URL` | Required. The HTTPS URL of the Cloud Run gateway service that connects to your SAP ERP instance.  
`Service Account JSON` | Optional. The service account JSON key used to authenticate with the Cloud Run gateway service. If both `Service Account JSON` and `Workload Identity Email` are provided, the integration uses `Service Account JSON`.  
`Workload Identity Email` | Optional. The service account email address used for Workload Identity authentication (recommended). Used when `Service Account JSON` is empty.  
`Verify SSL` | Optional. If selected, the integration validates the SSL certificate when connecting to the Cloud Run gateway server. Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from your workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Run a manual action in your case](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/what-actions-can-you-take-on-a-case#run-manual-action). 

### Activate Audit Log

Use the **Activate Audit Log** action to activate the SAP Security Audit Log on a target SAP instance and client through the Cloud Run SAP RFC Gateway.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Activate Audit Log** action requires the following parameters:

Parameter | Description  
---|---  
`SAP Client Number` | Required. The three-digit numeric SAP client number.  
`SAP Instance Name` | Required. The name of the target SAP instance configured in the Cloud Run SAP RFC Gateway.  
  
#### Action outputs

The **Activate Audit Log** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Activate Audit Log** action:
    
    
    {
      "status": "SUCCESS",
      "functionId": "ACTIVATE_AUDIT_LOG",
      "sap_instance": "PRD",
      "client": "100",
      "return": [
        {
          "type": "S",
          "message": "Security Audit Log activated successfully."
        }
      ]
    }
    

##### Output messages

The **Activate Audit Log** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully activated SAP audit log.` | The action succeeded.  
`Error executing action - "Activate Audit Log". Reason: Failed to activate audit log. SAP Error: ERROR_SUMMARY` | The action failed because the SAP system returned an error. Verify that the target SAP instance and client are reachable and that the gateway communication user has permission to activate the Security Audit Log.  
`Error executing action - "Activate Audit Log". Reason: SAP Client Number must be a 3-digit numeric string (got 'SAP_CLIENT_NUMBER').` | The action failed parameter validation. Provide a valid three-digit numeric string for `SAP Client Number`, such as `100`.  
`Error executing action - "Activate Audit Log". Reason: Proxy request failed (HTTP STATUS_CODE): ERROR_DETAIL` | The request to the Cloud Run SAP RFC Gateway failed. Verify the `Cloud Run Service URL`, service account permissions, and gateway logs.  
  
##### Script result

The following table lists the value for the script result output when using the **Activate Audit Log** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Delete User Session

Use the **Delete User Session** action to terminate a user's active sessions in SAP through the Cloud Run SAP RFC Gateway.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Delete User Session** action requires the following parameters:

Parameter | Description  
---|---  
`SAP Username` | Required. The SAP username whose active sessions you want to terminate.  
`SAP Client Number` | Required. The three-digit numeric SAP client number.  
`SAP Instance Name` | Required. The name of the target SAP instance configured in the Cloud Run SAP RFC Gateway.  
  
#### Action outputs

The **Delete User Session** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Delete User Session** action:
    
    
    {
      "status": "SUCCESS",
      "functionId": "DELETE_USER_SESSION",
      "sap_instance": "PRD",
      "client": "100",
      "return": [
        {
          "type": "S",
          "message": "User session terminated."
        }
      ]
    }
    

##### Output messages

The **Delete User Session** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully deleted user session for SAP_USERNAME.` | The action succeeded.  
`Error executing action - "Delete User Session". Reason: Failed to delete user session for SAP_USERNAME. SAP Error: ERROR_SUMMARY` | The action failed because the SAP system returned an error. Verify that the username exists in the specified SAP client and that the gateway communication user has permission to run `TH_DELETE_USER`.  
`Error executing action - "Delete User Session". Reason: SAP Client Number must be a 3-digit numeric string (got 'SAP_CLIENT_NUMBER').` | The action failed parameter validation. Provide a valid three-digit numeric string for `SAP Client Number`, such as `100`.  
`Error executing action - "Delete User Session". Reason: Proxy request failed (HTTP STATUS_CODE): ERROR_DETAIL` | The request to the Cloud Run SAP RFC Gateway failed. Verify the `Cloud Run Service URL`, service account permissions, and gateway logs.  
  
##### Script result

The following table lists the value for the script result output when using the **Delete User Session** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Lock SAP User

Use the **Lock SAP User** action to lock a specified user account in SAP through the Cloud Run SAP RFC Gateway.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Lock SAP User** action requires the following parameters:

Parameter | Description  
---|---  
`SAP Username` | Required. The SAP username of the account to lock.  
`SAP Client Number` | Required. The three-digit numeric SAP client number.  
`SAP Instance Name` | Required. The name of the target SAP instance configured in the Cloud Run SAP RFC Gateway.  
  
#### Action outputs

The **Lock SAP User** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Lock SAP User** action:
    
    
    {
      "status": "SUCCESS",
      "functionId": "USER_LOCK",
      "sap_instance": "PRD",
      "client": "100",
      "return": [
        {
          "type": "S",
          "message": "User locked successfully."
        }
      ]
    }
    

##### Output messages

The **Lock SAP User** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully locked user SAP_USERNAME.` | The action succeeded.  
`Error executing action - "Lock SAP User". Reason: Failed to lock user SAP_USERNAME. SAP Error: ERROR_SUMMARY` | The action failed because the SAP system returned an error. Verify that the username exists in the specified SAP client and that the gateway communication user has permission to lock user accounts.  
`Error executing action - "Lock SAP User". Reason: SAP Client Number must be a 3-digit numeric string (got 'SAP_CLIENT_NUMBER').` | The action failed parameter validation. Provide a valid three-digit numeric string for `SAP Client Number`, such as `100`.  
`Error executing action - "Lock SAP User". Reason: Proxy request failed (HTTP STATUS_CODE): ERROR_DETAIL` | The request to the Cloud Run SAP RFC Gateway failed. Verify the `Cloud Run Service URL`, service account permissions, and gateway logs.  
  
##### Script result

The following table lists the value for the script result output when using the **Lock SAP User** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Ping

Use the **Ping** action to test authentication and network connectivity to the SAP ERP Cloud Run gateway service.

This action doesn't run on Google SecOps entities. 

#### Action inputs

None.

#### Action outputs

The **Ping** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Ping** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the SAP ERP server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the SAP ERP server! Error is Failed to generate Google Cloud authentication token. Verify service account credentials and permissions.` | The action failed to generate a Google Cloud authentication token. Verify your `Service Account JSON` or `Workload Identity Email` configuration.  
`Failed to connect to the SAP ERP server! Error is Authentication to Cloud Run failed (HTTP STATUS_CODE). Verify the caller has roles/run.invoker on the service.` | The Cloud Run gateway rejected the authentication request. Make sure that the service account has the **Cloud Run Invoker** (`roles/run.invoker`) role on the Cloud Run service.  
`Failed to connect to the SAP ERP server! Error is Cloud Run service returned unexpected HTTP STATUS_CODE: ERROR_DETAIL` | The Cloud Run gateway returned an unexpected HTTP status code. Verify the `Cloud Run Service URL` and inspect the Cloud Run service logs.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
